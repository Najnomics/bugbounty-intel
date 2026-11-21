# They Used Tools I Used Logic 0-Click Account Takeover Without Breaking a Sweat

- **Source URL:** https://medium.com/@loayahmed686/they-used-tools-i-used-logic-0-click-account-takeover-without-breaking-a-sweat-fd57c078dc82?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250419083407/https://medium.com/@loayahmed686/they-used-tools-i-used-logic-0-click-account-takeover-without-breaking-a-sweat-fd57c078dc82
- **Fetched:** 2026-11-21
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/9390 (id 9390)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# They Used Tools I Used Logic 0-Click Account Takeover Without Breaking a Sweat

You know how most write-ups start with “I opened Burp Suite…”

Well, not this one.

This is the story of how I took over real user accounts on a live production system **without a single user interaction, no session fixation.**

**and guess what? Not even Burp Suite.**

# Reconnaissance Phase

I began with standard recon techniques and noticed that the target application operated across multiple subdomains, such as:

- `profile.example.com`
- `onboarding.app.example.com`
- `example.com`

Initially, I didn’t pay much attention to the subdomains. But during deeper testing, I stumbled upon something interesting a feature called **“Edit Entry”**.

When I tried accessing it, I was blocked with a message saying I wasn’t authorized and needed to “take ownership” the entry. That piqued my curiosity.

# Digging Deeper

I decided to investigate further. While analyzing the request flow, I came across a very suspicious endpoint on the `onboarding.app.example.com` subdomain:

`onboarding.app.example.com/claiming/{{entry_id}}/verified_claims/{{uuid}}`
This immediately caught my attention. Having a `uuid` in the URL like this seemed odd and potentially insecure

# The Idea That Changed Everything

I reached out to my friend [Ahmed Atef](https://medium.com/u/47bb4db24538?source=post_page---user_mention--fd57c078dc82---------------------------------------) (you can find a detailed technical breakdown on his blog highly recommended if you’re interested in the mitigation and backend logic behind this issue).

Together, we brainstormed and came up with a bold idea:

1. Register a new account.
2. Grab our own `uuid` (which we control).
3. But here’s the catch each account has a related **entry\_id** used to display products or user content.
4. what if we Replace our `uuid` with that of the target account we want to take over , it’s work !

So if we kept using our own `uuid`, but swapped in the `entry_id` of the victim , guess what ?

# Boooooooom Full Account Takeover with 0 User Interaction!

And just like that We were able to take over the account **without any interaction from the victim**. Full access, full control.

Who needs Burp when you’ve got curiosity, a browser, and some good old fashioned creativity and some good friends (make sure to check him out ) ?

# Persistent Token Abuse

One of the most critical aspects of this vulnerability is that the token used to **claim the entry** does **not expire**. Even worse, the same token can be reused **multiple times** without any rate limiting, invalidation, or restriction.

This means that once an attacker obtains a valid token (either through account creation or another method), they can **continuously perform account takeovers** effectively making the attack persistent and scalable. This significantly increases the impact and severity of the vulnerability, as the lack of token expiration or rotation removes any barrier to repeated exploitation.

# Key Takeaways from this one :

1. **Never underestimate a simplelooking endpoint** — A URL like `/claiming/{{entry_id}}/verified_claims/{{uuid}}` might be the gateway to a critical vulnerability.
2. **Manual testing can beat tools** Sometimes, your brain and curiosity reveal more than automated scanners like Burp.
3. **Reusable, non-expiring tokens are a security disaster** Tokens should be short lived, single use, and validated server-side.
4. **Cross subdomain interactions are dangerous if not properly secured** Always verify permissions and access control on every domain.
5. **Understanding and good guessing app logic helps spot flaws** Track how parameters like `uuid` and `entry_id` are used and misused.
6. **Think like an attacker, not a user** Swap values, bend the flow, and test assumptions the developers made.

Feel free to connect with me on [LinkedIn](https://www.linkedin.com/in/loay-ahmed-75ba29231) for more write-ups and technical breakdowns.
