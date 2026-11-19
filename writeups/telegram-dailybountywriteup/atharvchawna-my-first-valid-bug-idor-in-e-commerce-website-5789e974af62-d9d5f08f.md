# My First Valid Bug

- **Source URL:** https://medium.com/@atharvchawna/my-first-valid-bug-idor-in-e-commerce-website-5789e974af62?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20251223092908/https://medium.com/@atharvchawna/my-first-valid-bug-idor-in-e-commerce-website-5789e974af62
- **Fetched:** 2026-11-19
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/11900 (id 11900)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# My First Valid Bug: IDOR in E-commerce Website

Finally got my first valid bug after months of learning bug bounty. Not gonna lie, feels amazing after getting so many duplicates and N/A responses.

So I picked this e-commerce website as my target. I wasn’t even signed up yet, just wanted to see how everything works first. Started clicking around the site with my dev tools open because I always keep an eye on what requests are going back and forth. Added a few items to the cart as a guest user and then opened the cart page to see what’s inside.

While the cart page was loading, I noticed this one request in the network tab:

`GET /api/v2/cart/guest_cart_id`
This was pulling all my cart details even though I wasn’t logged in. Makes sense that there is a guest cart feature

But then something clicked in my head what happens if I take this guest cart endpoint and use it with an actual logged-in user’s cart ID instead? Maybe it checks, maybe it doesn’t. Only one way to find out.

I noted down that endpoint and then went ahead and created an account on the site. Added some products to my cart again and opened the cart page. Checked the network tab and saw a different request this time:

`GET /api/v2/user_cart/auth_cart_id`
So they’re using two completely different endpoints. One for guests, one for authenticated users. At this point most people would think okay, they’ve built separate systems for guest and logged-in users, probably secure. I almost moved on too. But inner me told to just try it once.

I copied my authenticated cart ID, went back to that guest cart endpoint, and replaced the guest cart ID with my actual cart ID. Hit send on that request without any authentication headers or cookies.

And Boom. The response came back with everything all the items sitting in my cart, their individual prices, how much tax i will pay, literally everything about my cart. No login needed, no session token, nothing. The endpoint just accepted whatever cart ID I threw at it and gave me the data.

That’s a textbook IDOR vulnerability. The guest cart endpoint had zero authentication checks. It trusted that if you’re asking for a cart ID, you must be allowed to see it.

What got me was how the separate endpoints made it look like they’d thought about security. Like they’d intentionally split guest and authenticated flows. But they forgot to actually verify if someone accessing a cart ID is supposed to access it. The architecture looked good on paper but the actual implementation missed the most important part.

My first bug wasn’t some insane exploitation chain or advanced technique. Just basic testing and not making assumptions. Sometimes that’s all it takes.

Now I’m hunting for the next one. Let’s see what else is broken out there.
