# Account Takeover via Duplicate Registration — A 1500 Euro Jackpot

- **Source URL:** https://balook.medium.com/account-takeover-via-duplicate-registration-a-1500-euro-jackpot-2912c23b3ac4?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250501114313/https://balook.medium.com/account-takeover-via-duplicate-registration-a-1500-euro-jackpot-2912c23b3ac4
- **Fetched:** 2026-11-27
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/8914 (id 8914)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# 🔥 Account Takeover via Duplicate Registration — A 1500 Euro Jackpot

Feb 27, 2025

# The Bug

Found a **critical account takeover** in a web application’s registration flow.

The platform **allowed creating the same account (same email)** from a different session, even though the account already existed.

# Step-by-Step PoC

1. Create account with email: **xyz@account.com** and place some orders.
2. In a **different session**, re-register using the **same email**: **xyz@account.com**.
3. ✅ Registration works again — no error for duplicate account.
4. Now the attacker controls:

- The victim’s orders
- Can change the password
- Full account access = Total takeover.

# Impact

- **Complete account takeover**
- Orders, personal data, everything exposed
- Victim locked out after attacker changes password

# Status

- **Accepted as High** ✅
- **Rewarded 1500 Euros** 💰

# Takeaway

Duplicate account creation = critical bug hiding in plain sight.

Sometimes **basic checks** (like preventing duplicate registrations) protect the **entire platform**.
