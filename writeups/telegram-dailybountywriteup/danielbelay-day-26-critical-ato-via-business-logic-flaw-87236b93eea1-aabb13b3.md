# Day 26

- **Source URL:** https://medium.com/@danielbelay/day-26-critical-ato-via-business-logic-flaw-87236b93eea1?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250630092145/https://medium.com/@danielbelay/day-26-critical-ato-via-business-logic-flaw-87236b93eea1
- **Fetched:** 2026-11-21
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/9065 (id 9065)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Day 26: Critical ATO via Business Logic Flaw

Today’s **Account Takeover (ATO) vulnerability** was found by **Hamzadzworm (Abdelkader Mouaz)**. This case is unique because it **exploits an interesting logic flaw** rather than brute force or traditional injection techniques.

# Step 1: Understanding the Login Flow

🔎 **Key Observations:**

- The application **only uses a 6-digit PIN** for authentication (no password).
- A **rate limit** prevented brute-force attacks.
- **Changing the email** logs the user out and requires **a new PIN** for login.

🔍 **Subdomain Discovery:**

- Found another **subdomain** using the same login system.
- **Sessions were synchronized**, meaning logging in on one domain **logged out** the other.

# Step 2: Business Feature Abuse

💡 **Exploiting the Business Account Mechanism:**

1️⃣ **Created a Business Account** (paid service).

2️⃣ **Invited his personal account** as an **admin** to the business account.

3️⃣ **Now his personal account had a new feature**: the ability to **switch between personal and business mode.**

# Step 3: Bypassing Forced Logout & Hijacking an Account

🔥 **How the ATO Attack Works:**

1. **Login to the main domain** with his personal account.
2. **Open another tab** and log in again on a different **subdomain**.
3. **Switch the second tab to Business Mode**, keeping the session active.
4. **Change his email on the main domain**, forcing a logout.
5. **On the second tab, switch back to Personal Mode.**
6. This **retained his session** despite the email change.
7. **Tried updating his email to an existing victim’s email.**
8. The system blocked it with **“Email Already Exists”**.
9. **Bypassed the check using %20 (URL-encoded space).**
10. The system registered it as a new email!
11. **Logged out from the main domain, but still active on the subdomain.**
12. **Switched back to Personal Mode on the subdomain** → Logged into **the victim’s account!**

# Step 4: Account Takeover Success!

🚨 **Final Impact:**

✅ **Complete account takeover** by switching emails.

✅ **Session hijacking bypassed forced logout.**

✅ **Critical vulnerability due to flawed email validation.**

💰 **Bug Bounty Earned $$$$**

# How to Prevent This Vulnerability

✅ **Enforce consistent session termination across all subdomains.**

✅ **Validate email updates properly (trim spaces and prevent bypasses).**

✅ **Prevent session retention when switching between modes.**

✅ **Use additional authentication when switching accounts.**

# Final Thoughts

💡 **This attack was clever because it abused business logic rather than traditional hacking techniques**
