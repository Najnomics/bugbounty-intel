# @mdp_sec — Marius du Preez (requested by Dorothy)

Compiled 11 Nov 2026 (WAT). This is the most fully-documented researcher in the repo. Full verbatim post text: [`posts/mdp_sec/`](../posts/mdp_sec/) (430+ files). Writeups, site pages, platform report metadata and his full prompt pack: [`writeups/mdp_sec/`](../writeups/mdp_sec/). Harness material derived from his workflow: [`harness/`](../harness/).

| Field | Value |
| --- | --- |
| X | [@mdp_sec](https://x.com/mdp_sec) (user id 2036270919757471747, created 2026-03-24 UTC) |
| Name | Marius du Preez |
| Location | Australia |
| Site | https://mdpsec.com (static marketing site — no report listing) |
| Specialty | Web / API — web apps, APIs, cloud backends, Android, business logic, access control |
| Platforms | HackerOne (`mdpsec`), Bugcrowd (`marius_dp`), HackenProof (`MDPSEC`) |
| Also builds | BB Arena (blackboxarena.ai, AI-vs-black-box-lab benchmark), HuntDeck; GitHub `mdpsec/bug-bounty-hunting-prompts` and `mdpsec/should-i-submit` |

**2026-11-17 refresh:** mdpsec.com unchanged (591 reports / 150 critical / 267 high / 6 platforms). HackerOne `mdpsec`: resolved 27 (was 26), reputation 889, rank 2659, hacktivity entries 18 (was 17; new entries are undisclosed — 0 public reports). HuntDeck "will be open sourced today" ([post](../posts/mdp_sec/2026-11-17-2122496514677444685.md)).

## Report counts — full vs metadata-only vs missing (exact)

His site claims **582 reports submitted, 148 critical, 263 high, across 5 platforms** (self-reported aggregate, last updated Oct 2026). The site has no per-report listing, no reports page, and no data API — only a `/security-test/` lead form (`/api/apply`). So almost all 582 are **undisclosed private-program reports** with no public detail anywhere. Breakdown of what is actually retrievable:

| Source | Reports | Full detail | Metadata only | Notes |
| --- | --- | --- | --- | --- |
| **HackerOne** `mdpsec` | 26 resolved (2026-11-16; was 24) | 0 | 17 (hacktivity) | 0 publicly disclosed. 17 hacktivity entries (2026-11-16 refresh adds 3925371 msd, 4061813 s-pankki) give program + internal id only; 2 show a bounty ($100 goldmansachs, $842 stripe). Rep 889, rank 2659, signal 6.55 (2026-11-16). |
| **HackenProof** `MDPSEC` | 15 paid | 0 | 15 (counts) | 0 disclosed. Severity split: 3 critical, 3 high, 6 medium, 3 low. Rank 104, rep 966, 29 influenced programs. |
| **Bugcrowd** `marius_dp` | unknown | 0 | 0 | Profile gated behind the authenticated hacker portal; no public per-report data retrievable on 2026-11-11. |
| **X (@mdp_sec)** | — | ~a dozen with technique | the rest | His own posts are the only place with real vulnerability detail; the detailed ones are analysed below. |

**Exact counts.** Full report detail available publicly: **0** disclosed platform reports. Metadata-only: **30** (15 HackerOne hacktivity + 15 HackenProof paid-report severity rows). Missing / undisclosed with no public metadata: the remainder of his self-reported 582 (i.e. ~552, including all Bugcrowd and the ~9 HackerOne resolved reports not in hacktivity). The platform figures are in [`writeups/mdp_sec/platform-reports.md`](../writeups/mdp_sec/platform-reports.md) and `.json`.

His own earliest retrievable post (2026-07-22) states: "$83,088 from bug bounties in my first 151 days. 203 reports since my first submission on 20 February." See [`posts/mdp_sec/2026-07-22-2079869121513378138.md`](../posts/mdp_sec/2026-07-22-2079869121513378138.md).

**2026-11-16 site refresh:** mdpsec.com now claims **591 reports submitted, 150 critical, 267 high, 6 platforms** ("Last updated: November 2026"); still no per-report listing. Bugcrowd posts this run add a $5,000 MCP auth bypass (details above).

## X capture

His full retrievable original-post timeline was captured verbatim: **430+ post files** spanning **2026-07-22 → 2026-11-11**. The X timeline API returns no posts older than 2026-07-22 (its reach limit), so his 2026-03-24 → 2026-07-21 posts are not retrievable ("as far as search allows"). Each file includes the full long-form/note text, media, quoted posts and his own self-reply thread.

## Key findings and analysis

### Horizontal IDOR in an AI support bot's tools — pair-consistency check without ownership → $1,500 (Bugcrowd) (2026-11-16)

- Post: https://x.com/mdp_sec/status/2122270955019919655 — verbatim: [`posts/mdp_sec/2026-11-16-2122270955019919655.md`](../posts/mdp_sec/2026-11-16-2122270955019919655.md)
- **Bug class:** Horizontal IDOR / BOLA in LLM-agent tool endpoints (read victim profile, modify victim support chat)
- **Root cause:** The tool API checked that `user id` and `chat id` matched each other but never that either belonged to the session ("never checked either one was mine").
- **How it was found:** Treating each bot tool call as its own API endpoint and replaying another user's (user_id, chat_id) pair (his stated method: "treat every tool like its own api endpoint and test auth on each").
- **Takeaways / harness:** Two-account replay of every chat/assistant tool request with swapped composite keys; flag 200s returning the other user's data. See [harness/bug-classes/2026-11-17-ai-tool-idor-oauth-scheme-roles-module.md](../harness/bug-classes/2026-11-17-ai-tool-idor-oauth-scheme-roles-module.md).

### DeepSeek V4.1 Flash across 13 inference providers: 0%–45% solve rate on the same labs (BB Arena) (2026-11-16)

- Post: https://x.com/mdp_sec/status/2122214974617710783 — verbatim: [`posts/mdp_sec/2026-11-16-2122214974617710783.md`](../posts/mdp_sec/2026-11-16-2122214974617710783.md)
- **Bug class:** AI hunting-harness engineering (model/provider selection)
- **Root cause:** Same open weights served by different providers produced 45% (direct) down to 12.5% and 0% (rate-limited) on 10 black-box labs × 40 attempts; resellers do not declare precision.
- **How it was found:** Own benchmark (BB Arena) with a fixed private lab set; full page saved at [writeups/mdp_sec/blackboxarena-deepseek-v4-1-flash-providers-2026-11-16.md](../writeups/mdp_sec/blackboxarena-deepseek-v4-1-flash-providers-2026-11-16.md).
- **Takeaways / harness:** Pin provider + model in harness config, regression-test providers on private labs, measure refusals (his data: mythos 5.2 refused 58/100, opus 5.5 32/100; stock DeepSeek direct 0). Speed follow-up: [posts/mdp_sec/2026-11-17-2122542745721974817.md](../posts/mdp_sec/2026-11-17-2122542745721974817.md) (Morph 198 tok/s but 17.5% solved vs direct 144 tok/s / 45%).

### Exposed llama.cpp server with tools/MCP on LAN = "free shell for anyone on the wifi" (2026-11-17)

- Post: https://x.com/mdp_sec/status/2122550959608131942 — verbatim: [`posts/mdp_sec/2026-11-17-2122550959608131942.md`](../posts/mdp_sec/2026-11-17-2122550959608131942.md)
- **Bug class:** Unauthenticated self-hosted LLM server with tool execution → RCE
- **Root cause:** llama-server before 1.0 would start with tools/MCP bound to a LAN address without an API key.
- **How it was found:** Comment on the llama.cpp 1.0 change (quoted context in the file).
- **Takeaways / harness:** Recon for 8080/11434/1234/8000 OpenAI-compatible endpoints on in-scope hosts; check unauthenticated chat + tool calling; prove with a benign tool call.

### Optimizely-served malware (178 orgs): SRI cannot protect dynamically built vendor scripts (2026-11-17)

- Post: https://x.com/mdp_sec/status/2122488006879932755 — verbatim: [`posts/mdp_sec/2026-11-17-2122488006879932755.md`](../posts/mdp_sec/2026-11-17-2122488006879932755.md)
- **Bug class:** Third-party script supply chain / client-side injection
- **Root cause:** Malicious JS injected into a vendor snippet that is generated on the fly, so Subresource Integrity hashes cannot pin it.
- **How it was found:** Reply to Scott Helme; full Report URI writeup: [writeups/mdp_sec/report-uri-optimizely-malware-178-orgs.md](../writeups/mdp_sec/report-uri-optimizely-malware-178-orgs.md).
- **Takeaways / harness:** Inventory dynamic vendor scripts per target; check whether their config is tenant-writable (pairs with his 2026-11-14 widget-config stored XSS).

### MCP servers: "clean on review, nasty on call three" (2026-11-16)

- Post: https://x.com/mdp_sec/status/2122459494433317371 — verbatim: [`posts/mdp_sec/2026-11-16-2122459494433317371.md`](../posts/mdp_sec/2026-11-16-2122459494433317371.md)
- **Bug class:** MCP / agent-tool security methodology
- **Root cause:** MCP behaviour and auth can change across a session; one-time review misses it.
- **How it was found:** Methodology comment.
- **Takeaways / harness:** Run ≥3 calls per tool, diff `tools/list` between calls, re-test auth on each call.

### Guest upload magic-byte bypass → unauthenticated RCE (2026-11-14)

- Post: https://x.com/mdp_sec/status/2121727373498257576 — verbatim: [`posts/mdp_sec/2026-11-14-2121727373498257576.md`](../posts/mdp_sec/2026-11-14-2121727373498257576.md)
- **Bug class:** Unauthenticated guest file-upload → RCE (magic-byte / content-type confusion + config-as-code)
- **Root cause:** Upload validator only inspected the first few bytes. He uploaded a config (valid header + chosen filename) telling the server to treat another upload in the same folder as code, then uploaded the payload and requested the path. No login; ran as the app user.
- **How it was found:** Probing guest upload surfaces for magic-byte-only checks and config files next to upload dirs.
- **Takeaways / harness:** Polyglot corpus + path-guessing after every guest upload; treat config-reload-from-upload-dir as an RCE primitive.

### Unauthenticated third-party widget config → site-wide stored XSS (2026-11-14)

- Post: https://x.com/mdp_sec/status/2121606577698308308 — verbatim: [`posts/mdp_sec/2026-11-14-2121606577698308308.md`](../posts/mdp_sec/2026-11-14-2121606577698308308.md)
- **Bug class:** Stored XSS via unauthenticated vendor widget config API (supply-chain XSS)
- **Root cause:** Third-party widget pulled config from a vendor API with no auth; he wrote a script into a config field; widget rendered it in the site's own origin for every visitor.
- **How it was found:** Inventorying embed/widget bootstrap XHRs and testing unauthenticated writes on their config hosts.
- **Takeaways / harness:** For every third-party embed, resolve config host → fuzz unauthenticated CRUD → DOM-XSS sink check on first-party pages.

### Sequential-ID IDOR: masked GET, unmasked UPDATE echo → full SSN (Critical, Duplicate) (2026-11-14)

- Post: https://x.com/mdp_sec/status/2121546179360276882 — verbatim: [`posts/mdp_sec/2026-11-14-2121546179360276882.md`](../posts/mdp_sec/2026-11-14-2121546179360276882.md)
- **Bug class:** Unauthenticated sequential IDOR / BOLA → PII (SSN, DOB, address); Critical; closed Duplicate of an Aug 10 report
- **Root cause:** Resident-portal applications used plain sequential numbers. Logged-out GET returned masked SSN; the update route echoed the full unmasked record. Walking ±id exposed other applicants.
- **How it was found:** Diffing GET vs update response bodies; incrementing application numbers without auth.
- **Takeaways / harness:** Automate "masking asymmetry" — fields masked on read must stay masked/absent on every other method.

### Hardcoded mobile key decrypts production private key from remote config (2026-11-14)

- Post: https://x.com/mdp_sec/status/2121515980211785729 — verbatim: [`posts/mdp_sec/2026-11-14-2121515980211785729.md`](../posts/mdp_sec/2026-11-14-2121515980211785729.md)
- **Bug class:** Hardcoded client crypto key → decryption of remote config containing a production private key
- **Root cause:** Same key ships in every install; decrypts a startup config blob that should never have held a server private key. Rotating the client key alone does nothing while the blob stays under that key.
- **How it was found:** Unpacking the mobile app, extracting the key, decrypting the startup config download.
- **Takeaways / harness:** Mobile-secret scanner → match against decrypted network blobs; never put prod private keys in client-decryptable config.

### AI hunting system: zero-steering agent + RAG + direct provider API (2026-11-15)

- Post: https://x.com/mdp_sec/status/2121817970381094966 — verbatim: [`posts/mdp_sec/2026-11-15-2121817970381094966.md`](../posts/mdp_sec/2026-11-15-2121817970381094966.md)
- **Bug class:** Methodology (AI harness)
- **Root cause:** N/A
- **How it was found:** N/A — he states AI does all hunting with no guiding; he builds prompts, helpers, RAG; goes direct to the provider API; only reviews reports. Same-day tip: enforce scope at the proxy, not the prompt.
- **Takeaways / harness:** Separate knowledge/RAG, scoped egress proxy, and human-only report review.


### $5,000 Bugcrowd auth bypass on an MCP server — any bearer token accepted (2026-11-15)

- Post: https://x.com/mdp_sec/status/2121878367997714848 — verbatim: [`posts/mdp_sec/2026-11-15-2121878367997714848.md`](../posts/mdp_sec/2026-11-15-2121878367997714848.md)
- **Bug class:** Broken authentication (presence-only header check) on MCP tool endpoints → unauthenticated write to a creator's AI knowledge base (critical)
- **Root cause:** "it just checked an auth header was there. made up token got u in"; "write was the one i proved. it took any bearer token as valid".
- **How it was found:** "treat every tool like its own api endpoint and test auth on each" — enumerate MCP tools/list and test every tools/call with no/junk tokens.
- **Takeaways / harness:** MCP scanner: initialize → tools/list → call each tool with no auth, `Bearer x`, random JWT; flag success parity, prioritise write tools.

### Anonymous file-lookup API leaks storage URLs behind a login-gated support portal (2026-11-15)

- Post: https://x.com/mdp_sec/status/2122089761938518398 — verbatim: [`posts/mdp_sec/2026-11-15-2122089761938518398.md`](../posts/mdp_sec/2026-11-15-2122089761938518398.md)
- **Bug class:** Broken access control — page-level auth only; file API returns direct storage URLs anonymously (confidential firmware/board designs)
- **Root cause:** Gated pages redirect to sign-in, but the anonymous file lookup returns the exact storage URL and storage serves it without auth.
- **How it was found:** Replaying the portal's own file API logged out.
- **Takeaways / harness:** Replay every file/attachment metadata endpoint without cookies; grep for storage URLs; fetch them unauthenticated; check signed-URL expiry.

### Unauthenticated data-query endpoints on a public data server — millions of records (Duplicate, 135 days late) (2026-11-15)

- Post: https://x.com/mdp_sec/status/2122059562161487988 — verbatim: [`posts/mdp_sec/2026-11-15-2122059562161487988.md`](../posts/mdp_sec/2026-11-15-2122059562161487988.md)
- **Bug class:** Missing authentication on data query API → mass data exposure
- **Root cause:** Admin/token pages locked; query endpoints open with no token/cookie; pagination to the last record reconstructs the dataset.
- **How it was found:** Logged-out queries against the data endpoints, then paging to the end.
- **Takeaways / harness:** Test data/query APIs unauthenticated, walk pagination for scale; expect dupes on long-unfixed issues.

### Free account mints paid perks via the generate endpoint — no tier check, no limit, no expiry (2026-11-15)

- Post: https://x.com/mdp_sec/status/2121968965266088068 — verbatim: [`posts/mdp_sec/2026-11-15-2121968965266088068.md`](../posts/mdp_sec/2026-11-15-2121968965266088068.md)
- **Bug class:** Business logic / missing authorization on entitlement issuance
- **Root cause:** Generate-perk endpoint used by the legit claim flow lacks tier check, rate limit and link expiry.
- **How it was found:** Watched a normal claim in the proxy, replayed the generate call as a free user, looped it.
- **Takeaways / harness:** Record eligible-user flows; replay issuance endpoints as lower tier; loop; test expiry and single-use.

### Stock DeepSeek V4.1 Flash: 0 refusals on 100 black-box labs at $1.59/solve (2026-11-15)

- Post: https://x.com/mdp_sec/status/2121908568110628935 — verbatim: [`posts/mdp_sec/2026-11-15-2121908568110628935.md`](../posts/mdp_sec/2026-11-15-2121908568110628935.md)
- **Bug class:** Methodology (AI harness model selection)
- **Root cause:** N/A
- **How it was found:** N/A — BB Arena benchmark: Claude Opus 5 22 solves $41.97/solve, Grok 4.6 21 $19.01, DeepSeek V4.1 Flash 21 $1.59; all 0 refusals; direct provider APIs only.
- **Takeaways / harness:** Benchmark on private labs with unique proof values; call first-party APIs (resellers may quantize); use a cheap worker + strong verifier; add an "irrefutable proof" validation step.

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

### Update 2026-11-18

- **ImageMagick SVG-as-JPG file read → public CDN** — https://x.com/mdp_sec/status/2122784337888506335 — [`posts/mdp_sec/2026-11-17-2122784337888506335.md`](../posts/mdp_sec/2026-11-17-2122784337888506335.md). Also: payouts since 1 Sep (Bugcrowd 24 / $69,675 / median $1,000; H1 16 / $24,458 / median $750) https://x.com/mdp_sec/status/2122633342977769570; BB Arena model results 17–18 Nov (gpt-6.2 sol/astra 0/100 with 37 refusals; gemini 4 refused all 100; qwen4 max 9/100; kimi k3.1 12/100); HuntDeck open-sourced (repo README [`writeups/mdp_sec/huntdeck-readme.md`](../writeups/mdp_sec/huntdeck-readme.md)). His site mdpsec.com unchanged (no new reports); board snapshot [`writeups/mdp_sec/blackboxarena-home-2026-11-18.md`](../writeups/mdp_sec/blackboxarena-home-2026-11-18.md).


### Update 2026-11-19

- **BB Arena results (black-box labs)** — https://x.com/mdp_sec/status/2123176925208227875 and https://x.com/mdp_sec/status/2123279041721774524 — AI-agent-app labs solved by only 5 models (Opus 5 2/10); Gemini 4 Neon Max refuses all 100 URL-only labs; snapshots [`writeups/mdp_sec/blackboxarena-gemini-4-neon-max-2026-11-19.md`](../writeups/mdp_sec/blackboxarena-gemini-4-neon-max-2026-11-19.md), [`writeups/mdp_sec/blackboxarena-deepseek-v4-1-flash-providers-2026-11-19.md`](../writeups/mdp_sec/blackboxarena-deepseek-v4-1-flash-providers-2026-11-19.md). Methodology post: 'do it by hand once, automate once predictable' ([`posts/mdp_sec/2026-11-18-2122965531804504449.md`](../posts/mdp_sec/2026-11-18-2122965531804504449.md)). Site check 2026-11-19: mdpsec.com unchanged (591 reports / 150 critical); no new publicly disclosed reports found.


### Update 2026-11-20

- **Unauthenticated PII CSV on public media URL (medium→High)** — https://x.com/mdp_sec/status/2123629909692039302 — [`posts/mdp_sec/2026-11-20-2123629909692039302.md`](../posts/mdp_sec/2026-11-20-2123629909692039302.md). ~15k signup emails, old "delete" cleanup export, no auth.
- **$3,500 Bugcrowd LFI** (details undisclosed) — https://x.com/mdp_sec/status/2123327919783059471 — [`posts/mdp_sec/2026-11-19-2123327919783059471.md`](../posts/mdp_sec/2026-11-19-2123327919783059471.md).
- **huntdeck open-sourced** (H1/Bugcrowd/Intigriti/YesWeHack scope+change monitor) — https://x.com/mdp_sec/status/2123358119392911553 — [`posts/mdp_sec/2026-11-19-2123358119392911553.md`](../posts/mdp_sec/2026-11-19-2123358119392911553.md); repo github.com/mdpsec/huntdeck, board huntdeck.io.
- **AI-hunting precision gate** — https://x.com/mdp_sec/status/2123388317786128746 — GitHub+MS OSS pilot: thousands of alerts → 99 worth fixing; his 591 reports→120 paid/$205,696, all human-read. [`posts/mdp_sec/2026-11-19-2123388317786128746.md`](../posts/mdp_sec/2026-11-19-2123388317786128746.md).
- **BB Arena black-box board** — https://x.com/mdp_sec/status/2123509113745498345 — best model 22/100, Claude Opus 5 High top. [`posts/mdp_sec/2026-11-19-2123509113745498345.md`](../posts/mdp_sec/2026-11-19-2123509113745498345.md). Site check 2026-11-20: mdpsec.com unchanged (591 reports / 150 critical); no new public disclosures.


### Update 2026-11-21

- **Cross-tenant IDOR on "mark for follow-up" (Medium)** — https://x.com/mdp_sec/status/2123871501539783102 — [`posts/mdp_sec/2026-11-20-2123871501539783102.md`](../posts/mdp_sec/2026-11-20-2123871501539783102.md). Bug: BOLA on a side-action endpoint of a vendor portal (1m+ ticket ids); root cause: tenant check on list/detail only; found by replaying another vendor's ticket id against the small button; read+delete+write across tenants. Takeaway: test every toggle/side action with a second tenant.
- **Provider drift for one model** — https://x.com/mdp_sec/status/2123660108425035820 — 15 hosts of DeepSeek v4.1 Flash solve 5–18/40 labs; one host swapped weights. [`posts/mdp_sec/2026-11-20-2123660108425035820.md`](../posts/mdp_sec/2026-11-20-2123660108425035820.md), [`writeups/mdp_sec/blackboxarena-deepseek-v4-1-flash-providers.md`](../writeups/mdp_sec/blackboxarena-deepseek-v4-1-flash-providers.md).
- **Weekly payout thread (bounty evidence, details undisclosed)** — https://x.com/mdp_sec/status/2123710445458505848 — $10k critical, $6k+120% quality bonus, $5,789 for @Assass1nmarcos, cost-per-solve $1.59 vs $41.97. [`posts/mdp_sec/2026-11-20-2123710445458505848.md`](../posts/mdp_sec/2026-11-20-2123710445458505848.md).
- **Black-box eval pack / provider challenges** — https://x.com/mdp_sec/status/2123946567359197319 · /2123921694746448236 (Boundless 40% vs 45% direct; abliterated 27.5%) · /2124005878571696338 (OrcaRouter 25%). [`writeups/mdp_sec/blackboxarena-labs.md`](../writeups/mdp_sec/blackboxarena-labs.md). Site check 2026-11-21: mdpsec.com unchanged (591 reports / 150 critical); no new public disclosures.

### 2026-11-21 — OTP verify/finalize identity mismatch ATO ($5k)
- **Bug / class:** Account takeover — OTP checked against attacker account, login session returned as victim.
- **Root cause:** MFA state-machine binding failure between verify and finalize identities.
- **How found:** AI-assisted (mdp_sec: "my ai found it, i just did the report"); platform undisclosed.
- **Takeaways:** Assert every field used at OTP verify equals identity committed at finalize; swap user_id/email between steps; race verify+finalize.
- **Local:** [posts/mdp_sec/2026-11-21-2124052695359381521.md](../posts/mdp_sec/2026-11-21-2124052695359381521.md)

### 2026-11-21 — Edge `/./metrics` path-rule bypass → applicant-token leak
- **Bug / class:** WAF/edge exact-path denylist bypass via `/./` and single-char percent-encoding; Prometheus metrics exporter labeled request paths with live applicant tokens → unauth cross-user R/W.
- **Root cause:** Edge matched exact path; origin app normalized `/./` away; metrics labels retained raw paths including tokens for ~8 days.
- **Takeaways:** Path-normalization bypass corpus next to every edge denylist; treat metrics exporters as credential sinks.
- **Local:** [posts/mdp_sec/2026-11-21-2124233889270939950.md](../posts/mdp_sec/2026-11-21-2124233889270939950.md)

### 2026-11-21 — HuntDeck pay-per-hour bug-class ranking
- **Signal:** 24 classes ranked by $/hour; S-tier mostly access control; open redirect $280 median on public disclosures.
- **Local:** [posts/mdp_sec/2026-11-21-2124022496446017575.md](../posts/mdp_sec/2026-11-21-2124022496446017575.md); huntdeck.io/disclosed fetch 403 on 2026-11-22.

### 2026-11-21/22 — Abliterated DeepSeek provider benchmarks (OrcaRouter 37.5%, abliteration_ai 25%)
- **Signal:** Abliterated builds still trail DeepSeek direct API (45% @ $0.46/solve).
- **Local:** [2124240867590549887](../posts/mdp_sec/2026-11-21-2124240867590549887.md), [2124374055747043600](../posts/mdp_sec/2026-11-22-2124374055747043600.md); blackboxarena compare page refreshed.

### 2026-11-22 — "Test your own harness" Black Box Arena pack (next week)
- **Local:** [posts/mdp_sec/2026-11-22-2124303479737049222.md](../posts/mdp_sec/2026-11-22-2124303479737049222.md)


### 2026-11-22 — Sitecore media-folder listing → public 15k-email CSV (Medium → High)
- **Bug / class:** Unauthenticated PII file exposure via CMS media-library enumeration (CWE-548/CWE-552).
- **Root cause:** Sitecore SOAP API let any signed-up account list media folders; files under `/-/media/` served publicly by path; stale `testing` export never deleted.
- **How found:** low-priv listing → `testing` folder → CSV opened with no login; random `?v=` to hit origin (not CDN cache).
- **Takeaways:** pair every authenticated listing API with unauthenticated fetch of listed paths; prioritise test/export/backup folders.
- **Local:** [posts/mdp_sec/2026-11-22-2124626476397916632.md](../posts/mdp_sec/2026-11-22-2124626476397916632.md); harness [2026-11-23 check-specs](../harness/bug-classes/2026-11-23-cms-media-listing-cdn-proxy-param-alias.md).

### 2026-11-22/23 — Provider bench v2 (self-host 55%), abliteration study, latency vs solves
- **Signal:** 21 providers + self-host: 10–55% solved; abliterated builds no benefit (0 refusals on stock; −45% reasoning, 2× time-outs); 143→236 tok/s per agent = 16→22/40 solves.
- **Local:** [providers](../posts/mdp_sec/2026-11-22-2124653323940937754.md), [abliteration](../posts/mdp_sec/2026-11-23-2124707206306427126.md), [speed thread](../posts/mdp_sec/2026-11-22-2124414813296279647.md); writeups [abliteration](../writeups/mdp_sec/blackboxarena-deepseek-v4-1-flash-abliteration.md), [providers 2026-11-23](../writeups/mdp_sec/blackboxarena-deepseek-v4-1-flash-providers-2026-11-23.md).

### 2026-11-22 — Ops notes (scope proxy, thumbnailer targets, dupes, HuntDeck OSS)
- Agents run on an overseas Linux box behind a MITM proxy that drops out-of-scope traffic ([post](../posts/mdp_sec/2026-11-22-2124600258223300633.md)); "every pdf thumbnailer on a bounty scope just became a target" after Upload2Shell ([post](../posts/mdp_sec/2026-11-22-2124468750242255159.md)); ~4 in 10 of his reports end up dupes ([x.com](https://x.com/mdp_sec/status/2124599244342563095)); HuntDeck open-sourced ([post](../posts/mdp_sec/2026-11-22-2124467610263965976.md), [README](../writeups/mdp_sec/huntdeck-github-2026-11-23.md)); CVSS-10 triage meme (bounty-meta, [post](../posts/mdp_sec/2026-11-22-2124384884265488887.md)).

### 2026-11-23/24 — HuntMail (open source catch-all inbox for agents)
- **Bug class enabled:** email-gated flows (OTP, reset, invite, email change) automated end-to-end.
- **How:** Cloudflare Email Routing catch-all → Worker + D1; `GET /api/wait?to=&since=&timeout=50` → `codes`, `link_details`, SPF/DKIM/DMARC; platform relay aliases → `bb@` with `from_domain` check.
- **Takeaways:** fresh address per signup, record `since` before trigger, open one-time links once, treat mail as untrusted data.
- **Local:** [post](../posts/mdp_sec/2026-11-23-2125001700218184092.md), [README](../writeups/mdp_sec/huntmail-github-2026-11-24.md).

### 2026-11-23 — White box vs black box; refusals; triage-challenge gate
- **Signal:** best model proves 22/100 black-box labs (URL only); frontier models refused in 58 (mythos 5.2) / 76 (gpt-6 astra) labs; "same plain harness for every model. a target and a shell"; "the server confirms every rung".
- **Triage gate:** with @arcwhite — submissions must read "As an attacker, I could…"; minimum precondition "an attacker that can already login to own account"; tool [should-i-submit](../writeups/mdp_sec/should-i-submit-github-2026-11-24.md).
- **Local:** [white/black box](../posts/mdp_sec/2026-11-23-2124807670121295974.md), [challenge thread](../posts/mdp_sec/2026-11-23-2124790046306041889.md), [should-i-submit reply](../posts/mdp_sec/2026-11-23-2124994769478881642.md).

### 2026-11-24 — Abliteration write-up, provider retests (Boundless, Morph), Sol/Daybreak, payouts
- Abliterated builds: rule checks 110→31/run, 2.8× wordlists, 4.3× request floods, 3.2× failed commands, no solve gain ([post](../posts/mdp_sec/2026-11-24-2125079460907200656.md), [writeup](../writeups/mdp_sec/blackboxarena-deepseek-v4-1-flash-abliteration-2026-11-24.md)).
- Boundless 16→18/40 at 189 tok/s ([post](../posts/mdp_sec/2026-11-24-2125023261025325102.md)); Morph 20th→2nd after fixing 131k-token-cap truncation ([post](../posts/mdp_sec/2026-11-24-2125098452275323340.md)); table [providers 2026-11-24](../writeups/mdp_sec/blackboxarena-deepseek-v4-1-flash-providers-2026-11-24.md).
- GPT-5.6 Sol kept via Daybreak Blue — "the only good gpt model for cyber" ([post](../posts/mdp_sec/2026-11-24-2125060582206566734.md)).
- 90-day payouts: H1 $12.8M, Bugcrowd $7.2M, Intigriti ≈$1M+€191k; $21M across 1,406 programs ([post](../posts/mdp_sec/2026-11-24-2125049262052651252.md)). Retests reports every 14 days to keep them valid ([x.com](https://x.com/mdp_sec/status/2124790454441173473)).
- mdpsec.com unchanged (591 reports / 150 critical / 267 high).
