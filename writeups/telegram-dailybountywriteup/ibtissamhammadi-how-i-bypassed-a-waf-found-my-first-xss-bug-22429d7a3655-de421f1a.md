# How I Bypassed a WAF & Found My First XSS Bug

- **Source URL:** https://medium.com/@ibtissamhammadi/how-i-bypassed-a-waf-found-my-first-xss-bug-22429d7a3655?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250427200603/https://medium.com/@ibtissamhammadi/how-i-bypassed-a-waf-found-my-first-xss-bug-22429d7a3655
- **Fetched:** 2026-11-21
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/9465 (id 9465)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
Member-only story

# **How I Bypassed a WAF & Found My First XSS Bug**

## **The Simple Trick That Made It Possible.**

I was a beginner when I stumbled on this flaw. Like most new hackers, I assumed **bypassing a WAF (Web Application Firewall)** was only for experts.

But then, I discovered something *so simple* that it worked when every other payload failed.

The WAF blocked every payload — until I tried THIS.

This is the story of how a **tiny oversight** in a security filter led to my first **reflected XSS** and a valuable lesson in **bug hunting**.

## The Target: Why This Program?

Public bug bounty programs are **goldmines for beginners**, but most hunters avoid them because they think *“everything’s already been found.”*

That’s a mistake.

I chose a **public program with a broad scope**, which meant more attack surfaces.

The key? **Manual testing beats automation** when hunting for edge cases.

## Subdomain Enumeration: Finding Hidden Entry Points

*Most guides skip this — but missing subdomains = missing bugs.*

I started with [**Subfinder**](https://securitytrails.com/blog/subfinder) and [**Assetfinder**](https://securitytrails.com/blog/Assetfinder) to gather every possible subdomain:
