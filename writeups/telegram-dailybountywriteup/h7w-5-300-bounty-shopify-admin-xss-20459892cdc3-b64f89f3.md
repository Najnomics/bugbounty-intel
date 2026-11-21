# $5,300 Bounty

- **Source URL:** https://medium.com/h7w/5-300-bounty-shopify-admin-xss-20459892cdc3?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250905104451/https://medium.com/h7w/5-300-bounty-shopify-admin-xss-20459892cdc3
- **Fetched:** 2026-11-21
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/10307 (id 10307)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
Member-only story

# $5,300 Bounty: Shopify Admin XSS

## Exploiting the Rich Text Editor in Product and Collection Descriptions for Persistent XSS

## Introduction

In the world of web security, the most devastating vulnerabilities are often hiding in plain sight. This was precisely the case with Shopify’s admin panel, where a simple toggle between a visual editor and HTML mode exposed a critical weakness. By inserting malicious HTML payloads into the product and collection descriptions, an attacker could execute persistent Cross-Site Scripting (XSS) — gaining the power to hijack sessions, steal cookies, and perform unauthorized actions on behalf of legitimate users.

This write-up explores how security researcher Ashish Dhone uncovered and responsibly disclosed a serious stored XSS vulnerability, earning a $5,300 bug bounty from Shopify. Let’s break it down.

### The Vulnerability: Rich Text Editor Gone Rogue

While reviewing past XSS reports acknowledged by Shopify, the researcher noticed that the Rich Text Editor (RTE) used in Shopify’s admin dashboard was listed as a known attack surface. However, further investigation revealed that certain attack vectors were still exploitable — specifically when using the “Show HTML” option in the RTE for products and…
