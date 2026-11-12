# 🛡️ History of Hacks and Vulnerabilities on Solana

- **Source URL:** https://www.helius.dev/blog/solana-hacks
- **Fetched:** 2026-11-12
- **Channel:** @defendor_eng
- **Telegram message:** https://t.me/defendor_eng/906 (id 906)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Solana Hacks, Bugs, and Exploits: A Complete History

This article was selected as a track winner in the recent Helius Redacted Hackathon.

## [Key Findings and Trends](https://www.helius.dev#key-findings-and-trends)

- **Incident Frequency**: 38 verified security incidents over 5 years (2020–Q1 2025), with a peak of 15 incidents in 2022, driven by Solana’s expanding ecosystem, particularly in the DeFi and NFT sectors. Application Exploits (26 incidents) dominated, reflecting the rapid proliferation of dApps, while Supply Chain Attacks emerged as a new threat in 2024.
- **Financial Impact**: Gross losses totaled approximately **\~$600M**, with **\~$469M** mitigated through reimbursements, recoveries, and protocol interventions, resulting in net losses of **\~$131M**. Users bore the brunt of losses in incidents such as the Slope Wallet hack ($8M) and DEXX exploit ($30M), though protocols also successfully mitigated significant losses, such as Wormhole’s $326M reimbursement and Loopscale’s $5.8M recovery.
- **Affected Parties**: Users were primary victims in Application Exploits (e.g., Slope Wallet, Solareum) and Supply Chain Attacks (e.g., Web3.js, Parcl Front-End), losing funds from wallets and liquidity pools. Network-Level Attacks (e.g., Grape Protocol’s 17-hour outage) and Core Protocol Vulnerabilities (e.g., JIT Cache Bug’s 5-hour outage) disrupted the entire ecosystem, impacting users, dApps, and validators with indirect losses from SOL price volatility.
- **Response Evolution**: Response times improved dramatically from hours or days in 2020–2022 (e.g., Wormhole patched in hours, Cashio shut down same day) to minutes or hours in 2024–2025 (e.g., Thunder Terminal halted in 9 minutes, Banana Gun shut down bots in minutes). Community vigilance, including alerts from CertiK (SVT Token) and ZachXBT (NoOnes), enhanced rapid detection. Remediations shifted from reactive measures like protocol shutdowns to proactive strategies, including audits, 2FA, and real-time monitoring.
- **Security Gaps**: Persistent vulnerabilities include program bugs (e.g., Cashio’s infinite mint glitch), oracle manipulation (e.g., Mango Markets’ $116M exploit), private key management (e.g., DEXX’s $30M leak), and third-party dependencies (e.g., Thunder Terminal’s MongoDB flaw). Core Protocol incidents, such as the Turbine Failure (2023), highlight the complexity of Solana’s high-throughput architecture, necessitating robust validation and fault detection. Insider threats (e.g., Pump.fun’s employee exploit, Cypher’s $317K theft) emerged as a growing concern.
- **Mitigation Success**: Protocols like Wormhole ($326M reimbursed), Pump.fun ($1.9M restored), Banana Gun ($1.4M refunded), and Loopscale ($5.8M recovered) fully mitigated losses, demonstrating effective recovery mechanisms. Raydium partially compensated users (100% for RAY pools, 90% for non-RAY pools), while others, such as Cashio and Solareum, collapsed due to insufficient funds, underscoring the critical need for robust insurance funds and diversified risk management strategies.

## [Introduction](https://www.helius.dev#introduction)

Solana, launched in March 2020 by Solana Labs, combines [Proof-of-History (PoH)](https://www.helius.dev/blog/proof-of-history-proof-of-stake-proof-of-work-explained#what-is-proof-of-history) and [Proof-of-Stake (PoS)](https://www.helius.dev/blog/proof-of-history-proof-of-stake-proof-of-work-explained#what-is-proof-of-stake) to deliver a high-throughput blockchain, targeting 65,000 transactions per second at sub-cent fees. Its scalability has driven widespread adoption in DeFi, NFTs, and Web3 applications. Still, this growth has exposed it to an extensive array of security incidents—application-level exploits draining hundreds of millions, supply chain attacks compromising ecosystem tools, network-level threats, and core protocol vulnerabilities causing outages and risks. ***This article provides an exhaustive catalog of Solana’s security history with in-depth research to uncover every known, verified security incident using only high-quality, verified resources.*** Every incident is thoroughly, independently checked to provide authentic data while analyzing root causes, repercussions, incident responses, remediations, lessons learned, and user losses.

## [Methodology](https://www.helius.dev#methodology)

- Aggregated incidents from yearly security audits, reports, post-mortems, and various reputable sites to come up with this list.
- The list only includes high-profile, verified incidents reported on quality sites.
- Avoided low-profile, less talked about, unverified incidents, and those irrelevant to projects or Solana’s security aspect.
- We disregarded the numerous scams and rug projects seen daily and only listed incidents related to exploits or hacks on Solana.
- Hundreds of projects on the Solana ecosystem have had their Twitter, Discord, or other social accounts compromised by scammers or hackers. These incidents do not relate to the protocol/project’s application, supply chain, or network-level vulnerabilities, so they are disregarded.
- Reviewed every incident independently, comparing different sources and figures to aggregate the most accurate information.
- Reviewed technical sources (GitHub commits, npm advisories, validator logs, audit reports).
- Estimated losses using reported figures, cross-checked with SOL/USD prices at the time.
- Each incident is summarized by highlighting the root cause, repercussions, incident response, remediations, lessons learned, and user losses.
- Every incident has references and citations to verify and a list of high-quality resources.
- Evaluated the frequency of incidents, total losses, and evolution of Solana’s security response.

Incidents are categorized into four different categories I) Application exploits, II) Supply chain attacks, III) Core protocol vulnerabilities, IV) Network-Level Attacks, and listed up to Q1 2025.

## [Incident Summary](https://www.helius.dev#incident-summary)

- **Application Exploits (26 incidents)**: Wormhole Bridge, Cashio, Crema Finance, Audius, Nirvana Finance, Slope Mobile Wallet, OptiFi Lockup Bug, Mango Markets, UXD Protocol, Tulip Protocol, Solend Protocol (Aug 2021), Solend Protocol (Nov 2022) Raydium, Cypher Protocol, SVT Token, io.net, Synthetify DAO, Aurory, Thunder Terminal, Saga DAO, Solareum, Pump.fun, Banana Gun, DEXX, NoOnes Platform, Loopscale.
- **Supply Chain Attacks (2 incidents)**: Parcl Front-End, Web3.js
- **Network-Level Attacks (4 incidents)**: Grape Protocol incident, Candy Machine NFT Minting Outage, Jito DDoS, Phantom wallet DDoS.
- **Core Protocol Vulnerabilities (6 incidents)**: Solana Turbine Bug, Solana Durable Nonce Bug, Solana Duplicate Block Bug, Solana Turbine Failure, Solana JIT Cache Bug, Solana ELF Address Alignment Vulnerability.

## [Application Exploits](https://www.helius.dev#application-exploits)

**Definition**

Application Exploits are security incidents that target vulnerabilities in the software applications, programs, or protocol logic built on top of the Solana blockchain. These exploits occur at the application layer, above the core blockchain protocol, and typically involve flaws in the design, coding, or configuration of decentralized applications (dApps), wallets, or DeFi protocols. They often result in unauthorized access, fund theft, or manipulation of protocol operations.

**Characteristics**

- **Scope**: Specific to individual dApps, programs, or wallet applications, not the Solana protocol itself.
- **Common Vulnerabilities**: Include program bugs (e.g., validation flaws, oracle manipulation), insecure key management, governance loopholes, and third-party service integrations within the application.
- **Impact**: Typically results in financial losses through stolen funds, manipulated transactions, or locked assets. Impacts users, protocols, or treasuries.

**Application Level Incidents**

### [Solend Auth Bypass Attempt (Aug 2021)](https://www.helius.dev#solend-auth-bypass-attempt-aug-2021)

**Root Cause:** On August 19, 2021, an attacker exploited an insecure authentication check in Solend’s \`UpdateReserveConfig\` function. The attacker bypassed admin checks by creating a new lending market and passing it as an account they owned, enabling unauthorized updates to reserve configurations for assets like USDC, SOL, ETH, and BTC. This allowed the attacker to lower the liquidation threshold, making nearly all borrowing accounts liquidatable and increase the liquidation bonus to create significant profits for liquidators (potentially the attacker) through inflating the liquidation bonus.

**Repercussions:** The exploit attempt put approximately $2 million at risk by making nearly all accounts with borrows liquidatable at an inflated bonus. Five users were wrongfully liquidated by Solend’s liquidator bot, incurring $16,000 in losses. No funds were stolen due to timely detection and intervention by the Solend team.

**Incident Response:** Solend detected the attack within 41 minutes, mitigated it within 1 hour and 10 minutes, and deployed a fix within 1 hour and 38 minutes. Borrowing operations were temporarily suspended, and the team reconciled the wrongfully liquidated accounts, refunding $16,000 from the liquidator’s undue earnings with a 2% bonus.

**Remediations:** Solend implemented stricter code review policies, scheduled follow-up audits, increased bug bounty sizes, and added monitoring alerts. They also introduced circuit breakers and speed bumps to prevent similar exploits and patched the vulnerable authentication check in the \`UpdateReserveConfig\` function.

**Lessons Learned:** Insecure authentication checks in programs can allow attackers to manipulate critical protocol parameters. Robust access controls, thorough code audits, and real-time monitoring are essential to secure decentralized protocols, especially during early launches.

**User Losses:** Five users lost $16,000 due to wrongful liquidations, but all were fully reimbursed with an additional 2% bonus from the liquidator’s earnings. No other user funds were lost.

**References and Citations:**

### [Wormhole Bridge Exploit (Feb 2022)](https://www.helius.dev#wormhole-bridge-exploit-feb-2022)

**Root Cause**: A signature verification flaw in Wormhole’s Solana-side program allowed an attacker to forge a valid signature, bypassing Guardian validation. This enabled the unauthorized minting of 120,000 wrapped Ether (wETH) without depositing equivalent Ethereum collateral.

**Repercussions**: Approximately $326 million in cryptocurrency was stolen, making it the second-largest DeFi hack at the time. The exploit disrupted the 1:1 peg between wETH and ETH, raising concerns about cross-chain bridge reliability.

**Incident Response**: The vulnerability was patched within hours on February 2, 2022. Jump Crypto, Wormhole’s parent company, reimbursed 120,000 ETH on February 3, restoring the 1:1 backing. A $10 million bug bounty was offered to the attacker, who did not return the funds.

**Remediations**: Enhanced signature verification with stricter input validation and improved account checks to prevent spoofing attacks.

**Lessons Learned**: Cross-chain bridges require layered security, including robust validation and audits, to mitigate complex smart contract vulnerabilities.

**User Losses**: None, as Jump Crypto fully reimbursed the stolen funds, preventing direct user losses.

**References and Citations**:

### [Cashio Exploit (Mar 2022)](https://www.helius.dev#cashio-exploit-mar-2022)

**Root Cause**: A vulnerability in Cashio’s program collateral validation allowed an attacker to mint 2 billion CASH tokens using fake accounts with worthless collateral. The flaw was due to a missing validation of the mint field in the saber\_swap.arrow account, enabled the attacker to bypass checks for Saber USDT-USDC LP tokens, exploiting an “infinite mint glitch.”

**Repercussions**: Approximately $52.8 million in assets (USDC, USDT, UST) were stolen, and the CASH stablecoin’s price collapsed from $1 to $0.00005. Cashio’s total value locked (TVL) dropped from $28.8 million to $579,000, halting operations.

**Incident Response**: Cashio halted minting at 9:00 AM UTC on March 23, 2022, and urged users to withdraw funds from liquidity pools. The team identified the root cause and collaborated with Saber Labs, which paused its CASH pools. The attacker returned funds to accounts holding less than $100,000 and pledged to donate larger amounts to charity, though $25 million remained unrecovered by June 2022.

**Remediations**: The vulnerability was patched through community efforts, but Cashio did not resume operations. A proposed two-token protocol and DAO to repay victims was announced in June 2022, but no updates followed.

**Lessons Learned**: Unaudited programs are highly vulnerable to exploits, emphasizing the need for rigorous audits, robust collateral validation, and a root of trust for account verification to prevent infinite mint scenarios.

**User Losses**: $52.8 million, partially mitigated; approximately $27.8 million was returned to smaller accounts, leaving $25 million unreimbursed, with no further recovery reported.

**References and Citations**

- [**CoinDesk:** “Stablecoin Cashio Suffers ‘Infinite Glitch’ Exploit, TVL Drops by $28M,” March 23, 2022](https://www.coindesk.com/tech/2022/03/23/stablecoin-cashio-suffers-infinite-glitch-exploit-tvl-drops-by-28m)
- [**The Block**: “Stablecoin Cashio on Solana Exploited for $52.8 Million in ‘Infinite Mint Glitch’,” March 24, 2022](https://www.theblockcrypto.com/post/138934/stablecoin-cashio-on-solana-exploited-for-28-million-in-infinite-mint-glitch)
- [**Halborn**: “Explained: The Cashio Hack (March 2022),” March 28, 2022.](https://www.halborn.com/blog/post/explained-the-cashio-hack-march-2022)
- [**CertiK**: “Cashio App Incident Analysis,” December 6, 2022](https://www.certik.com/resources/blog/3bHgCDnWaqUeQJn6695bea-cashio-app-incident-analysis)

### [Crema Finance Exploit (Jul 2022)](https://www.helius.dev#crema-finance-exploit-jul-2022)

**Root Cause**: A vulnerability in Crema Finance’s Concentrated Liquidity Market Maker (CLMM) allowed an attacker to create a fake tick account, bypassing owner verification. Using flash loans from Solend, the attacker manipulated transaction fee data to claim excessive fees, draining funds from multiple liquidity pools.

**Repercussions**: Approximately $8.8 million in assets (69,422.9 SOL and 6,497,738 USDC) were stolen, impacting Crema’s liquidity pools. The attacker bridged funds to Ethereum, swapping them for 6,064 ETH.

**Incident Response**: Crema suspended their programs on July 3, 2022, and negotiated with the attacker, who returned $7.2 million (6,064 ETH and 23,967.9 SOL) by July 7, 2022, keeping 45,455 SOL ($1.6 million) as a white hat bounty. The vulnerability was patched within days.

**Remediations**: Enhanced tick account validation, owner checks to prevent fake data manipulation, and stricter flash loan protections.

**Lessons Learned**: Liquidity protocols must secure price tick data and transaction fee logic to prevent flash loan exploits, emphasizing the need for robust audits.

**User Losses**: A net loss of $1.6 million (bounty), unreimbursed; $7.2 million returned mitigated most user impacts.

**References and Citations**:

### [Audius Governance Exploit (Jul 2022)](https://www.helius.dev#audius-governance-exploit-jul-2022)

**Root Cause**: A vulnerability in Audius’ governance program allowed an attacker to submit and execute malicious proposals, bypassing proper validation. The attacker reconfigured treasury permissions, transferring 18.5 million AUDIO tokens to their wallet.

**Repercussions**: Approximately $6.1 million in AUDIO tokens (valued at the time) were stolen from the treasury, causing a temporary price drop and raising concerns about decentralized governance security.

**Incident Response**: Audius halted all programs within hours, fixed the vulnerability, and upgraded the program by July 28, 2022. No funds were recovered from the attacker.

**Remediations**: Enhanced proposal validation, added timelocks for governance actions, and migrated to a new governance system with stricter access controls.

**Lessons Learned**: Governance programs require robust validation and delays to prevent unauthorized actions, emphasizing the need for thorough audits in DeFi.

**User Losses**: $6.1 million in treasury funds lost, unreimbursed; no direct user wallet losses.

**References and Citations**

- [**Lossless**: “Audius Hack: Code-Enabled Governance Attack,” July 29, 2022](https://losslessdefi.medium.com/audius-hack-code-enabled-governance-attack-33ac9d8084c8)
- [**CoinDesk**: “How Attackers Stole Around $1.1M Worth of Tokens From Decentralized Music Project Audius,” July 25, 2022](https://www.coindesk.com/tech/2022/07/25/how-attackers-stole-around-11m-worth-of-tokens-from-decentralized-music-project-audius/?outputType=amp)
- [**GoPlus Security**: “A brief analysis of the Web3 music platform Audius exploit,” July 24, 2022](https://goplussecurity.medium.com/a-brief-analysis-of-the-web3-music-platform-audius-exploit-79b3e9884c8d)
- [**Audius Twitter (@AudiusProject)**: July 24, 2022, exploit announcement](https://x.com/audius/status/1551131385515020288)

### [Nirvana Finance Exploit (Jul 2022)](https://www.helius.dev#nirvana-finance-exploit-jul-2022)

**Root Cause**: Attacker Shakeeb Ahmed exploited a pricing mechanism vulnerability in Nirvana Finance’s program using a flash loan of approximately $10 million. By purchasing ANA tokens and manipulating the bonding curve, Ahmed minted tokens at an inflated rate, draining $3.5 million in stablecoins.

**Repercussions**: Approximately $3.5 million was stolen, collapsing Nirvana’s total value locked and halting operations. The exploit, executed by a trained security engineer, eroded user trust and marked a significant setback for the protocol.

**Incident Response**: Nirvana shut down post-exploit on July 28, 2022, and ceased communication. In 2023, Ahmed was arrested and pleaded guilty, with $12.3 million in restitution ordered. By September 2024, Nirvana launched a claims portal, distributing 60% of restitution funds to affected users by December 2024.

**Remediations**: Due to the shutdown, no immediate program fixes were implemented. The relaunched Nirvana V2 (announced September 2024) introduced a “rising floor” price mechanism and protocol-owned liquidity to enhance stability.

**Lessons Learned**: Custom pricing mechanisms are vulnerable to flash loan attacks, requiring robust bonding curves, external oracles, and thorough audits to ensure DeFi protocol security.

**User Losses**: $3.5 million, partially mitigated; 60% of restitution funds have been distributed, with ongoing efforts to compensate affected users.

**References and Citations**:

### [Slope Mobile Wallet Exploit (Aug 2022)](https://www.helius.dev#slope-mobile-wallet-exploit-aug-2022)

**Root Cause**: Insecure handling of private keys in Slope’s mobile wallet application led to the leakage of users’ seed phrases. The app inadvertently transmitted encrypted seed phrases to Slope’s central logging server, where they were potentially intercepted or mishandled, allowing an attacker to access and drain affected wallets.

**Repercussions**: Approximately $8 million in assets were stolen from over 9,000 Solana wallets, with some Ethereum wallets also affected if users reused Slope-generated seed phrases. The exploit caused widespread concern about wallet security in the Solana ecosystem.

**Incident Response**: Slope acknowledged the issue on August 3, 2022, and urged users to transfer funds to hardware wallets or centralized exchanges. The vulnerability was mitigated within days, but no funds were recovered from the attacker.

**Remediations**: Slope implemented stricter data handling policies, removed seed phrase logging, and enhanced encryption practices to prevent future leaks.

**Lessons Learned**: Wallet applications must prioritize secure key management and avoid transmitting sensitive data to centralized servers, highlighting the risks of custodial-like practices in non-custodial wallets.

**User Losses**: $8 million, unreimbursed, with no reported recovery of stolen funds.

**References and Citations**:

### [OptiFi Lockup Bug (Aug 2022)](https://www.helius.dev#optifi-lockup-bug-aug-2022)

**Root Cause**: A coding error during a program update led to the accidental use of the “solana program close” command, permanently shutting down OptiFi’s mainnet and locking $661,000 in USDC within program-derived accounts (PDAs).

**Repercussions**: $661,000 in USDC became permanently inaccessible due to the irreversible closure of the Solana-based DEX; no funds were stolen, but they were effectively lost.

**Incident Response**: The OptiFi team acknowledged the mistake on August 30, 2022, confirmed the funds were unrecoverable, and committed to manually compensating all affected users by September 2, 2022, with a two-week process.

**Remediations**: Implemented a peer-surveillance system requiring at least three team members to review deployments, aiming to prevent future coding errors.

**Lessons Learned**: Due to blockchain immutability, non-malicious bugs can permanently lock funds in DeFi, emphasizing the need for rigorous review and testing before pushing updates.

**User Losses**: $661,000 locked and unreimbursed on-chain; OptiFi refunded users, with 95% of funds belonging to a team member, limiting external user losses to approximately $33,000.

**References and Citations**:

### [Mango Markets Exploit (Oct 2022)](https://www.helius.dev#mango-markets-exploit-oct-2022)

**Root Cause**: The attacker, Avraham Eisenberg, manipulated Mango Markets’ price oracle by inflating the MNGO token price through leveraged perpetual futures trades. Using two accounts with $10 million in USDC, he pumped MNGO’s price from $0.038 to $0.91 across exchanges, borrowing $116 million against the inflated collateral.

**Repercussions**: Approximately $116 million was drained from Mango’s liquidity pools, causing a 50% MNGO price drop and reducing the protocol’s TVL to near zero. After negotiations, Eisenberg returned $67 million, keeping $47 million as a “bug bounty.”

**Incident Response**: Mango froze deposits on October 11, 2022, and negotiated with Eisenberg, who returned $67 million by October 15. The oracle was patched within days to prevent further manipulation.

**Remediations**: Improved oracle security with external price feeds (e.g., Pyth, Chainlink) and implemented leverage limits to reduce manipulation risks.

**Lessons Learned**: Low-liquidity tokens and oracle-dependent systems are vulnerable to economic manipulation, requiring robust price feeds and risk controls.

**User Losses**: The net loss was $47 million, unreimbursed; $67 million returned mitigated some impact, but no further compensation was provided.

**References and Citations**:

### [UXD Protocol Exploit (Oct 2022)](https://www.helius.dev#uxd-protocol-exploit-oct-2022)

**Root Cause**: The UXD Protocol was indirectly impacted by the Mango Markets oracle manipulation exploit, in which attacker Avraham Eisenberg inflated MNGO prices to drain $116 million. UXD had $19.9 million in USDC deposited in Mango’s lending pools, which were frozen during the attack.

**Repercussions**: UXD lost access to $19.9 million in assets, halting its stablecoin minting operations. The protocol’s $UXD stablecoin remained 100% backed due to a $53.5 million insurance fund, but operations were paused until funds were recovered.

**Incident Response**: UXD paused $UXD minting on October 12, 2022, to minimize risk. After Mango’s negotiations returned $67 million, UXD reclaimed $19.9 million on October 20, resuming full operations by October 27.

**Remediations**: UXD reset its Asset Liability Management Module to restore functionality and planned to diversify away from Mango Markets to reduce single-point reliance.

**Lessons Learned**: Dependency on external DeFi protocols exposes stablecoins to third-party risks, necessitating diversified strategies and robust insurance funds.

**User Losses**: None; UXD’s insurance fund and Mango’s partial recovery ensured no direct user losses, with $UXD redeemable at par value via Jupiter Exchange.

**References and Citations**:

### [Tulip Protocol Exploit (Oct 2022)](https://www.helius.dev#tulip-protocol-exploit-oct-2022)

**Root Cause**: The Tulip Protocol was indirectly impacted by the Mango Markets oracle manipulation exploit, in which attacker Avraham Eisenberg inflated MNGO prices to drain $116 million. Tulip had $2.5 million in USDC and RAY strategy vaults deposited in Mango’s lending pools, which were frozen during the attack.

**Repercussions**: Tulip lost access to $2.5 million in assets, temporarily halting vault operations. Vault balances were affected, but Tulip’s integration with Chainlink oracles prevented direct exploitation of its own programs.

**Incident Response**: Tulip paused vault interactions on October 12, 2022. After Mango’s negotiations returned $67 million, Tulip reclaimed $2.5 million on October 20. After resetting its asset liability management module, Tulip restored vault balances and resumed operations by October 26.

**Remediations**: Tulip restricted vault deposits to its own lending pools and reevaluated risk exposure to external protocols to reduce dependency on platforms like Mango.

**Lessons Learned**: Yield aggregators relying on third-party protocols face significant risks from external exploits, necessitating diversified strategies and robust risk management.

**User Losses**: None; Tulip’s recovery of $2.5 million ensured no direct user losses, with vault balances fully restored.

**References and Citations**:

### [Save (formerly, Solend) Exploit (Nov 2022)](https://www.helius.dev#save-formerly-solend-exploit-nov-2022)

**Root Cause**: Oracle price manipulation in three isolated pools (USDH, Stable, and Turbo SOL) allowed attackers to over-borrow against inflated collateral values, exploiting outdated price feeds.

**Repercussions**: $1.26 million in bad debt accrued across the affected pools, impacting Solend’s total value locked and user trust.

**Incident Response**: Solend froze the affected pools within hours, patched the oracle feeds by November 3, 2022, and absorbed the bad debt into its treasury to protect users. No funds were recovered from the attacker.

**Remediations**: Enhanced oracle validation with faster price feed updates and stricter collateral checks to prevent manipulation.

**Lessons Learned**: Accurate and timely oracle data is critical for lending protocols to prevent over-borrowing exploits, emphasizing robust price feed integration.

**User Losses**: None; Solend’s treasury covered the $1.26 million bad debt, ensuring no direct user losses.

**References and Citations**:

### [Raydium Exploit (Dec 2022)](https://www.helius.dev#raydium-exploit-dec-2022)

**Root Cause**: A Trojan horse attack compromised the private key of Raydium’s Pool Owner account, granting the attacker access to the V4 liquidity pool’s admin functions. The attacker used the \`withdrawPNL\` function to inflate and withdraw fees, draining funds from eight constant product liquidity pools.

**Repercussions**: Approximately $4.4 million in assets (including USDC, wSOL, and RAY) was stolen, with $2.7 million later moved to Tornado Cash. The exploit led to a 10% drop in RAY’s price and reduced Raydium’s TVL by $4.4 million.

**Incident Response**: Raydium revoked the compromised account’s authority and patched the V4 AMM program by 14:16 UTC on December 16, 2022, halting further exploits. A 10% bounty was offered, but no funds were recovered.

**Remediations**: Admin parameters were removed via a Squads multisig upgrade, and ownership was transferred to a hardware wallet. A compensation plan was later enacted using RAY buyback funds and team tokens.

**Lessons Learned**: Privileged account security is critical in DeFi; private key compromises can bypass program protections, necessitating robust infrastructure security.

**User Losses**: $4.4 million, partially mitigated; liquidity providers in RAY pools were compensated 100%, non-RAY pools 90% plus 20% RAY bonuses, funded by Raydium’s treasury and team tokens.

**References and Citations**:

- [**CoinDesk**: “Solana-Based Raydium Exchange Victim of 7-Figure Exploit,” December 16, 2022](https://www.coindesk.com/business/2022/12/16/solana-based-raydium-exchange-victim-of-9-figure-exploit/?outputType=amp)
- [**The Block**: “Solana-based exchange Raydium suffers $4.4 million exploit,” December 16, 2022](https://www.theblock.co/amp/post/195712/solana-based-exchange-raydium-suffers-2-million-exploit)
- [**Certik**: “Raydium Protocol Exploit Incident Analysis,” January 18, 2023](https://www.certik.com/resources/blog/36QC53X75PfwlZhOSMkSFd-raydium-protocol-exploit-incident-analysis)
- [**Halborn**: “Explained: The Raydium Hack (November 2022),” December 22, 2022](https://www.halborn.com/blog/post/explained-the-raydium-hack-november-2022)

### [Cypher Protocol Exploit (Aug 2023)](https://www.helius.dev#cypher-protocol-exploit-aug-2023)

**Root Cause**: A vulnerability in Cypher’s program, likely in its margin or futures trading logic, allowed an attacker to steal 38,530 SOL and 123,184 USDC by exploiting unauthorized access to funds. The exact technical flaw remains undisclosed.

**Repercussions**: Approximately $1.04 million was drained, impacting Cypher’s liquidity and user trust during its mtnDAO hacker house event. A redemption program was later established to reimburse users, but in 2024, core contributor Hoak stole $317,000 from this fund, citing a gambling addiction.

**Incident Response**: Cypher froze its programs on August 7, 2023, within hours of the exploit. It attempted to negotiate with the attacker, who transferred 30,000 USDC to finance but did not return funds. The team investigated the breach and proposed a redemption plan.

**Remediations**: Post-exploit, Cypher planned a security audit but faced setbacks after Hoak’s theft. No specific program fixes were detailed, though general calls for robust audits followed.

**Lessons Learned**: DeFi protocols require rigorous program audits and secure key management to prevent both external exploits and insider threats, highlighting vulnerabilities in fast-growing platforms.

**User Losses**: $1.04 million from the initial exploit, unreimbursed; an additional $317,000 stolen by Hoak in 2024, with partial reimbursement attempts ongoing but incomplete.

**References and Citations**:

### [Solvent Protocol’s SVT Token Exploit (Aug 2023)](https://www.helius.dev#solvent-protocols-svt-token-exploit-aug-2023)

**Root Cause**: A flash loan attack exploited economic model loopholes in SVT transaction programs, allowing the attacker to manipulate token prices through repeated buying and selling operations and leverage flash loans to amplify profits.

**Repercussions**: The attacker profited approximately $400,000, draining funds from an unsuspecting user’s wallet and highlighting vulnerabilities in SVT’s program design.

**Incident Response**: No specific response from the SVT team is documented. CertiK alerted the community on August 26, 2023, and MistTrack traced the attacker’s funds, noting initial capital from SwftSwap and 1,070 BNB moved to Tornado Cash.

**Remediations**: No remediations are recorded, likely due to SVT’s obscurity or dissolution. The incident underscored the need for robust economic models in DeFi programs.

**Lessons Learned**: Flash loan attacks exploit poorly designed economic models, requiring secure program logic, oracle integration, and liquidity protections to prevent price manipulation.

**User Losses**: $400,000, unreimbursed, with no recovery reported.

**References and Citations**:

### [Synthetify DAO Exploit (Oct 2023)](https://www.helius.dev#synthetify-dao-exploit-oct-2023)

**Root Cause**: An attacker exploited Synthetify’s inactive DAO by creating and voting on malicious governance proposals. They submitted ten proposals, nine harmless and one containing code to transfer $230,000 in USDC, mSOL, and stSOL to their address, using their own tokens to meet the voting quorum unnoticed.

**Repercussions**: Approximately $230,000 was stolen and sent to Tornado Cash, highlighting governance vulnerabilities in inactive DAOs. Synthetify, already in debt post-FTX collapse, faced further setbacks despite restructuring plans announced in April 2023.

**Incident Response**: The exploit went unnoticed until after funds were transferred. Synthetify froze its programs and platform on October 19, 2023, but no funds were recovered due to the use of Tornado Cash.

**Remediations**: No specific remediations were implemented, as the protocol was already struggling. The incident prompted recommendations for DAOs to adopt veto councils and better notification systems.

**Lessons Learned**: Inactive DAOs with pure token-based voting are vulnerable to governance attacks, requiring active monitoring, engagement incentives, and robust proposal scrutiny.

**User Losses**: $230,000, unreimbursed, with no recovery reported.

**References and Citations**:

### [Thunder Terminal Exploit (Dec 2023)](https://www.helius.dev#thunder-terminal-exploit-dec-2023)

**Root Cause**: A compromised MongoDB connection URL, a third-party service vulnerability, allowed an attacker to access Thunder Terminal’s system, withdrawing 86.5 ETH and 439 SOL from user wallets via malicious approvals.

**Repercussions**: Approximately $240,000 in assets was stolen, with $192,500 transferred to Railgun. The incident affected 14% of hot wallet users, but cold wallets remained secure.

**Incident Response**: Thunder Terminal halted the attack within nine minutes on December 27, 2023, revoked malicious approvals, and restored platform operations within hours. The team offered a bounty and negotiated with the attacker, who made unverified claims of additional vulnerabilities, but no funds were recovered.

**Remediations**: To prevent similar compromises, enhanced security for third-party integrations, including stricter access controls and monitoring for MongoDB connections, was implemented.

**Lessons Learned**: Third-party service dependencies pose significant risks to DeFi platforms, requiring robust security audits and rapid response mechanisms to protect user funds.

**User Losses**: $240,000, unreimbursed, with no reported recovery of stolen funds.

**References and Citations**:

### [Aurory SyncSpace Exploit (Dec 2023)](https://www.helius.dev#aurory-syncspace-exploit-dec-2023)

**Root Cause**: On December 17, 2023, a malicious actor exploited a race condition vulnerability in Aurory’s off-chain marketplace buy endpoint. By sending multiple simultaneous buy requests, the attacker inflated their AURY balance in SyncSpace, a hybrid on-chain/off-chain inventory system. This allowed the withdrawal of approximately 600,000 AURY tokens (valued at \~$830,000) to the Arbitrum network, which were then sold on the open market.

**Repercussions**: The exploit caused an 80% liquidity drop in the AURY-USDC pool on Camelot DEX, reducing it from $1.5 million to $312,000. The AURY token price fell 17% to $1.17, with a 23.5% decline over 24 hours and 36.5% over seven days, though it later recovered slightly. No user funds or NFTs were lost, as the stolen tokens came from a team wallet.

**Incident Response**: The Aurory team detected suspicious activity within hours and disabled the SyncSpace bridge for maintenance, halting deposits and withdrawals. They absorbed selling pressure by buying back tokens and confirmed the attacker had exhausted their AURY supply. A global backend patch was in development, with a detailed postmortem planned.

**Remediations**: Aurory is working on a patch to fix the race condition vulnerability and plans to enhance marketplace security. Despite a prior audit by OtterSec, the vulnerability went undetected, prompting a review of audit scopes and processes. SyncSpace is expected to resume operations after fixes are implemented.

**Lessons Learned**: Race condition vulnerabilities in off-chain systems can lead to significant exploits, even in audited platforms. Comprehensive audit scopes, real-time monitoring, and robust marketplace logic are critical to prevent such attacks, especially for hybrid on-chain/off-chain systems.

**User Losses**: No user funds or NFTs were compromised. The $830,000 loss (later valued at \~$690,000 due to price drops) was borne by the team’s wallet, used for withdrawals by accounts without prior AURY deposits.

**References and Citations**:

### [Saga DAO Incident (Jan 2024)](https://www.helius.dev#saga-dao-incident-jan-2024)

**Root Cause**: Saga DAO, a fan club for the Solana Saga phone, had a security breach in Saga DAO’s multisig wallet, reportedly requiring only 1/12 wallet confirmations, allowing an attacker to drain approximately $60,000 in SOL from the treasury. The breach was linked to a compromised founder’s account, though some community members alleged insider involvement due to the low confirmation threshold.

**Repercussions**: The loss of $60,000 disrupted Saga DAO’s operations, which focus on managing airdrops for Saga Genesis NFT holders. The incident sparked accusations of mismanagement, with community trust eroded due to the DAO’s rapid treasury growth to over 1,000 SOL before the breach.

**Incident Response**: Saga DAO acknowledged the breach on January 24, 2024, and removed involved parties from leadership roles. The team committed to investigating and implementing safeguards, but no funds were recovered, and specifics on the hack remained unclear.

**Remediations**: Plans were announced to strengthen multisig wallet security, including higher confirmation thresholds and improved access controls, though no concrete updates were reported by early 2025.

**Lessons Learned**: Low confirmation thresholds in multisig wallets expose DAOs to significant risks, requiring robust governance and security protocols to protect community funds, especially in rapidly growing treasuries.

**User Losses**: $60,000, unreimbursed, with no recovery reported, impacting the DAO’s ability to distribute airdrop rewards.

**References and Citations**:

### [Solareum Exploit (Mar 2024)](https://www.helius.dev#solareum-exploit-mar-2024)

**Root Cause**: A security breach, allegedly involving a North Korean developer hired by Solareum, compromised user wallets by exploiting private keys imported into the Telegram bot. The attacker likely accessed keys through a third-party service vulnerability, possibly a MongoDB connection URL, draining funds from 302–309 user wallets.

**Repercussions**: Approximately $520,000-$1.4 million in SOL (2,808–6,045 SOL) was stolen, affecting over 300 users. Solareum shut down permanently due to the exploit, insufficient funds, and market challenges, leaving users demanding compensation.

**Incident Response**: Solareum acknowledged the exploit on March 29, 2024, and shut down operations by April 2, urging users to retrieve assets. The team contacted authorities to freeze funds on centralized exchanges, with Tether freezing $975,000. No user refunds were promised.

**Remediations**: None implemented, as Solareum ceased operations. The incident highlighted the need for secure third-party integrations and developer vetting in DeFi applications.

**Lessons Learned**: Telegram-based trading bots are vulnerable to private key leaks and insider threats, necessitating robust security audits, secure key management, and caution with third-party services.

**User Losses**: $520,000-$1.4 million, unreimbursed, with no recovery reported despite partial freezing of funds.

**References and Citations**:

### [io.net GPU Metadata Attack (Apr 2024)](https://www.helius.dev#ionet-gpu-metadata-attack-apr-2024)

**Root Cause**: Malicious actors spoofed approximately 400,000 virtual GPUs on io.net’s decentralized GPU network by abusing the platform’s worker registration process. The attackers manipulated metadata to inflate the number of active workers, potentially disrupting resource allocation and network integrity.

**Repercussions**: The attack did not result in direct financial losses, as no user funds were stolen. However, it strained io.net’s network by introducing fake workers, risking operational inefficiencies and undermining trust in the platform’s GPU allocation during its beta phase.

**Incident Response**: io.net’s security team identified the spoofing on April 18, 2024, and began automatically tagging malicious accounts for removal. The team retained some fake workers to study the attack, ensuring continued monitoring and mitigation without disrupting services.

**Remediations**: io.net implemented enhanced worker verification processes to prevent metadata spoofing.

**Lessons Learned**: Decentralized compute networks are vulnerable to metadata manipulation, requiring robust validation mechanisms to ensure the integrity of resource contributions and prevent abuse.

**User Losses**: None; the attack caused no direct financial losses, focusing on network disruption rather than asset theft.

**References and Citations**

### [Pump.fun Exploit (May 2024)](https://www.helius.dev#pumpfun-exploit-may-2024)

**Root Cause**: A former Pump.fun employee exploited their privileged withdrawal authority access to execute a flash loan attack using a Solana lending protocol. The attacker used the borrowed SOL to **artificially inflate token values.** By pushing token values to 100% on the bonding curve, the attacker accessed $1.9 million in bonding curve liquidity to repay the loan and keeping profit.

**Repercussions**: Approximately $1.9 million in SOL (12,300 SOL) was stolen, affecting 1,882 wallet addresses. Initial community reports exaggerated losses at $80 million, but the actual impact was limited to $1.9 million of the platform’s $45 million liquidity.

**Incident Response**: Pump.fun halted trading at 17:00 UTC on May 16, 2024, and redeployed bonding curve programs within hours. The team seeded affected liquidity pools with equal or greater SOL within 24 hours and waived trading fees for seven days to restore user trust.

**Remediations**: Upgraded program security to revoke unauthorized access and implemented stricter internal access controls to prevent future insider exploits.

**Lessons Learned**: Insider threats and privileged access vulnerabilities can bypass DeFi safeguards, necessitating robust employee oversight and secure program design.

**User Losses**: $1.9 million, fully mitigated; Pump.fun’s compensation plan restored affected liquidity, ensuring no net user losses.

**References and Citations**:

### [Banana Gun Exploit (Sep 2024)](https://www.helius.dev#banana-gun-exploit-sep-2024)

**Root Cause**: A vulnerability in Banana Gun’s Telegram message oracle allowed an attacker to intercept messages and manually transfer 563 ETH ($1.4 million) from 11 user wallets during live trading sessions. The flaw affected both Ethereum and Solana bots, targeting experienced traders with notable social or trading presence.

**Repercussions**: Approximately $1.4 million was stolen, initially reported as $3 million, affecting 36 users, but later clarified as $1.4 million across 11 users. The incident disrupted trust in Telegram-based trading bots, prompting community concerns about front-end vulnerabilities.

**Incident Response**: Banana Gun shut down its Ethereum and Solana bots within minutes on September 19, 2024, patched the Telegram oracle vulnerability, and redeployed the bots by September 20. Affected users were promised full refunds from the treasury, with no token sales.

**Remediations**: Implemented a two-hour transfer delay, added two-factor authentication for transactions, and partnered with Security Alliance for audits and penetration tests to enhance front-end security.

**Lessons Learned**: Telegram-based bots are vulnerable to oracle and front-end exploits, requiring robust security measures and user verification to protect against targeted attacks on high-value traders.

**User Losses**: $1.4 million, fully mitigated; Banana Gun’s treasury refunded all affected users, ensuring no net losses.

**References and Citations**:

### [DEXX Exploit (Nov 2024)](https://www.helius.dev#dexx-exploit-nov-2024)

**Root Cause**: Due to improper key management, a private key leak in DEXX’s centralized custody model allowed an attacker to access and drain user wallets. The plaintext display of private keys during \`export\_wallet\` requests on the official server facilitated the breach.

**Repercussions**: Approximately $30 million in assets were stolen, affecting over 900 unique users across 8,620+ Solana wallets. Most victims lost under $10,000, but one user lost over $1 million. The attacker converted stolen altcoins to SOL, complicating recovery.

**Incident Response**: DEXX halted operations on November 16, 2024, and collaborated with SlowMist and law enforcement to track funds. A bug bounty and a 24-hour return offer were issued, but no funds were recovered. The team announced a compensation plan pending fund recovery.

**Remediations**: Planned upgrades include a self-hosted wallet version, enhanced cloud security, and a comprehensive security framework overhaul to prevent future key leaks.

**Lessons Learned**: Centralized custody of private keys in DeFi platforms poses significant risks, requiring secure key management and encrypted communication to protect user assets.

**User Losses**: $30 million, unreimbursed, with no recovery reported as of November 29, 2024.

**References and Citations**:

- [**Cointelegraph**: “Over 8.6K Solana wallets linked to $21M DEXX hacker,” November 29, 2024](https://cointelegraph.com/news/solana-dexx-hack-november-2024-suspicious-wallets)
- [**Cryptopolitan**: “Over 8,620 Solana wallets have been linked to the DEXX hack,” December 11, 2024](https://www.cryptopolitan.com/8620-solana-wallets-linked-to-the-dexx-hack/)
- [**ChainCatcher**: “CertiK: The reason for the DEXX incident is improper management of private keys by the project team,” November 16, 2024](https://www.chaincatcher.com/en/article/2152336)

### [NoOnes Platform Exploit (Jan 2025)](https://www.helius.dev#noones-platform-exploit-jan-2025)

**Root Cause**: A vulnerability in NoOnes’ Solana cross-chain bridge allowed attackers to exploit the platform’s hot wallets, enabling hundreds of small transactions (each under $7,000) across Ethereum, TRON, Solana, and Binance Smart Chain.

**Repercussions**: Approximately $7.9-$8 million in crypto assets were stolen, with funds bridged to Ethereum and Binance Smart Chain and then funneled to Tornado Cash for mixing, complicating recovery efforts.

**Incident Response**: NoOnes’ security team contained the breach on January 1, 2025, and suspended the Solana bridge. CEO Ray Youssef confirmed the exploit on January 24, 2025, after ZachXBT’s investigation, ensuring user funds and data remained safe. The bridge remains inactive pending penetration testing.

**Remediations**: Planned comprehensive penetration testing and enhanced bridge security to prevent future exploits, though specific fixes are undisclosed.

**Lessons Learned**: Cross-chain bridges require robust security to prevent unauthorized access, highlighting the need for rigorous testing and monitoring in P2P platforms.

**User Losses**: $7.9-$8 million, unreimbursed, with no recovery reported as funds were mixed via Tornado Cash.

**References and Citations**:

### [Loopscale Exploit (Apr 2025)](https://www.helius.dev#loopscale-exploit-apr-2025)

**Root Cause:** On April 26, 2025, an attacker exploited a vulnerability in Loopscale’s pricing mechanism for RateX Principal Token (PT) collateral. By manipulating the oracle price feed, the attacker artificially inflated the perceived value of RateX PT tokens, enabling a series of undercollateralized loans. This allowed the withdrawal of approximately 5.7 million USDC and 1,200 SOL (valued at \~$5.8 million) from Loopscale’s USDC and SOL Genesis Vaults.

**Repercussions:** The exploit drained \~12% of Loopscale’s total value locked (TVL), which was \~$40 million before the incident. The attack triggered cascading liquidations and margin calls across interconnected Solana DeFi platforms, causing price volatility for SOL and USDC on decentralized exchanges. Investor confidence in emerging DeFi protocols waned, increasing regulatory scrutiny and restricting capital flows.

**Incident Response**: Loopscale detected the exploit on April 26, 2025, at 11:30 AM EST and immediately paused all lending markets and vault withdrawals to prevent further losses. Loan repayments, collateral top-ups, and loop closing were re-enabled later that day. The team initiated negotiations with the attacker, offering a 10% bug bounty and immunity from legal action. By April 29, all stolen funds (5,726,725 USDC and 1,211 SOL) were returned following successful negotiations.

**Remediations:** Loopscale conducted a code review with Sec3, releasing a patched version of the protocol. Vault withdrawals were re-enabled on May 8, 2025. The team committed to ongoing security audits, enhanced oracle validation, and improved collateral pricing mechanisms. A comprehensive postmortem was published, detailing the vulnerability and future security enhancements.

**Lessons Learned:** The incident underscored the risks of oracle manipulation in DeFi protocols, particularly for novel collateral pricing models. Comprehensive business logic validation, multi-layer audits, and robust oracle architectures are critical to prevent such exploits. Rapid response and transparent communication can mitigate user impact and facilitate fund recovery.

**User Losses:** No user deposits were lost. All stolen funds ($5.8 million) were recovered, ensuring depositors in the USDC and SOL vaults faced no financial impact.

**References and Citations:**

- [**Loopscale Official Statement**: @LoopscaleLabs, April 29, 2025, fund recovery announcement](https://x.com/LoopscaleLabs/status/1920182230762336342)
- [**The Block**: “Solana DeFi protocol Loopscale hit with $5.8 million exploit two weeks after launch,” April 27, 2025](https://www.theblock.co/post/352083/solana-defi-protocol-loopscale-hit-with-5-8-million-exploit-two-weeks-after-launch)
- [**Halborn**: “Explained: The Loopscale Hack (April 2025),” April 30, 2025](https://www.halborn.com/blog/post/explained-the-loopscale-hack-april-2025)
- [**Blockworks**: “Loopscale loses $5.8M in oracle attack,” April 29, 2025](https://blockworks.co/news/loopscale-loss-oracle-attack)

## [Supply Chain Attacks](https://www.helius.dev#supply-chain-attacks)

**Definition**

Supply Chain Attacks are security incidents that compromise the integrity of a platform or application by targeting its external dependencies, such as third-party services, libraries, or distribution channels. These attacks exploit vulnerabilities in the software supply chain, affecting downstream users or dApps that rely on the compromised component.

**Characteristics**

- **Scope**: Involves external components (e.g., cloud services, package repositories, browser extensions) integrated with or relied upon by Solana dApps.
- **Common Vulnerabilities**: Include phishing attacks on developer accounts, malicious updates to software packages, or DNS hijacking to redirect users to phishing sites.
- **Impact**: Results in stolen funds, compromised user credentials, or unauthorized access to wallets. Impacts users interacting with the compromised service.

**Supply Chain Incidents**

### [Parcl Front-End Attack (Aug 2024)](https://www.helius.dev#parcl-front-end-attack-aug-2024)

**Root Cause**: A DNS hijacking attack compromised Parcl’s front-end by altering its domain settings, redirecting users to a malicious site. Attackers extracted tokens from Solana wallets and displayed false transaction results in Phantom, exploiting the platform’s web interface.

**Repercussions**: The attack drained an undisclosed amount of tokens from user wallets, with no specific loss figure reported. Parcl’s X account appeared compromised, amplifying user confusion and distrust during the incident.

**Incident Response**: Parcl halted trading on August 20, 2024, and secured its domain within hours. By August 22, trading resumed with confirmed protections, and users were advised to verify the official website before interacting.

**Remediations**: Enhanced DNS security measures, including stricter Cloudflare access controls and domain monitoring, to prevent future hijacking attempts.

**Lessons Learned**: Front-end vulnerabilities, especially DNS-based attacks, pose significant risks to DeFi platforms, requiring robust third-party service security and user education to avoid phishing sites.

**User Losses**: Undisclosed amount, unreimbursed; no specific recovery or compensation reported.

**References and Citations**:

### [Web3.js Supply Chain Attack (Dec 2024)](https://www.helius.dev#web3js-supply-chain-attack-dec-2024)

**Root Cause**: A spear phishing campaign compromised a publish-access account for @solana
/web3.js, enabling an attacker to publish malicious npm package versions (1.95.6 and 1.95.7). These versions contained code to steal private key material from dapps handling keys directly, triggered by specific method calls.

**Repercussions**: An estimated $30–50 million in assets was potentially at risk, though exact losses are unconfirmed due to the short exposure window (3:20 PM to 8:25 PM UTC). The attack targeted Solana dapps, like trading bots, but did not affect non-custodial wallets or the Solana protocol.

**Incident Response**: The Web3.js team deprecated versions 1.95.6 and 1.95.7 by 8:52 PM UTC on December 3, 2024, and removed them from npm by 12:22 AM UTC on December 4. Developers were urged to upgrade to version 1.95.8 and rotate suspect keys. No stolen funds were recovered.

**Remediations**: Revoked compromised npm credentials, restored version 1.95.5 as the latest, and planned enhanced security measures, including stricter access controls and two-factor authentication for package publishing.

**Lessons Learned**: Supply chain attacks on critical libraries can compromise entire ecosystems, necessitating robust authentication, package monitoring, and developer vigilance to prevent malicious updates.

**User Losses**: As per some sources losses are \~$130K unreimbursed; losses depended on dapps deploying the malicious versions, with no reported recovery.

**References and Citations**:

## [Network-Level Attacks](https://www.helius.dev#network-level-attacks)

**Definition**

Network-Level Attacks are security incidents that target the infrastructure supporting Solana dApps or platforms, such as websites or servers, rather than the blockchain or application logic. These attacks aim to disrupt access or availability, typically through Distributed Denial-of-Service (DDoS) techniques.

**Characteristics**

- **Scope**: Affects the network infrastructure (e.g., web servers, APIs) of Solana-based platforms, not the blockchain or programs.
- **Common Vulnerabilities**: Include overwhelming servers with traffic (DDoS) to disrupt user access, often during high-traffic events like airdrops.
- **Impact**: Causes temporary service outages or slowed access, but typically no direct financial losses unless combined with other exploits. Impacts users through inconvenience.

**Network Level Incidents**

### [Grape Protocol IDO Incident (Sep 2021)](https://www.helius.dev#grape-protocol-ido-incident-sep-2021)

**Root Cause**: Bots spammed Grape Protocol’s IDO on Raydium with 400,000 transactions per second, overwhelming Solana’s transaction processing queues. The excessive load caused memory exhaustion in validator nodes, leading to network forks and a denial-of-service (DoS) outage.

**Repercussions**: The Solana network halted for 17 hours (September 14–15, 2021), disrupting all transactions and dApps. SOL’s price dropped 15% from $170 to $145, and Grape’s $600,000 IDO was chaotic, though no direct funds were stolen.

**Incident Response**: Solana engineers and over 1,000 validators coordinated a hard fork, restarting the network at slot 96,528,693 on September 15, 2021, with 80% consensus. A patch (v1.6.25) was deployed to stabilize transaction processing.

**Remediations**: To mitigate bot-driven floods, Solana improved transaction deduplication, optimized queue management, and enhanced validator memory handling. Raydium introduced anti-bot measures for future IDOs.

**Lessons Learned**: High-demand IDOs can trigger network-level attacks via bot spam, necessitating robust anti-bot protections and scalable infrastructure to maintain blockchain stability.

**User Losses**: None directly from theft; indirect losses occurred due to SOL price volatility and disrupted transactions, with no reported reimbursement.

**References and Citations**

- [**CoinDesk**: “Solana Blockchain Restarts After Bots Cause 17-Hour Outage,” September 15, 2021](https://www.coindesk.com/business/2021/09/23/grape-network-the-startup-that-broke-solana-raises-18m)
- [**CoinTelegraph**: “Solana attributes major outage to denial-of-service attack targeting DEX offering” September 21, 2021](https://cointelegraph.com/news/solana-attributes-major-outage-to-denial-of-service-attack-targeting-dex-offering)
- [**The** Block: “Solana-based Grape protocol raises $1.2 million in seed funding,” September 24, 2021](https://www.theblockcrypto.com/post/118410/solana-based-grape-protocol-seed-funding)

### [Candy Machine NFT Minting Outage (Apr 2022)](https://www.helius.dev#candy-machine-nft-minting-outage-apr-2022)

**Root Cause**: A swarm of bots flooded the Metaplex Candy Machine, a popular Solana NFT minting tool, with 4 million transaction requests and 100 gigabits of data per second, overwhelming network safeguards and knocking validators out of consensus.

**Repercussions**: The Solana network suffered a 7-hour outage, halting block production from 4:32 PM to 11:00 PM ET, causing a 10% SOL price drop to $83.13. Ecosystem services like Phantom wallet and Mango Markets faced disruptions.

**Incident Response**: Validators restarted the Mainnet Beta cluster at 3:00 AM UTC on May 1, 2022, restoring services. Metaplex announced a 0.01 SOL botting penalty to deter invalid transactions, deployed shortly after.

**Remediations**: Metaplex implemented a botting penalty and planned enhancements to the Candy Machine program to stabilize traffic. Solana developers continued investigating why safeguards failed.

**Lessons Learned**: High-traffic NFT minting tools require robust anti-bot measures and network capacity to prevent outages, highlighting Solana’s scalability challenges during peak demand.

**User Losses**: None directly from theft; indirect losses occurred due to SOL price volatility and disrupted transactions, with no reported reimbursement.

**References and Citations**:

### [Jito DDoS Attack (Dec 2023)](https://www.helius.dev#jito-ddos-attack-dec-2023)

**Root Cause**: A Distributed Denial-of-Service (DDoS) attack flooded Jito’s website with excessive traffic, disrupting access during the JTO token airdrop launch. The attack, likely perpetrated by scammers seeking ransom, targeted the platform’s server infrastructure, not its Solana-based programs.

**Repercussions**: The attack caused temporary outages, slowing or halting some users' access to Jito’s airdrop claim portal. No funds were stolen, and the airdrop of 90 million JTO tokens (\~$225 million) proceeded, with over 54 million tokens claimed.

**Incident Response**: Jito mitigated the attack within minutes, restoring website functionality by December 7, 2023. The team did not disclose ransom details but confirmed no compromise of user assets or protocol security.

**Remediations**: Enhanced anti-DDoS protections, including traffic filtering and server hardening, to prevent future disruptions during high-traffic events like airdrops.

**Lessons Learned**: DeFi platforms are prime targets for network-level attacks during major events, requiring robust infrastructure security to ensure uninterrupted user access.

**User Losses**: None; the DDoS attack disrupted access but did not result in stolen funds or direct user losses.

**References and Citations**:

### [Phantom Wallet DDoS Attack (Feb 2024)](https://www.helius.dev#phantom-wallet-ddos-attack-feb-2024)

**Root Cause**: A Distributed Denial-of-Service (DDoS) attack targeted Phantom Wallet’s infrastructure, overwhelming its systems with excessive traffic. The attack, likely exploiting the high-profile Jupiter (JUP) airdrop, aimed to disrupt service availability by flooding servers with requests, though no specific vulnerabilities were detailed.

**Repercussions**: For several hours, the attack temporarily interrupted Phantom’s services, including wallet access and transaction processing. No user funds were compromised, as assets remained secure on Solana. The incident coincided with increased scrutiny following Phantom’s integration of Bitcoin, Ordinals, and BRC-20 tokens.

**Incident Response**: Phantom’s team acknowledged the attack via X on February 1, 2024, at 15:20 UTC, reassuring users that assets were safe. Services were suspended to mitigate the attack, and functionality was restored by February 2, with an update confirming resolution. No funds were lost, and no further attack details were disclosed.

**Remediations**: Phantom implemented enhanced DDoS mitigation measures, though specifics were not shared. The team emphasized ongoing security improvements to handle high-traffic events and prevent future disruptions.

**Lessons Learned**: High-profile events like airdrops attract DDoS attacks, requiring robust network defenses, traffic filtering, and scalable infrastructure to maintain DeFi wallet availability, especially on Solana’s high-throughput network.

**User Losses**: None; the attack caused temporary service disruptions but no financial losses, as user assets remained secure.

**References and Citations**

## [Core Protocol Vulnerabilities](https://www.helius.dev#core-protocol-vulnerabilities)

**Definition**

Core Protocol Vulnerabilities are security incidents that exploit flaws in Solana’s protocol itself, such as its consensus mechanism, transaction validation, or network architecture. These would affect the entire blockchain, compromising its integrity, security, or availability.

Characteristics

- **Scope**: Impacts the Solana blockchain at its foundational level, affecting all nodes, transactions, or dApps.
- **Common Vulnerabilities**: Could include bugs in the consensus algorithm, vulnerabilities in transaction processing, or flaws in the blockchain’s cryptographic mechanisms.
- **Impact**: Would likely cause network-wide disruptions, loss of funds across dApps, or compromised blockchain integrity. Impacts all users and protocols on Solana.

**Core Protocol Incidents**

### [Solana Turbine Bug Incident (Dec 2020)](https://www.helius.dev#solana-turbine-bug-incident-dec-2020)

**Root Cause**: A block propagation bug in Turbine, Solana’s block propagation mechanism, caused a validator to transmit two different blocks for the same slot, which were propagated to separate network partitions (A and B). A third partition detected the inconsistency, but none achieved supermajority consensus due to insufficient stake, halting block production. The issue stemmed from tracking blocks by Proof of History (PoH) slot number (u64) rather than hash, leading nodes to misinterpret distinct blocks as identical, preventing fork repair.

**Repercussions**: Solana experienced a six-hour outage, disrupting all transactions and dApps. The network split into partitions, with nodes rejecting opposing forks due to differing state transitions, blocking finality. No funds were lost, but early-stage user trust was tested.

**Incident Response**: Validators coordinated a network restart at 80% stake participation, resuming block production by December 8, 2020. The Solana team identified the bug and deployed fixes to address block tracking and fault detection.

**Remediations**: Implemented block tracking by hash instead of slot number to distinguish conflicting blocks, enabled earlier fault detection in Turbine, and propagated faults to all validators via gossip. These changes ensured nodes could repair forks and resolve partitions, preventing similar consensus failures.

**Lessons Learned**: Block propagation systems must track blocks uniquely by hash to avoid misidentification, requiring robust fault detection and gossip mechanisms to maintain consensus in high-throughput blockchains like Solana.

**User Losses**: None; the outage caused disruptions but no direct financial losses, as no transactions were processed during the downtime.

**References and Citations**

### [Solana Durable Nonce Bug Incident (Jun 2022)](https://www.helius.dev#solana-durable-nonce-bug-incident-jun-2022)

**Root Cause**: A runtime bug in Solana’s durable nonce transactions feature allowed a failed transaction to be processed twice, once as a regular transaction and again as a nonce transaction, due to a recent blockhash. This led to nondeterminism, with validators producing conflicting outputs, halting consensus at 16:30 UTC.

**Repercussions**: Solana stopped producing blocks for 4.5 hours, disrupting transactions and dApps. SOL’s price dropped 13.9% to $39.08, and trading volume surged 61% to $2.141 billion.

**Incident Response**: Validator operators restarted the network at 21:00 UTC on June 1, 2022, disabling the durable nonce feature in releases v1.9.28/v1.10.23. Client services were restored over several hours, with no funds lost.

**Remediations**: The durable nonce feature remained disabled until a fix in v1.10.23 prevented duplicate processing by separating nonce and blockhash domains. Enhanced validation logic was also implemented.

**Lessons Learned**: Durable nonce transactions require robust mechanisms to prevent double processing, highlighting the need for thorough testing of niche protocol features to maintain network stability.

**User Losses**: None directly from theft; indirect losses occurred due to SOL price volatility and halted transactions, with no reported reimbursement.

**References and Citations**

### [Solana Duplicate Block Bug Incident (Sep 2022)](https://www.helius.dev#solana-duplicate-block-bug-incident-sep-2022)

**Root Cause**: A faulty validator produced duplicate blocks for its leader slots due to a bug in Solana’s fork choice logic. When validators could not revert to the heaviest bank if its slot matched their last voted slot, they became stuck, preventing consensus and halting the network. The issue was compounded by insufficient confirmed votes, stalling new root block production.

**Repercussions**: Solana halted block confirmations for several hours, disrupting transactions and dApps. A secondary bug during the restart caused fluctuating active stake amounts due to an inflation mechanism error, overflowing a 64-bit unsigned integer.

**Incident Response**: Validators restarted the network, aligning on a trusted snapshot to restore consensus. The stake overflow bug was quickly identified and patched before a second restart, ensuring network recovery by October 1, 2022.

**Remediations**: Later Solana client versions introduced a mechanism to prioritize vote transactions, preventing them from being overwhelmed by regular transactions, and fixed the fork choice flaw to ensure validators could switch to the heaviest fork.

**Lessons Learned**: Fork choice logic must robustly handle duplicate blocks to maintain consensus, highlighting the need for enhanced vote prioritization and stake calculation accuracy in high-throughput blockchains.

**User Losses**: None directly from theft; indirect losses occurred due to disrupted transactions, with no reported reimbursement.

**References and Citations**

### [Solana Turbine Failure Incident (Feb 2023)](https://www.helius.dev#solana-turbine-failure-incident-feb-2023)

**Root Cause**: A single large block overwhelmed Turbine’s deduplication logic due to malfunctioning block forwarding services, which continuously reforwarded the block’s shreds. This saturated deduplication filters creating loops in the Turbine tree, forcing reliance on the slower Block Repair protocol and halting block finalization.

**Repercussions**: Solana  experienced a 9-hour outage starting at 05:46 UTC, disrupting transactions and dApps. SOL’s price dropped 5% to $22.90, with no significant TVL impact.

**Incident Response**: Validators attempted a live software downgrade, suspecting a recent update (v1.14.16), but ultimately restarted the network at 01:28 UTC on February 26, 2023, using a trusted snapshot. No economic transactions were rolled back.

**Remediations**: Enhanced deduplication logic in v1.13.7 and v1.14.17 to mitigate filter saturation. Engineers collaborated with forwarding service providers to improve resiliency and planned to replace UDP with QUIC for better traffic control.

**Lessons Learned**: Turbine’s deduplication logic must handle large blocks robustly, emphasizing the need for optimized forwarding services and protocol upgrades to prevent congestion in high-throughput networks.

**User Losses**: None directly from theft; indirect losses occurred due to SOL price volatility and halted transactions, with no reported reimbursement.

**References and Citations**

### [Solana JIT Cache Bug Incident (Feb 2024)](https://www.helius.dev#solana-jit-cache-bug-incident-feb-2024)

**Root Cause**: A bug in the \`LoadedPrograms\` cache system, introduced in Agave v1.16, caused an infinite recompile loop in the JIT cache. For legacy loader programs, new JIT outputs were assigned a sentinel slot height of zero, making them invisible to \`LoadedPrograms\`. This triggered continuous recompilation, stalling validators on a specific block and halting consensus at 09:53 UTC.

**Repercussions**: Solana experienced a 5-hour outage, disrupting transactions and dApps. SOL’s price dropped to a six-day low of $93.75 but recovered to $105.46 within days. Over 95% of the cluster stake, running Agave v1.17, was affected.

**Incident Response**: Engineers identified the bug, previously seen on Devnet, and deployed a modified patch in v1.17.20. Validators restarted the network at 14:55 UTC using snapshot slot 246,464,040, restoring consensus. The fix disabled vulnerable legacy loaders.

**Remediations**: Patched v1.17.20 to prevent the recompile loop, with plans for a comprehensive LoadedPrograms overhaul in future releases to enhance cache efficiency and fork awareness.

**Lessons Learned**: Legacy loader programs require robust cache management to prevent infinite loops, highlighting the need for thorough testing across all network conditions and faster patch deployment.

**User Losses**: None directly from theft; indirect losses occurred due to SOL price volatility and halted transactions, with no reported reimbursement.

**References and Citations**

### [Solana ELF Address Alignment Vulnerability Incident (Aug 2024)](https://www.helius.dev#solana-elf-address-alignment-vulnerability-incident-aug-2024)

**Root Cause**: A critical vulnerability in Solana’s ELF address alignment logic, related to the processing of executable files in the Solana runtime, could have allowed an attacker to manipulate program execution, potentially halting the network or enabling unauthorized actions.

**Repercussions**: No exploitation occurred, as the vulnerability was patched preemptively. The incident had no immediate financial impact, with SOL’s price rising 0.89% to $155.88, reflecting confidence in the rapid response.

**Incident Response**: On August 7, 2024, the Solana Foundation privately contacted network operators, distributing a patch via an Anza engineer’s GitHub repository. By August 8, 14:00 UTC, 66.6% of the network stake was secured, and public disclosure followed after 70% adoption on August 9. The patch (v1.18.21) was fully implemented without disruption.

**Remediations**: The patch fixed the ELF address alignment flaw, and additional validation checks ensured proper program loading. The Solana team enhanced private disclosure protocols to prevent reverse-engineering risks.

**Lessons Learned**: Critical vulnerabilities in core runtime components, like ELF processing, require discreet patching and stakeholder coordination to prevent network-wide outages, emphasizing proactive security in high-throughput blockchains.

**User Losses**: None; the vulnerability was patched before exploitation, ensuring no financial losses or network disruption.

**References and Citations**

- [**Crypto Briefing**: “Solana devs and validators patch critical vulnerability, preventing a network-wide outage,” August 9, 2024](https://cryptobriefing.com/solana-critical-vulnerability-patch/)
- [**The Block**: “Solana developers address critical vulnerability with coordinated patch,” August 9, 2024](https://www.theblock.co/post/310361/solana-developers-address-critical-vulnerability-with-coordinated-patch)
- [**Cointelegraph**: “Solana prevents potential outage, patches critical vulnerability,” August 9, 2024](https://cointelegraph.com/news/solana-fixes-critical-security-vulnerability)

## [Incident Categorization and Frequency](https://www.helius.dev#incident-categorization-and-frequency)

38 verified security incidents on Solana from March 2020 to Q1 2025, categorized as follows:

- **Application Exploits**: 26 incidents (68.42% of total)
- **Supply Chain Attacks**: 2 incidents (5.26% of total)
- **Network-Level Attacks**: 4 incidents (10.53% of total)
- **Core Protocol Vulnerabilities**: 6 incidents (15.79% of total)

### [Frequency by Year](https://www.helius.dev#frequency-by-year)

**2020: 1 Incident**

- **1 Core Protocol Vulnerability:** Solana Turbine Bug

**2021: 2 Incidents**

- **1 Network-Level Attack:** Grape Protocol IDO Incident
- **1 Application Exploit:** Solend Auth Bypass Attempt

**2022: 15 Incidents**

- **12 Application Exploits:** Wormhole Bridge Exploit, Cashio Exploit, Crema Finance Exploit, Audius Governance Exploit, Nirvana Finance Exploit, Slope Mobile Wallet Exploit, OptiFi Lockup Bug, Mango Markets Exploit, UXD Protocol Exploit, Tulip Protocol Exploit, Save (formerly Solend) Exploit, Raydium Exploit
- **1 Network-Level Attack:** Candy Machine NFT Minting Outage
- **2 Core Protocol Vulnerabilities:** Solana Durable Nonce Bug Incident, Solana Duplicate Block Bug Incident

**2023: 7 Incidents**

- **5 Application Exploits:** Cypher Protocol Exploit, SVT Token Exploit, Synthetify DAO Exploit, Thunder Terminal Exploit, Aurory SyncSpace Exploit
- **1 Network-Level Attack:** Jito DDoS Attack
- **1 Core Protocol Vulnerability:** Solana Turbine Failure Incident

**2024: 11 Incidents**

- **6 Application Exploits:** Saga DAO Incident, Solareum Exploit, io.net GPU Metadata Attack, Pump.fun Exploit, Banana Gun Exploit, DEXX Exploit
- **2 Supply Chain Attacks:** Parcl Front-End Attack, Web3.js Supply Chain Attack
- **1 Network-Level Attack:** Phantom Wallet DDoS Attack
- **2 Core Protocol Vulnerabilities:** Solana ELF Address Alignment Vulnerability Incident, Solana JIT Cache Bug Incident

**2025 Q1: 2 Incidents**

- **2 Application Exploits:** NoOnes Platform Exploit, Loopscale Exploit

### [Observations](https://www.helius.dev#observations)

- **Application Exploits** are the most common, reflecting vulnerabilities in decentralized applications (dApps), programs, and wallets. Peaks in 2022 (12 incidents) and 2024 (6 incidents) align with DeFi and NFT growth.
- **Supply Chain** Attacks emerged in 2024, targeting third-party dependencies as Solana’s ecosystem expanded.
- **Network-Level Attacks** are infrequent but cause significant outages, concentrated in 2021–2022 during high-traffic events (e.g., IDOs, NFT mints).
- **Core Protocol Vulnerabilities,** though fewer, pose systemic risks due to their impact on the entire blockchain, with incidents spread across 2020–2024.
- **Incident frequency** peaked in 2022 (15 incidents), driven by Solana’s growing adoption and attack surface.

### [Severity Classification](https://www.helius.dev#severity-classification)

- **High Severity** (network-wide outages, losses >$10M): 13 incidents (e.g., Wormhole Bridge, Mango Markets, DEXX)
- **Medium Severity** (losses $1M - $10M): 12 incidents (e.g., Crema Finance, Raydium, Pump.fun)
- **Low Severity** (losses \<$1M or no financial loss): 13 incidents (e.g., SVT Token, ELF Address Alignment, Jito DDoS)

### [Total Financial Losses and Affected Parties](https://www.helius.dev#total-financial-losses-and-affected-parties)

### [Breakdown Of Losses](https://www.helius.dev#breakdown-of-losses)

**Application Exploits**

**Gross Losses**: \~$600M

**Breakdown**:

- Wormhole Bridge: $326M (fully reimbursed)
- Mango Markets: $116M (net $49M after $67M returned)
- Cashio: $52.8M (net $25M after $27.8M returned by hacker)
- DEXX: $30M
- UXD Protocol: $19.9M (recovered)
- Crema Finance: $8.8M (net $1.6M after $7.2M returned)
- Slope Mobile Wallet: $8M
- NoOnes Platform: $7.9M-$8M
- Audius: $6.1M
- Loopscale: $5.8M (fully recovered)
- Raydium: $4.4M (net \~$0.4M after \~$4M mitigated by team)
- Nirvana Finance: $3.5M (net $1.4M after \~$2.1M restitution)
- Pump.fun: $1.9M (mitigated)
- Banana Gun: $1.4M (mitigated)
- Cypher Protocol: $1.04M (+$317K insider theft)
- Solend (Aug 2021): $16K (mitigated)
- Solend (Nov 2022): $1.26M (mitigated)
- OptiFi Lockup Bug: $661K (95%mostly mitigated)
- Solareum: $520K-$1.4M
- SVT Token: $400K
- Thunder Terminal: $240K
- Aurory: $830K (mitigated)
- Synthetify DAO: $230K
- Saga DAO: $60K
- Tulip Protocol: $2.5M (recovered)

**Mitigated Losses**: \~$469M

- Wormhole: $326M (Jump Crypto)
- Cashio: $27.8M (returned)
- Mango Markets: $67M (returned)
- UXD Protocol: $19.9M (recovered)
- Crema Finance: $7.2M (returned)
- Pump.fun: $1.9M (restored)
- Banana Gun: $1.4M (refunded)
- Save (formerly Solend): $16K + $1.26M (treasury)
- OptiFi: \~$628K (95% team funds)
- Tulip Protocol: $2.5M (recovered)
- Loopscale: $5.8M (recovered)
- Raydium: \~$4M (Team)
- Aurory: $830K (Treasury)
- Nirvana Finance: \~$2.1M (60% restitution distributed)

**Net Losses**:\~$131M

**Affected Parties**: Users (wallets, liquidity providers), protocol treasuries, and DAOs. Users bore most losses, though protocols mitigated significant amounts (e.g., Wormhole, Pump.fun).

### [Supply Chain Attacks](https://www.helius.dev#supply-chain-attacks)

**Gross Losses**:\~ $130K

**Breakdown**:

- Web3.js: \~$130K(unconfirmed)
- Parcl Front-End: Undisclosed

**Mitigated Losses**: \~$0M

**Net Losses**: \~$130K

**Affected Parties**: Users interacting with compromised dApps or extensions, with losses primarily user-borne.

### [Network-Level Attacks](https://www.helius.dev#network-level-attacks)

**Gross Losses**: $0 (no direct theft)

**Indirect Losses**: SOL price volatility (e.g., 15% drop during Grape Protocol, 10% during Candy Machine) and disrupted transactions.

**Affected Parties**: Entire Solana ecosystem (users, dApps, validators).

### [Core Protocol Vulnerabilities](https://www.helius.dev#core-protocol-vulnerabilities)

**Gross Losses**: $0 (no direct theft)

**Indirect Losses**: SOL price drops (e.g., 13.9% during Durable Nonce Bug, 5% during Turbine Failure) and transaction disruptions.

**Affected Parties**: The entire Solana ecosystem.

### [Total Losses Across All Categories](https://www.helius.dev#total-losses-across-all-categories)

- **Gross Losses**: \~$600M
- **Mitigated Losses**: \~$469M
- **Net Losses**: \~$131M

**Indirect Losses**: Unquantified but significant due to SOL price volatility and transaction disruptions.

Who Bore the Impact?

- **Users**: Primary victims in Application Exploits (e.g., Slope Wallet, DEXX, Solareum) and Supply Chain Attacks (e.g., io.net, Parcl), losing funds from wallets or liquidity pools.
- **Protocols/DAOs**: Absorbed losses in some cases (e.g., Solend’s $1.26M, Raydium’s compensation) or shut down (e.g., Cashio, Nirvana).
- **Ecosystem-Wide**: Network-Level Attacks and Core Protocol Vulnerabilities disrupted all users, dApps, and validators, with indirect losses from SOL price drops.
- **Mitigation Efforts**: Protocols like Wormhole (Jump Crypto), Pump.fun, and Banana Gun fully reimbursed users, while others (e.g., Raydium, OptiFi) partially compensated via treasuries or team funds.

### [Evolution of Solana’s Security Response](https://www.helius.dev#evolution-of-solanas-security-response)

Solana’s security response has improved over time, as evidenced by faster incident response times, more robust remediation strategies, and ecosystem-wide enhancements.

### [Incident Response Speed](https://www.helius.dev#incident-response-speed)

**Application Exploits**

- **Early Incidents (2022)**: Responses ranged from hours to days (e.g., the Wormhole was patched in hours, Cashio shut down the same day, but there was no recovery).
- **Later Incidents (2024–2025)**: Minutes to hours (e.g., Pump.fun halted trading in \<1 hour, Banana Gun shut down bots in minutes, Loopscale paused markets same-day).
- **Trend**: Enhanced detection via real-time monitoring and community alerts (e.g., CertiK, ZachXBT).

**Supply Chain Attacks**

- Rapid responses due to external detection (e.g., Web3.js deprecated packages in \~5 hours).
- **Trend**: Improved coordination with third-party providers (e.g., Cloudflare, npm).

**Network-Level Attacks**

- **Early Incidents (2021–2022)**: Long outages (17 hours for Grape Protocol, 7 hours for Candy Machine) due to validator coordination challenges.
- **Later Incidents (2023–2024)**: Mitigated in minutes (Jito) or hours (Phantom) with better anti-DDoS measures. No Outages.
- **Trend**: Stronger infrastructure resilience.

**Core Protocol Vulnerabilities**

- **Early Incidents (2020–2022)**: Outages lasted 4.5–9 hours (e.g., Turbine Bug, Durable Nonce Bug).
- **Later Incidents (2024)**: 5-hour recovery (JIT Cache Bug) and preemptive patching (ELF Address Alignment, no outage).
- **Trend**: Faster patch deployment and private disclosure protocols.

## [Remediation Strategies](https://www.helius.dev#remediation-strategies)

**Application Exploits**

- **Early**: Limited remediations, with some protocols shutting down (e.g., Cashio, Nirvana).
- **Later**: Robust fixes (e.g., Wormhole’s signature validation, Raydium’s multisig upgrade) and compensation plans (e.g., Pump.fun, Banana Gun).
- **Trend**: Increased focus on audits, oracle security, and privileged access controls.

**Supply Chain Attacks**

- Implemented 2FA for third-party accounts (e.g.,.web3.js) and package monitoring (Web3.js).
- **Trend**: Greater emphasis on securing external dependencies.

**Network-Level Attacks**

- Anti-bot measures (e.g., Metaplex’s botting penalty) and anti-DDoS protections (e.g., Jito, phantom).
- **Trend**: Proactive infrastructure hardening.

**Core Protocol Vulnerabilities**

- Patches for specific bugs (e.g., Turbine deduplication, JIT cache fix) and long-term upgrades (e.g., QUIC adoption).
- **Trend**: Faster patch cycles and ecosystem coordination.

### [Ecosystem-Wide Improvements](https://www.helius.dev#ecosystem-wide-improvements)

- **Audits**: Mandatory post-2022 (e.g., Cashio’s unaudited collapse highlighted risks).
- **Bug Bounties**: Offered in several incidents (e.g., Wormhole’s $10M, Raydium’s 10% bounty), with Crema’s $1.6M as a notable payout.
- **Community Vigilance**: Security firms (CertiK, SlowMist) and individuals (ZachXBT) enhanced detection.
- **Validator Coordination**: Improved for Core Protocol incidents, reducing restart times (e.g., 5 hours for JIT Cache Bug vs. 9 hours for Turbine Bug).
- **Third-Party Security**: Strengthened post-2024 Supply Chain Attacks (e.g., Cloudflare, npm).

## [Conclusion](https://www.helius.dev#conclusion)

Solana’s security history reflects the challenges of a high-throughput blockchain with a rapidly growing ecosystem. Application Exploits dominate due to dApp vulnerabilities, while Supply Chain Attacks and Core Protocol Vulnerabilities highlight emerging and systemic risks. Gross financial losses total approximately **\~$600M**, with **\~$469M** mitigated through reimbursements, recoveries, and protocol interventions, resulting in net losses of **\~$131M**, primarily borne by users. Solana’s security response has evolved, with faster response times, robust remediations, and ecosystem-wide improvements, including robust audits and bounties. Addressing persistent gaps in program design, oracle security, and third-party dependencies through stricter audits, decentralized oracles, and infrastructure hardening will enhance Solana’s resilience, supporting its goal of scalable, secure blockchain innovation.

## Related Articles

## Subscribe to Helius

Stay up-to-date with the latest in Solana development and receive updates when we post
