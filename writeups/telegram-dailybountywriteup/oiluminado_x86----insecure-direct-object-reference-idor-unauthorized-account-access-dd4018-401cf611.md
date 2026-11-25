# ️Insecure Direct Object Reference (IDOR) — Unauthorized Account Access

- **Source URL:** https://medium.com/@Oiluminado_x86/%EF%B8%8Finsecure-direct-object-reference-idor-unauthorized-account-access-dd4018b98fa9?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250501121259/https://medium.com/@Oiluminado_x86/%EF%B8%8Finsecure-direct-object-reference-idor-unauthorized-account-access-dd4018b98fa9?source=rss------bug_bounty-5
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/9202 (id 9202)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# **🛡️Insecure Direct Object Reference (IDOR) — Unauthorized Account Access**

بسم الله والصلاة والسلام على رسول الله ﷺ❤️، اللهم علِّمنا ما ينفعنا، وانفعنا بما علَّمتنا، وزِدنا علمًا نافعًا

📌 Vulnerability Details

**Title:** IDOR Leads to Unauthorized Account Access .

**Vulnerability Rating Taxonomy (VRT):** P1 — Broken Access Control → IDOR

📝 Description

During my testing of \[programe-target.com\] , I discovered an **Insecure Direct Object Reference (IDOR)** vulnerability that allowed unauthorized access to **other users’ accounts** by simply modifying a numerical identifier in the URL. This issue stemmed from improper access control validation, meaning that an attacker could directly access another user’s dashboard **without authentication**.

# 🎯 Impact

**An attacker could :**

- Access **any user’s private dashboard** and view sensitive information.
- Perform **actions on behalf of other users** if additional functionalities exist .
- Potentially **escalate privileges** depending on the application structure .

This vulnerability could lead to **mass account compromise**, exposing sensitive data and harming user trust .

# 🚀 Proof of Concept (PoC)

# 1️⃣ Steps to Reproduce:

1. **Login** to the target application.
2. Navigate to the **dashboard** page where user-specific data is displayed.
3. Observe the URL structure :

1. Modify the `PANUM` parameter to another user's ID (e.g., `12346`).

1. **Result:** The account data of the modified `PANUM` is loaded **without authentication**, confirming an **IDOR vulnerability**.

# 📸 Screenshots/Evidence:

This My Actual Account :

Access to O**ther Users’ Accounts : ( by** changing id**)**

# 🎉 Final Thoughts

This was a fun **IDOR finding** , proving that **simple parameter tampering** can still lead to severe security risks! Always remember, **“Replacing IDs is my job!”** 😉

Let me know your thoughts and feedback! ❤️

**Happy Hunting!** 🐞🚀
