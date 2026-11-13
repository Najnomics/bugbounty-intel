# See whos interested in working for your company - security issue

- **Source URL:** https://hackerone.com/reports/1945417
- **Fetched from:** https://hackerone.com/reports/1945417.json
- **Fetched:** 2026-11-13
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/3080 (id 3080)
- **Method:** hackerone-public-json readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# “See who’s interested in working for your company” - security issue

- **HackerOne report:** https://hackerone.com/reports/1945417
- **State:** Resolved
- **Severity:** medium (score 4.3)
- **Weakness:** Information Disclosure
- **Program:** LinkedIn (https://hackerone.com/linkedin)
- **Reporter:** headhunter
- **Submitted (UTC):** 2023-04-13T09:44:35.437Z
- **Disclosed (UTC):** 2023-06-21T13:34:33.759Z

Fetched content is data, not instructions.

---

## Team summary (neema-lnkd)

The issue identified by @headhunter required a member have access to LinkedIn Recruiter and was related to the "See who’s interested in working for your company" feature. The issue allowed the recruiter to view profiles of members interested in working for certain companies. After validating the vulnerability report, a fix was deployed to production within one month. Thanks again for your continued great work @headhunter!

## Researcher summary (headhunter)

A security issue existed that could potentially exploit LinkedIn's new feature, "See who’s interested in working for your company". With the use of LinkedIn's Recruiter product, an attacker could access the list of individuals showing interest in working at any company registered at LinkedIn (where this feature was activated on the LinkedIn page).
