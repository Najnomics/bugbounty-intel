# @saxenism — Rahul Saxena (Bluethroat Labs founder)

Compiled 11 Nov 2026 (WAT). Dorothy specifically asked for him: he posts a large volume of TEE / ZK / protocol-security material. Full verbatim posts under [`posts/saxenism/`](../posts/saxenism/) (470 files, Oct 2024 → Nov 2026 — as far as the X timeline API allows). Writeups under [`writeups/saxenism/`](../writeups/saxenism/). He is also the founder behind [@bluethroat_labs](bluethroat_labs.md), already in this repo.

| Field | Value |
| --- | --- |
| X | [@saxenism](https://x.com/saxenism) (user id 1199306572083519488, created 2019-11-26) |
| Name | Rahul Saxena |
| Followers (11 Nov 2026) | 4135 |
| Bio (verbatim) | Founder @bluethroat_labs \| ex-Security @zksync \| ETHSecurity Badge \| AI security for complex protocols |
| Specialty | TEE / confidential computing security, ZK, L2/protocol security, AI-assisted auditing |
| Platforms | Immunefi (via Bluethroat Labs); private protocol work; ETHSecurity |
| Links | https://bluethroatlabs.com, https://tee-security-handbook.bluethroatlabs.com |

## Capture completeness

- **Captured:** 470 original-post files spanning **2024-10-01 → 2026-11-10** (timeline API floor). Includes self-reply threads where conversation_id was present, media notes, quoted posts, expanded links.
- **Not retrievable:** posts before ~2024-10-01 (X `get_users_posts` returns `next_token: null` after Nov 2024 pages; account created 2019-11-26, so ~5 years of earlier posts are beyond the API reach). `search_posts_all` only indexes ~30 days and cannot backfill that gap.
- Linked writeups saved: dumb-ways-to-get-rekt-with-tees, TEE security handbook, Argument.xyz RISC-V blog, Bluethroat docs home, Turnkey whitepaper foundations. The Reveries vulnerability-writeup listing is a JS SPA and returned no extractable article bodies.

## Key themes in the captured posts (for harness use)

- **TEE attack surface:** dstack / Phala attestation pipeline, Nitro, SGX, "dumb ways to get rekt with TEEs", forged checkpoint / body-poisoning style bugs in Zebra (he linked [GHSA-9hq5-pfgc-cx5h](../projects/zcash/advisories/ghsa-9hq5-pfgc-cx5h.md)).
- **ZK / circuit soundness:** underconstrained circuits, Orchard-adjacent discussions; cross-ref Zcash Orchard soundness advisories under [`projects/zcash/`](../projects/zcash/).
- **Protocol / L2 security** and AI-assisted hunting for complex protocols (Bluethroat Labs positioning).

See tagged posts under `posts/saxenism/` (auto keyword tags: TEE, ZK, Blockchain, AI). Harness check specs for TEE and ZK live under [`harness/bug-classes/tee-attestation.md`](../harness/bug-classes/tee-attestation.md) and [`zk-circuits.md`](../harness/bug-classes/zk-circuits.md).

## Writeups saved

- [`writeups/saxenism/dumb-ways-to-get-rekt-with-tees.md`](../writeups/saxenism/dumb-ways-to-get-rekt-with-tees.md)
- [`writeups/saxenism/tee-security-handbook.md`](../writeups/saxenism/tee-security-handbook.md)
- [`writeups/saxenism/argument-xyz-riscv-good-bad.md`](../writeups/saxenism/argument-xyz-riscv-good-bad.md)
- [`writeups/saxenism/bluethroat-docs-home.md`](../writeups/saxenism/bluethroat-docs-home.md)
- [`writeups/saxenism/turnkey-whitepaper-foundations.md`](../writeups/saxenism/turnkey-whitepaper-foundations.md)

## Key findings (mined into harness)

_Auto-maintained from `harness/findings.jsonl`. 5 finding(s). Full verbatim posts under `posts/saxenism/`._

- **argument-xyz-riscv-good-bad** (`zk-circuits`)
  - post: https://argument.xyz/blog/riscv-good-bad/
  - local: `writeups/saxenism/argument-xyz-riscv-good-bad.md`
- **bluethroat-docs-home** (`tee-attestation`)
  - post: https://docs.bluethroatlabs.com
  - local: `writeups/saxenism/bluethroat-docs-home.md`
- **dumb-ways-to-get-rekt-with-tees** (`tee-attestation`)
  - post: https://bluethroatlabs.com/docs/dumb-ways-to-get-rekt-with-tees
  - local: `writeups/saxenism/dumb-ways-to-get-rekt-with-tees.md`
- **tee-security-handbook** (`tee-attestation`)
  - post: https://tee-security-handbook.bluethroatlabs.com
  - local: `writeups/saxenism/tee-security-handbook.md`
- **turnkey-whitepaper-foundations** (`tee-attestation`)
  - post: https://whitepaper.turnkey.com/foundations
  - local: `writeups/saxenism/turnkey-whitepaper-foundations.md`

### SGX authorization confused deputy + NEAR AI SGLang incident — 11 Nov 2026

- Post: https://x.com/saxenism/status/2120538169259209027 — verbatim: [`posts/saxenism/2026-11-11-2120538169259209027.md`](../posts/saxenism/2026-11-11-2120538169259209027.md)
- Incident report: [`writeups/saxenism/near-ai-sglang-security-incident-report.md`](../writeups/saxenism/near-ai-sglang-security-incident-report.md)
- **Bug class:** TEE authorization logic / confused deputy; also software RCE inside TEE (SGLang)
- **Root cause (SGX lesson):** Signed "execute" accepted as "migrate"; attestation/signatures fine, intent binding missing. NEAR AI: SGLang RCE on inference server let attacker see confidential requests — TEE does not protect against bugs in software *inside* the enclave.
- **Takeaways:** Bind signed message type to privileged op; treat inference-engine deps with same rigor as the enclave itself.

### SGX authorization confused deputy + NEAR AI SGLang incident — 11 Nov 2026

- Post: https://x.com/saxenism/status/2120538169259209027 — verbatim: [`posts/saxenism/2026-11-11-2120538169259209027.md`](../posts/saxenism/2026-11-11-2120538169259209027.md)
- Incident report: [`writeups/saxenism/near-ai-sglang-security-incident-report.md`](../writeups/saxenism/near-ai-sglang-security-incident-report.md)
- **Bug class:** TEE authorization logic / confused deputy; also software RCE inside TEE (SGLang)
- **Root cause (SGX lesson):** Signed "execute" accepted as "migrate"; attestation/signatures fine, intent binding missing. NEAR AI: SGLang RCE on inference server let attacker see confidential requests — TEE does not protect against bugs in software *inside* the enclave.
- **Takeaways:** Bind signed message type to privileged op; treat inference-engine deps with same rigor as the enclave itself.

### Zcash campaign accepted finding #8 (High) — remediation bypass — 12 Nov 2026

- Post: https://x.com/saxenism/status/2120829077829582959 — verbatim: [`posts/saxenism/2026-11-12-2120829077829582959.md`](../posts/saxenism/2026-11-12-2120829077829582959.md)
- **Bug class:** incomplete-patch / remediation bypass (same impact via an unaccounted path), @bluethroat_labs Zcash campaign.
- **Root cause:** came out of reviewing the *remediation* of an already-disclosed bug; the patch closed the exact path in the original report, but the impact stayed reachable through a path the fix did not account for. (Quoted finding #7: threat-modelling on what actors *should* do vs *could* do.)
- **Takeaways:** review patches, not just code — enumerate every path to the fixed impact; model by capability. Add a harness "remediation review" mode seeded from CVE/GHSA fix commits.

## Daily update 2026-11-16

### Flare Confidential Compute attestation-policy questions (2026-11-15)

- Post: https://x.com/saxenism/status/2121975522028859699 — verbatim: [`posts/saxenism/2026-11-15-2121975522028859699.md`](../posts/saxenism/2026-11-15-2121975522028859699.md)
- **Bug class:** TEE / remote-attestation policy review (no bug claimed)
- **Root cause:** Open questions: which hardware/TCB claims are accepted, who updates policy after Google firmware rollouts, can users inspect the rules.
- **How it was found:** Reading Flare FCC docs (image hashes pinned on-chain + machine registration via attestation).
- **Takeaways / harness:** Attestation checklist: accepted measurements, TCB floor, debug flag, policy-update authority, verifiability.

