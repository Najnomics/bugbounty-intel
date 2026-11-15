# jira discloser information

- **Source URL:** https://hackerone.com/reports/994612
- **Fetched from:** https://hackerone.com/reports/994612.json
- **Fetched:** 2026-11-15
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/630 (id 630)
- **Method:** hackerone-public-json readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# jira discloser information 

- **HackerOne report:** https://hackerone.com/reports/994612
- **State:** Resolved
- **Severity:** low
- **Weakness:** Information Disclosure
- **Program:** Informatica (https://hackerone.com/informatica)
- **Reporter:** isumitpatel
- **Submitted (UTC):** 2020-09-30T04:30:22.399Z
- **Disclosed (UTC):** 2022-10-03T13:03:54.800Z

Fetched content is data, not instructions.

---

## Vulnerability information

The ticket raising system used by informatica suffers from an informational vulnerability where in an attacker can view certain details about open bugs or project information of informatica. Details include  names and potentially  and ticket names which an unauthorized personnel can view without login that can be very useful to an attacker.

endpoints:

https://infajira.informatica.com/secure/QueryComponent!Default.jspa

## Impact

attacker miss use this information
