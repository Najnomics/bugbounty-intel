# GHSA-j8gf-c4rj-6jv5: Transparent-output-dense blocks exhaust node memory through per-chain copies of the non-finalized output indexes, and the node is killed again on every restart

| Field | Value |
| --- | --- |
| Repo | ZcashFoundation/zebra |
| GHSA | GHSA-j8gf-c4rj-6jv5 |
| CVE | none assigned |
| Severity | high (CVSS 7.5) |
| CWE | CWE-770 |
| Published | 2026-11-17T08:46:39Z |
| Updated | 2026-11-17T08:46:39Z |
| Affected | zebrad < 7.1.0 (patched: 7.1.0); zebra-state < 17.0.0 (patched: 17.0.0) |
| Advisory URL | https://github.com/ZcashFoundation/zebra/security/advisories/GHSA-j8gf-c4rj-6jv5 |

## Description (verbatim)

## Am I affected?

You are affected if you run zebrad 7.0.0 or earlier, including the official Docker images, or use zebra-state 16.0.0 or earlier.

Every network is affected. Test networks are affected more, because Zebra tracks up to 100 non-finalized chain forks there, compared with 10 on Mainnet. Default configurations are affected, and no configuration option prevents the memory growth.

The restart loop described below needs the non-finalized state backup, which is on by default (`should_backup_non_finalized_state = true`).

## Summary

Blocks filled with many small transparent outputs can make a Zebra node run out of memory and be killed by the operating system. The node is then killed again on every restart, until an operator removes its non-finalized state backup. The blocks are consensus-valid and cheap to produce: a miner can fill its own coinbase with outputs at no fee cost. The cause is that each non-finalized chain fork keeps a full copy of the index of transparent outputs created in the non-finalized window, and Zebra copies that index again when it finalizes a block. Memory use grows with the number of forks times the number of transparent outputs in the window.

## Details

Line references are pinned to v7.0.0.

`ChainInner::created_utxos` is a plain `HashMap<OutPoint, OrderedUtxo>` ([`zebra-state/src/service/non_finalized_state/chain.rs:106`](https://github.com/ZcashFoundation/zebra/blob/v7.0.0/zebra-state/src/service/non_finalized_state/chain.rs#L106)). It holds every transparent output created in the chain's non-finalized blocks. Two paths copy it in full:

- `Chain::fork` starts from `self.clone()` ([`chain.rs:444-449`](https://github.com/ZcashFoundation/zebra/blob/v7.0.0/zebra-state/src/service/non_finalized_state/chain.rs#L444-L449)), so every new fork gets its own copy of the index for all blocks below the fork point.
- `NonFinalizedState::finalize` calls `Arc::make_mut` on the best chain and on every side chain that shares the finalized root ([`zebra-state/src/service/non_finalized_state.rs:325-372`](https://github.com/ZcashFoundation/zebra/blob/v7.0.0/zebra-state/src/service/non_finalized_state.rs#L325-L372)). The block write task publishes a clone of the non-finalized state to readers ([`zebra-state/src/service/write.rs:110`](https://github.com/ZcashFoundation/zebra/blob/v7.0.0/zebra-state/src/service/write.rs#L110)), so the chains are shared and each `make_mut` copies the whole chain before `pop_root` removes one block.

Zebra keeps up to `MAX_NON_FINALIZED_CHAIN_FORKS` (10) chains on Mainnet and `MAX_NON_FINALIZED_CHAIN_FORKS_TEST_NETWORKS` (100) on test networks ([`zebra-state/src/constants.rs:107-113`](https://github.com/ZcashFoundation/zebra/blob/v7.0.0/zebra-state/src/constants.rs#L107-L113)). The memory bound in the comment on the Mainnet constant counts serialized block bytes. The per-output index is several times larger than the serialized outputs, and it is not shared between chains.

The blocks that trigger this are ordinary:

- A P2SH output serializes to 32 bytes, so a 2 MB block holds about 60,000 of them.
- P2SH output scripts count no legacy signature operations, so the block sigop limit does not restrict them.
- A miner can add the outputs to its own coinbase. Through the mempool, ZIP-317 charges `MARGINAL_FEE`, 1,000 zatoshis, per output.

On restart, `restore_backup` recommits every block in the backup directory, including side-chain blocks ([`zebra-state/src/service/non_finalized_state/backup.rs:34-70`](https://github.com/ZcashFoundation/zebra/blob/v7.0.0/zebra-state/src/service/non_finalized_state/backup.rs#L34-L70)). The node rebuilds the same chains and runs out of memory again.

## Impact

A remote attacker who can get on the order of a million transparent outputs into blocks within the 1,000-block non-finalized window can crash Zebra nodes. In the reporter's reproduction on Regtest, a node limited to 8 GiB of memory was killed after about 20 output-filled blocks (about 1.2 million outputs) with 5 chains, and was killed again within seconds of restarting on the same state. Nodes with more memory need more outputs or more forks.

The cost is zero for a miner. Through the mempool, it is about 1,000 zatoshis per output, roughly 12.6 ZEC in fees for 1.26 million outputs (an estimate, not tested on Mainnet).

The node does not recover by restarting. It keeps crashing until the operator removes the non-finalized state backup, after which it syncs the affected range again on a single chain.

The reporter observed this on the public Testnet on 2026-11-09 and 2026-11-10, where blocks 4,602,598 to 4,602,673 contain about one million transparent outputs. Their zebrad nodes, with 12 GiB and 16 GiB memory limits, were killed in a loop.

Consensus rules, funds, and the finalized state are not affected.

## Patches

Fixed in zebrad 7.1.0 and zebra-state 17.0.0.

- Chain forks share each block's created outputs and transparent address changes, and their transaction, spend, and nullifier indexes, instead of copying them. Forks, read snapshots, and finalization no longer copy the output index of the whole non-finalized window.
- Every network now limits the total number of index entries in all non-finalized chains: 6,200,000 on Mainnet (`MAX_NON_FINALIZED_INDEX_ENTRIES`) and 2,000,000 on test networks (`MAX_NON_FINALIZED_INDEX_ENTRIES_TEST_NETWORKS`). Ordinary Mainnet blocks do not reach the limit.
- Past the limit, Zebra drops the lowest-work forks. If the chains are still too large, it finalizes the best chain's oldest blocks early, but keeps at least 100 blocks (`MIN_NON_FINALIZED_BLOCKS_OVER_INDEX_LIMIT`).

While the limit is active, Zebra can't follow a chain reorganization deeper than the blocks it kept. The worst-case non-finalized state is about 5 to 7 GB, so 16 GB of RAM is recommended, as in Zebra's system requirements.

Upgrade to 7.1.0.

## Workarounds

There is no configuration option that bounds the memory growth. Adding memory raises the number of outputs an attacker needs, but does not bound it.

To recover a node that is crashing in a loop, stop it, then move the `non_finalized_state/<network>` directory under the state cache directory aside. Setting `should_backup_non_finalized_state = false` in the `[state]` section also stops the restart loop, but the node can still run out of memory while it follows the chain.

## Credit

Reported by Foundry Digital, with a state-level test and an end-to-end Regtest reproduction.

## References

- [CWE-770: Allocation of Resources Without Limits or Throttling](https://cwe.mitre.org/data/definitions/770.html)
- [Zebra 7.1.0 release notes](https://github.com/ZcashFoundation/zebra/releases/tag/v7.1.0)
- [ZIP 317: Proportional Transfer Fee Mechanism](https://zips.z.cash/zip-0317)
- [`zebra-state/src/service/non_finalized_state/chain.rs` at v7.0.0](https://github.com/ZcashFoundation/zebra/blob/v7.0.0/zebra-state/src/service/non_finalized_state/chain.rs)
- [`zebra-state/src/service/non_finalized_state.rs` at v7.0.0](https://github.com/ZcashFoundation/zebra/blob/v7.0.0/zebra-state/src/service/non_finalized_state.rs)
- [GHSA-hj54-2mfv-4xg8](https://github.com/ZcashFoundation/zebra/security/advisories/GHSA-hj54-2mfv-4xg8): a related memory exhaustion through address balance queries over the non-finalized state, fixed in the same release.
