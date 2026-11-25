# Password reset link stays valid after requesting a new one (old token not invalidated on reissue)

- **Source URL:** https://medium.com/@jokodfir/password-reset-link-stays-valid-after-requesting-a-new-one-old-token-not-invalidated-on-reissue-4af0fb651a1c
- **Fetched from:** https://medium.com/@jokodfir/password-reset-link-stays-valid-after-requesting-a-new-one-old-token-not-invalidated-on-reissue-4af0fb651a1c?source=rss-637030b9c7b7------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14934 (id 14934)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** Joko Purwanto / Mon, 05 Oct 2026 04:18:12 GMT

Assalamualaikum wr.wb.

Bismillah

This is my sixteenth article, I hope it proves useful to readers.

While looking at the password reset flow, I noticed something that’s easy to miss because it only shows up if you actually keep an old reset link around: requesting a new “forgot password” email does not invalidate the previous one. Both links stay live at the same time, and either one can be used to take over the account, right up until one of them actually gets used.

That matters because a reset link is effectively a bearer credential for the account — anyone holding it can set a new password and get signed in immediately, no further verification. If an old link ever ends up somewhere it shouldn’t (a compromised mailbox that’s since been secured, a link cached by a mail scanner, a shared computer’s browser history, an old email search index), it should stop being useful the moment the legitimate user asks for a fresh one. Right now it doesn’t.

The realistic scenario this opens up: someone (attacker, or a mail provider’s link-prefetching bot, or anyone else) gets hold of an old, unused, not-yet-expired reset link — say, from a period where the account’s mailbox had been compromised or shared, which has since been locked back down. Today, the account owner requesting a brand new reset link for themselves does nothing to shut that old link off. It’s still live until it’s actually used by someone (attacker or owner, whoever gets there first) or until its own individual \~24-hour window runs out. That’s a real gap in the “I think I’ve secured my account” moment — the fix a user would reasonably expect (ask for a fresh link, ignore the old one) does not actually invalidate the old one.

I’ll say plainly that this is a narrower finding than some other reports I’ve submitted from this same hunt — it needs a specific precondition (an attacker already has an old, valid, unused link from some earlier point) rather than being exploitable from a cold start. I’m not claiming more than that.

Also worth noting, since it’s part of the same flow: the token itself (prq= value) is very high-entropy (\~490 bits, hex-encoded) — nowhere near brute-forceable, and not the concern here. The issue is purely about how many of these otherwise-strong tokens are allowed to be simultaneously valid, not the strength of any individual one.

When a new password-reset token is issued for an account, invalidate every other outstanding, unused reset token for that same account at that moment — not just when one of them gets consumed. This is usually a one-line change if tokens are tracked with an issued\_for\_user\_id + used/invalidated flag: on issuing a new one, mark all prior unused ones for that user as invalidated in the same transaction.
