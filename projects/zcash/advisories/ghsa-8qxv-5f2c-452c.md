# GHSA-8qxv-5f2c-452c: Unbounded retention of unverifiable blocks in the checkpoint and orphan queues

| Field | Value |
| --- | --- |
| Repo | ZcashFoundation/zebra |
| GHSA | GHSA-8qxv-5f2c-452c |
| CVE | none assigned |
| Severity | high (CVSS 7.5) |
| CWE | CWE-770 |
| Published | 2026-11-17T09:54:32Z |
| Updated | 2026-11-17T09:54:32Z |
| Affected | zebrad < 7.1.0 (patched: 7.1.0); zebra-state < 17.0.0 (patched: 17.0.0); zebra-consensus < 19.0.0 (patched: 19.0.0) |
| Advisory URL | https://github.com/ZcashFoundation/zebra/security/advisories/GHSA-8qxv-5f2c-452c |

## Description (verbatim)

## Am I affected

All zebrad nodes 7.0.0 and earlier are affected. A synced node is affected through the orphan queue; a node still below the final checkpoint of its checkpoint list (a new node or a resync) is also affected through the checkpoint queue.

## Summary

Two queues held blocks that could never be verified, with no total bound, no age limit and no eviction, and kept them after the caller stopped waiting.

The state's orphan queue kept any semantically verified block whose parent was unknown until the finalized tip passed its height, about 1,000 blocks later. A gossiped block within the inbound height window only had to pass the context-free checks (minimum-difficulty proof of work, Equihash solution, Merkle root), so a peer could park blocks with nonexistent parents; the inbound verify timeout freed the peer's download slot without releasing the state's copy, and the timeout was not scored. A block built from very many tiny outputs retained tens of times its wire size, because two output maps were kept per block.

The checkpoint verifier's queue kept every accepted block above its current progress, four per height across the whole range, until the contiguous chain reached that height, which for far-ahead junk never happened. It was reachable from any sync peer and from `submitblock`.

In both cases the effect is availability only: memory growth proportional to what a peer serves, up to and including the node being killed by the operating system, repeatable after restart.

## Details

Orphan queue: `QueuedBlocks::queue` (`zebra-state/src/service/queued_blocks.rs:88-118`, v7.0.0) inserted without a limit and copied every output into `known_utxos`; entries left only through `dequeue_children`, `prune_by_height` (176-229) or write-task exit. The semantic verifier asked the state only `KnownBlock` for the block's own hash (`zebra-consensus/src/block.rs:349`) before committing (540). The inbound downloader accepted heights up to `tip + full_verify_concurrency_limit` without checking the parent (`zebrad/src/components/inbound/downloads.rs:425-505`), wrapped the verifier in the 8-minute `BLOCK_VERIFY_TIMEOUT` (`inbound.rs:290-293`) and left that timeout unscored.

Checkpoint queue: `CheckpointVerifier::queue_block` (`zebra-consensus/src/checkpoint.rs:684-743`) admitted any block passing `check_block` (639-671) up to `MAX_QUEUED_BLOCKS_PER_HEIGHT` per height (135); entries left only in `process_height` (782-785) or `Drop` (1015-1028); `reset_progress` (414-420) did not clear them, and each spawned commit task held a second copy. The sync downloader bounded how far ahead a block could be (`sync/downloads.rs:486`), not how many were retained; `submitblock` applied no tip-relative check.

## Patches

Fixed in zebrad 7.1.0 (zebra-state 17.0.0, zebra-consensus 19.0.0). The queue of blocks waiting for their parent blocks is limited to 1,000 blocks and 320 MiB of estimated memory; when it is full, Zebra fails childless blocks whose callers stopped waiting first, then the highest queued blocks, with `CommitBlockError::OrphanQueueFull`. Blocks queued for checkpoint verification are limited to about 4 GB of estimated block memory, and the blocks kept alive by queued, committing, cancelled, or failed requests are limited to four per checkpoint gap or 2,000 blocks, whichever is greater. When that queue is full, the verifier keeps the blocks linked to the next checkpoint and returns `VerifyCheckpointError::QueuedLimit`, which doesn't score the peer. The syncer requests a block dropped from a full queue again without cancelling other downloads. Upgrade to 7.1.0.

## Workarounds

Restrict peers to known-good nodes where possible, and sync new nodes from a trusted cached state. Watch the `checkpoint_queued_slots` metric during initial sync and resident memory on synced nodes; sustained growth with a stable tip is the signature of this condition.

## Credit

Identified by the V12 audit on PR #11658 and the earlier Mythos audit (issue #10748), fixed by @upbqdn. Independently reported by @Maakai123, who demonstrated that the orphan queue is exploitable from gossip with measurements; by @DanielDerefaka, who demonstrated the checkpoint queue from peer-to-peer sync on default configuration; and by @SphereDonout for the `submitblock` path.

## References

- Issue #10748: https://github.com/ZcashFoundation/zebra/issues/10748
- PR #11658: https://github.com/ZcashFoundation/zebra/pull/11658
- Earlier fix on the `next` branch: https://github.com/ZcashFoundation/zebra/commit/9185b974bb798291dad82eaf5a50f227f1407828
- CWE-770: https://cwe.mitre.org/data/definitions/770.html


