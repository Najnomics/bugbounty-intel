# @mdp_sec — Marius du Preez (requested by Dorothy)

Compiled 11 Nov 2026 (WAT). Full verbatim post text lives under [`posts/mdp_sec/`](../posts/mdp_sec/); full writeups under [`writeups/mdp_sec/`](../writeups/mdp_sec/).

| Field | Value |
| --- | --- |
| X | [@mdp_sec](https://x.com/mdp_sec) (user id 2036270919757471747, joined 2026-03-24) |
| Name (profile) | Marius du Preez |
| Followers (11 Nov 2026) | 5252 |
| Bio (verbatim) | BB Arena: which AI models can really hack? https://t.co/vOXBILNHDr  HuntDeck: every bb platform on one board. https://t.co/3PaspAobXP   Hunting on @Hacker0x01 @Bugcrowd |
| Specialty | Web / API |
| Platforms | HackerOne (mdpsec / marius_dp), Bugcrowd (marius_dp), HackenProof (MDPSEC) |
| Evidence of valid finds | mdpsec.com (fetched, see writeups/mdp_sec/mdpsec-home.md) states 582 reports, 148 critical, 263 high. Posts in this folder include a $4,000 unauthenticated SQLi, an $8,000 HackerOne auth bypass, and a $1,200 Bugcrowd dependency-confusion payout. Builds BB Arena (AI-vs-black-box-lab benchmark) and HuntDeck. |
| Links | https://mdpsec.com, https://github.com/mdpsec/bug-bounty-hunting-prompts |

## Key findings and analysis

### Unauthenticated SQL injection in a public quote flow ($4,000)

- Post: https://x.com/mdp_sec/status/2120066429223317560 — verbatim: [`posts/mdp_sec/2026-11-10-2120066429223317560.md`](../posts/mdp_sec/2026-11-10-2120066429223317560.md)
- **Bug class:** SQL injection (write-then-read-back / second-order style) → PII + resume-token disclosure
- **Root cause:** A JSON field on a public "retrieve" endpoint was concatenated into a SQL string literal; the endpoint had zero auth (its own API spec said so); one shared backend table served several front ends, so the blast radius covered the whole quote system.
- **How it was found:** Posted a JSON body to the public retrieve endpoint, injected into the field to stage a quote under a reference he controlled, then fetched that reference back — the field returned already evaluated by the DB, exposing selected columns (names, emails, phones, addresses, resume tokens).
- **Takeaways:** His tip: in any "come back to your saved thing later" flow, go straight for lookup fields; if one field writes and another reads it back, treat it as an oracle. Read API specs for endpoints marked unauthenticated.

### /./ path normalisation past a login wall into an admin console

- Post: https://x.com/mdp_sec/status/2120338219841544604 — verbatim: [`posts/mdp_sec/2026-11-11-2120338219841544604.md`](../posts/mdp_sec/2026-11-11-2120338219841544604.md)
- **Bug class:** Auth bypass via path normalisation mismatch
- **Root cause:** The login check matched the exact raw path, but the router normalised the path afterwards, so /admin/./ failed the exact match yet still routed to /admin.
- **How it was found:** Testing path variants (/./, //, %2e, trailing slash) against protected prefixes.
- **Takeaways:** Whenever auth middleware and router parse paths differently, try dot-segments and encodings; check every layer (proxy, middleware, framework router).

### $8,000 auth bypass on HackerOne — token signature not verified

- Post: https://x.com/mdp_sec/status/2118435683329310786 — verbatim: [`posts/mdp_sec/2026-11-05-2118435683329310786.md`](../posts/mdp_sec/2026-11-05-2118435683329310786.md)
- **Bug class:** Auth bypass / broken JWT-style token validation
- **Root cause:** The server accepted tokens without verifying their signature, so a forged/modified token was trusted.
- **How it was found:** Tampering with token claims and signatures (strip, alter, re-sign with none/self key) and checking whether the server still accepts them.
- **Takeaways:** Always test whether signatures are actually verified, not just parsed.

### $1,200 Bugcrowd dependency confusion

- Post: https://x.com/mdp_sec/status/2118803107119325691 — verbatim: [`posts/mdp_sec/2026-11-06-2118803107119325691.md`](../posts/mdp_sec/2026-11-06-2118803107119325691.md)
- **Bug class:** Supply chain / dependency confusion
- **Root cause:** An internal package name used by the target was unclaimed on the public registry, so a public package with that name could be pulled by builds.
- **How it was found:** Harvesting package names (JS bundles, manifests, errors) and checking them against the public registry.
- **Takeaways:** Claim-check every internal package name you find; report with a benign callback-only PoC per program rules.

### Two-account IDOR/BAC testing checklist

- Post: https://x.com/mdp_sec/status/2118526280379343189 — verbatim: [`posts/mdp_sec/2026-11-06-2118526280379343189.md`](../posts/mdp_sec/2026-11-06-2118526280379343189.md)
- **Bug class:** Methodology: access control (IDOR/BOLA)
- **Root cause:** N/A – methodology post.
- **How it was found:** Create a private record as account A, read/modify as account B, share then revoke, retest.
- **Takeaways:** A repeatable A/B access-control loop; the revoke step catches stale-permission bugs.

### Bugcrowd vs HackerOne duplicate handling

- Post: https://x.com/mdp_sec/status/2094614973146448108 — verbatim: [`posts/mdp_sec/2026-09-01-2094614973146448108.md`](../posts/mdp_sec/2026-09-01-2094614973146448108.md)
- **Bug class:** Platform process
- **Root cause:** N/A – comparison of how duplicates are handled.
- **How it was found:** Experience from moving volume from Bugcrowd to HackerOne.
- **Takeaways:** Know each platform's dupe policy before choosing where to spend time.

## All captured posts (verbatim files)

- 2026-11-10 — i found an unauthed sql injection that let me pull customer pii and resume tokens off a public quote flow. pai — [`posts/mdp_sec/2026-11-10-2120066429223317560.md`](../posts/mdp_sec/2026-11-10-2120066429223317560.md) · https://x.com/mdp_sec/status/2120066429223317560
- 2026-11-11 — one /./ in the path walked me straight past a login wall into an admin console — [`posts/mdp_sec/2026-11-11-2120338219841544604.md`](../posts/mdp_sec/2026-11-11-2120338219841544604.md) · https://x.com/mdp_sec/status/2120338219841544604
- 2026-11-05 — $8,000 for an auth bypass — [`posts/mdp_sec/2026-11-05-2118435683329310786.md`](../posts/mdp_sec/2026-11-05-2118435683329310786.md) · https://x.com/mdp_sec/status/2118435683329310786
- 2026-11-06 — $1,200 for a package name nobody had claimed. dependency confusion, my only paid supply chain bug. Thx @Bugcro — [`posts/mdp_sec/2026-11-06-2118803107119325691.md`](../posts/mdp_sec/2026-11-06-2118803107119325691.md) · https://x.com/mdp_sec/status/2118803107119325691
- 2026-11-06 — two accounts and a private record is where id start on my own app @cursor_ai — [`posts/mdp_sec/2026-11-06-2118526280379343189.md`](../posts/mdp_sec/2026-11-06-2118526280379343189.md) · https://x.com/mdp_sec/status/2118526280379343189
- 2026-11-06 — hunters who got paid this week 👇 — [`posts/mdp_sec/2026-11-06-2118593724624023616.md`](../posts/mdp_sec/2026-11-06-2118593724624023616.md) · https://x.com/mdp_sec/status/2118593724624023616
- 2026-09-01 — I have spent most of my time hunting on @Bugcrowd — [`posts/mdp_sec/2026-09-01-2094614973146448108.md`](../posts/mdp_sec/2026-09-01-2094614973146448108.md) · https://x.com/mdp_sec/status/2094614973146448108
- 2026-11-09 — BB Arena v2 is live. 100 new private black-box labs, and it's a lot harder — [`posts/mdp_sec/2026-11-09-2119670856075166075.md`](../posts/mdp_sec/2026-11-09-2119670856075166075.md) · https://x.com/mdp_sec/status/2119670856075166075
- 2026-11-09 — claude fable 5.1 refused all 100 of my black-box hacking labs — [`posts/mdp_sec/2026-11-09-2119885234887876972.md`](../posts/mdp_sec/2026-11-09-2119885234887876972.md) · https://x.com/mdp_sec/status/2119885234887876972
- 2026-11-02 — Comments be brutal... — [`posts/mdp_sec/2026-11-02-2117342079303205204.md`](../posts/mdp_sec/2026-11-02-2117342079303205204.md) · https://x.com/mdp_sec/status/2117342079303205204

## Writeups saved (full text)

- [`writeups/mdp_sec/bug-bounty-hunting-prompts-readme.md`](../writeups/mdp_sec/bug-bounty-hunting-prompts-readme.md)
- [`writeups/mdp_sec/mdpsec-home.md`](../writeups/mdp_sec/mdpsec-home.md)
