# 🎁 How a $40K Donation Drained $6M From Summer[.]fi in One Transaction

- **Source URL:** https://www.quillaudits.com/blog/hack-analysis/summer-protocol-donation-attack
- **Fetched:** 2026-11-15
- **Channel:** @defendor_eng
- **Telegram message:** https://t.me/defendor_eng/1864 (id 1864)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
A donated, stale-valued token inflated a DeFi vault's NAV and share price, letting an attacker redeem against real depositor liquidity.

Anmol

On July 6, 2026, Lazy Summer Protocol lost approximately $6.04 million when an attacker manipulated the share price of two Ethereum-mainnet USDC vaults inside a single atomic transaction. This was not a compromised admin key, not an oracle price feed manipulation, not a reentrancy bug, and not a flaw in unaudited code, the contracts involved were verified and executed exactly as written. The attacker instead donated a stale-valued token directly into an Ark that had been capped for offboarding since October 2025 but never fully removed from the vault's asset count, inflating the vault's reported net asset value and redeeming against the vault's genuinely liquid capital.

Lazy Summer vaults are ERC-4626-compliant. Each vault, referred to as a Fleet, is managed by a `FleetCommander` contract sitting above a set of strategy adapters called Arks, each representing a position in an external protocol such as Morpho, Spark, Sky, or Silo. A vault's share price is derived by summing `totalAssets()` across every Ark in the active set and dividing by shares outstanding. Removing an Ark from that active set through  `removeArk`  requires the Ark's deposit cap to already be zero and its balance to already be empty. Setting the cap to zero only blocks new deposits, it does not remove the Ark from the active set or from the NAV calculation. That gap between *capped* and *removed* is what the exploit turned on.

Roughly three months before the exploit, the attacker began funding a set of wallets through the same funding path, an early sign the operation was planned well in advance rather than opportunistic.

Over the following weeks those wallets quietly accumulated Silo *Varlamore USDC Growth* vault tokens, a position that had kept reporting an on-chain value inherited from before November 2025's Stream Finance collapse, worth a fraction of what it still displayed on paper.

Just before 05:17 UTC on July 6, the attacker consolidated all of the pre-accumulated Varlamore tokens into a single, unverified exploit contract,  `0x0514F827C129C16418a0933E03C99A6AF982FC61`, ready to be donated in one motion.

In the same transaction, the attacker first primed the higher-risk vault, `LazyVault_HigherRisk_USDC` at `0xE9cDA459bED6dcfb8AC61CD8ce08E2D52370cB06`, with a near-costless deposit and withdraw round trip, moving roughly $398,000 into its buffer so a larger redemption later in the sequence could be paid out in liquid assets.

The attacker then flash-borrowed roughly 65.4M USDC plus 1M USDT from Morpho, requiring no capital of their own, and deposited about 64.8M USDC into the lower-risk vault, `LazyVault_LowerRisk_USDC` at `0x98C49e13bf99D7CAd8069faa2A370933EC9EcF17`, at the honest share price of roughly 1.0665, filling the vault to its deposit cap.

The attacker donated the consolidated Varlamore tokens directly into the Silo Ark still sitting inside that vault's active set, an Ark whose deposit cap had been zeroed months earlier but never fully removed, and the transfer alone pushed the vault's reported `totalAssets()` up by roughly 9.5 percent with no new shares minted.

The share price jumped from roughly 1.0665 to 1.1678 on the strength of that single donation, and the attacker immediately redeemed their freshly minted shares at the inflated rate, pulling out close to $71 million in USDC against a $64.8 million deposit.

That payout was assembled entirely from the vault's genuinely liquid Morpho, Spark, and Sky Ark positions and its buffer, not from the manipulated Silo Ark itself, because Lazy Summer drains Arks smallest-to-largest and stops once the requested amount is covered, so the inflated Ark was never touched during redemption.

The attacker repaid both flash loans in full, swapped the profit to DAI on Curve, and exited with 6,016,754.998 DAI, roughly $5.64 million pulled from the lower-risk vault and $0.40 million from the higher-risk vault.

This was not a coding bug, an oracle manipulation, or a compromised key; the contracts behaved exactly as written. **The root cause was that an Ark counts any tokens donated directly into it toward the vault's total assets without minting new shares, so a single donation of an over-valued token directly raises the share price, and the attacker had one Ark still active and priced into NAV that they could donate into.**

A vault's share price is simply `totalAssets()`, summed across every active Ark, divided by shares outstanding, so transferring a token straight into an Ark raises that Ark's reported assets, and therefore `totalAssets()`, with no new shares minted, and the transfer alone pushes price per share up.

The token the attacker chose to donate was worth pushing in precisely because it was cheap to acquire but still priced high by the Ark: Silo *Varlamore USDC Growth* tokens kept reporting a valuation from before November 2025's Stream Finance collapse, even though the position behind them was worth a fraction of that on the open market.

The Ark that received the donation should not have still been counted at all. Its deposit cap had been zeroed for offboarding back in October 2025, but `removeArk` also requires the Ark's balance to already be zero, a condition that offboarding never reached, so the Ark stayed in the active set and kept counting toward `totalAssets()` for roughly eight months.

Once the donation landed, `totalAssets()` jumped and share price jumped with it, from roughly 1.0665 to 1.1678, and the attacker simply redeemed their own freshly minted shares at that inflated price, a step that looked, mechanically, like any normal withdrawal.

**Ark decommissioning invariant.** A review would flag that `removeArk`'s zero-balance precondition can leave an Ark capped but active indefinitely, and would recommend a forced sweep-then-remove path, or a rule that excludes any Ark from NAV once its cap has been zero for longer than a defined grace period.

**Stale-asset devaluation checks.** Since the Varlamore Ark kept reporting a pre-collapse valuation months after the Stream Finance event, a review would recommend tying an Ark's reported value to the health of its underlying market, so an impaired position cannot continue pricing near par indefinitely.

**Donation-path threat modeling.** Because any ERC-4626-style Ark prices tokens transferred directly into it, a review would test *donate an over-valued asset directly into an active strategy* as a standard scenario against every Ark type in the fleet, not only against deposit and withdraw functions.

The attacker continues to hold approximately $2.5M in their EOA. [0x7BF716167B48CF527725722C6d79494b45B3BDCa](https://etherscan.io/address/0x7BF716167B48CF527725722C6d79494b45B3BDCa)

The remaining funds were routed through an attacker-controlled contract ([`0x824cb092b6f1dad5bf95b315250479fb38ef069a`](https://etherscan.io/address/0x824cb092b6f1dad5bf95b315250479fb38ef069a#tokentxns)), swapped from BONK to USDC and then to WETH, before being transferred to [`0x46e09c4d4d20c0474598b4d2ffdd08bdf416eba7`](https://etherscan.io/address/0x46e09c4d4d20c0474598b4d2ffdd08bdf416eba7). From there, the funds were deposited into Tornado Cash.

Roughly nine hours after the exploit, [Summer.fi](http://Summer.fi) confirmed publicly that it was aware of the reported exploit and was investigating the root cause, adding that protocol guardians were in the process of pausing every vault across the Lazy Summer Protocol.

[Summer.fi](http://Summer.fi) issued a formal security notice confirming an active exploit against the Lazy Summer Protocol, stating that Guardians had paused all vaults and zeroed deposit caps across every network, and asking users not to interact with the protocol until further notice.

The following day, [Summer.fi](http://Summer.fi) published a full post-mortem on behalf of the Lazy Summer Foundation, laying out the mechanism, a minute-by-minute timeline of the Guardian and Foundation response, the addresses involved, and the questions the DAO would need to resolve next.

Two days after the exploit, [Summer.fi](http://Summer.fi) invited the community to a dedicated call to walk through what happened on July 6, the response so far, and the expected timeline for next steps.

Following that call, [Summer.fi](http://Summer.fi) recapped the discussion publicly, the root cause was confirmed as a donation attack enabled by stale-valued tokens rather than a key compromise or contract bug, the Guardian module's first live-exploit use was reviewed, and a remediation RFC went live with three community polls covering whether to exclude the attacker's shares from any snapshot, whether to use the proposed snapshot, and how to structure a Merkle-based repayment.

**Attacker EOAs**

- Funder EOA: [0x7BF716167B48CF527725722C6d79494b45B3BDCa](https://etherscan.io/address/0x7BF716167B48CF527725722C6d79494b45B3BDCa)
- Intermediary wallet (Tornado Cash routing): [0x46E09c4D4d20C0474598b4d2fFDd08bdf416eBa7](https://etherscan.io/address/0x46E09c4D4d20C0474598b4d2fFDd08bdf416eBa7)

**Attacker-Deployed Contracts**

- Exploit contract, unverified: [0x0514F827C129C16418a0933E03C99A6AF982FC61](https://etherscan.io/address/0x0514F827C129C16418a0933E03C99A6AF982FC61)

**Vulnerable Contracts**

- LazyVault\_LowerRisk\_USDC (primary vault hit): [0x98C49e13bf99D7CAd8069faa2A370933EC9EcF17](https://etherscan.io/address/0x98C49e13bf99D7CAd8069faa2A370933EC9EcF17)
- LazyVault\_HigherRisk\_USDC (hit first to prime the buffer): [0xE9cDA459bED6dcfb8AC61CD8ce08E2D52370cB06](https://etherscan.io/address/0xE9cDA459bED6dcfb8AC61CD8ce08E2D52370cB06)
- Guardian Module (6-of-8 multisig): [0x91E4482CF58aC14d8DC25290d828b2A4D9492BA4](https://etherscan.io/address/0x91E4482CF58aC14d8DC25290d828b2A4D9492BA4)

Exploit **Transactions**

[0x0db528c44f23fc7fa4544684a2fab81096450a14aae8bc89f42cd0592d43da12](https://etherscan.io/tx/0x0db528c44f23fc7fa4544684a2fab81096450a14aae8bc89f42cd0592d43da12)

This was not a broken cryptographic scheme or a stolen key; the contracts behaved exactly as designed. The failure sat in the calendar, not the code: an Ark disabled for new deposits in October 2025 was never fully removed, and eight months later a $40,000 position built against its stale valuation was enough to pull $6.04 million from two vaults in a single transaction. Lazy Summer's response afterward- a fast Guardian pause, a swept donation, and a public, technically honest post-mortem- was executed well even though it came after the funds were already gone. Setting a deposit cap to zero disables new inflows; it does not disable a market's claim on a vault's net asset value. A cap is not a removal.

A great audit process is a mixture of great auditors, a layered approach for testing, and clear communication. At [<u>QuillAudits</u>](https://www.quillaudits.com/), we make sure that happens using our 7+ years of experience and talented team.

Contents

Tell Us About Your Project

Subscribe to Newsletter

Loading...

From day-zero risk mapping to exchange-ready audits, QuillAudits helps projects grow with confidence. Smart contracts, dApps, infrastructure, compliance: secured end to end.
