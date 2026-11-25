# Zero Click Account Takeover — JWT Token Manipulation via Programs HackerOne

- **Source URL:** https://medium.com/@HackerPlus/zero-click-account-takeover-jwt-token-manipulation-via-programs-hackerone-07da3868ada9?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250118224107/https://medium.com/@HackerPlus/zero-click-account-takeover-jwt-token-manipulation-via-programs-hackerone-07da3868ada9?source=rss------bug_bounty-5
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/8525 (id 8525)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Zero Click Account Takeover — JWT Token Manipulation via Programs HackerOne

Welcome to **HackerPlus**! 🌐💻

We specialize in **pentesting** and **Bug Bounty** to enhance the security of web applications. We share reports on past vulnerabilities and spread knowledge to help the cybersecurity community grow.

**HackerPlus — Together, we make the digital world safer.** 🛡️

**HackerPlus+** team has decided to create an account on HackerOne to participate in discovering security vulnerabilities in real-world programs, aiming to **educate others and share knowledge** practically. Write-ups will be published to explain the types of discovered vulnerabilities and how to identify them, while strictly avoiding any disclosure of private program details. The primary goal is to **spread knowledge and support the security community effectively.**

Now we will talk about the Zero Click Account Takeover — JWT Token Manipulation via [https://target](https://web.archive.org/web/20250118224107/https://target/) .com

We have discovered critical vulnerability has been discovered in the application’s authentication system, where an attacker can exploit a user’s JWT token to swap or manipulate it in order to gain access to other users’ accounts. This vulnerability occurs because the server does not properly verify the token signature or verify the session associated with the token User.

# Steps to exploit the vulnerability:

1- Step 1: Log in to the first account using user (A) data, and receive his JWT Token from the response coming from the server.

2- Step 2: Log in to the second account using user (B) data, and receive his token.

3- Step 3: Switch tokens between accounts:

-Use the first user’s token to access the second user’s data. 

-Use the second user’s token to access the first user’s data.

4- Step 4: Notice that the server processes requests using the modified tokens as if they were issued by the correct accounts without any additional verification.

5- Send the modified request using the other token to the server, and the server will respond as if the request came from the correct user.

# #JWT Token Analysis

sub (Subject): 4385971

Purpose: Represents the user ID of the token holder. Importance: Links the token to a specific user in the system

# Summary JWT Tokne:

This JWT payload provides authentication and authorization details for a user in the system. Key attributes like e\*\*, n\*\*, and i\*\* define the token’s validity window, while account\_id and sub link it to specific user and account details. Additional fields like jti and typ ensure security and proper token classification.

# Summary Hacker

Meaning that after decrypting the jwt token, there is nothing that identifies the account other than sub. In other words, if you make a modification to the jwt token and change the sub number, you will log in to another user account. Let me understand you more and more clearly. Now I logged in to an account, which is account number 1, and the sub number was 15. I received the request and kept it. Then I went and logged in to account number 20 and received the request and asked to see the response before sending the request to the server. Then I took the jwt token. I made a modification and changed the sub number from 20 to 15 and sent the request. It will log me in to account number one. This is because the server does not sufficiently verify the token signature (JWT Signature) or its authenticity.

The Vulnerability has been sent to HackerOne.

Programs : HackerOne BBP

Vulnerability Extraction Time : 25 minutes

We Hope You Benefited

Follow us on X Platform : [https://x.com/HackerPllus](https://web.archive.org/web/20250118224107/https://x.com/HackerPllus)

Team HackerPlus+
