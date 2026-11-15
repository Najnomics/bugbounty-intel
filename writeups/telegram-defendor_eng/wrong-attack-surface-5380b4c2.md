# 🎯 Rekt: The Wrong Attack Surface

- **Source URL:** https://rekt.news/wrong-attack-surface
- **Fetched:** 2026-11-15
- **Channel:** @defendor_eng
- **Telegram message:** https://t.me/defendor_eng/1921 (id 1921)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Wrong Attack Surface

*"A protocol can pass a flawless code audit and still lose millions because of a compromised admin key." - [Ronghui Gu, CertiK](https://www.forbes.com/sites/boazsobrado/2026/07/17/fewer-but-far-more-surgical-crypto-hacks-hit-13-billion-in-2026/)*

[It took 128 seconds to drain $285 million from Solana's largest perpetuals exchange](https://rekt.news/drift-protocol-rekt) on April Fool's Day.

Drift Protocol's control plane was the target, not its code. [Privileged key management was compromised](https://rekt.news/drift-protocol-rekt), and the money moved out through a transaction that looked, from the outside, like an authorized action.

**Seventeen days later, [a different protocol named KelpDAO was exploited on a different chain and lost $290 million through a different mechanism](https://rekt.news/kelpdao-rekt), and the result was exactly the same:** The system held, the money left.

**Two of the year's biggest heists. Two audits that were technically correct.**

*So what, exactly, did those audits protect - the code, or the illusion that code was the whole attack surface?*

*Credit:[Forbes](https://www.forbes.com/sites/boazsobrado/2026/07/17/fewer-but-far-more-surgical-crypto-hacks-hit-13-billion-in-2026/), [CredShields](https://discover.credshields.com/drift-protocol-incident-post-mortem/), [Chainalysis](https://www.chainalysis.com/blog/lessons-from-the-drift-hack/), [Neodyme](https://cdn.prod.website-files.com/6310e7dee49f0866da8eed4c/6686bbdfe7c6e5a997cc51bc_Neodyme%20-%20Drift%20Security%20Audit.pdf), [Elliptic](https://www.elliptic.co/insights/drift-protocol-exploited-for-286-million-in-suspected-dprk-linked-attack/), [LayerZero](https://layerzero.network/blog/layerzero-labs-kelpdao-incident-report), [decrypt](https://decrypt.co/364872/layerzero-pins-292m-kelpdao-bridge-hack-on-north-koreas-lazarus-group), [KelpDAO](https://x.com/KelpDAO/status/2051754226351771772), [The Defiant](https://thedefiant.io/news/blockchains/arbitrum-security-council-freezes-eth-linked-to-kelpdao-exploit), [samczsun](https://x.com/samczsun/status/2046455983082267096?s=20), [TRM Labs](https://www.trmlabs.com/resources/blog/h1-2026-crypto-hacks-reach-record-high-as-losses-fall-below-usd-1-billion), [Immunefi](https://docs.immunefi.foundation/june-2026-immunefi-ecosystem-update/), [Blockaid](https://x.com/blockaid_/status/2082127793916145944), [CertiK](https://www.certik.com/skynet-report/certik-hack3d-h1-2026-report), [SlowMist](https://slowmist.medium.com/slowmist-2026-mid-year-blockchain-security-and-aml-report-75e0862179ef), [QuillAudits](https://medium.com/coinmonks/quill-ledger-h1-2026-defi-security-report-5d9a50ccb851), [ack3](https://ack3.ai/research/defi-hacks-h1-2026/), [US Department of Treasury](https://home.treasury.gov/news/press-releases/sb0416), [Forbes](https://www.forbes.com/sites/boazsobrado/2026/07/17/fewer-but-far-more-surgical-crypto-hacks-hit-13-billion-in-2026/), [Groundhog Day](https://www.imdb.com/title/tt0107048/)*

**Drift and KelpDAO weren't just the year's two biggest losses.**

Together they became the clearest test of the thesis: when the failure sits outside the code, who was actually supposed to catch it?

Nobody involved agreed, and the two teams that lived through it had very different answers.

Drift's attackers didn't rush. [The operation appears to have started at a conference in the fall of 2025](https://rekt.news/drift-protocol-rekt), when a handful of people introduced themselves as a quantitative trading firm looking to integrate with the protocol.

[Contributors met them again in other cities, other countries](https://rekt.news/drift-protocol-rekt), over the following months.

**Trust built exactly the way it's supposed to build in this industry, in person, over time, through the ordinary motions of doing business with someone.**

By April 1, that trust paid off. [The attackers used a durable nonce](https://rekt.news/drift-protocol-rekt), a legitimate Solana feature, [to get pre-signed authority from Drift's Security Council](https://discover.credshields.com/drift-protocol-incident-post-mortem/), authority that should have required more than a signature to hand over.

Once inside, [they whitelisted a worthless token called CVT, deposited 500 million of it as collateral](https://www.chainalysis.com/blog/lessons-from-the-drift-hack/), and walked out with $285 million in USDC, SOL, and ETH.

**[Neodyme's 2024 audit flagged one issue that turned out to matter](https://cdn.prod.website-files.com/6310e7dee49f0866da8eed4c/6686bbdfe7c6e5a997cc51bc_Neodyme%20-%20Drift%20Security%20Audit.pdf):** Admin instructions like InitializeSpotMarket accept an oracle account with zero validation. The report rated it informational, reasoning that only the admin could call it, so the impact was limited.

*Roughly two years later, [that's the exact door the attackers walked through](https://rekt.news/drift-protocol-rekt). Once they held the compromised admin key, [they created a new collateral market for CVT, their fake token, pointed at an oracle they had built and controlled themselves for three weeks in advance](https://rekt.news/drift-protocol-rekt).*

[The audit had already named the mechanism](https://cdn.prod.website-files.com/6310e7dee49f0866da8eed4c/6686bbdfe7c6e5a997cc51bc_Neodyme%20-%20Drift%20Security%20Audit.pdf). It just assumed the key holding it would stay trustworthy.

[The same 128-second window also saw the attackers raise withdrawal caps to 500 trillion across five markets](https://rekt.news/drift-protocol-rekt), through an admin-only update instruction the report never itemized individually.

Investigators later linked the Drift attack, [with medium-high confidence, to UNC4736](https://www.elliptic.co/blog/drift-protocol-exploited-for-286-million-in-suspected-dprk-linked-attack), aka TraderTraitor, the same North Korea-linked group [behind 2024's Radiant Capital hack](https://www.elliptic.co/blog/drift-protocol-exploited-for-286-million-in-suspected-dprk-linked-attack).

[KelpDAO's turn came 17 days later](https://rekt.news/kelpdao-rekt), and the setup looked nothing like Drift's. No conference, no fake trading desk.

[Someone social-engineered a LayerZero Labs developer on March 6, lifted their session keys](https://layerzero.network/blog/layerzero-labs-kelpdao-incident-report), and used that access to poison the RPC infrastructure feeding LayerZero's verifier network.

**External nodes got DDoS'd into silence, [leaving only the compromised ones to answer](https://layerzero.network/blog/layerzero-labs-kelpdao-incident-report).**

When a forged cross-chain message needed a signature, [the compromised verifier gave it one](https://medium.com/coinmonks/quill-ledger-h1-2026-defi-security-report-5d9a50ccb851).

[The bridge minted 116,500 unbacked rsETH](https://rekt.news/kelpdao-rekt), about $290 million, and nothing upstream had reason to question it.

[Mandiant, CrowdStrike, and LayerZero jointly attributed the attack to TraderTraitor](https://layerzero.network/blog/layerzero-labs-kelpdao-incident-report), the Lazarus subgroup [also tied to the Ronin Bridge and WazirX hacks](https://decrypt.co/364872/layerzero-pins-292m-kelpdao-bridge-hack-on-north-koreas-lazarus-group).

**Different chains. Different entry points. Same outcome twice:** The system did exactly what it was built to do, and the money left anyway.

**[CredShields put it plainly in their Drift post-mortem](https://discover.credshields.com/drift-protocol-incident-post-mortem/):** The attack surface has moved "up the stack to governance, to signers, and to the people building the protocols themselves."

**Two firms had confirmed the code was fine. Neither had asked who was allowed to sign for it.**

*If the auditors did their jobs and the money still walked out the door, whose job was it to stop this?*

### The Blame Game

[LayerZero published its post-mortem first](https://layerzero.network/blog/layerzero-labs-kelpdao-incident-report), and it didn't flatter the protocol built on it.

[The report said KelpDAO had ignored repeated recommendations to run a multi-verifier setup, choosing instead a single DVN, LayerZero Labs' own, as the sole signer](https://layerzero.network/blog/kelpdao-incident-statement) on a bridge securing hundreds of millions of dollars.

**KelpDAO didn't accept that framing for a day. [The rebuttal came with receipts](https://x.com/KelpDAO/status/2051754226351771772):** Dune data showing that 47% of all LayerZero OApp contracts, more than 1,200 of them, run the exact same single-verifier configuration LayerZero was now calling reckless.

**[Screenshots followed](https://x.com/KelpDAO/status/2051754226351771772):** Over two and a half years and eight documented integration conversations, Kelp says LayerZero reviewed its configuration each time and raised no objections.

**[Kelp put it bluntly, early in its rebuttal](https://x.com/KelpDAO/status/2051754226351771772):** "LayerZero blamed their users for an issue that was caused by their own infrastructure failure."

[LayerZero co-founder Bryan Pellegrino pushed back hours later](https://x.com/PrimordialAA/status/2051781730168905984), disputing Kelp’s account with on-chain records. He said Kelp originally used LayerZero’s defaults, which were MultiDVN or DeadDVN, and later manually migrated to a 1/1 configuration.

**Take that with the obvious caveat:** It's coming from the infrastructure provider being blamed.

**3 days after that, [LayerZero reversed course entirely](https://layerzero.network/blog/an-overdue-apology):** “We made a mistake by allowing our DVN to act as a 1/1 DVN for high-value transactions,” the company wrote. “We didn’t police what our DVN was securing, which created a risk we simply didn’t see. We own that.”

The same company that had spent weeks pointing at Kelp's configuration chose to take the blame instead.

**The technical argument never fully closed, though.**

[LayerZero’s own forensic report, published weeks later with Mandiant, CrowdStrike, and zeroShadow](https://layerzero.network/publications/kelpdao-incident-report.pdf), said the rsETH bridge had been downgraded from a 2-of-2 configuration to a 1-of-1 before the attack.

[The report said the impact was made possible by the affected OApp’s single-verifier configuration](https://layerzero.network/publications/kelpdao-incident-report.pdf) and added that LayerZero’s DVN would no longer sign as the sole required attestor on any channel.

Three days after the exploit, something rarer happened. [The Arbitrum Security Council froze roughly 30,766 ETH](https://thedefiant.io/news/blockchains/arbitrum-security-council-freezes-eth-linked-to-kelpdao-exploit), about $71 million, tied to the stolen funds, acting on identifying information law enforcement had supplied.

[SEAL founder samczsun called it a huge day for victims of the Kelp DAO hack, saying he hoped](https://x.com/samczsun/status/2046455983082267096?s=20) “that we can look back on today as the day our industry realized that we can simultaneously build useful products while also protecting users rather than be a consequence-free infinite money glitch for hackers.”

That's the exception, not the pattern. Most of the money moved before anyone with the power to freeze it agreed on who should have stopped it.

**Two teams, two audits, two post-mortems, and neither one answers the question that actually mattered going into the exploit.**

*Who was responsible for the part nobody thought to audit?*

### A Moving Target

*Ask five security firms how bad the first half of 2026 was, and you get five different answers.*

**Security firms don't all track the same thing, and that's not a strike against any of them.**

Some scope to verified on-chain exploits only. Others count rug pulls and smaller token-level incidents, or narrow the field to DeFi specifically.

Every one of these teams does careful work, they're just building different rulers.

Run the numbers across the major trackers this half.

[TRM Labs counted 207 hacks](https://www.trmlabs.com/resources/blog/h1-2026-crypto-hacks-reach-record-high-as-losses-fall-below-usd-1-billion), $972 million.

[Immunefi's own June Ecosystem Update repeats that same $972 million figure](https://docs.immunefi.foundation/june-2026-immunefi-ecosystem-update/), attributing it directly to TRM Labs rather than reporting an independently tallied total, which illustrates that apparent agreement can sometimes reflect shared sourcing rather than independent tallies.

[Blockaid counted 212 incidents](https://x.com/blockaid_/status/2082127793916145944), $1.1 billion.

[CertiK's Hack3D put it at 344 incidents](https://www.certik.com/skynet-report/certik-hack3d-h1-2026-report), $1.315 billion.

[SlowMist logged 182 incidents](https://slowmist.medium.com/slowmist-2026-mid-year-blockchain-security-and-aml-report-75e0862179ef), $956 million.

[QuillAudits](https://medium.com/coinmonks/quill-ledger-h1-2026-defi-security-report-5d9a50ccb851), working from a narrower DeFi-only dataset, [found 87 incidents, $935.3 million](https://medium.com/coinmonks/quill-ledger-h1-2026-defi-security-report-5d9a50ccb851). They also highlighted there was an average of one hack every two days.

**Across those six trackers, incident counts span from 87 to 344, and total losses range from $935.3 million to $1.315 billion.**

Averaged out, that points to roughly 206 incidents and just over a billion dollars stolen, a rough center of gravity for the half, even if no two firms agree on the exact figure.

**[One number holds regardless of who's counting](https://www.trmlabs.com/resources/blog/h1-2026-crypto-hacks-reach-record-high-as-losses-fall-below-usd-1-billion):** The incident count is the highest ever recorded for a six-month period, according to TRM Labs.

Losses look lower than 2025 only because 2025 had a single [$1.5 billion outlier, the Bybit hack](https://www.certik.com/skynet-report/certik-hack3d-h1-2026-report), and 2026 didn't repeat it.

**[CertiK's own analysis makes that point directly](https://www.certik.com/skynet-report/certik-hack3d-h1-2026-report):** Strip Bybit out of the 2025 baseline, and its 2026 figures come in roughly 28% higher, not lower.

[The median hack cost about $219,000](https://www.trmlabs.com/resources/blog/h1-2026-crypto-hacks-reach-record-high-as-losses-fall-below-usd-1-billion), the midpoint if you ranked every H1 2026 incident by size.

[The mean](https://www.trmlabs.com/resources/blog/h1-2026-crypto-hacks-reach-record-high-as-losses-fall-below-usd-1-billion), the total divided evenly across every incident, [came to $4.7 million](https://www.trmlabs.com/resources/blog/h1-2026-crypto-hacks-reach-record-high-as-losses-fall-below-usd-1-billion), twenty times higher.

**That gap is the whole industry in one statistic:** Thousands of small, forgettable exploits pulling the median down, and a handful of nine-figure operations pulling the mean somewhere the typical incident never goes.

That split isn't just a quirk of the math. It's proof that frequency and severity are two separate problems wearing the same headline number.

*Zoom into DeFi specifically, and the picture shifts again, in a different direction.*

[ack3's evidence-graded incident ledger](https://ack3.ai/research/defi-hacks-h1-2026/), built specifically to track audit coverage rather than headline totals, [counted 135 verified incidents in H1 2026 worth $939.86 million](https://ack3.ai/research/defi-hacks-h1-2026/).

Of those, [68 had an audited party involved, 46 sat entirely outside any audit's scope, and 20 were in-scope misses](https://ack3.ai/research/defi-hacks-h1-2026/), incidents the relevant audit should have caught and didn't.

**Their ledger also caught something this piece hadn't touched yet:** Supply-chain compromise, sitting at three different scales across the half.

[Holdstation lost $462,000](https://ack3.ai/research/defi-hacks-h1-2026/) after a stolen developer session token let an attacker inject malicious code into an app update.

[Resolv Labs lost $24.5 million](https://ack3.ai/research/defi-hacks-h1-2026/) after a compromised signing key traced back to a software supply-chain breach.

[Polymarket's front end lost $3.1 million](https://ack3.ai/research/defi-hacks-h1-2026/) after a third-party vendor's script was compromised.

Different sizes, same root cause, and none of it a line of exploited contract code.

Even the question of what counts as audited turns out to be nearly as contested as the question of what counts as a hack.

**None of that is a knock on the people doing the counting. This year has genuinely been a rollercoaster, and a hard one to measure.**

*But if the industry's best trackers still can't settle on the shape of what already happened, what confidence should anyone have in spotting what's coming next?*

### No Bug Required

*The easiest wins in this entire dataset were never the smart contracts.*

**They were the people who work on them, the vendors they trust, and the keys nobody made hard enough to steal.**

Opsec, supply chain, identity, all of it is low-hanging fruit, whether the target is a person or the system they log into every day.

North Korea is just the sharpest, most concentrated version of that same pattern.

One answer to that doesn't depend on whose spreadsheet you trust.

**North Korea-linked actors were responsible for most of the loss total in H1 2026. [TRM Labs puts that figure at roughly 66%, about $643 million](https://www.trmlabs.com/resources/blog/h1-2026-crypto-hacks-reach-record-high-as-losses-fall-below-usd-1-billion).**

**[Blockaid's number is lower but points in the same direction](https://blockaid.io/h1-report-2026):** 55%, about $609 million, traced to a single DPRK cluster. Different tallies, same concentration of losses.

Hacks and exploits are only part of that revenue stream.

[TRM has also tied North Korea to covert IT worker placements](https://www.trmlabs.com/resources/blog/h1-2026-crypto-hacks-reach-record-high-as-losses-fall-below-usd-1-billion), phishing, and fraud that never touch a smart contract at all.

In March, [the US Department of Treasury sanctioned six individuals and two entities tied to one such scheme](https://home.treasury.gov/news/press-releases/sb0416), operatives placed inside crypto and tech firms using stolen identities, [laundering an estimated $800 million in 2024 alone](https://home.treasury.gov/news/press-releases/sb0416).

**It's similar to the broader infiltration pattern seen before Drift, built on patience and a fabricated professional identity rather than a single technical exploit.**

**[Sodot co-founder and CEO, Ido Sofer](https://x.com/sofer_ido), who builds key management infrastructure for a living, [put it plainly on the On The Margin podcast](https://www.forbes.com/sites/boazsobrado/2026/07/17/fewer-but-far-more-surgical-crypto-hacks-hit-13-billion-in-2026/):** "There will be hacks. The question is, is it going to be in your company or not. North Korea, they spend a significant amount of resources, and they're going to be successful one way or another. If a nation state is after you, it's going to be very hard."

What's realistic is raising the cost.

"You think about attackers. They're organizations," [Sofer said](https://www.forbes.com/sites/boazsobrado/2026/07/17/fewer-but-far-more-surgical-crypto-hacks-hit-13-billion-in-2026/). "They calculate the ROI. If you put enough constraints and enough security rails, the cost is going to be higher than my neighbor and the other company, so probably they're going to go there because the ROI is lower."

**None of that requires a smart contract bug. It requires months of patience and a convincing cover story.**

That's the wrong attack surface working exactly as intended, long before anyone signs anything.

It's been a long time since Rekt News had to flag an audit as in scope for one of these bigger exploits.

**Those are the memorable ones, since they mean contacting auditors with actual questions. It's been a while and they are great at providing receipts.**

*So when a state actor doesn't need to write a single line of exploit code to get in, what exactly is a security audit defending against?*

*The vault held. The money still walked out the front door.*

**Pete and Repeat walk into a store, Pete walks out and who is left?**

Repeat.

2026, and stretching back into 2025, these operational failures have been stuck on repeat.

Feels like we are living through the defi version of the [movie Groundhog Day](https://www.imdb.com/title/tt0107048/).

*Drift and KelpDAO had passed the audits that covered their code and integration paths, and [together they still lost $577 million to attacks that never touched a line of code](https://www.trmlabs.com/resources/blog/h1-2026-crypto-hacks-reach-record-high-as-losses-fall-below-usd-1-billion). LayerZero and KelpDAO couldn't agree on whose job it was to prevent it.*

**Five different security firms couldn't even agree on how big the damage was in the first place.**

The numbers disagree because the methods disagree, but the signal doesn't.

[TRM called it two distinct](https://www.trmlabs.com/resources/blog/h1-2026-crypto-hacks-reach-record-high-as-losses-fall-below-usd-1-billion) threat patterns.

[Ronghui Gu, CertiK's co-founder, called it the shape](https://www.forbes.com/sites/boazsobrado/2026/07/17/fewer-but-far-more-surgical-crypto-hacks-hit-13-billion-in-2026/) of the losses.

**Either way:** More attacks, and more of the damage concentrated in a handful of nine-figure operations, and more of it happening outside the contract entirely.

**Underneath all of it sat one threat actor who didn't need any of those disputes settled to keep winning:** Patient enough to spend six months building a relationship before it ever needed a keyboard.

Audits reduce code risk. They don't cover the keys, the signers, or the trust assumptions built around the code, and that's where the money left.

Multi-party computation, multi-verifier bridges, and withdrawal delays are all being proposed as fixes, and each one helps.

**None of them stop a six-month friendship built one meeting at a time.**

*When the wall is reinforced and the door is watched and the money still walks out through the person holding the key, what exactly was being protected?*

REKT serves as a public platform for anonymous authors, we take no responsibility for the views or content hosted on REKT.

**donate (ETH / ERC20): [0x3C5c2F4bCeC51a36494682f91Dbc6cA7c63B514C](https://etherscan.io/address/0x3C5c2F4bCeC51a36494682f91Dbc6cA7c63B514C)**

disclaimer:

REKT is not responsible or liable in any manner for any Content posted on our Website or in connection with our Services, whether posted or caused by ANON Author of our Website, or by REKT. Although we provide rules for Anon Author conduct and postings, we do not control and are not responsible for what Anon Author post, transmit or share on our Website or Services, and are not responsible for any offensive, inappropriate, obscene, unlawful or otherwise objectionable content you may encounter on our Website or Services. REKT is not responsible for the conduct, whether online or offline, of any user of our Website or Services.
