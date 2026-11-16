# 🌊 Vulnerabilities Live in Program States, Not Lines of Code

- **Source URL:** https://medium.com/@TalBeerySec/dense-in-depth-rethinking-security-when-vulns-are-everywhere-229dbd3e8477
- **Fetched from:** https://medium.com/feed/@TalBeerySec
- **Fetched:** 2026-11-16
- **Channel:** @defendor_eng
- **Telegram message:** https://t.me/defendor_eng/2308 (id 2308)
- **Method:** medium-rss-content readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
**TL;DR: The AI-driven Vulnpocalypse settled a 20-year-old debate: vulnerabilities are dense. Our defenses are still built as if they were sparse. Time for a paradigm shift.**

For more than 20 years, since Eric Rescorla’s seminal 2004 paper provocatively asked in its title “Is finding security holes a good idea?”, the strategic thinkers of the infosec community have been circling one question. Bruce [Schneier](https://www.schneier.com/essays/archives/2014/05/should_us_hackers_fi.html) later gave it its crisp form: are vulnerabilities in software dense or sparse?

The answer matters more than almost any other open question in our field, as Dan [Geer](http://geer.tinho.net/fgm/fgm.geer.1504.pdf) explained:

If they are sparse, then every vulnerability you find and fix meaningfully lowers the number of vulnerabilities that are extant. If they are dense, then finding and fixing one more is essentially irrelevant to security and a waste of the resources spent finding it. Six-take-away-one is a 15% improvement. Six-thousand-take-away-one has no detectable value.

The debate was never settled. What little empirical evidence existed (notably Ozment and Schechter’s 2006 [study](https://www.usenix.org/legacy/event/sec06/tech/full_papers/ozment/ozment.pdf) of OpenBSD, which found the rate of newly discovered vulns slowly decaying over the years) leaned towards “sparse”, but it rested on small numbers from a single, unusually security-obsessed codebase.

The industry didn’t wait for a verdict. It historically bet on “sparse”. Security teams are heavily invested in finding, triaging and patching vulns, and celebrate the process with bug bounties. Now that AI systems are finding vulns at record pace, much of the infosec community is (mostly unsuccessfully) trying to run the same playbook, only faster.

A few organizations can run the playbook at this speed. Most cannot, and it would not matter if they could. While the good intentions are not in doubt, the premise is. It is time to ask whether the bet was wrong, and vulns are actually dense. The evidence now says they are.

### The removal-capture method

How do you count what you cannot see? [Geer](http://geer.tinho.net/fgm/fgm.geer.1504.pdf) suggested borrowing a trick from wildlife biology: the removal-capture method.

Say a biologist wants to estimate how many fish live in a lake. Rather than trying to count them all, she:

1. Catches n₁ fish in a fishing round of fixed duration, and removes them from the lake.
2. Waits a short while.
3. Catches n₂ fish in a second round of the same duration, using the same method.

If the fish population is small, the second round comes up noticeably short, because the first round removed a meaningful share of the population. If the second round comes back with about as many fish as the first, the first round made no dent: the population is huge compared to the catch. (Plug n₁ = n₂ into the formula and N₀ goes to infinity.)

The translation to software is direct. The codebase is the lake, the vulns are the fish, and a pentest, a bug bounty program or an AI scanner is the fishing round:

1. Find n₁ vulns in a fixed-effort round, and remove them by patching.
2. Wait a short while.
3. Find n₂ vulns in a second round of the same effort.

If the catch doesn’t shrink, round after round and patch after patch, vulns are dense.

### Google Chrome’s removal-capture natural experiment

Chrome’s patch cycle is the perfect natural experiment for removal-capture, and thanks to Chrome’s extreme transparency, all the data is public. Patches ship in “milestones” on a regular cadence (every four weeks until recently, now every two), and each milestone’s release notes list every newly patched vuln along with its CVE.

The pre-AI years are the first experiment. For many years, Chrome vulns were caught using the same method and roughly the same effort: a world-class internal security team, external researchers and one of the industry’s richest bug bounty programs. Round after round, the catch stayed flat at a few dozen vulns per milestone. By removal-capture logic, that is already an answer. Many years of catching and removing fish made no visible dent in the lake’s fish population.

**Vulns are dense.**

Then the fishing equipment was upgraded. According to Google, it started scanning the Chrome codebase with AI in early 2026:

[Stronger with every update: How we're making Chrome and the web safer in the AI Era](https://blog.google/security/chrome-stronger-with-every-update/)

The impact was staggering:

In the last two milestones, Chrome 149 and 150, we have fixed 1072 security bugs, surpassing the total number of security bugs fixed across the prior 23 milestones combined.

If you are a Chrome user, you have probably felt it first hand, as nowadays the browser asks to restart itself to apply security updates every few days, compared to every few weeks in the past.

The uptick is visible from milestone 146, released in early March:

Read through the removal-capture lens, Google’s own numbers validate the uncomfortable truth about the pre-AI era: the manual catch was taking dozens of fish out of the lake every month with a fishing rod, while thousands sat there, reachable, waiting for a better net.

**Vulns are dense.**

But maybe the AI trawl, catching hundreds of vulns per milestone, can do what the fishing rod couldn’t? This is the second experiment. If the fish population were finite, we would expect the catch to start shrinking after a while. The data is public, so we can check for ourselves.

(One technical adjustment is needed first. Chrome moved from four-week to two-week milestones during this period, so raw per-milestone counts would mechanically halve even if nothing changed. The honest comparison is vulns patched per week, which is the lower panel below.)

After eight months of AI scanning and several thousand vulns removed, the equivalent of many years of pre-AI findings, the rate has not decayed. It has reached an all-time high: 175 patched vulns per week in milestone 156, released in October.

Google’s AI scanning is not catching the fish before anyone else can. External researchers serve as a control group here: Google’s share of reported vulns rose sharply, but the absolute number found by outsiders rose too, to several times its pre-AI level. The trawler is not emptying the lake, other players are catching more than ever, and there is no reason to think attackers, who fish the same water, are doing any worse.

Chrome is critical infrastructure serving billions of users, and it enjoys one of the industry’s best security programs: a well-maintained open-source codebase, some of the best security experts in the world and a generous bug bounty. And still, it cannot even begin to empty its lake of latent vulns, many of them high-severity and years old. (See appendix for more stats, methodology discussions and addressing possible objections)

**Vulns are dense.**

### Fish all the way down

At first, this result seems counter-intuitive. Our software is written by great developers. Surely they don’t plant a vuln in every line they write, only in a small fraction of them. So if we fish deep enough, patch after patch, we should eventually hit the codebase’s rock bottom and come out vuln-free.

The flaw in this intuition is that vulns are not a property of lines of code. They are a property of program states, and of the execution paths that reach them: the practically infinite combinations of memory contents, inputs and timing that the code can produce at runtime. The thing we would need to enumerate is not the code. It’s the states. The lake is far deeper than we naively estimated.

(Jonathan Spring reached the “dense” side from the other direction in his 2023 paper “[An Analysis of How Many Undiscovered Vulnerabilities Remain in Information Systems](https://arxiv.org/abs/2304.09259)”, arguing from computability theory rather than data: proving a program vuln-free is, in general, undecidable. The result follows directly from Rice’s theorem and is non-constructive, since a program can be vuln-free even if nobody can prove it, but the intuition is the same: the object is the states, not the code.)

So how does a finite amount of code produce a practically infinite number of vulnerable states? XBOW’s recent AI-assisted full-chain Chrome exploit gives a very concrete answer.

[Zero to Calc in Six Days: Inside XBOW's Chrome Full Chain](https://xbow.com/labs/research/zero-to-calc-in-six-days-inside-xbow-chrome-full-chain)

XBOW’s write-up contains a striking observation about the nature of the three vulnerabilities in the chain:

For the vulnerabilities themselves, we were struck by the fact that (coincidentally) all three vulnerabilities were ultimately about mutating something thought to be immutable: in stage 1, a HeapNumber; in stage 2, a transferred WebP buffer; and in stage 3, the page protection of a supposedly frozen process. These kind of invariant violations may be where LLMs shine: they can apply their encyclopedic knowledge of operating system APIs and open source code to come up with situations where the invariant fails.

All three vulns have the same shape: a sandwich. The bottom slice is an instruction that forms an implicit assumption about shared state (“this number can’t change”, “this buffer has been handed off”, “this process is frozen”). The top slice is a later instruction that relies on that assumption. The filling is a third instruction that the attacker manages to slip in between the two, breaking the assumption before it is used. Note that each of the three is perfectly correct on its own. The bug lives in none of them. It lives in the ordering.

So where can a vuln hide? Between any two instructions that share an assumption about state, which is to say, in any sandwich that can be assembled. That is a question about execution paths, and the number of possible execution paths grows exponentially with their length. In a browser, where multiple processes, threads, event loops, a JIT and a garbage collector all interleave, the attacker can nudge the ordering through inputs and timing. The invariant only needs to be violated once. Most of those orderings are unreachable in practice, and finding the one that is reachable is the attacker’s whole job.

So the lake is not merely deep. Developers add instructions linearly, and the lake of states deepens exponentially. Each new instruction can be a slice in exponentially many new sandwiches, or the filling that completes one that was already half-made. Every patch removes one bad ordering. Every feature may add a universe of them. There is no rock bottom, because the thing we are diving through isn’t the code. It’s the state; every order in which the code can run.

### Implications on software security

If vulns are dense, the “find and fix” paradigm the industry has run for two decades is not wrong. It is measuring the wrong thing. Here is what changes.

#### **Attack the mechanism, not the instances**

Fixing vulns one at a time means removing sandwiches from an infinite buffet. The useful question is not “where is the next sandwich?” but “what keeps the bread from being separated?” We should identify families of vulns (“equivalence classes”) by exposing the implicit invariant they share, and build mechanisms that enforce that invariant explicitly, so that the sandwich cannot be assembled at all. This is what a type system does for types, what an enforced-immutable object does for objects, what a LangSec-style parser does for inputs, what Rust’s borrow checker does for memory safety, and what formal verification does for program logic itself. Each of these retired an entire family of vulns, not an instance. Instead of directly patching [OpenSSL’s Heartbleed vulnerability](https://www.heartbleed.com/), make such buffer over-read impossible with technologies such as Rust.

**AI has made building software much cheaper. We should spend that dividend on rebuilding our software on top of generic security mechanisms, not on patching the old code faster.**

#### **Attacker-found vulns matter most**

We cannot drain the ocean, and however many vulns we close, attackers can always find new ones. So the bulk of a security team’s limited vuln-related resources should go to quickly identifying and patching the vulns that are actually being exploited. This is exactly the idea behind CISA’s Known Exploited Vulnerabilities (KEV) list, and in a dense world it stops being one input among many and becomes the primary one. 

This also means investing in spotting exploitation in the wild: crash-report analysis, telemetry anomaly detection, tripwires and canaries, and threat intelligence that surfaces exploitation others have seen.

#### **Whitehat-found vulns matter too, but differently: find to learn, not find to fix**

If the lake is practically bottomless, a whitehat find does not meaningfully reduce the attackers’ supply. Its value is what it teaches us: which invariant was assumed, which family it belongs to, which mechanism would have prevented it. That is the input the previous point needs. What a whitehat find does not justify is treating each one as an emergency to be individually patched and shipped. Rescorla warned in 2004 that in a dense world, finding and disclosing vulns mostly hands intelligence to attackers, who can use it until every client is patched. The patch gap makes this concrete: Chrome’s fixes land in the public Chromium repository before they reach users, and Volexity recently documented multiple Chinese threat actors reading those commits and exploiting the not-yet-shipped fixes in the wild.

[Mind the (Patch) Gap: Multiple Chinese Threat Actors Chain 0-day Exploits in Chrome & Windows](https://www.volexity.com/blog/2026/09/09/mind-the-patch-gap-multiple-chinese-threat-actors-chain-0-day-exploits-in-chrome-windows/)

Defenders should therefore invest in vuln hunting lightly, and in bug bounties with a repriced sense of what a single vuln is worth (sorry fellow whitehats 🙁), and treat the results as intelligence for the mechanism work, not as a remediation queue.

#### **Apply “Defense in Depth” to our “Dense in Depth” software products**

We have been chanting the “assume breach” gospel for more than a decade. The time has come to actually live by it. Accept that breaches will occur, and structure systems and networks accordingly: keep the crown jewels deep inside the network and harden the way to get there, use microsegmentation to deny easy lateral movement, and plant deception land mines and canaries so that an intruder is detected fast and dealt with early.

### Never let a good crisis go to waste

The AI vuln crisis is real, but the crisis is not the vulns. It is our model of them. Vulns did not become dense in 2026; they were always dense. AI only made it impossible to keep pretending otherwise.

If we respond by doing what we have always done, only faster, we will drown in our own patch queue while attackers keep fishing from an ocean we were never going to drain.

The better response is to take the data at its word. Stop measuring security by the number of vulns found and fixed. Patch what is actually being exploited. Treat everything else we find as intelligence, and spend it on mechanisms that retire whole families of vulns at once. And build systems that survive the breach we know is coming.

We were never going to hit rock bottom. It is time to stop diving deeper and start rebuilding.

### Appendix: Addressing objections to the Chrome natural experiment

This appendix takes up the main objections to the Chrome experiment.

- **“The lake keeps growing. New code is added every milestone, so the recent findings may be mostly new vulns in new, possibly AI-written, code.”**

To check this, I traced each patched vuln to the lines its fix changed and dated them with the [SZZ algorithm](https://dl.acm.org/doi/10.1145/1082983.1083147#artseq-00003), which identifies the commit that introduced the code a fix touches. The AI-era milestones (146 and later) show the same age profile as the pre-AI ones: a median vulnerable-code age of three to four years, and a 90th percentile above ten years. The trawler is not catching this year’s fish. It is catching fish that have been in the lake for a decade.

- **“AI findings are ‘vuln slop’, with AI finding mostly unimportant low-severity issues.”**

The AI-era milestones contain a large share of High and Critical findings, by CVSS score. The mix did not get worse; the volume got larger.

- **“Chrome is not representative: a huge, old, C++ codebase with the largest attack surface in software. Nothing about it generalizes.”**

Chrome is certainly not the worst candidate to check. Chrome’s attack surface is indeed large, but it has enjoyed one of the industry’s best security programs for over a decade: a well-maintained open-source codebase, some of the best security experts in the world and a generous bug bounty.

The broader “Vulnpocalypse” reports show the same trend across vendors and products:

And even if Chrome were unrepresentative, it is the engine behind most of the world’s browsers and is deployed in nearly every organization, which makes the question of how to defend against its bottomless supply of vulns important in its own right. Smaller codebases, or ones written in memory-safe languages from the start, may well be sparser. That is the mechanism argument of this post, not a counter to it.

- **“The net keeps getting bigger. Better models and more compute every month would produce a rising catch even from a finite lake.”**

True, and Google does not publish its scanning effort, so this cannot be ruled out directly. Two observations limit it. First, removal-capture asks for constant effort, and if effort is measured in money rather than model capability, the falling cost of AI means a flat budget buys a bigger net every quarter; there is no sign that the catch is getting more expensive.

Second, and more importantly, even if Google’s net reaches deeper water with every milestone, the lake is not being emptied for anyone else. External researchers, whose effort Google does not control, are catching more than they did before the AI era, not fewer. Whatever the trawler is doing, it is not making vulns harder for others, blackhats included, to find.

Thanks to Prof. [Ciaran Martin](https://www.linkedin.com/in/cyberciaran/), [halvarflake](https://x.com/halvarflake), [Alon Oring](https://x.com/alono88), Brendan Dolan-Gavitt ([moyix](https://x.com/moyix)), [ace\_\_pace](https://x.com/ace__pace), and [thegrugq](https://x.com/thegrugq) for reviewing drafts of this post and for their sharp comments. Any remaining errors, and all the opinions, are mine.
