# Authorization bypass due to cache misconfiguration

- **Source URL:** https://rikeshbaniya.medium.com/authorization-bypass-due-to-cache-misconfiguration-fde8b2332d2d?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250717150034/https://rikeshbaniya.medium.com/authorization-bypass-due-to-cache-misconfiguration-fde8b2332d2d
- **Fetched:** 2026-11-27
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/7041 (id 7041)
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
{"operationName":"GetOrders","variables":{"shop_id":"X"},"query":"query X"}
```
The response contained all the order information of my shop.

That is an expected behavior.

What was strange however is, Autorize flagged the endpoint as “bypassed” meaning that even a normal user is able to make this request and access order info of my shop.

But when i sent that request to repeater and tried to make request with user cookies it gave an error.

Hmmm[🤔](https://emojipedia.org/thinking-face)

autorize says bypassed , repeater says forbidden.

I assumed it to be a glitch within autorize and moved on.

For the entire week when i was testing the program, it kept happening.

Autorize kept showing the `GetOrders` endpoint as “bypassed” but when i used to send the request to repeater and test , it gave me the `403 forbidden` error.

At this point, I was certain that it isn’t an issue with Autorize, and I am just missing something.

Then it clicked.

Only difference between Autorize and Repeater was the time interval.

While they both had same cookies/token.

Autorize was making immediate call to the admin endpoint.

Where as me making the request from repeater took some time.

To test my theory:

I made a request to `GetOrders` endpoint using admin token.

```
POST /graphql
Host: admin.target.com
Auth: Bearer admin
{"operationName":"GetOrders","variables":{"shop_id":"X"},"query":"query X"}
```
then immediately made the same request with user token.

```
POST /graphql
Host: admin.target.com
Auth: Bearer user
{"operationName":"GetOrders","variables":{"shop_id":"X"},"query":"query X"}
```
To my surprise i was able to get all the order info of that shop including customer details.

**Issue**

So what was happening is:

The server was caching the `GetOrders` response for a very brief period of 3/4 seconds.

So if an attacker makes the request at the same time when a normal shop admin is using his admin portal, attacker is able to fetch all the order/customer info belonging to any shop just using `shop_id`.

The `shop_id` is a publicly accessible id.

**Exploit**

Create a simple bash script that will make continuous request to the `GetOrders` endpoint throughout the day

When ever the admin visits their portal , the order/customer info gets cached for a window of 3/4 seconds allowing attacker to fetch them and bypassing all access control restrictions.

**POC**

I ran my intruder making request to `GetOrders` endpoint with user token.

It gave a `403 forbidden` response initially due to access controls in place.

In the mean time i logged into `admin.target.com` as adminUser and normally visited `admin.target.com/orders`

The graphql request to `GetOrders` was made in the background on behalf of admin which was available to be cached for 3/4 seconds.

The cached response was eventually fetched by the same intruder tab that was giving 403 error just a minute earlier.

The issue was triaged as critical and immediately resolved within hours.

Hope you liked the writeup.

Follow: [x.com/rikeshbaniya](https://x.com/rikeshbaniya)
