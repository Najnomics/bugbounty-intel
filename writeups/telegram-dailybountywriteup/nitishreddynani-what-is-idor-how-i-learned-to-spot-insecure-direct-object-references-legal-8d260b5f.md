# What Is IDOR? How I Learned to Spot Insecure Direct Object References (Legally)

- **Source URL:** https://medium.com/@nitishreddynani/what-is-idor-how-i-learned-to-spot-insecure-direct-object-references-legally-6c0740b67322?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250905123023/https://medium.com/@nitishreddynani/what-is-idor-how-i-learned-to-spot-insecure-direct-object-references-legally-6c0740b67322?source=rss------bug_bounty-5
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/10091 (id 10091)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# 🔓 What Is IDOR? How I Learned to Spot Insecure Direct Object References (Legally)

## 🧐 Introduction

When I first started getting into web security, I kept seeing people mention something called **IDOR**. It sounded complicated… but when I actually understood it, I realized it’s one of the **simplest** and most common vulnerabilities out there.

And that’s what makes it dangerous.

IDOR (short for *Insecure Direct Object Reference*) is one of those bugs that seems harmless — until it lets someone access **another user’s data**, just by changing a number in the URL.

In this post, I’ll walk you through what IDOR is, how I tested it safely, why it happens, and how developers can stop it. Whether you’re new to cybersecurity or working on securing your own app, this one’s worth knowing.

### 💡 So… What Exactly Is IDOR?

Let’s say you’re logged into a website and visit your profile:

Now you change that 123 to 124 and suddenly you’re seeing **someone else’s profile**.

That’s IDOR in action. No hacking, no complex tools — just broken access control.

IDOR happens when a website lets users request data by referencing internal object IDs (like user IDs, invoice numbers, etc.), **without checking if they’re allowed to see it**.

### ⚠️ Why It’s a Big Deal

At first glance, IDOR might seem harmless — but it can lead to serious issues like:

- Leaking personal info (names, emails, addresses)
- Exposing invoices or receipts
- Viewing or modifying someone else’s support tickets
- Even full account takeover in some cases

The worst part? It’s super easy to miss — both for developers and testers.

### 🧪 How I Tried It in a Safe Lab

To see it in action (without getting arrested), I used a free lab from PortSwigger’s Web Security Academy:👉 [Check it out here](https://web.archive.org/web/20250905123023/https://portswigger.net/web-security/access-control/lab-user-id-controlled-by-request-parameter)

Here’s what I did:

1. Logged in as a demo user (like wiener).
2. Saw a URL like:

3\. Opened **Burp Suite**, intercepted the request, and changed the ID to 1002.

4\. Boom — it loaded another user’s account info.

No errors. No access denied. Just a complete breakdown of security.

### 🛠️ Why This Happens

IDOR usually happens when:

- The app shows internal IDs (like user or order numbers) directly in the URL or request.
- There’s **no backend check** to confirm the user owns that data.

It’s like handing out mail based only on the house number someone *says* they live at — without checking their ID.

### 🛡️ How to Prevent It

If you’re building or reviewing a web app, here are a few ways to fix or avoid IDOR:

1. **Always check permissions server-side**
2. Just because a request has a valid ID doesn’t mean it’s allowed.
3. **Use indirect object references**
4. Instead of using raw numbers (user\_id=123), use UUIDs or hashed tokens.
5. **Avoid predictable IDs**
6. Don’t make it easy for someone to guess the next user’s ID.
7. **Centralize access control logic**
8. Make sure permission checks are consistent across the app.
9. **Test like an attacker would**
10. Log in as one user and try to access another user’s data — not just with the UI, but by changing requests directly.

### 👨💻 Why I Love IDOR as a Learning Bug

If you’re new to bug bounties or CTFs, IDOR is one of the **best first bugs to look for**. It’s:

- Easy to understand
- Easy to test for (with tools like Burp)
- Still found in the wild (yes, even in 2025)

Try messing around with:

- Profile URLs
- File downloads
- Invoice lookups
- API endpoints with numeric IDs

Just **make sure you’re doing it legally** — use platforms like:

## 🧠 Final Thoughts

What surprised me most about IDOR is how *simple* it is. You don’t need fancy tools or deep technical skills to find it — just curiosity and the mindset of:

*“What happens if I change this?”*


But that simplicity is also what makes it powerful. With just one unchecked request, someone could access **any user’s private data**.

So whether you’re writing code or testing someone else’s, always ask:

Does the server check if I’m allowed to access this object?


If it doesn’t — you’ve got an IDOR vulnerability waiting to happen.

🔐 *Thanks for reading! If you’re into practical cybersecurity, bug hunting, or just breaking down real-world security problems, follow me here — more posts coming soon.*
