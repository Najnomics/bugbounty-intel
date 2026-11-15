# 📉 $16M Lost Across 5 Web3 Exploits

- **Source URL:** https://blocksec.com/blog/web3-security-dxsale-squidrouter-more
- **Fetched:** 2026-11-15
- **Channel:** @defendor_eng
- **Telegram message:** https://t.me/defendor_eng/1677 (id 1677)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
During the past week (2026/05/25 - 2026/05/31), BlockSec identified multiple attack incidents across several blockchain ecosystems. The table below lists 5 notable incidents with total estimated losses of approximately $16M.

| **Date** | **Incident** | **Type** | **Estimated Loss** | 
|---|---|---|---|
| 2026/05/27 | **SquidRouterModule** | Improper Input Validation | \~$3.2M | 
| 2026/05/29 | Stake DAO | Compromised Private Key | \~$91K\* | 
| 2026/05/29 | **DxSale** | Incorrect Business Logic & Key Compromise | \~$7.3M | 
| 2026/05/30 | Gravity Bridge | Vulnerable Off-chain Signing Process | \~$5.4M | 
| 2026/05/30 | Alephium | Vulnerable Off-chain Signing Process | \~$300K\* | 

**\*Additional notes:**

- In the **Stake DAO** incident, the attacker compromised the deployer's private key and used it to reconfigure the LayerZero v2 OFT peer on the `vsdCRV` contract on Arbitrum, enabling the minting of 5.4 trillion `vsdCRV`. Due to limited DEX liquidity, only approximately $91K was cashed out before the pools dried up.
- In the **Alephium** incident, beyond the approximately $300K in drained bridge custody assets (`USDT`, `USDC`, `WETH`, `WBTC` on Ethereum and `USDT`, `WBNB` on BNB Chain), the attacker also minted 13.7M unbacked `wALPH` on Ethereum. The bridge was shut down, preventing the attacker from redeeming or bridging these tokens back through the Alephium bridge.

Two incidents are selected for in-depth analysis:

- **SquidRouterModule**: Much like the CrossCurveFi exploit, it repeated the same class of integration mistake, showing how forking cross-chain logic without deep understanding and rigorous security review can quickly turn inherited complexity into inherited risk.
- **DxSale**: Its long attack timeline shows that unexploited legacy contracts are not necessarily safe, and that protocols must continuously monitor on-chain and off-chain activity, minimize privileged access, and never mistake years of silence for proof of security.

Best Security Auditor for Web3

Validate design, code, and business logic before launch

## Weekly Highlight: DxSale

*This incident was selected as the weekly highlight because the combination of a years-old unpatched locker contract and a compromised deployer key illustrates a recurring pattern: protocols that treat deployment-time code as permanently safe, without continuous auditing or privilege rotation, carry hidden risk that can be weaponized at any time.*

On May 29, 2026, DxSale, a token sale and liquidity locking platform on BNB Chain, was exploited [\[1\]](https://x.com/dxsale/status/2060373478885191994) for approximately $7.3M. The token withdrawal function contained three missing state updates that allowed any user with a valid lock position to repeatedly withdraw and drain the entire shared pool, with no owner privileges required. A separate compromise of the DxSale deployer key via EIP-7702 delegation was not a prerequisite for the exploit, but amplified the attacker's efficiency by enabling fee manipulation and blocking other users from creating new locks.

### Background

DxSale is a token sale and liquidity locking platform on BNB Chain. Its DxLock component allows project developers to lock LP tokens in time-locked vaults, providing assurance to investors that liquidity cannot be rug-pulled.

The core locking mechanism operates as follows: a user deposits tokens into the locker contract, creating a lock record indexed by the combination of the caller's address and a token ID. Each record stores whether the lock exists, whether tokens are currently locked, the locked amount, the unlock timestamp, and the token address. When the lock period expires, the user calls `unlockToken(tokenId)` to withdraw their tokens.

Because the locker holds tokens for many users simultaneously in a shared balance, individual allocations must be tracked accurately through separate lock records. The security of the entire pool depends on each withdrawal correctly validating the caller's own record and updating it after the transfer.

### Vulnerability Analysis

The `unlockToken` function in the buggy contract ([0xeb3a...e449](https://bscscan.com/address/0xeb3a9c56d963b971d320f889be2fb8b59853e449#code)) contained three compounding defects, each a missing state update or check:

```
function unlockToken(uint256 tokenId) public nonPayable {
    require(_increaseLockTime[msg.sender][tokenId].field0_0_0);  // locker exists
    require(_increaseLockTime[msg.sender][tokenId].field0_1_1);  // tokens are locked
    require(_increaseLockTime[msg.sender][tokenId].field2);       // amount > 0
    if (block.timestamp > _increaseLockTime[msg.sender][tokenId].field3) {
        _increaseLockTime[msg.sender][tokenId].field0_1_1 = 0;
    }
    v0, v1 = _increaseLockTime[msg.sender][tokenId].field5_0_19.balanceOf(this);
    require(v1 >= _increaseLockTime[msg.sender][tokenId].field2);
    v2, v3 = _increaseLockTime[msg.sender][tokenId].field5_0_19.transfer(
        msg.sender, _increaseLockTime[msg.sender][tokenId].field2
    );
}
```
1. **No lock-period enforcement.** The lock period was guarded by an `if` statement rather than a `require`. When called before the unlock timestamp, the function simply skipped clearing the locked flag instead of reverting. This meant tokens could be withdrawn at any time, regardless of the lock period.
2. **Locked amount never zeroed.** After transferring tokens to the caller, the function did not zero `field2` (the locked amount). Every subsequent call read the same original value and withdrew the same amount again, creating an infinite withdrawal loop.
3. **Shared-balance check instead of individual allocation.** The `balanceOf(this)` call verified the contract's total token balance rather than the caller's individual allocation. A caller with a small lock position could drain the entire shared pool as long as the contract still held sufficient total tokens.

Together, these three missing state updates removed every exit condition from the function: the call never reverted prematurely, the withdrawal amount never decreased, and the balance check never blocked until the contract was fully emptied. The bug was exploitable by any user who created a lock position; no owner privileges were required for the core drain.

### Attack Analysis

The DxSale deployer account (`0x47bacf93`), operating via EIP-7702 delegation, had exhibited anomalous activity since 2026-04-15, including mass ownership transfers, fee changes, and LP unlock operations across multiple DxSale contracts. On 2026-05-26, the deployer transferred ownership of the victim locker ([0xeb3a...e449](https://bscscan.com/address/0xeb3a9c56d963b971d320f889be2fb8b59853e449)) to the attacker contract ([0xc457...fa69](https://bscscan.com/address/0xc4574ddef299e7e563971e200433e592eeaafa69)). Two days later, the attacker executed a five-step drain.

The following analysis is based on a representative transaction [0x437b26...c1b303](https://app.blocksec.com/phalcon/explorer/tx/bsc/0x437b26887ba03c08b7541a86e8eeda5e92a9059244fcf814c721dc13f2c1b303).

- Step 1: The attacker swapped `BNB` for `BNBC` tokens on PancakeSwap and provided liquidity to create a new `Cake-LP (BNBC/WBNB)` pair, receiving approximately 0.323 LP tokens.
- Step 2: Using the owner privileges obtained via the prior ownership transfer, the attacker called `changeFees(1)` to set the lock creation fee to 1 wei, then called `createLocker` to deposit the approximately 0.323 LP tokens into a new lock position (tokenId=131). Immediately after, the attacker called `changeFees(10^36)` to raise the fee to an astronomical value, preventing other users from creating new locks.
- Step 3: The attacker called the exploit function (`0x11b432b4`), which orchestrated repeated `unlockToken` calls in a single transaction. Across multiple transactions, the attacker systematically drained the locker: [0x437b26...c1b303](https://app.blocksec.com/phalcon/explorer/tx/bsc/0x437b26887ba03c08b7541a86e8eeda5e92a9059244fcf814c721dc13f2c1b303) drained 161.4 LP tokens via tokenId=131, [0x82f541...a9fa73](https://app.blocksec.com/phalcon/explorer/tx/bsc/0x82f5418835642f6d8f29b0686f39b7ca73023748d3c2c7d1827418ce51a9fa73) and [0x5dd61f...4298aa](https://app.blocksec.com/phalcon/explorer/tx/bsc/0x5dd61f4301101cb55a7f89eea3ce98a3bcc6f0f55878c26ab16665a01e4298aa) drained additional lock positions, and [0xac8f5e...d36df9](https://app.blocksec.com/phalcon/explorer/tx/bsc/0xac8f5ed6cac1e6c6d6e96bad34f5211c8ae23cf05866b2531f3f3e63bcd36df9) drained 260.3 LP tokens via tokenId=319 across 478 calls.
- Step 4: The attacker called `removeLiquidity` on PancakeSwap to break the drained LP tokens back into their underlying tokens (`BNBC` and `WBNB`).
- Step 5: The attacker swapped the underlying tokens for `WBNB` and `BUSD` via PancakeSwap and transferred proceeds to external addresses. BSCScan recorded 123,447 transactions over 4 days (2026-05-28 to 05-31) for this attacker contract.

### Conclusion

The root cause of this incident is the three missing state updates in `unlockToken`. Each has a direct fix: enforce the lock period with `require` rather than `if`, zero the locked amount after each withdrawal, and check the caller's individual allocation rather than the contract's total balance. These defects alone were sufficient for exploitation; any user who created a lock position could drain the entire shared pool through repeated calls, with no owner privileges required.

The prior compromise of the DxSale deployer via EIP-7702 delegation was not a prerequisite for the exploit, but it amplified the attacker's efficiency. By transferring ownership and manipulating fees, the attacker created near-zero-cost lock positions and blocked legitimate users from creating competing locks. On the operational side, protocols must continuously audit legacy contracts, especially those holding user funds, and avoid single-key custody of admin functions. Years of incident-free operation do not validate the security of unaudited code.

### References

- [\[1\]](https://x.com/dxsale/status/2060373478885191994) DxSale announcement

## More Incidents This Week

## SquidRouterModule

On May 27, 2026, an unknown contract named SquidRouterModule was exploited [\[1\]](https://x.com/Phalcon_xyz/status/2058899283634692200) on Ethereum due to improper input validation, resulting in approximately $3.2M in losses. The root cause was a misuse of the Axelar Bridge integration, similar to the earlier CrossCurveFi attack pattern [\[2\]](https://x.com/Phalcon_xyz/status/2018167679300104449). The contract did not properly validate cross-chain messages through the Axelar Gateway, allowing the attacker to forge payloads that authorized and swapped victims' tokens into pre-constructed malicious pools. A separate attacker address that had deployed the fake token and seeded the pools later removed liquidity to extract the real assets. This attack affected 86 Safe wallets. Despite its name, the SquidRouterModule was not built, deployed, or operated by the Squid protocol team [\[3\]](https://x.com/squidrouter/status/2058890710611276238).

### Background

The contract is a cross-chain exchange service module designed for the Safe wallet, built on the Axelar cross-chain protocol. The contract provides the `expressExecuteWithToken` function, supporting early execution of transactions before cross-chain message confirmation. Users must pre-authorize the contract's APPROVE and SWAP permissions on their Safe wallet before using this service. When `expressExecuteWithToken` is called, the contract decodes the operation instructions in the payload and calls the Safe wallet's `execTransactionFromModule` to execute token authorization and exchange operations.

### Vulnerability Analysis

The `_executeWithToken` function in the vulnerable contract ([0x1f1d...23ca](https://etherscan.io/address/0x1f1d37a3bf840e35c6a860c7c2da71fe555123ca#code)) only checked whether `srcAddress` equaled the `squidRouter` constant. However, `srcAddress` is a caller-supplied parameter, while `squidRouter` is an immutable string that anyone can read from the contract. This allowed the attacker to trivially bypass the check and execute the `_processPayload` function with arbitrary payload content.

In contrast, the legitimate Squid Router's `executeWithToken` function calls `gateway.validateContractCallAndMint()` and reverts with `NotApprovedByGateway()` if the Axelar validator network has not confirmed the transaction.

The vulnerable contract did not enforce any such gateway authorization on the `expressExecuteWithToken` path. Combined with the APPROVE and SWAP permissions that Safe wallet users had pre-authorized to the module, forged payloads could directly operate on victims' funds.

### Attack Analysis

The following analysis is based on the transaction [0xd29d1c...3bb854](https://app.blocksec.com/phalcon/explorer/tx/eth/0xd29d1c8d9a1b424d4e0f472bd7b4a994028d35e9737c591eae51d917543bb854).

Before the attack, a separate attacker address deployed a fake token ([`0xe6Ff...3512`](https://etherscan.io/address/0xe6ff0fe017d09d690493dec0f0f55e8f9cdc3512)) and created multiple Uniswap V3 pools, each pairing the fake token against a different valuable token (e.g., `USDC`, `ENA`, `USDT`), seeding the pools with fake token liquidity.


- Step 1: The attacker forged malicious calldata and called the vulnerable contract's `expressExecuteWithToken` function, using the known `squidRouter` address as the `sourceAddress` to bypass the validation check. Through the APPROVE and SWAP permissions that the victim had pre-authorized to the module, the forged payload forced token approvals from the victim's Safe wallet to the Uniswap pool.
- Step 2: Using these forced approvals, the payload swapped the victim's tokens for the worthless fake token through the corresponding malicious pool.

The attacker repeated this method across multiple transactions, targeting a total of 86 Safe wallets that had authorized the vulnerable contract. The separate attacker address that had deployed the fake token and seeded the pools subsequently removed liquidity to extract the real assets, ultimately profiting approximately $3.2M.

### Conclusion

This incident was caused by improper input validation in the cross-chain message handling path. The only security check relied on a caller-controllable parameter compared against a publicly readable constant, providing no real protection. Combined with pre-authorized APPROVE and SWAP permissions from Safe wallet users, the attacker could forge cross-chain messages and steal user funds.

The incident is similar to the CrossCurveFi exploit [\[2\]](https://x.com/Phalcon_xyz/status/2018167679300104449): both involve Axelar Bridge integrations that failed to properly validate incoming cross-chain messages. When integrating cross-chain messaging infrastructure, the destination contract must independently validate message authenticity through the bridge's authorization mechanism. Skipping this validation and relying on attacker-controllable inputs turns the integration into an open attack surface.

### References

- [\[1\]](https://x.com/Phalcon_xyz/status/2058899283634692200) Phalcon Alert: SquidRouterModule exploit
- [\[2\]](https://x.com/Phalcon_xyz/status/2018167679300104449) Phalcon Alert: CrossCurveFi attack pattern
- [\[3\]](https://x.com/squidrouter/status/2058890710611276238) Squid Router clarification

## About BlockSec

BlockSec is a full-stack blockchain security and crypto compliance provider. We build products and services that help customers to perform code audit (including smart contracts, blockchain and wallets), intercept attacks in real time, analyze incidents, trace illicit funds, and meet AML/CFT obligations, across the full lifecycle of protocols and platforms.

BlockSec has published multiple blockchain security papers in prestigious conferences, reported several zero-day attacks of DeFi applications, blocked multiple hacks to rescue more than 20 million dollars, and secured billions of cryptocurrencies.

- Official website: [https://blocksec.com/](https://blocksec.com/)
- Official Twitter account: [https://twitter.com/BlockSecTeam](https://twitter.com/BlockSecTeam)
- 🔗 [BlockSec Auditing Service](https://blocksec.com/audit) : [Submit a request](https://blocksec.com/expert-contact?service=codeAuditingService)
- 🔗 [Phalcon Security APP](https://blocksec.com/phalcon/security): [Book a demo](https://blocksec.com/expert-contact)
- 🔗 [Phalcon Compliance](https://blocksec.com/phalcon/compliance)
