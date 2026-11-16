# 🌐 LayerZero: The New Standard for Web3 Security and Interoperability

- **Source URL:** https://layerzero.network/blog/the-default-is-many-chains
- **Fetched:** 2026-11-16
- **Channel:** @defendor_eng
- **Telegram message:** https://t.me/defendor_eng/1021 (id 1021)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
This essay provides an overview of the current state of interoperability, focusing first on the solutions available to developers: token standards that let assets live on every blockchain, security that applications control, and messaging that makes data as portable as tokens.

It then turns to three case studies showing how these technical solutions are being implemented to accelerate blockchains (counter-intuitively), institutional tokenization (specifically stablecoins), and AI agents (chain-agnostic entities) through products that work across every chain.

Interoperability creates a new design space. Once issuance, deposits, transfers, and exchange work the same everywhere, the industry can move on to harder, more meaningful problems instead of interoperability itself.

Let’s break this down.

#### **1. Tokens That Exist Everywhere**

Crypto has become a market defined by choice, not consolidation. Assets now need to be wherever that choice takes them. LayerZero is built for this reality.

Each month seemingly brings a new blockchain with its own edge or a refinement of one already operating. Some built for institutions. Some built for decentralization. Some built for consumers. Some purpose built for speed, privacy, or new execution models. Demand moves with these ecosystems. Liquidity shifts. Users migrate. Entire communities form around where the next experience lives.

LayerZero’s solution for enabling fungible assets to exist on multiple blockchains at once is called [the OFT Standard](https://layerzero.network/blog/explaining-the-oft-standard). It is supported across 170+ chains, from Ethereum to Solana to Aptos.

By tracking global supply at the contract level, the OFT Standard enables asset issuers to create a single, *consistent* experience everywhere for their token. This prevents double-spending by users moving between blockchains and preserves parity for assets being used in DeFi apps across blockchains. It is essentially a global solution for tokenization that works across blockchains with every type of asset.

With LayerZero’s OFT Standard, asset issuers can access the benefits of crypto without compromise:

1. **Issue on many chains (**L1, L2, rollups, and non-EVM) under one simple contract interface.
2. **Connect existing tokens**, unifying the supply of a stablecoin or RWA that exists on multiple chains into a single asset.
3. **Expand existing tokens,** enabling an asset issuer to start on a home chain and extend anywhere, anytime.
4. **Burn on one chain, mint on another**, ensuring total supply stays accurate when transferring between chains.
5. **Zero slippage transfers,** letting tokens move via messages without needing a middleman for liquidity.

The last bullet point is the most important for end holders of OFTs. This means asset holders can move tokens between chains at an unlimited size for just the price of gas, no slippage.

For example:

- A user recently [moved $80M](https://x.com/PrimordialAA/status/1880037346265223349) in USDT0 from Ethereum to Ink in 2 minutes for $5.
- A user moved [$1,000,000 in TRUMP](https://x.com/PrimordialAA/status/1881489895618929130) for $0.001 and 29 seconds from Solana to Avalanche.

This is not just important for DeFi native-assets. Today, money and traditional assets can move onchain further, faster, and without limits in a way that is simply not possible in legacy systems. For instance, Ondo Finance has [tokenized 400+ stocks](https://x.com/PrimordialAA/status/1881489895618929130) with the OFT Standard and [61% of stablecoins](https://messari.io/report/layerzero-scaling-stablecoin-issuers-with-the-oft-standard) move with LayerZero.

This is the benefit of crypto as better money technology: both dollars and memes can move anywhere, at any time. Any token (be it a stablecoin, RWA, gas token, or DAO governance asset) can be issued and transferred anywhere there is demand.

With LayerZero solving compatibility across blockchains, asset issuers can focus on [go-to-market strategy](https://layerzero.network/blog/the-inevitable-future-of-stablecoins) instead of getting to market, evaluating new blockchains as distribution channels rather than complex technical projects with added risk and cost. For example, with the OFT Standard, [PENGU launched on Solana](https://x.com/StargateFinance/status/1885483476306006345) and expanded to Abstract on day one with LayerZero. From there, PENGU expanded to Hyperliquid as well. Asset expansion is an ongoing distribution effort across the full stack.

Overall, the OFT Standard acts as streamlined *accounting software* for asset issuers, allowing token smart contracts on hundreds of chains. Tokens that can exist on every chain are the first interop use case to find true product market fit.

**Over $75B** in assets rely on the OFT Standard — spanning stablecoins like [USDT0](https://x.com/USDT0_to) and [PYUSD (PayPal USD)](https://x.com/PayPal/status/1856492017032860002) to commodities like [XAUT0](https://www.theblock.co/post/374786/tether-linked-usdt0-and-xaut0-launch-on-solana-via-layerzero-tech), to yield bearing tokens like [USDY (Ondo)](https://x.com/Ondo/status/1865465043866812611), to wrapped assets like [WBTC (BitGo)](https://x.com/LayerZero_Core/status/1833891554643067335) and [weETH (EtherFi),](https://x.com/ether_fi) along with gas, governance, meme, and utility tokens such as CAKE, WIF, APE and ZRO.

The OFT Standard is one of the most important building blocks for a multichain economy, it works across chains (170), across assets ($75B worth), and is quietly becoming the de facto way to launch tokens in 2026.

#### **2. Applications That Own Their Security**

For builders deciding where to allocate development resources, expanding across chains has historically meant a higher risk profile: more surface area, more attack vectors, and more to secure.

LayerZero’s technology is designed to give application developers the freedom to decide who verifies messages going between chains within their applications. Each app (or token issuer) chooses from a marketplace of permissionless verifiers called [Decentralized Verifier Networks (DVNs)](https://layerzero.network/blog/explaining-decentralized-verifier-networks). An application’s selected set of DVNs must sign off each transaction, attesting to its validity.

Applications themselves can change the security details of their implementation of LayerZero. This allows teams to focus on a set of trusted parameters that can scale as they do. Applications may choose any combination of DVNs to be part of their ***security stack***. An application’s security stack is made based on the DVNs that best fits use-case, speed, and price needs.

- A small NFT-based game might choose a 3/3 DVN set focused on fast and cheap verification.
- An institution using LayerZero for stablecoin issuance might set a security stack of 8/12 DVNs, meaning 8 of 12 DVNs must sign off on each tokenized dollar transfer. Furthermore, institutions can run their own DVN infrastructure to sign their own messages.

By enabling developers, not the LayerZero protocol itself, to choose who verifies transactions, [***sovereignty over security***](https://layerzero.network/blog/sovereignty-over-your-security-matters) *is shifted fully to the application itself.*

For example, BitGo’s WBTC has a security stack that includes a required signature from BitGo, along with additional attestation from the LayerZero Labs DVN and Nethermind DVN.

This decision to make LayerZero security application-owned drives DVNs to compete across client type, location, verification methodology, extra context attestations (i.e. sanctions checks, off-chain security integrations, etc), speed, and other verticals so that applications choose them. At the moment, [over 50 DVNs are available](https://docs.layerzero.network/v2/deployments/dvn-addresses) for apps to choose from when building with LayerZero.

- **Enterprise signers** like [Google Cloud](https://layerzero.network/blog/layerzero-google-cloud) or [Animoca/Blockdaemon](https://docs.blockdaemon.com/docs/blockdaemon-dvn-addresses).
- **zk-based verifiers** like [Polyhedra](https://bravenewcoin.com/insights/polyhedras-zkbridge-integrates-flare-to-enhance-cross-chain-security-with-zk-proofs), which rely on zero-knowledge proofs.
- **Application verifiers** include teams that run verifiers for their own apps, such as [BitGo](https://layerzero.network/blog/layerzero-selected-by-bitgo-for-wbtc) and [Paxos](https://layerzero.network/blog/paypal-usd-pyusd-integrates-layerzero).

Applications can also choose to implement a wide variety of other security configurations into their LayerZero products, such as [rate limits](https://docs.layerzero.network/v2/developers/evm/oapp/message-design-patterns#rate-limiting), increasing/decreasing block confirmations between blockchains, blacklisting/whitelisting tokens or certain addresses, among others. These controls can be embedded at the smart contract level (which developers control, not LayerZero), or at the DVN level.

Furthermore, the “[Endpoints](https://docs.layerzero.network/v2/concepts/protocol/layerzero-endpoint)” of the LayerZero protocol – the contracts that exist across 170+ blockchains and are used to send/receive messages – are immutable. Deployed once, they exist onchain without the ability of anyone to change them. These Endpoints have facilitated 160 million messages across chains, have a $15M bug bounty associated with them, and, with over 620 teams using the Endpoints (equating to 59,000 contracts), they are some of the most-used contracts in crypto.

Overall, sovereignty over security is:

- **Configurable**: Apps can switch DVNs if one goes down or acts maliciously.
- **Programmable**: Apps add logic like rate limits or block finality parameters (e.g., requiring a message to be final on the source chain for 10 blocks before bridging).
- **Immutable**: Apps interacting with LayerZero can rest assured that the only parameters that can be changed (DVNs, rate limits, etc) only by them. LayerZero is just an immutable framework to send/receive messages across chains.

Immutability of the messaging interface combined with the customizability of security parameters gives builders a very wide design space to work with when bringing an asset or application to market.

With LayerZero, the actual implementation of an application – from chain deployment, verification, and other security parameters – are all configured and owned by the applications themselves. Just as it should be in crypto.

#### **3. Applications That Exist Everywhere**

Token deployment and security are only the starting point with LayerZero. This is the baseline required to expand across chains.

Additional unlocks emerge when developers can send arbitrary data across chains and pull reliable data from anywhere. All within the same trust-minimized framework that token issuers use for asset expansion. This upgrade in communication for multichain apps is what enables businesses to build more complex products.

LayerZero’s protocol supports arbitrary [messaging](https://docs.layerzero.network/v2/developers/evm/oapp/message-design-patterns#message-passing) that extends cross-chain operations to any function call that can be embedded and sent via a data packet. Rather than just burning and minting assets, this enables developers to trigger events, execute transactions, or send complex logic across multiple chains as if the app were in one unified environment.

Applications can send messages between chains using LayerZero’s [OApp contract standard](https://docs.layerzero.network/v2/developers/evm/oapp/overview). This is available across all chain types – EVM, alt-VM, L1, L2, private, and public.

Examples of apps using messages to send business logic across chains:

- [**EtherFi**](https://layerzero.network/blog/introducing-native-l2-restaking): Streamlining multi-chain staking operations, allowing minting and syncing of staked assets (e.g., weETH, eBTC) on L2s while the main protocol exists on the L1. EtherFi often sends 200 messages per day across 19 chains.
- [**Pendle**](https://layerzero.network/blog/how-pendle-built-a-7b-protocol-everywhere): LayerZero enables cross-chain veTokenomics for Pendle, allowing DeFi participants to experience seamless cross-chain voting and rewards boosting, and to earn rewards on any supporting chain.
- [**Stargate**](https://stargate.finance/): Uses LayerZero messaging for locking and unlocking assets across dozens of chains, and keeping liquidity balanced across 40 chains.

Here is an example of EtherFi’s L2 Native Restaking Module:

*(Note: As with everything above, security is also configurable through the choice of DVNs.)*

***Another use case for messaging is intents.*** Messaging and intents is not an “either or” debate – it is a “yes and” conversation. With intents, messaging is the settlement layer: complementary, not competitive. In other words, messaging is the backbone of intents and is what enables an intent network to prove that a transaction was filled on the destination chain back to the source chain.

- For example, LayerZero is [used by Aori](https://www.aori.io/research/posts/fast-swaps) to power Fast Swaps on Stargate. This enables cross-chain swaps across blockchains that settle in less than a second.
- LayerZero also powers intents via Mach Exchange, which is live on Solana.

Message sending is just one aspect of bringing real data to all the chains. If OApp is about “sending” data, [lzRead](https://layerzero.network/blog/the-lzread-deep-dive) is about “pulling” data from any chain, or multiple chains at once, and computing it. This information can then be used by a smart contract.

- For example, an app can query data from 10 separate rollups, confirm the results through its chosen DVNs, and finalize logic on one chain, all in a single function call.
- Another example of what can be built is proof of reserves: checking a company’s token reserves or locked assets on one chain to assure solvency or collateralization on another.

We see lzRead in action with:

- **Shadow NFTs**: Verify NFT ownership on any lzRead supported chain without needing to bridge. Already [live](https://x.com/0xQuit/status/1869499712203825396) for Bored Apes, Mutant Apes, and Q00ts with many more to come.
- **Governance:** Through a multichain governor module, [**Agora**](https://www.agora.xyz/blogs/3-multichain-voting) voters are able to cast a vote in a single transaction using voting power 100+ chains.
- **Token Claims:** Users could claim ANIME on an L2 without bridging their NFT outside the L1 during the [**Azuki Claim**](https://x.com/LayerZero_Core/status/1882195193862226341).

With messaging and lzRead, LayerZero is expanding from basic token expansion to extending business logic between chains. Builders can send and receive, push and pull, read and compute data across 170+ chains.

Messaging upgrades crypto from a finance alternative to an internet alternative, with applications able to send/receive data packets across many different environments.

In other words, where the internet connected computers, LayerZero connects blockchains. And as global communication started to thrive once the computers were connected at scale, so will global finance begin to thrive as the blockchains get connected at scale.

### **Interoperability In Action: Blockchains, Institutions, AI**

If something can be tracked on a ledger, crypto rails increase its velocity and reduce its reliance on intermediaries. And today, the basics are no longer aspirational, as shown above.

- Tokens are everywhere.
- Applications own their security.
- Data can move across chains.

With these primitives in place, the next phase isn’t about onboarding to crypto, but building across all chains simultaneously. The question is no longer *if* you expand to many chains or *how* you do it, but *what* building on many blockchains can unlock.

In other words, the connectivity of blockchains is no longer the challenge. It’s the accelerator. It pulls the ecosystem together and creates real advantages for chains, institutions, AI, and more.

But don’t just take our word for it…

#### **1. Connecting Blockchains to All of Crypto**

In the early days of blockchain proliferation in 2020-2022, each new blockchain seemed fixated on becoming an isolated winner, locked in a zero-sum race for users and liquidity.

By 2026, that mindset has *somewhat* shifted. Crypto appears to recognize that different chains serve different niches, from DeFi to IP management to specialized VMs for apps. And all of them, old or new, benefit from being connected.

This can be seen in the chains’ go-to-market strategies, which have baked in LayerZero from day one.

- **Plasma** [embedded](https://dune.com/layerzero/layerzero?Chain+Analyzer+Chain+Name_e0f5bb=Plasma#chain-analyzer) LayerZero directly into its launch for users by using Stargate as its bridge and enabling major assets to expand with the OFT Standard expansion. Within its first week, over $8B in deposits flowed into Plasma via assets like USDT0, USDe, and weETH, wherein Plasma became one of the top-10 blockchains by TVL within days.
- **Berachain** addressed the “cold start” liquidity problem through [Boyco](https://layerzero.network/blog/boyco-let-the-bera-eat), which pooled over $3B in vaults from protocols like Ethena, and EtherFi on Ethereum and bridged them to Berachain on week of launch using LayerZero messaging. Once Berachain launched, [LayerZero was used as the canonical bridge for Berachain, facilitating 60,000 messages to the chain in its first week live,](https://x.com/berachain/status/1891554295394468130) along with another $1.5B in value transfer in addition to Boyco.

Furthermore, already launched blockchains saw new flywheels when integrating LayerZero at different levels of the stack:

- [Together with Offchain Labs, LayerZero Labs designed a system that treats OFTs as native tokens on Arbitrum Orbit chains](https://layerzero.network/blog/oft-standard-natively-supported-on-arbitrum-orbit). Orbit chains can even designate an OFT as their gas token, guaranteeing a single, unified supply across the Arbitrum ecosystem, as seen with Apechain. Most recently, this enabled Ethereal to launch using USDe as a gas token.
- Flow developer activity [increased by 602%](https://x.com/LayerZero_Core/status/1958964021153210634) after integrating with LayerZero. They were also able to onboard PYUSD to the network as an OFT, which soon flipped USDC to become the main stablecoin used in DeFi on Flow.
- Over twenty gas tokens expanded to new blockchains in 2025 with LayerZero, including Aptos’ APT, Sei’s SEI, and Sonic’s S. In this perspective, the OFT Standard is being used as a listing technology for L1 assets, enabling them to trade on popular onchain exchanges like PumpSwap and Hyperliquid.

Overall, blockchains are now designed with interoperability at the front of their roadmap. For new blockchains, by weaving in LayerZero right at mainnet launch, the bridging friction of the past is gone. No wrapped-asset sprawl, no guesswork about which cross-chain tool to trust. For older chains, interop connects their assets to new networks and liquidity, and links their existing hubs to the rest of crypto.

Whether it’s Berachain amassing $3B in deposits pre-launch, Arbitrum Orbit enshrining OFTs, or Aptos moving APT to Solana,chains have never been more specialized and have never been so obviously part of something bigger: crypto. Applications and assets are being decoupled from chains, enabling tokens and smart contracts to expand to where the users and liquidity are – even if they are first built natively for a single blockchain.

The same way the internet is a “network of networks,” the “crypto stack” is quickly becoming a network of blockchains, each optimized for certain domains yet connected via standardized messaging and verifiers – interop and LayerZero.

#### **2. Institutions Use Interoperability To Build With All Of Crypto**

Institutions and enterprises have historically approached crypto with caution, but in 2026, they’re actively engaging with the blockchain rails in a variety of ways, from tokenization to payments.

Crypto gives institutions tooling that is just better than what exists in legacy systems. When institutions see crypto, they see the magic of blockchains:

- **24/7 Availability**: No “bank holidays” or waiting for clearinghouses. Capital moves any time, anywhere.
- **Global Liquidity**: Banks in Singapore, a DeFi protocol in Europe, and a hedge fund in the U.S. can settle trades in seconds. .
- **Programmable**: Onchain logic via smart contracts eliminates middlemen and layers of bureaucracy, reducing errors and overhead.
- **Infinite Customization**: A stablecoin issuer can run its own DVN, earn fees, or reconfigure block finality to align with institutional risk requirements, all within a smart contract.

Deploying on many blockchains is the norm for large-scale businesses entering the crypto space. They care not about how many chains there are, but how to utilize crypto rails best by issuing assets or providing infrastructure to either monetize a product or make a product more efficient. Interop is simply a tool institutions can use to get the best of all the blockchains, enabling developers to create the best product by picking and choosing settlement layers without the bias or tribalism that comes with being crypto-native.

From stablecoin issuance to tokenized treasuries and beyond, institutions come into crypto and take multichain as state of the world.

**Stablecoin Interoperability:**

- [**PayPal USD**](https://x.com/PayPal/status/1795853572048871920) connected its stablecoin between Ethereum, Arbitrum, and Solana via LayerZero, enabling PYUSD to move between chains for just the cost of gas. By utilizing LayerZero, users who self-custody their PYUSD tokens can seamlessly transfer assets between blockchains -- without needing to rely on centralized platforms like Venmo or PayPal. It has also brought [PYUSD0](https://layerzero.network/blog/layerzero-brings-global-distribution-to-paypal-usd) to nine other blockchains with LayerZero.
- [**USDtb**](https://x.com/LayerZero_Core/status/1868669932185219323): USDtb is a stablecoin backed by BlackRock's BUIDL fund and tokenized by Securitize through Ethena. USDtb is now live on Arbitrum, Solana, Base, and Ethereum, powered by LayerZero.

**Infrastructure Interoperability:**

- [**Deutsche Telekom:**](https://layerzero.network/blog/deutsche-telekom-mms-joins-layerzero-as-dvn) Leveraging its trusted Open Telekom Cloud (OTC) infrastructure, Deutsche Telekom MMS operates a DVN to offer institutional clients - including banks, stablecoin issuers, and exchanges - as a secure, compliant, and scalable platform.
- [**Google Cloud**](https://layerzero.network/blog/layerzero-google-cloud) runs a DVN that is available to any application sending messages across the 14 chains it supports.
- [**Ubisoft**](https://blockworks.co/news/ubisoft-layerzero-blockchain-network-crypto-game)**:** Ubisoft runs its own DVN to verify crypto assets that are being moved or bridged from one blockchain to another by its gaming orgs and players.

**Tokenization Interoperability:**

- [**Dinari**](https://layerzero.network/blog/dinari-layerzero-tokenized-us-equities-global): LayerZero connects Dinari’s permissioned Layer 1, the Dinari Financial Network (DFN) powered by Avalanche, with 170+ chains. This enables Dinari’s tokenized equities, known as dShares™, to move and settle seamlessly across blockchains. The DFN provides the compliance, settlement, and throughput standards required for institutional-grade trading, while LayerZero extends this infrastructure across networks to support high-volume market activity. Launching on four blockchains with 200 tokens and expanding over time to LayerZero’s broader ecosystem of more than 170 blockchains and the full list of tickers on the U.S. stock market, the integration establishes a unified foundation for liquid, onchain markets where real-world equities can transact with the efficiency and accessibility of digital assets.
- [**Ondo Finance**](https://layerzero.network/blog/ondo-finance-goes-omnichain-with-layerzero), the #1 issuer of tokenized US Treasuries, deployed its yield-bearing USDY across three chains via LayerZero, letting investors anywhere into the world get exposure to yield from tokenized T-bills. It is also deploying its tokenized equities product, Ondo Global Markets, across blockchains with LayerZero, [enabling 400+ stocks](https://x.com/LayerZero_Core/status/1963236722634084682) to trade natively on many chains.
- [**Libre Capital**](https://x.com/LayerZero_Core/status/1907807346178560121) selected LayerZero to bring tokenized funds to 125+ blockchains. Libre puts global private markets onchain by tokenizing funds from industry leaders such as BlackRock, Brevan Howard, and Hamilton Lane. Going forward, institutional funds issued through Libre can tokenize on their choice of chains supported by LayerZero.

**Application Interoperability:**

- [**Project Guardian**](https://layerzero.network/blog/automating-portfolio-management-with-layerzero), led by JP Morgan and MAS (Monetary Authority of Singapore), slashed 3,000 manual steps into one automated transaction by adopting cross-chain messaging via LayerZero in a proof of concept establishing that crypto rails make asset rebalancing more efficient than legacy solutions.
- **IntellectEU** [demoed a cross-chain Delivery vs. Payment (DvP) concept](https://layerzero.network/blog/cross-chain-dvp), connecting Swift to onchain settlement via Polygon and Hyperledger Besu using LayerZero messaging. This drastically cuts settlement time and risk, replacing a tangled web of partial solutions with a single, always-on mechanism that is powered by interop.

The examples above are barely scratching the surface of what is possible with large-scale adoption of crypto. The blend of messaging, data queries, and tokenization derived from interop is a powerful lever for institutions.

***- Past state:*** institutions play with crypto to test the benefits of blockchains

***- Current state:*** institutions deploy on chains in a limited capacity

***- Future State:*** the chains become the institutions and the institutions become apps built on top of them

Going forward, institutions could automate complex instructions (e.g., rebalancing, cross-chain swaps, derivatives trades) with smart contracts via messaging. Data queries from multiple chains (pulling reserves data, historical prices, or user balances) could enable real-time analytics and automated compliance. From RWAs (treasuries, mortgages) to more abstract instruments, institutions might leverage OFTs for tokenization across many networks, seamlessly bridging, and/or “settling” transactions.

Ultimately crypto is becoming a many-chains-first financial layer whose capabilities (24/7 access, unstoppable programmability, global composability) far exceed what legacy finance can offer.

#### **3. AI Tooling Builds Everywhere In Crypto**

LayerZero is a [natural fit for autonomous finance](https://layerzero.network/blog/interop-accelerates-crypto-ai-agents). AI agents are inherently chain-agnostic and go wherever the optimal outcome is, be it yield, liquidity, or token prices. They act continuously and without the constraints that shape human behavior. LayerZero already supports some of crypto’s most-used contracts. We’re built for this shift.

Interop also gives AI agents the tools to interact with the entirety of crypto via push and pull messaging.

1. **Push Messaging**: Agents can send data or tokens from one chain to another (bridging stablecoins, swapping for ETH, re-staking) in a single flow.
2. **Pull Messaging (lzRead)**: Agents can retrieve real-time or historical data from many chains at once, fueling more intelligent decisions. An agent might check multiple DEX pools, gauge user balances, or query offchain data in verifiable form, all in one function call.

AI is already integrating LayerZero at scale. Developers are already creating AI agents that operate onchain.

- [**Halliday:**](https://x.com/LayerZero_Core/status/1892635335735312583) With Halliday, you can create high-level workflows without writing a single line of smart contract code. Halliday handles all the heavy lifting underneath: protocol integrations like LayerZero and DEXs, data translation, and reliable multi-chain execution.
- [**Wayfinder**](https://www.youtube.com/watch?v=stLMS_dPjdA): Demonstrated an agent that **bridges ETH to Base** via LayerZero, then **swaps** a portion of those funds for another token, coordinating multi-step logic automatically.

Coordinating capital, verifying state, and paying each other without human involvement. These agents operate at a speed and scale no traditional user or business can replicate. If AI agents soon outnumber active human users online, what does that mean for crypto?

With LayerZero providing real-time access to onchain data, messaging available to sync states across any chain, and tokenization being as easy as using a contract standard, the sophistication that an AI agent can create using interop is only going to expand.

In the future, AI agents might interact with crypto via interop in scenarios such as…

- **Agent-to-agent payments**: Automate cross-chain escrow or job completion payouts, leveraging the unstoppable, 24/7 nature of crypto.
- **Rebalancing:** Gather portfolio info across chains, find the best yields, and finalize trades in seconds, bridging only once or twice at the end, no repeated manual bridging steps.

Furthermore, as AI and cross-chain infrastructure advance, much of the underlying complexity will disappear from the user experience. People will interact with an app or agent and behind the scenes it:

- **Deploys** a yield vault on Plasma,
- **Reads** data from Ethereum,
- **Settles** final transactions on Monad,
- **Mints** an NFT on Story, and
- **Bridges** for a flash loan on Avalanche or MegaETH

All collapsing into a single transaction from the user’s point of view. No “bridge UI,” no multiple steps, no repeated confirmations, just the final result. LayerZero becomes as hidden as TCP/IP for the internet: essential, but invisible.

As these agents evolve, they’ll manage more capital, launch more tokens, and even run entire dApps autonomously.

This growing complexity is exactly why LayerZero matters. By unifying every chain through a single messaging and data layer, AI-driven use cases gain a durable foundation to operate without friction.

### **The Conclusion Is Acceleration.**

The primitives are in place. Tokens move everywhere, apps own their security, and data flows across chains to power applications. What was once constrained is ready to be used at scale.

- **Tokens** (OFTs) can be issued, managed, and transferred across chains quite easily.
- **Sovereignty** over DVNs lets applications expand across chains without giving up control of their security model.
- **Messaging & data** standards empower builders to build smart contracts that use onchain data for complex use cases.

**Now, LayerZero accelerates crypto**:

- **Differentiated chains** launch with composability, not competition, in mind.
- **Institutions demand many chains** as soon as they launch.
- **AI agents** are naturally chain agnostic.

The endgame is for LayerZero to become invisible.

Just as the internet’s protocols are hidden under everyday user experiences, the day is coming when a user’s wallet, dapp, or AI agent seamlessly engages with dozens of chains behind the scenes. Tokens, data, and logic will all flow unimpeded.

The result: a truly global, open, and programmable financial system that transcends any single blockchain.

The foundation is built. Everything past this is acceleration.

What’s next? **Crypto at internet scale.**
