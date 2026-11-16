# Intigriti HackDonalds Challenge Writeup — LFI via XXE

- **Source URL:** https://medium.com/@vishnu.raveendran1461/intigriti-hackdonalds-challenge-writeup-lfi-via-xxe-68a136663bb0?source=rss------bug_bounty-5
- **Fetched from:** https://medium.com/feed/@vishnu.raveendran1461
- **Fetched:** 2026-11-16
- **Channel:** @dailybountywriteup
- **Telegram message:**  (id 10081)
- **Method:** medium-rss-content readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
### Intigriti HackDonalds Challenge Writeup — LFI via XXE

### 🍔 Welcome to HackDonalds

A sweet little ride through an XXE vulnerability, with some login bypass seasoning and Next.js middleware confusion. Here’s the journey:

### Step 1: Visit the Challenge Server

I started by navigating to the challenge site:

**https://hackdonalds.intigriti.io**

Greeted with a stylish red theme and a login prompt — but I didn’t come here to just log in politely 😉

### I started with some light recon. Using tools like:

- **Webanalyze**

- **Wappalyzer**

I found that the site was running **Next.js 13.2.0**, which has a known middleware vulnerability that can lead to access control bypass if specific headers are tampered with.

Reference: [https://projectdiscovery.io/blog/nextjs-middleware-authorization-bypass](https://projectdiscovery.io/blog/nextjs-middleware-authorization-bypass)

### Step 3: Admin Panel Discovery & Login Bypass

While hovering over the logout button, I noticed a link pointing to /admin. Curious, I tried manually visiting [https://hackdonalds.intigriti.io/admin.](https://hackdonalds.intigriti.io/admin.)

At first, it seemed protected — but I remembered the middleware vulnerability from recon.

So I fired up **Burp Suite** , and using the **Match and Replace** feature, I added the header:

x-middleware-subrequest: middleware

This bypassed the middleware check and let me access the admin dashboard without logging in.

### Step 4: XML Settings in Ice Cream Machine

Clicked on the **Ice Cream Machines** section and found an XML parser form allowing user input. From here started enumerating internal server, after understanding the default directories of next js, found the flag using proc and cwd

### Summary:

Thanks for reading! This challenge was a great learning opportunity — from recon and bypass techniques to exploiting XXE for LFI.

I’ll be back with more writeups soon. Until then, go pwn the next ice cream machine 🍦😄
