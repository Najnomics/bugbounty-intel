# Insecure Direct Object Reference (IDOR) Walkthrough — VulnLab by Yavuzlar

- **Source URL:** https://medium.com/@muhammadriva/insecure-direct-object-reference-idor-walkthrough-vulnlab-by-yavuzlar-3d16ce3f5345?source=rss------bug_bounty-5
- **Fetched from:** https://medium.com/feed/@muhammadriva
- **Fetched:** 2026-11-19
- **Channel:** @dailybountywriteup
- **Telegram message:**  (id 6496)
- **Method:** medium-rss-content readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
### Insecure Direct Object Reference (IDOR) Walkthrough — VulnLab by Yavuzlar

Insecure Direct Object Reference (IDOR) is a vulnerability where a user can access and manipulate resources directly via an identifier (such as a database key or filename) without proper authorization checks. This means attackers can exploit IDOR to access sensitive information or perform actions they’re not allowed to.

The impact of IDOR can be significant. It allows unauthorized access to data or functionality that should be restricted, leading to breaches of privacy, data theft, or even unauthorized modifications. For example, an attacker might change a URL parameter to access another user’s private information, such as financial records or personal details.

Organizations must implement robust access controls and validate user permissions on both the client and server sides to mitigate IDOR vulnerabilities. Regular security testing and awareness among developers are crucial to prevent such exploits and safeguard sensitive data from unauthorized access.

### 1. Invoices

Gain unauthorized access to other users invoices.

Look at the parameter that indicates the unique ID of each invoice. We can modify this ID to view information from other customers.

### 2. Ticket Sales

The purchase price for 1 ticket is $10, but we can manipulate this price using Burpsuite.

### 3. Changing Password

Changing someone else’s password using an account we control, as shown in the picture, can be intercepted using BurpSuite by altering the ID to access another account.

Those are some learning examples I can provide, but moving forward, I will continue to create content like this with scenarios and their exploitation methods as learning materials for beginners.

Thank You
