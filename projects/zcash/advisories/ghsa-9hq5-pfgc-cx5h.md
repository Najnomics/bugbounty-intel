# GHSA-9hq5-pfgc-cx5h: Forged checkpoint block body stalls initial sync until restart

| Field | Value |
| --- | --- |
| Repo | ZcashFoundation/zebra |
| GHSA | GHSA-9hq5-pfgc-cx5h |
| CVE | none assigned |
| Severity | high (CVSS 7.5) |
| CWE | n/a |
| Published | 2026-10-22T12:04:22Z |
| Updated | 2026-10-22T12:04:23Z |
| Affected | zebrad < 7.0.0 (patched: 7.0.0) |
| Advisory URL | https://github.com/ZcashFoundation/zebra/security/advisories/GHSA-9hq5-pfgc-cx5h |

## Description (verbatim)

# Forged checkpoint block body stalls initial sync until restart

| Field | Content |
|---|---|
| Severity | High |
| CVSS 3.1 | `CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:H` (7.5) |
| CWE | CWE-459: Incomplete Cleanup |
| Affected versions | zebrad < 7.0.0 |
| Patched versions | zebrad 7.0.0 |
| Reporter credit | @saxenism (original report), @x15-eth, @manus-pi, @ouicate, @Nathanbyarugaba (independent re-discoveries) |
| GHSA | GHSA-9hq5-pfgc-cx5h |
| Fix | Shipped in zebrad 7.0.0 |

## Am I affected

You are affected if all of the following hold:

- You run zebrad 6.4.2 or earlier (back to the lower bound above), or 7.0.0-rc.0.
- `checkpoint_sync = true`, which is the default.
- The node is syncing from scratch or resyncing and is within about 3,000 blocks below the final compiled checkpoint. Nodes already past the final checkpoint are not exposed.

zebrad 7.0.0 is not affected. Nodes that have finished initial sync on an affected version are not exposed until they resync.

## Summary

An unauthenticated peer can stop a syncing Zebra node from making progress for the rest of that process's lifetime by serving one checkpoint block body with forged authorizing data. Since NU5 (ZIP 244), a block hash does not commit to the authorizing data of its transactions, so a forged body carries the expected block hash. Near the final checkpoint, Zebra records the hash as present before the deferred authorizing-data check runs in the finalized state; when that check rejects the body, the record is not cleared. The node then treats the block, and the blocks above it, as already downloaded and stops asking for them. A restart restores progress. No invalid state is persisted, no chain is forked, and no funds are affected.

## Details

References are to zebrad 6.4.2 unless noted.

The checkpoint verifier selects a queued body for a height by block hash alone (`zebra-consensus/src/checkpoint.rs`, `process_height`), and deliberately defers the authorizing-data check to the state, so a forged body with the expected hash is accepted into the checkpoint range. Near the final checkpoint, the state service records each checkpoint-verified block's hash and outputs in its sent-hash set before sending the block to the finalized writer (`zebra-state/src/service.rs`, `queue_and_commit_to_finalized_state`, via `SentHashes::add_finalized`). The finalized writer then runs the chain-history authorizing-data commitment check (`finalized_state.rs`, `commit_finalized`) and rejects the forged body.

On that rejection the writer sent only a reset to the durable tip (`zebra-state/src/service/write.rs`, the `commit_finalized` error arm) and silently dropped the blocks behind the failure. Nothing removed the rejected hash, or the dropped descendants, from the sent-hash set: the cleanup that exists for the non-finalized writer (added for GHSA-4m69-67m6-prqp and GHSA-x93j-mj2f-q338) has no finalized counterpart, and the reset handler only rewound the last-sent hash. `Request::KnownBlock` then answered `WriteChannel` (present) for every recorded hash, and the syncer and inbound downloader took that answer as "already have it" and never requested the blocks again.

The delivery needs no race: an admitted peer only has to be chosen to serve any one body in the roughly 3,000-block recording window below the final checkpoint. With the GHSA-3c94-hf7p-g5mf fix (6.4.0) the serving peer is scored and the syncer asks again, but the state still answers present, so the stall is unchanged on 6.4.x.

## Impact

A successful delivery halts ordinary P2P synchronization for the affected process. Honest peers hold every missing block, but the node's own state reports them as present. Software built on the node sees a stale chain until the process is restarted.

Limits: availability only; no invalid block reaches disk, no fork, no funds impact. One syncing node per delivery. The stale markers are in memory, so a restart rebuilds from the valid durable prefix and recovers. Already-synced nodes are not exposed.

## Patches

Fixed in zebrad 7.0.0. The finalized reset now carries the durable tip height; on a reset the state clears its sent-hash set, fails every block still queued above the tip so the syncer downloads them again, and rejects blocks that arrive before the next valid height. Both the `KnownBlock` and `AwaitUtxo` paths apply pending resets before answering. The companion fix for GHSA-2w9f-9wx8-f5c8, shipped in the same release, keeps the checkpoint verifier's own reset from being lost, so recovery does not depend on the timing of a sync restart.

There is no patched 6.4.x release [confirm]; upgrade to 7.0.0.

## Workarounds

Restart the node when sync stops advancing during initial sync near the final checkpoint; the stale state is in memory only. Upgrade to 7.0.0 to remove the exposure.

## Credit

Originally reported by @saxenism, who also supplied the production-stack reproducer and the single-body follow-up that established the delivery needs no race. Independently reported by @x15-eth, @manus-pi, @ouicate and Nathan Byarugaba. Thank you all.

## References

- ZIP 244: Transaction Identifier Non-Malleability: https://zips.z.cash/zip-0244
- CWE-459: https://cwe.mitre.org/data/definitions/459.html
- GHSA-4m69-67m6-prqp and GHSA-x93j-mj2f-q338 (the non-finalized sent-hash cleanup this advisory's finalized path lacked)
- GHSA-3c94-hf7p-g5mf (peer scoring and re-request for forged checkpoint bodies, zebrad 6.4.0)
- GHSA-2w9f-9wx8-f5c8 (companion verifier-reset fix, zebrad 7.0.0)
- Issue #2654, PR #6335, PR #6387 (design history of clearing queued finalized hashes on reset)

