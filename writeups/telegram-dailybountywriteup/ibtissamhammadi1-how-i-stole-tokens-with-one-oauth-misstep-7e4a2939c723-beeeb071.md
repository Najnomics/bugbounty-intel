# How I Stole Tokens with One OAuth Misstep

- **Source URL:** https://medium.com/@ibtissamhammadi1/how-i-stole-tokens-with-one-oauth-misstep-7e4a2939c723?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250905170904/https://medium.com/@ibtissamhammadi1/how-i-stole-tokens-with-one-oauth-misstep-7e4a2939c723
- **Fetched:** 2026-11-21
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/10143 (id 10143)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
Member-only story

# How I Stole Tokens with One OAuth Misstep

“It was 2 AM, my fifth coffee deep when I almost dismissed the bug that would leak thousands of tokens. All because of **one misconfigured header**.”


I wasn’t hacking a bank or a government site — just testing a **popular SaaS platform** for fun.

But what started as a casual bug hunt turned into a **real-world OAuth exploit** that could’ve led to **massive account takeovers**.

The scary part? **It wasn’t complicated.**

If you’ve ever set up OAuth — or worse, copy-pasted a config without thinking — you might’ve made the same mistake.

### Simplified OAuth Primer (For Non-Hackers)

*“OAuth is like a valet ticket for your data. You hand it to an app (say, Google) and say, ‘Let this weather app access my email — but only my email!’”*

But what if the valet (**the OAuth server**) doesn’t check **who’s asking**?

That’s where my exploit came in.

**The Exploit Flow (Step-by-Step)**

1. **The victim** logs in via OAuth (e.g., “Sign in with Google”).
2. **The attacker (me)** tampers with the `Host` header in the redirect URL.
3. **OAuth server** blindly trusts the tampered URL → sends tokens to **my server**.
