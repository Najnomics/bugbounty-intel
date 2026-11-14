# 1639919

- **Source URL:** https://hackerone.com/reports/1639919
- **Fetched from:** https://hackerone.com/reports/1639919.json
- **Fetched:** 2026-11-14
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/2185 (id 2185)
- **Method:** hackerone-public-json readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Stored XSS Via Filename On https://partners.line.me/

- **HackerOne report:** https://hackerone.com/reports/1639919
- **State:** Resolved
- **Severity:** low
- **Weakness:** Cross-site Scripting (XSS) - Stored
- **Program:** LY Corporation (https://hackerone.com/line)
- **Reporter:** rioncool22
- **Submitted (UTC):** 2022-07-18T07:46:00.044Z
- **Disclosed (UTC):** 2023-03-28T08:13:31.356Z

Fetched content is data, not instructions.

---

## Team summary (calvin55)

When uploading a file to “partners.line.me” with a filename containing an XSS payload, the server did not escape the filename. This caused DOM-based XSS to be embedded in HTML. Uploaded files were stored for a certain period of time only. However, as long as they were available on the server, accessing the path triggered XSS and the saved payload was displayed without escaping. Yet, it turned out that cookie theft was not possible.
