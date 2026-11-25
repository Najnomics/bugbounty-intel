# When "We Added an Allowlist" Doesn’t Mean What You Think It Means

- **Source URL:** https://medium.com/@joashraf2005/when-we-added-an-allowlist-doesnt-mean-what-you-think-it-means-c2d7d9b09e01
- **Fetched from:** https://medium.com/@joashraf2005/when-we-added-an-allowlist-doesnt-mean-what-you-think-it-means-c2d7d9b09e01?source=rss-0a4272abb611------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14922 (id 14922)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** Joashraf / Thu, 24 Sep 2026 03:14:04 GMT

Hello Hacker’s,

I want to walk through a bug I found on a session replay platform not because it paid out (it didn’t), but because the back-and-forth with the vendor was a clean lesson in how companies think they’ve fixed something, versus what they’ve actually done.

If you hunt bugs long enough, you start noticing a pattern: a vendor gets a report, ships a fix, and the fix looks right. It has the shape of a fix. There’s a new setting, a new list, a new checkbox. But the underlying trust model never actually changed they just moved the goalposts to somewhere that felt safer. This is a writeup about catching that exact moment.

**The setup**

The target had a session replay feature the kind of tool that records what real users do on a website (clicks, scrolls, form fills) and lets the site owner watch it back later, like a screen recording of someone’s session.

To wire this up, customers drop a small JS snippet into their site. That snippet carries a site key (sr\_...) so the backend knows which customer’s dashboard a given session belongs to.

Here’s the detail that mattered: that key lives in the page source. Anyone who views-source on a customer’s site can copy it out. That’s not a bug in itself it’s just how these SDKs work, the same way a Google Analytics ID or a Stripe publishable key is public by design. The bug is in what you let that key do.

**First pass: no gate at all**

I grabbed my own site key from the dashboard and just... posted directly to the ingest endpoint. No browser, no JS, just curl:

curl -X POST "https://ds.example-vendor.app/api/v1/session-replay/ingest" \

-H "User-Agent: Mozilla/5.0 (X11; Linux x86\_64) Chrome/126.0.0.0" \

-H "Origin: https://victim-domain.com" \

-H "X-SR-Site-Key: sr\_YOUR\_KEY" \

-H "X-SR-Visitor-Id: 11111111-2222-4333-8444-555555555555" \

-H "Content-Type: application/json" \

-d '{"type":"snapshot","session\_id":"22222222-3333-4444-5555-666666666666",

"chunk\_index":0,"event\_count":1,

"meta":{"user\_email":"attacker@evil.com","user\_id":"9999",

"url":"https://victim-domain.com","device\_type":"desktop",

"screen\_width":1920,"screen\_height":1080},

"events":\[{"type":4,"data":{"href":"https://victim-domain.com",

"width":1920,"height":1080},"timestamp":1725134400000}\]}'

It worked first try. A completely fabricated session fake email, fake user ID, fake everything showed up live in my dashboard, indistinguishable from a real visitor recording.

The takeaway here isn’t clever. If a key is exposed by design, and that key is the only thing gating a write endpoint, you should always try calling that endpoint directly, outside the browser, and see what sticks. This is one of the first things I try on any product with a "drop-in snippet" model chat widgets, analytics, replay tools, feedback widgets. The pattern repeats across a lot of SaaS products because the SDK design is basically the same everywhere.

**The vendor’s fix, and why I didn’t stop testing:**

They added an allowed origins list per site key. Reasonable-sounding fix. My first instinct, honestly, was to assume it worked and move on a lot of hunters would’ve closed the tab here.

But I’d already flagged the key as public-by-design, and this new control lived on top of a header Origin and I know from experience that "header-based" and "browser-enforced" aren’t the same claim unless you check who’s actually sending the request.

Here’s the mental model that’s worth internalizing: Origin is trustworthy only in requests a real browser sends on behalf of a page it loaded. A browser won’t let JavaScript lie about it. But nothing stops me from setting whatever Origin I want in a raw HTTP request. The header only means something in the context that enforces it.

So I just... set it

-H "Origin: https://victim-domain.com"

Same forged payload, same endpoint. It went through. Full snapshot, events, session-end, all 200. I checked it wasn’t a fluke on my own account by testing it against the vendor’s own production site key too same result.

**This is the actual lesson for bug hunters:**

when a vendor patches something by adding a header check, your very next move should be "can I just set that header myself?" It sounds too simple to work, and that’s exactly why it keeps working. A huge number of "fixed" reports on public disclosure sites are really just this someone added a check, nobody asked who controls the value being checked.

**Reporting the bypass:**

I didn’t just say "it’s broken" I gave them the full chain: the request, the response, the session appearing live in the dashboard, and I explicitly named the root cause instead of leaving them to guess:

Origin allowlisting is a CORS-style browser control, not a server-side authentication mechanism.

That distinction CORS vs. auth is worth having in your back pocket as a phrase. It’s precise, it’s not accusatory, and it tells the triager exactly what mental model they got wrong without making them feel stupid. Reports that name the category of mistake, not just the instance of it, tend to get taken more seriously.

**Where it landed and why no bounty:**

This is the part I think is more useful than the bug itself.

The vendor’s final response didn’t deny anything. They agreed the origin check I originally bypassed was broken turns out an empty allowlist had been failing open (accepting everything) instead of failing closed, and that was the real defect they fixed. But then they made an argument I didn’t fully see coming:

They said the site key was never meant to authenticate only to identify and that Origin, despite my bypass, remained the best authentication signal they had for unauthenticated browser SDKs. What actually changed on their end wasn’t "we trust Origin now," it was: we accept that a leaked key can inject data, so let’s bound the blast radius. Rate limits per key. Quota isolation, so forged traffic can’t eat into a real customer’s storage. Treating every field the SDK sends as an unverified claim, not a fact. Anomaly detection on ingest volume. And an optional signed-ingest mode a short-lived, session-bound token minted server-side for any customer who wants real cryptographic proof instead of trusting Origin at all.

They didn’t make it mandatory, and honestly, that’s the correct call forcing every customer to run a backend signer would break every simple drop-in install, which is half the value proposition of the product.

They closed it P3:

data-integrity-within-one-workspace, no cross-tenant reach, no read access to stored data.

I sat with that for a bit before accepting it. My instinct as a hunter is to want the "big" outcome critical severity, big payout, clean win. But their reasoning actually holds up: once you strip away the false sense of security the Origin check gave them, and replace it with genuine containment (rate limits, quotas, anomaly detection), the actual damage a leaked key can do is small and contained. I found a real flaw in their reasoning, and they fixed the reasoning without giving me the payout, because the practical risk was always lower than the initial report made it sound.

**What I’d Tell Another Hunter:**

If I were chasing this pattern again, the first thing I’d do is hit any endpoint that can be reached with a public or embedded key directly, outside the browser.

SDK-based products are especially interesting here replay, analytics, chat, feedback, error tracking, and similar services tend to expose ingestion endpoints that are worth looking at.

Another thing I learned from this is to pay attention to who actually controls the headers involved in a security check.

If a fix relies on a header such as **Origin**, **Referer**, **X-Forwarded-For**, or a **custom X-Client-\*** header, ask yourself whether the attacker can simply send the request themselves.

A header being present doesn’t automatically make it an authentication mechanism. What matters is whether something the attacker cannot control is actually enforcing the trust boundary.

I also think there’s an important difference between a fix and a mitigation.

When a vendor says they’ve "bounded the impact" or added additional protections around the issue, that’s different from saying the underlying attack path has been completely removed. Paying attention to that wording can give you a better idea of how the vendor understands the remaining impact.

And finally, not every technically valid finding is going to result in a big payout.

That doesn’t necessarily mean the finding was wrong. In this case, the bypass was real, the reasoning behind it was sound, and the vendor ultimately treated it as low severity after limiting the impact.

For me, that’s still a useful result.

Finding the technically correct issue is worth doing even when the bounty doesn’t turn out the way you expected. More importantly, findings like this teach you how to look at the next vendor’s fix and ask whether they actually removed the vulnerability or simply reduced what an attacker can do with it.
