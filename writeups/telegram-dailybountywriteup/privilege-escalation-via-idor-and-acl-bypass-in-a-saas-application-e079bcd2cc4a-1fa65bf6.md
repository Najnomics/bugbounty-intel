# Privilege Escalation via IDOR and ACL Bypass in a SaaS Application

- **Source URL:** https://kumarmohank889.medium.com/privilege-escalation-via-idor-and-acl-bypass-in-a-saas-application-e079bcd2cc4a?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250428204812/https://kumarmohank889.medium.com/privilege-escalation-via-idor-and-acl-bypass-in-a-saas-application-e079bcd2cc4a?source=rss------bug_bounty-5
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/9476 (id 9476)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Privilege Escalation via IDOR and ACL Bypass in a SaaS Application

Hello! This is a short writeup explaining how I was able to **chain an IDOR vulnerability with an ACL (Access Control List) bypass** while hunting on a SaaS platform that implements extensive **Role-Based Access Controls (RBAC)**.

[Click here to read the writeup for free](https://web.archive.org/web/20250428204812/https://kumarmohank889.medium.com/privilege-escalation-via-idor-and-acl-bypass-in-a-saas-application-e079bcd2cc4a?sk=848c799fa02a5695a5fa3481dfe3cb0f)

# Understanding ACLs in Web Applications (with Network-Based Restrictions)

In many web applications, ACLs are used to **restrict user access** based on their **network location** — for example, allowing access **only from a corporate VPN or internal IP range**.

# How it works:

- The web application checks the **source IP address** of incoming requests
- If the IP falls within an **allowed range** (like a company VPN or intranet), **access is granted**.
- Requests originating **outside** the allowed network are **denied**.

# Common Configurations:

- **Allow List:** Only specific IP ranges are allowed to access the application.
- **Deny List:** Specific IPs or ranges are blocked from accessing the application.

# Understanding the Target Application

**Roles and Permissions:**

- **Administrator:** Highest privilege user with full access and control.
- **Employee:** Mid-level privileged user; has full control over **“User”** accounts.
- **User:** Low-privilege user; minimal permissions, primarily for basic operations.

# Type of ACL Implemented

In the target application:

- An **Administrator** can configure **allow list-based ACLs** for **all users** or **specific users**.
- **Employees** can manage ACLs for **low-privileged “User”** accounts.
- However, **Employees are not allowed** to modify the ACLs configured for **their own account** (i.e., by the Admin).

# The Vulnerability: IDOR + ACL Bypass

# Scenario:

1. As an **Administrator**, I invited two new users:

- `user2` (with the **Employee** role)
- `user3` (with the **User** role)

2\. As per design:

- `user2` was allowed to **configure ACLs** for `user3`.
- `user2` **should not** be able to modify **his own ACL**.

# Exploitation:

- I logged in as **user2** and initiated editing the ACL configuration for **user3**.
- While inspecting the request, I noticed an **ID** parameter controlling which user’s ACL was being modified.
- **By changing the ID value** in the request from `user3`'s ID to `user2`'s own ID, I was able to **edit and remove ACL restrictions** applied to my own (user2’s) account.
- Thus, I successfully **bypassed the ACL restriction** by exploiting an **Insecure Direct Object Reference (IDOR)** vulnerability.

**Impact:** 

Privilege escalation: Employees could remove their network-based ACL restrictions.

Severity: Medium & Bounty Awarded : 100 USD

# If you found the write-up insightful, feel free to share it !

Thanks for reading, and see you soon for a new adventure.

*Contact : LinkedIn :* [https://www.linkedin.com/in/mohankumar007/](https://web.archive.org/web/20250428204812/https://www.linkedin.com/in/mohankumar007/)
