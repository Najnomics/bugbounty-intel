# 🛡️ Read-Only Reentrancy: A New Threat to Smart Contracts

- **Source URL:** https://zokyo.io/blog/read-only-reentrancy-attacks
- **Fetched from:** https://web.archive.org/web/20260129075907/https://zokyo.io/blog/read-only-reentrancy-attacks/
- **Fetched:** 2026-11-26
- **Channel:** @defendor_eng
- **Telegram message:** https://t.me/defendor_eng/389 (id 389)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
### Read-Only Reentrancy Attacks: Understanding the Threat to your Smart Contracts

Jan 23, 2025

9 Minutes

Are you familiar with the term “reentrancy attacks?” If not, it’s time to learn, as they are a common vulnerability in smart contracts.

In this post, we’ll explore a specific type of reentrancy attack called a “read-only reentrancy attack.” We’ll cover what it is, how it works, and how to prevent it.

#### What is a reentrancy attack?


When a function calls an untrusted external contract, and that contract makes a recursive call back to the original function, it can result in a reentrancy attack. Such an attack can cause funds to be drained or malicious activities to be initiated.


There are [multiple variations of this attack](https://web.archive.org/web/20260129075907/https://zokyo.io/blog/a-complete-guide-to-reentrancy-attacks/), such as:

- Single-Function Reentrancy
- Cross-Function Reentrancy
- Cross-Contract Reentrancy
- Cross-Chain Reentrancy
- Read-Only Reentrancy

This post will dive into one of the most novel forms of reentrancy attacks:

- Read-only Reentrancy.

The read-only reentrancy is a reentrancy scenario where a view function is reentered, which in most cases is unguarded as it does not modify the contract’s state. However, if the state is inconsistent, wrong values could be reported. Other protocols relying on a return value can be tricked into reading the wrong state to perform unwanted actions.

Protocols integrate with other DeFi protocols to read token prices or read prices of wrapped tokens minted on particular protocols. This is possible when any lending protocol supports the pool tokens from other protocols as collateral or allows staking. All these integrations will require reading pool token prices or wrapped token prices.

Attackers misuse these situations to perform read-only reentrancy attacks using price manipulation.

#### What is the modus operandi of this attack?


**Step 1** - An attacker contract will call a contract that can provide reentrancy. Other protocols must also be reading some values from it. So, let’s call it a reentrant contract.

**Step 2** - The reentrant contract will fall back to the attacker contract, and the fallback method logic will be executed.

**Step 3** - The attacker contract will now call a target DeFi protocol contract, as nothing prevents it from calling it.

**Step 4** - Target protocol, as assumed earlier, will be reading some value from the compromised reentrant contract.

**Step 5** - By the time Step 3 and Step 4 finish, the attacker would have already exploited the target contract and will simply proceed to let Step 1 and Step 2 finish.

#### Real-world attack examples


Several protocols have been subjected to read-only attacks, leading to the theft of millions of dollars of liquidity associated with those protocols.

##### Sentiment Platform attack:


**Attack analysis:** On the 4th of April, 2023, the Sentiment platform which was deployed on one of the most popular L2 solutions, Arbitrum, was attacked. The platform lost about a million dollars due to asset price manipulation (using read-only reentrancy).

**Protocols involved:**

- *Sentiment platform:* Sentiment aims to solve capital inefficiencies by providing a primitive-based solution to enable permissionless undercollateralized on-chain credit. Sentiment mitigates the challenge of widespread counterparty risk by implementing on-chain hypothecation. A Sentiment “Account,” the protocol’s key primitive, allows users to gain access to greater leverage than incumbent money markets while allowing the borrowed assets to be deployed across the DeFi ecosystem.
- *Balancer protocol:* Balancer is a decentralized automated market maker (AMM) protocol built on Ethereum that represents a flexible building block for programmable liquidity. At the heart of Balancer lies the Vault, a smart contract responsible for managing and holding all tokens in each Balancer pool. Additionally, the Vault serves as the primary gateway for most Balancer operations, such as swaps, joins, and exits.
- *Aave v3:* Aave Protocol is a non-custodial and decentralized liquidity protocol that allows users to participate as suppliers, borrowers, or liquidators. Users who supply liquidity to a market can earn interest on their provided crypto assets, while borrowers can overcollateralize and borrow assets. Moreover, borrowers can engage in “flash loans,” which are one-block-borrow transactions that do not require over-collateralization.

**Impact:** The Sentiment platform allows opening accounts with Balancer pools as assets. This means that the Sentiment platform uses the Balancer’s Vault contracts’ getPrice(token) method, which could be attacked using read-only reentrancy.


Attack details:

- *Attacker address:* https://arbiscan.io/address/0xdd0cdb4c3b887bc533957bc32463977e432e49c3
- *Attacker contract:* https://arbiscan.io/address/0x9f626F5941FAfe0A5b839907d77fbBD5d0deA9D0
- *Exploited contract:* https://arbiscan.io/address/0x0dDB1eA478F8eF0E22C7706D2903a41E94B1299B
- *Tx:* https://arbiscan.io/tx/0xa9ff2b587e2741575daf893864710a5cbb44bb64ccdc487a100fa20741e0f74d


The amount that was stolen: $1 million.


Attack flow:


Let us try to analyze this transaction for the attack: https://arbiscan.io/tx/0xa9ff2b587e2741575daf893864710a5cbb44bb64ccdc487a100fa20741e0f74d


The attacker utilized Aave v3 flash loan to borrow BTC, ETH, and USDC to deposit a large amount of liquidity.


The attacker first opened an account on the Sentiment platform and deposited 50 WETH, selecting the Balancer B-33WETH-33WBTC-33USDC pool as their asset of choice.


The attacker deposited the entire flash loan amount to Balancer B-33ETH-33BTC-33USDC pool using the `joinPool()` method.


Then, the attacker withdrew the deposited amount using `exitPool()`. During the asset transfer back, the WETH was unwrapped to the native token and transferred. This triggered the fallback method in the attacker’s contract.


During the `exitPool()` method call, the pool tokens’ total supply was changed, but the pool’s token balance remained unchanged.


The attacker then utilized the inflated price of the pool tokens as the collateral to repeatedly borrow the asset from the platform.


This was possible because the price oracle of the Sentiment platform obtained state info from the Balancer pool token, which did not reflect the correct state.


After the attack


This story has a [happy ending](https://web.archive.org/web/20260129075907/https://cointelegraph.com/news/sentiment-recovers-870k-after-negotiations-with-the-hacker) as the Sentiment team was able to recover 90% of the stolen funds from the attacker (and managed to recoup the rest).

#### Other read-only reentrancy attacks


Several read-only reentrancy attacks have occurred through price-asset manipulation. In 2023, [dForce network lost $3.6 million](https://web.archive.org/web/20260129075907/https://cryptopotato.com/defi-protocol-dforce-loses-3-6m-in-reentrancy-attack/) in this attack caused by the Oracle price issue.


As this protocol was deployed on two different networks, the losses extended across both Arbitrum ($2.6 million) and Optimism ($1 million) networks.


A similar attack occurred when the lending market of one of the most popular DEXs on the Polygon network, Quickswap, got exploited for $200,000 in two similar read-only reentrancy attacks. Soon after this attack, Quickswap closed its Lending feature.

#### Current threats


Read-only reentrancy is a novel form of attack sometimes neglected by developers and security auditors. As it’s based on interactions between different protocols, the risk is getting higher and more challenging to track.


It’s estimated that $100 million of funds are still at risk due to this attack vector.

#### Mitigation


Mitigation methods vary, depending on whether a new contract is being written or whether a contract that’s already deployed is being read.


For new contracts, a read-only reentrancy guard needs to be added. This works by verifying whether the reentrancy guard has not been locked. If it has, then an error is thrown (for example, Euler Finance).


The lock can be made public so those contracts that are calling the contract can check if the contract is already in lock mode.


For the rest, a function with a reentrant modifier can be called first. If it fails, the contract will be in locked mode, and reading from it should be avoided.
