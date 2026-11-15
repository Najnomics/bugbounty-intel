# 🌐 Frontend Hijack Attacks Target Web3 Protocols

- **Source URL:** https://blockaid.io/blog/frontend-hijacking-and-the-web2-attack-surface-threatening-web3-protocols
- **Fetched:** 2026-11-15
- **Channel:** @defendor_eng
- **Telegram message:** https://t.me/defendor_eng/1367 (id 1367)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Frontend Hijacking and the Web2 Attack Surface Threatening Web3 Protocols

## **Executive Summary**

Between February 16 and February 23, 2026, Blockaid identified and responded to a coordinated campaign of frontend compromises targeting five DeFi protocols: OpenEden, Curvance, Smithii, Avantis, and Nerochain, all within a single week. Each compromised frontend was injected with the AngelFerno drainer, one of the largest active wallet drainer operations in crypto.

In each incident, the attacker socially engineered domain registrar support staff into granting unauthorized access to the protocol's domain account. From there, they redirected DNS records to attacker-controlled infrastructure and deployed a fake version of the protocol's frontend. Any user who connected a wallet or engaged with the frontend was exposed to a wallet drainer hidden behind a UI that looked identical to the real thing.

This campaign is also a clear illustration of how modern Web3 attacks operate across both onchain and offchain layers. The malicious actors never exploited a smart contract or manipulated onchain infrastructure. Blockaid's ability to monitor across both layers is what made it possible to detect each compromise in real time and protect users before funds were lost.

## **What is a Frontend Hijack?**

A frontend hijack is when an attacker takes over the legitimate website of an established protocol and replaces it with a malicious version. This is made possible by targeting the web2 infrastructure that every Web3 protocol depends on, the domain name system (DNS). When an attacker gains control of a protocol's DNS records, they can silently redirect that URL to their own server, serving a fake version of the site to every user who visits it, without touching a single line of smart contract code.

Once that fake frontend is in place, the attacker embeds a crypto drainer into it, malicious code that tricks users into connecting their wallets and signing a transaction that instantly siphons their assets to attacker-controlled addresses, often before the victim realizes anything has happened.

## **How a Frontend Hijack Actually Works**

While every frontend hijacking incident has its own specifics, the underlying attack chain tends to follow a consistent playbook. Rather than targeting smart contracts or onchain infrastructure, attackers exploit the web2 layer that every Web3 protocol depends on to reach its users, working through four key steps to take control of a legitimate site and turn it into a trap.

- **Social Engineering** - The attacker contacted domain registrar support employees directly and manipulated them into granting unauthorized access to the protocol's domain account, without ever needing to compromise the protocol itself.
- **DNS Redirection** - With domain access secured, the attacker redirected DNS records to attacker-controlled hosting infrastructure, in at least three of the five incidents, the same Namecheap hosting servers. From this point, anyone visiting the legitimate domain URL was silently routed to the attacker's infrastructure instead of the real protocol.
- **SSL Certificate Issuance** - To preserve the appearance of a legitimate, secure site and maintain valid HTTPS connections, the attacker issued new SSL certificates for each compromised domain on the day of the attack, both paid Sectigo DV certificates and free Let's Encrypt and Google Trust Services certificates, likely as redundancy across different subdomains and hosting configurations.
- **Malicious Frontend Deployment** - With DNS redirected and fresh SSL certificates in place, the attacker served a fake version of the protocol's interface, visually identical to the real site, embedded with AngelFerno's drainer code. Users who visited the legitimate URL and connected their wallets were prompted to sign what appeared to be normal transactions, which instead immediately drained their assets to attacker-controlled addresses.

What makes this attack chain particularly difficult to detect is that from the user's perspective, nothing looks wrong. The URL is correct, the padlock is green, the site looks identical to the one they've used before. The compromise happens entirely at the infrastructure layer, invisible to the user until it's too late.

## **Why Attackers Exploit Domain Registrars**

This campaign exposes a systemic vulnerability in Web3 that has nothing to do with smart contracts, onchain logic, or protocol code. In every incident, the targeted protocols' onchain assets and treasuries remained completely secure. Instead, they targeted the human layer, support employees at domain registrars, who can be manipulated into transferring domain control without the legitimate owner's knowledge.

This is not a new attack vector. In July 2024, a coordinated campaign compromised Squarespace and GoDaddy-registered domains belonging to Compound Finance, Pendle Finance, Celer Network, and dYdX, deploying the Inferno drainer, the operation that later rebranded as AngelFerno. The February 2026 campaign follows the same playbook, executed faster and across more targets.

## **Who is Angelferno: The Crypto Drainer Powering the Attacks**

AngelFerno is one of the largest and most prominent Drainer-as-a-Service (DaaS) operations in the crypto threat landscape. Operating like a commercial software product, AngelFerno sells access to its drainer toolkit to affiliates, who can then deploy it in their own attacks, including campaigns like the frontend hijacks documented in this report, without needing to build any malicious infrastructure themselves.

What sets AngelFerno apart from a typical drainer operation is the breadth of its product suite. Rather than a single tool, AngelFerno offers a full family of chain-specific drainer variants: AngelFerno EVM targeting Ethereum and all major EVM-compatible chains; SolFerno for Solana; TronFerno for TRON; XRPFerno for the XRP Ledger; and SeedFerno, a cross-chain seed phrase theft tool that claimed over 5,000 seed phrases stolen in its first week after a January 2026 update.

In a separate Blockaid threat intelligence report, we documented how AngelFerno affiliates ran a large-scale distribution campaign across at least 20 coordinated X accounts, linking to 75 distinct malicious dApps between September 2025 and January 2026. The campaign documented in this report represents a significant escalation from that approach, with the attacker bypassing distribution entirely and going straight to the source, hijacking the real sites users already trust.

[Read the report: X as a Primary Distribution Vector of Malicious dApps →](https://www.blockaid.io/blog/how-crypto-drainers-are-using-x-twitter-to-target-web3-users)

## **Recent Frontend Hijacking Incidents**

Between February 16 and February 23, 2026, Blockaid detected and responded to five separate frontend compromise incidents, all delivering the AngelFerno drainer, all using the same attacker infrastructure, and all occurring within a single seven-day window.

- **OpenEden - February 16:** Blockaid flagged AngelFerno activity on OpenEden's portal after the domain was quietly transferred from GoDaddy to Namecheap, with DNS rerouted to attacker-controlled IPs and fresh SSL certificates issued on the same day.
- **Curvance - February 16:** Hours after the OpenEden compromise, Blockaid detected the same AngelFerno drainer on Curvance's app domain, with an identical registrar transfer and attacker infrastructure fingerprint.
- **Smithii - February 18:** Blockaid detected AngelFerno on Smithii's domain two days later. While the initial access vector was not publicly confirmed, multiple SSL certificates were issued on the day of compromise, matching the pattern seen across all five incidents.
- **Avantis - February 21:** Blockaid detected the AngelFerno drainer on Avantis five days into the campaign. The attacker had begun targeting Avantis's Squarespace registrar account three days earlier, extracting billing details through a support call before using them to take over the domain and redirect nameservers to the same Namecheap infrastructure.
- **Nerochain - February 23:** Blockaid detected AngelFerno activity after Nerochain's domain began redirecting users to a separate attacker-controlled site at mainnet.live-nerochain.io, with new wildcard SSL certificates issued for \*.nerochain.io matching the pattern observed across all incidents.

For the full breakdown of this campaign, including IOCs, malicious infrastructure, and compromised domains, [read the complete threat intelligence report →](https://docs.blockaid.io/docs/threat-intel/angelferno-frontend-compromise-campaign)

## **Why Web3 Security Must Combine Onchain and Offchain Intelligence**


Modern Web3 attacks operate across both the onchain and offchain layers. As this campaign demonstrates, attackers can combine onchain infrastructure with offchain methods like social engineering, DNS hijacking, and fraudulent SSL certificates to achieve their goals. An effective Web3 security platform needs to monitor across both layers, onchain signals like malicious addresses and drainer contract signatures, and offchain signals like certificate transparency logs, DNS registrar activity, and real-time web crawling. As Web3 adoption grows, the ability to correlate intelligence across both worlds in real time becomes increasingly critical to detecting and preventing attacks before they impact users and cause loss of funds.

## **How Blockaid Detects Frontend Hijacking in Real Time**

Blockaid continuously monitors onchain and offchain data sources, including certificate transparency logs, DNS registrars, and real-time web crawling, to detect frontend compromises as they happen. By maintaining a constantly updated understanding of both malicious code signatures and malicious infrastructure, Blockaid is able to identify when a legitimate protocol's frontend has been hijacked, flag the compromised domain, and notify affected teams before users are put at risk.

- [**dApp Scanning**](https://www.blockaid.io/dapp-scanning) - Real-time detection of malicious dApps, allowing Blockaid-integrated wallets and platforms to warn users and block interactions before they connect to a malicious drainer.
- [**Address Scanning**](https://www.blockaid.io/address-scanning) - Real-time data on malicious addresses tied to drainer campaigns, including those associated with AngelFerno, allowing platforms to warn users before they interact with a known malicious address.

In all five incidents documented in this report, Blockaid's transaction simulation, validation, and dApp scanning systems detected each compromised domain, securing users on Blockaid-protected platforms across every incident.

[Learn more about Blockaid's Transaction Simulation and Validation →](https://www.blockaid.io/transaction-security)

### **About Blockaid**

Blockaid is the onchain security platform trusted by the largest companies operating in Web3. Built by veterans of elite intelligence and cybersecurity units, Blockaid provides end-to-end protection for financial institutions, protocols, and end users — combining direct wallet and dApp integrations with real-time monitoring, detection, and response across smart contracts, infrastructure, and externally owned accounts. Since 2025, Blockaid scanned over 6.3+ billion transactions and blocked 585+ million attacks. Blockaid is the security infrastructure behind Coinbase, MetaMask, Uniswap, Safe, and dozens of the most widely used platforms in the industry.

Learn more at [blockaid.io](http://blockaid.io), and follow us on [Twitter](https://x.com/blockaid_) and [LinkedIn](https://www.linkedin.com/company/blockaid/).

## Blockaid is securing the biggest companies operating onchain

Get in touch to learn how Blockaid helps teams secure their infrastructure, operations, and users.
