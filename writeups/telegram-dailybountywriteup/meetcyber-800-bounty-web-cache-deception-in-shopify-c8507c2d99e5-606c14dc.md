# $800 Bounty — Web Cache Deception in Shopify

- **Source URL:** https://medium.com/meetcyber/800-bounty-web-cache-deception-in-shopify-c8507c2d99e5?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250915145605/https://medium.com/meetcyber/800-bounty-web-cache-deception-in-shopify-c8507c2d99e5
- **Fetched:** 2026-11-21
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/9639 (id 9639)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
Member-only story

# $800 Bounty — Web Cache Deception in Shopify

## How Path Confusion and a .css Extension Led to Personal Information and CSRF Token Leakage

### Introduction

Security researcher Matteo Golinelli discovered a critical Web Cache Deception vulnerability on Shopify.com one of the world’s largest e-commerce platforms. By combining path confusion techniques with a deceptive .css file extension golim was able to expose sensitive user data such as:

- Full name
- Email address
- Profile picture
- Valid CSRF token

The report earned $800 and is a textbook case of how a seemingly harmless caching behavior can result in a serious data leak. If you’re a bug bounty hunter this is the kind of misconfiguration that can be gold if you know how to look.

### Understanding Web Cache Deception

Web Cache Deception is a technique that exploits how web servers and caching systems (like CDNs or proxies) interpret URLs.

Here’s how it works in theory:

1. The victim visits a maliciously crafted URL while logged in.
2. The page is cached by the CDN or proxy.
