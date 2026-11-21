# IDOR

- **Source URL:** https://medium.com/@sachinpv2004/idor-when-one-tiny-change-exposes-everything-c54b6750d2fd?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250821201846/https://medium.com/@sachinpv2004/idor-when-one-tiny-change-exposes-everything-c54b6750d2fd
- **Fetched:** 2026-11-21
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/9633 (id 9633)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# 🔓 IDOR: When One Tiny Change Exposes Everything

# 🤔 What is IDOR?

Ever notice URLs like this?

Now imagine changing that `1001` to `1002`… and suddenly you’re looking at someone else’s private data. Scary simple, right?

That’s **Insecure Direct Object Reference (IDOR)** — a vulnerability where users can directly access unauthorized data just by tampering with object references like user IDs, document names, or message numbers.

No fancy hacking. Just curiosity and a little trial and error.

# 💣 How Do IDORs Happen?

Here’s where devs go wrong:

- Trusting user-supplied identifiers (like IDs in URLs or JSON bodies)
- Failing to check if the user actually owns the data they’re requesting
- Relying too much on client-side restrictions
- Using sequential or guessable IDs (like 101, 102, 103…)

If the backend doesn’t ask, *“Is this user allowed to access this?”* — then it’s open season.

# ⚠️ Real-World Attack Scenarios

*📬 1. Message Snooping*

📌 The Attack:

Endpoint like `/api/message/8391` returns your chat. Change the ID, and you’re reading someone else’s DMs.

🧠 Real Case:

A social media app leaked private messages via sequential message IDs. Bug bounty hunters exploited this to access random conversations.

✅ Takeaway: Always verify that the current user is authorized to access that message ID.

*🧾 2. Invoice Peeking*

📌 The Attack:

URL like `/invoices/view?doc=invoice123.pdf` can be changed to access someone else's billing data.

🧠 Real Case:

A major SaaS product was found leaking thousands of invoices. Attackers just changed the doc ID.

✅ Takeaway: Don’t rely on predictable filenames. Use UUIDs or hash-based references, and double-check ownership server-side.

*🎮 3. Account Settings Hijack*

📌 The Attack:

POST request to `/user/settings` with JSON like `{ "user_id": 2002, "email": "attacker@example.com" }` can change *someone else’s* email.

🧠 Real Case:

A mobile gaming platform allowed players to edit settings via exposed APIs — without validating if they were editing their own account.

✅ Takeaway: Never trust `user_id` or object IDs coming from the client. Always derive from session/context.

# 🔍 How Hackers Find IDORs

Here’s how attackers — and bounty hunters — discover IDORs:

- 🔄 **Change object IDs manually** in URLs or JSON payloads
- 🧪 **Replay intercepted requests** as a different user
- 🧰 **Use Burp Intruder** or Python scripts to automate ID enumeration
- 👀 **Look for unauthenticated endpoints** that return sensitive data
- 🔗 **Try accessing shared links** meant for specific users and check if they’re globally accessible

# 🛡️ Mitigation: How to Stop IDOR in Its Tracks

✅ **For Developers**

- Validate ownership of resources *on the backend*
- Use unpredictable identifiers (e.g., UUIDs instead of `1234`)
- Never trust object IDs sent from the client
- Apply access control at the object level (not just routes)
- Don’t expose internal DB IDs if unnecessary
- Monitor logs for ID enumeration attempts

✅ **For Bug Bounty Hunters**

- Check every ID or file reference you can see
- Try modifying any parameter ending in `_id`, `_ref`, `_uuid`
- Compare responses for different users — look for data leakage
- Mix IDOR with privilege escalation for bigger impact
- Don’t ignore mobile apps or old versions — they often miss access control checks

**🗝️ Key Facts**

If the app:

- Exposes user or object IDs in URLs, forms, or APIs
- Doesn’t validate ownership of those objects
- Trusts client input without verifying context

…then it is vulnerable to **IDOR** — and potentially leaking PII, payment data, chats, or worse.

It’s silent. It’s simple. And it’s everywhere.

#BugBounty #Pentesting #WebSecurity #Cybersecurity #DevTips
