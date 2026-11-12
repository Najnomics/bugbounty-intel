# Web Cache Deception vulnerability on algolia.com leads to personal information leakage

- **Source URL:** https://hackerone.com/reports/1530066
- **Fetched from:** https://hackerone.com/reports/1530066.json
- **Fetched:** 2026-11-12
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/2409 (id 2409)
- **Method:** hackerone-public-json readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Web Cache Deception vulnerability on algolia.com leads to personal information leakage

- **HackerOne report:** https://hackerone.com/reports/1530066
- **State:** Resolved
- **Severity:** medium (score 5.0)
- **Weakness:** Violation of Secure Design Principles
- **Program:** Algolia (https://hackerone.com/algolia)
- **Reporter:** golim
- **Submitted (UTC):** 2022-04-04T14:27:01.209Z
- **Disclosed (UTC):** 2023-04-19T09:25:31.873Z

Fetched content is data, not instructions.

---

## Team summary (antoineb)

A web cache deception(WCD) was found on our main website (algolia.com). An attacker could trick a caching proxy into storing private information transmitted over the internet from authenticated user. To do so, attacker would use simple social engineering where the victim is only required to open a link in a browser while being authenticated on the website. The attacker could then access the cached data, which can include personal and sensitive information of the victim. The exploit URL was formed by using a randomly named css file.
