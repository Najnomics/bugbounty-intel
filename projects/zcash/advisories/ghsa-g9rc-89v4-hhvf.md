# GHSA-g9rc-89v4-hhvf: A single peer can stop initial sync indefinitely by serving blocks with a rewritten coinbase height, without being banned

| Field | Value |
| --- | --- |
| Repo | ZcashFoundation/zebra |
| GHSA | GHSA-g9rc-89v4-hhvf |
| CVE | none assigned |
| Severity | high (CVSS 7.5) |
| CWE | CWE-345 |
| Published | 2026-11-17T09:05:30Z |
| Updated | 2026-11-17T09:05:30Z |
| Affected | zebrad < 7.1.0 (patched: 7.1.0); zebra-consensus < 19.0.0 (patched: 19.0.0); zebra-network < 16.0.0 (patched: 16.0.0) |
| Advisory URL | https://github.com/ZcashFoundation/zebra/security/advisories/GHSA-g9rc-89v4-hhvf |

## Description (verbatim)

## Am I affected?

You are affected if all of the following hold:

- You run zebrad 7.0.0 or earlier, including 7.1.0-alpha.0 and the official Docker images.
- Your node is doing initial sync below the final checkpoint, or within 1,000 blocks above it: a new node, a node re-syncing from scratch, or a node restarting from a cached state in that range. On Mainnet at v7.0.0 the final checkpoint is at height 3,522,460.
- Your node connects to untrusted peers (the default on Mainnet and Testnet).

Default configurations are affected. Upgrade to 7.1.0.

## Summary

A single peer can stop a syncing Zebra node at its current tip for as long as the peer stays connected, without ever being scored or banned. The peer answers Zebra's request for the next block with the block's real header and a coinbase whose height has been rewritten to a height Zebra has already verified. The block hash still matches, and no proof of work is needed. Zebra treats the body as a harmless duplicate, drops the block it still needs, and does not ask for it again. By advertising the block with an `inv`, the peer also makes itself the peer Zebra asks for that block in every later sync round.

## Details

Line references are pinned to v7.0.0.

1. **The forged body keeps the block hash.** The block hash commits only to the header ([`zebra-chain/src/block/hash.rs:88-95`](https://github.com/ZcashFoundation/zebra/blob/v7.0.0/zebra-chain/src/block/hash.rs#L88-L95)). For v5 transactions, the coinbase `scriptSig` that holds the height is authorizing data outside the ZIP 244 transaction ID, so the Merkle root also still matches. For earlier versions the Merkle root no longer matches, but `check_block` calls `check_height` before it checks the Merkle root ([`zebra-consensus/src/checkpoint.rs:639-671`](https://github.com/ZcashFoundation/zebra/blob/v7.0.0/zebra-consensus/src/checkpoint.rs#L639-L671)), so the height is used first in both cases.

2. **Claimed heights near the tip go straight to the verifier.** The downloader checks a claimed height against the block's parent, and scores the peer, only when the height is more than 1,000 blocks below the tip ([`zebrad/src/components/sync/downloads.rs:468-590`](https://github.com/ZcashFoundation/zebra/blob/v7.0.0/zebrad/src/components/sync/downloads.rs#L468-L590)). Other heights reach the router, which picks the checkpoint verifier by the claimed height ([`zebra-consensus/src/router.rs:221-236`](https://github.com/ZcashFoundation/zebra/blob/v7.0.0/zebra-consensus/src/router.rs#L221-L236)).

3. **The verifier reports a benign duplicate.** A claimed height at or below the last verified checkpoint returns `AlreadyVerified` ([`checkpoint.rs:556-583`](https://github.com/ZcashFoundation/zebra/blob/v7.0.0/zebra-consensus/src/checkpoint.rs#L556-L583)). `is_duplicate_request` is `true` for that error, and its misbehavior score is 0 ([`checkpoint.rs:1113-1186`](https://github.com/ZcashFoundation/zebra/blob/v7.0.0/zebra-consensus/src/checkpoint.rs#L1113-L1186)). Once the verifier has passed the final checkpoint, every block it receives gets `Finished` ([`checkpoint.rs:1228-1230`](https://github.com/ZcashFoundation/zebra/blob/v7.0.0/zebra-consensus/src/checkpoint.rs#L1228-L1230)), which also scores 0.

4. **The syncer drops the block.** `handle_block_response` sends a score only when it is non-zero, and its re-request list does not include these errors ([`zebrad/src/components/sync.rs:1216-1336`](https://github.com/ZcashFoundation/zebra/blob/v7.0.0/zebrad/src/components/sync.rs#L1216-L1336)). `should_restart_sync` continues after a duplicate, and restarts on `Finished` through its catch-all ([`sync.rs:1472-1570`](https://github.com/ZcashFoundation/zebra/blob/v7.0.0/zebrad/src/components/sync.rs#L1472-L1570)). Without the block, its checkpoint range cannot verify. The round ends when the 8-minute block verification timeout fires, and sync restarts after 67 seconds ([`sync.rs:199`](https://github.com/ZcashFoundation/zebra/blob/v7.0.0/zebrad/src/components/sync.rs#L199), [`sync.rs:232`](https://github.com/ZcashFoundation/zebra/blob/v7.0.0/zebrad/src/components/sync.rs#L232)). The next round starts from the state tip, so the dropped block is requested first again.

5. **The same peer gets every request for the block.** Any single-block `inv` registers its sender as having that block ([`zebra-network/src/peer/handshake.rs:1281-1316`](https://github.com/ZcashFoundation/zebra/blob/v7.0.0/zebra-network/src/peer/handshake.rs#L1281-L1316)). Block downloads prefer a ready peer that advertised the block ([`zebra-network/src/peer_set/set.rs:1465-1512`](https://github.com/ZcashFoundation/zebra/blob/v7.0.0/zebra-network/src/peer_set/set.rs#L1465-L1512)). Honest peers do not gossip old blocks, so the attacker is usually the only advertiser. A forged body is a successful response, so the peer is never recorded as failing or missing the block. Registry entries expire after two 53-second rotations ([`zebra-network/src/constants.rs:154`](https://github.com/ZcashFoundation/zebra/blob/v7.0.0/zebra-network/src/constants.rs#L154)), so the peer re-sends its `inv` to keep its place.

The fix for GHSA-g95h-hw6g-pvgv covers only claimed heights far below the tip, which is why this path remained open.

## Impact

A syncing node that receives the forged body stops at its current tip and makes no further sync progress while the peer stays connected. Each round also downloads and discards the lookahead window of later blocks. The peer is never scored, so restarting zebrad does not reliably help: the peer can reconnect, or the node can connect to it again. The attacker needs one inbound or outbound connection and no proof of work, stake, or keys.

There is no crash, no consensus divergence, no on-disk state corruption, and no effect on funds. Nodes more than 1,000 blocks past the final checkpoint are not affected.

## Patches

Fixed in zebrad 7.1.0 (zebra-consensus 19.0.0, zebra-network 16.0.0):

- The checkpoint and semantic verifiers check that the header commits to the coinbase height before they use it. A v5 or later coinbase must have an expiry height equal to its claimed height, and the Merkle root check now runs before the height check. A rewritten body is rejected as not matching its header.
- The syncer scores a peer that serves such a body with a score that bans it, and requests the block again from another peer. The downloader also checks the body against the header before it drops, pauses, or resumes downloads based on the block's height.
- A misbehavior report that bans a peer reaches the address book right away, instead of at the next batch flush.
- When a block is requested again, the peers that already returned it lose their preference and are only asked as a last resort.

Upgrade to 7.1.0.

## Workarounds

None at the configuration level. An operator who identifies the peer can ban it by hand. Syncing from a trusted cached state more than 1,000 blocks past the final checkpoint avoids the exposure.

## Credit

@x15-eth, for the finding, the three proof-of-concept tests, and the analysis of the inventory routing capture.
@Maakai123, who found the same mechanism independently, for the far-ahead height variant, the analysis of the inbound gossip path, and a proof of concept on the real verification stack. 
@SphereDonout, for an independent report of the far-ahead variant with a live loopback reproduction against an unmodified 7.0.0 binary and the release history of the non-restart arms. 
@Nathanbyarugaba, for an independent report of the far-ahead variant with the missing-coinbase forgery shape and fix-design notes.

## References

- [ZIP 244: Transaction Identifier Non-Malleability](https://zips.z.cash/zip-0244)
- [CWE-345: Insufficient Verification of Data Authenticity](https://cwe.mitre.org/data/definitions/345.html)
- [Zebra 7.1.0 release notes](https://github.com/ZcashFoundation/zebra/releases/tag/v7.1.0)
- GHSA-hvw5-x88g-2q8w: the checkpoint queue lockout from the same untrusted coinbase height, fixed in the same release.
- GHSA-g95h-hw6g-pvgv: the parent-height check for claimed heights far below the tip.
- [`zebra-consensus/src/checkpoint.rs` at v7.0.0](https://github.com/ZcashFoundation/zebra/blob/v7.0.0/zebra-consensus/src/checkpoint.rs)
- [`zebrad/src/components/sync.rs` at v7.0.0](https://github.com/ZcashFoundation/zebra/blob/v7.0.0/zebrad/src/components/sync.rs)

