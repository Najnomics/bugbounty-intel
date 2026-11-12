# CSRF with logout action

- **Source URL:** https://hackerone.com/reports/1971589
- **Fetched from:** https://hackerone.com/reports/1971589.json
- **Fetched:** 2026-11-12
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/3029 (id 3029)
- **Method:** hackerone-public-json readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# CSRF with logout action

- **HackerOne report:** https://hackerone.com/reports/1971589
- **State:** Resolved
- **Severity:** None
- **Weakness:** Cross-Site Request Forgery (CSRF)
- **Program:** Weblate (https://hackerone.com/weblate)
- **Reporter:** mbi3s
- **Submitted (UTC):** 2023-05-03T20:27:08.526Z
- **Disclosed (UTC):** 2023-06-16T07:59:20.707Z

Fetched content is data, not instructions.

---

## Vulnerability information

Hi, I wanted let you know and saw that previously similar issue was fixed.
Repro steps: Go to https://weblate.org/pl/ and click top right icon for logging in (user-tab user-anonymous, https://weblate.org/saml2/login/?next=/pl/).
Log in using username and password (https://hosted.weblate.org/accounts/login/?next=/idp/login/process/). 
Logged in on site https://weblate.org/pl/ use link: https://weblate.org/logout/
See logged out.

The similar result with using external page with prepared CSRF payload like:
`<a href="https://weblate.org/logout/"> Click me to see bonus pack`
Here as logged in user use this link from external page, next go to tab where logged in and refresh the page - see logged out there too.

Best regards,

## Impact

Bad actor can affect the user's login status - logged out.
