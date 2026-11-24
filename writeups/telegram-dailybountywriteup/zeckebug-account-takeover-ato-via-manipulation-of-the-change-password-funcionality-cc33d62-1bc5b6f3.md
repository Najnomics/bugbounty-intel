# Account Takeover (ATO) via Manipulation of the Change Password Funcionality

- **Source URL:** https://medium.com/@zeckebug/account-takeover-ato-via-manipulation-of-the-change-password-funcionality-cc33d6249cdf?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20251126142019/https://medium.com/@zeckebug/account-takeover-ato-via-manipulation-of-the-change-password-funcionality-cc33d6249cdf
- **Fetched:** 2026-11-24
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/3246 (id 3246)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# **Account Takeover (ATO) via Manipulation of the Change Password Funcionality**

My name is Ezequiel (aka Zecke) ethical hacker and bug bounty hunter from Argentina.


### **Introduction:**

In the realm of ethical hacking, uncovering security vulnerabilities is a vital step towards strengthening the defenses of organizations. In this article, I will shed light on a significant vulnerability discovered within a prominent company in the automobile and housing rental industry, referred to as ¨redacted.com¨. While I am unable to disclose the specific company’s name due to confidentiality reasons, I aim to provide educational insights into the vulnerability and the actions taken to address it.

This article serves as an educational resource, outlining the techniques utilized by ethical hackers during security assessments. By providing an in-depth explanation of the steps to reproduce the vulnerability, my goal is to share to new ethical hackers with valuable insights into the process.

### **Summary of Vulnerability:**

During a comprehensive security assessment conducted through the HackerOne platform, a critical vulnerability was identified in redacted.com’s password change functionality. This flaw allowed potential account takeovers by manipulating the server’s response during the password change process.

### **Steps to Reproduce:**

1. Create 2 accounts (Attacker: Phone Number=\*\*\*\*\*\*\*\*\*\*\***51** / Victim: Phone Number=\*\*\*\*\*\*\*\*\*\***59**)
2. Login to the application with a valid user account (Attacker Account).
3. Start the password change process.
4. Observe that the application prompts for the current password.
5. Intercept the server’s response during the password change process.

6\. Manipulate the status code and body of the response to indicate “successful” password change for the victim account.

7\. Submit the password change request.

8\. Verify that the password has been successfully changed for the victim account without requiring the current password.

*PS: I made a proof of concept (PoC) video of the full process (ATO), but unfortunately I can’t share it.*


### **Impact:**

This vulnerability poses a severe threat to the security of user accounts within the application. The consequences of this account takeover vulnerability may include, but are not limited to:

- Unauthorized access to the target user’s account and personal information.
- Potential exposure of sensitive data, such as financial details or private communications.
- Unauthorized actions and activities performed on behalf of the compromised account, leading to reputational damage for the user and the application.

### **Conclusion:**

The vulnerability in redacted.com’s password change process exposed a loophole that permitted unauthorized access to user accounts. By skillfully manipulating the server’s response, an attacker could bypass authentication, changing the password of a targeted user’s account without requiring the current password. The potential consequences of such an account takeover included unauthorized access to personal information, exposure of sensitive data, and reputational damage for both users and the company.

**Upon discovery of this vulnerability, I promptly reported it to redacted.com via the HackerOne platform. However, it is crucial to recognize that the company, at the time of writing, has not taken any remediation action in response to the report and the report was closed as “Informative”.**


Happy Hacking!
