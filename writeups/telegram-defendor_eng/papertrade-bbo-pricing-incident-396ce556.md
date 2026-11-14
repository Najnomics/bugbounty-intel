# 🔬 CertiK Analysis: PaperTrade Lost $1.28M to a Pricing Flaw

- **Source URL:** https://www.certik.com/blog/papertrade-bbo-pricing-incident
- **Fetched:** 2026-11-14
- **Channel:** @defendor_eng
- **Telegram message:** https://t.me/defendor_eng/2251 (id 2251)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
## Incident Summary

PaperTrade [reported (opens in a new tab)](https://x.com/papertrade_xyz/status/2109308773231911359) manipulation attempts on 10–11 October 2026 targeting the Hyperliquid best bid and ask (BBO) used to price its synthetic positions. The project acknowledged the attempts on 11 October. The account examined in this analysis withdrew **1,279,106.191184 USDC more than it deposited**. PaperTrade settled positions at the instantaneous BBO midpoint, while its profit haircut used a fixed reference notional. This linked large synthetic payouts to an influenceable quote without increasing the haircut percentage as position size grew.
*Graphic summary — Analyst-created diagram of the supported mechanism, position 72098's settlement and account-level withdrawals.*

## Addresses and Roles

All addresses below are on **HyperEVM, chain 999**.

| **Chain** | **Address** | **Established role** | 
|---|---|---|
| HyperEVM | [0x2025137a136bea7446deba681cbfc7cf1970840e (opens in a new tab)](https://hyperevmscan.io/address/0x2025137a136bea7446deba681cbfc7cf1970840e) | Trading account examined in this analysis. | 
| HyperEVM | [0x6cd5661646289fb6e65ea5c032310fded797d0a2 (opens in a new tab)](https://hyperevmscan.io/address/0x6cd5661646289fb6e65ea5c032310fded797d0a2) | Exchange proxy; records positions, balances and withdrawals. | 
| HyperEVM | [0xa9b4c7b7ca5835652d81e25739c870d49f39cc2e (opens in a new tab)](https://hyperevmscan.io/address/0xa9b4c7b7ca5835652d81e25739c870d49f39cc2e) | PriceOracle proxy. | 
| HyperEVM | [0x3997ffc8cbd281d4fc8d0548e505ae2fbbbd985a (opens in a new tab)](https://hyperevmscan.io/address/0x3997ffc8cbd281d4fc8d0548e505ae2fbbbd985a#code) | PriceOracle implementation executed in the traced opening and settlement transactions. | 

## Background

[PaperTrade (opens in a new tab)](https://docs.papertrade.xyz/#/intro/what-is-papertrade) offered leveraged synthetic trading against its Martingaler liquidity pool. Opening a position created internal exposure; PaperTrade did not place an equivalent order on Hyperliquid. Closing the position settled its PnL against the pool.

[PriceOracle (opens in a new tab)](https://docs.papertrade.xyz/#/how/pricing-bbo) obtained Hyperliquid’s current best bid and ask through precompile 0x080e and used their midpoint as the execution price. Profitable closes passed through a deadband, an asymmetric-impact haircut and a winning-close fee. Payments were queued when liquidity was insufficient.
The price therefore came from Hyperliquid’s inside quotes, while PaperTrade’s pool backed the synthetic exposure. The amount payable depended on the position size, even though no equivalent quantity had traded at that midpoint.

## Attack Flow

All times below are UTC. The four steps describe the examined account’s opening, settlement, external trading and withdrawals.

1. **Position opening**

At 21:41:36 on 10 October, 0x2025137a136bea7446deba681cbfc7cf1970840e opened ETH long position **72098** in transaction [0xe639…f225 (opens in a new tab)](https://hyperevmscan.io/tx/0xe639e83d3575367a18f93bb6b285b40a554122cab8d2fbfdc025cf3520f2f225). The opening receipt recorded **20,000 USDC margin, 500× leverage and an entry price of $2,506.45**. The historical trace shows a **$2,506.40 bid** and **$2,506.50 ask**, with the oracle returning their **$2,506.45 midpoint**. Margin multiplied by leverage established **$10 million of synthetic exposure**.

*Figure 1 — Step 1: local decoded view of the [opening receipt (opens in a new tab)](https://hyperevmscan.io/tx/0xe639e83d3575367a18f93bb6b285b40a554122cab8d2fbfdc025cf3520f2f225#eventlog), block 48,202,020, log 4. Notional is derived from margin × leverage.*

1. **Settlement**

Six minutes later, at 21:47:36, the position closed in transaction [0xb5bc…df42d (opens in a new tab)](https://hyperevmscan.io/tx/0xb5bcbb7bd1de0c98defb209e38510386601c5c9b30de6b2a660f9ae31d7df42d). The closing receipt records an exit at **$2,510.85**, a favorable movement of approximately **17.55 basis points**.
The historical call trace follows Exchange → PriceOracle → BBO precompile 0x080e. The precompile returns **251080 / 251090** in $0.01 quote units:
a **$2,510.80 bid** and **$2,510.90 ask**.
PriceOracle returned **251085**, exactly the **$2,510.85 exit** recorded by the successful settlement. Both BBO reads in this transaction agree.

These quotes have a **$0.10 spread** (approximately **0.40 basis points**). The **17.55 basis points** above measures the entry-to-exit return over six minutes, not a deviation from an independent market price. Neither observation establishes an abnormal quote or deliberate price influence. This position illustrates the recorded settlement rules; ordinary leveraged trading remains a sufficient explanation for this example.

*Figure 2 — Step 2: rendered local view of preserved historical dRPC traces, including position 72098's [opening (opens in a new tab)](https://hyperevmscan.io/tx/0xe639e83d3575367a18f93bb6b285b40a554122cab8d2fbfdc025cf3520f2f225) and [close (opens in a new tab)](https://hyperevmscan.io/tx/0xb5bcbb7bd1de0c98defb209e38510386601c5c9b30de6b2a660f9ae31d7df42d). Close BBO frame \[0,0,0,2,0,0\]; block 48,202,386, receipt log 10. This establishes quote consumption. It does not establish an abnormal quote or deliberate price influence.*

This is where the price input becomes a payout. Prices use $0.01 quote units, so the integer-rounded deadband is floor(250645 / 50000) = 5 units, or $0.05. The remaining favorable move is:
Using the [documented ETH parameters (opens in a new tab)](https://docs.papertrade.xyz/#/how/asymmetric-impact), the profit scale is:
The resulting calculation matches the recorded settlement. Values below are rounded to six decimals; intermediate calculations retain full precision.

| **Settlement stage** | **Calculation** | **USDC** | 
|---|---|---|
| Raw PnL after deadband | 10,000,000 × m | 17,355.223523 | 
| Adjusted PnL | Raw PnL × scale | 13,494.728986 | 
| Winning-close fee | Adjusted PnL × 2% | 269.894580 | 
| **Net gain after fee** | **Adjusted PnL − fee** | **13,224.834407** | 

*Figure 3 — Step 2: explorer capture of the [closing receipt (opens in a new tab)](https://hyperevmscan.io/tx/0xb5bcbb7bd1de0c98defb209e38510386601c5c9b30de6b2a660f9ae31d7df42d#eventlog), block 48,202,386, log 10. Event values match the account records and payout calculation; displayed amounts are rounded to six decimals.*

The fixed **100,000 USDC reference notional** in term2 is the critical size relationship: actual position size does not enter the scale calculation. At these same prices and parameters, a **hypothetical $500,000 position** would produce **661.241720 USDC** after the fee. The recorded $10 million position produces **20× the gain**, while the impact haircut remains **22.243992%** in both cases.

Thus, a $4.40 price change produced a **13,224.834407 USDC** gain on the recorded position. The account had no ETH fill within five seconds of this close, so this example establishes settlement behavior without identifying a corresponding manipulation trade.

1. **External trading and repeated settlements**

Between **22:01:00 and 22:03:00**, the same account executed **597 ETH fills** on Hyperliquid, buying **6,058.1450 ETH** and selling **383.0414 ETH**. Its broader collected history contains **10,427 ETH fills** and approximately **$231.84 million of ETH turnover**.

The PaperTrade history contains **337 settled ETH positions**, including **296 profitable closes**. Winning positions span six notional sizes from **$500,000 to $10 million**; aggregate exposure comprised multiple positions.

*Figure 4 — Step 3: local aggregation of Hyperliquid fill records and PaperTrade settlement checks. The sample retains native trade IDs.*

Across 296 profitable closes, 62 were within one second of a same-account ETH fill: **52 overlap maker fills only**, and **10 include taker fills**. The latter occur in three settlement transactions across two seconds. For example, [position 69035 (opens in a new tab)](https://hyperevmscan.io/tx/0x8846b12c1c7b3f92cd86a51439cb399f101d0b24b95dff3031db4457716fc31f#eventlog) closed a short at $2,505.85 while nearby taker sells executed at $2,505.80. By comparison, [position 71121 (opens in a new tab)](https://hyperevmscan.io/tx/0xf200fce68f4f4d223f8320130a2e7d879f7ea6cd689c8f13402ec85754a262e4#eventlog) overlaps ten maker buys.

The recovered trace for position 69035’s transaction reads **$2,505.80 / $2,505.90**, returning the recorded **$2,505.85 midpoint**. Position 71121’s transaction similarly reads **$2,509.70 / $2,509.80** and returns **$2,509.75**. The actual quote inputs are now established for these transactions.

These matches do not establish that either quote was distorted. Testing deliberate price influence requires ordered market-wide quotes, orders and cancellations, together with a contemporaneous independent price reference; timestamp overlap alone is insufficient.

**4. Cash out**

Across the collected window, five Exchange withdrawals match successful receipts and HyperCore USDC credits:

| **Withdrawal time, UTC** | **USDC** | **HyperEVM transaction** | 
|---|---|---|
| Oct 10, 21:13:59 | 17,961.112612 | [0x9979…cd72 (opens in a new tab)](https://hyperevmscan.io/tx/0x99794ad438dfd80de5454d42b6e40ccd5ec69108db50648e10f7da165b9fcd72) | 
| Oct 10, 21:34:09 | 131,739.237844 | [0x9a27…3fbc (opens in a new tab)](https://hyperevmscan.io/tx/0x9a273bf61789acddb63645b1fb70f79f1af8f4604550209dd504e5314b793fbc) | 
| Oct 10, 22:06:48 | 1,543,488.792097 | [0x4162…23b0 (opens in a new tab)](https://hyperevmscan.io/tx/0x4162ac5044104b91728580b156d25803a6f34c60281604c85b2d1d81418823b0) | 
| Oct 10, 22:13:21 | 735,681.502282 | [0x136e…abd6 (opens in a new tab)](https://hyperevmscan.io/tx/0x136ed416f4e430c2c8e9b4d721ce101a993f538e62749ae4dfa7fff2941babd6) | 
| Oct 11, 02:10:35 | 50,336.049203 | [0x0223…ac48 (opens in a new tab)](https://hyperevmscan.io/tx/0x0223dfef2a2ad41a378502ae908ec75563c561b2b59fde69dd45b8ed449eac48) | 
| **Total Withdrawals** | **2,479,206.694038** |  | 

*Figure 5 — Step 4: local view of the [largest withdrawal (opens in a new tab)](https://hyperevmscan.io/tx/0x4162ac5044104b91728580b156d25803a6f34c60281604c85b2d1d81418823b0#eventlog), block 48,203,557, log 17, and its matching HyperCore credit.*

Deposits totaled **1,200,100.502854 USDC**, including redeposits. Subtracting these from withdrawals gives a **1,279,106.191184 USDC net outflow** to the account. Gross withdrawals include returned principal and reused funds. This account total does not measure aggregate LP loss or profit after costs on other venues.

## Vulnerability

1. **BBO midpoint without independent price validation**

The decoded PriceOracle branch rejects zero prices and crossed quotes, then returns the instantaneous midpoint. It contains no averaging or independent price-deviation check. These checks validate the quotes without measuring the liquidity supporting the synthetic exposure.

*Figure 6 — Collected oracle disassembly: BBO read at PC 0x08f5; midpoint arithmetic at 0x01ea–0x01f6. The archive runtime at block 48,202,386 matches this disassembly; historical call traces independently establish the BBO read and midpoint return. Original Solidity/build remains unverified.*

1. **Haircut percentage independent of position size**

The [asymmetric-impact formula (opens in a new tab)](https://docs.papertrade.xyz/#/how/asymmetric-impact) substitutes a fixed referenceNotional for actual position size. Dollar payouts therefore grow with exposure while the haircut percentage remains unchanged. Across six position sizes, all **296 profitable closes** match the documented curve within **0.000000001 USDC**.

*Figure 7 — [Official haircut documentation (opens in a new tab)](https://docs.papertrade.xyz/#/how/asymmetric-impact), captured 19 October, showing the fixed reference notional. Documentation, not verified incident-deployed Solidity.*

## Response and Recovery

In its [11 October statement (opens in a new tab)](https://x.com/papertrade_xyz/status/2109308773231911359), PaperTrade acknowledged overnight BTC/ETH BBO manipulation attempts. It attributed their feasibility to permissive launch open-interest caps and said it had begun tightening limits onchain and at the relayer.

PaperTrade also said a winning user returned almost all profits through new accounts. The examined account recorded **30 later liquidations losing 450,000 USDC**, already included in the net-withdrawal total. The cap changes and recovery through other accounts were not independently verified.
