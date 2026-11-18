# GHSA-vw2c-5w35-x5q6: One already known hash anywhere past the first unknown hash in a FindBlocks answer aborts the whole obtain_tips round, so a single peer can halt chain sync indefinitely at zero cost and without attribution

| Field | Value |
| --- | --- |
| Repo | ZcashFoundation/zebra |
| GHSA | GHSA-vw2c-5w35-x5q6 |
| CVE | none assigned |
| Severity | high (CVSS 7.5) |
| CWE | CWE-400 |
| Published | 2026-11-17T09:52:05Z |
| Updated | 2026-11-17T09:52:05Z |
| Affected | zebrad < 7.1.0 (patched: 7.1.0) |
| Advisory URL | https://github.com/ZcashFoundation/zebra/security/advisories/GHSA-vw2c-5w35-x5q6 |

## Description (verbatim)

## Am I affected?

You are affected if all of the following hold:

- You run zebrad 7.0.0 or earlier, including the official Docker images.
- Your node connects to untrusted P2P peers (the default on Mainnet and Testnet).

No configuration option enables or disables the issue, so default configurations are affected. The effect is strongest on a node that is catching up to the network tip, because it depends on the syncer to download blocks. Upgrade to 7.1.0.

## Summary

A single P2P peer can stop a Zebra node from syncing new blocks for as long as it stays connected, while honest peers remain connected and keep serving the real chain. The peer only has to answer the syncer's block discovery requests with a list that contains one block hash the node already has, after one it does not have. Every sync round that receives such an answer is aborted, its in-flight downloads are cancelled, and the syncer waits before trying again. The syncer does not know which peer sent the answer, so the peer is never scored or disconnected, and the attack costs it nothing. The same abort can also happen without an attacker, when the node finishes verifying a block during discovery.

## Details

Line references are pinned to [v7.0.0](https://github.com/ZcashFoundation/zebra/tree/v7.0.0).

At the start of each sync round, `obtain_tips` sends `FindBlocks` requests to three peers (`FANOUT`) and merges their answers into one download set. For each answer, it skips only the leading run of hashes that the state already knows, and keeps everything from the first unknown hash onward, whether the later hashes are known or not ([`zebrad/src/components/sync.rs:853-867`](https://github.com/ZcashFoundation/zebra/blob/v7.0.0/zebrad/src/components/sync.rs#L853-L867)).

After merging, `obtain_tips` checks every hash in the download set again and returns an error for the whole round if any of them is known ([`sync.rs:917-923`](https://github.com/ZcashFoundation/zebra/blob/v7.0.0/zebrad/src/components/sync.rs#L917-L923)):

```rust
if self.state_contains(*hash).await? {
    return Err(eyre!("queued download of hash behind our chain tip"));
}
```

`state_contains` treats a block as known if it is in the finalized state, in any non-finalized chain, or already sent to the block write task. Only blocks waiting in the state queue count as unknown ([`sync.rs:1448-1463`](https://github.com/ZcashFoundation/zebra/blob/v7.0.0/zebrad/src/components/sync.rs#L1448-L1463), [`zebra-state/src/service.rs:1012-1016`](https://github.com/ZcashFoundation/zebra/blob/v7.0.0/zebra-state/src/service.rs#L1012-L1016)). So one known hash placed after an unknown hash in any answer fails the round.

The error leaves `try_to_sync` ([`sync.rs:639-647`](https://github.com/ZcashFoundation/zebra/blob/v7.0.0/zebrad/src/components/sync.rs#L639-L647)). The sync loop then calls `downloads.cancel_all()`, which drops every in-flight download and verify task ([`zebrad/src/components/sync/downloads.rs:667-690`](https://github.com/ZcashFoundation/zebra/blob/v7.0.0/zebrad/src/components/sync/downloads.rs#L667-L690)), and sleeps for `SYNC_RESTART_DELAY`, 67 seconds on Mainnet and Testnet ([`sync.rs:232-237`](https://github.com/ZcashFoundation/zebra/blob/v7.0.0/zebrad/src/components/sync.rs#L232-L237), [`594-612`](https://github.com/ZcashFoundation/zebra/blob/v7.0.0/zebrad/src/components/sync.rs#L594-L612)).

The syncer receives `FindBlocks` answers as a plain list of hashes, with no record of the peer that sent them, so it cannot score or disconnect that peer.

The same check can fail without an attacker. Downloads from the previous round keep running during discovery, so a block can move into the write task between the first scan and the final check. That block then counts as known and aborts the round.

## Impact

A node that keeps receiving these answers makes no sync progress. Each aborted round discards the work already in flight, up to the full download and verify pipeline, and waits 67 seconds before the next round. RPC and peer connections keep working.

The malicious peer has to be one of the three peers chosen for a round. A node with few peers is halted on most or all rounds. On a node with many peers, the attacker can raise its chance of being chosen by holding more connections.

The reporter confirmed the halt on a Regtest node with one honest and one malicious peer: the height stayed fixed while the malicious answers included the known hash, and the node caught up as soon as they stopped. Block gossip from honest peers was not part of that test.

There is no crash, no consensus divergence, no state corruption, and no effect on funds. The node resumes syncing when the peer disconnects or stops sending these answers.

## Patches

Fixed in zebrad 7.1.0. A known hash in a block discovery answer no longer fails the round. The syncer now removes known hashes from the download set one by one and downloads the rest. Blocks that are only queued in the state are still downloaded, so their missing parents can be fetched. A prospective tip from an answer is kept only when both of its hashes are still unknown, so filtering cannot join hashes that were not adjacent. The final recheck that aborted the round is removed. Regression tests are in `zebrad/src/components/sync/tests/known_hashes/`.

Upgrade to 7.1.0.

## Workarounds

None at the configuration level. Restarting zebrad does not help, because the peer can reconnect and resume. A stall shows in the logs as repeated `temporary error obtaining tips: queued download of hash behind our chain tip` messages, each followed by `waiting to restart sync` with a `state_tip` that does not advance.

## Credit

Reported by @AnticsDecoded, with a Regtest proof of concept and a matched control that isolated the known hash as the cause. Independently reported by @SphereDonout and by Filipe Casal at Trail of Bits. The reply shape was first described by Zebra's automated pull-request audit (@v12security).

### Timeline  

2026-08-05: Zebra's automated pull-request audit describes the reply shape in a public comment on PR #11187.
2026-10-24: @AnticsDecoded reports the issue privately. @SphereDonout reports it independently minutes later.

## References

- CWE-400: Uncontrolled Resource Consumption.
- Zebra 7.1.0 release notes: https://github.com/ZcashFoundation/zebra/releases/tag/v7.1.0
- [`zebrad/src/components/sync.rs` at v7.0.0](https://github.com/ZcashFoundation/zebra/blob/v7.0.0/zebrad/src/components/sync.rs)
- [`zebrad/src/components/sync/downloads.rs` at v7.0.0](https://github.com/ZcashFoundation/zebra/blob/v7.0.0/zebrad/src/components/sync/downloads.rs)

