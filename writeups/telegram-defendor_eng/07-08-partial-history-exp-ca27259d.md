# ⏳ Partial History Pruning in Ethereum

- **Source URL:** https://blog.ethereum.org/2025/07/08/partial-history-exp
- **Fetched:** 2026-11-12
- **Channel:** @defendor_eng
- **Telegram message:** https://t.me/defendor_eng/252 (id 252)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
As of today, all Ethereum execution clients support partial history expiry in accordance with [EIP-4444](https://eips.ethereum.org/EIPS/eip-4444). While work on full, rolling history expiry is ongoing, users can expect to reduce the disk space required for an Ethereum node by 300-500 GB by removing the block data prior to the Merge. This will allow a node to fit comfortably on a 2 TB disk. See below for information on each specific client.

## **Chain history**

By definition a blockchain is a chain of blocks starting at a specific genesis point. For Ethereum, that occurred on [July 30, 2015](https://etherscan.io/block/0). Each block includes information about the protocol itself, i.e. the current gas limit, a list of user transactions, and the result of those transactions encapsulated by a receipt. This data has many uses:

- Full validation of the chain requires executing every historical block to ensure that, not only is the current head state correct, but all historical states from genesis to today were correct.
- Constructing indexes over the chain history, e.g. tracking the balance changes of a certain account over time or how the state of a certain application changes.
- For L2s that have posted transactions using calldata, they would need the chain history to fully validate their chain or construct indexes.
- General proof-of-past operations such as proving a certain transaction was sent at some point.
- In rare cases, non-fungible token (NFT) data. But the prevailing method of hosting NFTs on-chain is to store the NFT data either in contract storage or reference external sources, such as IPFS.

This historical data is not regularly consumed by Ethereum users and instead serves more sophisticated users and developers. Accessing a current balance, executing a trade, borrowing assets, etc. will not be interrupted by history expiry. Accounts that have been dormant since genesis are also not affected, because the state for every account continues to be maintained. However, only the current state is maintained. Therefore a user’s balance at a specific point in the past is not easily determinable from the history alone. Such queries require an [archive node](https://ethereum.org/en/developers/docs/nodes-and-clients/archive-nodes/) with specialized indexes capable of determining past state values.

## **Block validation in proof-of-stake**

When Ethereum launched with proof-of-work, full validation from genesis was the default. Later on, clients implemented snap sync and other similar styles of syncing where clients jumped to the head of the chain based on heaviest chain rule, then proceeded to download all contracts and accounts state. Full syncing was retained for those who felt that the heaviest chain rule was not enough to verify the full integrity of the chain.

With the advent of proof-of-stake and the merge, the syncing strategy changed. Because signatures can be generated at basically no cost, clients need to anchor to a recent trusted checkpoint, also known as a [weak subjectivity checkpoint](https://ethereum.org/en/developers/docs/consensus-mechanisms/pos/weak-subjectivity/). This allows new users to bootstrap to the chain without being tricked by hypothetical long range attacks from validators who have exited the validator set long ago.

The introduction of subjectivity further removes the need for users to fully verify every block in the chain, and so for many other reasons, clients adopted a new reverse sync strategy where they walk the chain backwards toward genesis to download the history. Now that most clients do not fully execute the chain, there is little reason to force every Ethereum node to download over 1 TB of data that is not used from the p2p network. With history expiry we maintain a 1-of-N trust assumption, similar to other networks, that if at least one entity provides the historical blocks, nodes will be able to retrieve the history via out-of-protocol means.

The default security model of history expiry does not change from the current status quo. Clients have not fully validated the chain from genesis for over 5 years. The execution layer will continue to provide all headers which allows cryptographic verification of the chain from genesis. This helps avoid clients from accepting invalid historical data.

## **Availability, guaranteed**

Until today, every single node on the Ethereum network stored every block from genesis to the head. This provided an extremely high guarantee that history will be available for download by anyone at any time. We believe that it is possible to reduce the number of nodes storing all history while still ensuring high availability. We achieve this with the following distribution channels:

- Institutional providers — organizations who are willing to host historical archives on their own servers.
- Torrent — opt-in permissionless and decentralized hosting for archived history.
- Peer-to-peer network — the same retrieval mechanism as before, except peers who choose to not store the history will dilute the overall availability to some degree.

For a list of mirrors and torrent files, please visit the community maintained documentation [https://eth-clients.github.io/history-endpoints/](https://eth-clients.github.io/history-endpoints/).

## **Client-specific commands**

*While this information is up-to-date as of publishing, commands and flags associated with a particular client are subject to changes. The most up-to-date information will always be each client’s respective documentation.*

Every full-node focused client supports running without pre-merge data, however the exact process is dependent on the client. Below are instructions to run a pruned node for every execution client. Please note that only Mainnet and Sepolia have a non-Merge chain prefix, so pruning is only possible on those chains. Additionally, the non-Merge chain prefix in Sepolia is small so pruning may have little effect on the total disk size required by each client.

**Go-ethereum**

Available as of version [v1.16.0](https://github.com/ethereum/go-ethereum/releases/tag/v1.16.0). Full documentation available [here](https://geth.ethereum.org/docs/fundamentals/historypruning).

For an existing node:

1. Shutdown geth gracefully.
2. Run the offline prune command geth prune-history --datadir=\</path/to/data>
3. Start geth again.

For a new node:

1. Use the flag --history.chain postmerge to skip downloading the pre-merge blocks.

**Nethermind**

Activated by default as of version [1.32.2](https://github.com/NethermindEth/nethermind/releases/tag/1.32.2)**.**

History will only be removed on a newly synced node. Automated pruning will be added in future versions. The full documentation is available [here](https://docs.nethermind.io/fundamentals/history-expiry).

In order to disable history-expiry feature:

1. Use the flags --Sync.AncientBodiesBarrier 0 --Sync.AncientReceiptsBarrier 0.

**Besu**

Available as of version [25.7.0](https://github.com/hyperledger/besu/releases/tag/25.7.0). Full documentation available [here](https://besu.hyperledger.org/public-networks/how-to/pre-merge-history-expiry).

For an existing node, either:

Offline prune

1. Shutdown Besu gracefully.
2. Run the offline prune command: besu --data-path=\</path/to/data> storage prune-pre-merge-blocks
3. Start Besu with --history-expiry-prune
4. Wait until all space has been reclaimed, approximately 24-48 hours.
5. Remove --history-expiry-prune and restart Besu.
Online prune
6. Use the flag --history-expiry-prune when starting the client.

For a new node:

1. Use the flag --sync-mode=SNAP

**Erigon**

Available as of version [v3.0.12](https://github.com/erigontech/erigon/releases/tag/v3.0.12)

For new and existing nodes:

1. Use the flag --history-expiry when starting the client

**Reth**

[Available as of version v1.5.0.](https://github.com/paradigmxyz/reth/releases/tag/v1.5.0)

For new and existing nodes:

1. Use the flag --prune.bodies.pre-merge --prune.receipts.before 15537394 flag for Mainnet and --prune.bodies.pre-merge --prune.receipts.before 1450409 for Sepolia.
