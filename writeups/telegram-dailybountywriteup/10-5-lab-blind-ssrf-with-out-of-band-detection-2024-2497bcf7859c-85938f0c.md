# 10.5 Lab

- **Source URL:** https://cyberw1ng.medium.com/10-5-lab-blind-ssrf-with-out-of-band-detection-2024-2497bcf7859c?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20240302074804/https://cyberw1ng.medium.com/10-5-lab-blind-ssrf-with-out-of-band-detection-2024-2497bcf7859c
- **Fetched:** 2026-11-27
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/5393 (id 5393)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# 10.5 Lab: Blind SSRF with out-of-band detection | 2024

## This site uses analytics software which fetches the URL specified in the Referer header when a product page is loaded. To solve the lab, use this functionality to cause an HTTP request to the public Burp Collaborator server | Karthikeyan Nagaraj

1 min read4 days ago

# Description

This site uses analytics software which fetches the URL specified in the Referer header when a product page is loaded.

To solve the lab, use this functionality to cause an HTTP request to the public Burp Collaborator server.

# Solution

1. Click a product, capture the request, and Send it to Repeater.
2. Remove the Referer Value and type http://
3. Right-click, click Insert Collaborator Link and send the request.
4. Go to the Collaborator tab and Click Poll Now to solve the Lab

A YouTube Channel for Cybersecurity Lab’s Poc and Write-ups

Telegram Channel for Free Ethical Hacking Dumps

Thank you for Reading!

Happy Ethical Hacking \~

`Author: Karthikeyan Nagaraj ~ Cyberw1ng`
