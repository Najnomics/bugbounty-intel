# @Guhu95 — full verbatim X archive (security-relevant posts)

_Generated 2026-11-11 from the X API (full-archive search + timeline). Every post below is copied word-for-word; t.co links are expanded; quoted posts are inlined in full; media are listed with alt text when the author provided it. Posts are grouped by conversation (a thread = the author's root post followed by their own replies, oldest first). Groups are newest first. An agent without X access can rely on this file._

- Posts in this file: 26
- Conversations/threads: 23
- Oldest post captured: 2025-05-29
- Newest post captured: 2026-03-12


---

## 2026-03-12 · Post · Who wins? [pic.x.com/0Jz2RdMU72] https://twitter.com/z0r0zzz/status/2031755989968642511


### Post — @Guhu95 — 2026-03-12 06:29 UTC (2026-03-12 07:29 WAT)

- URL: https://x.com/Guhu95/status/2031980937421226167
- Metrics (at fetch): bookmark 2, impression 1113, like 8, quote 0, reply 0, retweet 0

> Who wins? [pic.x.com/0Jz2RdMU72] https://twitter.com/z0r0zzz/status/2031755989968642511

**Media:**
- photo: https://pbs.twimg.com/media/HDMKDn3bQAQ2WaM.jpg — no alt text provided by author

**Links in post:** https://twitter.com/z0r0zzz/status/2031755989968642511

**Quoted post** 2031755989968642511: not readable via the API (deleted, private, or withheld).


---

## 2026-02-26 · Post · Looking at a live Ethereum Mainnet bug is an unforgettable experience.


Tags (automatic): AI-assisted hunting, Platform: Code4rena / Sherlock / Cantina


### Post — @Guhu95 — 2026-02-26 07:42 UTC (2026-02-26 08:42 WAT)

- URL: https://x.com/Guhu95/status/2026925805176238370
- Metrics (at fetch): bookmark 9, impression 3823, like 42, quote 0, reply 2, retweet 4

> Looking at a live Ethereum Mainnet bug is an unforgettable experience.
>
> But then you realize you were handed that bug by an AI - just one bug among many more bugs in the same "scan"... This is when you feel the ground start shaking.
>
> This was part of a collab with @octane_security for the Fusaka contest. A glimpse into our future as auditors and bug hunters? Will share some more details later on what it was like.
>
> Thanks Octane, @ethereumfndn , @sherlockdefi for an amazing challenge and experience!

**Links in post:** https://twitter.com/octane_security/status/2026691133980684775

**Quoted post (full text):**

    #### Quoted post — @1678922837996998659 — 2026-02-25 16:09 UTC (2026-02-25 17:09 WAT)
    
    - URL: https://x.com/1678922837996998659/status/2026691133980684775
    - Metrics (at fetch): bookmark 46, impression 59452, like 208, quote 24, reply 22, repost 25
    
    > 1/ Octane’s AI found a high-severity liveness bug in the @Nethermind execution client that could have stopped local block production for 38% of @ethereum mainnet validators.
    >
    > This bug was patched via the @ethereumfndn bug bounty program, with no exploitation observed. [pic.x.com/ebdUt31WC8]
    
    **Media:**
    - photo: https://pbs.twimg.com/media/HCBAILla0AAsNNC.jpg — no alt text provided by author
    


---

## 2025-12-30 · Post · Glamsterdam upgrade contest rules wish-list🤞:


Tags (automatic): Platform: Code4rena / Sherlock / Cantina


### Post — @Guhu95 — 2025-12-30 07:19 UTC (2025-12-30 08:19 WAT)

- URL: https://x.com/Guhu95/status/2005901452196421928
- Metrics (at fetch): bookmark 9, impression 4887, like 45, quote 0, reply 2, retweet 3

> Glamsterdam upgrade contest rules wish-list🤞:
> - POCs on-request only if needed.
> - $750K pot: 50k infos, 250k lows, 450k meds + highs.
> - Unconditional pot. No "Mythical Critical".
> - No custom severity rules: regular platform rules with clarifications on how network safety and liveness impacts are treated.
> - Judging authority remains with platform judges.
> - Escalations open to everyone (for their own issues).
> - Live fixes are announced in a special thread.
> - No multipliers for early submissions.
>
> Why this is better for Ethereum's security?
>
> - Requiring POCs for all issues wastes a huge amount of very scarce time on things like vibe-fighting the different compilers, kurtosis quirks, writing and debugging scripts, and any number of tasks. Instead POCs can be requested by client team or judge IF it's actually needed. The impact from this change will be huge: 1.5x - 2x more time to find bugs.
>
> - Pot size. The contest is a huge challenge, 10x-30x harder than the typical contest, especially for SRs new to this scope. EV should be attractive to compensate. 1M unconditional would be best, but 750K should be possible given the value delivered by past contests. 1.5x to EV
>
> - Conditionals reduce perceived EV. Hated by many if not most SRs at this point. Also, since Highs were found in both, this was highly ineffective in Pectra and Fusaka - same money paid for less eyes. At least 1.5x perceived EV increase here.
>
> - Bigger "Lows" pot: Pectra 250k lows pot was a great EV signal and was also inclusive of more impacts. Fusaka's 25k infos pot was a terrible collective rug (80+ unique fixed issues for 25k in total + no dups). Impact: 2x EV.
>
> - Broader severity rules: narrow scope rules caused a lot of frustration, escalations, discussions, delays, and general pain for everyone. Custom severity rules are a huge known "red-flag" for contests. Too many issues became "infos", in a way that's incompatible with future participation under similar rules. Some great SRs found "only" infos when judging was done - they will never return for a similar treatment unless rules are different. 2x EV increase from this.
>
> - Judgement should be left to the hosting platform. In general, "sponsor judging" is a huge red-flag. Judging requires a lot of judging experience and a specific skill set - sponsors generally are not trusted by SRs to possess either, and are not impartial. In this contest a lot of seemingly in-scope findings were downgraded, and a lot of explicitly-OOS findings were upgraded. Note that making the pot unconditional makes this especially easy, since it makes the budget fixed. 30%-50% +EV due to more predictable judging.
>
> - Escalations should be open to everyone - like it was done by Sherlock for Fusaka🙌. Otherwise, most SRs that use other platforms, or don't do contests generally are looking at a huge reduction of EV. 2x EV increase from announcing this ahead of time.
>
> - Looking for fixes independently is a terrible waste of time. Each client repo has tens or hundreds of recently active or open PRs or branches, which can contain a fix anywhere. Reviewing these additional hundreds of diffs daily is a huge waste of time. Not reviewing them saves time, but leads to disappointment. Client teams can report contest-related fixes to the judges, who can post it to a common thread - this would save 90% of the pain. 10%-20% participation increase from saved time.
>
> - Multipliers. Whoever can start early - will start early, to have more time available, and to benefit from "live fixes" policy which already creates a huge incentive to be early. So multiplers' positive effect adds nothing, but the negative effect of reducing EV for late joiners remains. Whoever can only join late, sees lower EV for doing so. 10-30% increase in EV by fixing this.
>
> Of course, the effects don't add up linearly, and there is a fixed pool of SRs, and a fixed amount of time they can contribute. But these rules' goal is to make participating in Glam a "no brainer" good EV decision for SRs.
>
> Hopefully, this can help us achieve even better security for future upgrades.

**Links in post:** https://twitter.com/Guhu95/status/2004037063054971056

**Quoted post (full text):**

    #### Quoted post — @Guhu95 — 2025-12-25 03:50 UTC (2025-12-25 04:50 WAT)
    
    - URL: https://x.com/Guhu95/status/2004037063054971056
    - Metrics (at fetch): bookmark 25, impression 13626, like 76, quote 2, reply 3, retweet 6
    
    > Some Fusaka contest thoughts:
    >
    > The Good:
    > - Client diversity still a mind boggling security super power.
    > - EF doing contests for upgrades is great for security, and sets the right example.
    > - AI is a game-changer, indispensable in huge complex scopes.
    > - Geth is still the Goat - more secure, more readable, and more correct than even the spec.
    > - @alexfilippov314 dominates again! Only 1 info finding is a crazy flex.
    >
    > The Bad:
    > - Cryptography is still a bug hotspot.
    > - 2 KZG libraries for 11 clients is the Achilles heel of client diversity.
    > - PeerDAS is a whole new blockchain (a sharded one!) which is awkwardly entangled in the existing Ethereum chain. The surface area for severe issues is now much larger, even in parts that used to be non-critical.
    >
    > The Ugly:
    > - Contest rules were even more impossible than for Pectra. The more frustrating a contest is, the less participation it gets. Less eyes -> less security. There were 950 submissions for Monad, and only 360 submissions for Ethereum - it should be the other way around.
    > - The upgrade did not go smoothly this time :(
    >
    > A crazy ride and learning experience as always.
    
    **Links in post:** https://twitter.com/Guhu95/status/1904360201597387131
    
    **Quoted post** 1904360201597387131: not readable via the API (deleted, private, or withheld).
    


---

## 2025-12-25 · Post · Big thanks to @sherlockdefi &amp; the @ethereumfndn for the contest 🙏🙌


Tags (automatic): Platform: Code4rena / Sherlock / Cantina


### Post — @Guhu95 — 2025-12-25 03:58 UTC (2025-12-25 04:58 WAT)

- URL: https://x.com/Guhu95/status/2004039088706597103
- Metrics (at fetch): bookmark 0, impression 3420, like 40, quote 0, reply 2, retweet 0

> Big thanks to @sherlockdefi &amp; the @ethereumfndn for the contest 🙏🙌
>
> Congrats to the winners👑, an epic accomplishment and well deserved rewards!
>
> https://x.com/Guhu95/status/2004037063054971056 https://twitter.com/sherlockdefi/status/2003129673627349316

**Links in post:** https://x.com/Guhu95/status/2004037063054971056, https://twitter.com/sherlockdefi/status/2003129673627349316

**Quoted post** 2003129673627349316: not readable via the API (deleted, private, or withheld).


---

## 2025-12-25 · Post · Big thanks to @sherlockdefi &amp; the @ethereumfndn for the contest 🙏🙌


Tags (automatic): Platform: Code4rena / Sherlock / Cantina


### Post — @Guhu95 — 2025-12-25 03:57 UTC (2025-12-25 04:57 WAT)

- URL: https://x.com/Guhu95/status/2004038764671484364
- Metrics (at fetch): bookmark 0, impression 22, like 0, quote 0, reply 0, retweet 0

> Big thanks to @sherlockdefi &amp; the @ethereumfndn for the contest 🙏🙌
>
> Congrats to the winners👑, an epic accomplishment and well deserved rewards! https://t.co/u99Ay47i0M

**Quoted post** 2003129673627349316: not readable via the API (deleted, private, or withheld).


---

## 2025-12-25 · Post · Some Fusaka contest thoughts:


Tags (automatic): Blockchain / L1-L2 / bridge, AI-assisted hunting


### Post — @Guhu95 — 2025-12-25 03:50 UTC (2025-12-25 04:50 WAT)

- URL: https://x.com/Guhu95/status/2004037063054971056
- Metrics (at fetch): bookmark 25, impression 13626, like 76, quote 2, reply 3, retweet 6

> Some Fusaka contest thoughts:
>
> The Good:
> - Client diversity still a mind boggling security super power.
> - EF doing contests for upgrades is great for security, and sets the right example.
> - AI is a game-changer, indispensable in huge complex scopes.
> - Geth is still the Goat - more secure, more readable, and more correct than even the spec.
> - @alexfilippov314 dominates again! Only 1 info finding is a crazy flex.
>
> The Bad:
> - Cryptography is still a bug hotspot.
> - 2 KZG libraries for 11 clients is the Achilles heel of client diversity.
> - PeerDAS is a whole new blockchain (a sharded one!) which is awkwardly entangled in the existing Ethereum chain. The surface area for severe issues is now much larger, even in parts that used to be non-critical.
>
> The Ugly:
> - Contest rules were even more impossible than for Pectra. The more frustrating a contest is, the less participation it gets. Less eyes -> less security. There were 950 submissions for Monad, and only 360 submissions for Ethereum - it should be the other way around.
> - The upgrade did not go smoothly this time :(
>
> A crazy ride and learning experience as always.

**Links in post:** https://twitter.com/Guhu95/status/1904360201597387131

**Quoted post** 1904360201597387131: not readable via the API (deleted, private, or withheld).


---

## 2025-11-09 · Post · @samczsun Project team can seed it when launching signalling security. Anyone can contribute later, 


### Post — @Guhu95 — 2025-11-09 10:05 UTC (2025-11-09 11:05 WAT)

- URL: https://x.com/Guhu95/status/1987461502501376287
- Metrics (at fetch): bookmark 0, impression 91, like 0, quote 0, reply 0, retweet 0

> @samczsun Project team can seed it when launching signalling security. Anyone can contribute later, eg project backers (VCs or founders), to boost attractiveness to security conscious users / integrations.
>
> But no one will do it, because no one actually cares enough.


---

## 2025-08-29 · Thread · Looks dumb, but is a genius way to put values onchain transparently: 


Tags (automatic): Blockchain / L1-L2 / bridge


### Post — @Guhu95 — 2025-08-29 02:12 UTC (2025-08-29 03:12 WAT)

- URL: https://x.com/Guhu95/status/1961250661104074761
- Metrics (at fetch): bookmark 0, impression 907, like 5, quote 0, reply 1, retweet 0

> Looks dumb, but is a genius way to put values onchain transparently: 
>
> Q: Why not JSON in calldata?
> A: More opaque. Contract leverages explorers as frontends.
>
> Q: Why storage instead of immutables?
> A: More opaque off-chain, need ABI to read. Accessing storage by index is easier. [pic.x.com/ZZAkLN1G3Z] https://twitter.com/PopPunkOnChain/status/1961083122319069397

**Media:**
- animated_gif: https://pbs.twimg.com/tweet_video_thumb/GzfDE27bMAAck-W.jpg — no alt text provided by author

**Links in post:** https://twitter.com/PopPunkOnChain/status/1961083122319069397

**Quoted post** 1961083122319069397: not readable via the API (deleted, private, or withheld).


### Thread part 2 — @Guhu95 — 2025-08-29 02:24 UTC (2025-08-29 03:24 WAT)

- URL: https://x.com/Guhu95/status/1961253585641246757
- Metrics (at fetch): bookmark 0, impression 334, like 1, quote 0, reply 0, retweet 0

> It's even composable onchain: the hash means anyone can build a trustless oracle on top of the data. 
>
> They can use contract addresses to ensure provenance (by calculating from the deployer) and use "date in variable name" to prove the date. 
>
> Genius!


---

## 2025-08-22 · Post · wouldn't it be hilarious [pic.x.com/HEsasa94tL] https://twitter.com/zzykxx/status/189253195550313712


### Post — @Guhu95 — 2025-08-22 03:12 UTC (2025-08-22 04:12 WAT)

- URL: https://x.com/Guhu95/status/1958728873652494710
- Metrics (at fetch): bookmark 2, impression 1842, like 23, quote 0, reply 2, retweet 0

> wouldn't it be hilarious [pic.x.com/HEsasa94tL] https://twitter.com/zzykxx/status/1892531955503137126

**Media:**
- photo: https://pbs.twimg.com/media/Gy7NcJRboAIUuiN.jpg — no alt text provided by author

**Links in post:** https://twitter.com/zzykxx/status/1892531955503137126

**Quoted post** 1892531955503137126: not readable via the API (deleted, private, or withheld).


---

## 2025-08-14 · Post · Solidity "Treasury Company". But first, the magic trick of premium to NAV.


Tags (automatic): Smart contract / DeFi


### Post — @Guhu95 — 2025-08-14 08:32 UTC (2025-08-14 09:32 WAT)

- URL: https://x.com/Guhu95/status/1955910352925024439
- Metrics (at fetch): bookmark 2, impression 923, like 4, quote 1, reply 0, retweet 1

> Solidity "Treasury Company". But first, the magic trick of premium to NAV.
>
> Start by assuming a premium to NAV, like 1.5x:
> - Let's say asset is worth $10, you have 1 asset, and there is 1 share. 1 asset per share.
> - 1.5x premium means market pays $15 per share. Silly market, [pic.x.com/drr8jaoXmq] https://twitter.com/Guhu95/status/1946734325128671427

**Media:**
- photo: https://pbs.twimg.com/media/GyTIoxpa4AY6tTn.jpg — no alt text provided by author

**Links in post:** https://twitter.com/Guhu95/status/1946734325128671427

**Quoted post (full text):**

    #### Quoted post — @Guhu95 — 2025-07-20 00:50 UTC (2025-07-20 01:50 WAT)
    
    - URL: https://x.com/Guhu95/status/1946734325128671427
    - Metrics (at fetch): bookmark 1, impression 3095, like 10, quote 1, reply 1, retweet 0
    
    > So "crypto treasury companies" are: 
    >
    > Hundreds of companies + Only incompetent failed ones + Levering up on crypto + Luring in clueless money + Doing shady tradfi shit.
    >
    > Is this .. "decentralized" FTX? [pic.x.com/Q1MyvUPXWc]
    
    **Media:**
    - photo: https://pbs.twimg.com/media/GwQuQKGWEAA0tz1.jpg — no alt text provided by author
    


---

## 2025-07-20 · Post · So "crypto treasury companies" are: 


### Post — @Guhu95 — 2025-07-20 00:50 UTC (2025-07-20 01:50 WAT)

- URL: https://x.com/Guhu95/status/1946734325128671427
- Metrics (at fetch): bookmark 1, impression 3095, like 10, quote 1, reply 1, retweet 0

> So "crypto treasury companies" are: 
>
> Hundreds of companies + Only incompetent failed ones + Levering up on crypto + Luring in clueless money + Doing shady tradfi shit.
>
> Is this .. "decentralized" FTX? [pic.x.com/Q1MyvUPXWc]

**Media:**
- photo: https://pbs.twimg.com/media/GwQuQKGWEAA0tz1.jpg — no alt text provided by author


---

## 2025-07-17 · Post · Hot takes about the attack:


### Post — @Guhu95 — 2025-07-17 00:32 UTC (2025-07-17 01:32 WAT)

- URL: https://x.com/Guhu95/status/1945642655595291037
- Metrics (at fetch): bookmark 7, impression 1732, like 18, quote 0, reply 2, retweet 0

> Hot takes about the attack:
>
> 1. "Upgradeability is a vulnerability" for one more reason.
>
> 2. UUPS was always a mistake. "Premature (gas) optimization is the root of all evil".
>
> 3. Reliance on web2 infra was root cause again. Without etherscan bug attack is useless. https://twitter.com/dedaub/status/1945109337413742807

**Links in post:** https://twitter.com/dedaub/status/1945109337413742807

**Quoted post** 1945109337413742807: not readable via the API (deleted, private, or withheld).


---

## 2025-07-17 · Post · There are just two types of bugs:


Tags (automatic): Smart contract / DeFi, Memory corruption / native


### Post — @Guhu95 — 2025-07-17 00:23 UTC (2025-07-17 01:23 WAT)

- URL: https://x.com/Guhu95/status/1945640502025752709
- Metrics (at fetch): bookmark 51, impression 5581, like 78, quote 0, reply 4, retweet 3

> There are just two types of bugs:
>
> 1. Input validation. 
> 2. Logic bugs. Can also be called "output generation".
>  ̶3̶.̶ ̶O̶f̶f̶-̶b̶y̶-̶o̶n̶e̶.̶.̶  that's a logic bug
>
> Access control, price oracle, reentrancy, external calls, are all because of unchecked inputs of some type.
>
> Overflows, flashloans, DOS, insecure randomness, are all logic bugs.

**Links in post:** https://twitter.com/p_misirov/status/1945539845478330551

**Quoted post (full text):**

    #### Quoted post — @1232302723611201536 — 2025-07-16 17:43 UTC (2025-07-16 18:43 WAT)
    
    - URL: https://x.com/1232302723611201536/status/1945539845478330551
    - Metrics (at fetch): bookmark 112, impression 21840, like 170, quote 7, reply 6, repost 28
    
    > top 10 smart contract vulnerabilities in 2025 by OWASP 10 [pic.x.com/QunGhCSdRw]
    
    **Media:**
    - photo: https://pbs.twimg.com/media/Gv_yLb_aoAAbOSJ.jpg — no alt text provided by author
    


---

## 2025-06-28 · Post · Simplest form: num solos ≈ num unfound [pic.x.com/eNPVjJUQt6] https://twitter.com/Guhu95/status/1938


### Post — @Guhu95 — 2025-06-28 07:45 UTC (2025-06-28 08:45 WAT)

- URL: https://x.com/Guhu95/status/1938866425365700622
- Metrics (at fetch): bookmark 5, impression 2483, like 23, quote 1, reply 0, retweet 2

> Simplest form: num solos ≈ num unfound [pic.x.com/eNPVjJUQt6] https://twitter.com/Guhu95/status/1938224258515448042

**Media:**
- photo: https://pbs.twimg.com/media/Gug8DuUWgAE-8GJ.jpg — no alt text provided by author

**Links in post:** https://twitter.com/Guhu95/status/1938224258515448042

**Quoted post (full text):**

    #### Quoted post — @Guhu95 — 2025-06-26 13:14 UTC (2025-06-26 14:14 WAT)
    
    - URL: https://x.com/Guhu95/status/1938224258515448042
    - Metrics (at fetch): bookmark 65, impression 9171, like 107, quote 4, reply 8, retweet 10
    
    > You can measure how vulnerable the code is after a contest. This can help:
    > - Projects and users to estimate hack risk
    > - Bug hunters to scope targets
    > - Ecosystem to track what works best
    > - Platforms to manage reputation risk
    >
    > TL;DR: More solo findings -> more hidden bugs.
    >
    > This works for most formats: flat pot, conditionals, invitationals, reserved auditors. As long as duplicates are allowed.
    >
    > ### Recent examples: 
    >
    > - Cork exploit: last private contest had 4 solo mediums (out of 4 total mediums). "Chao 1 bias-corrected" estimates 6 unfound bugs. Jackknife 8 more bugs.
    >
    > - BeraBorrow's Recon's recent post about a critical: private contest had 8 solo mediums (out of 15 mediums), 6 doubletons (doubletons = found by two auditors). Chao 1: 4.5 more bugs, Jackknife: 9 more bugs.
    >
    > ### The science of capture-recapture
    >
    > There are many disciplines that use this approach: software engineering, quality control, biology & ecology, epidemiology, criminology, linguistics. 
    >
    > Similarly, there are many estimator formulas: Lincoln-Petersen, Chapman, Schnabel, Schumacher–Eschmeyer, Jolly–Seber, Chao 1 & 2, ACE, ICE, Jackknife 1 & 2, Bootstrap, Zelterman, Good–Turing, etc. Will post some links below.
    >
    > Two simple examples are Jackknife 1 & 2, Chao 1 & 2 which roughly say :
    >
    > - Jackknife 2 (second-order, simplified): `unfound = 2 * uniques - doubletons`. Jackknife is more popular in software-inspection studies.
    >
    > - Chao 1: `unfound = (uniques^2) / (2 * doubletons)`. (A slightly different version for no doubletons)
    >
    > Specifics don't matter really - pick your favorite from the long list. What's important is they all say: more unique findings -> more hidden bugs. 
    >
    > ### Intuitions
    >
    > Math is not always intuitive, so here are some intuitions.
    >
    > 1. Parallel worlds: If a bug is unique to one finder, there’s a parallel world where it stayed hidden because he got sick, or was booked on an audit, or just missed it. Maybe you're in that parallel world. In contrast, if there are many duplicates - in most worlds the same bugs are found.
    >
    > 2. Serial auditing: If you imagine auditors working in sequence, the contest is just a stopping point for the sequence. The contest with uniques stopped when new bugs were still being found, so more like these remain. In contrast, the contest with only duplicates stopped after finding most bugs of similar rarity.
    >
    > ### What can we do?!
    >
    > 1. Measure: what platforms, pot sizes, contest formats give the best coverage?
    > 2. Educate clients on the more secure formats with data.
    > 3. If you're a project, check if your contest was weak.
    >
    > ### No solo findings = code is safe? No. 
    >
    > It's possible whole classes of niche bugs (e.g. cryptography) or higher complexity bugs were not found because pot was too low. That's always a risk.
    >
    > This rule doesn't tell as what's safe, but it tells us what's LIKELY still vulnerable.
    >
    > ---------
    >
    > See next tweet for links and statistical nitpicking
    
    **Media:**
    - photo: https://pbs.twimg.com/media/GuXygVjasAA0zkX.jpg — no alt text provided by author
    


---

## 2025-06-26 · Thread · You can measure how vulnerable the code is after a contest. This can help:


### Post — @Guhu95 — 2025-06-26 13:14 UTC (2025-06-26 14:14 WAT)

- URL: https://x.com/Guhu95/status/1938224258515448042
- Metrics (at fetch): bookmark 65, impression 9171, like 107, quote 4, reply 8, retweet 10

> You can measure how vulnerable the code is after a contest. This can help:
> - Projects and users to estimate hack risk
> - Bug hunters to scope targets
> - Ecosystem to track what works best
> - Platforms to manage reputation risk
>
> TL;DR: More solo findings -> more hidden bugs.
>
> This works for most formats: flat pot, conditionals, invitationals, reserved auditors. As long as duplicates are allowed.
>
> ### Recent examples: 
>
> - Cork exploit: last private contest had 4 solo mediums (out of 4 total mediums). "Chao 1 bias-corrected" estimates 6 unfound bugs. Jackknife 8 more bugs.
>
> - BeraBorrow's Recon's recent post about a critical: private contest had 8 solo mediums (out of 15 mediums), 6 doubletons (doubletons = found by two auditors). Chao 1: 4.5 more bugs, Jackknife: 9 more bugs.
>
> ### The science of capture-recapture
>
> There are many disciplines that use this approach: software engineering, quality control, biology & ecology, epidemiology, criminology, linguistics. 
>
> Similarly, there are many estimator formulas: Lincoln-Petersen, Chapman, Schnabel, Schumacher–Eschmeyer, Jolly–Seber, Chao 1 & 2, ACE, ICE, Jackknife 1 & 2, Bootstrap, Zelterman, Good–Turing, etc. Will post some links below.
>
> Two simple examples are Jackknife 1 & 2, Chao 1 & 2 which roughly say :
>
> - Jackknife 2 (second-order, simplified): `unfound = 2 * uniques - doubletons`. Jackknife is more popular in software-inspection studies.
>
> - Chao 1: `unfound = (uniques^2) / (2 * doubletons)`. (A slightly different version for no doubletons)
>
> Specifics don't matter really - pick your favorite from the long list. What's important is they all say: more unique findings -> more hidden bugs. 
>
> ### Intuitions
>
> Math is not always intuitive, so here are some intuitions.
>
> 1. Parallel worlds: If a bug is unique to one finder, there’s a parallel world where it stayed hidden because he got sick, or was booked on an audit, or just missed it. Maybe you're in that parallel world. In contrast, if there are many duplicates - in most worlds the same bugs are found.
>
> 2. Serial auditing: If you imagine auditors working in sequence, the contest is just a stopping point for the sequence. The contest with uniques stopped when new bugs were still being found, so more like these remain. In contrast, the contest with only duplicates stopped after finding most bugs of similar rarity.
>
> ### What can we do?!
>
> 1. Measure: what platforms, pot sizes, contest formats give the best coverage?
> 2. Educate clients on the more secure formats with data.
> 3. If you're a project, check if your contest was weak.
>
> ### No solo findings = code is safe? No. 
>
> It's possible whole classes of niche bugs (e.g. cryptography) or higher complexity bugs were not found because pot was too low. That's always a risk.
>
> This rule doesn't tell as what's safe, but it tells us what's LIKELY still vulnerable.
>
> ---------
>
> See next tweet for links and statistical nitpicking

**Media:**
- photo: https://pbs.twimg.com/media/GuXygVjasAA0zkX.jpg — no alt text provided by author


### Thread part 2 — @Guhu95 — 2025-06-26 13:18 UTC (2025-06-26 14:18 WAT)

- URL: https://x.com/Guhu95/status/1938225388372795426
- Metrics (at fetch): bookmark 3, impression 577, like 3, quote 0, reply 1, retweet 0

> ### Links
> - https://blog.uvm.edu/tdonovan-vtcfwru/files/2020/06/18-Donov-pages-315-CB.pdf
> - https://www.uvm.edu/~ngotelli/manuscriptpdfs/Chapter%204.pdf
> - https://en.wikipedia.org/wiki/Good%E2%80%93Turing_frequency_estimation
>
> ### Stats nitpicks
>
> Directionally most nitpicks don't matter here, since "more uniques -> more hidden bugs" remains true. But:  
>
> 1. We assume mostly independent auditors, because of anti-sybil payout formula, and correlation causing underestimation (more duplicates) so is fine.
>
> 2. Doubletons vs. duplicates. Using any duplicates instead of doubletons is easier, but fine since underestimates.
>
> 3. If F2 (doubletons) is zero, Chao 1 as quoted doesn't work, so use something else, like the bias-corrected version.
>
> 4. Severity matters? Possibly, but also maybe not. Complexity (difficulty of finding) and its severity (impact and likelihood) are many times independent.

**Links in post:** https://blog.uvm.edu/tdonovan-vtcfwru/files/2020/06/18-Donov-pages-315-CB.pdf, https://www.uvm.edu/~ngotelli/manuscriptpdfs/Chapter%204.pdf, https://en.wikipedia.org/wiki/Good%E2%80%93Turing_frequency_estimation


### Thread part 3 — @Guhu95 — 2025-06-26 13:25 UTC (2025-06-26 14:25 WAT)

- URL: https://x.com/Guhu95/status/1938227200651878771
- Metrics (at fetch): bookmark 0, impression 527, like 4, quote 0, reply 2, retweet 0

> The industry after @wellbyt3's thread with data on number of solos's per format / platform / pot size / nSLOC ratio? [pic.x.com/0AlRuMc1Cp]

**Media:**
- animated_gif: https://pbs.twimg.com/tweet_video_thumb/GuX3XHMbEAArmLs.jpg — no alt text provided by author


---

## 2025-06-23 · Post · Stared at the code so hard that a 5 year old bug crawled out.


Tags (automatic): Smart contract / DeFi, Platform: Immunefi


### Post — @Guhu95 — 2025-06-23 05:13 UTC (2025-06-23 06:13 WAT)

- URL: https://x.com/Guhu95/status/1937016161847402638
- Metrics (at fetch): bookmark 22, impression 11322, like 223, quote 2, reply 17, retweet 11

> Stared at the code so hard that a 5 year old bug crawled out.
>
> Nothing like finding an attack that hundreds of people missed for years to want to keep hunting. The 60k helps too😎
>
> Plenty of bugs out there, even in simple ol' Solidity.
>
> Thanks to the project and @immunefi!

**Media:**
- photo: https://pbs.twimg.com/media/GuGh277agAA6_C6.png — no alt text provided by author


---

## 2025-06-18 · Post · Audits - pay for guaranteed level of skill and effort


### Post — @Guhu95 — 2025-06-18 08:07 UTC (2025-06-18 09:07 WAT)

- URL: https://x.com/Guhu95/status/1935247936205865371
- Metrics (at fetch): bookmark 5, impression 3556, like 46, quote 0, reply 3, retweet 0

> Audits - pay for guaranteed level of skill and effort
> Contests - pay for many eyes on the code
> Private contest - pay for .. what exactly? [pic.x.com/5p5cnw1isr] https://twitter.com/0xKaden/status/1935012795160166844

**Media:**
- photo: https://pbs.twimg.com/media/GttfCEQWQAAgH4y.jpg — no alt text provided by author

**Links in post:** https://twitter.com/0xKaden/status/1935012795160166844

**Quoted post** 1935012795160166844: not readable via the API (deleted, private, or withheld).


---

## 2025-06-16 · Post · Linea is living in the future: in the one where a 100k bounty is enough to secure 370M of user funds


Tags (automatic): Blockchain / L1-L2 / bridge, ZK


### Post — @Guhu95 — 2025-06-16 07:39 UTC (2025-06-16 08:39 WAT)

- URL: https://x.com/Guhu95/status/1934516179374379177
- Metrics (at fetch): bookmark 6, impression 5210, like 60, quote 1, reply 2, retweet 2

> Linea is living in the future: in the one where a 100k bounty is enough to secure 370M of user funds on a ZK L2 😰
>
> No need for "highs" either: users there don't mind liveness failures or frozen funds for any duration. [pic.x.com/Act1Hb6FEM] https://twitter.com/ethereumJoseph/status/1934449413067509966

**Media:**
- photo: https://pbs.twimg.com/media/GtjDTUFbMAAmWTl.jpg — no alt text provided by author

**Links in post:** https://twitter.com/ethereumJoseph/status/1934449413067509966

**Quoted post** 1934449413067509966: not readable via the API (deleted, private, or withheld).


---

## 2025-06-15 · Post · Tip for POCs in big codebases: use git blame to find the tests to use. It's the closest thing to jus


Tags (automatic): AI-assisted hunting


### Post — @Guhu95 — 2025-06-15 03:02 UTC (2025-06-15 04:02 WAT)

- URL: https://x.com/Guhu95/status/1934084017600774246
- Metrics (at fetch): bookmark 38, impression 3399, like 55, quote 0, reply 3, retweet 2

> Tip for POCs in big codebases: use git blame to find the tests to use. It's the closest thing to just asking the devs.
>
> Can be annoying to find the best test for a POC setup (even with AI) manually. Instead, blame on the buggy line -&gt; check the commit / PR, and it will often have [pic.x.com/mUwWAAZvNT]

**Media:**
- photo: https://pbs.twimg.com/media/Gtc7CqSbUAAVVS5.jpg — no alt text provided by author


---

## 2025-06-12 · Post · Reading new contracts [pic.x.com/cykZuKrVgj]


### Post — @Guhu95 — 2025-06-12 07:52 UTC (2025-06-12 08:52 WAT)

- URL: https://x.com/Guhu95/status/1933069985938878782
- Metrics (at fetch): bookmark 1, impression 2854, like 44, quote 1, reply 3, retweet 2

> Reading new contracts [pic.x.com/cykZuKrVgj]

**Media:**
- photo: https://pbs.twimg.com/media/GtOkQkIbMAEE892.jpg — no alt text provided by author


---

## 2025-06-07 · Post · The whole thread is great, but this insight is my favorite.


### Post — @Guhu95 — 2025-06-07 13:09 UTC (2025-06-07 14:09 WAT)

- URL: https://x.com/Guhu95/status/1931337623492063667
- Metrics (at fetch): bookmark 0, impression 611, like 3, quote 0, reply 0, retweet 0

> The whole thread is great, but this insight is my favorite.
>
> It's also why perps dexes keep rising and dying.
>
> Each incumbent is killed by new ones, eager to lose more money (LP or incentives) in order to grow. Reflexivity of liquidity does the rest, and a new incumbent is born. https://twitter.com/danielvf/status/1931071800609255471

**Links in post:** https://twitter.com/danielvf/status/1931071800609255471

**Quoted post** 1931071800609255471: not readable via the API (deleted, private, or withheld).


---

## 2025-06-05 · Post · Wild payouts for the winners for an absolute masterclass - finding highs in a huge, shifting scope; 


Tags (automatic): Platform: Code4rena / Sherlock / Cantina


### Post — @Guhu95 — 2025-06-05 05:22 UTC (2025-06-05 06:22 WAT)

- URL: https://x.com/Guhu95/status/1930495367554138246
- Metrics (at fetch): bookmark 3, impression 3579, like 58, quote 0, reply 4, retweet 0

> Wild payouts for the winners for an absolute masterclass - finding highs in a huge, shifting scope; very strong code; so many languages; with the time pressure of "no dups"... Epic performance. 
>
> Surprisingly, while it felt like everyone was participating, only 13 people on the https://twitter.com/cantinaxyz/status/1930250893175468142

**Links in post:** https://twitter.com/cantinaxyz/status/1930250893175468142

**Quoted post** 1930250893175468142: not readable via the API (deleted, private, or withheld).


---

## 2025-05-29 · Post · The "dark side" only wins if there are bugs to exploit.


### Post — @Guhu95 — 2025-05-29 02:39 UTC (2025-05-29 03:39 WAT)

- URL: https://x.com/Guhu95/status/1927917784887185575
- Metrics (at fetch): bookmark 1, impression 2306, like 15, quote 0, reply 1, retweet 1

> The "dark side" only wins if there are bugs to exploit.
>
> If there are no bugs, the sides don't matter.
>
> This is what crypto is about. Systems for enemies.
>
> Also, the "dark side" label is delusional, it's a "fundamental attribution error". If you were in their circumstances https://twitter.com/lonelysloth_sec/status/1927778954565255181

**Links in post:** https://twitter.com/lonelysloth_sec/status/1927778954565255181

**Quoted post** 1927778954565255181: not readable via the API (deleted, private, or withheld).
