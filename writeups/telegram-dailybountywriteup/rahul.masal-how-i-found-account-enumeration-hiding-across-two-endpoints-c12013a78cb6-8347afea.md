# How I Found Account Enumeration Hiding Across Two Endpoints

- **Source URL:** https://medium.com/@Rahul.Masal/how-i-found-account-enumeration-hiding-across-two-endpoints-c12013a78cb6
- **Fetched from:** https://medium.com/@Rahul.Masal/how-i-found-account-enumeration-hiding-across-two-endpoints-c12013a78cb6?source=rss-942d4053a36b------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14936 (id 14936)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** Rahul Masal / Mon, 05 Oct 2026 20:11:16 GMT

A beginner-friendly security writeup | CWE-204 | Medium Severity

**What is Account Enumeration?**

Before we get into the findings, let me explain what “account enumeration” actually means.

Imagine you go to a website’s login page and type in a wrong email. If the website says ”Email not found” — that’s a problem. Why? Because now you know for certain that nobody with that email has an account there. Try a hundred emails, and you’ll build a list of real users.

The secure way to handle this is to always say something vague like ”Incorrect email or password” — never hinting which one was wrong.

Account enumeration is when a website accidentally reveals whether an email address is registered. This writeup covers two places I found this on the same platform.

**The Target**

Platform name redacted — reported responsibly and pending triage

This is a social platform where creators share content and interact with their communities. Account registration is free and open to anyone.

Report Date: May 31, 2026

Severity: Medium (both findings)

Vulnerability Type: Account Enumeration — CWE-204

**What’s the issue?**

When a logged-in user tries to change their email address in Account Settings, the server checks if the new email is already taken by someone else. So far, so normal.

The problem? The server tells you **exactly** what happened in the response — using two very different codes:

\- \`EMAIL\_ALREADY\_REGISTERED\` → Someone already has that email

- \`code: “OK”\` → No account with that email

This makes the email change form into a tool for checking whether **any** email address is registered on the platform. Just send a request with any email you want to check and read the response.

**What you need to reproduce this**

**Steps**

1\. Log in and go to Account Settings → Email.

2. Turn on Burp Suite’s proxy intercept.

3. Submit any email in the change field — capture the request.

4. Send the request to Burp’s Repeater tab.

5. Replace the email value with any email you want to check.

6. Send it. Watch the response.

If the email is registered:

**code: “EMAIL\_ALREADY\_REGISTERED”**

If the email is NOT registered:

**status: 1, code: “OK”**

That’s your oracle — a clear, machine-readable signal that tells you exactly whether an account exists.

The forgot-password flow has the same problem — but worse. No account is needed at all.

When you submit an email on the password reset page:

\- If the email is registered → server responds with \`code: “OK”\`

- If the email is not registered → server responds with \`USER\_NOT\_FOUND\`

Anyone on the internet can check whether any email address belongs to a platform account — without logging in, without owning a profile.

1\. Open the Forgot Password page.

2. Turn on Burp Suite proxy intercept.

3. Submit an email and complete the CAPTCHA challenge.

4. Capture the request in Burp, send to Repeater.

5. Swap the email value, solve the CAPTCHA again, and send.

6. Read the response — it clearly states whether the account exists or not.

If the email is registered:

**code: “OK”**

If the email is NOT registered:

**code: “USER\_NOT\_FOUND”**

**What about the CAPTCHA?**

The platform uses Cloudflare Turnstile — a modern CAPTCHA. This is actually a good control, and it does slow things down. Each token is single-use and expires within seconds.

**But here’s the reality:**

\- Manual checking (one email at a time) is completely unaffected. The PoC above proves this.

- Commercial CAPTCHA solving services like 2captcha or CapSolver handle Turnstile for roughly $1–2 per 1,000 solves. That means automated, large-scale enumeration is still economically viable for someone motivated.

Turnstile is a good speed bump. It is not a fix.

**Why Does This Actually Matter?**

You might be thinking: ”So what if someone knows my email is on the platform? That’s not a big deal.”

Here’s why it is:

**How Can This Be Fixed?**

**Fix for the Email Change Endpoint**

Stop telling the API caller whether the email is taken. Instead:

**Fix for the Forgot Password Endpoint**

Use the industry-standard generic response:

“If an account with this email exists, you’ll receive a reset link shortly.”

Return this exact same message whether or not the email is registered. Never reveal which one is true. This single change eliminates the oracle entirely.

On top of that: add per-IP and per-email rate limiting (3–5 attempts per hour is standard), and monitor for high-volume submission patterns.

**Thanks for reading! If you found this helpful, feel free to clap and follow for more bug bounty writeups. Happy hunting! 🐛**
