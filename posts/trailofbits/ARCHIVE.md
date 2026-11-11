# @trailofbits — full verbatim X archive (security-relevant posts)

_Generated 2026-11-11 from the X API (full-archive search + timeline). Every post below is copied word-for-word; t.co links are expanded; quoted posts are inlined in full; media are listed with alt text when the author provided it. Posts are grouped by conversation (a thread = the author's root post followed by their own replies, oldest first). Groups are newest first. An agent without X access can rely on this file._

- Posts in this file: 58
- Conversations/threads: 58
- Oldest post captured: 2025-07-17
- Newest post captured: 2026-11-03


---

## 2026-11-03 · Post · A cryptographically verified tally doesn't mean every vote is legitimate. Paper ballots still matter


### Post — @trailofbits — 2026-11-03 12:18 UTC (2026-11-03 13:18 WAT)

- URL: https://x.com/trailofbits/status/2117592155568972217
- Metrics (at fetch): bookmark 19, impression 4347, like 47, quote 3, reply 3, retweet 16

> A cryptographically verified tally doesn't mean every vote is legitimate. Paper ballots still matter: they provide an audit record independent of software. We explain how electronic voting works, and how cryptography can make paper-based elections more trustworthy.


---

## 2026-11-03 · Post · A cryptographically verified tally doesn't mean every vote is legitimate. Paper ballots still matter


### Post — @trailofbits — 2026-11-03 12:17 UTC (2026-11-03 13:17 WAT)

- URL: https://x.com/trailofbits/status/2117592037016883405
- Metrics (at fetch): bookmark 0, impression 35, like 0, quote 0, reply 0, retweet 0

> A cryptographically verified tally doesn't mean every vote is legitimate. Paper ballots still matter: they provide an audit record independent of software. We explain how electronic voting works, and how cryptography can make paper-based elections more trustworthy.


---

## 2026-11-02 · Post · Stable software often ships with known bugs because the fixes are never backported. That backlog is 


Tags (automatic): Memory corruption / native, AI-assisted hunting


### Post — @trailofbits — 2026-11-02 12:15 UTC (2026-11-02 13:15 WAT)

- URL: https://x.com/trailofbits/status/2117229048749228374
- Metrics (at fetch): bookmark 19, impression 5582, like 51, quote 2, reply 5, retweet 5

> Stable software often ships with known bugs because the fixes are never backported. That backlog is now an easy target for cyber-capable agents.
>
> We used Codex to cut time per backport from days to ~30 min, with 149 Linux kernel CVE fixes applied so far.
> https://blog.trailofbits.com/2026/11/02/backporting-security-fixes-at-scale-with-codex/

**Links in post:** https://blog.trailofbits.com/2026/11/02/backporting-security-fixes-at-scale-with-codex/


---

## 2026-10-29 · Post · October Trail of Bits Tribune: Releasing a PHP exploit demo, new plugins for patching, and package-i


### Post — @trailofbits — 2026-10-29 13:58 UTC (2026-10-29 14:58 WAT)

- URL: https://x.com/trailofbits/status/2115805539061879092
- Metrics (at fetch): bookmark 11, impression 3005, like 22, quote 0, reply 3, retweet 4

> October Trail of Bits Tribune: Releasing a PHP exploit demo, new plugins for patching, and package-integrity research. Plus Brotli-checker, SequenceHash, and six new public security reviews.
>
> Read the Tribune: https://mailchi.mp/trailofbits/october-2026-tribune [pic.x.com/uczCaUftT9]

**Media:**
- photo: https://pbs.twimg.com/media/HVzZ7OwW8AAj0SC.jpg — no alt text provided by author

**Links in post:** https://mailchi.mp/trailofbits/october-2026-tribune


---

## 2026-10-23 · Post · We’re still testing how exploitable the Node.js/Brotli bug is, but we’ve found that it’s surprisingl


### Post — @trailofbits — 2026-10-23 23:14 UTC (2026-10-24 00:14 WAT)

- URL: https://x.com/trailofbits/status/2113771101058937163
- Metrics (at fetch): bookmark 214, impression 30121, like 309, quote 3, reply 14, retweet 69

> We’re still testing how exploitable the Node.js/Brotli bug is, but we’ve found that it’s surprisingly hard to tell whether you’re even affected.
>
> So @ToBScottA built a scanner that finds hidden copies of the decoder, even in stripped binaries.
> https://github.com/trailofbits/brotli-checker

**Links in post:** https://github.com/trailofbits/brotli-checker


---

## 2026-10-22 · Post · We got a PHP exploit working against MediaWiki, but getting freed memory reused just right takes som


Tags (automatic): AI-assisted hunting


### Post — @trailofbits — 2026-10-22 20:40 UTC (2026-10-22 21:40 WAT)

- URL: https://x.com/trailofbits/status/2113369851985375638
- Metrics (at fetch): bookmark 56, impression 13110, like 153, quote 3, reply 3, retweet 19

> We got a PHP exploit working against MediaWiki, but getting freed memory reused just right takes some tinkering under normal traffic. 
>
> LLMs struggle here without an expert's guidance, which may help explain the attempts but no confirmed successes. https://twitter.com/dguido/status/2113129153293897925

**Links in post:** https://twitter.com/dguido/status/2113129153293897925

**Quoted post** 2113129153293897925: not readable via the API (deleted, private, or withheld).


---

## 2026-10-21 · Post · Yesterday, rumors started circulating about two unpatched critical-severity bugs in PHP. 


Tags (automatic): AI-assisted hunting


### Post — @trailofbits — 2026-10-21 22:02 UTC (2026-10-21 23:02 WAT)

- URL: https://x.com/trailofbits/status/2113028241128821204
- Metrics (at fetch): bookmark 36, impression 5846, like 87, quote 3, reply 6, retweet 14

> Yesterday, rumors started circulating about two unpatched critical-severity bugs in PHP. 
>
> Within 17 hours, Cloudflare was blocking attacks and Patchstack reported active exploitation. 
>
> When AI can develop a working exploit in hours, bugs need to be patched just as fast.


---

## 2026-10-21 · Post · Finding bugs is the easy part. Shipping fixes that hold up is harder.


### Post — @trailofbits — 2026-10-21 16:04 UTC (2026-10-21 17:04 WAT)

- URL: https://x.com/trailofbits/status/2112938091585351824
- Metrics (at fetch): bookmark 99, impression 20791, like 143, quote 13, reply 17, retweet 24

> Finding bugs is the easy part. Shipping fixes that hold up is harder.
>
> We analyzed thousands of Codex sessions from our work on Patch the Planet with @OpenAI and built patching-bugs, a plugin that writes a fix, proves it, and checks it for regressions.


---

## 2026-09-30 · Post · September Trail of Bits Tribune: Fact-checking 1Password's AI patching benchmark, and a signature-fo


Tags (automatic): ZK, AI-assisted hunting


### Post — @trailofbits — 2026-09-30 13:20 UTC (2026-09-30 14:20 WAT)

- URL: https://x.com/trailofbits/status/2105286717640966539
- Metrics (at fetch): bookmark 3, impression 5711, like 22, quote 0, reply 0, retweet 3

> September Trail of Bits Tribune: Fact-checking 1Password's AI patching benchmark, and a signature-forgery bug in Miden's zkVM. Also: a string-slicing bug in Lean, 27 advisory submissions to OpenClaw, and seven new security reviews.
>
> https://mailchi.mp/trailofbits/september-2026-tribune [pic.x.com/z32C0a30r7]

**Media:**
- photo: https://pbs.twimg.com/media/HTd6_tEXYAMh8hT.png — no alt text provided by author

**Links in post:** https://mailchi.mp/trailofbits/september-2026-tribune


---

## 2026-09-25 · Post · Threshold signatures secure billions in crypto and increasingly run inside TEEs. But MPC and TEEs ma


Tags (automatic): TEE / enclave


### Post — @trailofbits — 2026-09-25 11:11 UTC (2026-09-25 12:11 WAT)

- URL: https://x.com/trailofbits/status/2103442265859387662
- Metrics (at fetch): bookmark 19, impression 3696, like 62, quote 0, reply 4, retweet 9

> Threshold signatures secure billions in crypto and increasingly run inside TEEs. But MPC and TEEs make different bets on trust: MPC spreads it across independent parties; TEEs concentrate it in the hardware manufacturer and its attestation infrastructure. https://blog.trailofbits.com/2026/09/25/dont-let-tees-break-your-mpc/

**Links in post:** https://blog.trailofbits.com/2026/09/25/dont-let-tees-break-your-mpc/


---

## 2026-09-21 · Post · A 2012 USENIX paper brought XML Signature Wrapping (XSW) attacks against SAML into the mainstream. S


### Post — @trailofbits — 2026-09-21 11:18 UTC (2026-09-21 12:18 WAT)

- URL: https://x.com/trailofbits/status/2101994434191585303
- Metrics (at fetch): bookmark 12, impression 3339, like 41, quote 0, reply 5, retweet 9

> A 2012 USENIX paper brought XML Signature Wrapping (XSW) attacks against SAML into the mainstream. SAML has repeatedly shown that complexity is the antithesis of security. Matt Schwager names 5 protocol design flaws enabling SAML's insecurity: https://blog.trailofbits.com/2026/09/21/saml-a-fractal-of-bad-design/

**Links in post:** https://blog.trailofbits.com/2026/09/21/saml-a-fractal-of-bad-design/


---

## 2026-09-21 · Post · A 2012 USENIX paper brought XML Signature Wrapping (XSW) attacks against SAML into the mainstream. S


### Post — @trailofbits — 2026-09-21 11:15 UTC (2026-09-21 12:15 WAT)

- URL: https://x.com/trailofbits/status/2101993603849429447
- Metrics (at fetch): bookmark 0, impression 441, like 1, quote 0, reply 0, retweet 0

> A 2012 USENIX paper brought XML Signature Wrapping (XSW) attacks against SAML into the mainstream. SAML has repeatedly shown that complexity is the antithesis of security. Matt Schwager names 5 protocol design flaws enabling SAML's insecurity: https://blog.trailofbits.com/2026/09/21/saml-a-fractal-of-bad-design/

**Links in post:** https://blog.trailofbits.com/2026/09/21/saml-a-fractal-of-bad-design/


---

## 2026-09-18 · Post · We audited parts of @0xMiden's zkVM, written in a custom assembly language called MASM. MASM origina


Tags (automatic): ZK, AI-assisted hunting


### Post — @trailofbits — 2026-09-18 11:03 UTC (2026-09-18 12:03 WAT)

- URL: https://x.com/trailofbits/status/2100903558111445193
- Metrics (at fetch): bookmark 120, impression 26302, like 203, quote 7, reply 14, retweet 27

> We audited parts of @0xMiden's zkVM, written in a custom assembly language called MASM. MASM originally had no developer tooling, so we used Claude and Codex to build a decompiler and static-analysis engine. It flagged a signature-forgery bug that could've cost millions.


---

## 2026-09-15 · Post · .@1Password's FLAWED report says AI models produce a clean security fix only 26% of the time.


Tags (automatic): AI-assisted hunting


### Post — @trailofbits — 2026-09-15 11:15 UTC (2026-09-15 12:15 WAT)

- URL: https://x.com/trailofbits/status/2099819316745060639
- Metrics (at fetch): bookmark 97, impression 557198, like 268, quote 13, reply 24, retweet 49

> .@1Password's FLAWED report says AI models produce a clean security fix only 26% of the time.
>
> Defenders shouldn't take that number seriously.


---

## 2026-09-10 · Post · Our engineer Joe Doyle built trailmix, the quantum circuit toolkit we open-sourced in June. The pape


Tags (automatic): ZK


### Post — @trailofbits — 2026-09-10 21:22 UTC (2026-09-10 22:22 WAT)

- URL: https://x.com/trailofbits/status/2098160138591039879
- Metrics (at fetch): bookmark 26, impression 7546, like 77, quote 2, reply 4, retweet 12

> Our engineer Joe Doyle built trailmix, the quantum circuit toolkit we open-sourced in June. The paper's leading circuits build on it, and his leaderboard submissions helped push the score past Google's. https://github.com/trailofbits/trailmix https://twitter.com/eigenlabs/status/2098037456067244098

**Links in post:** https://github.com/trailofbits/trailmix, https://twitter.com/eigenlabs/status/2098037456067244098

**Quoted post** 2098037456067244098: not readable via the API (deleted, private, or withheld).


---

## 2026-09-09 · Post · Last week, @AnthropicAI formalized Fermat's Last Theorem in 13 million lines of Lean code.


### Post — @trailofbits — 2026-09-09 11:15 UTC (2026-09-09 12:15 WAT)

- URL: https://x.com/trailofbits/status/2097644988121104815
- Metrics (at fetch): bookmark 128, impression 45827, like 486, quote 22, reply 17, retweet 64

> Last week, @AnthropicAI formalized Fermat's Last Theorem in 13 million lines of Lean code.
>
> We "proved" that same theorem in 20 lines by exploiting a bug we found in Lean. https://blog.trailofbits.com/2026/09/09/a-proof-of-fermats-last-theorem-that-fits-the-margin/

**Links in post:** https://blog.trailofbits.com/2026/09/09/a-proof-of-fermats-last-theorem-that-fits-the-margin/


---

## 2026-09-08 · Post · OpenSSL's latest advisory covers 9 patched vulnerabilities. Our engineers Filipe Casal and Opal Wrig


### Post — @trailofbits — 2026-09-08 15:43 UTC (2026-09-08 16:43 WAT)

- URL: https://x.com/trailofbits/status/2097350089089908950
- Metrics (at fetch): bookmark 4, impression 4643, like 45, quote 0, reply 0, retweet 14

> OpenSSL's latest advisory covers 9 patched vulnerabilities. Our engineers Filipe Casal and Opal Wright found 4 of them as part of Patch the Planet.
> https://openssl-library.org/news/secadv/20260825.txt

**Links in post:** https://openssl-library.org/news/secadv/20260825.txt


---

## 2026-08-31 · Post · We launched as a trusted auditor for Signal's Automatic Key Verification, watched GPT 5.6-Cyber chai


Tags (automatic): AI-assisted hunting


### Post — @trailofbits — 2026-08-31 11:00 UTC (2026-08-31 12:00 WAT)

- URL: https://x.com/trailofbits/status/2094379675032105043
- Metrics (at fetch): bookmark 44, impression 12651, like 113, quote 3, reply 10, retweet 11

> We launched as a trusted auditor for Signal's Automatic Key Verification, watched GPT 5.6-Cyber chain three 0-days into a VM escape, and found a Provenance bug representing ~$500K in drainable HASH. Plus 8 new public reviews, 2 open-source tools, and more.
>
> August Tribune: [pic.x.com/TU0svltI1E]

**Media:**
- photo: https://pbs.twimg.com/media/HQ1Dz2lboAA1SIN.png — no alt text provided by author


---

## 2026-08-26 · Post · We asked GPT 5.6-Cyber to escape a VM used to sandbox agents. It broke out three times.


Tags (automatic): AI-assisted hunting


### Post — @trailofbits — 2026-08-26 11:15 UTC (2026-08-26 12:15 WAT)

- URL: https://x.com/trailofbits/status/2092571523450114277
- Metrics (at fetch): bookmark 984, impression 499432, like 1698, quote 100, reply 69, retweet 333

> We asked GPT 5.6-Cyber to escape a VM used to sandbox agents. It broke out three times.
>
> In its final escape, the agent found three 0-days on its own and chained them into a working exploit. https://blog.trailofbits.com/2026/08/26/vms-wont-contain-cyber-capable-agents/

**Links in post:** https://blog.trailofbits.com/2026/08/26/vms-wont-contain-cyber-capable-agents/


---

## 2026-08-25 · Post · We found a bug that lets any user grant themselves admin access to live financial assets on Provenan


Tags (automatic): Blockchain / L1-L2 / bridge


### Post — @trailofbits — 2026-08-25 11:15 UTC (2026-08-25 12:15 WAT)

- URL: https://x.com/trailofbits/status/2092209135651557648
- Metrics (at fetch): bookmark 64, impression 16902, like 145, quote 4, reply 2, retweet 10

> We found a bug that lets any user grant themselves admin access to live financial assets on Provenance, a Cosmos SDK chain.
>
> 82 token accounts were exploitable, representing ~$500K in drainable HASH. Now patched. https://blog.trailofbits.com/2026/08/25/state-divergence-enables-unauthorized-access/

**Links in post:** https://blog.trailofbits.com/2026/08/25/state-divergence-enables-unauthorized-access/


---

## 2026-08-14 · Post · PATCH THE PLANET BUG SPOTLIGHT: We found a medium-severity bug in aiohttp, Python's HTTP engine that


### Post — @trailofbits — 2026-08-14 11:02 UTC (2026-08-14 12:02 WAT)

- URL: https://x.com/trailofbits/status/2088219615373504980
- Metrics (at fetch): bookmark 12, impression 5193, like 37, quote 1, reply 3, retweet 7

> PATCH THE PLANET BUG SPOTLIGHT: We found a medium-severity bug in aiohttp, Python's HTTP engine that had 600M+ downloads last month. Denys Pakizh caught oversized requests dodging its size limits. Now patched. CVE-2026-54277 in the dashboard: https://trailofbits.com/patch-the-planet/dashboard

**Links in post:** https://trailofbits.com/patch-the-planet/dashboard


---

## 2026-08-05 · Post · A malicious host can attack your AWS Nitro Enclave through its connection to KMS. If your enclave ta


Tags (automatic): TEE / enclave


### Post — @trailofbits — 2026-08-05 11:15 UTC (2026-08-05 12:15 WAT)

- URL: https://x.com/trailofbits/status/2084961381233606753
- Metrics (at fetch): bookmark 11, impression 2918, like 37, quote 0, reply 0, retweet 4

> A malicious host can attack your AWS Nitro Enclave through its connection to KMS. If your enclave talks with KMS, read this before you ship. https://blog.trailofbits.com/2026/08/05/a-few-notes-on-aws-nitro-enclaves-kms-integration/

**Links in post:** https://blog.trailofbits.com/2026/08/05/a-few-notes-on-aws-nitro-enclaves-kms-integration/


---

## 2026-07-31 · Post · PATCH THE PLANET BUG SPOTLIGHT: We found a high-severity use-after-free bug in nginx, the web server


Tags (automatic): Memory corruption / native


### Post — @trailofbits — 2026-07-31 14:01 UTC (2026-07-31 15:01 WAT)

- URL: https://x.com/trailofbits/status/2083191391358702029
- Metrics (at fetch): bookmark 15, impression 7548, like 78, quote 0, reply 2, retweet 3

> PATCH THE PLANET BUG SPOTLIGHT: We found a high-severity use-after-free bug in nginx, the web server handling over 30% of all websites in the world. Now patched.


---

## 2026-07-28 · Post · Rust maintainers assumed a team of engineers was behind our bug reports. It was one engineer using C


### Post — @trailofbits — 2026-07-28 11:15 UTC (2026-07-28 12:15 WAT)

- URL: https://x.com/trailofbits/status/2082062278229188646
- Metrics (at fetch): bookmark 84, impression 42455, like 389, quote 4, reply 7, retweet 10

> Rust maintainers assumed a team of engineers was behind our bug reports. It was one engineer using Codex's /goal.


---

## 2026-07-10 · Post · Later today at @SummerC0n, Asritha Bodepudi will show how to build a Windows n-day exploit chain for


Tags (automatic): Memory corruption / native


### Post — @trailofbits — 2026-07-10 11:15 UTC (2026-07-10 12:15 WAT)

- URL: https://x.com/trailofbits/status/2075539295272632492
- Metrics (at fetch): bookmark 3, impression 2989, like 13, quote 0, reply 0, retweet 3

> Later today at @SummerC0n, Asritha Bodepudi will show how to build a Windows n-day exploit chain for RasMan, the Remote Access Connection Manager service.
>
> 11:15AM ET, Main Stage, Littlefield in Brooklyn. https://www.summercon.org/schedule/

**Links in post:** https://www.summercon.org/schedule/


---

## 2026-07-08 · Post · Mewt grades your test suite by sabotaging your code. Each change that doesn't get flagged by your te


### Post — @trailofbits — 2026-07-08 11:15 UTC (2026-07-08 12:15 WAT)

- URL: https://x.com/trailofbits/status/2074814523257532555
- Metrics (at fetch): bookmark 9, impression 3558, like 24, quote 0, reply 1, retweet 6

> Mewt grades your test suite by sabotaging your code. Each change that doesn't get flagged by your tests is a potential bug. 
>
> Today we're expanding it to support DAML, @CantonNetwork's native language, with two new mutant classes for DAML's authorization rules.


---

## 2026-06-30 · Post · 1.2 billion downloads ran through pyca/cryptography last month. Nearly every Python app that touches


### Post — @trailofbits — 2026-06-30 11:15 UTC (2026-06-30 12:15 WAT)

- URL: https://x.com/trailofbits/status/2071915420584411634
- Metrics (at fetch): bookmark 13, impression 6493, like 48, quote 0, reply 2, retweet 4

> 1.2 billion downloads ran through pyca/cryptography last month. Nearly every Python app that touches crypto depends on it. If it doesn't ship post-quantum primitives, the Python ecosystem can't migrate. 🧵


---

## 2026-06-05 · Post · We beat Google's quantum circuit again, and we didn't have to forge a proof this time. 


Tags (automatic): ZK


### Post — @trailofbits — 2026-06-05 19:30 UTC (2026-06-05 20:30 WAT)

- URL: https://x.com/trailofbits/status/2062980523232805164
- Metrics (at fetch): bookmark 32, impression 22266, like 116, quote 6, reply 17, retweet 23

> We beat Google's quantum circuit again, and we didn't have to forge a proof this time. 
>
> Today we're releasing trailmix, a toolkit for quantum "kickmix" circuits. It includes 5 new circuits we built for elliptic curve addition, the hardest part of Shor's algorithm. [pic.x.com/X3jYoU5udB]

**Media:**
- photo: https://pbs.twimg.com/media/HKEt2pHWkAABC_7.jpg — no alt text provided by author


---

## 2026-05-19 · Post · .@obsdmd asked us to audit their Sync protocol. Our engineers delivered eleven findings. 


### Post — @trailofbits — 2026-05-19 15:08 UTC (2026-05-19 16:08 WAT)

- URL: https://x.com/trailofbits/status/2056753768432316567
- Metrics (at fetch): bookmark 62, impression 16926, like 105, quote 1, reply 4, retweet 14

> .@obsdmd asked us to audit their Sync protocol. Our engineers delivered eleven findings. 
>
> Five went above and beyond the original scope and found system-level issues that weren't specific to Sync itself. https://twitter.com/obsdmd/status/2054606618818711862

**Links in post:** https://twitter.com/obsdmd/status/2054606618818711862

**Quoted post** 2054606618818711862: not readable via the API (deleted, private, or withheld).


---

## 2026-05-13 · Post · We were one of four initial grant recipients in @OpenAI's Trusted Access for Cyber program. 


### Post — @trailofbits — 2026-05-13 14:43 UTC (2026-05-13 15:43 WAT)

- URL: https://x.com/trailofbits/status/2054573243680559165
- Metrics (at fetch): bookmark 112, impression 42773, like 201, quote 6, reply 7, retweet 32

> We were one of four initial grant recipients in @OpenAI's Trusted Access for Cyber program. 
>
> Daybreak matters because frontier models now find bugs faster than maintainers can triage them, and that gap is about to get worse. https://twitter.com/OpenAI/status/2053939702110269822

**Links in post:** https://twitter.com/OpenAI/status/2053939702110269822

**Quoted post** 2053939702110269822: not readable via the API (deleted, private, or withheld).


---

## 2026-05-12 · Post · Full house in Miami. Thanks to @HypernativeLabs and @zeroshadow_io for co-hosting a poker night with


Tags (automatic): Blockchain / L1-L2 / bridge


### Post — @trailofbits — 2026-05-12 14:57 UTC (2026-05-12 15:57 WAT)

- URL: https://x.com/trailofbits/status/2054214413536973303
- Metrics (at fetch): bookmark 0, impression 4597, like 20, quote 0, reply 0, retweet 3

> Full house in Miami. Thanks to @HypernativeLabs and @zeroshadow_io for co-hosting a poker night with us at Consensus, and to everyone who came through. Similar VIP events to come. [pic.x.com/yii9hVuBwi]

**Media:**
- photo: https://pbs.twimg.com/media/HIIId0xbsAEzad6.jpg — no alt text provided by author
- photo: https://pbs.twimg.com/media/HIIIefHa4AA1KDL.jpg — no alt text provided by author
- photo: https://pbs.twimg.com/media/HIIIy8vaMAEisI6.jpg — no alt text provided by author
- photo: https://pbs.twimg.com/media/HIIJEuabcAEpPuB.jpg — no alt text provided by author


---

## 2026-05-12 · Post · Go's fuzzer is missing half the toolkit Rust and C/C++ researchers use every day. gosentry, our fork


### Post — @trailofbits — 2026-05-12 11:02 UTC (2026-05-12 12:02 WAT)

- URL: https://x.com/trailofbits/status/2054155130052775952
- Metrics (at fetch): bookmark 28, impression 5793, like 49, quote 0, reply 1, retweet 7

> Go's fuzzer is missing half the toolkit Rust and C/C++ researchers use every day. gosentry, our fork of the Go toolchain, brings it inside `go test -fuzz`. 🧵


---

## 2026-05-05 · Post · 30 readers took our C/C++ challenge. Some solved the Linux warmup, but nobody cracked the Windows dr


### Post — @trailofbits — 2026-05-05 11:02 UTC (2026-05-05 12:02 WAT)

- URL: https://x.com/trailofbits/status/2051618417086525470
- Metrics (at fetch): bookmark 48, impression 13486, like 78, quote 0, reply 3, retweet 11

> 30 readers took our C/C++ challenge. Some solved the Linux warmup, but nobody cracked the Windows driver bug. https://x.com/trailofbits/status/2042253721581871121

**Links in post:** https://x.com/trailofbits/status/2042253721581871121

**Quoted post** 2042253721581871121: not readable via the API (deleted, private, or withheld).


---

## 2026-04-17 · Post · Google used a ZK proof to disclose a quantum breakthrough that cuts the cost of breaking cryptocurre


Tags (automatic): ZK


### Post — @trailofbits — 2026-04-17 11:02 UTC (2026-04-17 12:02 WAT)

- URL: https://x.com/trailofbits/status/2045095428975104009
- Metrics (at fetch): bookmark 273, impression 81086, like 714, quote 14, reply 14, retweet 90

> Google used a ZK proof to disclose a quantum breakthrough that cuts the cost of breaking cryptocurrency by 20x without handing attackers the circuit. We found anyone could forge a “proof” of an even stronger attack. 🧵


---

## 2026-04-07 · Post · Before its launch, we audited @whatsapp's Private Processing TEEs and found 8 high-severity issues (


Tags (automatic): TEE / enclave


### Post — @trailofbits — 2026-04-07 11:02 UTC (2026-04-07 12:02 WAT)

- URL: https://x.com/trailofbits/status/2041471550881153077
- Metrics (at fetch): bookmark 87, impression 40883, like 232, quote 7, reply 5, retweet 35

> Before its launch, we audited @whatsapp's Private Processing TEEs and found 8 high-severity issues (patched). The enclaves yielded to injected config files, unmeasured ACPI tables, spoofed firmware levels, and stale attestation reports. 🧵


---

## 2026-04-01 · Post · We saw high coverage mask a fund-draining vulnerability, and caught it with mutation testing. Then w


### Post — @trailofbits — 2026-04-01 11:11 UTC (2026-04-01 12:11 WAT)

- URL: https://x.com/trailofbits/status/2039299518483595480
- Metrics (at fetch): bookmark 16, impression 3951, like 41, quote 0, reply 3, retweet 1

> We saw high coverage mask a fund-draining vulnerability, and caught it with mutation testing. Then we built the tools to make this routine. 🧵


---

## 2026-03-11 · Post · A single bug in an ERC-4337 smart account can be as catastrophic as leaking a private key.


### Post — @trailofbits — 2026-03-11 13:02 UTC (2026-03-11 14:02 WAT)

- URL: https://x.com/trailofbits/status/2031717351607910890
- Metrics (at fetch): bookmark 61, impression 5401, like 66, quote 1, reply 4, retweet 10

> A single bug in an ERC-4337 smart account can be as catastrophic as leaking a private key.
>
> We've audited dozens of smart accounts and found six vulnerability patterns that consistently reappear across codebases. 🧵 [pic.x.com/z4REj3P8X6]

**Media:**
- photo: https://pbs.twimg.com/media/HDIcKhBXsAAd9pl.jpg — no alt text provided by author


---

## 2026-01-16 · Post · We just published Slither 0.11.5 which contains a new detector that can identify the reentrancy bug 


Tags (automatic): Smart contract / DeFi, AI-assisted hunting


### Post — @trailofbits — 2026-01-16 20:53 UTC (2026-01-16 21:53 WAT)

- URL: https://x.com/trailofbits/status/2012266921052488079
- Metrics (at fetch): bookmark 55, impression 14877, like 123, quote 0, reply 2, retweet 12

> We just published Slither 0.11.5 which contains a new detector that can identify the reentrancy bug used in this hack.
>
> This release also contains changes to allow more effective use of AI coding tools, making it easier and faster for us (or your team!) to write new detectors in https://twitter.com/Phalcon_xyz/status/2011404828115866061

**Links in post:** https://twitter.com/Phalcon_xyz/status/2011404828115866061

**Quoted post** 2011404828115866061: not readable via the API (deleted, private, or withheld).


---

## 2026-01-01 · Post · December Tribune: Constant-time coding support for LLVM,  and cryptography webinars. https://mailchi


### Post — @trailofbits — 2026-01-01 12:15 UTC (2026-01-01 13:15 WAT)

- URL: https://x.com/trailofbits/status/2006700697924890678
- Metrics (at fetch): bookmark 7, impression 5523, like 21, quote 0, reply 1, retweet 0

> December Tribune: Constant-time coding support for LLVM,  and cryptography webinars. https://mailchi.mp/trailofbits/december-2025-tribune

**Links in post:** https://mailchi.mp/trailofbits/december-2025-tribune


---

## 2025-12-18 · Post · Webinar starting in 1 hour


Tags (automatic): TEE / enclave


### Post — @trailofbits — 2025-12-18 15:03 UTC (2025-12-18 16:03 WAT)

- URL: https://x.com/trailofbits/status/2001669732655599808
- Metrics (at fetch): bookmark 11, impression 3915, like 21, quote 0, reply 0, retweet 2

> Webinar starting in 1 hour
> What you'll learn: 
> ✓ How to assess TEE security frameworks 
> ✓ Where confidential computing implementations fail 
> ✓ Real vulnerability patterns from production audits 
> Live with @tinfoilAI at 11 AM ET:
> https://watch.getcontrast.io/register/trail-of-bits-top-tee-bugs-you-should-fix-before-your-audit?utm_source=socials

**Links in post:** https://watch.getcontrast.io/register/trail-of-bits-top-tee-bugs-you-should-fix-before-your-audit?utm_source=socials


---

## 2025-12-16 · Post · Memory safety bugs are the most exploited vulnerability class, but AddressSanitizer is not designed 


Tags (automatic): Memory corruption / native


### Post — @trailofbits — 2025-12-16 12:15 UTC (2025-12-16 13:15 WAT)

- URL: https://x.com/trailofbits/status/2000902493228642495
- Metrics (at fetch): bookmark 59, impression 10238, like 81, quote 1, reply 4, retweet 6

> Memory safety bugs are the most exploited vulnerability class, but AddressSanitizer is not designed for production use. So, how do you catch use-after-free and buffer overflow bugs in live systems? 🧵


---

## 2025-12-13 · Post · Top TEE bugs you should fix before your audit in an upcoming webinar with @TinfoilAI 🧵 [pic.x.com/cn


Tags (automatic): TEE / enclave


### Post — @trailofbits — 2025-12-13 12:22 UTC (2025-12-13 13:22 WAT)

- URL: https://x.com/trailofbits/status/1999817089322807607
- Metrics (at fetch): bookmark 2, impression 5566, like 17, quote 1, reply 1, retweet 2

> Top TEE bugs you should fix before your audit in an upcoming webinar with @TinfoilAI 🧵 [pic.x.com/cn0Df2i7Vk]

**Media:**
- photo: https://pbs.twimg.com/media/G8DHC1OXsAEME6N.jpg — no alt text provided by author


---

## 2025-12-02 · Post · LLVM will soon protect cryptographic code from timing attacks at the compiler level 🧵 [pic.x.com/ZMG


### Post — @trailofbits — 2025-12-02 12:43 UTC (2025-12-02 13:43 WAT)

- URL: https://x.com/trailofbits/status/1995836322917879910
- Metrics (at fetch): bookmark 10, impression 9721, like 69, quote 4, reply 2, retweet 9

> LLVM will soon protect cryptographic code from timing attacks at the compiler level 🧵 [pic.x.com/ZMGlRy6QKi]

**Media:**
- photo: https://pbs.twimg.com/media/G7KijxuXsAAFb0i.jpg — no alt text provided by author


---

## 2025-11-20 · Post · November Tribune: Security behind passports, RCE in AI agents, and post-quantum cryptography 


Tags (automatic): RCE, AI-assisted hunting


### Post — @trailofbits — 2025-11-20 18:06 UTC (2025-11-20 19:06 WAT)

- URL: https://x.com/trailofbits/status/1991568834948657211
- Metrics (at fetch): bookmark 5, impression 4930, like 16, quote 0, reply 0, retweet 5

> November Tribune: Security behind passports, RCE in AI agents, and post-quantum cryptography 
> https://mailchi.mp/trailofbits/trail-of-bits-tribune-november-17475612

**Links in post:** https://mailchi.mp/trailofbits/trail-of-bits-tribune-november-17475612


---

## 2025-11-19 · Post · A summer cryptography intern discovered two vulnerabilities in one of JavaScript's most critical cry


### Post — @trailofbits — 2025-11-19 11:56 UTC (2025-11-19 12:56 WAT)

- URL: https://x.com/trailofbits/status/1991113230953988280
- Metrics (at fetch): bookmark 9, impression 2332, like 23, quote 1, reply 2, retweet 1

> A summer cryptography intern discovered two vulnerabilities in one of JavaScript's most critical cryptographic libraries, elliptic. [pic.x.com/jEHBZ6Xwaw]

**Media:**
- photo: https://pbs.twimg.com/media/G6Ha7pdXQAA6Lx2.jpg — no alt text provided by author


---

## 2025-11-14 · Post · We're releasing open-source @golang implementations of ML-DSA and SLH-DSA, NIST's post-quantum signa


### Post — @trailofbits — 2025-11-14 13:07 UTC (2025-11-14 14:07 WAT)

- URL: https://x.com/trailofbits/status/1989319269302284532
- Metrics (at fetch): bookmark 8, impression 4512, like 53, quote 0, reply 2, retweet 14

> We're releasing open-source @golang implementations of ML-DSA and SLH-DSA, NIST's post-quantum signature algorithms. These libraries are engineered to be constant time, preventing timing side-channel attacks like KyberSlash.


---

## 2025-11-05 · Post · Since the Balancer hack on Monday, we've been working around the clock to help the Balancer team und


### Post — @trailofbits — 2025-11-05 16:02 UTC (2025-11-05 17:02 WAT)

- URL: https://x.com/trailofbits/status/1986101923947200971
- Metrics (at fetch): bookmark 30, impression 44293, like 214, quote 2, reply 6, retweet 12

> Since the Balancer hack on Monday, we've been working around the clock to help the Balancer team understand the bug and its implications. We've verified the bug's cause and have independently verified that the exploit does not work on Balancer V3.
>
> Once the dust settles, we plan


---

## 2025-11-03 · Post · Take your lunch break on November 6th at 12:00 PM ET with us and @appblockchain as we break down rec


Tags (automatic): Blockchain / L1-L2 / bridge, TEE / enclave


### Post — @trailofbits — 2025-11-03 11:47 UTC (2025-11-03 12:47 WAT)

- URL: https://x.com/trailofbits/status/1985312754358522012
- Metrics (at fetch): bookmark 10, impression 4737, like 14, quote 0, reply 4, retweet 6

> Take your lunch break on November 6th at 12:00 PM ET with us and @appblockchain as we break down recent TEE attacks, why they're unpatchable, and what this means for blockchain teams dependent on confidential computing. https://watch.getcontrast.io/register/trail-of-bits-after-wiretap-and-battering-ram-what-changes-for-tee-based-blockchain-infrastructure?utm_source=tb&utm_medium=x

**Links in post:** https://watch.getcontrast.io/register/trail-of-bits-after-wiretap-and-battering-ram-what-changes-for-tee-based-blockchain-infrastructure?utm_source=tb&utm_medium=x


---

## 2025-10-30 · Post · We're spilling the TEE: an attack that extracts all data from 8 confidential computing systems by ch


Tags (automatic): TEE / enclave


### Post — @trailofbits — 2025-10-30 11:32 UTC (2025-10-30 12:32 WAT)

- URL: https://x.com/trailofbits/status/1983859501863174179
- Metrics (at fetch): bookmark 11, impression 2758, like 20, quote 0, reply 2, retweet 4

> We're spilling the TEE: an attack that extracts all data from 8 confidential computing systems by changing one field in LUKS2's metadata header 🧵 (CVE-2025-59054 and CVE-2025-58356) [pic.x.com/FE3cDU5Rvd]

**Media:**
- photo: https://pbs.twimg.com/media/G4gVs_lXgAALuvn.jpg — no alt text provided by author


---

## 2025-10-28 · Post · Confidential computing promises isolated execution, but physical attacks are breaking that guarantee


Tags (automatic): Blockchain / L1-L2 / bridge, TEE / enclave


### Post — @trailofbits — 2025-10-28 09:32 UTC (2025-10-28 10:32 WAT)

- URL: https://x.com/trailofbits/status/1983104461426880718
- Metrics (at fetch): bookmark 1, impression 1940, like 6, quote 0, reply 1, retweet 1

> Confidential computing promises isolated execution, but physical attacks are breaking that guarantee. Trail of Bits and @appblockchain explain how $50 hardware compromises Intel SGX and AMD SEV-SNP and what blockchain devs need to know moving forward. Nov 6, 12 PM ET. 🧵 [pic.x.com/PZZinDqp7u]

**Media:**
- photo: https://pbs.twimg.com/media/G4Vm_1AXkAAiaYh.jpg — no alt text provided by author


---

## 2025-10-21 · Post · With just $50 in hardware, attackers can extract attestation keys, view encrypted data, and tamper w


Tags (automatic): TEE / enclave


### Post — @trailofbits — 2025-10-21 10:20 UTC (2025-10-21 11:20 WAT)

- URL: https://x.com/trailofbits/status/1980579827733106828
- Metrics (at fetch): bookmark 6, impression 2671, like 20, quote 0, reply 1, retweet 7

> With just $50 in hardware, attackers can extract attestation keys, view encrypted data, and tamper with confidential workloads in Intel SGX and AMD SEV-SNP. 🧵 [pic.x.com/C4bje6geZB]

**Media:**
- photo: https://pbs.twimg.com/media/G3xu23mXkAA7M26.jpg — no alt text provided by author


---

## 2025-10-15 · Post · Today (4:00 PM GMT+2) @objective_see: Paweł Płatek shows a user-to-root exploit on modern macOS by c


### Post — @trailofbits — 2025-10-15 10:45 UTC (2025-10-15 11:45 WAT)

- URL: https://x.com/trailofbits/status/1978411831816282458
- Metrics (at fetch): bookmark 11, impression 4567, like 38, quote 0, reply 2, retweet 10

> Today (4:00 PM GMT+2) @objective_see: Paweł Płatek shows a user-to-root exploit on modern macOS by chaining bugs in mDNSResponder and traceroute6. Learn new libmalloc exploitation techniques and PAC bypass methods. 
> https://objectivebythesea.org/v8/ [pic.x.com/Kyfg0oP9HV]

**Media:**
- photo: https://pbs.twimg.com/media/G3S7E5KXUAAq9Xb.jpg — no alt text provided by author

**Links in post:** https://objectivebythesea.org/v8/


---

## 2025-10-08 · Post · On @SecWeekly 342, Will Vandevanter discusses two of our recent NVIDIA Triton Inference Server disc


### Post — @trailofbits — 2025-10-08 13:55 UTC (2025-10-08 14:55 WAT)

- URL: https://x.com/trailofbits/status/1975922904857514057
- Metrics (at fetch): bookmark 5, impression 2206, like 12, quote 0, reply 2, retweet 2

> On @SecWeekly #342, Will Vandevanter discusses two of our recent NVIDIA Triton Inference Server disclosures (CVE-2025-23310 and CVE-2025-23311) and their impact on ML security:
> https://www.youtube.com/watch?v=C2kSdo7aNzU [pic.x.com/UDmvqdytVK]

**Media:**
- photo: https://pbs.twimg.com/media/G2vjaSaWwAAG51W.jpg — no alt text provided by author

**Links in post:** https://www.youtube.com/watch?v=C2kSdo7aNzU


---

## 2025-09-30 · Post · We contributed upstream CodeQL query improvements to drastically improve SQL vulnerability detection


### Post — @trailofbits — 2025-09-30 12:47 UTC (2025-09-30 13:47 WAT)

- URL: https://x.com/trailofbits/status/1973006668859330930
- Metrics (at fetch): bookmark 6, impression 1649, like 9, quote 0, reply 2, retweet 1

> We contributed upstream CodeQL query improvements to drastically improve SQL vulnerability detection. Check them out ⬇️
> https://github.com/github/codeql/pulls?q=is%3Apr+author%3AVasco-jofra+is%3Aclosed

**Links in post:** https://github.com/github/codeql/pulls?q=is%3Apr+author%3AVasco-jofra+is%3Aclosed


---

## 2025-08-19 · Post · We won second place in @DARPA's AI Cyber Challenge. Plus, GitHub Copilot prompt injections, NVIDIA T


Tags (automatic): AI-assisted hunting


### Post — @trailofbits — 2025-08-19 11:04 UTC (2025-08-19 12:04 WAT)

- URL: https://x.com/trailofbits/status/1957760550491836783
- Metrics (at fetch): bookmark 31, impression 9313, like 73, quote 0, reply 1, retweet 8

> We won second place in @DARPA's AI Cyber Challenge. Plus, GitHub Copilot prompt injections, NVIDIA Triton vulnerability disclosure, and multi-agent system hijacking demos. Read our AI-packed Tribune: https://mailchi.mp/trailofbits/trail-of-bits-tribune-august

**Links in post:** https://mailchi.mp/trailofbits/trail-of-bits-tribune-august


---

## 2025-08-05 · Post · Today, we’re disclosing two 9.8 CVSS memory corruption vulnerabilities in the @NVIDIA Triton Inferen


Tags (automatic): AI-assisted hunting


### Post — @trailofbits — 2025-08-05 11:32 UTC (2025-08-05 12:32 WAT)

- URL: https://x.com/trailofbits/status/1952694252338544804
- Metrics (at fetch): bookmark 18, impression 14196, like 89, quote 3, reply 1, retweet 17

> Today, we’re disclosing two 9.8 CVSS memory corruption vulnerabilities in the @NVIDIA Triton Inference Server that lets attackers crash production AI services through malicious HTTP requests (CVE-2025-23310 and CVE-2025-23311) 🧵


---

## 2025-07-31 · Post · We hijacked multi-agent systems by exploiting how agents communicate with each other! Attackers can 


Tags (automatic): AI-assisted hunting


### Post — @trailofbits — 2025-07-31 15:12 UTC (2025-07-31 16:12 WAT)

- URL: https://x.com/trailofbits/status/1950937549809062244
- Metrics (at fetch): bookmark 9, impression 7041, like 25, quote 1, reply 4, retweet 4

> We hijacked multi-agent systems by exploiting how agents communicate with each other! Attackers can exploit malicious environments, tools, or agents with architectural weaknesses, amplifying attacks across the entire system.🧵 [pic.x.com/hGa0VR44MH]

**Media:**
- video: https://pbs.twimg.com/ext_tw_video_thumb/1950937531551260674/pu/img/haO_IQ6oa98bA-hG.jpg — no alt text provided by author


---

## 2025-07-17 · Post · Pwndbg makes GDB and LLDB debugging actually usable for security research. @disconnect3d_pl shows st


Tags (automatic): Memory corruption / native


### Post — @trailofbits — 2025-07-17 07:06 UTC (2025-07-17 08:06 WAT)

- URL: https://x.com/trailofbits/status/1945741801739931894
- Metrics (at fetch): bookmark 10, impression 2926, like 27, quote 0, reply 0, retweet 6

> Pwndbg makes GDB and LLDB debugging actually usable for security research. @disconnect3d_pl shows stack canary analysis, heap inspection, and exploit development @europython today at 10:30 AM GMT+2
> https://t.co/zBbVawO3Rf
