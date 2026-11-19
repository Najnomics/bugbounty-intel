# GHSA-4q7w-cx94-55pc: sighash computation has quadratic complexity

| Field | Value |
| --- | --- |
| Repo | zcash/librustzcash |
| GHSA | GHSA-4q7w-cx94-55pc |
| CVE | none assigned |
| Severity | low |
| CWE | CWE-1176 |
| Published | 2026-11-18T23:35:48Z |
| Updated | 2026-11-18T23:35:48Z |
| Affected | zcash_primitives <=0.30.1 (patched: 0.31.0) |
| Advisory URL | https://github.com/zcash/librustzcash/security/advisories/GHSA-4q7w-cx94-55pc |

## Description (verbatim)

### Summary

This was originally reported to Zebra by @asafmod.

In short: sighash computation takes quadratic time on the number of inputs, even if the sighash context is cached.

### Details

From Claude:

>  In zcash_primitives 0.30.0, `sighash_v5::transparent_sig_digest` rebuilds amounts_digest and scripts_digest on every call by calling `input_amounts()` and `input_scriptpubkeys()` on the `TransparentAuthorizingContext` trait. Those trait methods return a fresh `Vec` of all N values, and the whole vector is then BLAKE2b-hashed. The trait offers no way to hand over a precomputed digest, so Zebra's  `TransparentAuth` impl in `zebra-chain/src/primitives/zcash_primitives.rs` cannot fix it by caching the vectors. The hashing, not the allocation, is the cost.

### PoC

The Zebra report has a non-fully-disclosed PoC, but the impact should be straightforward to see.

### Impact

- Zero impact to wallet scanning.
  - The lightwallet protocol's `CompactTx` omits proofs and signatures, so wallets are not computing sighashes as part of scanning.
- Low impact to wallet spending.
  - Normal users won't be constructing such large transactions (due to note management).
  - A user's wallet could be dusted with tiny outputs if their recipient address is known to an adversary, but that would only affect users trying to spend their entire balance (because `zcash_client_backend` selects largest-first). It would potentially impact the `zcash_client_backend` shielding flow when run on the dusted address, but it is just a performance issue (the tx will be completed, just not in a timely fashion).
    - If this were in any way widespread than we'd have received reports from wallet providers.
- Moderate impact (DoS) to full nodes that utilise this code path in validation; low impact to network overall.
  - Original reporters claims a 39k-input transaction takes 14 min to validate with 2 cores.
    - Such a transaction would (at a ZIP 317 marginal fee of 1000) cost around US$500 in fees.
  - Zebra uses an async validation architecture, so an adversary would likely need to use more than one tx to prevent a node from validating user txs in the mempool (unconfirmed).
  - Zakura (a fork of Zebra) [fixed this in their codebase publicly three months ago](https://github.com/zakura-core/zakura/pull/281), and there have been no reported issues with mainnet in that time. If such a tx were mined, non-upgraded Zebra nodes would lag significantly behind the chain tip until done validating that block, but miners are mostly running Zakura so chain progress would be unaffected.

### Coordination

I think the easiest approach would be to develop the fix privately and get it publicly merged just before a zcash_primitives release is cut, and then we follow it right after with a Zebra release. The issue will be kinda of obvious to anyone paying attention but I don't think it warrants the effort of shipping a private fix.
