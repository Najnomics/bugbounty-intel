# 🕵️‍♂️ Cork: $12M Hack and the Post-Mortem Analysis in the Audit

- **Source URL:** https://rekt.news/after-post-mortem
- **Fetched:** 2026-11-17
- **Channel:** @defendor_eng
- **Telegram message:** https://t.me/defendor_eng/219 (id 219)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# After the Post-Mortem

*"sherlock missed it. ct > ds. [uniswap hook is not problem.](https://etherscan.io/tx/0xea7dc9c0356a97e7300022a540709b4c2592401df98621ac2181a9b295058f59)"*

[Cork Protocol lost $12 million](https://rekt.news/cork-protocol-rekt) and thought they knew who to blame. Then the person who actually took their money decided to fact-check their homework – in permanent ink on the blockchain.

While protocols scramble to assign blame and audit firms point fingers at each other, the person who actually pulled off the heist decided to weigh in on who really dropped the ball.

What followed wasn't your typical post-exploit damage control. Instead of the usual "sorry for your loss" theater, Cork's aftermath became an all-out war between audit firms, complete with leaked scope documents, overdue reports, and accusations flying faster than exit liquidity during a rug pull.

**Between a CEO writing tell-all exposés and the hacker donating stolen funds to imprisoned developers, the situation after Cork's post-mortem revealed something more damaging than any smart contract vulnerability: an audit industry that might be auditing everything except its own credibility.**

*When the person who stole your money starts fact-checking your security providers, what does that say about who's really watching the watchers?*

*Credit:[Cork Protocol](https://www.cork.tech/blog/post-mortem), [Jack Sanford](https://x.com/jack__sanford/status/1935306618998038680), [Sherlock](https://drive.google.com/file/d/1XiDqE0Pj7W7L2xmxR1Q7mSI32aXGgEe6/view), [Cantina/Spearbit](https://cantina.xyz/portfolio/2858a0dd-503c-4e73-9e67-165fe6b99714), [Trust Security](https://x.com/trust__90/status/1937938216142684545), [Roman Storm](https://x.com/rstormsf/status/1937885974731870387), [Phil Fogel](https://x.com/Philfog/status/1937965468314440073), [Quantstamp](https://drive.google.com/file/d/1ma-WMbiy5QS_aW4ySqGbyjyx6KHYXlzI/view), [Runtime Verification](https://drive.google.com/file/d/1snmZ1d3JU8He0L42rD6yybCGQdrPxSjV/view)*

[Cork Protocol's May 28th exploit](https://www.cork.tech/blog/post-mortem) seemed straightforward enough – a sophisticated attacker exploited two separate vulnerabilities to drain $12 million from the wstETH:weETH market.

But what happened after the post-mortem dropped turned into something more complex: a public audit accountability debate that exposed uncomfortable questions about how DeFi security really works.

Within days of Cork's detailed technical breakdown, [Sherlock CEO Jack Sanford published a methodical analysis](https://x.com/jack__sanford/status/1935306618998038680) that read less like industry commentary and more like a forensic investigation.

Sanford wasn't interested in the hack itself – he wanted to know why the people paid to prevent it had apparently missed the memo.

*Specifically Cantina and Spearbit. Cantina – one of the firms involved in Cork's security reviews – [merged with Spearbit in late May 2025](https://x.com/cantinaxyz/status/1927388627463537115), combining what they called "two parts of the same mission" into a unified platform.*

**Sanford's investigation cut straight to the documentation disparities.**

According to Sanford's research, [three audit firms provided clear documentation of their scope](https://docs.cork.tech/smart-contracts/v1/audits): commit hashes, public repositories, explicit boundaries.

But when he examined [Cantina and Spearbit's documentation](https://cantina.xyz/portfolio/2858a0dd-503c-4e73-9e67-165fe6b99714), he found something different – private repositories, missing commit hashes, and what appeared to be deliberate scope obfuscation.

*Sanford didn't stop at paperwork. The numbers told their own story.*

**He examined the actual audit results: [Sherlock's 12-day competition](https://drive.google.com/file/d/1XiDqE0Pj7W7L2xmxR1Q7mSI32aXGgEe6/view) attracted 39 security researchers who found 10 critical vulnerabilities.**

[Cantina's 22-day private competition](https://cantina.xyz/portfolio/2858a0dd-503c-4e73-9e67-165fe6b99714), completed in January 2025, found some issues but somehow missed every single critical vulnerability that had been flagged months earlier.

Either Cork's codebase underwent a miraculous transformation between audits, or something about the audit process produced different results.

[Cork's post-mortem acknowledged that multiple audits had missed "access control vulnerability in the Cork Hook"](https://www.cork.tech/blog/post-mortem) – yet some of those same auditors were now claiming the vulnerable code wasn't in their scope.

*When audit firms start playing semantic games about what they actually reviewed, what exactly are they protecting?*

### The Hacker’s Peer Review

*While audit firms debated scope and documentation standards, an unexpected voice joined the conversation – the Cork exploiter themselves, broadcasting their take directly onto Ethereum's public ledger.*

**"[sherlock missed it. ct > ds. uniswap hook is not problem.](https://etherscan.io/tx/0xea7dc9c0356a97e7300022a540709b4c2592401df98621ac2181a9b295058f59)"**

The message arrived via a zero-value transaction from [the attacker's wallet](https://etherscan.io/address/0xea6f30e360192bae715599e15e2f765b49e4da98) on June 11th, transforming the blockchain into a public bulletin board for exploit commentary.

But this wasn't just trolling – the hacker was directly contradicting [Cork's official post-mortem](https://www.cork.tech/blog/post-mortem), which blamed an "access control vulnerability in the Cork Hook."

Hours later, [a second message appeared](https://etherscan.io/tx/0xe82ad5097063589996b6ae2b042514b72cf17f56c7fcecc625a418f511cc150e), this time in Estonian, containing what reads like a broader critique of the security industry: firms that "failed to detect the real problem" yet rushed to publish analysis for "promotion" rather than accuracy.

*The hacker [took aim at post-exploit analysis firms](https://etherscan.io/tx/0xe82ad5097063589996b6ae2b042514b72cf17f56c7fcecc625a418f511cc150e), suggesting many rushed to publish commentary without understanding the actual vulnerability.*

**Cork's fallout didn't stay confined to just the firms who audited Cork.**

Trust Security decided to [air some dirty laundry](https://x.com/trust__90/status/1937938216142684545), calling out platforms that "default to client's perspective" and give clients an annual allowance for bounty scams.

Meanwhile, the Cork hacker was busy making their own kind of statement.

Then came the ultimate power move: the [attacker donated 10 ETH to the legal defense fund of Tornado Cash](https://x.com/PeckShieldAlert/status/1937771008276201864) developers Roman Storm and Alexey Pertsev.

*When [Storm returned the funds citing legal constraints](https://x.com/rstormsf/status/1937885974731870387), Cork's co-founder [Phil Fogel thanked him publicly](https://x.com/Philfog/status/1937965468314440073) and made his own donation to the defense fund.*

**Strange times when the person who drained your protocol ends up inadvertently facilitating your charitable giving.**

But the hacker's most intriguing claim was technical: disputing that Uniswap hooks were the core problem.

According to their on-chain messages, there were "many ways to take DS, not just the Uniswap hook."

This directly contradicted the narrative emerging from Cork's post-mortem and subsequent security analysis.

[The hacker's technical critique](https://etherscan.io/tx/0xe82ad5097063589996b6ae2b042514b72cf17f56c7fcecc625a418f511cc150e) hit harder than most security firms' analysis.

**They pointed out that Cover Tokens were "the most important" part of the exploit – suggesting the entire industry was focused on the wrong vulnerability.**

[Cork's own post-mortem later confirmed two separate attack vectors](https://www.cork.tech/blog/post-mortem) were combined, making the hacker's technical commentary uncomfortably accurate.

Either the exploiter was deflecting attention from their actual methods, or the industry's post-exploit analysis was focusing on the wrong vulnerability entirely.

**Given that this person had intimate knowledge of Cork's weaknesses, their technical commentary carried an uncomfortable weight.**

*When the person who successfully attacked your system starts correcting your security experts' analysis, should that maybe get some attention?*

### The Silent Treatment

*A few weeks after Cork's $12 million lesson in trust, questions about audit transparency persist.*

**Looking at the other firms involved, [Sherlock dropped their full report](https://drive.google.com/file/d/1XiDqE0Pj7W7L2xmxR1Q7mSI32aXGgEe6/view) with commit hashes and scope details. Same with [Quantstamp](https://drive.google.com/file/d/1ma-WMbiy5QS_aW4ySqGbyjyx6KHYXlzI/view) and [Runtime Verification](https://drive.google.com/file/d/1snmZ1d3JU8He0L42rD6yybCGQdrPxSjV/view).**

Their work is sitting there for anyone to scrutinize, critique, or vindicate.

Neither Quantstamp nor Runtime Verification have commented publicly on the post-exploit accountability debate.

**The contrast in transparency approaches becomes even starker when examining what Cork's own analysis revealed.**

[Cork's post-mortem was crystal clear](https://www.cork.tech/blog/post-mortem): "access control vulnerability in the Cork Hook, which none of our audits flagged." Yet some firms now claim that vulnerable code was never their job to review.

When accountability claims clash with documented outcomes, getting straight answers becomes its own challenge.

*When Rekt News reached out to Hari - the CEO of Cantina/Spearbit - for further clarification, he cited confidentiality agreements while disputing public criticism: "I can confirm that the article by Jack is incorrect and is a gross misrepresentation of facts. There are certain important facts we cannot disclose today, but we will disclose them in the future."*

**Asked specifically what factual errors could be corrected without violating confidentiality, Hari responded: "We cannot disclose anything without violating our confidentiality agreements... In this scenario, the situation is even more complicated."**

When you can claim someone is wrong but can't explain how, promise vindication but can't say when, and insist the truth exists but can't share it - what exactly are you clarifying?

When the CEO describes a situation as "even more complicated" than standard confidentiality, what exactly is he protecting?

**Funny how confidentiality never seems to prevent marketing materials from advertising security expertise, but suddenly kicks in when it's time to show the actual work.**

*When accountability becomes a matter of interpretation rather than documentation, what does that say about the audit process?*

*Cork's $12 million lesson is over, but the questions it raised are just getting started.*

**A handful of security researchers reached out after we published our initial Cork coverage, echoing many of the concerns that later surfaced publicly.**

Most stayed quiet - not from lack of opinions, but from lack of complete information.

When key evidence remains locked behind confidentiality agreements and missing reports, drawing firm conclusions becomes impossible.

That's the real problem here. Not whether any specific audit firm dropped the ball, but whether the current system allows anyone to figure out what actually happened when things go wrong.

*Jack Sanford put it best: important information needed to draw conclusions has been obscured.*

**Many sources won't speak publicly because they could face professional consequences for questioning the wrong firms or revealing the wrong details.**

This isn't sustainable. DeFi's security depends on accountability, and accountability requires transparency.

When audit scope becomes a semantic debate, when criticism gets buried under corporate speak about ongoing investigations - the whole system starts looking more like theater than security.

**Meanwhile, protocols keep launching with audit badges like security merit badges, users keep depositing based on those assurances, and when something inevitably breaks, everyone points fingers while the actual evidence stays locked away.**

Security researchers want to do good work. Protocols want real protection. Users want honest assessment of risks.

But somewhere between those goals and the current audit economy, something fundamental got lost.

**Maybe Cork's real lesson isn't about missed vulnerabilities or audit scope - maybe it's about an industry that's forgotten how to have honest conversations about failure.**

*When the people responsible for securing billion-dollar protocols can't even agree on what they were supposed to review, how can anyone else trust the process?*

REKT serves as a public platform for anonymous authors, we take no responsibility for the views or content hosted on REKT.

**donate (ETH / ERC20): [0x3C5c2F4bCeC51a36494682f91Dbc6cA7c63B514C](https://etherscan.io/address/0x3C5c2F4bCeC51a36494682f91Dbc6cA7c63B514C)**

disclaimer:

REKT is not responsible or liable in any manner for any Content posted on our Website or in connection with our Services, whether posted or caused by ANON Author of our Website, or by REKT. Although we provide rules for Anon Author conduct and postings, we do not control and are not responsible for what Anon Author post, transmit or share on our Website or Services, and are not responsible for any offensive, inappropriate, obscene, unlawful or otherwise objectionable content you may encounter on our Website or Services. REKT is not responsible for the conduct, whether online or offline, of any user of our Website or Services.
