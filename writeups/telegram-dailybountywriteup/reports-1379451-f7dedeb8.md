# Messages can be hidden regardless of server configuration

- **Source URL:** https://hackerone.com/reports/1379451
- **Fetched from:** https://hackerone.com/reports/1379451.json
- **Fetched:** 2026-11-13
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/2474 (id 2474)
- **Method:** hackerone-public-json readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Messages can be hidden regardless of server configuration

- **HackerOne report:** https://hackerone.com/reports/1379451
- **State:** Resolved
- **Severity:** medium (score 4.3)
- **Weakness:** None
- **Program:** Rocket.Chat (https://hackerone.com/rocket_chat)
- **Reporter:** gronke
- **Submitted (UTC):** 2021-10-23T22:45:17.973Z
- **Disclosed (UTC):** 2023-04-25T22:17:10.893Z
- **CVE:** CVE-2023-28318

Fetched content is data, not instructions.

---

## Team summary (mrd0d)

A vulnerability has been discovered in Rocket.Chat, where messages can be hidden regardless of the Message_KeepHistory or Message_ShowDeletedStatus server configuration. This allows users to bypass the intended message deletion behavior, hiding messages and deletion notices.
