# @Guhu95 — full verbatim X archive (security-relevant posts)

_Generated 2026-11-19 from the X API (full-archive search + timeline). Every post below is copied word-for-word; t.co links are expanded; quoted posts are inlined in full; media are listed with alt text when the author provided it. Posts are grouped by conversation (a thread = the author's root post followed by their own replies, oldest first). Groups are newest first. An agent without X access can rely on this file._

- Posts in this file: 75
- Conversations/threads: 63
- Oldest post captured: 2023-08-19
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
    
    **Quoted post (full text):**
    
        #### Quoted post — @Guhu95 — 2025-03-25 02:30 UTC (2025-03-25 03:30 WAT)
        
        - URL: https://x.com/Guhu95/status/1904360201597387131
        - Metrics (at fetch): bookmark 7, impression 11285, like 47, quote 2, reply 5, retweet 0
        
        > Some Pectra contest thoughts:
        >
        > The Good:
        > - Client diversity is an ETH superpower. Always liked it, but now 10x more.
        > - Testing sophistication is unbelievable. Beyond each client's tests, and the testnets, there are independent external tests (in python), a tool to run devnets https://t.co/Vyw5DtmBCS
        
        **Media:**
        - animated_gif:  — no alt text provided by author
        
    


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

**Quoted post (full text):**

    #### Quoted post — @Guhu95 — 2025-03-25 02:30 UTC (2025-03-25 03:30 WAT)
    
    - URL: https://x.com/Guhu95/status/1904360201597387131
    - Metrics (at fetch): bookmark 7, impression 11285, like 47, quote 2, reply 5, retweet 0
    
    > Some Pectra contest thoughts:
    >
    > The Good:
    > - Client diversity is an ETH superpower. Always liked it, but now 10x more.
    > - Testing sophistication is unbelievable. Beyond each client's tests, and the testnets, there are independent external tests (in python), a tool to run devnets https://t.co/Vyw5DtmBCS
    
    **Media:**
    - animated_gif:  — no alt text provided by author
    


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


---

## 2025-05-09 · Thread · "Stack too deep" makes you write better code. "Code is read more than it's written", especially Soli


Tags (automatic): Smart contract / DeFi


### Post — @Guhu95 — 2025-05-09 07:14 UTC (2025-05-09 08:14 WAT)

- URL: https://x.com/Guhu95/status/1920739091215511905
- Metrics (at fetch): bookmark 2, impression 2572, like 34, quote 0, reply 5, retweet 1

> "Stack too deep" makes you write better code. "Code is read more than it's written", especially Solidity. 
>
> Yes it's annoying, but you know what's more annoying? Error-prone ugly spaghetti code with too many variables used in the same scope.
>
> Humans barely handle 4 items in [pic.x.com/0yrF9cVPE2]

**Media:**
- photo: https://pbs.twimg.com/media/GqfV4O2WgAAEct9.jpg — no alt text provided by author


### Thread part 2 — @Guhu95 — 2025-05-09 07:15 UTC (2025-05-09 08:15 WAT)

- URL: https://x.com/Guhu95/status/1920739502244397134
- Metrics (at fetch): bookmark 1, impression 377, like 1, quote 0, reply 0, retweet 0

> [1] - https://t.co/InAgWRIUVz


---

## 2025-05-01 · Thread · Audit contests are just a spectator sport. That's the only sane way to treat them. Proof:


### Post — @Guhu95 — 2025-05-01 06:05 UTC (2025-05-01 07:05 WAT)

- URL: https://x.com/Guhu95/status/1917822712984265045
- Metrics (at fetch): bookmark 7, impression 3474, like 61, quote 0, reply 6, retweet 0

> Audit contests are just a spectator sport. That's the only sane way to treat them. Proof:
>
> - Endless drama all the time.
> - Top 0.1% are worshiped as demigods.
> - Top 1% make more money from selling other stuff (audit days).
> - Bottom 99% are there because of top 0.1%'s winnings.
> - https://t.co/7LjPpRdsqh

**Media:**
- animated_gif:  — no alt text provided by author


### Thread part 2 — @Guhu95 — 2025-05-01 08:51 UTC (2025-05-01 09:51 WAT)

- URL: https://x.com/Guhu95/status/1917864472418615520
- Metrics (at fetch): bookmark 0, impression 622, like 10, quote 0, reply 0, retweet 0

> To clarify: this is not me complaining, venting, or being negative.
>
> I'm suggesting a mental model I find more helpful, and pointing out similarities. 
>
> Contests are great, here to stay, people are doing their best, and as a whole provide a lot of value for literally everyone. I


---

## 2025-03-25 · Post · Some Pectra contest thoughts:


### Post — @Guhu95 — 2025-03-25 02:30 UTC (2025-03-25 03:30 WAT)

- URL: https://x.com/Guhu95/status/1904360201597387131
- Metrics (at fetch): bookmark 7, impression 11285, like 47, quote 2, reply 5, retweet 0

> Some Pectra contest thoughts:
>
> The Good:
> - Client diversity is an ETH superpower. Always liked it, but now 10x more.
> - Testing sophistication is unbelievable. Beyond each client's tests, and the testnets, there are independent external tests (in python), a tool to run devnets https://t.co/Vyw5DtmBCS

**Media:**
- animated_gif:  — no alt text provided by author


---

## 2024-12-01 · Post · Whoa. @immunefi showing the way!


Tags (automatic): Platform: Immunefi


### Post — @Guhu95 — 2024-12-01 01:48 UTC (2024-12-01 02:48 WAT)

- URL: https://x.com/Guhu95/status/1863037506910146579
- Metrics (at fetch): bookmark 0, impression 4770, like 49, quote 2, reply 1, retweet 3

> Whoa. @immunefi showing the way!
>
> 🏆 Record broken: first platform to advertize pot ranges for conditionals.
>
> Because good marketing fosters trust, and not just FOMO. https://t.co/37m3hWTKvO https://t.co/yVPuvcdDQ8

**Media:**
- animated_gif:  — no alt text provided by author

**Quoted post (full text):**

    #### Quoted post — @immunefi — 2024-11-29 20:35 UTC (2024-11-29 21:35 WAT)
    
    - URL: https://x.com/immunefi/status/1862596294986092595
    - Metrics (at fetch): bookmark 5, impression 6755, like 37, quote 2, reply 2, retweet 7
    
    > 💰 $1.81 Million in rewards available - Where will you be hunting?
    > (🔗 scope details &amp; links below) https://t.co/aFC8pTfjti
    
    **Media:**
    - media `3_1862593556256292866` (details not returned by the API)
    


---

## 2024-11-28 · Post · How conditionals are going. An update. 


### Post — @Guhu95 — 2024-11-28 06:33 UTC (2024-11-28 07:33 WAT)

- URL: https://x.com/Guhu95/status/1862021970256379908
- Metrics (at fetch): bookmark 55, impression 39586, like 236, quote 15, reply 20, retweet 21

> How conditionals are going. An update. 
>
> This is mostly a warning for future participants. Know what to expect, and adjust your EV calc. Below are several case studies and "records".
>
> ### 1. Uniswap
> - Hyped up as largest ever contest of 2.35M, paid only 12% of the hype (300k)
> - https://t.co/ugZ57P9Tqn https://t.co/sWMMYBjkU0

**Media:**
- animated_gif:  — no alt text provided by author

**Quoted post (full text):**

    #### Quoted post — @Guhu95 — 2024-07-04 13:27 UTC (2024-07-04 14:27 WAT)
    
    - URL: https://x.com/Guhu95/status/1808855240449667162
    - Metrics (at fetch): bookmark 49, impression 57634, like 122, quote 4, reply 18, retweet 7
    
    > [High] Conditional contest pots are bad and stupid. 
    >
    > Problem is that skilled participation is low because of low EV.
    >
    > ## POC - Euler at @cantinaxyz
    >
    > 1. A lot of prior audits, with few findings. Even 50% of no new high means the contest EV is now 670K instead of 1.15M. But wait.. https://t.co/y927YpIo3s
    
    **Quoted post (full text):**
    
        #### Quoted post — @1622629804791955458 — 2024-03-21 15:02 UTC (2024-03-21 16:02 WAT)
        
        - URL: https://x.com/1622629804791955458/status/1770828360471507068
        - Metrics (at fetch): bookmark 60, impression 157785, like 288, quote 154, reply 91, repost 134
        
        > Welcome... to the new largest competition in history with @eulerfinance!
        >
        > 💰 $1,250,000 USDC
        > 🗓️ May 20th - June 17th
        > 📍 @cantinaxyz 
        >
        > Invite only. Don't have one? Details below: [pic.x.com/M1MtDE7XKj]
        
        **Media:**
        - animated_gif: https://pbs.twimg.com/tweet_video_thumb/GJM-xJIXEAAKrdp.jpg — no alt text provided by author
        
    


---

## 2024-11-13 · Post · I propose that anyone should be able to retract their report from @immunefi in exchange for forfeiti


Tags (automatic): Platform: Immunefi


### Post — @Guhu95 — 2024-11-13 00:02 UTC (2024-11-13 01:02 WAT)

- URL: https://x.com/Guhu95/status/1856487726402658369
- Metrics (at fetch): bookmark 4, impression 5576, like 56, quote 1, reply 4, retweet 1

> I propose that anyone should be able to retract their report from @immunefi in exchange for forfeiting their proposed bounty. 
>
> It makes 0 sense for the industry or Immunefi that someone (and his intellectual property) can be "hushed" forever by a "closed report". 
>
> If you force https://t.co/qia4ZIth9T

**Quoted post (full text):**

    #### Quoted post — @TrustSecAudits — 2024-11-12 15:22 UTC (2024-11-12 16:22 WAT)
    
    - URL: https://x.com/TrustSecAudits/status/1856356982766063847
    - Metrics (at fetch): bookmark 57, impression 47845, like 287, quote 6, reply 21, retweet 50
    
    > Recently the bounty team at TrustSec found another critical leading to live unauthenticated theft of funds. Due to what we consider malicious behavior of the project and especially of @immunefi , not only did the project get away without paying the bounty, but due to a dirty
    


---

## 2024-10-22 · Thread · Main root cause to fix is not 3 signers IMO.


### Post — @Guhu95 — 2024-10-22 03:18 UTC (2024-10-22 04:18 WAT)

- URL: https://x.com/Guhu95/status/1848564637337588056
- Metrics (at fetch): bookmark 4, impression 3208, like 6, quote 0, reply 4, retweet 0

> Main root cause to fix is not 3 signers IMO.
>
> It is instead Safe's default design of allowing anyone to call execTransaction.
>
> This is why attackers could collect sigs undetected for maybe weeks, and then submitted them all at once only when they had enough.
>
> Yes, 3 signers is https://t.co/vbxBMJt9D4

**Quoted post (full text):**

    #### Quoted post — @5678 — 2024-10-17 21:15 UTC (2024-10-17 22:15 WAT)
    
    - URL: https://x.com/5678/status/1847023591117795708
    - Metrics (at fetch): bookmark 714, impression 764458, like 1304, quote 179, reply 97, retweet 289
    
    > Yesterday's sophisticated 50 million Radiant Capital hack happened after attacker's trojaned the computers of multiple team members.
    >
    > Team members saw and verified good multisig data on screens, but their hardware wallets signed evil data. 1/7 https://t.co/zE7Hk0zN22
    
    **Media:**
    - media `3_1847023472100208640` (details not returned by the API)
    


### Thread part 2 — @Guhu95 — 2024-10-22 12:24 UTC (2024-10-22 13:24 WAT)

- URL: https://x.com/Guhu95/status/1848701900948181005
- Metrics (at fetch): bookmark 0, impression 82, like 0, quote 0, reply 0, retweet 0

> I think step 4 is both hard and unlikely. 
>
> If one of the non-compromised signers added a sig to the non-evil nonce, now the evil-nonce is behind. But hijacking an exec can only be done when both nonces are ready to execute. So the attackers (or their now very smart malware) have to sit there, watch the safe, and wait for these conditions.
>
> The malware (or the attacker's bot controlling it) needs to not only upload and download sigs (as nonces advance), talk to the RPC (to check nonces), talk to Safe API (to check on non-evil sigs progress). It's a full on bridging protocol at this point.
>
> Also, the malware needs to trick the executor to sign an evil 712 - which doesn't show in Safe UI, then have them sign the good 712, and send it to Safe API, and only then wait for them to exec.


---

## 2024-09-06 · Post · Audits for Uni V4 published: https://t.co/W5jQL5CH70 :


### Post — @Guhu95 — 2024-09-06 06:37 UTC (2024-09-06 07:37 WAT)

- URL: https://x.com/Guhu95/status/1831944784203935970
- Metrics (at fetch): bookmark 19, impression 4262, like 30, quote 0, reply 1, retweet 1

> Audits for Uni V4 published: https://t.co/W5jQL5CH70 :
>
> - ABDK with a lot of nice assembly findings and this slapper from a clearly unimpressed auditor: "Such technic looks like a dirty hack." 
>
> - OZ with a neat Critical for some weird chains.
>
> - Formal verification found one https://t.co/uu0LomC1n1

**Quoted post (full text):**

    #### Quoted post — @1622629804791955458 — 2024-08-22 14:01 UTC (2024-08-22 15:01 WAT)
    
    - URL: https://x.com/1622629804791955458/status/1826620693657858173
    - Metrics (at fetch): bookmark 9, impression 57744, like 57, quote 9, reply 7, retweet 9
    
    > ATTENTION: ​Calling all Security Researchers 🪐
    >
    > Cantina, @Uniswap, and @UniswapFND will be hosting a HackerHouse for the massive $2.35M Uniswap v4 competition on @cantinaxyz.
    >
    > Full access to Uniswap's team. All meals provided. No costs. Just show up.
    >
    > Seats Limited. RSVP Below: https://t.co/hWiqDlSr0v
    
    **Media:**
    - media `3_1826620688905764869` (details not returned by the API)
    


---

## 2024-08-26 · Thread · Say NO to EOF. It is a shit-tornado that will cripple ETH and the EVM ecosystem.


Tags (automatic): Blockchain / L1-L2 / bridge, AI-assisted hunting


### Post — @Guhu95 — 2024-08-26 02:01 UTC (2024-08-26 03:01 WAT)

- URL: https://x.com/Guhu95/status/1827889143386460488
- Metrics (at fetch): bookmark 5, impression 1627, like 10, quote 1, reply 2, retweet 0

> Say NO to EOF. It is a shit-tornado that will cripple ETH and the EVM ecosystem.
>
> Short version
> - Look at this hideous monstrosity https://t.co/FyNzdsy4tk! Imagine having to develop and audit on that minefield.
> - Who the F thinks that having two EVMs on the same chain is a good https://t.co/LlMqzEkD3H

**Media:**
- animated_gif:  — no alt text provided by author


### Thread part 2 — @Guhu95 — 2024-08-26 02:05 UTC (2024-08-26 03:05 WAT)

- URL: https://x.com/Guhu95/status/1827890073968288110
- Metrics (at fetch): bookmark 0, impression 484, like 3, quote 0, reply 1, retweet 0

> Don't listen to me, listen to some devs: 
>
> https://t.co/fca1gEvWdy

**Quoted post (full text):**

    #### Quoted post — @1496567813737091075 — 2024-08-17 21:25 UTC (2024-08-17 22:25 WAT)
    
    - URL: https://x.com/1496567813737091075/status/1824920618795692125
    - Metrics (at fetch): bookmark 30, impression 44045, like 139, quote 5, reply 8, retweet 10
    
    > EOF will be like migrating from x86 to ARM. Solidity libraries and ERC standards will break. This is not like Paris -&gt; Shanghai (PUSH0 is child’s play compared to EOF).
    >
    > I hope the dev tooling teams (Foundry, Solidity) won’t immediately make the default EVM as EOF, but add it as
    


---

## 2024-08-08 · Post · An alternative model to contests. For contest platforms @sockdrawermoney @cantinaxyz @0xMackenzieM @


Tags (automatic): Platform: Code4rena / Sherlock / Cantina


### Post — @Guhu95 — 2024-08-08 01:56 UTC (2024-08-08 02:56 WAT)

- URL: https://x.com/Guhu95/status/1821364761252040903
- Metrics (at fetch): bookmark 8, impression 5033, like 9, quote 0, reply 4, retweet 2

> An alternative model to contests. For contest platforms @sockdrawermoney @cantinaxyz @0xMackenzieM @sherlockdefi 
>
> Problems with contests: Some bad for projects due to low participation. Some bad for SRs due to over crowding. Projects and SRs are worried and unhappy. Judging is https://t.co/dI0k6wSlG0

**Quoted post (full text):**

    #### Quoted post — @736235680603492352 — 2024-07-30 12:53 UTC (2024-07-30 13:53 WAT)
    
    - URL: https://x.com/736235680603492352/status/1818268760257474985
    - Metrics (at fetch): bookmark 22, impression 17639, like 70, quote 4, reply 18, retweet 6
    
    > I'm currently facing one of our biggest dilemma yet (bcoz in startups, treasury &gt;&gt; all problems).
    >
    > Context: There'll be a competitive audit in 2024 (yet to be announced) for @KakarotZkEvm 's core EVM implementation.
    > We're extremely ambitious in wanting to prove all EVM execution, https://t.co/OLLbvXiAfN
    
    **Quoted post (full text):**
    
        #### Quoted post — @Guhu95 — 2024-07-04 13:27 UTC (2024-07-04 14:27 WAT)
        
        - URL: https://x.com/Guhu95/status/1808855240449667162
        - Metrics (at fetch): bookmark 49, impression 57634, like 122, quote 4, reply 18, retweet 7
        
        > [High] Conditional contest pots are bad and stupid. 
        >
        > Problem is that skilled participation is low because of low EV.
        >
        > ## POC - Euler at @cantinaxyz
        >
        > 1. A lot of prior audits, with few findings. Even 50% of no new high means the contest EV is now 670K instead of 1.15M. But wait.. https://t.co/y927YpIo3s
        
        **Quoted post (full text):**
        
            #### Quoted post — @1622629804791955458 — 2024-03-21 15:02 UTC (2024-03-21 16:02 WAT)
            
            - URL: https://x.com/1622629804791955458/status/1770828360471507068
            - Metrics (at fetch): bookmark 60, impression 157785, like 288, quote 154, reply 91, repost 134
            
            > Welcome... to the new largest competition in history with @eulerfinance!
            >
            > 💰 $1,250,000 USDC
            > 🗓️ May 20th - June 17th
            > 📍 @cantinaxyz 
            >
            > Invite only. Don't have one? Details below: [pic.x.com/M1MtDE7XKj]
            
            **Media:**
            - animated_gif: https://pbs.twimg.com/tweet_video_thumb/GJM-xJIXEAAKrdp.jpg — no alt text provided by author
            
        
    


---

## 2024-07-04 · Thread · [High] Conditional contest pots are bad and stupid. 


Tags (automatic): Platform: Code4rena / Sherlock / Cantina


### Post — @Guhu95 — 2024-07-04 13:27 UTC (2024-07-04 14:27 WAT)

- URL: https://x.com/Guhu95/status/1808855240449667162
- Metrics (at fetch): bookmark 49, impression 57634, like 122, quote 4, reply 18, retweet 7

> [High] Conditional contest pots are bad and stupid. 
>
> Problem is that skilled participation is low because of low EV.
>
> ## POC - Euler at @cantinaxyz
>
> 1. A lot of prior audits, with few findings. Even 50% of no new high means the contest EV is now 670K instead of 1.15M. But wait.. https://t.co/y927YpIo3s

**Quoted post (full text):**

    #### Quoted post — @1622629804791955458 — 2024-03-21 15:02 UTC (2024-03-21 16:02 WAT)
    
    - URL: https://x.com/1622629804791955458/status/1770828360471507068
    - Metrics (at fetch): bookmark 60, impression 157785, like 288, quote 154, reply 91, repost 134
    
    > Welcome... to the new largest competition in history with @eulerfinance!
    >
    > 💰 $1,250,000 USDC
    > 🗓️ May 20th - June 17th
    > 📍 @cantinaxyz 
    >
    > Invite only. Don't have one? Details below: [pic.x.com/M1MtDE7XKj]
    
    **Media:**
    - animated_gif: https://pbs.twimg.com/tweet_video_thumb/GJM-xJIXEAAKrdp.jpg — no alt text provided by author
    


### Thread part 2 — @Guhu95 — 2024-07-04 13:35 UTC (2024-07-04 14:35 WAT)

- URL: https://x.com/Guhu95/status/1808857211034349794
- Metrics (at fetch): bookmark 0, impression 2084, like 3, quote 0, reply 0, retweet 0

> @cantinaxyz My follow up on this note @0xMackenzieM 
>
> BTW I think "gradual conditional" like with Fuel, is somewhat better by "smoothing" the EV. 
>
> But it's not the Chad way, and has many of the same issues as the "binary" conditional.
>
> https://x.com/0xMackenzieM/status/1798795067714314268

**Links in post:** https://x.com/0xMackenzieM/status/1798795067714314268


### Thread part 3 — @Guhu95 — 2024-07-04 23:46 UTC (2024-07-05 00:46 WAT)

- URL: https://x.com/Guhu95/status/1809010913951002914
- Metrics (at fetch): bookmark 2, impression 1569, like 5, quote 2, reply 3, retweet 0

> > Projects want to maximize upside while minimizing risk
>
> I agree that project want to minimize risk for money. The problem is that this model is doing the opposite.
>
> The value for an audit is not in the bugs FOUND, but it's in the bugs NOT MISSED. Since no one knows how many there are initially, you cannot know how many SHOULD be found.
>
> The only thing a project can pay for is for people to LOOK long and hard. In trad audits it's via reputation based, in contest it's pot based. The higher the pot, the more skilled effort you get competing for it. 
>
> A simple way to think about potential improvements:
>
> You want winnie to hunt? There's just one winnie - so you gotta outbid everyone and everything else for his time - really simple. You didn't outbid? Winnie's bug may still be there. Rekt.
>
> What's worse, is that the better the codebase, the more a conditional pot reduces the effective pot! For good codebases, the model works the WORST. 
>
> > I'm not convinced either way that a $500k flat pot outperforms a $1mil
>
> Very good chance the project pays 1M but get's way less than 500K worth of value anyway. The very opposite of what they want. 
>
> > 0. Reliable judging. The eternal issue.
>
> Not gonna happen soon. Judging needs to become MUCH more expensive, independent, and standardized for it to be credibly neutral and reliable.
>
> > if only Low/Med are found the pot should still be ~50% of the max pot.
>
> That's an improvement. But the reason that works better is the same reason a flat pot will work even better. But it could be a step that helps projects adapt to the right way of thinking.
>
> > we frame conditional pots as a way to INCREASE your rewards, not a way to minimize them
>
> It matters little how YOU frame it, what matters is how the best-paid SRs perceive them. If they perceive them as low EV - they do something else instead and the bugs remain there for the blackhats to find (when TVL - their EV - is high enough).


### Thread part 4 — @Guhu95 — 2024-07-30 23:18 UTC (2024-07-31 00:18 WAT)

- URL: https://x.com/Guhu95/status/1818425938969083985
- Metrics (at fetch): bookmark 0, impression 291, like 0, quote 0, reply 1, retweet 0

> @lonelysloth_sec @0xMackenzieM @cantinaxyz You can sell due diligence info to investment funds, in exchange for locked compensation conditional on no crits.


### Thread part 5 — @Guhu95 — 2024-07-31 03:25 UTC (2024-07-31 04:25 WAT)

- URL: https://x.com/Guhu95/status/1818488251730264145
- Metrics (at fetch): bookmark 0, impression 136, like 0, quote 0, reply 0, retweet 0

> @lonelysloth_sec @0xMackenzieM @cantinaxyz I mean it's a service you (or other bug hunters) could offer.
>
> It's basically p2p prediction market: 
>
> - the LP (funds, investors, community) trust your bet on your reputation in exchange for their money. 
>
> - you exchange your privileged information for their money.


---

## 2024-07-16 · Post · What technical work pays best in crypto? Maker's budget's take:


Tags (automatic): AI-assisted hunting


### Post — @Guhu95 — 2024-07-16 00:22 UTC (2024-07-16 01:22 WAT)

- URL: https://x.com/Guhu95/status/1813006165510660611
- Metrics (at fetch): bookmark 10, impression 6405, like 34, quote 0, reply 2, retweet 1

> What technical work pays best in crypto? Maker's budget's take:
>
> 1. Protocol dev: 9M
>
> 2. Front-end dev: 5M
>
> 3. Audits: 1.7M
>
> 4. Bug bounty: 90K 😬
>
> But also .. AI: 740K 🙈 https://t.co/kjOkm75HEf

**Quoted post (full text):**

    #### Quoted post — @1373304198448709632 — 2024-07-15 19:54 UTC (2024-07-15 20:54 WAT)
    
    - URL: https://x.com/1373304198448709632/status/1812938853835313461
    - Metrics (at fetch): bookmark 56, impression 32115, like 208, quote 3, reply 21, retweet 11
    
    > breakdown of the 41m costs maker spent in operations over the last year https://t.co/3r2ggZvoQJ
    
    **Media:**
    - media `3_1812938545931120641` (details not returned by the API)
    


---

## 2024-06-07 · Thread · Security platforms as chains (a 💩-post):


Tags (automatic): Platform: Code4rena / Sherlock / Cantina


### Post — @Guhu95 — 2024-06-07 03:03 UTC (2024-06-07 04:03 WAT)

- URL: https://x.com/Guhu95/status/1798913703540396406
- Metrics (at fetch): bookmark 11, impression 6226, like 50, quote 1, reply 3, retweet 1

> Security platforms as chains (a 💩-post):
>
> @code4rena  = ETH: the benchmark, forked a lot, early mover advantage, idealistic and open, congested, complex, dark forest, just hums along generating huge value.
>
> @sherlockdefi  = BSC: an old fork, pretty centralized, too many hacks to https://t.co/KIec4eUMXa https://t.co/SKPjAsMQW7

**Media:**
- animated_gif:  — no alt text provided by author

**Quoted post (full text):**

    #### Quoted post — @1357162894798909441 — 2024-06-06 09:08 UTC (2024-06-06 10:08 WAT)
    
    - URL: https://x.com/1357162894798909441/status/1798643063172313554
    - Metrics (at fetch): bookmark 39, impression 24388, like 94, quote 8, reply 6, retweet 8
    
    > @TheWavexyz @0xMackenzieM @0xnirlin @jack__sanford I’d prefer not to spend any energy debating this as I see no merit in it and the extremely narrow audience can make up their own minds, but I can fast forward it.
    >
    > I can point to evidence that LSW alters competition incentives without even  guaranteeing meaningful participation;
    


### Thread part 2 — @Guhu95 — 2024-06-07 03:51 UTC (2024-06-07 04:51 WAT)

- URL: https://x.com/Guhu95/status/1798925767273009249
- Metrics (at fetch): bookmark 0, impression 874, like 13, quote 0, reply 0, retweet 0

> @code4rena @sherlockdefi Points being:
> - it's all the same trade-offs everywhere
> - everyone has a lot to improve
> - arguing about it is fun, and important, and what we do for a living


---

## 2024-06-06 · Post · Some takeaways from the Blast contest: 


Tags (automatic): Smart contract / DeFi


### Post — @Guhu95 — 2024-06-06 02:06 UTC (2024-06-06 03:06 WAT)

- URL: https://x.com/Guhu95/status/1798537026620510717
- Metrics (at fetch): bookmark 37, impression 7825, like 86, quote 2, reply 12, retweet 1

> Some takeaways from the Blast contest: 
>
> 1. "No edge" is ok. Had no prior edge in: Geth, Bedrock, Lido, Maker, or even contests in general. 
>
> 2. Large scope is ok. Scope was 4.5K solidity, 1.5K go - too much for 3 weeks. Somehow managed to go through it, though it didn't seem https://t.co/mptx6ufxZ7

**Quoted post (full text):**

    #### Quoted post — @Guhu95 — 2024-06-05 05:44 UTC (2024-06-05 06:44 WAT)
    
    - URL: https://x.com/Guhu95/status/1798229348719431805
    - Metrics (at fetch): bookmark 4, impression 13249, like 67, quote 2, reply 6, retweet 0
    
    > Very happy to rank 2nd in such a huge contest. Have learned a ton, and will share some takeaways later.
    >
    > Thanks @Blast_L2  and @cantinaxyz  for taking audit contests to a new level 🙌 https://t.co/sCvN4gYwLs https://t.co/z14KPZ9PET
    
    **Media:**
    - photo: https://pbs.twimg.com/media/GPSWL4TakAAbuH_.jpg — no alt text provided by author
    
    **Quoted post (full text):**
    
        #### Quoted post — @1622629804791955458 — 2024-06-04 23:32 UTC (2024-06-05 00:32 WAT)
        
        - URL: https://x.com/1622629804791955458/status/1798135858048233802
        - Metrics (at fetch): bookmark 13, impression 56669, like 110, quote 13, reply 7, retweet 9
        
        > It's official. 🚀🪐
        >
        > The results are in for our massive $1.2M @Blast_l2 security competition:
        >
        > Here are your top 3 ranked researchers:
        > 🥇 @zachobront: $201,484.57
        > 🥈 @Guhu95: $119,941.96
        > 🥉 @tinchoabbate  &amp; @saucecri ( @theredguild ): $74,729.62
        >
        > Amazing work. Leaderboard below: https://t.co/xgcTHm5vQq
        
        **Media:**
        - media `3_1798135847650570240` (details not returned by the API)
        
    


---

## 2024-06-05 · Post · Very happy to rank 2nd in such a huge contest. Have learned a ton, and will share some takeaways lat


Tags (automatic): Platform: Code4rena / Sherlock / Cantina


### Post — @Guhu95 — 2024-06-05 05:44 UTC (2024-06-05 06:44 WAT)

- URL: https://x.com/Guhu95/status/1798229348719431805
- Metrics (at fetch): bookmark 4, impression 13249, like 67, quote 2, reply 6, retweet 0

> Very happy to rank 2nd in such a huge contest. Have learned a ton, and will share some takeaways later.
>
> Thanks @Blast_L2  and @cantinaxyz  for taking audit contests to a new level 🙌 https://t.co/sCvN4gYwLs https://t.co/z14KPZ9PET

**Media:**
- photo: https://pbs.twimg.com/media/GPSWL4TakAAbuH_.jpg — no alt text provided by author

**Quoted post (full text):**

    #### Quoted post — @1622629804791955458 — 2024-06-04 23:32 UTC (2024-06-05 00:32 WAT)
    
    - URL: https://x.com/1622629804791955458/status/1798135858048233802
    - Metrics (at fetch): bookmark 13, impression 56669, like 110, quote 13, reply 7, retweet 9
    
    > It's official. 🚀🪐
    >
    > The results are in for our massive $1.2M @Blast_l2 security competition:
    >
    > Here are your top 3 ranked researchers:
    > 🥇 @zachobront: $201,484.57
    > 🥈 @Guhu95: $119,941.96
    > 🥉 @tinchoabbate  &amp; @saucecri ( @theredguild ): $74,729.62
    >
    > Amazing work. Leaderboard below: https://t.co/xgcTHm5vQq
    
    **Media:**
    - media `3_1798135847650570240` (details not returned by the API)
    


---

## 2024-04-27 · Post · Sometimes EIP &gt; POC when validating bugs.


### Post — @Guhu95 — 2024-04-27 00:32 UTC (2024-04-27 01:32 WAT)

- URL: https://x.com/Guhu95/status/1784017738526314718
- Metrics (at fetch): bookmark 13, impression 1350, like 8, quote 0, reply 0, retweet 1

> Sometimes EIP &gt; POC when validating bugs.
>
> With create/create2 forge will not check creation (EIP-3860) or runtime (EIP-170) code size limits. This can make an invalid bug seem valid.
>
> TL;DR of the limits: EIP-170 - the constructor will revert for runtime code &gt; 24576 bytes, and https://t.co/CmiLPFBZFr

**Quoted post (full text):**

    #### Quoted post — @1496567813737091075 — 2024-04-26 21:44 UTC (2024-04-26 22:44 WAT)
    
    - URL: https://x.com/1496567813737091075/status/1783975395735523423
    - Metrics (at fetch): bookmark 3, impression 5297, like 47, quote 0, reply 5, retweet 2
    
    > Snippet from LibClone.
    >
    > Designed for long term safety. Our plans are measured in centuries.
    >
    > Yes, we have the spurious dragon limit today, but what if some le-wild researcher makes a graphene breakthrough and it becomes feasible to remove the spurious dragon limit? https://t.co/1WbfBr9FFN
    
    **Media:**
    - media `3_1783974895048900608` (details not returned by the API)
    


---

## 2024-04-03 · Post · This bug and writeup are a thing of beauty. https://t.co/xHXVhzTU0V


### Post — @Guhu95 — 2024-04-03 22:56 UTC (2024-04-03 23:56 WAT)

- URL: https://x.com/Guhu95/status/1775658788043071663
- Metrics (at fetch): bookmark 1, impression 930, like 5, quote 0, reply 0, retweet 1

> This bug and writeup are a thing of beauty. https://t.co/xHXVhzTU0V

**Quoted post (full text):**

    #### Quoted post — @933421614217220096 — 2024-04-03 14:39 UTC (2024-04-03 15:39 WAT)
    
    - URL: https://x.com/933421614217220096/status/1775533657505300922
    - Metrics (at fetch): bookmark 40, impression 28887, like 122, quote 12, reply 2, retweet 14
    
    > Prior to the Dencun upgrade, we disclosed a bug to the @ethereum Foundation that could remotely crash Ethereum mainnet geth clients over RPC through eth_call. All major RPC providers were affected, incl. @infura_io, @AlchemyPlatform, @ankr, @QuickNode, and others👇
    


---

## 2024-03-11 · Post · Raft exploit is a recent example of a info/low that turned out to be a critical. 


### Post — @Guhu95 — 2024-03-11 04:44 UTC (2024-03-11 05:44 WAT)

- URL: https://x.com/Guhu95/status/1767048930242789459
- Metrics (at fetch): bookmark 2, impression 1026, like 3, quote 1, reply 0, retweet 0

> Raft exploit is a recent example of a info/low that turned out to be a critical. 
>
> An audit (contest or not) should try to find all bugs.
>
> https://t.co/TvHDyOIii5 https://t.co/4qKpPHFY3r

**Quoted post (full text):**

    #### Quoted post — @1357162894798909441 — 2024-03-10 11:17 UTC (2024-03-10 12:17 WAT)
    
    - URL: https://x.com/1357162894798909441/status/1766785348552790054
    - Metrics (at fetch): bookmark 9, impression 15507, like 62, quote 4, reply 2, retweet 5
    
    > This is 100% why @code4rena didn’t drop lows even after competitors created marketing narrative that they only focus on serious issues.
    >
    > Not allowing low-severity issues in a competitive audit is a convenience to the platform, NOT an improvement of security outcomes for customers https://t.co/KIDNkIptiG
    
    **Quoted post** 1766744640865116512: not readable via the API (deleted, private, or withheld).
    


---

## 2024-03-07 · Post · Apparently, for 2023 I ended up at 22. Would have no idea without this upgrade, thanks @immunefi!


Tags (automatic): Platform: Immunefi


### Post — @Guhu95 — 2024-03-07 03:49 UTC (2024-03-07 04:49 WAT)

- URL: https://x.com/Guhu95/status/1765585507952844815
- Metrics (at fetch): bookmark 3, impression 7915, like 40, quote 0, reply 0, retweet 3

> Apparently, for 2023 I ended up at #22. Would have no idea without this upgrade, thanks @immunefi!
>
> This is great for whitehats, shows both history and recent work, and is much more motivating. https://t.co/StMHKWIxUB https://t.co/XwRlMXssWO

**Media:**
- photo: https://pbs.twimg.com/media/GICbwWnbsAA-t-g.jpg — no alt text provided by author

**Quoted post (full text):**

    #### Quoted post — @immunefi — 2024-03-06 17:27 UTC (2024-03-06 18:27 WAT)
    
    - URL: https://x.com/immunefi/status/1765428971674402860
    - Metrics (at fetch): bookmark 2, impression 19001, like 34, quote 6, reply 1, retweet 6
    
    > The Immunefi Leaderboard has just been UPGRADED.
    >
    > - You can now see ranks by all-time, year, and the last 90 days.
    >
    > - We’ve also expanded the leaderboard from top 50 to top 100.
    >
    > Check out where you rank on the list and put it in your Twitter bio!
    >
    > https://t.co/p0Y2YFegA1 https://t.co/aVuaJieA42
    
    **Media:**
    - media `3_1765416770842525696` (details not returned by the API)
    


---

## 2024-03-01 · Post · I think this actually breaks native ETH restaking. 


### Post — @Guhu95 — 2024-03-01 02:03 UTC (2024-03-01 03:03 WAT)

- URL: https://x.com/Guhu95/status/1763384425101115899
- Metrics (at fetch): bookmark 1, impression 681, like 1, quote 0, reply 1, retweet 0

> I think this actually breaks native ETH restaking. 
>
> Slashing on voluntary withdrawal can be postponed indefinitely, so:
> - The AVS can't get the ETH unlike with LSTs.
> - The staker keeps earning fees, MEV, and staking rewards (not slashed), so is incentivised to not withdraw!
> - https://t.co/LVpOBIi2Km

**Quoted post (full text):**

    #### Quoted post — @334346969 — 2024-02-29 17:07 UTC (2024-02-29 18:07 WAT)
    
    - URL: https://x.com/334346969/status/1763249568135688640
    - Metrics (at fetch): bookmark 2, impression 5838, like 22, quote 1, reply 1, retweet 0
    
    > So, the slashing doesn't "really" happen until I withdraw from the CL. And even then the ETH isn't really slashed it's just locked in the eigenpod. But none of that matters. It is *effectively* slashed as soon as the eigenpod gets the message about the slashing offence.
    


---

## 2024-02-24 · Post · Bug hunting quest types:


### Post — @Guhu95 — 2024-02-24 06:10 UTC (2024-02-24 07:10 WAT)

- URL: https://x.com/Guhu95/status/1761272386379546876
- Metrics (at fetch): bookmark 13, impression 3516, like 40, quote 1, reply 1, retweet 3

> Bug hunting quest types:
>
> Audits: Work. All about discipline, duty, thoroughness.
>
> Contests: Play. Carefree, quirky sub-games, cleverness.
>
> Bounties: Adventure. Big stakes, no promises, here be dragons. https://t.co/jxj1jyTLyZ

**Media:**
- photo: https://pbs.twimg.com/media/GHFL4gubMAA787V.jpg — no alt text provided by author


---

## 2024-02-24 · Post · Bug hunting quest types:


### Post — @Guhu95 — 2024-02-24 05:51 UTC (2024-02-24 06:51 WAT)

- URL: https://x.com/Guhu95/status/1761267683214143877
- Metrics (at fetch): bookmark 1, impression 41, like 1, quote 0, reply 0, retweet 0

> Bug hunting quest types:
>
> Audits: Work. All about discipline, duty, thoroughness.
>
> Contests: Play. Carefree, quirky sub-games, cleverness.
>
> Bounties: Adventure. Big stakes, no promises, here be dragons.


---

## 2024-02-24 · Post · Bug hunting quest types:


### Post — @Guhu95 — 2024-02-24 05:48 UTC (2024-02-24 06:48 WAT)

- URL: https://x.com/Guhu95/status/1761266955250811306
- Metrics (at fetch): bookmark 0, impression 11, like 0, quote 0, reply 0, retweet 0

> Bug hunting quest types:
>
> Audits: Work. All about discipline, duty, thoroughness.
>
> Contests: Play. Carefree, quirky sub-games, cleverness.
>
> Bounties: Adventure. Big stakes and no promises, here be dragons.


---

## 2024-01-18 · Post · Love it how the winners in this marketing fight between two firms are only bounty hunters and solo a


### Post — @Guhu95 — 2024-01-18 23:50 UTC (2024-01-19 00:50 WAT)

- URL: https://x.com/Guhu95/status/1748130734550978601
- Metrics (at fetch): bookmark 1, impression 826, like 5, quote 0, reply 0, retweet 0

> Love it how the winners in this marketing fight between two firms are only bounty hunters and solo auditors https://t.co/7iLJDNXmxM https://t.co/NeTVdbn0dw

**Media:**
- photo: https://pbs.twimg.com/media/GEKY3Kha8AAthi9.jpg — no alt text provided by author

**Quoted post (full text):**

    #### Quoted post — @3235769978 — 2024-01-18 22:07 UTC (2024-01-18 23:07 WAT)
    
    - URL: https://x.com/3235769978/status/1748104880269488547
    - Metrics (at fetch): bookmark 9, impression 15103, like 44, quote 5, reply 2, retweet 6
    
    > Short answer - we will not, this is not even a bug bounty report. 
    > But a very interesting finding, kudos to @zachobront, funny thing we found it in our audit as well, you would want to look at FNG-20 here (its the first bug in the link you shared, which I guess you haven’t https://t.co/MM2f0xlhFN
    
    **Quoted post** 1748069220301095073: not readable via the API (deleted, private, or withheld).
    


---

## 2024-01-18 · Post · Love it how the winners in this marketing fight between two firms are only bounty hunters and solo a


### Post — @Guhu95 — 2024-01-18 23:48 UTC (2024-01-19 00:48 WAT)

- URL: https://x.com/Guhu95/status/1748130289652797909
- Metrics (at fetch): bookmark 0, impression 3, like 0, quote 0, reply 0, retweet 0

> Love it how the winners in this marketing fight between two firms are only bounty hunters and solo auditors who do 0 marketing https://t.co/Nov0TA8BDp https://t.co/NeTVdbn0dw

**Media:**
- photo: https://pbs.twimg.com/media/GEKY3Kha8AAthi9.jpg — no alt text provided by author

**Quoted post (full text):**

    #### Quoted post — @3235769978 — 2024-01-18 22:07 UTC (2024-01-18 23:07 WAT)
    
    - URL: https://x.com/3235769978/status/1748104880269488547
    - Metrics (at fetch): bookmark 9, impression 15103, like 44, quote 5, reply 2, retweet 6
    
    > Short answer - we will not, this is not even a bug bounty report. 
    > But a very interesting finding, kudos to @zachobront, funny thing we found it in our audit as well, you would want to look at FNG-20 here (its the first bug in the link you shared, which I guess you haven’t https://t.co/MM2f0xlhFN
    
    **Quoted post** 1748069220301095073: not readable via the API (deleted, private, or withheld).
    


---

## 2024-01-18 · Post · Love it how the winners in this marketing fight between two firms are only bounty hunters and solo a


### Post — @Guhu95 — 2024-01-18 23:43 UTC (2024-01-19 00:43 WAT)

- URL: https://x.com/Guhu95/status/1748128983978553385
- Metrics (at fetch): bookmark 0, impression 16, like 1, quote 0, reply 0, retweet 0

> Love it how the winners in this marketing fight between two firms are only bounty hunters and solo auditors https://t.co/eC8y4hxgxX https://t.co/NeTVdbn0dw

**Media:**
- photo: https://pbs.twimg.com/media/GEKY3Kha8AAthi9.jpg — no alt text provided by author

**Quoted post (full text):**

    #### Quoted post — @3235769978 — 2024-01-18 22:07 UTC (2024-01-18 23:07 WAT)
    
    - URL: https://x.com/3235769978/status/1748104880269488547
    - Metrics (at fetch): bookmark 9, impression 15103, like 44, quote 5, reply 2, retweet 6
    
    > Short answer - we will not, this is not even a bug bounty report. 
    > But a very interesting finding, kudos to @zachobront, funny thing we found it in our audit as well, you would want to look at FNG-20 here (its the first bug in the link you shared, which I guess you haven’t https://t.co/MM2f0xlhFN
    
    **Quoted post** 1748069220301095073: not readable via the API (deleted, private, or withheld).
    


---

## 2023-12-15 · Post · Thanks @OddlySpecivik for the ImmunefiWrapped, a great way to wrap up the year on @immunefi. Pretty


Tags (automatic): Platform: Immunefi


### Post — @Guhu95 — 2023-12-15 01:04 UTC (2023-12-15 02:04 WAT)

- URL: https://x.com/Guhu95/status/1735465724297277624
- Metrics (at fetch): not returned

> Thanks @OddlySpecivik for the #ImmunefiWrapped, a great way to wrap up the year on @immunefi. Pretty happy with the results and the accuracy. Hope to have more time for hunting next year! [pic.x.com/r2Uk1kuuRv]

**Media:**
- photo: https://pbs.twimg.com/media/GBWZoWsaYAE3Y4j.jpg — no alt text provided by author


---

## 2023-11-09 · Post · The promised details for the @LybraFinance bug. Why share them?


Tags (automatic): Platform: Immunefi


### Post — @Guhu95 — 2023-11-09 08:36 UTC (2023-11-09 09:36 WAT)

- URL: https://x.com/Guhu95/status/1722533559943287251
- Metrics (at fetch): not returned

> The promised details for the @LybraFinance bug. Why share them?
> - Bug was not fixed, so @LybraFinance community should know that whales can unfairly manipulate rewards.
> - @Immunefi stories are not shared enough, so this may be useful to others.
>
> A short thread 👇 https://twitter.com/Guhu95/status/1720659980209287311

**Links in post:** https://twitter.com/Guhu95/status/1720659980209287311

**Quoted post (full text):**

    #### Quoted post — @Guhu95 — 2023-11-04 04:31 UTC (2023-11-04 05:31 WAT)
    
    - URL: https://x.com/Guhu95/status/1720659980209287311
    - Metrics (at fetch): not returned
    
    > @code4rena got hands, but it's no silver bullet.
    >
    > Got 5K for this one on @immunefi - project decided not to fix due to low likelihood (in their view). Still much better than nothing, so it's a win.
    >
    > It also means I am free to share, which I will, as the bug is pretty unusual. [pic.x.com/pVlG6i5IVT] https://twitter.com/Guhu95/status/1703987327469846838
    
    **Media:**
    - photo: https://pbs.twimg.com/media/F-D8irOawAAqRRE.jpg — no alt text provided by author
    
    **Links in post:** https://twitter.com/Guhu95/status/1703987327469846838
    
    **Quoted post (full text):**
    
        #### Quoted post — @Guhu95 — 2023-09-19 04:20 UTC (2023-09-19 05:20 WAT)
        
        - URL: https://x.com/Guhu95/status/1703987327469846838
        - Metrics (at fetch): not returned
        
        > Damn, bug hunting in a protocol that went through @code4rena feels much harder than usual - mostly dead ends, already "acknowledged", or minimal impact.
        
    


---

## 2023-11-04 · Reply · @code4rena got hands, but it's no silver bullet.


Tags (automatic): Platform: Immunefi, Platform: Code4rena / Sherlock / Cantina


### Post — @Guhu95 — 2023-11-04 04:31 UTC (2023-11-04 05:31 WAT)

- URL: https://x.com/Guhu95/status/1720659980209287311
- Metrics (at fetch): not returned

> @code4rena got hands, but it's no silver bullet.
>
> Got 5K for this one on @immunefi - project decided not to fix due to low likelihood (in their view). Still much better than nothing, so it's a win.
>
> It also means I am free to share, which I will, as the bug is pretty unusual. [pic.x.com/pVlG6i5IVT] https://twitter.com/Guhu95/status/1703987327469846838

**Media:**
- photo: https://pbs.twimg.com/media/F-D8irOawAAqRRE.jpg — no alt text provided by author

**Links in post:** https://twitter.com/Guhu95/status/1703987327469846838

**Quoted post (full text):**

    #### Quoted post — @Guhu95 — 2023-09-19 04:20 UTC (2023-09-19 05:20 WAT)
    
    - URL: https://x.com/Guhu95/status/1703987327469846838
    - Metrics (at fetch): not returned
    
    > Damn, bug hunting in a protocol that went through @code4rena feels much harder than usual - mostly dead ends, already "acknowledged", or minimal impact.
    


---

## 2023-10-15 · Post · Was your @Immunefi bounty nerfed due to "repeated attacks", and only first attack counted? Here's ev


Tags (automatic): Platform: Immunefi


### Post — @Guhu95 — 2023-10-15 01:06 UTC (2023-10-15 02:06 WAT)

- URL: https://x.com/Guhu95/status/1713360634384163166
- Metrics (at fetch): not returned

> Was your @Immunefi bounty nerfed due to "repeated attacks", and only first attack counted? Here's evidence for next time to refute with. TL;DR: projects are very slow to react, only 2% reacted within the first hour. 
>
> Projects should only be allowed to use "first hour" clause in their programs, instead of "first attack". Mediation rules should also be corrected.
>
> Or should we instead ask the blackhats to limit themselves to one attack too?

**Links in post:** https://twitter.com/dannygfromnyc/status/1670416136478003203

**Quoted post (full text):**

    #### Quoted post — @1548683514006192128 — 2023-06-18 13:00 UTC (2023-06-18 14:00 WAT)
    
    - URL: https://x.com/1548683514006192128/status/1670416136478003203
    - Metrics (at fetch): not returned
    
    > 5/
    >
    > Emergency Pauses Analysis
    >
    > - 47.5% of the protocols supported "pause" functionality
    >
    > - 58.6% pause the protocol within 48 hours of incident
    >
    > - Only 1 protocol paused within the first hour [pic.x.com/FBEpDVBoR2]
    
    **Media:**
    - media `3_1670416128626270208` (details not returned by the API)
    


---

## 2023-10-15 · Post · Was your @Immunefi bounty nerfed due to "repeated attacks", so that only the first attack counted? T


Tags (automatic): Platform: Immunefi


### Post — @Guhu95 — 2023-10-15 01:02 UTC (2023-10-15 02:02 WAT)

- URL: https://x.com/Guhu95/status/1713359694373478657
- Metrics (at fetch): not returned

> Was your @Immunefi bounty nerfed due to "repeated attacks", so that only the first attack counted? This is some evidence to use next time to refute such imaginary "defences". 
>
> TL;DR - projects are very slow to react, only 2% reacted within the first hour.
>
> From this:
> 1) The rule should be "first hour" instead of "first attack". 
> 2) Projects should only be allowed to use "first hour" clause in their programs, instead of "first attack". 
>
> Or should we instead ask the blackhats to limit themselves to one attack too?

**Quoted post (full text):**

    #### Quoted post — @1548683514006192128 — 2023-06-18 13:00 UTC (2023-06-18 14:00 WAT)
    
    - URL: https://x.com/1548683514006192128/status/1670416136478003203
    - Metrics (at fetch): not returned
    
    > 5/
    >
    > Emergency Pauses Analysis
    >
    > - 47.5% of the protocols supported "pause" functionality
    >
    > - 58.6% pause the protocol within 48 hours of incident
    >
    > - Only 1 protocol paused within the first hour [pic.x.com/FBEpDVBoR2]
    
    **Media:**
    - media `3_1670416128626270208` (details not returned by the API)
    


---

## 2023-10-13 · Post · Thanks! Auditing @Kwenta_io 's StakingV2 was a pleasure. The team's exceptionally high engineering s


### Post — @Guhu95 — 2023-10-13 02:25 UTC (2023-10-13 03:25 WAT)

- URL: https://x.com/Guhu95/status/1712655700374196596
- Metrics (at fetch): not returned

> Thanks! Auditing @Kwenta_io 's StakingV2 was a pleasure. The team's exceptionally high engineering standards, detailed docs, and quick and thorough comms ensured both a productive and an enjoyable audit. Happy to help 🤝 https://twitter.com/SNX_Exchange/status/1712113364338405701

**Links in post:** https://twitter.com/SNX_Exchange/status/1712113364338405701

**Quoted post (full text):**

    #### Quoted post — @1256020146360971264 — 2023-10-11 14:30 UTC (2023-10-11 15:30 WAT)
    
    - URL: https://x.com/1256020146360971264/status/1712113364338405701
    - Metrics (at fetch): not returned
    
    > What about reliability and security? 🔒
    >
    > Kwenta's worked in conjunction with auditors to identify and prevent potential issues. We'd like to give a special shoutout to @Guhu95 for having exceptional attention to detail, and being a pleasure to work with. 🤝
    


---

## 2023-10-06 · Post · When to move on from a codebase when bounty-hunting? Here's my approach, curious to hear other opini


### Post — @Guhu95 — 2023-10-06 08:45 UTC (2023-10-06 09:45 WAT)

- URL: https://x.com/Guhu95/status/1710214685264371904
- Metrics (at fetch): not returned

> When to move on from a codebase when bounty-hunting? Here's my approach, curious to hear other opinions!
>
> First, why not just wing it? 
> 1. Constant effort to make high-stakes decisions is exhausting.
> 2. Second-guessing yourself is emotionally draining. 
> 3. Hurts performance and focus because it's a repeated distraction.
>
> What I do now: an audit-like time-box: rough expected-value of reward divided by the cost of an audit day. Simple.
>
> So, Critical-Reward x P(find) x P(getting-paid) / Audit-Day-Price = Hunt-days. 
>
> I usually estimate P(find) at 10-20% depending on code quality, and P(getting-paid) depends on the sketchiness of project🫠. 
>
> The probabilities are a guess, but this really helps keep a positive, focused mindset knowing I followed a rational process.

**Links in post:** https://twitter.com/Guhu95/status/1703987327469846838

**Quoted post (full text):**

    #### Quoted post — @Guhu95 — 2023-09-19 04:20 UTC (2023-09-19 05:20 WAT)
    
    - URL: https://x.com/Guhu95/status/1703987327469846838
    - Metrics (at fetch): not returned
    
    > Damn, bug hunting in a protocol that went through @code4rena feels much harder than usual - mostly dead ends, already "acknowledged", or minimal impact.
    


---

## 2023-09-20 · Post · Life-hack for complex codebases: replace the interfaces with contracts. 


### Post — @Guhu95 — 2023-09-20 04:15 UTC (2023-09-20 05:15 WAT)

- URL: https://x.com/Guhu95/status/1704348640805077296
- Metrics (at fetch): not returned

> Life-hack for complex codebases: replace the interfaces with contracts. 
>
> Two main benefits:
> - Going from usage to definition goes to actual code.
> - Going from code to references shows all actual callers.
>
> (May need to resolve some cyclical references)

**Media:**
- photo: https://pbs.twimg.com/media/F6cPgDgaUAA9R9f.png — no alt text provided by author


---

## 2023-09-20 · Post · Life-hack for complex codebases: replace the interfaces with contracts. 


### Post — @Guhu95 — 2023-09-20 04:13 UTC (2023-09-20 05:13 WAT)

- URL: https://x.com/Guhu95/status/1704348061273878768
- Metrics (at fetch): not returned

> Life-hack for complex codebases: replace the interfaces with contracts. 
>
> Two main benefits:
> - Going to method definition goes to actual code.
> - Going to references shows all callers.
>
> (May need to resolve some cyclical references)

**Media:**
- photo: https://pbs.twimg.com/media/F6cPgDgaUAA9R9f.png — no alt text provided by author


---

## 2023-09-20 · Post · Life-hack for complex codebases: replace the interfaces with contracts. 


### Post — @Guhu95 — 2023-09-20 04:09 UTC (2023-09-20 05:09 WAT)

- URL: https://x.com/Guhu95/status/1704347039935696990
- Metrics (at fetch): not returned

> Life-hack for complex codebases: replace the interfaces with contracts. 
>
> Two main benefits:
> - Going to method definition goes to actual code.
> - Going to references shows all callers.
>
> (May need to resolve some cyclical references)

**Media:**
- photo: https://pbs.twimg.com/media/F6cNVV4bQAAtpgY.png — no alt text provided by author


---

## 2023-09-20 · Post · Life-hack for complex codebases: replace the interfaces with contracts. 


### Post — @Guhu95 — 2023-09-20 04:07 UTC (2023-09-20 05:07 WAT)

- URL: https://x.com/Guhu95/status/1704346589136146480
- Metrics (at fetch): not returned

> Life-hack for complex codebases: replace the interfaces with contracts. 
>
> Two huge benefits:
> - Going to method definition goes to actual code.
> - Going to references shows all callers.
>
> (May need to resolve some cyclical references)

**Media:**
- photo: https://pbs.twimg.com/media/F6cNVV4bQAAtpgY.png — no alt text provided by author


---

## 2023-09-20 · Post · Life-hack for complex codebases: replace the interfaces with contracts. 


### Post — @Guhu95 — 2023-09-20 04:07 UTC (2023-09-20 05:07 WAT)

- URL: https://x.com/Guhu95/status/1704346504759283773
- Metrics (at fetch): not returned

> Life-hack for complex codebases: replace the interfaces with contracts. 
>
> Two huge benefits:
> - Going to method definition goes to actual code.
> - Going to references shows all callers.
>
> (May need to resolve some cyclical references)

**Media:**
- photo: https://pbs.twimg.com/media/F6cNVV4bQAAtpgY.png — no alt text provided by author


---

## 2023-09-19 · Post · Damn, bug hunting in a protocol that went through @code4rena feels much harder than usual - mostly d


Tags (automatic): Platform: Code4rena / Sherlock / Cantina


### Post — @Guhu95 — 2023-09-19 04:20 UTC (2023-09-19 05:20 WAT)

- URL: https://x.com/Guhu95/status/1703987327469846838
- Metrics (at fetch): not returned

> Damn, bug hunting in a protocol that went through @code4rena feels much harder than usual - mostly dead ends, already "acknowledged", or minimal impact.


---

## 2023-08-19 · Post · Made it to the @immunefi leaderboard 😎 [pic.x.com/UumXBwjlFd]


Tags (automatic): Platform: Immunefi


### Post — @Guhu95 — 2023-08-19 10:47 UTC (2023-08-19 11:47 WAT)

- URL: https://x.com/Guhu95/status/1692850687682760982
- Metrics (at fetch): not returned

> Made it to the @immunefi leaderboard 😎 [pic.x.com/UumXBwjlFd]

**Media:**
- photo: https://pbs.twimg.com/media/F342uM9boAAECuC.jpg — no alt text provided by author
