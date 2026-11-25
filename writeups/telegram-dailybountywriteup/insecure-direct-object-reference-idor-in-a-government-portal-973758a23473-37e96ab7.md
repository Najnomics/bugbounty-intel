# Insecure Direct Object Reference (IDOR) in a Government Portal

- **Source URL:** https://akashxak.medium.com/insecure-direct-object-reference-idor-in-a-government-portal-973758a23473?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250424180933/https://akashxak.medium.com/insecure-direct-object-reference-idor-in-a-government-portal-973758a23473?source=rss------bug_bounty-5
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/9449 (id 9449)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Insecure Direct Object Reference (IDOR) in a Government Portal

# Introduction

While exploring a government web application, I stumbled upon a critical vulnerability—an **IDOR (Insecure Direct Object Reference)** that allowed access to sensitive user information just by modifying a parameter in an API request.

In this post, I’ll walk you through the methodology, demonstrate how the issue was found, and share how I responsibly disclosed the vulnerability

This write-up is for educational purposes only and does not contain any sensitive or personally identifiable information (PII).


# The Vulnerability: What is IDOR?

**IDOR** is a common security issue where an attacker can access objects (like user profiles or files) by modifying the input value in requests (e.g., user\_id=123).

It usually happens when access control checks are missing or improperly implemented.

# Steps to Reproduce

1. **Login** to theplatform with a test account.
2. Open **burpsuite** for analysing the requests and responses.
3. **Capture this request**:

POST /sso\_api/app/api/api\_results.php

Payload: case=getprofile&user\_id=3000&app\_id=4


4**. Modify the user\_id** to 1(admin), and 3001,3002.. (other user account)

5. **Observe** the response showing other users’ data (including potential admin/staff).

# Why This Matters

- This issue allows enumeration of **any user’s profile** without authentication or authorization.
- In some responses, administrative or staff-level details has been revealed.
- A malicious actor could exploit this.

# Takeaways

- Always validate user input on the **server-side**.
- Don’t rely solely on client-side restrictions.
- Apply proper **access control** to every API endpoint.
- IDOR is simple, yet dangerous — test your APIs thoroughly.

And ofcourse, responsibly disclosed this vulnerability to cert-In with the a remediation measures.

Thanks for reading! 

*If you found this helpful, feel free to share or connect with me.*

***Linkedin***:

[https://www.linkedin.com/in/akashxak/](https://web.archive.org/web/20250424180933/https://www.linkedin.com/in/akashxak/)
