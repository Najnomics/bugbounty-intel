# From SQL Injection to Remote Code Execution

- **Source URL:** https://medium.com/@gouravrathod8788/from-sql-injection-to-remote-code-execution-a-bug-bounty-hunters-unexpected-journey-bc91a3697f24?source=rss------bug_bounty-5
- **Fetched from:** https://medium.com/feed/@gouravrathod8788
- **Fetched:** 2026-11-27
- **Channel:** @dailybountywriteup
- **Telegram message:**  (id 8788)
- **Method:** medium-rss-content readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
Let’s get start 🫨

Introduction: A Routine Hunt Turns Wild

It all started as just another day in my bug bounty hunting routine. I had been scanning web applications for hours, looking for low-hanging fruit—basic misconfigurations, XSS, or maybe a juicy SQL injection. But little did I know, this hunt would lead me straight into Remote Code Execution (RCE)—one of the holy grails of exploitation! 🚀

The Target: A Login Page with a Secret

I had picked a private program that offered a decent bounty for critical vulnerabilities. The target? A simple login page—email and password fields, a login button, and a forgot password option. Nothing fancy.

But as any experienced hacker knows, "simplicity can be deceiving."

So, I fired up Burp Suite and started my passive reconnaissance.

Step 1: Testing for SQL Injection

I started with some classic payloads in the email field:

' OR 1=1 --

Boom! SQL error detected. 🚨

A quick UNION-based payload confirmed it:

' UNION SELECT 1,2,3,4 --

The application responded differently, meaning I had an exploitable SQL injection. Game on!

Step 2: Dumping Data – The Jackpot Moment

Using SQLMap, I retrieved the database names, and soon, I had a list of users. Then, something unexpected happened—

the database contained a table named "admin\_logs".

A quick peek inside revealed log entries of admin actions, including login credentials. Some passwords were stored in plaintext. 💀

I quickly tested an admin login—and it worked! ✅

Step 3: Admin Panel → File Upload

Inside the admin panel, I found a file upload feature meant for uploading profile images. Instantly, my hacker instincts kicked in.

I uploaded a PHP web shell disguised as an image:

\<?php system($\_GET\['cmd'\]); ?>

The response? "Invalid file type."

No worries—I intercepted the request with Burp and changed the Content-Type to image/jpeg.

💥 File uploaded successfully!

Step 4: Gaining RCE – The Moment of Truth

I navigated to the uploaded file:

http://target.com/uploads/shell.php?cmd=whoami

🔥 The server responded with "www-data" 🔥

I had Remote Code Execution. From a simple SQL injection, I had escalated to full system compromise!

Conclusion: The Bounty & The Lesson

I immediately reported the vulnerability, and within days, I received a high five-figure bounty. 🎉💰

This hunt reinforced a crucial lesson:

👉 A small vulnerability can snowball into a critical exploit. Never underestimate SQL injection—it can lead to full system compromise if you dig deep enough.

Bug bounty hunting is like treasure hunting—you never know what you'll find beneath the surface! 🏴☠️🔎

Would love to hear your thoughts! Have you ever taken a simple bug to a full RCE? Drop your stories in the comments! 🚀
