# Intigriti Halloween Challenge (1026) by Globules writeup

- **Source URL:** https://savi0r.medium.com/intigriti-halloween-challenge-1026-by-globules-writeup-6a830d69ffa2
- **Fetched from:** https://savi0r.medium.com/intigriti-halloween-challenge-1026-by-globules-writeup-6a830d69ffa2?source=rss-cbaed42f5efc------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14963 (id 14963)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** savi0r / Wed, 28 Oct 2026 20:39:17 GMT

A Halloween-themed e-commerce challenge let you stack discount coupons past their intended limit by racing concurrent requests against /api/cart/coupon. After stacking enough discounts, the cart total could be pushed below zero. Since checkout didn't validate the final total, the order still went through — and the flag was waiting in the receipt.

The challenge was a small candy shop with a cart, a checkout flow, store credit, and two coupon codes floating around:

Store credit was capped at €66, nowhere near enough to cover a €700+ cart even with one coupon applied. So the question became: can we stack more discount than the system intends?

My first instinct was the classic single-coupon race: fire the same NIGHT20 request 20 times in parallel and hope a few slip through before the “already applied” flag gets set.

POST /api/cart/coupon

{"code":"NIGHT20"}

Sadly, 19/20 requests came back clean:

```
{
  "ok": false,
  "error": "coupon_already_applied",
  "message": "Coupon already applied."
}
```
The server was properly guarding against duplicate applications of the *same* coupon. Dead end — or so it seemed.

The cart response had a telling detail:

"promotions":\[

{

"code":"NIGHT20",

"percent":20,

"amount":14026,

"count":1

}

\]

The promotions field was an array, which suggested that the system was designed to support multiple different coupons on the same cart. That was the crack.

Getting a second coupon was trivial — the newsletter endpoint handed one out on request:

POST /api/newsletter

{"email":"test@example.com"}

`{"ok":true,"code":"NEWS30", ...}`
Now I had two distinct codes.

Applying them sequentially, one at a time, worked fine. But the real bug showed up when I stopped being polite about it and just **fired both coupons repeatedly and in parallel** at /api/cart/coupon.

The “already applied” check clearly wasn’t atomic. Some requests landed between the check and the update, allowing additional promotion entries to slip into promotions\[\].

After a few rounds of sending both coupons in parallel, GET /api/cart eventually returned a cart with a heavily inflated discount.

At one point, the discount completely covered the item price:

"subtotal": 66600,

"discount": 66600,

"total": 0,

"credit": 6600,

"canCheckout": true

The important part was that the application still considered the cart valid and allowed checkout.

At this point, there was nothing left to bypass on the checkout side. The cart total had reached zero, but the application still allowed the order to be completed.

POST /api/checkout

{}

The order was accepted, and the flag was included in the receipt:

FLAG:

This was honestly a really fun challenge. I liked how the vulnerability wasn’t immediately obvious and required connecting the promotion logic with the race condition.

It was also surprisingly quick to solve once I understood what was happening. The only thing I regret is discovering the challenge during its last hour — I definitely would’ve spent more time digging into it if I had found it earlier.

Overall, a really enjoyable challenge and a great way to finish it.
