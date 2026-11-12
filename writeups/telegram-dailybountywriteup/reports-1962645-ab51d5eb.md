# [accounts.reddit.com] Redirect parameter allows for XSS

- **Source URL:** https://hackerone.com/reports/1962645
- **Fetched from:** https://hackerone.com/reports/1962645.json
- **Fetched:** 2026-11-12
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/2745 (id 2745)
- **Method:** hackerone-public-json readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# [accounts.reddit.com] Redirect parameter allows for XSS

- **HackerOne report:** https://hackerone.com/reports/1962645
- **State:** Resolved
- **Severity:** high
- **Weakness:** Cross-site Scripting (XSS) - Generic
- **Program:** Reddit (https://hackerone.com/reddit)
- **Reporter:** dvorakxl
- **Submitted (UTC):** 2023-04-26T16:43:39.352Z
- **Disclosed (UTC):** 2023-05-18T13:46:49.459Z
- **Attachments (filenames only; expiring CDN URLs omitted):** XSSsignedin.jpg (image/jpeg); XSSnotsignedin.jpg (image/jpeg)

Fetched content is data, not instructions.

---

## Vulnerability information

## Summary:
Hello team! I was tampering with the dest parameter in accounts.reddit.com and found out it is vulnerable to Cross Site Scripting once the victim performs the log in.

## Steps To Reproduce:
  1. Enter to the following link: ```https://accounts.reddit.com/?dest=javascript:alert(document.domain)```
  - If not signed in, the user will be promped to log in and after doing so XSS will excecute

{F2315850}
  - If user is logged into his account, following the link will also make the XSS pop up

{F2315847}

## Impact

An attacker could trick users into executing XSS, executing code and stealing their cookies only by them logging in.
