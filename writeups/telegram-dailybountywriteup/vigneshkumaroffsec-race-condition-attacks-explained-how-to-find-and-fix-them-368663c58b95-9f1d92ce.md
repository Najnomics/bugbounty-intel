# Race Condition Attacks Explained

- **Source URL:** https://medium.com/@vigneshkumaroffsec/race-condition-attacks-explained-how-to-find-and-fix-them-368663c58b95
- **Fetched from:** https://medium.com/feed/@vigneshkumaroffsec
- **Fetched:** 2026-11-24
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14997 (id 14997)
- **Method:** medium-rss-content readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
*Send the same request twice at exactly the same moment, and a “one-time” action can happen twice. That’s a race condition — simple, high-impact, and everywhere money or limits are involved. Here’s how they work, how to test for them, and how to close the gap. Authorized testing only.*

By Vignesh Kumar | Security Researcher

Imagine a gift card worth $100. You redeem it, your balance goes up $100, the card is marked used. Simple. Now imagine you send that redeem request *fifty times at the exact same millisecond*. For a brief instant, before the first request finishes marking the card used, all fifty see a valid, unused card — and all fifty add $100. You walk away with $5,000 from a $100 card.

That’s a **race condition**, and it’s one of the highest-impact, most under-tested classes of web vulnerability. It lives anywhere an application *checks* something and then *acts* on it as two separate steps. This guide explains how they work, their types, where they hide, how to test for them, and the fixes — all for systems **you own or are explicitly authorized to test**, with your own accounts.

### What a race condition actually is

A race condition happens when the outcome of an operation depends on the *timing* of events that are supposed to happen in order — and an attacker can disturb that timing.

In web apps, it almost always takes one shape: **a non-atomic check-then-act.** The code does something like:

1. **Check:** is this coupon unused? Does this account have enough balance? Has this user already voted?
2. **Act:** apply the coupon, subtract the balance, record the vote.

Between step 1 and step 2 there is a tiny window. If a second request runs its *check* inside that window — before the first request’s *act* has committed — both pass the check, and both act. The limit that was supposed to apply once applies twice. This gap between checking a condition and using the result has a classic name: **TOCTOU — time-of-check to time-of-use.**

The whole attack is just: make many requests race into that window at once.

### Why web applications are full of them

Modern apps are built to handle many requests at the same time — multiple server workers, multiple threads, a shared database. That concurrency is the point, and it’s also the exposure. A developer writing “fetch the balance, check it, subtract it” is thinking about *one* request at a time. The database, serving dozens in parallel, isn’t. Unless the check-and-act is made explicitly atomic, the default behavior is a race waiting to be triggered.

### The types of race condition

- **Limit overrun** — using a one-time or N-time action more than allowed: redeem a coupon or gift card repeatedly, claim a signup bonus multiple times, apply a discount twice, exceed a “one per customer” cap.
- **Balance / double-spend** — withdraw or transfer money more than once from the same balance, so it goes negative. The highest-impact variety.
- **Multi-step / state races** — slip between the steps of a workflow to reach a state you shouldn’t (e.g. confirm an order before payment clears).
- **Uniqueness collisions** — two requests both pass a “username available?” check and both register it, or two rows get the same supposedly-unique value.
- **Rate-limit / anti-bruteforce bypass** — fire many authentication or OTP attempts simultaneously so they all read the “attempts so far” counter before any increments it, sliding past the limit.

Different surfaces, same root cause: a check that isn’t fused to the act.

### Where they hide

Look for any endpoint that enforces a limit or a one-time rule:

- **Redeem / apply** — coupons, gift cards, promo codes, referral bonuses, free trials.
- **Money movement** — withdrawals, transfers, purchases, cashouts, point redemption.
- **“One per user” actions** — votes, likes, reviews, claims, RSVP, applications.
- **Account and uniqueness** — registration, username/email claiming, inviting.
- **Counters and limits** — OTP attempts, login attempts, API rate limits, stock/inventory decrements.
- **Multi-step flows** — checkout, KYC, approval chains, anything with “then.”

If the feature’s security depends on “this can only happen X times,” it’s a candidate.

### How to find and test it

The key ingredient is **parallelism** — the requests must arrive as close to simultaneously as possible.

**1. Find a limited action.** Pick something with a one-time or capped rule you can observe the result of — a coupon that should apply once, a balance you can watch, a vote count.

**2. Capture one valid request.** Through an intercepting proxy, grab the exact request that performs the action (the redeem, the withdraw).

**3. Fire many copies at once.** This is the whole technique:

- In **Burp Repeater**, add the request to a group and use **“Send group in parallel”** — it dispatches them together.
- **Turbo Intruder** can launch dozens of requests with tight timing.
- The modern, most reliable method is the **single-packet attack** (below).

**4. Check the result.** Did the action happen more than the limit allowed? Coupon applied five times? Balance went negative? Two accounts with the same “unique” name? That’s the race.

**5. Confirm it’s really the race.** The tell is that it *only* happens under concurrency — one request at a time behaves correctly, a burst breaks it. That contrast is your proof for the report.

### The single-packet attack (why this got easier)

The historic problem with testing races was **network jitter** — even requests sent “together” arrive microseconds apart because of the network, and that’s often enough to miss the window.

In 2023, PortSwigger’s research introduced the **single-packet attack**: using **HTTP/2**, you can pack 20–30 requests into a *single TCP packet*, so the server receives them all at once with essentially zero timing difference between them. (A similar “last-byte synchronization” trick exists for HTTP/1.1.) This neutralized network jitter and made race windows that were once nearly impossible to hit reliably exploitable — which is exactly why race conditions are worth testing today, and worth fixing properly.

### The fix: make check-and-act atomic

Every fix is the same idea: **remove the gap.** The check and the act must happen as one indivisible operation, so a second request can’t slip between them.

**Push the decision into the database**, which is built for exactly this:

-- Vulnerable: read, then (separately) write — two steps, a race window between them

SELECT balance FROM accounts WHERE id = 42; -- app checks balance >= 100

UPDATE accounts SET balance = balance - 100 WHERE id = 42;

-- Fixed: one atomic statement. The condition is enforced at write time;

-- a concurrent request can't double-spend because only one UPDATE can match.

UPDATE accounts SET balance = balance - 100

WHERE id = 42 AND balance >= 100;

-- then check "rows affected": 1 = success, 0 = insufficient funds

Other atomic tools, by situation:

- **Unique constraints** — let the database enforce “one per user” / uniqueness. Two racing inserts can’t both succeed; one gets a constraint violation. This kills collision and limit-overrun races cleanly.
- **Row locks** — SELECT ... FOR UPDATE locks the row so concurrent transactions queue instead of racing.
- **Optimistic concurrency** — a version column; the update only applies if the version matches, and a losing racer retries. Good for high-contention systems.
- **Transaction isolation** — run the critical section at **serializable** isolation so conflicting transactions can’t interleave.
- **Idempotency keys** — require a client-supplied key on sensitive actions and reject duplicates, so a replayed/raced request is a no-op.
- **Application-level locks** — a distributed lock (e.g. in Redis) around the critical section when the logic spans services.

The wrong “fixes” to avoid: a short delay, a client-side disable, or a “check again after” — none remove the window; they just shrink it, and the single-packet attack shrinks right back in.

### Common Mistakes to Avoid

- Testing against systems or accounts you aren’t authorized to use.
- Only sending requests sequentially — a race won’t show without true parallelism.
- Assuming “it’s fast, the window is too small” — the single-packet attack makes tiny windows hittable.
- Checking a condition in application code and acting in a separate statement (the core bug).
- “Fixing” with a sleep, a UI disable, or a second check instead of an atomic operation.
- Relying on a rate limiter that itself reads-then-increments non-atomically.
- Forgetting multi-step flows, where the race is between steps rather than on one endpoint.

### A Quick Race Condition Checklist

- You’re testing limited actions on an authorized target with your own accounts.
- Every “one-time” or capped action is identified: redeem, withdraw, vote, claim, register.
- Each is tested by sending many identical requests in parallel (Burp parallel group / Turbo Intruder / single-packet).
- Results checked for limit overrun: action succeeded more than allowed, balance negative, duplicate “unique” value.
- Confirmed the effect only appears under concurrency, not single requests.
- On the fix side: the check and the act are a single atomic statement or transaction.
- Unique constraints, row locks, or optimistic version checks guard limited resources.
- Sensitive actions accept an idempotency key and reject duplicates.
- No “fix” relies on timing, delays, or client-side controls.

### Final Thoughts

Race conditions are deceptive because the code looks completely correct — read the balance, check it, subtract it, in order. It only falls apart when two requests run that “in order” logic at the same time, and the database lets both pass the check before either commits the act. That’s not a logic error you can spot by reading one request; it’s a concurrency gap you find by *racing* the endpoint and close by making the operation atomic.

If you build or test apps handling money, limits, or one-time actions, do one thing this week: take your most sensitive “can only happen once” endpoint, send it thirty times in parallel, and watch what the limit does. If it holds at one, your check and your act are fused. If it doesn’t, you’ve found the window — and now you know how to close it.

### About me

I’m Vignesh Kumar, a security researcher working across application security, DevSecOps, cloud security, and vulnerability research.

I share practical findings from security assessments and responsible disclosures to help improve the security of real-world systems.

*The techniques in this article are described for defending and testing systems you own or are authorized to assess.*
