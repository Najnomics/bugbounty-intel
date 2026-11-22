# Authorization bypass due to cache misconfiguration

- **Source URL:** https://medium.com/@bilalresearcher/authorization-bypass-due-to-cache-misconfiguration-7407aa1c6374?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20240829062259/https://medium.com/@bilalresearcher/authorization-bypass-due-to-cache-misconfiguration-7407aa1c6374
- **Fetched:** 2026-11-22
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/7043 (id 7043)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Authorization bypass due to cache misconfiguration

This writeup is about one of my favorite findings as it was a very unexpected issue.

I was testing an ecommerce site.

It had 2 assets in scope.

`target.com` and `admin.target.com`

`target.com` was the user facing portal where users could go and buy items.

`admin.target.com` was basically the admin portal for sellers where they could list their items, track orders, customer info and so on.

I was testing for idors and access controls. I generally use Autorize for it.

If a lower privilege user is able to hit the admin endpoint Autorize will flag it as “bypassed” .

With the normal user cookie from `target.com` placed into Autorize , i was using the `admin.target.com` to check if a normal user can access the admin endpoints.

During my testing something unusual happened.

Every time i visited the endpoint:

`https://admin.target.com/orders` , following GraphQL request was being made.

```
POST /graphql
Host: admin.target.com
```
`{"operationName":"GetOrders","variables":{"shop_id":"X"},"query":"query X"}`
