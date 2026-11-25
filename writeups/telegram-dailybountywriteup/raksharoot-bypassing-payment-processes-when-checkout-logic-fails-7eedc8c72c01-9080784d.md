# Bypassing Payment Processes

- **Source URL:** https://medium.com/@raksharoot/bypassing-payment-processes-when-checkout-logic-fails-7eedc8c72c01
- **Fetched from:** https://medium.com/@raksharoot/bypassing-payment-processes-when-checkout-logic-fails-7eedc8c72c01?source=rss-4206d471b207------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14940 (id 14940)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** Raksharoot / Thu, 08 Oct 2026 18:00:36 GMT

How attackers pay less, pay once, or don’t pay at all.

Disclaimer: Educational content only. Test systems you own or have written permission to test. Unauthorized access is illegal. Use legal labs and engagement-owned test accounts. Never test payment flows on live production systems without written authorization.

Payment bugs are the most satisfying finds in web security.

Not because they’re technically complex, most of them aren’t. But because they hit the company exactly where it hurts. A checkout that trusts the client is a checkout that can be manipulated. And once you find one payment bug, you’ll start seeing them everywhere.

**The core problem is always the same**: the server is trusting something the client controls.

Either the price, the payment status, the order ID, or the callback that says “this was paid.” Every payment bypass comes from one of those four being handled wrong.

Here’s how it actually plays out.

You can’t break a payment flow you don’t understand. So the first thing you do is trace it end to end.

Cart → checkout session → payment provider redirect → webhook/callback → order fulfillment → refund → cancellation

*Every step. Every request. Every state transition.*

*The question you’re answering is simple:* where does the paid amount, currency, order ID, and final status actually get decided?

If the answer is “the server, from its own database,” you’re probably safe. If the answer involves anything the browser sent, keep digging.

Three parameters show up again and again in broken flows:

If any of those decide whether an order is marked paid, you’ve found something.

This one is subtle and I love it.

The client never submits a price. It just says “here’s my cart, here’s my session.” The server does all the math. That sounds safe.

But here’s ***where it breaks***:

The backend creates a pricing object, a quote, a discount calculation, a checkout session, based on cart state A. Then the user changes the cart. Now it’s cart state B. The server accepts the change, but reuses the pricing context from state A.

***The result:*** the server calculates a total that doesn’t match the current cart. And it trusts its own old math.

Now compare. Does the new total reflect the current cart? Or the old one?

Check everything: product ID, quantity, currency, subtotal, discount eligibility, shipping, tax, and final total. If any of those describe a different cart than what you’re actually buying, you’ve found

stale state.

And here’s the part most people miss: don’t stop at the preview.

A lot of apps show a wrong price at checkout but recalculate at the final payment step. That’s not exploitable. The real test is whether the stale lower amount survives all the way through order creation and the payment callback. If it does, that’s server side price manipulation.

That’s real money.

Sometimes you’ll see a parameter that looks like this: https://example.com/payment/MD5HASH

That’s not a normal URL. That’s a bearer token pretending to be a URL. Copy it. Open it in a fresh browser profile. No cookies, no session. If the page loads and shows you a completed payment, you need to answer three questions:

If the answer to all three is “no,” “no,” and “no,” you have a payment bypass. Anyone with the link can see the payment, and possibly complete one.

This is the oldest one in the book, and it still works more often than it should.

You intercept the response from the payment endpoint.

The server returns something like:

{“success”: false}

*Change it to:*

{“success”: true}

Forward it to the browser. See what happens.

If the app marks the order as paid, the server was never validating the payment, it was just trusting whatever the client said. That’s a full payment bypass.

*Also test:*

Some systems fail open. When the expected parameter is missing, they assume success.

If the app stores payment status or user identity in a cookie, that’s worth a look.

Decode it. Check if it’s signed. If it isn’t, change the values and see what happens.

A cookie that says *paid=false* and can be flipped to *paid=true* is a bug. A cookie that says *user=123* and can be changed to *user=456* is worse, that’s someone else’s order.

Check whether the payment token is:

If it’s none of those, you can replay it. You can substitute it across accounts. You can reuse it after it should be dead.

This is where the real money is.

Most payment providers (Stripe, PayPal, etc.) send a webhook to your server after a successful payment. That webhook is the source of truth. Not the browser redirect. Not the client-side success page.

But a lot of apps treat the redirect as authoritative.

*What to test:*

If the app fulfills orders based on a webhook that isn’t signed or isn’t verified, that’s a critical bug. You can mark any order paid.

Payment providers often redirect the user back to the app with a parameter like:

?payment=success&order\_id=123

The app reads this and thinks “great, payment went through.”

Except, that parameter is in the URL. The user controls it. Anyone can navigate to *?payment=success* and the app might believe them.

Always check whether the app:

A redirect that says “success” should never be enough to fulfill an order.

Small details that turn into big bugs.

These are all business logic bugs. No scanner will find them. That’s why they’re valuable.

Payment sessions are sometimes treated differently from login sessions. They’re often longer-lived and less protected.

If any of those fail, you have a cross-account payment bug.

Intercept every response in the payment flow. Look for:

Then modify it. Change the browser-visible response to show success. That alone shouldn’t matter, fulfillment should wait for the server-to-server result. But test it anyway.

***The real check:*** does changing the client-visible response affect anything server-side? If yes, you’ve found a bug.

Not exhaustive, but this is the order I go in:

Every payment bypass comes from the same root cause: *the server trusting the client.*

The fix is always the same too, the server should derive the amount, the currency, and the payment status from its own trusted state, not from anything the browser sends.

When you’re testing, don’t look for the specific bug. Look for the moment where the server stops verifying and starts believing. That’s where the money is.

Test in legal labs. Use engagement-owned accounts. And if you find a payment bypass, report it fast — because real money is on the line

Read the whole series in order: [Web Pentesting: A Complete Guide](https://medium.com/@raksharoot/list/web-pentesting-a-complete-guide-ad31d529002a)
