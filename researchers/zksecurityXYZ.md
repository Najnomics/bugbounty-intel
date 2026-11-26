# @zksecurityXYZ

Compiled 11 Nov 2026 (WAT). Full verbatim post text lives under [`posts/zksecurityXYZ/`](../posts/zksecurityXYZ/).

| Field | Value |
| --- | --- |
| X | [@zksecurityXYZ](https://x.com/zksecurityXYZ) (user id 1658514510569959427, joined 2023-05-16) |
| Name (profile) | zkSecurity |
| Followers (11 Nov 2026) | 7055 |
| Bio (verbatim) | Security audits, development, and research for ZKP, MPC, FHE, PQC, and more generally advanced cryptography. Contact us: hello@zksecurity.xyz |
| Specialty | ZK / cryptography |
| Platforms | Audit firm |
| Evidence of valid finds | ZK audits; challenges and tooling. |

## Key findings and analysis

_No single post in this capture describes a specific vulnerability in enough detail for a root-cause write-up; see the posts list and writeups below._

## All captured posts (verbatim files)

- 2026-10-25 — New  challenge ⛳️ Google ID Token Claims Extraction. — [`posts/zksecurityXYZ/2026-10-25-2114284396450893976.md`](../posts/zksecurityXYZ/2026-10-25-2114284396450893976.md) · https://x.com/zksecurityXYZ/status/2114284396450893976
- 2026-10-16 — We're proud to announce the release of zkao version 3, the most powerful zkao update we've released so far. If — [`posts/zksecurityXYZ/2026-10-16-2110927385868571017.md`](../posts/zksecurityXYZ/2026-10-16-2110927385868571017.md) · https://x.com/zksecurityXYZ/status/2110927385868571017
- 2026-10-21 — we packed the last zk podcast with zksecurity folks! mathias, giorgio, nico, and kobi talk about our lean fram — [`posts/zksecurityXYZ/2026-10-21-2112911877403758680.md`](../posts/zksecurityXYZ/2026-10-21-2112911877403758680.md) · https://x.com/zksecurityXYZ/status/2112911877403758680
- 2026-11-03 — evm.asm, our collaboration with EF on an e2e verified EVM implementation for zkVMs, now has its own autoresear — [`posts/zksecurityXYZ/2026-11-03-2117550503060185134.md`](../posts/zksecurityXYZ/2026-11-03-2117550503060185134.md) · https://x.com/zksecurityXYZ/status/2117550503060185134
- 2026-10-28 — latest zk report mentions our work on  and — [`posts/zksecurityXYZ/2026-10-28-2115470138355138982.md`](../posts/zksecurityXYZ/2026-10-28-2115470138355138982.md) · https://x.com/zksecurityXYZ/status/2115470138355138982

## Writeups saved (full text)

- None fetched in this pass.

### Solana Privacy Rings / Zolana audit (Helius) — posted 12 Nov 2026

- Post: https://x.com/zksecurityXYZ/status/2120735261399433504 — [`posts/zksecurityXYZ/2026-11-12-2120735261399433504.md`](../posts/zksecurityXYZ/2026-11-12-2120735261399433504.md)
- Full audit text: [`writeups/zksecurityXYZ/solana-privacy-rings-zolana-audit-2026-08.md`](../writeups/zksecurityXYZ/solana-privacy-rings-zolana-audit-2026-08.md)
- **High #00:** Unauthorized spending of P-256-owned UTXOs via gnark underconstrained fake-GLV (gnark issue #1767 / GHSA-7fx8-hmgc-82jp class).
- **High #01:** Public `private_tx_hash` leaks spent UTXO (unlinkability).

### Generalized Bulletproofs for Monero FCMP++ — Lean machine-checked proof — 12 Nov 2026

- Post: https://x.com/zksecurityXYZ/status/2120960376791847035 — verbatim: [`posts/zksecurityXYZ/2026-11-12-2120960376791847035.md`](../posts/zksecurityXYZ/2026-11-12-2120960376791847035.md)
- Writeup: [`writeups/zksecurityXYZ/monero-generalized-bulletproofs-lean-proof-2026-11.md`](../writeups/zksecurityXYZ/monero-generalized-bulletproofs-lean-proof-2026-11.md)
- **Summary:** reviewed `generalized-bulletproofs` in `monero-oxide` (4 low, 3 info, no high/med), then published an independent Lean proof of completeness/ZK/soundness for the interactive protocol.
- **Takeaway:** verification scope excludes Fiat-Shamir, the Rust impl, the concrete curves, and FCMP++ circuits — the real audit surface.

## Daily update 2026-11-16

### Collision Atlas — 123 runnable hash-collision pairs (2026-11-16)

- Post: https://x.com/zksecurityXYZ/status/2122127588986438139 — verbatim: [`posts/zksecurityXYZ/2026-11-16-2122127588986438139.md`](../posts/zksecurityXYZ/2026-11-16-2122127588986438139.md)
- **Bug class:** Cryptography reference (hash collisions; 15 full breaks incl. MD5/SHA-1, 108 reduced-round)
- **Root cause:** N/A
- **How it was found:** N/A
- **Takeaways / harness:** Full dataset in [writeups/zksecurityXYZ/collision-atlas-2026-11-16.md](../writeups/zksecurityXYZ/collision-atlas-2026-11-16.md); use MD5/SHA-1 pairs as test vectors against dedupe/integrity/allowlist logic.



### Update 2026-11-21

- **38-step SHA-256 collision verifier** — https://x.com/zksecurityXYZ/status/2123882976547377591 — [`posts/zksecurityXYZ/2026-11-20-2123882976547377591.md`](../posts/zksecurityXYZ/2026-11-20-2123882976547377591.md), [`writeups/zksecurityXYZ/sha256-collisions-verifier.md`](../writeups/zksecurityXYZ/sha256-collisions-verifier.md); zk.golf / better.codes as model benchmarks — /2123984029829501049.

## 2026-11-26 run additions

- [Partnership on inference proofs with @lucidcomputing](../posts/zksecurityXYZ/2026-11-25-2125629516282274272.md) (quotes @AbdelStark's "InferenceProofs" video announcement; no bug content).
