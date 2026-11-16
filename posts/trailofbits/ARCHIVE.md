# @trailofbits — full verbatim X archive (security-relevant posts)

_Generated 2026-11-16 from the X API (full-archive search + timeline). Every post below is copied word-for-word; t.co links are expanded; quoted posts are inlined in full; media are listed with alt text when the author provided it. Posts are grouped by conversation (a thread = the author's root post followed by their own replies, oldest first). Groups are newest first. An agent without X access can rely on this file._

- Posts in this file: 416
- Conversations/threads: 347
- Oldest post captured: 2012-04-03
- Newest post captured: 2026-11-12


---

## 2026-11-12 · Post · Patching is the hardest step for agents to get right. 


Tags (automatic): AI-assisted hunting


### Post — @trailofbits — 2026-11-12 22:37 UTC (2026-11-12 23:37 WAT)

- URL: https://x.com/trailofbits/status/2121009628855357931
- Metrics (at fetch): bookmark 91, impression 9408, like 145, quote 3, reply 20, retweet 11

> Patching is the hardest step for agents to get right. 
>
> We took what we learned from hundreds of Patch the Planet patches, thousands of internal Codex sessions, and a decade of fix reviews, and built it into two open-source agent plugins.                                           
>
> A good fix looks different in every codebase, and building one takes judgment and expertise. Our plugins encode best practices that work for our engineers so you can patch along at home.
>
> •patching-bugs makes an agent prove each fix: the original code fails, the patched code passes, and a full revert fails again.
> •regression-hunt checks what else the change broke, with a live proof of concept for every regression it reports.
>
> Both work best with a THREAT_MODEL.md and patching guidelines, so agents know what your project considers a bug, a regression, and an acceptable fix. 
>
> They fit naturally in loops like @OpenAI's new Daybreak Defense Factory, where agents draft patches for people to review.
> https://blog.trailofbits.com/2026/10/21/your-ai-agent-fixed-the-bug-but-what-else-did-it-change/

**Links in post:** https://twitter.com/gdb/status/2121004237413142656, https://blog.trailofbits.com/2026/10/21/your-ai-agent-fixed-the-bug-but-what-else-did-it-change/

**Quoted post (full text):**

    #### Quoted post — @162124540 — 2026-11-12 22:16 UTC (2026-11-12 23:16 WAT)
    
    - URL: https://x.com/162124540/status/2121004237413142656
    - Metrics (at fetch): bookmark 226, impression 65113, like 670, quote 28, reply 126, retweet 62
    
    > Announcing two new cyber products:
    >
    > - Daybreak Defense Factory (https://openai.com/daybreak/defense-factory/)
    > - Daybreak Red Team (https://openai.com/daybreak/red-team/)
    >
    > Both make it much easier to put frontier cyber capabilities to work, helping defend companies in new ways. https://twitter.com/OpenAI/status/2120202353907486826
    
    **Links in post:** https://openai.com/daybreak/defense-factory/, https://openai.com/daybreak/red-team/, https://twitter.com/OpenAI/status/2120202353907486826
    
    **Quoted post (full text):**
    
        #### Quoted post — @OpenAI — 2026-11-10 17:10 UTC (2026-11-10 18:10 WAT)
        
        - URL: https://x.com/OpenAI/status/2120202353907486826
        - Metrics (at fetch): bookmark 313, impression 491874, like 2237, quote 123, reply 477, retweet 153
        
        > We're turning our lessons from defending OpenAI into practical tools for our customers. On Thursday, join us at Cyber at the Frontier, a live keynote, for our latest cyber announcements.
        >
        > Working with our frontier models, we've identified and resolved important vulnerabilities in our own code and infrastructure. That experience is informing the tools and playbooks we're building to help other security teams strengthen their defenses.
        >
        > @gdb shares what we've learned and why security teams should keep putting the latest models to work as capabilities improve.
        >
        > Tune in on November 12 at 10 a.m. PT: https://openai.com/cyber-at-the-frontier/
        
        **Media:**
        - media `13_2120202060255928320` (details not returned by the API)
        
        **Links in post:** https://openai.com/cyber-at-the-frontier/
        
    


---

## 2026-11-12 · Post · Patch the Planet update: We’ve now merged 500+ fixes across 75 open-source projects, with 100 CVEs d


Tags (automatic): Memory corruption / native, AI-assisted hunting


### Post — @trailofbits — 2026-11-12 18:14 UTC (2026-11-12 19:14 WAT)

- URL: https://x.com/trailofbits/status/2120943246587392210
- Metrics (at fetch): bookmark 6, impression 3834, like 37, quote 1, reply 7, retweet 3

> Patch the Planet update: We’ve now merged 500+ fixes across 75 open-source projects, with 100 CVEs disclosed in the Linux kernel, curl, OpenSSL, nginx, vLLM, and more.
>
> https://trailofbits.com/patch-the-planet/dashboard/ https://twitter.com/OpenAI/status/2120202353907486826

**Links in post:** https://trailofbits.com/patch-the-planet/dashboard/, https://twitter.com/OpenAI/status/2120202353907486826

**Quoted post (full text):**

    #### Quoted post — @OpenAI — 2026-11-10 17:10 UTC (2026-11-10 18:10 WAT)
    
    - URL: https://x.com/OpenAI/status/2120202353907486826
    - Metrics (at fetch): bookmark 313, impression 491874, like 2237, quote 123, reply 477, retweet 153
    
    > We're turning our lessons from defending OpenAI into practical tools for our customers. On Thursday, join us at Cyber at the Frontier, a live keynote, for our latest cyber announcements.
    >
    > Working with our frontier models, we've identified and resolved important vulnerabilities in our own code and infrastructure. That experience is informing the tools and playbooks we're building to help other security teams strengthen their defenses.
    >
    > @gdb shares what we've learned and why security teams should keep putting the latest models to work as capabilities improve.
    >
    > Tune in on November 12 at 10 a.m. PT: https://openai.com/cyber-at-the-frontier/
    
    **Media:**
    - media `13_2120202060255928320` (details not returned by the API)
    
    **Links in post:** https://openai.com/cyber-at-the-frontier/
    


---

## 2026-11-06 · Post · Attackers can drain wallets by abusing a signing service, even without stealing private keys. Our 4-


### Post — @trailofbits — 2026-11-06 17:53 UTC (2026-11-06 18:53 WAT)

- URL: https://x.com/trailofbits/status/2118763769593741553
- Metrics (at fetch): bookmark 74, impression 10048, like 104, quote 7, reply 12, retweet 20

> Attackers can drain wallets by abusing a signing service, even without stealing private keys. Our 4-step post-Binance hack guidance helps wallet teams test what their signing systems can authorize and what limits the damage if signing is compromised.
>
> https://blog.trailofbits.com/2026/11/06/after-binance-check-what-your-signing-systems-can-approve/

**Links in post:** https://blog.trailofbits.com/2026/11/06/after-binance-check-what-your-signing-systems-can-approve/


---

## 2026-11-03 · Post · A cryptographically verified tally doesn't mean every vote is legitimate. Paper ballots still matter


### Post — @trailofbits — 2026-11-03 12:18 UTC (2026-11-03 13:18 WAT)

- URL: https://x.com/trailofbits/status/2117592155568972217
- Metrics (at fetch): bookmark 19, impression 4410, like 47, quote 3, reply 3, retweet 16

> A cryptographically verified tally doesn't mean every vote is legitimate. Paper ballots still matter: they provide an audit record independent of software. We explain how electronic voting works, and how cryptography can make paper-based elections more trustworthy. https://blog.trailofbits.com/2026/11/03/the-cryptography-behind-electronic-voting-and-why-paper-ballots-are-still-essential/

**Links in post:** https://blog.trailofbits.com/2026/11/03/the-cryptography-behind-electronic-voting-and-why-paper-ballots-are-still-essential/


---

## 2026-11-03 · Post · A cryptographically verified tally doesn't mean every vote is legitimate. Paper ballots still matter


### Post — @trailofbits — 2026-11-03 12:17 UTC (2026-11-03 13:17 WAT)

- URL: https://x.com/trailofbits/status/2117592037016883405
- Metrics (at fetch): bookmark 0, impression 35, like 0, quote 0, reply 0, retweet 0

> A cryptographically verified tally doesn't mean every vote is legitimate. Paper ballots still matter: they provide an audit record independent of software. We explain how electronic voting works, and how cryptography can make paper-based elections more trustworthy. https://blog.trailofbits.com/2026/11/03/the-cryptography-behind-electronic-voting-and-why-paper-ballots-are-still-essential/

**Links in post:** https://blog.trailofbits.com/2026/11/03/the-cryptography-behind-electronic-voting-and-why-paper-ballots-are-still-essential/


---

## 2026-11-02 · Post · Stable software often ships with known bugs because the fixes are never backported. That backlog is 


Tags (automatic): Memory corruption / native, AI-assisted hunting


### Post — @trailofbits — 2026-11-02 12:15 UTC (2026-11-02 13:15 WAT)

- URL: https://x.com/trailofbits/status/2117229048749228374
- Metrics (at fetch): bookmark 19, impression 5637, like 51, quote 2, reply 5, retweet 5

> Stable software often ships with known bugs because the fixes are never backported. That backlog is now an easy target for cyber-capable agents.
>
> We used Codex to cut time per backport from days to ~30 min, with 149 Linux kernel CVE fixes applied so far.
> https://blog.trailofbits.com/2026/11/02/backporting-security-fixes-at-scale-with-codex/

**Links in post:** https://blog.trailofbits.com/2026/11/02/backporting-security-fixes-at-scale-with-codex/


---

## 2026-10-29 · Post · October Trail of Bits Tribune: Releasing a PHP exploit demo, new plugins for patching, and package-i


### Post — @trailofbits — 2026-10-29 13:58 UTC (2026-10-29 14:58 WAT)

- URL: https://x.com/trailofbits/status/2115805539061879092
- Metrics (at fetch): bookmark 11, impression 3332, like 22, quote 0, reply 4, retweet 4

> October Trail of Bits Tribune: Releasing a PHP exploit demo, new plugins for patching, and package-integrity research. Plus Brotli-checker, SequenceHash, and six new public security reviews.
>
> Read the Tribune: https://mailchi.mp/trailofbits/october-2026-tribune [pic.x.com/uczCaUftT9]

**Media:**
- photo: https://pbs.twimg.com/media/HVzZ7OwW8AAj0SC.jpg — no alt text provided by author

**Links in post:** https://mailchi.mp/trailofbits/october-2026-tribune


---

## 2026-10-28 · Post · We achieved RCE via Brotli in Linux labs:


Tags (automatic): RCE


### Post — @trailofbits — 2026-10-28 19:24 UTC (2026-10-28 20:24 WAT)

- URL: https://x.com/trailofbits/status/2115525010840510574
- Metrics (at fetch): bookmark 46, impression 8936, like 120, quote 1, reply 3, retweet 27

> We achieved RCE via Brotli in Linux labs:
>
> • Node.js 24.22.0 + Express 5.3.0 (x86-64/ARM64) through its standard JSON parser 
> • Electron 41.10.7 (x86-64) using a custom-built decoding service
>
> Getting it to work requires a carefully matched setup and can take repeated attempts. [pic.x.com/cQ8B7IG7lN] https://twitter.com/trailofbits/status/2113771101058937163

**Media:**
- photo: https://pbs.twimg.com/media/HVvasyAacAACGDa.jpg — no alt text provided by author

**Links in post:** https://twitter.com/trailofbits/status/2113771101058937163

**Quoted post (full text):**

    #### Quoted post — @trailofbits — 2026-10-23 23:14 UTC (2026-10-24 00:14 WAT)
    
    - URL: https://x.com/trailofbits/status/2113771101058937163
    - Metrics (at fetch): bookmark 213, impression 30168, like 308, quote 3, reply 14, retweet 69
    
    > We’re still testing how exploitable the Node.js/Brotli bug is, but we’ve found that it’s surprisingly hard to tell whether you’re even affected.
    >
    > So @ToBScottA built a scanner that finds hidden copies of the decoder, even in stripped binaries.
    > https://github.com/trailofbits/brotli-checker
    
    **Links in post:** https://github.com/trailofbits/brotli-checker
    


---

## 2026-10-26 · Post · Our demo shows PHP2Shell giving a shell on MediaWiki, Symfony, Laravel, and phpBB.


### Post — @trailofbits — 2026-10-26 22:01 UTC (2026-10-26 23:01 WAT)

- URL: https://x.com/trailofbits/status/2114839775173906751
- Metrics (at fetch): bookmark 153, impression 40044, like 287, quote 7, reply 14, retweet 51

> Our demo shows PHP2Shell giving a shell on MediaWiki, Symfony, Laravel, and phpBB.
>
> We’ve confirmed exploits work on pre-patch releases of PHP 8.2–8.5. If you haven’t updated, assume attackers can compromise your server, and that exploitation will only get easier. [pic.x.com/6BMOwrSujk] https://twitter.com/dguido/status/2113825891021144306

**Media:**
- video: https://pbs.twimg.com/amplify_video_thumb/2114839531509948416/img/AwstQiJUX69AwVdr.jpg — no alt text provided by author

**Links in post:** https://twitter.com/dguido/status/2113825891021144306

**Quoted post (full text):**

    #### Quoted post — @14290525 — 2026-10-24 02:52 UTC (2026-10-24 03:52 WAT)
    
    - URL: https://x.com/14290525/status/2113825891021144306
    - Metrics (at fetch): bookmark 473, impression 110440, like 678, quote 20, reply 39, retweet 105
    
    > Update: Our PHP exploit is now production-grade.
    > * stock php.ini-production, display_errors=off, normal memory_limit, multi-worker, ASLR, under load
    > * ARM64 + x86-64 targets
    > * MediaWiki, WordPress, phpBB, Laravel
    > * Apache/mod_php and nginx/php-fpm -&gt; root
    > https://x.com/dguido/status/2113129153293897925 [pic.x.com/CAF1htNW0o]
    
    **Media:**
    - media `13_2113825813195866112` (details not returned by the API)
    
    **Links in post:** https://x.com/dguido/status/2113129153293897925
    
    **Quoted post (full text):**
    
        #### Quoted post — @14290525 — 2026-10-22 04:43 UTC (2026-10-22 05:43 WAT)
        
        - URL: https://x.com/14290525/status/2113129153293897925
        - Metrics (at fetch): bookmark 329, impression 109681, like 437, quote 7, reply 15, retweet 75
        
        > Re: the widely circulated blog claiming the PHP bugs aren't easily exploitable: @trailofbits has a working exploit that gets a shell on an unmodified MediaWiki installation.
        > https://eliastaylor.com/noexploit/ [pic.x.com/WLFLGj9i9V]
        
        **Media:**
        - media `3_2113126032609792000` (details not returned by the API)
        
        **Links in post:** https://eliastaylor.com/noexploit/
        
    


---

## 2026-10-23 · Post · We’re still testing how exploitable the Node.js/Brotli bug is, but we’ve found that it’s surprisingl


### Post — @trailofbits — 2026-10-23 23:14 UTC (2026-10-24 00:14 WAT)

- URL: https://x.com/trailofbits/status/2113771101058937163
- Metrics (at fetch): bookmark 213, impression 30168, like 308, quote 3, reply 14, retweet 69

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
- Metrics (at fetch): bookmark 56, impression 13128, like 152, quote 3, reply 3, retweet 19

> We got a PHP exploit working against MediaWiki, but getting freed memory reused just right takes some tinkering under normal traffic. 
>
> LLMs struggle here without an expert's guidance, which may help explain the attempts but no confirmed successes. https://twitter.com/dguido/status/2113129153293897925

**Links in post:** https://twitter.com/dguido/status/2113129153293897925

**Quoted post (full text):**

    #### Quoted post — @14290525 — 2026-10-22 04:43 UTC (2026-10-22 05:43 WAT)
    
    - URL: https://x.com/14290525/status/2113129153293897925
    - Metrics (at fetch): bookmark 329, impression 109681, like 437, quote 7, reply 15, retweet 75
    
    > Re: the widely circulated blog claiming the PHP bugs aren't easily exploitable: @trailofbits has a working exploit that gets a shell on an unmodified MediaWiki installation.
    > https://eliastaylor.com/noexploit/ [pic.x.com/WLFLGj9i9V]
    
    **Media:**
    - media `3_2113126032609792000` (details not returned by the API)
    
    **Links in post:** https://eliastaylor.com/noexploit/
    


---

## 2026-10-22 · Post · “You want to find the bugs, but it’s only good if you can also fix them.”—@anishrnaik on Risky Biz.


### Post — @trailofbits — 2026-10-22 11:03 UTC (2026-10-22 12:03 WAT)

- URL: https://x.com/trailofbits/status/2113224633105138021
- Metrics (at fetch): bookmark 5, impression 2744, like 34, quote 0, reply 3, retweet 3

> “You want to find the bugs, but it’s only good if you can also fix them.”—@anishrnaik on Risky Biz.
>
> Many open-source projects have only a handful of maintainers, and fixes are falling behind. We’re building a reusable toolkit to help.
>
> Full pod: https://www.youtube.com/watch?v=6SIgPjQ9V1g [pic.x.com/t3qPBamUdN]

**Media:**
- video: https://pbs.twimg.com/ext_tw_video_thumb/2113224546916372480/pu/img/NKu8hV9R7GqLxj8F.jpg — no alt text provided by author

**Links in post:** https://www.youtube.com/watch?v=6SIgPjQ9V1g


---

## 2026-10-21 · Post · Yesterday, rumors started circulating about two unpatched critical-severity bugs in PHP. 


Tags (automatic): AI-assisted hunting


### Post — @trailofbits — 2026-10-21 22:02 UTC (2026-10-21 23:02 WAT)

- URL: https://x.com/trailofbits/status/2113028241128821204
- Metrics (at fetch): bookmark 36, impression 5875, like 87, quote 3, reply 6, retweet 14

> Yesterday, rumors started circulating about two unpatched critical-severity bugs in PHP. 
>
> Within 17 hours, Cloudflare was blocking attacks and Patchstack reported active exploitation. 
>
> When AI can develop a working exploit in hours, bugs need to be patched just as fast.        
>
> Each day without a fix carries the risk that an attacker will find and exploit the bug. But it takes time to create a working patch, and PHP's patch was more complex than most.  
>
> The patch changed 402 files and added more than 11,000 lines, reworking core engine behavior that dozens of extensions depended on. The bug was reported on Aug 11, and fixes were shipped 71 days later. But less than a day after details leaked, systems running PHP were already under attack.  
>
> Patching needs to keep up with the pace of bug discovery. For the past four months, we’ve worked directly with open-source projects as part of Patch the Planet to understand how AI can expedite patching. Our ongoing research and work show that project-specific documentation, skills, and plugins can be embedded at the repo level to give agents and contributors access to the context maintainers carry in their heads: what counts as a bug, how a fix should look, and what can't break.  
>
> Our two new open-source plugins, patching-bugs and regression-hunt, are a first step toward a generalized set of tools and guidance for getting a working patch out faster: https://blog.trailofbits.com/2026/10/21/your-ai-agent-fixed-the-bug-but-what-else-did-it-change/ 
>
> PHP’s account of the incident: https://thephp.foundation/blog/2026/10/21/todays-php-security-release-and-how-were-strengthening-php-security/

**Links in post:** https://blog.trailofbits.com/2026/10/21/your-ai-agent-fixed-the-bug-but-what-else-did-it-change/, https://thephp.foundation/blog/2026/10/21/todays-php-security-release-and-how-were-strengthening-php-security/


---

## 2026-10-21 · Post · Finding bugs is the easy part. Shipping fixes that hold up is harder.


Tags (automatic): AI-assisted hunting


### Post — @trailofbits — 2026-10-21 16:04 UTC (2026-10-21 17:04 WAT)

- URL: https://x.com/trailofbits/status/2112938091585351824
- Metrics (at fetch): bookmark 99, impression 20818, like 143, quote 13, reply 17, retweet 24

> Finding bugs is the easy part. Shipping fixes that hold up is harder.
>
> We analyzed thousands of Codex sessions from our work on Patch the Planet with @OpenAI and built patching-bugs, a plugin that writes a fix, proves it, and checks it for regressions.                                                                                               
>
> To prove a fix, the plugin checks that the original code fails, the patch passes, and reverting the patch brings the bug back.
>
> patching-bugs hands each fix to regression-hunt, our second new plugin. We ran it on the patches behind 21 known regressions, and it reported 25% fewer false positives than a baseline Codex agent.
>
> Both plugins work best when your repo has a THREAT_MODEL.md and a PATCHING_GUIDELINES.md. https://blog.trailofbits.com/2026/10/21/your-ai-agent-fixed-the-bug-but-what-else-did-it-change/

**Links in post:** https://blog.trailofbits.com/2026/10/21/your-ai-agent-fixed-the-bug-but-what-else-did-it-change/


---

## 2026-10-20 · Post · We’re heading to Mumbai for @EFDevcon 8 to talk security with Ethereum builders. Meet our team at bo


### Post — @trailofbits — 2026-10-20 17:32 UTC (2026-10-20 18:32 WAT)

- URL: https://x.com/trailofbits/status/2112597938589278371
- Metrics (at fetch): bookmark 0, impression 2023, like 24, quote 0, reply 1, retweet 2

> We’re heading to Mumbai for @EFDevcon 8 to talk security with Ethereum builders. Meet our team at booth Starter 06, November 3–4, to talk about what you're building, where it can fail, and how to test it. https://twitter.com/EFDevcon/status/2112589668814344499

**Links in post:** https://twitter.com/EFDevcon/status/2112589668814344499

**Quoted post (full text):**

    #### Quoted post — @1013526003015184385 — 2026-10-20 17:00 UTC (2026-10-20 18:00 WAT)
    
    - URL: https://x.com/1013526003015184385/status/2112589668814344499
    - Metrics (at fetch): bookmark 0, impression 4108, like 44, quote 1, reply 3, retweet 1
    
    > We're excited to welcome @trailofbits as a supporter of Devcon 8!🎉
    >
    > With over a decade of experience in security research, Trail of Bits helps teams identify vulnerabilities, strengthen their code &amp; build more secure systems.
    >
    > Meet their team in Mumbai at their booth on Nov 3–4. [pic.x.com/syFQqEULJf]
    
    **Media:**
    - media `13_2112571070196641792` (details not returned by the API)
    


---

## 2026-10-15 · Post · We tested 25 package managers against a simulated malicious repository. Without a lockfile, only Go 


### Post — @trailofbits — 2026-10-15 13:01 UTC (2026-10-15 14:01 WAT)

- URL: https://x.com/trailofbits/status/2110717790810239270
- Metrics (at fetch): bookmark 22, impression 10346, like 76, quote 7, reply 6, retweet 15

> We tested 25 package managers against a simulated malicious repository. Without a lockfile, only Go and vcpkg verified every download in our tests. With a lockfile, it's fewer than half.
>
> https://blog.trailofbits.com/2026/10/14/package-managers-have-an-integrity-problem/

**Links in post:** https://blog.trailofbits.com/2026/10/14/package-managers-have-an-integrity-problem/


---

## 2026-10-13 · Post · "Every one of these maintainers has these two wolves in them."


Tags (automatic): AI-assisted hunting


### Post — @trailofbits — 2026-10-13 13:22 UTC (2026-10-13 14:22 WAT)

- URL: https://x.com/trailofbits/status/2109998148206694655
- Metrics (at fetch): bookmark 5, impression 2572, like 17, quote 1, reply 3, retweet 3

> "Every one of these maintainers has these two wolves in them."
>
> @thebensams on @hackaday's FLOSS Weekly, on why some maintainers go all-in on AI agents and others, a lot of them in Rust, won't unless they're forced to. https://www.youtube.com/watch?v=TaTxSyGMcmM [pic.x.com/h52orkGtUq]

**Media:**
- video: https://pbs.twimg.com/ext_tw_video_thumb/2109998097447153664/pu/img/EL8aokIfmrlbB1dA.jpg — no alt text provided by author

**Links in post:** https://www.youtube.com/watch?v=TaTxSyGMcmM


---

## 2026-10-05 · Post · We're hiring a Solutions Architect to own the technical strategy for our key clients, stay with acco


### Post — @trailofbits — 2026-10-05 17:02 UTC (2026-10-05 18:02 WAT)

- URL: https://x.com/trailofbits/status/2107154463106421009
- Metrics (at fetch): bookmark 7, impression 3690, like 20, quote 0, reply 1, retweet 3

> We're hiring a Solutions Architect to own the technical strategy for our key clients, stay with accounts after each engagement, and design the program that follows.
>
> Remote, US or Canada. https://apply.workable.com/trailofbits/j/8B4F20779A/

**Links in post:** https://apply.workable.com/trailofbits/j/8B4F20779A/


---

## 2026-10-05 · Post · We're sponsoring @arbitrum's Open House Singapore, hosted in collaboration with Robinhood Chain, to 


Tags (automatic): Blockchain / L1-L2 / bridge


### Post — @trailofbits — 2026-10-05 14:02 UTC (2026-10-05 15:02 WAT)

- URL: https://x.com/trailofbits/status/2107109116166455611
- Metrics (at fetch): bookmark 0, impression 5486, like 34, quote 1, reply 3, retweet 7

> We're sponsoring @arbitrum's Open House Singapore, hosted in collaboration with Robinhood Chain, to support founders across both the online Buildathon and Founder House.
>
> From October 23-25, Founder House Singapore brings selected teams together for 3 days of product, technical, and go-to-market support to help turn early ideas into launch-ready onchain products, while competing for a share of $300K in prizes and grants.
>
> Founder House teams will get a remote mentoring session with @gintaria from our team.
>
> Apply here: https://luma.com/openhouse-singapore?utm_source=src.sponsor-trailofbits~med.social~cmp.oh-singapore-founder-house

**Links in post:** https://luma.com/openhouse-singapore?utm_source=src.sponsor-trailofbits~med.social~cmp.oh-singapore-founder-house


---

## 2026-10-02 · Post · Hashing multiple values together is easy to get wrong, and mistakes can lead to forgeries worth mill


### Post — @trailofbits — 2026-10-02 11:15 UTC (2026-10-02 12:15 WAT)

- URL: https://x.com/trailofbits/status/2105979911437537534
- Metrics (at fetch): bookmark 21, impression 3579, like 45, quote 2, reply 7, retweet 8

> Hashing multiple values together is easy to get wrong, and mistakes can lead to forgeries worth millions in zero-knowledge proofs. We built SequenceHash and SequenceMAC to fix that for any hash function, not just Keccak. https://blog.trailofbits.com/2026/10/02/sequencehash-multihashing-for-the-rest-of-us/

**Links in post:** https://blog.trailofbits.com/2026/10/02/sequencehash-multihashing-for-the-rest-of-us/


---

## 2026-09-30 · Post · September Trail of Bits Tribune: Fact-checking 1Password's AI patching benchmark, and a signature-fo


Tags (automatic): ZK, AI-assisted hunting


### Post — @trailofbits — 2026-09-30 13:20 UTC (2026-09-30 14:20 WAT)

- URL: https://x.com/trailofbits/status/2105286717640966539
- Metrics (at fetch): bookmark 3, impression 5725, like 22, quote 0, reply 0, retweet 3

> September Trail of Bits Tribune: Fact-checking 1Password's AI patching benchmark, and a signature-forgery bug in Miden's zkVM. Also: a string-slicing bug in Lean, 27 advisory submissions to OpenClaw, and seven new security reviews.
>
> https://mailchi.mp/trailofbits/september-2026-tribune [pic.x.com/z32C0a30r7]

**Media:**
- photo: https://pbs.twimg.com/media/HTd6_tEXYAMh8hT.png — no alt text provided by author

**Links in post:** https://mailchi.mp/trailofbits/september-2026-tribune


---

## 2026-09-29 · Post · We've reviewed AvalancheGo, libevm, and Subnet EVM for @AvaLabs. We also built Slither, Echidna, and


Tags (automatic): Blockchain / L1-L2 / bridge


### Post — @trailofbits — 2026-09-29 15:05 UTC (2026-09-29 16:05 WAT)

- URL: https://x.com/trailofbits/status/2104950711700058529
- Metrics (at fetch): bookmark 5, impression 4253, like 27, quote 2, reply 3, retweet 2

> We've reviewed AvalancheGo, libevm, and Subnet EVM for @AvaLabs. We also built Slither, Echidna, and Medusa, and published 391 blockchain security reviews.
>
> Avalanche builders can now request an audit from us through the Avalanche Audit Marketplace. https://build.avax.network/audits/firms https://twitter.com/AvaxDevelopers/status/2104949988459770024

**Links in post:** https://build.avax.network/audits/firms, https://twitter.com/AvaxDevelopers/status/2104949988459770024

**Quoted post (full text):**

    #### Quoted post — @1648403727592701956 — 2026-09-29 15:02 UTC (2026-09-29 16:02 WAT)
    
    - URL: https://x.com/1648403727592701956/status/2104949988459770024
    - Metrics (at fetch): bookmark 15, impression 31276, like 203, quote 22, reply 25, retweet 63
    
    > The Avalanche Audit Marketplace is live on the Builder Hub 🔺
    >
    > One request reaches all Ava Labs vetted firms. Quotes stay private, you pick one, and the program can cover up to 75% of the cost.
    >
    > $0 fees for builders and auditors.
    >
    > Request quotes 👇 [pic.x.com/x4AjleD6lq]
    
    **Media:**
    - media `3_2104949651816239104` (details not returned by the API)
    


---

## 2026-09-29 · Post · We've reviewed AvalancheGo, libevm, and Subnet EVM for Ava Labs. We also built Slither, Echidna, and


Tags (automatic): Blockchain / L1-L2 / bridge


### Post — @trailofbits — 2026-09-29 15:05 UTC (2026-09-29 16:05 WAT)

- URL: https://x.com/trailofbits/status/2104950583648223557
- Metrics (at fetch): bookmark 0, impression 323, like 0, quote 0, reply 0, retweet 0

> We've reviewed AvalancheGo, libevm, and Subnet EVM for Ava Labs. We also built Slither, Echidna, and Medusa, and published 391 blockchain security reviews.
>
> Avalanche builders can now request an audit from us through the Avalanche Audit Marketplace. https://build.avax.network/audits/firms https://twitter.com/AvaxDevelopers/status/2104949988459770024

**Links in post:** https://build.avax.network/audits/firms, https://twitter.com/AvaxDevelopers/status/2104949988459770024

**Quoted post (full text):**

    #### Quoted post — @1648403727592701956 — 2026-09-29 15:02 UTC (2026-09-29 16:02 WAT)
    
    - URL: https://x.com/1648403727592701956/status/2104949988459770024
    - Metrics (at fetch): bookmark 15, impression 31276, like 203, quote 22, reply 25, retweet 63
    
    > The Avalanche Audit Marketplace is live on the Builder Hub 🔺
    >
    > One request reaches all Ava Labs vetted firms. Quotes stay private, you pick one, and the program can cover up to 75% of the cost.
    >
    > $0 fees for builders and auditors.
    >
    > Request quotes 👇 [pic.x.com/x4AjleD6lq]
    
    **Media:**
    - media `3_2104949651816239104` (details not returned by the API)
    


---

## 2026-09-25 · Post · Threshold signatures secure billions in crypto and increasingly run inside TEEs. But MPC and TEEs ma


Tags (automatic): TEE / enclave


### Post — @trailofbits — 2026-09-25 11:11 UTC (2026-09-25 12:11 WAT)

- URL: https://x.com/trailofbits/status/2103442265859387662
- Metrics (at fetch): bookmark 19, impression 3704, like 61, quote 0, reply 4, retweet 9

> Threshold signatures secure billions in crypto and increasingly run inside TEEs. But MPC and TEEs make different bets on trust: MPC spreads it across independent parties; TEEs concentrate it in the hardware manufacturer and its attestation infrastructure. https://blog.trailofbits.com/2026/09/25/dont-let-tees-break-your-mpc/

**Links in post:** https://blog.trailofbits.com/2026/09/25/dont-let-tees-break-your-mpc/


---

## 2026-09-24 · Post · We're the only red team for @ARIA_research's Safeguarded AI programme, led by @ammannnora.


Tags (automatic): AI-assisted hunting


### Post — @trailofbits — 2026-09-24 16:44 UTC (2026-09-24 17:44 WAT)

- URL: https://x.com/trailofbits/status/2103163612768702501
- Metrics (at fetch): bookmark 9, impression 6790, like 48, quote 2, reply 3, retweet 8

> We're the only red team for @ARIA_research's Safeguarded AI programme, led by @ammannnora.
>
> Each development cycle, we attack the code, its proofs, and everything those proofs rest on: the models, specs, assumptions, and deployment choices behind every team's assurance case. https://twitter.com/ARIA_research/status/2103061040632139954

**Links in post:** https://twitter.com/ARIA_research/status/2103061040632139954

**Quoted post (full text):**

    #### Quoted post — @1357299664115142657 — 2026-09-24 09:56 UTC (2026-09-24 10:56 WAT)
    
    - URL: https://x.com/1357299664115142657/status/2103061040632139954
    - Metrics (at fetch): bookmark 39, impression 25422, like 91, quote 9, reply 2, retweet 16
    
    > AI-enabled cyber attacks are getting faster + going further. But what if AI-enabled formal methods could make high-assurance cyber defence practical at unprecedented speed + scale? We’re funding eight teams with £22m to test that idea. Meet them here: https://link.aria.org.uk/SAI-TA2-Creators-X [pic.x.com/6H9vxHZC45]
    
    **Media:**
    - media `13_2103060043763466240` (details not returned by the API)
    
    **Links in post:** https://link.aria.org.uk/SAI-TA2-Creators-X
    


---

## 2026-09-24 · Post · We're hiring a Senior Developer Relations Engineer who builds and ships, with the security depth to 


### Post — @trailofbits — 2026-09-24 14:01 UTC (2026-09-24 15:01 WAT)

- URL: https://x.com/trailofbits/status/2103122611823677691
- Metrics (at fetch): bookmark 6, impression 2999, like 21, quote 0, reply 1, retweet 3

> We're hiring a Senior Developer Relations Engineer who builds and ships, with the security depth to work alongside our engineers and open-source maintainers. 
>
> Apply here: https://apply.workable.com/trailofbits/j/427E4C8AA4/ [pic.x.com/VJ5GS5613K]

**Media:**
- photo: https://pbs.twimg.com/media/HS_K3QNW0AAsylD.jpg — no alt text provided by author

**Links in post:** https://apply.workable.com/trailofbits/j/427E4C8AA4/


---

## 2026-09-23 · Post · We reviewed @bee__computer Private Compute's mobile apps, servers, and AMI builder and reported 21 i


### Post — @trailofbits — 2026-09-23 23:41 UTC (2026-09-24 00:41 WAT)

- URL: https://x.com/trailofbits/status/2102906181882916953
- Metrics (at fetch): bookmark 20, impression 7549, like 55, quote 2, reply 3, retweet 3

> We reviewed @bee__computer Private Compute's mobile apps, servers, and AMI builder and reported 21 issues. Amazon fixed all 7 high-severity findings and published the full report.
> https://github.com/trailofbits/publications/blob/master/reviews/2026-09-amazonbeeprivatecompute-securityreview.pdf https://twitter.com/EthanSutin/status/2102902595249652071

**Links in post:** https://github.com/trailofbits/publications/blob/master/reviews/2026-09-amazonbeeprivatecompute-securityreview.pdf, https://twitter.com/EthanSutin/status/2102902595249652071

**Quoted post (full text):**

    #### Quoted post — @136114696 — 2026-09-23 23:27 UTC (2026-09-24 00:27 WAT)
    
    - URL: https://x.com/136114696/status/2102902595249652071
    - Metrics (at fetch): bookmark 28, impression 14247, like 63, quote 2, reply 13, retweet 3
    
    > Personal AI should have frontier intelligence without sacrificing privacy. That's why we built Bee Private Compute.
    >
    > Bee believes trust is built on transparency, so today we are publishing our whitepaper and a third-party audit performed by @trailofbits.
    


---

## 2026-09-21 · Post · Our @openclaw security assessment produced 27 advisories, 3 hardening PRs, and 1 architectural submi


### Post — @trailofbits — 2026-09-21 20:39 UTC (2026-09-21 21:39 WAT)

- URL: https://x.com/trailofbits/status/2102135648224481765
- Metrics (at fetch): bookmark 21, impression 7893, like 64, quote 1, reply 6, retweet 7

> Our @openclaw security assessment produced 27 advisories, 3 hardening PRs, and 1 architectural submission.
>
> Read the report: 
> https://github.com/trailofbits/publications/blob/master/reviews/2026-09-openai-openclaw-securityreview.pdf https://twitter.com/joshavant/status/2102036150739169745

**Links in post:** https://github.com/trailofbits/publications/blob/master/reviews/2026-09-openai-openclaw-securityreview.pdf, https://twitter.com/joshavant/status/2102036150739169745

**Quoted post (full text):**

    #### Quoted post — @123978606 — 2026-09-21 14:04 UTC (2026-09-21 15:04 WAT)
    
    - URL: https://x.com/123978606/status/2102036150739169745
    - Metrics (at fetch): bookmark 40, impression 455167, like 150, quote 7, reply 8, retweet 9
    
    > Excited to have had the chance to work with @trailofbits via the @OpenAI Patch the Planet initiative to do a security audit on OpenClaw!
    >
    > Security is paramount at @openclaw 🔒
    > https://openclaw.ai/blog/openclaw-trail-of-bits-engagement-recap
    
    **Links in post:** https://openclaw.ai/blog/openclaw-trail-of-bits-engagement-recap
    


---

## 2026-09-21 · Post · A 2012 USENIX paper brought XML Signature Wrapping (XSW) attacks against SAML into the mainstream. S


### Post — @trailofbits — 2026-09-21 11:18 UTC (2026-09-21 12:18 WAT)

- URL: https://x.com/trailofbits/status/2101994434191585303
- Metrics (at fetch): bookmark 12, impression 3347, like 41, quote 0, reply 5, retweet 9

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
- Metrics (at fetch): bookmark 120, impression 26312, like 203, quote 7, reply 14, retweet 27

> We audited parts of @0xMiden's zkVM, written in a custom assembly language called MASM. MASM originally had no developer tooling, so we used Claude and Codex to build a decompiler and static-analysis engine. It flagged a signature-forgery bug that could've cost millions. https://blog.trailofbits.com/2026/09/18/auditing-in-the-age-of-good-enough-ai/ @fegge

**Links in post:** https://blog.trailofbits.com/2026/09/18/auditing-in-the-age-of-good-enough-ai/


---

## 2026-09-16 · Post · We’re hiring an Engineering Director to lead Application Security. We want someone who still finds b


Tags (automatic): AI-assisted hunting


### Post — @trailofbits — 2026-09-16 14:11 UTC (2026-09-16 15:11 WAT)

- URL: https://x.com/trailofbits/status/2100226150538588544
- Metrics (at fetch): bookmark 10, impression 4187, like 53, quote 0, reply 2, retweet 7

> We’re hiring an Engineering Director to lead Application Security. We want someone who still finds bugs in code, builds excellent teams, and has a clear view of how AI impacts security audits.
>
> Apply here: https://apply.workable.com/trailofbits/j/336A3CC4BC [pic.x.com/NgPfsCmG2E]

**Media:**
- photo: https://pbs.twimg.com/media/HSV-S3yWMAA2jVc.jpg — no alt text provided by author

**Links in post:** https://apply.workable.com/trailofbits/j/336A3CC4BC


---

## 2026-09-16 · Post · We’re hiring an Engineering Director to lead Application Security. We want someone who still finds b


Tags (automatic): AI-assisted hunting


### Post — @trailofbits — 2026-09-16 14:01 UTC (2026-09-16 15:01 WAT)

- URL: https://x.com/trailofbits/status/2100223666583654680
- Metrics (at fetch): bookmark 1, impression 494, like 1, quote 0, reply 0, retweet 0

> We’re hiring an Engineering Director to lead Application Security. We want someone who still finds bugs in code, builds excellent teams, and has a clear view of how AI impacts security audits.
>
> Apply here: https://apply.workable.com/trailofbits/j/336A3CC4BC [pic.x.com/OJEHiuDnbj]

**Media:**
- photo: https://pbs.twimg.com/media/HSV-S3yWMAA2jVc.jpg — no alt text provided by author

**Links in post:** https://apply.workable.com/trailofbits/j/336A3CC4BC


---

## 2026-09-15 · Thread · .@1Password's FLAWED report says AI models produce a clean security fix only 26% of the time.


Tags (automatic): AI-assisted hunting


### Post — @trailofbits — 2026-09-15 11:15 UTC (2026-09-15 12:15 WAT)

- URL: https://x.com/trailofbits/status/2099819316745060639
- Metrics (at fetch): bookmark 97, impression 557234, like 268, quote 13, reply 24, retweet 49

> .@1Password's FLAWED report says AI models produce a clean security fix only 26% of the time.
>
> Defenders shouldn't take that number seriously.                                                                                                                                        
>
> • The six vulnerabilities were handpicked because their fixes were complex. Clean-fix rates ran from 3% to 60% depending on the bug, and the report averaged them together.
>
> • Agents set up to fail were counted in the headline figure. Two of 1Password's prompts instructed the agent to apply the wrong fix. Those trials make up 22% of the data. One evaluation mode prevented the agent from compiling or running any code, and it accounts for 36% of the data.
>
> • The report ran two models, GPT-5.5 at medium effort and Opus 4.8 at high. Neither was tested at its highest available setting, so the report says nothing about how more effort or stronger models change the results.
>
> • Several instruction and grading errors further undercut the headline, and are elaborated upon in the attached blog.
>
> We've spent four months submitting hundreds of AI-authored patches to widely adopted open-source projects as part of Patch the Planet.
>
> Our experience didn't match 1Password's report, so we did a full analysis across 186 AI-authored pull requests and 33,500 subsequent commits, benchmarked against 2,265 human-authored patches we graded across years of security engagements. https://blog.trailofbits.com/2026/09/15/1passwords-ai-patching-benchmark-is-misleading/

**Links in post:** https://blog.trailofbits.com/2026/09/15/1passwords-ai-patching-benchmark-is-misleading/


### Thread part 2 — @trailofbits — 2026-09-15 11:15 UTC (2026-09-15 12:15 WAT)

- URL: https://x.com/trailofbits/status/2099819318028452343
- Metrics (at fetch): bookmark 13, impression 5031, like 26, quote 2, reply 3, retweet 2

> @1Password Alongside our analysis, we’re releasing two new skills: post-patch-validation to help agents test fixes, and review-walkthrough to help engineers review them. Both are now available in our skills repo. https://github.com/trailofbits/skills

**Links in post:** https://github.com/trailofbits/skills


---

## 2026-09-10 · Post · Our engineer Joe Doyle built trailmix, the quantum circuit toolkit we open-sourced in June. The pape


Tags (automatic): ZK


### Post — @trailofbits — 2026-09-10 21:22 UTC (2026-09-10 22:22 WAT)

- URL: https://x.com/trailofbits/status/2098160138591039879
- Metrics (at fetch): bookmark 26, impression 7554, like 77, quote 2, reply 4, retweet 12

> Our engineer Joe Doyle built trailmix, the quantum circuit toolkit we open-sourced in June. The paper's leading circuits build on it, and his leaderboard submissions helped push the score past Google's. https://github.com/trailofbits/trailmix https://twitter.com/eigenlabs/status/2098037456067244098

**Links in post:** https://github.com/trailofbits/trailmix, https://twitter.com/eigenlabs/status/2098037456067244098

**Quoted post (full text):**

    #### Quoted post — @1707105432630915072 — 2026-09-10 13:14 UTC (2026-09-10 14:14 WAT)
    
    - URL: https://x.com/1707105432630915072/status/2098037456067244098
    - Metrics (at fetch): bookmark 37, impression 113091, like 242, quote 35, reply 30, retweet 59
    
    > The first full paper on http://ECDSA.fail is on arXiv
    >
    > In March, Google Quantum AI reported a more efficient quantum circuit for a core step in breaking the signatures behind Bitcoin and Ethereum. It published a proof that the circuit existed and a program to verify any candidate, but kept the circuit itself private.
    >
    > We turned that verifier into a public leaderboard and opened it to everyone. Over 2 months, 100+ contributors and their AI agents produced a circuit with a cost score more than 50% below Google's reported result. The live leaderboard has since moved to 62% ahead.
    >
    > The paper documents both the circuits and the open, multiplayer research model behind them.
    >
    > That model is now @YukonResearch.
    >
    > And the challenge is still open.
    
    **Media:**
    - media `3_2098034295076253696` (details not returned by the API)
    
    **Links in post:** https://ECDSA.fail, http://ECDSA.fail
    


---

## 2026-09-09 · Post · Last week, @AnthropicAI formalized Fermat's Last Theorem in 13 million lines of Lean code.


### Post — @trailofbits — 2026-09-09 11:15 UTC (2026-09-09 12:15 WAT)

- URL: https://x.com/trailofbits/status/2097644988121104815
- Metrics (at fetch): bookmark 128, impression 45844, like 486, quote 22, reply 17, retweet 64

> Last week, @AnthropicAI formalized Fermat's Last Theorem in 13 million lines of Lean code.
>
> We "proved" that same theorem in 20 lines by exploiting a bug we found in Lean. https://blog.trailofbits.com/2026/09/09/a-proof-of-fermats-last-theorem-that-fits-the-margin/

**Links in post:** https://blog.trailofbits.com/2026/09/09/a-proof-of-fermats-last-theorem-that-fits-the-margin/


---

## 2026-09-08 · Post · OpenSSL's latest advisory covers 9 patched vulnerabilities. Our engineers Filipe Casal and Opal Wrig


### Post — @trailofbits — 2026-09-08 15:43 UTC (2026-09-08 16:43 WAT)

- URL: https://x.com/trailofbits/status/2097350089089908950
- Metrics (at fetch): bookmark 4, impression 4646, like 45, quote 0, reply 0, retweet 14

> OpenSSL's latest advisory covers 9 patched vulnerabilities. Our engineers Filipe Casal and Opal Wright found 4 of them as part of Patch the Planet.
> https://openssl-library.org/news/secadv/20260825.txt

**Links in post:** https://openssl-library.org/news/secadv/20260825.txt


---

## 2026-09-04 · Post · aiohttp is downloaded 600M+ times a month. Its maintainers just recapped a year of security work, in


### Post — @trailofbits — 2026-09-04 11:02 UTC (2026-09-04 12:02 WAT)

- URL: https://x.com/trailofbits/status/2095829855279395125
- Metrics (at fetch): bookmark 7, impression 3290, like 27, quote 0, reply 3, retweet 4

> aiohttp is downloaded 600M+ times a month. Its maintainers just recapped a year of security work, including the 10 issues (8 CVEs) we reported through Patch the Planet.
>
> Every fix shipped days later in 3.14.1. https://aio-libs.org/news/2026/security-at-aio-libs/

**Links in post:** https://aio-libs.org/news/2026/security-at-aio-libs/


---

## 2026-09-03 · Post · 1,535 potential bugs found, 1,017 awaiting patches, 326 fixes open upstream, 192 merged.


Tags (automatic): AI-assisted hunting


### Post — @trailofbits — 2026-09-03 14:05 UTC (2026-09-03 15:05 WAT)

- URL: https://x.com/trailofbits/status/2095513427028377637
- Metrics (at fetch): bookmark 10, impression 4802, like 37, quote 1, reply 1, retweet 12

> 1,535 potential bugs found, 1,017 awaiting patches, 326 fixes open upstream, 192 merged.
>
> Since Aug 4: +398 bugs, +46 merged, 55 codebases under review, and scapy has overtaken vllm as the most-reported codebase in Patch the Planet.
>
> https://trailofbits.com/patch-the-planet/dashboard/

**Links in post:** https://trailofbits.com/patch-the-planet/dashboard/


---

## 2026-08-31 · Post · We launched as a trusted auditor for Signal's Automatic Key Verification, watched GPT 5.6-Cyber chai


Tags (automatic): AI-assisted hunting


### Post — @trailofbits — 2026-08-31 11:00 UTC (2026-08-31 12:00 WAT)

- URL: https://x.com/trailofbits/status/2094379675032105043
- Metrics (at fetch): bookmark 44, impression 12653, like 113, quote 3, reply 10, retweet 11

> We launched as a trusted auditor for Signal's Automatic Key Verification, watched GPT 5.6-Cyber chain three 0-days into a VM escape, and found a Provenance bug representing ~$500K in drainable HASH. Plus 8 new public reviews, 2 open-source tools, and more.
>
> August Tribune: https://mailchi.mp/trailofbits/august-2026-tribune

**Media:**
- photo: https://pbs.twimg.com/media/HQ1Dz2lboAA1SIN.png — no alt text provided by author

**Links in post:** https://mailchi.mp/trailofbits/august-2026-tribune


---

## 2026-08-27 · Post · We signed the call for collective action. Across 3 months, we audited 50 open-source projects using 


### Post — @trailofbits — 2026-08-27 23:04 UTC (2026-08-28 00:04 WAT)

- URL: https://x.com/trailofbits/status/2093112327239553140
- Metrics (at fetch): bookmark 30, impression 13029, like 107, quote 3, reply 13, retweet 8

> We signed the call for collective action. Across 3 months, we audited 50 open-source projects using frontier cyber models. To date, we've found 1,268 potential issues and wrote 298 patches. 
>
> Critical infrastructure around the world carries the same technical debt, but has far fewer defenders. It will take the entire industry working together to fix it.

**Links in post:** https://twitter.com/gdb/status/2093021551855812842

**Quoted post (full text):**

    #### Quoted post — @162124540 — 2026-08-27 17:03 UTC (2026-08-27 18:03 WAT)
    
    - URL: https://x.com/162124540/status/2093021551855812842
    - Metrics (at fetch): bookmark 2036, impression 1426470, like 3953, quote 381, reply 410, retweet 686
    
    > An open letter for a global surge in cyber defense, signed by over 100 organizations including Anthropic, AWS, Google, Microsoft, OpenAI, and Oracle. https://x.com/i/article/2093011711712456704
    >
    > [X Article — A call for collective action on cyber defense — full text follows]
    >
    > An open letter for a global surge in cyber defense, signed by over 100 organizations including Anthropic, AWS, Google, Microsoft, OpenAI, and Oracle.
    > We have a limited window to strengthen cyber defenses.
    > In the coming months, AI-enabled cyber attacks will become far more widespread and sophisticated as models around the world become increasingly capable. The companies and public services our communities depend on — from hospitals to water treatment plants to the infrastructure that powers the internet — are at risk.
    > Today’s AI advances are already giving defenders new ways to fix weaknesses that have accumulated for years. If we act decisively, we can use the defenders’ window to make our digital world much more secure.
    > We propose the following principles for a collective response:
    > Recognize that status quo security won’t be enough. Longstanding bugs, excessive permissions, misconfigurations, insecure and unpatched software, weak authentication, and technical debt in legacy systems have left systems exposed. Security teams, particularly for critical infrastructure, have been historically under-resourced and need a surge in tools and resources.
    > Empower more defenders with cyber-capable AI. AI brings specialist skills to more defenders and makes core security tasks faster, cheaper and better. Sharing tools, practical knowledge, and verified fixes lets one organization’s work help protect many others.
    > Mobilize a collective response. Cyber capabilities are advancing worldwide, and that can be a net positive: no single company should control the future. It also means a global response is necessary, requiring new partnerships to raise security standards and find new solutions to emerging cyber threats.
    > Each of us can reduce risk now. All organizations, cybersecurity companies, technology partners, governments, and AI frontier companies have an important role: accelerate defenders’ priorities with tools, funding, and hands-on support, especially for critical infrastructure organizations with limited budgets.
    > Here’s what we think needs to happen next:
    > 01 Every organization
    > Make cyber defense an immediate leadership priority. Raise your security standards and meet them with the urgency and coordination of an incident that takes precedence over everything except critical business operations. Fix the highest-risk weaknesses, verify results without disrupting essential services, and raise the security bar for what you buy, build, and deploy, including AI-generated code. Upgrade or replace systems to build in least privilege, strong access controls, and defense in depth. Use capable, lower-cost models for broad coverage, and apply frontier capabilities to the hardest problems. Where a system cannot be patched without disrupting essential services, apply and verify compensating controls.
    > 02 Cybersecurity companies and technology partners
    > Help lead the response to defend against sustained AI-enabled attacks, including testing defenses continuously against frontier cyber capabilities, strengthening existing tools with AI, and working with technology partners to close gaps now. Make AI-powered defense accessible and deployable for critical-infrastructure operators, with hands-on help to deploy tools and verify fixes, and collaborate with critical infrastructure supply chain manufacturers and system integrators to patch and issue interim guidance. Share threat intelligence and tested playbooks, and measure progress by how many organizations are protected, how quickly attacks are contained, and whether fixes work.
    > 03 Governments
    > Coordinate cyber defense at local, national, and international levels. Strengthen existing government and industry channels to share actionable threat intelligence, prioritize the most serious risks, and coordinate incident response and recovery around the world. Fund cyber defense, starting with essential services that lack the staff or budget to act. Expedite the expansion of trusted access programs, especially for critical infrastructure supply chains, and broaden access to defensive capabilities for other defenders. Give hospitals, water utilities, and local governments access to capable defensive AI, authorized testing, and hands-on support through trusted security providers and partners. Impose costs on attackers.
    > 04 Frontier AI companies
    > Provide responsible model access, significant funding, training, and hands-on support, especially for under-resourced critical-infrastructure defenders. Build observability and security tools, ensure agentic identities are traceable and accountable, and share best practices in continuous monitoring. Invest in authorized testing, private disclosure, and verified fixes, and share tools, playbooks, and credible threat assessments with governments, security partners, and open-source maintainers to strengthen preparedness, response, and recovery.
    >  
    > We can make the digital infrastructure we all depend on more secure.
    > We call on leaders across industry and government to bring the full weight of their technology, resources, and expertise to this effort. Put cyber-capable AI in the hands of defenders, starting with the teams protecting essential services. Fix the most dangerous weaknesses, verify the fixes, and share what works so others can build on it. Together, we can turn today’s AI advances into lasting improvements in security that benefit everyone. Let’s put them to work.
    > https://openai.com/collective-cyberdefense
    >
    > [Links in article: https://openai.com/collective-cyberdefense]
    
    **Links in post:** https://x.com/i/article/2093011711712456704
    


---

## 2026-08-26 · Post · We asked GPT 5.6-Cyber to escape a VM used to sandbox agents. It broke out three times.


Tags (automatic): AI-assisted hunting


### Post — @trailofbits — 2026-08-26 11:15 UTC (2026-08-26 12:15 WAT)

- URL: https://x.com/trailofbits/status/2092571523450114277
- Metrics (at fetch): bookmark 983, impression 499585, like 1698, quote 100, reply 69, retweet 332

> We asked GPT 5.6-Cyber to escape a VM used to sandbox agents. It broke out three times.
>
> In its final escape, the agent found three 0-days on its own and chained them into a working exploit. https://blog.trailofbits.com/2026/08/26/vms-wont-contain-cyber-capable-agents/

**Links in post:** https://blog.trailofbits.com/2026/08/26/vms-wont-contain-cyber-capable-agents/


---

## 2026-08-25 · Post · We found a bug that lets any user grant themselves admin access to live financial assets on Provenan


Tags (automatic): Blockchain / L1-L2 / bridge


### Post — @trailofbits — 2026-08-25 11:15 UTC (2026-08-25 12:15 WAT)

- URL: https://x.com/trailofbits/status/2092209135651557648
- Metrics (at fetch): bookmark 64, impression 16917, like 145, quote 4, reply 2, retweet 10

> We found a bug that lets any user grant themselves admin access to live financial assets on Provenance, a Cosmos SDK chain.
>
> 82 token accounts were exploitable, representing ~$500K in drainable HASH. Now patched. https://blog.trailofbits.com/2026/08/25/state-divergence-enables-unauthorized-access/

**Links in post:** https://blog.trailofbits.com/2026/08/25/state-divergence-enables-unauthorized-access/


---

## 2026-08-14 · Post · PATCH THE PLANET BUG SPOTLIGHT: We found a medium-severity bug in aiohttp, Python's HTTP engine that


### Post — @trailofbits — 2026-08-14 11:02 UTC (2026-08-14 12:02 WAT)

- URL: https://x.com/trailofbits/status/2088219615373504980
- Metrics (at fetch): bookmark 12, impression 5197, like 37, quote 1, reply 3, retweet 7

> PATCH THE PLANET BUG SPOTLIGHT: We found a medium-severity bug in aiohttp, Python's HTTP engine that had 600M+ downloads last month. Denys Pakizh caught oversized requests dodging its size limits. Now patched. CVE-2026-54277 in the dashboard: https://trailofbits.com/patch-the-planet/dashboard

**Links in post:** https://trailofbits.com/patch-the-planet/dashboard


---

## 2026-08-11 · Post · We're a day-one auditor for @signalapp's new Automatic Key Verification, which depends on external a


### Post — @trailofbits — 2026-08-11 17:40 UTC (2026-08-11 18:40 WAT)

- URL: https://x.com/trailofbits/status/2087232590017155289
- Metrics (at fetch): bookmark 20, impression 11127, like 115, quote 2, reply 2, retweet 22

> We're a day-one auditor for @signalapp's new Automatic Key Verification, which depends on external auditors to confirm everyone sees the same keys. 
>
> We built our auditing software from scratch, open-sourced it, and run it as a public good. https://t.co/CrHsFQiLGk


---

## 2026-08-11 · Post · See you next year. https://t.co/hskWrTmFEF


### Post — @trailofbits — 2026-08-11 11:02 UTC (2026-08-11 12:02 WAT)

- URL: https://x.com/trailofbits/status/2087132447494344848
- Metrics (at fetch): bookmark 2, impression 2829, like 38, quote 0, reply 1, retweet 3

> See you next year. https://t.co/hskWrTmFEF

**Media:**
- photo: https://pbs.twimg.com/media/HPb74pjWMAAi9DI.jpg — no alt text provided by author
- photo: https://pbs.twimg.com/media/HPb75G7W8AA_Xy8.jpg — no alt text provided by author
- photo: https://pbs.twimg.com/media/HPb74kPXQAAYjgZ.jpg — no alt text provided by author
- photo: https://pbs.twimg.com/media/HPb74qGXAAAbf0Y.jpg — no alt text provided by author


---

## 2026-08-07 · Post · "Until I came across Dan’s talk, we didn’t have a structured process."


Tags (automatic): AI-assisted hunting


### Post — @trailofbits — 2026-08-07 14:00 UTC (2026-08-07 15:00 WAT)

- URL: https://x.com/trailofbits/status/2085727817371676678
- Metrics (at fetch): bookmark 11, impression 3367, like 27, quote 0, reply 1, retweet 2

> "Until I came across Dan’s talk, we didn’t have a structured process."
>
> @timoreilly invited our CEO @dguido to explain what it takes to make a company AI-native. https://t.co/pLgRVYeeYR


---

## 2026-08-07 · Reply · @WorkOS built an internal AI pipeline that hunts for deep logic bugs, ran 1,000+ scans with it, and 


Tags (automatic): AI-assisted hunting


### Post — @trailofbits — 2026-08-07 11:02 UTC (2026-08-07 12:02 WAT)

- URL: https://x.com/trailofbits/status/2085682872812179658
- Metrics (at fetch): bookmark 108, impression 8477, like 127, quote 2, reply 4, retweet 15

> @WorkOS built an internal AI pipeline that hunts for deep logic bugs, ran 1,000+ scans with it, and surfaced multiple high-severity issues. They used our public code auditing skills as a foundation. https://t.co/5hJqS9WoFz


---

## 2026-08-06 · Post · remill spotted in the wild https://t.co/DPhnUCwPv5


### Post — @trailofbits — 2026-08-06 00:25 UTC (2026-08-06 01:25 WAT)

- URL: https://x.com/trailofbits/status/2085160343442166237
- Metrics (at fetch): bookmark 10, impression 8752, like 58, quote 0, reply 1, retweet 1

> remill spotted in the wild https://t.co/DPhnUCwPv5

**Quoted post (full text):**

    #### Quoted post — @1114558827133898757 — 2026-08-05 01:35 UTC (2026-08-05 02:35 WAT)
    
    - URL: https://x.com/1114558827133898757/status/2084815605710893459
    - Metrics (at fetch): bookmark 105, impression 25193, like 301, quote 2, reply 8, retweet 36
    
    > Finally got around to getting a working PoC of my native object file to LLVM IR lifter. 
    >
    > Started this small side-project to see how far can I push my own VM tech and perhaps transpiling existing tradecrafts, executables and post-ex toolings by simply lifting them up to LLVM IR https://t.co/CRW41sgnHw
    
    **Media:**
    - media `3_2084806595788091392` (details not returned by the API)
    - media `3_2084806615996203008` (details not returned by the API)
    


---

## 2026-08-05 · Post · A malicious host can attack your AWS Nitro Enclave through its connection to KMS. If your enclave ta


Tags (automatic): TEE / enclave


### Post — @trailofbits — 2026-08-05 11:15 UTC (2026-08-05 12:15 WAT)

- URL: https://x.com/trailofbits/status/2084961381233606753
- Metrics (at fetch): bookmark 11, impression 2919, like 37, quote 0, reply 0, retweet 4

> A malicious host can attack your AWS Nitro Enclave through its connection to KMS. If your enclave talks with KMS, read this before you ship. https://blog.trailofbits.com/2026/08/05/a-few-notes-on-aws-nitro-enclaves-kms-integration/

**Links in post:** https://blog.trailofbits.com/2026/08/05/a-few-notes-on-aws-nitro-enclaves-kms-integration/


---

## 2026-08-04 · Post · 1,137 potential bugs found, 866 awaiting patches, 125 fixes open upstream, 146 merged.


Tags (automatic): AI-assisted hunting


### Post — @trailofbits — 2026-08-04 11:05 UTC (2026-08-04 12:05 WAT)

- URL: https://x.com/trailofbits/status/2084596569211330767
- Metrics (at fetch): bookmark 30, impression 5933, like 78, quote 2, reply 3, retweet 11

> 1,137 potential bugs found, 866 awaiting patches, 125 fixes open upstream, 146 merged.
>
> Since July 20: +279 bugs, 5 new projects, and vllm is now the most-reported codebase in Patch the Planet. https://t.co/dDV7RUbxgQ


---

## 2026-07-31 · Thread · PATCH THE PLANET BUG SPOTLIGHT: We found a high-severity use-after-free bug in nginx, the web server


Tags (automatic): Memory corruption / native, AI-assisted hunting


### Post — @trailofbits — 2026-07-31 14:01 UTC (2026-07-31 15:01 WAT)

- URL: https://x.com/trailofbits/status/2083191391358702029
- Metrics (at fetch): bookmark 15, impression 7549, like 78, quote 0, reply 2, retweet 3

> PATCH THE PLANET BUG SPOTLIGHT: We found a high-severity use-after-free bug in nginx, the web server handling over 30% of all websites in the world. Now patched.


### Thread part 2 — @trailofbits — 2026-07-31 14:01 UTC (2026-07-31 15:01 WAT)

- URL: https://x.com/trailofbits/status/2083191392390570059
- Metrics (at fetch): bookmark 4, impression 1659, like 10, quote 2, reply 0, retweet 3

> Remote and unauthenticated, it can crash nginx and potentially run code, all through HTTP/3. Engineer Evan Hellman found it with Codex after roughly 14 hours of automated analysis. CVE-2026-42530 in the dashboard: https://trailofbits.com/patch-the-planet/dashboard/

**Links in post:** https://trailofbits.com/patch-the-planet/dashboard/


---

## 2026-07-31 · Post · We've hijacked multi-agent systems, exfiltrated Gmail data through Perplexity's Comet browser, hidde


Tags (automatic): AI-assisted hunting


### Post — @trailofbits — 2026-07-31 11:00 UTC (2026-07-31 12:00 WAT)

- URL: https://x.com/trailofbits/status/2083145852873261430
- Metrics (at fetch): bookmark 112, impression 14466, like 227, quote 1, reply 5, retweet 34

> We've hijacked multi-agent systems, exfiltrated Gmail data through Perplexity's Comet browser, hidden prompt injection inside images, and won $3M at DARPA's AIxCC for AI that finds and patches vulnerabilities. All documented on our blog. https://t.co/0Fm9DJvYfq


---

## 2026-07-30 · Post · We shipped post-quantum crypto to Python, watched GPT-5.5-Cyber build a zlib fuzzing lab in a day, a


Tags (automatic): AI-assisted hunting


### Post — @trailofbits — 2026-07-30 14:01 UTC (2026-07-30 15:01 WAT)

- URL: https://x.com/trailofbits/status/2082828874287595592
- Metrics (at fetch): bookmark 34, impression 6664, like 70, quote 2, reply 2, retweet 9

> We shipped post-quantum crypto to Python, watched GPT-5.5-Cyber build a zlib fuzzing lab in a day, and shared our /goal playbook for finding real bugs. Plus 9 new public reviews, mutation testing for DAML, and more. July Tribune: https://t.co/ow6ogCfdI0


---

## 2026-07-30 · Post · Hooks in @Uniswap v4 move real security decisions into app code: who can call the hook, which pools 


### Post — @trailofbits — 2026-07-30 11:15 UTC (2026-07-30 12:15 WAT)

- URL: https://x.com/trailofbits/status/2082787068522991721
- Metrics (at fetch): bookmark 63, impression 8728, like 67, quote 3, reply 0, retweet 12

> Hooks in @Uniswap v4 move real security decisions into app code: who can call the hook, which pools to trust, how to account for value.
>
> @nisedo analyzed dozens of audit findings, found seven ways that code breaks, and turned them into a builder checklist.


---

## 2026-07-28 · Post · 858 potential bugs found, 595 awaiting patches, 120 fixes open upstream, 143 merged.


### Post — @trailofbits — 2026-07-28 16:37 UTC (2026-07-28 17:37 WAT)

- URL: https://x.com/trailofbits/status/2082143542047064105
- Metrics (at fetch): bookmark 23, impression 9166, like 95, quote 3, reply 5, retweet 15

> 858 potential bugs found, 595 awaiting patches, 120 fixes open upstream, 143 merged.
>
> Our new Patch the Planet dashboard breaks down the latest results from our audits of curl, OpenSSL, Kubernetes, and 38 other open-source projects.
> https://t.co/iJxPqKLL7M


---

## 2026-07-28 · Thread · Rust maintainers assumed a team of engineers was behind our bug reports. It was one engineer using C


### Post — @trailofbits — 2026-07-28 11:15 UTC (2026-07-28 12:15 WAT)

- URL: https://x.com/trailofbits/status/2082062278229188646
- Metrics (at fetch): bookmark 83, impression 42458, like 389, quote 4, reply 7, retweet 10

> Rust maintainers assumed a team of engineers was behind our bug reports. It was one engineer using Codex's /goal.


### Thread part 2 — @trailofbits — 2026-07-28 11:15 UTC (2026-07-28 12:15 WAT)

- URL: https://x.com/trailofbits/status/2082062279420342319
- Metrics (at fetch): bookmark 122, impression 8384, like 124, quote 4, reply 1, retweet 14

> Over the first few weeks of Patch the Planet, our engineers independently converged on three techniques that get the most out of /goal’s ability to find real bugs. We wrote them down into a field report, with prompts included. https://t.co/YlUZqmZdBF


---

## 2026-07-21 · Post · We audited ExecuTorch, the engine that runs @PyTorch AI models on-device for billions of people acro


Tags (automatic): AI-assisted hunting


### Post — @trailofbits — 2026-07-21 11:02 UTC (2026-07-21 12:02 WAT)

- URL: https://x.com/trailofbits/status/2079522279835283936
- Metrics (at fetch): bookmark 20, impression 3851, like 45, quote 0, reply 5, retweet 11

> We audited ExecuTorch, the engine that runs @PyTorch AI models on-device for billions of people across Instagram, WhatsApp, and Messenger.
>
> In one month, we reported 42 issues. 26 came from AI-assisted workflows.


---

## 2026-07-20 · Post · Snow secures encrypted connections between machines for Ethereum clients, Polkadot, and 80+ Rust pro


### Post — @trailofbits — 2026-07-20 11:02 UTC (2026-07-20 12:02 WAT)

- URL: https://x.com/trailofbits/status/2079159889054605381
- Metrics (at fetch): bookmark 4, impression 2757, like 19, quote 1, reply 1, retweet 5

> Snow secures encrypted connections between machines for Ethereum clients, Polkadot, and 80+ Rust projects.
>
> We found 10 issues and validated 8 fixes that protect against forged packets, malformed PSK indices, and oversized messages. Funded by @1Password.
> https://t.co/28JmccBZ5x


---

## 2026-07-14 · Post · "The oldest principles in security—auditing, logging, isolation, least privilege—matter more than ev


### Post — @trailofbits — 2026-07-14 11:02 UTC (2026-07-14 12:02 WAT)

- URL: https://x.com/trailofbits/status/2076985561001136220
- Metrics (at fetch): bookmark 12, impression 3593, like 28, quote 1, reply 3, retweet 5

> "The oldest principles in security—auditing, logging, isolation, least privilege—matter more than ever now that actions happen at machine speed, not human speed."—Artem Dinaburg, our chief scientist, on Silver Bullet ep 158. https://t.co/HFPnZAedPT


---

## 2026-07-13 · Post · What we’ve learned about testing Rust for security, now available as a Testing Handbook chapter. We 


### Post — @trailofbits — 2026-07-13 11:15 UTC (2026-07-13 12:15 WAT)

- URL: https://x.com/trailofbits/status/2076626471410434541
- Metrics (at fetch): bookmark 61, impression 9286, like 97, quote 1, reply 6, retweet 22

> What we’ve learned about testing Rust for security, now available as a Testing Handbook chapter. We also released rust-review, a plugin for automated Rust security reviews, co-built with @AptosLabs.
> https://t.co/bGtE97yhyh


---

## 2026-07-10 · Post · Later today at @SummerC0n, Asritha Bodepudi will show how to build a Windows n-day exploit chain for


Tags (automatic): Memory corruption / native


### Post — @trailofbits — 2026-07-10 11:15 UTC (2026-07-10 12:15 WAT)

- URL: https://x.com/trailofbits/status/2075539295272632492
- Metrics (at fetch): bookmark 3, impression 2990, like 12, quote 0, reply 0, retweet 3

> Later today at @SummerC0n, Asritha Bodepudi will show how to build a Windows n-day exploit chain for RasMan, the Remote Access Connection Manager service.
>
> 11:15AM ET, Main Stage, Littlefield in Brooklyn. https://www.summercon.org/schedule/

**Links in post:** https://www.summercon.org/schedule/


---

## 2026-07-08 · Thread · Mewt grades your test suite by sabotaging your code. Each change that doesn't get flagged by your te


### Post — @trailofbits — 2026-07-08 11:15 UTC (2026-07-08 12:15 WAT)

- URL: https://x.com/trailofbits/status/2074814523257532555
- Metrics (at fetch): bookmark 9, impression 3559, like 24, quote 0, reply 1, retweet 6

> Mewt grades your test suite by sabotaging your code. Each change that doesn't get flagged by your tests is a potential bug. 
>
> Today we're expanding it to support DAML, @CantonNetwork's native language, with two new mutant classes for DAML's authorization rules.


### Thread part 2 — @trailofbits — 2026-07-08 11:15 UTC (2026-07-08 12:15 WAT)

- URL: https://x.com/trailofbits/status/2074814524297814206
- Metrics (at fetch): bookmark 2, impression 1243, like 2, quote 0, reply 0, retweet 1

> @CantonNetwork We tried Mewt on OpenZeppelin's canton-stablecoin reference implementation. 
>
> All tests were green and coverage was 100%, but four surviving mutants exposed missing test cases. https://t.co/8vSg17n4CF


---

## 2026-07-02 · Post · We gave GPT-5.5-Cyber a single /goal: find a specific class of bugs in zlib, the compression library


Tags (automatic): Mobile / Android / iOS, AI-assisted hunting


### Post — @trailofbits — 2026-07-02 11:15 UTC (2026-07-02 12:15 WAT)

- URL: https://x.com/trailofbits/status/2072640196944781594
- Metrics (at fetch): bookmark 158, impression 21580, like 263, quote 4, reply 7, retweet 47

> We gave GPT-5.5-Cyber a single /goal: find a specific class of bugs in zlib, the compression library used by Linux, macOS, iOS, and Git.
>
> It built a fuzzing lab in less than a day, a task that takes a skilled researcher weeks.
>
> Patch the Planet field report by Benjamin Samuels:


---

## 2026-07-01 · Post · cargo-audit flags Rust dependencies with known vulnerabilities, but it doesn't tell you whether your


### Post — @trailofbits — 2026-07-01 11:01 UTC (2026-07-01 12:01 WAT)

- URL: https://x.com/trailofbits/status/2072274373784879437
- Metrics (at fetch): bookmark 34, impression 7848, like 111, quote 3, reply 4, retweet 21

> cargo-audit flags Rust dependencies with known vulnerabilities, but it doesn't tell you whether your code calls the vulnerable function.
>
> We added a feature that checks your binary for vulnerable functions and labels any matches as "Affected," separating real exposure from https://t.co/VdtFpht3fl

**Media:**
- photo: https://pbs.twimg.com/media/HMIyj5jWkAEiIrC.jpg — no alt text provided by author


---

## 2026-06-30 · Post · .@OpenAI handed us their most cyber-capable models and asked us to work directly with open-source ma


### Post — @trailofbits — 2026-06-30 14:00 UTC (2026-06-30 15:00 WAT)

- URL: https://x.com/trailofbits/status/2071957019301392838
- Metrics (at fetch): bookmark 30, impression 5633, like 100, quote 0, reply 5, retweet 15

> .@OpenAI handed us their most cyber-capable models and asked us to work directly with open-source maintainers to Patch the Planet.
>
> We started with 19 projects: cURL, Python, Sigstore, NATS, and more. 50 projects have now joined the initiative. https://t.co/9X0pO8EtCt


---

## 2026-06-30 · Thread · 1.2 billion downloads ran through pyca/cryptography last month. Nearly every Python app that touches


### Post — @trailofbits — 2026-06-30 11:15 UTC (2026-06-30 12:15 WAT)

- URL: https://x.com/trailofbits/status/2071915420584411634
- Metrics (at fetch): bookmark 13, impression 6495, like 46, quote 0, reply 2, retweet 4

> 1.2 billion downloads ran through pyca/cryptography last month. Nearly every Python app that touches crypto depends on it. If it doesn't ship post-quantum primitives, the Python ecosystem can't migrate. 🧵


### Thread part 2 — @trailofbits — 2026-06-30 11:15 UTC (2026-06-30 12:15 WAT)

- URL: https://x.com/trailofbits/status/2071915421544960263
- Metrics (at fetch): bookmark 3, impression 1391, like 17, quote 1, reply 1, retweet 3

> We helped add ML-DSA and ML-KEM, NIST's post-quantum standards for signatures and key exchange, to the library. Install and migration details in the blog. https://blog.trailofbits.com/2026/06/30/shipping-post-quantum-cryptography-to-python/

**Links in post:** https://blog.trailofbits.com/2026/06/30/shipping-post-quantum-cryptography-to-python/


---

## 2026-06-26 · Post · We redesigned http://trailofbits.com. Everything we publish is now in one place.


### Post — @trailofbits — 2026-06-26 11:02 UTC (2026-06-26 12:02 WAT)

- URL: https://x.com/trailofbits/status/2070462582931046681
- Metrics (at fetch): bookmark 29, impression 5802, like 77, quote 0, reply 3, retweet 5

> We redesigned http://trailofbits.com. Everything we publish is now in one place.

**Links in post:** http://trailofbits.com


---

## 2026-06-25 · Post · We're a sponsor of @Stanford's Real World AI Security conference, where Sam Judson will present late


Tags (automatic): AI-assisted hunting


### Post — @trailofbits — 2026-06-25 11:02 UTC (2026-06-25 12:02 WAT)

- URL: https://x.com/trailofbits/status/2070100194960556116
- Metrics (at fetch): bookmark 12, impression 4236, like 50, quote 0, reply 2, retweet 1

> We're a sponsor of @Stanford's Real World AI Security conference, where Sam Judson will present later today on why AI skill scanners fail. https://seclab.stanford.edu/RealWorldAIsec/

**Links in post:** https://seclab.stanford.edu/RealWorldAIsec/


---

## 2026-06-24 · Post · We launched Patch the Planet with OpenAI, factored hundreds of weak RSA keys with a new polynomial t


Tags (automatic): AI-assisted hunting


### Post — @trailofbits — 2026-06-24 11:15 UTC (2026-06-24 12:15 WAT)

- URL: https://x.com/trailofbits/status/2069741108666536271
- Metrics (at fetch): bookmark 31, impression 8691, like 83, quote 0, reply 1, retweet 15

> We launched Patch the Planet with OpenAI, factored hundreds of weak RSA keys with a new polynomial technique, and bypassed every AI skill scanner we tested. Plus 10 new public reviews, gosentry, and more. June Tribune: https://mailchi.mp/trailofbits/june-2026-tribune

**Links in post:** https://mailchi.mp/trailofbits/june-2026-tribune


---

## 2026-06-22 · Post · Patch the Planet is our joint initiative with @OpenAI to help maintainers strengthen critical open-s


Tags (automatic): AI-assisted hunting


### Post — @trailofbits — 2026-06-22 17:08 UTC (2026-06-22 18:08 WAT)

- URL: https://x.com/trailofbits/status/2069105257389666760
- Metrics (at fetch): bookmark 37, impression 42898, like 191, quote 8, reply 4, retweet 35

> Patch the Planet is our joint initiative with @OpenAI to help maintainers strengthen critical open-source software.
>
> In one week, we used Codex and GPT-5.5-Cyber to find hundreds of bugs inside OSS like cURL, Python, and the Go project. 37 patches merged, with more in flight. 🧵 https://twitter.com/OpenAI/status/2069104288417390688

**Links in post:** https://twitter.com/OpenAI/status/2069104288417390688

**Quoted post (full text):**

    #### Quoted post — @OpenAI — 2026-06-22 17:04 UTC (2026-06-22 18:04 WAT)
    
    - URL: https://x.com/OpenAI/status/2069104288417390688
    - Metrics (at fetch): bookmark 159, impression 414477, like 864, quote 33, reply 39, retweet 59
    
    > Patch the Planet is our effort to help open source maintainers move from security findings to merged fixes.
    >
    > We’re working with Trail of Bits, HackerOne, Calif, researchers, and maintainers to bring Codex Security and advanced models into the remediation process, with human review at the center.
    
    **Media:**
    - media `13_2069102965512916992` (details not returned by the API)
    


---

## 2026-06-15 · Post · A Mythos audit of Symfony found 19 vulnerabilities. One of our engineers pointed our internal skills


### Post — @trailofbits — 2026-06-15 19:42 UTC (2026-06-15 20:42 WAT)

- URL: https://x.com/trailofbits/status/2066607280699953219
- Metrics (at fetch): bookmark 103, impression 35030, like 147, quote 0, reply 6, retweet 13

> A Mythos audit of Symfony found 19 vulnerabilities. One of our engineers pointed our internal skills at the same code. https://twitter.com/ToBScottA/status/2065468153669312520

**Links in post:** https://twitter.com/ToBScottA/status/2065468153669312520

**Quoted post (full text):**

    #### Quoted post — @2036163170717618176 — 2026-06-12 16:15 UTC (2026-06-12 17:15 WAT)
    
    - URL: https://x.com/2036163170717618176/status/2065468153669312520
    - Metrics (at fetch): bookmark 32, impression 43652, like 28, quote 2, reply 2, retweet 4
    
    > Last month, the @Symfony blog posted about some results from Claude Mythos.
    >
    > https://symfony.com/blog/claude-mythos-audited-symfony-and-found-19-vulnerabilities
    
    **Links in post:** https://symfony.com/blog/claude-mythos-audited-symfony-and-found-19-vulnerabilities
    


---

## 2026-06-12 · Post · RSA private keys biased toward 0 bits can be factored by swapping a hard math problem for an easy on


### Post — @trailofbits — 2026-06-12 11:15 UTC (2026-06-12 12:15 WAT)

- URL: https://x.com/trailofbits/status/2065392441566400615
- Metrics (at fetch): bookmark 402, impression 52271, like 796, quote 7, reply 9, retweet 160

> RSA private keys biased toward 0 bits can be factored by swapping a hard math problem for an easy one: integer factorization becomes polynomial factorization.
>
> We found hundreds of real-world keys vulnerable to this. Many traced to a type mismatch in CompleteFTP (now patched): each 32-bit limb got only 8 bits of randomness. We recovered 603 RSA and 74 DSA private keys. https://blog.trailofbits.com/2026/06/12/factoring-short-sleeve-rsa-keys-with-polynomials/

**Links in post:** https://blog.trailofbits.com/2026/06/12/factoring-short-sleeve-rsa-keys-with-polynomials/


---

## 2026-06-05 · Thread · We beat Google's quantum circuit again, and we didn't have to forge a proof this time. 


Tags (automatic): ZK


### Post — @trailofbits — 2026-06-05 19:30 UTC (2026-06-05 20:30 WAT)

- URL: https://x.com/trailofbits/status/2062980523232805164
- Metrics (at fetch): bookmark 32, impression 22276, like 115, quote 6, reply 17, retweet 23

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

## 2026-06-04 · Post · SEAL Certifications check the operational side of security, from multisigs and treasury to DNS, cred


### Post — @trailofbits — 2026-06-04 11:02 UTC (2026-06-04 12:02 WAT)

- URL: https://x.com/trailofbits/status/2062490046050017770
- Metrics (at fetch): bookmark 15, impression 8304, like 30, quote 0, reply 1, retweet 2

> SEAL Certifications check the operational side of security, from multisigs and treasury to DNS, credentials, and incident response. If you want to get certified, contact us. https://twitter.com/1756434947202748416/status/2061818470472237429

**Links in post:** https://twitter.com/1756434947202748416/status/2061818470472237429

**Quoted post (full text):**

    #### Quoted post — @1756434947202748416 — 2026-06-02 14:33 UTC (2026-06-02 15:33 WAT)
    
    - URL: https://x.com/1756434947202748416/status/2061818470472237429
    - Metrics (at fetch): bookmark 19, impression 31264, like 144, quote 22, reply 17, retweet 28
    
    > It's finally happening! 
    >
    > SEAL Certifications are now open for business. 🎉 [pic.x.com/FgEl50JkAS]
    
    **Media:**
    - media `3_2061816731564142592` (details not returned by the API)
    


---

## 2026-06-03 · Post · We built four malicious skills to test whether skill scanners actually work. Three took less than an


### Post — @trailofbits — 2026-06-03 11:15 UTC (2026-06-03 12:15 WAT)

- URL: https://x.com/trailofbits/status/2062130946434834817
- Metrics (at fetch): bookmark 209, impression 32290, like 279, quote 5, reply 9, retweet 63

> We built four malicious skills to test whether skill scanners actually work. Three took less than an hour to conceive and implement. ClawHub, Cisco, and Vercel's http://skills.sh marked them as safe. 🧵

**Links in post:** http://skills.sh


---

## 2026-05-22 · Post · A CI/CD compromise like Trivy → LiteLLM can multiply across the software supply chain. We hardened z


Tags (automatic): Dependency confusion / supply chain, AI-assisted hunting


### Post — @trailofbits — 2026-05-22 11:15 UTC (2026-05-22 12:15 WAT)

- URL: https://x.com/trailofbits/status/2057782296527208709
- Metrics (at fetch): bookmark 39, impression 7148, like 62, quote 1, reply 4, retweet 12

> A CI/CD compromise like Trivy → LiteLLM can multiply across the software supply chain. We hardened zizmor, the static analyzer for GitHub Actions, so it reliably catches more workflow misconfigs. 🧵


---

## 2026-05-19 · Post · .@obsdmd asked us to audit their Sync protocol. Our engineers delivered eleven findings. 


### Post — @trailofbits — 2026-05-19 15:08 UTC (2026-05-19 16:08 WAT)

- URL: https://x.com/trailofbits/status/2056753768432316567
- Metrics (at fetch): bookmark 62, impression 16926, like 105, quote 1, reply 4, retweet 14

> .@obsdmd asked us to audit their Sync protocol. Our engineers delivered eleven findings. 
>
> Five went above and beyond the original scope and found system-level issues that weren't specific to Sync itself.                                                                            
>
> We see this pattern often with our clients. We respect scope as a delivery contract, but we have a professional obligation to surface what our engineers see.  
>
> Anything they catch is flagged, and the client decides what to do. When a finding warrants it, the report includes an Exploit Scenario, the path from observation to working exploit. We take an attacker's mindset, and exploit scenarios show our clients what a bug costs them. 
>
> With security-first teams like Obsidian, that meant five system-level findings that were either patched or explicitly acknowledged:
>
> 1. Math.random used for password and salt generation (High severity, medium difficulty)
>
> 2. Variable-time comparison of password-reset tokens and MFA recovery codes (High severity, high difficulty)
>
> 3. TOTP codes replayable within the validity window (High severity, high difficulty)
>
> 4. Plaintext storage of MFA secrets and recovery codes (High severity, medium difficulty)
>
> 5. Password reset without MFA (Medium severity, medium difficulty)

**Links in post:** https://twitter.com/obsdmd/status/2054606618818711862

**Quoted post (full text):**

    #### Quoted post — @1239876481951596545 — 2026-05-13 16:56 UTC (2026-05-13 17:56 WAT)
    
    - URL: https://x.com/1239876481951596545/status/2054606618818711862
    - Metrics (at fetch): bookmark 126, impression 69075, like 473, quote 2, reply 4, retweet 40
    
    > Two new security audits of Obsidian Sync by @cure53berlin and @trailofbits are now available on our Security page.
    >
    > All findings have been addressed via remediations and disclosures validated by the respective auditors. Read more:
    > https://obsidian.md/blog/cure53-tob-sync-audits/
    
    **Links in post:** https://obsidian.md/blog/cure53-tob-sync-audits/
    


---

## 2026-05-13 · Post · We were one of four initial grant recipients in @OpenAI's Trusted Access for Cyber program. 


### Post — @trailofbits — 2026-05-13 14:43 UTC (2026-05-13 15:43 WAT)

- URL: https://x.com/trailofbits/status/2054573243680559165
- Metrics (at fetch): bookmark 112, impression 42777, like 201, quote 6, reply 7, retweet 32

> We were one of four initial grant recipients in @OpenAI's Trusted Access for Cyber program. 
>
> Daybreak matters because frontier models now find bugs faster than maintainers can triage them, and that gap is about to get worse.                                                        
>
> Next-gen models can bury open-source maintainers in reports. While working with frontier labs this year, we have seen the bottleneck shift. Bug finding is easy, but triaging, disclosing, and fixing them takes disproportionate time and effort. Each finding still needs a human to confirm the bug, a static or dynamic check to reproduce it, a working proof-of-concept, and a minimal patch. That work is heavy, and right now it falls on the maintainer.  
>
> On the OSS engagements we ran this year, we prioritized minimizing maintainer workload and keeping noise out of their inboxes. Every report we sent included a PoC, a fix patch, and a regression test. Anything that did not clear that bar did not get sent.  
>
> Commonly used software has never been short of bugs. Cyber-tier models will surface them at machine speed with little human effort, and the volume will overwhelm OSS projects without clear processes for disclosure, triage, and remediation. If you maintain an OSS project, do four things:
>
> 1. Publish a SECURITY.md. If you already have one, verify the reporting flow still works end to end.
>
> 2. Set a high bar for submissions. Require a PoC, a fix patch, and a regression test wherever possible.
>
> 3. Build validation harnesses that quickly answer three questions: is the bug real, does the fix work, and does anything else break?
>
> 4. Sandbox those harnesses. Malicious reports are a credible threat once the cost of generating them drops to near zero.
>
> Bug finding is getting faster. Triage, verification, disclosure, and patching have to catch up.

**Links in post:** https://twitter.com/OpenAI/status/2053939702110269822

**Quoted post (full text):**

    #### Quoted post — @OpenAI — 2026-05-11 20:45 UTC (2026-05-11 21:45 WAT)
    
    - URL: https://x.com/OpenAI/status/2053939702110269822
    - Metrics (at fetch): bookmark 4340, impression 5590225, like 11103, quote 574, reply 611, retweet 1100
    
    > Introducing Daybreak: frontier AI for cyber defenders.
    >
    > Daybreak brings together the most capable OpenAI models, Codex, and our security partners to accelerate cyber defense and continuously secure software.
    >
    > A step toward a future where security teams can move at the speed defense demands.
    
    **Media:**
    - media `13_2053933700275167232` (details not returned by the API)
    


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

## 2026-05-11 · Post · We're sponsoring @Offensive_Con in Berlin and sending a crew. If you're there for the AI bughunting 


Tags (automatic): AI-assisted hunting


### Post — @trailofbits — 2026-05-11 09:46 UTC (2026-05-11 10:46 WAT)

- URL: https://x.com/trailofbits/status/2053773611031220454
- Metrics (at fetch): bookmark 6, impression 2620, like 23, quote 0, reply 3, retweet 2

> We're sponsoring @Offensive_Con in Berlin and sending a crew. If you're there for the AI bughunting training or the main conference, come say hi. https://www.offensivecon.org/

**Links in post:** https://www.offensivecon.org/


---

## 2026-05-08 · Post · We submitted SequenceHash to C2SP. It's a new spec for safely combining multiple inputs into a singl


### Post — @trailofbits — 2026-05-08 11:02 UTC (2026-05-08 12:02 WAT)

- URL: https://x.com/trailofbits/status/2052705578472837515
- Metrics (at fetch): bookmark 6, impression 2973, like 25, quote 0, reply 2, retweet 1

> We submitted SequenceHash to C2SP. It's a new spec for safely combining multiple inputs into a single hash with any hash function, preventing a class of subtle cryptographic bugs.


---

## 2026-05-07 · Post · We beat Google's zero-knowledge proof of quantum cryptanalysis by exploiting bugs in their Rust ZKP 


Tags (automatic): ZK


### Post — @trailofbits — 2026-05-07 14:01 UTC (2026-05-07 15:01 WAT)

- URL: https://x.com/trailofbits/status/2052388265039135123
- Metrics (at fetch): bookmark 50, impression 11774, like 102, quote 1, reply 5, retweet 18

> We beat Google's zero-knowledge proof of quantum cryptanalysis by exploiting bugs in their Rust ZKP code, then forged a proof with better metrics. Plus 11 new public reviews, Trailmark, MuTON and mewt, dimensional analysis, and more. May Tribune: https://mailchi.mp/trailofbits/may-2026-tribune

**Links in post:** https://mailchi.mp/trailofbits/may-2026-tribune


---

## 2026-05-07 · Post · mewt 3.1.0 adds Sui Move support for mutation testing. @SuiDevelopers can now mutate source code and


### Post — @trailofbits — 2026-05-07 11:02 UTC (2026-05-07 12:02 WAT)

- URL: https://x.com/trailofbits/status/2052343191718744474
- Metrics (at fetch): bookmark 3, impression 3431, like 15, quote 1, reply 1, retweet 5

> mewt 3.1.0 adds Sui Move support for mutation testing. @SuiDevelopers can now mutate source code and rerun tests. If your tests still pass, you have a coverage gap. https://github.com/trailofbits/mewt/releases/tag/v3.1.0

**Links in post:** https://github.com/trailofbits/mewt/releases/tag/v3.1.0


---

## 2026-05-05 · Post · VLC has 6B+ downloads. We spent five weeks reviewing libVLC, the C library at its core. 🧵


### Post — @trailofbits — 2026-05-05 13:56 UTC (2026-05-05 14:56 WAT)

- URL: https://x.com/trailofbits/status/2051662199706222747
- Metrics (at fetch): bookmark 79, impression 40902, like 161, quote 1, reply 4, retweet 11

> VLC has 6B+ downloads. We spent five weeks reviewing libVLC, the C library at its core. 🧵


---

## 2026-05-05 · Thread · 30 readers took our C/C++ challenge. Some solved the Linux warmup, but nobody cracked the Windows dr


### Post — @trailofbits — 2026-05-05 11:02 UTC (2026-05-05 12:02 WAT)

- URL: https://x.com/trailofbits/status/2051618417086525470
- Metrics (at fetch): bookmark 48, impression 13487, like 78, quote 0, reply 3, retweet 11

> 30 readers took our C/C++ challenge. Some solved the Linux warmup, but nobody cracked the Windows driver bug. https://x.com/trailofbits/status/2042253721581871121

**Links in post:** https://x.com/trailofbits/status/2042253721581871121

**Quoted post (full text):**

    #### Quoted post — @trailofbits — 2026-04-09 14:50 UTC (2026-04-09 15:50 WAT)
    
    - URL: https://x.com/trailofbits/status/2042253721581871121
    - Metrics (at fetch): bookmark 19, impression 15418, like 25, quote 1, reply 2, retweet 4
    
    > Spot the bugs, first 10 correct answers win swag. Full details in the blog. https://blog.trailofbits.com/2026/04/09/master-c-and-c-with-our-new-testing-handbook-chapter/
    
    **Links in post:** https://blog.trailofbits.com/2026/04/09/master-c-and-c-with-our-new-testing-handbook-chapter/
    


### Thread part 2 — @trailofbits — 2026-05-05 11:02 UTC (2026-05-05 12:02 WAT)

- URL: https://x.com/trailofbits/status/2051618417858232660
- Metrics (at fetch): bookmark 9, impression 1619, like 14, quote 1, reply 0, retweet 4

> Full walkthrough below explaining both challenges, including the Windows escalation that beat every submission.
>
> Best 10 submissions are still getting swag. If you won, we'll be in contact. https://t.co/yxF5YpJvIX


---

## 2026-04-29 · Post · “You can write exploits for software that exists in only one configuration that one company has. And


Tags (automatic): AI-assisted hunting


### Post — @trailofbits — 2026-04-29 14:00 UTC (2026-04-29 15:00 WAT)

- URL: https://x.com/trailofbits/status/2049489109048017259
- Metrics (at fetch): bookmark 50, impression 35570, like 67, quote 1, reply 3, retweet 12

> “You can write exploits for software that exists in only one configuration that one company has. And you can do it on the fly.”—@dguido in @verge on how AI collapses the cost of finding bugs. https://www.theverge.com/ai-artificial-intelligence/915660/mythos-script-kiddies-hackers-attack-cybersecurity-ai

**Links in post:** https://www.theverge.com/ai-artificial-intelligence/915660/mythos-script-kiddies-hackers-attack-cybersecurity-ai


---

## 2026-04-29 · Post · libFuzzer is in maintenance mode. We added LibAFL support to Ruzzy so Ruby devs and security researc


### Post — @trailofbits — 2026-04-29 11:02 UTC (2026-04-29 12:02 WAT)

- URL: https://x.com/trailofbits/status/2049444159916818621
- Metrics (at fetch): bookmark 9, impression 4313, like 31, quote 0, reply 2, retweet 1

> libFuzzer is in maintenance mode. We added LibAFL support to Ruzzy so Ruby devs and security researchers can run their next fuzzing campaign without harness modifications. 🧵


---

## 2026-04-28 · Post · The fastest way to get a team to adopt AI is to make them put in reps. We run hackathons as a forcin


Tags (automatic): AI-assisted hunting


### Post — @trailofbits — 2026-04-28 11:02 UTC (2026-04-28 12:02 WAT)

- URL: https://x.com/trailofbits/status/2049081767072608455
- Metrics (at fetch): bookmark 28, impression 5145, like 39, quote 1, reply 7, retweet 3

> The fastest way to get a team to adopt AI is to make them put in reps. We run hackathons as a forcing function. @dguido at unprompted [pic.x.com/UmdP1NumZG]

**Media:**
- video: https://pbs.twimg.com/ext_tw_video_thumb/2049081701142245376/pu/img/6IDtTcG5l2iZsKMg.jpg — no alt text provided by author


---

## 2026-04-23 · Post · When Claude reasons about code, it reasons about lists, but the questions that actually matter are g


Tags (automatic): AI-assisted hunting


### Post — @trailofbits — 2026-04-23 11:02 UTC (2026-04-23 12:02 WAT)

- URL: https://x.com/trailofbits/status/2047269756047081614
- Metrics (at fetch): bookmark 327, impression 44333, like 371, quote 6, reply 16, retweet 48

> When Claude reasons about code, it reasons about lists, but the questions that actually matter are graph questions.
>
> We just open-sourced Trailmark to make it easy for security engineers to parse source code into a call graph for Claude. 🧵


---

## 2026-04-22 · Post · If you market a machine that “cooks for you,” a chef will never buy it. 


Tags (automatic): AI-assisted hunting


### Post — @trailofbits — 2026-04-22 15:01 UTC (2026-04-22 16:01 WAT)

- URL: https://x.com/trailofbits/status/2046967662375579715
- Metrics (at fetch): bookmark 139, impression 23157, like 154, quote 3, reply 5, retweet 20

> If you market a machine that “cooks for you,” a chef will never buy it. 
>
> This is called identity threat, one of the four reasons why people resist adopting AI. @dguido breaks it down at unprompted: https://t.co/XF2LhWDBqo

**Media:**
- video: https://pbs.twimg.com/amplify_video_thumb/2046967439381172224/img/HoA-rHYcSyaa5Eot.jpg — no alt text provided by author


---

## 2026-04-21 · Post · Security auditors aren't going anywhere. @thebensams on @SuiNetwork Spaces https://t.co/9Jyd88Hltq


### Post — @trailofbits — 2026-04-21 11:02 UTC (2026-04-21 12:02 WAT)

- URL: https://x.com/trailofbits/status/2046545021898215907
- Metrics (at fetch): bookmark 29, impression 5868, like 71, quote 0, reply 2, retweet 3

> Security auditors aren't going anywhere. @thebensams on @SuiNetwork Spaces https://t.co/9Jyd88Hltq

**Media:**
- video: https://pbs.twimg.com/ext_tw_video_thumb/2046544987324600320/pu/img/moKyVLAXiWAYqZY4.jpg — no alt text provided by author


---

## 2026-04-20 · Post · We're testing frontier AI models like GPT-5.4-Cyber as part of @OpenAI's Trusted Access for Cyber pr


Tags (automatic): AI-assisted hunting


### Post — @trailofbits — 2026-04-20 15:19 UTC (2026-04-20 16:19 WAT)

- URL: https://x.com/trailofbits/status/2046247449283694854
- Metrics (at fetch): bookmark 25, impression 9631, like 75, quote 2, reply 2, retweet 10

> We're testing frontier AI models like GPT-5.4-Cyber as part of @OpenAI's Trusted Access for Cyber program.
>
> AI is dual-use, and the fastest way to find what attackers will do is to let defenders go first. https://t.co/Du2s1x99Gj


---

## 2026-04-17 · Post · Our sales team's AI Maturity Matrix. Scored from 0-3, defining what AI-enabled work looks like at ea


Tags (automatic): AI-assisted hunting


### Post — @trailofbits — 2026-04-17 14:00 UTC (2026-04-17 15:00 WAT)

- URL: https://x.com/trailofbits/status/2045140423891378619
- Metrics (at fetch): bookmark 32, impression 5111, like 35, quote 0, reply 4, retweet 3

> Our sales team's AI Maturity Matrix. Scored from 0-3, defining what AI-enabled work looks like at each level. 🧵 https://t.co/60leGpf4kt

**Media:**
- photo: https://pbs.twimg.com/media/HGHMYB6XIAA2cEY.jpg — no alt text provided by author


---

## 2026-04-17 · Thread · Google used a ZK proof to disclose a quantum breakthrough that cuts the cost of breaking cryptocurre


Tags (automatic): ZK


### Post — @trailofbits — 2026-04-17 11:02 UTC (2026-04-17 12:02 WAT)

- URL: https://x.com/trailofbits/status/2045095428975104009
- Metrics (at fetch): bookmark 273, impression 81092, like 714, quote 14, reply 14, retweet 90

> Google used a ZK proof to disclose a quantum breakthrough that cuts the cost of breaking cryptocurrency by 20x without handing attackers the circuit. We found anyone could forge a “proof” of an even stronger attack. 🧵


### Thread part 2 — @trailofbits — 2026-04-17 11:02 UTC (2026-04-17 12:02 WAT)

- URL: https://x.com/trailofbits/status/2045095429675552838
- Metrics (at fetch): bookmark 133, impression 56962, like 368, quote 8, reply 5, retweet 47

> The Rust code behind the proof had memory safety bugs. We used this new attack surface to forge a proof that beats Google’s on every metric.
>
> Google patched it within days. Their quantum claims are unaffected. https://blog.trailofbits.com/2026/04/17/we-beat-googles-zero-knowledge-proof-of-quantum-cryptanalysis/

**Links in post:** https://blog.trailofbits.com/2026/04/17/we-beat-googles-zero-knowledge-proof-of-quantum-cryptanalysis/


---

## 2026-04-16 · Post · 4 billion downloads a day run through @pypi. A missing permission check let any org member invite ne


### Post — @trailofbits — 2026-04-16 16:27 UTC (2026-04-16 17:27 WAT)

- URL: https://x.com/trailofbits/status/2044814847599374410
- Metrics (at fetch): bookmark 12, impression 8680, like 56, quote 0, reply 5, retweet 10

> 4 billion downloads a day run through @pypi. A missing permission check let any org member invite new owners. 
>
> One of 14 findings from our second audit. https://t.co/bms690Maxx

**Quoted post (full text):**

    #### Quoted post — @909754784705597441 — 2026-04-16 13:28 UTC (2026-04-16 14:28 WAT)
    
    - URL: https://x.com/909754784705597441/status/2044769869418102795
    - Metrics (at fetch): bookmark 7, impression 15834, like 36, quote 1, reply 0, retweet 10
    
    > 🔎🔐 #PyPI has completed its second external #security audit! Thanks to Sovereign Tech Agency for funding, @trailofbits for the audit, and @AlphaOmegaOSS for supporting rapid remediation. Find the full report on the Trail of Bits publication page. #Python
    > https://t.co/Gc3Xnhlj75
    


---

## 2026-04-16 · Post · An audit is not a clean bill of health. @thebensams on @SuiNetwork Spaces https://t.co/1aoRzYwa9x


### Post — @trailofbits — 2026-04-16 11:02 UTC (2026-04-16 12:02 WAT)

- URL: https://x.com/trailofbits/status/2044733085250433336
- Metrics (at fetch): bookmark 9, impression 5587, like 46, quote 0, reply 5, retweet 2

> An audit is not a clean bill of health. @thebensams on @SuiNetwork Spaces https://t.co/1aoRzYwa9x

**Media:**
- video: https://pbs.twimg.com/ext_tw_video_thumb/2044733059912675328/pu/img/4bGmIh2Zq83mrCr0.jpg — no alt text provided by author


---

## 2026-04-15 · Post · Our C/C++ security challenge closes Friday. If you can audit real code for memory safety and privile


### Post — @trailofbits — 2026-04-15 11:02 UTC (2026-04-15 12:02 WAT)

- URL: https://x.com/trailofbits/status/2044370790427009027
- Metrics (at fetch): bookmark 48, impression 5581, like 80, quote 0, reply 2, retweet 9

> Our C/C++ security challenge closes Friday. If you can audit real code for memory safety and privilege escalation, prove it. First 10 correct writeups win swag. https://t.co/a5JNWGkDWH


---

## 2026-04-14 · Post · Frosty runs two of our open-source skills for scoping and adversarial reasoning in its seven-stage p


### Post — @trailofbits — 2026-04-14 22:01 UTC (2026-04-14 23:01 WAT)

- URL: https://x.com/trailofbits/status/2044174159069286692
- Metrics (at fetch): bookmark 92, impression 18887, like 99, quote 1, reply 3, retweet 6

> Frosty runs two of our open-source skills for scoping and adversarial reasoning in its seven-stage pipeline.
>
> Our full skills repo: https://t.co/BuuCMEyS2L https://t.co/Krw5iT73SR

**Quoted post (full text):**

    #### Quoted post — @2555176531 — 2026-04-14 15:39 UTC (2026-04-14 16:39 WAT)
    
    - URL: https://x.com/2555176531/status/2044078174020006326
    - Metrics (at fetch): bookmark 67, impression 89956, like 93, quote 9, reply 21, retweet 15
    
    > Introducing Frosty, our AI-powered smart contract auditing tool that outperformed every other tool we evaluated. It runs in ~1-2 hours, can be 100x cheaper than a manual audit, and is now part of every smart contract review at Coinbase. Here's how we built it:
    


---

## 2026-04-14 · Post · Most companies use AI to do the same work slightly faster. We call that level one adoption. Companie


Tags (automatic): AI-assisted hunting


### Post — @trailofbits — 2026-04-14 11:02 UTC (2026-04-14 12:02 WAT)

- URL: https://x.com/trailofbits/status/2044008301751304338
- Metrics (at fetch): bookmark 82, impression 10662, like 96, quote 1, reply 3, retweet 4

> Most companies use AI to do the same work slightly faster. We call that level one adoption. Companies at level three do fundamentally different work.
>
> We're somewhere between level two and level three, and it took us a year to get there. 🧵 https://t.co/plYOQzIO2y

**Media:**
- video: https://pbs.twimg.com/ext_tw_video_thumb/2044008268213653504/pu/img/rP8Gk9Dh9Ek5IAxb.jpg — no alt text provided by author


---

## 2026-04-10 · Post · We open-sourced the system we built to make Trail of Bits AI-first. A six-step playbook for embeddin


Tags (automatic): AI-assisted hunting


### Post — @trailofbits — 2026-04-10 11:02 UTC (2026-04-10 12:02 WAT)

- URL: https://x.com/trailofbits/status/2042558794815635537
- Metrics (at fetch): bookmark 307, impression 27650, like 295, quote 3, reply 6, retweet 27

> We open-sourced the system we built to make Trail of Bits AI-first. A six-step playbook for embedding AI into how your team actually works, not just what tools they have access to. 🧵


---

## 2026-04-09 · Thread · We wrote two code challenges to go with this handbook. A Linux ping program with two libc gotchas an


Tags (automatic): RCE, Memory corruption / native


### Post — @trailofbits — 2026-04-09 14:50 UTC (2026-04-09 15:50 WAT)

- URL: https://x.com/trailofbits/status/2042253719476281499
- Metrics (at fetch): bookmark 32, impression 7673, like 58, quote 0, reply 3, retweet 4

> We wrote two code challenges to go with this handbook. A Linux ping program with two libc gotchas and a Windows driver handler hiding a path to kernel code execution. 🧵 https://t.co/TJh6AEWrLv

**Quoted post (full text):**

    #### Quoted post — @trailofbits — 2026-04-09 11:02 UTC (2026-04-09 12:02 WAT)
    
    - URL: https://x.com/trailofbits/status/2042196332471804000
    - Metrics (at fetch): bookmark 119, impression 13219, like 122, quote 1, reply 2, retweet 28
    
    > Language-level bug classes, stdlib pitfalls, Linux and Windows issues from usermode to kernel, seccomp sandbox escapes. One checklist, hundreds of checks. https://t.co/p2WWsuodi8
    


### Thread part 2 — @trailofbits — 2026-04-09 14:50 UTC (2026-04-09 15:50 WAT)

- URL: https://x.com/trailofbits/status/2042253721581871121
- Metrics (at fetch): bookmark 19, impression 15418, like 25, quote 1, reply 2, retweet 4

> Spot the bugs, first 10 correct answers win swag. Full details in the blog. https://blog.trailofbits.com/2026/04/09/master-c-and-c-with-our-new-testing-handbook-chapter/

**Links in post:** https://blog.trailofbits.com/2026/04/09/master-c-and-c-with-our-new-testing-handbook-chapter/


---

## 2026-04-09 · Post · Language-level bug classes, stdlib pitfalls, Linux and Windows issues from usermode to kernel, secco


Tags (automatic): Memory corruption / native


### Post — @trailofbits — 2026-04-09 11:02 UTC (2026-04-09 12:02 WAT)

- URL: https://x.com/trailofbits/status/2042196332471804000
- Metrics (at fetch): bookmark 119, impression 13219, like 122, quote 1, reply 2, retweet 28

> Language-level bug classes, stdlib pitfalls, Linux and Windows issues from usermode to kernel, seccomp sandbox escapes. One checklist, hundreds of checks. https://t.co/p2WWsuodi8


---

## 2026-04-09 · Post · C and C++ run your OS, your browser, your database, and your critical infrastructure. They're also t


### Post — @trailofbits — 2026-04-09 11:02 UTC (2026-04-09 12:02 WAT)

- URL: https://x.com/trailofbits/status/2042196330810937646
- Metrics (at fetch): bookmark 79, impression 9303, like 118, quote 4, reply 3, retweet 9

> C and C++ run your OS, your browser, your database, and your critical infrastructure. They're also the easiest languages to get catastrophically wrong. We wrote down everything a security auditor should check. 🧵


---

## 2026-04-07 · Post · Thousands of CEOs said AI had no impact on productivity. We use AI to catch 200 bugs/week where we u


Tags (automatic): AI-assisted hunting


### Post — @trailofbits — 2026-04-07 14:01 UTC (2026-04-07 15:01 WAT)

- URL: https://x.com/trailofbits/status/2041516603603386524
- Metrics (at fetch): bookmark 108, impression 25368, like 192, quote 3, reply 6, retweet 9

> Thousands of CEOs said AI had no impact on productivity. We use AI to catch 200 bugs/week where we used to find 15, and generate $8M per sales rep. 🧵


---

## 2026-04-07 · Thread · Before its launch, we audited @whatsapp's Private Processing TEEs and found 8 high-severity issues (


Tags (automatic): TEE / enclave


### Post — @trailofbits — 2026-04-07 11:02 UTC (2026-04-07 12:02 WAT)

- URL: https://x.com/trailofbits/status/2041471550881153077
- Metrics (at fetch): bookmark 87, impression 40888, like 232, quote 7, reply 5, retweet 35

> Before its launch, we audited @whatsapp's Private Processing TEEs and found 8 high-severity issues (patched). The enclaves yielded to injected config files, unmeasured ACPI tables, spoofed firmware levels, and stale attestation reports. 🧵


### Thread part 2 — @trailofbits — 2026-04-07 11:02 UTC (2026-04-07 12:02 WAT)

- URL: https://x.com/trailofbits/status/2041471551879381088
- Metrics (at fetch): bookmark 39, impression 5030, like 56, quote 1, reply 2, retweet 15

> @WhatsApp TEE security is only as good as the implementation details. Four lessons and the full report: https://blog.trailofbits.com/2026/04/07/what-we-learned-about-tee-security-from-auditing-whatsapps-private-inference/

**Links in post:** https://blog.trailofbits.com/2026/04/07/what-we-learned-about-tee-security-from-auditing-whatsapps-private-inference/


---

## 2026-04-03 · Post · 99.86% of 73K+ obfuscated expressions, simplified. CoBRA is a new open-source tool that handles four


### Post — @trailofbits — 2026-04-03 11:02 UTC (2026-04-03 12:02 WAT)

- URL: https://x.com/trailofbits/status/2040021999536287835
- Metrics (at fetch): bookmark 13, impression 4570, like 59, quote 0, reply 3, retweet 8

> 99.86% of 73K+ obfuscated expressions, simplified. CoBRA is a new open-source tool that handles four types of Mixed Boolean-Arithmetic obfuscation where existing tools fail. 🧵


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

## 2026-04-01 · Post · If you're competing in the @‌Wonderland CTF later today, these are the most common open-source tools


### Post — @trailofbits — 2026-04-01 07:00 UTC (2026-04-01 08:00 WAT)

- URL: https://x.com/trailofbits/status/2039236398985654495
- Metrics (at fetch): bookmark 58, impression 8511, like 68, quote 0, reply 4, retweet 8

> If you're competing in the @‌Wonderland CTF later today, these are the most common open-source tools we use to review contracts in production. 🧵


---

## 2026-03-27 · Post · We made the paper. Dimensional analysis catching Solidity bugs hiding in plain sight. 13 down in the


Tags (automatic): Smart contract / DeFi


### Post — @trailofbits — 2026-03-27 10:01 UTC (2026-03-27 11:01 WAT)

- URL: https://x.com/trailofbits/status/2037469976529969518
- Metrics (at fetch): bookmark 21, impression 5663, like 54, quote 0, reply 2, retweet 5

> We made the paper. Dimensional analysis catching Solidity bugs hiding in plain sight. 13 down in the @RektHQ Summit crossword. Come find us in Cannes. https://t.co/WTPLU1326Z

**Media:**
- photo: https://pbs.twimg.com/media/HEaMJBMWwAAWMBS.jpg — no alt text provided by author


---

## 2026-03-25 · Post · 93% recall vs 50% for baseline prompts. Our new dimensional-analysis plugin for Claude Code doesn't 


Tags (automatic): AI-assisted hunting


### Post — @trailofbits — 2026-03-25 12:00 UTC (2026-03-25 13:00 WAT)

- URL: https://x.com/trailofbits/status/2036775300579672233
- Metrics (at fetch): bookmark 155, impression 42299, like 160, quote 4, reply 4, retweet 19

> 93% recall vs 50% for baseline prompts. Our new dimensional-analysis plugin for Claude Code doesn't ask it to find bugs. It annotates your codebase with dimensional types, then flags mismatches mechanically. 🧵


---

## 2026-03-24 · Post · Physicists catch formula errors in seconds with a trick most DeFi developers have never heard of. Yo


Tags (automatic): Smart contract / DeFi


### Post — @trailofbits — 2026-03-24 12:00 UTC (2026-03-24 13:00 WAT)

- URL: https://x.com/trailofbits/status/2036412837233320208
- Metrics (at fetch): bookmark 149, impression 22265, like 152, quote 6, reply 8, retweet 21

> Physicists catch formula errors in seconds with a trick most DeFi developers have never heard of. You should learn dimension analysis. 🧵


---

## 2026-03-23 · Post · If you’re heading to EthCC in Cannes and want to meet the team, here’s where we’ll be. 🧵


### Post — @trailofbits — 2026-03-23 11:00 UTC (2026-03-23 12:00 WAT)

- URL: https://x.com/trailofbits/status/2036035345733607718
- Metrics (at fetch): bookmark 3, impression 4178, like 16, quote 0, reply 1, retweet 1

> If you’re heading to EthCC in Cannes and want to meet the team, here’s where we’ll be. 🧵


---

## 2026-03-19 · Post · HTTPS protected browsers. But satellites broadcasting military positions and cell tower audio in pla


### Post — @trailofbits — 2026-03-19 14:18 UTC (2026-03-19 15:18 WAT)

- URL: https://x.com/trailofbits/status/2034635532471337167
- Metrics (at fetch): bookmark 11, impression 2087, like 25, quote 0, reply 2, retweet 9

> HTTPS protected browsers. But satellites broadcasting military positions and cell tower audio in plain text? Nobody fixed that. https://t.co/HlP9QNqinQ

**Media:**
- photo: https://pbs.twimg.com/media/HDx6PB_XEAAshLm.jpg — no alt text provided by author


---

## 2026-03-17 · Post · Over 700,000 repos ship crypto libraries that default to a static IV, creating widespread key reuse.


Tags (automatic): AI-assisted hunting


### Post — @trailofbits — 2026-03-17 11:13 UTC (2026-03-17 12:13 WAT)

- URL: https://x.com/trailofbits/status/2033864175726850349
- Metrics (at fetch): bookmark 49, impression 14299, like 95, quote 0, reply 7, retweet 13

> Over 700,000 repos ship crypto libraries that default to a static IV, creating widespread key reuse. We also released mquire, a Linux memory forensics tool, and added 12 new open-source Claude Code skills for security engineering. March Tribune: https://t.co/jqoW9hzIAa


---

## 2026-03-11 · Thread · A single bug in an ERC-4337 smart account can be as catastrophic as leaking a private key.


### Post — @trailofbits — 2026-03-11 13:02 UTC (2026-03-11 14:02 WAT)

- URL: https://x.com/trailofbits/status/2031717351607910890
- Metrics (at fetch): bookmark 61, impression 5402, like 66, quote 1, reply 4, retweet 10

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

## 2026-03-05 · Post · We’re now an official ecosystem security partner for @SuiNetwork.


### Post — @trailofbits — 2026-03-05 18:00 UTC (2026-03-05 19:00 WAT)

- URL: https://x.com/trailofbits/status/2029617993278201975
- Metrics (at fetch): bookmark 12, impression 23440, like 88, quote 5, reply 5, retweet 11

> We’re now an official ecosystem security partner for @SuiNetwork.
>
> Sui builders get a direct line to our team for architecture reviews and security assessments. 🧵 https://t.co/yal5didZJ3

**Media:**
- photo: https://pbs.twimg.com/media/HCqmz0EX0AA4qsB.jpg — no alt text provided by author


---

## 2026-03-05 · Post · We're sponsoring @REverseConf in Orlando this week. A few of our research engineers will be there. C


### Post — @trailofbits — 2026-03-05 12:02 UTC (2026-03-05 13:02 WAT)

- URL: https://x.com/trailofbits/status/2029527855609049589
- Metrics (at fetch): bookmark 1, impression 2839, like 9, quote 0, reply 1, retweet 0

> We're sponsoring @REverseConf in Orlando this week. A few of our research engineers will be there. Come find them if you want to talk reverse engineering or binary analysis. https://t.co/LO9NaHDpnT

**Quoted post (full text):**

    #### Quoted post — @1819119228894707712 — 2025-10-20 18:08 UTC (2025-10-20 19:08 WAT)
    
    - URL: https://x.com/1819119228894707712/status/1980335268625314153
    - Metrics (at fetch): bookmark 0, impression 5330, like 9, quote 1, reply 0, retweet 1
    
    > We’re pumped to have Trail of Bits back at RE//verse as a 2026 Silver Sponsor! @trailofbits research has helped secure some of the world's most targeted organizations and products, combining high-end security research with a real-world attacker mentality to reduce risk and https://t.co/WLYOVLlkgt
    
    **Media:**
    - media `3_1980335265152376833` (details not returned by the API)
    


---

## 2026-03-04 · Post · Aave's approach to security serves as a benchmark for all DeFi protocols.


Tags (automatic): Smart contract / DeFi


### Post — @trailofbits — 2026-03-04 23:19 UTC (2026-03-05 00:19 WAT)

- URL: https://x.com/trailofbits/status/2029336023810097391
- Metrics (at fetch): bookmark 12, impression 12965, like 58, quote 0, reply 10, retweet 11

> Aave's approach to security serves as a benchmark for all DeFi protocols.
>
> Last month, we published a public security assessment of Aave V4 that's included in Aave's transparency report. 
>
> Read it to see how layered security works in practice. https://t.co/vZEpEFpV8T

**Quoted post (full text):**

    #### Quoted post — @867100084248469505 — 2026-03-04 18:12 UTC (2026-03-04 19:12 WAT)
    
    - URL: https://x.com/867100084248469505/status/2029258696761516461
    - Metrics (at fetch): bookmark 17, impression 84997, like 343, quote 14, reply 34, retweet 25
    
    > Aave V4 was built security-first, with layered security controls from early architecture through post-audit fix validation.
    >
    > We’ve published a full transparency report on the Aave V4 security program.
    >
    > Read it below. https://t.co/p7ixWP5Kil
    
    **Media:**
    - media `3_2029254781756125184` (details not returned by the API)
    


---

## 2026-03-04 · Post · Every Linux memory dump needs a different set of files before forensics tools can analyze it. You sh


### Post — @trailofbits — 2026-03-04 12:02 UTC (2026-03-04 13:02 WAT)

- URL: https://x.com/trailofbits/status/2029165464165736848
- Metrics (at fetch): bookmark 24, impression 10634, like 67, quote 0, reply 1, retweet 11

> Every Linux memory dump needs a different set of files before forensics tools can analyze it. You should know why that's no longer true.


---

## 2026-03-02 · Post · How do you rebuild a security consultancy around AI without breaking what works? @dguido talks syste


Tags (automatic): AI-assisted hunting


### Post — @trailofbits — 2026-03-02 12:02 UTC (2026-03-02 13:02 WAT)

- URL: https://x.com/trailofbits/status/2028440695183220759
- Metrics (at fetch): bookmark 11, impression 3391, like 18, quote 0, reply 0, retweet 3

> How do you rebuild a security consultancy around AI without breaking what works? @dguido talks systems, feedback loops, and what it actually takes to go AI-native at [un]prompted on March 4th at 9:10 AM https://t.co/9sGD4Hv6l5 https://t.co/HnJLDH4ZRU

**Quoted post (full text):**

    #### Quoted post — @15615663 — 2026-02-14 03:20 UTC (2026-02-14 04:20 WAT)
    
    - URL: https://x.com/15615663/status/2022511320885805291
    - Metrics (at fetch): bookmark 7, impression 10081, like 36, quote 2, reply 1, retweet 12
    
    > [un]prompted agenda is out!
    > This has been a complex selection process, with almost 500 talks submitted – many of which submitted in the final two days. But we got it done, and the agenda has now been released.
    >
    > https://t.co/6BFHjZPXC8 https://t.co/cUtExToAY3
    
    **Media:**
    - media `3_2022511315345117184` (details not returned by the API)
    


---

## 2026-02-27 · Post · We're sponsoring @Wonderland CTF 2026.


Tags (automatic): Blockchain / L1-L2 / bridge


### Post — @trailofbits — 2026-02-27 23:44 UTC (2026-02-28 00:44 WAT)

- URL: https://x.com/trailofbits/status/2027530286310035479
- Metrics (at fetch): bookmark 11, impression 6954, like 52, quote 1, reply 4, retweet 7

> We're sponsoring @Wonderland CTF 2026.
>
> Cybersecurity must be honed through practice, and many of our blockchain engineers got started through CTF competitions.
>
> Best of luck to all participants. https://t.co/LtFJ8lLif2

**Quoted post (full text):**

    #### Quoted post — @1384415976423317504 — 2026-02-24 17:53 UTC (2026-02-24 18:53 WAT)
    
    - URL: https://x.com/1384415976423317504/status/2026354713222909985
    - Metrics (at fetch): bookmark 27, impression 17781, like 79, quote 6, reply 4, retweet 17
    
    > Our first CTF sponsor is in.
    >
    > The team behind Slither, Echidna, and the next generation of open-source AI-assisted security tooling: @trailofbits.
    >
    > See you there.
    >
    > https://t.co/YQc8yQOVgY https://t.co/WwIwUu8T7J
    
    **Media:**
    - media `3_2026354680964546560` (details not returned by the API)
    


---

## 2026-02-24 · Post · By the end of 2026, the difference between consultants using AI and those who aren’t will be easy to


Tags (automatic): AI-assisted hunting


### Post — @trailofbits — 2026-02-24 11:32 UTC (2026-02-24 12:32 WAT)

- URL: https://x.com/trailofbits/status/2026258823875317946
- Metrics (at fetch): bookmark 34, impression 5792, like 56, quote 1, reply 2, retweet 4

> By the end of 2026, the difference between consultants using AI and those who aren’t will be easy to see. @dguido sat down with @riskybusiness to talk systems, feedback loops, and organizational change. https://t.co/X3qSRngibv https://t.co/PcytZWOOmG

**Media:**
- video: https://pbs.twimg.com/ext_tw_video_thumb/2026258810554253312/pu/img/N3vT5_xBPaOlxRoF.jpg — no alt text provided by author


---

## 2026-02-20 · Post · Before launch, @perplexity_ai hired us to test the security of Comet, their AI browser assistant. We


Tags (automatic): AI-assisted hunting


### Post — @trailofbits — 2026-02-20 16:26 UTC (2026-02-20 17:26 WAT)

- URL: https://x.com/trailofbits/status/2024883282605953039
- Metrics (at fetch): bookmark 103, impression 21125, like 164, quote 1, reply 9, retweet 18

> Before launch, @perplexity_ai hired us to test the security of Comet, their AI browser assistant. We demonstrated how four prompt injection techniques could extract users' private information from Gmail. 🧵


---

## 2026-02-18 · Post · Today at 12:55 PM MT on the Future Llama stage @EthereumDenver, @dguido opens the hood on how we're 


Tags (automatic): AI-assisted hunting


### Post — @trailofbits — 2026-02-18 19:27 UTC (2026-02-18 20:27 WAT)

- URL: https://x.com/trailofbits/status/2024204134061351237
- Metrics (at fetch): bookmark 6, impression 1950, like 18, quote 0, reply 0, retweet 1

> Today at 12:55 PM MT on the Future Llama stage @EthereumDenver, @dguido opens the hood on how we're making Trail of Bits AI-native. https://t.co/wD6V9JLy4N

**Media:**
- photo: https://pbs.twimg.com/media/HBdomyGXsAE0yIp.jpg — no alt text provided by author


---

## 2026-02-18 · Post · Today at 12:55 PM MT on the Future Llama stage @EthereumDenver, @dguido opens the hood on how he mad


Tags (automatic): AI-assisted hunting


### Post — @trailofbits — 2026-02-18 19:17 UTC (2026-02-18 20:17 WAT)

- URL: https://x.com/trailofbits/status/2024201575460135146
- Metrics (at fetch): bookmark 0, impression 1321, like 1, quote 1, reply 0, retweet 0

> Today at 12:55 PM MT on the Future Llama stage @EthereumDenver, @dguido opens the hood on how he made Trail of Bits AI-native. https://t.co/unxJxnXOa6

**Media:**
- photo: https://pbs.twimg.com/media/HBdomyGXsAE0yIp.jpg — no alt text provided by author


---

## 2026-02-18 · Post · Two AES libraries ship a default IV that guarantees key reuse. 700K+ repos depend on aes-js alone. A


### Post — @trailofbits — 2026-02-18 12:15 UTC (2026-02-18 13:15 WAT)

- URL: https://x.com/trailofbits/status/2024095323484729583
- Metrics (at fetch): bookmark 101, impression 43758, like 318, quote 10, reply 6, retweet 55

> Two AES libraries ship a default IV that guarantees key reuse. 700K+ repos depend on aes-js alone. A developer flagged the problem years ago, but it was never fixed. 🧵


---

## 2026-02-17 · Post · We're hiring a senior technical recruiter who can own the full hiring lifecycle and build a talent p


Tags (automatic): ZK


### Post — @trailofbits — 2026-02-17 11:50 UTC (2026-02-17 12:50 WAT)

- URL: https://x.com/trailofbits/status/2023726629692793231
- Metrics (at fetch): bookmark 7, impression 5031, like 42, quote 0, reply 1, retweet 3

> We're hiring a senior technical recruiter who can own the full hiring lifecycle and build a talent pipeline. If you thrive on personal connections with a knack for evaluating technical candidates across engineering and non-engineering roles, apply: https://t.co/zK9fIY7Oq1 https://t.co/oh6besMZPZ

**Media:**
- photo: https://pbs.twimg.com/media/HBW4pUvXsAAQRda.jpg — no alt text provided by author


---

## 2026-02-10 · Post · We shipped the infrastructure behind our AI security workflows: sandboxed devcontainers, dropkit for


Tags (automatic): AI-assisted hunting


### Post — @trailofbits — 2026-02-10 16:08 UTC (2026-02-10 17:08 WAT)

- URL: https://x.com/trailofbits/status/2021255004414185904
- Metrics (at fetch): bookmark 128, impression 17155, like 165, quote 2, reply 7, retweet 12

> We shipped the infrastructure behind our AI security workflows: sandboxed devcontainers, dropkit for cloud compute, and 23+ Claude Skills from our CEO and engineers. Catch up in our latest Tribune: https://t.co/UOOK9Kjf39


---

## 2026-01-30 · Post · Our team had 375+ pull requests merged into 90+ open-source projects in 2025. From the Rust compiler


### Post — @trailofbits — 2026-01-30 12:09 UTC (2026-01-30 13:09 WAT)

- URL: https://x.com/trailofbits/status/2017208425965305983
- Metrics (at fetch): bookmark 5, impression 6527, like 35, quote 1, reply 4, retweet 9

> Our team had 375+ pull requests merged into 90+ open-source projects in 2025. From the Rust compiler to PyPI Warehouse, these contributions strengthen the infrastructure devs rely on daily. 🧵


---

## 2026-01-29 · Post · Today's software signatures may not survive tomorrow's quantum computers. 🧵


### Post — @trailofbits — 2026-01-29 12:15 UTC (2026-01-29 13:15 WAT)

- URL: https://x.com/trailofbits/status/2016847561051557977
- Metrics (at fetch): bookmark 2, impression 2141, like 13, quote 0, reply 2, retweet 2

> Today's software signatures may not survive tomorrow's quantum computers. 🧵


---

## 2026-01-21 · Post · We've cut a new release of slither-mcp today that adds 11 new tools that help your AI-guided techniq


Tags (automatic): AI-assisted hunting


### Post — @trailofbits — 2026-01-21 16:26 UTC (2026-01-21 17:26 WAT)

- URL: https://x.com/trailofbits/status/2014011811633500642
- Metrics (at fetch): bookmark 51, impression 5968, like 79, quote 0, reply 3, retweet 7

> We've cut a new release of slither-mcp today that adds 11 new tools that help your AI-guided techniques become even more powerful: https://t.co/k1KjlwD1Va
>  
> It's easier than ever to add slither-mcp to Claude Code:
>
> claude mcp add --transport stdio --scope user slither -- uvx


---

## 2026-01-20 · Post · When did AI go from email drafts to binary analysis? 17 security Claude skills, open sourced. 🧵 http


Tags (automatic): AI-assisted hunting


### Post — @trailofbits — 2026-01-20 12:01 UTC (2026-01-20 13:01 WAT)

- URL: https://x.com/trailofbits/status/2013582670467309643
- Metrics (at fetch): bookmark 75, impression 10607, like 110, quote 1, reply 5, retweet 10

> When did AI go from email drafts to binary analysis? 17 security Claude skills, open sourced. 🧵 https://t.co/JdouaA9gkN

**Media:**
- photo: https://pbs.twimg.com/media/G_GuvWpXgAAHYfr.jpg — no alt text provided by author


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

**Quoted post (full text):**

    #### Quoted post — @1278266969532203008 — 2026-01-14 11:47 UTC (2026-01-14 12:47 WAT)
    
    - URL: https://x.com/1278266969532203008/status/2011404828115866061
    - Metrics (at fetch): bookmark 33, impression 23119, like 45, quote 2, reply 1, retweet 2
    
    > The @futureswapx' contract on #Arbitrum, which we reported was attacked four days ago, was exploited again, with an estimated loss of about $74K. While the loss is not large, the interesting part is that a new attack surface appeared: a reentrancy vulnerability.
    >
    > Specifically, https://t.co/RERkEWGdJW https://t.co/LRZ9nmNN6w
    
    **Media:**
    - media `3_2011404525194928129` (details not returned by the API)
    
    **Quoted post** 2009992056828244156: not readable via the API (deleted, private, or withheld).
    


---

## 2026-01-13 · Post · We exploited the lack of isolation in agentic browsers to steal data and hijack sessions. These atta


Tags (automatic): XSS, AI-assisted hunting


### Post — @trailofbits — 2026-01-13 12:11 UTC (2026-01-13 13:11 WAT)

- URL: https://x.com/trailofbits/status/2011048337181385071
- Metrics (at fetch): bookmark 20, impression 5728, like 61, quote 0, reply 3, retweet 11

> We exploited the lack of isolation in agentic browsers to steal data and hijack sessions. These attacks mirror XSS and CSRF, attacks the web spent years defending against. https://t.co/V93DbEAfQj

**Media:**
- photo: https://pbs.twimg.com/media/G-itzllW8AAoO26.jpg — no alt text provided by author


---

## 2026-01-08 · Post · Our 2026 summer internship applications are now open! Join our team to work on cutting-edge security


### Post — @trailofbits — 2026-01-08 12:37 UTC (2026-01-08 13:37 WAT)

- URL: https://x.com/trailofbits/status/2009242941823295714
- Metrics (at fetch): bookmark 259, impression 26582, like 344, quote 1, reply 13, retweet 20

> Our 2026 summer internship applications are now open! Join our team to work on cutting-edge security research, conduct assessments of critical systems, and build tools that advance the field. 🧵 https://t.co/3mpDksPn3B

**Media:**
- photo: https://pbs.twimg.com/media/G-JDzu1WwAA6k-Q.jpg — no alt text provided by author


---

## 2026-01-06 · Post · Are we entering a world where chatbots will replace devs? 🧵


### Post — @trailofbits — 2026-01-06 10:45 UTC (2026-01-06 11:45 WAT)

- URL: https://x.com/trailofbits/status/2008489982676070591
- Metrics (at fetch): bookmark 9, impression 6571, like 31, quote 0, reply 3, retweet 2

> Are we entering a world where chatbots will replace devs? 🧵


---

## 2026-01-01 · Post · December Tribune: Constant-time coding support for LLVM,  and cryptography webinars. https://mailchi


### Post — @trailofbits — 2026-01-01 12:15 UTC (2026-01-01 13:15 WAT)

- URL: https://x.com/trailofbits/status/2006700697924890678
- Metrics (at fetch): bookmark 7, impression 5524, like 21, quote 0, reply 1, retweet 0

> December Tribune: Constant-time coding support for LLVM,  and cryptography webinars. https://mailchi.mp/trailofbits/december-2025-tribune

**Links in post:** https://mailchi.mp/trailofbits/december-2025-tribune


---

## 2026-01-01 · Post · Trail of Bits Tribune: our hot take on vibe coding with LLMs - https://t.co/W3fJULKyB7


Tags (automatic): AI-assisted hunting


### Post — @trailofbits — 2026-01-01 11:59 UTC (2026-01-01 12:59 WAT)

- URL: https://x.com/trailofbits/status/2006696801051566310
- Metrics (at fetch): bookmark 28, impression 10597, like 54, quote 0, reply 4, retweet 7

> Trail of Bits Tribune: our hot take on vibe coding with LLMs - https://t.co/W3fJULKyB7


---

## 2025-12-31 · Post · Go's silent integer overflows hide bugs from fuzzers. go-panikint modifies the Go compiler to panic 


Tags (automatic): Memory corruption / native


### Post — @trailofbits — 2025-12-31 12:15 UTC (2025-12-31 13:15 WAT)

- URL: https://x.com/trailofbits/status/2006338305072234556
- Metrics (at fetch): bookmark 29, impression 5737, like 89, quote 0, reply 2, retweet 5

> Go's silent integer overflows hide bugs from fuzzers. go-panikint modifies the Go compiler to panic on arithmetic overflows, exposing vulnerabilities that wrap around undetected.


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

## 2025-12-16 · Post · How to stand out in security interviews 🧵 [pic.x.com/5e76V21T3b]


### Post — @trailofbits — 2025-12-16 12:35 UTC (2025-12-16 13:35 WAT)

- URL: https://x.com/trailofbits/status/2000907541333549476
- Metrics (at fetch): bookmark 12, impression 3665, like 20, quote 1, reply 3, retweet 2

> How to stand out in security interviews 🧵 [pic.x.com/5e76V21T3b]

**Media:**
- video: https://pbs.twimg.com/ext_tw_video_thumb/2000907515274350592/pu/img/UapHRGOeiaA7vCsf.jpg — no alt text provided by author


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

## 2025-12-15 · Post · Pull GitHub's pre-built CodeQL databases and run queries at scale in your terminal with mrva [pic.x.


### Post — @trailofbits — 2025-12-15 12:06 UTC (2025-12-15 13:06 WAT)

- URL: https://x.com/trailofbits/status/2000537833325379769
- Metrics (at fetch): bookmark 3, impression 2190, like 12, quote 0, reply 2, retweet 0

> Pull GitHub's pre-built CodeQL databases and run queries at scale in your terminal with mrva [pic.x.com/3yp7dyIkxO]

**Media:**
- photo: https://pbs.twimg.com/media/G8NWjtUXoAEYEY3.jpg — no alt text provided by author


---

## 2025-12-13 · Thread · Top TEE bugs you should fix before your audit in an upcoming webinar with @TinfoilAI 🧵 [pic.x.com/cn


Tags (automatic): TEE / enclave


### Post — @trailofbits — 2025-12-13 12:22 UTC (2025-12-13 13:22 WAT)

- URL: https://x.com/trailofbits/status/1999817089322807607
- Metrics (at fetch): bookmark 2, impression 5569, like 17, quote 1, reply 1, retweet 2

> Top TEE bugs you should fix before your audit in an upcoming webinar with @TinfoilAI 🧵 [pic.x.com/cn0Df2i7Vk]

**Media:**
- photo: https://pbs.twimg.com/media/G8DHC1OXsAEME6N.jpg — no alt text provided by author


### Thread part 2 — @trailofbits — 2025-12-13 12:22 UTC (2025-12-13 13:22 WAT)

- URL: https://x.com/trailofbits/status/1999817091050819813
- Metrics (at fetch): bookmark 3, impression 1136, like 5, quote 0, reply 0, retweet 0

> @TinfoilAI Using @tinfoilAI's infrastructure as a live example, @Julesdrean, @paulbottinelli, and @tjade273 walk through actual confidential computing code, configs, and attestation flows. https://watch.getcontrast.io/register/trail-of-bits-top-tee-bugs-you-should-fix-before-your-audit?utm_source=socials

**Links in post:** https://watch.getcontrast.io/register/trail-of-bits-top-tee-bugs-you-should-fix-before-your-audit?utm_source=socials


---

## 2025-12-12 · Post · Monitor unauthorized uses of your identity in transparency logs with Sigstore's rekor-monitor🧵 [pic.


### Post — @trailofbits — 2025-12-12 12:14 UTC (2025-12-12 13:14 WAT)

- URL: https://x.com/trailofbits/status/1999452681807483179
- Metrics (at fetch): bookmark 3, impression 1858, like 8, quote 0, reply 2, retweet 4

> Monitor unauthorized uses of your identity in transparency logs with Sigstore's rekor-monitor🧵 [pic.x.com/cr6n0YVxd0]

**Media:**
- photo: https://pbs.twimg.com/media/G797nmGXkAALXba.jpg — no alt text provided by author


---

## 2025-12-09 · Post · Webinar starting in 2 hours: Building end-to-end encrypted systems with our cryptographers. Join us:


### Post — @trailofbits — 2025-12-09 14:01 UTC (2025-12-09 15:01 WAT)

- URL: https://x.com/trailofbits/status/1998392557173145867
- Metrics (at fetch): bookmark 2, impression 2563, like 17, quote 0, reply 0, retweet 2

> Webinar starting in 2 hours: Building end-to-end encrypted systems with our cryptographers. Join us: https://watch.getcontrast.io/register/trail-of-bits-running-effective-threat-models-in-e2ee?utm_source=social [pic.x.com/rpkV0vwwLv]

**Media:**
- photo: https://pbs.twimg.com/media/G7u3cMTWMAAUHDV.jpg — no alt text provided by author

**Links in post:** https://watch.getcontrast.io/register/trail-of-bits-running-effective-threat-models-in-e2ee?utm_source=social


---

## 2025-12-08 · Post · Building a system with E2EE? Join our cryptographers tomorrow, December 9, at 11:00 a.m. ET for a we


### Post — @trailofbits — 2025-12-08 11:52 UTC (2025-12-08 12:52 WAT)

- URL: https://x.com/trailofbits/status/1997997594035761662
- Metrics (at fetch): bookmark 2, impression 2351, like 11, quote 0, reply 0, retweet 2

> Building a system with E2EE? Join our cryptographers tomorrow, December 9, at 11:00 a.m. ET for a webinar on implementation patterns and formal modeling approaches, followed by a Q&amp;A session. https://watch.getcontrast.io/register/trail-of-bits-running-effective-threat-models-in-e2ee?utm_source=social [pic.x.com/TMDcypGzXH]

**Media:**
- photo: https://pbs.twimg.com/media/G7pQOUFXsAAHxr7.jpg — no alt text provided by author

**Links in post:** https://watch.getcontrast.io/register/trail-of-bits-running-effective-threat-models-in-e2ee?utm_source=social


---

## 2025-12-05 · Post · We’re speaking @BlackHatEvents EU Dec 10 🧵 [pic.x.com/UWeW74okqO]


### Post — @trailofbits — 2025-12-05 12:40 UTC (2025-12-05 13:40 WAT)

- URL: https://x.com/trailofbits/status/1996922517143838886
- Metrics (at fetch): bookmark 1, impression 1982, like 15, quote 0, reply 1, retweet 1

> We’re speaking @BlackHatEvents EU Dec 10 🧵 [pic.x.com/UWeW74okqO]

**Media:**
- photo: https://pbs.twimg.com/media/G7Z-ckSXwAAJSO4.jpg — no alt text provided by author


---

## 2025-12-02 · Post · Continuous group key agreement. Device enrollment and unenrollment. Message backup. Contact discover


Tags (automatic): AI-assisted hunting


### Post — @trailofbits — 2025-12-02 14:49 UTC (2025-12-02 15:49 WAT)

- URL: https://x.com/trailofbits/status/1995867815417463111
- Metrics (at fetch): bookmark 2, impression 2051, like 15, quote 0, reply 1, retweet 2

> Continuous group key agreement. Device enrollment and unenrollment. Message backup. Contact discovery. Abuse reporting. E2EE problems you need to solve. 🧵 [pic.x.com/t8TGMuU4e7]

**Media:**
- photo: https://pbs.twimg.com/media/G7K_M3sWsAAqrKf.jpg — no alt text provided by author


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

## 2025-12-02 · Post · We’re thrilled to see Slither being used by Anthropic to augment their agentic smart contract resear


Tags (automatic): Smart contract / DeFi, AI-assisted hunting


### Post — @trailofbits — 2025-12-02 07:05 UTC (2025-12-02 08:05 WAT)

- URL: https://x.com/trailofbits/status/1995751143126040770
- Metrics (at fetch): bookmark 151, impression 36499, like 284, quote 5, reply 9, retweet 21

> We’re thrilled to see Slither being used by Anthropic to augment their agentic smart contract research.
>
> If you’re interested in adding Slither to your LLM-based agents or workflows, check out our newly released slither-mcp: https://github.com/trailofbits/slither-mcp [pic.x.com/uzcqS2knaN] https://twitter.com/AnthropicAI/status/1995631802032287779

**Media:**
- photo: https://pbs.twimg.com/media/G7JU8SPbEAASc9P.png — no alt text provided by author
- photo: https://pbs.twimg.com/media/G7JU9jhacAAl8Ec.jpg — no alt text provided by author

**Links in post:** https://github.com/trailofbits/slither-mcp, https://twitter.com/AnthropicAI/status/1995631802032287779

**Quoted post (full text):**

    #### Quoted post — @AnthropicAI — 2025-12-01 23:11 UTC (2025-12-02 00:11 WAT)
    
    - URL: https://x.com/AnthropicAI/status/1995631802032287779
    - Metrics (at fetch): bookmark 2246, impression 2128900, like 4727, quote 502, reply 340, retweet 682
    
    > New on our Frontier Red Team blog: We tested whether AIs can exploit blockchain smart contracts.
    >
    > In simulated testing, AI agents found $4.6M in exploits.
    >
    > The research (with @MATSprogram and the Anthropic Fellows program) also developed a new benchmark: https://red.anthropic.com/2025/smart-contracts/
    
    **Links in post:** https://red.anthropic.com/2025/smart-contracts/
    


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
- Metrics (at fetch): bookmark 9, impression 2333, like 23, quote 1, reply 2, retweet 1

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

## 2025-11-13 · Post · Quickly identify weak binaries in your browser by dragging files into Checksec Anywhere, which will 


### Post — @trailofbits — 2025-11-13 12:51 UTC (2025-11-13 13:51 WAT)

- URL: https://x.com/trailofbits/status/1988952814794731974
- Metrics (at fetch): bookmark 10, impression 8468, like 26, quote 1, reply 1, retweet 3

> Quickly identify weak binaries in your browser by dragging files into Checksec Anywhere, which will then automatically create a color-coded security report. [pic.x.com/ov32r72FKZ]

**Media:**
- animated_gif: https://pbs.twimg.com/tweet_video_thumb/G5otz4FbkAABKXO.jpg — no alt text provided by author


---

## 2025-11-08 · Post · Our Balancer retro is live. The ecosystem has evolved &amp; rounding issues are more critical than e


Tags (automatic): Smart contract / DeFi


### Post — @trailofbits — 2025-11-08 00:05 UTC (2025-11-08 01:05 WAT)

- URL: https://x.com/trailofbits/status/1986948235269972275
- Metrics (at fetch): bookmark 52, impression 15607, like 72, quote 3, reply 3, retweet 11

> Our Balancer retro is live. The ecosystem has evolved &amp; rounding issues are more critical than ever. Here are recommendations for preventing rounding issues and other important lessons from this incident: https://blog.trailofbits.com/2025/11/07/balancer-hack-analysis-and-guidance-for-the-defi-ecosystem/ https://twitter.com/trailofbits/status/1986101923947200971

**Links in post:** https://blog.trailofbits.com/2025/11/07/balancer-hack-analysis-and-guidance-for-the-defi-ecosystem/, https://twitter.com/trailofbits/status/1986101923947200971

**Quoted post (full text):**

    #### Quoted post — @trailofbits — 2025-11-05 16:02 UTC (2025-11-05 17:02 WAT)
    
    - URL: https://x.com/trailofbits/status/1986101923947200971
    - Metrics (at fetch): bookmark 30, impression 44295, like 214, quote 2, reply 6, retweet 12
    
    > Since the Balancer hack on Monday, we've been working around the clock to help the Balancer team understand the bug and its implications. We've verified the bug's cause and have independently verified that the exploit does not work on Balancer V3.
    >
    > Once the dust settles, we plan on doing a retrospective and sharing more information including long-term, strategic guidance on how to avoid similar bugs.
    


---

## 2025-11-07 · Post · Catch @kiki_morozova on November 8th @SidesBer. They show how AI image downscaling creates prompt in


Tags (automatic): AI-assisted hunting


### Post — @trailofbits — 2025-11-07 10:41 UTC (2025-11-07 11:41 WAT)

- URL: https://x.com/trailofbits/status/1986745702953689299
- Metrics (at fetch): bookmark 0, impression 2323, like 11, quote 0, reply 1, retweet 2

> Catch @kiki_morozova on November 8th @SidesBer. They show how AI image downscaling creates prompt injection vectors. Learn fingerprinting techniques to detect these vulnerabilities in your systems. https://bsides.berlin/#schedule [pic.x.com/TPo5tOUnBt]

**Media:**
- photo: https://pbs.twimg.com/media/G5JWsDiXkAAxG_o.jpg — no alt text provided by author

**Links in post:** https://bsides.berlin/#schedule


---

## 2025-11-05 · Post · Since the Balancer hack on Monday, we've been working around the clock to help the Balancer team und


### Post — @trailofbits — 2025-11-05 16:02 UTC (2025-11-05 17:02 WAT)

- URL: https://x.com/trailofbits/status/1986101923947200971
- Metrics (at fetch): bookmark 30, impression 44295, like 214, quote 2, reply 6, retweet 12

> Since the Balancer hack on Monday, we've been working around the clock to help the Balancer team understand the bug and its implications. We've verified the bug's cause and have independently verified that the exploit does not work on Balancer V3.
>
> Once the dust settles, we plan on doing a retrospective and sharing more information including long-term, strategic guidance on how to avoid similar bugs.


---

## 2025-11-05 · Post · NYC cyber students: Meet our team @CSAW_NYUTandon on November 6th 🧵


### Post — @trailofbits — 2025-11-05 11:55 UTC (2025-11-05 12:55 WAT)

- URL: https://x.com/trailofbits/status/1986039609969549409
- Metrics (at fetch): bookmark 0, impression 1589, like 3, quote 0, reply 1, retweet 0

> NYC cyber students: Meet our team @CSAW_NYUTandon on November 6th 🧵


---

## 2025-11-04 · Post · Nov 6: our CEO, @dguido, and @RickySkiroToB discuss making Buttercup accessible for real-world secur


Tags (automatic): AI-assisted hunting


### Post — @trailofbits — 2025-11-04 09:42 UTC (2025-11-04 10:42 WAT)

- URL: https://x.com/trailofbits/status/1985643693924127076
- Metrics (at fetch): bookmark 3, impression 2407, like 12, quote 0, reply 1, retweet 4

> Nov 6: our CEO, @dguido, and @RickySkiroToB discuss making Buttercup accessible for real-world security teams at Berkeley's online AI Cybersecurity workshop 🧵 [pic.x.com/pGnJnbXCfx]

**Media:**
- photo: https://pbs.twimg.com/media/G45saiUXYAAEZbE.jpg — no alt text provided by author


---

## 2025-11-03 · Post · Take your lunch break on November 6th at 12:00 PM ET with us and @appblockchain as we break down rec


Tags (automatic): Blockchain / L1-L2 / bridge, TEE / enclave


### Post — @trailofbits — 2025-11-03 11:47 UTC (2025-11-03 12:47 WAT)

- URL: https://x.com/trailofbits/status/1985312754358522012
- Metrics (at fetch): bookmark 10, impression 4737, like 14, quote 0, reply 4, retweet 6

> Take your lunch break on November 6th at 12:00 PM ET with us and @appblockchain as we break down recent TEE attacks, why they're unpatchable, and what this means for blockchain teams dependent on confidential computing. https://watch.getcontrast.io/register/trail-of-bits-after-wiretap-and-battering-ram-what-changes-for-tee-based-blockchain-infrastructure?utm_source=tb&utm_medium=x

**Links in post:** https://watch.getcontrast.io/register/trail-of-bits-after-wiretap-and-battering-ram-what-changes-for-tee-based-blockchain-infrastructure?utm_source=tb&utm_medium=x


---

## 2025-10-31 · Post · Most border crossings depend on cryptographic protocols most people have never heard of. You should 


### Post — @trailofbits — 2025-10-31 11:46 UTC (2025-10-31 12:46 WAT)

- URL: https://x.com/trailofbits/status/1984225464571867580
- Metrics (at fetch): bookmark 135, impression 25283, like 187, quote 3, reply 4, retweet 18

> Most border crossings depend on cryptographic protocols most people have never heard of. You should know the technology and security risks behind your passport. [pic.x.com/dVmZl4YGt5]

**Media:**
- photo: https://pbs.twimg.com/media/G4lii4VWMAAgnYF.jpg — no alt text provided by author


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

## 2025-10-27 · Post · We'll see your Offsec Team @DistrictCon for our talk on backdooring Electron apps.


### Post — @trailofbits — 2025-10-27 19:07 UTC (2025-10-27 20:07 WAT)

- URL: https://x.com/trailofbits/status/1982886929613107536
- Metrics (at fetch): bookmark 6, impression 4492, like 14, quote 0, reply 0, retweet 3

> We'll see your Offsec Team @DistrictCon for our talk on backdooring Electron apps.
> In the meantime, https://blog.trailofbits.com/2025/09/03/subverting-code-integrity-checks-to-locally-backdoor-signal-1password-slack-and-more/ [pic.x.com/sf5nHgkdxR] https://twitter.com/DistrictCon/status/1982849778087276937

**Media:**
- photo: https://pbs.twimg.com/media/G4ShJYUWUAA-_eV.png — no alt text provided by author

**Links in post:** https://blog.trailofbits.com/2025/09/03/subverting-code-integrity-checks-to-locally-backdoor-signal-1password-slack-and-more/, https://twitter.com/DistrictCon/status/1982849778087276937

**Quoted post (full text):**

    #### Quoted post — @1763969352150532097 — 2025-10-27 16:40 UTC (2025-10-27 17:40 WAT)
    
    - URL: https://x.com/1763969352150532097/status/1982849778087276937
    - Metrics (at fetch): bookmark 7, impression 25571, like 40, quote 7, reply 1, retweet 14
    
    > We're officially announcing our speakers DistrictCon Year 1! Check out our incredible lineup: https://www.districtcon.org/speakers
    
    **Links in post:** https://www.districtcon.org/speakers
    


---

## 2025-10-23 · Post · Fickling now blocks malicious payloads with one line of code, our CodeQL query narrowed down 2,500 c


### Post — @trailofbits — 2025-10-23 11:04 UTC (2025-10-23 12:04 WAT)

- URL: https://x.com/trailofbits/status/1981315729057010023
- Metrics (at fetch): bookmark 4, impression 3734, like 11, quote 0, reply 1, retweet 1

> Fickling now blocks malicious payloads with one line of code, our CodeQL query narrowed down 2,500 compiler warnings in OpenVPN2 to 20, and mutation testing insights in this month's Tribune. https://mailchi.mp/trailofbits/trail-of-bits-tribune-october

**Links in post:** https://mailchi.mp/trailofbits/trail-of-bits-tribune-october


---

## 2025-10-22 · Post · AI agents with "human approval" protections can be bypassed with argument injection. We achieved RCE


Tags (automatic): RCE, AI-assisted hunting


### Post — @trailofbits — 2025-10-22 14:15 UTC (2025-10-22 15:15 WAT)

- URL: https://x.com/trailofbits/status/1981001436725915668
- Metrics (at fetch): bookmark 27, impression 7086, like 39, quote 3, reply 2, retweet 19

> AI agents with "human approval" protections can be bypassed with argument injection. We achieved RCE across three platforms by exploiting pre-approved commands like git, ripgrep, and go test. 🧵 [pic.x.com/30JobvQ2zW]

**Media:**
- photo: https://pbs.twimg.com/media/G33uTu1XUAAbKFX.jpg — no alt text provided by author


---

## 2025-10-21 · Thread · With just $50 in hardware, attackers can extract attestation keys, view encrypted data, and tamper w


Tags (automatic): Blockchain / L1-L2 / bridge, TEE / enclave


### Post — @trailofbits — 2025-10-21 10:20 UTC (2025-10-21 11:20 WAT)

- URL: https://x.com/trailofbits/status/1980579827733106828
- Metrics (at fetch): bookmark 6, impression 2672, like 20, quote 0, reply 1, retweet 7

> With just $50 in hardware, attackers can extract attestation keys, view encrypted data, and tamper with confidential workloads in Intel SGX and AMD SEV-SNP. 🧵 [pic.x.com/C4bje6geZB]

**Media:**
- photo: https://pbs.twimg.com/media/G3xu23mXkAA7M26.jpg — no alt text provided by author


### Thread part 2 — @trailofbits — 2025-10-21 10:20 UTC (2025-10-21 11:20 WAT)

- URL: https://x.com/trailofbits/status/1980579828886634574
- Metrics (at fetch): bookmark 4, impression 1333, like 7, quote 0, reply 0, retweet 2

> Trail of Bits and @appblockchain explain how Wiretap and DRAM aliasing attacks work, why they're unpatchable, and what this means for confidential computing in blockchain infrastructure. Nov 6, 12 PM ET. https://watch.getcontrast.io/register/trail-of-bits-after-wiretap-and-battering-ram-what-changes-for-tee-based-blockchain-infrastructure?utm_source=tb&utm_medium=x

**Links in post:** https://watch.getcontrast.io/register/trail-of-bits-after-wiretap-and-battering-ram-what-changes-for-tee-based-blockchain-infrastructure?utm_source=tb&utm_medium=x


---

## 2025-10-17 · Post · Buttercup found 28 real vulnerabilities and patched them autonomously during @DARPA’s AIxCC finals. 


Tags (automatic): AI-assisted hunting


### Post — @trailofbits — 2025-10-17 11:55 UTC (2025-10-17 12:55 WAT)

- URL: https://x.com/trailofbits/status/1979154177516286008
- Metrics (at fetch): bookmark 8, impression 2095, like 16, quote 0, reply 0, retweet 3

> Buttercup found 28 real vulnerabilities and patched them autonomously during @DARPA’s AIxCC finals. See how our open-source Cyber Reasoning System scales from laptops to enterprise environments @_ringzer0 Counter Measure conference. 
> https://ringzer0.training/countermeasure25-buttercup-and-darpas-ai-cyber-challenge/

**Links in post:** https://ringzer0.training/countermeasure25-buttercup-and-darpas-ai-cyber-challenge/


---

## 2025-10-16 · Post · Today @GriffissInst: Director of Research, Dr. Trent Brunson, will present Buttercup, our open-sourc


### Post — @trailofbits — 2025-10-16 10:45 UTC (2025-10-16 11:45 WAT)

- URL: https://x.com/trailofbits/status/1978774202623619272
- Metrics (at fetch): bookmark 1, impression 1981, like 8, quote 0, reply 1, retweet 2

> Today @GriffissInst: Director of Research, Dr. Trent Brunson, will present Buttercup, our open-source CRS that won @DARPA's AIxCC $3M 2nd place prize. https://app.smartsheet.com/b/form/93b8c5da7d6f4243ad75a5bf229da6a4 [pic.x.com/hiBiA4q1mu]

**Media:**
- photo: https://pbs.twimg.com/media/G3YEpouWUAAzW94.jpg — no alt text provided by author

**Links in post:** https://app.smartsheet.com/b/form/93b8c5da7d6f4243ad75a5bf229da6a4


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

## 2025-10-10 · Post · We built a framework to automate benchmarking OpenSearch and Elasticsearch using OpenSearch Benchmar


### Post — @trailofbits — 2025-10-10 11:03 UTC (2025-10-10 12:03 WAT)

- URL: https://x.com/trailofbits/status/1976604570634588373
- Metrics (at fetch): bookmark 0, impression 1590, like 4, quote 0, reply 3, retweet 2

> We built a framework to automate benchmarking OpenSearch and Elasticsearch using OpenSearch Benchmark. With the click of a button, users can continuously gather results to make actionable decisions on which search engine fits their needs best. [pic.x.com/4N76DqzhWj]

**Media:**
- video: https://pbs.twimg.com/ext_tw_video_thumb/1976604552997564416/pu/img/1Vydbh9kO8T0OjJq.jpg — no alt text provided by author


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

## 2025-10-06 · Post · We're hiring an ML Security Researcher to break frontier AI systems. Work with leading labs, plus co


Tags (automatic): AI-assisted hunting


### Post — @trailofbits — 2025-10-06 22:57 UTC (2025-10-06 23:57 WAT)

- URL: https://x.com/trailofbits/status/1975334657055961450
- Metrics (at fetch): bookmark 10, impression 7063, like 60, quote 0, reply 4, retweet 10

> We're hiring an ML Security Researcher to break frontier AI systems. Work with leading labs, plus conduct and publish novel research that moves the needle in the AI/ML field. 🧵 [pic.x.com/CEMbGtUWmS]

**Media:**
- photo: https://pbs.twimg.com/media/G2nMZy0WwAA2Zpg.jpg — no alt text provided by author


---

## 2025-09-30 · Post · We contributed upstream CodeQL query improvements to drastically improve SQL vulnerability detection


### Post — @trailofbits — 2025-09-30 12:47 UTC (2025-09-30 13:47 WAT)

- URL: https://x.com/trailofbits/status/1973006668859330930
- Metrics (at fetch): bookmark 6, impression 1649, like 9, quote 0, reply 2, retweet 1

> We contributed upstream CodeQL query improvements to drastically improve SQL vulnerability detection. Check them out ⬇️
> https://github.com/github/codeql/pulls?q=is%3Apr+author%3AVasco-jofra+is%3Aclosed

**Links in post:** https://github.com/github/codeql/pulls?q=is%3Apr+author%3AVasco-jofra+is%3Aclosed


---

## 2025-09-30 · Post · We’re speaking @DeComputeConf and will be at @Token2049 later in the week. DM us if you’d like to gr


### Post — @trailofbits — 2025-09-30 00:15 UTC (2025-09-30 01:15 WAT)

- URL: https://x.com/trailofbits/status/1972817441521602940
- Metrics (at fetch): bookmark 1, impression 2102, like 11, quote 0, reply 4, retweet 1

> We’re speaking @DeComputeConf and will be at @Token2049 later in the week. DM us if you’d like to grab coffee with one of our cryptographers attending 🧵


---

## 2025-09-26 · Post · We are pleased to announce that Trail of Bits has joined the Mastercard Engage partner


Tags (automatic): Blockchain / L1-L2 / bridge


### Post — @trailofbits — 2025-09-26 10:05 UTC (2025-09-26 11:05 WAT)

- URL: https://x.com/trailofbits/status/1971516359113683024
- Metrics (at fetch): bookmark 3, impression 2347, like 19, quote 0, reply 0, retweet 2

> We are pleased to announce that Trail of Bits has joined the Mastercard Engage partner
> network to accelerate time to market for blockchain innovation.
> https://engagepartners.mastercard.com/English/directory/search?f0=Domain&f0v0=Crypto&f1=Sub+Domain&f1v0=Crypto+Issuance&f2=Solution&f2v0=Web3+Card&length=48
>
> @mastercardnews [pic.x.com/mOwJyvs1La]

**Media:**
- photo: https://pbs.twimg.com/media/G1w7rjdW0AAK4_G.jpg — no alt text provided by author

**Links in post:** https://engagepartners.mastercard.com/English/directory/search?f0=Domain&f0v0=Crypto&f1=Sub+Domain&f1v0=Crypto+Issuance&f2=Solution&f2v0=Web3+Card&length=48


---

## 2025-09-25 · Post · We improved the signal-to-noise ratio of compiler warnings for @OpenVPN (v2) with a custom CodeQL qu


### Post — @trailofbits — 2025-09-25 15:19 UTC (2025-09-25 16:19 WAT)

- URL: https://x.com/trailofbits/status/1971232984264007890
- Metrics (at fetch): bookmark 3, impression 2403, like 13, quote 0, reply 1, retweet 1

> We improved the signal-to-noise ratio of compiler warnings for @OpenVPN (v2) with a custom CodeQL query that you can now run on your codebase. 🧵 [pic.x.com/I3hyRtoFQn]

**Media:**
- photo: https://pbs.twimg.com/media/G1s59BMXgAAgAki.jpg — no alt text provided by author


---

## 2025-09-24 · Post · Do you trust what you're installing when you run cargo add or pip install? 🧵 [pic.x.com/ocB94UrBi9]


### Post — @trailofbits — 2025-09-24 14:48 UTC (2025-09-24 15:48 WAT)

- URL: https://x.com/trailofbits/status/1970862967500447932
- Metrics (at fetch): bookmark 11, impression 2962, like 15, quote 0, reply 1, retweet 7

> Do you trust what you're installing when you run cargo add or pip install? 🧵 [pic.x.com/ocB94UrBi9]

**Media:**
- photo: https://pbs.twimg.com/media/G1npbLnWoAA_zUH.jpg — no alt text provided by author


---

## 2025-09-24 · Post · NY Governor Kathy Hochul congratulated us on winning 2nd place in @DARPA's AI Cyber Challenge and re


Tags (automatic): AI-assisted hunting


### Post — @trailofbits — 2025-09-24 11:55 UTC (2025-09-24 12:55 WAT)

- URL: https://x.com/trailofbits/status/1970819261657411958
- Metrics (at fetch): bookmark 2, impression 3641, like 30, quote 0, reply 3, retweet 5

> NY Governor Kathy Hochul congratulated us on winning 2nd place in @DARPA's AI Cyber Challenge and recognized our impact on NY's cybersecurity ecosystem through our research, community building, and educational initiatives. [pic.x.com/grfGF9oyb8]

**Media:**
- photo: https://pbs.twimg.com/media/G1nBrKRWQAAolTz.jpg — no alt text provided by author
- photo: https://pbs.twimg.com/media/G1nBrHpW4AAwOe5.jpg — no alt text provided by author


---

## 2025-09-23 · Post · Read about AI image scaling attacks, backdooring Chromium apps, a security review of Meta's WhatsApp


Tags (automatic): AI-assisted hunting


### Post — @trailofbits — 2025-09-23 11:04 UTC (2025-09-23 12:04 WAT)

- URL: https://x.com/trailofbits/status/1970444116216426990
- Metrics (at fetch): bookmark 11, impression 6369, like 20, quote 0, reply 2, retweet 2

> Read about AI image scaling attacks, backdooring Chromium apps, a security review of Meta's WhatsApp and so much more in this month's Tribune: https://mailchi.mp/trailofbits/trail-of-bits-tribune-september

**Links in post:** https://mailchi.mp/trailofbits/trail-of-bits-tribune-september


---

## 2025-09-16 · Post · In a pickle with ML security?


### Post — @trailofbits — 2025-09-16 11:08 UTC (2025-09-16 12:08 WAT)

- URL: https://x.com/trailofbits/status/1967908329855803671
- Metrics (at fetch): bookmark 13, impression 7538, like 44, quote 0, reply 1, retweet 8

> In a pickle with ML security?
>  We added a new pickle file scanner to Fickling that enhances supply-chain security 🧵 [pic.x.com/DDaUU9T0tC]

**Media:**
- photo: https://pbs.twimg.com/media/G09qMn1XYAAfzRL.jpg — no alt text provided by author


---

## 2025-09-08 · Post · Join Michael Brown, Head of AI/ML Security Research at Trail of Bits, when he sits down for a Q&amp;


Tags (automatic): AI-assisted hunting


### Post — @trailofbits — 2025-09-08 11:30 UTC (2025-09-08 12:30 WAT)

- URL: https://x.com/trailofbits/status/1965014853606691215
- Metrics (at fetch): bookmark 5, impression 3433, like 26, quote 0, reply 0, retweet 2

> Join Michael Brown, Head of AI/ML Security Research at Trail of Bits, when he sits down for a Q&amp;A with Edera to chat about our experience in AIxCC and what we learned building AI security agents that actually work. 
>
>  September 11, 2025 | 12:00 PM ET 
>  https://edera.link/vev2li [pic.x.com/z12HIgbGu7]

**Media:**
- photo: https://pbs.twimg.com/media/G0UimK0WIAAqvAH.jpg — no alt text provided by author

**Links in post:** https://edera.link/vev2li


---

## 2025-09-04 · Post · We built local backdoors for @signalapp, @1Password, @SlackHQ, and @googlechrome using a “data” file


### Post — @trailofbits — 2025-09-04 16:43 UTC (2025-09-04 17:43 WAT)

- URL: https://x.com/trailofbits/status/1963644218749886616
- Metrics (at fetch): bookmark 375, impression 79891, like 965, quote 11, reply 10, retweet 97

> We built local backdoors for @signalapp, @1Password, @SlackHQ, and @googlechrome using a “data” file their integrity checks ignored. [pic.x.com/eIPVDQQR2n]

**Media:**
- photo: https://pbs.twimg.com/media/G0BEAtgWwAAdi_W.jpg — no alt text provided by author


---

## 2025-09-04 · Post · Learn more about our CRS, Buttercup 👇 


### Post — @trailofbits — 2025-09-04 09:44 UTC (2025-09-04 10:44 WAT)

- URL: https://x.com/trailofbits/status/1963538530057007104
- Metrics (at fetch): bookmark 4, impression 2499, like 8, quote 0, reply 0, retweet 0

> Learn more about our CRS, Buttercup 👇 
> https://www.trailofbits.com/buttercup https://twitter.com/DARPA/status/1963331540684828767

**Links in post:** https://www.trailofbits.com/buttercup, https://twitter.com/DARPA/status/1963331540684828767

**Quoted post (full text):**

    #### Quoted post — @54645160 — 2025-09-03 20:01 UTC (2025-09-03 21:01 WAT)
    
    - URL: https://x.com/54645160/status/1963331540684828767
    - Metrics (at fetch): bookmark 60, impression 25768, like 234, quote 11, reply 20, retweet 87
    
    > The DARPA AI Cyber Challenge was designed to advance cybersecurity technology and ensure that technology is applied to secure the code we all rely on. All seven finalist teams have released their competition cyber reasoning systems open source. https://archive.aicyberchallenge.com/ [pic.x.com/00fOoBhhuf]
    
    **Media:**
    - media `3_1963331538499547137` (details not returned by the API)
    
    **Links in post:** https://archive.aicyberchallenge.com/
    


---

## 2025-08-29 · Post · See you all on Tuesday https://twitter.com/RektHQ/status/1961425666164887879


### Post — @trailofbits — 2025-08-29 17:58 UTC (2025-08-29 18:58 WAT)

- URL: https://x.com/trailofbits/status/1961488536613654893
- Metrics (at fetch): bookmark 0, impression 2366, like 4, quote 0, reply 0, retweet 0

> See you all on Tuesday https://twitter.com/RektHQ/status/1961425666164887879

**Links in post:** https://twitter.com/RektHQ/status/1961425666164887879

**Quoted post (full text):**

    #### Quoted post — @1297925400090337280 — 2025-08-29 13:48 UTC (2025-08-29 14:48 WAT)
    
    - URL: https://x.com/1297925400090337280/status/1961425666164887879
    - Metrics (at fetch): bookmark 6, impression 16131, like 53, quote 3, reply 11, retweet 5
    
    > And we won’t be alone.
    >
    > @thebensams, Engineering Director at @trailofbits the team behind critical bugs, emergency forks, and billion-dollar post-mortems, joins us for the opening cut.
    >
    > https://x.com/i/spaces/1vAxRQZEOqYJl https://twitter.com/RektHQ/status/1960368784952152265
    
    **Links in post:** https://x.com/i/spaces/1vAxRQZEOqYJl, https://twitter.com/RektHQ/status/1960368784952152265
    
    **Quoted post** 1960368784952152265: not readable via the API (deleted, private, or withheld).
    


---

## 2025-08-28 · Post · Looking forward to joining our @nisedo  as he moderates this webinar today. https://twitter.com/summ


### Post — @trailofbits — 2025-08-28 15:37 UTC (2025-08-28 16:37 WAT)

- URL: https://x.com/trailofbits/status/1961090790865928208
- Metrics (at fetch): bookmark 0, impression 2558, like 8, quote 0, reply 1, retweet 0

> Looking forward to joining our @nisedo  as he moderates this webinar today. https://twitter.com/summit_defi/status/1958552046698627362

**Links in post:** https://twitter.com/summit_defi/status/1958552046698627362

**Quoted post (full text):**

    #### Quoted post — @1506671749940850691 — 2025-08-21 15:29 UTC (2025-08-21 16:29 WAT)
    
    - URL: https://x.com/1506671749940850691/status/1958552046698627362
    - Metrics (at fetch): bookmark 1, impression 14494, like 27, quote 8, reply 2, retweet 9
    
    > Join us on Aug 28th at 5PM UTC for a DSS webinar on Automation Security, with:
    > • @0xad1eth (@BrahmaFi) 
    > • @VinyasAlex (@CoWSwap)
    > • @agustincit0x (@mimicfi)
    >
    > We’ll explore security best practices in automated execution and how to make automation easier across DeFi
    >
    > Register ⬇️
    
    **Media:**
    - media `3_1958549045695098880` (details not returned by the API)
    


---

## 2025-08-28 · Post · Most internships = coffee runs and busy work. Our interns work on real problems that outlive their i


### Post — @trailofbits — 2025-08-28 11:07 UTC (2025-08-28 12:07 WAT)

- URL: https://x.com/trailofbits/status/1961022703525122440
- Metrics (at fetch): bookmark 2, impression 4966, like 20, quote 1, reply 1, retweet 0

> Most internships = coffee runs and busy work. Our interns work on real problems that outlive their internship.


---

## 2025-08-27 · Post · Before its prod launch, we used every crowbar in our toolbox to break into @WhatsApp’s Private Proce


Tags (automatic): TEE / enclave


### Post — @trailofbits — 2025-08-27 16:19 UTC (2025-08-27 17:19 WAT)

- URL: https://x.com/trailofbits/status/1960738970150584358
- Metrics (at fetch): bookmark 51, impression 40120, like 135, quote 6, reply 3, retweet 14

> Before its prod launch, we used every crowbar in our toolbox to break into @WhatsApp’s Private Processing TEEs, and starting from a compromised hypervisor gave plenty of leverage. The enclaves yielded to injected ACPI tables, environment variables and evil file names; but now the system is stronger for it.


---

## 2025-08-27 · Post · DeFi users don't have enough info to safely validate their transactions. The $1.5B Bybit hack proves


Tags (automatic): Smart contract / DeFi


### Post — @trailofbits — 2025-08-27 11:44 UTC (2025-08-27 12:44 WAT)

- URL: https://x.com/trailofbits/status/1960669625412161866
- Metrics (at fetch): bookmark 2, impression 2106, like 15, quote 0, reply 1, retweet 1

> DeFi users don't have enough info to safely validate their transactions. The $1.5B Bybit hack proves it.


---

## 2025-08-25 · Post · How do Trail of Bits security engineers spend their free time? 🧵


### Post — @trailofbits — 2025-08-25 11:22 UTC (2025-08-25 12:22 WAT)

- URL: https://x.com/trailofbits/status/1959939314437005600
- Metrics (at fetch): bookmark 5, impression 3876, like 22, quote 0, reply 1, retweet 0

> How do Trail of Bits security engineers spend their free time? 🧵


---

## 2025-08-22 · Post · Companies are monitoring AI systems like traditional apps, but AI attacks work completely differentl


Tags (automatic): AI-assisted hunting


### Post — @trailofbits — 2025-08-22 11:58 UTC (2025-08-22 12:58 WAT)

- URL: https://x.com/trailofbits/status/1958861244032590255
- Metrics (at fetch): bookmark 2, impression 1527, like 3, quote 2, reply 1, retweet 2

> Companies are monitoring AI systems like traditional apps, but AI attacks work completely differently. https://t.co/HyF74V1QLK

**Media:**
- video: https://pbs.twimg.com/ext_tw_video_thumb/1958861211753119744/pu/img/55Pdmpfbcy-VoQfm.jpg — no alt text provided by author


---

## 2025-08-21 · Post · We hacked Gemini CLI, Vertex AI, Assistant, and other AI systems by embedding prompts into images th


Tags (automatic): AI-assisted hunting


### Post — @trailofbits — 2025-08-21 13:38 UTC (2025-08-21 14:38 WAT)

- URL: https://x.com/trailofbits/status/1958524099011002391
- Metrics (at fetch): bookmark 123, impression 57164, like 277, quote 16, reply 8, retweet 56

> We hacked Gemini CLI, Vertex AI, Assistant, and other AI systems by embedding prompts into images that are not visible to users. https://t.co/PN9zGl8fBH

**Media:**
- photo: https://pbs.twimg.com/media/Gy4TSeoXcAEsngr.jpg — no alt text provided by author


---

## 2025-08-20 · Post · Ruby's Marshal deserialization exploits: a fundamental issue dating back over a decade. Learn the hi


### Post — @trailofbits — 2025-08-20 11:09 UTC (2025-08-20 12:09 WAT)

- URL: https://x.com/trailofbits/status/1958124106466882017
- Metrics (at fetch): bookmark 17, impression 4626, like 36, quote 2, reply 1, retweet 10

> Ruby's Marshal deserialization exploits: a fundamental issue dating back over a decade. Learn the history and where we go from here 🧵 https://t.co/JaWxCUhKyr

**Media:**
- photo: https://pbs.twimg.com/media/Gyynf4lW0AEbjVH.jpg — no alt text provided by author


---

## 2025-08-19 · Post · Hackers use Zoom calls to target professionals, hunting for crypto wallets. @dguido breaks down ELUS


### Post — @trailofbits — 2025-08-19 11:15 UTC (2025-08-19 12:15 WAT)

- URL: https://x.com/trailofbits/status/1957763261207576840
- Metrics (at fetch): bookmark 5, impression 1901, like 10, quote 0, reply 2, retweet 3

> Hackers use Zoom calls to target professionals, hunting for crypto wallets. @dguido breaks down ELUSIVE COMET's social engineering on @ClickHereShow
> https://t.co/jRDAJyxCkH https://t.co/gL6CiIuh3C

**Media:**
- video: https://pbs.twimg.com/ext_tw_video_thumb/1957763242714972160/pu/img/HvowI4a4k8VRHhXV.jpg — no alt text provided by author


---

## 2025-08-19 · Post · We won second place in @DARPA's AI Cyber Challenge. Plus, GitHub Copilot prompt injections, NVIDIA T


Tags (automatic): AI-assisted hunting


### Post — @trailofbits — 2025-08-19 11:04 UTC (2025-08-19 12:04 WAT)

- URL: https://x.com/trailofbits/status/1957760550491836783
- Metrics (at fetch): bookmark 31, impression 9314, like 73, quote 0, reply 1, retweet 8

> We won second place in @DARPA's AI Cyber Challenge. Plus, GitHub Copilot prompt injections, NVIDIA Triton vulnerability disclosure, and multi-agent system hijacking demos. Read our AI-packed Tribune: https://mailchi.mp/trailofbits/trail-of-bits-tribune-august

**Links in post:** https://mailchi.mp/trailofbits/trail-of-bits-tribune-august


---

## 2025-08-14 · Post · As part of the @Gemini Wallet ecosystem, we conducted a security review of the newly launched Gemini


Tags (automatic): AI-assisted hunting


### Post — @trailofbits — 2025-08-14 20:00 UTC (2025-08-14 21:00 WAT)

- URL: https://x.com/trailofbits/status/1956083544385523979
- Metrics (at fetch): bookmark 0, impression 2143, like 11, quote 0, reply 1, retweet 1

> As part of the @Gemini Wallet ecosystem, we conducted a security review of the newly launched Gemini Wallet 🧵 https://t.co/0I819zX8IF

**Media:**
- photo: https://pbs.twimg.com/media/GyVnnggXcAIKY-x.jpg — no alt text provided by author


---

## 2025-08-14 · Post · Principal AppSec engineer, Artur Cygan, explains why fuzzing has become one of the most successful a


### Post — @trailofbits — 2025-08-14 12:22 UTC (2025-08-14 13:22 WAT)

- URL: https://x.com/trailofbits/status/1955968197183582621
- Metrics (at fetch): bookmark 5, impression 1504, like 12, quote 0, reply 1, retweet 1

> Principal AppSec engineer, Artur Cygan, explains why fuzzing has become one of the most successful automated security tools on @SecWeekly #336.
> https://t.co/S8tsBW6oWC https://t.co/iIOMwEMZbh

**Media:**
- video: https://pbs.twimg.com/ext_tw_video_thumb/1955968157186686982/pu/img/qLV0eMPaiDqTSvqP.jpg — no alt text provided by author


---

## 2025-08-09 · Post · Buttercup won the $3M second prize at DARPA's AIxCC. We found 28 vulnerabilities across 20 CWEs with


Tags (automatic): AI-assisted hunting


### Post — @trailofbits — 2025-08-09 21:01 UTC (2025-08-09 22:01 WAT)

- URL: https://x.com/trailofbits/status/1954286988615438474
- Metrics (at fetch): bookmark 20, impression 11709, like 134, quote 3, reply 2, retweet 15

> Buttercup won the $3M second prize at DARPA's AIxCC. We found 28 vulnerabilities across 20 CWEs with 90% accuracy at just $181/point, achieving this with exclusively non-reasoning LLMs. https://t.co/CG6TwVLPU5

**Media:**
- photo: https://pbs.twimg.com/media/Gx8EY3jWgAAUbFl.jpg — no alt text provided by author


---

## 2025-08-09 · Post · If you're @DEFCON, join our team today at 4:00 pm - 4:30 pm AIxCC Stage Talk: "Building Buttercup" a


Tags (automatic): AI-assisted hunting


### Post — @trailofbits — 2025-08-09 17:28 UTC (2025-08-09 18:28 WAT)

- URL: https://x.com/trailofbits/status/1954233214219739152
- Metrics (at fetch): bookmark 3, impression 2510, like 23, quote 0, reply 0, retweet 4

> If you're @DEFCON, join our team today at 4:00 pm - 4:30 pm AIxCC Stage Talk: "Building Buttercup" as we share our experience developing Buttercup, what worked, what didn't, and lessons learned from competing in @DARPA's AI Cyber Challenge. https://t.co/mH8qCdDQDF


---

## 2025-08-08 · Post · We won second place in @DARPA's AIxCC with Buttercup! Our CRS is now open source for everyone to use


### Post — @trailofbits — 2025-08-08 19:24 UTC (2025-08-08 20:24 WAT)

- URL: https://x.com/trailofbits/status/1953900255197770002
- Metrics (at fetch): bookmark 34, impression 18097, like 249, quote 7, reply 7, retweet 44

> We won second place in @DARPA's AIxCC with Buttercup! Our CRS is now open source for everyone to use. https://t.co/YWPyiZsMDv

**Media:**
- photo: https://pbs.twimg.com/media/Gx2l425WMAAjuGE.jpg — no alt text provided by author


---

## 2025-08-08 · Post · 11 Trail of Bits engineers spent 2+ years building Buttercup. After the announcement, the code will 


### Post — @trailofbits — 2025-08-08 13:49 UTC (2025-08-08 14:49 WAT)

- URL: https://x.com/trailofbits/status/1953815715544269280
- Metrics (at fetch): bookmark 22, impression 11707, like 83, quote 0, reply 0, retweet 10

> 11 Trail of Bits engineers spent 2+ years building Buttercup. After the announcement, the code will be open-sourced! Not at @DEFCON? Follow @dguido for live updates. https://t.co/4OCuuQ18Wj

**Quoted post (full text):**

    #### Quoted post — @54645160 — 2025-08-04 20:17 UTC (2025-08-04 21:17 WAT)
    
    - URL: https://x.com/54645160/status/1952463984038121731
    - Metrics (at fetch): bookmark 28, impression 33892, like 113, quote 11, reply 37, retweet 50
    
    > We’ll announce the results and winners of the 
    > DARPA AI Cyber Challenge (AIxCC) on Friday at 
    > DEF CON 33. For more on the challenge, the teams, and the AIxCC Experience at the event, visit: https://t.co/L6S9zw3Bth. https://t.co/ATrW5O7UzM
    
    **Media:**
    - media `7_1952463874013196288` (details not returned by the API)
    


---

## 2025-08-07 · Post · Seven teams, two years, $4M prize. Meet the teams that competed in @DARPA's AI Cyber Challenge. http


Tags (automatic): AI-assisted hunting


### Post — @trailofbits — 2025-08-07 19:50 UTC (2025-08-07 20:50 WAT)

- URL: https://x.com/trailofbits/status/1953544360127033671
- Metrics (at fetch): bookmark 4, impression 5504, like 34, quote 1, reply 2, retweet 2

> Seven teams, two years, $4M prize. Meet the teams that competed in @DARPA's AI Cyber Challenge. https://t.co/c4IvrgqHaM

**Media:**
- photo: https://pbs.twimg.com/media/GxxiPipX0AA1Hc-.jpg — no alt text provided by author


---

## 2025-08-06 · Post · Prompt injection dominates AI security discussions, but little public research exists on writing pow


Tags (automatic): AI-assisted hunting


### Post — @trailofbits — 2025-08-06 19:29 UTC (2025-08-06 20:29 WAT)

- URL: https://x.com/trailofbits/status/1953176705230639465
- Metrics (at fetch): bookmark 66, impression 16119, like 109, quote 1, reply 1, retweet 19

> Prompt injection dominates AI security discussions, but little public research exists on writing powerful, discreet, and reliable exploits until now 🧵


---

## 2025-08-05 · Post · A wild Buttercup appears! Our @DARPA AI Cyber Challenge CRS is in the @BSidesLV Silent Auction. Bid 


Tags (automatic): AI-assisted hunting


### Post — @trailofbits — 2025-08-05 17:45 UTC (2025-08-05 18:45 WAT)

- URL: https://x.com/trailofbits/status/1952788088024920466
- Metrics (at fetch): bookmark 2, impression 2077, like 12, quote 0, reply 0, retweet 3

> A wild Buttercup appears! Our @DARPA AI Cyber Challenge CRS is in the @BSidesLV Silent Auction. Bid on this encrypted limited edition! https://t.co/dCKZIwjCKC

**Media:**
- photo: https://pbs.twimg.com/media/GxmyatDWYAALFiU.jpg — no alt text provided by author


---

## 2025-08-05 · Thread · Today, we’re disclosing two 9.8 CVSS memory corruption vulnerabilities in the @NVIDIA Triton Inferen


Tags (automatic): RCE, Memory corruption / native, AI-assisted hunting


### Post — @trailofbits — 2025-08-05 11:32 UTC (2025-08-05 12:32 WAT)

- URL: https://x.com/trailofbits/status/1952694252338544804
- Metrics (at fetch): bookmark 18, impression 14198, like 89, quote 3, reply 1, retweet 17

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

## 2025-08-04 · Post · We're at @BSidesLV today kicking off Hacker Summer Camp! This week: @BlackHatEvents, then @DEFCON, w


Tags (automatic): AI-assisted hunting


### Post — @trailofbits — 2025-08-04 15:29 UTC (2025-08-04 16:29 WAT)

- URL: https://x.com/trailofbits/status/1952391332942516250
- Metrics (at fetch): bookmark 1, impression 1170, like 4, quote 0, reply 1, retweet 0

> We're at @BSidesLV today kicking off Hacker Summer Camp! This week: @BlackHatEvents, then @DEFCON, where @DARPA will announce the AI Cyber Challenge results for our autonomous system, Buttercup. https://t.co/1HVgvrzHUq


---

## 2025-08-01 · Post · Our founder @dguido went from being banned from his high school's computers to founding Trail of Bit


### Post — @trailofbits — 2025-08-01 14:38 UTC (2025-08-01 15:38 WAT)

- URL: https://x.com/trailofbits/status/1951291482276552770
- Metrics (at fetch): bookmark 5, impression 6268, like 59, quote 2, reply 6, retweet 7

> Our founder @dguido went from being banned from his high school's computers to founding Trail of Bits. Now he's established a $2,500 scholarship at Mineola HS to celebrate students who push boundaries and explore tech beyond the curriculum. https://t.co/FttUXn7eo6


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

## 2025-07-29 · Post · Learn about the latest MCP security advancements and new security tools today at our webinar "MCP Se


### Post — @trailofbits — 2025-07-29 15:41 UTC (2025-07-29 16:41 WAT)

- URL: https://x.com/trailofbits/status/1950220119872868536
- Metrics (at fetch): bookmark 1, impression 1465, like 11, quote 0, reply 0, retweet 2

> Learn about the latest MCP security advancements and new security tools today at our webinar "MCP Security Deep Dive: From Attacks to Defense" at 1:00 PM ET. https://t.co/Y8N2AIsT9a https://t.co/r2CNvDxMO8

**Media:**
- photo: https://pbs.twimg.com/media/GxCS3TYWMAAvwhi.jpg — no alt text provided by author


---

## 2025-07-28 · Post · NEW TOOL: context-protector proxies and sanitizes MCP server communications to block prompt injectio


### Post — @trailofbits — 2025-07-28 16:29 UTC (2025-07-28 17:29 WAT)

- URL: https://x.com/trailofbits/status/1949869829214687709
- Metrics (at fetch): bookmark 21, impression 5161, like 34, quote 4, reply 3, retweet 8

> NEW TOOL: context-protector proxies and sanitizes MCP server communications to block prompt injection through tool descriptions, server instructions, and ANSI sequences. https://t.co/CSNVxuvIIo https://t.co/VtK9JTyp8r

**Media:**
- photo: https://pbs.twimg.com/media/Gw9URp4XUAIKHR6.jpg — no alt text provided by author


---

## 2025-07-25 · Post · End-of-life network devices become perfect attack targets due to unpatched vulnerabilities frozen in


### Post — @trailofbits — 2025-07-25 15:24 UTC (2025-07-25 16:24 WAT)

- URL: https://x.com/trailofbits/status/1948766257643184239
- Metrics (at fetch): bookmark 2, impression 4282, like 10, quote 2, reply 1, retweet 1

> End-of-life network devices become perfect attack targets due to unpatched vulnerabilities frozen in time like fossils. We proved this in @DistrictCon's Junkyard competition ⬇️


---

## 2025-07-24 · Post · New Trail of Bits Tribune: Our AIxCC finals submission, how we exposed critical flaws in Go's built-


Tags (automatic): Auth bypass


### Post — @trailofbits — 2025-07-24 11:11 UTC (2025-07-24 12:11 WAT)

- URL: https://x.com/trailofbits/status/1948340136275488925
- Metrics (at fetch): bookmark 13, impression 6905, like 30, quote 0, reply 0, retweet 7

> New Trail of Bits Tribune: Our AIxCC finals submission, how we exposed critical flaws in Go's built-in parsers that can enable authentication bypass and data exfiltration from production systems, and 14 new security reviews. https://t.co/vK99FUiSUK


---

## 2025-07-23 · Post · Pick the brains of AI/ML security leaders in Vegas. We're raffling off 6 spots to join us for lunch 


Tags (automatic): AI-assisted hunting


### Post — @trailofbits — 2025-07-23 18:16 UTC (2025-07-23 19:16 WAT)

- URL: https://x.com/trailofbits/status/1948084869084418252
- Metrics (at fetch): bookmark 0, impression 1426, like 1, quote 0, reply 1, retweet 0

> Pick the brains of AI/ML security leaders in Vegas. We're raffling off 6 spots to join us for lunch on August 4 @BSidesLV


---

## 2025-07-21 · Post · TOOL RELEASE: Detect plagiarized code even when variable names change and comments disappear. Vendet


### Post — @trailofbits — 2025-07-21 12:42 UTC (2025-07-21 13:42 WAT)

- URL: https://x.com/trailofbits/status/1947275960459362392
- Metrics (at fetch): bookmark 21, impression 13861, like 80, quote 2, reply 0, retweet 25

> TOOL RELEASE: Detect plagiarized code even when variable names change and comments disappear. Vendetect uses semantic fingerprinting to catch copied code that traditional tools miss. https://t.co/68HfWUrcCU


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

## 2025-04-24 · Thread · MCP Vulnerability: AI systems can be manipulated to silently leak your entire conversation history t


Tags (automatic): AI-assisted hunting


### Post — @trailofbits — 2025-04-24 15:46 UTC (2025-04-24 16:46 WAT)

- URL: https://x.com/trailofbits/status/1915432077727600917
- Metrics (at fetch): bookmark 82, impression 22399, like 171, quote 8, reply 5, retweet 38

> MCP Vulnerability: AI systems can be manipulated to silently leak your entire conversation history to malicious servers. https://t.co/teuv0KYOs1

**Media:**
- photo: https://pbs.twimg.com/media/GpT7UuAWgAEdeRe.jpg — no alt text provided by author


### Thread part 2 — @trailofbits — 2025-04-24 15:52 UTC (2025-04-24 16:52 WAT)

- URL: https://x.com/trailofbits/status/1915433668220510236
- Metrics (at fetch): bookmark 8, impression 2014, like 21, quote 0, reply 1, retweet 5

> Why is this attack better than noisy shell exploits? It's stealthy, can persist long-term, and attackers can customize triggers for high-value targets—looking for account numbers at banks, AWS keys at tech firms, or classified government codes. https://t.co/9EdNHRaEP7


---

## 2025-04-18 · Thread · Coming to PyCA Cryptography—a new Rust-powered ASN.1 API that reduces parser differentials while giv


### Post — @trailofbits — 2025-04-18 13:20 UTC (2025-04-18 14:20 WAT)

- URL: https://x.com/trailofbits/status/1913220972888408419
- Metrics (at fetch): bookmark 0, impression 1354, like 8, quote 0, reply 1, retweet 1

> Coming to PyCA Cryptography—a new Rust-powered ASN.1 API that reduces parser differentials while giving you clean Python syntax and native-speed parsing. https://t.co/t1UH6Y1gJa

**Media:**
- photo: https://pbs.twimg.com/media/Go0gVhOXQAAxEg7.jpg — no alt text provided by author


### Thread part 2 — @trailofbits — 2025-04-18 13:20 UTC (2025-04-18 14:20 WAT)

- URL: https://x.com/trailofbits/status/1913221124969902389
- Metrics (at fetch): bookmark 1, impression 1105, like 6, quote 0, reply 0, retweet 1

> Why does Python need this? Most devs aren't working with ASN.1 daily, but many need custom encoding beyond standard X.509. Think extracting DER-encoded values from X.509 certs like sigstore custom extensions
> https://t.co/44WHvzhMD9


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

## 2024-06-11 · Thread · We’ve developed a new ML model attack technique, Sleepy Pickle, that exploits weaknesses in Pickle f


### Post — @trailofbits — 2024-06-11 13:01 UTC (2024-06-11 14:01 WAT)

- URL: https://x.com/trailofbits/status/1800513566958620708
- Metrics (at fetch): bookmark 24, impression 11703, like 60, quote 2, reply 1, retweet 15

> We’ve developed a new ML model attack technique, Sleepy Pickle, that exploits weaknesses in Pickle files used to distribute ML models. Learn how this attack can compromise ML models / their users and how you can reduce your risk. 
> https://t.co/3BG7eDiNq4


### Thread part 2 — @trailofbits — 2024-06-11 13:01 UTC (2024-06-11 14:01 WAT)

- URL: https://x.com/trailofbits/status/1800513568376308095
- Metrics (at fetch): bookmark 0, impression 1187, like 3, quote 0, reply 0, retweet 0

> Stay tuned later today for Sticky Pickle, a variant of Sleepy Pickle that incorporates a self-replicating mechanism, enabling long-lasting presence on compromised systems while evading detection.


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

## 2024-05-17 · Thread · Advanced expertise in ZK circuits. 


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


### Thread part 2 — @trailofbits — 2024-05-17 13:01 UTC (2024-05-17 14:01 WAT)

- URL: https://x.com/trailofbits/status/1791453896130347227
- Metrics (at fetch): bookmark 0, impression 979, like 1, quote 0, reply 0, retweet 0

> @Scroll_ZKP Our team has the practical and theoretical experience to help you build your ZK system securely. Contact us to learn more! https://t.co/eo8sF63bwc


---

## 2024-05-16 · Thread · Our contributions to the LLVM project have improved AddressSanitizer's (ASan) bug detection capabili


### Post — @trailofbits — 2024-05-16 13:05 UTC (2024-05-16 14:05 WAT)

- URL: https://x.com/trailofbits/status/1791092495067070588
- Metrics (at fetch): bookmark 13, impression 9197, like 44, quote 4, reply 1, retweet 10

> Our contributions to the LLVM project have improved AddressSanitizer's (ASan) bug detection capabilities. Bootstrap ASan to better protect codebases against memory issues.  https://buff.ly/44Gm3BP [pic.x.com/pmJFu2mxv6]

**Media:**
- photo: https://pbs.twimg.com/media/GNs9IcwWMAA0C1u.jpg — no alt text provided by author

**Links in post:** https://buff.ly/44Gm3BP


### Thread part 2 — @trailofbits — 2024-05-16 13:05 UTC (2024-05-16 14:05 WAT)

- URL: https://x.com/trailofbits/status/1791092496757375328
- Metrics (at fetch): bookmark 0, impression 1185, like 1, quote 0, reply 0, retweet 0

> If you need help with ASan annotations, fuzzing, or anything related to LLVM, contact us! We are happy to help tailor sanitizers or other LLVM tools to your specific needs. http://www.trailofbits.com/contact

**Links in post:** http://www.trailofbits.com/contact


---

## 2024-04-30 · Thread · Developing invariants with Curvance. Over 9 weeks, we wrote and tested 216 invariants, uncovering 13


### Post — @trailofbits — 2024-04-30 13:39 UTC (2024-04-30 14:39 WAT)

- URL: https://x.com/trailofbits/status/1785302839721439457
- Metrics (at fetch): bookmark 29, impression 12413, like 61, quote 4, reply 1, retweet 15

> Developing invariants with Curvance. Over 9 weeks, we wrote and tested 216 invariants, uncovering 13 critical findings while pushing the limits of our tools. https://t.co/rCCEe12fbx


### Thread part 2 — @trailofbits — 2024-04-30 13:39 UTC (2024-04-30 14:39 WAT)

- URL: https://x.com/trailofbits/status/1785302840971284689
- Metrics (at fetch): bookmark 1, impression 1392, like 10, quote 0, reply 0, retweet 3

> The Curvance engagement pushed our tools like Echidna, Medusa, and CloudExec to their limits, leading to significant enhancements. From improved trace printing to corpus preservation, our tools evolved to meet the project's challenges. https://t.co/rIVNasA7QR


---

## 2024-03-25 · Thread · Presenting our paper "Weak Fiat-Shamir Attacks on Modern Proof Systems," a collaboration with @Quang


Tags (automatic): ZK


### Post — @trailofbits — 2024-03-25 15:16 UTC (2024-03-25 16:16 WAT)

- URL: https://x.com/trailofbits/status/1772281304316600658
- Metrics (at fetch): bookmark 9, impression 6166, like 36, quote 1, reply 1, retweet 13

> Presenting our paper "Weak Fiat-Shamir Attacks on Modern Proof Systems," a collaboration with @QuangVDao & @pag_crypto from @CarnegieMellon, @RealWorldCrypto this Wednesday. Let's look at some critical vulnerabilities that we found as part of that research https://eprint.iacr.org/2023/691

**Media:**
- photo: https://pbs.twimg.com/media/GJhoBrSbsAAKotg.png — no alt text provided by author
- photo: https://pbs.twimg.com/media/GJhoU11aAAAjuHn.jpg — no alt text provided by author

**Links in post:** https://eprint.iacr.org/2023/691


### Thread part 2 — @trailofbits — 2024-03-25 15:16 UTC (2024-03-25 16:16 WAT)

- URL: https://x.com/trailofbits/status/1772281306623201523
- Metrics (at fetch): bookmark 1, impression 831, like 1, quote 0, reply 1, retweet 0

> We found one such critical Fiat-Shamir vulnerability in a live system with millions of dollars at risk: incognito chain. They use the ZKP system Bulletproofs, which had a mistake in its original version that specified an insecure Fiat-Shamir transformation.https://blog.trailofbits.com/2023/08/02/a-mistake-in-the-bulletproofs-paper-could-have-led-to-the-theft-of-millions-of-dollars/

**Links in post:** https://blog.trailofbits.com/2023/08/02/a-mistake-in-the-bulletproofs-paper-could-have-led-to-the-theft-of-millions-of-dollars/


### Thread part 3 — @trailofbits — 2024-03-25 15:16 UTC (2024-03-25 16:16 WAT)

- URL: https://x.com/trailofbits/status/1772281308330209700
- Metrics (at fetch): bookmark 0, impression 786, like 1, quote 0, reply 1, retweet 0

> While still in the testnet phase, we found a critical vulnerability affecting Dusk Network’s Plonk implementation that uses ZKPs to achieve confidential transactions. This vulnerability could be exploited to mint yourself free money.


### Thread part 4 — @trailofbits — 2024-03-25 15:16 UTC (2024-03-25 16:16 WAT)

- URL: https://x.com/trailofbits/status/1772281310381539680
- Metrics (at fetch): bookmark 0, impression 993, like 2, quote 1, reply 1, retweet 0

> We found a critical vulnerability affecting the Plonk implementation of SnarkJS, the underlying ZKP implementation that powers Circom. When the vulnerability was discovered, Circom supported only the Groth16 backend in SnarkJS, not Plonk, making Circom apps immune to the attack.


### Thread part 5 — @trailofbits — 2024-03-25 15:16 UTC (2024-03-25 16:16 WAT)

- URL: https://x.com/trailofbits/status/1772281312159949271
- Metrics (at fetch): bookmark 0, impression 934, like 1, quote 0, reply 0, retweet 0

> If you would like help designing or troubleshooting these kinds of systems, schedule an office hours session with our cryptography team where you can receive free technical help, no strings attached. https://share.hsforms.com/1gcBB5lwtRzaAV1D-PEV7oAdffjk

**Links in post:** https://share.hsforms.com/1gcBB5lwtRzaAV1D-PEV7oAdffjk


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

## 2024-01-29 · Thread · Warning: @lfgexchange  is falsely claiming to have worked with us on an audit. The report on their p


### Post — @trailofbits — 2024-01-29 23:21 UTC (2024-01-30 00:21 WAT)

- URL: https://x.com/trailofbits/status/1752109824282910869
- Metrics (at fetch): bookmark 13, impression 87160, like 170, quote 14, reply 8, retweet 37

> Warning: @lfgexchange  is falsely claiming to have worked with us on an audit. The report on their page is fake. If you want to verify the authenticity of a @trailofbits report, find it on our publications repo, the authoritative source straight from us. https://github.com/trailofbits/publications?tab=readme-ov-file#security-reviews [pic.x.com/c2sT5xM1T1]

**Media:**
- photo: https://pbs.twimg.com/media/GFC92kUbsAAvuiO.png — no alt text provided by author

**Links in post:** https://github.com/trailofbits/publications?tab=readme-ov-file#security-reviews


### Thread part 2 — @trailofbits — 2024-01-29 23:21 UTC (2024-01-30 00:21 WAT)

- URL: https://x.com/trailofbits/status/1752109825864176096
- Metrics (at fetch): bookmark 0, impression 4203, like 20, quote 0, reply 4, retweet 1

> LFG is also claiming to have worked with @osec_io. Can anyone from @osec_io chime in?


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

## 2023-08-31 · Thread · The @OpenSSF's Security Software Repositories WG has been instrumental in improving package index se


Tags (automatic): AI-assisted hunting


### Post — @trailofbits — 2023-08-31 16:01 UTC (2023-08-31 17:01 WAT)

- URL: https://x.com/trailofbits/status/1697278331173966081
- Metrics (at fetch): bookmark 2, impression 5803, like 14, quote 1, reply 1, retweet 4

> The @OpenSSF's Security Software Repositories WG has been instrumental in improving package index security, and we've been honored to help them build many of their key initiatives!
>
> Read their post here https://t.co/OKUiTk3zsa, and read on for our specific contributions 🧵:


### Thread part 2 — @trailofbits — 2023-08-31 16:01 UTC (2023-08-31 17:01 WAT)

- URL: https://x.com/trailofbits/status/1697278332474171409
- Metrics (at fetch): bookmark 0, impression 64, like 1, quote 0, reply 1, retweet 0

> In April, we helped PyPI develop Trusted Publishing, a new, more secure way to publish packages from CI platforms to package indices! It's now being used to secure hundreds of critical PyPI packages, and enrollment is growing.
>
> Learn more on our blog: https://t.co/vpYawnsUsr


### Thread part 3 — @trailofbits — 2023-08-31 16:01 UTC (2023-08-31 17:01 WAT)

- URL: https://x.com/trailofbits/status/1697278334038679578
- Metrics (at fetch): bookmark 0, impression 826, like 1, quote 0, reply 1, retweet 0

> Coming up next: we've been working with the OpenSSF on a proposal to add build provenance to Homebrew, the dominant package manager for macOS.


### Thread part 4 — @trailofbits — 2023-08-31 16:01 UTC (2023-08-31 17:01 WAT)

- URL: https://x.com/trailofbits/status/1697278335686967773
- Metrics (at fetch): bookmark 0, impression 836, like 1, quote 0, reply 0, retweet 0

> Build provenance will give millions of Homebrew users increased confidence in the integrity of Homebrew's software distributions, with knock-on benefits for countless software packages developed primarily on macOS! Check out the proposal here: https://t.co/No2cBtGIjo


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

## 2023-07-18 · Thread · How will AI affect national security? In our responses to an RFI by the White House's OTSP, we highl


Tags (automatic): AI-assisted hunting


### Post — @trailofbits — 2023-07-18 19:57 UTC (2023-07-18 20:57 WAT)

- URL: https://x.com/trailofbits/status/1681392695330078750
- Metrics (at fetch): bookmark 1, impression 5930, like 20, quote 1, reply 1, retweet 6

> How will AI affect national security? In our responses to an RFI by the White House's OTSP, we highlight a few key points 🧵: https://t.co/gcQ4n2pDim


### Thread part 2 — @trailofbits — 2023-07-18 19:57 UTC (2023-07-18 20:57 WAT)

- URL: https://x.com/trailofbits/status/1681392697104388096
- Metrics (at fetch): bookmark 0, impression 452, like 1, quote 0, reply 1, retweet 0

> To reduce the systemic risks AI-based systems may introduce, we need to construct precise, verifiable claims about AI and hold developers accountable to them. https://t.co/1wPfgVnQJC

**Media:**
- photo: https://pbs.twimg.com/media/F1WAtHsXgAAuuMn.png — no alt text provided by author


### Thread part 3 — @trailofbits — 2023-07-18 19:57 UTC (2023-07-18 20:57 WAT)

- URL: https://x.com/trailofbits/status/1681392698836516885
- Metrics (at fetch): bookmark 1, impression 1441, like 4, quote 0, reply 1, retweet 0

> When identifying security risks or developing code, AI should complement, not replace, human methods. AI is poorly suited to perform these tasks alone. https://t.co/mufj0zvNI4

**Media:**
- photo: https://pbs.twimg.com/media/F1WA7dYWYAAgqG9.jpg — no alt text provided by author


### Thread part 4 — @trailofbits — 2023-07-18 19:57 UTC (2023-07-18 20:57 WAT)

- URL: https://x.com/trailofbits/status/1681392700778479620
- Metrics (at fetch): bookmark 0, impression 1294, like 1, quote 0, reply 0, retweet 0

> AI presents a systemic risk to existing defenses. AI can make it far easier to perform attacks, write or customize exploits, and craft phishing messages. https://t.co/l7VxffEL3d

**Media:**
- photo: https://pbs.twimg.com/media/F1WBnZuWAAwDHHi.jpg — no alt text provided by author


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

## 2022-10-25 · Thread · Earlier this year, one of our interns found a vulnerability that affects applications using the SQLi


### Post — @trailofbits — 2022-10-25 11:30 UTC (2022-10-25 12:30 WAT)

- URL: https://x.com/trailofbits/status/1584870065698136064
- Metrics (at fetch): bookmark 59, impression 0, like 296, quote 8, reply 6, retweet 92

> Earlier this year, one of our interns found a vulnerability that affects applications using the SQLite library API. We are publicly disclosing that vuln today. https://t.co/vDsZKqvsoi


### Thread part 2 — @trailofbits — 2022-10-25 11:34 UTC (2022-10-25 12:34 WAT)

- URL: https://x.com/trailofbits/status/1584871094577762304
- Metrics (at fetch): bookmark 0, impression 0, like 13, quote 1, reply 1, retweet 2

> Our strange journey to finding the vuln started with a vulnerability in PHP that seemed like the perfect candidate for a variant analysis. So then we dove into SQLite string formatting: https://t.co/vDsZKqvsoi


### Thread part 3 — @trailofbits — 2022-10-25 11:36 UTC (2022-10-25 12:36 WAT)

- URL: https://x.com/trailofbits/status/1584871516759531520
- Metrics (at fetch): bookmark 0, impression 0, like 11, quote 0, reply 1, retweet 2

> SQLite is the most widely deployed database engine, thanks to its very permissive licensing and portable design. It seems to be used everywhere—a perception that was reinforced when we tripped right over this vulnerability while hunting for bugs elsewhere. https://t.co/vDsZKqvsoi


### Thread part 4 — @trailofbits — 2022-10-25 11:39 UTC (2022-10-25 12:39 WAT)

- URL: https://x.com/trailofbits/status/1584872192180895745
- Metrics (at fetch): bookmark 2, impression 0, like 26, quote 2, reply 1, retweet 7

> Although this bug may be difficult to reach in deployed applications, it's an example of a vuln that is made easier to exploit by “divergent representations” that result from applying compiler optimizations to undefined behavior. https://t.co/vDsZKqvsoi


### Thread part 5 — @trailofbits — 2022-10-25 11:41 UTC (2022-10-25 12:41 WAT)

- URL: https://x.com/trailofbits/status/1584872744176451585
- Metrics (at fetch): bookmark 0, impression 0, like 11, quote 1, reply 1, retweet 4

> Not every system or application that uses the SQLite printf functions is vulnerable. For those that are, CVE-2022-35737 is a critical bug. We would like to thank the teams at SQLite and CERT/CC for working swiftly with us to address these issues. https://t.co/vDsZKqvsoi


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

## 2021-12-21 · Thread · We found critical flaws in common TSS libraries, a cryptographic protocol for distributed key genera


Tags (automatic): ZK


### Post — @trailofbits — 2021-12-21 13:57 UTC (2021-12-21 14:57 WAT)

- URL: https://x.com/trailofbits/status/1473291464264269826
- Metrics (at fetch): bookmark 34, impression 0, like 178, quote 13, reply 6, retweet 56

> We found critical flaws in common TSS libraries, a cryptographic protocol for distributed key generation and signing. We’ve released https://ZKDocs.com to help secure the rapidly advancing field of ZKPs, TSS, and similar schemes. https://blog.trailofbits.com/2021/12/21/disclosing-shamirs-secret-sharing-vulnerabilities-and-announcing-zkdocs/

**Links in post:** https://ZKDocs.com, https://blog.trailofbits.com/2021/12/21/disclosing-shamirs-secret-sharing-vulnerabilities-and-announcing-zkdocs/


### Thread part 2 — @trailofbits — 2021-12-21 14:13 UTC (2021-12-21 15:13 WAT)

- URL: https://x.com/trailofbits/status/1473295626792230912
- Metrics (at fetch): bookmark 5, impression 0, like 33, quote 2, reply 1, retweet 5

> Todays vulnerability release helps describe threshold signature schemes (TSS) and verifiable secret sharing (VSS) for new readers. Fun fact, aside from academic pubs about them, there is virtually no guidance for implementing them securely! (Until ZKDocs). https://blog.trailofbits.com/2021/12/21/disclosing-shamirs-secret-sharing-vulnerabilities-and-announcing-zkdocs/

**Links in post:** https://blog.trailofbits.com/2021/12/21/disclosing-shamirs-secret-sharing-vulnerabilities-and-announcing-zkdocs/


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

## 2018-01-17 · Thread · Working on an audit for the @RSKsmart blockchain platform was one of the most fun projects we had la


Tags (automatic): Blockchain / L1-L2 / bridge


### Post — @trailofbits — 2018-01-17 18:22 UTC (2018-01-17 19:22 WAT)

- URL: https://x.com/trailofbits/status/953693965164871683
- Metrics (at fetch): bookmark 0, impression 0, like 20, quote 1, reply 1, retweet 7

> Working on an audit for the @RSKsmart blockchain platform was one of the most fun projects we had last quarter. See the results from that work on their blog! https://x.com/julianor/status/953648290062618625

**Links in post:** https://x.com/julianor/status/953648290062618625

**Quoted post (full text):**

    #### Quoted post — @16845633 — 2018-01-17 15:20 UTC (2018-01-17 16:20 WAT)
    
    - URL: https://x.com/16845633/status/953648290062618625
    - Metrics (at fetch): bookmark 0, impression 0, like 17, quote 1, reply 0, retweet 6
    
    > audit of RSKj (Bitcoin sidechain with EVM smart contracts) by @trailofbits @paddyucl @socrates1024  #BugBounty hints maybe? https://t.co/cMBvP3vAIp https://t.co/2efUnD2fPX
    
    **Quoted post** 953645634422231040: not readable via the API (deleted, private, or withheld).
    


### Thread part 2 — @trailofbits — 2018-01-17 18:24 UTC (2018-01-17 19:24 WAT)

- URL: https://x.com/trailofbits/status/953694521895813120
- Metrics (at fetch): bookmark 0, impression 0, like 5, quote 0, reply 0, retweet 0

> @RSKsmart Here are direct links to RSK's announcement and our results:
> https://media.rsk.co/rsk-security-audit-results/
> https://www.trailofbits.com/reports/RSKj.pdf

**Links in post:** https://media.rsk.co/rsk-security-audit-results/, https://www.trailofbits.com/reports/RSKj.pdf


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
