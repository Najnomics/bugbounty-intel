# How IDOR and Business Logic Flaw Exposed PII

- **Source URL:** https://scriptjacker.medium.com/how-idor-and-business-logic-flaw-exposed-pii-24545a078e04?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20261018133603/https://scriptjacker.medium.com/how-idor-and-business-logic-flaw-exposed-pii-24545a078e04
- **Fetched:** 2026-11-27
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/11673 (id 11673)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# **How IDOR and Business Logic Flaw Exposed PII**

Hey Hackers, I am Parth Narula. A penetration tester, bug hunter, red teamer and overall a security researcher. I live for those moments where a bit of out-of-the-box thinking cracks open a critical vulnerability.

I’m excited to share the story of how I found a severe PII (Personally Identifiable Information) disclosure flaw. The vulnerability was an Insecure Direct Object Reference (IDOR) hidden within a login page’s OTP verification process. This finding wasn’t about complex tools; it was all about playing with the application’s logic.

My engagement began with testing a web application for a client in the creative industry. Like any good tester, I started at the beginning: the registration page.

- **Entry Point:** `https://app.redacted/new-account/`
- **Registration Fields:** Email, password, country, and a nickname.
- **The Flow:** I filled in my details, hit “Register,” and was redirected to a next page.

Post-registration, I landed on an OTP verification screen:

`https://app.redacted/compte-confirmation/976`

A 2FA code (in my case, **19353**) arrived in my inbox.

Standard procedure, right? But my eyes were glued to the URL. That number **976** was clearly my User ID (UID). A simple, sequential identifier.

This got my hacker senses tingling. If I’m user **976**, then users before me must be **1 through 975**. And who’s often user #1? An administrator.

This is where logic bypassed the obvious security check. I asked myself two simple questions:

## Get Parth Narula’s stories in your inbox

Join Medium for free to get updates from this writer.

**What if I change the UID in the URL to someone else’s, say, user 970?** New URL: [https://app.redacted/compte-confirmation/970](https://app.redacted/compte-confirmation/970)

**Now, how do I get past the OTP? The server is asking for a code for user 970, but I don’t have access to their email… or do I?**

- What if the application’s logic was flawed? What if it was only checking *if an OTP was correct*, but not *which user that OTP belonged to*?

I decided to test this theory. On the page for user **970**, I entered **my own OTP (19353)** and clicked “Validate the code”.

It worked.

Instead of an error, I was redirected to the standard login page at `https://app.redacted/connection`. And there, in the "email" field, pre-populated for the world to see, was the victim's email address: the private email account belonging to user **970**.

The vulnerability was confirmed. The application was making a critical mistake:

The server checked if the OTP was valid anywhere in the system, not if it belonged to the user in the URL/Request. Once I entered a correct code, it showed me that user’s email.


I repeated this process for multiple UIDs, including low-numbered ones. Successfully, I extracted the email addresses of several users and, critically, the internal admin accounts.

I responsibly reported the vulnerability to the client and it got fixed and disclosed the bug with permission.

## Lessons Learned

1. **IDOR Isn’t Just in API Endpoints:** We often look for IDOR in `/api/v1/user/123` endpoints, but it can lurk anywhere an object is referenced—including multi-step authentication flows.
2. **Never Trust the Client… Even for Reference:** The UID was a direct, predictable object reference that the client could manipulate. Authorization must be checked on the server for every single request that accesses data.
3. **Test the “Happy Path” for Abuse:** The flow worked perfectly for its intended use. The flaw was only exposed when I used the *correct* OTP in the *wrong* user’s context. Always ask, “What if a valid piece of data is used in an invalid context?”

I hope you learn something new. Follow for more amazing articles and give claps if you like this one :)

Need expert pentesting services? 

Visit [https://scriptjacker.in](https://scriptjacker.in) or let’s collaborate on your next project! 🤝

Want to learn from my experiences? Check out my articles on [https://](https://lnkd.in/guKvpNYz)blogs.scriptjacker.in
