# No password length restriction in reset password endpoint

- **Source URL:** https://hackerone.com/reports/1820864
- **Fetched from:** https://hackerone.com/reports/1820864.json
- **Fetched:** 2026-11-14
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/1660 (id 1660)
- **Method:** hackerone-public-json readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# No password length restriction in reset password endpoint

- **HackerOne report:** https://hackerone.com/reports/1820864
- **State:** Resolved
- **Severity:** low (score 3.5)
- **Weakness:** Uncontrolled Resource Consumption
- **Program:** Nextcloud (https://hackerone.com/nextcloud)
- **Reporter:** aditya404
- **Submitted (UTC):** 2023-01-03T08:44:39.654Z
- **Disclosed (UTC):** 2023-02-09T13:57:52.319Z
- **CVE:** CVE-2023-25816
- **Attachments (filenames only; expiring CDN URLs omitted):** Screenshot_2023-01-03_14_09_52.png (image/png)

Fetched content is data, not instructions.

---

## Vulnerability information

Hi, 

##Summary:
There is no password length restriction in reset password endpoint at https://efss.qloud.my/index.php/login when resetting for new password.


##Steps To Reproduce:
1. Visit https://nextcloud.com/sign-up/ and Sign up.

2. Logout and reset your password.

 3.Go to your email and click on reset password link.
4.Enter 150 characters or more as a password and confirm the characters.
5.You will successfully logged in.

## Impact

Attacker can do denial of service to your server since there is no restriction in the length of password.
Example when he enter like 2500 character, your server will crash for some time 
Below Image is the impact of entering 2500 characters.

##Mitigation :

Restrict user to use less than 40 character as a password, while the restriction should be both on back-end and front-end (with javascript ).

##THANK YOU

## Team summary (nickvergessen)

Security advisory at https://github.com/nextcloud/security-advisories/security/advisories/GHSA-53q2-cm29-7j83
