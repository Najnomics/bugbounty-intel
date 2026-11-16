# 🛡️ Web3 Security Highlights: Key Takeaways from 2025

- **Source URL:** https://www.openzeppelin.com/news/web3-security-auditors-2025-rewind
- **Fetched:** 2026-11-16
- **Channel:** @defendor_eng
- **Telegram message:** https://t.me/defendor_eng/1179 (id 1179)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Web3 Security Auditor's 2025 Rewind

- Jainil Vora
- Frank Lei
- Kose Dogus & Ionut-Viorel Gingu

Welcome to the Web3 Security Auditor’s 2025 Rewind, a collection of succinct technical breakdowns of notable security incidents and vulnerabilities from the past year.

Previously known as the `Ethereum Smart Contract Auditor's Rewind`, the article series was originally authored by [Patrick Drotleff](https://x.com/patrickd_de), an Information Security and Privacy advocate, independent security researcher and mentor in the [Secureum](https://x.com/TheSecureum) community. After connecting at TrustX Istanbul, Patrick entrusted OpenZeppelin with continuing this tradition while he shifts focus to new endeavors.

In our [2024 Rewind](https://www.openzeppelin.com), we adhered to the original format while introducing several key changes: we expanded the scope beyond exploits to include bugs uncovered through traditional audits, contests, and bug bounty platforms, increasing the diversity of issues covered. This year, we have also included Ethereum upgrades, Rust-specific vulnerabilities, supply chain attacks, and Beacon Chain specific issues. Each entry delivers concise, actionable insights—highlighting the vulnerabilities and offering just enough context to identify these issues during security reviews or bug hunting.

Table of Content

## **The Highlights**

### The Pectra Upgrade

On May 7, 2025, Ethereum underwent its largest upgrade to date, [Pectra (Prague + Electra)](https://consensys.io/ethereum-pectra-upgrade), a dual-layer hard fork bundling 11 EIPs spanning smart account capabilities, staking mechanics, and rollup data efficiency. Out of all the changes, the following are the most relevant.

### EIP-7702: Set Code for EOAs

[EIP-7702: Set Code for EOAs](https://eips.ethereum.org/EIPS/eip-7702) enhances Ethereum account abstraction by introducing a new transaction type that lets EOAs persistently delegate execution to smart contract code (via an on-chain delegation indicator), enabling contract-like behavior for EOAs across transactions. This allows regular wallets to gain capabilities such as transaction batching, gas sponsorship or social recovery, without migrating to new addresses. Note that such powerful functionality comes with multiple security risks, as noted in [this article](https://quantstamp.com/blog/will-eip-7702-affect-your-code). Thus, soon after this feature was introduced, interesting vulnerability patterns and exploits started to emerge.

### Staking and Validator Related EIPs

- [**EIP-7251: Increase `MAX_EFFECTIVE_BALANCE`**](https://eips.ethereum.org/EIPS/eip-7251) increases the maximum validator stake from 32 ETH to 2,048 ETH, enabling automatic reward compounding and validator consolidation on the consensus layer. This enables institutional stakers to run less validators, reducing operational complexity while raising concerns about centralization.
- [**EIP-6110: Supply Validator Deposits On Chain**](https://eips.ethereum.org/EIPS/eip-6110) streamlines deposit processing by moving part of it to the execution layer, reducing the minimum deposit processing delay from hours to approximately 13 minutes. This improvement significantly enhances the user experience for new validators entering the network.
- [**EIP-7685: General Purpose Execution Layer Requests**](https://eips.ethereum.org/EIPS/eip-7685) is mostly relevant for the consensus layer, as it establishes a standardized communication framework between execution and consensus layers for handling deposits, withdrawals, and consolidations. This creates a unified system for cross-layer operations and lays the groundwork for future protocol enhancements.
- [**EIP-2935: Serve Historical Block Hashes from State**](https://eips.ethereum.org/EIPS/eip-2935) is mostly relevant for the execution layer, as it extends `BLOCKHASH` availability from approximately 1 hour (256 blocks) to roughly 27 hours (8,192 blocks), enabling contracts to reference recent historical data on-chain. This supports use cases like enhanced randomness generation, verifiable proofs, and rollup fraud proofs without requiring external dependencies - a developer can prove consensus layer state on the execution layer (i.e. the [EigenPods Checkpoint Proof System](https://hackmd.io/U36dE9lnQha3tbf7D0GtKw#The-Checkpoint-Proof-System)), up to 27 hours worth of roots.
- [**EIP-7002: Execution Layer Triggerable Exits**](https://eips.ethereum.org/EIPS/eip-7002) enables validators to initiate full or partial withdrawals directly from the execution layer instead of requiring consensus layer operations.

### Others

- [**EIP-2537: Precompile for BLS12-381 Curve Operations**](https://eips.ethereum.org/EIPS/eip-2537) introduces precompiled contracts for BLS12-381 operations, enabling efficient signature aggregation and zero-knowledge proof verification.
- [**EIP-7691: Blob Throughput Increase**](https://eips.ethereum.org/EIPS/eip-7691) raises the blob count from 3/6 to 6/9 per block, effectively doubling rollup data availability capacity and reducing L2 transaction costs.

For a deeper analysis of the inner-workings of the execution layer after the Pectra upgrade, consider reading [Inside Ethereum’s Engine: How the Execution Layer Actually Works](https://www.openzeppelin.com/news/how-the-ethereum-execution-layer-works).

### The Fusaka Upgrade

On December 23, 2025, Ethereum undervent another upgrade, [Fusaka](https://consensys.io/ethereum-fusaka-upgrade), bundling 13 EIPs that combine to improve scaling capacity, network efficiency and foundation for parallel executions for the Ethereum Network. Out of all the changes, the most relevant are:

### Major EIPs

- [**EIP-7825: Transaction Gas Limit Cap**](https://github.com/ethereum/EIPs/blob/master/EIPS/eip-7825.md) caps the maximum gas usage per transaction to 16,777,216 (2^24) gas. This cap represents approximately half of typical of block sizes(30-40 million before Fusaka). This decreased gas limit increases the probablity of denial-of-service attacks/scenarios on smart contracts with out-of-gas reverts on transactions.
- [**EIP-7594: Peer Data Availability Sampling**](https://github.com/ethereum/EIPs/blob/master/EIPS/eip-7594.md) allows nodes to perform data availability sampling(DAS) that helps scales Ethereum’s Layer 2. PeerDAS is a networking protocol that utilizes gossip for distribution, discovery for finding peers of particular data custody, and peer requests for sampling.
- [**EIP-7951: Precompile for secp256r1 Curve Support**](https://github.com/ethereum/EIPs/blob/master/EIPS/eip-7951.md) adds a precompile contract that efficiently performs ECDSA signature verification over the `secp256r1` elliptic curve. This provides major upgrade to wallet UX as hardware security modules (HSMs) including Apple Secure Enclave, Android Keystore, and FIDO2/WebAuthn devices can now be natively supported.

### Others

- [**EIP-7935: Increased Default Block Gas Limit**](https://github.com/ethereum/EIPs/blob/master/EIPS/eip-7935.md) increases the default block gas limit from 36 million to 60 million. While the transaction gas limit is approximately halved, the block gas limit is approximately doubled ensuring higher number of transactions to be included in a single block.
- [**EIP-7939: Count leading zeros (CLZ) opcode**](https://github.com/ethereum/EIPs/blob/master/EIPS/eip-7939.md) introduces a new opcode, `CLZ`, that counts the number of leading zero bits in a 256-bit word.

Find the full list of the EIPs [here](https://github.com/ethereum/EIPs/blob/master/EIPS/eip-7607.md/) to dive deeper into the Fusaka Upgrade.

Exploits Involving EIP-7702

### POT Token Exploit: Bypass Flashloan Protection Using EIP-7702

*Check out the full explanation in our [Notorious Bug Digest](https://www.openzeppelin.com).*

By allowing EOAs to set code in their account, EIP-7702 breaks backward compatibility of some contracts by deprecating the “EOA-only” check (i.e., `msg.sender == tx.origin`) that was commonly used to ensure that the caller was an EOA.

In August, an [unverified staking contract](https://bscscan.com/address/0x0aeb8c4a449e1f712676692ef8948d8c952feb53) on BSC [was exploited for $85k](https://bscscan.com/tx/0x8a7c96521ac64fc33d8d8ceecdea9c1da9c72148c4399905c38a07ee47c3f36f). The victim contract used the “EOA only” check to protect its `stake` function from flashloan-based price manipulation. The contract was exploited in the following steps:

1. The attacker deployed a [malicious contract](https://bscscan.com/address/0x3f94E8d115FB7a27ac6b8CfeaacfFe94652E8dEd#code) and [authorized its delegation to an EOA](https://bscscan.com/tx/0xd0b56d3a8eb9d2039c3855b64fb000d87853a67228746e4e182220b62ee5e993) using a 7702-type transaction.
2. The EOA transferred \~13.9 BNB tokens to **itself**, triggering arbitrary smart contract logic while ensuring that future `tx.origin == msg.sender` checks pass.
3. In the `fallback` function, the malicious contract flashloaned $3.5M BSC-USD tokens, bought POT tokens from the [PancakeSwap BSC-USD/POT pool](https://bscscan.com/address/0x408ea55ee4bf91b8d21a0f6a757b90edf287cf36#readContract) to inflate the price, then staked \~220k POT at the inflated price.
4. The attacker swapped the remaining POT tokens back to BSC-USD tokens to repay the flashloan and almost reset the BSC-USD/POT price.
5. In a [subsequent transaction](https://bscscan.com/tx/0x089e37fc8d51a16e4cf1865a5c2ad75ea0c06e50f3e43beb7368706f852f44fc), the attacker unstaked and received 3.3M POT tokens (versus 220k staked) due to the inflated recorded value.

### Gana Payment Exploit: Attacker Utilizes EIP-7702 Delegated EOAs to Update Operational Parameter and Bypass EOA-Only Protection

The same “EOA only” check was bypassed in the [Gana Payment exploit](https://rekt.news/gana-payment-rekt) in November. After compromising the staking contract’s owner private key, the attacker transferred ownership to another account, then used an EIP-7702 transaction to delegate execution to a malicious contract. This delegated code updated critical operational parameters in the staking contract and called `unstake`, bypassing the EOA-only guard via multiple EIP-7702 delegations causing a loss of **$3.1M**funds.

### The Evolution of Wallet Draining: From Single-Token Approvals to Complex Arbitrary-Logic Delegations

Traditional wallet-draining malware operates with significant limitations. Attackers typically trick users into signing malicious `approve()` transactions for individual tokens, instead of the intended action. However, this approach has significant constraints: it only works for one token per transaction, requiring multiple signatures and user-errors for comprehensive fund drainage.

EIP-7702 fundamentally changed this threat model. By enabling EOAs to temporarily delegate code execution to a smart contract, attackers can now trick users into [signing a single delegation transaction](https://x.com/realScamSniffer/status/1959423014011126224) that grants a malicious contract full authority to act on their behalf. Unlike traditional approvals, the delegated contract can execute arbitrary logic within a single delegated atomic transaction: it can sweep all token balances across multiple contracts, drain native ETH, liquidate positions, and bridge assets to other chains-all in one indivisible operation.

[Wintermute Research has highlighted](https://x.com/wintermute_t/status/1928501765865091400) another dangerous variant: attackers trick victims or use compromised private keys to delegate to simple malicious contracts that automatically sweep any incoming ETH to an attacker-controlled address, creating a persistent drain on the compromised account.

Bybit Cold Wallet Compromise: $1.4 Billion Stolen

In February, the centralized exchange Bybit [suffered a security breach](https://x.com/Bybit_Official/status/1892965292931702929) that led to the theft of approximately $1.4 billion (401,347 ETH) from its cold wallet. The attack [exploited vulnerabilities in the Safe Wallet multi-signature interface](https://x.com/safe/status/1894768522720350673), not the underlying smart contracts, highlighting how attackers can deceive signers into approving unintentional, malicious transactions—a reminder that on-chain security is only one layer of defense.

The breach [originated from a compromised Safe Wallet developer machine](https://x.com/safe/status/1894768522720350673), which allowed attackers to inject malicious JavaScript code into the Safe UI delivered to users. The tampered code specifically targeted Bybit’s signers through sophisticated transaction manipulation steps: when they attempted to approve routine internal transfers, the script saved a copy of the original transaction data, replaced it with attacker-controlled parameters, sent the modified transaction to hardware wallets for signing, and then restored the original data while keeping the malicious signature. This gave valid signatures for a transaction that redirected the proxy’s implementation slot to an attacker-controlled address—granting full control to drain the wallet.

The key takeaway is that multi-signature owners must verify hardware wallet prompts against the intended transaction structure. The article titled [Safe SecOps Guidelines for High-Value Safe Smart Accounts](https://medium.com/@bazzanigianfranco/safe-secops-guidelines-for-high-value-safe-smart-accounts-a5641f6ee725) outlines best practices for blind-signing and operational security, while [the following incident investigation report](<https://github.com/verichains/public-audit-reports/blob/main/Bybit%20Incident%20Investigation%20-%20Preliminary%20Report%20v1.0%20(for%20public%20release).pdf>) provides detailed technical insights into the breach.

### Balancer v2 Rounding Precision Loss

In November, Balancer v2 Composable Stable Pools [suffered a sophisticated attack](https://x.com/Balancer/status/1990856260988670132) resulting in over $121 million in stolen funds. The vulnerability exploited a rounding behavior in the Stable Pool contracts, which are designed for assets that swap at near parity or known exchange rates.

The root cause was a precision loss in the `_upscale` function which is called during swaps to scale an amount of tokens by a given amount of decimals and a variable exchange rate. The `_upscale` function always rounded down (`mulDown`) regardless of swap direction.

When token amounts were orders of magnitude smaller than their scaling factors, this truncation became non-negligible. For example, with `amount = 17` and `scalingFactor = 1058132408689971699`, the calculation `17 * 1058132408689971699 / 1e18` should yield approximately 17.98, but Solidity’s floor division truncated this to 17. This leads to a complete loss of the intended rate adjustment, which ultimately causes the attacker to underpay for a given `amountOut` of tokens they take out of the pool.

To further magnify the effects of the imprecision and make them exploitable, a low-liquidity state was necessary. The attack leveraged Balancer’s `batchSwap` functionality, which allows transient internal balances that only settle at batch completion. The attacker manipulated pools into low-liquidity states by burning BPT (Balancer Pool Tokens) for underlying tokens like WETH and osETH.

The exploit executed in the following repeating triplet:

1. a “prime” swap to position the pool for maximum truncation (e.g., WETH to osETH).
2. an “exploit” swap that realized the rounding loss (often using exactly 17 wei against vault balances of 18).
3. a “reset” swap to restore balances for the next iteration.

After numerous iterations, the accumulated deltas credited the attacker with the majority of pool funds.

For further details and mathematical analysis, consider reviewing the [Balancer post-mortem](https://x.com/Balancer/status/1990856260988670132) or articles from [OpenZeppelin](https://www.openzeppelin.com/news/understanding-the-balancer-v2-exploit), [Trail of Bits](https://blog.trailofbits.com/2025/11/07/balancer-hack-analysis-and-guidance-for-the-defi-ecosystem/), and [Certora](https://www.certora.com/blog/breaking-down-the-balancer-hack).

### Forked Protocol Side-Story - Beets on Sonic

As a Balancer fork, Beets on Sonic was [affected by the same vulnerability](https://x.com/beets_fi/status/1985281285816754179?s=20), enabling the [attacker](https://sonicscan.org/address/0xf19fd5c683a958ce9210948858b80d433f6bfae2) to steal \~$3M worth in [Beets Staked Sonic (stS) tokens](https://sonicscan.org/address/0xf4fa7f3308a1543e7d89950519341c7ce479400b). To contain the exploit, the Sonic team [updated](https://github.com/0xsoniclabs/sonic-sfc/commit/b584c863b498319f9f90494247750333f1a8e120) their Special Fee Contract—a privileged contract capable of modifying the EVM state database—to freeze the attacker’s account. The added `freeze` function sets the account’s native token balance to zero and replaces the account’s code with a [special contract](https://sonicscan.org/address/0xcdc13932990fdbc8e4397af1bfd0762d7e6d71ba#code) that has no `public`functions and cannot receive native tokens. Since the attacker had no external approvals, this was intended to prevent them from paying gas and moving funds.

However, the stS supported `permit`, which the attacker [used](https://sonicscan.org/tx/0x91cd63353da36065928702df03b5e8b030b979bc4e6a87601ba68c590f26732c) to grant allowance to another owned address, and then [execute `transferFrom`](https://sonicscan.org/tx/0x21a1b217e25d1bcd63c72bdaa4bbf64bf6108e1345e214e4da733833bdc8a257) to move the frozen tokens to that account. Finally, the attacker swapped the stS tokens across multiple [transactions](https://sonicscan.org/tx/0xd777b50814f90f83fa13094618700620fe71cb2b3042266dd87d42372a1a291d).

Paxos Accidentally Mints $300 Trillion

In October, Paxos—the issuer of PayPal’s PYUSD stablecoin—[accidentally minted $300 trillion worth of tokens](https://etherscan.io/tx/0xc45dd1a77c05d9ae5b2284eea5393ecce2ac8a7e88e973c6ba3fe7a18bf45634) as part of an internal transfer process.

[PYUSD](https://etherscan.io/address/0x94d0f384d839a7cef8bb6a8be3e2541ec9355343#code) is a permissioned token: minting and burning are restricted via role-based controls and specific whitelists for each `supplyController`.

However, the system lacks failsafes or upper limits on mintable supply, allowing a permissioned entity to inadvertently mint an arbitrarily large amount. The incident [was attributed to a technical error](https://x.com/Paxos/status/1978565015943950411) and was quickly reversed-the [$300 trillion was burned](https://etherscan.io/tx/0xaa532ae7f06cccdbdc226f59b68733ae8594464a98e128365f8170e305c34f4b) within minutes. Otherwise, it could have caused significant distress in PyUSD markets and a catastrophic depeg.

While no significant market disruption occurred, the episode highlights the need for stronger operational safeguards around permissioned stablecoins. The sheer scale of the mint—exceeding global GDP by some estimates—underscores that permissioned on-chain design must be matched by robust off-chain controls, such as minting caps, multi-party validation, or on-chain proof-of-reserve checks.

### Yearn yETH Weighted StableSwap Exploit

In [late November 2025](https://github.com/yearn/yearn-security/blob/master/disclosures/2025-12-01.md), Yearn’s yETH weighted stableswap pool suffered a multi-phase exploit. At a high level, by pushing the pool into an extreme numerical regime, the attacker drove the iterative supply solver outside its designed domain. At a low level, repeated `unsafe_div` floor-rounding inside the solver caused the product accumulator (`r`, the pool’s `Π`-like term) to truncate to `0`, collapsing a key constraint in the `D` calculation and enabling massive over-minting:

1. **Product-term collapse**: By repeatedly shaping the pool into an extreme imbalance and then performing carefully crafted deposits, the solver’s iteration pushed the product accumulator toward `0` via integer floor-division updates. Once `Π` hit `0`, the supply calculation effectively drops the product constraint, returning an inflated `D` and causing the protocol to over-mint yETH LP tokens.
2. **“Repair” `Π` but keep inflated `D`**: A subsequent call path recomputed `Π` from balances (restoring it to a non-zero value) without undoing the inflated supply. Then, a permissionless rate update reconciled the discrepancy by burning yETH from the staking contract, allowing repeated withdrawals until the pool’s internal supply was driven to `0`.
3. **Re-enter bootstrap path**: With `supply == 0`, an initialization-only branch became reachable again. A dust deposit that violated the solver’s domain (effectively `A * Σ < D * Π`) hit an unsafe subtraction that underflowed, wrapping into a massive value and minting roughly `2.35e56` yETH LP tokens, which was used to drain the remaining liquidity from the yETH/WETH Curve pool.

The core failure mode in the solver looks like this (simplified from [`Pool.vy`](https://etherscan.io/address/0xCcd04073f4BdC4510927ea9Ba350875C3c65BF81#code)):

This incident highlights two audit points:

- Ensuring that roundings and any unchecked arithmetic cannot break math invariants, especially under extreme/imbalanced inputs.
- Ensuring that one-time lifecycle paths (e.g., initialization branches) cannot be re-entered once the system is settled.

### CPIMP: Clandestine Proxy in the Middle of Proxy

In July, a [sophisticated industry-wide attack campaign](https://x.com/deeberiroz/status/1943041785476894996) targeting proxy contracts across multiple chains was discovered. The CPIMP (“Clandestine Proxy in the Middle of Proxy”) front-runs proxy initialization transactions, inserting a malicious implementation that forwards to the legitimate one while retaining hidden control.

The CPIMP lets the victim’s initialization succeed, transparently forwards calls, restores itself in storage after every transaction, and spoofs events and storage slots so that explorers like Etherscan display the legitimate implementation. It remains dormant until sufficient funds accumulate, at which point the attacker has full control to upgrade to arbitrary logic.

[Decompiled CPIMP code revealed](https://dedaub.com/blog/the-cpimp-attack-an-insanely-far-reaching-vulnerability-successfully-mitigated/#dissecting-the-cpimp-a-backdoor-powerhouse) - a highly engineered backdoor framework with multiple sophisticated features:

- A hardcoded backdoor address (0xa72df45a…), acting as a super-admin with unrestricted control
- Granular function-level routing, allowing the attacker to selectively hijack specific functions (e.g., only divert transfers) without alerting all users
- Protocol-specific logic, embedded to thwart recovery attempts—some CPIMPs contained hard-coded checks that reverted transactions attempting to transfer more than 90% of balances, forcing protocols like Pendle to recover funds in smaller batches
- CPIMP nesting, in which malicious proxies point to other malicious proxies
- Meta-transactions, allowing execution capabilities through signatures in cases the admin addresses were blacklisted
- Batch token-draining functions and direct storage slot manipulation

While most affected protocols recovered funds, the attack vector remains viable against proxies not initialized atomically at deployment. CPIMPs were leveraged to [exploit Kinto in July](https://medium.com/mamori-finance/%EF%B8%8F-post-mortem-k-proxy-hack-our-path-forward-c2c3809882c6), as well as [the USPD protocol in December](https://x.com/USPD_io/status/1996711283446464598?t=OBoRpE4KaqXjT1yCJwkUtw&s=35).

### GMX Cross Contract Re-entrancy and Price Manipulation Exploit

In July, [GMX V1](https://x.com/GMX_IO/status/1943336664102756471) on Arbitrum suffered a \~$40 million exploit.

The root cause of this exploit was design flaw allowing cross-contract reentrancy in `GMX Vault` contract. This allowed for the price manipulation of GLP tokens which were later redeemed for all underlying tokens in the GMX V1 protocol.

The `PositionManager` contract managed two important things:

- Updating global short data by calling `ShortsTracker.updateGlobalShortData` function before any changes in the positions
- Enabling and disabling leverage by calling the `TimeLock` contract that allows `GMXVault` to manage positions

However, the in-between `OrderBook` contract transferred ETH to the user if the underlying collateral was WETH, which allowed the attacker to hijack the context of the transaction.

Once the attacker gained control of the transaction, they first staked \~$5M amount of `USDC` to purchase `GLP` token at fair price. Then, they opened a huge short position($15M) directly on the `GMXVault` which was allowed since leverage was not yet disabled, and also without updating the global short data that inflated the `AUM`(Assets Under Management) calculation. This manipulation artificially inflated the price of the GLP token from $1.45 to $27 and which the attacker redeemed for different underlying tokens in GMX protocol through the `RewardRouter` contract. The following diagram showcases the entire attack vector:

At the end, the hacker accepted a 10% white-hat bounty and returned the stolen funds back to GMX team.

### Cork Protocol: Rollover Pricing Manipulation, Arbitrary Configuration, and Missing Access Control in a Uniswap v4 Hook

*An exploit so complex, the attacker had to chime in to [explain the root cause](https://etherscan.io/tx/0xe82ad5097063589996b6ae2b042514b72cf17f56c7fcecc625a418f511cc150e)*.

In May 2025, Cork Protocol [suffered an exploit](https://www.cork.tech/blog/post-mortem) that resulted in the loss of 3,761.8 wstETH (\~$12M), affecting the `wstETH:wETH` market. Cork Protocol offers a product similar to a Credit Default Swap (CDS), allowing users to hedge against depegging risks for pegged assets such as stablecoins and liquid staking tokens. These products are implemented as **Depegged Swaps (DS)**. In the `wstETH:wETH` market, wstETH is the **Pegged Asset (PA)**, wETH is the **Redemption Asset (RA)**, weETH8CT-2 is the **Cover Token (CT)**, and weETH8DS-2 is the **Depegged Swap (DS)** token. The CT and DS tokens form a paired set of derivative tokens, managed dynamically by Cork’s **Peg Stability Module (PSM)**, which supports the following exchanges:- `PA + DS = RA` and `CT + DS = RA`

The exploit combined multiple moving parts to steal both weETH8CT-2 (CT) and weETH8DS-2 (DS), and then redeem them for the RA token (wstETH) via the PSM’s `returnRaWithCtDs` function. The attacker leveraged **three vulnerabilities** to execute the drain:

1. **Manipulating rollover pricing at market expiry** Once a market expires, the rollover mechanism ensures continuous pricing when the next market kicks-off. However, an edge-case occurs when `DS` tokens are purchased in a low-liquidity market which is about to expire: the risk premium drastically increases and [Historical Implied Yield Average (HIYA)](https://github.com/Cork-Technology/Depeg-swap/blob/04068807d3c350955a1e84532b68805b68ca96fb/contracts/libraries/DsFlashSwap.sol#L103-L112) values are skewed. So, when the next market begins, the price of CT tokens starts out being extremely cheap. The attacker exploited this bug to steal CT tokens from the next market at an extremely cheap price.
2. **Market creation using arbitrary configuration** The Cork Protocol allowed for the creation of markets without thoroughly validating the configuration. As a result, the attacker was able to create a fake proxy market (`weETH8DS-2:wstETH`) with proxy derivative tokens wstETH5CT-3 and wstETH5DS-3 (referred to here as pCT and pDS). Critically, the proxy market was configured such that weETH8DS-2 was treated as the Redemption Asset (RA)\*\*, even though it is actually the DS token of the real `wstETH:wETH` market. This configuration helped deceive the `FlashSwapRouter` to transfer the weETH8DS-2(DS) held by it to the proxy market.
3. **`CorkHook` lacked sufficient access control** Once the UniswapV4 [pool was `unlocked`](https://github.com/Cork-Technology/Cork-Hook), the `beforeSwap` hook in `CorkHook` allowed [arbitary `hookData`](https://github.com/Cork-Technology/Cork-Hook) to be passed on to `CorkCall` contract through flash swap process. The attacker utilized this to pass malicious hook data to the `CorkHook` acting as **men-in-the-middle** between the `CorkHook` and `UniswapV4` callback. Using price manipulation and malicious hook data on `FlashSwapRouter` the attacker was able to extract weETH8DS-2 (DS) tokens from the proxy market as well.

Combining all these vulnerabilities, the attacker was able to capture both weETH8DS-2 (DS) and weETH8CT-2 (CT) token, and executed `returnRaWithCtDs` function in `Pegging Stability Module` on the *real* `wstETH:wETH` market, redeeming the paired tokens to drain wstETH collateral.

This was one of the most complex attacks observed in 2025. For a deeper dive, see the [official post-mortem](https://www.cork.tech/blog/post-mortem).

### Panoptic Protocol Position Spoofing Bug and Whitehat Rescue

Panoptic V1 is a decentralized perpetual options trading protocol on Ethereum. In late August 2025, it was found to have a [critical security flaw](https://panoptic.xyz/blog/position-spoofing-post-mortem#appendix-how-do-you-spoof-your-position-list-in-panoptic-v1). The issue, known as the *position-spoofing exploit*, could allow an attacker to bypass Panoptic’s collateral checks and drain funds from the protocol’s liquidity pools. The exploit was reported by a security researcher before any confirmed malicious use, which enabled the Panoptic team to respond quickly to protect user assets.

The root cause was Panoptic’s **position fingerprinting** design. In Panoptic V1, smart contracts tracked each user’s open positions by **XOR-hashing** multiple position IDs into a single fingerprint value. In the Panoptic Protocol, users may hold up to 25 open positions. While this approach was order-independent and gas-efficient, it was not collision-resistant. Panoptic V1 contracts neither fully validated user-supplied position lists during verification nor checked if the count of open positions, assuming that **fingerprint** would always be unique.

As a result, an attacker could craft a fake list of position IDs that produced the same fingerprint as a legitimate list. This allowed them to spoof ownership and trick the system into accepting positions they did not actually hold. With spoofed positions, the attacker could bypass collateral requirements and withdraw assets without proper backing, creating a potential pool-drain scenario.

The Panoptic team, working alongside Cantina and SEAL-911, coordinated incident response with the community and successfully secured \~$4M in user funds. Of that total, \~$550K required an active whitehat rescue to prevent potential exploitation.

## **The Usual**

### Deflationary Tokens in AMM Pools

In January, multiple instances of the [PumpToken](https://etherscan.io/address/0x539d54074e052ae82de4936ae6bb213ab773559e#code) template were [exploited](https://etherscan.io/tx/0xef34f4fdf03e403e3c94e96539354fb4fe0b79a5ec927eacc63bc04108dbf420), resulting in losses of roughly $60,000. The root cause was a math flaw in the `removeLiquidityWhenKIncreases` function: when the liquidity in the PumpToken/WETH Uniswap pool exceeds 105% of its initial value, the function burns a portion of the PumpTokens directly from the pool to reduce liquidity. This mechanism **artificially increases the PumpToken’s price, enabling profitable arbitrage for token holders**.

The attacker flash-loaned 30,000 WETH, swapped it for 99.8% of the pool’s PumpTokens, and then supplied both assets to quadruple the pool’s liquidity. Upon calling `removeLiquidityWhenKIncreases`, three-quarters of the deposited PumpTokens were burned, further inflating the token’s price. Finally, the attacker withdrew their liquidity and sold the remaining PumpTokens back into the pool at the inflated rate, draining nearly all of its WETH.

In May, a [KRC/BUSD pool on BSC was drained](https://www.openzeppelin.com) after an attacker exploited deflationary token behavior, not a flaw in the AMM itself. The attacker repeatedly transferred KRC tokens to the pool and called `skim`, triggering KRC’s burn logic on each transfer. Since the pool did not account for token burns, its KRC balance steadily decreased, pushing the price to extreme levels. Once KRC became artificially scarce, the attacker swapped a small amount of KRC for nearly all the BUSD in the pool.

In September, the New Gold Protocol’s NGP token on BNB Chain [was exploited](https://x.com/hklst4r/status/1968413473487868150) for \~$2M due to incorrect fee-handling logic in its `transfer` implementation, which allowed an attacker to manipulate AMM reserves and extract value via repeated swaps [\[1\]](https://rekt.news/newgold-protocol-rekt).

NGP charged a proportional fee on `sell` actions by detecting transfers to the liquidity pair. However, instead of deducting the fee from the seller’s tokens, the implementation removed tokens directly from the pool’s balance **first**, and then called `sync()` before the seller’s tokens were transferred in. This ordering violated AMM assumptions by artificially reducing the pool’s token reserves and immediately updating the price upward.

Using large flash loans, the attacker repeatedly swapped USDT to NGP and then sold NGP back into the pool. On each `sell`, the flawed fee logic reduced the pool’s NGP balance before the trade settled, causing the pool price to spike and enabling profitable round trips. Repeating this process allowed the attacker to drain the pool’s reserves.

A similar deflationary token mechanism [was exploited](https://blog.verichains.io/p/rant-exploit-analysis) in the RANT token on BSC. RANT implemented a balance-based burn mechanism that automatically burned tokens when the RANT balance held by a designated liquidity pool exceeded a user-controlled threshold. By repeatedly transferring RANT into the pool and triggering this burn logic, the attacker continuously reduced the pool’s RANT balance without updating the AMM’s reserves. This artificially inflated the RANT price, allowing the attacker to first drain the pool of RANT tokens and then sell them back at extreme prices to extract all the WBNB liquidity.

### Denial of Service Through User-Manipulated Storage

During an [OpenZeppelin audit of f(x) v2 protocol](https://www.openzeppelin.com), a [critical bug was identified](https://www.openzeppelin.com) that could be exploited to permanently lock user positions via manipulation of a recursive function.

The f(x) protocol manages leveraged positions using a tick-tree structure (implemented through [Disjoint Sets](https://en.wikipedia.org/wiki/Disjoint-set_data_structure)), where positions are grouped into price bands (“ticks”) and collectively rebalanced or liquidated. Each tick has a root node, and partial liquidations shift nodes between ticks, creating parent–child relationships. To compute a position’s current collateral and debt, the protocol traverses this tree using [a recursive path-compression function](https://github.com/AladdinDAO/fx-protocol-contracts/blob/56a47eab8d10334e479df83a2b13a8b68ce390e9/contracts/core/pool/TickLogic.sol#L65-L85).

The vulnerability arose from the interaction of three issues:

The `_liquidateTick` function failed to ensure that a partially liquidated tick actually moved to a new tick, allowing child nodes to be repeatedly attached to the same tick. Hence, disjoint sets could be lengthened.

The `redeem`, `rebalance`, and `liquidate` functions allowed partial liquidations with arbitrarily small debt amounts (as low as 2 wei). This made the attack repeatable many times until a position would be deemed healthy again.

The recursive `_getRootNodeAndCompress` function would eventually cause a `Stack Overflow` error if a node chain grew to \~150 levels.

By repeatedly calling `redeem` with minimal amounts, an attacker could force the creation of hundreds of child nodes on the same tick without changing prices. Once the tree depth exceeded the recursion limit, any attempt by affected users to update or close their positions would revert due to stack overflow, effectively locking their funds.

The issue was fixed by replacing the recursive logic with an iterative implementation, enforcing minimum liquidation amounts, ensuring that ticks always advance during liquidation, and adding admin tooling to compress malformed trees.

The issue highlights how attacker-influenced data structures can lead to denial-of-service conditions. Depth limits, iteration over recursion, and strict input constraints are essential to prevent fund-locking attacks.

### Missing Input Validations

In April, [Loopscale was exploited](https://rekt.news/loopscale-rekt) for approximately $5.8 million after an attacker abused insufficient validation of oracle accounts used in asset pricing [\[1\]](https://rekt.news/loopscale-rekt), [\[2\]](https://x.com/greyswan_/status/1916227201067872263). The issue allowed the attacker to obtain undercollateralized loans by supplying manipulated price data to the protocol’s lending logic.

The root cause was that the protocol accepted an `oracle_account` directly from user-provided `remaining_accounts` when computing asset prices, without verifying that the account matched the oracle registered for the given collateral. This allowed an attacker to deploy a malicious program that mimicked a valid oracle interface and return attacker-controlled prices during loan creation.

By feeding artificially inflated collateral prices into the `create_loan` flow, the attacker was able to borrow assets with much less than their collateral value, draining the USDC and SOL vaults. The exploit did not require modifying Loopscale’s contracts; it relied entirely on supplying a forged oracle account that passed insufficient checks.

Following the incident, Loopscale halted markets and patched the oracle validation logic. The stolen funds were later returned to protocol-controlled wallets after engagement with the attacker.

In June, [a bug was discovered](https://www.chainsecurity.com/blog/when-empty-means-valid-exploiting-mpt-proof-verification-for-an-alternative-truth?utm_source=substack&utm_medium=email) in the [`proveth` Merkle Patricia Tree (MPT) proof verification library](https://github.com/lorenzb/proveth), widely used to prove inclusion or exclusion of L1 contract storage on L2.

`proveth` verifies inclusion by walking a proof path until it reaches a node matching the full queried key; if the path ends without reaching such a node, the key is treated as absent, enabling exclusion proofs. However, the implementation failed to verify that the provided proof path was complete. An attacker could intentionally truncate the proof while still passing validation, causing the verifier to incorrectly accept a forged exclusion proof. This breaks a fundamental MPT invariant: absence is only meaningful if the path is complete. By accepting “early termination” as valid absence, the verifier allowed attackers to present an alternative state where existing storage slots appeared empty, potentially proving false claims about balances, ownership, or configuration values.

In July, an [attacker exploited ZKSwap’s Ethereum bridge](https://blockaid.io/blog/how-zkswaps-5m-exploit-couldve-been-prevented-with-onchain-monitoring) by abusing its emergency withdrawal feature (Exodus Mode) to steal roughly **$5 million**. The core vulnerability was that the bridge’s `verifyExitProof()` function (intended to validate withdrawal proofs) was programmed to always return `true` without performing any cryptographic verification. After triggering Exodus Mode, the attacker submitted fabricated proofs claiming fake token balances, which the contract accepted as valid due to the broken verification step. The attacker then repeated the process across multiple token IDs and exploited a faulty **“exited” mapping** (nullifier) that failed to prevent duplicate claims, allowing for the repeated crediting of balances. Finally, the attacker called the standard withdrawal flow to transfer out the fraudulently credited tokens, draining approximately **$5 million** from the bridge.

### Underflows and Overflows

In March, [the TrustedVolumes market maker was exploited](https://blog.decurity.io/yul-calldata-corruption-1inch-postmortem-a7ea7a53bfd9) after using an obsolete and vulnerable version of the 1inch - Fusion V1 protocol’s `Settlement` contract. The attacker crafted a malicious swap (6 wei USDT for 1,000,000 USDC) and exploited an integer overflow in the settlement logic to corrupt memory, allowing arbitrary call data to be injected at unexpected memory locations, similarly to a Web2 buffer overflow.

This allowed the attacker to trick the 1inch `Settlement` contract into calling `TrustedVolumes` as the resolver, breaking a core design assumption: only the resolver that initiated settlement should ever be called back. Since the resolvers are the entities that transfer and collect any deficits/surpluses from the swap, this prompted the `TrustedVolumes` contract to use its own funds for the swap.

In May, Cetus, then the largest DEX on Sui, [was exploited](https://x.com/CetusProtocol/status/1925567348586815622) for \~$223 million due to a flaw in its overflow-checking logic during liquidity calculations. About $162M was frozen and later recovered via a [validator-approved protocol upgrade](https://blog.sui.io/cetus-incident-response-onchain-community-vote/), while the rest was lost. The underlying issue allowed an attacker to mint extremely large concentrated liquidity positions while supplying only one unit of token, and then drain liquidity from multiple pools.

The root cause was an incorrect bounds check in a helper function validating whether values could be safely left-shifted by 64 bits. While Move aborts on arithmetic overflows, bit shifts truncate silently, requiring explicit checks. Cetus used an incorrect threshold, allowing certain oversized values to pass even though shifting them would drop significant bits.

The attacker exploited this during liquidity provisioning. By choosing an extremely narrow tick range at the upper end of the price spectrum and supplying an intentionally oversized liquidity value, they caused an intermediate multiplication to exceed the safe bit width. The flawed check allowed execution to continue, and the subsequent shift truncated the value, collapsing the numerator used in the token-amount calculation. This caused the protocol to compute that only one token was required to back an enormous liquidity position. After minting this position, the attacker immediately removed the liquidity across several transactions, extracting assets from the pools before repaying their flash loan.

Price Manipulations

In September, [Sharwa Finance was exploited](https://x.com/SharwaFinance/status/1980535243875463639) via a flash-loan driven price manipulation that abused unsafe price oracle usage and missing slippage checks.

The protocol relied on Uniswap V3 spot price as a price oracle without any validation. After depositing collateral and opening a leveraged long position, the attacker flash-loaned large amounts of assets to manipulate the Uniswap pool price. They then closed their position through Sharwa’s swap logic, which executed at the manipulated price and further amplified the price impact. Once the protocol accepted the broken exchange rate, the attacker reversed the manipulation, repaid the flash loan and kept the difference.

This incident highlights the risk of using DEX spot prices as sole oracles without further validation or TWAP price feeds.

### Rounding Errors

In February, [the zkLend lending protocol was exploited](https://www.openzeppelin.com) due to a rounding-down error in its withdraw logic. The attacker first initialized an empty market with a 1-wei deposit, then used flash loans to artificially inflate the `lending_accumulator` by paying extra fees. After other users deposited funds, the attacker repeatedly deposited and withdrew assets. Since rounding caused withdrawals to burn the same number of shares as deposits—despite withdrawing more assets each time—the attacker extracted value and drained the protocol.

This exploit follows a broader pattern seen in other lending protocols, including [Radiant Capital](https://medium.com/@RadiantCapital/post-mortem-report-radiant-capital-aea46cb985ae), [Silo Finance](https://medium.com/immunefi/silo-finance-logic-error-bugfix-review-35de29bd934a), [Raft Finance](https://immunebytes.com/blog/raft-protocol-exploit-nov-10-2023-detailed-analysis), and [Wise Finance](https://x.com/danielvf/status/1746303616778981402?s=46), where attackers target empty markets to inflate accounting variables and amplify otherwise minor rounding errors.

The key takeaway is that rounding bugs only become critical when they can be amplified via inflation. Empty markets are especially dangerous in lending protocols, as inflated variables can affect other markets and drain system-wide liquidity. As such, auditors should ask which variables are inflatable in empty states and evaluate rounding behavior in that context—many of these exploits were not just rounding issues, but rounding-plus-inflation attacks that escalated low-severity bugs into critical failures.

In September, [Bunni V2 AMM was hacked](https://blog.bunni.xyz/posts/exploit-post-mortem/) for \~$8.4M: a rounding direction that was safe in normal cases became unsafe in extreme cases. Each pool splits funds into an active balance (used for swaps) and an idle balance, and computes liquidity from two estimates based on each token’s active balance, then uses the smaller estimate. During LP [withdrawals](https://github.com/Bunniapp/bunni-v2/blob/ad8acfc30249da5a63450adf4a92c946c260e9de/src/lib/BunniHubLogic.sol#L478), the pool decreases the idle balance proportionally, and the computation below was intentionally rounded down:

The assumption was rounding down the decrease keeps more idle balance and less active balance, leading to higher price impact in the pool’s favor. However, the attacker broke the assumption: they pushed token0’s (USDC) price to an extreme via flashloan swaps, leaving token0’s active balance at 28 wei, then issued many tiny withdrawals that disproportionately reduced the token0’s active balance to 4 wei and caused liquidity to drop by \~84%. Finally, a large swap moved token0’s price more than it should have, flipped the pool to use the token1 liquidity estimate, and the resulting recorded liquidity increase was then sandwiched for profit.

In June, [ResupplyFi was exploited](https://rekt.news/resupplyfi-rekt) for approximately $9.8 million after an attacker manipulated the exchange rate by targeting a near-empty ERC4626 collateral vault [\[1\]](https://x.com/Phalcon_xyz/status/1938073001087652021). This allowed them to borrow essentially all available reUSD reserves while supplying only **1 wei** of collateral.

The root cause was an exchange-rate calculation that divided a fixed constant by the collateral’s share price and rounded the result down. Because the market had just been deployed and held almost no shares, the attacker was able to inflate the collateral’s share price via a direct donation. When this inflated value was used as the denominator, the floor division caused the computed exchange rate to collapse to zero.

With the exchange rate equal to zero, the protocol’s loan-to-value checks effectively broke: depositing even a minimal amount of collateral appeared sufficient to support an arbitrarily large borrow. The attacker deposited 1 wei of collateral and immediately borrowed all available liquidity from the market before it could be paused.

### Inconsistent Scaling

- In May, the [MBU token contract was exploited](https://www.openzeppelin.com) for \~$2M due to an incorrect decimal scaling bug in its deposit logic. When BNB was deposited, the contract correctly converted its value to USDT (scaled by 1e18), but then erroneously applied an additional 1e18 scaling before dividing by the MBU/USDT price. This caused the minted MBU amount to be inflated by 1e18, allowing the attacker to deposit a tiny amount of BNB and mint an enormous number of MBU tokens. USDT deposits were unaffected, as they bypassed the extra scaling.
- A similar decimal-mismatch issue was [identified in Across protocol during an audit](https://www.openzeppelin.com). The contract calculated required gas token amounts assuming an 18-decimal token, failing to adjust for tokens with fewer decimals such as USDC (6 decimals). As a result, withdrawals from a funder contract would overcharge by a factor of 10¹², leading to significant fund losses.
- In May, the [KelpDAO](https://x.com/KelpDAO) treasury [minted excessive 31.2 quintillion](https://x.com/KelpDAO/status/1917503028267213270) of rsETH tokens as protocol fee. The root cause was identified that the new upgrade incorrectly assumed the scaling base as `1e18` instead of the actual `1e36` used in the protocol. This inflated the protocol fee calculation and minted KelpDAO extra amount of rsETH tokens. No funds were lost and the team responsibly burned those extra tokens.

### Arbitrary Calls

In January, a [project using ERC-6492 was exploited](https://www.openzeppelin.com) for \~$50k due to an arbitrary call vulnerability in its signature verification logic. [ERC-6492](https://eips.ethereum.org/EIPS/eip-6492) extends [ERC-1271](https://eips.ethereum.org/EIPS/eip-1271) by allowing signature validation for counterfactual contracts via wrapped signatures that optionally deploy the signer contract using user-supplied create2Factory and calldata.

The project used a simplified verifier that, when encountering a counterfactual signature and a signer address with `code.length == 0`, blindly called the user-provided `create2Factory`. While this appears exploitable, naive attempts failed because calls to `isValidSignature` on non-deployed contracts revert due to empty return data.

The attacker bypassed this by abusing EVM precompile contracts, which have `code.length == 0` but still return data. Specifically, they used precompile 0x04, which echoes its input, ensuring the isValidSignature call returned sufficient data to pass decoding. By setting the signer to the precompile and the factory calldata to `USDC.transfer(attacker, balance)`, the attacker triggered an arbitrary token transfer while still satisfying the ERC-1271 check.

In June, Silo Finance was [exploited due to missing input validation in the `Leverage` contract](https://silofinance.atlassian.net/wiki/external/NjUxMDY2ZDA2NjQyNDBmZGFkODZlNTA1YTE3YWFmMTA). The contract allows users to open leveraged positions by approving it to borrow on their behalf up to their solvency limit. However, its swap logic let callers supply an arbitrary target and calldata:

The attacker abused this by initiating a “swap” that instead called borrowing functions, causing the contract to borrow on behalf of unsuspecting users and send the funds to the attacker as the receiver.

In July, [ArcadiaFi was exploited](https://rekt.news/arcadiafi-rekt) for approximately $3.6M after an attacker abused unvalidated external calls in the protocol’s rebalancing logic, enabling arbitrary actions on victim accounts under elevated privileges [\[1\]](https://x.com/Fried_rice/status/1945022619063144856).

Prior to the exploit, the attacker deployed contracts that triggered ArcadiaFi’s automated circuit breakers, forcing the protocol into a `paused` state. After investigation found no immediate threat, the protocol was `unpaused`. However, this `pause`–`unpause` cycle activated a cooldown period, during which the protocol could not be paused again, removing an important mitigation at the moment the real attack began.

The main technical flaw was that the rebalancer accepted user-supplied swap data and router addresses without validation. Although the system enforced a layered permission model, where only `Account`s could call the `Rebalancer` and only the `Rebalancer` could invoke privileged account actions, these guarantees relied on the assumption that the router invoked during rebalancing was trusted. That assumption was never enforced.

By injecting a malicious contract as the swap router during a `rebalance` call, the attacker effectively executed code with Rebalancer-level authority over victim accounts. With this, they were able to selectively specify which debts to repay while withdrawing the account’s full asset balance. This allowed the attacker to repay only a minimal portion of liabilities to satisfy health checks while extracting most of the funds. Since the account ended the transaction in a “healthy” state, the protocol treated the operations as valid, and assets were drained.

### Faulty Business Logic

In October, the Abracadabra protocol was [exploited for \~$1.7M](https://x.com/hklst4r/status/1974477630171734327). The `CauldronV`4 contract’s `cook` function processes a list of actions (similar to `multicall`) and performs a solvency check only at the end of execution, if the `needsSolvencyCheck` was set. This flag is set by actions such as `ACTION_BORROW`, which naturally should make sure the borrower’s position is still healthy. However, upon encountering an unsupported action, the `cook` function would reset the `needsSolvencyCheck` flag.

By calling `cook` with actions = \[5 (`ACTION_BORROW`), 0 (`ACTION_UNSUPPORTED`)\], the attacker borrowed funds without collateral, then cleared the flag via the invalid action, bypassing the final solvency check and extracting uncollateralized liquidity.

In January, the [UniLend protocol was exploited](https://slowmist.medium.com/analysis-of-the-unilend-hack-90022fa35a54), suffering a loss of $197K. The exploit was made possible due to a logic flaw in the protocol’s **health factor calculation** logic. Specifically, the contract used an outdated USDC pool balance when computing a user’s collateral health during a redemption, which caused the system to overestimate collateralization. In other words, the protocol incorrectly treated the attacker’s position as safe (over-collateralized) when it wasn’t, allowing them to bypass solvency checks and withdraw funds.

The attacker leveraged a large flash loan to inflate their collateral shares: after depositing only **200 USDC** of their own, they borrowed and deposited a significant amount of **USDC + staked ETH** via flash loan to boost their lending pool balance, then borrowed **\~60 stETH** against the artificially inflated collateral. Finally, by calling the vulnerable `redeemUnderlying` function, they withdrew all pledged assets (**stETH first, then USDC**) without triggering a health-factor failure—the check passed incorrectly because it still relied on the old pool balance (which included the soon-to-be-withdrawn funds). After repaying the flash loan, the attacker walked away with **\~60 stETH**.

### Self Transfers

[TheIdolsNFT](https://www.openzeppelin.com)’s yield mechanism tracked cumulative rewards per NFT in `rewardPerGod` and claimed amounts per user in `claimedSnapshots`. The `_beforeTokenTransfer` hook automatically claimed rewards for `sender` and `receiver`, resetting the sender’s `claimedSnapshots` to zero if they held no NFTs post-transfer. When `sender` and `receiver` were the same address holding one NFT, the receiver’s `claimedSnapshots` were reset before claiming, allowing them to reclaim already-distributed rewards. The attacker exploited this by repeatedly self-transferring a single NFT.

### Unsafe Storage Use

In March, [Synthetics Implemented Right (SIR) was exploited](https://defihacklabs.substack.com/p/sir-exploit-355k-loss-vulnerability) due to improper use of transient storage. SIR allows for the permissionless creation of leveraged trading vaults, each tied to a Uniswap pool used as a price oracle and issuing APE (leveraged) and TEA (LP) tokens.

The vulnerability was present in the vault’s `mint` flow. When depositing debt tokens, the vault swaps them for collateral and stores the Uniswap pool address in transient storage slot 1, later checking this slot to authorize the `uniswapV3SwapCallback`. Among other things, the callback is responsible for sending the input tokens to the Uniswap pool. However, at the end of the callback, the same slot was overwritten with the amount of `APE` tokens minted.

By initializing a vault with attacker-controlled tokens, the attacker manipulated the minted `APE` amount so that, when interpreted as an address, it pointed to a malicious contract. They then deployed code at that address and impersonated the Uniswap pool, bypassing the callback authorization and draining the vault by supplying all funds as swap inputs.

The exploit highlights the risks of reusing transient storage for multiple logical purposes within a single execution flow.

### Flawed Reward Systems

In August, BetterBank, a lending protocol on PulseChain, [was exploited for $5 million](https://x.com/Fried_rice/status/1960534610485633369) after an attacker abused its bonus-minting logic by bypassing tax payments using a self-created liquidity pool [\[1\]](https://rekt.news/betterbank-rekt).

BetterBank rewarded users with bonus ESTEEM tokens whenever FAVOR tokens are purchased. To prevent reward farming via repeated large-volume swaps, they imposed trading taxes intended to make such activity economically unprofitable. These taxes, however, were enforced only on liquidity pairs explicitly registered as “official”. Because PulseX allows anyone to create liquidity pools, the attacker deployed their own pool pairing FAVOR with a worthless token they controlled. Swaps through this pool incurred no taxes, bypassing the protocol’s primary economic safeguard.

With taxes effectively disabled, repeated large-volume swaps through the unregistered pool continuously triggered bonus minting with no cost, allowing the attacker to extract value from the protocol. No protocol invariants were technically violated as the exploit relied entirely on mismatch between reward eligibility and tax enforcement.

### Transaction Timing Attacks

In January, Alien Base Dex [lost around $22k](https://www.openzeppelin.com) in a classic **Sell-(Force) AddLiquidity-Buy** sandwich attack [\[1\]](https://app.blocksec.com/explorer/tx/base/0x77855f3a363f8a3301c612d34e794154a10560be98ed50d64ca0480675625df6) [\[2\]](https://app.blocksec.com/explorer/tx/eth/0x2a32fd400186eb7b32d405be008ea74f9f7c820824c11ea22177e0d4ab804188). The contract featured a `compound` function meant to collect fees from a liquidity pool and reinvest them. This function was permissionless; the tick range was determined by the caller, and there was no slippage protection (`amountMin = 0`).

The attacker began by selling flash-loaned ALB tokens, which drove down the ALB/WETH price. They then triggered the `compound` function, adding liquidity at this artificially low price. Following this, the attacker repurchased ALB with WETH, taking advantage of the increased liquidity at the lower price to end up with more ALB than they started with. Finally, the attacker converted these ALB tokens back into WETH in another pool to secure their profits.

In February, the contract at `0x2d70d62` was exploited via a multi-layer sandwich attack that abused missing slippage protection in its `depositBNB` function [\[1\]](https://bscscan.com/address/0xc011232f9891bf698c7dff8bff95d79ed9eb4e74) [\[2\]](https://x.com/TenArmorAlert/status/1888063017163624929). The function swapped WBNB for ADAcash without slippage, allowing an attacker to manipulate prices around the deposit.

The exploit was non-trivial because ADAcash is a fee-on-transfer token that charges a 15% transfer fee on each buy and sell, which would normally make a simple sandwich unprofitable. However, the protocol’s fee-handling logic introduced a second attack surface. Collected fees were accumulated by the token contract and, once a threshold was reached, automatically swapped without slippage protection: most fees were swapped for ADA, while roughly 13% were converted to WBNB and added as liquidity to the \`ADAcash/WBNB pool.

The attacker exploited this by effectively sandwiching both the user-facing swap and the internal fee swaps. They flash-loaned WBNB, bought ADAcash to raise its price (incurring the transfer fee), and simultaneously pushed up ADA’s price. They then triggered depositBNB, executing the first sandwich and further inflating ADAcash. When selling ADAcash back, each sell incurred another 15% fee and triggered the contract’s fee-swap logic. By splitting the sell into multiple transactions, the attacker repeatedly forced large, unprotected swaps from the fee pool, creating a second sandwich around the ADAcash to ADA conversions. Finally, they sold the accumulated ADA, repaid the flashloan, and kept the profit.

This incident shows that slippage protection must be applied consistently to all protocol-controlled swaps, not just user-facing ones.

### Protocol Misconfigurations

- Two weeks after the exploit on [Yearn’s yETH](https://www.openzeppelin.com), in mid-December, another [incident](https://github.com/banteg/iearn-2025-12-investigation/blob/master/technical-writeup.md) happened in a [legacy vault](https://etherscan.io/address/0x73a052500105205d34daf004eab301916da8190f). The yTUSD vault was misconfigured to track the wrong external lender: its underlying token was TUSD, but the `fulcrum` address pointed to iSUSD (underlying sUSD), which broke the vault’s accounting model. It allowed an attacker to donate iSUSD to inflate the vault value, then use `withdraw` and `rebalance()` to flush out other holdings while leaving sUSD behind, which the vault did not price or track. Once the accounted value was forced down to dust, the attacker could mint an enormous amount of yTUSD shares from a small TUSD deposit. Those shares were then used as swap input against Curve’s pool for valuable yDAI and yUSDC and impact the oracle. Although the attacker’s profit was relatively small (\~$250k) compared with the previous exploit, the incident is another example of how legacy code + misconfiguration can compose into a real exploit.

### Unset Initialization Flags

[A critical vulnerability was found](https://www.openzeppelin.com) in the [`BaseCustomAccounting` hook](https://github.com/OpenZeppelin/uniswap-hooks/blob/f051c147dbf296b2b854de92970905a880cd1d51/src/base/BaseCustomAccounting.sol#L35) of the [Uniswap Hooks](https://github.com/OpenZeppelin/uniswap-hooks) library. This hook is designed to fully control liquidity in its associated pool, ensuring that all liquidity modifications pass through it. Therefore, it must be permanently linked to a single pool. Otherwise, liquidity could become inaccessible.

However, due to an asymmetry in pool-hook awareness, any valid hook address can be attached to any pool unless explicitly rejected by the hook itself. The `BaseCustomAccounting` hook lacked safeguards against reinitialization, allowing an attacker to redirect it from a victim’s pool to a maliciously created Uniswap pool. This effectively locked the victim pool’s liquidity, preventing access to funds.

The fix ensures that once directed to a pool, a hook that inherits `BaseCustomAccounting` will not be able to be reinitialized and point to another pool.

In February, [an unverified contract was exploited](https://x.com/TenArmorAlert/status/1890776122918309932) after being deployed without initialization. Once enough funds had accumulated, the attacker initialized the contract, set themselves as owner, and drained the funds via `withdrawFees`.

### Beacon Chain Specific

A [bug was identified](https://hackmd.io/@rNlehaDSRBydbF_i_McDcw/ByyodLJ9ex) in EigenLayer’s EigenPod implementation-a logic flaw in handling partial withdrawals allowed a validator to artificially inflate their recorded stake. This issue exploited the key difference between a validator’s `actual_balance` and `effective_balance` on the beacon chain.

The `actual_balance` of a validator is the total amount of ETH currently staked on the validator. It changes when the beacon chain processes balance updates (e.g., when withdrawals are processed, rewards accrue, or penalties are applied). `effective_balance` serves as an approximation of the `actual_balance`, rounded down to the highest multiple of 1 ETH (given current beacon chain configuration). For example, an `actual_balance` of 100.75 ETH yields an `effective_balance` of 100 ETH.

The `effective_balance` is [only updated once per epoch](https://github.com/ethereum/consensus-specs/blob/master/specs/electra/beacon-chain.md?plain=1#L877) and is utilized by EigenLayer in the `verifyWithdrawalCredentials` function. The `actual_balance` is updated immediately upon deposit and is utilized by EigenLayer in the `verifyCheckpointProofs` function. Due to this discrepancy, a malicious user could have their shares calculated using stale effective balance data and thus receive more ETH shares than the capital they actually staked. Below is a step-by-step explanation of the issue:

1. Alice has a validator with 100 ETH effective balance and requests a 68 ETH partial withdrawal, leaving 32 ETH on the validator.
2. After the withdrawal queue clears, 68 ETH is swept to Alice’s pod, where she immediately completes a checkpoint (via `verifyCheckpointProofs`) and mints 68 ETH in shares.
3. Before the epoch ends, the validator’s **effective balance is still 100 ETH**, since effective balances only update at epoch boundaries.
4. Alice calls `verifyWithdrawalProofs`, which uses the **stale effective balance**, minting 100 ETH in shares, resulting in **168 ETH in shares backed by only 100 ETH**.

A critical bug found in an OpenZeppelin audit stemmed from an incorrect assumption about the beacon chain’s [`state.pending_deposits` list](https://github.com/ethereum/consensus-specs/blob/master/specs/electra/beacon-chain.md?plain=1#L986). Deposits are appended and later batch-processed; once processed, the validator’s [`actual_balance` is updated](https://github.com/ethereum/consensus-specs/blob/master/specs/electra/beacon-chain.md?plain=1#L1028).

The codebase assumed that `pending_deposits` is strictly ordered by deposit slot. It treated the slot of the first pending deposit as a cutoff: if a deposit was issued at slot X and the first pending deposit was at slot Y, then X \< Y was taken to mean the deposit at X must already be processed and could be accounted for in the smart contracts. The smart contract utilized [beacon block root](https://eips.ethereum.org/EIPS/eip-4788) and merkle proofs to confirm the first depending deposit slot Y existed on Beacon Chain and then compared against deposit slot X to verify if X was processed or not.

However, the Electra spec’s [`process_pending_deposits` function](https://github.com/ethereum/consensus-specs/blob/01454a2afc442a32644df45deb8f81687e461785/specs/electra/beacon-chain.md#new-process_pending_deposits) explicitly allows pending deposits for exiting validators to be postponed to the end of the queue each epoch, breaking strict ordering by slot.

This invalidated the cutoff logic and led to incorrect accounting (under- or double-counting) and even temporary or permanent processing halts. The design was later changed to avoid relying on queue slot ordering.

### Rust Specific

An audit of the Stylus crypto library [uncovered a shift overflow bug](https://www.openzeppelin.com) stemming from Rust’s release-mode behavior, where shift amounts are masked modulo the bit width. In the `<<=` and `>>=` implementations for `Uint<N>`, a shift by a multiple of 64 could result in unintended no-op shifts instead of zeroing limbs. This produced incorrect arithmetic results when shifting by 64 \* x bits. The issue illustrates subtle semantic differences between Rust, Solidity, and Go that can lead to critical arithmetic bugs in low-level libraries.

During an OpenZeppelin audit of ZKsync OS, [a critical issue was identified](https://www.openzeppelin.com) that arose from the use of Rust’s architecture-dependent `usize` type, which spans either 32 or 64 bits, depending on the computer architecture it runs on. Since ZKsync OS executes transactions in a 64-bit environment (“forward mode”) and replays them on a 32-bit RISC-V prover (“proof mode”), `usize` arithmetic could lead to non-deterministic execution paths. This is problematic since the execution in both environments should be identical.

Multiple cases were found where crafted calldata caused operations to proceed further on the 64-bit sequencer but fail earlier on the 32-bit prover. Although both executions reverted, the failure occurred at different points, breaking determinism and preventing L1 proof verification.

Similar discrepancies appeared in memory-size rounding logic. In the bootloader’s transaction handling, rounding transaction sizes to `USIZE_SIZE` could overflow on 32-bit systems and wrap to zero in release builds, while behaving correctly on 64-bit targets, leading to different execution paths.

In systems requiring deterministic execution across architectures, Rust’s `usize` or (or similar types like `size_t` in C++) must not be used for arithmetic. Fixed-width integers (`u32`, `u64`) should be used instead to ensure consistent behavior between execution and proof generation.

### Stellar

- The OpenZeppelin team uncovered a [medium-severity DoS issue](https://www.openzeppelin.com/news/stellar-contracts-library-0.1.0-audit#medium-severity) in the Stellar Contracts fungible token implementation. On Stellar, contract data in temporary storage has a Time to Live (TTL) that must be periodically extended. The approval mechanism allowed users to specify approval durations, but attempting to extend the TTL beyond Stellar’s maximum (1 year) caused the transaction to panic and revert, preventing any long-term approvals.

### Missing Access Control

In February, [a MEV bot was exploited](https://www.openzeppelin.com) due to missing access control on its `fallback` function. This allowed an attacker to supply arbitrary call parameters and drain all WETH within the contract.

In May, [KiloEx was exploited](https://medium.com/@KiloEx/kiloex-security-incident-root-cause-analysis-post-mortem-3d899caac08c) for approximately $7.5 million due to missing access control in a relayed execution path that ultimately governed oracle price updates.

The root cause was a contract inheriting OpenZeppelin’s `MinimalForwarderUpgradeable` (an experimental library that was not production-ready) without restricting its `execute` function, leaving the top-level entry point effectively permissionless. Several downstream contracts relied on the assumption that calls reaching them had already been authorized, but no component in the chain actually enforced that requirement.

By abusing this broken chain of trust, the attacker relayed unauthorized calls to the price update logic, forcing oracle prices to extreme values. They first set prices artificially low to open leveraged positions, then immediately raised prices and closed the positions for profit.

In June, [MetaPool was exploited](https://www.openzeppelin.com) due to improperly inheriting `ERC4626Upgradeable` and handling access control. In mpETH, both the public `deposit` function and the internal `_deposit` function were overridden. As part of a design change, the receipt check was moved out of `_deposit` and into `deposit`, allowing token transfers and additional logic to occur outside the internal function.

However, the team overlooked the fact that the `mint` function also relies on `_deposit` for enforcing the receipt check. Since `mint` was not overridden, it called the new `_deposit` implementation without any receipt verification, allowing mpETH to be minted without supplying assets.

In October, [Typus Finance](https://medium.com/@TypusFinance/typus-finance-tlp-oracle-exploit-post-mortem-report-response-plan-ce2d0800808b) was exploited via unaudited functionality that allowed oracle prices to be updated without any access control. Since swap rates were oracle-driven, the attacker set malicious prices and drained the pools with minimal input tokens.

In July, the [SuperRare staking contract](https://blog.solidityscan.com/superrare-hack-analysis-488d544d89e0) was exploited, allowing an attacker to steal **11.9M `RARE`** tokens(\~**$730K**). The root cause was a broken access control check on the `updateMerkleRoot` function, which incorrectly allowed arbitrary callers to update the Merkle root. Specifically, the authorization logic used an invalid condition:

`require((msg.sender != owner() || msg.sender != address(0xc2F394a45e994bc81EfF678bDE9172e10f7c8ddc)), "Not Authorized");`

Since the check combined `!=` with an `OR`, it evaluated to `true` for almost all callers, effectively disabling the authorization gate. This allowed the attacker to replace the Merkle root and illegitimately claim staking rewards.

### Compromised Private Keys

- In January, approximately $73 million [were drained](https://www.halborn.com/blog/post/explained-the-phemex-hack-january-2025) from the Phemex centralized exchange hot wallets, likely due to a private key compromise that drained funds sixteen different blockchains.
- Similar incidents have happened to [Moby Trade in January](https://rekt.news/mobytrade-rekt), [Zoth in March](https://rekt.news/zoth-rekt), [ZKsync in April](https://x.com/zksync/status/1912141160744632737), [HAI token in June](https://x.com/hackenclub/status/1936487412101742852), [CoinDCX in July](https://rekt.news/coindcx-rekt), [Woo X in July](https://rekt.news/woox-rekt) and [BtcTurk in August](https://rekt.news/btcturk-rekt).

### Supply Chain Attacks

One of the [largest supply chain attacks](https://www.paloaltonetworks.com/blog/cloud-security/npm-supply-chain-attack/) in the history of NodeJS happened in September, when widely used packages [chalk](https://www.npmjs.com/package/chalk), [debug](https://www.npmjs.com/package/debug) and 16 others were compromised after attacker gained control of developer’s npm account, enabling them to publish malicious code. Upon publishing, the attacker inserted malicious payload designed specifically for theft of cryptocurrency by targetting wallet extensions in browsers.

Collectively, these packages get more than 2 billion downloads **every week**, thus magnifying the capability of this attack. Luckily, these packages were detected soon enough and attacker’s were only able to steal cryptocurrency worth less than 50 dollars.

In April, a malicious solidity extension on visual studio code, [cursor.ai](http://cursor.ai/), and openvsx marketplace popped up that was similar to the original [Ethereum Solidity Language for Visual Studio Code](https://marketplace.visualstudio.com/items?itemName=JuanBlanco.solidity) by author Juan Blanco which managed to showcase [fake downloads and fake reviews](https://x.com/juanfranblanco/status/1914225236809044029). This [attack](https://x.com/0xzak/status/1955265807807545763?s=20) led to blockchain developers losing more than $500K.

In December, a new [malicious version of the Trust Wallet browser extension](https://trustwallet.com/blog/announcements/trust-wallet-browser-extension-v268-incident-community-update) (v2.68) was published using a CWS key that got exposed through [`Sha1-Hulud` attack](https://snyk.io/blog/sha1-hulud-npm-supply-chain-incident/), an industry wide supply chain attack, on one of the developer’s machine. Around 2520 wallet users that updated to this malicious version were affected with $8.5M drained by the attackers.

### Others

In November, MegaETH, an Ethereum Layer 2 preparing for its mainnet launch, experienced a major disruption during a pre-deposit campaign that resulted in **$500 million** of deposits accumulated under operationally chaotic conditions, despite no smart contract vulnerabilities or loss of funds [\[1\]](https://rekt.news/megaoops), [\[2\]](https://x.com/megaeth/status/1993395774164488361).

The pre-deposit system combined a KYC-gated frontend using Echo’s **Sonar** service, an on-chain pre-deposit contract governed by a 4/6 **Safe multisig**, and a fixed deposit cap initially set at **$250 million**. Shortly after launch, deposits failed due to a misconfigured `SaleUUID` parameter that did not match Sonar’s expected identifier. Fixing this required coordinating a multisig transaction, delaying recovery while users repeatedly retried failed deposit attempts.

At the same time, Sonar’s infrastructure experienced rate-limiting issues under heavy load, preventing many users from completing deposits. Once these issues were resolved, the deposit window reopened automatically at an unannounced time, causing the **$250 million** cap to be filled within minutes by users repeatedly refreshing the interface. During this brief window, individual deposits of **$40 million** and **$25.5 million** were recorded, deviating from the expected distribution.

In response, the team announced plans to raise the cap to **$1 billion** at a later time. To prepare, the required multisig signatures were gathered in advance. However, once the required threshold of signatures was reached, the transaction became executable by anyone, as per **Safe**’s design. Someone who noticed that the signature threshold had been reached executed the transaction early, lifting the cap ahead of the announced schedule. The unexpected cap increase triggered another surge of deposits further amplifying the imbalance in participation. As deposits rapidly accumulated beyond the originally intended limits, the team attempted to reassert control by lowering the cap. An initial attempt to cap deposits at **$400 million** failed because total deposits had already exceeded that amount by the time the team’s transaction was processed. A subsequent adjustment set the cap at **$500 million**, at which point deposits stabilized. Shortly after, MegaETH abandoned the planned **$1 billion** extension and announced that users would be offered a withdrawal option, which fewer than **5%** of participants ultimately chose to use.

In the end, the pre-deposit achieved its intended distribution outcome in aggregate, yet the sequence of pauses, misconfigurations, and premature parameter changes turned what was designed to be a predictable first-come-first-served process into a chaotic and uneven experience for participants.

In December, OpenZeppelin published [A Developer’s Guide to FHEVM Security](https://www.openzeppelin.com/news/a-developers-guide-to-fhevm-security), covering how Zama’s FHEVM on-chain library works and highlighting common pitfalls and vulnerability patterns. These include handling underflows/overflows without using branching, accidentally granting decryption rights to unauthorized arbitrary addresses, as well as correctly disclosing information in the context of blockchain reorgs—along with straightforward mitigations for each.

DPRK has been [observed using sophisticated Etherhiding](https://cloud.google.com/blog/topics/threat-intelligence/dprk-adopts-etherhiding), a technique where attackers embed malicious code (often JavaScript payloads) inside smart contracts on public blockchains such as Ethereum, BSC, and Polygon. Payloads are stored in contract storage or disguised as legitimate ERC-20 tokens, then retrieved in multi-stage off-chain attacks. Compared to traditional servers, this approach offers attackers several advantages:

1. **High availability**: On-chain malware cannot be taken down, even by law enforcement, and is easily retrievable via RPC calls.
2. **Reduced detection**: Many existing detection systems rely on domain reputation and are not designed to identify Etherhiding.
3. **Low cost**: Updating payloads is cheap, and storage and retrieval typically fall within the free tiers of most RPC providers.

The following article performs an [analysis of address poisoning scams](https://www.chainalysis.com/blog/address-poisoning-scam/?utm_source=substack&utm_medium=email), in which attackers send small transactions from spoofed addresses that closely resemble a victim’s legitimate counterparties. The goal is to trick users into copying and pasting the attacker’s address for future transfers. These scams are particularly effective on low-fee blockchains, where attackers can cheaply target many victims at scale, and have [recently been observed on TRON](https://www.trmlabs.com/resources/blog/understanding-address-poisoning-on-the-tron-blockchain?utm_source=substack&utm_medium=email).

Similar to previous years, 2025 has been rich in valuable research, innovative vulnerabilities, and creative exploits.

*It is important to emphasise that the intent behind the article is not to criticise or blame the affected projects, but rather provide objective overviews that serve as educational material for the community to learn from and better protect projects in the future.*

Ready to secure your code?
