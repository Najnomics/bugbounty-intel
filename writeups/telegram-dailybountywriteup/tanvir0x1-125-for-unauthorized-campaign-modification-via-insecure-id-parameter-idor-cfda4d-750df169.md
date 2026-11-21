# $125 For Unauthorized Campaign Modification via Insecure ID Parameter (IDOR)

- **Source URL:** https://medium.com/@Tanvir0x1/125-for-unauthorized-campaign-modification-via-insecure-id-parameter-idor-cfda4db522e2?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250822021250/https://medium.com/@Tanvir0x1/125-for-unauthorized-campaign-modification-via-insecure-id-parameter-idor-cfda4db522e2
- **Fetched:** 2026-11-21
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/10510 (id 10510)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# 🚨$125 For Unauthorized Campaign Modification via Insecure ID Parameter (IDOR)

2 min readAug 13, 2025

# 📝 Summary

A vulnerability was discovered in the campaign management feature that allows one authenticated user to modify another user’s campaign by tampering with the request parameters. This is caused by insufficient access control on the campaign ID parameter in the backend. An attacker can manipulate the campaign ID in requests and bypass CSRF protection to perform unauthorized edits. 😱

# 🔍 **Steps to Reproduce**

1. Log in to **Account A** and create a campaign publicly. 🎯
2. Capture the request for creating or modifying the campaign using a proxy tool (e.g., Burp Suite). 🕵️♂️
3. Inspect the request and identify the id parameter associated with the campaign. 🔑
4. Log in to **Account B** and navigate to the campaign management page.
5. Initiate an edit action on a (same) campaign under Account B, capturing the request. ✏️
6. Modify the request:

- Replace the campaign id with the ID from Account A’s campaign. 🔄
- Remove the CSRF token. ❌

1. Send the modified request. **Boom!** 💥 Account A’s campaign is modified without authorization.

# ⚠️ Impact

- **Confidentiality:** Attackers can read and modify other users’ campaigns. 👀
- **Integrity:** Users’ campaigns can be maliciously edited or destroyed. 🛑
- **Business Risk:** Potential for defacement, misinformation, or abuse of campaign-related features. 💼

# 🛠 Mitigation

1. Implement proper access control checks on all sensitive endpoints, verifying that the authenticated user owns the resource they are attempting to access or modify. ✅
2. Ensure that CSRF tokens are strictly validated and tied to the user session. 🔒
3. Avoid exposing sequential or guessable identifiers; consider using UUIDs or other non-sequential identifiers for sensitive objects. 🔢
4. Conduct a full audit of endpoints handling user data to confirm no other IDOR vulnerabilities exist. 🧹

# **Reward**

Reported Date:June 15, 2025, 11:16am UTC

Reward Date:July 7

Reward:125$
