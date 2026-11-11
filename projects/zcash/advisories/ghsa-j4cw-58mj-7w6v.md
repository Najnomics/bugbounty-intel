# GHSA-j4cw-58mj-7w6v: Uncached ZIP-244 transparent sighash digests let one invalid transaction occupy the verification thread pool for minutes

| Field | Value |
| --- | --- |
| Repo | ZcashFoundation/zebra |
| GHSA | GHSA-j4cw-58mj-7w6v |
| CVE | none assigned |
| Severity | high (CVSS 7.5) |
| CWE | CWE-407 |
| Published | 2026-10-22T13:38:43Z |
| Updated | 2026-10-22T16:01:18Z |
| Affected | zebrad < 7.0.0 (patched: 7.0.0) |
| Advisory URL | https://github.com/ZcashFoundation/zebra/security/advisories/GHSA-j4cw-58mj-7w6v |

## Description (verbatim)

| Field | Value |
|---|---|
| Severity | High |
| CVSS 3.1 | `CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:H` (7.5) |
| CWE | CWE-407 (Inefficient Algorithmic Complexity), CWE-400 (Uncontrolled Resource Consumption) |
| Affected versions | < 7.0.0 |
| Patched version | zebrad 7.0.0 , via `zcash_primitives` 0.31.0 |
| Reporter | @asafmod ; @x15-eth and @janneh2000 (independent rediscoveries) |
| Advisory URL | https://github.com/ZcashFoundation/zebra/security/advisories/GHSA-j4cw-58mj-7w6v |

## Am I affected?

You are affected if all of the following hold:

- You run any zebrad release before 7.0.0 with the default configuration.
- Your node accepts inbound peer connections or relays transactions from peers (the default), or exposes `sendrawtransaction` to untrusted callers.
- Your node is synced close to the tip, so the mempool is enabled.

Nodes that are still syncing and have not enabled the mempool are not exposed to the transaction relay path. Upgrade to zebrad 7.0.0 or later.

## Summary

A single transaction of at most 2 MB, built from ordinary pay-to-public-key outputs and spent with signatures that are well formed but do not verify, makes a Zebra node perform on the order of N squared hashing work, where N is the number of inputs (about 39,000 at the size limit). The work runs on the global Rayon thread pool and is not cancelled when the transaction is rejected, so it keeps running after the rejection is returned. While it drains, every other job on that pool, including the script and proof checks that block verification needs, waits behind it. The reporter measured roughly 1,700 CPU-seconds for one such transaction, which is about 7 minutes of stalled verification on a 4-core node and 14 minutes on a 2-core node. The transaction is never mined, so the attacker's funds are not spent and the same outputs can be reused, and the rejection carries no peer misbehavior score, so the sender is not disconnected or banned.

## Details

Zebra computes v5 transparent signature hashes through `zcash_primitives::transaction::sighash::signature_hash`, called from `sighash_inner` in `zebra-chain/src/primitives/zcash_primitives.rs` (lines 523 to 530 at v6.4.2). The library's `transparent_sig_digest` (`zcash_primitives` 0.30.0, `src/transaction/sighash_v5.rs` lines 58 to 80) recomputes two of the ZIP-244 S.2 digests on every call: the amounts digest (S.2c, personalization `ZTxTrAmountsHash`) over every spent amount, and the scripts digest (S.2d, personalization `ZTxTrScriptsHash`) over every spent scriptPubKey. Both are independent of the input index for every non-ANYONECANPAY hash type, but unlike the prevouts, sequence and outputs digests they are not stored in `TxDigests`, so they are rebuilt from scratch each time. Zebra's `TransparentAuth::input_amounts` and `input_scriptpubkeys` (`zcash_primitives.rs` lines 36 to 57) supply them by allocating and filling a fresh vector of all N values on each call. Each sighash is therefore O(N), and a transaction with N inputs needs N sighashes, giving O(N squared) total work.

The mempool verifier dispatches one script verification job per input onto the global Rayon pool (`zebra-consensus/src/transaction.rs` lines 1239 to 1248; `zebra-consensus/src/script.rs` line 61; `zebra-consensus/src/primitives.rs` lines 38 to 50). Each job evaluates the input's script through the `zcash_script` C++ interpreter, which calls back into Zebra's sighasher before checking the ECDSA signature (`zebra-script/src/lib.rs` lines 182 to 262). A scriptSig holding a minimal DER-encoded signature passes the standardness checks (push-only, within the size limit, standard spent-script kind; `zebra-consensus/src/transaction/check.rs` lines 827 to 864) and the encoding checks inside the interpreter, so the full sighash is computed before the signature fails.

Two things keep the work running after rejection. The verifier returns on the first failed input and drops the remaining futures (`transaction.rs` lines 1523 to 1532), but a dropped future does not remove a job already handed to Rayon, which has no cancellation; the closure runs to completion and sends its result into a closed channel. The mempool's per-transaction timeout (`zebrad/src/components/mempool/downloads.rs` line 499, 73 seconds, shared with the crawler interval at `crawler.rs` line 84) has the same limitation and additionally releases the sender's per-peer queue slot (`downloads.rs` lines 267 to 283), so one peer can keep adding work faster than any realistic core count drains it.

A script failure reaches `TransactionError::from(BoxError)` (`zebra-consensus/src/error.rs` lines 344 to 381) as a boxed `zebra_script::Error`, for which there is no downcast arm, so it is recorded as `InternalDowncastError` with a misbehavior score of 0 instead of the 100 points assigned to `TransactionError::Script`.

The v4 (ZIP-243) path has the same shape: `v4_signature_hash` recomputes the prevouts, sequence and outputs hashes on every call (`sighash_v4.rs` lines 151 to 182), so a v4 transaction with many inputs triggers the same quadratic cost.

## Impact

Any peer, or any caller that can reach `sendrawtransaction`, can make a node spend minutes of CPU per transaction on hashing that produces nothing. Because the work lands on the shared Rayon pool, block verification (transparent script checks and the shielded signature and proof batch verifiers all use the same pool) stops until the queued jobs drain. A mining node cannot verify new blocks during that time and its templates go stale. Peer message handling and RPC are served by the Tokio runtime and continue, more slowly, so the node does not lose its connections or crash.

The attacker's cost is bounded by the fee headroom the transaction must carry for ZIP-317 (on the order of 1 to 3 ZEC held in roughly 39,000 small outputs), and that headroom is never spent because the transaction is never mined; the same outputs can back an unlimited number of distinct invalid transactions, each with a fresh authorizing-data digest that bypasses the rejection cache. No private key is needed. A consensus-valid variant also exists: a properly signed 2 MB transaction with roughly 17,400 pay-to-public-key inputs costs every node about 190 CPU-seconds to verify when it arrives in a block, which the chain must accept.

The reporter's single-core measurements overstate one effect: pinning the whole process to one core while the Rayon pool keeps its core-count thread budget also starves the Tokio runtime, which is why RPC appeared frozen in the proof of concept. On an unpinned node the stall is confined to Rayon-backed verification. Re-verification on chain tip changes only re-queues pending transactions on a chain reset (reorg), not on ordinary growth, and a transaction that has already been rejected is not re-queued, so the "self-amplifying" variant the reporter describes needs a reorg to trigger.

## Patches

Fixed in zebrad 7.0.0. `zcash_primitives` 0.31.0 introduces `PrecomputedSighashData`, which computes the ZIP-244 amounts and scripts digests (and the ZIP-243 prevouts, sequence and outputs digests for v4 transactions) once per transaction and reuses them for every input, so each signature hash is constant-time in the number of inputs after a single linear precompute. Zebra 7.0.0 builds this structure once in `PrecomputedTxData` and reads every input's signature hash from it. Signature hash values are unchanged; the ZIP-243 and ZIP-244 test vectors for every hash type, including SINGLE, NONE and the ANYONECANPAY variants, pass unmodified.

Zebra 7.0.0 also scores peers that relay transactions whose transparent scripts fail (GHSA-jq45-ghw5-v37x), so the sender of such a transaction is now banned. Cancelling per-input verification jobs that are already queued when a transaction is rejected is not in 7.0.0 and is tracked as #11888; after this fix the residual cost of a rejected transaction is in line with verifying an honest one of the same size.

## Workarounds

Upgrade to zebrad 7.0.0 or later. On older releases there is no configuration that removes the exposure. Operators can reduce it by limiting inbound peers (`network.max_connections_per_ip` is already 1 by default; lowering `network.peerset_initial_target_size` reduces the number of peers that can relay) and by not exposing the RPC port to untrusted callers. Neither prevents a peer that is already connected from relaying one such transaction.

## Credit

Reported by @asafmod with a working Regtest proof of concept and scaling measurements. Independently reported by @x15-eth who also measured the v4 path and the effect on block verification and memory, and by @janneh2000 who added the consensus-valid block variant. The fix in `zcash_primitives` was developed with the librustzcash maintainers.

## References

- ZIP-244, section S.2 (transparent sig digest): https://zips.z.cash/zip-0244#s-2-transparent-sig-digest
- ZIP-243 (v4 signature hash): https://zips.z.cash/zip-0243
- ZIP-317 (conventional fee, mempool relay rules): https://zips.z.cash/zip-0317
- CWE-407: https://cwe.mitre.org/data/definitions/407.html
- CWE-400: https://cwe.mitre.org/data/definitions/400.html
- https://github.com/ZcashFoundation/zebra/blob/v6.4.2/zebra-chain/src/primitives/zcash_primitives.rs#L36-L57
- https://github.com/ZcashFoundation/zebra/blob/v6.4.2/zebra-chain/src/primitives/zcash_primitives.rs#L523-L530
- https://github.com/ZcashFoundation/zebra/blob/v6.4.2/zebra-consensus/src/primitives.rs#L38-L50
- https://github.com/ZcashFoundation/zebra/blob/v6.4.2/zebra-consensus/src/transaction.rs#L1239-L1248
- https://github.com/ZcashFoundation/zebra/blob/v6.4.2/zebra-consensus/src/error.rs#L344-L381
- https://github.com/ZcashFoundation/zebra/blob/v6.4.2/zebrad/src/components/mempool/downloads.rs#L499
- `zcash_primitives` 0.30.0 `src/transaction/sighash_v5.rs` lines 58 to 80 (the per-call recomputation); 0.31.0 `src/transaction/sighash.rs` (`PrecomputedSighashData`) and `sighash_v5.rs` (`TransparentInputsDigests`)
- GHSA-jq45-ghw5-v37x (companion advisory: unscored transparent script failures)

