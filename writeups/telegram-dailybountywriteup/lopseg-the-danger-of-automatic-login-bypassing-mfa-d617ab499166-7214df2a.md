# The Danger of Automatic Login

- **Source URL:** https://medium.com/@lopseg/the-danger-of-automatic-login-bypassing-mfa-d617ab499166?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20230507203409/https://medium.com/@lopseg/the-danger-of-automatic-login-bypassing-mfa-d617ab499166
- **Fetched:** 2026-11-27
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/2384 (id 2384)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# The Danger of Automatic Login: Bypassing MFA

--

A few years ago, during a security assessment, I found a vulnerability that allowed a user to bypass multi-factor authentication (MFA) through the password reset process. This vulnerability is caused by the application’s automatic login feature, which logs users in after they reset their password, bypassing the MFA requirement.

In this scenario, I assumed that the attacker had access to the victim’s password reset link and could reset their password. The problem arises when the app logs the user in automatically, without asking for the MFA code on the user’s phone, making it possible to bypass MFA.

MFA is designed to protect users from unauthorized access to their accounts, especially when an attacker has access to their login credentials. By requiring the MFA code, the application ensures that only authorized users can access the account, making it difficult for attackers to gain unauthorized access.

Unfortunately, the automatic login feature in the app bypasses this crucial security feature, leaving users vulnerable to attack.

I reported this vulnerability to the security team, and they responded promptly by disabling the automatic login feature and implementing proper MFA checks during the password reset process.

If you enjoyed my content, please consider supporting me by buying me a coffee at
