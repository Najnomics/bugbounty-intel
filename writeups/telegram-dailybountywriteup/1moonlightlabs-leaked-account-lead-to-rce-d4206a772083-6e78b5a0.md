# Leaked account lead to RCE

- **Source URL:** https://medium.com/@1moonlightlabs/leaked-account-lead-to-rce-d4206a772083
- **Fetched from:** https://medium.com/@1moonlightlabs/leaked-account-lead-to-rce-d4206a772083?source=rss-3d0685b44041------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:**  (id 14915)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** MoonLightLabs / Wed, 16 Sep 2026 16:59:11 GMT

Hello guys welcome to my new writeup, today i will explain how did i got from leaked accounts lead to RCE.

First of all, i tried to look at waybackurls if there was something that could be intersting but didn’t found anything also i tried with subfinder still nothing.

so i started to look at the source and the website himself and i found something intersting.

A JavaScript file exposed a function that could retrieve account information by ID. I started testing the function to see whether it was actually working and discovered that it did not have any rate limiting.

After testing different IDs, I eventually found a valid account and received credentials in the response.

I tried logging in with the credentials, and it worked.

I did not report the vulnerability immediately because I wanted to understand whether it could lead to something more serious.

While testing the application, I noticed that I could upload files, so I started testing different file types and checking common upload restrictions. Files such as PHP, JavaScript, and SVG were rejected, but the server accepted .shtml files.

After researching this behavior, I found that the server supported Server-Side Includes (SSI), which allowed me to execute server-side commands

For testing purposes, I was able to control the command input through an HTTP header.

I continued testing and confirmed that this could lead to Remote Code Execution. Some requests were blocked by the server’s firewall, so I continued testing different encoding techniques until I was able to bypass the firewall and obtain a reverse shell.

The final attack chain was:

**Leaked credentials -> Account takeover -> file upload -> Server-Side Includes -> Remote Code Execution**

**Note:** The vulnerabilities were responsibly reported, patched, and rewarded. I cannot disclose the company or any identifying details. This was my first bug bounty report.
