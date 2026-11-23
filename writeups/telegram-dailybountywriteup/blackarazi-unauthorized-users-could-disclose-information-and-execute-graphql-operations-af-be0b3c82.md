# Unauthorized Users Could Disclose Information and Execute GraphQL Operations After Permission…

- **Source URL:** https://medium.com/@blackarazi/unauthorized-users-could-disclose-information-and-execute-graphql-operations-after-permission-961094edf7c8?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250719190945/https://medium.com/@blackarazi/unauthorized-users-could-disclose-information-and-execute-graphql-operations-after-permission-961094edf7c8
- **Fetched:** 2026-11-23
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/9441 (id 9441)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
Member-only story

# Unauthorized Users Could Disclose Information and Execute GraphQL Operations After Permission Revoked via WebSocket

Hello everyone,

In this post, I will show you how I discovered a Broken Access Control vulnerability at the GraphQL Subscriptions. Due to this vulnerability, a malicious actor could disclose & execute GraphQL operations after their permission was revoked via WebSocket in a limited attack time window.

## Who is the target?

The target is **Shopify**, which is a public program on HackerOne.

## Reconnaissance

While exploring the Shopify store admin, I noticed that it has a WebSocket connection under `wss://argus.shopifycloud.com/graphql`, after further inspection, I can confirm that it uses the GraphQL Subscriptions feature. However, the domain `argus.shopifycloud.com` is not explicitly specified in the scope & probably would be a better fit under `*.shopifycloud.com` but since it's called from the main asset `admin.shopify.com` so I decided to put it under `admin.shopify.com`.

Other than Subscriptions, the Argus GraphQL also supports other operations such as…
