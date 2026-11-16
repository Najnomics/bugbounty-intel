# 🛡️ HIP-3: A New Level of Security and Accountability in Hyperliquid

- **Source URL:** https://blocksec.com/blog/deep-dive-into-hip-3-a-builder-centric-perspective
- **Fetched:** 2026-11-16
- **Channel:** @defendor_eng
- **Telegram message:** https://t.me/defendor_eng/1138 (id 1138)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
**Hyperliquid Improvement Proposal 3 (HIP-3)** \[1\] introduces a fundamental change in how perpetual markets are created and scaled on Hyperliquid. By opening the market listing process to third-party builders, HIP-3 shifts listing from a discretionary, platform-controlled action to a protocol-level, ruled-based interface.

Since its deployment on mainnet, builder-deployed markets have generated over $13 billion in trading volume in roughly three months, demonstrating that HIP-3 can materially improve the scalability and flexibility of market expansion. However, ***this shift does not simply decentralize power; it also reallocates responsibility***. Risks that were previously absorbed or mitigated by centralized platform operations are now borne directly by builders.

As a result, the core question under HIP-3 is no longer whether a market can be launched, but whether it can be operated safely over time. This report analyzes HIP-3 from a builder-centric perspective, focusing on how markets are defined and operated, the risks builders face, and how those risks, particularly oracle-related risks, can be mitigated.

## 0x0 Background

Hyperliquid's architecture \[2\] departs from this model by decoupling execution and risk infrastructure from market definition. Its dual-layer design consists of:

- HyperCore, a purpose-built Layer 1 blockchain optimized for derivatives trading, providing unified matching, liquidation, and settlement.
- HyperEVM, an EVM-compatible application layer that enables extensible logic and builder interaction.

Because execution and liquidation are enforced uniformly at the protocol level, new markets can reuse the same core infrastructure without reimplementing critical safety logic. However, ***pricing cannot be fully standardized***. Oracle inputs, leverage design, and runtime operations inevitably vary by market, making pricing the primary interface where decentralization meets risk.

Despite this architecture, the listing process for Hyperliquid's native perpetual markets, also referred to as validator-operated perps, still resembles a traditional CEX approach. Listing new contracts is largely driven by the core team, while delistings are determined via validator votes.

HIP-3 was introduced to decentralize this listing process by enabling builder-deployed perpetual markets. It formalizes the separation between market definition and protocol-enforced execution by allowing builders to define and operate markets, while the protocol enforces hard execution and risk boundaries. As such, HIP-3 represents a key milestone toward a fully decentralized perp listing process.

## 0x1 Builder Responsibilities: Definition and Operation

Under HIP-3, builders assume end-to-end responsibility for market lifecycle management. In this section, we first walk through the market launch workflow, and then focus on the operational levers that most directly determine market stability in production.

### 0x1.1 Market Launch Flow: Definition and Operation

Under HIP-3, launching a market is not a single action. As illustrated in the full market launch workflow below, it is a process that spans two distinct phases: **market definition** (steps 1 through 4) and **market operation** (step 5).

During the market definition phase, a builder must first stake 500,000 HYPE on mainnet. After meeting the staking requirement, the builder can deploy one perpetual DEX, which forms an independent trading domain with its own margin system, order books, and deployer-controlled settings. At the DEX level, the builder selects a quote asset to be used as collateral for all markets on that DEX. The selected quote asset must retain permissionless status, as losing this status will disable the corresponding DEX. The builder then defines core market parameters, including oracle specifications, contract parameters such as the symbol and leverage limits, and margin tables. The first three markets can be deployed directly, while additional markets require acquiring slots through a Dutch auction.

Dutch auction: Each round lasts 31 hours, the starting price each time is 2× the previous final price (last winning price / lowest price).


Once markets are live, the builder enters the market operation phase. This phase involves continuously updating oracle prices via the `setOracle` interface, maintaining leverage and margin configurations, monitoring liquidity and open interest, and executing emergency actions such as halting trading and settling positions when necessary.

In practice, most severe failures under HIP-3 occur not during market definition, but during prolonged operation under stressed market conditions. Importantly, builder responsibility does not end immediately after halting markets. Unstaking is only possible after all markets are settled, and the stake remains slashable during the mandatory unstaking period.

### 0x1.2 Critical Focus Areas: Pricing and Solvency

Builders face two coupled focus areas across market definition and market operation: **oracle configuration and price formation**, and **market solvency under stress**. These two areas are tightly coupled, as pricing failures can quickly propagate into solvency stress through protocol-level risk controls.

#### 1. Oracle Configuration and Price Formation

Hyperliquid defines two prices:

- **Oracle Price**: a weighted median of spot mid-prices from major external exchanges, designed to be independent of Hyperliquid's internal market data and primarily used to anchor funding.
- **Mark Price**: an internal risk price derived from multiple inputs, including the oracle price and local market data, used for unrealized PnL (profit and loss) and risk controls.

In short, oracle price anchors funding, while mark price drives margin checks, liquidations, and **TP** (Take Profit) and **SL** (Stop Loss) triggers.

Under HIP-3, the roles of oracle price and mark price do not change, but the computation mechanism changes:

**a) Inputs to `setOracle`**

- `oraclePx` (required): same definition as in HyperCore.
- `markPx` (optional): 0–2 externally computed mark price candidates.
- `externalPerpPx` (required): a reference value to prevent sudden mark price deviation.

Builders typically deploy relayer nodes to feed prices: `oraclePx` is computed from multiple external sources, `markPx` is computed by the relayer with a custom algorithm, and `externalPerpPx` from the weighted median of perp mid prices from multiple CEXs.


**b) Actual mark price**

- Compute **local mark**: `median(best bid, best ask, last trade)`.
- Take **local mark** and `markPx` (0–2 values) together and take the **median** to get the new mark price.

**c) `setOracle` constraints**

- **Update frequency**: at least 2.5s between calls; if `markPx` is not updated for 10s, it falls back to **local mark price**.
- **Amplitude limits**: `markPx` can change by at most ±1% per update; all prices are clamped within 10× the start-of-day price.

**Why Asset Type Matters for Pricing in HIP-3?**

Under HIP-3, perpetual markets can be launched for any type of asset. These assets can generally be divided into 24/7 assets (tradable around the clock) and non-24/7 assets (tradable only during specific market hours, with no spot trading outside those hours). The difference in trading hours fundamentally determines how prices are sourced and maintained.

For 24/7 assets (e.g., BTC), relatively stable prices can be continuously obtained by aggregating data from CEXs, DEXs, or trusted oracle services.

For non-24/7 assets (e.g., equities), sufficient liquidity and reliable external market prices are only available during official trading hours. To keep such assets trading continuously on HIP-3, a separate pricing mechanism must be used during off-market hours.

Take the stock perp markets on **trade.xyz** as an example:

- ***During market hours***, stable oracle prices are provided by external oracle services such as Pyth.
- ***During off-market hours***, prices are adjusted based on the asset's last closing price, combined with internal buy/sell pressure from the order book. The mark price is constrained to fluctuate within **±1 / max\_leverage** of the last closing price (e.g., Tesla: 10× leverage → ±10%).

#### 2. Market Solvency Under Stress

Hyperliquid adopts two mechanisms, liquidation and ADL (auto-deleveraging), to maintain market solvency. Under HIP-3, both liquidation and ADL largely follow HyperCore’s design. The primary difference is a protocol-level restriction: HLP (Hyperliquidity Provider), which serves as the protocol vault, cannot take over risky positions in HIP-3 markets. As a result, the intermediate vault buffer that can absorb positions between market liquidation and ADL in HyperCore is absent in HIP-3.

Given the importance of this liquidation-to-ADL pathway during stressed market conditions, we review liquidation and ADL in detail below. All solvency mechanics discussed here assume isolated margin, the only margin mode currently supported in HIP-3 markets.

**a) Liquidation**

Liquidation is triggered when the **position's net value (isolated position value)** is insufficient to meet the **maintenance margin requirement**, it becomes liquidatable. All liquidation-related checks are based on the mark price, not on particular execution price.

Liquidation price formula is defined in the following:

Where:

- `side`: 1 for long positions, -1 for short positions
- `l` is the maintenance margin ratio

The value of `MAINTENANCE_LEVERAGE` is determined by the margin tier corresponding to the position.From that tier, the maintenance margin ratio `mmr` is obtained:

When margin tiers are configured, apply the mmr of the tier that corresponds to the position's notional value at the liquidation price.

- margin\_available (isolated): isolated\_margin - maintenance\_margin\_required

Once a position becomes liquidatable, the system first attempts to close it via **market orders on the order book**. If the execution successfully brings risk back within safe bounds, any remaining margin is returned to the trader.

However, in cases of insufficient order book depth or price gaps, the **actual average execution price may be significantly worse than the mark price**, resulting in a **''liquidation shortfall''**.

Isolated position value refers to the net value of an isolated position at the current mark price, representing the margin allocated to that position after accounting for unrealized PnL.


**b) ADL (auto-deleveraging)**

In extreme scenarios, the ADL (auto-deleveraging) mechanism acts as a final backstop.

ADL is triggered when an **isolated position value turns negative**. The system ranks profitable counterparties by PnL and leverage, then forcibly reduces or closes these positions at the **previous mark price** (the previous recorded mark price before ADL is triggered). By using the winning side's profits to **offset the deficit**, the protocol remains solvent and does not incur bad debt.

The sorting index is calculated as:

Here, `notional_position` refers to the absolute market value of the position at the prevailing mark price, computed as `|position_size| × mark_price`. `account_value` denotes the account’s equity at the mark price, that is, collateral value plus unrealized PnL.

Example:

- Before ADL is triggered, the system's **mark price = 3,000**.
- Due to setOracle constraints, the new mark price can only be updated to **2,970 (−1%)**.
- However, the bid side of the order book is very thin. After liquidation market orders hit the book, the **actual average execution price = 2,910** (−3% relative to 3,000).
- Losses on long positions are settled at **2,910**, potentially pushing the isolated position value below zero and creating a shortfall, which triggers **ADL**.
- ADL then selects opposing-side (profitable shorts) positions and forcibly reduces/closes them at **previous mark price = 3,000**, shifting the shortfall into **''the winning side passively earning less''**.

## 0x2 Builder Risk Landscape

Under HIP-3, risk is no longer abstract or purely theoretical for builders. Through staking and validator-governed slashing, operational failures and misconfigurations can translate directly into economic penalties. As a result, understanding how slashing is triggered, and what types of builder behavior can lead to it, becomes central to the builder’s risk model. Accordingly, this section first explains the slashing mechanism as the accountability framework, and then analyzes the two primary sources of builder risk under HIP-3.

### 0x2.1 Slashing Mechanism and Accountability

HIP-3 enforces accountability through staking and validator-governed slashing. Slashing is strictly outcome-based. Hyperliquid does not distinguish between malicious behavior, operational mistakes, private key compromise, or third-party dependency failure.

Stake requirement: On mainnet, builders must maintain 500k HYPE staked. Even if a builder halts all of their markets, they must continue to maintain it for 30 days (responsibility does not disappear immediately because trading is halted).


If a builder's actions result in invalid state, prolonged downtime, or significant performance degradation, slashing may be triggered. Depending on severity, slashing can range from partial stake reduction to full stake burn. This design makes builders economically responsible for the full runtime behavior of their markets.

The slashing percentage is decided by validator voting, with reference upper bounds:

- Invalid state / prolonged downtime: up to 100%
- Short downtime: up to 50%
- Performance degradation: up to 20%

Slashed tokens are burned, not redistributed.


Under HIP-3, builder risk primarily originates from two sources: **internal parameter misconfiguration** and **external oracle dependencies**. The following sections examine these two sources in detail and explain how they can translate into slashing outcomes.

### 0x2.2 Risks from Internal Parameter Misconfiguration

Misconfiguration risks include excessive leverage in low-liquidity markets, improper margin table design, sudden parameter changes that render large numbers of positions liquidatable, and inappropriate use of emergency controls such as halting trading.

These risks are largely deterministic and preventable. With sufficient care, review, and operational discipline, most internal configuration errors can be avoided. While important, they are not the most structurally challenging risks under HIP-3.

#### 1. setOracle

Oracle prices typically come from the builder's relayer servers, which introduces centralization risk. If the private key leaks or the relayer suffers DDoS, the market's oracle price may be maliciously manipulated or remain divergent for a long time.

#### 2. haltTrading

The builder can cancel all orders in the market via `haltTrading` and close positions at the current mark price. This operation should be used cautiously. For example, if the market is detected to be maliciously manipulated by an attacker and `haltTrading` is called to close at mark price, it may directly realize the attacker's unrealized profit (where the attacker might otherwise struggle to find enough opposing orders), and may also lead to bad debt.

#### 3. setMarginTableIds & InsertMarginTable

- **InsertMarginTable**: defines a new margin table, specifying margin requirements and max leverage for a class of assets.
- **setMarginTableIds**: binds a market to a specified `marginTableId`.

For a low-liquidity / insufficient-market-making market, setting max leverage too high increases the probability of triggering ADL.

Suddenly switching `marginTableId` is equivalent to modifying the maintenance margin ratio of user positions, which may turn many accounts from safe to liquidatable at the same time, triggering cascading liquidations.

#### 4. setMarginModes

HIP-3 currently only allows isolated margin, and may support cross margin in the future. Within a DEX hosting both high-liquidity and low-liquidity markets, cross margin can enable risk contagion where losses in illiquid markets propagate to liquid markets. Therefore, until the official team provides a mature solution, it is not recommended for builders to introduce cross margin.

### 0x2.3 Risks from External Oracle Dependencies

For **24/7 assets**, the primary risk lies in the **accuracy and stability of external oracle services**, as well as the **centralization risks of relayer servers** discussed earlier. Any disruption, delay, or manipulation in these external dependencies can directly affect pricing integrity and downstream risk controls.

For **non-24/7 assets**, the risk surface is significantly broader and is mainly concentrated in **how oracle prices are obtained or computed during non-trading hours**.

Taking [trade.xyz](https://trade.xyz/) as an example, during off-market periods prices are derived from a combination of the **last available external oracle price** and **internal market prices**. On weekends, stock perpetual markets often suffer from severely reduced liquidity—order books become thin and market makers scale back quoting—while no external oracle prices are available to provide anchoring. Even though a hard cap on price movement is imposed (e.g., 1 / max\_leverage), this constraint can still be too loose for low-volatility assets. Price movements within this range may nonetheless trigger **large-scale liquidations or even ADL events**.

On December 14, 2025, the XYZ100-USDC market on trade.xyz—a perpetual contract tracking the NASDAQ-100—was manipulated. An attacker shorted **398 XYZ100** (approximately **$10M USDC** in notional exposure), causing severe price depegging. A large number of long positions were liquidated, and the liquidations themselves further pushed prices downward, ultimately resulting in approximately **$13M USDC** in long-side liquidations.

this is probably the first such move under the ‘growth mode’ regime on the weekend. Someone slammed the market, dropping the price of XYZ100 by more than 3% in a minute and liquidating roughly \$3M worth of positions [pic.twitter.com/XttBHfTB0D](https://t.co/XttBHfTB0D)

— bart.hl (equity perps era) (@bartdothl) [December 14, 2025](https://twitter.com/bartdothl/status/2000292798755684839?ref_src=twsrc%5Etfw)

On the other hand, during non-trading hours, the absence of a continuous and externally anchored **oracle price** forces markets to rely on a **constrained internal pricing band** formed by the "last external price + internal order book" (e.g., trade.xyz caps max fluctuation at 1/max\_leverage).

The most critical risk emerges at the **market reopening transition**. External markets can suddenly provide a **clear and authoritative reference price**. If this price exhibits a significant gap relative to the internal off-hours pricing, the system faces two unfavorable paths: either prices remain **clamped**, resulting in a severe divergence between external fair value and tradable prices, or the system rapidly switches back to external anchoring, triggering **abrupt repricing**. Both scenarios can concentrate liquidation pressure within a short time window and, in extreme cases, lead to a **surge in ADL events**.

## 0x3 Builder Risk Controls

Configuration discipline alone cannot eliminate risk. The most effective mitigation strategies focus on reducing exposure to oracle dependency failures.

### 0x3.1 Selecting Stable Oracles

For **non-24/7 traded assets** such as equities, the primary challenge lies in **pricing during off-market hours**. During these periods, stable and externally anchored price references are scarce, making markets more susceptible to manipulation or endogenous drift under thin liquidity.

Currently, industry approaches generally fall into two directions:

- **Suspending oracle updates and restricting trading during off-market hours**.
For example, the Lighter protocol only accepts reduce-only orders when the underlying market is closed.Protocols such as Ostium further reduce maximum leverage during off-market hours and forcibly liquidate positions that exceed the new limits.
- **Adopting an ''internal pricing” mechanism''**, as seen on trade.xyz, where the protocol continues operating during off-hours by relying on internal liquidity and pricing algorithms when external data is unavailable.

These two approaches reflect a fundamental trade-off between **security** and **user experience**.The first approach prioritizes strict risk controls but significantly degrades trading continuity and user experience. The second preserves continuous trading but, due to the lack of external references, increases the risk that internal prices diverge from the asset's fundamental value.

During off-market periods, protocol pricing should avoid fully degenerating into a **purely internal price**. Instead, introducing **external reference anchors** can reduce depegging and gap risks. Possible references include:

- **Blue Ocean ATS**. As an after-hours/overnight trading venue, it can provide a degree of **continuous price reference** during closures (more timely than "last close"), helping generate closure-period oracle price or serving as a monitoring baseline for depegging.
- **IG Weekend CFD Quotes**. Weekend CFD quotes can provide an **alternative price signal reflecting** ''weekend market expectations'', suitable as an external anchor or monitoring comparison during closures to help detect in advance the likely direction and magnitude of an ''opening gap''.

The common characteristic of these sources is their ability to provide price signals during off-market hours. However, they do not share the same market structure as the underlying spot market and are therefore better suited as anchors, references, or early-warning signals, rather than unconditional substitutes.


### 0x3.2 Price Verification

Under HIP-3, oracle prices are sourced from **builder-operated relayer servers**, which introduces concerns around ***centralization***. To mitigate this, builders are encouraged to implement a **price verification framework** that allows any user or institution to verify pricing correctness and fairness off-chain—similar to RedStone, which packages prices together with data sources and cryptographic proofs.

#### 1. Data Transparency

- **Algorithm specification**: publicly disclose pricing algorithms and computation logic.
- **Data source list**: all sources should be public, immune to builder manipulation, and documented with detailed interfaces and parameters.
- **Price submission rules**: permissions, triggering conditions, update frequency, and volatility constraints for `setOracle`.

#### 2. Price Proofs

For each `setOracle` call, generate a corresponding proof containing:

- **Inputs**: raw (or normalized) responses from each data source at the sampling timestamp.
- **Computation**: reproducible intermediate values at every calculation step.
- **Outputs**: the oracle price submitted on-chain.

Each proof is serialized into a `proofHash`, which is then signed by the `oracleUpdater`.

#### 3. On-Chain Commitments

- Maintain a sequential list of `proofHash` entries in a Merkle tree.
- Periodically (e.g., hourly or daily) publish the MerkleRoot on-chain.

#### 4. Verification

- Provide open-source tools or a webpage where users input a time range or a `setOracle` transaction hash
- Verify signatures, timestamps, and MerkleRoot, etc.
- Recompute oracle prices using the public algorithm for comparison.

### 0x3.3 Risk Monitoring

Price verification makes `setOracle` **recomputable** and **auditable**, establishing whether price feeds are trustworthy. However, it cannot protect against live market deterioration. Feed interruptions, price divergence, and liquidity degradation—when combined with large open interest (OI)—can easily escalate localized anomalies into **systemic risks** like cascading liquidations or even ADL events.

Therefore, market abnormalities must be detected and converted into **observable signals as early as possible**, and addressed within a time window to contain risk within manageable boundaries.

To make monitoring actionable rather than fragmented, we organize signals into three layers, each mapped to a distinct failure mode and response priority.

- **Price-side monitoring** detects oracle feed failures and depegging that can invalidate risk controls at the source, so it is treated as the highest priority and is typically addressed via relayer failover, open interest caps, and leverage reductions.
- **Order book-side monitoring** captures liquidity withdrawal and spoofed depth that amplify liquidation slippage and shortfall risk, so interventions focus on limiting incremental exposure and forcing de-leveraging when fragility increases.
- **Position-side monitoring** tracks rapid open interest buildup and one-side concentration that make markets vulnerable to cascades, and is generally lower priority than price and liquidity signals, serving primarily as an early warning layer that informs tighter caps and heightened alerts.

The following sections detail each layer in turn, along with the corresponding monitoring points and recommended actions.

#### 1. Price-Side Monitoring

**a) Oracle Feed Failure**

**Metrics**:

- Use on-chain observables to judge whether the feed is stalled:

**Thresholds**:

- Level 1: ( ∆t > 5s ) — relayer process may be stalled or blocked
- Level 2: ( ∆t > 15s ) — on-chain prices may be severely depegged and increasingly market-driven

**Actions**:

- Level 1: perform relayer health checks, switch to backup relayers, and issue alerts with health diagnostics
- Level 2: call `setOpenInterestCaps` to reduce the OI cap

**b) Price Depegging**

**Metrics**:

- Signal A (`d1`): deviation between mark price and oracle price.

- Signal B (`d2`): deviation between order-book mid price and oracle price.

- Signal C (`d3`): deviation between mark price and mid price.

- Signal D (`ext_diff`): deviation between oracle price and external reference price.

**Threshold Logic**:

- Level 1: at least **2** of A, B, D exceed thresholds.
- Level 2: at least **3** of A, B, C, D exceed thresholds for **X** seconds.

**Actions**:

- Level 1: reduce OI cap via `setOpenInterestCaps`.
- Level 2: gradually update margin tables to reduce maximum leverage by tiers, and enable clamp mechanisms on relayers.
- Level 3: persistent alerts under Level 2 conditions. The builder then evaluates whether to invoke `haltTrading`.

#### 2. Order Book-Side Monitoring

**a) Liquidity Withdrawal**

**Metrics**:

- `depth_band(±x%)`: order book liquidity available within ±x% of mid price.
- `spread = bestAsk - bestBid`: price spread to measure spread widening.
- `aggressiveVolume_Δt`: taker volume within Δt (aggregated by trade side).
- `impact_ratio`:  indicator for market fragility (higher values indicate greater price impact vulnerability).

**Risk Patterns**:

- `depth_band` decreases while `spread` and `impact_ratio` increase.

**Actions**:

- Level 1: set `OI cap = current OI` via `setOpenInterestCaps`, limiting incremental positions.
- Level 2: force de-leverage via `setMarginTableIds`, while liquidating **high-leverage**, **high-risk positions**.

**b) Spoofed Liquidity**

**Risk Patterns**:

- Sudden spikes in `depth_band` followed by collapse within a short time window.

**Actions**:

- Level 1: call setOpenInterestCaps to set `OI cap = current OI`.
- Level 2: if **combined with severe depegging**, consider halting the market.

#### 3. Position-Side Monitoring

Position-side monitoring does not attempt to **predict price direction**. Instead, it identifies transitions from **balanced trading activity** to **one-side position accumulation**. When OI accumulates rapidly, positions become highly concentrated, and majority-side PnL reaches extremes, even minor exogenous shocks can trigger liquidation cascades or ADL events.

As a result, position-side actions typically have **lower priority** than price- and order book–side interventions.

**a) Excessive Short-Term OI**

**Metrics**:

- `OI_notional`: open interest notional.
- `Volume_24h_notional`: 24-hour notional volume.

A rapidly increasing ratio indicates a shift from active turnover to speculative position buildup and often precedes sharp volatility.

**Actions**:

- Level 1: trigger alerts when thresholds are exceeded.

**b) Majority-Side PnL**

**Majority side** refers to the side (Long or Short) with more position holders within the observation window.

**Metrics**:

- `avgEntry_major`: average entry price of majority-side positions.
- `size_major`: total position size of the majority side.
- `equity_major`: total equity of the majority side.

The majority-side PnL and its ratio are defined as follows:

**Actions**:

- Level 1: alert on threshold breach.
- Level 2: if it persists, consider calling `setOpenInterestCaps` to reduce OI cap.

## 0x4 Conclusion

The core narrative of HIP-3 is straightforward. It transforms market listings from a discretionary process controlled by a few into **a protocol-level capability that any qualified builder can invoke once the requirements are met**. By staking, builders can launch their own perp DEXs on HyperCore, list an initial set of markets at no cost, and acquire additional slots through auctions. This shifts market expansion from waiting for approval to **rule-based, permissionless scaling**.

What is equally clear is that HIP-3 does not eliminate risk. It **repositions and reshapes** it. Responsibilities previously absorbed by platform-level risk controls are now largely borne by builders through their inputs and operational quality. This includes oracle pricing and update cadence via `setOracle`, the selection and constraints of `markPx`, tiered leverage design through margin tables, off-market pricing ranges for non-24/7 assets, and powerful controls such as `haltTrading`, which can either contain losses or amplify them. Under thin liquidity, misconfiguration or operational failure can be magnified into liquidation cascades, gap losses, and ultimately ADL events. The question is no longer ***''Can a market be listed?''*** but rather **''Can it remain stable after listing?''**

At the protocol level, Hyperliquid addresses this redistribution of risk by converting permissions into accountable permissions. Staking, combined with validator-governed slashing, establishes clear economic consequences for builder misoperation. Constraints on pricing and leverage, including clamps, update intervals, volatility limits, and isolated margin requirements, aim to keep the most dangerous tail risks within manageable bounds. In this framing, HIP-3's value proposition becomes clear: **scaling through openness**, **safety through constraints**, and **long-term sustainability through verifiability and accountability**.

HIP-3 does not make listings freer. It makes them **more standardized**, deployable, operable, and slashable. Whether this standardization can operate at scale ultimately depends on the real-world quality of oracle design, leverage and risk parameters, and runtime monitoring. If you are designing market access rules, parameter templates, alerting systems, or emergency workflows on top of HIP-3, or if you require auditing and continuous security support, feel free to contact BlockSec at [\[email protected\]](https://blocksec.com/cdn-cgi/l/email-protection).

## Reference

\[1\] https://hyperliquid.gitbook.io/hyperliquid-docs/hyperliquid-improvement-proposals-hips/hip-3-builder-deployed-perpetuals

\[2\] https://hyperliquid.gitbook.io/hyperliquid-docs

## About BlockSec

BlockSec is a full-stack blockchain security and crypto compliance provider. We build products and services that help customers to perform code audit (including smart contracts, blockchain and wallets), intercept attacks in real time, analyze incidents, trace illicit funds, and meet AML/CFT obligations, across the full lifecycle of protocols and platforms.

BlockSec has published multiple blockchain security papers in prestigious conferences, reported several zero-day attacks of DeFi applications, blocked multiple hacks to rescue more than 20 million dollars, and secured billions of cryptocurrencies.

- Official website: [https://blocksec.com/](https://blocksec.com/)
- Official Twitter account: [https://twitter.com/BlockSecTeam](https://twitter.com/BlockSecTeam)
- 🔗 [BlockSec Auditing Service](https://blocksec.com/audit) : [Submit a request](https://blocksec.com/expert-contact?service=codeAuditingService)
- 🔗 [Phalcon Security APP](https://blocksec.com/phalcon/security): [Book a demo](https://blocksec.com/expert-contact)
- 🔗 [Phalcon Compliance](https://blocksec.com/phalcon/compliance)
