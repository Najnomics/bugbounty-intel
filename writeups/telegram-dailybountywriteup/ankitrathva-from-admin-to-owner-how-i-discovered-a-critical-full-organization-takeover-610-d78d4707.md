# From Admin to Owner

- **Source URL:** https://medium.com/@ankitrathva/from-admin-to-owner-how-i-discovered-a-critical-full-organization-takeover-610a1aa013a7
- **Fetched from:** https://medium.com/@ankitrathva/from-admin-to-owner-how-i-discovered-a-critical-full-organization-takeover-610a1aa013a7?source=rss-d479b91985ef------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14922 (id 14922)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** Ankit Rathva aka Gujarati Hacker / Thu, 24 Sep 2026 06:13:53 GMT

**Summary**

**How a simple role parameter manipulation lead to a Critical Broken Access Control vulnerability**

While testing a web application, I came across an interesting authorization issue in the organization management functionality.

At first, everything appeared to be working as expected. ✅

The application allowed organization administrators to invite new users, but the available roles were restricted to **Admin** and **User**.

The **Owner** role was not available when an administrator invited a new member.

However, when I started looking at the underlying API request rather than relying only on the frontend, things became interesting. 👀

I discovered that the backend was not properly enforcing the role restriction.

By modifying a single parameter, an administrator could invite another account with **Owner privileges**. 🚨

The newly created Owner could then remove the legitimate organization Owner.

The result?

💥**Complete organization takeover.**

Hi everyone! I’m **Ankit Rathva aka Gujarati Hacker**, a security researcher and bug bounty hunter who enjoys finding vulnerabilities in web applications. 🕵️♂️🔐

I mainly focus on areas such as:

For me, bug bounty hunting isn’t just about finding a bug. It’s about understanding **how an application is supposed to work, where its security boundaries are, and what happens when those boundaries are tested in unexpected ways.**

This write-up is about one such finding.

During a security assessment, I discovered a **Critical Broken Access Control vulnerability** that allowed an organization administrator to escalate their privileges to **Owner** by manipulating a single parameter in an API request.

The vulnerability ultimately allowed the newly created Owner to remove the legitimate Owner and take complete control of the organization. 💥

Let’s break down how I found it. 👇

**Connect with me:** [https://linkedin.com/in/ankitrathva](https://linkedin.com/in/ankitrathva)

The application had an organization management feature where users could invite other members.

There were multiple roles within the organization, including:

The important restriction was that an **Admin could invite users as Admin or User**, but should not be able to create another Owner.

From the frontend, this restriction appeared to be correctly implemented. ✅

As an administrator, when I opened the invitation functionality, the **Owner** role wasn’t available as an option.

At this point, the application appeared secure from a normal user-interface perspective.

But there was one important question:

*🤔* ***Was this restriction actually enforced by the backend?***

So I decided to inspect the API request.

I created an organization and configured the accounts required to reproduce the issue.

The basic setup was:

👑 Account A → Organization Owner

↓

🛡️ Account B → Organization Admin

The Owner invited Account B as an Administrator. I then logged in as Account B.

As an Admin, I attempted to manage/invite users and captured the relevant request using **Burp Suite**. 🦋 The request contained a parameter controlling the user’s organization role.

Conceptually, the request looked like:

```
{
  "role": "admin"
}
```
The frontend only allowed the administrator to select permitted roles. But instead of trusting the UI, I decided to modify the request manually.

I changed:

"role": "admin"

to:

"role": "owner"

and forwarded the request. 🚀

I expected the server to reject the request. For example, I expected something similar to:

403 Forbidden

or an authorization error indicating that an Admin was not allowed to create an Owner. Instead…

**The server accepted the modified request.** 😳

The invitation was successfully created with the **Owner** role.

This was the key authorization failure. 🔥

The backend trusted a client-controlled role value without verifying whether the requesting user was actually authorized to assign that role.

Next, I switched to the invited account. The invitation could be accepted normally. ✅

After accepting it, the account was added to the organization with **Owner privileges**. 👑 The privilege escalation flow was now:

🛡️ Admin

↓

📝 Modify API request

↓

🔧 role = owner

↓

✉️ Accept invitation

↓

👑 Organization Owner

An administrator who should never have been able to create an Owner account could now do exactly that.

At this point, the vulnerability was already a serious privilege-escalation issue. But I wanted to understand the **real-world impact**.

As the newly created Owner, I checked the organization management functionality. The Owner had the ability to manage organization members, including the legitimate Owner.

The newly created Owner could therefore remove the original Owner from the organization. The complete attack chain became:

🛡️ Compromised/low-privileged Admin

↓

🔧 Manipulate invitation role

↓

👑 Create unauthorized Owner

↓

✉️ Accept invitation

↓

🔓 Gain Owner privileges

↓

❌ Remove legitimate Owner

↓

💥 Full organization control

This transformed what initially looked like a simple role-manipulation issue into a **full organization takeover** scenario.

The vulnerability could allow a malicious administrator to:

Depending on the application’s organization model and the resources connected to the organization, this could potentially expose or affect a significant amount of organizational data and functionality.

The company ultimately classified the vulnerability as **Critical**. 🚨

📩 Reporting the Vulnerability

I reported the issue to the company with a detailed proof of concept, including:

The security team investigated the report and confirmed the vulnerability.

They classified it as **Critical** 🚨 and recognized the finding by adding me to their **Hall of Fame** 🏆.

I really appreciate the security team’s response and the opportunity to contribute to improving the security of their platform. 🙏

This was a great reminder that some of the most impactful vulnerabilities can come from a very small difference between what the frontend **allows** and what the backend **actually enforces**.

The application correctly hid the Owner role from administrators.

But hiding the option wasn’t enough.

The real security boundary was the API — and the API accepted a role assignment that should never have been permitted.

A single parameter change turned:

🛡️ Admin → Admin

into:

🛡️ Admin → 👑 Owner

and ultimately:

🛡️ Admin

↓

👑 Owner

↓

❌ Remove Original Owner

↓

💥 Full Organization Takeover

For bug bounty hunters, this is why testing **authorization boundaries and business logic** is so important. 🕵️♂️

For developers, the lesson is equally important:

*🔐* ***If a user isn’t authorized to perform an action, the backend must reject it — even when the request is manually crafted.***

If you enjoy practical web application security and bug bounty write-ups, follow me for more vulnerability research, methodology, and real-world findings. 🚀

🔐 **Keep Hunting. Keep Learning. Keep Securing.**
