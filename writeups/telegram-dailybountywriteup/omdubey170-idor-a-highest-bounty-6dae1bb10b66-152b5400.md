# IDOR a Highest Bounty

- **Source URL:** https://medium.com/@omdubey170/idor-a-highest-bounty-6dae1bb10b66?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20251126143521/https://medium.com/@omdubey170/idor-a-highest-bounty-6dae1bb10b66
- **Fetched:** 2026-11-24
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/2437 (id 2437)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# IDOR a Highest Bounty

This is a Private Program so i can not revealed the name of the website so let’s take example.com

Insecure Direct Object References (IDOR Vulnerability) Insecure direct object references (IDOR) are a type of access control vulnerability that arises when an application uses user-supplied input to access objects directly. The term IDOR was popularized by its appearance in the OWASP 2007 Top Ten.

Proof of Concept

1. so i use google dorks for recon the website so is use the dork site:\*.example.com inurl:.aspx
2. so in the result the user data has been leaked and URL is like this [https://buy.example.com/protect/landing.aspx?**base64encoded**](https://buy.example.com/protect/landing.aspx?base64encoded=)**data**
3. this base64 encoded data is a user’s mobile number by which a user is validated so i change the mobile number to other user’s mobile number and the other user’s data has been leaked
4. i can not put screenshot because of company policies
5. this Vulnerability gives me 2000$ and the severity of this bug is P0
6. Google Dorks always gives different result

Follow me on Linkedin [https://www.linkedin.com/in/dubeyom/](https://www.linkedin.com/in/dubeyom/)

checkout my personal findings and contact me on telegram [https://t.me/+27aPEPMHR6w3Mjg1](https://t.me/+27aPEPMHR6w3Mjg1)

IMPACT

Unauthorized access to sensitive data — Object references often include database IDs, which attackers can access to expose sensitive information about the application/users. The unauthorized user can also use database entries to prepare malicious SQL payloads for further attacks. Object manipulation — With access to internal references, attackers gain direct access to the data and state of the application. Attackers can then manipulate the exposed objects to modify data, access hidden functions, or further escalate privileges. Direct file access — Malicious users can combine IDOR attacks with directory transversal attack techniques to manipulate the host’s file system. This grants them the ability to upload/download files freely and manipulate content accessed by other users.

MITIGATION

The most foolproof way to prevent IDOR vulnerabilities and attacks is to perform access validation. If an attacker tries to tamper with an application or database by modifying the given reference, the system should be able to shut down the request, verifying that the user does not have the proper credentials.
