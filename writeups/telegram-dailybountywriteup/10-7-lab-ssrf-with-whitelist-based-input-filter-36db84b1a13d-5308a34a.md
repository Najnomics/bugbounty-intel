# 10.7 Lab

- **Source URL:** https://cyberw1ng.medium.com/10-7-lab-ssrf-with-whitelist-based-input-filter-36db84b1a13d?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20240814094335/https://cyberw1ng.medium.com/10-7-lab-ssrf-with-whitelist-based-input-filter-36db84b1a13d
- **Fetched:** 2026-11-27
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/6681 (id 6681)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# 10.7 Lab: SSRF with whitelist-based input filter

## This lab has a stock check feature that fetches data from an internal system. To solve the lab, change the stock check URL to access the admin interface at [http://localhost/admin](http://localhost/admin) and delete the user carlos. The developer has deployed an anti-SSRF defense you will need to bypass | Kartthikeyan Nagaraj

2 min readJul 13, 2024

# Description

This lab has a stock check feature that fetches data from an internal system.

To solve the lab, change the stock check URL to access the admin interface at [http://localhost/admin](http://localhost/admin) and delete the user carlos.

The developer has deployed an anti-SSRF defense you will need to bypass

# Solution

1. Visit a product, click “Check stock”, intercept the request in Burp Suite, and send it to Burp Repeater.
2. Change the URL in the `stockApi` parameter to `http://127.0.0.1/` and observe that the application is parsing the URL, extracting the hostname, and validating it against a whitelist.
3. Change the URL to `http://username@stock.weliketoshop.net/` and observe that this is accepted, indicating that the URL parser supports embedded credentials.
4. Append a `#` to the username and observe that the URL is now rejected.
5. Double-URL encodes the `#` to `%2523` and observe the extremely suspicious "Internal Server Error" response, indicating that the server may have attempted to connect to "username".
6. To access the admin interface and delete the target user, change the URL to:
[http://localhost:80%2523@stock.weliketoshop.net/admin/delete?username=carlos](http://localhost:80%2523@stock.weliketoshop.net/admin/delete?username=carlos)

A YouTube Channel for Cybersecurity Lab’s Poc and Write-ups

Github for Resources:

Telegram Channel for Free Ethical Hacking Dumps

Thank you for Reading!

Happy Ethical Hacking \~

`Author: Karthikeyan Nagaraj ~ Cyberw1ng`
