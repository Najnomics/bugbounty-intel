# Bypassing 2FA Authentication in TeamPass System

- **Source URL:** https://medium.com/@developer_1991/bypassing-2fa-authentication-in-teampass-system-f3184fe8589d?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20240105165108/https://medium.com/@developer_1991/bypassing-2fa-authentication-in-teampass-system-f3184fe8589d
- **Fetched:** 2026-11-27
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/4623 (id 4623)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Bypassing 2FA Authentication in TeamPass 3.0.10 System

--

**Introduction:**

I am HamidReza Faghani, a penetration testing expert in the field of security testing. In this report, I have discovered a security vulnerability in this web ([TeamPass](https://teampass.net/)) system that allows malicious actors to bypass two-factor authentication (2FA). In this scenario, an attacker could obtain login credentials from other means and exploit this vulnerability to bypass 2FA. [GitHub](https://github.com/nilsteampassnet/TeamPass) address of this [TeamPass](https://teampass.net/) project.

**Vulnerability Details:**

This vulnerability is related to the two-step authentication process in the system. When users log in with limited permissions and an administrator account, a two-factor authentication mechanism (such as a one-time password sent via email) is used. This vulnerability allows an attacker to bypass 2FA and gain access to an administrator account. To implement this scenario, it is assumed that we have the credentials of two users (this can be obtained from social engineering techniques, brute force attacks or other known methods).

**Attack Scenario Description:**

To better understand this vulnerability, I will explain the attack scenario as follows:

1\. At the initial stage, two user accounts with different access levels are created: one with limited access and the other with administrative privileges.

2\. To capture traffic, we utilize the powerful tool Burp Suite. Using the account with limited access, we enter the login information and request the 2FA code. Then, we capture and save the sent request.

3\. Next, using the account with administrative privileges, we submit the 2FA code request. However, since we do not have access to the administrator’s or victim’s email, we need to bypass this step.

4\. During the 2FA code request, we replace the request body with the previously saved request body to impersonate the victim’s or administrator’s request. Consequently, the two-factor code is emailed to the user with lower access levels instead of the administrator. By exploiting this method, a hacker can bypass the 2FA verification and gain access to the administrator account.

\[1.\] Request

\[2.\] Response

5\. After replacing the request body with the user request body, we submit the 2FA code request. As we can see, the request for the 2FA code is being sent to the email of the regular user instead of the administrator.

6\. It can be seen that the two-factor authentication of the system has been bypassed using this method and gained access to the administrator panel.

— — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — —

I hope you enjoyed reading the writeup!

the tools that i used: Burp suit

linkedin : [https://ir.linkedin.com/in/hamidreza-nemesis-ab70108b](https://ir.linkedin.com/in/hamidreza-nemesis-ab70108b)

Instagram : [https://www.instagram.com/developer\_1991/](https://www.instagram.com/developer_1991/)
