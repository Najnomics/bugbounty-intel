# Easy Logic Bugs

- **Source URL:** https://medium.com/@ziad22mohammad/easy-logic-bugs-how-i-bypassed-two-unbypassable-checks-in-production-systems-2cdea7d56232
- **Fetched from:** https://medium.com/@ziad22mohammad/easy-logic-bugs-how-i-bypassed-two-unbypassable-checks-in-production-systems-2cdea7d56232?source=rss-7f390727575d------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14936 (id 14936)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** Ziadmohammad / Mon, 05 Oct 2026 19:30:13 GMT

*by Ziad Mohammad — Bug Hunter & Security Researcher*

There’s a myth in security research that the best bugs require exotic payloads, zero-days, or deep reverse engineering. Sometimes the best bugs are the opposite: a server that trusts the client a little too much, and a rule that’s enforced in the wrong place.

Here are two real-world examples I found — both business logic flaws, both patched through the applications’ normal flows, and both reduced to “just don’t check the thing where it matters.” Target names are withheld; the mechanics are what matter here.

A major online retailer ran an opt-in “extra deals” campaign: a 20% discount, gated behind a simple rule — **minimum 2 items, minimum €69 total**. Try to check out with less, and a dialog pops up:

*“Below minimum amount — Shop minimum 2 items for minimum 69 € to use the extra deals voucher. By continuing to checkout the discount will be deactivated.”*

Click “Continue,” and sure enough — the discount vanishes. Total goes back to full price. Rule enforced, as designed.

Except it wasn’t enforced. It was *performed*.

The deactivation logic lived entirely behind that dialog’s “Continue” button — a client-side action. So I asked the obvious question: what happens if I just… don’t click it?

**The bypass:**

No dialog. No check. The checkout loaded fully order-ready — billing form, delivery options, payment selection — with the 20% discount still applied to a single item. €99.99 became €79.99. The discounted total wasn’t a UI glitch either; it was baked into the server-side checkout session and survived full page reloads.

**Why it worked:** the eligibility rule was enforced *reactively*, triggered by a specific client-side interaction, instead of being validated *structurally* every time the checkout state was built. Any path that skipped the dialog — a bookmarked URL, a typed address, a browser autofill suggestion — skipped the rule entirely.

**The fix I recommended:** validate campaign eligibility server-side at checkout construction (and again at order placement), based on actual cart state — item count and total — not on which button the user happened to click.

**Severity:** Medium.

The second bug lived in a booking cancellation API, and it’s an even more classic example of the same disease: **the server trusted an identifier it should have re-validated.**

The cancellation request looked like this:

POST /api/.../cancelBooking?url=.../bookings/cancellation/\[BOOKING\_ID\]

Nothing unusual — a standard authenticated cancellation call, with the booking ID embedded in a URL parameter.

The setup: two bookings under one account.

Response:

json

`{"status":"Cancelled Booking"}`
Checked the booking record afterward:

"status": "Cancelled Booking",

"non\_cancelable": true

Not a cosmetic error message — an actual state change. A booking explicitly marked non-cancelable was cancelled, because the endpoint checked “does this user own *a* booking” but never re-checked “is *this specific* booking actually eligible for cancellation right now.”

This is textbook **IDOR-meets-business-logic**: the authorization check (is this your booking?) passed, while the authorization check that actually mattered (is this booking in a cancellable state?) was never run.

**Severity:** Medium — low complexity, no user interaction required, real integrity impact on the booking record.

Strip away the specifics and both reports say the exact same thing:

***A rule was enforced at the point where the user usually interacts with it — not at the point where the system actually commits to it.***

Neither bug needed fuzzing, injection, or a single exotic tool. Just:

It usually doesn’t — because developers test the happy path, and the happy path is exactly where the validation *looks* like it’s working.

If you’re building anything with conditional pricing, cancellation windows, eligibility gates, or any rule that *can* be expressed as “if X, don’t allow Y” — ask where that check actually lives:

If it’s the second one, you have exactly the bug class above, and someone will find it — because, as shown here, it doesn’t take much.
