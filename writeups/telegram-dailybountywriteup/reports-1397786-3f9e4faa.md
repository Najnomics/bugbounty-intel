# Default Admin Username and Password on remedysso.mtncameroon.net

- **Source URL:** https://hackerone.com/reports/1397786
- **Fetched from:** https://hackerone.com/reports/1397786.json
- **Fetched:** 2026-11-15
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/91 (id 91)
- **Method:** hackerone-public-json readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Default Admin Username and Password on remedysso.mtncameroon.net

- **HackerOne report:** https://hackerone.com/reports/1397786
- **State:** Resolved
- **Severity:** high (score 7.3)
- **Weakness:** None
- **Program:** MTN Group (https://hackerone.com/mtn_group)
- **Reporter:** dh0pe
- **Submitted (UTC):** 2021-11-10T19:00:17.419Z
- **Disclosed (UTC):** 2022-09-01T20:50:32.925Z

Fetched content is data, not instructions.

---

## Vulnerability information

## Summary:
A Remedy Single Sign-On (Remedy SSO) Server is running at https://remedysso.mtncameroon.net/rsso/admin/#/.  
It is possible to access the application is using the default Administrator credentials.

## Steps To Reproduce:
Go to https://remedysso.mtncameroon.net/rsso/admin/#/ and login with credentials:
- Username: Admin
- Password: RSSO#Admin#

## Remediation
Change the password of the Admin user or disable the account.

## References
https://cwe.mitre.org/data/definitions/521.html

## Impact

A MNT Group Single Sign-On application was misconfigured in a manner that may have allowed a malicious user to login with the administrator user. The user is capable to perform any kind of configuration of the SSO system and retrieve sensitive information about organization users and infrastructure.
