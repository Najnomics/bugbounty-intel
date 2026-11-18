# GHSA-m44m-9r8r-r64j: Permanent Checkpoint Sync Halt via Forged Child Block in `StateService::queue_and_commit_to_non_finalized_state`

| Field | Value |
| --- | --- |
| Repo | ZcashFoundation/zebra |
| GHSA | GHSA-m44m-9r8r-r64j |
| CVE | none assigned |
| Severity | high (CVSS 7.5) |
| CWE | CWE-20 |
| Published | 2026-11-17T09:00:16Z |
| Updated | 2026-11-17T09:00:16Z |
| Affected | zebrad < 7.1.0 (patched: 7.1.0); zebra-state < 17.0.0 (patched: 17.0.0) |
| Advisory URL | https://github.com/ZcashFoundation/zebra/security/advisories/GHSA-m44m-9r8r-r64j |

## Description (verbatim)

## Am I affected?

You are affected if all of the following hold:

- You run zebrad 7.0.0 or earlier, including the official Docker images.
- Your node is still committing checkpoint-verified blocks: a new node, a node re-syncing from scratch, or a node restarting from a cached state below the final checkpoint. On Mainnet, the final checkpoint in zebrad 7.0.0 is at height 3,522,460. With `checkpoint_sync = false`, the final checkpoint is the first one at or above the mandatory checkpoint, so the same window exists at a lower height.
- The node downloads blocks from untrusted peers (the default on Mainnet and Testnet).

Nodes whose finalized tip is already past the final checkpoint are not affected. No configuration option enables or disables the issue. Upgrade to 7.1.0.

## Summary

A single malicious peer can permanently stop a syncing Zebra node before it reaches the final checkpoint, so initial sync never completes. The peer sends one forged block that claims a height just above the final checkpoint and names the node's current finalized tip as its parent. Zebra's state service treats any queued child of the last checkpoint-verified block as the signal that checkpoint sync is finished, without checking that child's height. It closes the checkpoint commit channel, and every remaining checkpointed block is then discarded. The forged block is rejected shortly after, but the rejection scores the sender zero, and the node stays stuck. A restart clears the condition, but the peer can repeat it at no cost.

## Details

Line references are pinned to v7.0.0.

1. **The handoff checks the parent hash, not the height.** `StateService::queue_and_commit_to_non_finalized_state` switches from checkpoint commits to full validation when three conditions hold: the checkpoint commit channel is open, some queued non-finalized block has the last sent checkpoint block as its parent, and that block is the finalized tip (`zebra-state/src/service.rs:848-871`). The parent test is a hash lookup in `QueuedBlocks::has_queued_children` (`zebra-state/src/service/queued_blocks.rs:120-122`). The queued block's height is never compared with its parent's, and the code carries a `TODO: configure the state with the last checkpoint hash instead?` (`service.rs:848`).

2. **A forged block reaches that queue cheaply.** The block verifier router sends a block to the checkpoint verifier only if its coinbase height is at or below the final checkpoint; anything higher goes to the semantic verifier (`zebra-consensus/src/router.rs:218-242`). The context-free checks there can be met by an attacker. In particular, the header's difficulty only has to be within the network's proof-of-work limit, and the hash only has to meet the header's own target (`zebra-consensus/src/block/check.rs:69-130`). A block at minimum difficulty needs little work to produce. Height continuity and the difficulty adjustment are contextual checks, which run only after the block is queued.

3. **The channel closes and is never reopened.** When the forged block is queued while the checkpoint pipeline is drained, all three conditions hold, and the state drops the checkpoint commit channel (`service.rs:858`). The channel is created once at startup. From then on, `queue_and_commit_to_finalized_state` rejects every checkpoint-verified block as already finalized (`service.rs:545`, `service.rs:559-572`), and any blocks already queued for the finalized state are dropped the same way (`service.rs:866-870`). The missing checkpointed blocks are downloaded again and rejected again, from every peer, so honest peers cannot repair it.

4. **The forger is not scored.** The forged block later fails contextual validation because its height does not follow its parent's. That error has a misbehavior score of 0 (`zebra-state/src/error.rs:622-634`), so the sender keeps its connection.

The drained state the attack needs is the normal resting state of a node whose next checkpoint range has not arrived. A peer that serves part of the chain and withholds the next range can hold the node in that state.

## Impact

The node stops committing blocks below the final checkpoint and never begins full validation or reaches the chain tip. The process keeps running, RPC and peer connections keep working, and sync rounds keep restarting without progress. There is no timeout or automatic recovery. A restart rebuilds the commit channel, but the node then resumes from the same finalized tip and is exposed to the same block again.

The attacker needs no credentials and only an ordinary peer connection to a node that is still in checkpoint sync. There is no consensus divergence, no on-disk state corruption, and no effect on funds. Nodes already past the final checkpoint are not affected.

## Patches

Fixed in zebrad 7.1.0 (zebra-state 17.0.0):

- The state rejects a queued non-finalized block whose height is not one more than its finalized parent's, with the new error `ValidateContextError::NonSequentialFinalizedChild`. This check runs when the block arrives and again for blocks already queued at the moment of the handoff. The error has a misbehavior score of 100, so the peer that sent the block is banned.
- The state switches from checkpoint commits to full validation only once the block at the final checkpoint height has been written. A queued child is used as the signal only when there is no final checkpoint.

Upgrade to 7.1.0.

## Workarounds

None at the configuration level. On an affected version, a restart lets sync resume until the node is served a forged block again. Starting from a trusted cached state that is already past the final checkpoint avoids the exposure.

## Credit

Reported by @unusualbyte with a full network reproduction.
Independently reported by @ouicate with a state-level reproduction and the pre-positioned trigger variant and by @x15-eth with a reproduction through the real router and sync downloader, the affected-version lower bound, and fix-scope suggestions.

## References

- CWE-20: Improper Input Validation: https://cwe.mitre.org/data/definitions/20.html
- Zebra 7.1.0 release notes: https://github.com/ZcashFoundation/zebra/releases/tag/v7.1.0
- `zebra-state/src/service.rs` at v7.0.0: https://github.com/ZcashFoundation/zebra/blob/v7.0.0/zebra-state/src/service.rs
- `zebra-consensus/src/router.rs` at v7.0.0: https://github.com/ZcashFoundation/zebra/blob/v7.0.0/zebra-consensus/src/router.rs

