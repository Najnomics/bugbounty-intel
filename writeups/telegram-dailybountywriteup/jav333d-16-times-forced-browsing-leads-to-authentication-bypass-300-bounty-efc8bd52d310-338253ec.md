# 16 Times Forced Browsing Leads to Authentication bypass [ 300$ Bounty ]

- **Source URL:** https://medium.com/@jav333d/16-times-forced-browsing-leads-to-authentication-bypass-300-bounty-efc8bd52d310?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20240524183004/https://medium.com/@jav333d/16-times-forced-browsing-leads-to-authentication-bypass-300-bounty-efc8bd52d310
- **Fetched:** 2026-11-22
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/6106 (id 6106)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# 16 Times Forced Browsing Leads to Authentication bypass \[ 300$ Bounty \]

**Hello everyone, I’m Javeed Shaik. A bug bounty Hunter and Ethical Hacker**

# Story:-

While hunting on a public bug bounty program, I discovered an HTML injection vulnerability. However, it was categorized as P5 since authentication is required to access the profile. To enter the profile, one needs to input the code received via email

I have now decided to bypass the authentication process in order to upgrade my P5 HTML injection to a P4 😂.

**Vulnerability Details:**

Forced Browsing Vulnerability:Forced browsing allows an attacker to navigate directly to restricted or protected pages without providing the required verification code.By exploiting this vulnerability, an attacker can bypass the profile code verification step and gain unauthorized access to protected functionalities.

# Steps to Reproduce :-

1. Navigate to this url :- [https://example.com/account/profile](https://example.com/account/profile)
2. It will prompt for a code, To bypass this,. Utilize this endpoint and engage in forced browsing \[/sign-up/profile\]
3. we have to do this for **16 times** , then click **Alt + Left Arrow**
4. Authentication successfully bypassed, we have accessed the profile page without entering the code

# Reply from the Program:-

*Thanks for reading*
