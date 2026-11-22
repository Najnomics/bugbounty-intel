# Bypassing 2FA for Password Reset

- **Source URL:** https://infosecwriteups.com/bypassing-2fa-for-password-reset-by-request-manipulation-500-bug-3c6ed909322f?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20231118081745/https://infosecwriteups.com/bypassing-2fa-for-password-reset-by-request-manipulation-500-bug-3c6ed909322f
- **Fetched:** 2026-11-22
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/4200 (id 4200)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Bypassing 2FA for Password Reset *:* By Request Manipulation *500$ Bug*

--

*Explore a real-world account security threat — a 2FA bypass vulnerability. Learn how this flaw allows unauthorized access.*

Recently, I found a security flaw in Exam.me(virtual name of private program) that allowed an attacker to bypass Two-Factor Authentication (2FA) during the password reset process. This write-up takes into the specifics of the issue,steps to reproduce and its potential impact.

**Understanding the Vulnerability**


The security of an online account often relies on multiple layers of protection. One of these layers is 2FA, a process that demands two forms of verification before granting access to an account. This additional step is essential in preventing unauthorized access to an account, even if the password or email falls into the wrong hands.

However, the vulnerability in question highlighted a scenario where a potential attacker, having gained control of a user’s email account, could make critical password reset to the victim’s exam.me account without needing the 2FA verification code. This scenario is where the security concern lay.

**The Flaw**


The process of password reset and 2FA confirmation on exam.me follows a set pattern. After entering the verification code, the system redirects to a 2FA confirmation page. However, the vulnerability allowed the attacker to manipulate the request by intercepting it and removing the **“/code”** endpoint from the API request. By adding a **password** and **password\_confirmation** in the JSON parameters, an attacker could create a new password for the account without needing the 2FA verification code. In essence, they could reset the password without genuine authorization.

**Steps to Reproduce**


To reproduce this vulnerability, the following steps were taken:

1. Access Password Reset Page: Go to [https://exam.me/en/passwords/new](https://exam.me/en/passwords/new).
2. Enter OTP and Confirm: Enter the OTP received via email and click on the “Confirm” button. This will lead to the 2FA verification page.
3. Intercept the Request: Intercept the API request sent when confirming the code verification, specifically [https://exam.me/en/passwords/------------------------/code](https://exam.me/en/passwords/------------------------/code).
4. Modify Request: Remove the “/code” endpoint from the API request and add the **password** and **password\_confirmation** parameters in JSON format with the desired new password.

5\. Send the modified request.

6\. Observe that the new password is created without requiring the 2FA verification code.

**The Impact**


1. Unauthorized access to user accounts/account takeovers.
2. Bypassing the 2FA security layer.

The exploitation of this vulnerability can lead to a full account takeover by overriding exam.me’s security protocols. The implications are clear — unauthorized access and account takeovers.

**The Bounty Reward**


In recognition of the critical discovery and the responsible disclosure of this security flaw, a bounty of $500 was awarded tome. This bounty aligns with medium severity concerns and highlights the significance of the vulnerability’s impact.

It’s essential to note that the successful exploitation of this security issue hinges on a specific scenario — the attacker must have previously compromised the victim’s email address.

**Takeaway**


Remember, even the most complex systems have their weak points. By scrutinizing each step of a process, especially where sensitive data is involved, you can uncover vulnerabilities that others may overlook. Stay curious, stay diligent, and keep exploring.

*Leave some clap if you enjoyed this read, leave your feedback in comment and consider following me for more exciting findings.*


*Find me on Twitter: @a13h1\_*


# Thank you everyone

Keep Supporting, Keep Clapping, Keep Commenting.
