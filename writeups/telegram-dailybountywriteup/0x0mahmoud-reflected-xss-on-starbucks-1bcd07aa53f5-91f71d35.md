# Reflected XSS on Starbucks

- **Source URL:** https://medium.com/@0x0mahmoud/reflected-xss-on-starbucks-1bcd07aa53f5?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250822072753/https://medium.com/@0x0mahmoud/reflected-xss-on-starbucks-1bcd07aa53f5
- **Fetched:** 2026-11-21
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/10590 (id 10590)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Reflected XSS on Starbucks

**Hello everyone!**

“Welcome back. Today, our **writupe** is about a vulnerability I found: a **reflected cross-site scripting** (XSS) bug on the Starbucks online store.”

# The Scope

Before I started looking for a bug, my first step was to understand Starbucks’ business from a security perspective. I knew Starbucks wasn’t just a coffee company; it’s a massive technology brand that relies heavily on its online presence and customer trust.

With this in mind, I decided to focus my attention on their **online store**. I knew this is where they handle customer information, payments, and shipping details, making it a critical part of their business.

So, I began searching for all of Starbucks’ online stores using a variety of methods. For this **writupe**, I’ll focus on the specific technique I used to find the exact domain where the vulnerability was located.

The method I used to find the host was **dorking**. This is a technique where you use advanced search queries to find very specific information on a website.

I used a simple but powerful query: `site:onlinestore.starbucks.com.*`. My goal was to find a domain that was still in active use.

That’s when I found **onlinestore.starbucks.com.hk** — the Hong Kong online store. I focused my attention on this specific host, and it wasn’t long before I found what I was looking for.

# **The Hunting Ground:**

I wanted to find every corner of the website to search for weaknesses. I used a tool called [**Gau**](https://github.com/lc/gau), which stands for “Get All URLs.” This tool scours public sources to find every old and forgotten link associated with the website. It’s like a digital archaeologist, helping me dig up old pathways on the site that nobody might be using anymore.

Next, I used another tool called [**uro**](https://github.com/s0md3v/uro). As you know, a list of URLs from a tool like Gau can be full of duplicates or uninteresting pages. **uro** aims to solve that problem. It analyzes the list of URLs without sending any HTTP requests and removes all the irrelevant links, leaving me with a clean, unique list of pages to test. This saved me a huge amount of time.

Thanks to these tools, a massive list of potential links was transformed into a small, focused list. I then began testing each URL on the list, one by one.

# The Missing Safety Feature:

I began my search using a **Burp Suite**. While examining the website’s responses, I immediately noticed a crucial detail: a lack of security headers.

These headers are like the built-in safety features on a website, designed to protect users from common attacks. Not only was the site missing the **X-XSS-Protection** header, a basic defense against XSS, but it was also missing the **Content-Security-Policy (CSP)** header.

Finding both of these major defenses missing was a huge red flag and a strong reason to continue looking for a XSS.

# The Proof of Concept:

So, I began searching for a **reflected parameter**. This is an input on the website that “reflects” back to the page what you type into it, like an echo.

After testing several inputs, I found a parameter named `namespaces`. This was my target. The first thing I did was test for proper **parameter sanitization**. Think of sanitization as a security filter; a well-built website should automatically remove or neutralize any dangerous characters you try to input.

I used a simple payload to test this. I inserted the following code into the `namespaces` parameter: `%3Cscript%3Econfirm(1)%3C/script%3E`. This is the URL-encoded version of `<script>confirm(1)</script>`. All this code does is make a small pop-up box appear on the screen with the number '1' inside it.

The website was not properly filtering my input. The code was executed, and the pop-up box appeared, confirming that the site was vulnerable to reflected cross-site scripting.

The Resolution and The Bounty 💰

After a long wait, the time had finally come. On **January 14, 2025**, I received a message from the Starbucks security team. They confirmed they had fixed the vulnerability and asked me to perform a **retest**. This meant I needed to go back to the site and confirm that my exploit no longer worked.

This was the moment of truth. I retested the `namespaces` parameter, and to my satisfaction, the payload didn't work. The fix was in place. The vulnerability was gone. I sent them my confirmation.

And then, the moment I had been waiting for. For my discovery, Starbucks awarded me a **$$$bounty**. They also gave me an additional $50for completing the retest.

*Thank you.*
