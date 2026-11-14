# 963384

- **Source URL:** https://hackerone.com/reports/963384
- **Fetched from:** https://hackerone.com/reports/963384.json
- **Fetched:** 2026-11-14
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/1174 (id 1174)
- **Method:** hackerone-public-json readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# mysql credentials exposed on - https://cz.acronis.com/docker-compose.yml

- **HackerOne report:** https://hackerone.com/reports/963384
- **State:** Resolved
- **Severity:** low
- **Weakness:** Insufficiently Protected Credentials
- **Program:** Acronis (https://hackerone.com/acronis)
- **Reporter:** melar_dev
- **Submitted (UTC):** 2020-08-20T15:59:21.830Z
- **Disclosed (UTC):** 2022-12-24T01:33:24.087Z

Fetched content is data, not instructions.

---

## Vulnerability information

Hi, there are some MySQL credentials exposed on https://cz.acronis.com/docker-compose.yml
It is not that you are gonna avoid a compromise with that user/password pair, but just in case you don't wanna make it even easier publishing the credentials to the wild x]

## Impact

MySQL credentials exposed publicly
