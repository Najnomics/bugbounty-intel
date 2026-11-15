# 🕵️ Telegram's Underground Escrow Market Moved $12B+ — Mostly on TRON

- **Source URL:** https://www.certik.com/blog/in-depth-research-on-the-telegram-escrow-market
- **Fetched:** 2026-11-15
- **Channel:** @defendor_eng
- **Telegram message:** https://t.me/defendor_eng/1571 (id 1571)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
## Executive Summary

The Telegram escrow market has gradually evolved into an underground service ecosystem that integrates escrow matching, fund settlement, merchant management, and traffic distribution, showing clear signs of “platformization” and network-based development.

From the development trajectory of leading platforms, the succession from Huione to Tudou and then Xinbi shows that the Telegram escrow market does not simply depend on the expansion of a single platform. Instead, under sustained regulatory and law-enforcement pressure, it has undergone a dynamic evolution of platform contraction, demand spillover, and absorption by new nodes.

Although several leading platforms have successively been affected by regulation, enforcement actions, or sanctions, market demand has not disappeared accordingly. Instead, it has continued to migrate toward other platforms, merchant networks, and alternative tools. New private-domain tools represented by SafeW, together with the frequent rotation of platform addresses, indicate that this ecosystem is adjusting toward a more decentralized, more concealed, and more resilient operating model.

Overall, while single-point enforcement actions can suppress the activity of leading platforms, the sustained governance of the broader Telegram escrow ecosystem still faces the long-term challenge of cross-platform migration and rapid reorganization.

## I. Current Overview of Telegram Escrow Services

In recent years, the "escrow services" that developed within the Telegram ecosystem have gradually evolved from auxiliary tools used to solve trust issues in anonymous transactions into important infrastructure supporting the operation of the underground economy. By introducing third-party escrow agents and using on-chain crypto assets (mainly USDT) for fund custody and transaction matching, these services have built an alternative credit mechanism in an environment lacking legal constraints and identity-based trust.

Unlike traditional regulated escrow or payment systems, Telegram escrow services are inherently cross-border, anonymous, and low-threshold, allowing them to rapidly penetrate and expand across a wide range of high-risk and even illegal transaction scenarios. From early transaction models based mainly on simple intermediary matching to today's more complex structures combining merchant systems, automated bots, fund aggregation, and distribution capabilities, their functional boundaries have expanded significantly. They are no longer limited to a "transaction safety tool," but increasingly exhibit the multiple attributes of a "marketplace + clearing/settlement network + credit intermediary."

During this evolution, escrow platforms have not only carried large volumes of high-frequency fund flows, but have also objectively become key liquidity nodes in the underground economy. Particularly in fund-flow businesses such as OTC exchange, collection and payout, and pass-through laundering networks, the escrow mechanism has become an important hub connecting both sides of fund supply and demand, enabling previously fragmented illegal transactions to operate at scale and in a more systematic manner.

It is worth noting that, although regulatory and enforcement pressure on related platforms has continued to intensify in recent years, market demand has not disappeared. Instead, it has driven escrow services to evolve continuously from centralized platforms toward decentralized, multi-node, and even tool-based forms. This change means that the Telegram escrow system is shifting from a "single identifiable and targetable object" into a "networked structure with self-reconfiguration capability."

Against this backdrop, this report focuses on the infrastructural role of Telegram escrow platforms in the underground economy and, based on open-source intelligence and on-chain fund-flow data, analyzes their business structure, evolutionary path, fund-flow characteristics, and implications for AML risk control.

## II. Scope of Business

Telegram escrow platforms essentially function as comprehensive illicit and gray-market transaction marketplaces that incorporate credit-based escrow services. Their businesses can be divided into four major categories according to their functions within the illicit and gray-market value chain: **fund flows, resource supply, technical services, and high-risk applications.** Together, these four categories form a complete underground industrial loop.

*Figure 1: Business Landscape of the Escrow Market*

### 1. Fund-Flow Services

This category directly revolves around the movement of money. It is the core and largest fund-volume component of the escrow system, and is also the key area of concern for AML. The main types include:

- **OTC exchange:** conversion between crypto assets, mainly USDT, and fiat currency, including USDT-in/fiat-out and fiat-in/USDT-out flows.
- **Collection and payout:** using third-party accounts to aggregate and distribute funds, or using relatively clean funds to provide payment exits for upstream illicit proceeds.
- **Pass-through laundering/mixing:** typical underground laundering networks that provide laundering services for funds from various illicit and gray-market activities.

**Core characteristics:**

- Strong dependence on escrow platforms as credit intermediaries.
- Fund flows show high-frequency, small-value splitting and re-aggregation patterns.
- Addresses are frequently rotated and usually carry large transaction volumes.
- Widely used in the cash-out stage after fraud, gambling, and illicit-fund laundering activities.

The essential function of this category is to complete the "circulation, substitution, and route restructuring" of illicit funds.

### 2. Resource Supply

This category provides "usable resources" for various illegal activities and forms the foundational support layer of the illicit and gray-market economy.

**Main types include:**

- **Account resources:** bank cards, payment accounts, and third-party/fourth-party collection QR codes.
- **Identity resources:** real-name materials, KYC information, and corporate accounts.
- **Communication resources:** SIM cards, verification-code receiving platforms, and SMS channels.
- **Corporate and channel resources:** shell companies, payment channels, and merchant qualifications.

**Core characteristics:**

- Mostly one-off or short-cycle assets.
- Can be repeatedly resold, forming a "resource market."
- Highly coupled with fund-flow services and used to receive or process funds.

Their essential function is to provide the "landing carrier" and "identity shell" for fund flows.

### 3. Technology and Services

This category does not directly generate funds or resources, but it significantly improves the "efficiency" and "scalability" of illicit and gray-market operations.

**Main types include:**

- **Fraud technical support:** phishing sites, impersonation pages, and malware.
- **Traffic acquisition and customer acquisition:** social-media promotion, scripted chat services, and targeted data packages.
- **System deployment:** pass-through laundering systems, payment-channel systems, and back-end management panels.
- **Risk-control evasion services:** anti-detection strategies, IP proxies, and device-environment spoofing.

**Core characteristics:**

- A clear trend toward "service outsourcing."
- Increasingly refined specialization, with technology, operations, and conversion separated.
- Reusable across multiple crime scenarios.

Their essential function is to push illicit industries from "workshop-style operations" toward "industrialized assembly lines."

### 4. High-Risk Transaction Services

This category represents the final landing scenarios for the preceding three categories and directly corresponds to specific illegal and criminal activities.

**Main types include:**

- **Gambling-related activities:** platform top-ups, point settlement, and fund return flows.
- **Sexual services and companion arrangements:** transaction matching, long-term relationship maintenance, and related services.
- **Human trafficking / illegal labor:** cross-border labor movement and intermediary matching.
- **Data and account trading:** personal information, social-media accounts, e-commerce accounts, and similar assets.

**Core characteristics:**

- The transaction objects are highly non-standardized.
- They rely heavily on escrow mechanisms to reduce fraud risk.
- Both fund and resource requirements exist at the same time.

Their essential function is to use the other service categories above to conduct final illegal business activities and launder related funds.

## III. Overall Development Path

Overall, the development of Telegram escrow platforms shows certain stage-based evolutionary characteristics. However, this "stage division" is based more on observable structural changes than on strict organizational succession. These changes have also often been accompanied by stronger regulatory pressure. The following section uses leading escrow platforms at different stages as examples to analyze their evolution and development.

*Figure 2: Development Path of Mainstream Escrow Platforms*

### 1. Huione Guarantee Dominates the Market

Huione was a relatively mature early form of the Telegram escrow market, with its core characteristic being the establishment of transaction order around "platform credit."

At this stage, Huione Guarantee built a relatively stable merchant system, mainly covering fund-related businesses such as OTC exchange and card suppliers, and established fixed escrow groups, deposit mechanisms, and basic arbitration rules. This shifted transactions from fragmented matching toward platform-based organization. At one point, it surpassed Hydra and became the largest underground illicit marketplace at the time.

The structural characteristics of this stage mainly included:

- A credit-discipline mechanism centered on platform rules and reputation.
- Steady growth in merchant numbers, far ahead of other platforms.
- Funds were concentrated in a small number of core addresses, showing strong aggregation characteristics.

However, because the structure was highly centralized, this model had relatively limited resilience when facing external regulatory shocks. [Its ecosystem activity later showed obvious fluctuations under relevant enforcement actions and restrictions (opens in a new tab)](https://www.fincen.gov/news/news-releases/fincen-issues-final-rule-severing-huione-group-us-financial-system).

### 2. Tudou Guarantee Leads the Market

After Huione's activity declined, market demand shifted to other escrow platforms. Tudou Guarantee absorbed much of Huione's market demand in this process and saw a significant rise in activity.

At this stage, Tudou Guarantee became the new-generation market leader in escrow services, while other platforms also became more active. This was mainly due to the massive demand dispersed from Huione and the exposed risks of strong centralization, which together led to market fragmentation.

However, because Huione held part of the equity in Tudou Guarantee, the vast majority of its merchants migrated to Tudou to continue their operations. As a result, Tudou's market share and transaction volume surged within a short period, showing a rapid trend of catching up with Huione. It even once became the third-largest underground illicit marketplace after Huione and the dark web.

This state did not last. Affected by the U.S. [Treasury Department's sanctions against Cambodia's Prince Group (opens in a new tab)](http://www.ca-pgc.org/2026-01/09/c_188359.htm), and after the founder of Prince Group was arrested, Tudou Guarantee was forced to announce its collapse under intense political pressure.

### 3. Xinbi Guarantee Emerges

Even if a leading platform is shut down under enforcement or regulatory pressure, there may be a brief market vacuum in the short term, but a new platform will inevitably emerge to absorb that demand. Xinbi Guarantee became the next recipient after the collapse of Tudou.

Although some merchants began to diversify risk and reduce their reliance on a single market under the influence of enforcement actions against Huione and Tudou, moving to other escrow markets with some influence, Xinbi still gradually became the leading platform of this stage by relying on its innovations.

By introducing bots to standardize transaction processes, including automatic order creation, fund custody, release of assets, and partial arbitration functions, the platform also built a more complete merchant-management and traffic-distribution system. It gradually formed a multi-layer ecosystem of "escrow + merchants + agents + traffic," marking Telegram escrow's entry into a more systematic and automated stage. Its core role was no longer merely to match transactions, but to improve overall operational efficiency and concealment through technical means.

**The main characteristics of this stage included:**

- A significant increase in automation, reducing dependence on manual operations.
- Multi-address and multi-role operations, reducing single-point risk.
- The platform became closer to a "transaction operating system" than a single marketplace.

However, as its scale expanded, its risk exposure also increased. On [March 26, 2026 (opens in a new tab)](https://www.gov.uk/government/news/uk-crackdown-on-vile-scam-centres-steps-up-with-sanctions-on-illicit-crypto-network), Xinbi Group, the parent company of Xinbi Guarantee, was sanctioned by the United Kingdom. This directly led to a visible contraction in its related ecosystem in the near term, with some Telegram escrow businesses forced to suspend operations or reduce activity. This event again had a major impact on the overall Telegram escrow system:

**Short-term impact:**

- Some leading merchants suspended transactions or shifted into a wait-and-see mode.
- Fund-flow efficiency declined.
- Market confidence was shaken.

**Structural change:** business migration and the emergence of alternative tools. Some practitioners, including Xinbi Guarantee, began promoting migration to new tools. A typical example is the promotion and use of SafeW. Such tools attempt to:

- Reduce dependence on Telegram as a single platform.
- Provide a more closed or private-domain transaction environment.
- Maintain escrow functionality while improving resistance to bans and takedowns.

*Figure 3: Xinbi Guarantee Platform Migration Announcement*

In summary, the Telegram escrow ecosystem is evolving from centralized platforms toward decentralized networks and upgrading from credit-driven operations toward technology-driven operations. Its function has also gradually shifted from that of a single transaction intermediary to key infrastructure for fund aggregation and distribution. Under sustained regulatory pressure, the system has demonstrated strong resilience and replicability through continuous adaptation and reconstruction.

## IV. Fund Scale

The fund data in this section is based on the identified Collateral Address of 20 Telegram escrow platforms that were still operating as of 2026. Collateral Address refers to on-chain addresses publicly used by platforms to receive merchant deposits, security deposits, or perform fund-custody functions, and can be regarded as the core fund entry points of the platforms.

The statistical scope covers all historical inbound funds to the relevant addresses as of April 22, 2026, uniformly converted into USD value at the time of transaction, mainly denominated in USDT.

In terms of methodology, this report first identified platform addresses based on public group information, platform announcements, and on-chain interaction relationships, then supplemented aggregation by combining fund-flow directions and address-association characteristics. The final statistical analysis was conducted from dimensions such as time variation, chain distribution, and platform share.

It should be noted that escrow platforms commonly show frequent address changes, distributed collection, fund transfers through intermediaries, and partially unidentified addresses. Therefore, the results in this report are better suited as a reference for market trends and structural changes rather than a complete estimate of total market size.

### 1. Overall Fund-Scale Changes: Event-Driven Nonlinear Growth

We analyzed the monthly total fund volume of these Collateral Addresses. From the perspective of fund inflows over the past year, the fund scale of escrow platforms shows clear nonlinear changes. It does not follow a stable growth pattern or cyclical fluctuations, but instead exhibits a typical event-driven jump structure.

*Figure 4: Total Deposit Funds of Existing Escrow Platforms Over the Past Year*

#### Stage-based change characteristics

**April-October 2025: low-level stable stage, at the tens-of-millions level:**

- The market was in a state of decentralized competition among multiple platforms.
- Existing individual platforms had relatively small fund volumes and had not formed a concentration effect.
- Huione dominated the market, while existing platforms had low market share.

**November 2025: first jump, approximately USD 177M:**

- Fund scale increased by more than 20 times compared with the previous period.

**December 2025-January 2026: sustained high level, USD 2.4B-2.5B:**

- The market entered a highly concentrated stage.

**February-March 2026: high-level volatility, USD 1.6B-2.1B:**

- Funds began to diverge but remained at a high level.

**April 2026: slight pullback, approximately USD 92M:**

- Market activity declined rapidly.

#### Analysis of core driving factors

The two jumps in fund scale were mainly driven by two key events:

1. November 2025: Huione Group was sanctioned.

Huione Group, the parent company of Huione Guarantee, was targeted by the international enforcement and sanctions system, directly disabling the original core liquidity center of the escrow market. Although most funds entered Tudou Guarantee, it is evident that a large volume of funds also migrated to other escrow platforms. In essence, this represented the first structural redistribution of funds.

1. January 2026: Tudou Guarantee shut down.

Tudou Guarantee was forced to close due to investigations related to the "Prince Group case," resulting in a second contraction on the supply side of leading platforms. The impact was reflected in:

- Short-term retention of funds at a high level.
- Subsequent re-concentration toward the remaining leading platforms.
- Further decline in market confidence.

In essence, this was a second round of structural concentration reinforcement combined with confidence erosion.

It is worth noting that in April this year, as of the statistical cut-off date of April 22, the total fund scale of escrow platforms is estimated at approximately USD 1.22B on a full-month basis, down by about 40% compared with the previous month. It is clear that the UK's sanctions against Xinbi Group on March 27, while not causing an absolute operational shutdown of the platform, still exerted a certain suppressive effect on the broader illicit and gray-market economy.

Overall, changes in escrow-platform funds were not the result of organic growth, but were driven by "sanctions/shutdown" events affecting leading platforms:

**A cyclical structure of "liquidity migration -> oligopolistic concentration -> confidence erosion."**

### 2. On-Chain Fund Structure: Heavy Dependence on a Single Base Network

From the perspective of chain distribution, the current fund structure of escrow platforms shows extremely strong concentration, with funds almost entirely dependent on the TRON network.

The data shows that the vast majority of funds are concentrated on TRON, with more than USD 11.92B, accounting for 99.9% of the total. Ethereum and other public chains, such as BSC, Base, and Polygon, account for an extremely low share, totaling only USD 420,000. This structure indicates that escrow-platform operations are highly dependent on a single underlying infrastructure and have not formed a cross-chain decentralized fund-carrying system.

This phenomenon is mainly driven by three factors:

- First, the transaction-cost structure. USDT transfer fees on TRON are extremely low and, in some scenarios, close to zero. This makes it highly suitable for escrow platforms' high-frequency, small-value, multi-transaction fund-flow model.
- Second, ecosystem path dependence. TRON has long developed relatively complete illicit and gray-market infrastructure, including wallet tools, OTC exchange systems, and automated trading tools, making user migration costs very high.
- Finally, operational habits have become entrenched. Users and merchants who have used the TRON network over a long period have formed stable path dependence, and large-scale chain migration is unlikely without strong external incentives.

### 3. Market Structure: A Highly Concentrated Oligopoly

Based on the historical deposit-fund data of these Collateral Addresses, the current market remains a highly concentrated oligopoly in terms of fund share across escrow platforms. In the existing data, Xinbi Guarantee holds an absolute dominant position, with deposit funds exceeding USD 1B and accounting for more than 90% of the overall market. Other platforms combined are significantly smaller, accounting for only about 10% of the market.

*Figure 5: Comparison of Xinbi Guarantee's Leading-Platform Effect*

This structure shows that the current escrow market is still a centralized structure dominated by a single super platform. In such a structure, highly concentrated market share is not accidental, but the result of mutual reinforcement between credit mechanisms and network effects.

On the one hand, escrow services are essentially credit-intermediary services. Their core competitiveness lies in fund scale, dispute-resolution capability, and historical stability. Therefore, users often display clear "safety convergence" when choosing platforms, preferring platforms that have already formed scale advantages. On the other hand, escrow platforms have significant network effects: the expansion of the user base directly improves liquidity, which further attracts new users and merchants, forming a positive feedback loop.

At the same time, because small and medium-sized platforms lack sufficient liquidity support, they are more likely to lose user trust in high-risk environments and gradually become marginalized. This process ultimately pushes the market structure toward leading platforms and forms the current pattern of "one dominant platform + long-tail supplementation."

Taking one recent platform address of Xinbi Guarantee as the analysis object, its transaction volume exceeded USD 52M in just 20 days, demonstrating the influence of its leading-platform effect.

*Figure 6: Risk Profile of a Xinbi Guarantee Platform Address*

*Figure 7: Fund Scale of a Xinbi Guarantee Platform Address*

## V. Forecast of Future Development Trends

The successive sanctions against Huione, Tudou, and Xinbi Guarantee were not isolated incidents, but stage-based outcomes of continued regulatory pressure on the underground transaction system. Unlike in the past, however, Xinbi Guarantee's adjustment path in response to sanctions may mark the Telegram escrow ecosystem's entry into a new evolutionary stage. Its impact is no longer limited to the contraction of a single platform, but has begun to transmit across the entire industry and drive systemic changes in market behavior.

Based on current feedback, merchants may no longer rely on a single escrow platform over the long term. Instead, they are likely to adopt multi-platform operations or even decentralized transactions to reduce single-point risk exposure. At the same time, escrow functionality is beginning to move downward from centralized platforms to smaller teams and private-domain networks, gradually weakening the aggregation role of the original leading platforms. In this process, independent tools represented by SafeW are being promoted, transforming escrow capability from a "platform-provided service" into a "replicable technical capability" and pushing the overall system from platform-driven to capability-driven.

While the structure is becoming more decentralized, the overall confrontation model is also being upgraded. On-chain address-use strategies are becoming more dynamic: deposit-address rotation cycles have shortened significantly, and multi-address parallel operation has become normal. Transaction paths are being lengthened and made more complex through splitting, hops, and multi-layer transfers in order to reduce traceability. In addition, transactions are gradually migrating from public groups to more closed private-domain or invitation-only networks, continuously weakening platform features that were previously identifiable in a centralized manner. Compared with the earlier confrontation model centered on a single platform, the current model is closer to a distributed evasion mechanism based on network structure. The figure below shows that Xinbi Guarantee is adopting this type of strategy to respond to regulatory and enforcement pressure.

*Figure 8: Partial Fund-Flow Path of Xinbi Guarantee*

Furthermore, the emergence of tools such as SafeW is pushing Telegram escrow services into standardizing capabilities and lowering the threshold, enabling any small team with certain resources to quickly build similar functional modules and thereby weakening the control of leading platforms. At the same time, the transaction environment becomes more closed and no longer fully dependent on Telegram's public ecosystem. This change means that the original recognition target centered on "platforms" is shifting into a large number of decentralized and dynamically changing nodes, while on-chain behavior shows stronger fragmentation.

Overall, the Telegram escrow ecosystem is evolving from a "centralized market dominated by leading platforms" toward a "technology-driven distributed network." In this process, risk dispersion, structural concealment, and capability replicability have become the main characteristics, posing continuous challenges to traditional analysis methods that rely on static identification and centralized targets.

## Conclusion

The evolution of the Telegram escrow ecosystem is essentially a continuous reconstruction of "credit and fund infrastructure" within the underground economy. Under sustained regulatory pressure, its operating form has gradually shifted from an early centralized market dependent on leading platforms to a networked structure characterized by technology-driven operations and decentralized nodes. This transition has not weakened its overall function; instead, decentralization and “toolization” have improved the system's survivability and replicability, making it harder to effectively contain through single-point enforcement.

Regulatory and AML practices also need to adjust accordingly. For regulators, sanctions aimed solely at platforms are showing diminishing marginal effectiveness. A more effective future path is to shift from "cracking down on single entities" to "constraining key infrastructure," including strengthening cross-border coordination; coordinating with exchanges and stablecoin issuers to constrain fund on- and off-ramps; and implementing entry-point governance targeting key links such as OTC exchange and pass-through laundering, thereby compressing fund-flow space at the source. At the same time, attention to new tools and technological diffusion will become increasingly important, and the scope of regulation needs to extend gradually from the application layer to the technical and service layers that support these operations.

For AML providers, traditional identification models that rely primarily on address labels and static rules are becoming increasingly inadequate for highly dynamic and fragmented financial networks. Going forward, stronger capabilities in dynamic clustering and cross-cycle linkage analysis will be required, shifting the focus from simply identifying addresses to identifying networks. At the same time, combining off-chain intelligence—such as Telegram groups, bots, and merchant information—with on-chain analytics will be essential for integrated investigations. In addition, introducing higher-frequency monitoring and early-warning mechanisms, and improving responsiveness to emerging nodes and structural changes, will become a key competitive advantage.Currently, some market solutions are already moving in this direction. For example, [SkyInsights (opens in a new tab)](https://skyinsights.certik.com/zh/login) and similar platforms are seeking to integrate on-chain analytics with off-chain intelligence to support more dynamic risk detection and investigative workflows.

Overall, changes in the Telegram escrow system are pushing regulation and AML from "static identification of centralized targets" toward "dynamic identification of distributed networks." Whoever can complete this paradigm shift first is more likely to gain the initiative in the next stage of regulatory confrontation.

## FAQs

**1. What is the Telegram escrow market?**

The Telegram escrow market refers to an intermediary escrow transaction system that operates through Telegram groups, channels, or bots. Platforms usually provide transaction matching, fund custody, dispute arbitration, merchant management, and advertising/traffic services, and are widely used in high-risk or anonymous transaction scenarios.

**2. Why has the Telegram escrow market persisted over the long term?**

The core reason is that the market continues to have demand for anonymous transactions, cross-border settlement, missing trust mechanisms, and high-risk fund flows. Escrow platforms solve the trust problem in transactions between strangers through a "third-party credit intermediary." Therefore, even when leading platforms are targeted, demand migrates to other nodes.

**3. What do the rise and fall of Huione, Tudou, and Xinbi indicate?**

The changes involving Huione, Tudou, and Xinbi show that the Telegram escrow market does not depend on the long-term monopoly of any single platform. Instead, under regulatory shocks, it continuously undergoes a cyclical evolution of platform contraction, demand transfer, and absorption by new nodes.

**4. Why did the market not disappear after leading platforms were targeted?**

Regulatory actions can usually target platform entry points, core organizers, and public traffic channels, but they cannot eliminate the underlying transaction demand at the same time. After leading platforms exit, merchants, agents, and users often quickly migrate to other platforms, private groups, or alternative tools to continue operating.

**5. What illegal activities are mainly involved in the Telegram escrow market?**

Based on public group business information, fund-flow patterns, and historical cases, the Telegram escrow market is often used to support multiple categories of illicit and gray-market transactions and high-risk fund activities, mainly including:

- Settlement of funds from telecom fraud, pig-butchering scams, and similar fraud schemes.
- Money laundering and illegal fund exchange.
- Pass-through laundering, collection and payout, and bank-card trading.
- Gambling-platform top-ups, settlement, and fund return flows.
- Trading of false identity materials and illicit tools.
- Facilitation of sexual services, human trafficking, and other illegal services.
- Cross-border fund transfers and sanctions-evasion activities.

In essence, this is not merely an escrow service, but transaction-credit and payment infrastructure for multiple types of underground economic activity.

**6. How may the Telegram escrow market evolve in the future?**

In the future, the escrow market is likely to develop in a more decentralized, more concealed, and more flexible fund-dispatching direction. Some participants have already begun experimenting with private-domain tools such as SafeW to reduce dependence on Telegram as a single platform and improve resistance to bans and takedowns.

From the perspective of fund operations, this ecosystem is gradually showing the following trends:

- High-frequency updates of Collateral Address: to reduce address-exposure risk, platforms may frequently change collection addresses, Collateral Address, and intermediary addresses, shortening the usage cycle of each single address.
- Rapid fund migration: after regulatory actions, sanctions, or risk events occur, funds can quickly move to new addresses, new platforms, or other on-chain channels.
- Increasingly complex transaction paths: multi-hop transfers, multi-address splitting and aggregation, and cross-platform flows are used to increase the difficulty of fund tracing. In other words, even if a single leading platform is suppressed in the future, the overall market may continue to exist through address rotation, fund migration, and fragmented reorganization.
