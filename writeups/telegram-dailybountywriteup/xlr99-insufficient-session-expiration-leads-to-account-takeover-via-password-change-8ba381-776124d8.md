# Insufficient Session Expiration leads to Account Takeover via Password Change

- **Source URL:** https://medium.com/@xlr99/insufficient-session-expiration-leads-to-account-takeover-via-password-change-8ba38191df52
- **Fetched from:** https://web.archive.org/web/20261111075314/https://medium.com/@xlr99/insufficient-session-expiration-leads-to-account-takeover-via-password-change-8ba38191df52
- **Fetched:** 2026-11-19
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14957 (id 14957)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Insufficient Session Expiration leads to Account Takeover via Password Change

Howdy fellers! During my recent bug hunting in VDP programs, I was analyzing a presentation platform and came across a vulnerability. At first glance, it seemed like an ordinary issue that might easily be classified as low or P4. However, once you fully understand the impact, the true danger becomes clear. In this write-up, I am going to share a session management vulnerability and show how a simple mistake in the back-end code can expose users’ accounts to complete takeover.

### Vulnerability Analysis and Discovery Method

While searching for access control vulnerabilities on the platform, I found that on the user profile page, I could modify user data. I tried changing the account name using a token from another account, like “auth\_token=abk193”, and it successfully changed the victim’s account name. Up to this point, everything was working.

I decided to analyze this token to see what it exactly consisted of. I tried to decode it to see if it stored user information that I could exploit via IDOR or something similar. After decoding it, I found that it stored user data like ID, username, and email. Unfortunately, I noticed that a part of the token was encrypted, so I couldn’t just decode it, modify the user\_id, re-encode it, and use it.

So, I decided to test “Session management vulnerabilities”. I went back to changing the account name, but this time, I kept the token I used, logged out of the account, and logged back in. I tried to change the account name again, but instead of using the new active token, I replaced it with the old token I used before logging out. When I tried it, it worked and changed the account name! I realized this was an “Insufficient Session Expiration vulnerability”.

However, if I reported it in this state, it would likely be classified as an “Informative” So, I decided to try the same method, but this time on the account password change feature. I noticed the platform didn’t have any security measures like 2FA for changing the password. I repeated the same process on the password change endpoint, and when I tried using an old token after logging out, it changed the account password using the old token!

I realized this was a very dangerous vulnerability. It means an attacker could take over any account on the platform just by having an old token of the victim. The attacker could log into their own account, prepare a password change request, replace their token with the victim’s old token, and permanently take over the account. What makes this even more dangerous is that the token doesn’t have a clear expiration date. From my testing, the token remained valid for more than 24 hours!

## Get xlr9’s stories in your inbox

Join Medium for free to get updates from this writer.

Because of this, the severity of the vulnerability increased significantly, turning into “Insufficient Session Expiration leads to Account Takeover”, making it around High / P2. I wrote a report and submitted the vulnerability, but unfortunately, they replied and told me it was a duplicate.

### Impact of the Vulnerability

The impact of this vulnerability is highly critical due to a combination of two dangerous factors. First, the user’s session token never truly expires. Second, the password change feature lacks any security protections. To change the password, the system only asks for the new password and a confirmation field there is no requirement to enter the old password, and there is no 2FA or OTP verification. Because of this, it is very easy for an attacker who has an old token to log into their own account, use the stolen token in the password change request, and successfully change the victim’s password. This leads to a permanent account takeover, even if the victim clicks “Logout”, because the server still considers the old token valid. As for how an attacker could get this old token, there are many realistic ways, such as through XSS vulnerabilities. Furthermore, if an attacker manages to access the victim’s account just once on a compromised device, they can easily grab the token and use it whenever they want to completely take over the account.

### How to fix the Vulnerability

\- When a user changes their password, the server should immediately invalidate all active sessions associated with that user account, except the current one.

\- When a user clicks “Logout”, the server must not only delete the token from the browser but also invalidate or blacklist it on the server side. This ensures that even if an attacker has the old token, it will no longer work.

\- Session tokens should have a reasonable expiration time. A token that stays valid for 24 hours or more without any rotation is dangerous. Developers should set a short lifetime for tokens and require users to re-authenticate after that period.

\- Implement an additional layer of verification (such as 2FA or email OTP) before executing critical actions like changing the password or email address. This ensures that even if a session token is stolen, the attacker cannot complete the Account Takeover without access to the user’s email or 2FA device.

**Thank you for your time.**
