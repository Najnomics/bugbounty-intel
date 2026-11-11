# GHSA-2w9f-9wx8-f5c8: A sync restart during a failed checkpoint commit loses the verifier rewind and stalls checkpoint sync until restart

| Field | Value |
| --- | --- |
| Repo | ZcashFoundation/zebra |
| GHSA | GHSA-2w9f-9wx8-f5c8 |
| CVE | none assigned |
| Severity | high (CVSS 7.5) |
| CWE | n/a |
| Published | 2026-10-22T12:14:40Z |
| Updated | 2026-10-22T15:36:11Z |
| Affected | zebrad < 7.0.0 (patched: 7.0.0) |
| Advisory URL | https://github.com/ZcashFoundation/zebra/security/advisories/GHSA-2w9f-9wx8-f5c8 |

## Description (verbatim)

# zebrad: A sync restart during a failed checkpoint commit loses the verifier rewind and stalls checkpoint sync until restart

| Field | Content |
|---|---|
| Severity | High |
| CVSS 3.1 | `CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:H` (7.5) |
| CWE | CWE-755 (Improper Handling of Exceptional Conditions); related CWE-362 |
| Affected versions | zebrad < 7.0.0 |
| Patched versions | 7.0.0 |
| Reporter credit | @SphereDonout; @x15-eth (independent rediscovery) |
| Affected packages | zebrad, zebra-consensus |

## Am I affected?

You are affected if all of the following hold:

- You run zebrad 6.4.2 or earlier, or 7.0.0-rc.0, including the official Docker images.
- Your node is syncing through checkpoint ranges at NU5 heights or later (on Mainnet, from 1,687,104 up to the final checkpoint): a new node, a node re-syncing from scratch, or a node restarting from a cached state below the final checkpoint. Nodes already past the final checkpoint are not affected.
- `checkpoint_sync` is enabled (the default) and the node downloads blocks from untrusted peers (the default on Mainnet and Testnet).

No configuration change enables or disables the issue. Default configurations are affected. Upgrade to 7.0.0; there is no 6.4.x patch release.

## Summary

A single malicious peer can stop a syncing Zebra node in any NU5 or later checkpoint range, so initial sync makes no further progress until an operator restarts the node, and the peer can repeat the attack after the restart. The peer needs no proof of work and no keys. It serves a block body that keeps a genuine block's header and hash but carries altered authorizing data, together with a second block that makes the sync round fail. The checkpoint verifier advances past the forged block, the state then rejects it, and the step that should move the verifier back to the state tip is cancelled with the failed sync round. From then on the verifier rejects the missing honest blocks as already verified.

## Details

Line references are pinned to v6.4.2 (the last affected stable release). `zebra-consensus/src/checkpoint.rs` is identical on 7.0.0-rc.0.

1. **A forged body passes checkpoint verification.** Checkpoint verification matches the block hash against the checkpoint list. Under ZIP 244, authorizing data (such as the coinbase `scriptSig`) is excluded from v5 transaction ids, so a body with altered authorizing data keeps its merkle root and block hash. The authorizing data commitment is only checked when the state commits the block (`zebra-state/src/service/finalized_state.rs:379`, `zebra-state/src/service/check.rs:137`).

2. **Progress advances before commit.** When a checkpoint range is complete, `process_checkpoint_range` signals success for each block and advances the verifier's progress (`checkpoint.rs:887`) before the state has committed the range.

3. **The rewind runs in a cancellable future.** `CheckpointVerifier::call` spawns the state commit as a task (`checkpoint.rs:1144`), which survives if its handle is dropped. The rewind to the state tip on a commit failure, `reset_sender.send(tip)` (`checkpoint.rs:1214`), is sent from the returned future that awaits that task (`checkpoint.rs:1168-1215`). That is the only send site; the verifier consumes the rewind at the start of the next `call` (`checkpoint.rs:1101-1103`).

4. **A second block cancels the round.** Any verification error that the syncer treats as restart-worthy makes `sync()` call `downloads.cancel_all()` (`zebrad/src/components/sync.rs:597-599`), which drops every in-flight verify future through the cancellation branch at `zebrad/src/components/sync/downloads.rs:622-632`. Two triggers are confirmed:
   - a child with an invalid merkle root (`BadMerkleRoot`), at the final checkpoint;
   - a block from a later range whose coinbase height is rewritten into the current range. `check_height` accepts the claimed height (`checkpoint.rs:507-529`), and when the range completes `process_height` rejects it as `UnexpectedSideChain` (`checkpoint.rs:732-751`). That error is neither a duplicate nor an authorizing-data mismatch (`checkpoint.rs:1022-1054`), so `should_restart_sync` (`sync.rs:1440-1470`) restarts the round, and it carries a misbehavior score of 0 (`checkpoint.rs:1075`).

   The syncer keeps up to 1,000 blocks in flight by default (`sync.rs:110`), which spans several 400-block checkpoint ranges, so a block from a later range is normally requested while the current range is still pending.

5. **The verifier and the state stay out of step.** The commit tasks finish: the blocks below the forged block commit, the forged block fails with `InvalidChainHistoryBlockTxAuthCommitment`, and the rest of the range is dropped. Nothing rewinds the verifier. At a non-final range, re-delivered honest blocks are rejected as `AlreadyVerified` (`checkpoint.rs:522`), which `is_duplicate_request` treats as benign (`checkpoint.rs:1024`), and the syncer drops them (`sync.rs:1443-1446`). At the final checkpoint, the genuine block is rejected as `Finished` (`checkpoint.rs:1105-1107`). Only a process restart rebuilds the verifier from the state tip.

The fix for GHSA-3c94-hf7p-g5mf in 6.4.0 re-requests a forged body and scores the serving peer when the authorizing-data error reaches the syncer. It does not help here, because the future that would carry that error has been dropped. PR #11385 (in 6.4.0) limited the rewind to commit failures, which is correct, but left it in the cancellable future.

## Impact

A syncing node that is served the two blocks stops committing blocks at the forged height and makes no further sync progress. Sync rounds keep restarting and re-downloading the missing blocks, which the verifier keeps rejecting. RPC and peer connections keep working. With the `UnexpectedSideChain` trigger the serving peer is never scored, so it can repeat the attack in a later range after each restart.

The attack works in every checkpoint range from NU5 activation to the final checkpoint, about 1.8 million blocks of Mainnet initial sync. The attacker needs to be asked for two blocks while a range is pending, which a peer serving a share of a syncing node's block requests is likely to be during a full sync.

There is no crash, no consensus divergence, no on-disk state corruption, and no effect on funds. The finalized state stays at the last valid block. Nodes already past the final checkpoint are not affected.

## Patches

Fixed in zebrad 7.0.0. The commit task now owns recovery: on a commit failure it reads the state tip and sends the reset itself, so a cancelled caller cannot discard it (`checkpoint.rs:1346-1385` at v7.0.0). Resets carry an epoch, and only the first failure in an epoch rewinds the verifier, so a late reset from the same failed range cannot undo progress the verifier has since re-earned (`checkpoint.rs:1212-1218`). The children of a failed block are queued again instead of being dropped, so the honest range re-verifies after the rewind. The syncer forgets a verified block's re-download entry so the honest block is requested again. Regression tests: `commit_failure_resets_progress_after_dropped_future` and `commit_failure_requeues_children_of_invalid_block` in `zebra-consensus/src/checkpoint/tests.rs`.

There is no 6.4.x patch release. Operators on 6.4.x should upgrade to 7.0.0.

## Workarounds

None at the configuration level. On an affected version, restarting zebrad rebuilds the verifier from the state tip and lets sync resume, but the node can be stalled again in a later range. A stall shows in the logs as `committing a block to the finalized state failed, resetting state queue` with `InvalidChainHistoryBlockTxAuthCommitment`, followed by a `current_height` that stops advancing while sync rounds repeat. Syncing from a trusted cached state already past the final checkpoint avoids the exposure.

## Credit

Reported by @SphereDonout, with an end-to-end proof of concept through the P2P interface and a negative control. Independently reported by @x15-eth, who showed that the issue affects every NU5 or later checkpoint range and identified the unscored `UnexpectedSideChain` trigger and the `AlreadyVerified` path, with crate-level tests.

## References

- ZIP 244: Transaction Identifier Non-Malleability.
- CWE-755: Improper Handling of Exceptional Conditions. CWE-362: Concurrent Execution using Shared Resource with Improper Synchronization.
- Zebra 7.0.0 release notes: https://github.com/ZcashFoundation/zebra/releases/tag/v7.0.0
- PR #11385: https://github.com/ZcashFoundation/zebra/pull/11385
- GHSA-3c94-hf7p-g5mf: the syncer re-request path that this finding bypasses.
- GHSA-9hq5-pfgc-cx5h: the related finalized sent-hash stall, fixed in the same release; its recovery depends on this fix.
- GHSA-g95h-hw6g-pvgv: scoring of rewritten coinbase heights below the tip.
- Zakura, the same defect fixed in 1.5.0: https://github.com/zakura-core/zakura/pull/939
