# Critical sensitive information Disclosure. [HtUS]

- **Source URL:** https://hackerone.com/reports/1626236
- **Fetched from:** https://hackerone.com/reports/1626236.json
- **Fetched:** 2026-11-14
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/1381 (id 1381)
- **Method:** hackerone-public-json readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Critical sensitive information Disclosure. [HtUS]

- **HackerOne report:** https://hackerone.com/reports/1626236
- **State:** Resolved
- **Severity:** high (score 7.5)
- **Weakness:** Information Disclosure
- **Program:** U.S. Dept Of Defense (https://hackerone.com/deptofdefense)
- **Reporter:** ghostkernalbbt
- **Submitted (UTC):** 2022-07-05T14:04:33.153Z
- **Disclosed (UTC):** 2023-01-13T18:05:48.810Z

Fetched content is data, not instructions.

---

## Vulnerability information

(Database user,Database password,Database name) 
on https://██████.edu/

I got sensitive information:
view-source:https://██████████.edu/database.php.orig


Database information (Database user,Database password,Database name)
$hostname     = '████████.edu';
$db         = '█████████';
$username     = '████_user';
$password     = '████';

## Impact

Bug impact:
Sensitive information disclosed and possible for an attacker can access into the system.
