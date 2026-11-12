# @mdp_sec — Marius du Preez (requested by Dorothy)

Compiled 11 Nov 2026 (WAT). This is the most fully-documented researcher in the repo. Full verbatim post text: [`posts/mdp_sec/`](../posts/mdp_sec/) (422 files). Writeups, site pages, platform report metadata and his full prompt pack: [`writeups/mdp_sec/`](../writeups/mdp_sec/). Harness material derived from his workflow: [`harness/`](../harness/).

| Field | Value |
| --- | --- |
| X | [@mdp_sec](https://x.com/mdp_sec) (user id 2036270919757471747, created 2026-03-24 UTC) |
| Name | Marius du Preez |
| Location | Australia |
| Site | https://mdpsec.com (static marketing site — no report listing) |
| Specialty | Web / API — web apps, APIs, cloud backends, Android, business logic, access control |
| Platforms | HackerOne (`mdpsec`), Bugcrowd (`marius_dp`), HackenProof (`MDPSEC`) |
| Also builds | BB Arena (blackboxarena.ai, AI-vs-black-box-lab benchmark), HuntDeck; GitHub `mdpsec/bug-bounty-hunting-prompts` and `mdpsec/should-i-submit` |

## Report counts — full vs metadata-only vs missing (exact)

His site claims **582 reports submitted, 148 critical, 263 high, across 5 platforms** (self-reported aggregate, last updated Oct 2026). The site has no per-report listing, no reports page, and no data API — only a `/security-test/` lead form (`/api/apply`). So almost all 582 are **undisclosed private-program reports** with no public detail anywhere. Breakdown of what is actually retrievable:

| Source | Reports | Full detail | Metadata only | Notes |
| --- | --- | --- | --- | --- |
| **HackerOne** `mdpsec` | 24 resolved | 0 | 15 (hacktivity) | 0 publicly disclosed. 15 hacktivity entries give program + internal id only; 2 show a bounty ($100 goldmansachs, $842 stripe). Rep 849, rank 2739, signal 6.52. |
| **HackenProof** `MDPSEC` | 15 paid | 0 | 15 (counts) | 0 disclosed. Severity split: 3 critical, 3 high, 6 medium, 3 low. Rank 104, rep 966, 29 influenced programs. |
| **Bugcrowd** `marius_dp` | unknown | 0 | 0 | Profile gated behind the authenticated hacker portal; no public per-report data retrievable on 2026-11-11. |
| **X (@mdp_sec)** | — | ~a dozen with technique | the rest | His own posts are the only place with real vulnerability detail; the detailed ones are analysed below. |

**Exact counts.** Full report detail available publicly: **0** disclosed platform reports. Metadata-only: **30** (15 HackerOne hacktivity + 15 HackenProof paid-report severity rows). Missing / undisclosed with no public metadata: the remainder of his self-reported 582 (i.e. ~552, including all Bugcrowd and the ~9 HackerOne resolved reports not in hacktivity). The platform figures are in [`writeups/mdp_sec/platform-reports.md`](../writeups/mdp_sec/platform-reports.md) and `.json`.

His own earliest retrievable post (2026-07-22) states: "$83,088 from bug bounties in my first 151 days. 203 reports since my first submission on 20 February." See [`posts/mdp_sec/2026-07-22-2079869121513378138.md`](../posts/mdp_sec/2026-07-22-2079869121513378138.md).

## X capture

His full retrievable original-post timeline was captured verbatim: **422 post files** spanning **2026-07-22 → 2026-11-11**. The X timeline API returns no posts older than 2026-07-22 (its reach limit), so his 2026-03-24 → 2026-07-21 posts are not retrievable ("as far as search allows"). Each file includes the full long-form/note text, media, quoted posts and his own self-reply thread.

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

## Writeups, site pages, platform data and prompt pack (full text)

- [`writeups/mdp_sec/bug-bounty-hunting-prompts-readme.md`](../writeups/mdp_sec/bug-bounty-hunting-prompts-readme.md)
- [`writeups/mdp_sec/mdpsec-home.md`](../writeups/mdp_sec/mdpsec-home.md)
- [`writeups/mdp_sec/mdpsec-privacy.md`](../writeups/mdp_sec/mdpsec-privacy.md)
- [`writeups/mdp_sec/mdpsec-security-test.md`](../writeups/mdp_sec/mdpsec-security-test.md)
- [`writeups/mdp_sec/platform-reports.md`](../writeups/mdp_sec/platform-reports.md)
- [`writeups/mdp_sec/should-i-submit-readme.md`](../writeups/mdp_sec/should-i-submit-readme.md)
- [`writeups/mdp_sec/prompts/ADAPTATION.md`](../writeups/mdp_sec/prompts/ADAPTATION.md)
- [`writeups/mdp_sec/prompts/SECURITY.md`](../writeups/mdp_sec/prompts/SECURITY.md)
- [`writeups/mdp_sec/prompts/phases/phase-00-recon.md`](../writeups/mdp_sec/prompts/phases/phase-00-recon.md)
- [`writeups/mdp_sec/prompts/phases/phase-01-access.md`](../writeups/mdp_sec/prompts/phases/phase-01-access.md)
- [`writeups/mdp_sec/prompts/phases/phase-02-sweep.md`](../writeups/mdp_sec/prompts/phases/phase-02-sweep.md)
- [`writeups/mdp_sec/prompts/phases/phase-03-closeout.md`](../writeups/mdp_sec/prompts/phases/phase-03-closeout.md)
- [`writeups/mdp_sec/prompts/phases/phase-04a-scope.md`](../writeups/mdp_sec/prompts/phases/phase-04a-scope.md)
- [`writeups/mdp_sec/prompts/phases/phase-04b-browser-walk.md`](../writeups/mdp_sec/prompts/phases/phase-04b-browser-walk.md)
- [`writeups/mdp_sec/prompts/phases/phase-05a-scope.md`](../writeups/mdp_sec/prompts/phases/phase-05a-scope.md)
- [`writeups/mdp_sec/prompts/phases/phase-05b-critical.md`](../writeups/mdp_sec/prompts/phases/phase-05b-critical.md)
- [`writeups/mdp_sec/prompts/phases/phase-06-triage.md`](../writeups/mdp_sec/prompts/phases/phase-06-triage.md)
- [`writeups/mdp_sec/prompts/phases/phase-07-validate-escalate.md`](../writeups/mdp_sec/prompts/phases/phase-07-validate-escalate.md)
- [`writeups/mdp_sec/prompts/phases/phase-08-verify-escalate.md`](../writeups/mdp_sec/prompts/phases/phase-08-verify-escalate.md)
- [`writeups/mdp_sec/prompts/phases/phase-08a-independent-escalation.md`](../writeups/mdp_sec/prompts/phases/phase-08a-independent-escalation.md)
- [`writeups/mdp_sec/prompts/phases/phase-09-triage-gate.md`](../writeups/mdp_sec/prompts/phases/phase-09-triage-gate.md)
- [`writeups/mdp_sec/prompts/phases/phase-10-self-duplicate-check.md`](../writeups/mdp_sec/prompts/phases/phase-10-self-duplicate-check.md)

All 422 verbatim posts are in [`posts/mdp_sec/`](../posts/mdp_sec/).

## Key findings (mined into harness)

_Auto-maintained from `harness/findings.jsonl`. 8 finding(s). Full verbatim posts under `posts/mdp_sec/`._

- **Unauthenticated SQL injection in a public quote flow ($4,000)** (`SQL injection (write-then-read-back / second-order style) → PII + resume-token disclosure`)
  - post: https://x.com/mdp_sec/status/2120066429223317560
  - local: `posts/mdp_sec/2026-11-10-2120066429223317560.md`, `writeups/mdp_sec/bug-bounty-hunting-prompts-readme.md`, `writeups/mdp_sec/mdpsec-home.md`
  - bounty: $4,000
- **/./ path normalisation past a login wall into an admin console** (`Auth bypass via path normalisation mismatch`)
  - post: https://x.com/mdp_sec/status/2120338219841544604
  - local: `posts/mdp_sec/2026-11-11-2120338219841544604.md`, `writeups/mdp_sec/bug-bounty-hunting-prompts-readme.md`, `writeups/mdp_sec/mdpsec-home.md`
  - bounty: undisclosed
- **$8,000 auth bypass on HackerOne — token signature not verified** (`Auth bypass / broken JWT-style token validation`)
  - post: https://x.com/mdp_sec/status/2118435683329310786
  - local: `posts/mdp_sec/2026-11-05-2118435683329310786.md`, `writeups/mdp_sec/bug-bounty-hunting-prompts-readme.md`, `writeups/mdp_sec/mdpsec-home.md`
  - bounty: $8,000
- **$1,200 Bugcrowd dependency confusion** (`Supply chain / dependency confusion`)
  - post: https://x.com/mdp_sec/status/2118803107119325691
  - local: `posts/mdp_sec/2026-11-06-2118803107119325691.md`, `writeups/mdp_sec/bug-bounty-hunting-prompts-readme.md`, `writeups/mdp_sec/mdpsec-home.md`
  - bounty: $1,200
- **Two-account IDOR/BAC testing checklist** (`Methodology: access control (IDOR/BOLA)`)
  - post: https://x.com/mdp_sec/status/2118526280379343189
  - local: `posts/mdp_sec/2026-11-06-2118526280379343189.md`, `writeups/mdp_sec/bug-bounty-hunting-prompts-readme.md`, `writeups/mdp_sec/mdpsec-home.md`
- **Bugcrowd vs HackerOne duplicate handling** (`Platform process`)
  - post: https://x.com/mdp_sec/status/2094614973146448108
  - local: `posts/mdp_sec/2026-09-01-2094614973146448108.md`, `writeups/mdp_sec/bug-bounty-hunting-prompts-readme.md`, `writeups/mdp_sec/mdpsec-home.md`
- **Public OAuth client ID treated as authority — free account R/W production billing catalog ($2,500)** (`oauth`)
  - post: https://x.com/mdp_sec/status/2095462761111388207
  - local: `posts/mdp_sec/2026-09-03-2095462761111388207.md`
  - bounty: $2,500
- **Stored XSS: unauth API writes into LESS config later sunk in back-office designer** (`xss`)
  - post: https://x.com/mdp_sec/status/2099031404252434591
  - local: `posts/mdp_sec/2026-09-13-2099031404252434591.md`

### Daily finds 11–12 Nov 2026

- **SSRF leaks live cloud creds without metadata IP** — https://x.com/mdp_sec/status/2120519414491566209 — [`posts/mdp_sec/2026-11-11-2120519414491566209.md`](../posts/mdp_sec/2026-11-11-2120519414491566209.md). Point fetch at own sink; request arrived signed with worker keys/session token. Harness: log Authorization / identity headers on every SSRF collab before chasing 169.254.
- **October platform payout totals** — https://x.com/mdp_sec/status/2120428817130881387 — H1 ≈$1.2M, Bugcrowd $551k, Intigriti ≈$54k+€26k. Stats: [`writeups/mdp_sec/huntdeck-stats.md`](../writeups/mdp_sec/huntdeck-stats.md).
- **BB Arena v2 methodology notes** — https://x.com/mdp_sec/status/2120489215947313417 — refusals/fallbacks score 0; 4-rung verifier-in-trace required. Board: [`writeups/mdp_sec/blackboxarena-home.md`](../writeups/mdp_sec/blackboxarena-home.md).
- **X Article: open-weights black-box hunting stack** — https://x.com/mdp_sec/status/2120699530589196595 — full article text in [`posts/mdp_sec/2026-11-12-2120699530589196595.md`](../posts/mdp_sec/2026-11-12-2120699530589196595.md). DeepSeek as MVP; 0 refusals on 100 labs for ranked open weights.

### Daily finds 11–12 Nov 2026

- **SSRF leaks live cloud creds without metadata IP** — https://x.com/mdp_sec/status/2120519414491566209 — [`posts/mdp_sec/2026-11-11-2120519414491566209.md`](../posts/mdp_sec/2026-11-11-2120519414491566209.md). Point fetch at own sink; request arrived signed with worker keys/session token. Harness: log Authorization / identity headers on every SSRF collab before chasing 169.254.
- **October platform payout totals** — https://x.com/mdp_sec/status/2120428817130881387 — H1 ≈$1.2M, Bugcrowd $551k, Intigriti ≈$54k+€26k. Stats: [`writeups/mdp_sec/huntdeck-stats.md`](../writeups/mdp_sec/huntdeck-stats.md).
- **BB Arena v2 methodology notes** — https://x.com/mdp_sec/status/2120489215947313417 — refusals/fallbacks score 0; 4-rung verifier-in-trace required. Board: [`writeups/mdp_sec/blackboxarena-home.md`](../writeups/mdp_sec/blackboxarena-home.md).
- **X Article: open-weights black-box hunting stack** — https://x.com/mdp_sec/status/2120699530589196595 — full article text in [`posts/mdp_sec/2026-11-12-2120699530589196595.md`](../posts/mdp_sec/2026-11-12-2120699530589196595.md). DeepSeek as MVP; 0 refusals on 100 labs for ranked open weights.
