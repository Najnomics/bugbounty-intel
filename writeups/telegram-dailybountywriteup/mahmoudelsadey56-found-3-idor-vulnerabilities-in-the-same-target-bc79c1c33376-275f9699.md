# Found 3 IDOR Vulnerabilities in the Same Target!

- **Source URL:** https://medium.com/@mahmoudelsadey56/found-3-idor-vulnerabilities-in-the-same-target-bc79c1c33376?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250413142048/https://medium.com/@mahmoudelsadey56/found-3-idor-vulnerabilities-in-the-same-target-bc79c1c33376
- **Fetched:** 2026-11-21
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/9347 (id 9347)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Found 3 IDOR Vulnerabilities in the Same Target!😱🔥

# **Let me tell you the full story…**

# 🧠 The Introduction:

I was casually doing a pentest on [Target.com](https://us.jora.com) when I stumbled upon something *really* interesting…

The site had **three separate IDOR (Insecure Direct Object Reference)** vulnerabilities — all inside the **Email Alerts** feature. 😲

To put it simply:

Anyone could **delete**, **pause**, or even **edit** another user’s email alert — *without having any authorization!* 🤯

All I had to do was play around with the requests a bit using Burp Suite — and boom! 💥 Let me walk you through it step-by-step.

# 1️⃣ IDOR in Deleting Email Alerts

# 🔍 The Issue:

When you try to delete an email alert, the app sends a request like this:

`GET /account/email_alerts/[unique_id]/cancel`
The **problem?**

The server doesn’t verify if the alert actually belongs to you! 🤦♂️

# 💥 How I Exploited It:

1. I created two accounts: `Account A` and `Account B`.
2. Each account created its own email alert.
3. I intercepted the delete request from **Account A** using Burp Suite.
4. I changed the `unique_id` to the one from **Account B**.
5. I sent the request…

✅ Result? The alert from **Account B got deleted** — just like that!

# Impact:

Anyone could delete another user’s alerts without their permission.

Imagine a job seeker waiting for new opportunities, and suddenly their alerts disappear — **just because someone decided to mess with them.**

That’s a big deal.

# 2️⃣ IDOR in Pausing/Resuming Alerts

# 🔍 The Issue:

When a user pauses or resumes an alert, the site sends a request like:

`POST /account/email_alerts/[unique_id]/toggle`
Again… **no ownership check.** 😅

# 💥 How I Exploited It:

1. Same two accounts (A and B).
2. I intercepted the pause request from Account A.
3. Replaced the alert ID with one from Account B.
4. Sent the request.

✅ Boom. **Account B’s alert was paused** without any consent.

# Impact:

An attacker can silently pause or resume alerts for any user, affecting their ability to receive timely job offers. Not cool.

# 3️⃣ IDOR in Editing Alerts

# 🔍 The Issue:

When editing an alert, the site sends a request like:

`POST /account/email_alerts/[unique_id]`
You guessed it — **no validation** to confirm ownership.

# 💥 How I Exploited It:

1. I modified an alert from Account A and intercepted the request.
2. Changed the ID to that of an alert from Account B.
3. Edited the alert settings and sent the request.

✅ And just like that — **Account B’s alert was modified** without them even knowing.

# Impact:

This one is particularly dangerous. An attacker could:

- Change the alert keywords
- Mislead users with fake job listings
- Disable job categories
- Or silently mess up the alert settings to make it useless

This affects both **data integrity** and **user trust** in the platform.

# How to Fix It:

To patch these vulnerabilities, the app should:

- ✅ Link every action to the authenticated user session
- ✅ Validate if the user owns the object (email alert) before performing any operation
- ✅ Avoid using easily guessable `unique_id`s in the URL
- ✅ Consider using **authorization tokens** or secure server-side checks

# 😅 Unfortunately…

Unfortunately, after submitting the report, I found out that the vulnerabilities were **duplicates**.

But hey, I’m not disappointed — **not at all**! ✨

This experience taught me a lot, and showed me how small details can uncover big issues.

It’s just the beginning…

**The best is yet to come, and this is only the start of the journey! 💪🔥**
