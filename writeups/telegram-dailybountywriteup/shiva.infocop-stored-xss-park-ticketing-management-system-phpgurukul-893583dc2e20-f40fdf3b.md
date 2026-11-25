# Stored XSS — PARK TICKETING MANAGEMENT SYSTEM(Phpgurukul)

- **Source URL:** https://medium.com/@shiva.infocop/stored-xss-park-ticketing-management-system-phpgurukul-893583dc2e20?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20230311160700/https://medium.com/@shiva.infocop/stored-xss-park-ticketing-management-system-phpgurukul-893583dc2e20?source=rss------bug_bounty-5
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/1587 (id 1587)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Stored XSS — PARK TICKETING MANAGEMENT SYSTEM(Phpgurukul)

*# Exploit Title: PARK TICKETING MANAGEMENT SYSTEM — Stored XSS Vulnreability. # Date: 25–01–2023 # Exploit Author: Venkata Siva Kumar Medituru # Vendor Homepage:* 

[*https://phpgurukul.com/*](https://web.archive.org/web/20230311160700/https://phpgurukul.com/)

*# Software Link:* 

[*https://phpgurukul.com/park-ticketing-management-system-using-php-and-mysql/*](https://web.archive.org/web/20230311160700/https://phpgurukul.com/park-ticketing-management-system-using-php-and-mysql/)

*# Vulnerable Parameter : Admin Name
# Version: 1.0
# Tested on: Windows 10
# Contact:* 

[*https://www.linkedin.com/in/shivakumar-m-v/*](https://web.archive.org/web/20230311160700/https://www.linkedin.com/in/shivakumar-m-v/)

XSS is an attack technique that injects malicious code into vulnerable web applications. Unlike other attacks, this technique does not target the web server itself, but the user’s browser.

Stored XSS is a type of XSS that stores malicious code on the application server. Using stored XSS is only possible if your application is designed to store user input.

The Reproducive Steps are given in Video PoC.

Remediation :

01\) Use Web Application Firewall.

02\) Input validation.
