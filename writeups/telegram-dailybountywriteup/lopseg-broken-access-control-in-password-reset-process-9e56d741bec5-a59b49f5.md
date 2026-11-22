# Broken Access Control in Password Reset Process

- **Source URL:** https://medium.com/@lopseg/broken-access-control-in-password-reset-process-9e56d741bec5?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20230410235941/https://medium.com/@lopseg/broken-access-control-in-password-reset-process-9e56d741bec5
- **Fetched:** 2026-11-22
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/2266 (id 2266)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Broken Access Control in Password Reset Process

This write-up seeks to describe a vulnerability that I encountered years ago, I hope you enjoy reading it.

While testing the password reset process of a web application, I discovered a Broken Access Control issue that allowed me to change the password of any user account.

Here’s how it works:

When a user requests a password reset link, an email is sent to their registered email address with a link to reset the password. Upon clicking the link, the user is redirected to a page where they can set a new password.

However, the email address used to send the reset link is user-controlled, which means that an attacker can change the email address to a different user’s email address and reset their password instead. This is due to a lack of proper access control in the password reset process.

To demonstrate this vulnerability, I changed the email address in the password reset form to my second account’s email address, and was able to successfully change the password for that account, even though I was logged in with my first account.

With this exploit, an attacker could repeat this process multiple times to change passwords for any user account on the website. This could lead to serious consequences, including unauthorized access to sensitive information and data breaches.

As a responsible security researcher, I reported this vulnerability to the website’s security team, who promptly fixed the issue and rewarded me with a generous bounty.

This incident highlights the importance of thorough security testing and the need for proper access controls to prevent unauthorized access to user accounts. As a website owner, it is essential to prioritize security and invest in regular security testing to identify and fix vulnerabilities before they can be exploited by attackers.

In conclusion, as a bug bounty hunter, I encourage fellow researchers to report any vulnerabilities they discover to the appropriate authorities and practice responsible disclosure. As a website owner, I urge you to prioritize security and take proactive measures to protect your users’ sensitive information.
