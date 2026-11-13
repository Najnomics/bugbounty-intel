# 1947376

- **Source URL:** https://hackerone.com/reports/1947376
- **Fetched from:** https://hackerone.com/reports/1947376.json
- **Fetched:** 2026-11-13
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/3157 (id 3157)
- **Method:** hackerone-public-json readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# ███████  ' can delete any animal from other account  '  at ██████████ 

- **HackerOne report:** https://hackerone.com/reports/1947376
- **State:** Resolved
- **Severity:** medium
- **Weakness:** Insecure Direct Object Reference (IDOR)
- **Program:** Mars (https://hackerone.com/mars)
- **Reporter:** 0xs4m
- **Submitted (UTC):** 2023-04-14T15:23:41.106Z
- **Disclosed (UTC):** 2023-06-23T14:59:57.194Z

Fetched content is data, not instructions.

---

## Vulnerability information

hi team
i found ███████████ , i can delete any animal from other account easily

1.  Go to registration page (████████)
2.  Verified your account.
3.  Go to login page and login your account.

For the fastly test, use this credentials to login (my test account)

 █████████████████ For Attacker

email: ████████████████
pass: Password

 █████████████ For Victim

email: ████
pass: Password

After login i create 2 account for attacker and victim , in the attacker's account, i delete my animal, and i send request to burp .. i change my animal id to victim animal id so i succeeded

███

## Impact

████████████████

## Team summary (ideborah)

A vulnerability was present in the ████████████ website that allows an authenticated user to delete animals belonging to other users' accounts. This issue arises due to an Insecure Direct Object Reference (IDOR) vulnerability where the system's authorization mechanism fails to properly validate and restrict access to protected resources based on the user's identity. As a result, a malicious user can manipulate the ██████████████ parameter in the request sent to the ████████████████ endpoint to delete any animal from other users' accounts, leading to unauthorized data deletion.
