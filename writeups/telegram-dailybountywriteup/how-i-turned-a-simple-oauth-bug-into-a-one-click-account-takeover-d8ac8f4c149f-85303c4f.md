# How I Turned a Simple OAuth Bug Into a One-Click Account Takeover

- **Source URL:** https://sr0x01.medium.com/how-i-turned-a-simple-oauth-bug-into-a-one-click-account-takeover-d8ac8f4c149f?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20251118112703/https://sr0x01.medium.com/how-i-turned-a-simple-oauth-bug-into-a-one-click-account-takeover-d8ac8f4c149f
- **Fetched:** 2026-11-27
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/10541 (id 10541)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
Member-only story

# How I Turned a Simple OAuth Bug Into a One-Click Account Takeover

When we think of OAuth, most imagine it as a secure, battle-tested protocol that giants like Google, Facebook, and Twitter rely on for authentication. But as I discovered during one of my bug bounty hunts on redacted.com, even tiny oversights in the OAuth flow can escalate into a full-blown account takeover (ATO).

This is the story of how I found a vulnerability in the Google account linking feature of a public bug bounty program that we will be calling redacted.com, I managed to chain it and escalated it from a two-click exploit into a single-click account takeover.

### The Discovery

While exploring redacted.com’s Oauth login flow, I noticed something unusual in the OAuth callback.

The endpoint looked like this:

[https://www.redacted.com/link/google/callback/?state=link&code=\<code>](https://www.redacted.com/link/google/callback/?state=link&code=%3Ccode%3E)


Normally, the state parameter is a critical defense mechanism in OAuth. It prevents Cross-Site Request Forgery (CSRF) attacks by making sure the callback belongs to the same session that started the login process.

But here’s the problem:

redacted.com wasn’t validating the state parameter at all.That means I could craft a malicious OAuth callback URL, intercept it, and send it to a victim and the victim will get…
