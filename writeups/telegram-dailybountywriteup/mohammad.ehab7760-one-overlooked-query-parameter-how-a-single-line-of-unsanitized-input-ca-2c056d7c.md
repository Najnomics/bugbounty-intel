# One Overlooked Query Parameter

- **Source URL:** https://medium.com/@mohammad.ehab7760/one-overlooked-query-parameter-how-a-single-line-of-unsanitized-input-can-undo-a-platforms-entire-9a1742755550
- **Fetched from:** https://medium.com/@mohammad.ehab7760/one-overlooked-query-parameter-how-a-single-line-of-unsanitized-input-can-undo-a-platforms-entire-9a1742755550?source=rss-a8121c8ce626------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14910 (id 14910)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** Mohammed Ehab / Sun, 13 Sep 2026 21:38:25 GMT

*A field note from a penetration tester on discovering — and responsibly disclosing — a reflected XSS vulnerability on a live job-search platform.*

Every once in a while, you stumble onto a vulnerability while doing absolutely nothing sophisticated. No custom tooling, no exotic bypass chain, no zero-day research. Just… browsing. That’s exactly how this one happened.

I wasn’t hunting. I was job-hunting — literally scrolling through listings on a public job-search platform used by startups and job seekers alike. Somewhere between filtering locations and skimming postings, something in the URL bar caught my eye: a search parameter that looked a little too trusting of whatever I typed into it.

So I typed something into it.

**A JavaScript alert box popped up.**

That’s the moment every penetration tester knows well — the small, almost comedic “it actually worked” jolt that turns a casual afternoon into a disclosure timeline.

The vulnerability itself is a textbook case of **Reflected Cross-Site Scripting (XSS)** — one of the oldest and most well-documented vulnerability classes on the web, and yet still one of the most common findings in real-world bug bounty programs today, more than two decades after it was first described.

Here’s the core issue, stripped down to its essence: a value the user types into a search field gets echoed back into the page — into the visible content, and in this case even into the browser tab’s title — without the platform properly encoding special characters like \<, >, or " first. Normally, a browser treats those characters as inert text. But if a server reflects them back *unescaped*, the browser instead interprets them as live HTML and JavaScript. In other words, one specially-crafted link is enough to make your browser execute code that came from someone else, while still believing it came from a trusted site.

While digging around the platform a bit further, I also noticed a second, related weak point: a user-facing profile field that appeared to store special characters without proper sanitization either. Two independent findings pointing to the same underlying gap is rarely a coincidence — it usually means input handling wasn’t treated as a first-class security concern across the codebase, not just in one form.

A JavaScript alert() popping up looks harmless — almost like a party trick. But it's a proof-of-concept, not the actual attack. In the hands of someone with different intentions, that same injection point could instead be used to:

This is precisely why reflected XSS, despite requiring “just” a crafted link and a click, is consistently rated as a serious — sometimes critical — vulnerability class. The browser’s entire security model is built around trusting content that comes from a given origin. Reflected XSS breaks that trust from the inside.

I did what responsible disclosure is supposed to look like: I stopped at proof-of-concept. No session hijacking, no data exfiltration, no attempts to pivot the finding into something bigger than it needed to be to prove impact. I documented:

…and sent the full report directly to the platform’s support team, requesting it be routed to whoever owns security there.

At the time of writing, the report is still under review, which is exactly why you won’t find the platform’s name, its URL, or the exact payload anywhere in this article. Publishing exploit-ready details for a vulnerability that hasn’t been fixed yet doesn’t help anyone — it just hands a working attack to whoever reads it first. If and when the issue is resolved, that’s a conversation for a different, more detailed follow-up.

If you’re building web applications: **never trust a “we’ll just skip it, it’s a small field” moment.** Every place user input touches your rendered HTML — a search box, a profile name, a comment field, even something as unassuming as a page title — is a potential injection point. Output encoding isn’t a “nice to have” bolted on later; it has to be the default behavior for anything user-controlled.

If you’re breaking web applications for a living (or for fun, responsibly): don’t underestimate the boring-looking parameters. Some of the most impactful findings I’ve come across didn’t need custom tooling or novel research — they needed someone to actually look at what a query parameter does with what you give it.

Sometimes the most dangerous line of code isn’t the one doing something complex. It’s the one that was never told *not* to trust you.

*I’m a penetration tester focused on web application security and Active Directory attack simulation. If you’re a platform owner reading this and think this might be about you — reach out to your own security team first. Chances are, you already know the fix.*
