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


### Update 2026-11-18

- **Lighter nonce-reuse thread** — https://x.com/saxenism/status/2122673176752619797 — [`posts/saxenism/2026-11-17-2122673176752619797.md`](../posts/saxenism/2026-11-17-2122673176752619797.md); supply-chain-is-not-P3 post https://x.com/saxenism/status/2122632691346800678.


### Update 2026-11-19

- **Bluethroat Labs Zcash campaign: 4 High + 1 Medium GHSAs published (18 Nov 2026)** — https://x.com/saxenism/status/2123003101548556624 — [`posts/saxenism/2026-11-18-2123003101548556624.md`](../posts/saxenism/2026-11-18-2123003101548556624.md); advisories (verbatim) in [`projects/zcash/advisories/`](../projects/zcash/advisories/) (lightwalletd GHSA-p4pq-3cf7-45rv, GHSA-5xg7-x58j-m5vr, GHSA-xrx5-jc6q-9h8r, GHSA-8vh8-6jg3-8f5v; zebra GHSA-hj54-2mfv-4xg8; earlier zebra high GHSA-9hq5-pfgc-cx5h).
  - Separately, accepted finding #8 (High) of the Zcash campaign came from reviewing the *remediation* of an already-disclosed bug: the patch closed the reported path but the impact stayed reachable via another path ([post](../posts/saxenism/2026-11-18-2122996063590334928.md)). Takeaway: retest the impact state, not the original PoC; he notes that is closer to a property to formally verify than a test.


### Update 2026-11-21

- **GHSA-6r9w-cxjj-5776 — `@taquito/sapling` commitment trapdoor `rcm` + spend rerandomizer `ar` reuse (published 2026-11-20, low)** — https://github.com/ecadlabs/taquito/security/advisories/GHSA-6r9w-cxjj-5776 (thanked by ECAD Labs: https://x.com/jevonearth/status/2123844421766828423; reply https://x.com/saxenism/status/2123897866594951670). Class: cryptographic randomness reuse / privacy break. Root cause: random values sampled once outside per-output/per-input loops. How found: code review of the Sapling tx builder, validated on an Octez 25.3 sandbox replay harness, reported to security@tezos.com 2026-11-15. Takeaway: grep for hoisted randomness in shielded-tx builders. Files: [`writeups/saxenism/taquito-GHSA-6r9w-cxjj-5776.md`](../writeups/saxenism/taquito-GHSA-6r9w-cxjj-5776.md), [`projects/crypto/advisories/taquito-sapling-ghsa-6r9w-cxjj-5776.md`](../projects/crypto/advisories/taquito-sapling-ghsa-6r9w-cxjj-5776.md), [`posts/saxenism/2026-11-20-2123897866594951670.md`](../posts/saxenism/2026-11-20-2123897866594951670.md).
- **DeFi Security Summit 2026 talk: real nature of TEEs and secure use in web3** — https://x.com/saxenism/status/2124014069644701728 — [`posts/saxenism/2026-11-21-2124014069644701728.md`](../posts/saxenism/2026-11-21-2124014069644701728.md), page [`writeups/saxenism/dss2026-tee-talk-page.md`](../writeups/saxenism/dss2026-tee-talk-page.md) (video; no transcript).

## 2026-11-25 — TEE Security Handbook funding push
- [Post](../posts/saxenism/2026-11-24-2125143637340348752.md): TEE Security Handbook (Bluethroat Labs) up for funding on The DAO Fund; $4.5k pledges needed by 2026-11-25 14:00 UTC; mentions his DSS talk on the attestation gap in TEE-backed DeFi. Handbook text already archived at [`writeups/saxenism/tee-security-handbook.md`](../writeups/saxenism/tee-security-handbook.md).
