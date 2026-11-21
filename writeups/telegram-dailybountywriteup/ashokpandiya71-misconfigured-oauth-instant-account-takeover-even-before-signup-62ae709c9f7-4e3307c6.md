# Misconfigured OAuth = Instant Account Takeover (Even Before Signup!)

- **Source URL:** https://medium.com/@ashokpandiya71/misconfigured-oauth-instant-account-takeover-even-before-signup-62ae709c9f7e?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250906022422/https://medium.com/@ashokpandiya71/misconfigured-oauth-instant-account-takeover-even-before-signup-62ae709c9f7e
- **Fetched:** 2026-11-21
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/9746 (id 9746)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Misconfigured OAuth = Instant Account Takeover (Even Before Signup!)

## 🕵️♂️ How I Took Over Accounts Before Users Even Registered — Thanks to a Misconfigured OAuth System

Imagine being able to **log into someone’s account before they even create it**. Sounds like fiction? But it actually happened — all because of a login system flaw that many websites are still vulnerable to today.

Let me walk you through this real-world vulnerability called a **Pre-Account Takeover via Misconfigured OAuth**, in the simplest way possible.

## 🔐 Two Login Methods, One Big Mistake

Most modern websites let users:

- Sign up using **email & password**, or
- Use a **social login** (like Google, Facebook, or Apple) — also known as **OAuth**

Nothing unusual so far. But when both methods aren’t **securely connected**, something dangerous happens.

## 🧠 What Is a Pre-Account Takeover?

Think of it like this:

- There’s a house with **two entrances**
- One entrance requires a **key** (email/password)
- The other entrance just asks if you’re from a **trusted group** (Google/Facebook)

Now imagine I **sneak into the house first** using a fake key, **before the real owner ever arrives**. When they finally show up and use the second door, we both end up in the same house — but I was there first, and I may have changed the locks.

That’s a **pre-account takeover** — and it’s real.

## 🪜 Step-by-Step Breakdown

1\. I signed up using someone else’s email address (like [victim123@gmail.com](mailto:victim123@gmail.com)) through the regular email-password method.

\`No email verification? Account created.\`

2\. I set a password. Now I own the account with that email on the platform.

3\. Days or weeks later, the real owner of that email signs up using Google login.

4\. The platform doesn’t detect that this email is already tied to another account — and it allows the login without any checks.

5\. Result?

\* Both users are in the same account.

\* The attacker still knows the password.

\* The attacker can change the password anytime.

## 📸 Proof of Finding

Here’s the screenshot from the platform where I submitted this vulnerability.

✅ Marked **valid**, **P2 (high impact)**

⛔ Labeled as **duplicate**, but it was still recognized with **5 points** and earned me a spot in the **Hall of Fame**

## 🎉 Bonus: Hall of Fame Recognition

Even though the report was marked as a duplicate, it was **recognized with points** and I was listed in the **Hall of Fame** for discovering it independently. These wins matter — especially when they highlight **real-world security risks**. **\~\~\~ ashoka\_\_11**

## 🎯 Final Thoughts

This issue proves how **overlooking logic and identity verification** can lead to full account compromise — before a real user ever steps in.

Whether you’re a developer or a bug bounty hunter:

- **Think like an attacker**
- **Test assumptions**
- **Always link and verify identities between login flows**

It’s not just about writing secure code — it’s about thinking securely.

🌐 Connect with Me

If you enjoyed this write-up or want to discuss bug bounty hunting, ethical hacking, or security in general — let’s connect!

- 🔗 LinkedIn: https://[www.linkedin.com/in/ashok-ghewarchand-pareek-b01b7226b](http://www.linkedin.com/in/ashok-ghewarchand-pareek-b01b7226b)
- 📸 Instagram: [https://www.instagram.com/ashoka\_\_11/](https://www.instagram.com/ashoka__11/)
- 🐦 Twitter/X: [https://x.com/Pareek\_\_ashoka](https://x.com/Pareek__ashoka)

🔐 I regularly share bug bounty findings, cybersecurity tips, and responsible disclosure write-ups.

Let’s grow together as a community of ethical hackers 🚀

Happy Hunting…!!
