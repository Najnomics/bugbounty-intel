# 2FA Bypass via OAuth Account Migration

- **Source URL:** https://sudohunt.medium.com/2fa-bypass-via-oauth-account-migration-9722cdcc8b10
- **Fetched from:** https://sudohunt.medium.com/2fa-bypass-via-oauth-account-migration-9722cdcc8b10?source=rss-cac87d75628a------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:**  (id 14974)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** SudoHunt / Sat, 07 Nov 2026 16:14:34 GMT

Hey everyone! How you been?

Recently, I found an interesting 2FA bypass vulnerability in an external bug bounty program. The concept behind the bypass is simple, but it represents a classic logic flaw that developers easily overlook when implementing third-party authentication.

Let’s dive into the details!

around testing the application’s Two-Factor Authentication (2FA) implementation, every standard request worked as intended. Every classic bypass technique I tried failed — everything looked completely secure on the primary login flow. I decided to leave it for a bit and started testing other features.

Two days later, something clicked. I remembered that the web application offers a third-party login option (**“Sign in with \[APP\]”**).

This alternative authentication path lets users sign in using a third-party provider and merge or link their existing password-based account with that OAuth provider. Once logged in, a user can also unlink the OAuth provider in settings and revert to the standard email/password authentication model. This process is called **migration**.

POST /api/OAuth/migration HTTP/2

Host: target.com

Content-Type: application/json

{

"id": "1234",

"password": "password"

}

HTTP/2 200 OK

Content-Type: application/json

{

"message": "Migration completed successfully!",

"data": {

"token": "ey..."

}

}

**Vulnerability:** The backend server completes the migration process and immediately issues a fully authenticated session token without ever prompting for the 2FA TOTP code.

5\. While in this newly authenticated session, navigate to **Account Settings** and click **“Unlink OAuth account”**.

6\. Enter a new password when prompted to convert the account back to standard authentication. then go to **Security Settings** and disable 2FA using the newly set password.

**Result:** 2FA is completely stripped from the account without ever requiring verification or confirmation from the user’s registered 2FA authenticator device.

Multi-factor authentication is specifically designed to mitigate scenarios where primary factors (including email inbox access or leaked passwords) are compromised.

The app correctly enforces 2FA on the primary login flow email/password, but fails to enforce the same 2FA requirement on the alternative authentication path OAuth.

This report was marked as a **Duplicate**.

That’s the dark side of bug bounty not every report gets accepted, and not every valid finding gets rewarded. We all know the feeling — you invest time and effort into an app, find a flaw, get excited expecting a bounty, and then see the status to **Dup** or **Info**.

*It’s a part of the game. You either take it all or leave it all.*

**Thank you!**
