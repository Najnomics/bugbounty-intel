# GHSA-7jvw-68q7-xfh4: A forged block body queued in the state gets the next honest peer that serves the same block banned, while the forger goes unscored

| Field | Value |
| --- | --- |
| Repo | ZcashFoundation/zebra |
| GHSA | GHSA-7jvw-68q7-xfh4 |
| CVE | none assigned |
| Severity | medium (CVSS 5.3) |
| CWE | CWE-345 |
| Published | 2026-11-17T09:57:42Z |
| Updated | 2026-11-17T09:57:42Z |
| Affected | zebrad < 7.1.0 (patched: 7.1.0); zebra-state < 17.0.0 (patched: 17.0.0) |
| Advisory URL | https://github.com/ZcashFoundation/zebra/security/advisories/GHSA-7jvw-68q7-xfh4 |

## Description (verbatim)

## Am I affected?

You are affected if all of the following hold:

- You run zebrad 7.0.0 or earlier, including the official Docker images.
- Your node verifies blocks with full validation, which is the normal mode after the final checkpoint: while catching up to the chain tip, and whenever it falls behind.
- The node downloads blocks from untrusted peers (the default on Mainnet and Testnet).

No configuration option enables or disables the issue. Upgrade to 7.1.0.

## Summary

A malicious peer can get an honest peer banned for 24 hours, while the malicious peer itself goes unscored. The attacker serves a forged body for a block that the node is also fetching from an honest peer. The forged body keeps the genuine header, and so the genuine block hash, but carries altered authorizing data. When the forged body reaches the state's queue first, the state keeps that body but hands its eventual result to the honest peer's request. The forged body then fails the authorizing-data commitment check, and Zebra scores the honest peer 100, the ban threshold. Repeated over a catch-up, this can remove honest peers from the node's peer set.

## Details

Line references are pinned to v7.0.0.

1. **The queue keeps the older body.** When `StateService::queue_and_commit_to_non_finalized_state` receives a block whose hash is already queued, it swaps only the response channels. The older request is answered with a benign duplicate error, the newer body is dropped, and the newer request is bound to the older body (`zebra-state/src/service.rs:818-839`). The request documentation says the newer request replaces the older one (`zebra-state/src/request.rs:862-863`), but the body that is later committed is the older one.

2. **The failure reaches the wrong caller.** When the queued block's parent commits, the block write task commits the queued body and sends any error on that entry's response channel (`zebra-state/src/service/write.rs:442`), which now belongs to the newer request.

3. **The wrong peer is scored.** The block verifier converts the state error with `map_commit_error` (`zebra-consensus/src/block.rs:151-161`). An authorizing-data commitment mismatch scores 100 (`zebra-state/src/error.rs:622-634`). The syncer and the inbound block downloader each score the peer attached to their own request (`zebrad/src/components/sync.rs:1232-1244`, `zebrad/src/components/inbound.rs:348-391`). Neither can tell that the body that failed is not the body its peer served. A score of 100 reaches `MAX_PEER_MISBEHAVIOR_SCORE` (`zebra-network/src/constants.rs:415`), and the ban lasts `BAN_DURATION`, 24 hours (`constants.rs:447`). An IPv6 ban covers the peer's whole `/64` (`zebra-network/src/address_book.rs:82`).

4. **Two copies of one block can overlap.** The block verifier checks whether a hash is already known only once, when verification starts (`zebra-consensus/src/block.rs:340-357`). A block that spends an output of a block not yet committed then waits up to six minutes for that output (`UTXO_LOOKUP_TIMEOUT`, `zebra-consensus/src/transaction.rs:61`). Two copies of the same hash can therefore both pass the check, wait together, and reach the state's queue close together. A peer that serves neighboring blocks can influence that timing, and an attempt that loses the race costs it nothing.

The forged body is possible because, under ZIP 244, authorizing data is not part of a v5 transaction id, so changing it does not change the block hash. The state checks the header's commitment to that data at commit time. The checkpoint verifier's queue had the same problem and has replaced the whole queued block on a duplicate hash since PR #2697 (`zebra-consensus/src/checkpoint.rs:710-725`). The state's non-finalized queue did not.

## Impact

Each successful attempt bans one honest peer, or its whole IPv6 `/64`, for 24 hours, while the attacker keeps its connection. Repeated during catch-up, this reduces the number of honest peers available to the node and increases the share of connections the attacker controls.

The forged block itself is rejected and its hash is requested again, so the chain recovers and the node does not accept invalid data. There is no consensus divergence, no on-disk state corruption, and no effect on funds.

## Patches

Fixed in zebrad 7.1.0 (zebra-state 17.0.0). When the state receives a block it has already queued under the same hash, it now replaces the queued body together with its response channel. Each caller gets the result of its own body: the older request receives a duplicate error, and the newer request is validated against the body it sent. A forged body can no longer cause the peer that served the genuine block to be scored. Regression tests: `queued_replacement_commits_its_own_body` and `queued_forged_replacement_fails_and_scores_only_forger` in `zebra-state/src/service/tests.rs`.

The fix does not stop a forged body that arrives after the genuine one from replacing it in the queue. In that case only the forger is scored, and the honest peer is not penalized. The block is committed once it is downloaded again, which can take until the next sync round, so block processing can be briefly delayed.

Upgrade to 7.1.0.

## Workarounds

None. No configuration option changes how the state queues duplicate blocks or how peers are scored.

## Credit

Reported by @x15-eth.
Independently reported by @AnticsDecoded with a state-level regression test and a proposed patch.

## References

- CWE-345: Insufficient Verification of Data Authenticity: https://cwe.mitre.org/data/definitions/345.html
- ZIP 244: Transaction Identifier Non-Malleability: https://zips.z.cash/zip-0244
- Zebra 7.1.0 release notes: https://github.com/ZcashFoundation/zebra/releases/tag/v7.1.0
- GHSA-3c94-hf7p-g5mf: the commit-time authorizing-data check and peer scoring that this issue misattributes.
- PR #2697, the same fix in the checkpoint verifier: https://github.com/ZcashFoundation/zebra/pull/2697
- `zebra-state/src/service.rs` at v7.0.0: https://github.com/ZcashFoundation/zebra/blob/v7.0.0/zebra-state/src/service.rs

