# Easiest $225 Ever

- **Source URL:** https://medium.com/@whoadnan01/easiest-225-ever-a-simple-sql-injection-win-f40c0a6b8e45?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250131004200/https://medium.com/@whoadnan01/easiest-225-ever-a-simple-sql-injection-win-f40c0a6b8e45
- **Fetched:** 2026-11-19
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/8628 (id 8628)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
Hi everyone, I’m **Adnan Kaisar**, a cybersecurity enthusiast pursuing **B.Tech in CSE** from **Dehradun**. My journey into **hacking and bug bounty** started in my **first year of college**, and ever since, I’ve been hooked on the thrill of finding vulnerabilities.

# The Hunt Begins

One day, while exploring **responsible disclosure programs**, I came across a **bug bounty program** that caught my attention. The scope looked promising, so without wasting any time, I fired up my **Kali Linux machine** and got to work, Since I can’t disclose the program’s name, I’ll refer to the target as **example.com** for this write-up.

I started with **subdomain enumeration** using `subfinder`:

`subfinder -d example.com -o example.txt`
Once I had a list of subdomains stored in `example.txt`, I filtered out the **live** ones using `httpx`:

`cat example.txt | httpx -status-code -mc 200,301 -silent`
This left me with around **50–60 live subdomains**. From there, I randomly picked about **20–30 subdomains** and opened them all at once using a Chrome extension called **“Open Multiple URLs.”**

# The Discovery: A Classic SQL Injection

While going through the subdomains, a few immediately stood out. One of them had a **“page=” parameter** in the URL, which instantly caught my attention.

Out of instinct, I tested it for **SQL Injection** by injecting a simple **tilde (\`)** character.

The server responded with an **error message**, leaking internal paths, **error-based SQL Injection**.

# Reporting the Vulnerability

Without overthinking, I immediately wrote a **detailed report** and submitted it. What I should have done was escalate the bug but instead, I reported it as it was, missing a bigger opportunity 😞 Just when I thought I was done, I decided to check a few more subdomains and guess what? **Two more had the exact same issue.**

So, I included all three vulnerable URLs in my report and sent it over to the **security team.**

A day later, I received a response:

*“Thank you for reporting! We were able to reproduce the vulnerability and will be rewarding you with $50.”*


**Wait, what? $50 for an SQL Injection?** 😑

I politely asked them to **increase the bounty** to at least **$200 per subdomain**, but they only agreed to **$75 per subdomain.** Well, something is better than nothing, right?

Within **2–3 days**, the bounty was credited to my **PayPal account.**

# Final Thoughts

This experience taught me a lot — not just about hacking, but also about how **bounty rewards can be unpredictable.** Some companies pay generously, while others, well… you get the idea.

🚀 **Keep learning, keep hunting!**

If you found this write-up interesting, **give it a clap** and feel free to reach out with any questions.

You can connect with me on **X (formerly Twitter) and LinkedIn**
