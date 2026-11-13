# Cloudflare CASB Confused Deputy Problem

- **Source URL:** https://hackerone.com/reports/1952124
- **Fetched from:** https://hackerone.com/reports/1952124.json
- **Fetched:** 2026-11-13
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/2932 (id 2932)
- **Method:** hackerone-public-json readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Cloudflare CASB Confused Deputy Problem

- **HackerOne report:** https://hackerone.com/reports/1952124
- **State:** Resolved
- **Severity:** critical (score 9.7)
- **Weakness:** None
- **Program:** Cloudflare Public Bug Bounty (https://hackerone.com/cloudflare)
- **Reporter:** albertspedersen
- **Submitted (UTC):** 2023-04-18T13:45:50.324Z
- **Disclosed (UTC):** 2023-06-07T09:05:52.488Z

Fetched content is data, not instructions.

---

## Team summary (m0nia)

Cloudflare CASB on a select number of integrations, Microsoft and GitHub, was vulnerable to the confused deputy problem. If an attacker, via a brute force attack or another mechanism, was able to enumerate a valid Microsoft tenant UUID or Microsoft domain, or GitHub installation_id that an existing Cloudflare CASB customer had integrated with, then the attacker would have been able to create a new integration which could surface sensitive information. Cloudflare's CASB engineering team rapidly implemented a fix to disallow the ability to create multiple integrations pointing to the same tenant, thus nullifying the attack as an option. Moreover, an internal investigation did not show impact to any customer data (outside of the reporting researcher's accounts).
