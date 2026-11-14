# 🔬 Analysis: Dormant MakerDAO Keeper Drained of 200 ETH

- **Source URL:** https://www.certik.com/blog/makerdao-legacy-auction-keeper-incident-analysis
- **Fetched:** 2026-11-14
- **Channel:** @defendor_eng
- **Telegram message:** https://t.me/defendor_eng/2209 (id 2209)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
## Incident Summary

On October 6, 2026, at 06:13:11 UTC, an attacker [drained (opens in a new tab)](https://etherscan.io/tx/0xbb6940f7c2a1e68cafbae7bb9b94d09af9af06ec3a114f6996f2cab993f3a88c) 200 ETH ($542,982 at the time of the exploit) of ETH-A collateral from a legacy auction-keeper contract on Ethereum mainnet.
The 200 ETH came from four 50 ETH lots that the keeper won with zero bids during MakerDAO's "Black Thursday" liquidations in March 2020 and never settled. An unauthenticated function on the keeper let the attacker give a contract it controlled full delegation over the keeper's MakerDAO Vat account. In a single transaction, the attacker settled the old auctions and withdrew the collateral.

## Key Transactions (Times in UTC)

| Timestamp | Transaction / Explanation | 
|---|---|
| 2026-10-06 05:57:23 UTC | [0xd4c0b18a058e7f0a12855f30174f4cb1e973c15c886063deab97e1a21f048ac6 (opens in a new tab)](https://etherscan.io/tx/0xd4c0b18a058e7f0a12855f30174f4cb1e973c15c886063deab97e1a21f048ac6): Funding. Tornado Cash withdrawal of 0.1 ETH. This was the account's only funding. | 
| 2026-10-06 06:12:11 UTC | [0x4a587af4213cc345c4c109fbf5fec46f9643183f91a9edf60305380f31ad1167 (opens in a new tab)](https://etherscan.io/tx/0x4a587af4213cc345c4c109fbf5fec46f9643183f91a9edf60305380f31ad1167): Deployment of the attack contract that was used in the exploit. | 
| 2026-10-06 06:13:11 UTC | [0xbb6940f7c2a1e68cafbae7bb9b94d09af9af06ec3a114f6996f2cab993f3a88c (opens in a new tab)](https://etherscan.io/tx/0xbb6940f7c2a1e68cafbae7bb9b94d09af9af06ec3a114f6996f2cab993f3a88c): Exploit transaction. The attack contract obtained Vat delegation through keeper function 0x8804d1de, settled auctions 1457–1460, and sent 200 ETH to the attacker EOA. | 
| 2026-10-06 06:19:35 UTC | [0xb8ecff9c129d8d9331c85558eaeddff29a38c4c16b71a40986acbf8f6febefeb (opens in a new tab)](https://etherscan.io/tx/0xb8ecff9c129d8d9331c85558eaeddff29a38c4c16b71a40986acbf8f6febefeb): First of nine 10 ETH deposits into the Tornado Cash router. | 

## Key Addresses

## Attack Flow

1. **Module deployment.** The exploit transaction began with the attack contract creating an adapter module at 0xf09a13072Ed939B79Bc25B66AA3a836ea6DCC170. The constructor received: the Flipper, Vat, ETH-A GemJoin, ilk, WETH, the payout address, and the four auction IDs.
2. **Delegation.** The attack contract called keeper function 0x8804d1de and passed the newly created adapater at 0xf09. The keeper then called drip() and vat() on the module, checked whether it had already delegated to it via Vat.can(), and called Vat.hope(). This gave the module unrestricted authority over the keeper's Vat account.
3. **Callback.** The keeper then called the attacker's join() function, which handed control to attacker-written code while the new delegation was active.
4. **Settlement.** Inside the callback, the module called deal(id) on the retired ETH-A Flipper for auctions 1457, 1458, 1459 and 1460. The keeper had originally won each 50 ETH lot with a zero bid in March 2020 but never settled. Settling the auctions credited 200 ETH of ETH-A collateral to the keeper's Vat account.
5. **Extraction.** The module read the keeper's collateral balance and used its delegation to flux() all 200 ETH from the keeper's Vat account to itself. It then exited the collateral through the ETH-A GemJoin as 200 WETH and forwarded the WETH to the attack contract.

## Vulnerability

The root cause was a missing access control on function 0x8804d1de in keeper implementation 0x68399ed8aa33C5b43F863EE6782de492006A5546. Every other privileged function in the contract, including the keeper's hope, flux and move wrappers, runs a ds-auth check first and reverts with ds-auth-unauthorized for unauthorized callers. Function 0x8804d1de accepts any address as an adapter, calls Vat.hope on that address if the keeper has not already delegated to it, and then calls join() on the same address. In the Vat, hope gives the delegated address full control over the account's collateral and internal DAI. Because the keeper then called join(), the attacker's module ran its own code while that authority was active. The function never calls nope, so the delegation remained in place after the transaction. The keeper's four unsettled 2020 lots made the flaw profitable. Anyone can call deal on an auction.

## Fund Flow

The attacker received the full 200 ETH directly in the exploit [transaction (opens in a new tab)](https://etherscan.io/tx/0xbb6940f7c2a1e68cafbae7bb9b94d09af9af06ec3a114f6996f2cab993f3a88c).
At 06:19:35 UTC, six minutes later, the attacker began sending the funds to Tornado Cash in 20 x 10 ETH deposits.

To keep up to date on the latest incident alerts and statistics, follow [@certikalert (opens in a new tab)](https://x.com/CertiKAlert) on X, explore our [incident dashboard](https://www.certik.com/certik-report/dashboard), or read our latest analysis on [certik.com](https://www.certik.com/blog).
