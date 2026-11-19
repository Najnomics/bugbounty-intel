# ️Full Account Takeover Through Unsafe Google Linking With Permanent Loss of Access for the Victim

- **Source URL:** https://medium.com/@0xMo7areb/%EF%B8%8Ffull-account-takeover-through-unsafe-google-linking-with-permanent-loss-of-access-for-the-victim-abbfae81538a?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20260507170142/https://medium.com/@0xMo7areb/%EF%B8%8Ffull-account-takeover-through-unsafe-google-linking-with-permanent-loss-of-access-for-the-victim-abbfae81538a
- **Fetched:** 2026-11-19
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/13499 (id 13499)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# 🕸️Full Account Takeover Through Unsafe Google Linking With Permanent Loss of Access for the Victim

*الحمد لله الذي عَلَّمَ بالقلم.. عَلَّمَ الإنسانَ ما لم يَعْلَم والصلاةُ والسلامُ على خيرِ مُعَلِّمي الناسِ الخير محمد أما بعد*

## Let’s Dive into Today’s Bug

While testing an application’s authentication flow, I found an issue that could lead to **full account takeover** and eventually **lock the real user out of their account.**

The root cause was simple: the application allowed account registration with any email address without verifying ownership.

Later, when the real owner signed in using **Google OAuth**, the system automatically linked both identities based on the email match.

This created a dangerous scenario where an attacker could pre-register a victim’s email, wait for the victim to authenticate via Google, and then take control of the same account.

## How I Found It

I started by testing the authentication flow as a normal user, focusing on registration, login, and profile settings.

Two key issues stood out:

- **Account registration did not require email verification**
- **Email changes also did not require verification**

This raised a simple question:

**What happens if someone registers using a victim’s email and the victim later logs in with Google OAuth?**

That question led directly to the vulnerability.

## Proof of Concept

1. The attacker registers an account using **victim@email.com**
2. Later, the victim logs in using **Google OAuth** with the same email. The system automatically links both identities, while the victim is unaware that the account is already shared.
3. The attacker logs in using the original password and gains access (**password reset is still available at this stage**).
4. **To escalate to full account takeover and permanent lockout**, the attacker changes the account email to **Free@Palestine.com**
4.1**Password reset becomes unusable** since recovery is now tied to the new email.
4.2**Google OAuth linkage is updated to the new email**, showing a critical issue where identity binding depends on a mutable field **(this may also indicate a separate high-impact OAuth misconfiguration, included for severity context)**.
5. The attacker then changes the password, which **invalidates the victim’s active session** and fully secures control of the account.
6. After these changes, the original Google OAuth association is no longer consistent with the account state.
7. When the victim attempts to log in again using **Google OAuth**, the system cannot correctly map the identity.

At this point, **the attacker retains full control of the account while the legitimate user is permanently locked out.**

## Impact

This issue can lead to:

- Full account takeover
- Permanent user account lockout
- Broken Google OAuth login after email manipulation
- Unauthorized access to sensitive account data and settings
- No reliable recovery path for the legitimate user

## Root Cause

The application over-relied on the email address as the identity anchor.

Since emails are mutable, using them for account linking introduces a critical security weakness.

A safer approach is to rely on stable OAuth provider identifiers instead of email matching.

## Recommendation

To remediate this issue:

- Require email verification before activating accounts
- Avoid automatic account merging based only on email
- Use Google’s stable OAuth identifier (`sub`) for identity mapping
- Require verification for all email change operations
- Invalidate all active sessions after any identity-related change

## Takeaway

Small authentication flaws can compound quickly — when unverified account creation meets automatic Google OAuth linking, it can escalate into full account takeover and complete user lockout.

## Report Status

This report was marked as a **duplicate :)**

*Let’s Connect: x account || linkedin account*


D*on’t forget to follow me on this medium account :)*

*“سُبْحَانَكَ اللَّهُمَّ وَبِحَمْدِكَ ، أَشْهَدُ أَنْ لا إِلَهَ إِلا أَنْتَ ، أَسْتَغْفِرُكَ وَأَتُوبُ إِلَيْكَ”*
