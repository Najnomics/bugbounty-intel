# open redirect to a remote website which can phish users

- **Source URL:** https://hackerone.com/reports/1397804
- **Fetched from:** https://hackerone.com/reports/1397804.json
- **Fetched:** 2026-11-12
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/908 (id 908)
- **Method:** hackerone-public-json readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# open redirect to a remote website which can phish users

- **HackerOne report:** https://hackerone.com/reports/1397804
- **State:** Informative
- **Severity:** medium (score 5.4)
- **Weakness:** Open Redirect
- **Program:** Concrete CMS (https://hackerone.com/concretecms)
- **Reporter:** adrian_t
- **Submitted (UTC):** 2021-11-10T19:58:19.110Z
- **Disclosed (UTC):** 2022-11-25T18:08:35.649Z
- **Attachments (filenames only; expiring CDN URLs omitted):** Open_redirect.png (image/png)

Fetched content is data, not instructions.

---

## Vulnerability information

By Adding some extra headers in the request I noticed that  the user is redirected to a remote website. This can lead to stealing a user credentials (phishing) on a remote server.

These headers can be added either using a MITM attack or by chaining with another vulnerability such as request smuggling, header injection more commonly abusing a reverse proxy that sits in front of the website.

ps:crayons

## Impact

This can lead to stealing a user credentials (phishing) on a remote server or planting malware on the user's computer.
