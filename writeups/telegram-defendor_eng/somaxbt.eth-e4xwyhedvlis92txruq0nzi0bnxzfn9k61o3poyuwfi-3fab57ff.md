# 🕵️‍♂️ Methods of Investigating and Laundering Stolen Cryptocurrencies

- **Source URL:** https://mirror.xyz/somaxbt.eth/E4XWyHedVlIS92TXrUq0NzI0BnXZFN9k61o3pOYUWFI
- **Fetched from:** https://paragraph.com/@somaxbt/qSvhQEP7t6etOFnI4BAD
- **Fetched:** 2026-11-17
- **Channel:** @defendor_eng
- **Telegram message:** https://t.me/defendor_eng/344 (id 344)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
**1. Introduction**

**2. Understanding the Threat Landscape**

**3. What is Blockchain Forensics**

**4. Investigation Methodology**

- Recognizing On-Chain Exploits and Theft
- Define the Scope
- Data Collection & Enrichment
- Transaction Tracking
- Chain Analysis
- Collaborate & Validate
- Profile Building & Reporting

**5. Challenges in Blockchain Forensics**

**6. Analysis of Stolen Funds and Laundering Methods**

- Post-Theft Objective
- Laundering Techniques

**7. Conclusion**

The rapid rise of cryptocurrency has introduced groundbreaking innovation and global financial opportunity—but it has also brought unprecedented challenges in digital security. Since 2016, the crypto ecosystem has witnessed a surge in malicious activity, with an average of **over $1.3 billion in digital assets stolen each year through hacks, scams, and protocol exploits**

These incidents range from smart contract vulnerabilities and bridge hacks to phishing campaigns, wallet drainers, and sophisticated laundering operations. What makes these crimes particularly difficult to combat is the global nature of crypto itself. While blockchain transactions are inherently transparent and traceable, enforcement is often hindered by cross-border jurisdictional barriers. Attackers routinely exploit regulatory gaps between countries, moving funds across chains and into unregulated platforms faster than authorities can respond. With no unified global standard, many investigations stall—even when the on-chain evidence is indisputable.

This guide offers a comprehensive introduction to **blockchain forensics and investigative techniques, blending core principles with advanced analysis methods.** Designed for both aspiring and active investigators, it provides a structured, practical framework for analyzing stolen funds, understanding attacker behavior, and using the tools required to follow money across chains.

To succeed as a blockchain investigator, one must first understand the **foundational elements of the technology itself how blockchains work, how they differ from traditional finance, and why their transparency is both a strength and a vulnerability in the context of financial crime.** This report is structured to take readers from those fundamentals into the real-world methodologies that drive modern crypto investigations.

Crypto doesn’t just attract innovation—it attracts attackers. As billions of dollars flow through decentralized protocols and open financial systems, so too does the attention of increasingly sophisticated threat actors. What began with isolated phishing scams has evolved into a complex ecosystem of smart contract exploits, bridge hacks, wallet drainers, laundering-as-a-service operations, and state-sponsored cybercrime.

These threats span a wide spectrum:

- **Protocol-level vulnerabilities** exploited through flash loans or logic flaws
- **Cross-chain bridge hacks** that drain liquidity by bypassing validation mechanisms
- **Automated wallet drainers and scam token contracts** deployed to target unsuspecting users
- **Phishing campaigns and front-end compromises** that exploit trust in legitimate platforms
- **Nation-state-aligned attacks**, such as those linked to DPRK—and more recently, the **Gonjeshke Darande (Predatory Sparrow)** group, which exploited the Iranian exchange **Nobitex** as part of a regionally targeted financial disruption

If you want to explore these threats more comprehensively from scam tactics and laundering playbooks to real-world attack breakdowns these resources offer valuable insights:

- **[Illicit Crypto Ecosystem](https://www.trmlabs.com/resources/reports/the-illicit-crypto-ecosystem-report-2022)** Report by [TRM Labs](https://x.com/trmlabs)
- [The Crypto Threat Landscape: Threats and Exploits Targeting Crypto Users](https://mirror.xyz/somaxbt.eth/PcTxjP1wUuutwmFizHYuzG33nJm1hx8i66iQ-T7y210)

**Blockchain forensics** is the process of analyzing on-chain activity to trace the flow of digital assets, detect illicit behavior, and uncover patterns used in financial crimes involving cryptocurrencies. It combines technical analysis, behavioral clustering, and investigative techniques to follow how funds move across wallets, protocols, and chains—often in real time and with complete transactional transparency.

Unlike traditional financial investigations that rely on private banking records or institutional access, blockchain forensics operates on **open, immutable, and decentralized ledgers**. Investigators can monitor wallet interactions, decode smart contract activity, detect laundering strategies, and, in some cases, attribute wallet behavior to real-world actors using open-source intelligence (OSINT).

***For example***\*, in the 2016 Bangladesh Bank heist—widely attributed to DPRK—the investigation depended on internal banking records, SWIFT logs, and government cooperation, limiting who could trace the funds. In contrast, the recent Bybit exchange hack could be analyzed by any qualified investigator globally using public on-chain data and forensic tools, without needing institutional access.\*


- **Transparency:** Public blockchains record every transaction on a distributed ledger, enabling full visibility into token transfers, swaps, contract interactions, and bridge activity. Investigators can reconstruct entire fund flows, step by step, using open data.
- **Pseudonymity:** While addresses are public, they aren’t tied to real identities. Blockchain forensics focuses on clustering wallets based on behavior, identifying repeated patterns, and correlating with external data (e.g., exchange logs, social media, or leaked info) to uncover the entities behind them.
- **Immutability:** Transactions on a blockchain cannot be altered or deleted. This makes blockchain forensics **evidence-based and auditable**, allowing investigators to revisit old cases, validate claims, and establish historical fund flows without fear of data manipulation.
- **Global Accessibility:** On-chain data is not restricted by borders or institutions. Whether you're a protocol developer, exchange analyst, or independent investigator, you have access to the same dataset—making investigations decentralized and more democratized than traditional finance.

- **Tracing Stolen Funds:** After a hack or exploit, forensics is used to follow how the attacker moved assets—from the exploit transaction to token swaps, bridging, mixing, or off-ramping. This helps identify laundering routes and potential recovery opportunities.
- **Detecting Laundering Patterns:** Attackers often try to hide their tracks using mixers (e.g., Tornado Cash, Railgun), micro-splitting across wallets, or bridging funds across chains. Forensics helps detect these methods and reveal hidden linkages in the transaction trail.
- **Monitoring Scam Tokens and Rug Pulls:** Investigators use on-chain data to track scam tokens, sudden liquidity withdrawals, coordinated wallet behavior, and repeated abuse patterns. This is essential for identifying malicious actors in the memecoin, NFT, or airdrop space.
- **Supporting Compliance and AML:** Forensics tools are used by exchanges, DeFi protocols, and investigators to meet compliance obligations, detect high-risk users, and file reports on suspicious activity. Wallet screening and transaction monitoring help prevent illicit financial flows from entering regulated platforms.
- **Assisting Protocol Teams and Law Enforcement:** Blockchain forensics supports both internal protocol teams and external law enforcement with actionable insights, fund freeze alerts, evidence documentation, and technical attribution that leads to recovery, sanctions, or legal action.

*For a more detailed glossary of blockchain investigation terms, refer to*

[https://www.elliptic.co/learning-resources#glossary](https://www.elliptic.co/learning-resources#glossary)

Investigating crypto crimes requires a methodical and well-structured approach, as the decentralized and pseudonymous nature of blockchain networks can make tracking illicit activities both complex and time-sensitive.Below is a step-by-step methodology designed to guide you through each stage of the forensic process from identifying an incident and tracing stolen funds to clustering wallets and building attribution.

Identifying a potential exploit or theft is the first critical step in any blockchain investigation. While every transaction on public blockchains is visible, malicious activity often blends in with legitimate traffic—making pattern recognition a vital skill.

Experienced investigators develop the ability to distinguish normal operational behavior from suspicious or malicious activity. For beginners, this skill can be built by learning the common signs of compromise, understanding protocol behavior, and closely following real-world case studies.

**What Does an On-Chain Theft Look Like?**

Crypto theft doesn’t always announce itself with a flashing red alert. Instead, it often begins with subtle transaction behavior that escalates quickly. Some early red flags include:

- **Sudden large outflows** from known exchange, protocol, or multisig treasury wallets
- **Unusual token swaps** involving governance tokens, staked assets, or illiquid LP tokens
- **Approvals to suspicious contracts**, followed immediately by token transfers
- **Bridging activity** moving funds to obscure chains or known laundering zones
- **Out-of-character behavior** from long-dormant wallets suddenly going active
- **Rapid fund distribution** across dozens or hundreds of wallets in short bursts

These patterns often indicate that a wallet or contract has been compromised, a backdoor has been exploited, or a scam has reached its execution phase.

**Common Sources of Exploit Discovery -**

Before official confirmations surface, many blockchain exploits are first detected through community alerts, unusual on-chain activity, or monitoring tools. Being aware of where incidents typically emerge—and knowing how to verify them—can help investigators respond quickly and accurately.

**1. Threat Monitoring & On-Chain Auditing Firms**

- In the rapidly evolving crypto ecosystem, specialized firms play a critical role in detecting and responding to exploits. These organizations combine on-chain surveillance, behavioral analytics, and security auditing to identify suspicious activity across major protocols, bridges, and exchange wallets—often in real time.

- **[PeckShield](https://x.com/PeckShieldAlert)** – Known for real-time incident alerts and exploit monitoring
- **[CertiK](https://x.com/CertiK)** – Offers Skynet surveillance and publishes exploit dashboards
- **[SlowMist](https://x.com/MistTrack_io)** – Provides AML, transaction tracing, and incident reporting
- **[Cyvers](https://x.com/CyversAlerts)** – Real-time transaction anomaly detection for DeFi protocols
- **[Hexagate](https://x.com/hexagate_)** – Focuses on on-chain detection and front-running protection
- **[BlockSec](https://x.com/Phalcon_xyz)** – Specializes in DeFi security auditing and attack simulations
- **[OpenZeppelin](https://x.com/OpenZeppelin)** – Advanced audit firms often publish postmortems on complex protocol failures

These firms often detect and flag malicious behavior within minutes of an exploit, making them a valuable source for investigators. Many operate public Twitter/X accounts or Telegram channels, where they share verified incident alerts, compromised addresses, and early-stage breach indicators.

✅ *Tip: Follow multiple firms for broader coverage. Each specializes in different chains, contract types, or detection methods*


**2. Independent Investigators**

Alongside security firms, a growing network of **independent blockchain investigators** has become instrumental in detecting and exposing on-chain exploits, frauds, and market manipulation. These individuals often work without institutional backing but contribute significantly through deep on-chain analysis and timely public disclosures.

Their investigations have led to exchange crackdowns, influencer accountability, and connections between hacks that went previously unnoticed.

- [@zachxbt](https://x.com/zachxbt) – Known for tracing stolen funds and exposing crypto influencers involved in fraud
- [@spreekaway](https://x.com/spreekaway) – Real-time updates on protocol exploits and attacker wallets
- [@tayvano\_](https://x.com/tayvano_) – Specializes in wallet security, phishing kits, and token approval drainers
- [@Iamdeadlyz](https://x.com/lamdedlyz) – Tracks on-chain scams, airdrop exploitation, and protocol vulnerabilities
- [@jconorgrogan](https://x.com/jconorgrogan) – Shares wallet-based research and macro insights linked to real-world actors
- [@WazzCrypto](https://x.com/wazzcrypto) – Known for memecoin-related exploit monitoring and scam tracing
- [@\_iphelix](https://x.com/_imhelix) – Conducts infrastructure-level investigation of laundering paths and malicious contracts
- [@FatManTerra](https://x.com/fatmanterra) – Rose to prominence during the Terra collapse; later provided key insights around FTX, helping shape early public scrutiny

These individuals often collaborate quietly or share their research openly, helping shape both public awareness and backend attribution efforts across the ecosystem. While only a few are listed here, the broader community includes many other skilled investigators contributing valuable insights behind the scenes.

✅ *Tip: Following these individuals is especially useful for catching early-stage thrats, behavioral patterns, and attribution clues that may not appear in tools or firm reports.*


Independent investigators serve as a bridge between public data and actionable insights—often pushing the industry toward faster response and accountability.

**3. Blockchain Explorers**

These are foundational tools that allow you to manually search and inspect wallet activity, transaction flows, contract interactions, and token movements.

- Etherscan / Solscan / BscScan / SnowTraceUsed to track real-time transactions, verify contracts, monitor internal transfers, and identify approvals or bridging vents.
- Phalcon / TenderlyUseful for decoding complex smart contract interactions or understanding exploits involving proxy upgrades, reentrancy, etc.

✅ *Tip: Always check token approval history and internal transactions in addition to surface-level transfers.*


**4. On-Chain Monitoring & Attribution Tools**

These tools provide visualization, clustering, and alerts that help spot unusual flows or reconnect wallets to known threats.

- [Arkham Intelligence](https://x.com/arkham)**:** Shows real-time balances, alerts, and wallet relationships across entities.
- [Breadcrumbs](https://x.com/AppBreadcrumbs) **/** [MetaSleuth](https://x.com/MetaSleuth) **/ DeBank:** Offer tracing, address clustering, tagging, and exportable transaction paths.
- [MistTrack](https://x.com/MistTrack_io) **/** [Crystal Intelligence](https://x.com/CrystalPlatform) **/** [Elliptic](https://x.com/elliptic)**:** Advanced forensic platforms offering attribution, risk scores, and investigation dashboards. Often used by professionals and compliance teams.
- [Nansen](https://x.com/nansen_ai) **/** [Dune](https://x.com/Dune) **Dashboards:** Great for monitoring bridge outflows, whale movements, and protocol-specific wallets.

On **February 21, 2025**, crypto exchange **Bybit** experienced a catastrophic security breach involving one of its Ethereum cold wallets. The exploit resulted in the theft of over **$1.46 billion** in ETH, making it one of the largest exchange-related crypto thefts in history.

[https://t.me/investigations/211](https://t.me/investigations/211)

Contrary to early speculation, this was **not a private key leak**. Instead, the attackers executed a sophisticated **smart contract logic manipulation** through a **masked transaction via a spoofed Safe UI**. According to Bybit CEO **Ben Zhou**, all wallet signers viewed a legitimate interface showing the correct transaction details and Safe URL—but the actual message they signed modified the smart contract logic of the wallet itself. Once the logic was altered, the attacker gained full control of the cold wallet and immediately drained its ETH balance.

Independent investigator **ZachXBT** was among the first to alert the community via Telegram, prompting immediate response from security teams and tracing professionals across the ecosystem.

[https://x.com/benbybit/status/1892963530422505586](https://x.com/benbybit/status/1892963530422505586)

Starting out in blockchain investigations doesn’t require mastering every tool or technique at once—but it does require discipline, curiosity, and consistency. By setting up real-time alerts, building your own threat wallet database, using multiple tools for cross-verification, and tapping into trusted investigator communities, you’ll quickly gain confidence and accuracy.

Remember: no one becomes an expert overnight. Every case you follow, every transaction you analyze, and every tool you explore builds your intuition and sharpens your skills. Document your work, stay up to date with threat trends, and keep learning from others in the space.

This is a space where **persistence pays off**, and even small discoveries can contribute to protecting the broader crypto ecosystem.

Every effective investigation begins with a clearly defined scope. This includes understanding the nature of the incident—whether it involves a smart contract exploit, wallet drainer, laundering operation, phishing scam, or centralized exchange breach—and assessing whether the investigation is both **strategically relevant and economically viable**.

💡 “Blockchain forensic investigations aren’t just about technical skill—they require significant time, coordination, and legal awareness. Recovery is never guaranteed, and not every incident justifies full pursuit.”


A critical step here is conducting a **cost-benefit analysis**. For instance, it may not be practical to spend $100,000 worth of time, tools, or legal support to recover $10,000 in stolen assets. This is especially true when dealing with slow or fragmented law enforcement channels that vary region by region.

Also consider the **scale of the event**. In large incidents like the Bybit hack—where over $1 billion was stolen and hundreds of wallets moved funds simultaneously—**a single investigator cannot realistically track the entire operation alone**. In such cases, it's essential to:

- Narrow the focus to a subset of critical wallets or high-value transactions,
- Prioritize early movements or known off-ramps,
- Work with communities or security teams when collaboration is feasible.

Additionally, assess the **tooling and infrastructure available for the blockchain(s) involved**. Some ecosystems (e.g., Ethereum, Solana) have mature explorers, dashboards, and investigation tools. Others—especially newer or niche chains—lack effective visualization platforms, indexed APIs, or even reliable explorers. In those cases, **investigations become significantly more manual and time-consuming**, requiring direct parsing of raw transactions and logs.

**Questions to Ask Before You Begin:**

- What type of crime occurred? (Exploit, phishing, laundering, etc.)
- What is the estimated financial loss?
- Are the assets traceable on-chain?
- What tools or legal pathways will be required?
- Is this investigation proportionate to the potential recovery?

By defining the scope thoughtfully, you ensure your efforts are focused, scalable, and aligned with real-world outcomes.

**Investigator Mindset: Be Self-Reliant:**

While collaboration tools and open-source intelligence can be useful, **never rely entirely on others** to solve a case. Most successful investigations are cracked by noticing a small detail that others missed—a reused address, a bot pattern, a cross-chain bridge interaction. At critical moments, you’ll need to **find your own path forward**.

“No one will hand you complete intel. Progress comes from persistence, creativity, and building your own leads. Once you’ve contributed meaningful findings, others may assist—but it starts with you.”


Once the scope is clearly defined, the next critical step is to collect and enrich data that will form the foundation of your investigation. Effective blockchain forensics relies heavily on accurate, well-organized information—sourced from both on-chain and off-chain platforms.

**What to Collect:**

The specific data points required will vary based on the type of incident, but typically include:

- Wallet addresses: attacker, victim, intermediaries, funders
- Transaction hashes: initial exploits, swaps, or bridge transfers
- Smart contract addresses: malicious contracts, routers, bridges
- Token details: asset types, amounts, transaction paths
- Timestamps: to sequence key events
- Event logs: for internal contract interactions or flash loans
- Bridging data: source and destination chains, asset types
- Exchange deposit addresses: for off-ramping analysis
- Known labels and tags: sourced from open-source intel or analytics tools

This raw data must be validated and structured before tracing begins. An error at this stage—such as an incorrect wallet address or overlooked internal transaction—can compromise the entire investigation.

**Enrichment Before Tracing:**

Before analyzing fund flows, it's important to enrich the data with context. Ask critical questions like:

- Is the attacker wallet newly created or reused from another exploit?
- Are the transaction patterns similar to known laundering behaviors?
- Is this contract obfuscated or copied from previous malicious deployments?
- Are tools like automated drainers, mixers, or bridges being used?

Data collection is not overly complicated and typically does not require expensive software In most cases, investigators can begin by using free tools such as public blockchain explorers (e.g., Etherscan, Solscan) to gather relevant transaction data, wallet addresses, and contract interactions. To enrich your investigation, you can also study historical incidents, leverage previously attributed wallet addresses, and reference free datasets shared by the community. Proper attribution and historical context can significantly enhance the accuracy and depth of your findings.


**For Example What Data to Collect in The Bybit Case**

To begin investigating this incident, the following data points are essential:

- **Victim Address**:(Bybit in this case) 0x1Db92e2EeBC8E0c075a02BeA49a2935BcD2dFCF4
- **Attacker Wallet**(s): 0x47666Fab8bd0Ac7003bce3f5C3585383F09486E2
- **Transaction Hashes:** These are all the transactions involved in the incident. You can identify them by labeling the victim and attacker wallets on your preferred blockchain explorer.

You can manually copy and paste them into a sheet to keep things organized, or you can extract them into a spreadsheet like this:

In the Bybit case, there is **limited on-chain data available for enrichment** or attribution, as the attack did not involve contract-level exploitation or complex laundering mechanisms initially. Instead, attackers executed a social engineering attack by exploiting the Safe (Gnosis Safe) frontend interface, presenting a manipulated transaction interface to the signers.

All transaction signers believed they were approving a legitimate transfer, but in reality, they were unknowingly signing a transaction that handed control of the cold wallet to the attacker. As a result, the stolen funds were directly transferred from Bybit’s multisig to the attacker’s wallet, without any intermediary contract interaction or typical exploit patterns that might leave behind traceable breadcrumbs.

Note: Maintain structured records of all findings from the start. Keeping logs of wallet addresses, timestamps, token flows, and known labels ensures you don’t lose track of critical leads and allows for clean visualization when presenting evidence or writing reports.


Transaction tracking is the process of tracing the movement of stolen or suspicious crypto assets across the blockchain. It involves analyzing how funds are transferred, split, swapped, bridged, or laundered by the attacker after the initial compromise. This step is critical for uncovering laundering techniques, attributing additional wallets to the attacker, and identifying potential off-ramps where intervention is possible.

Once initial data collection is complete and the relevant wallets are labeled, investigators should consider the following key points before beginning the actual tracking process:

**Key Considerations Before Starting Transaction Tracking -**

- **Watch for Immediate Asset Swaps:** Attackers often convert freeze-prone assets (such as USDT or USDC) into non-freezable, decentralized tokens like ETH, SOL, or TRX within minutes of the theft. This early swap helps them avoid asset freezes and marks the beginning of the laundering process.
- **Expect Transaction Splitting Across Multiple Wallets:** Funds are frequently split into dozens of wallets—a tactic known as "peel chains"—to obscure the trail. This creates multiple transaction paths that require parallel tracking.
- **Prepare for Dormancy:** After the initial flurry of activity, attackers may leave the funds dormant for days, weeks, or even months. This cooling-off period is used to reduce attention and delay monitoring efforts. These wallets should still be watched closely for signs of reactivation.
- **Anticipate Use of Obfuscation Tools:** Be prepared to encounter mixers (e.g., Tornado Cash), privacy layers (e.g.Railgun), and cross-chain bridges (e.g.Wormhole, Portal, or Synapse) as attackers attempt to launder assets. Cross-chain tracking capabilities are essential.
- **Set Real-Time Wallet Alerts:** Use tools like Arkham, MistTrack, or Etherscan to set alerts on known attacker wallets. These notifications allow investigators to respond instantly when funds are moved—no matter how small the amount.
- **Monitor for Micro Withdrawals to CEXs:** Attackers often attempt to cash out by sending small, fragmented amounts to centralized exchanges using fake or stolen identities. These patterns are subtle but consistent and should be flagged for further review.
- **Consider Cross-Chain Movement Early:** Many laundering operations involve bridging funds between chains. Prepare to switch between explorers (e.g., Solscan, Tronscan, BscScan) and use multi-chain analytics platforms to maintain visibility.
- **Pay Attention to Behavioral Patterns:** Analyzing transaction timing and amounts can reveal attacker routines or geographic clues (e.g., time zones, sleep cycles). These patterns can help anticipate future actions and movement.
- **Learn from Previous Incidents:** Studying past hacks and tracking operations can help identify recurring tactics and infrastructures. Many attackers reuse laundering methods or wallets across incidents.

**Example Case Study: Bybit Hack – Post-Theft Fund Movement**

On **February 21, 2025**, **Bybit** suffered a major breach resulting in the theft of:

- 401,000 ETH
- 90,300 stETH
- 15,000 cmETH
- 8,000 mETH

**Attacker Movements Post-Theft**

Shortly after the breach, the attacker **transferred the stolen stETH and mETH to a single newly created wallet**, seeded with **1 ETH for gas fees**. From this wallet, the tokens were **swapped using decentralized protocols** such as **ParaSwap** and **BreederDodo**, allowing the attacker to bypass centralized platforms and reduce the risk of blacklisting or intervention.

An attempt was also made to **transfer and launder 15,000 cmETH**, but **Mantle’s 8-hour withdrawal delay acted as a critical safeguard**, preventing the attacker from extracting the stolen funds.

For full details on the mitigation steps taken, refer to the official update from the Mantle team

[https://x.com/mETHProtocol/status/1893264673837109585](https://x.com/mETHProtocol/status/1893264673837109585)

Following the initial swaps, the attacker began splitting the 401,000 ETH into 40 separate transactions, each transferring **10,000 ETH,** to initiate the laundering process. This is a classic obfuscation technique, commonly used to fragment large holdings, slow down investigators, and increase the attacker’s chances of successfully laundering the funds.

The full list of these transactions is documented in the sheet below:

**Key Takeaways**

- **Decentralized swaps:** were used immediately post-theft to offload non-native tokens and avoid freeze actions from issuers.
- **Protocol-level safeguards**: like Mantle’s withdrawal delay, played a decisive role in halting the theft of cmETH mid-execution.
- **ETH obfuscation through batch splitting:** was used to fragment and conceal the origin of stolen funds.
- **Real-time monitoring and early wallet labeling:** enabled investigators to trace movements and respond quickly.

*This case illustrates how protocol-level defenses, combined with real-time transaction tracking, can significantly reduce attacker success—even in high-value, large-scale thefts.*


Chain analysis refers to the structured examination of blockchain activity with the goal of uncovering deeper insights into the behavior, infrastructure, and relationships between wallets involved in suspicious or illicit transactions. Unlike basic transaction tracking—which focuses on tracing the flow of stolen assets—chain analysis provides a broader, contextual view of an attacker's strategy. It helps investigators identify patterns, detect wallet clusters, attribute behavior to known entities, and surface laundering methods across multiple chains and services.

This analytical layer is critical in complex cases where attackers fragment funds, utilize privacy tools, or attempt to disguise ownership through layered transactions.

**Objectives of Chain Analysis**

- **Identify Wallet Clusters:** Group addresses likely controlled by the same entity based on behavioral heuristics, transaction timing, and shared funding patterns.
- **Map the Laundering Infrastructure:** Understand the attacker's use of specific tools—such as DEXs, cross-chain bridges, and mixers—and trace the laundering strategy over time.
- **Detect Behavioral Signatures:** Profile the attacker by analyzing transaction frequency, preferred tools, gas settings, or operational timing (e.g., consistent activity windows).
- **Surface Additional Linked Addresses:** Uncover previously unknown wallets that interact with or mirror the behavior of known attacker-controlled addresses.
- **Support Attribution and Escalation:** Provide evidence to aid in attribution, allowing for escalations to centralized exchanges, protocols, or relevant authorities for potential asset recovery or blocking.

**When to Apply Chain Analysis**

Chain analysis becomes especially valuable in the following scenarios:

- When stolen assets are fragmented across multiple wallets, making direct tracking difficult
- When the attacker uses mixers, DEXs, or cross-chain bridges to obfuscate fund movement
- When behavioral patterns or wallet activity suggest the use of automation or prior infrastructure
- When investigators need to attribute wallets to known actors, past hacks, or flagged entities
- When preparing reports for exchanges, protocols, or law enforcement that require contextual analysis
- When attempting to surface hidden relationships or wallet clusters that weren’t immediately visible during initial tracking
- When funds move across chains, and tracking requires pivoting between multiple blockchain ecosystems
- When investigating cases with potential social engineering, phishing campaigns, or wallet reuse

**Common Techniques in Chain Analysis**

**Tools Commonly Used in Chain Analysis**

Renowned crypto investigator **[ZachXBT](https://x.com/zachxbt)** has shared a list of tools he commonly uses for both on-chain and OSINT investigations. His toolkit highlights the importance of combining blockchain analysis with open-source intelligence to trace funds, uncover identities, and verify connections. A screenshot of his recommended tools is included below:

**Chain Analysis Example: Bybit Hack Linked to Multiple Past Exploits**

A powerful demonstration of effective chain analysis emerged during the 2025 Bybit hack. While tracing the laundering of stolen funds, **ZachXBT** publicly revealed that the attacker was linked on-chain to several previous exchange breaches — including **Poloniex**, **Phemex**, and **BingX**. The same entity was identified using **similar laundering patterns**, **fund flows**, and **wallet infrastructure** across all four incidents.

[https://x.com/zachxbt/status/1893211577836302365](https://x.com/zachxbt/status/1893211577836302365)

During my own investigation, [I also uncovered on-chain links to the](https://x.com/somaxbt/status/1894613344826294462) [AlphaPo/Coinspaid hack (2023)](https://x.com/somaxbt/status/1894613344826294462)[.](https://x.com/somaxbt/status/1894613344826294462) In that case, attackers consolidated small batches of Bitcoin, bridged the funds to Ethereum, swapped them into **USDT**, and then used **Bridgers(.)xyz** to move assets to other chains — a pattern mirrored in the Bybit laundering process.

This example illustrates how chain analysis not only reveals laundering tactics but also connects seemingly isolated incidents. It surfaces **repeat actors** and highlights the **reuse of laundering infrastructure** across different hacks, timelines, and ecosystems.

These overlaps are not coincidental. Multiple blockchain investigators — including ZachXBT — attribute these incidents to the **Lazarus Group**, a **DPRK-linked nation-state APT**, based on extensive on-chain evidence, recurring behavioral patterns, and infrastructure reuse. The Bybit hack adds further weight to that attribution.

**Laundering Methods Used in the Bybit Hack**

After the initial theft and token swaps, the attackers began moving large portions of the stolen assets off Ethereum. The majority of the stolen **ETH was bridged to Bitcoin** using services such as **eXch** and **THORChain**, closely following the laundering patterns seen in previous **North Korea–linked exploits**.

Once the assets were converted to Bitcoin, the attackers employed mixing tools to obscure the trail. Hundreds of thousands of dollars in BTC have already been laundered through:

- **Cryptomixer** – A **centralized Bitcoin mixer** that pools user deposits and redistributes them with new inputs. Operating since 2016, it has evaded law enforcement scrutiny, making it a trusted tool among experienced laundering operators.
- **Wasabi Wallet** – A **non-custodial privacy wallet** that utilizes **CoinJoin transactions** to anonymize Bitcoin movements. Unlike centralized mixers, it uses a coordinator to facilitate the process without taking custody of user funds.

This approach — bridging to Bitcoin followed by layered mixing — represents a **deliberate, high-level laundering strategy**, consistent with the tactics commonly attributed to the **Lazarus Group**.

To support the investigation and encourage global collaboration, **Bybit launched a dedicated website** providing structured data, wallet details, and real-time updates — an uncommon but valuable move in response to a major crypto crime.

**Investigator Insight: Chain Analysis in Practice**

Chain analysis is where investigators uncover the bigger picture. It involves dissecting laundering patterns, recognizing infrastructure reuse, and connecting incidents that appear unrelated at first glance. Skilled investigators organize their findings into private libraries of wallet clusters, tools, and behavioral signatures, which become invaluable resources for future cases.

While some findings are shared publicly to expose threat actors and alert the community, much of the deeper analysis remains private to protect investigative methods and prevent tipping off adversaries.

For new investigators, this is an opportunity. With consistent practice, curiosity, and access to publicly available data from past hacks, anyone can build the skills to conduct effective chain analysis and contribute to the fight against crypto crime.

In blockchain investigations, **collaboration and validation** are critical for increasing both the accuracy and impact of your findings. No matter how experienced the investigator, working in isolation can lead to missed patterns, blind spots, or unverified assumptions.

Sharing findings—such as wallet connections, laundering patterns, or entity attribution—with a **trusted network of peers** allows for cross-verification, fresh perspectives, and sometimes critical new leads. This collaboration doesn’t always mean going public; often, it takes place in **[private investigator groups](https://t.me/ETHSecurity)**, **Telegram circles**, or **platforms like** **[SEAL-ISAC](https://www.securityalliance.org/intel)**, where professionals coordinate quietly but effectively.

At the same time, **validating your conclusions** is just as important as reaching them. Before labeling a wallet or attributing an incident to a known group:

- **Re-check behavioral patterns:** across multiple tools.
- **Corroborate your findings:** with threat intelligence sources or previous cases.
- **Consult with other investigators:** who may have seen similar indicators.

Many successful attributions—like linking the Bybit hack to past exploits—only gained credibility through multi-party confirmation and shared knowledge.

🔍 **Tip:** *Always document your reasoning and evidence. Good validation is not just about being right, but being able to show why you’re right.*


Collaboration and validation don’t just strengthen the findings — they protect your credibility, reduce false positives, and make your work actionable for exchanges, protocols, and the broader community.

Once the on-chain investigation is complete and key findings are validated, the final step is to **build a threat profile** and document your conclusions in a clear, actionable report. This stage transforms raw blockchain data into intelligence that can be used by exchanges, protocols, security teams, or law enforcement.

Profile building involves summarizing the attacker’s behavior, methods, and possible identity indicators. A good threat profile includes:

- **Wallet clusters** linked through behavior, timing, or gas usage
- **Infrastructure used**, such as DEXs, bridges, mixers, and contracts
- **Laundering techniques** (e.g., batch splitting, cross-chain routing, use of privacy tools)
- **Attribution evidence**, such as similarities to past hacks or connections to known threat groups
- **Tactics, techniques, and procedures (TTPs)** that match previously observed threat actor behavior

The goal is to paint a clear picture of how the attacker operates—not just what they did in one incident.

Reporting is about making your investigation **understandable and actionable** for others. Depending on your audience, your report may be shared with:

- **Exchanges or protocols**, to request freezes, blacklisting, or internal monitoring
- **Security researchers or investigative peers**, for collaboration and continued tracking
- **Public audiences**, when the intent is to raise awareness or expose threat actors
- **Law enforcement or compliance teams**, with structured evidence and timelines

A strong report should include:

- A concise summary of the incident
- Timeline of events with key transactions
- Visuals (wallet flow diagrams, transaction graphs, or address maps)
- Supporting data (wallet addresses, TX hashes, tags, screenshots)
- Clear recommendations or conclusions

🧠 **Tip:** Use structured formats, avoid speculation, and always distinguish between confirmed facts and assumptions. This protects your credibility and helps others act on your findings.


This methodology outlines the **core investigative process** used to track stolen assets, uncover laundering patterns, and attribute blockchain-based crimes. From defining a clear scope to building detailed threat profiles, each phase plays a critical role in transforming raw on-chain data into actionable intelligence.

Effective blockchain investigation is not just about tracing transactions — it’s about understanding behavior, validating findings, and communicating clearly with those who can act: protocols, exchanges, communities, and enforcement bodies.

Whether you’re a new investigator or an experienced analyst, applying this structured approach improves the **accuracy, credibility, and impact** of your work. As threats evolve, so must our ability to **collaborate, document, and respond**—not only to stop bad actors but to make crypto safer for everyone.

Despite the transparency of blockchain networks, crypto investigations are far from straightforward. Investigators face a wide range of **technical, operational, and legal challenges** that can slow progress, obstruct attribution, or prevent asset recovery altogether. Below are the most critical barriers commonly encountered during on-chain investigations:

- **Cross-Border Jurisdiction and Enforcement:** Cryptocurrency transactions are global, but enforcement is not. Attackers exploit this fragmentation by routing funds through unregulated jurisdictions and services with weak or nonexistent AML enforcement. Even when stolen funds are traced, the absence of international legal coordination often delays or prevents seizure, prosecution, or restitution.
- **Use of Privacy Tools and Obfuscation:** Mixers like Tornado Cash, Railgun, Wasabi Wallet, and protocols like Samourai Whirlpool introduce significant noise into transaction trails. In combination with tactics like peeling chains, micro-splitting, and gas obfuscation, these tools make forensic reconstruction difficult—even for well-equipped investigators.
- **Cross-Chain Laundering**: Bridges and wrapped tokens allow attackers to move funds across blockchains in minutes. Many cross-chain protocols lack real-time visibility, unified indexing, or forensic tooling, creating blind spots where asset flow becomes untraceable—particularly on smaller or emerging chains.
- **Pseudonymity and Lack of Identity Ties:** Even with a complete on-chain transaction history, wallet addresses are pseudonymous by default. Without access to off-chain intelligence, exchange KYC, or OSINT indicators, linking wallet activity to real-world identities remains extremely difficult.
- **Limited Tooling on Some Chains:** Not all blockchains have mature forensic infrastructure. Newer or less popular chains may lack reliable explorers, public APIs, or labeling support. This forces investigators to manually decode transaction data, parse bytecode, or reverse-engineer contract interactions—slowing down critical investigations.
- **Limited Cooperation from Centralized Platforms:** While some regulated exchanges respond quickly to tracing requests, others—especially offshore or unregulated platforms—delay or ignore investigator outreach. Many attackers exploit this gap by cashing out through platforms that don’t comply with freeze requests or subpoenas.
- **Rapid Obfuscation and Automation:** Sophisticated attackers increasingly use automated scripts to fragment funds across hundreds of wallets within minutes. Transactions are often broken into sub-dust values, combined with gas manipulation or delay tactics to evade detection and disrupt tracing efforts in real time.
- **Evolving Tactics by Threat Actors**: Threat actors constantly adapt their laundering techniques. This includes shifting to under-monitored chains, deploying custom laundering contracts, or utilizing “laundering-as-a-service” tools. Investigators must maintain constant learning and monitoring to stay ahead of these threats.

The theft of digital assets has become a persistent and evolving threat within the cryptocurrency ecosystem. From large-scale exchange hacks to highly targeted social engineering attacks, the value of stolen crypto runs into billions of dollars annually. However, the theft itself is only one phase of the crime. What follows—the laundering of these illicit funds—is equally critical and far more complex.

This section explores how stolen crypto assets are laundered, obfuscated, and ultimately converted into usable value. It provides a detailed examination of the common laundering techniques employed by attackers, the infrastructure that enables these activities, and the various strategies used to transform illicit funds into stablecoins, fiat currency, or privacy-preserving assets.

Once an attacker successfully exfiltrates digital assets—whether through a smart contract exploit, private key compromise, phishing campaign, or other means—the focus immediately shifts to preserving access to the stolen funds while minimizing traceability and exposure. The post-theft phase is often highly calculated, leveraging automation, cross-chain infrastructure, and knowledge of investigative blind spots.

Below are the key objectives threat actors pursue in the critical hours and days following a crypto theft:

**1. Obfuscate the Origin of Funds**

Attackers often use privacy tools before and after the theft to obfuscate both the source of funds used in the exploit and the subsequent movements of stolen assets. This includes pre-loading operational wallets via mixers (e.g., Tornado Cash) or non-custodial swaps (e.g., ChangeNOW, eXch), and then layering transactions through multiple wallets to conceal origin points.

In some cases, stolen assets are immediately bridged or swapped across chains, making real-time tracking extremely difficult. This step is crucial to avoid attribution and to disrupt investigative timelines.

**2. Break Forensic Linkages**

Blockchain forensics relies heavily on tracing transaction flows and wallet associations. Sophisticated actors deliberately introduce noise—using **peel chains**, **token shuffling**, **DEXes**, or **wrapped assets**—to complicate analysis. The goal is to sever or confuse the direct path between the source (the hacked contract or victim wallet) and the attacker's real off-ramp.

**3. Avoid Immediate Detection and Freezing**

High-profile exploits often draw fast attention from exchanges, law enforcement, and on-chain analysts. As such, attackers aim to **disperse funds rapidly** across multiple wallets and chains before any entity can respond with freezing requests. They often rely on:

- **Time-zone mismatches** (executing attacks when exchanges are offline)
- **High-speed bridging** (especially to unregulated jurisdictions)
- **Use of automation bots** for executing complex laundering flows within minutes

**Convert Volatile Assets to Stable Value**

Many stolen tokens, especially in DeFi exploits, are illiquid or volatile. Attackers frequently swap these assets for **stablecoins (USDT, USDC, DAI)** or liquid blue-chip tokens like ETH or BTC. This serves two purposes:

- Reduces exposure to price fluctuations
- Makes future laundering and off-ramping easier

**4. Monitor Investigator and Community Reactions**

Sophisticated attackers often **monitor Arkham alerts, Etherscan comments, X (Twitter), and Telegram** channels for signs that their addresses or flows have been flagged. In some cases, they adjust tactics mid-way based on public intel.

This is one of the key reasons why many investigators choose not to immediately disclose their findings publicly. Instead, they may withhold information until disclosure becomes necessary—either to support victim recovery efforts or to prompt action from exchanges and law enforcement—minimizing the chance of alerting the attacker prematurely.

After an initial theft, crypto criminals must convert the stolen assets into usable funds while minimizing the risk of detection or recovery. Given the public nature of blockchain data, laundering stolen crypto requires the deliberate use of **multi-layered obfuscation strategies** and infrastructure that exploits technical, jurisdictional, and procedural blind spots.

This section outlines the most common laundering techniques used by attackers today.

**1. Chain Hopping (Cross-Chain Laundering)**

**Chain hopping** refers to the deliberate movement of assets across multiple blockchain networks in an effort to **break forensic traceability**, fragment transaction paths, and bypass monitoring tools or compliance frameworks. This tactic is widely used by both opportunistic hackers and state-sponsored actors in the immediate aftermath of an exploit.

Attackers typically begin on high-surveillance networks like **Ethereum**, which are closely monitored by blockchain analytics firms and law enforcement agencies. From there, they quickly **bridge assets to less-regulated or lightly monitored chains**, such as **BNB Chain**, **Tron**, **Avalanche**, or **Polygon**, where transparency tools and wallet attribution are more limited.

**Table: Common Tools Used for Chain Hopping and Cross-Chain Laundering**

Why it’s Effective:

- Allows seamless movement between ecosystems with differing surveillance depth
- Most tools lack native compliance or transaction attribution
- Enables attackers to exploit low-liquidity or less-regulated chains (e.g., BNB, Tron)
- Provides a mix of token formats (wrapped assets, stablecoins, etc.) to mask flows

This method is frequently used in conjunction with mixers, NFT laundering, and micro-disbursement strategies, creating multi-chain transactional webs that frustrate investigators and delay enforcement responses.

For example, in the 2025 Bybit hack, attackers used Thorchain and eXch to bridge a large portion of the stolen funds from Ethereum to Bitcoin, making it harder to trace and bypassing KYC restrictions.


**2. Mixing Services**

Mixing services, also known as tumblers, are tools designed to obfuscate the on-chain origin and destination of cryptocurrency transactions. They achieve this by aggregating crypto deposits from multiple users, pooling them together, and redistributing the funds to new wallet addresses in a randomized and pseudonymous manner. This breaks the direct link between sender and receiver, making it significantly harder to trace the flow of funds on-chain.

Mixers can be either smart contract-based (decentralized and on-chain) or custodial (operated by centralized entities). While originally developed to enhance financial privacy, these services are frequently abused by malicious actors involved in ransomware, DeFi exploits, phishing schemes, and darknet market activity.

**How Mixing Services Work**

1. **Deposit**: The user deposits cryptocurrency into the mixer.
2. **Aggregation**: The mixer pools funds from multiple users into a shared liquidity pool.
3. **Delay & Distribution**: After a time delay, the user withdraws an equivalent amount of crypto to a new, unrelated address.
4. **Outcome**: The trail between the source and destination wallets is broken, concealing the asset’s origin.

***For example:*** in the recent Bybit hack, after bridging the stolen funds to Bitcoin via Thorchain and eXch, the attackers began mixing the assets through **CoinJoin transactions** using various Bitcoin mixing services. In contrast, during the WazirX hack, the attackers **deposited the entire stolen amount into Tornado Cash** shortly after the exploit to obfuscate the trail.

**3. Peel Chains (Micro Laundering)**

**Peel chains** are a laundering technique in which stolen crypto assets are **dispersed in small increments across a series of transactions and wallets**, often through automated scripts. Rather than moving the full amount in a single transaction—which is easier to flag and track—attackers **“peel off” small portions of the stolen funds**, sending them through long chains of intermediary wallets to slowly distance the final destination from the source.

**How Peel Chains Work**

1. **Initial Wallet**: The attacker holds a large balance in one wallet post-exploit.
2. **Incremental Transfers**: Small amounts (e.g., 0.1 BTC or 10 ETH) are sent out to new addresses in a step-by-step manner.
3. **Multiple Hops**: Each transaction funds a new wallet, which then peels off a smaller amount to the next, and so on.
4. **Exit Nodes**: Eventually, the funds reach a destination wallet used to swap, mix, or off-ramp the cleaned funds.

**Purpose and Effectiveness**

- **Avoids Detection**: Small transfers are less likely to be flagged by automated AML systems or real-time monitoring tools.
- **Increases Complexity**: Long chains of transactions complicate forensic tracing by bloating the transaction graph.
- **Time-Delayed Movement**: Peel chains can operate over days or weeks, making it harder to detect laundering in real time.

**4. Off-Ramping via P2P and OTC Brokers**

Once stolen crypto assets have been sufficiently obfuscated—through mixers, peel chains, or cross-chain swaps—the final objective for most attackers is to **exit into fiat currency or stable assets**. This process, known as **off-ramping**, is typically carried out through **peer-to-peer (P2P) platforms** or **over-the-counter (OTC) brokers** to avoid detection and bypass centralized exchange (CEX) compliance controls.

**How It Works**

- **Peer-to-Peer Platforms**: Attackers use services like **Binance P2P**, **LocalBitcoins**, or **HodlHodl** to sell crypto directly to buyers in exchange for fiat (bank transfers, mobile payments, gift cards). These platforms often have minimal oversight or allow trading through burner identities.
- **OTC Brokers**: These are **private intermediaries** or small firms that specialize in converting large amounts of crypto into fiat, usually in exchange for a percentage fee. Some OTC desks operate informally over **Telegram**, **WeChat**, or **WhatsApp**, and may offer services that deliberately ignore KYC/AML protocols.

**Why Attackers Prefer These Methods**

- **Bypass KYC**: Unlike regulated exchanges, many P2P and OTC options do not require verified identities, or they allow access through **purchased KYC’d accounts**.
- **Discreet Transactions**: OTC deals often occur off-platform and leave limited digital footprints.
- **High Liquidity**: Brokers can absorb large volumes without triggering exchange alerts or causing price slippage.

**5. Laundering via Unregulated Exchanges**

One of the most common and effective laundering techniques used by attackers is the use of **unregulated or loosely regulated cryptocurrency exchanges**, particularly those operating in jurisdictions with weak enforcement or limited oversight. These platforms allow threat actors to **swap, withdraw, or off-ramp stolen crypto into fiat or stablecoins** without triggering compliance alerts.

**Notable Examples**

- **Huione**: A widely used payment platform and exchange network, reportedly linked to entities in Cambodia. It has been frequently associated with **pig butchering scams**, fraud rings, and underground banking operations. Huione's ecosystem operates across messaging platforms like Telegram and WeChat, offering fiat off-ramps and laundering services disguised as e-commerce or financial agents.
- **Xinbi**: A lesser-known crypto exchange reportedly used in laundering stolen assets from phishing scams and on-chain exploits. Xinbi has weak KYC standards, making it attractive to actors needing to cash out without scrutiny.
- **Grantex**: A Russia-based exchange service that has been used in darknet transactions and illicit fund flows. Known for processing high-volume swaps without enforcing KYC, Grantex is frequently used by ransomware operators and actors in sanctioned regions.

**Why Attackers Use Them**

- **No KYC / AML Enforcement**: These platforms often allow anonymous trading or accept fake documents.
- **High Risk Tolerance**: They do not blacklist wallets flagged by global blockchain analytics providers.
- **Cross-Border Fiat Access**: Many support cash-out options in local currencies via informal money agents or P2P transfers.
- **Low Regulatory Oversight**: Operating from jurisdictions with limited crypto enforcement, they face little international pressure.

These exchanges often represent the final stage in a laundering operation, where previously obfuscated funds are either converted into fiat currency and withdrawn, or further transferred into privacy-focused assets such as Monero (XMR) or Zcash (ZEC). At this point, the trail becomes exceedingly difficult to follow, as many of these platforms operate outside the reach of major regulatory frameworks, do not cooperate with law enforcement or analytics providers, and often conduct off-chain settlements through informal financial networks. Once funds exit the transparent blockchain environment through these channels, investigators face significant barriers to attribution, asset recovery, or timely intervention.


As the crypto ecosystem continues to grow in scale and complexity, so too does the sophistication of illicit actors operating within it. The laundering of stolen funds is no longer a simple process—it is a **strategic, multi-phase operation** that combines privacy-enhancing tools, decentralized infrastructure, and cross-jurisdictional blind spots to evade detection.

This article has explored how attackers move from **theft to obfuscation to off-ramping**, using a range of laundering techniques such as **chain hopping**, **mixing services**, **peel chains**, and **unregulated exchanges**. It has also highlighted the supporting infrastructure—bridges, DEXes, privacy coins, and OTC brokers—that enables attackers to fragment, conceal, and ultimately convert stolen crypto into usable value.

By understanding these techniques and the tools involved, investigators and compliance teams can better anticipate the movement of illicit funds and identify chokepoints where intervention is possible. However, the challenge remains steep. Attackers are not only technically adept—they are also reactive, closely monitoring the blockchain intelligence space and adapting their laundering strategies in real time.

Effective countermeasures require more than just technical capabilities—they demand **cross-chain visibility**, **timely intelligence sharing**, and **coordinated efforts between analysts, exchanges, and law enforcement**. Education also plays a vital role: as more investigators, developers, and security professionals become aware of these laundering methods, the ecosystem becomes more resilient to future abuse.

Ultimately, disrupting crypto laundering is not just about tracking stolen funds—it's about preserving the integrity of the financial layer that powers decentralized innovation. By continuing to document, analyze, and expose these methods, we can close the gap between criminal activity and accountability, and build a safer, more transparent crypto ecosystem for all.

**Disclaimer** : *“ This article is intended for educational and informational purposes only. It does not constitute financial, legal, or cybersecurity advice. While every effort has been made to ensure accuracy, the crypto threat landscape evolves rapidly, and the information presented may not reflect the most current developments. Readers should conduct independent research and consult with qualified professionals before making decisions based on this content.*

*References to specific companies, platforms, or individuals are based on publicly available information and do not imply wrongdoing unless independently confirmed. The goal of this article is to raise awareness and encourage best practices for user safety and ecosystem security.”*
