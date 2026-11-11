# Techniques and patterns

High-level methodology, recon tips, and bug patterns pulled from the public sources in this repo. Each item is linked to its source. This is a workflow aid, not an exploit guide: reproduction steps and payloads stay in the original writeups.

Last updated: 11 November 2026 (Africa/Lagos).

---

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
