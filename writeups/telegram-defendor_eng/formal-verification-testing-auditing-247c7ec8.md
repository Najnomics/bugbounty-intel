# 🔍 Certora: Audits, Fuzzing and Formal Verification Each Miss Different Bugs

- **Source URL:** https://www.certora.com/blog/formal-verification-testing-auditing
- **Fetched:** 2026-11-14
- **Channel:** @defendor_eng
- **Telegram message:** https://t.me/defendor_eng/2170 (id 2170)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
[← Blog](https://www.certora.com/blog)

# Formal Verification vs. Testing vs. Auditing: What Each One Catches

What each security method catches, where its guarantees stop, and how they work together across a protocol’s lifecycle.

Author:

[Nisarg Patel](https://www.certora.com/author/nisarg)

Formal verification, testing, and smart contract auditing are often treated as interchangeable steps toward the same goal of making sure code works. In practice, each one asks a different question about a protocol's risk, and treating them as substitutes can be expensive. *[What Is Formal Verification?](https://www.certora.com/blog/what-is-formal-verification)* covered what formal verification proves and how an engagement works. This article compares the three approaches directly: where each one's guarantee stops, and what a business leader should take from that when deciding how a protocol is secured.

CoinGecko's [2026 State of Crypto Security Report](https://www.coingecko.com/research/publications/state-of-crypto-security-report-2026) counted 245 security incidents between January 2025 and July 2026, with $3.63 billion lost. Of those, 147 hit platforms that had already been audited, and those platforms accounted for 88 percent of the money stolen. Most of those attacks went after components outside a standard smart contract audit, code added after the audit, or governance features working as designed. The rest still cost $396 million: just under 11 percent of the audited platforms were hit through flaws inside code the audit had reviewed.

Furthermore, a [2025 study](https://arxiv.org/abs/2507.20175) of 50 major smart contract attacks found that only 14 came down to an isolated coding error. The rest traced to flawed economic design, failed upgrades and governance, or unsafe trust in outside data. Testing and formal verification stop at boundaries of their own, and a protocol is exposed wherever none of the three methods reaches.

## How Smart Contract Audits, Fuzzing, and Formal Verification Differ

A smart contract **audit** asks whether the code, and the design behind it, holds up under expert scrutiny. Experienced reviewers read the code within a fixed scope and a fixed amount of time, looking for mistakes and for weaknesses in how the system is meant to work. Their strength is judgment and context. An auditor can ask whether a mechanism is a good idea at all, which is a question no automated tool is built to answer.

**Testing** asks whether the code behaves correctly on the inputs someone ran. A test feeds the code specific values and compares the result with what should happen. Fuzzing automates this by generating huge numbers of inputs, many of them unusual. When a fuzzer is given a property, a precise statement of what the code must always do, the question sharpens: can any of these inputs break the property?

**Formal verification** asks whether a property can fail in any state the model reaches, and either proves that it cannot or produces a counterexample showing how it fails. Our *[What Is Formal Verification?](https://www.certora.com/blog/what-is-formal-verification)* blog explains how this works.

In practice, the boundaries between the three blur. Many smart contract audits include fuzzing, and some include formal verification. Trail of Bits, a well-known audit firm, [says it runs](https://trailofbits.com/services/blockchain/) its fuzzing and analysis tools on every engagement. A formal verification engagement includes expert review in turn, because deciding which properties matter means working out what the protocol must guarantee. Fuzzing and formal verification also share a starting point in stated properties, and what separates them is that a fuzzer samples cases while formal verification covers every state the model reaches.

These are three lenses on the same code, and each one sees something the others miss. A clean result from one method does not answer the questions the other two ask. The rest of this article looks at what each lens makes visible, and where the money is actually lost.

## DeFi Exploit Root Causes and Which Security Method Covers Each

One major area of risk sits outside the code entirely. Attacks on infrastructure target the systems, credentials, and signing keys that control assets. [TRM Labs found](https://www.trmlabs.com/resources/blog/h1-2026-crypto-hacks-reach-record-high-as-losses-fall-below-usd-1-billion) that infrastructure attacks made up about 15 percent of incidents in the first half of 2026 and roughly 76 percent of the money lost. The two largest, at Drift Protocol and KelpDAO, took $577 million between them. An audit, a fuzzing campaign, and a formal verification all examine the code, so none of them covers this area, and operational security and monitoring are the main defense. The rest of this section focuses on attacks that involve the code, where the three methods actually differ.

The [2025 study](https://arxiv.org/abs/2507.20175) mentioned above, by Rezaei and colleagues, maps those attacks. It examined 50 major attacks between April 2022 and April 2025 on blockchains that run Ethereum's execution environment, with about $1 billion lost in total. It sorted each attack into one of four categories by root cause: implementation-level weaknesses (14 incidents), flawed economic design and protocol logic (12), protocol lifecycle and governance failures (12), and external dependency vulnerabilities (12). Only 28 percent of incidents came down to a classic coding mistake. The paragraphs below take each category in turn and look at how much of it each method covers.

## Implementation-Level Weaknesses

Implementation-level weaknesses are coding mistakes, such as a calculation that goes wrong at the extremes or a missing permission check.

All three methods aim at this category, and each catches different things. An audit catches what a reviewer notices, and fuzzing catches what its sampled inputs happen to reach. Formal verification checks every input against the stated properties, within the assumptions the verification makes about the code and its environment. A mistake that breaks a property cannot slip through those checks, while a mistake that no property describes can. The Stake Pool example in [*What Is Formal Verification?*](https://www.certora.com/blog/what-is-formal-verification) showed this in practice. Solana's Stake Pool had been audited nine times, and the bug that let its reserve be drained surfaced while Certora was proving that the pool stays solvent.

P-Token, also on Solana, shows on a single codebase how each method adds findings of its own. P-Token is a more efficient replacement for SPL Token, the program that manages standard tokens on Solana, so it has to behave exactly like the original. According to its developer, in an [interview published by Anza](https://www.anza.xyz/blog/febo-on-pinocchio-p-token-and-pushing-solanas-limits), the team's fuzzing found cases on its first run where P-Token failed at the right step but reported a different error from the original. An audit caught a problem with ownership checks that the other methods had missed. Formal verification surfaced further differences from the original that the fuzzing had not, as Certora's [write-up on P-Token](https://www.certora.com/blog/proving-p-token) describes, so each method contributed something the others did not.

## Flawed Economic Design and Protocol Logic

Flawed economic design and protocol logic covers cases where the code does what it says, but what it says is unsound.

Certora's [work on Suilend](https://www.certora.com/blog/fv-suilend), a lending protocol on the Sui blockchain, gives an example. When a borrower's loan grows too large relative to their collateral, other users can liquidate the position, repaying part of the loan in exchange for some of the collateral at a discount. Liquidation is supposed to make a risky position healthier. Certora found that past a certain point, each liquidation made the position slightly less healthy, so repeated liquidations could leave it insolvent. The flaw came to light through the question behind a property: does liquidation always improve a position? Choosing which properties to prove forces questions like that about the design. A good verification engagement evaluates the design this way and often exposes design flaws before any proof runs, which is where it overlaps most with an audit.

Beyond that review, formal verification can prove economic properties directly, such as "the pool's assets always cover what it owes depositors," within the market behavior the model describes. Fuzzing also reaches this category when it is given a property to check or a profit goal to pursue.

## Protocol Lifecycle and Governance Failures

Protocol lifecycle and governance failures happen when a contract is set up, upgraded, or governed badly.

The study's examples include upgrades or initial setups that left a contract in an unsafe state, misused administrator keys combined with a flaw in the contract, and manipulated governance votes. Formal verification checks the rules written into the code for every case, such as who can upgrade the contract, what delay applies, and whether its state after an upgrade still satisfies its properties.

Certora's [verification of Squads](https://www.certora.com/reports/squads-v4), a shared wallet on Solana, proved properties of this kind, including that only a designated authority can change who approves transactions and how many approvals are needed. The concrete settings chosen at deployment, such as which accounts hold which roles, are often outside formal verification's scope, and tests and audits that examine the deployed contract fill that gap.

## External Dependency Vulnerabilities

External dependency vulnerabilities come from trusting outside data or inputs. In the study, most of these incidents involve inputs the protocol failed to check, and the rest involve manipulated prices. Team Finance, a service that locks up crypto projects' funds, lost about $15 million in 2022. Its function for migrating locked funds accepted inputs it should have rejected and paid out more than the positions were worth. Checking inputs is core audit territory, and formal verification of a property such as "migrating a locked position never pays out more than the position is worth" would have flagged the flaw.

The table below summarizes the coverage each method provides across the four categories. Reading down a column shows where that method's coverage stops.

Every cell in the table carries a condition. An audit covers what reviewers noticed within its scope, fuzzing covers the inputs it sampled, and formal verification covers the stated properties within what the model includes. No category is fully covered by one method, and a clean result is only as broad as the condition behind it.

## What a Clean Smart Contract Audit, Fuzzing Run, or Formal Proof Guarantees

Every security review ends with a result, and a clean one is easy to read as a verdict on the whole protocol. Each method's clean result means something narrower. It matters in two ways: what it says about the code today, and whether it still says anything after the next change.

A **clean audit** means experienced reviewers examined specific code, within a set scope and a set amount of time, and did not find an issue. How much that is worth depends on who looked, for how long, and at what. The reviewers' judgment is the product, which is both the method's strength and the reason its result is hard to check from the outside.

A **clean fuzzing run** means none of the inputs tried broke the stated properties. It speaks only for the inputs the runs actually reached, and when the failing case is rare, reaching it can take a long time. Certora's [white paper](https://www.certora.com/blog/white-paper) describes an issue in the code of Maker, the protocol behind the DAI stablecoin, that took a fuzzer 13 hours and 125 million attempts to find. The [Certora Prover](https://www.certora.com/prover), Certora's formal verification tool, found it in 23 seconds.

A **proof** means the property holds in every state the model reaches, under the stated assumptions. It is as strong as the list of properties and the assumptions behind them, and both are written down. For example, Certora's report on [Aave V4 Hub](https://www.certora.com/reports/aave-v4-fv-hub)  names what it leaves out, starting with the quality of oracle feeds, the services that supply outside data such as prices to a contract. It also excludes economic attacks, blockchain infrastructure risks, and administrator compromise.

That written record also makes proofs and fuzzing runs repeatable. Anyone with the code and the properties can run the same check again and see what the properties establish. Confirming an audit's clean result means repeating the review itself, with new reviewers bringing their own judgment.

## Smart Contract Upgrades and Continuous Formal Verification

A clean result describes the code as it stood on the day it was checked, and protocols keep changing after launch. Fuzzing and formal verification handle that differently from an audit, because their properties stay with the code. Built into continuous integration, the automated system that runs checks every time the code changes, they test each new change against the same properties before it ships. A proof that no longer holds flags the change, and so does any failing input the fuzzer reaches.That makes them a guardrail against future mistakes, as long as the team keeps the properties up to date alongside the code.

An audit's conclusion applies to the code it reviewed. Smart contract auditing firms routinely review later changes, and an audit can leave tests behind, but a change is covered only if that follow-up review happens. Trail of Bits, for example, [hands clients suites of properties](https://trailofbits.com/services/blockchain/) that their teams keep running after the engagement ends. The guardrail comes from the properties, whoever writes them.

Certora has set up continuous integration for a substantial number of clients, checking formal verification properties against their changing code. Aave, a major lending protocol, has [run the Certora Prover this way](https://www.certora.com/blog/formal-verification) since March 2022, with more than 800 checks run on every code addition.

Outside research points the same way. The 2025 study recommends property checks that run on an upgraded contract and block the deployment if they fail, as the first defense against failed upgrades. [CoinGecko's 2026 security report](https://www.coingecko.com/research/publications/state-of-crypto-security-report-2026) traced many attacks on audited platforms to code updates that had never been audited. That is the gap a guardrail is designed to close.

## Combining Smart Contract Audits, Testing, and Formal Verification Across the Protocol Lifecycle

Since each method answers a different question, the practical issue is when each one does its work. Certora performs manual audits alongside formal verification, and several of its reports, including those for Squads, Kamino, and Uniswap v4, combine both. The division of labor below reflects that practice.

During development, unit tests, which check individual pieces of code, and fuzzing against stated properties catch mistakes while the code is being written. Formal verification can begin once the design is stable enough to say what must hold. If the design is still unsettled, the first priority is to settle the requirements, as our *[What Is Formal Verification?](https://www.certora.com/blog/what-is-formal-verification)* article describes.

Before launch, formal verification covers the parts whose requirements can be stated precisely, such as accounting, authorization, core economic properties, and the governance rules written into the code. By the time the proofs run, choosing those properties has already put the design under review. The audit covers what does not reduce to properties or sits outside the verification's scope. That includes the integration with outside systems, deployment settings, unexpected attack paths, and whether the design makes sense beyond what the properties capture. The two can come as separate engagements or as one combined engagement, in whichever order suits the project.

After launch, the properties keep running on every change, and upgrades need a follow-up review of what changed. Monitoring, bug bounties that reward outsiders for reporting flaws, and incident response are the main defense for the risks outside the code, which none of the three methods reach.

Protocols with serious value at stake tend to use all three. Kamino, a lending protocol on Solana, [lists 18 audits](https://kamino.com/docs/security/audits), three formal verifications by Certora, and a [months-long fuzzing campaign](https://cryptobriefing.com/kamino-security-page-solana-4b-protections/) by Ackee Blockchain. Uniswap v4 [combined audits](https://www.certora.com/blog/uniswap-v4-audits-what-we-learned-about-defi-security) from several firms, including OpenZeppelin, Spearbit, Trail of Bits, and Certora, whose review used formal verification, with a public security competition and a bug bounty. Used together over a protocol's life, the three methods are how the table above actually gets filled in.

## Questions to Ask a Smart Contract Security Vendor

A business leader can hold a security program to account without reading any code, by putting these questions to the vendor or the engineering team..

1. For each kind of risk, which method covered it, and which risks did none of them cover? Operations, key management, and trust in outside systems usually fall in the second group, and someone still needs to be responsible for them.
2. What does each clean result actually mean? For an audit, the answer is which code and what scope. For fuzzing and formal verification, it is which properties, and for formal verification, which assumptions.
3. Which checks run automatically on every change, and which changes have had a follow-up review? A clean result from last year says little about code written since, unless something has been checking it along the way.

A report that says "audited," "tested," or "verified" without naming its scope tells a buyer very little.

To put these questions to your own protocol, [request an audit](https://www.certora.com/audits) from Certora, where manual review and formal verification run as one engagement.

--

*The assumptions behind a proof, and what verification looks like on specific blockchains, are topics this series will return to. Follow Certora on [X](https://x.com/Certora?lang=en) and [LinkedIn](https://il.linkedin.com/company/certora) to catch the next article when it's published.*
