# Completely remove VPN profile from locked WARP iOS cient.

- **Source URL:** https://hackerone.com/reports/1633231
- **Fetched from:** https://hackerone.com/reports/1633231.json
- **Fetched:** 2026-11-12
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/745 (id 745)
- **Method:** hackerone-public-json readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Completely remove VPN profile from locked WARP iOS cient.

- **HackerOne report:** https://hackerone.com/reports/1633231
- **State:** Resolved
- **Severity:** high (score 7.3)
- **Weakness:** Client-Side Enforcement of Server-Side Security
- **Program:** Cloudflare Public Bug Bounty (https://hackerone.com/cloudflare)
- **Reporter:** oracularhades
- **Submitted (UTC):** 2022-07-11T09:19:51.155Z
- **Disclosed (UTC):** 2022-11-07T10:59:27.873Z
- **CVE:** CVE-2022-3337

Fetched content is data, not instructions.

---

## Team summary (m0nia)

It was possible for a user to delete VPN profile from  WARP mobile client on iOS platform despite the [Lock WARP switch](https://developers.cloudflare.com/cloudflare-one/connections/connect-devices/warp/warp-settings/#lock-warp-switch) feature being enabled on Zero Trust Platform. This led to bypassing policies and restriction enforced for enrolled devices by the Zero Trust platform.
The issue was fixed in Warp iOS mobile client v. 6.15.
