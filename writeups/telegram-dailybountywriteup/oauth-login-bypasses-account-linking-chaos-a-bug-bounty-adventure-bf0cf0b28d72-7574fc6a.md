# OAuth Login Bypasses & Account Linking Chaos — A Bug Bounty Adventure

- **Source URL:** https://sohanxp56.medium.com/oauth-login-bypasses-account-linking-chaos-a-bug-bounty-adventure-bf0cf0b28d72?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250829022523/https://sohanxp56.medium.com/oauth-login-bypasses-account-linking-chaos-a-bug-bounty-adventure-bf0cf0b28d72
- **Fetched:** 2026-11-23
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/10523 (id 10523)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# OAuth Login Bypasses & Account Linking Chaos — A Bug Bounty Adventure

During a routine bug bounty hunt, I stumbled upon an OAuth login flow behaving like it had a mind of its own. Two related quirks made me raise an eyebrow (and maybe snicker) — all perfectly legal to test, of course.

Think of it like a digital “oops” moment, but with potential account takeover consequences.

🕵️♂️ The Misbehaving Features

1️⃣ Email Verification Bypass via OAuth 📨

Imagine registering an account, not verifying your email, and then logging in via Google — OAuth says: “Sure, you’re verified… I trust you!”

Spoiler: you’re not verified. But suddenly, you can edit profiles and poke around features.

It’s like showing up at a party without an invite, and the bouncer hands you the keys anyway. 🎉

2️⃣ Automatic Account Linking Without Consent 🔗

Now imagine logging in via Google with an email that matches an existing account. Instead of politely asking, “Hey, do you want to link these?”, the system just merges them.

It’s like your digital self saying: “We’re family now. No need to ask.”

OAuth clearly likes to play matchmaker… aggressively. ❤️

🛠 Steps to Reproduce 🧪

Issue 1 — Email Verification Bypass 🚪

1 Registered an account using [hello@gmail.com](mailto:hello@gmail.com) via email/password.

2 Ignored the verification email.

3 Logged out.

4 Clicked “Login with Google” and authenticated using the same email.

5 Boom — I was in.

No verification. No restrictions.

The account was still marked as unverified, but I could access features like editing the profile and possibly more.

Issue 2 — Account Linking Without Asking 🔄

Then I decided to see what happens with a verified email/password account.

1 Created an account using [hello@gmail.com](mailto:hello@gmail.com) via email/password.

2 Verified the email.

3 Logged out.

4 Logged in with Google using the same email.

5 I was instantly logged into the existing account

No confirmation prompt. No “Do you want to link accounts?” message.

The system just assumed, “If the email matches, they must be the same person.”

Impact:

If someone controls a Google account with the same email (due to a previous breach, credential stuffing, or weak email security), they could instantly access the victim’s account without the password.

Why This Is Dangerous

This isn’t just a “minor best-practice” issue.

It’s a chainable flaw:

Step 1: Attacker registers a victim’s email (or finds an existing unverified account).

Step 2: Logs in via OAuth and bypasses verification.

Step 3: Gains access to account features or takes over entirely.

When combined, these issues undermine the entire authentication flow.

Recommendations

Enforce verification checks on all login methods.

Add explicit user consent prompts before linking OAuth to an existing account.

Monitor unusual linking behavior for signs of abuse.

Takeaway

OAuth integrations are convenient, but convenience without security is an open door for attackers.

Always validate verification status and never auto-link accounts without asking the user.

This bug could have easily gone unnoticed, but sometimes the most impactful vulnerabilities hide in plain sight — right behind a shiny “Login with Google” button.

If you found this useful, hit the 👏 button, share it with your fellow hunters, and follow me here so you don’t miss the next drop.

[https://x.com/Comrade\_proxy](https://x.com/Comrade_proxy) follow me
