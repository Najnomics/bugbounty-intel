# Privilege Escalation

- **Source URL:** https://medium.com/@0298muneezabadar/privilege-escalation-from-user-to-admin-22befa6f1f9c?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250822041252/https://medium.com/@0298muneezabadar/privilege-escalation-from-user-to-admin-22befa6f1f9c
- **Fetched:** 2026-11-19
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/10371 (id 10371)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Privilege Escalation: From User to Admin.

In this post, I’ll share how a simple bug can lead to million-dollar loss. Have you ever wonder how it is possible? The reason behind this is a vulnerability called Privilege Escalation. Let’s understand what is Privilege Escalation.

**What is Privilege Escalation?**

Privilege escalation is a cyberattack technique where an attacker gains unauthorized access to elevated permissions on a system or application, often moving from a lower-privilege account to a higher-level one like an administrator. This allows them to perform actions they shouldn’t normally be able to, potentially leading to data breaches, system compromise, and other malicious activities.

To understand how an attacker can gain unauthorize access, we will perform exploitation on Buggy Buy.

Buggy Buy is a purposely vulnerable e-commerce platform that simulates real-world scenarios for security testing.

For this practical;

*Requirements:*

- Buggy Buy: [https://vulnerable-web-application-jecw.vercel.app/login](https://vulnerable-web-application-jecw.vercel.app/login)
- Burp Suit

**Step # 1: Register as a Normal user**

- Fill out the registration form with valid credentials (name, email, password).

**Step # 2: Start Burp Suite and Enable Intercept**

- Open Burp Suite and go to the Proxy tab.
- Make sure Intercept is ON.
- Submit the form.
- You’ll see the captured request on Burp Suit.

**Step # 3: Modify the isAdmin Field**

- In Burp, right-click the request → Send to repeater.
- modify isAdmin field value, from false to true.
- Hit send.

**Step # 4: Login as Admin**

- Visit Admin login page [https://vulnerable-web-application-jecw.vercel.app/admin](https://vulnerable-web-application-jecw.vercel.app/admin)
- Login as Admin using the same crediential.

**What Happened?**

The application’s registration endpoint (`/api/v1/users/register`) allows users to manipulate the `isAdmin` field during registration. By default, this field is set to `false` for normal users, but attackers can override it to `true`, granting unauthorized administrative privileges.

**Impact**

· **Unauthorized Admin Access**: Attackers can register as administrators, bypassing role-based access controls (RBAC).

· **Full System Compromise**: Admin privileges allow access to sensitive data, user management, and application configuration.

· **Data Breach**: Exposure of all user records, orders, and payment details.

**Remediation**

**1. Server-Side Role Validation**:

- Remove the `isAdmin` field from client-side registration requests.
- Assign roles server-side (e.g., only admins can create admin accounts).

**2. Input Sanitization**:

- Reject requests containing unexpected fields like `isAdmin`.

**3. Session Validation**:

- Store user roles server-side (e.g., in the database) and validate them during authentication.

**Conclusion:**

With a small change to the request, privilege escalation — a stealthy but deadly vulnerability — can elevate a regular user to the status of full administrator. Ignoring server-side validation can lead to total system breach, data theft, and money loss, as was the case with Buggy Buy. This highlights how crucial it is to always enforce role assignments securely on the backend and never trust client-side input. Even the slightest mistake can have the most significant effect on cybersecurity.

This post is for educational purposes only. All testing was performed in a legal, controlled environment.


**WEB APPLICATION PENETRATION TESTING:**
