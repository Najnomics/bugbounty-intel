# Bypassing AI Quotas

- **Source URL:** https://medium.com/@ziadabdo1255/bypassing-ai-quotas-how-a-null-value-led-to-infinite-ai-generation-on-rebelmouse-ebc56c386328
- **Fetched from:** https://medium.com/@ziadabdo1255/bypassing-ai-quotas-how-a-null-value-led-to-infinite-ai-generation-on-rebelmouse-ebc56c386328?source=rss-09e7e8318a71------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14923 (id 14923)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** Ziad  Abdo / Thu, 24 Sep 2026 17:02:37 GMT

In the era of AI-driven SaaS platforms, API tokens are money. Every time a user generates a prompt, the platform pays a downstream provider like OpenAI or Anthropic. To protect their resources, companies implement strict billing and quota systems. But what happens when that billing system trusts the user a little too much?

During a recent security assessment of RebelMouse, I discovered a critical Business Logic flaw in their AI generation feature. By simply manipulating a single parameter in the JSON payload, I was able to completely bypass their paywall, leading to infinite AI prompt generation at the company’s expense.

Here is the technical breakdown of how a simple "Fail-Open" architecture allowed this bypass.

🔍 The Core Concept: Fail-Open vs. Fail-Closed

When designing authorization or billing checks, systems should ideally be Fail-Closed. This means if an unexpected input occurs (like a missing ID, a database error, or a malformed request), the system should block the action by default.

However, in this case, the RebelMouse backend implemented a Fail-Open logic for its quota tracking. It relied on a client-supplied orgId to deduct credits. If the system couldn’t parse the orgId, instead of dropping the request, it simply skipped the billing deduction and processed the AI prompt anyway.

🛠️ Proof of Concept (PoC)

1. Hitting the Paywall

To understand the limitation, I first used the AI generation feature until my account exhausted its daily credits. At this point, attempting to generate a new prompt resulted in the expected 402 Payment Required block:

Server Response:

HTTP/2 402 Payment Required

Content-Type: application/json

{

"error": "Daily credit limit reached",

"dailyRemaining": -208

}

2\. Intercepting the Request

I fired up Burp Suite and captured the POST request responsible for the AI generation. The vulnerable endpoint was:

/dashboard/api/properties/\[PROPERTY\_ID\]/pages/codex/runs

The original request body looked like this:

{

"prompt": "hi",

"siteId": "pages-\[ID\].rebelmouse.ai",

"projectName": "\[PROJECT\_NAME\]",

"conversationId": "\[CONVERSATION\_ID\]",

"orgId": "12345-VALID-ORG-ID",

"personalityId": "\[PERSONALITY\_ID\]"

}

3\. The Bypass (Null/Empty String Injection)

Since the 402 error indicates that the backend is checking the quota based on my organization, I decided to tamper with the orgId parameter.

I sent the request to Burp Repeater and modified the orgId value to an empty string ("").

Malicious Request:

POST /dashboard/api/properties/\[PROPERTY\_ID\]/pages/codex/runs HTTP/2 

Host: rebelmouse.ai 

Content-Type: application/json

{

"prompt": "hi",

"siteId": "pages-\[ID\].rebelmouse.ai",

"projectName": "\[PROJECT\_NAME\]",

"conversationId": "\[CONVERSATION\_ID\]",

"orgId": "",

"personalityId": "\[PERSONALITY\_ID\]"

}

4\. The Result

By sending the empty string, the backend’s billing middleware failed to map the request to a valid entity. Instead of safely failing, it forwarded the payload directly to the AI service. The server accepted the request and successfully processed the prompt!

Server Response:

HTTP/2 200 OK

Content-Type: application/json

{

"runId": "5519",

"conversationId": "\[CONVERSATION\_ID\]"

}

At this point, an attacker could load this request into Burp Intruder or write a simple Python script to generate an infinite number of AI responses without spending any valid credits.

💥 Business & Security Impact

Vulnerabilities like this are highly critical for SaaS platforms, as they translate directly into Financial Loss.

Resource Exhaustion: An attacker can script thousands of API calls, consuming backend AI tokens entirely at the company’s expense.

Paywall Evasion: Complete circumvention of the platform’s monetization model, allowing malicious actors to use premium services for free.

🛡️ Remediation & Takeaways for Developers

This vulnerability is a classic example of CWE-602: Client-Side Enforcement of Server-Side Security.

To prevent this, developers should ensure:

Never Trust Client Data for Billing: Parameters like orgId should never be accepted from the client request body for authorization or billing.

Backend Extraction: The backend must extract the organization ID securely from the authenticated user’s JWT or Session Token.

Strict Fail-Closed Logic: If the billing engine encounters an invalid, missing, or empty ID, the API must immediately halt execution and return a 400 Bad Request or 403 Forbidden.

📅 Vulnerability Timeline

May 2026: Vulnerability discovered and reported to RebelMouse via Bugcrowd.

Late May 2026: Triaged and moved to "Waiting for customer".

\[Date\]: Fixed by the RebelMouse team.

\[Date\]: Bounty Awarded.

(If you found this writeup helpful, feel free to leave a clap or follow for more bug bounty tips and logic flaws!)
