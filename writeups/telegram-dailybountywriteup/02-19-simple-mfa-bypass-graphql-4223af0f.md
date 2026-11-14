# $600 Simple MFA Bypass – Graphql - Security Cipher

- **Source URL:** https://securitycipher.com/2024/02/19/simple-mfa-bypass-graphql
- **Fetched:** 2026-11-14
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/5341 (id 5341)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
Welcome to my blog! In this post, I'll delve into my recent security testing adventure focusing on multi-factor authentication (MFA) implementation in an application. As a [Product Security Engineer](https://linkedin.com/in/piyush-kumawat), I'm always on the lookout for vulnerabilities, including those related to GraphQL. I'll share my experience of attempting to bypass MFA and how I stumbled upon accessing post-authenticated data without going through the MFA process. If you're keen on learning about MFA security and potential vulnerabilities, stay tuned for the insights I'll be sharing.

Testing Methodology - 2FA Bypass: [https://securitycipher.com/docs/2fa-bypass/](https://securitycipher.com/docs/2fa-bypass/)

Testing Methodology - Captcha Bypass : [https://securitycipher.com/docs/captcha-bypass/](https://securitycipher.com/docs/captcha-bypass/)

Testing Methodology - Graphql : [https://securitycipher.com/docs/graphql-inprogress/](https://securitycipher.com/docs/graphql-inprogress/)


After setting up [Multi-Factor Authentication (MFA)](https://securitycipher.com/docs/2fa-bypass/), we usually expect an extra layer of security to access our apps. But, in this case, I discovered something intriguing. Despite the MFA setup, I found a way to access certain app features without entering MFA details.

## **What did I do?**

Well, I managed to tweak my email, and username without completing the MFA process. I even added card details, bank info, and updated user details with a mobile number, all without MFA hassles.

So, I decided to put MFA to the test. I ran through a series of security tests, focusing on MFA implementation. But every time I tried to access a restricted API, I got hit with an "unauthorized" error. Frustrating, right?

## **Then it dawned on me**

The app wasn't just using traditional API endpoints; it was also using GraphQL for some functions. Lightbulb moment! So, I logged into the app (MFA already set up) and waited for the MFA prompt.

Meanwhile, I whipped out the **InQL scanner** plugin to dig into the GraphQL queries. Lo and behold, using one of those queries, I was able to view and edit data without completing the MFA process.

Burp Suite POC

Burp Suite POC

Screenshot showing the Payment Flow

## **What's the deal?**

It turns out the app had set up session tokens specifically for GraphQL API, bypassing the usual MFA checks. This revelation allowed me to access sensitive user information (PII) and tweak some parameters, illustrating the potential impact of this oversight.

Money 😀

At long last, they acknowledged the bug, and I received a bounty along with a bonus for my discovery.

Bug Bounty

*Looking for Penetration testing services? https://securitycipher.com/services*

**Follow me on:**

Twitter: [https://twitter.com/piyush\_supiy](https://twitter.com/piyush_supiy)

Linkedin: [https://linkedin.com/in/piyush-kumawat](https://linkedin.com/in/piyush-kumawat)

Medium: [https://securitycipher.medium.com](https://securitycipher.medium.com)

Telegram: [https://t.me/securecipher](https://t.me/securecipher)


*Guide for Penetration Testing -  https://play.google.com/store/apps/details?id=com.securitycipher.penetrationtesting&hl=en-IN*
