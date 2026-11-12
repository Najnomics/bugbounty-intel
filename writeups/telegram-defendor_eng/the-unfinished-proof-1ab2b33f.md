# 🧩 An error in zk-SNARK verification cost the FoomCash protocol $2.26 million

- **Source URL:** https://rekt.news/the-unfinished-proof
- **Fetched:** 2026-11-12
- **Channel:** @defendor_eng
- **Telegram message:** https://t.me/defendor_eng/1305 (id 1305)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# The Unfinished Proof

*$2.26 million. [Gone in a flash of math](https://www.cryptopolitan.com/foom-cash-faces-2-3m-loss-in-exploit/).*

[FoomCash billed itself as](https://www.cryptopolitan.com/foom-cash-faces-2-3m-loss-in-exploit/) a “ZKProof-powered private lottery protocol”, a system where zero-knowledge proofs ensured withdrawals couldn’t be faked.

[The project positioned itself as an upgrade to the sanctioned Tornado Cash mixer](https://www.cryptopolitan.com/foom-cash-faces-2-3m-loss-in-exploit/), touting higher daily transaction volumes, over $8 million in liquidity, and annual returns of 50–80% for liquidity providers.

[One omitted cryptographic step](https://www.quillaudits.com/blog/hack-analysis/foomcash-exploit-explained) erased that promise entirely.

The [Groth16 verifier deployed on both Ethereum and Base](https://www.quillaudits.com/blog/hack-analysis/foomcash-exploit-explained) had set two critical constants - gamma and delta - to the same elliptic curve point, collapsing the entire soundness guarantee of the zk proof system.

No deposit required. No valid witness needed. Just math, iterated by a script, against a verifier that had been broken from day one.

*What followed wasn't a sophisticated attack. It was arithmetic.*

**BlockSec Phalcon flagged it as a copycat of a near-identical exploit on Veil Cash, a smaller Base-network privacy protocol hit just days earlier via the same Groth16 misconfiguration.**

Someone pointed the same technique at a larger target and [walked away with $320K, legitimately, as it turned out](https://x.com/Foomclub_/status/2028231845788188747).

**[Because FoomCash had posted a public bounty challenge on Bitcointalk with one rule](https://bitcointalk.org/index.php?topic=5548104.new#new):** THE ONLY RULE IS CODE.

A separate actor drained the Ethereum side in a claimed rescue, [later confirmed as Decurity](https://x.com/Foomclub_/status/2028231845788188747).

**The team had [been silent since approximately November 2025](https://www.quillaudits.com/blog/hack-analysis/foomcash-exploit-explained) before any of this happened.**

*When your privacy protocol's entire guarantee is 'math can't lie', what happens when the math was always wrong?*

*Credit:[Cryptopolitan](https://www.cryptopolitan.com/foom-cash-faces-2-3m-loss-in-exploit/), [QuillAudits](https://www.quillaudits.com/blog/hack-analysis/foomcash-exploit-explained), [BlockSec Phalcon](https://twitter.com/Phalcon_xyz/status/2026941738141778394), [CoinsBench](https://coinsbench.com/forging-zksnark-proofs-via-misconfigured-verification-keys-the-veil-01-eth-exploit-2a6bb7d0078b), [Foom](https://x.com/Foomclub_/status/2028231845788188747), [Bitcointalk](https://bitcointalk.org/index.php?topic=5548104.new#new), [CertiK](https://twitter.com/CertiKAlert/status/2026935120943526178), [BeosInAlert](https://x.com/beosinalert/status/2026949474065809838), [DK27ss](https://github.com/DK27ss/FoomClub-1.6M-PoC?tab=readme-ov-file), [Tornado Cash](https://docs.tornado.cash/introduction/how-tornado-cash-works), [ZKSecurity](https://blog.zksecurity.xyz/posts/groth16-setup-exploit/), [beac](https://x.com/beacon302/status/2027111035531034915), [EthSecurity Telegram](https://t.me/ETHSecurity/149888), [Elliot](https://x.com/Elliot0x/status/2027073668694917486), [duha](https://x.com/duha_real/status/2028272537864724666)*

[CertiK appears to be the first to diagnose the exploit on February 26th, with the root cause already pinned](https://twitter.com/CertiKAlert/status/2026935120943526178), “We have seen a \~$1.8M exploit/whitehat rescue on FOOMCASH lottery contract. The root cause may be the delta2==gamma2 setting of the Groth16 verifier. This enables the exploiter to compute 'pC' needed for different 'nullifierHash' while all other inputs are the same, and repeatedly collect ZOOM tokens.”

[BlockSec Phalcon’s monitoring system raised the alarm next](https://x.com/Phalcon_xyz/status/2026941738141778394), tagging FOOMCASH on Ethereum and Base as a rerun of the recent Veil Cash verifier bug and pegging losses in the low seven figures.

**[BeosInAlert added more detail shortly after](https://x.com/beosinalert/status/2026949474065809838):** “An exploit/whitehat rescue has been detected on FOOMCASH and it seems to be another potential victim of a misconfigured Groth16 verifier.”

A misconfigured Groth16 verifier. $1.6 million walking out the door, at least that was the first count.

[BlockSec Phalcon’s system flagged it as an imitation attack](https://twitter.com/Phalcon_xyz/status/2026941738141778394), not a novel exploit, not a zero-day, not the work of a sophisticated adversary probing for undiscovered weaknesses.

[An analysis on a nearly identical bug in Veil Cash](https://coinsbench.com/forging-zksnark-proofs-via-misconfigured-verification-keys-the-veil-01-eth-exploit-2a6bb7d0078b), a smaller Base-network privacy protocol, had already laid out the technique.

Veil Cash's legacy pools held \~4.5 ETH. An exploiter drained 2.9 ETH via the same Groth16 misconfiguration. Decurity detected the attack and rescued the remaining pools. The original exploiter subsequently returned the drained funds unprompted. 100% of Veil Cash funds were recovered.

Someone read that post-mortem, identified a larger target, and scaled it up by several orders of magnitude.

The blueprint was already published. FoomCash didn't read it.

The attack unfolded across two chains simultaneously.

*On Base, [a single whitehat transaction sequence drained essentially the entire lottery balance](https://github.com/DK27ss/FoomClub-1.6M-PoC?tab=readme-ov-file), securing roughly the low‑six‑figure share of the $2.26M exploit before any malicious actor could move.*

**On Ethereum, [a separate whitehat operation stripped the mainnet lottery to zero](https://github.com/DK27ss/FoomClub-1.6M-PoC?tab=readme-ov-file), front‑running attackers for the remaining seven‑figure tranche that [Foom later said was 90% recovered and counted toward the $1.84M white‑hat response](https://x.com/Foomclub_/status/2028231845788188747).**

Two wallets, same technique, same broken verifier, same morning.

The protocol's social accounts hadn't posted since [approximately November 2025](https://bitcoinethereumnews.com/finance/upgraded-tornado-cash-foom-cash-faces-almost-2-3m-loss-in-exploit/)

Was anybody even watching?

**By the time security researchers were documenting the mechanics, both chains were empty.**

*If the verifier was broken from deployment, and it was, how long had the door been open before anyone walked through it?*

### The Broken Proof

*FoomCash ran on zero‑knowledge proofs. The entire privacy guarantee depended on them, the standard deposit/proof/redeem model where users prove a withdrawal links to some prior deposit without revealing which one or linking sender to recipient.*

**That’s [the privacy mixer pattern implemented by Tornado Cash](https://docs.tornado.cash/introduction/how-tornado-cash-works), using Groth16 zk‑SNARKs, and the guarantee FoomCash was selling as “a lottery/gambling dApp using ZK proofs (Groth16) for withdrawals” [per FoomCash’s PoC write‑up](https://github.com/DK27ss/FoomClub-1.6M-PoC#summary).**

[The Groth16 verifier is the contract that checks whether a submitted proof is legitimate](https://www.quillaudits.com/blog/hack-analysis/foomcash-exploit-explained), by evaluating a pairing equation that relates the proof elements (A, B, C) to a fixed verification key.

**Two constants in that key are critical:** γ (gamma) and δ (delta), the G2 elements that anchor the two right‑hand pairing terms in the equation, [as detailed in QuillAudits’ analysis](https://www.quillaudits.com/blog/hack-analysis/foomcash-exploit-explained).

In a correct setup, γ and δ must be independent random G2 elements generated during the trusted setup ceremony. That independence underpins soundness by preventing algebraic relations that collapse the pairing equation — [as shown when γ = δ in QuillAudits’ analysis](https://www.quillaudits.com/blog/hack-analysis/foomcash-exploit-explained) and [Foom’s PoC](https://github.com/DK27ss/FoomClub-1.6M-PoC#summary).

*On FoomCash’s deployed verifiers, γ and δ were identical, both set to the BN254 G2 generator, on Ethereum and Base, from day one.*

**A misconfiguration [Foom itself described as “delta == gamma == G2 generator”](https://x.com/Foomclub_/status/2028231849374367860/photo/1) in its technical post‑mortem and reproduced in the public PoC.**

When γ = δ, the verifier’s security check fails completely.

**The math was supposed to verify:** “Does this proof match a real deposit?”

**Instead it checked:** “Does 1 = 1?” → Always “Yes”.

*Attackers exploited this by setting C = −vk\_x (right side cancels to 1), and using public constants A = α, B = β (left side also cancels to 1). [DK27ss’ PoC proves it](https://github.com/DK27ss/FoomClub-1.6M-PoC#why-delta--gamma-breaks-everything): “The verifier accepts the proof without needing a valid witness.”*

**From there, forgery is mechanical. The exploit contract reads α, β, and the IC points from the on‑chain verification key, computes vk\_x from chosen public inputs (root, nullifier, recipient), then sets A = α, B = β, and C = −vk\_x before calling collect(), incrementing the nullifier, and repeating the loop, [exactly as implemented in the PoC’s forgeAndCollect routine](https://github.com/DK27ss/FoomClub-1.6M-PoC#why-delta--gamma-breaks-everything).**

The exploit contracts looped this logic at scale. [On Base, 10 iterations drained 99.97% of the FOOM balance; on Ethereum mainnet, 30 iterations drained 99.99%](https://github.com/DK27ss/FoomClub-1.6M-PoC#output), matching the before‑and‑after lottery balances on both chains.

[QuillAudits confirmed the verifier remained exploitable](https://www.quillaudits.com/blog/hack-analysis/foomcash-exploit-explained): anyone could run their published Foundry cast call against [the live Ethereum verifier contract](https://etherscan.io/address/0xc043865fb4D542E2bc5ed5Ed9A2F0939965671A6), a fabricated proof using only public inputs returns true instead of reverting.

A privacy protocol “secured by math” failed due to one skipped step.

**[Foom’s post‑exploit analysis](https://x.com/Foomclub_/status/2028231849374367860/photo/1) and [ZKSecurity’s analysis](https://blog.zksecurity.xyz/posts/groth16-setup-exploit/) agree:** During snarkjs Phase 2 trusted setup, the CLI command that generates random values for γ and δ from their default G2 generator values was never run.

**Not wrong random values. No randomness at all. Just snarkjs placeholder defaults left untouched.**

*Two constants never meant to match. Who checked?*

### Transparent Captivity

*Two chains drained. Two actors. One broken verifier doing all the work.*

**On Base, a single transaction accounted for $320K in FOOM tokens, attributed to [a white hat named duha](https://x.com/duha_real).**

On Ethereum, $1.84M was [drained by whitehat-rescue.eth](https://etherscan.io/address/0x46c403e3DcAF219D9D4De167cCc4e0dd8E81Eb72), a separate [white hat actor linked to security firm Decurity](https://x.com/Foomclub_/status/2028231845788188747), who independently identified the gamma==delta flaw and executed a claimed rescue.

The FOOM tokens on Base didn’t stay on Base for long.

**They were bridged across to Ethereum through FoomCash’s own official bridge contract:**
[0x2f534ce6843e7a773fd9f2e45d04e8608b9de3f8](https://basescan.org/address/0x2f534ce6843e7a773fd9f2e45d04e8608b9de3f8)

[According to QuillAudits' initial analysis](https://www.quillaudits.com/blog/hack-analysis/foomcash-exploit-explained), published February 27th, before the whitehat resolution was confirmed, the bridged tokens were subsequently converted into WETH, and the Ethereum-side FOOM tokens were swapped for USDT at reportedly discounted prices, with converted funds parked across the identified EOAs.

The full picture changed on March 1st, when [it was revealed that Decurity returned $1.84M to the protocol in a rescue operation](https://x.com/Foomclub_/status/2028231845788188747).

**Decurity returned the rescued funds the same day, [on-chain records confirm the return transaction at 10:11 AM UTC on February 26th](https://etherscan.io/tx/0xfed2dc60634b321fab073312168b327a47fdd76d2a39489249e4ef986671e83f), within hours of the drain. The $100K security fee was offered by the protocol. Decurity made no demands.**

*Victim Contracts are as follows.*

**ETH Lottery Contract:**
[0x239af915abcd0a5dcb8566e863088423831951f8](https://etherscan.io/address/0x239af915abcd0a5dcb8566e863088423831951f8)

**Base Lottery Contract:**
[0xdb203504ba1fea79164af3ceffba88c59ee8aafd](https://basescan.org/address/0xdb203504ba1fea79164af3ceffba88c59ee8aafd)

*Misconfigured Verifier Libraries are as follows.*

**ETH Verifier (the broken contract):**
[0xc043865fb4D542E2bc5ed5Ed9A2F0939965671A6](https://etherscan.io/address/0xc043865fb4D542E2bc5ed5Ed9A2F0939965671A6)

**Base Verifier (identically broken):**
[0x02c30D32A92a3C338bc43b78933D293dED4f68C6](https://basescan.org/address/0x02c30D32A92a3C338bc43b78933D293dED4f68C6)

*Attack Transactions are as follows.*

**Primary ETH Transaction:**
[0xce20448233f5ea6b6d7209cc40b4dc27b65e07728f2cbbfeb29fc0814e275e48](https://etherscan.io/tx/0xce20448233f5ea6b6d7209cc40b4dc27b65e07728f2cbbfeb29fc0814e275e48)

*Secondary ETH Transaction:*\*
[0xa88317a105155b464118431ce1073d272d8b43e87aba528a24b62075e48d929d](https://basescan.org/tx/0xa88317a105155b464118431ce1073d272d8b43e87aba528a24b62075e48d929d)

**Decurity Returned Funds:**

[0xfed2dc60634b321fab073312168b327a47fdd76d2a39489249e4ef986671e83f](https://etherscan.io/tx/0xfed2dc60634b321fab073312168b327a47fdd76d2a39489249e4ef986671e83f)

**Attacker / Whitehat EOAs:**

[0x46c403e3DcAF219D9D4De167cCc4e0dd8E81Eb72](https://etherscan.io/address/0x46c403e3DcAF219D9D4De167cCc4e0dd8E81Eb72) (whitehat-rescue.eth) [0x73f55A95D6959D95B3f3f11dDd268ec502dAB1Ea](https://etherscan.io/address/0x73f55A95D6959D95B3f3f11dDd268ec502dAB1Ea)
[0xa30841846259c02eb540059100b57d87c2384358](https://etherscan.io/address/0xa30841846259c02eb540059100b57d87c2384358)

24,283,773,519,600 FOOM tokens drained in total across both chains.

**A privacy protocol whose funds were never private, held by rescuers waiting to see if the team that built it still had anything left to say.**

*If the code already decided where the money went, why was anyone negotiating the rules after the fact?*

### The Only Rule Is Code

*FoomCash’s social accounts had been dark [since approximately November 2025](https://bitcoinethereumnews.com/finance/upgraded-tornado-cash-foom-cash-faces-almost-2-3m-loss-in-exploit/).*

**No posts. No updates. No acknowledgment that a protocol holding millions of dollars in user funds had anyone at the wheel. Three months of silence before the exploit. And after it? More silence.**

But the story didn’t end with empty contracts.

Before the attack, the FoomCash team had published a [public bounty challenge on Bitcointalk](https://bitcointalk.org/index.php?topic=5548104.new#new).

**[The prize](https://bitcointalk.org/index.php?topic=5548104.new#new):** Approximately $500K in FOOM tokens sitting on the Base network.

**[The terms, in their entirety](https://bitcointalk.org/index.php?topic=5548104.new#new):** “THE ONLY RULE IS CODE. If your code can take the funds, YOU’VE WON.”

*No restitution clause. No disclosure requirement. No deadline. No partial return condition. An unconditional dare, published and verifiable on-chain.*

[duha took them up on it](https://x.com/beacon302/status/2027111035531034915), using the exact vulnerability to drain the Base lottery contract. Legitimately. In scope. On the network specified. With the only rule satisfied.

Then the FoomCash team, apparently rediscovering their voice, demanded 90% back.

**[beacon302, acting as public advocate for duha\_real, didn’t let that stand quietly](https://x.com/beacon302/status/2027111035531034915):** “Foom team is not respecting their own contract. duha\_real is legally within his rights to keep all of the Base network funds. This is a public unilateral commitment. Terms are clear and verifiable on-chain. When you launch a bounty challenge with no restitution conditions, you accept consequences.”

What followed was one of the stranger public disputes the space has produced.

*On February 26th, [duha (using the handle Hao Pham), walked into the EthSecurity Telegram group and publicly defended their position](https://t.me/ETHSecurity/149888), then asked SEAL to get involved as mediator.*

**The person who just drained a protocol was now requesting formal arbitration to protect their right to keep the money.**

**[Security professional Elliot flagged it to the wider community](https://x.com/Elliot0x/status/2027073668694917486):** “You can’t even make the eth security stuff up it’s so absurd.”

[SEAL’s Safe Harbor framework](https://frameworks.securityalliance.org/safe-harbor/overview/) exists precisely to formalize the line between whitehat rescue and exploit.

FoomCash had never adopted it. There was no pre-authorized rescue scope, no legal protection framework, no recovery address. Just a Bitcointalk post and a broken verifier.

beacon302 announced the resolution [at approximately $330K on February 26th](https://x.com/beacon302/status/2027190555881476421).

[FoomCash’s own March 1st would later put the figure at $320K](https://x.com/Foomclub_/status/2028231845788188747). The $10K discrepancy between the two accounts was never publicly explained.

*The FoomCash team made no public statement [until March 1st, when their post put the figure at $320K](https://x.com/Foomclub_/status/2028231845788188747). The $10K discrepancy between the two accounts was never publicly explained.*

[duha\_real keeps the Base bounty](https://x.com/Foomclub_/status/2028231845788188747).

The Ethereum-side funds were resolved in the [same announcement from FoomCash](https://x.com/Foomclub_/status/2028231845788188747).

[FoomCash’s official post confirmed that Decurity](https://x.com/Foomclub_/status/2028231845788188747), the firm behind the whitehat-rescue.eth wallet, returned $1.84M, representing 90% of the Ethereum funds.

**Decurity was paid [a $100K security fee](https://x.com/Foomclub_/status/2028231845788188747).**

**[Total bounty and recovery costs](https://x.com/Foomclub_/status/2028231845788188747):** $420K.

**[Total recovered](https://x.com/Foomclub_/status/2028231845788188747):** $1.84M.

**[Net loss](https://x.com/Foomclub_/status/2028231845788188747):** approximately $420K from a $2.26M event.

*Two actors. Same exploit. Same morning.*

**One kept $320K–$330K by winning a dare. One received $100K for returning what they’d taken.**

That was the version the blockchain recorded. The version the team published looked different.

Then came the rewrite.

[FoomCash’s March 1st post](https://x.com/Foomclub_/status/2028231845788188747) did not describe a protocol that had been drained by a bounty winner and saved by a security firm that returned funds within hours and accepted a bounty the protocol offered. It described as an “[elite white-hat response.](https://x.com/Foomclub_/status/2028231845788188747)”

[It called duha someone who “identified the vulnerability and moved to secure the funds](https://x.com/Foomclub_/status/2028231845788188747) on Base before malicious actors could strike.”

**It called Decurity’s drain of the Ethereum contracts [an “analogous rescue” performed to “front-run malicious actors.”](https://x.com/Foomclub_/status/2028231852981706835)**

[It recast duha, the live bounty hunter exploiting the Base flaw, as the "winner of our Bitcointalk hacking contest held a year ago"](https://x.com/Foomclub_/status/2028231845788188747) who just happened to spot the vulnerability and "secure the funds before malicious actors could strike."

The 90% restitution demand, the public dispute, the EthSecurity Telegram standoff, the beacon302 threads, the days of public pressure, none of it appeared.

**[duha responded in kind](https://x.com/duha_real/status/2028272537864724666):** “By honoring their bug bounty policy, foomclub has proven that they take protocol security seriously and value the researchers helping them.”

For someone who'd just had a public standoff defending their right to keep funds a team was demanding back, it was a notably gracious exit.

The blockchain recorded a different sequence of events. So did Twitter.

**A team that went silent for three months found its voice only to demand 90% back from someone who'd beaten them by their own rules. They folded shortly after security researchers took the fight to Twitter, then four days later published an account in which none of it had happened.**

*Which version do you trust, the one that's immutable, or the one that's convenient?*

*The blueprint was already public.*

[Someone found a public post-mortem about an exploit on a protocol nobody had heard of](https://coinsbench.com/forging-zksnark-proofs-via-misconfigured-verification-keys-the-veil-01-eth-exploit-2a6bb7d0078b), identified a larger target running the same broken verifier, and drained $2.26 million from contracts the team had stopped watching, three months after they’d stopped watching anything at all.

No public audit. No monitoring. No pause function.

[A cryptographic guarantee marketed to users](https://bitcoinethereumnews.com/finance/upgraded-tornado-cash-foom-cash-faces-almost-2-3m-loss-in-exploit/) that had been mathematically void from the moment the contracts were deployed, [not because someone set the wrong value](https://blog.zksecurity.xyz/posts/groth16-setup-exploit/), but because [no one ever ran the CLI step that would have set any value at all](https://x.com/Foomclub_/status/2028231849374367860).

FoomCash was the second victim in the same week. It will not be the last.

*In the aftermath, [ZKSecurity and Dedaub scanned known EVM chains](https://blog.zksecurity.xyz/posts/groth16-setup-exploit/) for other active contracts carrying the same flaw.*

**None of the relevant [Groth16 verifiers with δ = γ had significant recent activity or value locked](https://blog.zksecurity.xyz/posts/groth16-setup-exploit/).**

But [the GitHub search turned up repositories still carrying the pattern](https://blog.zksecurity.xyz/posts/groth16-setup-exploit/), including [a Tornado Cash rebuild with 248 stars](https://github.com/nkrishang/tornado-cash-rebuilt/blob/9dac30e9104c8a8cc00ca24d309fb85d9c74e947/src/Verifier.sol#L37).

The known blast radius may be contained for now. The unknown one is harder to measure.

When the setup ships with its defaults still in place, the certainty was never more than a placeholder.

**And a protocol that can reframe a public standoff as a coordinated rescue operation has found a different kind of zero-knowledge proof, one that proves nothing about what actually happened, accepted as valid anyway.**

*How many protocols right now are marketing mathematical certainty held together by a CLI step nobody ever ran, and how many of them will get to write the official version of what happens when someone finally notices?*

REKT serves as a public platform for anonymous authors, we take no responsibility for the views or content hosted on REKT.

**donate (ETH / ERC20): [0x3C5c2F4bCeC51a36494682f91Dbc6cA7c63B514C](https://etherscan.io/address/0x3C5c2F4bCeC51a36494682f91Dbc6cA7c63B514C)**

disclaimer:

REKT is not responsible or liable in any manner for any Content posted on our Website or in connection with our Services, whether posted or caused by ANON Author of our Website, or by REKT. Although we provide rules for Anon Author conduct and postings, we do not control and are not responsible for what Anon Author post, transmit or share on our Website or Services, and are not responsible for any offensive, inappropriate, obscene, unlawful or otherwise objectionable content you may encounter on our Website or Services. REKT is not responsible for the conduct, whether online or offline, of any user of our Website or Services.
