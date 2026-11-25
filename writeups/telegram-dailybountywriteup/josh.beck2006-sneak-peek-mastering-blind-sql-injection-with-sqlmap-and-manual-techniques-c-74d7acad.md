# Sneak Peek

- **Source URL:** https://medium.com/@josh.beck2006/sneak-peek-mastering-blind-sql-injection-with-sqlmap-and-manual-techniques-cve-2023-6063-af904f61f822?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20240306181037/https://medium.com/@josh.beck2006/sneak-peek-mastering-blind-sql-injection-with-sqlmap-and-manual-techniques-cve-2023-6063-af904f61f822?source=rss------bug_bounty-5
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/5458 (id 5458)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Sneak Peek: Mastering Blind SQL Injection with SQLMap and Manual Techniques (CVE-2023–6063)

Downloadable VM and Walkthrough Linked at the bottom of this writeup.

**Lab Summary:**

While the internet is flooded with automated Proof of Concept (PoC) code for exploiting this particular vulnerability, there isn’t a whole lot that explains how SQLMap is able to exfiltrate the data that it does. Focused on the recent CVE-2023–6063 vulnerability in the WordPress plugin WP Fastest Cache, you’ll find no shortage of automated scripts online. However, most leave out the crucial “why” and “how” behind the process

**Lab Objective: (2 Parts)**

- In the first part of this lab we exploit the Blind SQL condition in the WordpPress wp-fastest-cache plugin (ver 1.2.2) using SQLMap
- In the second part of the lab we examine the underlying mechanics of Blind SQL injection and write a manual exploit.

VM with Walkthrough Here:
