# Stored cross-site scripting in dataset owner.

- **Source URL:** https://hackerone.com/reports/708123
- **Fetched from:** https://hackerone.com/reports/708123.json
- **Fetched:** 2026-11-15
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/1160 (id 1160)
- **Method:** hackerone-public-json readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Stored cross-site scripting in dataset owner.

- **HackerOne report:** https://hackerone.com/reports/708123
- **State:** Resolved
- **Severity:** none
- **Weakness:** Cross-site Scripting (XSS) - Stored
- **Program:** Quantopian (https://hackerone.com/quantopian)
- **Reporter:** irisrumtub
- **Submitted (UTC):** 2019-10-05T09:23:46.300Z
- **Disclosed (UTC):** 2022-12-21T20:13:33.471Z

Fetched content is data, not instructions.

---

## Vulnerability information

Hi again. Another XSS this time.
**Summary:** Unescaped chars in 'dataset owner' could be abused to store arbitrary javascript.

**Description:** There is a 'dataset owner' field in new 'custom dataset dashboard' which contains unsanitized output. If attacker would modify his name, like first name '<img src=x' and last name 
'onerror=alert(1)>', the field would hold a script. While for most users this is a case of self-xss, for enterprise users (for which, as i understand. this field was introduced in the first place), it can lead to executing arbitrary javascript.

**Steps To Reproduce:**

  1. Put the payload in name and/or surname
 *(first name '<img src=x' and last name 
'onerror=alert(1)>')*
  2. Navigate to custom datasets. 


**Test account information**

tvburis+hackerone@gmail.com

## Impact

Executing arbitrary javascript, stealing other users' algos as demonstrated in previous reports with XSS on quantopian domain.
