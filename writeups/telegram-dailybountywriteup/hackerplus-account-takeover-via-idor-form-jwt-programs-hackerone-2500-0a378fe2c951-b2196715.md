# Account Takeover via IDOR form JWT Programs HackerOne 2500$

- **Source URL:** https://medium.com/@HackerPlus/account-takeover-via-idor-form-jwt-programs-hackerone-2500-0a378fe2c951?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250317110440/https://medium.com/@HackerPlus/account-takeover-via-idor-form-jwt-programs-hackerone-2500-0a378fe2c951?source=rss------bug_bounty-5
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/8510 (id 8510)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Account Takeover via IDOR form JWT Programs HackerOne 2500$

Welcome to **HackerPlus**! 🌐💻

We specialize in **pentesting** and **Bug Bounty** to enhance the security of web applications. We share reports on past vulnerabilities and spread knowledge to help the cybersecurity community grow.

**HackerPlus — Together, we make the digital world safer.** 🛡️

Now we will talk about the Insecure Direct Object Reference (IDOR) report via [https://target](https://web.archive.org/web/20250317110440/https://target/) .com which led to the Account Takeover.

#Summary of the IDOR vulnerability via target.com

Insecure Direct Object Reference (IDOR) vulnerability means that a system allows access to data or changes to other accounts simply by knowing the user\_id or other values.

In this case, we found that the application relies on the user\_id stored within a JWT (JSON Web Token) to change account data, such as the display name.

#How does the vulnerability work?

When a user requests to change the display name, a request is sent containing session information along with a JWT that includes the user identifier (user\_id).

When the request is manually modified to change the user\_id to another user identifier, the attacker can modify the data of the other user.

If the request is accepted, the system responds with 200 OK, meaning that the change was successful.

#Request and Response Analysis

A name change request was submitted, containing the following data:

Session Token: Contains the JWT.

user\_id: The user ID of the account.

After testing:

Successful response (200 OK): If the information is correct and the change is accepted Failed response (401 Unauthorized): If the information is incorrect or the user is not authorized.

#Request Tampering Test

The request was manually modified to change the value of user\_id to another user ID (inferred from encryption or guessing).

When the request was sent again, the change was accepted and a response of 200 OK was returned, meaning that the system implemented the change on the other user’s account.

\# JWT Analysis

When the JWT was decrypted, information such as:

uid: user\_id.

tz: timestamp.

t: timestamp.

This information was directly tied to the user\_id, meaning that anyone who could modify the JWT or extract another user’s ID could exploit this vulnerability.

JWT Token :

`{``"_permanent": true,``"uid": "01946fa0-xxxxxx-04f8-0000-xxxxxxxxx",``"st": 3,``"t": 173700000,``"tz": "Africa"``}`
If you notice the request I mentioned and this token after decrypting it, you will notice something similar here.

“user\_id”:”User:01946fa0-xxxxxx-04f8–0000-xxxxxxxxx"

JWT

“uid”: “01946fa0-xxxxxx-04f8–0000-xxxxxxxxx”

I definitely understood that inside the session there is a JWT after encryption it is in user\_id”:”User:01946fa0-xxxxxx-04f8–0000-xxxxxxxxx which is outside in front of you in the request

If you can access User:01946fa0-xxxxxx-04f8–0000-xxxxxxxxx like this for a user account you will be able to change the name of his account indeed.

#Vulnerability Check

It has been proven that if user\_id is modified within the request or JWT, an attacker can:

Access other users’ accounts.

Change their data (such as display name).

#Proving the vulnerability with tools

A tool can be written using a library like jsonwebtoken (in Node.js) to generate a modified JWT containing another user’s id. When this modified token is sent in the request, changes can be made to other accounts.

Programs : HackerOne

Bounty : 2500$

We hope you benefited

Team HackerPlus+
