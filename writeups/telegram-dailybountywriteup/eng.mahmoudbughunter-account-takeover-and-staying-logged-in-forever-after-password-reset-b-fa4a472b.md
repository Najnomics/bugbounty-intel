# Account Takeover And Staying Logged In Forever After Password Reset

- **Source URL:** https://medium.com/@eng.mahmoudbughunter/account-takeover-and-staying-logged-in-forever-after-password-reset-b0ed4b65ac22?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20251014195120/https://medium.com/@eng.mahmoudbughunter/account-takeover-and-staying-logged-in-forever-after-password-reset-b0ed4b65ac22
- **Fetched:** 2026-11-19
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/11266 (id 11266)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Account Takeover And Staying Logged In Forever After Password Reset

### الحمد لله والصلاة والسلام على رسول الله وعلى آله وصحبه أما بعد

**I’m Mahmoud Farag — a security researcher and bug hunter on YesWeHack.**

### TL;DR

During an authorized test I discovered the system allows account creation without email verification and issues access\_token and refresh\_token at signup. If the real account owner later signs in with Google or changes/resets their password, the old tokens the attacker obtained remain valid — enabling persistent access. All sensitive data in this post is redacted.

### Scenario

- I can register any email on the platform because the system does not require email verification during signup.
- If the legitimate account owner later signs in using Google, this does not prevent the attacker — who created the unverified account — from maintaining control over the same account.
- When the real account owner uses the Reset Password flow and changes their password, the attacker still retains the refresh\_token obtained during signup. This token is not revoked or expired as a result of the password change.
- The attacker can, at any later time, use the stored token to generate new access tokens and regain full access to the account — allowing actions such as viewing PII or changing account settings.

### Impact

- Critical Account Takeover: Changing the password does not terminate stolen tokens; the attacker retains account control even after the victim performs recovery steps.
- High — Data & Financial Exposure: Potential access to user-sensitive data, subscriptions, and billing information.
- High — Fraud & Abuse: The attacker can carry out actions as the victim or misuse paid features.
- Medium — Reputational / Operational: Incident response burden, user notifications, and regulatory obligations.

### Technical Reasons

1\. Refresh tokens issued to unverified accounts (email\_verified: false).

2. No mechanism to revoke/invalidate tokens on password reset/change.

3. No refresh-token rotation or reuse detection.

4. Lack of email canonicalization/normalization (e.g., Gmail aliases / dot-variants), allowing creation of logically-duplicate accounts.

### PoC

1\. Created an account using an email variation that logically maps to the victim’s mailbox (alias). The system created the account without verification and issued tokens.

2. Saved the issued refresh\_token.

3. Later, the victim used “Forgot Password” and successfully changed their password.

4. After the password change, used the saved refresh\_token and observed the system returned a new access\_token — demonstrating the original refresh token was not revoked.

- Result: I was able to access the account and perform actions even though the victim had changed their password.
