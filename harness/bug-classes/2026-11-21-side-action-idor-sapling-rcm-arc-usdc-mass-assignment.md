# Bug classes from the 21 Nov 2026 run (side-action IDOR, Sapling randomness hoisting, Arc dual-decimal USDC, nested-schema mass assignment, IP-gated admin check, AI-agent rejection audit)

Sources are verbatim in the repo; this file is the harness-oriented digest. Items marked *(inference)* go beyond what the source states.

## 1. Cross-tenant IDOR on a "little button" side action (@mdp_sec, Medium)
- Source: [`posts/mdp_sec/2026-11-20-2123871501539783102.md`](../../posts/mdp_sec/2026-11-20-2123871501539783102.md).
- Vendor portal with 1m+ sequential ticket ids: list + detail endpoints checked tenant; the **mark-for-follow-up** endpoint did not → returned another vendor's note, author and vendor id; **unmark** deleted it; **re-mark** wrote attacker text into the victim's ticket view. Normal vendor login, no victim click.
- Harness check: two owned tenants (A, B). Enumerate every request carrying B's object id, including toggles (follow/flag/star/pin/watch/subscribe/archive/mark-read/assign/tag). Replay with A's session; flag any 2xx returning B's fields or changing B's state. Always run the toggle sequence mark → unmark → mark.

## 2. Randomness hoisted out of a per-item crypto loop — Sapling `rcm`/`ar` reuse (GHSA-6r9w-cxjj-5776, @saxenism)
- Sources: [`projects/crypto/advisories/taquito-sapling-ghsa-6r9w-cxjj-5776.md`](../../projects/crypto/advisories/taquito-sapling-ghsa-6r9w-cxjj-5776.md), [`writeups/saxenism/taquito-GHSA-6r9w-cxjj-5776.md`](../../writeups/saxenism/taquito-GHSA-6r9w-cxjj-5776.md).
- `@taquito/sapling` <= 25.1.2 called `getRandomCommitmentTrapdoor()` once per tx and `getRandomPublicKeyReRandomization()` once per spend batch; every output (incl. change) shared `rcm` → any recipient decrypting their note can test candidate `(address, value)` against other outputs' public `cm`. Fixed 25.1.3 (sample inside loop). Fork `@tezos-x/octez.js-sapling` unpatched at advisory time.
- Harness check (static): in wallet/SDK code, find `getRandom*`/`random*`/`rcm`/`rseed`/`esk`/`alpha`/`ar`/nonce/IV assigned before `map`/`for` over outputs/inputs and passed into each iteration. Dynamic: build a 2-output tx, decrypt both notes, assert per-note randomness differs. Generalises to ECDSA/Schnorr nonce reuse and AES-GCM IV reuse. *(inference: check other Sapling/Orchard JS/Rust wallet builders and forks for the same pattern.)*

## 3. Arc (Circle L1) native-USDC dual interface: 18-dec native vs 6-dec ERC-20 on the same balance (B612 threat model)
- Source: [`writeups/telegram-defendor_eng/b612-arc-usdc-dual-decimals-threat-model-privacy-protocol-crit.md`](../../writeups/telegram-defendor_eng/b612-arc-usdc-dual-decimals-threat-model-privacy-protocol-crit.md) (B612's Parth found a critical in a privacy protocol on Arc from a flawed chain assumption; mechanism undisclosed).
- Properties to test: `USDC.balanceOf(a) = floor(nativeBalance(a)/10^12)` — vaults summing both views overstate reserves; boundary-test 10^12−1 / 10^12 / 10^12+1 native units; native `call{value:}` not limited by ERC-20 allowance; system emitter `0xffff…fffE` 18-dec log + ERC-20 6-dec Transfer for one movement → indexers must not double-credit (key on `(chainId, txHash, systemLogIndex)`); blocklisted-recipient / zero-address / precompile payout reverts must preserve claims; `Memo`/`Multicall3From` route via CallFrom so target sees the signing EOA as `msg.sender`, `allowFailure` legs can fail silently; `PREVRANDAO` = 0; adjacent blocks may share timestamps; CCTP/Gateway/StableFX need destination-side settlement checks.
- Harness: add an "Arc profile" to the smart-contract pass: grep for `address(this).balance` + `IERC20(USDC).balanceOf` summed, `msg.value` + `transferFrom` deposit paths with different scaling, `block.prevrandao` usage, `block.timestamp` strict ordering.

## 4. Nested-schema mass assignment (Rocket.Chat H1 #4059370, CVE-2026-106075)
- Source: [`hackerone/reports/2026/4059370.md`](../../hackerone/reports/2026/4059370.md).
- `POST /api/v1/chat.sendMessage`: outer body `additionalProperties:false`, inner `message` object unrestricted; REST path calls `executeSendMessage` directly, bypassing the DDP `check()` allow-list → default user sets `md`, `reactions`, `actionLinks`, `urls`, `pinned`, `pinnedBy`, `starred`, `editedBy`, `editedAt` → room DoS, stored iframe via forged link preview, cross-user starred/pin/edit spoofing, invisible mentions.
- Harness check: for each JSON API, diff the accepted field set of sibling endpoints (REST vs RPC/DDP/GraphQL) and add server-controlled fields (`*By`, `*At`, `pinned`, `role`, `owner`, `verified`, `urls/preview`) inside *nested* objects; verify persistence by re-reading the object.

## 5. IP-gated admin check reused as identity check (Nextcloud H1 #4004074)
- Source: [`hackerone/reports/2026/4004074.md`](../../hackerone/reports/2026/4004074.md).
- `SubAdmin::isUserAccessible()` used `isAdmin()` which returns false when the *request IP* is outside `allowed_admin_ranges` → subadmin outside the range could reset a group-member admin's password (`PUT /ocs/v2.php/cloud/users/<admin>` `key=password`) → admin takeover. Siblings used IP-independent `isInGroup(...,'admin')`.
- Harness check: when an app has context-dependent role helpers (IP allowlist, step-up auth, device trust), grep for those helpers used to classify a *target* user; test privileged-target actions from outside the restricted context.

## 6. libcurl `Host: []` cookie-domain truncation (H1 #4218369, CVE-2026-6276 listed; report closed N/A)
- Source: [`hackerone/reports/2026/4218369.md`](../../hackerone/reports/2026/4218369.md). Malformed custom `Host: []` + shared `CURLSH` cookie store → cookie stored with empty domain, later sent to a different numeric IP. Harness: when an app proxies user-controlled Host headers through libcurl with shared cookie jars, test empty/bracketed Host values.

## 7. AI-auditor rejection audit (@DevDacian, Cyfrin)
- Source: [`posts/DevDacian/2026-11-20-2123789113660768415.md`](../../posts/DevDacian/2026-11-20-2123789113660768415.md).
- Strong models can lose recall by wrongly *rejecting* valid findings. Fix: log every rejection with its reason and run a separate cross-model review agent over the rejections; one mental frame per agent. Directly maps to apex-core `disprove_finding`/phase-6 gates: add a "rejection auditor" pass.

## 8. Provider drift for the same model (@mdp_sec)
- Sources: [`posts/mdp_sec/2026-11-20-2123660108425035820.md`](../../posts/mdp_sec/2026-11-20-2123660108425035820.md), [`writeups/mdp_sec/blackboxarena-deepseek-v4-1-flash-providers.md`](../../writeups/mdp_sec/blackboxarena-deepseek-v4-1-flash-providers.md).
- Same model, 15 hosts: 5–18/40 black-box labs solved; one host silently swapped weights (refusals 83–98% → 1%); abliterated builds solve fewer labs. Harness: pin provider, run canary evals on provider change, log provider per finding.
