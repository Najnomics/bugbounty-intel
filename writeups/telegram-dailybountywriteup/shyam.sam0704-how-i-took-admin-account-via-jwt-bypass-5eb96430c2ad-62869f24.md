# How I Took Admin Account via JWT Bypass

- **Source URL:** https://medium.com/@shyam.sam0704/how-i-took-admin-account-via-jwt-bypass-5eb96430c2ad?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250403224322/https://medium.com/@shyam.sam0704/how-i-took-admin-account-via-jwt-bypass-5eb96430c2ad
- **Fetched:** 2026-11-23
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/9115 (id 9115)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
Hello Everyone ✋,

I’m **Shyamsundhar**, a security researcher from **Coimbatore, Tamil Nadu**. This is my first blog, and I look forward to your feedback. If you have any suggestions or difficulties, please let me know!

# Introduction

In web applications, **JSON Web Tokens (JWT)** have become a popular choice for handling authentication and authorization. They offer a simple and efficient way to manage user sessions and access control. However, improper implementation of JWTs can lead to serious security vulnerabilities.

During a recent security assessment of **DUMMY EVENTS** (`https://www.dummyevents.com`), I discovered a critical **JWT authentication bypass vulnerability** that allowed privilege escalation and admin panel takeover. By manipulating the JWT claims, I was able to gain unauthorized access to sensitive data and administrative controls.

In this write-up, I’ll walk you through how I identified the flaw, exploited it, and recommended fixes to prevent similar vulnerabilities.

Let’s get started…

# How I Found the Vulnerability

As a security researcher, my reconnaissance process involves a thorough investigation of the target application. **DUMMY EVENTS** is an event-hosting and ticketing platform that also offers various web services.

During my reconnaissance, I created an account on their platform and started gathering information about the technologies they used, endpoints that were redirected to other pages, and resources integrated into their application.

After collecting enough information, I began inspecting the source code. Reviewing application source code is one of my favorite activities as it often reveals hidden insights. While analyzing the code, I discovered a **JavaScript file** that controlled the application’s rendering logic. This file determined whether the user interface should display the **admin console** or the standard **user interface**.

# Steps I Followed

Upon further analysis of the JavaScript code, I discovered sensitive information, including:

- Admin, manager, sales, and marketing user IDs.
- Corresponding email addresses for these roles.

The code was designed to verify these credentials to decide which user interface to render. I copied this information and saved it for later use.

# How I Exploited the Vulnerability

Next, I logged into the application with my regular user credentials and captured the requests and responses using **Burp Suite**. I noticed that the application used JWT for authentication and authorization, specifically employing the **HS256 algorithm**. The JWT contained critical claims such as:

- **User ID**
- **Role**
- **Email**
- **Password Provider**

Since I had previously identified the admin’s **user ID** and **email** but lacked the password, I leveraged my own account’s JWT. I modified the JWT claims to:

- Set the **user ID** to match the admin’s.
- Change the **email** to the admin’s email.
- Update the **role** to `admin`.
- Change the **algorithm** to `none` (commonly exploited in JWT attacks).

Once I modified these claims, I forwarded the manipulated response back to the browser. Surprisingly, the browser accepted the token and treated my session as an **admin session**.

# Why This Worked:

The server failed to verify the JWT’s **algorithm** and **signature**, which are crucial for ensuring the token’s authenticity. Without proper validation, the server trusted the manipulated JWT, granting me full access to the admin panel. This oversight exposed the platform to complete compromise, allowing me to:

- Manage events.
- Access customer data.
- Modify user accounts.

# Resolution and Acknowledgment

I promptly reported this vulnerability to the development team. They quickly addressed the issue by implementing proper JWT validation mechanisms, including signature verification and enforcing strict role-based access control (RBAC). As a result, I was recognized in their **Hall of Fame** for responsibly disclosing this vulnerability.

# Conclusion

This experience highlights the importance of robust JWT implementation. Developers must ensure proper token validation, including signature checks, secure algorithms, and clear role-based controls. As security researchers, it’s crucial to stay vigilant and continue exploring new ways to improve application security.

If you have any thoughts or questions, feel free to reach out. Thanks for reading

*“Keep calm and keep hunting!”*
