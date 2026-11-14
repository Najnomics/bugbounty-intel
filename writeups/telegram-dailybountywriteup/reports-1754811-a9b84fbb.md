# Extraction of Pages build scripts, config values, tokens, etc. via symlinks

- **Source URL:** https://hackerone.com/reports/1754811
- **Fetched from:** https://hackerone.com/reports/1754811.json
- **Fetched:** 2026-11-14
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/1914 (id 1914)
- **Method:** hackerone-public-json readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Extraction of Pages build scripts, config values, tokens, etc. via symlinks

- **HackerOne report:** https://hackerone.com/reports/1754811
- **State:** Resolved
- **Severity:** medium (score 4.8)
- **Weakness:** Information Disclosure
- **Program:** Cloudflare Public Bug Bounty (https://hackerone.com/cloudflare)
- **Reporter:** mattipv4
- **Submitted (UTC):** 2022-10-29T03:05:11.594Z
- **Disclosed (UTC):** 2023-03-06T16:03:29.964Z

Fetched content is data, not instructions.

---

## Team summary (ncabete)

Due to a broader permission set on certain folders within the filesystem structure, a malicious Pages build could leverage symlinks to extract build source/configuration and environment variables. While these variables were scoped to allow access to the user's own Pages site data and not the data of others, Cloudflare's Engineering team chose to remediate the issue by tightening permissions on the file system.
