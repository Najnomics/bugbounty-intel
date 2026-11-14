# 🌉 Blockaid: Bridges Lost Another $24.6M to Verification Failures in July-August

- **Source URL:** https://blockaid.io/blog/cross-chain-verification-failures-how-bridges-lost-another-246m-and-how-onchain-teams-stay-protected
- **Fetched:** 2026-11-14
- **Channel:** @defendor_eng
- **Telegram message:** https://t.me/defendor_eng/2115 (id 2115)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Cross-Chain Verification Failures: How Bridges Lost Another $24.6M and How Onchain Teams Stay Protected

## **Executive Summary**

Blockaid's [H1 2026 Onchain Security Report](https://blockaid.io/h1-report-2026) flagged cross-chain bridges as the single largest source of dollar losses in the first half of the year, with at least seven noteworthy bridge incidents led by [the $292 million KelpDAO exploit](https://blockaid.io/blog/how-a-single-layerzero-dvn-compromise-drained-292m-from-kelpdao). The same class of failure kept landing after the half closed. July and August produced 10 more bridge-verification incidents totaling roughly $24.6 million, with about $2.7 million recovered.

Across Protocol, Wanchain, and Verus took the largest hits, losing roughly $4.5 million to forged deposits, $9.3 million to a reused signature, and $7.54 million to an unbound payout. Each method broke the same underlying check and moved real funds against a source event that never happened. Response speed then separated the outcomes, with Elastos containing nearly all of the stolen funds through fast consensus action while the Verus reserves left through a mixer and were not recovered.

This post breaks down where cross-chain verification fails, what happened in each incident, and why no single audit closes the gap. It then covers the defenses that do, including how Blockaid's [Cosigner](https://blockaid.io/cosigner) acts as an independent signing check, so onchain teams catch a forged payout or a compromised bridge before anything is signed.

## **What Is a Cross-Chain Verification Failure?**

A blockchain can only verify its own state. When a user deposits on Chain A and withdraws on Chain B, the bridge contract on Chain B never sees the deposit itself. It relies on a check to confirm the deposit actually happened before releasing anything. In a cross-chain verification failure, an attacker fools that check, and the bridge pays out real funds for a deposit that never happened.

Depending on the design, the check can be a Merkle or attestation proof, a set of guardian or MPC signatures, an event re-observed by an offchain relayer, a validator-signed withdrawal batch, or a ZK proof. What they all share is that the destination side is trusting a representation of a source event rather than the event itself. If that representation can be forged, replayed, re-encoded, or manufactured from a failed or non-existent source transaction, the attacker controls what the bridge believes.

The attack surface has three recurring forms:

- **Payouts never tied to a real deposit** - The proof or message verifies cryptographically, but the contract never checks that the amount and asset being released match an actual, funded source event.
- **Offchain systems the bridge has to trust** - Relayers, indexers, and re-observation paths are part of the trust boundary. If they accept an event that did not really succeed, or one emitted by the wrong contract, the honest signers downstream turn a fraudulent message into a "valid" one.
- **Encoding, parsing, and registry ambiguity** - A single valid signature reused for a different meaning, two layers parsing the same payload differently, or a poisoned asset registry all let attacker-supplied data pass checks that were never designed to be adversarial at that layer.

Because bridges pool large value behind a narrow trust assumption, a single accepted forgery can drain an entire escrow or mint an unbacked supply. Recovery depends on the path the funds take. Logic exploits sometimes end in partial or full recovery through freezes, burns, or whitehat negotiation, while funds that reach mixers quickly are usually gone.

## **The Three Largest Recent Losses**

### 1. Across Protocol: Forged Deposits (\~$4.5M, July 17)

Across's relayer infrastructure accepted deposit-like data reconstructed from a failed Solana transaction without adequately verifying that the source transaction had succeeded and produced real state changes. Using a custom Solana program and fabricated deposit IDs against the SVM SpokePool, the attacker triggered relayer-funded destination fills for deposits that never really happened, and the relayer filled 581 of 1,627 forged deposits.

Genuine transfers completed or were refunded the same day, and the loss fell on relayer capital (Risk Labs), with roughly $500K trapped in-protocol and net public loss under $4 million. The attacker routed Solana-origin proceeds through CCTP. The failure sat in the offchain re-observation path feeding the bridge rather than in any onchain contract.

### 2. Wanchain: Reused Signature (\~$9.3M, July 20)

About 515.2 million NIGHT was unlocked from Wanchain's Cardano TreasuryCheck through non-injective encoding of adjacent amount fields. Per Wanchain's post-mortem, the bridge's MPC had legitimately signed a small BNB-to-Cardano withdrawal. The attacker redrew the byte boundary between the NIGHT and ADA amount fields and reused that same valid signature to authorize a far larger Cardano unlock.

The Midnight network itself was unaffected, with the compromise confined to the bridge layer. The broader lesson is that when two components can parse the same signed payload differently, one honest signature can carry two meanings, and the attacker picks which one executes.

### 3. Verus: Unbound Payout (\~$7.54M, July 23)

The attacker called the Verus Ethereum bridge's import and payout path (submitImports) and drained its reserves of ETH, tBTC, USDC, USDT, EURC, MKR, and scrvUSD to a fresh, Tornado-funded wallet. The contract failed to validate that input amounts on the source chain matched payouts on Ethereum, the same bug class behind the May 17 drain of this bridge for about $11.58 million.

The two Verus incidents also show how much response mechanics decide the final number. The May drain ended with roughly $8.5 million recovered through the deployer's emergency path. This round, the attacker moved the funds into Tornado Cash, and nothing came back.

Elastos supplied the opposite outcome from the same class of failure. Hit on July 13 for about $2.21 million via a signature and Arbiter validation bypass on cross-chain reserve spends, the network froze, contained, or burned roughly 99.96% of the funds with fast mainchain and sidechain consensus action. The difference between the Elastos and Verus outcomes came down to containment speed.

The other July and August incidents were smaller and fell into the same class the H1 report documented, driven by logic, proof, signature, offchain re-observation, or ZK-circuit flaws.

## **Why These Attacks Keep Working**

The conditions behind these incidents are structural, and anyone whose value crosses a bridge inherits them:

- **A verified message can describe a deposit that never existed** - Proof and signature checks certify the message itself. Verus's payout path passed those checks twice and still released reserves against source events with no funded deposit behind them.
- **Off-chain infrastructure sits inside the trust boundary** - Relayers, indexers, and re-observation paths can turn a failed or fabricated event into a signed message the rest of the system accepts, as they did at Across in July and at Alephium in H1. A poisoned input defeats every honest component downstream.
- **Encoding ambiguity turns one signature into two authorizations** - Wanchain's MPC signed a small withdrawal, and the redrawn byte boundary let the attacker replay that signature as approval for a far larger unlock.
- **Single-trust designs concentrate failure** - A single verifier or a threshold-of-one is catastrophic whether the failure is a logic bug or a key theft, because no independent check remains to disagree.
- **Audits pass and the system still breaks** - Most of these incidents passed their audits, because the failure lives in the trust boundary between components, in an off-chain relayer, a signature-encoding ambiguity, or an import path, where a single-contract review does not reach.
- **Recovery is a race the defender usually loses** - When the forged event surfaces as a real transaction on a covered chain, it is visible and screenable in real time, and the Verus payout was flagged within roughly 11 minutes. Once funds reach a mixer, recovery is effectively off the table, which pushes the entire problem upstream toward stopping the payout before signature.

None of these conditions resolves on its own, and the countermeasures are well understood.

## **How to Prevent Cross-Chain Verification Failures**

Based on the pattern across these incidents, Blockaid recommends treating the bridge trust boundary as critical infrastructure and defending it in layers:

- **Bind every destination payout to observable source-chain state** - Confirm the released amount and asset match a real, funded deposit before anything moves, since a cryptographically valid proof does not establish this on its own. This was the most repeated root cause across the wave.
- **Treat off-chain relayers and indexers as in-scope** - They must verify that the source event actually succeeded and came from the legitimate contract before feeding signers.
- **Assume single-trust designs will fail** - Require multi-party trust so that no single verifier, signer, or component can authorize an outflow alone.
- **Screen every outflow before it is signed** - A forged source event still has to produce a destination-side transaction. If that transaction is checked against policy before a signature is issued, the forgery becomes a blocked or held request instead of a loss.

The first three defenses sit with the teams that build and operate bridges. The last one covers everyone a bridge serves, from the blockchain networks standing behind canonical bridges to the issuance providers, DeFi protocols, and institutions whose assets depend on them, because every cross-chain outflow ends at a signature.

## **How Blockaid's Cosigner Blocks Forged Payouts Before They Execute**

Correct trust-boundary design closes most of the distance, but eventually a destination-side transaction has to be signed. Most protocols and institutions route privileged operations, including escrow releases, mints, and treasury movements, through a multisig or MPC signing setup, and that signing layer is where the last line of defense sits.

[Cosigner](https://blockaid.io/cosigner) is Blockaid's zero-trust transaction security and policy enforcement tool that integrates directly into that multisig or MPC workflow, joining either as a required signer or in read-only mode. Before anything is signed, it simulates the full transaction call object against the real-time state of the chain, surfacing every function call and validating the integrity of every state change, so the signing decision rests on what the transaction will actually do rather than on a frontend, a proposal description, or an upstream message.

Its behavior-based policy engine then checks the simulated outcome against the organization's own rules, applying transaction size limits, disallowed functions, variable change rules, and pre/post state differences alongside recipient checks. A payout that does not correspond to a real, funded source event fails those checks, and Cosigner withholds its signature.

Over the last 90 days, Cosigner screened roughly 22,000 signing requests across more than 45 organizations and around 100 live cosigners, spanning Ethereum, Base, Arbitrum, BSC, Polygon, Avalanche, Optimism, and Solana. It simulated and policy-checked every request before signing, and held for human review any transaction that reverted or touched a flagged participant.

[Learn more about Blockaid's Cosigner →](https://blockaid.io/cosigner)

## **Conclusion**

Across, Wanchain, Verus, and Elastos landed within a five-week window, and each fit the pattern the H1 report documented. The destination side accepted a fabricated or reinterpreted source event and paid out real reserves against it, and the speed of response, more than the exploit itself, set each final loss.

The attack surface persists because it sits between components rather than inside any one contract, where no single audit reaches. The durable defense is to tie every destination payout to a real, funded source event and to screen the resulting transaction against policy ahead of signing.

Blockaid's [Cosigner](https://blockaid.io/cosigner) provides that second layer, validating in real time what every privileged action will actually do before it is signed, so an exploit in this class ends as a rejected request rather than a drained escrow. For the bridges and institutions holding escrows like the ones drained this summer, that protection can be in place before the next forged message arrives.

### **About Blockaid**

Blockaid is the onchain security platform trusted by the largest companies operating in Web3. Built by veterans of elite intelligence and cybersecurity units, Blockaid provides end-to-end protection for financial institutions, protocols, and end users, combining direct wallet and dApp integrations with real-time monitoring, detection, and response across smart contracts, infrastructure, and externally owned accounts. Since 2025, Blockaid scanned over 6.3 billion transactions and blocked 585 million attacks. Blockaid is the security infrastructure behind Coinbase, MetaMask, Uniswap, Safe, and dozens of the most widely used platforms in the industry.

Learn more at [Blockaid.io](https://blockaid.io/), and follow us on [Twitter](https://x.com/blockaid_) and [LinkedIn](https://www.linkedin.com/company/blockaid).

## Blockaid is securing the biggest companies operating onchain

Get in touch to learn how Blockaid helps teams secure their infrastructure, operations, and users.
