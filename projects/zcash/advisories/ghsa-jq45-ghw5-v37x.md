# GHSA-jq45-ghw5-v37x: Transparent script verification failures are never scored, on the mempool, block-sync and block-gossip paths

| Field | Value |
| --- | --- |
| Repo | ZcashFoundation/zebra |
| GHSA | GHSA-jq45-ghw5-v37x |
| CVE | none assigned |
| Severity | high (CVSS 7.5) |
| CWE | n/a |
| Published | 2026-10-22T13:13:05Z |
| Updated | 2026-10-22T16:10:44Z |
| Affected | zebrad >= 2.3.0, < 7.0.0 (patched: 7.0.0); zebra-consensus >= 1.0.0-beta.46, < 18.0.0 (patched: 18.0.0) |
| Advisory URL | https://github.com/ZcashFoundation/zebra/security/advisories/GHSA-jq45-ghw5-v37x |

## Description (verbatim)

# Transparent script verification failures are never scored, on the mempool, block-sync and block-gossip paths

| Field | Content |
|---|---|
| Severity | High (7.5) |
| CVSS 3.1 | `CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:H` (7.5) |
| CWE | CWE-755 (Improper Handling of Exceptional Conditions); CWE-400 (Uncontrolled Resource Consumption) |
| Affected versions | zebrad >= 2.3.0, < 7.0.0 (includes 7.0.0-rc.0) |
| Patched versions | zebrad 7.0.0 (scoring on all paths); the block-sync round restart is not yet changed, see Patches |
| Reporter | @x15-eth; @ouicate (independent rediscovery and further analysis) |
| Fix | Zebra 7.0.0 |
| Related | GHSA-j4cw-58mj-7w6v |

## Am I affected

You are affected if you run zebrad 2.3.0 or later before 7.0.0, including 7.0.0-rc.0. The mempool consequence needs the mempool enabled (the default once the node is near the chain tip). The block-sync consequence applies to a node downloading blocks above the last mandatory checkpoint (initial sync in that range, or catching up after downtime); the block-gossip consequence applies at the tip. No configuration change exposes or protects you; any inbound or outbound peer can trigger it after the handshake. Upgrade to 7.0.0.

## Summary

Zebra does not penalize a peer that relays a transaction, or serves a block, whose transparent script fails verification. The failure is scored 100 in the misbehavior table, which would ban the peer, but the error never reaches that table: it arrives boxed from the script verifier, the conversion to `TransactionError` has no arm for it, and it collapses to `InternalDowncastError`, which scores 0. Zebra only reports non-zero scores.

On the mempool path, a peer can keep relaying transactions that fail script verification for as long as it likes. Each one is rejected, but only after the node has done the full signature-hash and script work for it (see GHSA-j4cw-58mj-7w6v), so the missing penalty turns a bounded cost into a sustained one.

The same missing penalty applies when a peer serves a block body. After NU5 a flipped byte in a non-coinbase transparent `scriptSig` leaves the block hash and Merkle root unchanged, so the forged body is accepted as the answer to a download request and rejected only at script verification. On the block-sync path that rejection is treated as a genuinely invalid block: the syncer cancels every in-flight download, drops the still-valid hash and idles for 67 seconds, and the serving peer is not scored. The handling added for GHSA-3c94-hf7p-g5mf does not apply, because it is keyed to the state's authorizing-data commitment check, which runs after transaction verification.

## Details

Verified on zebrad 6.4.2 (e3eef2f) and 7.0.0-rc.0 (6d1e414d6); the fix verified on 7.0.0 (e8db87e).

**The missing arm.**

- The script verifier runs `CachedFfiTransaction::is_valid` on the Rayon pool and returns its `zebra_script::Error` as a `BoxError` (`zebra-consensus/src/script.rs:61`; `zebra-consensus/src/primitives.rs:23-35`).
- The transaction verifier awaits those checks and converts the first failure with `From<BoxError> for TransactionError` (`zebra-consensus/src/transaction.rs:557` at 6.4.2). Before 7.0.0 that conversion downcasts the ed25519, RedJubjub, RedPallas, `ValidateContextError` and `TransactionError` types and falls through to `InternalDowncastError` for anything else (`zebra-consensus/src/error.rs:344-381` at 6.4.2; 356-393 at 7.0.0-rc.0). There is no `zebra_script::Error` arm.
- `mempool_misbehavior_score` lists `Script(_)` in the 100-point arm (`error.rs:412` at 6.4.2; 424 at 7.0.0-rc.0), but that variant is only produced by the direct `From<libzcash_script::Error>` conversion (`error.rs:319-323`), which verification never uses: the only live constructor is the sigops mapping, which runs after `async_checks.check().await?` has already failed. `InternalDowncastError` takes the wildcard `0` (`error.rs:436`; 448).
- Two tests pin the behaviour before the fix, for a v4 and a v5 transaction (`zebra-consensus/src/transaction/tests.rs:2092` and `:2701` at 6.4.2).

The arm has been missing since mempool misbehavior scoring was introduced in zebrad 2.3.0 (PR #9201): the `Script(_)` arm was unreachable from the day it was added, and the same tests asserted `InternalDowncastError` then. The shielded verification errors were given downcast arms in 6.2.1 for GHSA-2p4c-3q4q-p463; transparent script errors were not.

**Mempool path.**

- The mempool sends a misbehavior report only when the score is non-zero (`zebrad/src/components/mempool.rs:741-742` at 6.4.2), so the peer is never reported.
- The rejection cache is keyed by the exact `UnminedTxId` and cleared on every new tip (`zebrad/src/components/mempool/storage.rs:190`, `855-878`; `mempool.rs:782`), so changing one output amount produces a new transaction the node verifies in full again.

**Block paths.**

- The download layer accepts a body by header hash alone (`zebra-network/src/peer/connection.rs:308`), and `merkle_root_validity` compares the header root against txids only (`zebra-consensus/src/block/check.rs:427-433`). The ZIP-244 txid excludes `scriptSig`, so a flipped `scriptSig` byte in a v5 transaction changes neither.
- The semantic verifier awaits every transaction (`zebra-consensus/src/block.rs:324-350`) before the state commit (`:415-419`); the authorizing-data commitment is checked only in the state (`zebra-state/src/service/check.rs:203-214`). The forged input fails script verification first, so the error is `VerifyBlockError::Transaction(InternalDowncastError(..))`, scored through `err.mempool_misbehavior_score()` (`block.rs:138`), never the `Commit` error the GHSA-3c94 fix keyed on (`is_auth_commitment_mismatch`, `block.rs:112-116`).
- Block sync: the scoring arm requires a non-zero score (`zebrad/src/components/sync.rs:1223`), so the peer is not reported; `reobtain_hash` re-queues only `NotFound`, the height-limit variant, UTXO races, verify timeouts and the two commitment cases (`:1282-1303`), so the still-valid hash is dropped; `should_restart_sync` returns `true` by default for an invalid block (`:1440-1500`); `sync()` then calls `cancel_all()` and sleeps `SYNC_RESTART_DELAY = 67 s` (`:229`, `:597-606`).
- Block gossip: the inbound downloader scores through `VerifyBlockError::misbehavior_score()` (`zebrad/src/components/inbound.rs:355-358`) and only sends non-zero scores, so a gossiped forged body is unscored and costs one block verification, bounded by the in-flight limit. No restart on this path.
- A v4 `scriptSig` edit changes the txid and fails `BadMerkleRoot` (scored 100), so the block construction needs a v5 transaction. Below the last mandatory checkpoint the checkpoint verifier runs no script verification.

## Impact

**Mempool.** A peer can relay an unlimited number of transactions with invalid transparent scripts without being scored, rate-limited beyond the per-peer download cap, or banned. Each costs the node its full transparent script verification before rejection. Before 7.0.0 that cost was quadratic in the input count (GHSA-j4cw-58mj-7w6v): a single 2 MB transaction with about 23,500 P2PKH inputs cost about 85 CPU-seconds, and a peer could keep five queued at all times from one IP address. Block verification shares the same thread pool, so blocks were verified late while the attack lasted; honest mempool transactions waited behind the same work and were dropped if they waited longer than the 73-second verification timeout. The attacker needs existing transparent outputs to spend (about 1.2 ZEC in fees to create 23,500 of them once; they are never consumed) and ordinary peer connections.

**Block sync.** A node syncing above the checkpoint range can be held back by one connected peer. Each time that peer is selected to serve a block the node still needs, the round is cancelled, the hash is dropped and the syncer idles 67 seconds; the next round re-discovers the hash and the peer can do it again, never scored, never banned. No funds, keys, proofs or mining are needed.

**Block gossip.** A forged body at the tip costs one block verification per attempt and is never scored.

All three effects stop when the attack stops. None crashes the node, corrupts state, or changes what the node accepts into the chain.

## Patches

Fixed in Zebra 7.0.0. `From<BoxError> for TransactionError` now downcasts `zebra_script::Error` first and returns `TransactionError::Script`, so a transparent script failure carries its 100-point score on the mempool, block-sync and block-gossip paths, and the serving or relaying peer is banned (`zebra-consensus/src/error.rs:356-370` at 7.0.0; the two tests now assert `TransactionError::Script`). Zebra 7.0.0 also makes each invalid transaction cheap to reject (GHSA-j4cw-58mj-7w6v), so what remains per banned address is one rejected transaction, or up to five already queued, at linear cost.

One consequence is bounded rather than removed in 7.0.0. On block sync, a forged body that fails script verification now bans the serving peer, but the syncer still treats it as a genuinely invalid block: it cancels the round, drops the hash and idles 67 seconds, once per banned address (bans last 24 hours as of 7.0.0). Scoring the peer and re-requesting the hash without a restart, as GHSA-3c94-hf7p-g5mf already does for the authorizing-data commitment case, is tracked as #11889 for a later release. Cancelling the checks that are still queued when a transaction is rejected is tracked separately under GHSA-j4cw-58mj-7w6v.

## Workarounds

Upgrade to 7.0.0. On earlier versions there is no configuration that removes the issue. A node already synced past the checkpoint range is exposed only to the gossip variant and the mempool flood. Operators can reduce exposure by keeping the default `network.max_connections_per_ip = 1`, bounding outbound connections with `network.peerset_initial_target_size`, and watching the `mempool.full_queue.per_peer.total` metric and script-verification latency.

## Credit

Reported by @x15-eth, who also measured the combined effect with GHSA-j4cw-58mj-7w6v (reported by @asafmod). Independently reported by @ouicate, who showed the block-sync and block-gossip consequences and the same-hash `scriptSig` construction.

## References

- GHSA-j4cw-58mj-7w6v (companion advisory)
- GHSA-3c94-hf7p-g5mf (the sync-round restart handling this fix must extend)
- GHSA-2p4c-3q4q-p463 (the shielded-error downcast arms this fix mirrors)
- CWE-755, CWE-400
- Fix at 7.0.0: https://github.com/ZcashFoundation/zebra/blob/e8db87eb69254e0d4eedd058eadd48bdfa09065a/zebra-consensus/src/error.rs#L356-L370
- `zebra-consensus/src/error.rs` at 6.4.2: https://github.com/ZcashFoundation/zebra/blob/e3eef2f37c35127ad1769f19a1ebc7eaa5d5d291/zebra-consensus/src/error.rs#L344-L381
- `zebra-consensus/src/script.rs` at 6.4.2: https://github.com/ZcashFoundation/zebra/blob/e3eef2f37c35127ad1769f19a1ebc7eaa5d5d291/zebra-consensus/src/script.rs#L61
- `zebra-consensus/src/block.rs` at 6.4.2: https://github.com/ZcashFoundation/zebra/blob/e3eef2f37c35127ad1769f19a1ebc7eaa5d5d291/zebra-consensus/src/block.rs#L133-L141
- `zebrad/src/components/mempool.rs` at 6.4.2: https://github.com/ZcashFoundation/zebra/blob/e3eef2f37c35127ad1769f19a1ebc7eaa5d5d291/zebrad/src/components/mempool.rs#L741-L742
- `zebrad/src/components/sync.rs` at 6.4.2: https://github.com/ZcashFoundation/zebra/blob/e3eef2f37c35127ad1769f19a1ebc7eaa5d5d291/zebrad/src/components/sync.rs#L1219-L1303 and https://github.com/ZcashFoundation/zebra/blob/e3eef2f37c35127ad1769f19a1ebc7eaa5d5d291/zebrad/src/components/sync.rs#L1440-L1500
- `zebrad/src/components/inbound.rs` at 6.4.2: https://github.com/ZcashFoundation/zebra/blob/e3eef2f37c35127ad1769f19a1ebc7eaa5d5d291/zebrad/src/components/inbound.rs#L355-L358
- `zebra-network/src/peer/connection.rs` at 6.4.2: https://github.com/ZcashFoundation/zebra/blob/e3eef2f37c35127ad1769f19a1ebc7eaa5d5d291/zebra-network/src/peer/connection.rs#L308

