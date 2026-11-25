# Demystifying Ethereum Layer 1 and Layer 2

- **Source URL:** https://medium.com/codecrafts/demystifying-ethereum-layer-1-and-layer-2-zk-rollups-optimistic-rollups-and-more-d73d22ffb4be?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20231028042452/https://medium.com/codecrafts/demystifying-ethereum-layer-1-and-layer-2-zk-rollups-optimistic-rollups-and-more-d73d22ffb4be?source=rss------bug_bounty-5
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/4123 (id 4123)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Demystifying Ethereum Layer 1 and Layer 2: ZK Rollups, Optimistic Rollups, and More

--

The Ethereum network often faces issues like slow transactions and high gas prices due to congestion. This ongoing problem requires a more efficient solution that can increase transaction speed without compromising security. This is where Layer 2 solutions come into play.

Imagine Ethereum as a busy highway with limited lanes, causing traffic jams (congestion) and slower movement of vehicles (transactions). Rollups are like adding additional, faster lanes to this highway, making it easier for more cars (transactions) to move quickly without the road becoming clogged.

Rollups achieve this by bundling multiple transactions together off the main Ethereum highway, processing them efficiently, and then periodically settling these bundled transactions back onto the main Ethereum network. This significantly speeds up transaction processing while maintaining the security of the Ethereum blockchain.

In simple word, we can say that rollups are a Layer 2 solution that helps alleviate Ethereum’s congestion by batching and processing transactions off the main network and later settling them in a way that balances speed and security.

**Layer 1 (L1):**

Example: The Ethereum network or Bitcoin.

Layer 1, or L1, is like the foundation of a building. It represents the primary blockchain, such as Ethereum or Bitcoin. L1 blockchains have a critical role in setting the core rules and ensuring the security of the entire network. Think of it as the groundwork for everything.

To put it in simpler terms, L1 is like the base layer of a cake. It’s the cake itself, determining its size, shape, and basic flavor.

**Solidity Smart Contract on Layer 1 (L1):**

```
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;
contract MyL1SmartContract {
    uint public data;
    constructor(uint initialValue) {
        data = initialValue;
    }
    function updateData(uint newValue) public {
        data = newValue;
    }
}
```
In this L1 contract, we have a simple storage contract where you can set and retrieve a value.

**Layer 2 (L2):**
