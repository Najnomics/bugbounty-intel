# When verified

- **Source URL:** https://medium.com/@sanjivanidobhal05/when-verified-false-still-got-a-valid-jwt-b91770294dc6
- **Fetched from:** https://medium.com/@sanjivanidobhal05/when-verified-false-still-got-a-valid-jwt-b91770294dc6?source=rss-10cd7e4b4fb2------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:**  (id 14897)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** Sanjivani Dobhal / Fri, 04 Sep 2026 06:04:18 GMT

Testing Whether Email Verification Was Actually Enforced

While testing a web application, I wanted to understand how the backend handled **email verification**.

So I asked a simple question:

***“What happens if I log in without verifying my email?”***

That simple question led me to an interesting authentication issue.

I created a new test account and **did not verify the email address**.

The account was still marked as:

```
{
  "verified": false
}
```
I then logged in normally.

Surprisingly, the application returned a **valid JWT** even though the account was still unverified.

But getting a token wasn’t enough. I wanted to know whether the backend would actually accept it on a protected API.

So I used the JWT in the Authorization header and sent a request to a protected company endpoint using **Burp Suite Repeater**.

The server responded with:

HTTP/2 200 OK

and returned data belonging to my own test account’s company.

Create Account

↓

Email NOT Verified

↓

Login Successfully

↓

Valid JWT Issued

↓

Protected API Request

↓

HTTP 200 OK ❗

The interesting part wasn’t simply that an unverified account could log in.

The important question was whether the backend **actually enforced the verification status** when the JWT was used.

The application knew the account was:

verified: false

but the tested protected API still accepted the authentication token.

This taught me an important lesson:

***Don’t assume a security control is enforced just because the application shows it in the UI. Test what the backend actually allows.***

I used **Burp Suite** to:

All testing was performed using my own test account.

After reproducing the behavior, I reported it to the security team with reproduction steps, Burp Suite evidence, request/response details, impact analysis, and remediation suggestions.

The security team informed me that the issue was **already known and being tracked**, so my report was classified as a **duplicate**.

Although it wasn’t a unique finding, the process was still a valuable learning experience.

Getting a JWT doesn’t automatically mean a user should have access to every protected resource.

Always ask:

***“What can this token actually access?”***

A restriction shown by the frontend doesn’t necessarily mean the backend enforces it.

If an account is verified: false, don't simply assume the application handles that state correctly.

Test what actually happens.

This was my **second real-world security research report**.

It was another duplicate, but it helped me improve my understanding of authentication, JWTs, API testing, Burp Suite, and responsible disclosure.

Sometimes security research starts with a very simple question:

***“The application says I’m unverified — but does the backend actually care?”***

That’s the kind of question I want to keep asking as I continue learning **Web Application Security and VAPT**.

**Keep testing. Keep learning. Keep improving. 🔐**
