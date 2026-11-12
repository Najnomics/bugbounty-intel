# 📊 Weekly Web3 Recap: $37M+ Lost Across Phishing, Mints, and Bridge Exploits

- **Source URL:** https://www.cryptotimes.io/2026/08/16/crypto-whale-loses-25-6m-again-as-weekly-hacks-cross-37m
- **Fetched:** 2026-11-12
- **Channel:** @defendor_eng
- **Telegram message:** https://t.me/defendor_eng/1982 (id 1982)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
The week of August 9 to August 15 delivered another rough stretch for crypto security, with a repeat phishing drain of $25.6 million on an unidentified whale wallet, a $7.9 million cross-chain breach at Coinsbuy, a suspected 4 billion ONE mint on Harmony Protocol, a 200,000 XRP theft from the Coreum-XRPL Bridge, an unauthorized minting incident at Oraichain, and a pricing-logic flaw at USM Protocol pushing weekly confirmed damage past $37 million.

The stretch lands on top of an August that already opened with the fallout from the [Coldcard firmware exploit](https://www.cryptotimes.io/2026/08/04/nothing-is-100-safe-in-crypto-bitcoins-coldcard-exploit-and-growing-security-crisis/), whose stolen bitcoin cache had climbed past $130 million by mid-month. It also extends the shift documented in [CertiK’s H1 2026 report](https://www.cryptotimes.io/2026/07/06/web3-lost-1-31b-in-h1-2026-as-hackers-changed-their-playbook-certik/), which found Web3 lost more than $1.31 billion across 344 incidents in the first half, with wallet compromises and infrastructure breaches now the costliest attack surface.

A repeat phishing attack on the same wallet that lost $24.2 million in 2023 drained another $25.6 million on August 12, this time with no return of funds.

Cross-chain infrastructure took the second-largest hit of the week, with Coinsbuy losing $7.9 million across Ethereum and TRON before the attacker laundered proceeds through Monero.

Protocol-level failures at Harmony, Coreum, and Oraichain exposed how unchecked minting paths and deposit-verification gaps continue to bypass audits aimed at conventional smart-contract bugs.

## Crypto Whale Drained of $25.6M in Repeat Phishing Attack

The biggest single-victim loss of the week hit an unidentified crypto whale on August 12, when an attacker drained roughly $25.6 million in a wallet compromise that mirrored an incident the same address suffered in September 2023.

On-chain analyst Specter flagged the drain on X, noting that the attacker swapped a basket of assets, including WBTC, cbBTC, LDO, USDS, and CRV, into DAI and ETH within minutes of the initial move. Blockchain security firm PeckShield subsequently broke down the largest components of the loss, listing roughly $6.3 million in aWBTC (Aave-wrapped Bitcoin), $5.1 million in DAI, $4.7 million in WBTC, and about $2.6 million in ETH, with smaller balances of cbBTC, USDS, LDO, and CRV also taken.

The proceeds were consolidated into approximately 20 million DAI and 3,000 ETH sitting across four attacker-controlled addresses at the time of disclosure. As of mid-week, no portion of the stolen assets had been returned.

### A Familiar Address

The 2026 incident was the second time the same wallet had been hit. In September 2023, the address lost approximately $24.2 million after signing malicious token approvals that let an attacker pull 4,851 Rocket Pool ETH (rETH) and 9,579.2 Lido Staked ETH (stETH), later swapped for roughly 13,785 ETH and 1.64 million DAI. In that earlier case, the 2023 attacker returned around 90% of the stolen funds, leaving the victim with a manageable net loss.

The August 12 drain has followed a different trajectory. PeckShield tracked the stolen basket into four fresh addresses and reported no signs of a return offer. Combined, the two incidents have now cost the same address close to $50 million.

Security researchers have not confirmed whether the latest breach came from a fresh signature-phishing prompt or a direct private-key compromise, and both routes remain live theories. A similar large-holder phishing pattern was documented earlier this year when a [crypto user lost $999,999 in USDT](https://www.cryptotimes.io/2026/07/09/crypto-user-loses-999999-in-usdt-to-a-single-phishing-signature/) to a single malicious approval, part of what Scam Sniffer has described as an industry-wide shift toward “whale hunting.”

**Latest update:** The victim has not been publicly identified, and no post-incident statement has been issued from the address’s owner. PeckShield continues to monitor the four attacker wallets, and DAI issuer Sky (formerly MakerDAO) has not signaled any freeze action on the roughly 20 million DAI now sitting in those addresses.

## Coinsbuy Loses $7.9M in Coordinated Ethereum and TRON Drain

Two days earlier, wallets tied to B2B crypto payment processor [Coinsbuy were drained](https://www.cryptotimes.io/2026/08/10/coinsbuy-wallets-drained-for-over-7-9-million-on-ethereum-and-tron/) of more than $7.9 million on August 9, in a coordinated incident that hit both the Ethereum and TRON networks simultaneously around 13:00 UTC.

On-chain investigator Specter first flagged the abnormal outflows on Telegram, with the alert later amplified by DarkWebInformer in an X [post](https://x.com/DarkWebInformer/status/2086566165665522120). The attacker’s activity was traced to two Ethereum addresses (0x4d1bEF2F…61d3 and 0x66790b54…4b17) and one TRON address (TVpX9xCzrj…dgubGR), with independent researcher CryptoEights publishing a detailed forensic [thread](https://x.com/CryptoEights/status/2086688020254818633) mapping the movement.

According to on-chain data, the attacker began with a 5 USDT probing transaction before siphoning 6.04 million USDT from eight TRON wallets in the space of an hour. On Ethereum, three wallets were simultaneously emptied of 1.89 million USDT and 77 ETH, with the two chains linked through the cross-chain swap service Bridgers to convert what looked like separate operations into a single incident.

### The Laundering Path

The attacker moved quickly to convert the stolen basket into Monero (XMR) using instant-exchange services such as ChangeNOW, FixedFloat, and BingX in an attempt to break the on-chain trail before freezes could take effect. ChangeNOW cooperated with investigators and froze a six-figure sum linked to the stolen funds mid-transfer, though most of the $7.9 million had already been converted by the time freezes activated.

The simultaneous activity on two separate chains pointed multiple investigators toward a hot-wallet private key compromise or an elevated administrative privilege breach rather than a smart-contract exploit. Coinsbuy has served enterprise, merchant, and exchange clients since 2019, and this was the first publicly confirmed hack on the platform.

**Latest update:** Coinsbuy temporarily paused deposits and withdrawals after the incident, then refilled the drained wallets to within 0.05% of their pre-attack balances within 24 hours, stating that the incident had been “contained” and that “all affected amounts have been covered in full by the company from its own reserves.” The processor has since announced a $100,000 bounty for information identifying the attacker.

## Harmony Protocol Hit by 4 Billion ONE Mint

Layer-1 blockchain [Harmony was exploited](https://www.cryptotimes.io/2026/08/12/harmony-faces-suspected-4b-one-mint-as-team-explores-network-rollback/) between August 11 and 12, with an attacker suspected of minting roughly 4 billion ONE tokens, equal to about 26% of the network’s circulating supply, according to on-chain analyst Juiceberg.

The claim was first posted at 01:42 UTC on August 12 by Juiceberg, who [wrote](https://x.com/the_juice_berg/status/2087354915995709642) on X that on-chain data showed an unauthorized mint of 4 billion ONE via empty blocks, with 2.8 billion of those tokens moved to centralized exchanges as the price collapsed while the network’s totalSupply endpoint failed to reflect the additional supply.

In a follow-up post approximately three hours later, the same account said the attacker had roughly 115 million ONE left to sell on-chain, about 2.9% of the total minted, with the remainder already on exchanges either sold or sitting in deposit wallets.

Harmony confirmed the exploit at 04:26 UTC on August 12, [posting](https://x.com/harmonyprotocol/status/2087395174263705704) that it was working with its team and appropriate exchanges to stop and freeze the funds, that it was working on a patch and rollback options, and that it would issue further updates as information became available.

### The Scale of the Damage

SlowMist logged the realized loss from the incident at approximately $3.2 million based on the value the attacker was able to extract through on-chain sales before liquidity dried up, though the dilution effect of the mint on remaining holders was materially larger. ONE traded at $0.0007605 at 06:07 UTC on August 12, down 38.33% over the previous 24 hours, with market capitalization compressed to $11.41 million on 24-hour volume up more than 3,700%.

Harmony published four wallet addresses at 05:25 UTC on August 12 and asked all exchanges to block and freeze funds tracing back to them, listing them in both native Harmony and hexadecimal formats. The project then [released](https://github.com/harmony-one/harmony/releases/tag/v2026.1.1) an emergency validator patch (v2026.1.1) at 06:40 UTC that it said prevents any further minting, and asked all validators to upgrade. Bridge.harmony.one was paused as a precaution.

### Harmony’s Third Major Incident

The August exploit is Harmony’s third significant on-chain security event. In [June 2022, an attacker drained the Horizon bridge](https://www.cryptotimes.io/2022/06/27/harmony-protocol-offers-1m-bounty-following-100m-exploit/) of approximately $100 million after compromising validator private keys, an incident the FBI later attributed to North Korea’s Lazarus Group. In December 2023, a software defect in the network’s staking system improperly minted 146.28 million ONE across 74 delegator addresses, which was contained via an emergency hard fork. The August 2026 figure of 4 billion ONE would be more than 27 times the scale of the 2023 bug if confirmed.

**Latest update:** Harmony has not yet published the specific vulnerability behind the mint, confirmed the final amount involved, or laid out the boundary from which a potential rollback would run. No major exchange had published a formal notice on ONE deposits or withdrawals at the time of writing, and coordination with venues on freezing the flagged addresses is understood to be ongoing.

## Coreum-XRPL Bridge Drained of Nearly 200,000 XRP

Alongside the Coinsbuy incident on August 9, the cross-chain bridge connecting [Coreum to the XRP Ledger was exploited](https://www.cryptotimes.io/2026/08/11/coreum-bridge-loses-nearly-200000-xrp-in-deposit-verification-attack/) for approximately 199,916 XRP, worth around $200,000 at the time, in a 97-minute window that stripped the bridge account of 99.7% of its reserves.

The attack began at 19:16 UTC and unfolded through 94 multisig-authorized payment transactions, each requiring 17 of 28 relayer keys to sign off. The bridge account balance fell from roughly 200,410 XRP to just 493.5 XRP by the time the outflows stopped at 20:53 UTC.

TX, the U.S.-based blockchain company that operates Coreum and Sologenic following their March 2026 merger, [confirmed](https://x.com/txEcosystem/status/2087269579190046895) the incident in an X thread and acknowledged that bridged XRP on Coreum is not currently fully backed as a result. The company also said it has filed a complaint with the FBI.

### A Verification Gap in the Relayer Logic

The exploit did not compromise the XRP Ledger itself, and no private keys were stolen. Instead, the attacker exploited a flaw in the bridge’s deposit verification logic: the relayer software scanned the bridge account’s transaction history for payments carrying a specific Coreum recipient memo, treating that memo as proof that a deposit had genuinely arrived, without confirming that the payment had actually reached the correct destination wallet.

The attacker exploited that gap by moving self-controlled wrapped tokens between wallets they owned, attaching a Coreum-formatted memo to each transfer. Because those wrapped tokens had originally been issued by the bridge itself, the transactions showed up cleanly in its history with nothing to flag them as fake deposits. Each of the 94 fake deposits then triggered a real XRP withdrawal from the bridge’s XRPL wallet.

An analysis from the XRPL analytics platform xrpl.to confirmed that the loss came from the bridge’s own processes and not from any weakness in the XRP Ledger, ruling out an earlier community theory that the “rippling” feature had been abused.

**Latest update:** The Coreum bridge remained suspended at the time of writing, with the Coreum Development Foundation yet to publish a formal post-mortem or identify the attacker. Two recipient wallets, created less than two hours before the first payment, received about 107,397 XRP and 92,519 XRP respectively before onward-routing most of the funds to two accounts created on June 28, 2026.

## Oraichain Halts Network After Unauthorized ORAI Mint

AI-focused Layer-1 blockchain Oraichain suffered a security incident on August 9 that forced the team to halt the entire network and restrict bridges, cross-chain routes, and public interfaces.

Oraichain [disclosed](https://x.com/oraichain/status/2086774707882451012) on X that a vulnerability in an EVM cross-chain transfer path had enabled unauthorized ORAI minting, prompting the halt at 04:00 UTC on August 9. In a follow-up statement, the team said the exploit path had been identified and addressed, that it was working with partners and centralized exchanges to limit fund movements, and that it was preparing to burn the unauthorized minted balances and reconcile protocol state to restore the canonical ORAI supply.

The team did not initially disclose the size of the mint or a dollar figure for the loss, and detailed on-chain reconstruction has been delayed by the halt itself. Oraichain also asked users not to transfer ORAI or perform any mainnet transactions until further notice, and its OraiBridge and cross-chain routes remain restricted.

The pattern echoes the Harmony incident three days later: both involved unauthorized minting through a compromised or under-verified path rather than a classical smart-contract reentrancy or oracle attack, and both required a full network response beyond the immediate contract layer.

**Latest update:** Oraichain has not yet published a full post-mortem, disclosed the total ORAI minted, or confirmed the restart timeline for the mainnet. No affected exchange has publicly named the incident in its status pages.

## USM Protocol Loses $136K in Pricing Logic Flaw

Ethereum stablecoin protocol USM was exploited on August 10 for approximately 70.83 ETH, worth around $136,000, after an attacker abused a pricing-logic flaw inside the protocol’s defund path.

Blockchain security firm SlowMist [reported](https://x.com/SlowMist_Team/status/2086644725143183639) that the ethFromDefund() function inside defund() used the arithmetic mean of the current and estimated final FUM sell prices for a single redemption but lacked what SlowMist described as “split invariance.” Combined with a per-redemption state contraction (adjShrinkFactor) and integer rounding, that meant the same FUM position could yield more ETH when redeemed as many small transactions than as one large one.

The attacker used a flash loan to call fund() and manipulate the protocol’s internal pricing, then split the same FUM amount into 64 small defund() calls, extracting more ETH than a single large call would have permitted. USM is a decentralized minimalist ETH-backed stablecoin protocol that has historically drawn attention for its no-governance design, and the incident is the first significant exploit against the protocol in 2026.

**Latest update:** USM has not issued a public statement on the August 10 exploit at the time of writing. Security researchers are categorising the incident as an economic exploit of the protocol’s redemption math rather than a classical reentrancy or oracle failure, and the transaction has been circulated for downstream monitoring by exchanges and analytics providers.

## The Bigger Picture

Every major loss this week traced back to infrastructure, keys, or economic logic rather than smart-contract code executing as designed. The unidentified whale fell to a repeat phishing or private-key compromise. Coinsbuy fell to a coordinated hot-wallet drain across two chains. Harmony fell to a minting path that produced blocks the network’s own totalSupply endpoint did not reflect.

The Coreum-XRPL bridge fell to a relayer that trusted a memo instead of verifying a destination. Oraichain fell to an EVM cross-chain transfer path that permitted an unauthorized mint. USM fell to a redemption function whose arithmetic mean pricing rewarded the exact split pattern an attacker used.

The wider August context reinforces the pattern. The ongoing [Coldcard firmware exploit](https://www.cryptotimes.io/2026/08/14/galaxy-claims-coldcard-attacks-halt-after-aug-6/), which began on July 30 and continued to drain seed-vulnerable wallets into early August, has now been logged at more than $130 million in stolen bitcoin. During the current week, the primary Coldcard attacker also resurfaced for the first time since the theft, [moving 30.185 BTC (roughly $1.94 million)](https://www.cryptotimes.io/2026/08/15/coldcard-attackers-likely-used-unrestricted-ai-models-galaxy-says/) to a newly created wallet in what on-chain analysts flagged as an early cash-out signal.

The shift also tracks with the [$47 million loss](https://www.cryptotimes.io/2026/07/26/crypto-loses-over-47m-in-a-week-as-afx-trade-wanchain-verus-get-hacked/) two weeks ago at AFX Trade, Wanchain, Verus, Allbridge, B² Network, and Lien Finance, and the [$20 million loss](https://www.cryptotimes.io/2026/07/19/crypto-loses-over-20m-in-a-week-as-ostium-across-cascade-get-hacked/) the week before that across Ostium, Cascade, DeFiTuna, and Across. Nominis has separately pegged 2026 losses through July at approximately $1.65 billion, a figure that continues to climb as the attack surface migrates further up the stack, away from the code that gets audited and toward the keys, permissions, minting paths, and off-chain infrastructure that mostly do not.

Also Read: [Walix Wallet Hack: Over $1M in Stolen Crypto Traced to Xhash](https://www.cryptotimes.io/2026/08/14/walix-wallet-hack-over-1m-in-stolen-crypto-traced-to-xhash/)


**Disclaimer:**The information researched and reported by The Crypto Times is for informational purposes only and is not a substitute for professional financial advice. Investing in crypto assets involves significant risk due to market volatility. Always Do Your Own Research (DYOR) and consult with a qualified Financial Advisor before making any investment decisions.
