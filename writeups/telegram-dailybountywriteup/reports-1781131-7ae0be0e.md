# Cross-Site-Scripting in "Search Messages"

- **Source URL:** https://hackerone.com/reports/1781131
- **Fetched from:** https://hackerone.com/reports/1781131.json
- **Fetched:** 2026-11-13
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/2621 (id 2621)
- **Method:** hackerone-public-json readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Cross-Site-Scripting in "Search Messages"

- **HackerOne report:** https://hackerone.com/reports/1781131
- **State:** Resolved
- **Severity:** medium
- **Weakness:** Cross-site Scripting (XSS) - Stored
- **Program:** Rocket.Chat (https://hackerone.com/rocket_chat)
- **Reporter:** sectex
- **Submitted (UTC):** 2022-11-22T14:38:54.738Z
- **Disclosed (UTC):** 2023-05-09T19:57:26.653Z
- **CVE:** CVE-2023-28358

Fetched content is data, not instructions.

---

## Team summary (mrd0d)

A vulnerability has been discovered in Rocket.Chat where a markdown parsing issue in the "Search Messages" feature allows the insertion of malicious tags. This can be exploited on servers with content security policy disabled possible leading to some issues attacks like account takeover.
