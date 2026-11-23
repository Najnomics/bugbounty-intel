# How I Bypass 2FA through confirmation link..

- **Source URL:** https://medium.com/write-a-catalyst/how-i-bypass-2fa-through-confirmation-link-5bfdd773057a?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250905093925/https://medium.com/write-a-catalyst/how-i-bypass-2fa-through-confirmation-link-5bfdd773057a
- **Fetched:** 2026-11-23
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/10197 (id 10197)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
Member-only story

🎉How I Bypass 2FA through confirmation link..

🫡helo guys, I am Aftab aka security researcher and bug hunter from india🇮🇳…

🚴in this article, I’ll share a real-world vulnerability I discovered during my bug bounty research on a website that allowed me to bypass 2FA completely, all thanks to the confirmation link sent to my email.

🧐The setup: — -

one day I Create a Account on website https://target.com , I was sent a email containing confirmation link to verify my email address. then I decided to enable 2fa mechanism. most website don’t give permission to add 2fa mechanism before verifying account. once i successfully enable 2fa and logout and try to re-login it ask 2fa code that not the problem, the real problem ask me please click me means ( confirmation Link) when I click confirmation link I login without enter the 2fa code…

STEPS TO REPRODUCE:-

Step 1: I created an account and received the confirmation link in my Gmail inbox.

Step 2: I enabled 2FA before confirming the account with the help confirmation link.

Step 3: After logged out, I attempted to log in again — It ask 2FA code.

Step 4: I clicked the confirmation link from the email.

Step 5: Instead of confirming the email, the link logged me in without asking for the 2FA code, bypassing the authentication process entirely.
