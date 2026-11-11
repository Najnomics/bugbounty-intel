# Recon methodology (merged)

_Merged from the hunters' own published workflows. The most complete public, step-by-step methodology in this repo is Marius du Preez's prompt pack, saved verbatim under [`writeups/mdp_sec/prompts/`](../writeups/mdp_sec/prompts/). Everything below cites a local file; nothing is invented._

## The backbone: Marius du Preez's phased workflow

Full text: [`writeups/mdp_sec/prompts/`](../writeups/mdp_sec/prompts/) (his repo <https://github.com/mdpsec/bug-bounty-hunting-prompts>). The phase sequence:

| Phase | File | Purpose |
| --- | --- | --- |
| 0 | [phase-00-recon](../writeups/mdp_sec/prompts/phases/phase-00-recon.md) | Lightweight unauthenticated surface map |
| 1 | [phase-01-access](../writeups/mdp_sec/prompts/phases/phase-01-access.md) | Account setup and authenticated access |
| 2 | [phase-02-sweep](../writeups/mdp_sec/prompts/phases/phase-02-sweep.md) | Broad endpoint + vulnerability-class sweep (the class matrix) |
| 3 | [phase-03-closeout](../writeups/mdp_sec/prompts/phases/phase-03-closeout.md) | Validate handoff, release resources |
| 4a/4b | [scope](../writeups/mdp_sec/prompts/phases/phase-04a-scope.md) / [browser-walk](../writeups/mdp_sec/prompts/phases/phase-04b-browser-walk.md) | Authenticated browser walk |
| 5a/5b | [scope](../writeups/mdp_sec/prompts/phases/phase-05a-scope.md) / [critical](../writeups/mdp_sec/prompts/phases/phase-05b-critical.md) | Critical-impact hunting |
| 6 | [phase-06-triage](../writeups/mdp_sec/prompts/phases/phase-06-triage.md) | Triage + dedupe |
| 7 | [phase-07-validate-escalate](../writeups/mdp_sec/prompts/phases/phase-07-validate-escalate.md) | Validate + escalate |
| 8 / 8a | [verify-escalate](../writeups/mdp_sec/prompts/phases/phase-08-verify-escalate.md) / [independent](../writeups/mdp_sec/prompts/phases/phase-08a-independent-escalation.md) | Independent verification |
| 9 | [phase-09-triage-gate](../writeups/mdp_sec/prompts/phases/phase-09-triage-gate.md) | Independent live triage gate |
| 10 | [phase-10-self-duplicate-check](../writeups/mdp_sec/prompts/phases/phase-10-self-duplicate-check.md) | Same-program duplicate convergence |

Adaptation index (every `YOUR_*`/placeholder integration): [ADAPTATION.md](../writeups/mdp_sec/prompts/ADAPTATION.md).

## Phase 0 — surface map (concrete steps, from phase-00-recon)

- Build the **minimum** unauth map; do not hunt in recon.
- Subdomains (wildcard only): `subfinder -d APEX -silent`, prioritise hosts matching `(app|api|auth|account|id|login|portal|dashboard|console|admin|www)\.`, cap at 200.
- Liveness/tech: `httpx -silent -status-code -title -tech-detect -content-length -follow-redirects`.
- Shallow browser map: visit only 3–6 routes (root, signup, login, reset, account, API entry), capture traffic with mitmdump, extract `METHOD url` and `status METHOD url`.
- Build first-party sibling list from redirects/form actions/XHR/fetch/WebSocket; ignore analytics, captcha, CDN, payment, support, identity providers.
- JS + operation inventory → `operation-candidates.jsonl` as Phase 2 hypotheses.
- P00 does **not** run Amass, Naabu, Gau, DNSx, Nuclei, GitHub scanning, default-cred checks, or broad wordlist fuzzing (those belong to later phases). Source: [phase-00-recon](../writeups/mdp_sec/prompts/phases/phase-00-recon.md).

## Phase 2 — the class matrix (what to test, in priority order)

The authoritative per-class list, stage (A = controller/stateful, B = stateless/delegable), and modes is in [phase-02-sweep](../writeups/mdp_sec/prompts/phases/phase-02-sweep.md). Key priorities:

- **High value:** access control (IDOR cross-account, id-walk, path-bypass, API-version bypass, function-level), auth/session (JWT, OAuth, password reset, token leak, pre-auth bypass), business logic (numeric tampering, mass assignment, race, workflow step-skip, entitlement), server-side execution (SSRF, SSTI, XXE, deser, LFI, upload processing).
- **Demoted:** systematic parameter fuzzing for SQLi/NoSQLi/command/CSV — *zero* confirmed origins over his last 100 reports / ~107h; opportunistic only. (SSTI, LFI, header injection are NOT demoted.)
- **Skip as standalone:** CORS, login/account enumeration, timing oracles, rate-limit absence — report only when they enable an ATO or mass-data chain.

See per-class check specs in [`bug-classes/`](bug-classes/).

## Testing policy (from the sweep + should-i-submit)

- Bounded, non-destructive proofs; restore reversible changes; no bulk data, no real users, no DoS. Source: [phase-02-sweep](../writeups/mdp_sec/prompts/phases/phase-02-sweep.md), [should-i-submit-readme](../writeups/mdp_sec/should-i-submit-readme.md).
- Pre-submission gate: one report = one root cause (or one necessary chain); split unrelated findings; a report must contain real proof, not recon notes. The `should-i-submit` reviewer returns `YES` / `NO` / `NOT YET` / `CANNOT DECIDE SAFELY`. Source: [should-i-submit-readme](../writeups/mdp_sec/should-i-submit-readme.md).

## Cross-researcher recon notes

- Enumerate **every** OAuth client_id (web/iOS/Android/desktop) — redirect_uri validation often differs per client. Source: [`posts/xssdoctor/`](../posts/xssdoctor/).
- Brute-force hidden/internal headers (Param Miner); trusted internal headers accepted externally paid $300k. Source: [`posts/albinowax/`](../posts/albinowax/).
- Feed mobile-static seeds (hosts, routes, intents, object refs) into web recon. Source: [phase-00-recon](../writeups/mdp_sec/prompts/phases/phase-00-recon.md), [`posts/_bagipro/`](../posts/_bagipro/).
- For Web3: read both circuits and verifiers; model oracle source spread; audit callback/approval patterns and governance vote accounting. Source: [`bug-classes/smart-contract.md`](bug-classes/smart-contract.md), [`bug-classes/zk-circuits.md`](bug-classes/zk-circuits.md).

See also the repo-wide [`techniques.md`](../techniques.md).
