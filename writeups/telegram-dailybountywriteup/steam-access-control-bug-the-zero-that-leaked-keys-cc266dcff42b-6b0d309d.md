# Steam Access Control Bug

- **Source URL:** https://masimshahzad.medium.com/steam-access-control-bug-the-zero-that-leaked-keys-cc266dcff42b
- **Fetched from:** https://masimshahzad.medium.com/steam-access-control-bug-the-zero-that-leaked-keys-cc266dcff42b?source=rss-440524433a10------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14998 (id 14998)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** Muhammad Asim Shahzad / Tue, 24 Nov 2026 05:03:27 GMT

*AI-assisted: drafted with AI help from public sources, then reviewed and edited. This is an analytical case study of a public disclosure, not my own discovery.*

One number turned a developer portal into a vending machine for other studios’ game keys. In 2018, Artem Moskowsky found a Steam access control bug in Valve’s partner site: asking to download zero keys skipped the ownership check and returned an entire key set, in one test 36,000 Portal 2 keys. Valve fixed it within days and paid $20,000.

***Disclaimer:*** *Educational and defensive use only. This was fixed in August 2018. Reproduction details are intentionally omitted.*

Steam’s partner portal lets developers generate and download activation keys for their games. A download request named a key set and how many keys to take.

Other studios’ key-set IDs returned an error saying he had no assignment for that set. Ownership was being checked. Then he changed the quantity to zero. The check vanished, and the server returned the full contents of the set.

Valve has not published the root cause. A plausible reading is that the ownership test lived inside the “assign N keys” branch, and a count of zero took a different path that went straight to export. That is a classic authorization bug: the check exists, but not on every path to the data.

With key-set IDs guessable and, per the researcher, more than 430,000 sets in existence, one partner account could in principle have pulled every key Steam developers had ever generated.

Steam keys are money: leaked keys get resold on grey markets, and each activation is a lost sale. Valve reports that audit logs still recorded these requests, and that reviewing them showed no prior or ongoing exploitation.

Timeline from the report: submitted and triaged on 7 August 2018, rewarded and resolved on 11 August, publicly disclosed on 31 October.

**1. Authorize first, unconditionally.** Ownership is checked before any parameter decides which code path runs.

**2. Treat edge values as invalid, not special.** Zero, negative, empty and huge counts should fail validation, not mean “everything”.

**3. Keep the audit trail.** It let Valve rule out abuse.

\# Pseudocode: ownership check runs before the quantity can choose a code path

def download\_keys(session, key\_set\_id, count):

key\_set = key\_sets.get(key\_set\_id)

if key\_set is None or not partner\_owns\_app(session.partner\_id, key\_set.app\_id):

audit("key\_download\_denied", session.partner\_id, key\_set\_id)

return deny("not\_found") # same answer for missing or foreign

if type(count) is not int or count \< 1 or count > MAX\_KEYS\_PER\_REQUEST:

return reject("invalid\_count") # 0 is not a shortcut for "all"

keys = key\_sets.allocate(key\_set.id, session.partner\_id, count) # atomic, marks delivered

audit("key\_download", session.partner\_id, key\_set.id, len(keys))

return keys

# Test: foreign set with count=0 -> not\_found; own set with count=0 -> invalid\_count

Found by **Artem Moskowsky** (HackerOne: moskowsky). Primary sources: HackerOne report [#391217, Getting all the CD keys of any game](https://hackerone.com/reports/391217) (Valve’s summary, timeline, rating and reward) and the researcher’s own write-up on [Habr](https://habr.com/ru/articles/421215/) (1 October 2018, in Russian): ownership error, zero-count bypass, 36,000-key example and set count. Facts come from those sources; analysis and code are original.

Next breakdown: another real bug bounty case. Follow @masimshahzad for daily bug bounty breakdowns.
