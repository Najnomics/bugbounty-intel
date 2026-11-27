# $9,400 Bounty

- **Source URL:** https://osintteam.blog/9-400-bounty-xss-in-shopifys-jamf-pro-via-exposed-swagger-ui-7b029a4be766?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250512153915/https://osintteam.blog/9-400-bounty-xss-in-shopifys-jamf-pro-via-exposed-swagger-ui-7b029a4be766
- **Fetched:** 2026-11-27
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/9605 (id 9605)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
Member-only story

# $9,400 Bounty: XSS in Shopify’s Jamf Pro via Exposed Swagger UI

## How an old Swagger UI left Shopify’s Jamf Pro vulnerable to XSS and account takeover

## Introduction

What if a single outdated admin panel exposed your organization to complete account takeover?

That’s exactly what security researcher kannthu discovered when they found an exposed Swagger UI on Shopify’s Jamf Pro instance leading to a stored XSS vulnerability that allowed arbitrary JavaScript execution in an authenticated context.

This vulnerability earned a $9,400 bug bounty from Shopify under Report ID: #1444682.In this article I’ll break down how this bug was found exploited and how you can hunt for similar vulnerabilities at scale.

## The Vulnerability

Shopify was running Jamf Pro at [https://jamfpro.shopifycloud.com](https://jamfpro.shopifycloud.com) which had an old Swagger UI exposed at the endpoint:

`/classicapi/doc/`
This outdated Swagger UI allowed users to supply a custom config URL via a GET parameter (configUrl) that wasn’t sanitized properly enabling an attacker to inject arbitrary HTML and JavaScript by pointing configUrl to a malicious page or even a data URI.
