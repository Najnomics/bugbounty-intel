# 🛡️ GMX V1 Hack of $42 Million Due to Smart Contract Vulnerability

- **Source URL:** https://blog.solidityscan.com/gmx-v1-hack-analysis-ed0ab0c0dd0f
- **Fetched:** 2026-11-12
- **Channel:** @defendor_eng
- **Telegram message:** https://t.me/defendor_eng/262 (id 262)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# GMX v1 Hack Analysis

### GMX v1 Hack Analysis

### Overview:

On **July 9, 2025**, **GMX (@GMX\_IO)** — a decentralized perpetuals trading protocol on Arbitrum — was exploited for over **$42 million**. The attacker abused a r**efund-based reentrancy-like vulnerability** in the `PositionManager.executeDecreaseOrder()` function, along with an **internal accounting desynchronization** in the GLP pricing mechanism.

The root cause includes the implicit assumption in `executeDecreaseOrder()` that the `_account` parameter is an Externally Owned Account (EOA), when in fact it can be a malicious smart contract. This vulnerability is an combination of [OWASP SC05: Reentrancy Attacks](https://scs.owasp.org/sctop10/SC05-Reentrancy/) and [SC03: Logic Errors.](https://scs.owasp.org/sctop10/SC03-LogicErrors/)

This allowed the attacker to deploy a malicious contract and spoof GMX’s keeper execution flow to gain reentrant access into core vault logic. By hijacking control flow during ETH refunds and exploiting a stale `getAum()` (Assets Under Management) calculation, the attacker repeatedly minted GLP at a low price, opened phantom short positions that artificially inflated AUM, and redeemed GLP at a higher price—draining liquidity from GMX’s vault across ETH, USDC, and WBTC.

### Smart Contract Hack Overview:

- **Victim Contract:** [0x489ee](https://arbiscan.io/address/0x489ee077994b6658eafa855c308275ead8097c4a) (vault), [0x321f6](https://arbiscan.io/address/0x321f653eed006ad1c29d174e17d96351bde22649) (GLP Manager),
- **Attack Transaction:** [0x03182](https://arbiscan.io/tx/0x03182d3f0956a91c4e4c8f225bbc7975f9434fab042228c7acdc5ec9a32626ef) (Arbitrum)
- **Attacker Addresses:** [0xDF334](https://arbiscan.io/address/0xdf3340a436c27655ba62f8281565c9925c3a5221), [0x7D3BD](https://arbiscan.io/address/0x7d3bd50336f64b7a473c51f54e7f0bd6771cc355)
- **OWAPS SC Top 10:** [SC05: Reentrancy Attacks](https://scs.owasp.org/sctop10/SC05-Reentrancy/) and [SC03: Logic Errors.](https://scs.owasp.org/sctop10/SC03-LogicErrors/)

### Decoding the Smart Contract Vulnerability:

- The root cause of the GMX exploit lies in the improper trust assumption in the `PositionManager.executeDecreaseOrder()` function, which allowed a **malicious smart contract to hijack execution flow**, and in the **flawed AUM (Assets Under Management) accounting logic** in the `GlpManager.sol` during leveraged position handling.
- This vulnerability led to a sophisticated multi-step attack where the attacker was able to **artificially inflate the protocol’s AUM**, redeem GLP for more assets than deserved, and ultimately extract over **$42 million** worth of tokens from the GMX vault.

- In the `PositionManager.sol` contract, the function `executeDecreaseOrder()` is designed to be called by a privileged **keeper bot**, and takes the `_account` as a parameter representing the user whose position is being reduced.

`IOrderBook(orderBook).executeDecreaseOrder(_account, _orderIndex, _feeReceiver);`
- The vulnerability arises because `_account` can be **any address**, including a **smart contract**, yet GMX implicitly assumes it to be an **EOA** (Externally Owned Account).
- Within the `executeDecreaseOrder(),`the function internally calls `getDecreaseOrder()`, which returns the full position details — including size, index token, and collateral. Then, after updating short data, the system enables leverage and calls into the order book to execute the order. During this process, the `_account` (attacker’s contract) is refunded ETH for gas costs using a `call{value: ...}` with no gas limit, which causes the fallback function of the attacker’s contract to execute.
- This gives the attacker a **reentrancy window** to call other GMX functions while the state is in an inconsistent, pre-settlement phase — specifically, they were able to call `increasePosition()` and open large **short positions** on WBTC while `enableLeverage = true` inside the callback of their malicious contract.

- The second key vulnerability lies in how `GlpManager.sol` calculates the **value of GLP tokens** during redemption, using the `getAum()` function.

```
function getAum(bool maximise) public view returns (uint256) {
    ...
    uint256 price = maximise ? vault.getMaxPrice(token) : vault.getMinPrice(token);
    ...
    uint256 size = _vault.globalShortSizes(token);
    if (size > 0) {
        (uint256 delta, bool hasProfit) = getGlobalShortDelta(token, price, size);
        if (!hasProfit) {
            aum = aum.add(delta); // Unrealized short losses are added to AUM
        } else {
            shortProfits = shortProfits.add(delta);
        }
    }
    ...
}
```
- The problem here is **timing**. When a short position is first opened (via reentrancy), the short size is updated immediately, but the **average short price** lags behind. During this in-between state, the system wrongly assumes that the position is opened at a much lower price, resulting in unrealized losses being calculated and **added to AUM**.
- Thus, the AUM — used in GLP redemption via `unstakeAndRedeemGlp()` to determine how much value each GLP token represents — becomes artificially inflated due to mispriced unrealized losses, even though no real losses exist yet.
- This allowed the attacker to redeem their GLP at an overstated value, exploiting the stale AUM calculation and **draining excess assets from the vault.**

### Attack Sequence:

The attacker deploys a malicious contract compatible with GMX’s `OrderBook` interface and places a crafted `decreaseOrder()` using this contract.


GMX’s keeper bot calls `executeDecreaseOrder()` with the attacker’s contract as `_account`.


As part of order execution, ETH is refunded to `_account` using `call{value:}`. This triggers the fallback function in the attacker’s contract — **creating a reentrancy window**


Within the callback, the attacker immediately reenters GMX logic and calls `increasePosition()`to open a large short on WBTC.


The vault updates `globalShortSizes` right away, but `globalShortAveragePrices` still reflects old data. This discrepancy leads the system to believe the short is deeply underwater.


When `getAum()` is called, the unrealized loss from the perceived underwater short is added to AUM — **artificially inflating it**.


The AUM becomes artificially inflated, making GLP appear more valuable.


The attacker then calls `unstakeAndRedeemGlp()` to redeem GLP tokens at the inflated AUM rate — extracting more assets than deserved.


The attacker repeats the process across various vault tokens (e.g., WBTC, ETH, USDC), draining \~$42 million from GMX’s liquidity pool.


- GMX Team confirmed that the exploit is isolated to GMX V1’s GLP pool on Arbitrum. V2 contracts, GMX tokens, and liquidity pools on Avalanche remain unaffected. All GLP trading, minting, and redemption has been paused on both Arbitrum and Avalanche as a precaution. More details can be found in this X thread:

- Team member from GMX ([@xdev\_10](https://x.com/xdev_10)) also confirmed the order keeper bot was not compromised. It executed the order flow as expected. The exploit originated from the malicious smart contract crafted by the attacker, which was used to create and hijack execution during order fulfillment.
- GMX has sent an on-chain message to the exploiter, offering a 10% (nearly 4M USD) white-hat bounty for the return of funds. *“If 90% of the stolen assets are returned within 48 hours, GMX commits to no legal action.”* The message was embedded in this [on-chain transaction](https://arbiscan.io/tx/0x92a39e66e54aff033cd7b41b468de7891cf459593495d68d78099cc889547380).

- GMX Team is working with security partners and lead auditors to conduct a full investigation. A detailed post-mortem will be published after the review is complete. Preliminary analysis can be found here:

### Mitigation and Best Practices:

- Never assume an address is an EOA. Always validate inputs like `_account` to avoid smart contract callbacks. Also avoid using `call{value: ...}` without gas limits. Prefer pull-based refund mechanisms or deferred withdrawals.
- Atomically update `globalShortAveragePrices` alongside `globalShortSizes` to prevent AUM miscalculations during leveraged actions.Use pull-based refunds, reentrancy guards, CEI pattern, and smooth AUM calculations to harden liquidity-sensitive logic.
- Ensure off-chain bots verify all assumptions (e.g., `_account` type) and consider invariant testing to catch stale-state exploits early.
- To prevent such vulnerabilities, the best Smart Contract auditors must examine the Smart Contracts for logical issues. We at [CredShields](https://credshields.com/) provide smart contract security and end-to-end security of web applications and externally exposed networks. Our public audit reports can be found on [https://github.com/Credshields/audit-reports](https://github.com/Credshields/audit-reports). Schedule a call at [https://credshields.com/](https://credshields.com/)
- Scan your Solidity contracts against the latest common security vulnerabilities with 494+ detections at [SolidityScan](https://solidityscan.com/).

### Conclusion:

SolidityScan is an advanced smart contract scanning tool that discovers vulnerabilities and reduces risks in code. Request a security audit with us, and we will help you secure your smart contracts. Signup for a free trial at [https://solidityscan.com/signup](https://solidityscan.com/signup?utm_source=blog&utm_medium=blog&utm_campaign=solidity_scan_loop_blog)

Follow us on our Social Media for Web3 security-related updates.
