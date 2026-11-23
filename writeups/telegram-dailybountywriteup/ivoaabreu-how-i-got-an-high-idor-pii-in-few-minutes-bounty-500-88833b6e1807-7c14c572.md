# How I got an High IDOR + PII in few minutes. Bounty

- **Source URL:** https://medium.com/@ivoaabreu/how-i-got-an-high-idor-pii-in-few-minutes-bounty-500-88833b6e1807?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20240526091945/https://medium.com/@ivoaabreu/how-i-got-an-high-idor-pii-in-few-minutes-bounty-500-88833b6e1807
- **Fetched:** 2026-11-23
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/6164 (id 6164)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Introduction

Hello folks! I’m Ivo Abreu, I’ve been studying for almost 2 years and doing bug bounty in my spare time and learning daily with the bug hunters community. This is my first writeup, I hope you like it.

Today I’m going to share with you how I got an IDOR in just a short time in a Bug Bounty program. Let’s get started!

# What is IDOR?

The IDOR (Insecure Direct Object Reference) flaw is a security vulnerability in web applications that arises when the application allows direct access to internal objects, such as files or database records, without carrying out proper permissions checks. This allows a malicious user to manipulate the references to these objects in order to access data that they shouldn’t have access to.

# Steps until the bug

The start to exploit the the IDOR began after I received a private invitation on Intigriti on a program with multiple domains with authentication. I selected one, let’s consider the domain to be **redacted.com**

After noticing that the application had authentication. I had the idea to test IDOR.

*After create my account I follow this steps:*

- Logged in to the application , I used the burp history to analyse the login requests.
- After going through some requests, one caught my attention, like this: **GET /connectif/tags/ajaxconnectiftags?\_=id HTTP/2** and after see the response, I notice that response included exposure of **PII** (*Personally Identifiable Information*) that includes data that could potentially identify a specific individual.
- After this interesting scenario involving some private information of the user. I thought, if I put another id, I will be able to read data from another user? Let’s try!
- I created another account representing the victim, I logged to the application and captured the same request and I sent it to the repeater, changing the attacker’s ID to the ID of the account representing the victim ***and with a little of luck …***

The IDOR happened exposing user PII such as **email, address, city, name, telephone and number.**

**Curiosity about this bug:** The ID was dynamic, every time a user logged into the application a new id was generated, and half of the id number was a static value, that is, it was a default value, so it was possible to discover that the request was vulnerable too to brute force. With this information, users who were logged into the application could be affected by the IDOR.

# Impact

The impact of Insecure Direct Object References (IDOR) can allow the reading of other users’ personal data can be significant and detrimental to the security of a system.

**Exposure of PII Privacy Violation:** Unauthorized disclosure of PII can result in serious privacy violations. When personal information falls into the wrong hands, individuals can become victims of identity theft, harassment or other forms of exploitation.

**Identity Theft Risk:** Exposing PII significantly increases the risk of identity theft. This can lead to fraudulent activities such as opening bank accounts, applying for credit cards, or even more serious crimes using the victim’s identity.

**Damage to Reputation:** Companies that fail to adequately protect their customers’ PII can suffer significant reputational damage. Customer trust can be lost, resulting in a decrease in profits and market share.

**Bounty:** €500

**Severity:** High

**Tip:** Always check login requests, you might be surprised!

***One special thanks to*** @crd0x49 , I learned BAC/IDOR with this guy!

Follow him: [https://medium.com/@crd0x49](/@crd0x49)

# Timeline

Reported — 16/02/2024

Triaged — 16/02/2024

Bounty — 26/02/2024
