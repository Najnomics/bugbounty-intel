# From IDOR to Admin Takeover

- **Source URL:** https://medium.com/@wanqais007/from-idor-to-admin-takeover-how-i-accidentally-walked-into-an-ato-8ec9f7b034c8?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20260325012530/https://medium.com/@wanqais007/from-idor-to-admin-takeover-how-i-accidentally-walked-into-an-ato-8ec9f7b034c8?source=rss------bug_bounty-5
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/13144 (id 13144)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
Member-only story

# 🔥 From IDOR to Admin Takeover: How I Accidentally Walked Into an ATO

Assalamualaikum and Hi everyone! Back again, Qais El Profesor here. Enough with introduction. Lets get started the Biggest Payout! $$$$

## 🧠 The Hunt Begins

Bug hunting is often a mix of patience, frustration, and those rare moments where everything suddenly clicks.

This story is about one of those moments.

I was exploring a target on Bugcrowd, a fairly large web application with multiple subdomains. Like any hunter, I started mapping the surface area, checking endpoints, and digging into JavaScript files.

That’s when I found something interesting.

## 🔍 The First Clue: Internal API Exposure

While analyzing the JS files, I stumbled upon an endpoint:

`/api/internal/user/InternalUser`
At first glance, this didn’t look like something meant for public access.

But curiosity wins in bug hunting. 😝

When I interacted with it, it **returned sensitive internal data** — including:

- Admin emails
- Usernames

💥 That’s already a red flag.
