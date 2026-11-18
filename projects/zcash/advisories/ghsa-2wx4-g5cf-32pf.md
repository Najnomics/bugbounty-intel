# GHSA-2wx4-g5cf-32pf: Anchor Error Masks Halo2 Batch Poisoning and Evades Peer Scoring

| Field | Value |
| --- | --- |
| Repo | ZcashFoundation/zebra |
| GHSA | GHSA-2wx4-g5cf-32pf |
| CVE | none assigned |
| Severity | medium (CVSS 5.3) |
| CWE | CWE-400 |
| Published | 2026-11-17T11:01:15Z |
| Updated | 2026-11-17T11:01:15Z |
| Affected | zebrad < 7.1.0 (patched: 7.1.0); zebra-consensus < 19.0.0 (patched: 19.0.0) |
| Advisory URL | https://github.com/ZcashFoundation/zebra/security/advisories/GHSA-2wx4-g5cf-32pf |

## Description (verbatim)

## Am I affected?

You are affected if all of the following hold:

- You run zebrad 7.0.0 or earlier, including the official Docker images, or use zebra-consensus 18.0.0 or earlier.
- Your mempool is active, which it is once the node is close to the chain tip.
- Your node accepts transactions from untrusted peers (the default).

The reporter demonstrated the issue with a v6 transaction that carries an Ironwood bundle. At v7.0.0, v5 transactions with Orchard actions go through the same verification order, so treat any affected node with an active mempool as exposed. No configuration option changes the order.

## Summary

An unauthenticated peer can repeatedly slow down Halo2 proof verification on a Zebra node, including proof verification for blocks, without ever being penalized. The peer sends a mempool transaction with an invalid Halo2 proof and an anchor that Zebra doesn't know. Zebra queues the proof in the shared batch verifier before it checks the anchor. The anchor check fails first, so Zebra returns that error, which carries no misbehavior score. The invalid proof stays in the batch, makes the batch fail, and forces every other proof in it through slower individual verification. This bypasses the peer scoring added for GHSA-g7c4-2w6c-cr3r. It is an availability issue only.

## Details

Line references are pinned to v7.0.0.

`MempoolTxVerifier::call` builds the version-specific proof and signature checks with `dispatch_version_verification`, then appends the state query that checks the transaction's nullifiers and anchors against the best chain tip ([`zebra-consensus/src/transaction.rs:543-563`](https://github.com/ZcashFoundation/zebra/blob/v7.0.0/zebra-consensus/src/transaction.rs#L543-L563)). It then awaits all of them together.

`AsyncChecks::check` polls the checks concurrently and returns the first error. It cancels the other checks by dropping their futures ([`transaction.rs:1545-1557`](https://github.com/ZcashFoundation/zebra/blob/v7.0.0/zebra-consensus/src/transaction.rs#L1545-L1557)).

When the Halo2 check is polled, the cache wrapper `Cached::call` waits for the batch service to be ready and submits the proof to it ([`zebra-consensus/src/primitives/cache.rs:460-514`](https://github.com/ZcashFoundation/zebra/blob/v7.0.0/zebra-consensus/src/primitives/cache.rs#L460-L514)). Dropping the caller's future afterwards does not remove the item from the batch. The Halo2 verifiers are process-global batch services that flush at most every 100 ms, with a fallback to individual verification when a batch fails ([`zebra-consensus/src/primitives/halo2.rs:291-302`](https://github.com/ZcashFoundation/zebra/blob/v7.0.0/zebra-consensus/src/primitives/halo2.rs#L291-L302), [`zebra-consensus/src/primitives.rs:19`](https://github.com/ZcashFoundation/zebra/blob/v7.0.0/zebra-consensus/src/primitives.rs#L19)). Block and mempool transactions share them.

The state query usually answers before the batch flushes. If the anchor is unknown, the transaction fails with `TransactionError::ValidateContextError`. `mempool_misbehavior_score` gives that error a score of 0 ([`zebra-consensus/src/error.rs:406-456`](https://github.com/ZcashFoundation/zebra/blob/v7.0.0/zebra-consensus/src/error.rs#L406-L456)), and the mempool sends a misbehavior report only for a non-zero score ([`zebrad/src/components/mempool.rs:755-778`](https://github.com/ZcashFoundation/zebra/blob/v7.0.0/zebrad/src/components/mempool.rs#L755-L778)). The peer is never penalized, and the invalid proof is still verified later as part of the batch.

The zero score for unknown anchors is correct on its own: a peer with a different chain tip can honestly send a transaction whose anchor this node doesn't know yet. The defect is that the expensive proof work was queued before that cheap check.

## Impact

Each such transaction makes a shared Halo2 batch fail, so every honest proof in that batch, including proofs from blocks being verified, is checked individually on the slow path. Because the error carries no score, the peer is not disconnected or banned, and can repeat the transaction with fresh anchors and transaction data. This can slow block verification and mempool admission on the targeted node.

There is no consensus, proof soundness, funds, or persistent state impact.

## Patches

Fixed in zebrad 7.1.0 and zebra-consensus 19.0.0. `MempoolTxVerifier` now checks the transaction's nullifiers and anchors against the best chain tip, with a timeout, before it starts proof and signature verification. A transaction rejected by that check never reaches the batch verifiers, and an error without a score can no longer be returned while an invalid proof from the same transaction is still in a batch.

Upgrade to 7.1.0.

## Workarounds

None at the configuration level.

## Credit

Reported independently by @SphereDonout (the valid-proof case on Sapling, with block-delay measurements) and @Nathanbyarugaba (the invalid-proof case, the failed shared batch, and the missing peer score).The same ordering was also reported independently by @AnticsDecoded and @Itunuolu.

### Timeline

2026-10-18: @SphereDonout reports that Sapling proofs are still verified after an unknown-anchor rejection.
2026-10-20: @Nathanbyarugaba reports the invalid-proof case and the missing peer score.
2026-10-21: A fix is prepared privately.
2026-10-25 and 2026-10-30: Two further reports of the same ordering are received and closed as duplicates.
2026-11-06: The reports are consolidated under this advisory.

## References

- [CWE-400: Uncontrolled Resource Consumption](https://cwe.mitre.org/data/definitions/400.html)
- [Zebra 7.1.0 release notes](https://github.com/ZcashFoundation/zebra/releases/tag/v7.1.0)
- [`zebra-consensus/src/transaction.rs` at v7.0.0](https://github.com/ZcashFoundation/zebra/blob/v7.0.0/zebra-consensus/src/transaction.rs)
- [`zebra-consensus/src/primitives/cache.rs` at v7.0.0](https://github.com/ZcashFoundation/zebra/blob/v7.0.0/zebra-consensus/src/primitives/cache.rs)
- GHSA-g7c4-2w6c-cr3r: peer scoring for pushed-transaction verification failures, which this finding bypasses.

