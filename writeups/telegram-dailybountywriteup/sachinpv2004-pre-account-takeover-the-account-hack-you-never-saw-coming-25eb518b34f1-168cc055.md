# Pre-Account Takeover

- **Source URL:** https://medium.com/@sachinpv2004/pre-account-takeover-the-account-hack-you-never-saw-coming-25eb518b34f1?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250418153428/https://medium.com/@sachinpv2004/pre-account-takeover-the-account-hack-you-never-saw-coming-25eb518b34f1
- **Fetched:** 2026-11-21
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/9394 (id 9394)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# What Is a Pre-Account Takeover?

Imagine signing up for a new app with your email address, only to find that… your account already exists. Even worse? Someone else has been using it.

A **Pre-Account Takeover (PreATO)** is a type of attack where a malicious actor *creates an account using your email address before you do*. When you eventually sign up using that same email, the attacker already has access to your account — and possibly control over sensitive information.

# How Do Pre-Account Takeovers Work?

There are a few common scenarios where PreATO can happen:

# 1. Insecure Password Reset Flows

## 📌 The Attack:

Attackers trigger password resets on dormant or inactive accounts, then wait. If the password reset link doesn’t expire (or remains valid for too long), they reset the password and gain control.

## 🧠 Real Case:

**Twitter (2020)** — While not a classic PreATO, attackers exploited weak internal tools and password reset APIs to hijack high-profile accounts like **Elon Musk**, **Barack Obama**, and **Apple**. The flaw? Poor access control and token handling.

*✅ Takeaway: Always expire password reset tokens promptly. Don’t allow resets on inactive or unverified accounts.*


# 2. Session Hijacking Before Login

## 📌 The Attack:

Some platforms create guest session tokens *before* authentication (e.g., for browsing or adding items to a cart). If these tokens persist after login or can be tied to new accounts, attackers can hijack them.

## 🧠 Real Case:

A **major e-commerce platform** allowed unauthenticated users to create carts. Attackers stole session tokens, waited for victims to register, and gained access to their carts, addresses, and even saved cards.

*✅ Takeaway: Don’t allow pre-authenticated session tokens to persist across login boundaries unless tightly scoped and revalidated.*


# 3. Fake Account Creation (Shadow Accounts)

## 📌 The Attack:

Attackers pre-register accounts using email addresses of real users or typo variants (e.g., `john.doe@gmai1.com`). When the real user signs up or logs in via OAuth, the attacker already controls the account—or a lookalike.

## 🧠 Real Case:

A **fintech startup** found over **5,000 “shadow accounts”** created using misspelled emails (e.g., `jane.doe@gmial.com`). These were used to receive bonus credits and perform fraudulent transactions.

*✅ Takeaway: Validate and verify email ownership* before *granting access or bonuses. Implement typo-squatting detection if possible.*


# 4. Weak Email Verification

## 📌 The Attack:

If an app doesn’t enforce email verification, attackers can:

- Sign up using **disposable emails**
- Abuse “unverified” accounts for **free trials**, **referrals**, or **spam**

## 🧠 Real Case:

A **VPN provider** reported losing over **$2 million** from attackers abusing free trials and referral programs via throwaway, unverified accounts.

*✅ Takeaway: Don’t grant premium features to unverified accounts. Block disposable email domains.*


# 5. OAuth & Native Login Confusion

## 📌 The Attack:

Apps that support both Google login and email/password signup can mishandle account linking:

- Attacker signs up with `user@example.com` using a password
- Victim later logs in using Google
- The app either creates a **duplicate account** or links to the attacker’s

## 🧠 Real Case:

Several mobile apps were found by researchers to mishandle account linking, allowing attackers to “steal” OAuth logins when users tried to authenticate via Google or Facebook.

*✅ Takeaway: Always verify that OAuth logins are linked to verified and owned accounts. Treat identity providers as authoritative.*


# 👨💻 Who’s Affected?

Pre-account takeover isn’t limited to one industry. Any app that allows account creation *without strict identity verification* is vulnerable. Here’s how different sectors can get burned:

## **🧩 SaaS Platforms**

**Scenario:** An attacker signs up with `ceo@company.com` on a project tool. When the real CEO joins, they inherit a compromised account.

**Fix:** Require verified emails before granting access.

**Real Case:** Collaboration tools like Slack have seen similar shadow account issues via invite links.

## 🛍️ E-Commerce Sites

**Scenario:** Attackers hijack guest session tokens tied to carts and payment info before users create accounts.

**Fix:** Invalidate unauthenticated sessions at login.

**Real Case:** A top retailer patched this after a bug bounty report exposed token reuse vulnerabilities.

## 💸 Fintech & Banking Apps

**Scenario:** Attackers pre-create accounts using real emails. Victims later get locked out or inherit malicious profiles.

**Fix:** Enforce KYC and verified email before account creation.

**Real Case:** A crypto wallet provider faced mass impersonations and theft via pre-registered emails.

## 🕵️ VPNs & Subscriptions

**Scenario:** Attackers use disposable emails to farm free trials, costing millions in abuse.

**Fix:** Block temp emails, enforce verification pre-trial.

**Real Case:** A VPN lost over $2M from fake, unverified accounts.

## 💬 Social Networks

**Scenario:** Attackers create fake profiles using real emails before the actual users join.

**Fix:** Lock messaging/features until email is confirmed.

**Real Case:** Platforms like Instagram and LinkedIn constantly battle impersonation via early signups.

# 🔐 How to Prevent Pre-Account Takeovers(Mitigation)

## ✅ For Developers

- **Require strict email/phone verification before full access**
- **Expire password reset and verification links quickly**
- **Sanitize and verify all OAuth logins**
- **Don’t let session tokens persist between unauthenticated and authenticated states**
- **Block disposable/temporary email domains**
- **Rate-limit account creation per IP/device**
- **Monitor for typosquatted emails and suspicious patterns**

## 👤 For Users

- Sign up early for services you intend to use (beat the attackers)
- Use strong, unique passwords and 2FA wherever possible
- Watch for verification or password reset emails you didn’t request
- Use email aliases to track usage and spot impersonation

## Key Takeaway

If your app lets users:

- Sign up without verifying their email or phone
- Log in via OAuth without proper account linking
- Use features before proving ownership of identity

…then you’re opening the door to **pre-account hijacking**, impersonation, fraud, or abuse.

[Hacker4help](https://medium.com/u/e33c6c1bd4ed?source=post_page---user_mention--25eb518b34f1---------------------------------------) [Amish Patel](https://medium.com/u/49f68f75c58?source=post_page---user_mention--25eb518b34f1---------------------------------------) [Rey Patel](https://medium.com/u/87ba6554136e?source=post_page---user_mention--25eb518b34f1---------------------------------------)

**Tags:** #Cybersecurity #DataLeaks #InfoSec #BugBounty #DevOpsSecurity

**🙌 Special Thanks:** Big thanks to **@Hacker4Help** — always dropping 🔥 insights and tools to level up your security game. A must-follow for anyone in InfoSec!
