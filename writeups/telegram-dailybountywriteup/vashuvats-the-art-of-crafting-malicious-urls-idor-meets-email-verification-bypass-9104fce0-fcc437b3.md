# The Art of Crafting Malicious URLs

- **Source URL:** https://medium.com/@vashuvats/the-art-of-crafting-malicious-urls-idor-meets-email-verification-bypass-9104fce05a1e?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250822144029/https://medium.com/@vashuvats/the-art-of-crafting-malicious-urls-idor-meets-email-verification-bypass-9104fce05a1e
- **Fetched:** 2026-11-21
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/10578 (id 10578)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# The Art of Crafting Malicious URLs: IDOR Meets Email Verification Bypass

**Hey everyone!** 👋 I’m **Vashu Vats** a cybersecurity enthusiast and bug bounty hunter.

Today I’ll share how a strange **IDOR leaking PII via crafted URLs** and an **email update flaw** that skips verification can be chained together, leading to targeted attacks and even denial of service for new users in European Union official website .

# The First Vulnerability: IDOR Leak

The first vulnerability was unusual — an **IDOR that leaks the portion of an email address before the “@”**.

This could be triggered by crafting a malicious URL that combines three elements:

- the **registration verification link**,
- a **password reset token**, and
- the **numeric account ID**.

**The Attack Flow is as follows:**

1. **Register a new account** on the target web application.
2. Receive an **email verification link** of the form:
`<redacted>.europa.eu/registration/../<numeric_id>/../<verification_token>`
3. Trigger a **password reset** for your account. The link will look like:
`<redacted>.europa.eu/…/<reset_token>`
4. Ensure you are **logged in** to your account.
5. Extract the **\<reset\_token>** from the password reset link and **replace the \<verification\_token>** in the registration verification URL.

- Modify the **numeric\_id (6-digit and easily brute-forceable)** to that of the victim.
- The crafted URL becomes:
`<redacted>.europa.eu/registration/../<victim_id>/../<reset_token>` The server responds with **personal information of the target account**, confirming account existence and leaking **PII (personally identifiable information)**.

# Chaining With Another Flaw: Email Update Vulnerability

The attacker can leverage the leaked email fragment from the first flaw to perform targeted attack on the users as a**nother vulnerability in the system allows an attacker to change the registered email address of their account to any arbitrary email without requiring verification.**

# Attacker Workflow

1. The attacker registers an account with their own email address (normal registration flow).
2. The attacker logs in and navigates to:*\<redacted>.europa.eu/login-details*
3. The attacker changes their account email to the victim’s email address.
4. Since **no verification link** is sent for email updates, the attacker gains the ability to associate any victim’s email with their account.
5. **Denial of Service (DoS):** If the victim later attempts to register using their legitimate email address, they will be prevented from doing so, since the system already links that email to another account. This effectively enables an account takeover, as the attacker has preemptively claimed unregistered emails on the platform.

Even worse, I discovered that **multiple attacker accounts could be linked to the same victim email**, bypassing the intended restriction that each email should only belong to one account.

# Disclosure

The vulnerabilities were acknowledged by **CERT-EU** under their **Responsible Vulnerability Disclosure program**.

Thanks for reading, and stay tuned for more breakdowns of interesting bugs! 🚀
