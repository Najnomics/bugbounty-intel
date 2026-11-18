# GHSA-hvw5-x88g-2q8w: Checkpoint verifier admits and queues blocks by a coinbase height a peer can rewrite without changing the block hash

| Field | Value |
| --- | --- |
| Repo | ZcashFoundation/zebra |
| GHSA | GHSA-hvw5-x88g-2q8w |
| CVE | none assigned |
| Severity | medium (CVSS 5.9) |
| CWE | CWE-345 |
| Published | 2026-11-17T10:05:54Z |
| Updated | 2026-11-17T10:05:55Z |
| Affected | zebrad < 7.1.0 (patched: 7.1.0); zebra-consensus < 19.0.0 (patched: 19.0.0) |
| Advisory URL | https://github.com/ZcashFoundation/zebra/security/advisories/GHSA-hvw5-x88g-2q8w |

## Description (verbatim)

## Am I affected?

You are affected if all of the following hold:

- You run zebrad 7.0.0 or earlier, including 7.1.0-alpha.0 and the official Docker images.
- Your node is checkpoint syncing at NU5 heights or later, below the final checkpoint: a new node, a node re-syncing from scratch, or a node restarting from a cached state in that range. Nodes past the final checkpoint are not affected.
- Your node downloads blocks from untrusted peers (the default on Mainnet and Testnet).

Checkpoint verification of required checkpoints cannot be turned off, so default configurations are affected. Upgrade to 7.1.0.

## Summary

A peer serving blocks to a syncing Zebra node can delay or block checkpoint sync at a height it chooses. It rewrites the height in a NU5 or later coinbase while keeping the block's real header, proof of work, and Merkle root. Zebra's checkpoint verifier queues the body at the rewritten height. Four different real blocks relabeled to one needed height fill that height's queue, so the genuine block is rejected with `QueuedLimit`, and checkpoint progress cannot pass that height until the forged entries clear. The forged bodies never reach chain state, so this is an availability issue during sync, not a consensus split.

## Details

Line references are pinned to v7.0.0.

**The height comes from data the block hash does not cover.** The block hash commits only to the header ([`zebra-chain/src/block/hash.rs:88-95`](https://github.com/ZcashFoundation/zebra/blob/v7.0.0/zebra-chain/src/block/hash.rs#L88-L95)). Under ZIP 244, a v5 coinbase `scriptSig`, which holds the block height, is authorizing data outside the transaction ID. A body with a rewritten height therefore keeps its transaction IDs, Merkle root, and header hash. The coinbase expiry height is part of the transaction ID, and from NU5 onward consensus requires it to equal the block height. That rule is checked only in full semantic verification ([`zebra-consensus/src/transaction/check.rs:506`](https://github.com/ZcashFoundation/zebra/blob/v7.0.0/zebra-consensus/src/transaction/check.rs#L506)).

**Routing and admission trust the claimed height.** The downloader reads `block.coinbase_height()` for its height bounds ([`zebrad/src/components/sync/downloads.rs:474`](https://github.com/ZcashFoundation/zebra/blob/v7.0.0/zebrad/src/components/sync/downloads.rs#L474)), and the router sends any block whose claimed height is at or below the final checkpoint to the checkpoint verifier ([`zebra-consensus/src/router.rs:221-236`](https://github.com/ZcashFoundation/zebra/blob/v7.0.0/zebra-consensus/src/router.rs#L221-L236)). `CheckpointVerifier::check_block` checks the height range, proof of work, and Merkle root, but never compares the claimed height with the coinbase expiry height ([`zebra-consensus/src/checkpoint.rs:639-671`](https://github.com/ZcashFoundation/zebra/blob/v7.0.0/zebra-consensus/src/checkpoint.rs#L639-L671)).

**The queue is keyed by the claimed height.** `queue_block` stores the block under its claimed height ([`checkpoint.rs:684-743`](https://github.com/ZcashFoundation/zebra/blob/v7.0.0/zebra-consensus/src/checkpoint.rs#L684-L743)). A block with the same hash at that height replaces the queued one. A block with a different hash is appended until `MAX_QUEUED_BLOCKS_PER_HEIGHT` (four, [`checkpoint.rs:135`](https://github.com/ZcashFoundation/zebra/blob/v7.0.0/zebra-consensus/src/checkpoint.rs#L135)) is reached, and any further block returns `QueuedLimit`. Four different real NU5 or later blocks relabeled to one height therefore fill it, and the genuine block for that height is rejected. Because duplicate detection is scoped to one height, the same real block can also be queued again at each height it is relabeled to, which increases the bodies the verifier retains.

**How long the effect lasts.** Entries at a height are removed only when checkpoint processing reaches that height through a continuous chain ([`checkpoint.rs:777-831`](https://github.com/ZcashFoundation/zebra/blob/v7.0.0/zebra-consensus/src/checkpoint.rs#L777-L831)), which the forged entries at a needed height can prevent. `reset_progress` does not clear the queue ([`checkpoint.rs:414-420`](https://github.com/ZcashFoundation/zebra/blob/v7.0.0/zebra-consensus/src/checkpoint.rs#L414-L420)). The lockout ends if the genuine block is queued before the forged ones, if the range completes another way, or if the verifier is rebuilt, for example when zebrad restarts.

## Impact

If one peer serves four relabeled bodies for a needed height before an honest peer serves the genuine block, checkpoint sync cannot pass that height until the forged entries clear. The attacker must be asked for four distinct blocks in the download window and must win the race with honest peers. It needs no proof of work or keys, since the headers are real. How reliably and how often one peer can win that race on a default configuration has not been measured, so the result may be a recoverable delay rather than a lasting stall.

There is no crash, no consensus-invalid commit, no on-disk state corruption, and no effect on funds. The relabeled bodies fail the coinbase expiry rule and the authorizing-data commitment before they reach chain state.

## Patches

Fixed in zebrad 7.1.0 (zebra-consensus 19.0.0):

- The checkpoint and semantic verifiers check that the header commits to the coinbase height before they use it. A v5 or later coinbase whose expiry height differs from its claimed height is rejected as not matching its header, before it takes a queue slot.
- The syncer bans a peer that serves such a body and requests the block again from another peer.

The aggregate queue bound and required-block eviction from GHSA-8qxv-5f2c-452c, in the same release, also limit the retained bodies and let the required block into a full height.

Upgrade to 7.1.0.

## Workarounds

None at the configuration level. On an affected version, restarting zebrad rebuilds the checkpoint verifier and clears its queue, but the node can be locked out again. The `checkpoint.queued_slots` metric shows how many heights the verifier is holding.

## Credit

The V12 audit identified the root cause as finding F-181 on 2026-10-30.

Reported by @SphereDonout, who described the queue lockout, supplied an in-process reproduction using Zebra's own NU5 Mainnet block fixtures, and proposed binding the height to the coinbase expiry height. 

### Timeline

2026-10-30: V12 finding F-181 posted on public pull requests #12129, #12131 and #12135: checkpoint admission trusts the malleable NU5 coinbase height for routing and queue indexing.
2026-11-03: GHSA-8cpx-9j95-c99j opened by SphereDonout: four relabeled headers lock the genuine block out of a checkpoint queue height; expiry-binding fix proposed; in-process reproducer.
2026-11-03: Zebra triage verifies the code path and reachability on v7.0.0.
2026-11-06: Cross-check against V12 findings; this canonical advisory opened as GHSA-hvw5-x88g-2q8w for the shared root cause; GHSA-8cpx-9j95-c99j closed into it.

## References

- [Zcash Protocol Specification](https://zips.z.cash/protocol/protocol.pdf): from NU5, a coinbase transaction's `nExpiryHeight` must equal the block height.
- [ZIP 244: Transaction Identifier Non-Malleability](https://zips.z.cash/zip-0244)
- [CWE-345: Insufficient Verification of Data Authenticity](https://cwe.mitre.org/data/definitions/345.html)
- [Zebra 7.1.0 release notes](https://github.com/ZcashFoundation/zebra/releases/tag/v7.1.0)
- GHSA-g9rc-89v4-hhvf: the sync stall from the same untrusted coinbase height, fixed in the same release.
- GHSA-8qxv-5f2c-452c: unbounded retention in the checkpoint and orphan queues, fixed in the same release.
- [`zebra-consensus/src/checkpoint.rs` at v7.0.0](https://github.com/ZcashFoundation/zebra/blob/v7.0.0/zebra-consensus/src/checkpoint.rs)

