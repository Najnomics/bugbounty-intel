# user_oidc app is missing bruteforce protection

- **Source URL:** https://hackerone.com/reports/1954711
- **Fetched from:** https://hackerone.com/reports/1954711.json
- **Fetched:** 2026-11-13
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/3131 (id 3131)
- **Method:** hackerone-public-json readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# user_oidc app is missing bruteforce protection

- **HackerOne report:** https://hackerone.com/reports/1954711
- **State:** Resolved
- **Severity:** medium (score 5.5)
- **Weakness:** Improper Restriction of Authentication Attempts
- **Program:** Nextcloud (https://hackerone.com/nextcloud)
- **Reporter:** nickvergessen
- **Submitted (UTC):** 2023-04-19T14:53:04.396Z
- **Disclosed (UTC):** 2023-06-23T09:44:42.159Z
- **CVE:** CVE-2023-32074

Fetched content is data, not instructions.

---

## Vulnerability information

## Summary:
Various controllers of the user_oidc app are not bruteforce protected, allowing attackers to iterate over data until they find valid one.

* Id4meController::login
* Id4meController::code
* LoginController::login
* LoginController::code
* LoginController::csingleLogoutService
* LoginController::cbackChannelLogout

## Impact

Authentication can be broken/bypassed

## Team summary (julien_veyssier)

SA: https://github.com/nextcloud/security-advisories/security/advisories/GHSA-x8mc-84wj-rf34
