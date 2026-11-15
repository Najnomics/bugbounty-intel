# 🤖 Agentic Payments Are Here, and Security Standards Are Lagging

- **Source URL:** https://www.openzeppelin.com/news/what-are-agentic-payments
- **Fetched:** 2026-11-15
- **Channel:** @defendor_eng
- **Telegram message:** https://t.me/defendor_eng/1821 (id 1821)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# What Are Agentic Payments? The Security Standards Financial Institutions Should Understand

- OpenZeppelin

For most of financial history, a payment required a human decision. Someone authorized a transfer, approved a transaction, or signed off on a settlement. That assumption is changing.

Agentic payments are transactions initiated and settled by autonomous software agents on a user's behalf, with no human in the loop at the moment of payment. The numbers are still early, but the trajectory is not. According to a [2026 Keyrock report](https://keyrock.com/who-pays-the-agent/), AI agents settled over $73 million across 176 million blockchain transactions between May 2025 and April 2026. [Gartner](https://www.digitalcommerce360.com/2025/11/28/gartner-ai-agents-15-trillion-in-b2b-purchases-by-2028/) projects agents could intermediate $15 trillion in purchases by 2028, and [McKinsey](https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-agentic-commerce-opportunity-how-ai-agents-are-ushering-in-a-new-era-for-consumers-and-merchants) estimates $3 to $5 trillion in retail agentic commerce by 2030.

For financial institutions evaluating onchain finance, agentic payments are an emerging layer of infrastructure being built now, and the institutions that understand it early will be better positioned to manage the risks that come with it.

## What an Agentic Payment Actually Is

Unlike traditional automated payments, where scheduled transfers and rule-based triggers execute pre-configured logic at predetermined times, agentic payments involve autonomous systems making real-time financial decisions: selecting a merchant, negotiating a price, initiating a transfer, and settling value, with no human confirmation required.

When the transaction initiator is software rather than a person, questions of authorization, liability, compliance, and auditability take on new complexity.

## Two Camps Building the Infrastructure

The agentic payments landscape is organizing around two parallel tracks:

**The first is a crypto-native track built on open blockchain standards.** [x402](https://x402.org/), an HTTP-native payment protocol settling in stablecoins, is chain agnostic and now governed under the Linux Foundation. Alongside it, the [Machine Payments Protocol](https://stripe.com/blog/machine-payments-protocol) (MPP), co-authored by Stripe and Tempo, offers an alternative open standard supporting both stablecoin and fiat settlement. Emerging Ethereum-specific standards like [ERC-8183](https://eips.ethereum.org/EIPS/eip-8183) (an onchain escrow primitive for agent commerce jobs) are defining how agents transact on blockchain rails. These standards are largely open source, composable, and built on battle-tested smart contract libraries. The x402 protocol alone recorded 75 million transactions and $24 million in volume over a recent 30-day period.

**The second is a consortium and card-network track.** Major card networks have each launched agent payment frameworks focused on extending existing card rails to accommodate machine-initiated transactions. [Google donated its Agent Payments Protocol](https://blog.google/products-and-platforms/platforms/google-pay/agent-payments-protocol-fido-alliance/) to the FIDO Alliance in April 2026, which now houses a dedicated Payments working group with participation from major card networks and payment processors.

These two tracks are not mutually exclusive. Products like [Alchemy's AgentCard](https://agentcard.ai/about), launched in June 2026, are already designed to route through card tokens by default and upgrade to stablecoin-based protocols where merchants support them.

## Why Stablecoins Dominate Early Volume

One of the clearest signals from early agentic payment data is the dominance of stablecoins. The Keyrock report found that 98.6% of agent-settled transactions used USDC, with a median transaction value between $0.01 and $0.10. Seventy-six percent of transactions fell below the $0.30 card-fee floor, a range where traditional payment rails are not economically viable.

This points to a structural reason stablecoin-settled blockchain infrastructure is attracting agent payment activity: micropayments at machine speed and machine scale require settlement infrastructure with near-zero fees and near-instant finality. Card rails, designed for human-scale commerce, were not built for this.

For financial institutions, this has direct relevance to how they think about digital asset infrastructure, stablecoin strategy, and their role in a payments landscape that is beginning to operate at a different order of magnitude.

## The Security and Compliance Questions That Follow

Agentic payments introduce a new attack surface. When agents transact continuously, autonomously, and at high volume, the security properties of the underlying smart contract infrastructure matter enormously. A single vulnerability in a payment primitive propagates as a systemic risk across every agent running on that standard.

For any institution interacting with this infrastructure, the security standards underlying agentic payment protocols carry direct risk management implications. Whether the smart contract libraries underlying payment protocols have been independently reviewed directly affects the risk profile of any institution building on or interacting with that infrastructure.

The compliance dimension is equally unresolved. Agentic payments raise open questions around authorization (who is legally responsible when an agent transacts?), auditability (how do institutions reconstruct a transaction trail when no human initiated it?), and mandate scope (what limits govern how much an agent can spend, and on what?). Emerging standards are beginning to address these questions, but no settled framework yet exists.

## What Comes Next

Agentic payments are not waiting for financial institutions to finalize their positions. The infrastructure is being built, standards are being adopted, and transaction volume is growing. The institutions that understand the landscape now, including the protocols, the standards bodies, the security considerations, and the compliance gaps, will be better positioned to engage with it on their own terms.

## FAQs

## What is an agentic payment?

An agentic payment is a transaction initiated and settled by an autonomous software agent on a user's behalf, with no human involved at the moment of payment.

## How much agentic payment volume exists today?

According to a [2026 Keyrock report](https://keyrock.com/who-pays-the-agent/), AI agents settled over $73 million across 176 million blockchain transactions between May 2025 and April 2026, with 98.6% settling in USDC.

## Why are stablecoins dominant in agentic payments?

Most agent transactions are micropayments below the $0.30 card-fee floor, making blockchain-settled stablecoins more economically viable than traditional card rails.

## What are the two main infrastructure tracks for agentic payments?

A crypto-native track built on open blockchain standards (such as the chain-agnostic x402 protocol and Ethereum-specific standards like ERC-8183) and a consortium track led by card networks and the FIDO Alliance, with some products already bridging both.

## What security and compliance risks should financial institutions consider?

Agentic payments introduce new risks around smart contract vulnerabilities at scale, as well as unresolved questions around transaction authorization, auditability, and agent mandate scope.
