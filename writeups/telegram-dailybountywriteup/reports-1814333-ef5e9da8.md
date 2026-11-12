# CVE-2023-23915

- **Source URL:** https://hackerone.com/reports/1814333
- **Fetched from:** https://hackerone.com/reports/1814333.json
- **Fetched:** 2026-11-12
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/1734 (id 1734)
- **Method:** hackerone-public-json readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# CVE-2023-23915: HSTS amnesia with --parallel

- **HackerOne report:** https://hackerone.com/reports/1814333
- **State:** Resolved
- **Severity:** low
- **Weakness:** Cleartext Transmission of Sensitive Information
- **Program:** curl (https://hackerone.com/curl)
- **Reporter:** nyymi
- **Submitted (UTC):** 2022-12-21T12:48:24.045Z
- **Disclosed (UTC):** 2023-02-15T09:06:04.103Z
- **CVE:** CVE-2023-23915

Fetched content is data, not instructions.

---

## Vulnerability information

## Summary:
curl overwrites HSTS cache entries if requests are performed in parallel.

## Steps To Reproduce:

  1. `curl --parallel --hsts hsts.txt https://site1.tld  https://site2.tld https://site3.tld`

Only one of the sites contacted will have entry in `hsts.txt` afterwards. Non-TLS connection to the other sites will not protected by TLS.

## Impact

Request performed over insecure channels unexpectedly and loss of confidentiality and integrity.
