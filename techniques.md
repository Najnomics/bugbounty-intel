# Techniques and patterns

High-level methodology, recon tips, and bug patterns pulled from the public sources in this repo. Each item is linked to its source. This is a workflow aid, not an exploit guide: reproduction steps and payloads stay in the original writeups.

Last updated: 16 November 2026 (Africa/Lagos).

---

## 2026-11-16 additions (daily X sweep, HackerOne, Telegram)

**MCP servers: test every tool as its own API — presence-only bearer checks.** mdp_sec was paid $5,000 (Bugcrowd, critical) because an MCP server "just checked an auth header was there. made up token got u in" and the *write* tool let anyone rewrite a creator's AI knowledge base. Harness: `initialize` → `tools/list` → call each `tools/call` with no header, `Bearer x`, random JWT; flag parity with a valid token. Source: [@mdp_sec 15 Nov 2026](posts/mdp_sec/2026-11-15-2121878367997714848.md).

**"Pages locked, data endpoints open."** Three mdp_sec finds in one day share the pattern: a login-gated support portal whose anonymous file-lookup API returns raw storage URLs (confidential firmware/board designs) ([post](posts/mdp_sec/2026-11-15-2122089761938518398.md)); a public data server whose query endpoints return millions of proprietary rows without a token (dupe, 135 days late) ([post](posts/mdp_sec/2026-11-15-2122059562161487988.md)); Lovable-built apps with locked pages but open data endpoints ([post](posts/mdp_sec/2026-11-15-2122081089435181494.md)). Harness: replay every XHR/API seen in an authenticated crawl with cookies and Authorization stripped; walk pagination for scale.

**Entitlement issuance is as sensitive as redemption.** A "generate perk link" endpoint called by the legit claim flow had no tier check, no limit and non-expiring links → any free account mints paid perks forever. Source: [@mdp_sec 15 Nov 2026](posts/mdp_sec/2026-11-15-2121968965266088068.md).

**Public RPC custom JS tracers = unauthenticated node DoS ($10,000, HackerOne/Cantina arc-bbp).** `debug_traceCall`/`debug_traceTransaction` with custom JavaScript tracers (Boa engine via revm-inspectors `JsInspector`) exposed with no auth/timeout/memory caps: parser stack overflow → SIGABRT, Map+GC `BorrowMutError` non-unwinding panic → process abort, `regress` ReDoS pins threads, native `toHex` over a 4 GiB-length array, unbounded result size. Harness: probe every public RPC for `debug_*` methods and JS tracer support; fingerprint engine (`web3_clientVersion`); test bounded single-request crash primitives only with permission. Source: [hackerone/reports/2026/3966160.md](hackerone/reports/2026/3966160.md).

**Proxy-header trust in rate limiters.** Weblate's DRF `RateOverrideThrottle` inherited `SimpleRateThrottle.get_ident()` so `X-Forwarded-For` chose the throttle bucket → anonymous rate-limit bypass. Harness: rotate `X-Forwarded-For`/`X-Real-IP`/`Forwarded` per request against throttled endpoints and compare 429 behaviour. Source: [hackerone/reports/2026/4059744.md](hackerone/reports/2026/4059744.md). Same day: Weblate Change API leaked `details.ip_address` of anonymous suggestions to read-only users ([4117330](hackerone/reports/2026/4117330.md)) — diff API objects against what the HTML view hides.

**Debug logs + vulnerable observability stack = key theft (Proxima, 5,324 SOL).** A debug log statement around wallet create/import emitted private keys once prod log level was lowered to debug; 15-day retention kept them in a SigNoz instance running a version with a public unauthenticated-data-access vuln; attacker extracted logs and drained 870 wallets while extraction was ongoing. Harness: fingerprint exposed observability UIs/APIs (SigNoz, Grafana, Kibana, Loki, Jaeger, OpenSearch) on in-scope hosts, check known unauth CVEs, grep accessible logs for key/seed/JWT material. Source: [writeups/telegram-defendor_eng/proxima-post-mortem-signoz-leaked-private-keys.md](writeups/telegram-defendor_eng/proxima-post-mortem-signoz-leaked-private-keys.md).

**Hash-collision test vectors.** zkSecurity's Collision Atlas: 123 runnable colliding pairs (15 full breaks incl. MD5/SHA-1; 108 reduced-round). Use full-break pairs against anything that dedupes, caches, signs or allowlists by MD5/SHA-1. Full dataset: [writeups/zksecurityXYZ/collision-atlas-2026-11-16.md](writeups/zksecurityXYZ/collision-atlas-2026-11-16.md).

**Attestation-policy questions for TEE-backed chains.** saxenism on Flare Confidential Compute: which hardware/TCB claims are accepted, who updates the policy after Google firmware rollouts, can users inspect the rules? Source: [@saxenism 15 Nov 2026](posts/saxenism/2026-11-15-2121975522028859699.md).

**Hardware badge/wallet zero-click over Wi-Fi.** Neodyme got zero-click RCE on the Solana Breakpoint badge via deauth or joining a vulnerable AP (details pending). Source: [@Neodyme 15 Nov 2026](posts/Neodyme/2026-11-15-2121941626822004761.md).

**AI harness economics.** Stock DeepSeek V4.1 Flash via first-party API: 0 refusals on 100 black-box labs, 21 solves at $1.59/solve vs Claude Opus 5 22 at $41.97 and Grok 4.6 21 at $19.01 (mdp_sec's BB Arena). Call providers directly (resellers may quantize); add an "irrefutable proof" validation step. Sources: [deepseek post](posts/mdp_sec/2026-11-15-2121908568110628935.md), [validation step](posts/mdp_sec/2026-11-16-2122139706913878466.md).

**Formal verification lessons (Will Papper, 5 years of Certora at Syndicate).** Specs = reachable/unreachable state machine; keep specs close to code; verified model ≠ deployed code (prefer bytecode-level verification); tool map Lean / Certora CVL / Verus / Aeneas / Hax. Source: [writeups/telegram-defendor_eng/willpapper-five-years-formal-verification-certora.md](writeups/telegram-defendor_eng/willpapper-five-years-formal-verification-certora.md).


## 2026-11-15 additions (from daily X sweep)

**Guest upload magic-byte filters are not content parsers.** If an upload only checks the first few bytes, ship a valid header + attacker filename that makes the server treat a sibling upload as code, then request the path. Automate with a polyglot corpus and path-guessing against the returned URL. Source: [@mdp_sec 14 Nov 2026](posts/mdp_sec/2026-11-14-2121727373498257576.md).

**Third-party widget config APIs are often unauthenticated write → first-party stored XSS.** Inventory embed bootstrap XHRs, fuzz vendor config CRUD without auth, and confirm sinks render in the site origin (not a sandboxed opaque iframe). Source: [@mdp_sec 14 Nov 2026](posts/mdp_sec/2026-11-14-2121606577698308308.md).

**Masking asymmetry = IDOR.** Diff GET vs PUT/PATCH/POST for the same sequential id: fields masked on read may come back full on the update echo. Walk ±id without auth. Source: [@mdp_sec 14 Nov 2026](posts/mdp_sec/2026-11-14-2121546179360276882.md).

**Mobile hardcoded keys decrypting remote "config" often yield server secrets.** Unpack APK/IPA, extract keys, decrypt startup blobs; assert no production private keys. Rotation of the client key alone is useless while the blob stays under it. Source: [@mdp_sec 14 Nov 2026](posts/mdp_sec/2026-11-14-2121515980211785729.md).

**AI hunting harness layout (mdp_sec):** zero-steering agent; human builds prompts + helpers + RAG; call provider API directly; enforce scope at the egress proxy (not the prompt); human only reviews reports. Source: [@mdp_sec 15 Nov 2026](posts/mdp_sec/2026-11-15-2121817970381094966.md), [scope-at-proxy reply](posts/mdp_sec/2026-11-14-2121733132487737398.md).

**Harnesses are not pure functions.** kobigurk: "Treating harnesses as functions is a form of skeuomorphism." Keep the recon→hypothesis→probe→evidence→report loop stateful. Source: [@kobigurk 15 Nov 2026](posts/kobigurk/2026-11-15-2121784321799598543.md).

**Pool Party ($215K): recorded LP/position editable → drain across 15 pools (Arbitrum/Base).** Attacker edited their recorded position and drained ~$215K; fixed on all four chains; funds converted to XMR. Harness: any pool/position accounting that trusts a mutable on-chain or off-chain "recorded position" without re-deriving from deposits/shares is a drain primitive — fuzz position-update entrypoints and assert share↔asset invariants. Source: [@defendor_eng #2342](telegram/defendor_eng/), 14 Nov 2026.

**Centrifuge V3.3 private bounty (B612): malicious pool manager withdrawing other pools' assets.** 17 researchers, 21 reports, 2 accepted; critical fixed in 24h. Harness: for multi-pool managers, test cross-pool withdraw/transfer with a manager role scoped to pool A against pool B assets. Source: [@defendor_eng #2344](telegram/defendor_eng/), 14 Nov 2026.




## Recon and process

**Stay on one good target.** Swartz went from 9 to 10 to 11 triaged reports on a single Bugcrowd program in a few weeks and explicitly advises "loyalty" to the right wildcard-domain target. Source: [15 Oct 2026](https://x.com/Swartz068/status/2110728116180226209), [8 Oct 2026](https://x.com/Swartz068/status/2108307317322379620).

**Prefer wildcard-domain programs when you want depth.** Swartz: "I always choose wild card domain program." Source: [16 Oct 2026](https://x.com/Swartz068/status/2110996965148266599).

**Store recon in a queryable database, not loose text files.** Harley Kimball: endpoints, parameters, headers, request/response shapes, related services — then let an agent query that store ("what other parameters have we seen on this endpoint?"). He mentioned Supabase + MCP as a concrete setup. Source: [30 Oct 2026](https://x.com/infinitelogins/status/2116236446147240443).

**Accuracy over volume.** krishnsec posted a 69% 90-day accuracy and said he still reports only a few bugs even when he can file more. Source: [13 Oct 2026](https://x.com/krishnsec/status/2109886780657029303).

**Inspect forgotten surfaces: affiliate pages, admin subdomains, "dummy" bot hosts, help-center search.** Aditya's $5k ATO was on an affiliate reset flow, not the main login. The $3,500 admin takeover started with subdomain + directory enumeration behind `admin`. The $200 path disclosure was on a chat-bot subdomain after "boring" tests failed. Sources: [ATO writeup](https://assassin-marcos.medium.com/5k-misconfigured-reset-password-that-leads-to-account-takeover-no-user-interaction-ato-e6a36b8ef183), [admin takeover](https://www.bugbountydirectory.com/blogs/breaking-the-barrier-admin-panel-takeover-worth-3500), [error writeup](https://assassin-marcos.medium.com/dont-underestimates-the-errors-they-can-provide-good-bounty-d437ecca6596).

**Read official API documentation when a token or object leaks but the consumer is unclear.** That is how the admin-panel token became a password reset. Source: [admin takeover](https://www.bugbountydirectory.com/blogs/breaking-the-barrier-admin-panel-takeover-worth-3500).

**Historical JS and archived URLs are still in scope for secrets.** Swartz: Wayback snapshots of `config.js` / `env.js` / `app.js` from different years; JWTs embedded in archived URLs that decode to PII or roles. Sources: [4 Nov 2026](https://x.com/Swartz068/status/2117931096726016043), [2 Nov 2026](https://x.com/Swartz068/status/2117202589918114241).

**Watch patch diffs before CVEs land.** infinitelogins highlighted @spaceraccoon's project that monitors GitHub commit/PR diffs for vulnerability patches — useful for variants and downstream forks. Source: [19 Feb 2026](https://x.com/infinitelogins/status/2024484231062114553).

**Inventory every privileged address, including deprecated contracts.** Kiki found a years-old privileged contract that still bypassed cooldown checks. Source: [29 Jan 2026](https://x.com/Kiki_developer/status/2016925457271361718).

**Know which programs exist.** LonelySloth says line-by-line ZK reading paid well, but he never hunted Zcash or Solana because he did not know they had bounties. Source: [5 Jun 2026](https://x.com/lonelysloth_sec/status/2062916729676648907).

**Thick-client work depends on source-code analysis, and the niche is less crowded.** Suryesh's 2026 streak of accepted thick-client RCEs is the evidence; method not public. Source: [22 Jun 2026](https://x.com/Suryesh_92/status/2069043943640301896), [10 Sep 2026](https://x.com/Suryesh_92/status/2097850230930862237).

---

## Authentication, session, and account takeover

**Password-reset and token-issuance APIs must not return the token to the caller.** Two of Aditya's writeups are the same class on different targets: reset token in the JSON response → build the change-password URL → ATO or admin takeover, no inbox access required. Always read the response body, not just "email sent." Sources: [2021 ATO](https://assassin-marcos.medium.com/5k-misconfigured-reset-password-that-leads-to-account-takeover-no-user-interaction-ato-e6a36b8ef183), [2024 admin panel](https://www.bugbountydirectory.com/blogs/breaking-the-barrier-admin-panel-takeover-worth-3500).

**Secret-lookup endpoints that use pattern match (e.g. SQL `LIKE`) can be enumerated with a wildcard.** If a lookup of a key or token returns more than one row, you may have a table dump, not a point query. Rate limits matter once that is true. Source: Harley, [4 Nov 2026](https://x.com/infinitelogins/status/2117981403161764138).

**"Device" or "auto-login" keys are credentials.** If presenting the key issues a session, leakage is account takeover. The same path often skips MFA because no human is present. Source: Harley, [4 Nov 2026](https://x.com/infinitelogins/status/2117981403161764138) and [28 Oct 2026](https://x.com/infinitelogins/status/2115429533738262954).

**Audit every token-issuing path when MFA is added.** Harley's privilege-escalation chain survived because device auto-login did not enforce MFA. Source: [28 Oct 2026](https://x.com/infinitelogins/status/2115429533738262954).

**Mint a long-lived credential before a new security boundary appears, then reuse it after.** Same post: a device key created *before* the account became admin still worked after MFA was required on the normal login.

**Mass assignment on permission fields.** A trial user could write `admin_permissions` (including a superadmin flag) through a PUT that did not check the caller was already an admin. Source: [28 Oct 2026](https://x.com/infinitelogins/status/2115429533738262954).

**Parser differentials: gateway vs backend.** If the gateway skips auth for "static" suffixes (for example `.json`) but the backend still serves the API, you have an auth bypass once you can make both layers accept the same request. Map every layer's path parsing. Trusted-client headers are not authentication. Source: Harley, [8 Oct 2026](https://x.com/infinitelogins/status/2108181015885685018).

**Sequential IDs plus broken tenant isolation** turn one privileged session into cross-org PII. Source: [28 Oct 2026](https://x.com/infinitelogins/status/2115429533738262954).

**Account-abstraction / guardian models:** look for a path that still drains almost the entire balance in a single block, especially after the design's point was to survive key compromise. Source: Naresh on Quantus, [23 Sep 2026](https://x.com/naresh_1337/status/2102840461430005790), [24 Sep 2026](https://x.com/naresh_1337/status/2103196335851614609).

---

## Injection and WAF

**Verbose database errors are an output channel.** Harley's unauth SQLi was useful because HTTP 500s included BigQuery error text, which could carry query results, not only a boolean. Never return raw DB errors to unauthenticated clients. Source: [14 Oct 2026](https://x.com/infinitelogins/status/2110355630133322159).

**When a WAF blocks textbook keywords, learn the dialect.** Filters that catch `UNION` / `SELECT` may miss vendor-specific scripting, encodings, or comment-insertion tricks. Fingerprint the engine from the error first. Same source.

**Unexpected status codes on header tampering can leak paths.** Aditya removed a Host header and got a 401 with a source path instead of a generic 400. Source: [2019 writeup](https://assassin-marcos.medium.com/dont-underestimates-the-errors-they-can-provide-good-bounty-d437ecca6596).

**WAF 403 on basic XSS is not the end.** Suryesh's help-center search blocked simple probes (nginx 403) but still executed a polyglot, and the sink also evaluated a client-side template (CSTI). Source: [29 Oct 2024](https://hackwithsuryesh.medium.com/rxss-csti-in-search-field-via-polygot-payload-65ca1a8be8ba).

**OS command injection still appears on modern platforms.** Naresh posted a paid YesWeHack critical tagged CWE-78, without a method writeup. Source: [19 Aug 2026](https://x.com/naresh_1337/status/2090140871182242262).

---

## Access control, uploads, and third-party keys

**Frontend third-party keys are credentials.** An Algolia key in `main.js` with write or `editSettings` / `listIndexes` ACLs is not "just a search key." Check the actual ACL; a search-only key is a different (often informative) issue. Do not prove impact by deleting data. Source: Suryesh, [11 Feb 2025](https://hackwithsuryesh.medium.com/algolia-api-key-exploitation-leads-to-1000-bounty-p2-on-private-program-2e147f052ff0).

**File-upload filters that trust Content-Type may accept a double MIME type.** Suryesh's stored-XSS tip: a header like `application/pdf,text/html`. Full mechanics unpublished. Source: [24 Jan 2026](https://x.com/Suryesh_92/status/2014855434696597734).

**SSRF remains a HackenProof-era bug class.** Piki reported an SSRF that was triaged; sink undisclosed. Source: [26 Oct 2026](https://x.com/Piki_eth/status/2114761602025304105). Client-controlled URLs in TEE verifiers are the same class in another costume (Bluethroat / dstack `pccs_url`). Source: [Phala advisory](https://phala.com/posts/dstack-security-update-attestation-pipeline-hardening).

---

## Supply chain

**Unclaimed internal package names are dependency-confusion candidates.** Look in `package.json`, lockfiles, and npm/yarn debug logs; verify the name on the public registry; impact is install-hook execution in CI or on a developer machine, which can also become a local file read. Source: Suryesh, [17 Sep 2024](https://hackwithsuryesh.medium.com/how-i-chained-rce-via-dependencies-to-lfi-348315aa17e8).

---

## AI application and AI-assisted hunting

**Model extraction via the query API is a P1 class krishnsec has already used.** Do not stop at prompt injection on AI features. Source: [1 Nov 2026](https://x.com/krishnsec/status/2116965015777628269).

**The harness matters more than the model name.** krishnsec: "4.6 can still find P1 criticals — it's all about the harness." Source: [25 Oct 2026](https://x.com/krishnsec/status/2114270259687661611).

**Treat model output as a draft.** Piki manually reviewed and reproduced a DoS after a five-hour local Qwen run, then hit a reputation gate on HackenProof. Source: [28 Aug 2026](https://x.com/Piki_eth/status/2093217981732171978). LonelySloth planted an "obvious" critical that contradicted a code comment; the model missed it, talked itself out of it, and under-severed it. Source: [8 Mar 2026](https://x.com/lonelysloth_sec/status/2030545303607329178). krishnsec: part of the skill is knowing when AI is hallucinating. Source: [15 Aug 2026](https://x.com/krishnsec/status/2088675304198078711).

---

## Smart contracts and DeFi

**Missing access control on risk-parameter setters.** If anyone can change the liquidation threshold, healthy positions become liquidatable. Source: Kiki, [Bounties/013.md](https://raw.githubusercontent.com/devNamedKiki/Audits/main/Bounties/013.md).

**Leftover privileged contracts.** See recon, above.

**Common contest classes Kiki still uses as a question list:** reentrancy (CEI; shared state across external calls), DoS via attacker-inflated loops or unsatisfiable conditions, unsafe `delegatecall` targets, unchecked call returns, transaction-order / ERC-20 approve races, flash-loan price manipulation, oracle edge cases, overflow/underflow and unsafe downcasts. Source: [1 Feb 2024](https://medium.com/@kiki.auditor/8-common-smart-contract-vulnerabilities-found-throughout-audit-contest-d8f19c494f7e).

**First-depositor vault inflation, elastic-supply tokens, zero-premium options, and "brick the settlement path"** appear as titles in Kiki's public bounty table even when the writeup is still empty — useful as a review checklist, not as verified root causes. Source: [Audits README](https://github.com/devNamedKiki/Audits).

---

## Bridges, consensus, TEEs, and chain clients

**On bridges, ask whether funds can be permanently destroyed, not only stolen.** Piki's HackenProof report (triaged, not confirmed paid in the post) was about wallet-ownership proof logic that could permanently destroy bridged funds. Source: [29 Oct 2026](https://x.com/Piki_eth/status/2115783655092277530).

**Write down the quorum rule in every layer and look for disagreements.** Bluethroat: two layers disagreed on what counts as a quorum ($10k from a major L1). Their bar: derive the invariant, reproduce on stock clients, run a matched control, test recovery. Source: [7 Nov 2026](https://x.com/bluethroat_labs/status/2119050683840438658).

**Deterministic execution is an invariant.** If the same contract can behave differently because of CPU-level instruction differences, honest clients can disagree. Bluethroat used paired execution + consensus analysis for Immunefi findings #9 and #10. Source: [1 Oct 2026](https://x.com/bluethroat_labs/status/2105581456550461936), [6 Oct 2026](https://x.com/bluethroat_labs/status/2107490499305124027).

**Attestation / TEE verifier checklist (from the public dstack advisory):**
- Is quoting-enclave *identity* actually verified, or could an unauthorized QE be accepted?
- Is TCB status *enforced*, or only informational?
- Are TLS certificate checks on for collateral/PCCS fetches, and is stale-but-valid collateral replayable?
- Can a caller supply the verifier's URL (SSRF)?
- Is "is_valid" / "event_log_verified" a cryptographic fact or a confusing green light?
Source: [Phala, 10 Feb 2026](https://phala.com/posts/dstack-security-update-attestation-pipeline-hardening), plus Bluethroat's stale-collateral explanation.

**Node and networking bugs sit under the Solidity layer and can pay well.** Immunefi framed Keizo's $33k high as a core-infra bug "serious enough to disrupt how that network operates." Source: [4 Nov 2026](https://x.com/immunefi/status/2117965345550172382).

**On Cosmos-style chains, a single transaction can pack many messages.** That changes how you reason about "this would take several suspicious steps." Source: f4lc0n on Injective (payout disputed — see his file), [18 Mar 2026](https://x.com/al_f4lc0n/status/2034125406748741827).

**ZK: read circuits line by line, and also read verifiers.** LonelySloth's 2023 claim: several loss-of-TVL bugs in circuits and verifiers on high-max-bounty Immunefi programs. Source: [5 Jun 2026](https://x.com/lonelysloth_sec/status/2062916729676648907).

---

## Reporting and program hygiene

- Prefer non-destructive impact demonstrations (Aditya / Suryesh both warn against deleting data).
- A triaged report is not a paid bug (Piki, Swartz, Suyash posts).
- If two of your reports share a payload, expect a duplicate (Suryesh XSS).
- Some programs under-pay or stall; record the process, but do not treat a public dispute as proof of a bug (Assass1nmarcos vs a BOLA triage; f4lc0n vs Injective).

---

## Added Nov 2026 — techniques from the expanded researcher set

Every item links to the verbatim post file in this repo (full text, no X access needed).

### Web / API
- **Write-then-read-back SQLi in "save and resume later" flows.** A public quote endpoint concatenated a JSON field into SQL; staging a record and reading it back returned DB-evaluated columns, incl. resume tokens. Treat any field that is written and later echoed as an oracle. — Marius du Preez, [`posts/mdp_sec/2026-11-10-2120066429223317560.md`](posts/mdp_sec/2026-11-10-2120066429223317560.md)
- **Gate vs router path disagreement.** Auth matched the exact path; router normalised afterwards, so `/admin/./` bypassed login. Retry 403/login-redirect paths with `/./`, `//`, trailing dots, `%2e`. — [`posts/mdp_sec/2026-11-11-2120338219841544604.md`](posts/mdp_sec/2026-11-11-2120338219841544604.md)
- **Check token signatures are actually verified** ($8,000 H1 auth bypass). — [`posts/mdp_sec/2026-11-05-2118435683329310786.md`](posts/mdp_sec/2026-11-05-2118435683329310786.md)
- **Dependency confusion**: unclaimed internal package names ($1,200 Bugcrowd). — [`posts/mdp_sec/2026-11-06-2118803107119325691.md`](posts/mdp_sec/2026-11-06-2118803107119325691.md)
- **Two-account access-control loop incl. revoke step.** — [`posts/mdp_sec/2026-11-06-2118526280379343189.md`](posts/mdp_sec/2026-11-06-2118526280379343189.md)
- **Differential query-param extraction + regex char-class bug** (`[?|&]` treats `|` literally) → validation sees one value, `location.href` gets another → XSS. — Frans Rosén, [`posts/fransrosen/2024-08-27-1828503460183941420.md`](posts/fransrosen/2024-08-27-1828503460183941420.md)
- **Enumerate every OAuth client_id**; a mobile client allowed any protocol in redirect_uri → malicious app steals login. — xssdoctor, [`posts/xssdoctor/2026-10-01-2105723370125881675.md`](posts/xssdoctor/2026-10-01-2105723370125881675.md)
- **Trusted internal headers accepted from outside** ($300k); brute-force hidden headers (Param Miner). — James Kettle, [`posts/albinowax/`](posts/albinowax/)
- **Response-header XSS in Firefox**: XSLT from a `data:` URL in a `Link` header; **CSS-only token exfiltration** (Frag). — Gareth Heyes, [`posts/garethheyes/`](posts/garethheyes/), [`writeups/garethheyes/`](writeups/garethheyes/)
- **Sanitizer bypass via browser-specific parsing** (DOMPurify ≤3.2.6 Safari SMIL), **DB logic privilege escalation** (MariaDB GRANT PROXY), **Cloudflare /cdn-cgi/image XSS**. — Kévin Mizu, [`posts/kevin_mizu/`](posts/kevin_mizu/), [`writeups/kevin_mizu/`](writeups/kevin_mizu/)
- **Connected-car and gaming back-office APIs.** — Sam Curry & Shubs, [`writeups/samwcyo/`](writeups/samwcyo/), [`writeups/infosec_au/`](writeups/infosec_au/)

### Mobile
- **Android Uri host-validation bypass** and **content-provider access via system apps**; 140 Samsung preinstalled-app bugs. — Sergey Toshin, [`posts/_bagipro/`](posts/_bagipro/), [`writeups/_bagipro/`](writeups/_bagipro/)

### Native / thick client
- **Zero-click MMS image-codec exploitation and ASLR oracle** (Samsung Qmage series). — j00ru, [`writeups/j00ru/`](writeups/j00ru/)

### Web3 / blockchain / ZK
- **Enumerate all branch combinations in special-case node logic.** Polygon zkEVM: non-free reverted claim txs were pooled and marked deposit counts used → DoS + blocked L1→L2 claims. — iczc, [`posts/0xiczc/2023-05-26-1662090451493740545.md`](posts/0xiczc/2023-05-26-1662090451493740545.md)
- **Precompile-induced state inconsistency on Cosmos EVM chains; Evmos arbitrary mint.** — iczc, [`writeups/0xiczc/`](writeups/0xiczc/)
- **Holes that line up**: unchecked callback return + stale approval + EIP-7702. — kankodu, [`posts/kankodu/2026-09-11-2098377603396915590.md`](posts/kankodu/2026-09-11-2098377603396915590.md)
- **Median oracles**: model the real price spread; 6/11 is the naïve bound. — cmichel, [`posts/cmichelio/2024-06-11-1800463263433678945.md`](posts/cmichelio/2024-06-11-1800463263433678945.md)
- **Governance vote accounting** (Solana validator erasing delegators' votes). — Asymmetric Research, [`posts/asymmetric_re/2026-10-19-2112236410455597403.md`](posts/asymmetric_re/2026-10-19-2112236410455597403.md)
- **EVM-compatible chains break Ethereum assumptions** (Frontier wrapped-native insolvency). — pwning.eth, [`writeups/PwningEth/`](writeups/PwningEth/)
- **Old code still hides bugs** (Guhu95's 5-year-old $60k bug; Shanon on >1-year-old codebases). — [`posts/Guhu95/`](posts/Guhu95/), [`posts/Shanon40439853/`](posts/Shanon40439853/)
- **Price-oracle manipulation and undercollateralised-loan patterns.** — samczsun, [`writeups/samczsun/`](writeups/samczsun/)

---

## Protocol clients & cryptography (Nov 2026)

Drawn from the verbatim advisories under `projects/`.

- **Enumerate every branch of special-case node logic** (free×reverted×non-free). Zcashd / lightwalletd / Polygon zkEVM-style claim and fee paths. Sources: [`projects/zcash/`](projects/zcash/), [`posts/0xiczc/`](posts/0xiczc/).
- **P2P / block-body poisoning**: malformed NU5 bodies, auth-data body poisoning, forged checkpoint blocks that stall sync. Sources: Zebra and zcashd GHSAs under [`projects/zcash/advisories/`](projects/zcash/advisories/).
- **Circuit soundness**: Orchard Action circuit under-constrained base (GHSA-ghc3-g8w4-whf9); use the 0xPARC ZK bug tracker classes. Sources: [`projects/zcash/advisories/ghsa-ghc3-g8w4-whf9.md`](projects/zcash/advisories/ghsa-ghc3-g8w4-whf9.md), [`projects/crypto/zk-bug-tracker-readme.md`](projects/crypto/zk-bug-tracker-readme.md).
- **Solidity compiler version → known bugs**: map pragma to the 67-entry canonical list. Source: [`projects/ethereum/solidity-compiler-bugs.md`](projects/ethereum/solidity-compiler-bugs.md).
- **Crypto crate advisories**: check deps against RustSec (aes-gcm nonce, dalek malleability, etc.). Source: [`projects/crypto/advisories-index.md`](projects/crypto/advisories-index.md).
- **TEE attestation pipeline questions** (enforced TCB? TLS on collateral? stale replay? SSRF on verifier URL?): Bluethroat / saxenism. Sources: [`writeups/saxenism/dumb-ways-to-get-rekt-with-tees.md`](writeups/saxenism/dumb-ways-to-get-rekt-with-tees.md), [`harness/bug-classes/tee-attestation.md`](harness/bug-classes/tee-attestation.md).

---

## Daily update 12 Nov 2026 (Africa/Lagos)

- **CSP `form-action 'self'` credential theft (no JS).** `form-action` does not inherit from `default-src`. Two-stage self-posting form + `meta referrer=unsafe-url` + meta refresh → credentials in Collaborator Referer. Source: [@garethheyes](https://x.com/garethheyes/status/2120523482220167240), [`writeups/garethheyes/blind-trust-stealing-credentials-through-csp.md`](writeups/garethheyes/blind-trust-stealing-credentials-through-csp.md).
- **SSRF: log what the box signs before chasing 169.254.** Point fetch at own sink; worker's own cloud keys/session token arrived. Source: [@mdp_sec](https://x.com/mdp_sec/status/2120519414491566209).
- **TEE checklist (every time):** physical-access → compromised; attestation ≠ safe code; verifier must authenticate+enforce+bind; reproducible build → attested measurement. GPU path that only parses JSON is a "Verified" lie. Source: [@bluethroat_labs](https://x.com/bluethroat_labs/status/2120528783673299290), [`writeups/bluethroat_labs/phala-cloud-gpu-attestation-fake-verified-no-cryptography.md`](writeups/bluethroat_labs/phala-cloud-gpu-attestation-fake-verified-no-cryptography.md).
- **TEE confused deputy:** bind signed message type to the privileged op ("execute" ≠ "migrate"). Source: [@saxenism](https://x.com/saxenism/status/2120538169259209027).
- **AI-agent GitHub Actions:** untrusted issue body into Codex + `/tmp` CoreCLR debug pipes (`MT_ReadMemory`) + cache poison → npm supply chain. Source: Depi via [@Rhynorater](https://x.com/Rhynorater/status/2120539019427889278), [`writeups/Rhynorater/depi-backdooring-codex.md`](writeups/Rhynorater/depi-backdooring-codex.md).
- **ZK emulated scalar mul:** range-check hinted subscalars to the bit-width the EC relation actually consumes (gnark fake-GLV / Zolana High #00). Source: [`writeups/zksecurityXYZ/solana-privacy-rings-zolana-audit-2026-08.md`](writeups/zksecurityXYZ/solana-privacy-rings-zolana-audit-2026-08.md), [`projects/crypto/advisories/gnark-ghsa-7fx8-hmgc-82jp.md`](projects/crypto/advisories/gnark-ghsa-7fx8-hmgc-82jp.md).
- **Besu consensus/crypto:** EIP-7702 / sender recovery must enforce secp256k1 curve-order on r,s (backend divergence → chain split). Source: [`projects/ethereum/advisories/ghsa-4h4f-925g-8h9p.md`](projects/ethereum/advisories/ghsa-4h4f-925g-8h9p.md).
- **Intel TDX attestation:** `verify_x509_cert` must check cert validity period (RUSTSEC-2026-0481). Source: [`projects/crypto/advisories/crates-tdx_workload_attestation-rustsec-2026-0481.md`](projects/crypto/advisories/crates-tdx_workload_attestation-rustsec-2026-0481.md).

## 13 Nov 2026 additions

- **Remediation-bypass hunting (incomplete patch).** Treat every published fix/advisory as a lead: extract the violated impact/invariant, enumerate *all* code paths reaching it, and confirm the patch covers each — not just the PoC path. Re-model actors by capability ("what they COULD do") not policy. Source: saxenism Zcash finding #8 — [`posts/saxenism/2026-11-12-2120829077829582959.md`](posts/saxenism/2026-11-12-2120829077829582959.md).
- **"Formally verified" ZK — check the scope.** A Lean/Coq proof usually covers the interactive protocol in an abstract group, not the Fiat-Shamir transform, the implementation, the concrete curves, or the circuits on top. Hunt in the uncovered layers. Source: [`writeups/zksecurityXYZ/monero-generalized-bulletproofs-lean-proof-2026-11.md`](writeups/zksecurityXYZ/monero-generalized-bulletproofs-lean-proof-2026-11.md).
- **Wallet pentest attack surface.** Key storage, signing flows (WYSIWYS: what is signed must equal what the UI showed — hunt blind-signing/tamper-between-display-and-signature), backend/API authz, and the update supply chain (only trusted accounts publish releases). Source: [`writeups/telegram-defendor_eng/guardianaudits-crypto-wallet-pentest-2120924685890413008.md`](writeups/telegram-defendor_eng/guardianaudits-crypto-wallet-pentest-2120924685890413008.md).
- **Score AI-found candidates before reporting.** Volume AI vuln-discovery (Glasswing: 37,966 findings, 2 ITW, ~56% false-positive on curl's sample) means a harness must rank by reachability/impact and dedup against CVE/GHSA/KEV before filing, or it just shifts triage burden to maintainers. n-days are the higher-value defender automation target. Source: [`writeups/S1r1u5_/glasswing-nday-0day-exploited-in-wild-2026-11.md`](writeups/S1r1u5_/glasswing-nday-0day-exploited-in-wild-2026-11.md).
- **Exchange custody drains (Mercado Bitcoin $48.6M).** Signing access reached both the payout system (hot wallets) and deposit-address keys (36,042 swept); exchanges often derive deposit keys from one master key, so a root compromise exposes all derived addresses — disabling a payout system does not revoke a stolen key. Source: [`writeups/telegram-defendor_eng/mercado-rekt-c0939a8c.md`](writeups/telegram-defendor_eng/mercado-rekt-c0939a8c.md).


## 14 Nov 2026 additions

- **Cross-tenant IDOR that returns a *credential* (not just data).** On "connect/link/import integration" flows, create a resource on your own account but pass another tenant's `link id`; read the object back and inspect the response/stored object for credential-shaped values (`Authorization`, `Bearer`, `x-api-key`, AWS keys, JWT). If the backend bound the victim's creds to your object, you get a live auth header and can walk ids across tenants → account/tenant takeover. Automate with a two-account diff + credential-regex scanner on the link parameter. Source: [`posts/mdp_sec/2026-11-13-2121244189593940355.md`](posts/mdp_sec/2026-11-13-2121244189593940355.md).
- **Pin the inference provider, benchmark by cost-per-solve.** For an autonomous hacking harness, the same model name served via an aggregator can be a quantized build that halves solve rate; call the first-party API directly, and choose models by $-per-solved-lab and refusal rate, not benchmark score or recency (Grok 4.6 beat 4.7 2:1 at a quarter of the cost on 100 black-box labs). Source: [`posts/mdp_sec/2026-11-13-2121358210577883544.md`](posts/mdp_sec/2026-11-13-2121358210577883544.md).
- **Hunt un-redacted secrets in LLM/agent trace & training stores.** The Cursor/Fireworks breach chained a partner-exposed access key → read-only trace bucket → un-redacted customer creds in <0.01% of traces → SaaS pivot → poisoned Claude Code extension on the marketplace CDN cache. Check agent traces/logs for `Authorization`/`Bearer`/`x-api-key`/AWS keys; verify served extension/plugin artifact hashes against the signed source (CDN cache poisoning bypasses a clean upstream). Source: [`writeups/S1r1u5_/cursor-security-incident-update-2026-11.md`](writeups/S1r1u5_/cursor-security-incident-update-2026-11.md).
- **Patch-gap is now the dominant window (Project Zero "Full X").** No grace period, zero patch-to-exploit assumed; prioritize an automated patch-diff → PoC pipeline on freshly disclosed bugs. Source: [`writeups/S1r1u5_/project-zero-disclosure-policy-update-2026-11.md`](writeups/S1r1u5_/project-zero-disclosure-policy-update-2026-11.md).
- **Stored XSS → nonce-inheriting script exec → admin takeover.** Basecamp H1 #4175245: attacker HTML survived in a `bc-attachment content` attribute; when an admin opened the edit form, a legacy path wrote attacker HTML via `innerHTML`, then a cross-origin `turbo-frame` response inherited the victim page's CSP nonce so the script ran in-origin, read the CSRF token, and called the admin-grant endpoint. Hunt rich-text normalizers + Turbo/HTMX frame nonce inheritance. Source: [`hackerone/reports/2026/4175245.md`](hackerone/reports/2026/4175245.md).
- **OpenAPI `$id` rebasing → local file read.** Burp Community H1 #4000535: validator and click-parser selected different OpenAPI objects from one response (3.0 `swaggerDoc` enabled the action, 3.1 top-level parsed on click); a `file:///` URL in `$id` became the base for a fragment `$ref`, reading a local schema example. Parser-differential + schema `$id`/`$ref` base rebasing is a reusable local-resource-restriction bypass. Source: [`hackerone/reports/2026/4000535.md`](hackerone/reports/2026/4000535.md).
- **PHP string-synthesis filter bypass.** PHP `^` (and old string `++`) builds blocked function names (`system`, `exec`, `id`, `curl`) from allowed bytes at runtime, defeating denylists; detect by probing XOR-composed function execution, defend with allowlists / disabled functions. Source: [`posts/garethheyes/2026-11-13-2121236435273675134.md`](posts/garethheyes/2026-11-13-2121236435273675134.md).
- **Email-only bounty intake drops `.zip` PoCs.** Gmail/Workspace silently blocks archive/executable attachments; inline the PoC or host it behind an authenticated link rather than attaching an archive. Source: [`posts/saxenism/2026-11-13-2121239127467434217.md`](posts/saxenism/2026-11-13-2121239127467434217.md).
- **RCE proof-of-impact bar is rising.** Some programs now reject `id`/`whoami` output and expect demonstrated post-exploitation (cred access, lateral movement) — but retrieving real sensitive data to "prove impact" can violate the asset owner's policy even when the platform requests it; record exactly what each program accepted. Source: [`posts/albinowax/2026-11-13-2121234124476183016.md`](posts/albinowax/2026-11-13-2121234124476183016.md).

## 17 Nov 2026 additions

- **Composite-key IDOR in AI support-bot "tools".** A Bugcrowd $1,500 horizontal IDOR: the bot's tool endpoint checked that `user_id` matched `chat_id` but never that either belonged to the session. Proxy the chat widget, collect tool/function-call requests, and from a second account replay the full `(user_id, chat_id)` pair — a 403 that only clears when both ids are the victim's is still exploitable via full-pair swap. Automate a "composite-key swap" module that permutes any request with ≥2 object ids against a second account's id pool. Source: [`posts/mdp_sec/2026-11-16-2122270955019919655.md`](posts/mdp_sec/2026-11-16-2122270955019919655.md).
- **OAuth `redirect_uri` non-HTTP scheme fuzzing → ATO.** @rgjny_ (quoted by Rhynorater, triaged High 8.1): `redirect_uri=android-app://…` passed validation and leaked the auth code to an attacker scheme — "works without any app installed and the attack only takes a link." Add `android-app://`, `intent://…#Intent;scheme=https;end`, `ios-app://`, and target custom schemes to the redirect_uri fuzz set; flag a `Location` carrying `code`/`token` to the alternate scheme. Source: [`posts/Rhynorater/2026-11-16-2122339336163090519.md`](posts/Rhynorater/2026-11-16-2122339336163090519.md).
- **Safe/Zodiac Roles unconstrained recipient = drain primitive.** $6.45M Safe drain: the Roles Modifier scoped a value-moving function but left the recipient (`to`/`receiver`/`onBehalfOf`) unconstrained. Enumerate modules with `getModulesPaginated`, read scope events, and for every allowed function verify the recipient is pinned to the avatar (EqualToAvatar); also check `ExecutionOptions` DelegateCall and multisend unwrapping. Source: [`posts/0xriptide/2026-11-16-2122371409594749120.md`](posts/0xriptide/2026-11-16-2122371409594749120.md), [`writeups/telegram-defendor_eng/specter-gnosis-safe-zodiac-roles-6-45m-drain.md`](writeups/telegram-defendor_eng/specter-gnosis-safe-zodiac-roles-6-45m-drain.md).
- **Exposed self-hosted LLM servers with tools = free shell.** llama.cpp / Ollama / LM Studio OpenAI-compatible endpoints on LAN (8080/11434/1234/8000) with no api-key and tool/MCP calling enabled grant command execution. Scan internal ranges for these ports during recon. Source: [`posts/mdp_sec/2026-11-17-2122550959608131942.md`](posts/mdp_sec/2026-11-17-2122550959608131942.md).
- **libcurl SSH connection reuse skips the per-transfer host-key pin.** curl H1 #4199917: `ssh_config_matches()` compares only key *filenames*, so a reused SFTP/SCP connection ignores a later transfer's `--hostpubsha256`/`--hostpubmd5`/known_hosts pin (same class as CVE-2023-27538). Test multi-transfer libcurl apps: a wrong pin that succeeds on a reused connection but fails on a fresh one confirms it. Source: [`hackerone/reports/2026/4199917.md`](hackerone/reports/2026/4199917.md).
- **Reward-checkpoint mint & e-mode self-liquidation.** CHAIN (~37.98M on Polygon) abused a delegation reward-checkpoint bug to mint delegation tokens from a small stake; MORE DeFi on Flow EVM (~$308k) self-liquidated correlated-asset e-mode positions after a flash loan, leaving unbacked debt paid from the reserve. Invariants: `sum(delegation tokens)==sum(underlying)` at every checkpoint; self-liquidation must never leave bad debt. Sources: [`writeups/telegram-defendor_eng/chain-polygon-staking-exploit-reward-checkpoint-mint.md`](writeups/telegram-defendor_eng/chain-polygon-staking-exploit-reward-checkpoint-mint.md), [`writeups/telegram-defendor_eng/more-defi-flow-evm-self-liquidation-emode-exploit.md`](writeups/telegram-defendor_eng/more-defi-flow-evm-self-liquidation-emode-exploit.md).
- **Gas-repricing invariants (EIP-8037/8038).** pcaversaccio: pending gas repricings break immutable contracts that rely on fixed gas stipends, `gasleft()` thresholds, or refund economics. Audit deployed contracts for 2300-stipend guards and gas-based branching. Source: [`posts/pcaversaccio/2026-11-16-2122277228855836959.md`](posts/pcaversaccio/2026-11-16-2122277228855836959.md).

### Added 18 Nov 2026
- **Java4Shell (CVE-2026-114938).** OpenJDK 17.0.6+ HotSpot AVX-512 VBMI Base64 decoder heap overflow (`"A"*64+"="`; JDK 17 needs 128 A's); pre-auth via Basic auth / JWT / SAML Base64 decoding on Ice Lake+/Zen 4+ hosts; mitigation `-XX:-UseBASE64Intrinsics` or `-XX:UseAVX=2`. Sources: [`writeups/irsdl/java4shell-calif-write-once-rce-everywhere.md`](writeups/irsdl/java4shell-calif-write-once-rce-everywhere.md), [`writeups/irsdl/java4shell-vulncheck.md`](writeups/irsdl/java4shell-vulncheck.md); harness digest [`harness/bug-classes/2026-11-18-java4shell-imagemagick-sig-binding-nonce.md`](harness/bug-classes/2026-11-18-java4shell-imagemagick-sig-binding-nonce.md).
- **ImageMagick SVG-in-JPG file read + WAF slash-doubling + public CDN.** @mdp_sec: upload an SVG named .jpg, backend ImageMagick renders `text:`-read server files into the output image; WAF blocked the path until a doubled slash; stored image on a public CDN exposed prod source + hardcoded credential. [`posts/mdp_sec/2026-11-17-2122784337888506335.md`](posts/mdp_sec/2026-11-17-2122784337888506335.md).
- **Signature bound to a different occurrence / ownership proof not bound to action** (HackenProof titles posted by @Piki_eth; details undisclosed): [`posts/Piki_eth/2026-11-17-2122570832006586557.md`](posts/Piki_eth/2026-11-17-2122570832006586557.md).
- **Nonce reuse in client signing code (Lighter).** @saxenism's analysis + Telegram post-mortem; recover key from repeated `r`: [`posts/saxenism/2026-11-17-2122673176752619797.md`](posts/saxenism/2026-11-17-2122673176752619797.md).
- **CVE-2026-21601 Jira Service Management DC BASM** (Nagli/Wiz, pre-auth act-as-another-user, CVSS 4.0 8.7): [`posts/galnagli/2026-11-17-2122787201176019399.md`](posts/galnagli/2026-11-17-2122787201176019399.md).
- **Frag update (CSS-only token exfil):** one-shot blind exfil, Base64/alphanumeric tokens: [`posts/garethheyes/2026-11-17-2122639054638301455.md`](posts/garethheyes/2026-11-17-2122639054638301455.md).
- **Zebra / lightwalletd GHSA wave (24 advisories)**: peer-triggerable sync halts / OOM, RPC password exposed via `/debug/vars`: [`projects/zcash/advisories-index.md`](projects/zcash/advisories-index.md).
