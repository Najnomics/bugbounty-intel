# $900 IDOR

- **Source URL:** https://medium.com/@a13h1/900-idor-unauthorized-access-to-form-attachments-via-direct-api-2eb6fed81030?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20260603013532/https://medium.com/@a13h1/900-idor-unauthorized-access-to-form-attachments-via-direct-api-2eb6fed81030
- **Fetched:** 2026-11-19
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/13657 (id 13657)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# $900 IDOR: Unauthorized Access to Form Attachments via Direct API

Hi Everyone! While testing a SaaS platform (**ExampleCenter**), I discovered an **authorization bypass vulnerability** that allowed a low-privileged user to download file attachments from forms they had no access to.

For this finding, I was awarded a **$800 bounty + $100 retest bonus**. At first, this looked like a simple endpoint issue but once I explored it deeper, it turned into a classic **IDOR with enumeration potential**. Let’s break it down.

## Understanding the Target

ExampleCenter provides a **People/Form system** where organizations collect data through forms.

These forms often contain:

- Personal documents
- IDs
- Consent forms
- Sensitive user information

Access control is supposed to ensure that:

- Only authorized users can view form submissions
- Attachments are restricted to users with proper permissions

I tested using a **Viewer-level account**, which:

- ❌ Cannot access target forms
- ❌ Cannot view submissions
- ❌ Cannot download attachments via UI

So from the UI perspective — everything looked secure.

## The Thought That Triggered the Bug

While inspecting network traffic, I noticed that file downloads were happening via a direct endpoint.

That made me think:

*“What if the backend only checks the attachment ID… and not the actual permissions?”*


So I decided to test it manually.

## The Flaw: Direct Access to Attachments

I crafted a request using a valid session of a **Viewer user**:

```
GET /form_submission_value/{attachment_id}/attachments?attachment_name={attachment_name} HTTP/2
Host: api.examplecenter.com
Cookie: session=<viewer_session>
```
## What I Expected vs What Happened

I expected to get 403 Forbidden or Access denied error but Actual i get **200 OK — File Downloaded Successfully**

Even though:

- I had no access to the form
- I couldn’t see the submission in UI

👉 I could still download the attachment

## The Missing Piece: Enumeration

The analyst asked an important question:

*“How do you get the attachment name?”*


And this is where the bug becomes more interesting 👇

## Enumeration Possibility

- attachment\_id → sequential
- attachment\_name → guessable / enumerable
- No rate limiting on endpoint

👉 This allows brute-force / enumeration attacks

An attacker can:

- Iterate IDs
- Try common file names
- Extract valid attachments

## Why This Matters

Even if enumeration requires effort, the impact is serious because:

👉 Once valid parameters are found → **full file access**

## Root Cause

This was a classic IDOR:

*Backend authorization relies only on object reference (attachment\_id and attachment\_name)*


Missing checks;

- Does user have access to form?
- Does user have access to submission?
- Is this attachment allowed for this user?

👉 No authorization validation

## Impact

This vulnerability leads to:

### Confidentiality Impact

- Access to sensitive documents and images
- Exposure of personal user data

### Data Exposure

- IDs
- Medical forms
- Private submissions

### Privacy Risk

- Violation of user trust
- Unauthorized data disclosure

## Bounty & Program Response

- **Reported:** Jan 6, 2026
- **Clarification:** Enumeration explained
- **Triaged:** Jan 13, 2026
- **Severity:** Medium (CVSS-based)
- **Bounty:** $800 + $100 bonus
- **Retest:** Fix confirmed

## Key Takeaways

- Always test **direct download endpoints**
- IDORs often hide behind: File downloads, Media access & Attachments
- Don’t stop at “need one parameter” — test enumeration
- Lack of rate limiting can turn low bugs into real exploits
- Even partial control over parameters = potential data exposure

## Personal Insight

This bug came from a very simple mindset:

*“If I can’t access it in UI… can I still fetch it directly?”*


That question alone leads to many real-world bugs.

## Conclusion

This vulnerability highlights how dangerous it is to rely only on **object identifiers without proper authorization checks**.

Even though the UI correctly restricted access, the backend allowed direct retrieval of sensitive files completely bypassing access controls.

These types of bugs are very common, especially in systems handling uploads and documents.

Always remember:

*If an endpoint returns a file… it MUST verify who is asking for it if not u got the bounty.*


Until next time — happy hacking! 🚀

## Connect and Engage

💬 Comment your best experience with IDOR bugs!

Follow me on Twitter: [@a13h1\_](https://x.com/a13h1_)

Keep clapping, commenting, and sharing your thoughts — your support motivates me to share more real bug bounty stories!
