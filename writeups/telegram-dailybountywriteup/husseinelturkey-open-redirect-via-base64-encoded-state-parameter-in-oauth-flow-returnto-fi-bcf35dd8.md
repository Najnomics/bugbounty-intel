# Open Redirect via Base64-Encoded state Parameter in OAuth Flow (returnTo field)

- **Source URL:** https://medium.com/@husseinelturkey/open-redirect-via-base64-encoded-state-parameter-in-oauth-flow-returnto-field-42a0319ef296?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250517015317/https://medium.com/@husseinelturkey/open-redirect-via-base64-encoded-state-parameter-in-oauth-flow-returnto-field-42a0319ef296?source=rss------bug_bounty-5
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/9658 (id 9658)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Open Redirect via Base64-Encoded `state` Parameter in OAuth Flow (returnTo field)

Hi there, It is me Hussein, I Bug Bounty Hunter (Former Web Developer), I will tell you about an Open Redirect via Base64-Encoded bug I found last month.

While testing `target.com`’s authentication flow in late April 2025, I came across a classic open redirect vulnerability—except it was hidden inside a base64-encoded `state` parameter used during OAuth passwordless login.

After decoding the base46-encoded I found a returnTo field as image shown:

Here’s the core issue:

1. Users login at `https://target.com/login` via email.
2. They receive a **magic link** to verify their login.
3. That link goes to:
[https://auth.target.com/passwordless/verify_redirect?...&state=...](https://web.archive.org/web/20250517015317/https://auth.target.com/passwordless/verify_redirect?...=&state=...)
4. The `state` parameter is base64-encoded JSON that includes:

`{"blabla":".....", "returnTo": "https://target.com"}`
5\. You can decode it, change `returnTo` to something like `https://attacker.com`, and re-encode it.

6\. Boom — a redirect to any domain after login.

# Bugcrowd Response

Here’s what the triager wrote:

“Thank you for your submission. Unfortunately, we have received this report from another researcher. Therefore, it is considered a duplicate issue. Your effort is appreciated and we hope that you will continue to research and submit any future security issues you find.”


Not gonna lie — that one stung.

Why?

Because the previous report submitted: **17 Jan 2025 08:59:55 UTC, But still the bug unsolved, I do not know why? And why wasting our time in an unresolved duplicated issues?**
