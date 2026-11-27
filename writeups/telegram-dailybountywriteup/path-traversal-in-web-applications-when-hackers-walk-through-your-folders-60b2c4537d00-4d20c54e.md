# ️ Path Traversal in Web Applications

- **Source URL:** https://sukhveersingh97997.medium.com/%EF%B8%8F-path-traversal-in-web-applications-when-hackers-walk-through-your-folders-60b2c4537d00?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250904165720/https://sukhveersingh97997.medium.com/%EF%B8%8F-path-traversal-in-web-applications-when-hackers-walk-through-your-folders-60b2c4537d00
- **Fetched:** 2026-11-27
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/10572 (id 10572)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# 🗂️ Path Traversal in Web Applications: When Hackers Walk Through Your Folders

Hey security folks 👋! Today, let’s explore one of the oldest yet still powerful vulnerabilities in web applications — **Path Traversal** (also known as **Directory Traversal**). If you’re a bug bounty hunter 🕵️♂️ or a developer who wants to secure apps, this guide will walk you through everything you need.

## 🚨 What is Path Traversal?

Path Traversal happens when an application allows users to access files **outside of the intended directory**. By manipulating file paths, attackers can “traverse” folders and gain access to sensitive files.

## 🧨 Why is it Dangerous?

- Attackers can **read sensitive system files** (like `/etc/passwd`, `web.config`, or application logs).
- They may gain **source code access** → leaking database passwords or API keys.
- In some cases, path traversal leads to **remote code execution (RCE)**.

*In bug bounties, Path Traversal is often critical severity → $$$ rewards 💰.*

## 🔎 Common Path Traversal Scenarios

## 💻 Example Exploit

Imagine a vulnerable PHP code: —

## ✅ How to Prevent Path Traversal

If you’re a developer:

- **Never trust user input.** Always validate file paths.
- Use **whitelists** (only allow specific files, like `about.html`, `contact.html`).
- Use **built-in path normalization** functions (e.g., `realpath()` in PHP).
- Run applications with **least privilege** → don’t let the app user access system files.
- Avoid concatenating user input directly into file paths.

## 🎯 For Bug Bounty Hunters: How to Spot It

Here’s your checklist 📝:

- Look for parameters like `file`, `path`, `doc`, `page`, `download`, `view`, `template`.
- Try basic payloads like: —
- ../../../../etc/passwd
..\..\..\..\windows\win.ini
- Use **encoding tricks** to bypass filters (`%2e%2e%2f`).
- Always check **error messages** → they might leak the real server path.
- Test in **file download/file view features**.

*💡 Pro Tip: Automate initial testing with tools like Burp Suite Intruder, but always try manual payloads — creative inputs often bypass WAFs.*

### Also, complete all labs of path traversal by PortSwigger.

## 🚀 Final Thoughts

Path Traversal may sound old-school, but it **remains one of the most critical vulnerabilities** in modern applications. If you can read source code, configs, or system files, you’re one step away from **full compromise**. 😬

For bug bounty hunters → always check for it, even in modern apps (you’ll be surprised how often it works). For developers → fix it early and save yourself from huge breaches. 🔐

👉 Remember: sometimes the simplest payload (`../../`) is all it takes. Stay sharp and happy hacking! 🕵️♂️💻

✨ Thanks for reading! If you liked this post, share it with your friends, drop a comment, and clap 👏 on Medium. Let’s make the web safer together!

You can follow me on [LinkedIn](https://www.linkedin.com/in/sukhveer-singh-byte128/).
