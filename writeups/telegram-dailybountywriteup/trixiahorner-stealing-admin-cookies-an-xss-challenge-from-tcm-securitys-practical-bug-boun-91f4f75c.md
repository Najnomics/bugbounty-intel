# Stealing Admin Cookies

- **Source URL:** https://medium.com/@trixiahorner/stealing-admin-cookies-an-xss-challenge-from-tcm-securitys-practical-bug-bounty-course-b08a990cca84?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20261019201732/https://medium.com/@trixiahorner/stealing-admin-cookies-an-xss-challenge-from-tcm-securitys-practical-bug-bounty-course-b08a990cca84
- **Fetched:** 2026-11-23
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/7063 (id 7063)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
Member-only story

# Stealing Admin Cookies: An XSS Challenge from TCM Security’s Practical Bug Bounty Course

## CHALLENGE

This Cross-Site Scripting (XSS) challenge is part of the Injection Attacks section from TCM Security Academy’s Practical Bug Bounty Course. The goal of the challenge is to exploit a XSS vulnerability in order to steal or exfiltrate the admin’s cookie.

🔓Not a member? I want this story to be available to everyone, so click [***HERE***](/@trixiahorner/stealing-admin-cookies-an-xss-challenge-from-tcm-securitys-practical-bug-bounty-course-b08a990cca84?sk=1830fd40546ae0df82a2ee8f00357d6d) to read it for free.

## ENVIRONMENT

- Netcat listener on Kali Attack machine: 192.168.65.130:8080
- Container 1: Support Portal to submit a support ticket
- Container 2: Admin Portal where tickets are submitted

*Containers are separate, isolated browser environments that prevent cookies, sessions, and other data from being shared between them.*
