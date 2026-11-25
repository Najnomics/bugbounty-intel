# How I Uncovered IDOR, XSS, and Full Account Takeover in a Single Hunt

- **Source URL:** https://krishna-cyber.medium.com/how-i-uncovered-idor-xss-and-full-account-takeover-in-a-single-hunt-acfce2f9a84f?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250501113836/https://krishna-cyber.medium.com/how-i-uncovered-idor-xss-and-full-account-takeover-in-a-single-hunt-acfce2f9a84f?source=rss------bug_bounty-5
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/8942 (id 8942)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
Member-only story

# **How I Uncovered IDOR, XSS, and Full Account Takeover in a Single Hunt 🎯💥**

*From Curiosity to Chaos: A Bug Bounty Journey That Netted $6,500 and a Security Overhaul*

# 🌟 Introduction

Imagine finding *three critical vulnerabilities* in one target — each flaw more dangerous than the last. That’s exactly what happened during my recent bug bounty sprint, where I chained an **IDOR**, a **stored XSS**, and a **full account takeover** to compromise an entire social media platform. Buckle up as I walk you through this rollercoaster ride — and how it earned me a **$6,500 bounty**!

# 🎯 Target Selection: The Perfect Storm

I targeted a **social media app** with:

- **High user engagement**: Millions of posts, DMs, and profile views daily.
- **Complex features**: File uploads, real-time chat, and third-party integrations.
- **Generous HackerOne program**: Critical flaws = $5k+ rewards.

Spoiler: The app’s “convenience over security” design became my golden ticket. 🎟️

# 🔍 Part 1: The IDOR That Started It All

While testing user profiles, I noticed the endpoint `/api/user/[ID]/posts` leaked private posts by incrementing the `[ID]` parameter. Changing `user_id=1001` to…
