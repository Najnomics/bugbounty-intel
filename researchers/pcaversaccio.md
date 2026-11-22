# @pcaversaccio

Index of captured posts and analysis (already-watched handle; index file created 17 Nov 2026). Verbatim posts: [`posts/pcaversaccio/`](../posts/pcaversaccio/).

## Daily update 2026-11-17

### EIP-8037 / EIP-8038: consensus compatibility ≠ application compatibility (gas invariants) (2026-11-16)

- Post: https://x.com/pcaversaccio/status/2122277228855836959 — verbatim: [`posts/pcaversaccio/2026-11-16-2122277228855836959.md`](../posts/pcaversaccio/2026-11-16-2122277228855836959.md)
- **Bug class:** Ethereum protocol change risk to immutable contracts (gas repricing, refunds, gasleft(), nested calls/reverts)
- **Root cause:** Glamsterdam gas-invariant review listed eight application assumptions affected; they were not first-class spec invariants and were reviewed late.
- **How it was found:** GitHub comment on ethereum/pm#2299 (saved: [writeups/pcaversaccio/ethereum-pm-2299-eip-8037-8038-discussion.md](../writeups/pcaversaccio/ethereum-pm-2299-eip-8037-8038-discussion.md)).
- **Takeaways / harness:** Flag contracts relying on gas stipends, `gasleft()` thresholds or refunds; fork-test under proposed schedules.

### 2026-11-21 — Zama FHE walkaway / CROPS critique
- **Signal:** Vendor-dependent FHE privacy fails walkaway when license grants no patent rights and commercial use needs vendor permission.
- **Takeaways:** Audit FHE/TEE privacy stacks for independent reimplementability, patent/license walkaway, maintainer succession, attestation independent of vendor keys.
- **Local:** [posts/pcaversaccio/2026-11-21-2124077434697846817.md](../posts/pcaversaccio/2026-11-21-2124077434697846817.md)
