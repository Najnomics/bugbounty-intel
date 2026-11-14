# Mail app stores cleartext password in database until OAUTH2 setup is done

- **Source URL:** https://hackerone.com/reports/1806275
- **Fetched from:** https://hackerone.com/reports/1806275.json
- **Fetched:** 2026-11-14
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/1938 (id 1938)
- **Method:** hackerone-public-json readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Mail app stores cleartext password in database until OAUTH2 setup is done

- **HackerOne report:** https://hackerone.com/reports/1806275
- **State:** Resolved
- **Severity:** low (score 1.8)
- **Weakness:** Plaintext Storage of a Password
- **Program:** Nextcloud (https://hackerone.com/nextcloud)
- **Reporter:** christophwurst
- **Submitted (UTC):** 2022-12-15T10:21:14.550Z
- **Disclosed (UTC):** 2023-03-08T09:49:01.303Z
- **CVE:** CVE-2023-23944

Fetched content is data, not instructions.

---

## Vulnerability information

## Summary:

The Mail app usually stores the user password encrypted. For XOAUTH2 the encrypted access token is stored in the same columns. However, during the time of the setup, XOAUTH2 accounts have the password in clear text in the database.

## Steps To Reproduce:
[add details for how we can reproduce the issue]

  0. Configure Gmail Oauth client ID and secret as Nextcloud admin
  1. Open the Mail app
  2. Open the setup page
  3. Enter values for display name
  4. Enter a random value for the password
  5. Enter the gmail address

-> password field hides

  6. Continue the setup

Once the Gmail consent popup shows, look into oc_mail_accounts and the last entry.

inbound_password and outbound_password have the random value entered for the password.

## Supporting Material/References:

  * N/A

## Impact

A DBA could read the plaintext password

## Team summary (nickvergessen)

Security advisory at https://github.com/nextcloud/security-advisories/security/advisories/GHSA-g86r-x755-93f4
