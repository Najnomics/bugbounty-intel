# “Trust ’em — let the app handle it!”

- **Source URL:** https://medium.com/@mohammadsoubanliaqat/trust-em-let-the-app-handle-it-983156cea5c0
- **Fetched from:** https://medium.com/@mohammadsoubanliaqat/trust-em-let-the-app-handle-it-983156cea5c0?source=rss-557be0ddc7e0------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14956 (id 14956)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** Mohammad Souban Liaqat / Thu, 22 Oct 2026 10:38:03 GMT

The mindset after cracking 10 PortSwigger business-logic labs.

Scanners habitually scan code but not intent. Assumptions are what gives birth to logical flaws. From price manipulation to unauthorized admin access, logical errors are hiding everywhere. After crushing 10 labs, here are the questions I ask before blindly trusting what the rules say:

1.“Who says the client is telling the truth?”

The browser’s validation is the gate, so whatever arrives at the server is already clean.

The browser was not allowing me to enter a negative, decimal or fractional value, which proved the controls were properly enforced on the front end.

I tried intercepting the request and changing the price parameter value which the server happily accepted.

What if the validation was just happening at the cart’s total and not on the arithmetic calculation?

I tried multiple types of unconventional inputs but server-side validation was rejecting it every time.

Finally, I kept removing the product from the cart making the cart’s total go negative.

Then I started adding another product to such an extent that cancels out that negative total by the second product’s total.

This resulted in purchasing any arbitrary item at an unintended price.

Every user supplied input must be verified on the server-side before processing and the server must also avoid trusting client’s math.

2\. “Are the rules enforced — or just stated?”

No need to burden the server with checks — the user is already authenticated.

I tried registering ‘administrator’ which was already taken, so some check existed.

The back-end was not allowing me to create a user that already existed. So I tried to create a new user using the provided mail followed by dontwannacry.com, which didn’t work either.

I logged in with provided credentials and just updated my email to attacker@dontwannacry.com. The login panel appeared immediately.

What if the server doesn’t care about the necessary parameters?

I logged in my account using the provided credentials and tried to change the password.

Captured the POST request carrying the username, current password, new password, and confirm new password parameters.

Modified the request in such a way by changing username to ‘administrator’ and removing the ‘current password’ parameter entirely, which changed the administrator’s account password and allowed me to login.

Security controls must be enforced consistently where a privileged action is going to happen — whether it’s the email change, or the password POST.

3\. “What if the number is negative — or absurd?”

This data type is sufficient here, nobody would want to cross it.

I tried ordering an item which exceeded my current balance, used negative and real numbers also in the quantity parameter, but the server gracefully handled these quirks.

As soon as I tried to put a number greater than 99, I noticed that I can’t add more than 99 units in the cart at one time.

I kept on adding 99 units to study how the server behaves if a user tried to order more items than the available stock.

Upon a certain limit, the cart total wrapped to the negative values — confirming an integer overflow.

19,899 × $1,337. The total went backwards.

I started to adjust the cart so that it reached a point where it became non-negative, below my available balance.

Emails typically are under 255 characters.

Initially, I tried registering ‘administrator’ on my provided mail, with and without case randomization.

Then I tried URL, Base-64 and HTML encoding also but the back-end checks wouldn’t allow me to register administrator on a different mail.

Finally, I came to know that upon entering an exceptionally long mail, the back-end only cared about the first 255 characters — stripping away the remaining ones.

I carefully tried to craft such a mail that the last character of dontwannacry.com would be exactly at 255th character. In this way, I became successful in creating an account on my email while being able to login in without putting the remaining characters.

Boundaries must be implemented properly and never be assumed, so that any unconventional input can’t expose another attack surface.

4\. “Does the server know which step I’m on?”

Every step is followed by previous one, so no need to verify each step individually.

I followed along the whole workflow and noticed that there are only 3 steps in total.

I added an item into the cart (Step 1), and instead of doing checkout (Step 2), I just replayed the confirm order GET request (Step 3).

Admin interface only available if logged in as administrator.

I completed the login workflow. Noted that there are four steps in this workflow. POST /login → GET /role-selector → POST /role-selector → GET /

I tried to directly modify the role parameter by setting “role=admin” in the POST /role-selector request.

Then I tried to forcefully introduce the same role parameter in the POST /login request but failed.

What I didn’t think of was to skip the role-selector step entirely.

Upon attacking the workflow itself by skipping the GET /role-selector request and directly accessing the GET /admin endpoint right after the POST /login, I managed to break into the admin’s panel.

No role-selector. Straight from /login to /.

Each step in the workflow must be validated properly so that no one can skip, repeat or reorder steps in the workflow.

5\. “What if I obey every rule — and still win?”

Each rule is properly enforced, the app will not misbehave — even on combining multiple rules.

I tried redeeming the coupon multiple times but some check restricted the coupon to be redeemed more than once.

I suspected that the coupon might be tied to csrf-token instead of a particular user account. Even a fresh csrf token failed.

I tried to perform a race-condition attack to determine whether the check is actually getting enforced on back-end or not.

Eventually, I scrolled down and found a “Sign up to newsletter” functionality. Upon signing up, I was handed another coupon.

I tried coupon1 → coupon2 → coupon1 → coupon2 and so on, which confirmed the check was confined only to prevent the usage of same coupon consecutively — not permanently.

The alternation stack. Total: $0.00.

Credit issued can never exceed value paid.

First of all, I tested how the “redeem” functionality actually worked. I tried to use the same gift card code before and after changing my email address to determine if the functionality is tied to email.

I purchased a bunch of gift cards. After applying the coupon, the price of each gift card reduced to 7$ — crediting 10$ on redeem.

I continued repeating the same process and noticed that the coupon didn’t expire after one-time use. Instead it remained valid crediting more money than it took.

Rules must be enforced per account, and discounts must not give away more than what they cost.

Mindset for your next hunt

Always start by exploring the application first, pay close attention to nearby features or how they can be combined or manipulated before testing the functionality.

When a test fails, change strategy instantly. Don’t dig deeper to prove the bug exists.

When the page validates something, ask who enforces it by manipulating it.

Try unconventional inputs or breaking the limits that the developer might have assumed, such as supplying 256 characters on email or name fields and checking out more than the available stocks.

Study the workflow first, then try skipping steps, doing them in reverse order, redoing or changing the order of steps of the workflow.

If the app uses multiple parameters in different steps of a workflow, try manipulating them also. This may include forcefully adding or removing parameters, supplying a single steps’ parameter to another step and supplying more values than expected. At times, effect of parameter manipulation may show up stages later.

Find the invariant the business depends on, then try to break it in one action.

If possible try to automate the steps that need to be performed repeatedly.

The labs handed me the assumptions on a plate — they were intentionally broken. Real targets won’t be that generous. Most of these questions will hit nothing, and that’s fine: misses are cheap, and one hit pays for all of them. What I’m carrying to live VDPs isn’t the bugs — it’s the habit. First question on my next target: who enforces what the page validates?
