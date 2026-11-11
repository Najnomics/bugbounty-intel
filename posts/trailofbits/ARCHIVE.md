# @trailofbits — full verbatim X archive (security-relevant posts)

_Generated 2026-11-11 from the X API (full-archive search + timeline). Every post below is copied word-for-word; t.co links are expanded; quoted posts are inlined in full; media are listed with alt text when the author provided it. Posts are grouped by conversation (a thread = the author's root post followed by their own replies, oldest first). Groups are newest first. An agent without X access can rely on this file._

- Posts in this file: 228
- Conversations/threads: 187
- Oldest post captured: 2012-04-03
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

## 2026-07-31 · Thread · PATCH THE PLANET BUG SPOTLIGHT: We found a high-severity use-after-free bug in nginx, the web server


Tags (automatic): Memory corruption / native, AI-assisted hunting


### Post — @trailofbits — 2026-07-31 14:01 UTC (2026-07-31 15:01 WAT)

- URL: https://x.com/trailofbits/status/2083191391358702029
- Metrics (at fetch): bookmark 15, impression 7548, like 78, quote 0, reply 2, retweet 3

> PATCH THE PLANET BUG SPOTLIGHT: We found a high-severity use-after-free bug in nginx, the web server handling over 30% of all websites in the world. Now patched.


### Thread part 2 — @trailofbits — 2026-07-31 14:01 UTC (2026-07-31 15:01 WAT)

- URL: https://x.com/trailofbits/status/2083191392390570059
- Metrics (at fetch): bookmark 4, impression 1659, like 10, quote 2, reply 0, retweet 3

> Remote and unauthenticated, it can crash nginx and potentially run code, all through HTTP/3. Engineer Evan Hellman found it with Codex after roughly 14 hours of automated analysis. CVE-2026-42530 in the dashboard: https://trailofbits.com/patch-the-planet/dashboard/

**Links in post:** https://trailofbits.com/patch-the-planet/dashboard/


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

## 2026-06-30 · Thread · 1.2 billion downloads ran through pyca/cryptography last month. Nearly every Python app that touches


### Post — @trailofbits — 2026-06-30 11:15 UTC (2026-06-30 12:15 WAT)

- URL: https://x.com/trailofbits/status/2071915420584411634
- Metrics (at fetch): bookmark 13, impression 6493, like 48, quote 0, reply 2, retweet 4

> 1.2 billion downloads ran through pyca/cryptography last month. Nearly every Python app that touches crypto depends on it. If it doesn't ship post-quantum primitives, the Python ecosystem can't migrate. 🧵


### Thread part 2 — @trailofbits — 2026-06-30 11:15 UTC (2026-06-30 12:15 WAT)

- URL: https://x.com/trailofbits/status/2071915421544960263
- Metrics (at fetch): bookmark 3, impression 1391, like 17, quote 1, reply 1, retweet 3

> We helped add ML-DSA and ML-KEM, NIST's post-quantum standards for signatures and key exchange, to the library. Install and migration details in the blog. https://blog.trailofbits.com/2026/06/30/shipping-post-quantum-cryptography-to-python/

**Links in post:** https://blog.trailofbits.com/2026/06/30/shipping-post-quantum-cryptography-to-python/


---

## 2026-06-05 · Thread · We beat Google's quantum circuit again, and we didn't have to forge a proof this time. 


Tags (automatic): ZK


### Post — @trailofbits — 2026-06-05 19:30 UTC (2026-06-05 20:30 WAT)

- URL: https://x.com/trailofbits/status/2062980523232805164
- Metrics (at fetch): bookmark 32, impression 22266, like 116, quote 6, reply 17, retweet 23

> We beat Google's quantum circuit again, and we didn't have to forge a proof this time. 
>
> Today we're releasing trailmix, a toolkit for quantum "kickmix" circuits. It includes 5 new circuits we built for elliptic curve addition, the hardest part of Shor's algorithm. [pic.x.com/X3jYoU5udB]

**Media:**
- photo: https://pbs.twimg.com/media/HKEt2pHWkAABC_7.jpg — no alt text provided by author


### Thread part 2 — @trailofbits — 2026-06-05 19:31 UTC (2026-06-05 20:31 WAT)

- URL: https://x.com/trailofbits/status/2062980524700729693
- Metrics (at fetch): bookmark 6, impression 2628, like 23, quote 1, reply 0, retweet 3

> INRIA researcher André Schrottenloher cracked the code first, but we improved upon his work in just a few days using this toolkit. Our jump-lowqubit circuit beats Google's qubit and gate metrics, and our shrunken-PZ circuit sets a new low-qubit record. https://github.com/trailofbits/trailmix

**Links in post:** https://github.com/trailofbits/trailmix


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

## 2026-05-12 · Thread · Go's fuzzer is missing half the toolkit Rust and C/C++ researchers use every day. gosentry, our fork


Tags (automatic): Race condition


### Post — @trailofbits — 2026-05-12 11:02 UTC (2026-05-12 12:02 WAT)

- URL: https://x.com/trailofbits/status/2054155130052775952
- Metrics (at fetch): bookmark 28, impression 5793, like 49, quote 0, reply 1, retweet 7

> Go's fuzzer is missing half the toolkit Rust and C/C++ researchers use every day. gosentry, our fork of the Go toolchain, brings it inside `go test -fuzz`. 🧵


### Thread part 2 — @trailofbits — 2026-05-12 11:02 UTC (2026-05-12 12:02 WAT)

- URL: https://x.com/trailofbits/status/2054155130732249538
- Metrics (at fetch): bookmark 6, impression 1293, like 6, quote 0, reply 1, retweet 2

> LibAFL underneath, plus Nautilus grammar fuzzing, struct mutation, and race detection. We've already used it to disclose 4 bugs in Optimism and Revm. https://blog.trailofbits.com/2026/05/12/go-fuzzing-was-missing-half-the-toolkit.-we-forked-the-toolchain-to-fix-it./

**Links in post:** https://blog.trailofbits.com/2026/05/12/go-fuzzing-was-missing-half-the-toolkit.-we-forked-the-toolchain-to-fix-it./


---

## 2026-05-05 · Post · 30 readers took our C/C++ challenge. Some solved the Linux warmup, but nobody cracked the Windows dr


### Post — @trailofbits — 2026-05-05 11:02 UTC (2026-05-05 12:02 WAT)

- URL: https://x.com/trailofbits/status/2051618417086525470
- Metrics (at fetch): bookmark 48, impression 13486, like 78, quote 0, reply 3, retweet 11

> 30 readers took our C/C++ challenge. Some solved the Linux warmup, but nobody cracked the Windows driver bug. https://x.com/trailofbits/status/2042253721581871121

**Links in post:** https://x.com/trailofbits/status/2042253721581871121

**Quoted post** 2042253721581871121: not readable via the API (deleted, private, or withheld).


---

## 2026-04-17 · Thread · Google used a ZK proof to disclose a quantum breakthrough that cuts the cost of breaking cryptocurre


Tags (automatic): ZK


### Post — @trailofbits — 2026-04-17 11:02 UTC (2026-04-17 12:02 WAT)

- URL: https://x.com/trailofbits/status/2045095428975104009
- Metrics (at fetch): bookmark 273, impression 81086, like 714, quote 14, reply 14, retweet 90

> Google used a ZK proof to disclose a quantum breakthrough that cuts the cost of breaking cryptocurrency by 20x without handing attackers the circuit. We found anyone could forge a “proof” of an even stronger attack. 🧵


### Thread part 2 — @trailofbits — 2026-04-17 11:02 UTC (2026-04-17 12:02 WAT)

- URL: https://x.com/trailofbits/status/2045095429675552838
- Metrics (at fetch): bookmark 133, impression 56962, like 368, quote 8, reply 5, retweet 47

> The Rust code behind the proof had memory safety bugs. We used this new attack surface to forge a proof that beats Google’s on every metric.
>
> Google patched it within days. Their quantum claims are unaffected. https://blog.trailofbits.com/2026/04/17/we-beat-googles-zero-knowledge-proof-of-quantum-cryptanalysis/

**Links in post:** https://blog.trailofbits.com/2026/04/17/we-beat-googles-zero-knowledge-proof-of-quantum-cryptanalysis/


---

## 2026-04-07 · Thread · Before its launch, we audited @whatsapp's Private Processing TEEs and found 8 high-severity issues (


Tags (automatic): TEE / enclave


### Post — @trailofbits — 2026-04-07 11:02 UTC (2026-04-07 12:02 WAT)

- URL: https://x.com/trailofbits/status/2041471550881153077
- Metrics (at fetch): bookmark 87, impression 40883, like 232, quote 7, reply 5, retweet 35

> Before its launch, we audited @whatsapp's Private Processing TEEs and found 8 high-severity issues (patched). The enclaves yielded to injected config files, unmeasured ACPI tables, spoofed firmware levels, and stale attestation reports. 🧵


### Thread part 2 — @trailofbits — 2026-04-07 11:02 UTC (2026-04-07 12:02 WAT)

- URL: https://x.com/trailofbits/status/2041471551879381088
- Metrics (at fetch): bookmark 39, impression 5030, like 56, quote 1, reply 2, retweet 15

> @WhatsApp TEE security is only as good as the implementation details. Four lessons and the full report: https://blog.trailofbits.com/2026/04/07/what-we-learned-about-tee-security-from-auditing-whatsapps-private-inference/

**Links in post:** https://blog.trailofbits.com/2026/04/07/what-we-learned-about-tee-security-from-auditing-whatsapps-private-inference/


---

## 2026-04-01 · Thread · We saw high coverage mask a fund-draining vulnerability, and caught it with mutation testing. Then w


Tags (automatic): Smart contract / DeFi, Blockchain / L1-L2 / bridge, AI-assisted hunting


### Post — @trailofbits — 2026-04-01 11:11 UTC (2026-04-01 12:11 WAT)

- URL: https://x.com/trailofbits/status/2039299518483595480
- Metrics (at fetch): bookmark 16, impression 3951, like 41, quote 0, reply 3, retweet 1

> We saw high coverage mask a fund-draining vulnerability, and caught it with mutation testing. Then we built the tools to make this routine. 🧵


### Thread part 2 — @trailofbits — 2026-04-01 11:11 UTC (2026-04-01 12:11 WAT)

- URL: https://x.com/trailofbits/status/2039299520186515550
- Metrics (at fetch): bookmark 6, impression 4129, like 11, quote 1, reply 1, retweet 1

> MuTON and mewt introduce bugs, run tests, and find what coverage misses. MuTON supports TON languages, built in collaboration with @ton_blockchain. mewt covers Solidity, Rust, and more. https://blog.trailofbits.com/2026/04/01/mutation-testing-for-the-agentic-era/

**Links in post:** https://blog.trailofbits.com/2026/04/01/mutation-testing-for-the-agentic-era/


---

## 2026-03-11 · Thread · A single bug in an ERC-4337 smart account can be as catastrophic as leaking a private key.


### Post — @trailofbits — 2026-03-11 13:02 UTC (2026-03-11 14:02 WAT)

- URL: https://x.com/trailofbits/status/2031717351607910890
- Metrics (at fetch): bookmark 61, impression 5401, like 66, quote 1, reply 4, retweet 10

> A single bug in an ERC-4337 smart account can be as catastrophic as leaking a private key.
>
> We've audited dozens of smart accounts and found six vulnerability patterns that consistently reappear across codebases. 🧵 [pic.x.com/z4REj3P8X6]

**Media:**
- photo: https://pbs.twimg.com/media/HDIcKhBXsAAd9pl.jpg — no alt text provided by author


### Thread part 2 — @trailofbits — 2026-03-11 13:02 UTC (2026-03-11 14:02 WAT)

- URL: https://x.com/trailofbits/status/2031717352891400628
- Metrics (at fetch): bookmark 9, impression 1189, like 8, quote 0, reply 1, retweet 1

> If you're working with smart accounts, each pattern includes safe code examples so you can reference them for your own implementation: https://blog.trailofbits.com/2026/03/11/six-mistakes-in-erc-4337-smart-accounts/

**Links in post:** https://blog.trailofbits.com/2026/03/11/six-mistakes-in-erc-4337-smart-accounts/


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

## 2025-12-16 · Thread · Memory safety bugs are the most exploited vulnerability class, but AddressSanitizer is not designed 


Tags (automatic): Memory corruption / native


### Post — @trailofbits — 2025-12-16 12:15 UTC (2025-12-16 13:15 WAT)

- URL: https://x.com/trailofbits/status/2000902493228642495
- Metrics (at fetch): bookmark 59, impression 10238, like 81, quote 1, reply 4, retweet 6

> Memory safety bugs are the most exploited vulnerability class, but AddressSanitizer is not designed for production use. So, how do you catch use-after-free and buffer overflow bugs in live systems? 🧵


### Thread part 2 — @trailofbits — 2025-12-16 12:15 UTC (2025-12-16 13:15 WAT)

- URL: https://x.com/trailofbits/status/2000902494612820055
- Metrics (at fetch): bookmark 19, impression 2177, like 35, quote 1, reply 1, retweet 7

> GWP-ASan uses sampling + guard pages to detect memory safety bugs at scale. Learn the technique and how to implement it in your C++ projects using LLVM's scudo allocator: https://blog.trailofbits.com/2025/12/16/use-gwp-asan-to-detect-exploits-in-production-environments/

**Links in post:** https://blog.trailofbits.com/2025/12/16/use-gwp-asan-to-detect-exploits-in-production-environments/


---

## 2025-12-13 · Thread · Top TEE bugs you should fix before your audit in an upcoming webinar with @TinfoilAI 🧵 [pic.x.com/cn


Tags (automatic): TEE / enclave


### Post — @trailofbits — 2025-12-13 12:22 UTC (2025-12-13 13:22 WAT)

- URL: https://x.com/trailofbits/status/1999817089322807607
- Metrics (at fetch): bookmark 2, impression 5566, like 17, quote 1, reply 1, retweet 2

> Top TEE bugs you should fix before your audit in an upcoming webinar with @TinfoilAI 🧵 [pic.x.com/cn0Df2i7Vk]

**Media:**
- photo: https://pbs.twimg.com/media/G8DHC1OXsAEME6N.jpg — no alt text provided by author


### Thread part 2 — @trailofbits — 2025-12-13 12:22 UTC (2025-12-13 13:22 WAT)

- URL: https://x.com/trailofbits/status/1999817091050819813
- Metrics (at fetch): bookmark 3, impression 1136, like 5, quote 0, reply 0, retweet 0

> @TinfoilAI Using @tinfoilAI's infrastructure as a live example, @Julesdrean, @paulbottinelli, and @tjade273 walk through actual confidential computing code, configs, and attestation flows. https://watch.getcontrast.io/register/trail-of-bits-top-tee-bugs-you-should-fix-before-your-audit?utm_source=socials

**Links in post:** https://watch.getcontrast.io/register/trail-of-bits-top-tee-bugs-you-should-fix-before-your-audit?utm_source=socials


---

## 2025-12-02 · Thread · LLVM will soon protect cryptographic code from timing attacks at the compiler level 🧵 [pic.x.com/ZMG


### Post — @trailofbits — 2025-12-02 12:43 UTC (2025-12-02 13:43 WAT)

- URL: https://x.com/trailofbits/status/1995836322917879910
- Metrics (at fetch): bookmark 10, impression 9721, like 69, quote 4, reply 2, retweet 9

> LLVM will soon protect cryptographic code from timing attacks at the compiler level 🧵 [pic.x.com/ZMGlRy6QKi]

**Media:**
- photo: https://pbs.twimg.com/media/G7KijxuXsAAFb0i.jpg — no alt text provided by author


### Thread part 2 — @trailofbits — 2025-12-02 12:43 UTC (2025-12-02 13:43 WAT)

- URL: https://x.com/trailofbits/status/1995836323920257472
- Metrics (at fetch): bookmark 0, impression 1260, like 7, quote 0, reply 0, retweet 4

> The compiler translates __builtin_ct_select across multiple architectures (x86-64, i386, ARM, AArch64) to appropriate constant-time implementations using native instructions, such as cmov or CSEL, where available, or masked arithmetic patterns elsewhere. https://blog.trailofbits.com/2025/12/02/introducing-constant-time-support-for-llvm-to-protect-cryptographic-code/

**Links in post:** https://blog.trailofbits.com/2025/12/02/introducing-constant-time-support-for-llvm-to-protect-cryptographic-code/


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

## 2025-11-19 · Thread · A summer cryptography intern discovered two vulnerabilities in one of JavaScript's most critical cry


### Post — @trailofbits — 2025-11-19 11:56 UTC (2025-11-19 12:56 WAT)

- URL: https://x.com/trailofbits/status/1991113230953988280
- Metrics (at fetch): bookmark 9, impression 2332, like 23, quote 1, reply 2, retweet 1

> A summer cryptography intern discovered two vulnerabilities in one of JavaScript's most critical cryptographic libraries, elliptic. [pic.x.com/jEHBZ6Xwaw]

**Media:**
- photo: https://pbs.twimg.com/media/G6Ha7pdXQAA6Lx2.jpg — no alt text provided by author


### Thread part 2 — @trailofbits — 2025-11-19 11:56 UTC (2025-11-19 12:56 WAT)

- URL: https://x.com/trailofbits/status/1991113232367370451
- Metrics (at fetch): bookmark 0, impression 1209, like 3, quote 0, reply 1, retweet 1

> Both vulnerabilities were caught using Wycheproof test vectors, standardized cryptography tests that every library should run, but many skip. 
> https://blog.trailofbits.com/2025/11/18/we-found-cryptography-bugs-in-the-elliptic-library-using-wycheproof/

**Links in post:** https://blog.trailofbits.com/2025/11/18/we-found-cryptography-bugs-in-the-elliptic-library-using-wycheproof/


### Thread part 3 — @trailofbits — 2025-11-19 11:56 UTC (2025-11-19 12:56 WAT)

- URL: https://x.com/trailofbits/status/1991113233386606812
- Metrics (at fetch): bookmark 2, impression 1149, like 5, quote 0, reply 1, retweet 1

> Big lesson: cryptography libraries have inconsistent application of continuous cryptographic testing. The Wycheproof chapter in our Testing Handbook teaches you how to implement these tests in your CI/CD pipeline. https://appsec.guide/docs/crypto/wycheproof/

**Links in post:** https://appsec.guide/docs/crypto/wycheproof/


---

## 2025-11-14 · Thread · We're releasing open-source @golang implementations of ML-DSA and SLH-DSA, NIST's post-quantum signa


### Post — @trailofbits — 2025-11-14 13:07 UTC (2025-11-14 14:07 WAT)

- URL: https://x.com/trailofbits/status/1989319269302284532
- Metrics (at fetch): bookmark 8, impression 4512, like 53, quote 0, reply 2, retweet 14

> We're releasing open-source @golang implementations of ML-DSA and SLH-DSA, NIST's post-quantum signature algorithms. These libraries are engineered to be constant time, preventing timing side-channel attacks like KyberSlash.


### Thread part 2 — @trailofbits — 2025-11-14 13:07 UTC (2025-11-14 14:07 WAT)

- URL: https://x.com/trailofbits/status/1989319270611013794
- Metrics (at fetch): bookmark 6, impression 1345, like 8, quote 0, reply 0, retweet 2

> Constant-time means no branches on secret data and no variable-time division. We use Barrett reduction with precomputed reciprocals to eliminate timing vulnerabilities in cryptographic operations: https://blog.trailofbits.com/2025/11/14/how-we-avoided-side-channels-in-our-new-post-quantum-go-cryptography-libraries/

**Links in post:** https://blog.trailofbits.com/2025/11/14/how-we-avoided-side-channels-in-our-new-post-quantum-go-cryptography-libraries/


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

## 2025-10-30 · Thread · We're spilling the TEE: an attack that extracts all data from 8 confidential computing systems by ch


Tags (automatic): TEE / enclave


### Post — @trailofbits — 2025-10-30 11:32 UTC (2025-10-30 12:32 WAT)

- URL: https://x.com/trailofbits/status/1983859501863174179
- Metrics (at fetch): bookmark 11, impression 2758, like 20, quote 0, reply 2, retweet 4

> We're spilling the TEE: an attack that extracts all data from 8 confidential computing systems by changing one field in LUKS2's metadata header 🧵 (CVE-2025-59054 and CVE-2025-58356) [pic.x.com/FE3cDU5Rvd]

**Media:**
- photo: https://pbs.twimg.com/media/G4gVs_lXgAALuvn.jpg — no alt text provided by author


### Thread part 2 — @trailofbits — 2025-10-30 11:32 UTC (2025-10-30 12:32 WAT)

- URL: https://x.com/trailofbits/status/1983859502874005953
- Metrics (at fetch): bookmark 0, impression 721, like 3, quote 1, reply 1, retweet 2

> LUKS2 stores its encryption config in a JSON header on the disk itself. An attacker with write access changes "aes-xts-plain64" to "cipher_null-ecb", which does nothing. The CVM boots as if the disk was still encrypted. https://blog.trailofbits.com/2025/10/30/vulnerabilities-in-luks2-disk-encryption-for-confidential-vms/ [pic.x.com/mXTlvD04RF]

**Media:**
- photo: https://pbs.twimg.com/media/G4gVtB8W0AArWd-.jpg — no alt text provided by author

**Links in post:** https://blog.trailofbits.com/2025/10/30/vulnerabilities-in-luks2-disk-encryption-for-confidential-vms/


### Thread part 3 — @trailofbits — 2025-10-30 11:32 UTC (2025-10-30 12:32 WAT)

- URL: https://x.com/trailofbits/status/1983859504186831059
- Metrics (at fetch): bookmark 0, impression 395, like 1, quote 0, reply 1, retweet 1

> CVE-2025-59054 and CVE-2025-58356 affect LUKS2 disk encryption in confidential VMs from Oasis, Phala, Flashbots, Secret Network, Fortanix, Edgeless, and Cosmian. All 8 affected projects are now patched.


### Thread part 4 — @trailofbits — 2025-10-30 11:32 UTC (2025-10-30 12:32 WAT)

- URL: https://x.com/trailofbits/status/1983859504983761097
- Metrics (at fetch): bookmark 2, impression 1247, like 4, quote 0, reply 1, retweet 1

> The fix: validate headers before use. [pic.x.com/QPWKsB5eSQ]

**Media:**
- photo: https://pbs.twimg.com/media/G4gVs93WIAABaSw.jpg — no alt text provided by author


### Thread part 5 — @trailofbits — 2025-10-30 11:32 UTC (2025-10-30 12:32 WAT)

- URL: https://x.com/trailofbits/status/1983859505961021748
- Metrics (at fetch): bookmark 0, impression 1163, like 2, quote 0, reply 0, retweet 1

> If you're building confidential computing systems and want to avoid similar footguns, contact us for a free one-hour office hours with our engineers:
> https://share.hsforms.com/1VVGPLTjiRduOpGNOh2sHUgdffjk

**Links in post:** https://share.hsforms.com/1VVGPLTjiRduOpGNOh2sHUgdffjk


---

## 2025-10-28 · Thread · Confidential computing promises isolated execution, but physical attacks are breaking that guarantee


Tags (automatic): Blockchain / L1-L2 / bridge, TEE / enclave


### Post — @trailofbits — 2025-10-28 09:32 UTC (2025-10-28 10:32 WAT)

- URL: https://x.com/trailofbits/status/1983104461426880718
- Metrics (at fetch): bookmark 1, impression 1940, like 6, quote 0, reply 1, retweet 1

> Confidential computing promises isolated execution, but physical attacks are breaking that guarantee. Trail of Bits and @appblockchain explain how $50 hardware compromises Intel SGX and AMD SEV-SNP and what blockchain devs need to know moving forward. Nov 6, 12 PM ET. 🧵 [pic.x.com/PZZinDqp7u]

**Media:**
- photo: https://pbs.twimg.com/media/G4Vm_1AXkAAiaYh.jpg — no alt text provided by author


### Thread part 2 — @trailofbits — 2025-10-28 09:32 UTC (2025-10-28 10:32 WAT)

- URL: https://x.com/trailofbits/status/1983104462911570351
- Metrics (at fetch): bookmark 0, impression 1313, like 3, quote 0, reply 0, retweet 1

> @AppBlockchain Register here: https://watch.getcontrast.io/register/trail-of-bits-after-wiretap-and-battering-ram-what-changes-for-tee-based-blockchain-infrastructure?utm_source=tb&utm_medium=x [pic.x.com/Jb2tUHMEmA]

**Media:**
- photo: https://pbs.twimg.com/media/G4Vm_4XWAAAUNdu.jpg — no alt text provided by author

**Links in post:** https://watch.getcontrast.io/register/trail-of-bits-after-wiretap-and-battering-ram-what-changes-for-tee-based-blockchain-infrastructure?utm_source=tb&utm_medium=x


---

## 2025-10-21 · Thread · With just $50 in hardware, attackers can extract attestation keys, view encrypted data, and tamper w


Tags (automatic): Blockchain / L1-L2 / bridge, TEE / enclave


### Post — @trailofbits — 2025-10-21 10:20 UTC (2025-10-21 11:20 WAT)

- URL: https://x.com/trailofbits/status/1980579827733106828
- Metrics (at fetch): bookmark 6, impression 2671, like 20, quote 0, reply 1, retweet 7

> With just $50 in hardware, attackers can extract attestation keys, view encrypted data, and tamper with confidential workloads in Intel SGX and AMD SEV-SNP. 🧵 [pic.x.com/C4bje6geZB]

**Media:**
- photo: https://pbs.twimg.com/media/G3xu23mXkAA7M26.jpg — no alt text provided by author


### Thread part 2 — @trailofbits — 2025-10-21 10:20 UTC (2025-10-21 11:20 WAT)

- URL: https://x.com/trailofbits/status/1980579828886634574
- Metrics (at fetch): bookmark 4, impression 1333, like 7, quote 0, reply 0, retweet 2

> Trail of Bits and @appblockchain explain how Wiretap and DRAM aliasing attacks work, why they're unpatchable, and what this means for confidential computing in blockchain infrastructure. Nov 6, 12 PM ET. https://watch.getcontrast.io/register/trail-of-bits-after-wiretap-and-battering-ram-what-changes-for-tee-based-blockchain-infrastructure?utm_source=tb&utm_medium=x

**Links in post:** https://watch.getcontrast.io/register/trail-of-bits-after-wiretap-and-battering-ram-what-changes-for-tee-based-blockchain-infrastructure?utm_source=tb&utm_medium=x


---

## 2025-10-15 · Thread · Today (4:00 PM GMT+2) @objective_see: Paweł Płatek shows a user-to-root exploit on modern macOS by c


### Post — @trailofbits — 2025-10-15 10:45 UTC (2025-10-15 11:45 WAT)

- URL: https://x.com/trailofbits/status/1978411831816282458
- Metrics (at fetch): bookmark 11, impression 4567, like 38, quote 0, reply 2, retweet 10

> Today (4:00 PM GMT+2) @objective_see: Paweł Płatek shows a user-to-root exploit on modern macOS by chaining bugs in mDNSResponder and traceroute6. Learn new libmalloc exploitation techniques and PAC bypass methods. 
> https://objectivebythesea.org/v8/ [pic.x.com/Kyfg0oP9HV]

**Media:**
- photo: https://pbs.twimg.com/media/G3S7E5KXUAAq9Xb.jpg — no alt text provided by author

**Links in post:** https://objectivebythesea.org/v8/


### Thread part 2 — @trailofbits — 2025-10-15 14:44 UTC (2025-10-15 15:44 WAT)

- URL: https://x.com/trailofbits/status/1978472124563194019
- Metrics (at fetch): bookmark 2, impression 1394, like 2, quote 0, reply 0, retweet 1

> Correction: talk is tomorrow at 4:00 GMT+2 and will be live streamed at https://www.youtube.com/@objectiveseefoundation

**Links in post:** https://www.youtube.com/@objectiveseefoundation


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

## 2025-08-05 · Thread · Today, we’re disclosing two 9.8 CVSS memory corruption vulnerabilities in the @NVIDIA Triton Inferen


Tags (automatic): RCE, Memory corruption / native, AI-assisted hunting


### Post — @trailofbits — 2025-08-05 11:32 UTC (2025-08-05 12:32 WAT)

- URL: https://x.com/trailofbits/status/1952694252338544804
- Metrics (at fetch): bookmark 18, impression 14196, like 89, quote 3, reply 1, retweet 17

> Today, we’re disclosing two 9.8 CVSS memory corruption vulnerabilities in the @NVIDIA Triton Inference Server that lets attackers crash production AI services through malicious HTTP requests (CVE-2025-23310 and CVE-2025-23311) 🧵


### Thread part 2 — @trailofbits — 2025-08-05 11:32 UTC (2025-08-05 12:32 WAT)

- URL: https://x.com/trailofbits/status/1952694253211017600
- Metrics (at fetch): bookmark 11, impression 1498, like 19, quote 0, reply 1, retweet 5

> @nvidia Found during new hire onboarding, our AI/ML Security Engineer, Will Vandevanter, followed our standard static analysis approach against Pwn2Own 2025 targets. https://blog.trailofbits.com/2025/08/04/uncovering-memory-corruption-in-nvidia-triton-as-a-new-hire/ [pic.x.com/B0EOUSGJ61]

**Media:**
- photo: https://pbs.twimg.com/media/GxldEumXgAAoypA.jpg — no alt text provided by author

**Links in post:** https://blog.trailofbits.com/2025/08/04/uncovering-memory-corruption-in-nvidia-triton-as-a-new-hire/


### Thread part 3 — @trailofbits — 2025-08-05 11:32 UTC (2025-08-05 12:32 WAT)

- URL: https://x.com/trailofbits/status/1952694254729359462
- Metrics (at fetch): bookmark 1, impression 624, like 3, quote 0, reply 1, retweet 1

> @nvidia Step one: point @Semgrep at the codebase using community rulesets from the Trail of Bits Testing Handbook. https://appsec.guide/docs/static-analysis/semgrep/

**Links in post:** https://appsec.guide/docs/static-analysis/semgrep/


### Thread part 4 — @trailofbits — 2025-08-05 11:32 UTC (2025-08-05 12:32 WAT)

- URL: https://x.com/trailofbits/status/1952694255744356568
- Metrics (at fetch): bookmark 1, impression 536, like 2, quote 0, reply 1, retweet 1

> @nvidia @semgrep This Semgrep rule flagged unsafe alloca() patterns in Triton's HTTP code. The 0xdea ruleset caught what manual review might miss: stack allocation controlled by HTTP requests. [pic.x.com/U5ZO6nSrlY]

**Media:**
- photo: https://pbs.twimg.com/media/GxldEuoXAAARNYm.jpg — no alt text provided by author


### Thread part 5 — @trailofbits — 2025-08-05 11:32 UTC (2025-08-05 12:32 WAT)

- URL: https://x.com/trailofbits/status/1952694257254379620
- Metrics (at fetch): bookmark 0, impression 467, like 0, quote 0, reply 1, retweet 1

> Here's how it works: malicious HTTP requests use chunked encoding to fragment data across many segments. This forces alloca() to allocate stack space based on attacker-controlled input, leading to a stack-based buffer overflow, which can crash the server. With the help of CVE-2025-23334 from @wiz_io, stack-based buffer overflows have the potential to lead to Remote Code Execution (RCE).


### Thread part 6 — @trailofbits — 2025-08-05 11:32 UTC (2025-08-05 12:32 WAT)

- URL: https://x.com/trailofbits/status/1952694258177016223
- Metrics (at fetch): bookmark 0, impression 437, like 0, quote 0, reply 1, retweet 1

> @nvidia @semgrep Affects core Triton HTTP endpoints, including inference requests and repository operations. Since authentication is optional and disabled by default, any exposed Triton deployment becomes a target for service disruption attacks.


### Thread part 7 — @trailofbits — 2025-08-05 11:32 UTC (2025-08-05 12:32 WAT)

- URL: https://x.com/trailofbits/status/1952694259166953857
- Metrics (at fetch): bookmark 0, impression 1620, like 2, quote 0, reply 1, retweet 1

> @nvidia @semgrep .@NVIDIA confirmed and patched both issues, replacing unsafe stack allocation with heap-based allocation and proper error handling. Upgrade to the latest Triton release when available to protect your AI infrastructure. https://github.com/triton-inference-server/server/releases/tag/v2.59.1

**Links in post:** https://github.com/triton-inference-server/server/releases/tag/v2.59.1


### Thread part 8 — @trailofbits — 2025-08-05 11:32 UTC (2025-08-05 12:32 WAT)

- URL: https://x.com/trailofbits/status/1952694260173554002
- Metrics (at fetch): bookmark 1, impression 1477, like 3, quote 0, reply 0, retweet 1

> @nvidia @semgrep Running or building AI/ML infrastructure? Our team specializes in securing AI systems from model training to inference deployment and beyond. Contact us to assess your AI security posture before attackers find and exploit such vulnerabilities.
> https://www.trailofbits.com/contact/

**Links in post:** https://www.trailofbits.com/contact/


---

## 2025-07-31 · Thread · We hijacked multi-agent systems by exploiting how agents communicate with each other! Attackers can 


Tags (automatic): AI-assisted hunting


### Post — @trailofbits — 2025-07-31 15:12 UTC (2025-07-31 16:12 WAT)

- URL: https://x.com/trailofbits/status/1950937549809062244
- Metrics (at fetch): bookmark 9, impression 7041, like 25, quote 1, reply 4, retweet 4

> We hijacked multi-agent systems by exploiting how agents communicate with each other! Attackers can exploit malicious environments, tools, or agents with architectural weaknesses, amplifying attacks across the entire system.🧵 [pic.x.com/hGa0VR44MH]

**Media:**
- video: https://pbs.twimg.com/ext_tw_video_thumb/1950937531551260674/pu/img/haO_IQ6oa98bA-hG.jpg — no alt text provided by author


### Thread part 2 — @trailofbits — 2025-07-31 15:12 UTC (2025-07-31 16:12 WAT)

- URL: https://x.com/trailofbits/status/1950937550903795874
- Metrics (at fetch): bookmark 1, impression 1153, like 6, quote 0, reply 1, retweet 1

> Reproduce our attacks with pajaMAS! These demos teach critical MAS security principles: privilege separation, trust validation, and secure control flows.
> https://github.com/trailofbits/pajaMAS

**Links in post:** https://github.com/trailofbits/pajaMAS


### Thread part 3 — @trailofbits — 2025-07-31 15:12 UTC (2025-07-31 16:12 WAT)

- URL: https://x.com/trailofbits/status/1950937551860072522
- Metrics (at fetch): bookmark 3, impression 1287, like 2, quote 0, reply 0, retweet 0

> Beyond demos, we created comprehensive guidance for developing secure-by-design MASs. If you've decided a MAS is necessary, start here:
> https://blog.trailofbits.com/2025/07/31/hijacking-multi-agent-systems-in-your-pajamas/

**Links in post:** https://blog.trailofbits.com/2025/07/31/hijacking-multi-agent-systems-in-your-pajamas/


---

## 2025-07-17 · Post · Pwndbg makes GDB and LLDB debugging actually usable for security research. @disconnect3d_pl shows st


Tags (automatic): Memory corruption / native


### Post — @trailofbits — 2025-07-17 07:06 UTC (2025-07-17 08:06 WAT)

- URL: https://x.com/trailofbits/status/1945741801739931894
- Metrics (at fetch): bookmark 10, impression 2926, like 27, quote 0, reply 0, retweet 6

> Pwndbg makes GDB and LLDB debugging actually usable for security research. @disconnect3d_pl shows stack canary analysis, heap inspection, and exploit development @europython today at 10:30 AM GMT+2
> https://t.co/zBbVawO3Rf


---

## 2025-06-18 · Post · Three unexpected attack scenarios:


### Post — @trailofbits — 2025-06-18 11:23 UTC (2025-06-18 12:23 WAT)

- URL: https://x.com/trailofbits/status/1935297340497187230
- Metrics (at fetch): bookmark 94, impression 21266, like 133, quote 2, reply 2, retweet 35

> Three unexpected attack scenarios:
> 1. Marshaling private data with misconfigured tags
> 2. Parser differentials in a microservices architecture
> 3. Cross-format confusion attacks (JSON→XML)
> https://t.co/2IpN8pvVI0


---

## 2025-04-24 · Post · MCP Vulnerability: AI systems can be manipulated to silently leak your entire conversation history t


Tags (automatic): AI-assisted hunting


### Post — @trailofbits — 2025-04-24 15:46 UTC (2025-04-24 16:46 WAT)

- URL: https://x.com/trailofbits/status/1915432077727600917
- Metrics (at fetch): bookmark 82, impression 22399, like 171, quote 8, reply 5, retweet 38

> MCP Vulnerability: AI systems can be manipulated to silently leak your entire conversation history to malicious servers. https://t.co/teuv0KYOs1

**Media:**
- photo: https://pbs.twimg.com/media/GpT7UuAWgAEdeRe.jpg — no alt text provided by author


---

## 2025-04-18 · Post · Coming to PyCA Cryptography—a new Rust-powered ASN.1 API that reduces parser differentials while giv


### Post — @trailofbits — 2025-04-18 13:20 UTC (2025-04-18 14:20 WAT)

- URL: https://x.com/trailofbits/status/1913220972888408419
- Metrics (at fetch): bookmark 0, impression 1354, like 8, quote 0, reply 1, retweet 1

> Coming to PyCA Cryptography—a new Rust-powered ASN.1 API that reduces parser differentials while giving you clean Python syntax and native-speed parsing. https://t.co/t1UH6Y1gJa

**Media:**
- photo: https://pbs.twimg.com/media/Go0gVhOXQAAxEg7.jpg — no alt text provided by author


---

## 2025-03-06 · Post · We're sponsoring the inaugural Queer in Cryptography conference! Our crypto team is attending and pr


### Post — @trailofbits — 2025-03-06 16:24 UTC (2025-03-06 17:24 WAT)

- URL: https://x.com/trailofbits/status/1897684803258032381
- Metrics (at fetch): bookmark 2, impression 2541, like 15, quote 0, reply 3, retweet 1

> We're sponsoring the inaugural Queer in Cryptography conference! Our crypto team is attending and presenting; make sure to say "hi"! https://t.co/mV4COFaRCL

**Media:**
- photo: https://pbs.twimg.com/media/GlXt8oAasAAiXXM.jpg — no alt text provided by author


---

## 2025-02-21 · Post · 2 weeks ago at @summit_defi from @Montyly:


Tags (automatic): Smart contract / DeFi


### Post — @trailofbits — 2025-02-21 18:42 UTC (2025-02-21 19:42 WAT)

- URL: https://x.com/trailofbits/status/1893008382677659893
- Metrics (at fetch): bookmark 4, impression 10505, like 41, quote 3, reply 3, retweet 10

> 2 weeks ago at @summit_defi from @Montyly:
> Q: Will we see a billion dollar exploit in 2025?
> A: "If it happens, it won't be a smart contract, it'll be an operational security issue."
> https://t.co/UWMnG92oWA https://t.co/lKETTAOLGL

**Media:**
- video: https://pbs.twimg.com/ext_tw_video_thumb/1893007933153132544/pu/img/xK4akSssuyQq0Vre.jpg — no alt text provided by author

**Quoted post** 1886746705472692675: not readable via the API (deleted, private, or withheld).


---

## 2025-02-06 · Thread · Security teams don't just rely on our audits - they actively use our research to solve complex chall


Tags (automatic): Blockchain / L1-L2 / bridge, TEE / enclave


### Post — @trailofbits — 2025-02-06 15:20 UTC (2025-02-06 16:20 WAT)

- URL: https://x.com/trailofbits/status/1887521655288963421
- Metrics (at fetch): bookmark 3, impression 3061, like 13, quote 2, reply 1, retweet 0

> Security teams don't just rely on our audits - they actively use our research to solve complex challenges. @Turnkeyhq used our TEE, secure enclave, and cryptographic protocol research to inform their development and auditor selection. [pic.x.com/dbzaTHLUcW]

**Media:**
- photo: https://pbs.twimg.com/media/GjHS8TWaMAAY-8h.jpg — no alt text provided by author


### Thread part 2 — @trailofbits — 2025-02-06 15:32 UTC (2025-02-06 16:32 WAT)

- URL: https://x.com/trailofbits/status/1887524687745589612
- Metrics (at fetch): bookmark 2, impression 1069, like 5, quote 0, reply 0, retweet 0

> Complex security requires deep expertise across domains. Combining our AppSec, blockchain, and cryptography knowledge, we helped @turnkeyhq improve their TEE and secure enclave infrastructure: https://resources.trailofbits.com/hubfs/Case%20studies/trailofbits-20250205-turnkey-casestudy.pdf

**Links in post:** https://resources.trailofbits.com/hubfs/Case%20studies/trailofbits-20250205-turnkey-casestudy.pdf


---

## 2025-01-29 · Thread · We are now accepting applications for our annual summer internship in the following areas:


Tags (automatic): Blockchain / L1-L2 / bridge, Memory corruption / native, AI-assisted hunting


### Post — @trailofbits — 2025-01-29 16:43 UTC (2025-01-29 17:43 WAT)

- URL: https://x.com/trailofbits/status/1884643624237097411
- Metrics (at fetch): bookmark 65, impression 14235, like 131, quote 1, reply 4, retweet 13

> We are now accepting applications for our annual summer internship in the following areas:
> • AI/ML
> • Application security
> • Blockchain
> • Cryptography
> • Operations
> Learn more in 🧵 [pic.x.com/oilYQ80JTe]

**Media:**
- photo: https://pbs.twimg.com/media/GieZQO5bAAAFYw1.jpg — no alt text provided by author


### Thread part 2 — @trailofbits — 2025-01-29 16:43 UTC (2025-01-29 17:43 WAT)

- URL: https://x.com/trailofbits/status/1884643625763819587
- Metrics (at fetch): bookmark 12, impression 1474, like 8, quote 0, reply 1, retweet 0

> From June - August, you'll exploit kernel vulnerabilities, develop cryptanalysis tools, enhance AI safety systems, improve Slither and Echidna, or drive strategic initiatives with our CEO. Work on real projects that impact millions.https://apply.workable.com/trailofbits/j/7476E8C7DC/

**Links in post:** https://apply.workable.com/trailofbits/j/7476E8C7DC/


### Thread part 3 — @trailofbits — 2025-01-29 16:43 UTC (2025-01-29 17:43 WAT)

- URL: https://x.com/trailofbits/status/1884643627030466662
- Metrics (at fetch): bookmark 0, impression 1774, like 5, quote 0, reply 0, retweet 0

> Our 2024 interns enhanced PwnDbg and Binary Ninja for reverse engineers, implemented post-quantum cryptography in Rust, and strengthened AI safety frameworks. https://x.com/dguido/status/1823484447062171959

**Links in post:** https://x.com/dguido/status/1823484447062171959

**Quoted post (full text):**

    #### Quoted post — @14290525 — 2024-08-13 22:19 UTC (2024-08-13 23:19 WAT)
    
    - URL: https://x.com/14290525/status/1823484447062171959
    - Metrics (at fetch): bookmark 9, impression 14141, like 44, quote 2, reply 1, retweet 7
    
    > We're setting up for our end-of-summer intern showcase @trailofbits. It's a public event through @empirehacking and I'll be live tweeting some of the takeaways 🧵
    > https://x.com/EmpireHacking/status/1823323369078497630
    
    **Links in post:** https://x.com/EmpireHacking/status/1823323369078497630
    
    **Quoted post** 1823323369078497630: not readable via the API (deleted, private, or withheld).
    


---

## 2025-01-23 · Thread · Our team submitted 750+ pull requests to improve 80+ open-source projects in 2024. These contributio


Tags (automatic): Memory corruption / native


### Post — @trailofbits — 2025-01-23 14:11 UTC (2025-01-23 15:11 WAT)

- URL: https://x.com/trailofbits/status/1882430963679965382
- Metrics (at fetch): bookmark 0, impression 5230, like 54, quote 1, reply 4, retweet 2

> Our team submitted 750+ pull requests to improve 80+ open-source projects in 2024. These contributions strengthen critical security infrastructure, from foundational cryptography libraries to package managers that security engineers rely on daily.


### Thread part 2 — @trailofbits — 2025-01-23 14:28 UTC (2025-01-23 15:28 WAT)

- URL: https://x.com/trailofbits/status/1882435239647363371
- Metrics (at fetch): bookmark 1, impression 1050, like 10, quote 0, reply 0, retweet 1

> Key contributions include:
>  • LLVM gained container overflow detection
>  • pwndbg has an LLDB port and other new features 
> • hevm supports Cancun opcodes
> • we implemented NIST-standardized PQC signature schemes in Rust and Go.
> https://blog.trailofbits.com/2025/01/23/celebrating-our-2024-open-source-contributions/?utm_content=322648478&utm_medium=social&utm_source=linkedin&hss_channel=lcp-912286

**Links in post:** https://blog.trailofbits.com/2025/01/23/celebrating-our-2024-open-source-contributions/?utm_content=322648478&utm_medium=social&utm_source=linkedin&hss_channel=lcp-912286


---

## 2024-12-19 · Thread · Who examines package manager security? We do, as highlighted on @SecWeekly (ASW 311), discussing ou


Tags (automatic): Dependency confusion / supply chain, TEE / enclave


### Post — @trailofbits — 2024-12-19 18:35 UTC (2024-12-19 19:35 WAT)

- URL: https://x.com/trailofbits/status/1869813763928666224
- Metrics (at fetch): bookmark 1, impression 2264, like 5, quote 0, reply 1, retweet 0

> Who examines package manager security? We do, as highlighted on @SecWeekly (ASW #311), discussing our audit of the Ruby central package manager, http://RubyGems.org
> https://youtu.be/6ocFzjANthg?t=1799 [pic.x.com/TVjKdW6qTq]

**Media:**
- video:  — no alt text provided by author

**Links in post:** http://RubyGems.org, https://youtu.be/6ocFzjANthg?t=1799


### Thread part 2 — @trailofbits — 2024-12-20 15:59 UTC (2024-12-20 16:59 WAT)

- URL: https://x.com/trailofbits/status/1870137003746177218
- Metrics (at fetch): bookmark 2, impression 1438, like 4, quote 0, reply 0, retweet 1

> We are advancing packaging security across the Ruby and Python ecosystems:
> • RubyGems: https://blog.trailofbits.com/2024/12/11/auditing-the-ruby-ecosystems-central-package-repository/
> • Trusted publishing in PyPI: https://blog.trailofbits.com/2023/05/23/trusted-publishing-a-new-benchmark-for-packaging-security/
> • Replacing PGP signatures with attestations: https://blog.trailofbits.com/2024/11/14/attestations-a-new-generation-of-signatures-on-pypi/
> • Software supply chain: https://blog.trailofbits.com/2024/10/01/securing-the-software-supply-chain-with-the-slsa-framework/

**Links in post:** https://blog.trailofbits.com/2024/12/11/auditing-the-ruby-ecosystems-central-package-repository/, https://blog.trailofbits.com/2023/05/23/trusted-publishing-a-new-benchmark-for-packaging-security/, https://blog.trailofbits.com/2024/11/14/attestations-a-new-generation-of-signatures-on-pypi/, https://blog.trailofbits.com/2024/10/01/securing-the-software-supply-chain-with-the-slsa-framework/


---

## 2024-11-19 · Post · Fall Tribune: We uncovered security pitfalls in AWS Nitro Enclaves, published our audit of @HuggingF


Tags (automatic): TEE / enclave


### Post — @trailofbits — 2024-11-19 11:59 UTC (2024-11-19 12:59 WAT)

- URL: https://x.com/trailofbits/status/1858842656576594050
- Metrics (at fetch): bookmark 6, impression 10956, like 25, quote 1, reply 0, retweet 4

> Fall Tribune: We uncovered security pitfalls in AWS Nitro Enclaves, published our audit of @HuggingFace's Gradio library, and expanded our Testing Handbook with cryptographic testing guidance.https://t.co/B9nKyQXsc5


---

## 2024-10-31 · Thread · ToB's @arturcygan found code execution and DoS bugs after just a few hours of fuzzing ZBar, an open-


Tags (automatic): RCE


### Post — @trailofbits — 2024-10-31 15:52 UTC (2024-10-31 16:52 WAT)

- URL: https://x.com/trailofbits/status/1852015840008233440
- Metrics (at fetch): bookmark 26, impression 6563, like 71, quote 0, reply 1, retweet 18

> ToB's @arturcygan found code execution and DoS bugs after just a few hours of fuzzing ZBar, an open-source library for reading barcodes.
> tl;dr basic fuzz testing can reveal serious bugs - even in widely used software. https://blog.trailofbits.com/2024/10/31/fuzzing-between-the-lines-in-popular-barcode-software/

**Links in post:** https://blog.trailofbits.com/2024/10/31/fuzzing-between-the-lines-in-popular-barcode-software/


### Thread part 2 — @trailofbits — 2024-10-31 15:52 UTC (2024-10-31 16:52 WAT)

- URL: https://x.com/trailofbits/status/1852015841384055158
- Metrics (at fetch): bookmark 2, impression 1056, like 6, quote 0, reply 0, retweet 3

> @arturcygan Takeaways for security teams:
> - Don't assume popular code has been fuzzed 
> - Start with simple fuzzing harnesses 
> - Build with sanitizers enabled - they catch issues early
> - Limit attack surface by disabling unnecessary features
> - Focus on code that processes untrusted input


---

## 2024-10-10 · Thread · We audited Gradio 5, @HuggingFace's ML GUI framework. Beyond bug-finding, we advised on SDLC enhance


Tags (automatic): SSRF, RCE


### Post — @trailofbits — 2024-10-10 16:22 UTC (2024-10-10 17:22 WAT)

- URL: https://x.com/trailofbits/status/1844413248021356792
- Metrics (at fetch): bookmark 8, impression 19231, like 31, quote 2, reply 1, retweet 6

> We audited Gradio 5, @HuggingFace's ML GUI framework. Beyond bug-finding, we advised on SDLC enhancements: security testing integration, fuzz testing implementation, and deployment streamlining for improved security. https://blog.trailofbits.com/2024/10/10/auditing-gradio-5-hugging-faces-ml-gui-framework/

**Links in post:** https://blog.trailofbits.com/2024/10/10/auditing-gradio-5-hugging-faces-ml-gui-framework/


### Thread part 2 — @trailofbits — 2024-10-10 16:22 UTC (2024-10-10 17:22 WAT)

- URL: https://x.com/trailofbits/status/1844413249199939670
- Metrics (at fetch): bookmark 1, impression 1466, like 3, quote 0, reply 1, retweet 2

> @huggingface Gradio enables ML engineers to create interactive web demos for models with minimal code. It's widely used, powering popular projects like Stable-diffusion-webui and text-generation-webui. 
> https://huggingface.co/blog/gradio-5-security [pic.x.com/8XLhTFacpG]

**Media:**
- photo: https://pbs.twimg.com/media/GZisEvjXUBAvs2A.jpg — no alt text provided by author

**Links in post:** https://huggingface.co/blog/gradio-5-security


### Thread part 3 — @trailofbits — 2024-10-10 16:22 UTC (2024-10-10 17:22 WAT)

- URL: https://x.com/trailofbits/status/1844413251389452789
- Metrics (at fetch): bookmark 0, impression 2250, like 5, quote 0, reply 1, retweet 2

> Our audit uncovered 8 high-severity issues, including an RCE vulnerability on the Gradio API Server, SSRF in server configurations, and arbitrary file leaks. The Gradio team fixed all reported issues in the latest release (Gradio 5), strengthening security across all deployment scenarios.

**Media:**
- photo: https://pbs.twimg.com/media/GZisEv_WsAo75B0.jpg — no alt text provided by author


### Thread part 4 — @trailofbits — 2024-10-10 16:22 UTC (2024-10-10 17:22 WAT)

- URL: https://x.com/trailofbits/status/1844413253146828864
- Metrics (at fetch): bookmark 3, impression 2259, like 6, quote 0, reply 0, retweet 1

> @huggingface For a detailed analysis of our findings and the security enhancements implemented in Gradio 5, read our full report: 
> https://github.com/trailofbits/publications/blob/master/reviews/2024-10-huggingface-gradio-securityreview.pdf

**Links in post:** https://github.com/trailofbits/publications/blob/master/reviews/2024-10-huggingface-gradio-securityreview.pdf


---

## 2024-09-17 · Post · At DEF CON, @trailofbits Principal Security Engineer @MichaelBrownUC discussed with @ISMG_News how A


Tags (automatic): AI-assisted hunting


### Post — @trailofbits — 2024-09-17 13:47 UTC (2024-09-17 14:47 WAT)

- URL: https://x.com/trailofbits/status/1836039382941217034
- Metrics (at fetch): bookmark 3, impression 1641, like 7, quote 0, reply 0, retweet 3

> At DEF CON, @trailofbits Principal Security Engineer @MichaelBrownUC discussed with @ISMG_News how AI/ML is revolutionizing cybersecurity. They covered four critical areas transforming the field, from surpassing traditional analysis to @DARPA's AI Cyber Challenge. https://t.co/4cV0E6nddM

**Media:**
- video:  — no alt text provided by author


---

## 2024-09-10 · Post · Learn how to equip your C++ code with ASan annotations to catch more bugs. We also contributed to LL


### Post — @trailofbits — 2024-09-10 14:16 UTC (2024-09-10 15:16 WAT)

- URL: https://x.com/trailofbits/status/1833509969930719246
- Metrics (at fetch): bookmark 19, impression 12665, like 57, quote 3, reply 0, retweet 9

> Learn how to equip your C++ code with ASan annotations to catch more bugs. We also contributed to LLVM, including annotations to std::string and std::deque, custom allocators, and bug fixes in libc++. https://t.co/QFpWOH4TVq https://t.co/eSdMdskbOm

**Media:**
- photo: https://pbs.twimg.com/media/GXHpq-DXEAAMIai.jpg — no alt text provided by author
- photo: https://pbs.twimg.com/media/GXHprLIWEAAhN3y.jpg — no alt text provided by author


---

## 2024-09-10 · Post · Learn how to equip your C++ code with ASan annotations to catch more bugs. We also contributed to AS


### Post — @trailofbits — 2024-09-10 13:51 UTC (2024-09-10 14:51 WAT)

- URL: https://x.com/trailofbits/status/1833503454460830192
- Metrics (at fetch): bookmark 2, impression 777, like 3, quote 0, reply 0, retweet 0

> Learn how to equip your C++ code with ASan annotations to catch more bugs. We also contributed to ASan in GCC and LLVM, including annotations to std::string and std::deque, custom allocators, and bug fixes in libc++. https://t.co/QFpWOH4m5S https://t.co/7e8dyOk1Se

**Media:**
- photo: https://pbs.twimg.com/media/GXHpq-DXEAAMIai.jpg — no alt text provided by author
- photo: https://pbs.twimg.com/media/GXHprLIWEAAhN3y.jpg — no alt text provided by author


---

## 2024-09-10 · Post · We released the results of our Ask Astro AI audit! 🎉 Plus, watch our Burp webinar ft. @albinowax and


Tags (automatic): AI-assisted hunting


### Post — @trailofbits — 2024-09-10 11:08 UTC (2024-09-10 12:08 WAT)

- URL: https://x.com/trailofbits/status/1833462427066724601
- Metrics (at fetch): bookmark 10, impression 7576, like 16, quote 0, reply 4, retweet 2

> We released the results of our Ask Astro AI audit! 🎉 Plus, watch our Burp webinar ft. @albinowax and read about even more PQC in this month's newsletter. Dive in now: https://t.co/Mr4qKMnegg https://t.co/oOg4fzR6ZD

**Media:**
- photo: https://pbs.twimg.com/media/GXHEXFNWAAAet_S.jpg — no alt text provided by author


---

## 2024-07-30 · Post · Homebrew, the missing package manager for macOS, produces the binaries that millions of users downlo


### Post — @trailofbits — 2024-07-30 13:03 UTC (2024-07-30 14:03 WAT)

- URL: https://x.com/trailofbits/status/1818271079355261371
- Metrics (at fetch): bookmark 10, impression 5117, like 45, quote 1, reply 1, retweet 14

> Homebrew, the missing package manager for macOS, produces the binaries that millions of users download daily. 
> 👉 Read about our audit of Homebrew’s CI/CD pipeline and brew. 
> https://t.co/QOOrdo3qJk https://t.co/Z97S4pEsAH

**Media:**
- photo: https://pbs.twimg.com/media/GTvL6PPWgAALnGe.jpg — no alt text provided by author


---

## 2024-07-11 · Post · The hack behind your "sold out" ticket: we confirmed that scalpers reverse-engineered @Ticketmaster'


### Post — @trailofbits — 2024-07-11 17:19 UTC (2024-07-11 18:19 WAT)

- URL: https://x.com/trailofbits/status/1811450172884549891
- Metrics (at fetch): bookmark 2, impression 2510, like 15, quote 0, reply 0, retweet 3

> The hack behind your "sold out" ticket: we confirmed that scalpers reverse-engineered @Ticketmaster's rotating barcodes to transfer their "untransferable" tickets. More from @404mediaco:
> https://t.co/OfZSLsjET2


---

## 2024-07-05 · Post · For our second open-source AI security audit, we reviewed the Ask Astro chatbot, which supports the 


Tags (automatic): AI-assisted hunting


### Post — @trailofbits — 2024-07-05 14:03 UTC (2024-07-05 15:03 WAT)

- URL: https://x.com/trailofbits/status/1809226711315210731
- Metrics (at fetch): bookmark 10, impression 5489, like 30, quote 2, reply 1, retweet 6

> For our second open-source AI security audit, we reviewed the Ask Astro chatbot, which supports the Astronomer orchestration tool for Apache Airflow. The 4 issues we identified could lead to output poisoning, inaccurate document ingestion, and DoS. https://t.co/WKiDcgtfSP


---

## 2024-07-02 · Thread · Async-unsafe signal handlers are at the core of the recent regreSSHion vulnerability (CVE-2024-6387)


### Post — @trailofbits — 2024-07-02 21:36 UTC (2024-07-02 22:36 WAT)

- URL: https://x.com/trailofbits/status/1808253409386287259
- Metrics (at fetch): bookmark 39, impression 11832, like 122, quote 2, reply 1, retweet 29

> Async-unsafe signal handlers are at the core of the recent regreSSHion vulnerability (CVE-2024-6387). We published a new CodeQL query that searches for this often overlooked class of bugs.
>
> https://t.co/4vEmP7wqrw


### Thread part 2 — @trailofbits — 2024-07-02 21:36 UTC (2024-07-02 22:36 WAT)

- URL: https://x.com/trailofbits/status/1808253411906728214
- Metrics (at fetch): bookmark 2, impression 1494, like 5, quote 0, reply 0, retweet 0

> Install and run our CodeQL query packs to search your codebase for this insecure pattern. https://appsec.guide/docs/static-analysis/codeql/installation/#installing-new-query-packs

**Links in post:** https://appsec.guide/docs/static-analysis/codeql/installation/#installing-new-query-packs


---

## 2024-06-11 · Post · Introducing Sticky Pickle: An advanced variant of the Sleepy Pickle attack that enables persistent a


Tags (automatic): AI-assisted hunting


### Post — @trailofbits — 2024-06-11 15:03 UTC (2024-06-11 16:03 WAT)

- URL: https://x.com/trailofbits/status/1800544266810179674
- Metrics (at fetch): bookmark 6, impression 7574, like 30, quote 2, reply 0, retweet 7

> Introducing Sticky Pickle: An advanced variant of the Sleepy Pickle attack that enables persistent and stealthy compromise of ML models. Learn about the implications of this self-replicating technique and its potential impact on AI/ML security.
> https://t.co/4QgszInrXh


---

## 2024-06-11 · Post · We’ve developed a new ML model attack technique, Sleepy Pickle, that exploits weaknesses in Pickle f


### Post — @trailofbits — 2024-06-11 13:01 UTC (2024-06-11 14:01 WAT)

- URL: https://x.com/trailofbits/status/1800513566958620708
- Metrics (at fetch): bookmark 24, impression 11703, like 60, quote 2, reply 1, retweet 15

> We’ve developed a new ML model attack technique, Sleepy Pickle, that exploits weaknesses in Pickle files used to distribute ML models. Learn how this attack can compromise ML models / their users and how you can reduce your risk. 
> https://t.co/3BG7eDiNq4


---

## 2024-05-30 · Post · We've added a comprehensive section on leveraging OSS-Fuzz to improve the security and stability of 


### Post — @trailofbits — 2024-05-30 13:24 UTC (2024-05-30 14:24 WAT)

- URL: https://x.com/trailofbits/status/1796170701012926565
- Metrics (at fetch): bookmark 37, impression 6788, like 60, quote 0, reply 0, retweet 17

> We've added a comprehensive section on leveraging OSS-Fuzz to improve the security and stability of open-source projects to our testing handbook. Learn how to run fuzzing harnesses, extend them, and reproduce crashes. https://t.co/upY09TNsb7


---

## 2024-05-28 · Post · As part of our work with the @sovtechfund, we're leveraging Rust's memory safety features to improve


### Post — @trailofbits — 2024-05-28 13:16 UTC (2024-05-28 14:16 WAT)

- URL: https://x.com/trailofbits/status/1795443911399260652
- Metrics (at fetch): bookmark 3, impression 1918, like 6, quote 0, reply 0, retweet 1

> As part of our work with the @sovtechfund, we're leveraging Rust's memory safety features to improve the internal development of the PyCA Cryptography package, ensuring a more secure foundation for this critical software library. https://t.co/saoB1fpprB


---

## 2024-05-17 · Post · Advanced expertise in ZK circuits. 


Tags (automatic): ZK


### Post — @trailofbits — 2024-05-17 13:01 UTC (2024-05-17 14:01 WAT)

- URL: https://x.com/trailofbits/status/1791453894402326951
- Metrics (at fetch): bookmark 5, impression 2106, like 8, quote 0, reply 1, retweet 0

> Advanced expertise in ZK circuits. 
> Impactful recommendations that enhance your SDLC. 
> Instructions on implementing tools and custom Semgrep rules into your CI. 
>
> These are just a few reasons why @Scroll_ZKP chose @TrailofBits. Read the case study: https://t.co/ArObQNlopa https://t.co/wER59KC5YQ

**Media:**
- photo: https://pbs.twimg.com/media/GNyF0BUWMAIx5SA.jpg — no alt text provided by author
- photo: https://pbs.twimg.com/media/GNyF0TTWsAATjBV.jpg — no alt text provided by author
- photo: https://pbs.twimg.com/media/GNyF0lxWsAAliHt.jpg — no alt text provided by author


---

## 2024-05-16 · Post · Our contributions to the LLVM project have improved AddressSanitizer's (ASan) bug detection capabili


### Post — @trailofbits — 2024-05-16 13:05 UTC (2024-05-16 14:05 WAT)

- URL: https://x.com/trailofbits/status/1791092495067070588
- Metrics (at fetch): bookmark 13, impression 9197, like 44, quote 4, reply 1, retweet 10

> Our contributions to the LLVM project have improved AddressSanitizer's (ASan) bug detection capabilities. Bootstrap ASan to better protect codebases against memory issues.  https://t.co/7w0STB87m8 https://t.co/pmJFu2mxv6

**Media:**
- photo: https://pbs.twimg.com/media/GNs9IcwWMAA0C1u.jpg — no alt text provided by author


---

## 2024-04-30 · Post · Developing invariants with Curvance. Over 9 weeks, we wrote and tested 216 invariants, uncovering 13


### Post — @trailofbits — 2024-04-30 13:39 UTC (2024-04-30 14:39 WAT)

- URL: https://x.com/trailofbits/status/1785302839721439457
- Metrics (at fetch): bookmark 29, impression 12413, like 61, quote 4, reply 1, retweet 15

> Developing invariants with Curvance. Over 9 weeks, we wrote and tested 216 invariants, uncovering 13 critical findings while pushing the limits of our tools. https://t.co/rCCEe12fbx


---

## 2024-03-25 · Post · Presenting our paper "Weak Fiat-Shamir Attacks on Modern Proof Systems," a collaboration with @Quang


### Post — @trailofbits — 2024-03-25 15:16 UTC (2024-03-25 16:16 WAT)

- URL: https://x.com/trailofbits/status/1772281304316600658
- Metrics (at fetch): bookmark 9, impression 6166, like 36, quote 1, reply 1, retweet 13

> Presenting our paper "Weak Fiat-Shamir Attacks on Modern Proof Systems," a collaboration with @QuangVDao &amp; @pag_crypto from @CarnegieMellon, @RealWorldCrypto this Wednesday. Let's look at some critical vulnerabilities that we found as part of that research https://t.co/Fo845kbRgj https://t.co/B6VYBjLot2

**Media:**
- photo: https://pbs.twimg.com/media/GJhoBrSbsAAKotg.png — no alt text provided by author
- photo: https://pbs.twimg.com/media/GJhoU11aAAAjuHn.jpg — no alt text provided by author


---

## 2024-03-06 · Post · We use a blend of SaaS (Slack, Github, Coda) and self-hosted open-source for our internal IT, and ev


### Post — @trailofbits — 2024-03-06 15:54 UTC (2024-03-06 16:54 WAT)

- URL: https://x.com/trailofbits/status/1765405638568382572
- Metrics (at fetch): bookmark 3, impression 4853, like 12, quote 1, reply 1, retweet 2

> We use a blend of SaaS (Slack, Github, Coda) and self-hosted open-source for our internal IT, and every app gets a @trailofbits audit. Today, that resulted in a high severity auth bug in @coderhq, now patched.
> https://t.co/0bCd1ZE1ec


---

## 2024-02-26 · Post · Circomspect, our security tool for Circom circuits, has been integrated into @SindriLabs’ CLI to sup


Tags (automatic): ZK


### Post — @trailofbits — 2024-02-26 15:17 UTC (2024-02-26 16:17 WAT)

- URL: https://x.com/trailofbits/status/1762134886746386725
- Metrics (at fetch): bookmark 4, impression 2196, like 14, quote 2, reply 0, retweet 3

> Circomspect, our security tool for Circom circuits, has been integrated into @SindriLabs’ CLI to support secure circuit development for even more Circom users.
> https://t.co/Vd8JPc6Txb


---

## 2024-02-09 · Post · Fuzz smarter, not harder, with our newest Testing Handbook chapter that will take your fuzzing skill


### Post — @trailofbits — 2024-02-09 14:15 UTC (2024-02-09 15:15 WAT)

- URL: https://x.com/trailofbits/status/1755958490525257750
- Metrics (at fetch): not returned

> Fuzz smarter, not harder, with our newest Testing Handbook chapter that will take your fuzzing skills from 0 to 60. https://buff.ly/3w8PAa1 [pic.x.com/4XXoDv2Cto]

**Media:**
- photo: https://pbs.twimg.com/media/GF5q8I3XEAASndg.jpg — no alt text provided by author

**Links in post:** https://buff.ly/3w8PAa1


---

## 2024-02-08 · Post · How to never find the same bug twice with @dguido on this week's @RiskyBusiness episode 735, plus i


### Post — @trailofbits — 2024-02-08 12:11 UTC (2024-02-08 13:11 WAT)

- URL: https://x.com/trailofbits/status/1755564893774774526
- Metrics (at fetch): not returned

> How to never find the same bug twice with @dguido on this week's @RiskyBusiness episode #735, plus insights on the AIxCC by @DARPA and @TrailofBits' efforts to secure open-source software.  https://buff.ly/3UEy2wy [pic.x.com/LFiG3oUnR4]

**Media:**
- photo: https://pbs.twimg.com/media/GF0E93-WcAAdOrH.jpg — no alt text provided by author

**Links in post:** https://buff.ly/3UEy2wy


---

## 2024-01-29 · Post · Warning: @lfgexchange  is falsely claiming to have worked with us on an audit. The report on their p


### Post — @trailofbits — 2024-01-29 23:21 UTC (2024-01-30 00:21 WAT)

- URL: https://x.com/trailofbits/status/1752109824282910869
- Metrics (at fetch): bookmark 13, impression 87160, like 170, quote 14, reply 8, retweet 37

> Warning: @lfgexchange  is falsely claiming to have worked with us on an audit. The report on their page is fake. If you want to verify the authenticity of a @trailofbits report, find it on our publications repo, the authoritative source straight from us. https://github.com/trailofbits/publications?tab=readme-ov-file#security-reviews [pic.x.com/c2sT5xM1T1]

**Media:**
- photo: https://pbs.twimg.com/media/GFC92kUbsAAvuiO.png — no alt text provided by author

**Links in post:** https://github.com/trailofbits/publications?tab=readme-ov-file#security-reviews


---

## 2024-01-16 · Post · Today, we are disclosing LeftoverLocals, a vulnerability that allows listening to LLM responses thro


Tags (automatic): AI-assisted hunting


### Post — @trailofbits — 2024-01-16 17:00 UTC (2024-01-16 18:00 WAT)

- URL: https://x.com/trailofbits/status/1747302889163219303
- Metrics (at fetch): not returned

> Today, we are disclosing LeftoverLocals, a vulnerability that allows listening to LLM responses through leaked GPU local memory created by another process on Apple, Qualcomm, AMD, and Imagination GPUs (CVE-2023-4969) https://buff.ly/48RDP68 [pic.x.com/GE7bKYWnXJ]

**Media:**
- animated_gif: https://pbs.twimg.com/tweet_video_thumb/GD-qrNCXoAAvaXz.jpg — no alt text provided by author

**Links in post:** https://buff.ly/48RDP68


---

## 2024-01-15 · Post · Since 2019, @trailofbits has partnered with @OpenTechFund's Red Team Lab to audit critical software 


### Post — @trailofbits — 2024-01-15 13:37 UTC (2024-01-15 14:37 WAT)

- URL: https://x.com/trailofbits/status/1746889227890012239
- Metrics (at fetch): not returned

> Since 2019, @trailofbits has partnered with @OpenTechFund's Red Team Lab to audit critical software that protects privacy and enables internet freedom. https://buff.ly/3tPmg7R

**Links in post:** https://buff.ly/3tPmg7R


---

## 2024-01-02 · Post · Circom remains a mainstay for zero-knowledge (ZK) proofs. Learn how to use a lesser-known language f


Tags (automatic): ZK


### Post — @trailofbits — 2024-01-02 14:12 UTC (2024-01-02 15:12 WAT)

- URL: https://x.com/trailofbits/status/1742186986163544127
- Metrics (at fetch): not returned

> Circom remains a mainstay for zero-knowledge (ZK) proofs. Learn how to use a lesser-known language feature called signal tags with four simple rules. 
> https://buff.ly/3TB6wzM

**Links in post:** https://buff.ly/3TB6wzM


---

## 2023-12-29 · Post · Dive into the challenges of writing resilient @Ethereum ABI parsers in our latest blog. Discover a n


### Post — @trailofbits — 2023-12-29 14:03 UTC (2023-12-29 15:03 WAT)

- URL: https://x.com/trailofbits/status/1740735195597205567
- Metrics (at fetch): not returned

> Dive into the challenges of writing resilient @Ethereum ABI parsers in our latest blog. Discover a newfound bug affecting libraries like eth_abi (Python), ethabi (Rust), and more. https://buff.ly/4aQm5tJ

**Links in post:** https://buff.ly/4aQm5tJ


---

## 2023-12-15 · Post · Wondering why your fuzz tests aren’t catching bugs? Fuzzing tip 2: Pay attention to fuzzing coverag


### Post — @trailofbits — 2023-12-15 13:47 UTC (2023-12-15 14:47 WAT)

- URL: https://x.com/trailofbits/status/1735657715156828350
- Metrics (at fetch): not returned

> Wondering why your fuzz tests aren’t catching bugs? Fuzzing tip #2: Pay attention to fuzzing coverage. Regularly review coverage reports to confirm the accuracy of your fuzzing setup. 
> https://buff.ly/46Ho3Jq.

**Links in post:** https://buff.ly/46Ho3Jq


---

## 2023-12-14 · Post · We are competing in @DARPA’s AI Cyber Challenge (AIxCC). DARPA is challenging competitors to develop


Tags (automatic): AI-assisted hunting


### Post — @trailofbits — 2023-12-14 14:16 UTC (2023-12-14 15:16 WAT)

- URL: https://x.com/trailofbits/status/1735302630711111735
- Metrics (at fetch): not returned

> We are competing in @DARPA’s AI Cyber Challenge (AIxCC). DARPA is challenging competitors to develop novel, fully automated AI-driven systems capable of securing the critical software that underpins the modern world.
> https://buff.ly/41jlEDN

**Links in post:** https://buff.ly/41jlEDN


---

## 2023-12-11 · Post · Join us for @empirehacking's last meetup of 2023 on Tuesday, Dec 12th at 6pm (tomorrow night). Talks


### Post — @trailofbits — 2023-12-11 17:31 UTC (2023-12-11 18:31 WAT)

- URL: https://x.com/trailofbits/status/1734264534515232872
- Metrics (at fetch): not returned

> Join us for @empirehacking's last meetup of 2023 on Tuesday, Dec 12th at 6pm (tomorrow night). Talks include:
> - Ellen Cooper of @hackmanhattan on reversing Japanese feature phones
> - Evan Sultanik of @trailofbits on dataflow analysis for bug hunting
> RSVP: https://buff.ly/3sZKeNa

**Links in post:** https://buff.ly/3sZKeNa


---

## 2023-12-06 · Post · Cryptography misuse, bugs in string methods, and insecure file permissions are critical issues that 


### Post — @trailofbits — 2023-12-06 13:33 UTC (2023-12-06 14:33 WAT)

- URL: https://x.com/trailofbits/status/1732392701931229432
- Metrics (at fetch): not returned

> Cryptography misuse, bugs in string methods, and insecure file permissions are critical issues that can be detected using @trailofbit’s CodeQL open-sourced queries for Go and C. Follow along in our blog:  https://buff.ly/480njQy

**Links in post:** https://buff.ly/480njQy


---

## 2023-11-22 · Post · Event Tracing for Windows (ETW) is crucial for modern EDR solutions. But what do you really know abo


### Post — @trailofbits — 2023-11-22 14:25 UTC (2023-11-22 15:25 WAT)

- URL: https://x.com/trailofbits/status/1727332494838747561
- Metrics (at fetch): not returned

> Event Tracing for Windows (ETW) is crucial for modern EDR solutions. But what do you really know about its internal workings? Dive into ETW to discover useful attack targets and forensic information.
> https://blog.trailofbits.com/2023/11/22/etw-internals-for-security-research-and-forensics/

**Links in post:** https://blog.trailofbits.com/2023/11/22/etw-internals-for-security-research-and-forensics/


---

## 2023-11-15 · Post · We assessed the YOLOv7 vision model and identified 11 security vulnerabilities that could enable RCE


Tags (automatic): RCE


### Post — @trailofbits — 2023-11-15 17:28 UTC (2023-11-15 18:28 WAT)

- URL: https://x.com/trailofbits/status/1724841699803820244
- Metrics (at fetch): not returned

> We assessed the YOLOv7 vision model and identified 11 security vulnerabilities that could enable RCE, DoS, and model differentials. We do not recommend using the codebase for mission-critical applications or applications that require high availability.
> https://buff.ly/47aP751

**Links in post:** https://buff.ly/47aP751


---

## 2023-11-14 · Post · We completed an audit of Warehouse and cabotage, the codebases that power @pypi and serve billions o


### Post — @trailofbits — 2023-11-14 14:41 UTC (2023-11-14 15:41 WAT)

- URL: https://x.com/trailofbits/status/1724437391715299347
- Metrics (at fetch): not returned

> We completed an audit of Warehouse and cabotage, the codebases that power @pypi and serve billions of Python packages weekly.
>
> https://blog.trailofbits.com/2023/11/14/our-audit-of-pypi/

**Links in post:** https://blog.trailofbits.com/2023/11/14/our-audit-of-pypi/


---

## 2023-11-14 · Thread · The @raft_fi issue is complex and we're actively investigating it. We've offered to help their team 


### Post — @trailofbits — 2023-11-14 08:30 UTC (2023-11-14 09:30 WAT)

- URL: https://x.com/trailofbits/status/1724344137065886183
- Metrics (at fetch): bookmark 74, impression 51130, like 153, quote 6, reply 2, retweet 22

> The @raft_fi issue is complex and we're actively investigating it. We've offered to help their team however we can. Here's some of what we know so far:


### Thread part 2 — @trailofbits — 2023-11-14 08:30 UTC (2023-11-14 09:30 WAT)

- URL: https://x.com/trailofbits/status/1724344149283868983
- Metrics (at fetch): not returned

> Scope varied, but here is the full list of external eyes on Raft's codebase:
> * @trailofbits, Apr 24-28
> * @HatsFinance, May 11-18
> * @0xcuriousapple, May 22-23
> * @aviggiano, June 21-23
> * @0xcuriousapple, Aug 25, Aug 31, &amp; Sep 13
> * @certora unknown


---

## 2023-10-05 · Post · We’re launching a new service: invariant development. We’ll identify, implement, and test security-c


### Post — @trailofbits — 2023-10-05 12:00 UTC (2023-10-05 13:00 WAT)

- URL: https://x.com/trailofbits/status/1709901302665191664
- Metrics (at fetch): not returned

> We’re launching a new service: invariant development. We’ll identify, implement, and test security-critical invariants to prevent bugs &amp; secure your codebase over the long term. Plus, we’ll upskill your team to write their own invariants! https://buff.ly/3PIbjM7

**Links in post:** https://buff.ly/3PIbjM7


---

## 2023-09-20 · Post · If you overextend the Oblivious Transfer (OT) in your threshold ECDSA implementation, an attacker ca


### Post — @trailofbits — 2023-09-20 12:30 UTC (2023-09-20 13:30 WAT)

- URL: https://x.com/trailofbits/status/1704473021891666336
- Metrics (at fetch): bookmark 3, impression 1588, like 2, quote 0, reply 0, retweet 0

> If you overextend the Oblivious Transfer (OT) in your threshold ECDSA implementation, an attacker can steal your signing key. Learn more about OT and how the attack works on our blog:
> https://t.co/yA5E286XjZ


---

## 2023-09-14 · Post · New role open: we're hiring an IT engineer. We're looking for someone to provide tech support to our


### Post — @trailofbits — 2023-09-14 15:02 UTC (2023-09-14 16:02 WAT)

- URL: https://x.com/trailofbits/status/1702336964366934284
- Metrics (at fetch): bookmark 1, impression 4713, like 13, quote 0, reply 1, retweet 5

> New role open: we're hiring an IT engineer. We're looking for someone to provide tech support to our employees while helping to design, implement, &amp; operate our critical technology infrastructure. https://t.co/THW4nQTLCO


---

## 2023-08-31 · Post · The @OpenSSF's Security Software Repositories WG has been instrumental in improving package index se


### Post — @trailofbits — 2023-08-31 16:01 UTC (2023-08-31 17:01 WAT)

- URL: https://x.com/trailofbits/status/1697278331173966081
- Metrics (at fetch): bookmark 2, impression 5803, like 14, quote 1, reply 1, retweet 4

> The @OpenSSF's Security Software Repositories WG has been instrumental in improving package index security, and we've been honored to help them build many of their key initiatives!
>
> Read their post here https://t.co/OKUiTk3zsa, and read on for our specific contributions 🧵:


---

## 2023-08-21 · Post · Echidna makes it "super easy" to fuzz Ethereum smart contracts. Just ask @Superfluid_HQ, who ran Ech


Tags (automatic): Smart contract / DeFi


### Post — @trailofbits — 2023-08-21 19:42 UTC (2023-08-21 20:42 WAT)

- URL: https://x.com/trailofbits/status/1693710127474311568
- Metrics (at fetch): bookmark 7, impression 7072, like 55, quote 0, reply 2, retweet 13

> Echidna makes it "super easy" to fuzz Ethereum smart contracts. Just ask @Superfluid_HQ, who ran Echidna over the weekend on an idle Mac mini. https://t.co/QtLgWjlB3W


---

## 2023-07-21 · Post · With Echidna 2.1.0 and later, you can retrieve on-chain data to fuzz deployed contracts and test how


Tags (automatic): Blockchain / L1-L2 / bridge


### Post — @trailofbits — 2023-07-21 11:06 UTC (2023-07-21 12:06 WAT)

- URL: https://x.com/trailofbits/status/1682346312325373952
- Metrics (at fetch): bookmark 32, impression 17386, like 96, quote 3, reply 2, retweet 27

> With Echidna 2.1.0 and later, you can retrieve on-chain data to fuzz deployed contracts and test how new code integrates with existing contracts. You can also use it to recreate real-world hacks! https://t.co/tA9r2qqD5Z


---

## 2023-07-18 · Post · How will AI affect national security? In our responses to an RFI by the White House's OTSP, we highl


Tags (automatic): AI-assisted hunting


### Post — @trailofbits — 2023-07-18 19:57 UTC (2023-07-18 20:57 WAT)

- URL: https://x.com/trailofbits/status/1681392695330078750
- Metrics (at fetch): bookmark 1, impression 5930, like 20, quote 1, reply 1, retweet 6

> How will AI affect national security? In our responses to an RFI by the White House's OTSP, we highlight a few key points 🧵: https://t.co/gcQ4n2pDim


---

## 2023-07-12 · Post · Creating earned trust in AI, two new tools, and two million pip-audit downloads: Read our July newsl


Tags (automatic): AI-assisted hunting


### Post — @trailofbits — 2023-07-12 12:25 UTC (2023-07-12 13:25 WAT)

- URL: https://x.com/trailofbits/status/1679104729060724736
- Metrics (at fetch): not returned

> Creating earned trust in AI, two new tools, and two million pip-audit downloads: Read our July newsletter! https://mailchi.mp/trailofbits/trail-of-bits-tribuneits-been-a-busy-july

**Links in post:** https://mailchi.mp/trailofbits/trail-of-bits-tribuneits-been-a-busy-july


---

## 2023-06-16 · Post · We submitted a response to the NTIA’s RFC on AI accountability. Here's what we told them: https://bl


Tags (automatic): AI-assisted hunting


### Post — @trailofbits — 2023-06-16 12:32 UTC (2023-06-16 13:32 WAT)

- URL: https://x.com/trailofbits/status/1669684291846938626
- Metrics (at fetch): not returned

> We submitted a response to the NTIA’s RFC on AI accountability. Here's what we told them: https://blog.trailofbits.com/2023/06/16/trail-of-bitss-response-to-ntia-ai-accountability-rfc/
>
> The main themes of our recommendations include 🧵:

**Links in post:** https://blog.trailofbits.com/2023/06/16/trail-of-bitss-response-to-ntia-ai-accountability-rfc/


---

## 2023-06-15 · Post · Bug-finding tools are restricted to a single IR, but bugs don't conform to this limit. Our VAST tool


Tags (automatic): Blockchain / L1-L2 / bridge


### Post — @trailofbits — 2023-06-15 11:19 UTC (2023-06-15 12:19 WAT)

- URL: https://x.com/trailofbits/status/1669303520669908993
- Metrics (at fetch): not returned

> Bug-finding tools are restricted to a single IR, but bugs don't conform to this limit. Our VAST tool builds a tower of IRs to bridge the gap between low-level code analysis and higher-level logic. Bugs span the semantic gap and so should code analysis.
>
> https://blog.trailofbits.com/2023/06/15/finding-bugs-with-mlir-and-vast/

**Links in post:** https://blog.trailofbits.com/2023/06/15/finding-bugs-with-mlir-and-vast/


---

## 2023-06-01 · Post · Our first public AI/ML audit, German funding for open-source infrastructure, and 20x faster Echidna 


Tags (automatic): AI-assisted hunting


### Post — @trailofbits — 2023-06-01 10:59 UTC (2023-06-01 11:59 WAT)

- URL: https://x.com/trailofbits/status/1664225226358505474
- Metrics (at fetch): not returned

> Our first public AI/ML audit, German funding for open-source infrastructure, and 20x faster Echidna fuzzing. Read our spring newsletter! https://mailchi.mp/trailofbits/trail-of-bits-tribunewhats-new-this-summer

**Links in post:** https://mailchi.mp/trailofbits/trail-of-bits-tribunewhats-new-this-summer


---

## 2023-05-25 · Post · We're hiring for an appsec consultant to join our assurance team. Join our team if you enjoy finding


### Post — @trailofbits — 2023-05-25 16:45 UTC (2023-05-25 17:45 WAT)

- URL: https://x.com/trailofbits/status/1661775409002819593
- Metrics (at fetch): not returned

> We're hiring for an appsec consultant to join our assurance team. Join our team if you enjoy finding bugs in complex and new attack surfaces:
> https://buff.ly/3IGdltk

**Links in post:** https://buff.ly/3IGdltk


---

## 2023-05-10 · Post · We're incredibly excited for this partnership! Our OSS engineering team has been working on securing


### Post — @trailofbits — 2023-05-10 13:00 UTC (2023-05-10 14:00 WAT)

- URL: https://x.com/trailofbits/status/1656282942229086211
- Metrics (at fetch): not returned

> We're incredibly excited for this partnership! Our OSS engineering team has been working on securing and improving critical pieces of the ecosystem since 2019, and this collaboration with @sovtechfund is instrumental in continuing that work! https://twitter.com/sovtechfund/status/1655919455669567491

**Links in post:** https://twitter.com/sovtechfund/status/1655919455669567491

**Quoted post (full text):**

    #### Quoted post — @1567101650619322368 — 2023-05-09 12:55 UTC (2023-05-09 13:55 WAT)
    
    - URL: https://x.com/1567101650619322368/status/1655919455669567491
    - Metrics (at fetch): not returned
    
    > We're excited to announce our investment to the Python ecosystem security in partnership with @trailofbits. Our support will focus on critical engineering, maintenance, and support to PyPI package repository and highly used packages, as well as
    


---

## 2023-04-20 · Post · Staff Engineer @disconnect3d_pl noticed during an audit that a typo caused the _FORTIFY_SOURCE macro


### Post — @trailofbits — 2023-04-20 11:05 UTC (2023-04-20 12:05 WAT)

- URL: https://x.com/trailofbits/status/1649006244617650176
- Metrics (at fetch): not returned

> Staff Engineer @disconnect3d_pl noticed during an audit that a typo caused the _FORTIFY_SOURCE macro to not be enabled. We found 20 projects with similar problems and fixed them. Learn more about how to test your code against rouge coding fingers!
>
> https://blog.trailofbits.com/2023/04/20/typos-that-omit-security-features-and-how-to-test-for-them/

**Links in post:** https://blog.trailofbits.com/2023/04/20/typos-that-omit-security-features-and-how-to-test-for-them/


---

## 2023-02-16 · Post · An appsec engineer was fawning over a sudo bug, leading him to research and discovery of a separate 


### Post — @trailofbits — 2023-02-16 13:00 UTC (2023-02-16 14:00 WAT)

- URL: https://x.com/trailofbits/status/1626204774034198530
- Metrics (at fetch): not returned

> An appsec engineer was fawning over a sudo bug, leading him to research and discovery of a separate logic bug in Linux. Bottom line: Don't use readline in your SUID applications https://blog.trailofbits.com/2023/02/16/suid-logic-bug-linux-readline/

**Links in post:** https://blog.trailofbits.com/2023/02/16/suid-logic-bug-linux-readline/


---

## 2022-12-14 · Post · We are going to be starting in a few minutes! come by and fuzz with us 


### Post — @trailofbits — 2022-12-14 16:58 UTC (2022-12-14 17:58 WAT)

- URL: https://x.com/trailofbits/status/1603072005611339779
- Metrics (at fetch): bookmark 1, impression 0, like 1, quote 0, reply 0, retweet 0

> We are going to be starting in a few minutes! come by and fuzz with us 
>
> https://t.co/OjIHpMI0K1
> https://t.co/YvzTIFXESA https://t.co/uQwHwJmrS2

**Quoted post (full text):**

    #### Quoted post — @trailofbits — 2022-12-13 17:43 UTC (2022-12-13 18:43 WAT)
    
    - URL: https://x.com/trailofbits/status/1602720892076888065
    - Metrics (at fetch): bookmark 0, impression 0, like 7, quote 1, reply 0, retweet 2
    
    > 24 hours from now, we'll be hosting another livestream tool workshop. If you want to join us, make sure you subscribe to our Twitch and YouTube channels for a notification on when we go live! https://t.co/Mb5BRMcDZl https://t.co/5b2kZQQw0k
    


---

## 2022-12-13 · Post · 24 hours from now, we'll be hosting another livestream tool workshop. If you want to join us, make s


### Post — @trailofbits — 2022-12-13 17:43 UTC (2022-12-13 18:43 WAT)

- URL: https://x.com/trailofbits/status/1602720892076888065
- Metrics (at fetch): bookmark 0, impression 0, like 7, quote 1, reply 0, retweet 2

> 24 hours from now, we'll be hosting another livestream tool workshop. If you want to join us, make sure you subscribe to our Twitch and YouTube channels for a notification on when we go live! https://t.co/Mb5BRMcDZl https://t.co/5b2kZQQw0k


---

## 2022-11-16 · Post · Come learn to fuzz like a pro: Live now on Twitch and YouTube! 


### Post — @trailofbits — 2022-11-16 16:58 UTC (2022-11-16 17:58 WAT)

- URL: https://x.com/trailofbits/status/1592925072117084160
- Metrics (at fetch): bookmark 6, impression 0, like 28, quote 1, reply 0, retweet 15

> Come learn to fuzz like a pro: Live now on Twitch and YouTube! 
>
> https://t.co/Mb5BRMdbOT
>
> https://t.co/IXZ5ws7Qlu


---

## 2022-11-10 · Post · During research that led to our discovery of a vuln in SQLite, we found something we call "divergent


### Post — @trailofbits — 2022-11-10 12:31 UTC (2022-11-10 13:31 WAT)

- URL: https://x.com/trailofbits/status/1590683470740656129
- Metrics (at fetch): bookmark 45, impression 0, like 153, quote 5, reply 3, retweet 36

> During research that led to our discovery of a vuln in SQLite, we found something we call "divergent representations." Once we started looking for them, we found them everywhere https://t.co/fsSbITWgGx


---

## 2022-11-04 · Post · We released a new version of Slither, which contains several bug fixes and a new tool to help diagno


### Post — @trailofbits — 2022-11-04 16:38 UTC (2022-11-04 17:38 WAT)

- URL: https://x.com/trailofbits/status/1588571489590280194
- Metrics (at fetch): bookmark 1, impression 0, like 31, quote 0, reply 0, retweet 9

> We released a new version of Slither, which contains several bug fixes and a new tool to help diagnose issues with the static analyzer. Thank you to our growing number of contributors who continually make this tool better! https://t.co/48ddumEmPD


---

## 2022-10-25 · Post · Earlier this year, one of our interns found a vulnerability that affects applications using the SQLi


### Post — @trailofbits — 2022-10-25 11:30 UTC (2022-10-25 12:30 WAT)

- URL: https://x.com/trailofbits/status/1584870065698136064
- Metrics (at fetch): bookmark 59, impression 0, like 296, quote 8, reply 6, retweet 92

> Earlier this year, one of our interns found a vulnerability that affects applications using the SQLite library API. We are publicly disclosing that vuln today. https://t.co/vDsZKqvsoi


---

## 2022-10-12 · Post · The RBPF JIT compiler plays a critical role on the Solana blockchain. But the mode only works on x86


Tags (automatic): Blockchain / L1-L2 / bridge


### Post — @trailofbits — 2022-10-12 12:00 UTC (2022-10-12 13:00 WAT)

- URL: https://x.com/trailofbits/status/1580166636702556160
- Metrics (at fetch): not returned

> The RBPF JIT compiler plays a critical role on the Solana blockchain. But the mode only works on x86 hosts. Our intern Andrew Haberlandt added support for ARM64 during his internship https://blog.trailofbits.com/2022/10/12/solana-jit-compiler-ebpf-arm64/

**Links in post:** https://blog.trailofbits.com/2022/10/12/solana-jit-compiler-ebpf-arm64/


---

## 2022-09-01 · Post · We're extremely excited to add our work on pip-audit and gh-action-pip-audit to PyPA's repertoire! h


### Post — @trailofbits — 2022-09-01 14:54 UTC (2022-09-01 15:54 WAT)

- URL: https://x.com/trailofbits/status/1565352354773630981
- Metrics (at fetch): not returned

> We're extremely excited to add our work on pip-audit and gh-action-pip-audit to PyPA's repertoire! https://twitter.com/ThePyPA/status/1565345532842610689

**Links in post:** https://twitter.com/ThePyPA/status/1565345532842610689

**Quoted post (full text):**

    #### Quoted post — @2407526894 — 2022-09-01 14:27 UTC (2022-09-01 15:27 WAT)
    
    - URL: https://x.com/2407526894/status/1565345532842610689
    - Metrics (at fetch): not returned
    
    > The PyPA has voted to accept two new member projects: https://pypi.org/p/pip-audit &amp; the corresponding GitHub action, https://github.com/pypa/gh-action-pip-audit 🎉
    >
    > pip-audit audits Python environments and dependency trees for known vulnerabilities, and the action lets you easily run these audits in CI.
    
    **Links in post:** https://pypi.org/p/pip-audit, https://github.com/pypa/gh-action-pip-audit
    


---

## 2022-07-26 · Post · We have been using Echidna - our smart contract fuzzer - for years in our audits and it has found ma


Tags (automatic): Smart contract / DeFi


### Post — @trailofbits — 2022-07-26 17:05 UTC (2022-07-26 18:05 WAT)

- URL: https://x.com/trailofbits/status/1551976969411117057
- Metrics (at fetch): bookmark 11, impression 0, like 35, quote 0, reply 1, retweet 12

> We have been using Echidna - our smart contract fuzzer - for years in our audits and it has found many critical issues. Watch our recent presentation at @EthCC to learn how you can leverage Echidna to write safer contracts: 
>
> https://t.co/QTsXf3pIrT


---

## 2022-06-09 · Post · Last month we attended PyCon US 2022. Here are some of the cool things we saw, including our work on


### Post — @trailofbits — 2022-06-09 11:00 UTC (2022-06-09 12:00 WAT)

- URL: https://x.com/trailofbits/status/1534852915755683842
- Metrics (at fetch): bookmark 4, impression 0, like 24, quote 0, reply 0, retweet 8

> Last month we attended PyCon US 2022. Here are some of the cool things we saw, including our work on pip-audit and sigstore-python! https://t.co/wbwTc2HR7l


---

## 2022-04-26 · Post · Intern Christian Presa Schnell describes the improvements he proposed for go-fuzz, including a fix f


### Post — @trailofbits — 2022-04-26 11:00 UTC (2022-04-26 12:00 WAT)

- URL: https://x.com/trailofbits/status/1518907837312901120
- Metrics (at fetch): bookmark 0, impression 0, like 17, quote 1, reply 0, retweet 3

> Intern Christian Presa Schnell describes the improvements he proposed for go-fuzz, including a fix for type alias issues, integration of dictionary support, and new mutation strategies. https://t.co/IR0ptadbud


---

## 2022-04-20 · Post · We're emptying the Node.js bug queue! Thanks to @openjsf and @openssf, the @trailofbits Engineering 


### Post — @trailofbits — 2022-04-20 15:17 UTC (2022-04-20 16:17 WAT)

- URL: https://x.com/trailofbits/status/1516798301928054791
- Metrics (at fetch): bookmark 1, impression 0, like 30, quote 2, reply 1, retweet 1

> We're emptying the Node.js bug queue! Thanks to @openjsf and @openssf, the @trailofbits Engineering team is addressing externally reported language-level bugs in Node. https://t.co/sXizSvQgX1

**Quoted post (full text):**

    #### Quoted post — @14538601 — 2022-04-18 16:14 UTC (2022-04-18 17:14 WAT)
    
    - URL: https://x.com/14538601/status/1516087900340846594
    - Metrics (at fetch): bookmark 1, impression 0, like 19, quote 1, reply 0, retweet 2
    
    > Node.js is critical to many. The OpenSSF investment brings in engineering resources from NearForm and Trail of Bits to support Node.js maintainers who strive for a stable and secure codebase. Read the announcement on our blog: https://t.co/T2y8AGxffT 2/2
    


---

## 2022-04-15 · Post · In part 3 of our series, we explore how to exploit a Frozen Heart vulnerability in the Bulletproofs 


### Post — @trailofbits — 2022-04-15 11:00 UTC (2022-04-15 12:00 WAT)

- URL: https://x.com/trailofbits/status/1514921716836970504
- Metrics (at fetch): bookmark 1, impression 0, like 23, quote 0, reply 0, retweet 8

> In part 3 of our series, we explore how to exploit a Frozen Heart vulnerability in the Bulletproofs system https://t.co/QTvHHP6ovy


---

## 2022-04-14 · Post · In part 2 of our series on the Frozen Heart vulnerability, we explore how to exploit one such vulner


### Post — @trailofbits — 2022-04-14 11:00 UTC (2022-04-14 12:00 WAT)

- URL: https://x.com/trailofbits/status/1514559240278528002
- Metrics (at fetch): bookmark 2, impression 0, like 21, quote 3, reply 0, retweet 4

> In part 2 of our series on the Frozen Heart vulnerability, we explore how to exploit one such vulnerability in Girault’s proof of knowledge https://t.co/ncJLzQVX7B


---

## 2022-03-25 · Post · There's a dark side to compiler optimizations that can inadvertently cause information leaks or remo


### Post — @trailofbits — 2022-03-25 12:58 UTC (2022-03-25 13:58 WAT)

- URL: https://x.com/trailofbits/status/1507341268040531973
- Metrics (at fetch): bookmark 31, impression 0, like 146, quote 1, reply 3, retweet 47

> There's a dark side to compiler optimizations that can inadvertently cause information leaks or remove code critical to security. Read about the research being done to mitigate this risk and reduce the exposure to code-reuse attacks in software. https://t.co/a92xm8ubNW


---

## 2022-01-27 · Post · With the race to start using Cairo, we have the cryptographic and smart contract expertise to help. 


Tags (automatic): Race condition, Smart contract / DeFi


### Post — @trailofbits — 2022-01-27 17:32 UTC (2022-01-27 18:32 WAT)

- URL: https://x.com/trailofbits/status/1486753907925782529
- Metrics (at fetch): bookmark 7, impression 0, like 46, quote 3, reply 0, retweet 6

> With the race to start using Cairo, we have the cryptographic and smart contract expertise to help. A quick review of one popular NFT library yielded a critical bug! https://t.co/WJ09e6womL


---

## 2022-01-21 · Post · The first empirehacking of 2022 is coming up quickly on February 8th and is currently looking for p


### Post — @trailofbits — 2022-01-21 16:21 UTC (2022-01-21 17:21 WAT)

- URL: https://x.com/trailofbits/status/1484561726850879491
- Metrics (at fetch): bookmark 1, impression 0, like 2, quote 0, reply 0, retweet 1

> The first #empirehacking of 2022 is coming up quickly on February 8th and is currently looking for presenters! Think you can hack it? Shoot empirehacking@trailofbits.com an email and let us know what you'd like to speak about. https://t.co/IDW5XKoaRh

**Quoted post (full text):**

    #### Quoted post — @3129975465 — 2022-01-21 16:19 UTC (2022-01-21 17:19 WAT)
    
    - URL: https://x.com/3129975465/status/1484561228261433350
    - Metrics (at fetch): bookmark 0, impression 0, like 3, quote 1, reply 0, retweet 5
    
    > Call for speakers: We are currently recruiting speakers for our February 8th Empire Hacking virtual event. We're looking for 5-10 minute lightning talks. Have a cool tool you've been working on or solve an interesting problem? Let us know at empirehacking@trailofbits.com!
    


---

## 2021-12-21 · Post · We found critical flaws in common TSS libraries, a cryptographic protocol for distributed key genera


Tags (automatic): ZK


### Post — @trailofbits — 2021-12-21 13:57 UTC (2021-12-21 14:57 WAT)

- URL: https://x.com/trailofbits/status/1473291464264269826
- Metrics (at fetch): bookmark 34, impression 0, like 178, quote 13, reply 6, retweet 56

> We found critical flaws in common TSS libraries, a cryptographic protocol for distributed key generation and signing. We’ve released https://t.co/jJMhKTaSVW to help secure the rapidly advancing field of ZKPs, TSS, and similar schemes. https://t.co/OQ4NfyU60K


---

## 2021-11-22 · Post · There's a $5k bounty on porting Echidna's underlying dependencies to M1 Macs! Get in touch if you're


### Post — @trailofbits — 2021-11-22 13:57 UTC (2021-11-22 14:57 WAT)

- URL: https://x.com/trailofbits/status/1462782319950020617
- Metrics (at fetch): bookmark 1, impression 0, like 9, quote 0, reply 1, retweet 1

> There's a $5k bounty on porting Echidna's underlying dependencies to M1 Macs! Get in touch if you're familiar with Haskell and want to help: https://t.co/VwyI4gTBRD


---

## 2021-03-15 · Post · Do you know how pickles are stored? It’s jarring! Read about our new tool, Fickling, and how it can 


### Post — @trailofbits — 2021-03-15 15:06 UTC (2021-03-15 16:06 WAT)

- URL: https://x.com/trailofbits/status/1371477874625146880
- Metrics (at fetch): bookmark 3, impression 0, like 50, quote 6, reply 0, retweet 27

> Do you know how pickles are stored? It’s jarring! Read about our new tool, Fickling, and how it can be used to attack machine learning model files. https://t.co/vTXyMDZTrS


---

## 2020-08-05 · Post · Accidentally stepping on a DeFi lego: @samczsun helped save ~$400k from a bug in yEarn. 🎉 https://t.


Tags (automatic): Smart contract / DeFi


### Post — @trailofbits — 2020-08-05 13:15 UTC (2020-08-05 14:15 WAT)

- URL: https://x.com/trailofbits/status/1290999997631205376
- Metrics (at fetch): bookmark 2, impression 0, like 86, quote 3, reply 4, retweet 25

> Accidentally stepping on a DeFi lego: @samczsun helped save ~$400k from a bug in yEarn. 🎉 https://t.co/JXkA3V39ZH


---

## 2020-06-02 · Post · 🐝Johns Hopkins partnership for zero-knowledge proofs, Winchecksec 2.0 release, Crytic-al bug hunting


### Post — @trailofbits — 2020-06-02 10:59 UTC (2020-06-02 11:59 WAT)

- URL: https://x.com/trailofbits/status/1267772875001466880
- Metrics (at fetch): bookmark 1, impression 0, like 6, quote 1, reply 0, retweet 2

> 🐝Johns Hopkins partnership for zero-knowledge proofs, Winchecksec 2.0 release, Crytic-al bug hunting 🐝 - https://t.co/K6AoObGotC https://t.co/AC0pkBe1aA

**Media:**
- photo: https://pbs.twimg.com/media/EZgItioXQAA8lxA.jpg — no alt text provided by author


---

## 2020-05-15 · Post · We reported and fixed 12 security issues in projects across Ethereum, some of them critical. Get the


### Post — @trailofbits — 2020-05-15 14:19 UTC (2020-05-15 15:19 WAT)

- URL: https://x.com/trailofbits/status/1261300071339110406
- Metrics (at fetch): bookmark 0, impression 0, like 16, quote 0, reply 0, retweet 5

> We reported and fixed 12 security issues in projects across Ethereum, some of them critical. Get the details in 'Bug Hunting with Crytic': https://t.co/kbJD540qoY


---

## 2020-03-20 · Post · 🌟Landmark “white-box” Voatz report, the great Manticore ENS bug exploit, huge osquery update🌟 - http


### Post — @trailofbits — 2020-03-20 10:59 UTC (2020-03-20 11:59 WAT)

- URL: https://x.com/trailofbits/status/1240956131150888960
- Metrics (at fetch): bookmark 0, impression 0, like 4, quote 0, reply 0, retweet 1

> 🌟Landmark “white-box” Voatz report, the great Manticore ENS bug exploit, huge osquery update🌟 - https://t.co/zO1wBVJv5G https://t.co/Jqdl3HpZ9P

**Media:**
- photo: https://pbs.twimg.com/media/ETjDBkDXsAIW5Oc.jpg — no alt text provided by author


---

## 2020-03-03 · Post · Manticore discovers the ENS bug https://t.co/ouniU6x79P https://t.co/Z0ttQolY2t


### Post — @trailofbits — 2020-03-03 19:21 UTC (2020-03-03 20:21 WAT)

- URL: https://x.com/trailofbits/status/1234921978399789063
- Metrics (at fetch): bookmark 0, impression 0, like 16, quote 0, reply 0, retweet 5

> Manticore discovers the ENS bug https://t.co/ouniU6x79P https://t.co/Z0ttQolY2t

**Media:**
- photo: https://pbs.twimg.com/media/ESNS_qtXYAocTLx.jpg — no alt text provided by author


---

## 2020-01-16 · Post · We have a working proof-of-concept exploit for ‘Whose Curve is it Anyway?’ — NSA’s bug in Microsoft’


### Post — @trailofbits — 2020-01-16 16:48 UTC (2020-01-16 17:48 WAT)

- URL: https://x.com/trailofbits/status/1217851031104688134
- Metrics (at fetch): bookmark 15, impression 0, like 125, quote 4, reply 2, retweet 59

> We have a working proof-of-concept exploit for ‘Whose Curve is it Anyway?’ — NSA’s bug in Microsoft’s Crypto API.
>
> Read on for our explainer:
> https://t.co/DMmkDu2XKM


---

## 2019-11-01 · Post · Stop wasting time manually reverseengineering. We'll teach you to streamline analysis, deobfuscate 


### Post — @trailofbits — 2019-11-01 17:51 UTC (2019-11-01 18:51 WAT)

- URL: https://x.com/trailofbits/status/1190325569247944704
- Metrics (at fetch): bookmark 0, impression 0, like 6, quote 0, reply 0, retweet 0

> Stop wasting time manually #reverseengineering. We'll teach you to streamline analysis, deobfuscate code, exploit vulnerabilities, and more. Grab a seat before Early Bird pricing ends: https://t.co/hw8hyiy1zo


---

## 2019-10-24 · Post · Watch Your Language: Our First Vyper Audit https://t.co/IsPqG0vFqY https://t.co/L3T0g68nLe


### Post — @trailofbits — 2019-10-24 11:01 UTC (2019-10-24 12:01 WAT)

- URL: https://x.com/trailofbits/status/1187323108618833920
- Metrics (at fetch): bookmark 0, impression 0, like 3, quote 0, reply 0, retweet 2

> Watch Your Language: Our First Vyper Audit https://t.co/IsPqG0vFqY https://t.co/L3T0g68nLe

**Media:**
- photo: https://pbs.twimg.com/media/EHo4EwYWwAAw8UV.png — no alt text provided by author


---

## 2019-09-11 · Post · osquery 4.0.1 is here! 🎉


### Post — @trailofbits — 2019-09-11 15:10 UTC (2019-09-11 16:10 WAT)

- URL: https://x.com/trailofbits/status/1171803280403587072
- Metrics (at fetch): bookmark 0, impression 0, like 10, quote 0, reply 0, retweet 7

> osquery 4.0.1 is here! 🎉
> - Build system supports diverse deployments
> - More event types, search options, improved event tracing
> - Perf &amp; perf measurement improved
> - 9mo of bug fixes &amp; hardening
> Try the first stable release under the @linuxfoundation!
> https://t.co/6VJqEy7JQg


---

## 2019-08-19 · Post · Echidna's latest release lets you fuzz for assertion violations even if you don't write any explicit


### Post — @trailofbits — 2019-08-19 16:27 UTC (2019-08-19 17:27 WAT)

- URL: https://x.com/trailofbits/status/1163487550738243585
- Metrics (at fetch): bookmark 1, impression 0, like 5, quote 1, reply 0, retweet 3

> Echidna's latest release lets you fuzz for assertion violations even if you don't write any explicit tests (!), and recycles return value constants, as detailed in our analysis of the MakerDAO contracts: https://t.co/M5yOKfB1nW
> https://t.co/fTFvef0gBs


---

## 2019-08-19 · Post · The latest Bluetooth bug (KNOB attack) is bad but hard to exploit in practice: It requires local pro


### Post — @trailofbits — 2019-08-19 15:26 UTC (2019-08-19 16:26 WAT)

- URL: https://x.com/trailofbits/status/1163472198398566400
- Metrics (at fetch): bookmark 0, impression 0, like 3, quote 0, reply 0, retweet 2

> The latest Bluetooth bug (KNOB attack) is bad but hard to exploit in practice: It requires local proximity, perfect timing, and a clear signal to fully MitM both peers. We’ll apply the patches and continue using our bluetooth keyboards. 
> https://t.co/S1rx5PZAwM


---

## 2019-07-17 · Post · Watch Artem and @peter_a_goodman's presentation at the @Qualcomm Mobile Security Summit about their 


### Post — @trailofbits — 2019-07-17 15:19 UTC (2019-07-17 16:19 WAT)

- URL: https://x.com/trailofbits/status/1151511663969013760
- Metrics (at fetch): bookmark 1, impression 0, like 26, quote 1, reply 0, retweet 12

> Watch Artem and @peter_a_goodman's presentation at the @Qualcomm Mobile Security Summit about their incredible journey trying to fuzz legacy VxWorks PowerPC targets with AFL and QEMU #QPSISummit2019 https://t.co/DPB3yoACXB


---

## 2019-07-01 · Post · Use siderophile to quickly identify the ideal fuzz targets in a Rust codebase https://t.co/y6gmFNRIG


### Post — @trailofbits — 2019-07-01 15:30 UTC (2019-07-01 16:30 WAT)

- URL: https://x.com/trailofbits/status/1145716254449311744
- Metrics (at fetch): bookmark 3, impression 0, like 25, quote 2, reply 0, retweet 12

> Use siderophile to quickly identify the ideal fuzz targets in a Rust codebase https://t.co/y6gmFNRIGS


---

## 2019-01-14 · Post · Data from @Hacker0x01 and @facebook proves that bug bounties only benefit a small elite group. Is th


Tags (automatic): Platform: HackerOne


### Post — @trailofbits — 2019-01-14 12:36 UTC (2019-01-14 13:36 WAT)

- URL: https://x.com/trailofbits/status/1084791374468259846
- Metrics (at fetch): bookmark 18, impression 0, like 124, quote 7, reply 5, retweet 80

> Data from @Hacker0x01 and @facebook proves that bug bounties only benefit a small elite group. Is this model meeting researchers' interests? Read our review of "New Solutions for Cybersecurity" by @mitpress. https://t.co/bt89Jj4MVn


---

## 2018-10-30 · Post · Slither 0.2.0 is out w/ new bug detectors, printers, API enhancements, and IR refinements. Big new f


Tags (automatic): Smart contract / DeFi


### Post — @trailofbits — 2018-10-30 09:56 UTC (2018-10-30 10:56 WAT)

- URL: https://x.com/trailofbits/status/1057209660862816256
- Metrics (at fetch): bookmark 2, impression 0, like 11, quote 0, reply 0, retweet 5

> Slither 0.2.0 is out w/ new bug detectors, printers, API enhancements, and IR refinements. Big new feature: truffle integration! Find bugs in your Solidity code now: https://t.co/hufk6kW48Y


---

## 2018-08-01 · Post · You could have invented that bluetooth attack https://t.co/8NCcTFGTpb https://t.co/BapdXU1A2o


### Post — @trailofbits — 2018-08-01 11:05 UTC (2018-08-01 12:05 WAT)

- URL: https://x.com/trailofbits/status/1024612137296125952
- Metrics (at fetch): bookmark 4, impression 0, like 59, quote 2, reply 1, retweet 37

> You could have invented that bluetooth attack https://t.co/8NCcTFGTpb https://t.co/BapdXU1A2o

**Media:**
- photo: https://pbs.twimg.com/media/DjgnTv6U8AAQa1C.png — no alt text provided by author


---

## 2018-07-26 · Post · Lack of curve point validation continues to trip people up, part 899372. Read @japesinator's comment


### Post — @trailofbits — 2018-07-26 15:42 UTC (2018-07-26 16:42 WAT)

- URL: https://x.com/trailofbits/status/1022507538342916096
- Metrics (at fetch): bookmark 0, impression 0, like 4, quote 0, reply 0, retweet 0

> Lack of curve point validation continues to trip people up, part 899372. Read @japesinator's commentary about the latest Bluetooth protocol bug in @arstechnica: https://t.co/ygCxkhnbeW

**Quoted post (full text):**

    #### Quoted post — @717313 — 2018-07-26 00:21 UTC (2018-07-26 01:21 WAT)
    
    - URL: https://x.com/717313/status/1022275564386873349
    - Metrics (at fetch): bookmark 1, impression 0, like 24, quote 9, reply 3, retweet 45
    
    > Decade-old Bluetooth flaw lets hackers steal data passing between devices https://t.co/MNJWEHzN30 by @dangoodin001
    


---

## 2018-04-06 · Post · You just approved an audit of your codebase. What now? How to prepare for a security audit: https://


### Post — @trailofbits — 2018-04-06 10:50 UTC (2018-04-06 11:50 WAT)

- URL: https://x.com/trailofbits/status/982209041945378818
- Metrics (at fetch): bookmark 1, impression 0, like 17, quote 2, reply 0, retweet 5

> You just approved an audit of your codebase. What now? How to prepare for a security audit: https://t.co/S1pv5URvPH


---

## 2018-02-25 · Post · $2,000 of bounty payments for Manticore, McSema, DeepState, and Algo were sent out today. Thanks to 


### Post — @trailofbits — 2018-02-25 20:58 UTC (2018-02-25 21:58 WAT)

- URL: https://x.com/trailofbits/status/967866336738267137
- Metrics (at fetch): bookmark 0, impression 0, like 6, quote 0, reply 0, retweet 1

> $2,000 of bounty payments for Manticore, McSema, DeepState, and Algo were sent out today. Thanks to our contributors! (ps. DM us if we missed you -- it can be difficult to track down emails sometimes.) https://t.co/H8QlviZHYP

**Media:**
- photo: https://pbs.twimg.com/media/DW6MsspW4AIq9oR.jpg — no alt text provided by author


---

## 2018-02-07 · Post · There's a great multi-part spread on the state of the security industry talent gap in @cxo_magazine 


### Post — @trailofbits — 2018-02-07 19:59 UTC (2018-02-07 20:59 WAT)

- URL: https://x.com/trailofbits/status/961328522479525888
- Metrics (at fetch): bookmark 0, impression 0, like 4, quote 0, reply 0, retweet 0

> There's a great multi-part spread on the state of the security industry talent gap in @cxo_magazine this month. See our comments in the bug bounty section. https://t.co/CWGkXaawgg

**Quoted post (full text):**

    #### Quoted post — @913772130298408961 — 2018-02-07 16:32 UTC (2018-02-07 17:32 WAT)
    
    - URL: https://x.com/913772130298408961/status/961276418134036480
    - Metrics (at fetch): bookmark 0, impression 0, like 4, quote 1, reply 0, retweet 2
    
    > New CXO Report launches: Closing the cybersecurity talent gap 
    > https://t.co/jjF9Q9vk7z 
    >
    > #CyberSecurity #cxomagazine #CXOReports #talentgap #cyberworkforce https://t.co/7L4joGiVkt
    
    **Media:**
    - media `3_961276363754815488` (details not returned by the API)
    


---

## 2018-01-26 · Post · Trail of Bits has reviewed custody solutions for cryptocurrency exchanges. Please contact us for an 


### Post — @trailofbits — 2018-01-26 18:20 UTC (2018-01-26 19:20 WAT)

- URL: https://x.com/trailofbits/status/956955036994617344
- Metrics (at fetch): bookmark 0, impression 0, like 2, quote 0, reply 1, retweet 1

> Trail of Bits has reviewed custody solutions for cryptocurrency exchanges. Please contact us for an audit and make sure your funds are safely stored! https://t.co/wbAItRacvl

**Quoted post (full text):**

    #### Quoted post — @6083342 — 2018-01-26 17:38 UTC (2018-01-26 18:38 WAT)
    
    - URL: https://x.com/6083342/status/956944561472815104
    - Metrics (at fetch): bookmark 0, impression 0, like 151, quote 32, reply 7, retweet 166
    
    > "Tokyo-based cryptocurrency exchange Coincheck has confirmed that it has suffered what appears to be the biggest hack in history of the technology" 58 billion yen, or $533 million https://t.co/wi3OfqKN8G
    


---

## 2018-01-17 · Post · Working on an audit for the @RSKsmart blockchain platform was one of the most fun projects we had la


Tags (automatic): Blockchain / L1-L2 / bridge


### Post — @trailofbits — 2018-01-17 18:22 UTC (2018-01-17 19:22 WAT)

- URL: https://x.com/trailofbits/status/953693965164871683
- Metrics (at fetch): bookmark 0, impression 0, like 20, quote 1, reply 1, retweet 7

> Working on an audit for the @RSKsmart blockchain platform was one of the most fun projects we had last quarter. See the results from that work on their blog! https://t.co/ss7GaEpwoF

**Quoted post (full text):**

    #### Quoted post — @16845633 — 2018-01-17 15:20 UTC (2018-01-17 16:20 WAT)
    
    - URL: https://x.com/16845633/status/953648290062618625
    - Metrics (at fetch): bookmark 0, impression 0, like 17, quote 1, reply 0, retweet 6
    
    > audit of RSKj (Bitcoin sidechain with EVM smart contracts) by @trailofbits @paddyucl @socrates1024  #BugBounty hints maybe? https://t.co/cMBvP3vAIp https://t.co/2efUnD2fPX
    
    **Quoted post** 953645634422231040: not readable via the API (deleted, private, or withheld).
    


---

## 2018-01-03 · Post · Today's Project Zero Intel bug built on work by our @Calaquendi44 https://t.co/gY4BWLriAH https://t.


### Post — @trailofbits — 2018-01-03 23:49 UTC (2018-01-04 00:49 WAT)

- URL: https://x.com/trailofbits/status/948702867740921856
- Metrics (at fetch): bookmark 0, impression 0, like 16, quote 0, reply 0, retweet 5

> Today's Project Zero Intel bug built on work by our @Calaquendi44 https://t.co/gY4BWLriAH https://t.co/S2lJSSVV6s

**Media:**
- photo: https://pbs.twimg.com/media/DSp13_AWkAIui_0.jpg — no alt text provided by author


---

## 2017-11-07 · Post · Our @Calaquendi44 will be speaking tonight at Capital (sic) Hack in DC tonight on Hardware Side Chan


### Post — @trailofbits — 2017-11-07 17:06 UTC (2017-11-07 18:06 WAT)

- URL: https://x.com/trailofbits/status/927945478582521856
- Metrics (at fetch): bookmark 0, impression 0, like 4, quote 0, reply 0, retweet 0

> Our @Calaquendi44 will be speaking tonight at Capital (sic) Hack in DC tonight on Hardware Side Channels. Come out and say hi!


---

## 2017-11-02 · Post · Are you at DevCon3 and interested in Ethereum security talks? Check out "Automatic Bug Finding for 


Tags (automatic): Blockchain / L1-L2 / bridge


### Post — @trailofbits — 2017-11-02 18:19 UTC (2017-11-02 19:19 WAT)

- URL: https://x.com/trailofbits/status/926151770614661121
- Metrics (at fetch): bookmark 0, impression 0, like 3, quote 0, reply 0, retweet 3

> Are you at #DevCon3 and interested in Ethereum security talks? Check out "Automatic Bug Finding for the Blockchain"https://t.co/kxXKUpRzvD


---

## 2017-09-22 · Post · The SEC EDGAR hack simply reflects the status quo of our digital security. https://t.co/1RV9sKowjO


### Post — @trailofbits — 2017-09-22 20:36 UTC (2017-09-22 21:36 WAT)

- URL: https://x.com/trailofbits/status/911328269978537985
- Metrics (at fetch): bookmark 0, impression 0, like 1, quote 0, reply 0, retweet 1

> The SEC EDGAR hack simply reflects the status quo of our digital security. https://t.co/1RV9sKowjO


---

## 2017-05-09 · Post · Take a whirlwind tour of next-level static analyses for bug hunting with @Calaquendi44 in this @Infi


### Post — @trailofbits — 2017-05-09 19:55 UTC (2017-05-09 20:55 WAT)

- URL: https://x.com/trailofbits/status/862033253565431811
- Metrics (at fetch): bookmark 0, impression 0, like 25, quote 0, reply 0, retweet 15

> Take a whirlwind tour of next-level static analyses for bug hunting with @Calaquendi44 in this @InfiltrateCon video https://t.co/rxyvq4CPrv


---

## 2016-11-25 · Post · Hi students! Bored this weekend? Claim bounties on Algo:


### Post — @trailofbits — 2016-11-25 20:35 UTC (2016-11-25 21:35 WAT)

- URL: https://x.com/trailofbits/status/802249356183216128
- Metrics (at fetch): bookmark 0, impression 0, like 29, quote 0, reply 2, retweet 24

> Hi students! Bored this weekend? Claim bounties on Algo:
> $500: ChromeOS support
> $250: Win10 support
> $250: go-audit
> https://t.co/JK7WC08UBW


---

## 2016-11-01 · Post · We're offering a $500 bounty for ChromeOS support in Algo. Help us close this ticket: https://t.co/F


### Post — @trailofbits — 2016-11-01 15:37 UTC (2016-11-01 16:37 WAT)

- URL: https://x.com/trailofbits/status/793477180869251073
- Metrics (at fetch): bookmark 0, impression 0, like 4, quote 0, reply 0, retweet 14

> We're offering a $500 bounty for ChromeOS support in Algo. Help us close this ticket: https://t.co/FgMe6mVE0k


---

## 2016-10-04 · Post · Mozilla paid us to audit zlib with the 400lb hacking robot in our basement. What it found will shock


### Post — @trailofbits — 2016-10-04 11:51 UTC (2016-10-04 12:51 WAT)

- URL: https://x.com/trailofbits/status/783273422893649921
- Metrics (at fetch): bookmark 0, impression 0, like 83, quote 9, reply 4, retweet 48

> Mozilla paid us to audit zlib with the 400lb hacking robot in our basement. What it found will shock you! https://t.co/3m9lOwKzrv


---

## 2016-06-03 · Post · How to instantly exploit 2000 binaries with Binary Ninja https://t.co/GO2G61rTaE https://t.co/z64erJ


### Post — @trailofbits — 2016-06-03 16:14 UTC (2016-06-03 17:14 WAT)

- URL: https://x.com/trailofbits/status/738765867001909248
- Metrics (at fetch): bookmark 1, impression 0, like 278, quote 0, reply 1, retweet 188

> How to instantly exploit 2000 binaries with Binary Ninja https://t.co/GO2G61rTaE https://t.co/z64erJvfo5

**Media:**
- photo: https://pbs.twimg.com/media/CkCfo4OUgAAnJSL.jpg — no alt text provided by author


---

## 2016-05-05 · Post · The DBIR’s ‘Forest’ of Exploit Signatures https://t.co/7pTtYALwII https://t.co/rdEQB8Cgcq


### Post — @trailofbits — 2016-05-05 20:56 UTC (2016-05-05 21:56 WAT)

- URL: https://x.com/trailofbits/status/728327464884146176
- Metrics (at fetch): bookmark 0, impression 0, like 23, quote 0, reply 0, retweet 35

> The DBIR’s ‘Forest’ of Exploit Signatures https://t.co/7pTtYALwII https://t.co/rdEQB8Cgcq

**Media:**
- photo: https://pbs.twimg.com/media/ChuJ-B4U4AA5heE.jpg — no alt text provided by author


---

## 2016-04-01 · Post · We're launching a new bug bounty for hacker handles. See the details here: https://t.co/qPQkVJybTm h


### Post — @trailofbits — 2016-04-01 11:51 UTC (2016-04-01 12:51 WAT)

- URL: https://x.com/trailofbits/status/715869114699374592
- Metrics (at fetch): bookmark 0, impression 0, like 24, quote 0, reply 3, retweet 12

> We're launching a new bug bounty for hacker handles. See the details here: https://t.co/qPQkVJybTm https://t.co/OYoGemGSkk

**Media:**
- photo: https://pbs.twimg.com/media/Ce9HKmIUMAAeTkA.jpg — no alt text provided by author


---

## 2014-10-06 · Post · JPMorgan attack shows hackers gaining upper hand in cyberwars http://t.co/zEkBft6IsP via @learmonth


### Post — @trailofbits — 2014-10-06 16:16 UTC (2014-10-06 17:16 WAT)

- URL: https://x.com/trailofbits/status/519159184466513920
- Metrics (at fetch): bookmark 0, impression 0, like 1, quote 0, reply 0, retweet 3

> JPMorgan attack shows hackers gaining upper hand in cyberwars http://t.co/zEkBft6IsP via @learmonth


---

## 2014-09-25 · Post · New 'Bash' software bug may pose bigger threat than 'Heartbleed' http://t.co/5CzMKo60tG via @reuters


### Post — @trailofbits — 2014-09-25 17:34 UTC (2014-09-25 18:34 WAT)

- URL: https://x.com/trailofbits/status/515192597782863872
- Metrics (at fetch): bookmark 0, impression 0, like 2, quote 0, reply 0, retweet 1

> New 'Bash' software bug may pose bigger threat than 'Heartbleed' http://t.co/5CzMKo60tG via @reuters


---

## 2014-04-18 · Post · TOB's Andrew Ruef talks about the Heartbleed bug on @WPBF25News http://t.co/GnujaUI26V


### Post — @trailofbits — 2014-04-18 02:07 UTC (2014-04-18 03:07 WAT)

- URL: https://x.com/trailofbits/status/456977202668896256
- Metrics (at fetch): bookmark 0, impression 0, like 1, quote 0, reply 1, retweet 1

> TOB's Andrew Ruef talks about the Heartbleed bug on @WPBF25News http://t.co/GnujaUI26V


---

## 2014-03-25 · Post · We helped @RANDCorporation understand in-the-wild exploit use for: “Markets for Cybercrime Tools and


### Post — @trailofbits — 2014-03-25 16:45 UTC (2014-03-25 17:45 WAT)

- URL: https://x.com/trailofbits/status/448500988056698880
- Metrics (at fetch): bookmark 0, impression 0, like 3, quote 0, reply 0, retweet 3

> We helped @RANDCorporation understand in-the-wild exploit use for: “Markets for Cybercrime Tools and Data” http://t.co/dZHPLtwJxu


---

## 2013-06-06 · Post · All 30 attendees of our Ruby security workshop solved the first YAML exploit lab. Great success! htt


### Post — @trailofbits — 2013-06-06 16:48 UTC (2013-06-06 17:48 WAT)

- URL: https://x.com/trailofbits/status/342684331107569664
- Metrics (at fetch): bookmark 0, impression 0, like 0, quote 0, reply 0, retweet 0

> All 30 attendees of our Ruby security workshop solved the first YAML exploit lab. Great success! http://t.co/mXDB5mo08B

**Media:**
- photo: https://pbs.twimg.com/media/BMF1lWICUAEYgTc.jpg — no alt text provided by author


---

## 2013-05-20 · Post · In case it’s not clear, we spent more time on our Elderwood report than they spent creating their la


### Post — @trailofbits — 2013-05-20 15:55 UTC (2013-05-20 16:55 WAT)

- URL: https://x.com/trailofbits/status/336510599792046080
- Metrics (at fetch): bookmark 0, impression 0, like 3, quote 0, reply 0, retweet 3

> In case it’s not clear, we spent more time on our Elderwood report than they spent creating their last attack http://t.co/zt45N1UZOr


---

## 2013-05-20 · Post · We continue our blow-by-blow of an Elderwood attack campaign with a new blog today: http://t.co/zt45


### Post — @trailofbits — 2013-05-20 15:39 UTC (2013-05-20 16:39 WAT)

- URL: https://x.com/trailofbits/status/336506407983669249
- Metrics (at fetch): bookmark 0, impression 0, like 5, quote 0, reply 0, retweet 4

> We continue our blow-by-blow of an Elderwood attack campaign with a new blog today: http://t.co/zt45N1UZOr


---

## 2013-05-15 · Post · We're delaying our next post on Elderwood so we can do more detailed testing of their exploit code. 


### Post — @trailofbits — 2013-05-15 13:37 UTC (2013-05-15 14:37 WAT)

- URL: https://x.com/trailofbits/status/334663938174238720
- Metrics (at fetch): bookmark 0, impression 0, like 0, quote 0, reply 0, retweet 0

> We're delaying our next post on Elderwood so we can do more detailed testing of their exploit code. Expect it on Friday!


---

## 2013-05-13 · Post · Elderwood and the Department of Labor Hack (1 of 5) http://t.co/1p5LSBf150


### Post — @trailofbits — 2013-05-13 16:33 UTC (2013-05-13 17:33 WAT)

- URL: https://x.com/trailofbits/status/333983401315024897
- Metrics (at fetch): bookmark 0, impression 0, like 7, quote 0, reply 1, retweet 10

> Elderwood and the Department of Labor Hack (1 of 5) http://t.co/1p5LSBf150


---

## 2012-12-12 · Post · Have a training budget at work? Learn to find and exploit modern bugs from the best! http://t.co/CZ7


### Post — @trailofbits — 2012-12-12 22:30 UTC (2012-12-12 23:30 WAT)

- URL: https://x.com/trailofbits/status/278990195955732480
- Metrics (at fetch): bookmark 0, impression 0, like 3, quote 0, reply 0, retweet 2

> Have a training budget at work? Learn to find and exploit modern bugs from the best! http://t.co/CZ7rmQIN


---

## 2012-07-16 · Post · Web exploit kit developers have demonstrated minor but largely insignificant advances in skill since


### Post — @trailofbits — 2012-07-16 22:17 UTC (2012-07-16 23:17 WAT)

- URL: https://x.com/trailofbits/status/224991156507906048
- Metrics (at fetch): bookmark 0, impression 0, like 3, quote 0, reply 0, retweet 4

> Web exploit kit developers have demonstrated minor but largely insignificant advances in skill since last year: http://t.co/6UaGrzPf


---

## 2012-04-20 · Post · We have posted slides for the Mobile Exploit Intelligence Project: http://t.co/IVkR8aO7 (cc @mikearp


### Post — @trailofbits — 2012-04-20 02:16 UTC (2012-04-20 03:16 WAT)

- URL: https://x.com/trailofbits/status/193161119802724353
- Metrics (at fetch): bookmark 0, impression 0, like 15, quote 0, reply 0, retweet 20

> We have posted slides for the Mobile Exploit Intelligence Project: http://t.co/IVkR8aO7 (cc @mikearpaia) Reddit thread: http://t.co/NfIoDM1B


---

## 2012-04-19 · Post · Dan Guido (@dguido) and Mike Arpaia (@mikearpaia) will be presenting the Mobile Exploit Intelligence


### Post — @trailofbits — 2012-04-19 17:26 UTC (2012-04-19 18:26 WAT)

- URL: https://x.com/trailofbits/status/193027764880814081
- Metrics (at fetch): bookmark 0, impression 0, like 0, quote 0, reply 0, retweet 1

> Dan Guido (@dguido) and Mike Arpaia (@mikearpaia) will be presenting the Mobile Exploit Intelligence Project at #sourcebos in 5 minutes.


---

## 2012-04-03 · Post · New podcast up with Dan Guido (@dguido) covering attacker math and exploit intel. Thanks @DennisF! h


### Post — @trailofbits — 2012-04-03 16:48 UTC (2012-04-03 17:48 WAT)

- URL: https://x.com/trailofbits/status/187220157838528512
- Metrics (at fetch): bookmark 0, impression 0, like 3, quote 0, reply 0, retweet 4

> New podcast up with Dan Guido (@dguido) covering attacker math and exploit intel. Thanks @DennisF! https://threatpost.com/en_us/blogs/dan-guido-attacker-math-and-exploit-intelligence-040312

**Links in post:** https://threatpost.com/en_us/blogs/dan-guido-attacker-math-and-exploit-intelligence-040312


---

## 2012-04-03 · Post · You can also catch the Mobile Exploit Intelligence Project in NYC at TechTarget InfoSec Decisions on


### Post — @trailofbits — 2012-04-03 13:50 UTC (2012-04-03 14:50 WAT)

- URL: https://x.com/trailofbits/status/187175124196265984
- Metrics (at fetch): bookmark 0, impression 0, like 0, quote 0, reply 0, retweet 0

> You can also catch the Mobile Exploit Intelligence Project in NYC at TechTarget InfoSec Decisions on May 15th http://infosecuritydecisions.techtarget.com/

**Links in post:** http://infosecuritydecisions.techtarget.com/


---

## 2012-04-03 · Post · Dan Guido (@dguido) will be speaking about the Mobile Exploit Intelligence Project at @SOURCEConf on


### Post — @trailofbits — 2012-04-03 13:49 UTC (2012-04-03 14:49 WAT)

- URL: https://x.com/trailofbits/status/187174882516283392
- Metrics (at fetch): bookmark 0, impression 0, like 2, quote 0, reply 0, retweet 1

> Dan Guido (@dguido) will be speaking about the Mobile Exploit Intelligence Project at @SOURCEConf on April 19th http://www.trailofbits.com/research/#mobile-eip

**Links in post:** http://www.trailofbits.com/research/#mobile-eip
