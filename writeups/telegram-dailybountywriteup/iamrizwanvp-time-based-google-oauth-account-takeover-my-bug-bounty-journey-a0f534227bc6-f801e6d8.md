# Time-Based Google OAuth Account Takeover

- **Source URL:** https://medium.com/@iamrizwanvp/time-based-google-oauth-account-takeover-my-bug-bounty-journey-a0f534227bc6?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20240531132218/https://medium.com/@iamrizwanvp/time-based-google-oauth-account-takeover-my-bug-bounty-journey-a0f534227bc6
- **Fetched:** 2026-11-23
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/6193 (id 6193)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Social Login OAuth State Flaw : Predictable token in a time stamp

**Peace be upon you**, everyone! I am Rizwanvp from India, a bug bounty hunter and security analyst.Let’s talk about an another interesting bug I found on a private bug bounty platform. I can’t share the domain because of the rules. Platforms like HackerOne and Bugcrowd are crowded, making it hard to find high-severity (P1) bugs. Often, only easy bugs are left, and they are frustrating because many programs don’t pay for them or consider them as just informative.

Background

Feeling demotivated by these easy bugs, I decided to try something different. I used Google dorking and found an interesting program. I wanted to find something significant, so I began my hunt.

The Hunt

I tried all the basic vulnerabilities and found some self-XSS and cross-domain policy issues, but I ignored them because I wanted to find P2 or P1 vulnerabilities. I spent a week digging deep into every part of the program, but it seemed pretty secure, and I started to lose hope. Still, I didn’t give up.

I began fuzzing directories using a mega list (I will provide the mega fuzz list link at the end), but still no luck. Just when I thought about giving up and moving on to the next program, something caught my attention.

**The Discovery**

The server had a secondary social login option via Google OAuth and Facebook. I checked for OAuth misconfigurations, but the state and redirect URIs were perfectly configured. However, I noticed something odd with the Google OAuth login. When I signed in with my first Google account, I noted the state code, then logged out and signed in with my second Google account. To my surprise, the state code was the same for both accounts. I thought, “Wait, what?!”

*Understanding the State Code*

For those who are confused, the OAuth state code is a parameter used to keep track of the client and server during the OAuth authentication process. It’s designed to prevent CSRF attacks by making sure the response received is in response to a request made by the same client.

**Validating the Vulnerability**

To confirm the vulnerability, I created another main account and signed in using the secondary login. The state value was indeed the same as my first account’s value. The server was issuing the same state code but i found that the state value is not same a time frame when that time end server generate next value for every user same code based on a time frame for all users same code. This means an attacker could perform a CSRF attack and take full control of a user’s account.

*Impact*

This vulnerability is severe (P2) because it allows an attacker to take over a user’s account through CSRF by exploiting the predictable state token.

Reporting and Response

I created a detailed report and proof of concept (PoC) and sent it via email to the team. They acknowledged receiving the report, and I am currently waiting for their response and the bounty. :)

*Motivation*

To my fellow bug bounty hunters, never lose hope. I’ve faced many rejections, sleepless nights, and moments where I almost quit. But remember, even if hope is only 1%, it still exists. Stick to that hope. Keep learning, keep hunting, and aim for those P1 and P2 vulnerabilities.

*Conclusion*

This experience taught me that perseverance is key in bug hunting. Even when things seem secure and there’s no hope, dig deeper. You never know when you’ll uncover something significant.

Happy hunting :)

*Resources:*

https://github.com/netsecurity-as/subfuz/blob/master/subdomain\_megalist.txt
