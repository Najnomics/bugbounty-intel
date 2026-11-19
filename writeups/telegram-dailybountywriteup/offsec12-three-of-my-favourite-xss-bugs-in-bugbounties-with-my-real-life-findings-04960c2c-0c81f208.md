# Three of my favourite XSS bugs in bugbounties with my real life findings!

- **Source URL:** https://medium.com/@offsec12/three-of-my-favourite-xss-bugs-in-bugbounties-with-my-real-life-findings-04960c2cecf5?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20251105124353/https://medium.com/@offsec12/three-of-my-favourite-xss-bugs-in-bugbounties-with-my-real-life-findings-04960c2cecf5
- **Fetched:** 2026-11-19
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/11573 (id 11573)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
Member-only story

# **Three of my favourite XSS bugs in bugbounties with my real life findings!**

**Hello friends** 👋 **today I want to share three of the most common XSS bugs I run into in web apps, how they usually show up, why they matter, and what devs/security folks can do about them.**

## **1. Frontend only filtering**

This one appears when an app attempts to detect or block XSS only on the client side (JavaScript in the browser) and assumes the backend enforces nothing. In practice, you can easily bypass client side checks by modifying requests or using the browser console, and if the server doesn’t validate or encode output correctly, the injected content will execute in other users’ browsers.

### Example from my findings

A clear example of this bug was on a quiz website’s bug bounty program (not on HackerOne). I bypassed the client side filters on quiz question preparing page and created stored XSS payloads inside quizzes. When someone attempted to take my quiz, their session cookies were sent to my webhook.

### Defense

Always validate and canonicalize inputs on the server, use context aware output encoding, and apply a strict Content Security Policy (CSP). Treat client-side checks as UX helpers never as security measures.
