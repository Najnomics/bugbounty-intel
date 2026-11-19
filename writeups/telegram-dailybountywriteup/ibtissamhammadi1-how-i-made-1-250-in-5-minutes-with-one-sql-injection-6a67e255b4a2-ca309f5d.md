# How I Made $1,250 in 5 Minutes with One SQL Injection

- **Source URL:** https://medium.com/@ibtissamhammadi1/how-i-made-1-250-in-5-minutes-with-one-sql-injection-6a67e255b4a2?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250915035924/https://medium.com/@ibtissamhammadi1/how-i-made-1-250-in-5-minutes-with-one-sql-injection-6a67e255b4a2
- **Fetched:** 2026-11-19
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/9837 (id 9837)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
Member-only story

# How I Made $1,250 in 5 Minutes with One SQL Injection

## The SQL Injection Payload That Earned Me $1,250

You’ve probably heard about ethical hackers making thousands from bug bounty programs, but what if I told you that just one SQL injection (SQLi) flaw earned me $1,250 in under 5 minutes?

This isn’t a “get rich quick” scam. It’s real, legal, and repeatable — if you know what to look for.

Let me break down exactly how it happened, the payload I used, and how you can do it too (if you’re willing to learn).

### The Moment It Clicked: Finding the SQLi Vulnerability

I was testing a popular e-commerce site (name hidden for security) on [**HackerOne**](/tag/hackerone), looking for common web flaws.

Most hackers focus on XSS or CSRF, but SQL injection is often overlooked — especially in modern apps.

Then, I stumbled upon a search filter that looked like this:

`/products?search=shoes`
A tiny change in the URL made all the difference:

`/products?search=' OR 1=1--`
**Boom.** The page loaded all products at once — no filtering.

### Why This Worked:

- The site wasn’t sanitizing…
