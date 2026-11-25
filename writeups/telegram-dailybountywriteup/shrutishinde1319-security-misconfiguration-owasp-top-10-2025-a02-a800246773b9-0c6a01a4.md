# Security Misconfiguration

- **Source URL:** https://medium.com/@shrutishinde1319/security-misconfiguration-owasp-top-10-2025-a02-a800246773b9
- **Fetched from:** https://medium.com/@shrutishinde1319/security-misconfiguration-owasp-top-10-2025-a02-a800246773b9?source=rss-85fdc83f6cda------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14948 (id 14948)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** Shruti Vijay Shinde / Wed, 14 Oct 2026 17:42:39 GMT

*A beginner-friendly look at the #2 web security risk*

Hey everyone! 👋

In my previous article, we discussed **A01: Broken Access Control**, the #1 risk in the OWASP Top 10 (2025).

Read it here: [Broken Access Control: OWASP Top 10 2025](https://medium.com/@shrutishinde1319/broken-access-control-owasp-top-10-2025-the-1-web-security-risk-d843bd36ef5e)

Today, let’s understand **A02:2025 — Security Misconfiguration**, the #2 web security risk.

**Configuration means the settings that control how an application or system works.**

For example:

**Security Misconfiguration happens when a system has incorrect or insecure settings that expose sensitive information, unnecessary features, or unauthorized access.**

Imagine your house has strong locks, but you accidentally leave a window open. Someone could enter through that window.

Similarly, even if a website has good security, one incorrect setting can make it vulnerable.

Let’s look at some common examples.

Some software comes with default usernames and passwords, such as:

Username: admin

Password: admin

If these credentials are not changed, an attacker might use them to access the system.

**As a Pentester:** Identify the technology and check its official documentation for known default credentials. Test only with proper authorization.

Files like .env, .git, backups, and database dumps may contain passwords, API keys, or other sensitive information.

For example, if this file is publicly accessible:

https://example.com/.env

An attacker might discover secrets that should remain private.

**As a Pentester:** Check for exposed files and directories using tools such as ffuf and dirsearch.

An IP address identifies a machine, while a port identifies a service running on it.

A database port exposed to the internet may allow unauthorized connection attempts.

**As a Pentester:** Use Nmap to identify open ports and investigate whether the exposed services are necessary.

nmap example.com

HTTP does not encrypt web traffic by itself. HTTPS uses TLS to protect communication between the browser and server.

With plain HTTP, someone capable of intercepting network traffic may read or modify sensitive information.

**Prevention:** Use HTTPS and redirect HTTP traffic to HTTPS.

When something goes wrong, an application may reveal information such as:

Error: Database connection failed

File: /var/www/app/database.py

Database: MySQL

Internal IP: 10.0.0.15

This information can help an attacker understand the application’s internal structure.

**As a Pentester:** Observe how the application responds to invalid URLs and inputs.

**Prevention:** Display generic error messages to users and keep detailed errors in protected server-side logs.

A directory is simply a folder on the server.

If directory listing is enabled, visiting a folder might reveal its contents:

Index of /backup/

backup.zip

config.old

database.sql

These files may contain sensitive information.

**Prevention:** Disable directory listing and prevent public access to sensitive files.

Debug mode helps developers identify errors during development. However, leaving it enabled in production may expose file paths, internal details, and secrets.

DatabaseError

File: /var/www/app/login.py

Line: 87

**As a Pentester:** Trigger harmless errors and check whether detailed technical information appears in the response.

**Prevention:** Disable debug mode in production and show users generic error messages.

Here are the key practices:

Security Misconfiguration is often caused by simple mistakes, As a **Pentester**, your goal is to identify these insecure settings, understand their impact, and recommend fixes.

Thanks for reading!

#CyberSecurity #OWASP #WebApplicationSecurity #PenetrationTesting #InfoSec
