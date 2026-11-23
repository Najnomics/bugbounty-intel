# @bluethroat_labs — full verbatim X archive (security-relevant posts)

_Generated 2026-11-23 from the X API (full-archive search + timeline). Every post below is copied word-for-word; t.co links are expanded; quoted posts are inlined in full; media are listed with alt text when the author provided it. Posts are grouped by conversation (a thread = the author's root post followed by their own replies, oldest first). Groups are newest first. An agent without X access can rely on this file._

- Posts in this file: 147
- Conversations/threads: 59
- Oldest post captured: 2025-12-02
- Newest post captured: 2026-11-11


---

## 2026-11-11 · Post · "We use TEEs" is not a security guarantee.


Tags (automatic): TEE / enclave


### Post — @bluethroat_labs — 2026-11-11 14:47 UTC (2026-11-11 15:47 WAT)

- URL: https://x.com/bluethroat_labs/status/2120528783673299290
- Metrics (at fetch): bookmark 6, impression 644, like 14, quote 0, reply 0, repost 3

> "We use TEEs" is not a security guarantee.
>
> Two teams can both run TEEs and offer wildly different protection. The details are where it breaks.
>
> 4 things we check every time:
>
> 1. Physical access changes everything
> If your adversary can touch the machine, we treat the TEE as compromised. Published attacks like http://TEE.fail are why. Whoever hosts your hardware is in your threat model.
>
> 2. Attestation doesn't mean your code is safe
> A TEE will faithfully run vulnerable code. Bug in the inference engine or a dependency? Data can leak without anyone breaking the hardware isolation.
> The code inside the boundary needs review too.
>
> 3. Attestation is evidence. Your verifier makes the call.
> Authenticate the report. Validate the collateral. Check identity and measurements. Enforce a real policy on platform security status. Then bind that decision to the endpoint actually receiving your data.
> Importing an attestation library does none of this for you.
>
> 4. Is the audited code the code that's running?
> Open source is a start. You still need a verifiable link from source → build → attested measurement. Reproducible builds get you there. Without that, "audited" and "attested" can be describing two different things.
>
> Real example from our Phala/dstack research:
> CPU evidence was cryptographically verified. GPU evidence was fetched, parsed as JSON, and shown under "TEE Hardware Verified" with no GPU crypto checks.
> The GPU claim had no cryptographic backing. That path has since been fixed.
> https://bluethroatlabs.com/reveries/phala-cloud-gpu-attestation-fake-verified-no-cryptography
>
> Inference providers are under attack. Securing the hardware boundary is one layer of securing the service.
>
> More real failures and practical checks in our TEE Security Handbook:
> https://tee-security-handbook.bluethroatlabs.com/
>
> https://x.com/ilblackdragon/status/2120092118349729863

**Links in post:** https://x.com/ilblackdragon/status/2120092118349729863, http://TEE.fail, https://bluethroatlabs.com/reveries/phala-cloud-gpu-attestation-fake-verified-no-cryptography, https://tee-security-handbook.bluethroatlabs.com/

**Quoted post (full text):**

    #### Quoted post — @ilblackdragon — 2026-11-10 09:52 UTC (2026-11-10 10:52 WAT)
    
    - URL: https://x.com/ilblackdragon/status/2120092118349729863
    - Metrics (at fetch): bookmark 84, impression 48260, like 587, quote 18, reply 87, repost 82
    
    > Inference providers are under attack. 
    >
    > AI inference is now playing a critical role and is a honey pot of data and ability to inject actions back into users devices via agents for malicious actors.
    >
    > NEAR AI thwarted a series of attacks on its systems and is back to normal. NEAR Protocol, Intents and other infra wasn’t affected.
    >
    > TEE architecture is part of the answer to making sure that from outside even inference provider doesn’t have an access. User should verify exactly what happens with their data and prompts.
    >
    > NEAR AI code is open and inspected by many partners when deciding to leverage the stack to validate exactly what runs inside TEE and ensuring privacy.
    >
    > In this case there was also a vulnerability within SGLang, open source inference engine that runs inside an enclave. Even though this had a minimum disruption it still was a very 
    >
    > Going forward we are going increase security rigor of dependencies and also improve a “turnstile” to detect when anything out of normal runs inside TEE.
    >
    > Proactive security against external attackers has became a must. We have been using Abliterated models and red teaming harness to continuously monitor and detect issues. We are also expanding scope and compute invested into this.
    
    **Links in post:** https://twitter.com/near_ai/status/2120043366444601458
    
    **Quoted post (full text):**
    
        #### Quoted post — @near_ai — 2026-11-10 06:38 UTC (2026-11-10 07:38 WAT)
        
        - URL: https://x.com/near_ai/status/2120043366444601458
        - Metrics (at fetch): bookmark 40, impression 53944, like 168, quote 28, reply 35, repost 28
        
        > Update: On November 8, an attacker used a vulnerability in SGLang, the inference engine we run, to access part of our infrastructure. We’ve closed the access and fixed it.
        >
        > Affected users have been contacted. If you haven’t heard from us, no action is needed.
        > https://near.ai/blog/security-incident-report-sglang-vulnerability
        
        **Links in post:** https://near.ai/blog/security-incident-report-sglang-vulnerability
        
    


---

## 2026-11-07 · Post · A major L1 offered Bluethroat Labs a $10,000 bounty for a finding where two layers disagreed on what


Tags (automatic): Blockchain / L1-L2 / bridge, AI-assisted hunting


### Post — @bluethroat_labs — 2026-11-07 12:53 UTC (2026-11-07 13:53 WAT)

- URL: https://x.com/bluethroat_labs/status/2119050683840438658
- Metrics (at fetch): bookmark 9, impression 1009, like 28, quote 0, reply 0, retweet 0

> A major L1 offered Bluethroat Labs a $10,000 bounty for a finding where two layers disagreed on what counts as a quorum.
>
> The bar for our agentic consensus research: derive the protocol invariant, reproduce a failure on stock clients, run a matched control, and test recovery. https://twitter.com/saxenism/status/2119034210556223617

**Links in post:** https://twitter.com/saxenism/status/2119034210556223617

**Quoted post (full text):**

    #### Quoted post — @saxenism — 2026-11-07 11:48 UTC (2026-11-07 12:48 WAT)
    
    - URL: https://x.com/saxenism/status/2119034210556223617
    - Metrics (at fetch): bookmark 33, impression 11147, like 162, quote 1, reply 4, retweet 3
    
    > Oh, and also got a little gift for securing a major L1 :) [pic.x.com/A0rNwzT3ru]
    
    **Media:**
    - photo: https://pbs.twimg.com/media/HWhSNsZbYAAAKCQ.jpg — no alt text provided by author
    


---

## 2026-11-07 · Post · We are happy and proud to announce that we have moved to the 4th place on the @immunefi BBP leaderbo


Tags (automatic): Platform: Immunefi


### Post — @bluethroat_labs — 2026-11-07 11:34 UTC (2026-11-07 12:34 WAT)

- URL: https://x.com/bluethroat_labs/status/2119030716373832154
- Metrics (at fetch): bookmark 2, impression 2021, like 47, quote 1, reply 4, retweet 1

> We are happy and proud to announce that we have moved to the 4th place on the @immunefi BBP leaderboard.
>
> We are confident that we will be breaching the top 3 very soon. Stay tuned :)
>
> And as always, we are on the lookout for exceptional talent at Bluethroat Labs, so feel free to DM us.

**Media:**
- photo: https://pbs.twimg.com/media/HWhPLbKbQAAC6KT.jpg — no alt text provided by author

**Links in post:** https://twitter.com/saxenism/status/2118914993630630057

**Quoted post (full text):**

    #### Quoted post — @saxenism — 2026-11-07 03:54 UTC (2026-11-07 04:54 WAT)
    
    - URL: https://x.com/saxenism/status/2118914993630630057
    - Metrics (at fetch): bookmark 5, impression 3938, like 85, quote 1, reply 7, retweet 1
    
    > A bunch of bounties just got processed and now @bluethroat_labs is #4 on the 90 days Immunefi leaderboard!!
    >
    > Lesssssssssggoooooo!!!!
    >
    > PS: Photo's blurred cause that's how I remember the last night XD [pic.x.com/D8CWZaIazC]
    
    **Media:**
    - photo: https://pbs.twimg.com/media/HWfl8zHbcAA2AEw.jpg — no alt text provided by author
    - photo: https://pbs.twimg.com/media/HWfl8y-aIAArbLP.jpg — no alt text provided by author
    


---

## 2026-11-05 · Post · We carried out an extremely involved and thought provoking session, led by @saxenism.


### Post — @bluethroat_labs — 2026-11-05 11:30 UTC (2026-11-05 12:30 WAT)

- URL: https://x.com/bluethroat_labs/status/2118304882654605598
- Metrics (at fetch): bookmark 4, impression 764, like 23, quote 0, reply 0, retweet 1

> We carried out an extremely involved and thought provoking session, led by @saxenism.
>
> The post-talk interactions were just as engaging.
>
> Presentation slides: https://docs.google.com/presentation/d/1mhSexzgZYosD_AfW6B1J1GPC-HjrgphonvDpY4hOC5I/edit?usp=drivesdk [pic.x.com/lfIsoOeIR7] https://twitter.com/saxenism/status/2118203579697861082

**Media:**
- photo: https://pbs.twimg.com/media/HWW7D0vaQAAFpJC.jpg — no alt text provided by author
- photo: https://pbs.twimg.com/media/HWW7D02bUAAzQHJ.jpg — no alt text provided by author

**Links in post:** https://docs.google.com/presentation/d/1mhSexzgZYosD_AfW6B1J1GPC-HjrgphonvDpY4hOC5I/edit?usp=drivesdk, https://twitter.com/saxenism/status/2118203579697861082

**Quoted post (full text):**

    #### Quoted post — @saxenism — 2026-11-05 04:47 UTC (2026-11-05 05:47 WAT)
    
    - URL: https://x.com/saxenism/status/2118203579697861082
    - Metrics (at fetch): bookmark 1, impression 1415, like 14, quote 1, reply 1, retweet 1
    
    > About to give a detailed presentation on how companies can defend themselves in the AI era, in the Security Hub.
    >
    > If you're around, come say Hi and let's debate cutting edge security technologies, techniques and policies :) https://twitter.com/thedaofund/status/2117319992652001664
    
    **Links in post:** https://twitter.com/thedaofund/status/2117319992652001664
    
    **Quoted post (full text):**
    
        #### Quoted post — @1988994064914739210 — 2026-11-02 18:16 UTC (2026-11-02 19:16 WAT)
        
        - URL: https://x.com/1988994064914739210/status/2117319992652001664
        - Metrics (at fetch): bookmark 4, impression 2076, like 26, quote 4, reply 3, retweet 3
        
        > Thursday, November 5
        >
        > 09:00–10:00 | Networking
        >
        > 10:00–10:20 | ART-ECDSA: Threshold Signing Light Enough for a Hardware Wallet
        > Sung-Hyun Jo, @crossbar_inc 
        >
        > 10:30–11:10 | LeakDetectAI
        > Manu Gupta, @libp2p 
        >
        > 11:20–12:00 | How to Defend Your Protocol in the AI Era
        > @saxenism, https://t.co/YL7KVf6oJ2
        
        **Media:**
        - media `3_2117318286987939840` (details not returned by the API)
        
    


---

## 2026-11-03 · Post · The Bluethroat team is at @EFDevcon. 


Tags (automatic): Blockchain / L1-L2 / bridge


### Post — @bluethroat_labs — 2026-11-03 05:51 UTC (2026-11-03 06:51 WAT)

- URL: https://x.com/bluethroat_labs/status/2117494801608384998
- Metrics (at fetch): bookmark 1, impression 1809, like 41, quote 1, reply 3, retweet 1

> The Bluethroat team is at @EFDevcon. 
>
> Find any of us to talk about security, bug bounties, TEEs, consensus security, the future of web3 and anything in between. [pic.x.com/AqzdVKe7e9]

**Media:**
- photo: https://pbs.twimg.com/media/HWLaS5kbkAAAc_I.jpg — no alt text provided by author


---

## 2026-10-31 · Post · We are hosting a private, limited capacity dinner tonight in Mumbai in the run-up to @EFDevcon tonig


### Post — @bluethroat_labs — 2026-10-31 11:57 UTC (2026-10-31 12:57 WAT)

- URL: https://x.com/bluethroat_labs/status/2116499706025308501
- Metrics (at fetch): bookmark 3, impression 2767, like 33, quote 2, reply 4, retweet 1

> We are hosting a private, limited capacity dinner tonight in Mumbai in the run-up to @EFDevcon tonight.
>
> DM @saxenism if you're around and available tonight.
>
> We are looking forward to hosting you :) [pic.x.com/ie7O6gMvtt]

**Media:**
- photo: https://pbs.twimg.com/media/HV9RQr8bQAARCrW.jpg — no alt text provided by author


---

## 2026-10-30 · Post · Our founder, @saxenism asked us to operate with one core, fundamental philosophy, ie, UP ONLY.


### Post — @bluethroat_labs — 2026-10-30 10:43 UTC (2026-10-30 11:43 WAT)

- URL: https://x.com/bluethroat_labs/status/2116118833631220070
- Metrics (at fetch): bookmark 3, impression 745, like 12, quote 0, reply 2, retweet 1

> Our founder, @saxenism asked us to operate with one core, fundamental philosophy, ie, UP ONLY.
>
> So here we go, with many more on the way... so stay tuned ;) [pic.x.com/ZlCBy0zuD3] https://twitter.com/bluethroat_labs/status/2111127705119002739

**Media:**
- photo: https://pbs.twimg.com/media/HV30z5aaMAA_M_B.jpg — no alt text provided by author

**Links in post:** https://twitter.com/bluethroat_labs/status/2111127705119002739

**Quoted post (full text):**

    #### Quoted post — @bluethroat_labs — 2026-10-16 16:10 UTC (2026-10-16 17:10 WAT)
    
    - URL: https://x.com/bluethroat_labs/status/2111127705119002739
    - Metrics (at fetch): bookmark 1, impression 1449, like 7, quote 1, reply 1, retweet 0
    
    > Big update coming soon 👀 https://t.co/oyZoJ6jGNU
    
    **Media:**
    - photo: https://pbs.twimg.com/media/HUw7I4wa4AADCjV.jpg — no alt text provided by author
    


---

## 2026-10-29 · Thread · Congratulations, you got the job. 


Tags (automatic): AI-assisted hunting


### Post — @bluethroat_labs — 2026-10-29 10:44 UTC (2026-10-29 11:44 WAT)

- URL: https://x.com/bluethroat_labs/status/2115756540342964687
- Metrics (at fetch): bookmark 11, impression 2857, like 25, quote 3, reply 2, retweet 6

> Congratulations, you got the job. 
>
> Now, do you open the attached PDF to sign the joining letter on your personal system?
>
> BluePaper, our next free public good, renders the document in a disposable sandbox and returns a PDF rebuilt from pixels.
>
> Live: https://bluepaper.bluethroatlabs.com [pic.x.com/Mkd7jBwDUj]

**Media:**
- video: https://pbs.twimg.com/amplify_video_thumb/2115743735011217410/img/4_cU0-YPl27fEh2i.jpg — no alt text provided by author

**Links in post:** https://bluepaper.bluethroatlabs.com


### Thread part 2 — @bluethroat_labs — 2026-10-29 10:44 UTC (2026-10-29 11:44 WAT)

- URL: https://x.com/bluethroat_labs/status/2115756542918312420
- Metrics (at fetch): bookmark 0, impression 239, like 6, quote 0, reply 1, retweet 0

> BluePaper builds on Dangerzone. It handles PDFs, Office files, e-books and images, with optional OCR.
>
> Its report lists raw-byte indicators, not a "clean" verdict. A rebuilt PDF doesn't make the sender or message trustworthy.
>
> Source: https://github.com/BluethroatLabs/BluePaper

**Links in post:** https://github.com/BluethroatLabs/BluePaper


### Thread part 3 — @bluethroat_labs — 2026-10-29 10:44 UTC (2026-10-29 11:44 WAT)

- URL: https://x.com/bluethroat_labs/status/2115756545489109128
- Metrics (at fetch): bookmark 0, impression 103, like 5, quote 0, reply 1, retweet 0

> BlueMask, BlueSkills, BluePaper: each came from a trust decision we faced or we saw our community face.
>
> We build and keep these tools running, covering hosting, LLM usage, and whatever else it takes, so they stay free for everyone.
>
> We open-source what we can. Across the line,


### Thread part 4 — @bluethroat_labs — 2026-10-29 10:44 UTC (2026-10-29 11:44 WAT)

- URL: https://x.com/bluethroat_labs/status/2115756547896963289
- Metrics (at fetch): bookmark 0, impression 62, like 4, quote 0, reply 0, retweet 0

> Use them freely. Push them hard. Try to break them. Tell us what we missed and what feels clunky. That's how they get better.
>
> More public goods are coming. Peace out 🦅


---

## 2026-10-16 · Post · Big update coming soon 👀 https://t.co/oyZoJ6jGNU


### Post — @bluethroat_labs — 2026-10-16 16:10 UTC (2026-10-16 17:10 WAT)

- URL: https://x.com/bluethroat_labs/status/2111127705119002739
- Metrics (at fetch): bookmark 1, impression 1449, like 7, quote 1, reply 1, retweet 0

> Big update coming soon 👀 https://t.co/oyZoJ6jGNU

**Media:**
- photo: https://pbs.twimg.com/media/HUw7I4wa4AADCjV.jpg — no alt text provided by author


---

## 2026-10-09 · Post · Bounty 11 on @immunefi was downgraded from a Critical to a High due to a contrived trigger requirem


Tags (automatic): Platform: Immunefi


### Post — @bluethroat_labs — 2026-10-09 15:07 UTC (2026-10-09 16:07 WAT)

- URL: https://x.com/bluethroat_labs/status/2108575109535433161
- Metrics (at fetch): bookmark 4, impression 2643, like 34, quote 1, reply 0, retweet 1

> Bounty #11 on @immunefi was downgraded from a Critical to a High due to a contrived trigger requirement.
>
> Kudos to the team for appropriately rewarding us anyway :) [pic.x.com/g7NjgSdLbg] https://twitter.com/bluethroat_labs/status/2107490499305124027

**Media:**
- photo: https://pbs.twimg.com/media/HUMp38EWcAAViPa.jpg — no alt text provided by author

**Links in post:** https://twitter.com/bluethroat_labs/status/2107490499305124027

**Quoted post (full text):**

    #### Quoted post — @bluethroat_labs — 2026-10-06 15:17 UTC (2026-10-06 16:17 WAT)
    
    - URL: https://x.com/bluethroat_labs/status/2107490499305124027
    - Metrics (at fetch): bookmark 6, impression 3164, like 37, quote 2, reply 1, retweet 0
    
    > Bounty #10 on @immunefi stems from the same root as #9.
    >
    > Our in-house agents, specialising in low-level execution & consensus flaws were leveraged by our experts to find this vulnerability.
    >
    > We were able to break the guarantees of deterministic execution by fiddling with the exact CPU instructions for the same contracts.
    >
    > Overall, it was really fun. Onto the next one :)
    
    **Links in post:** https://twitter.com/bluethroat_labs/status/2105581456550461936
    
    **Quoted post (full text):**
    
        #### Quoted post — @bluethroat_labs — 2026-10-01 08:51 UTC (2026-10-01 09:51 WAT)
        
        - URL: https://x.com/bluethroat_labs/status/2105581456550461936
        - Metrics (at fetch): bookmark 9, impression 3011, like 43, quote 1, reply 6, retweet 1
        
        > Bounty #9 on @immunefi is extremely special for us.
        >
        > Our researchers used two in-house agents, first one a domain expert on low-level execution and another one, a domain expert for consensus flaws, to follow a failure across both domains. 
        >
        > Confirmed High.
        >
        > This is what research-led, agent-powered security looks like.
        
        **Media:**
        - photo: https://pbs.twimg.com/media/HThsFsybMAA5n7q.jpg — no alt text provided by author
        
        **Links in post:** https://twitter.com/bluethroat_labs/status/2099837289048494143
        
        **Quoted post (full text):**
        
            #### Quoted post — @bluethroat_labs — 2026-09-15 12:26 UTC (2026-09-15 13:26 WAT)
            
            - URL: https://x.com/bluethroat_labs/status/2099837289048494143
            - Metrics (at fetch): bookmark 2, impression 3243, like 22, quote 1, reply 1, retweet 2
            
            > This is a new low.
            >
            > Hope the pun landed, just like our report did XD
            >
            > This was a fun one, extremely creative but because of limited impact, we accept the Low ruling :) [pic.x.com/Oe3LUSk2vP] https://twitter.com/bluethroat_labs/status/2097594124891521488
            
            **Media:**
            - photo: https://pbs.twimg.com/media/HSQenlKaQAEYsAp.jpg — no alt text provided by author
            
            **Links in post:** https://twitter.com/bluethroat_labs/status/2097594124891521488
            
            **Quoted post (full text):**
            
                #### Quoted post — @bluethroat_labs — 2026-09-09 07:53 UTC (2026-09-09 08:53 WAT)
                
                - URL: https://x.com/bluethroat_labs/status/2097594124891521488
                - Metrics (at fetch): bookmark 0, impression 5838, like 16, quote 2, reply 3, retweet 2
                
                > This one was submitted by us 3 months ago and this had all the drama you can expect.
                >
                > This report was literally re-opened by the project themselves after they closed it (kudos to them) and voluntarily confirmed the bug (without any mediation)
                >
                > All is well that ends well :) [pic.x.com/eVvhbXGShf] https://twitter.com/bluethroat_labs/status/2090436657384141182
                
                **Media:**
                - photo: https://pbs.twimg.com/media/HRwf47zagAAGEwb.jpg — no alt text provided by author
                - photo: https://pbs.twimg.com/media/HRwmmatbcAAlJCo.jpg — no alt text provided by author
                - photo: https://pbs.twimg.com/media/HRwmsama8AA88oz.jpg — no alt text provided by author
                
                **Links in post:** https://twitter.com/bluethroat_labs/status/2090436657384141182
                
                **Quoted post (full text):**
                
                    #### Quoted post — @bluethroat_labs — 2026-08-20 13:51 UTC (2026-08-20 14:51 WAT)
                    
                    - URL: https://x.com/bluethroat_labs/status/2090436657384141182
                    - Metrics (at fetch): bookmark 3, impression 2842, like 39, quote 1, reply 0, retweet 2
                    
                    > We just got another Medium severity finding confirmed on @immunefi.
                    >
                    > Happy to continuously secure the web3 ecosystem :) [pic.x.com/rxshaoaMnq] https://twitter.com/bluethroat_labs/status/2089821971941044602
                    
                    **Media:**
                    - photo: https://pbs.twimg.com/media/HQK4uh1XQAAacVk.jpg — no alt text provided by author
                    
                    **Links in post:** https://twitter.com/bluethroat_labs/status/2089821971941044602
                    
                    **Quoted post (full text):**
                    
                        #### Quoted post — @bluethroat_labs — 2026-08-18 21:09 UTC (2026-08-18 22:09 WAT)
                        
                        - URL: https://x.com/bluethroat_labs/status/2089821971941044602
                        - Metrics (at fetch): bookmark 2, impression 5193, like 25, quote 2, reply 0, retweet 1
                        
                        > And the streak continues :) https://t.co/8aYLRDZA3G https://t.co/FZTRev3ah1
                        
                        **Media:**
                        - photo: https://pbs.twimg.com/media/HQCJ3FlbsAApZay.jpg — no alt text provided by author
                        
                        **Quoted post (full text):**
                        
                            #### Quoted post — @bluethroat_labs — 2026-08-17 10:46 UTC (2026-08-17 11:46 WAT)
                            
                            - URL: https://x.com/bluethroat_labs/status/2089302846642831475
                            - Metrics (at fetch): bookmark 7, impression 7597, like 61, quote 3, reply 5, retweet 1
                            
                            > Celebrating another win for Bluethroat Labs with everyone on @immunefi 
                            >
                            > We have developed a robust, verifiable, deeply technical, human-in-the-loop system that helps us provide extremely deep security to distributed systems.
                            >
                            > Hit us up if you're looking for security partners :) [pic.x.com/JqGD7CaBxX] https://twitter.com/bluethroat_labs/status/2088147607734702500
                            
                            **Media:**
                            - photo: https://pbs.twimg.com/media/HP6uw8Fa0AAtTLe.jpg — no alt text provided by author
                            
                            **Links in post:** https://twitter.com/bluethroat_labs/status/2088147607734702500
                            
                            **Quoted post (full text):**
                            
                                #### Quoted post — @bluethroat_labs — 2026-08-14 06:16 UTC (2026-08-14 07:16 WAT)
                                
                                - URL: https://x.com/bluethroat_labs/status/2088147607734702500
                                - Metrics (at fetch): bookmark 4, impression 5832, like 46, quote 2, reply 0, retweet 1
                                
                                > New day, New bounty :)
                                >
                                > We deeply understand TEEs and distributed systems and everyday we strive to become even better. 
                                >
                                > And armed with our in-house experts, we are on a war-path to improve security standards acorss web3.
                                >
                                > Cheers to another bounty for our finding on @immunefi [pic.x.com/G2s8V3qt3S] https://twitter.com/bluethroat_labs/status/2087791137251795005
                                
                                **Media:**
                                - photo: https://pbs.twimg.com/media/HPqW3cgb0AAMcHd.jpg — no alt text provided by author
                                
                                **Links in post:** https://twitter.com/bluethroat_labs/status/2087791137251795005
                                
                                **Quoted post (full text):**
                                
                                    #### Quoted post — @bluethroat_labs — 2026-08-13 06:39 UTC (2026-08-13 07:39 WAT)
                                    
                                    - URL: https://x.com/bluethroat_labs/status/2087791137251795005
                                    - Metrics (at fetch): bookmark 1, impression 5747, like 29, quote 2, reply 0, retweet 1
                                    
                                    > At Bluethroat, we have a simple objective:
                                    > Wake up and stack receipts.
                                    >
                                    > Cheers on another confirmed finding on @immunefi 
                                    >
                                    > Onwards and Upwards [pic.x.com/kJCYiNbthW] https://twitter.com/bluethroat_labs/status/2084313356698325268
                                    
                                    **Media:**
                                    - photo: https://pbs.twimg.com/media/HPlSlkyaUAEK94S.jpg — no alt text provided by author
                                    
                                    **Links in post:** https://twitter.com/bluethroat_labs/status/2084313356698325268
                                    
                                    **Quoted post (full text):**
                                    
                                        #### Quoted post — @bluethroat_labs — 2026-08-03 16:20 UTC (2026-08-03 17:20 WAT)
                                        
                                        - URL: https://x.com/bluethroat_labs/status/2084313356698325268
                                        - Metrics (at fetch): bookmark 11, impression 11588, like 139, quote 2, reply 8, retweet 1
                                        
                                        > We just found a confirmed bug on @immunefi #immunefitribe 
                                        >
                                        > https://immunefi.com/s/ss/?severity=critical&status=confirmed&gifId=0&programType=bug-bounty
                                        
                                        **Links in post:** https://immunefi.com/s/ss/?severity=critical&status=confirmed&gifId=0&programType=bug-bounty
                                        
                                    
                                
                            
                        
                    
                
            
        
    


---

## 2026-10-09 · Post · Daily reminder: your agent can read your files and run commands. That skill you found on X can tell 


Tags (automatic): AI-assisted hunting


### Post — @bluethroat_labs — 2026-10-09 01:52 UTC (2026-10-09 02:52 WAT)

- URL: https://x.com/bluethroat_labs/status/2108375027582144846
- Metrics (at fetch): bookmark 2, impression 458, like 10, quote 0, reply 0, retweet 1

> Daily reminder: your agent can read your files and run commands. That skill you found on X can tell it what to do.
>
> Scan before installing. Review the evidence. Then decide.
>
> Make BlueSkills part of your workflow:
> https://t.co/yRjnfsDe2V


---

## 2026-10-06 · Thread · Bounty 10 on @immunefi stems from the same root as 9.


Tags (automatic): Blockchain / L1-L2 / bridge, AI-assisted hunting, Platform: Immunefi


### Post — @bluethroat_labs — 2026-10-06 15:17 UTC (2026-10-06 16:17 WAT)

- URL: https://x.com/bluethroat_labs/status/2107490499305124027
- Metrics (at fetch): bookmark 6, impression 3164, like 37, quote 2, reply 1, retweet 0

> Bounty #10 on @immunefi stems from the same root as #9.
>
> Our in-house agents, specialising in low-level execution & consensus flaws were leveraged by our experts to find this vulnerability.
>
> We were able to break the guarantees of deterministic execution by fiddling with the exact CPU instructions for the same contracts.
>
> Overall, it was really fun. Onto the next one :)

**Links in post:** https://twitter.com/bluethroat_labs/status/2105581456550461936

**Quoted post (full text):**

    #### Quoted post — @bluethroat_labs — 2026-10-01 08:51 UTC (2026-10-01 09:51 WAT)
    
    - URL: https://x.com/bluethroat_labs/status/2105581456550461936
    - Metrics (at fetch): bookmark 9, impression 3011, like 43, quote 1, reply 6, retweet 1
    
    > Bounty #9 on @immunefi is extremely special for us.
    >
    > Our researchers used two in-house agents, first one a domain expert on low-level execution and another one, a domain expert for consensus flaws, to follow a failure across both domains. 
    >
    > Confirmed High.
    >
    > This is what research-led, agent-powered security looks like.
    
    **Media:**
    - photo: https://pbs.twimg.com/media/HThsFsybMAA5n7q.jpg — no alt text provided by author
    
    **Links in post:** https://twitter.com/bluethroat_labs/status/2099837289048494143
    
    **Quoted post (full text):**
    
        #### Quoted post — @bluethroat_labs — 2026-09-15 12:26 UTC (2026-09-15 13:26 WAT)
        
        - URL: https://x.com/bluethroat_labs/status/2099837289048494143
        - Metrics (at fetch): bookmark 2, impression 3243, like 22, quote 1, reply 1, retweet 2
        
        > This is a new low.
        >
        > Hope the pun landed, just like our report did XD
        >
        > This was a fun one, extremely creative but because of limited impact, we accept the Low ruling :) [pic.x.com/Oe3LUSk2vP] https://twitter.com/bluethroat_labs/status/2097594124891521488
        
        **Media:**
        - photo: https://pbs.twimg.com/media/HSQenlKaQAEYsAp.jpg — no alt text provided by author
        
        **Links in post:** https://twitter.com/bluethroat_labs/status/2097594124891521488
        
        **Quoted post (full text):**
        
            #### Quoted post — @bluethroat_labs — 2026-09-09 07:53 UTC (2026-09-09 08:53 WAT)
            
            - URL: https://x.com/bluethroat_labs/status/2097594124891521488
            - Metrics (at fetch): bookmark 0, impression 5838, like 16, quote 2, reply 3, retweet 2
            
            > This one was submitted by us 3 months ago and this had all the drama you can expect.
            >
            > This report was literally re-opened by the project themselves after they closed it (kudos to them) and voluntarily confirmed the bug (without any mediation)
            >
            > All is well that ends well :) [pic.x.com/eVvhbXGShf] https://twitter.com/bluethroat_labs/status/2090436657384141182
            
            **Media:**
            - photo: https://pbs.twimg.com/media/HRwf47zagAAGEwb.jpg — no alt text provided by author
            - photo: https://pbs.twimg.com/media/HRwmmatbcAAlJCo.jpg — no alt text provided by author
            - photo: https://pbs.twimg.com/media/HRwmsama8AA88oz.jpg — no alt text provided by author
            
            **Links in post:** https://twitter.com/bluethroat_labs/status/2090436657384141182
            
            **Quoted post (full text):**
            
                #### Quoted post — @bluethroat_labs — 2026-08-20 13:51 UTC (2026-08-20 14:51 WAT)
                
                - URL: https://x.com/bluethroat_labs/status/2090436657384141182
                - Metrics (at fetch): bookmark 3, impression 2842, like 39, quote 1, reply 0, retweet 2
                
                > We just got another Medium severity finding confirmed on @immunefi.
                >
                > Happy to continuously secure the web3 ecosystem :) [pic.x.com/rxshaoaMnq] https://twitter.com/bluethroat_labs/status/2089821971941044602
                
                **Media:**
                - photo: https://pbs.twimg.com/media/HQK4uh1XQAAacVk.jpg — no alt text provided by author
                
                **Links in post:** https://twitter.com/bluethroat_labs/status/2089821971941044602
                
                **Quoted post (full text):**
                
                    #### Quoted post — @bluethroat_labs — 2026-08-18 21:09 UTC (2026-08-18 22:09 WAT)
                    
                    - URL: https://x.com/bluethroat_labs/status/2089821971941044602
                    - Metrics (at fetch): bookmark 2, impression 5193, like 25, quote 2, reply 0, retweet 1
                    
                    > And the streak continues :) https://t.co/8aYLRDZA3G https://t.co/FZTRev3ah1
                    
                    **Media:**
                    - photo: https://pbs.twimg.com/media/HQCJ3FlbsAApZay.jpg — no alt text provided by author
                    
                    **Quoted post (full text):**
                    
                        #### Quoted post — @bluethroat_labs — 2026-08-17 10:46 UTC (2026-08-17 11:46 WAT)
                        
                        - URL: https://x.com/bluethroat_labs/status/2089302846642831475
                        - Metrics (at fetch): bookmark 7, impression 7597, like 61, quote 3, reply 5, retweet 1
                        
                        > Celebrating another win for Bluethroat Labs with everyone on @immunefi 
                        >
                        > We have developed a robust, verifiable, deeply technical, human-in-the-loop system that helps us provide extremely deep security to distributed systems.
                        >
                        > Hit us up if you're looking for security partners :) [pic.x.com/JqGD7CaBxX] https://twitter.com/bluethroat_labs/status/2088147607734702500
                        
                        **Media:**
                        - photo: https://pbs.twimg.com/media/HP6uw8Fa0AAtTLe.jpg — no alt text provided by author
                        
                        **Links in post:** https://twitter.com/bluethroat_labs/status/2088147607734702500
                        
                        **Quoted post (full text):**
                        
                            #### Quoted post — @bluethroat_labs — 2026-08-14 06:16 UTC (2026-08-14 07:16 WAT)
                            
                            - URL: https://x.com/bluethroat_labs/status/2088147607734702500
                            - Metrics (at fetch): bookmark 4, impression 5832, like 46, quote 2, reply 0, retweet 1
                            
                            > New day, New bounty :)
                            >
                            > We deeply understand TEEs and distributed systems and everyday we strive to become even better. 
                            >
                            > And armed with our in-house experts, we are on a war-path to improve security standards acorss web3.
                            >
                            > Cheers to another bounty for our finding on @immunefi [pic.x.com/G2s8V3qt3S] https://twitter.com/bluethroat_labs/status/2087791137251795005
                            
                            **Media:**
                            - photo: https://pbs.twimg.com/media/HPqW3cgb0AAMcHd.jpg — no alt text provided by author
                            
                            **Links in post:** https://twitter.com/bluethroat_labs/status/2087791137251795005
                            
                            **Quoted post (full text):**
                            
                                #### Quoted post — @bluethroat_labs — 2026-08-13 06:39 UTC (2026-08-13 07:39 WAT)
                                
                                - URL: https://x.com/bluethroat_labs/status/2087791137251795005
                                - Metrics (at fetch): bookmark 1, impression 5747, like 29, quote 2, reply 0, retweet 1
                                
                                > At Bluethroat, we have a simple objective:
                                > Wake up and stack receipts.
                                >
                                > Cheers on another confirmed finding on @immunefi 
                                >
                                > Onwards and Upwards [pic.x.com/kJCYiNbthW] https://twitter.com/bluethroat_labs/status/2084313356698325268
                                
                                **Media:**
                                - photo: https://pbs.twimg.com/media/HPlSlkyaUAEK94S.jpg — no alt text provided by author
                                
                                **Links in post:** https://twitter.com/bluethroat_labs/status/2084313356698325268
                                
                                **Quoted post (full text):**
                                
                                    #### Quoted post — @bluethroat_labs — 2026-08-03 16:20 UTC (2026-08-03 17:20 WAT)
                                    
                                    - URL: https://x.com/bluethroat_labs/status/2084313356698325268
                                    - Metrics (at fetch): bookmark 11, impression 11588, like 139, quote 2, reply 8, retweet 1
                                    
                                    > We just found a confirmed bug on @immunefi #immunefitribe 
                                    >
                                    > https://immunefi.com/s/ss/?severity=critical&status=confirmed&gifId=0&programType=bug-bounty
                                    
                                    **Links in post:** https://immunefi.com/s/ss/?severity=critical&status=confirmed&gifId=0&programType=bug-bounty
                                    
                                
                            
                        
                    
                
            
        
    


### Thread part 2 — @bluethroat_labs — 2026-10-06 17:45 UTC (2026-10-06 18:45 WAT)

- URL: https://x.com/bluethroat_labs/status/2107527705894023400
- Metrics (at fetch): bookmark 0, impression 78, like 1, quote 0, reply 0, retweet 0

> @kalyan__tr @immunefi 🫡🫡


---

## 2026-10-01 · Thread · Our founder secures protocols for a living. He still ran an AI skill from X in Codex without reading


Tags (automatic): AI-assisted hunting


### Post — @bluethroat_labs — 2026-10-01 11:00 UTC (2026-10-01 12:00 WAT)

- URL: https://x.com/bluethroat_labs/status/2105613704469598659
- Metrics (at fetch): bookmark 6, impression 2106, like 46, quote 2, reply 9, retweet 6

> Our founder secures protocols for a living. He still ran an AI skill from X in Codex without reading it.
>
> Codex could read and write files and run commands on his laptop.
>
> He got lucky. You might not. So we built BlueSkills.
>
> Live now: https://t.co/hyJEHflo4r https://t.co/jPgK3W9TR9

**Media:**
- video: https://pbs.twimg.com/amplify_video_thumb/2105604161714917376/img/DXMbveBFkz1cAWnZ.jpg — no alt text provided by author


### Thread part 2 — @bluethroat_labs — 2026-10-01 11:00 UTC (2026-10-01 12:00 WAT)

- URL: https://x.com/bluethroat_labs/status/2105613704935149736
- Metrics (at fetch): bookmark 0, impression 365, like 5, quote 0, reply 1, retweet 0

> BlueSkills works on the web, through Telegram, or via CLI from your agent. Scan a public repo, ZIP, or SKILL.md before installing.
>
> The report shows the verdict, findings, evidence, and coverage gaps. CLEAN is not a guarantee of safety.


### Thread part 3 — @bluethroat_labs — 2026-10-01 11:00 UTC (2026-10-01 12:00 WAT)

- URL: https://x.com/bluethroat_labs/status/2105613705241379191
- Metrics (at fetch): bookmark 0, impression 307, like 5, quote 1, reply 0, retweet 0

> We paid people to break BlueSkills. Three malicious skills scored CLEAN. We patched those bypasses and published the lessons.
>
> BlueSkills is a public good from Bluethroat Labs. More tools are coming.
>
> Full story: https://t.co/ZAF0Pov98y


---

## 2026-10-01 · Post · Bounty 9 on @immunefi is extremely special for us.


Tags (automatic): Blockchain / L1-L2 / bridge, AI-assisted hunting, Platform: Immunefi


### Post — @bluethroat_labs — 2026-10-01 08:51 UTC (2026-10-01 09:51 WAT)

- URL: https://x.com/bluethroat_labs/status/2105581456550461936
- Metrics (at fetch): bookmark 9, impression 3011, like 43, quote 1, reply 6, retweet 1

> Bounty #9 on @immunefi is extremely special for us.
>
> Our researchers used two in-house agents, first one a domain expert on low-level execution and another one, a domain expert for consensus flaws, to follow a failure across both domains. 
>
> Confirmed High.
>
> This is what research-led, agent-powered security looks like.

**Media:**
- photo: https://pbs.twimg.com/media/HThsFsybMAA5n7q.jpg — no alt text provided by author

**Links in post:** https://twitter.com/bluethroat_labs/status/2099837289048494143

**Quoted post (full text):**

    #### Quoted post — @bluethroat_labs — 2026-09-15 12:26 UTC (2026-09-15 13:26 WAT)
    
    - URL: https://x.com/bluethroat_labs/status/2099837289048494143
    - Metrics (at fetch): bookmark 2, impression 3243, like 22, quote 1, reply 1, retweet 2
    
    > This is a new low.
    >
    > Hope the pun landed, just like our report did XD
    >
    > This was a fun one, extremely creative but because of limited impact, we accept the Low ruling :) [pic.x.com/Oe3LUSk2vP] https://twitter.com/bluethroat_labs/status/2097594124891521488
    
    **Media:**
    - photo: https://pbs.twimg.com/media/HSQenlKaQAEYsAp.jpg — no alt text provided by author
    
    **Links in post:** https://twitter.com/bluethroat_labs/status/2097594124891521488
    
    **Quoted post (full text):**
    
        #### Quoted post — @bluethroat_labs — 2026-09-09 07:53 UTC (2026-09-09 08:53 WAT)
        
        - URL: https://x.com/bluethroat_labs/status/2097594124891521488
        - Metrics (at fetch): bookmark 0, impression 5838, like 16, quote 2, reply 3, retweet 2
        
        > This one was submitted by us 3 months ago and this had all the drama you can expect.
        >
        > This report was literally re-opened by the project themselves after they closed it (kudos to them) and voluntarily confirmed the bug (without any mediation)
        >
        > All is well that ends well :) [pic.x.com/eVvhbXGShf] https://twitter.com/bluethroat_labs/status/2090436657384141182
        
        **Media:**
        - photo: https://pbs.twimg.com/media/HRwf47zagAAGEwb.jpg — no alt text provided by author
        - photo: https://pbs.twimg.com/media/HRwmmatbcAAlJCo.jpg — no alt text provided by author
        - photo: https://pbs.twimg.com/media/HRwmsama8AA88oz.jpg — no alt text provided by author
        
        **Links in post:** https://twitter.com/bluethroat_labs/status/2090436657384141182
        
        **Quoted post (full text):**
        
            #### Quoted post — @bluethroat_labs — 2026-08-20 13:51 UTC (2026-08-20 14:51 WAT)
            
            - URL: https://x.com/bluethroat_labs/status/2090436657384141182
            - Metrics (at fetch): bookmark 3, impression 2842, like 39, quote 1, reply 0, retweet 2
            
            > We just got another Medium severity finding confirmed on @immunefi.
            >
            > Happy to continuously secure the web3 ecosystem :) [pic.x.com/rxshaoaMnq] https://twitter.com/bluethroat_labs/status/2089821971941044602
            
            **Media:**
            - photo: https://pbs.twimg.com/media/HQK4uh1XQAAacVk.jpg — no alt text provided by author
            
            **Links in post:** https://twitter.com/bluethroat_labs/status/2089821971941044602
            
            **Quoted post (full text):**
            
                #### Quoted post — @bluethroat_labs — 2026-08-18 21:09 UTC (2026-08-18 22:09 WAT)
                
                - URL: https://x.com/bluethroat_labs/status/2089821971941044602
                - Metrics (at fetch): bookmark 2, impression 5193, like 25, quote 2, reply 0, retweet 1
                
                > And the streak continues :) https://t.co/8aYLRDZA3G https://t.co/FZTRev3ah1
                
                **Media:**
                - photo: https://pbs.twimg.com/media/HQCJ3FlbsAApZay.jpg — no alt text provided by author
                
                **Quoted post (full text):**
                
                    #### Quoted post — @bluethroat_labs — 2026-08-17 10:46 UTC (2026-08-17 11:46 WAT)
                    
                    - URL: https://x.com/bluethroat_labs/status/2089302846642831475
                    - Metrics (at fetch): bookmark 7, impression 7597, like 61, quote 3, reply 5, retweet 1
                    
                    > Celebrating another win for Bluethroat Labs with everyone on @immunefi 
                    >
                    > We have developed a robust, verifiable, deeply technical, human-in-the-loop system that helps us provide extremely deep security to distributed systems.
                    >
                    > Hit us up if you're looking for security partners :) [pic.x.com/JqGD7CaBxX] https://twitter.com/bluethroat_labs/status/2088147607734702500
                    
                    **Media:**
                    - photo: https://pbs.twimg.com/media/HP6uw8Fa0AAtTLe.jpg — no alt text provided by author
                    
                    **Links in post:** https://twitter.com/bluethroat_labs/status/2088147607734702500
                    
                    **Quoted post (full text):**
                    
                        #### Quoted post — @bluethroat_labs — 2026-08-14 06:16 UTC (2026-08-14 07:16 WAT)
                        
                        - URL: https://x.com/bluethroat_labs/status/2088147607734702500
                        - Metrics (at fetch): bookmark 4, impression 5832, like 46, quote 2, reply 0, retweet 1
                        
                        > New day, New bounty :)
                        >
                        > We deeply understand TEEs and distributed systems and everyday we strive to become even better. 
                        >
                        > And armed with our in-house experts, we are on a war-path to improve security standards acorss web3.
                        >
                        > Cheers to another bounty for our finding on @immunefi [pic.x.com/G2s8V3qt3S] https://twitter.com/bluethroat_labs/status/2087791137251795005
                        
                        **Media:**
                        - photo: https://pbs.twimg.com/media/HPqW3cgb0AAMcHd.jpg — no alt text provided by author
                        
                        **Links in post:** https://twitter.com/bluethroat_labs/status/2087791137251795005
                        
                        **Quoted post (full text):**
                        
                            #### Quoted post — @bluethroat_labs — 2026-08-13 06:39 UTC (2026-08-13 07:39 WAT)
                            
                            - URL: https://x.com/bluethroat_labs/status/2087791137251795005
                            - Metrics (at fetch): bookmark 1, impression 5747, like 29, quote 2, reply 0, retweet 1
                            
                            > At Bluethroat, we have a simple objective:
                            > Wake up and stack receipts.
                            >
                            > Cheers on another confirmed finding on @immunefi 
                            >
                            > Onwards and Upwards [pic.x.com/kJCYiNbthW] https://twitter.com/bluethroat_labs/status/2084313356698325268
                            
                            **Media:**
                            - photo: https://pbs.twimg.com/media/HPlSlkyaUAEK94S.jpg — no alt text provided by author
                            
                            **Links in post:** https://twitter.com/bluethroat_labs/status/2084313356698325268
                            
                            **Quoted post (full text):**
                            
                                #### Quoted post — @bluethroat_labs — 2026-08-03 16:20 UTC (2026-08-03 17:20 WAT)
                                
                                - URL: https://x.com/bluethroat_labs/status/2084313356698325268
                                - Metrics (at fetch): bookmark 11, impression 11588, like 139, quote 2, reply 8, retweet 1
                                
                                > We just found a confirmed bug on @immunefi #immunefitribe 
                                >
                                > https://immunefi.com/s/ss/?severity=critical&status=confirmed&gifId=0&programType=bug-bounty
                                
                                **Links in post:** https://immunefi.com/s/ss/?severity=critical&status=confirmed&gifId=0&programType=bug-bounty
                                
                            
                        
                    
                
            
        
    


---

## 2026-09-29 · Post · We’ve been finding and responsibly disclosing vulnerabilities across Web3.


### Post — @bluethroat_labs — 2026-09-29 13:24 UTC (2026-09-29 14:24 WAT)

- URL: https://x.com/bluethroat_labs/status/2104925306947792941
- Metrics (at fetch): bookmark 0, impression 1313, like 16, quote 1, reply 1, retweet 1

> We’ve been finding and responsibly disclosing vulnerabilities across Web3.
>
> But we haven’t just been finding problems. We’ve been building, too.
>
> Tomorrow, we’re unveiling a new tool to help you build more safely.
>
> September 30 · 15:00 UTC / 8:30 PM IST.
>
> 🦅 Stay tuned 🦅


---

## 2026-09-15 · Post · This is a new low.


### Post — @bluethroat_labs — 2026-09-15 12:26 UTC (2026-09-15 13:26 WAT)

- URL: https://x.com/bluethroat_labs/status/2099837289048494143
- Metrics (at fetch): bookmark 2, impression 3243, like 22, quote 1, reply 1, retweet 2

> This is a new low.
>
> Hope the pun landed, just like our report did XD
>
> This was a fun one, extremely creative but because of limited impact, we accept the Low ruling :) [pic.x.com/Oe3LUSk2vP] https://twitter.com/bluethroat_labs/status/2097594124891521488

**Media:**
- photo: https://pbs.twimg.com/media/HSQenlKaQAEYsAp.jpg — no alt text provided by author

**Links in post:** https://twitter.com/bluethroat_labs/status/2097594124891521488

**Quoted post (full text):**

    #### Quoted post — @bluethroat_labs — 2026-09-09 07:53 UTC (2026-09-09 08:53 WAT)
    
    - URL: https://x.com/bluethroat_labs/status/2097594124891521488
    - Metrics (at fetch): bookmark 0, impression 5838, like 16, quote 2, reply 3, retweet 2
    
    > This one was submitted by us 3 months ago and this had all the drama you can expect.
    >
    > This report was literally re-opened by the project themselves after they closed it (kudos to them) and voluntarily confirmed the bug (without any mediation)
    >
    > All is well that ends well :) [pic.x.com/eVvhbXGShf] https://twitter.com/bluethroat_labs/status/2090436657384141182
    
    **Media:**
    - photo: https://pbs.twimg.com/media/HRwf47zagAAGEwb.jpg — no alt text provided by author
    - photo: https://pbs.twimg.com/media/HRwmmatbcAAlJCo.jpg — no alt text provided by author
    - photo: https://pbs.twimg.com/media/HRwmsama8AA88oz.jpg — no alt text provided by author
    
    **Links in post:** https://twitter.com/bluethroat_labs/status/2090436657384141182
    
    **Quoted post (full text):**
    
        #### Quoted post — @bluethroat_labs — 2026-08-20 13:51 UTC (2026-08-20 14:51 WAT)
        
        - URL: https://x.com/bluethroat_labs/status/2090436657384141182
        - Metrics (at fetch): bookmark 3, impression 2842, like 39, quote 1, reply 0, retweet 2
        
        > We just got another Medium severity finding confirmed on @immunefi.
        >
        > Happy to continuously secure the web3 ecosystem :) [pic.x.com/rxshaoaMnq] https://twitter.com/bluethroat_labs/status/2089821971941044602
        
        **Media:**
        - photo: https://pbs.twimg.com/media/HQK4uh1XQAAacVk.jpg — no alt text provided by author
        
        **Links in post:** https://twitter.com/bluethroat_labs/status/2089821971941044602
        
        **Quoted post (full text):**
        
            #### Quoted post — @bluethroat_labs — 2026-08-18 21:09 UTC (2026-08-18 22:09 WAT)
            
            - URL: https://x.com/bluethroat_labs/status/2089821971941044602
            - Metrics (at fetch): bookmark 2, impression 5193, like 25, quote 2, reply 0, retweet 1
            
            > And the streak continues :) https://t.co/8aYLRDZA3G https://t.co/FZTRev3ah1
            
            **Media:**
            - photo: https://pbs.twimg.com/media/HQCJ3FlbsAApZay.jpg — no alt text provided by author
            
            **Quoted post (full text):**
            
                #### Quoted post — @bluethroat_labs — 2026-08-17 10:46 UTC (2026-08-17 11:46 WAT)
                
                - URL: https://x.com/bluethroat_labs/status/2089302846642831475
                - Metrics (at fetch): bookmark 7, impression 7597, like 61, quote 3, reply 5, retweet 1
                
                > Celebrating another win for Bluethroat Labs with everyone on @immunefi 
                >
                > We have developed a robust, verifiable, deeply technical, human-in-the-loop system that helps us provide extremely deep security to distributed systems.
                >
                > Hit us up if you're looking for security partners :) [pic.x.com/JqGD7CaBxX] https://twitter.com/bluethroat_labs/status/2088147607734702500
                
                **Media:**
                - photo: https://pbs.twimg.com/media/HP6uw8Fa0AAtTLe.jpg — no alt text provided by author
                
                **Links in post:** https://twitter.com/bluethroat_labs/status/2088147607734702500
                
                **Quoted post (full text):**
                
                    #### Quoted post — @bluethroat_labs — 2026-08-14 06:16 UTC (2026-08-14 07:16 WAT)
                    
                    - URL: https://x.com/bluethroat_labs/status/2088147607734702500
                    - Metrics (at fetch): bookmark 4, impression 5832, like 46, quote 2, reply 0, retweet 1
                    
                    > New day, New bounty :)
                    >
                    > We deeply understand TEEs and distributed systems and everyday we strive to become even better. 
                    >
                    > And armed with our in-house experts, we are on a war-path to improve security standards acorss web3.
                    >
                    > Cheers to another bounty for our finding on @immunefi [pic.x.com/G2s8V3qt3S] https://twitter.com/bluethroat_labs/status/2087791137251795005
                    
                    **Media:**
                    - photo: https://pbs.twimg.com/media/HPqW3cgb0AAMcHd.jpg — no alt text provided by author
                    
                    **Links in post:** https://twitter.com/bluethroat_labs/status/2087791137251795005
                    
                    **Quoted post (full text):**
                    
                        #### Quoted post — @bluethroat_labs — 2026-08-13 06:39 UTC (2026-08-13 07:39 WAT)
                        
                        - URL: https://x.com/bluethroat_labs/status/2087791137251795005
                        - Metrics (at fetch): bookmark 1, impression 5747, like 29, quote 2, reply 0, retweet 1
                        
                        > At Bluethroat, we have a simple objective:
                        > Wake up and stack receipts.
                        >
                        > Cheers on another confirmed finding on @immunefi 
                        >
                        > Onwards and Upwards [pic.x.com/kJCYiNbthW] https://twitter.com/bluethroat_labs/status/2084313356698325268
                        
                        **Media:**
                        - photo: https://pbs.twimg.com/media/HPlSlkyaUAEK94S.jpg — no alt text provided by author
                        
                        **Links in post:** https://twitter.com/bluethroat_labs/status/2084313356698325268
                        
                        **Quoted post (full text):**
                        
                            #### Quoted post — @bluethroat_labs — 2026-08-03 16:20 UTC (2026-08-03 17:20 WAT)
                            
                            - URL: https://x.com/bluethroat_labs/status/2084313356698325268
                            - Metrics (at fetch): bookmark 11, impression 11588, like 139, quote 2, reply 8, retweet 1
                            
                            > We just found a confirmed bug on @immunefi #immunefitribe 
                            >
                            > https://immunefi.com/s/ss/?severity=critical&status=confirmed&gifId=0&programType=bug-bounty
                            
                            **Links in post:** https://immunefi.com/s/ss/?severity=critical&status=confirmed&gifId=0&programType=bug-bounty
                            
                        
                    
                
            
        
    


---

## 2026-09-09 · Post · This one was submitted by us 3 months ago and this had all the drama you can expect.


### Post — @bluethroat_labs — 2026-09-09 07:53 UTC (2026-09-09 08:53 WAT)

- URL: https://x.com/bluethroat_labs/status/2097594124891521488
- Metrics (at fetch): bookmark 0, impression 5838, like 16, quote 2, reply 3, retweet 2

> This one was submitted by us 3 months ago and this had all the drama you can expect.
>
> This report was literally re-opened by the project themselves after they closed it (kudos to them) and voluntarily confirmed the bug (without any mediation)
>
> All is well that ends well :) [pic.x.com/eVvhbXGShf] https://twitter.com/bluethroat_labs/status/2090436657384141182

**Media:**
- photo: https://pbs.twimg.com/media/HRwf47zagAAGEwb.jpg — no alt text provided by author
- photo: https://pbs.twimg.com/media/HRwmmatbcAAlJCo.jpg — no alt text provided by author
- photo: https://pbs.twimg.com/media/HRwmsama8AA88oz.jpg — no alt text provided by author

**Links in post:** https://twitter.com/bluethroat_labs/status/2090436657384141182

**Quoted post (full text):**

    #### Quoted post — @bluethroat_labs — 2026-08-20 13:51 UTC (2026-08-20 14:51 WAT)
    
    - URL: https://x.com/bluethroat_labs/status/2090436657384141182
    - Metrics (at fetch): bookmark 3, impression 2842, like 39, quote 1, reply 0, retweet 2
    
    > We just got another Medium severity finding confirmed on @immunefi.
    >
    > Happy to continuously secure the web3 ecosystem :) [pic.x.com/rxshaoaMnq] https://twitter.com/bluethroat_labs/status/2089821971941044602
    
    **Media:**
    - photo: https://pbs.twimg.com/media/HQK4uh1XQAAacVk.jpg — no alt text provided by author
    
    **Links in post:** https://twitter.com/bluethroat_labs/status/2089821971941044602
    
    **Quoted post (full text):**
    
        #### Quoted post — @bluethroat_labs — 2026-08-18 21:09 UTC (2026-08-18 22:09 WAT)
        
        - URL: https://x.com/bluethroat_labs/status/2089821971941044602
        - Metrics (at fetch): bookmark 2, impression 5193, like 25, quote 2, reply 0, retweet 1
        
        > And the streak continues :) https://t.co/8aYLRDZA3G https://t.co/FZTRev3ah1
        
        **Media:**
        - photo: https://pbs.twimg.com/media/HQCJ3FlbsAApZay.jpg — no alt text provided by author
        
        **Quoted post (full text):**
        
            #### Quoted post — @bluethroat_labs — 2026-08-17 10:46 UTC (2026-08-17 11:46 WAT)
            
            - URL: https://x.com/bluethroat_labs/status/2089302846642831475
            - Metrics (at fetch): bookmark 7, impression 7597, like 61, quote 3, reply 5, retweet 1
            
            > Celebrating another win for Bluethroat Labs with everyone on @immunefi 
            >
            > We have developed a robust, verifiable, deeply technical, human-in-the-loop system that helps us provide extremely deep security to distributed systems.
            >
            > Hit us up if you're looking for security partners :) [pic.x.com/JqGD7CaBxX] https://twitter.com/bluethroat_labs/status/2088147607734702500
            
            **Media:**
            - photo: https://pbs.twimg.com/media/HP6uw8Fa0AAtTLe.jpg — no alt text provided by author
            
            **Links in post:** https://twitter.com/bluethroat_labs/status/2088147607734702500
            
            **Quoted post (full text):**
            
                #### Quoted post — @bluethroat_labs — 2026-08-14 06:16 UTC (2026-08-14 07:16 WAT)
                
                - URL: https://x.com/bluethroat_labs/status/2088147607734702500
                - Metrics (at fetch): bookmark 4, impression 5832, like 46, quote 2, reply 0, retweet 1
                
                > New day, New bounty :)
                >
                > We deeply understand TEEs and distributed systems and everyday we strive to become even better. 
                >
                > And armed with our in-house experts, we are on a war-path to improve security standards acorss web3.
                >
                > Cheers to another bounty for our finding on @immunefi [pic.x.com/G2s8V3qt3S] https://twitter.com/bluethroat_labs/status/2087791137251795005
                
                **Media:**
                - photo: https://pbs.twimg.com/media/HPqW3cgb0AAMcHd.jpg — no alt text provided by author
                
                **Links in post:** https://twitter.com/bluethroat_labs/status/2087791137251795005
                
                **Quoted post (full text):**
                
                    #### Quoted post — @bluethroat_labs — 2026-08-13 06:39 UTC (2026-08-13 07:39 WAT)
                    
                    - URL: https://x.com/bluethroat_labs/status/2087791137251795005
                    - Metrics (at fetch): bookmark 1, impression 5747, like 29, quote 2, reply 0, retweet 1
                    
                    > At Bluethroat, we have a simple objective:
                    > Wake up and stack receipts.
                    >
                    > Cheers on another confirmed finding on @immunefi 
                    >
                    > Onwards and Upwards [pic.x.com/kJCYiNbthW] https://twitter.com/bluethroat_labs/status/2084313356698325268
                    
                    **Media:**
                    - photo: https://pbs.twimg.com/media/HPlSlkyaUAEK94S.jpg — no alt text provided by author
                    
                    **Links in post:** https://twitter.com/bluethroat_labs/status/2084313356698325268
                    
                    **Quoted post (full text):**
                    
                        #### Quoted post — @bluethroat_labs — 2026-08-03 16:20 UTC (2026-08-03 17:20 WAT)
                        
                        - URL: https://x.com/bluethroat_labs/status/2084313356698325268
                        - Metrics (at fetch): bookmark 11, impression 11588, like 139, quote 2, reply 8, retweet 1
                        
                        > We just found a confirmed bug on @immunefi #immunefitribe 
                        >
                        > https://immunefi.com/s/ss/?severity=critical&status=confirmed&gifId=0&programType=bug-bounty
                        
                        **Links in post:** https://immunefi.com/s/ss/?severity=critical&status=confirmed&gifId=0&programType=bug-bounty
                        
                    
                
            
        
    


---

## 2026-08-20 · Post · We just got another Medium severity finding confirmed on @immunefi.


Tags (automatic): Platform: Immunefi


### Post — @bluethroat_labs — 2026-08-20 13:51 UTC (2026-08-20 14:51 WAT)

- URL: https://x.com/bluethroat_labs/status/2090436657384141182
- Metrics (at fetch): bookmark 3, impression 2842, like 39, quote 1, reply 0, retweet 2

> We just got another Medium severity finding confirmed on @immunefi.
>
> Happy to continuously secure the web3 ecosystem :) [pic.x.com/rxshaoaMnq] https://twitter.com/bluethroat_labs/status/2089821971941044602

**Media:**
- photo: https://pbs.twimg.com/media/HQK4uh1XQAAacVk.jpg — no alt text provided by author

**Links in post:** https://twitter.com/bluethroat_labs/status/2089821971941044602

**Quoted post (full text):**

    #### Quoted post — @bluethroat_labs — 2026-08-18 21:09 UTC (2026-08-18 22:09 WAT)
    
    - URL: https://x.com/bluethroat_labs/status/2089821971941044602
    - Metrics (at fetch): bookmark 2, impression 5193, like 25, quote 2, reply 0, retweet 1
    
    > And the streak continues :) https://t.co/8aYLRDZA3G https://t.co/FZTRev3ah1
    
    **Media:**
    - photo: https://pbs.twimg.com/media/HQCJ3FlbsAApZay.jpg — no alt text provided by author
    
    **Quoted post (full text):**
    
        #### Quoted post — @bluethroat_labs — 2026-08-17 10:46 UTC (2026-08-17 11:46 WAT)
        
        - URL: https://x.com/bluethroat_labs/status/2089302846642831475
        - Metrics (at fetch): bookmark 7, impression 7597, like 61, quote 3, reply 5, retweet 1
        
        > Celebrating another win for Bluethroat Labs with everyone on @immunefi 
        >
        > We have developed a robust, verifiable, deeply technical, human-in-the-loop system that helps us provide extremely deep security to distributed systems.
        >
        > Hit us up if you're looking for security partners :) [pic.x.com/JqGD7CaBxX] https://twitter.com/bluethroat_labs/status/2088147607734702500
        
        **Media:**
        - photo: https://pbs.twimg.com/media/HP6uw8Fa0AAtTLe.jpg — no alt text provided by author
        
        **Links in post:** https://twitter.com/bluethroat_labs/status/2088147607734702500
        
        **Quoted post (full text):**
        
            #### Quoted post — @bluethroat_labs — 2026-08-14 06:16 UTC (2026-08-14 07:16 WAT)
            
            - URL: https://x.com/bluethroat_labs/status/2088147607734702500
            - Metrics (at fetch): bookmark 4, impression 5832, like 46, quote 2, reply 0, retweet 1
            
            > New day, New bounty :)
            >
            > We deeply understand TEEs and distributed systems and everyday we strive to become even better. 
            >
            > And armed with our in-house experts, we are on a war-path to improve security standards acorss web3.
            >
            > Cheers to another bounty for our finding on @immunefi [pic.x.com/G2s8V3qt3S] https://twitter.com/bluethroat_labs/status/2087791137251795005
            
            **Media:**
            - photo: https://pbs.twimg.com/media/HPqW3cgb0AAMcHd.jpg — no alt text provided by author
            
            **Links in post:** https://twitter.com/bluethroat_labs/status/2087791137251795005
            
            **Quoted post (full text):**
            
                #### Quoted post — @bluethroat_labs — 2026-08-13 06:39 UTC (2026-08-13 07:39 WAT)
                
                - URL: https://x.com/bluethroat_labs/status/2087791137251795005
                - Metrics (at fetch): bookmark 1, impression 5747, like 29, quote 2, reply 0, retweet 1
                
                > At Bluethroat, we have a simple objective:
                > Wake up and stack receipts.
                >
                > Cheers on another confirmed finding on @immunefi 
                >
                > Onwards and Upwards [pic.x.com/kJCYiNbthW] https://twitter.com/bluethroat_labs/status/2084313356698325268
                
                **Media:**
                - photo: https://pbs.twimg.com/media/HPlSlkyaUAEK94S.jpg — no alt text provided by author
                
                **Links in post:** https://twitter.com/bluethroat_labs/status/2084313356698325268
                
                **Quoted post (full text):**
                
                    #### Quoted post — @bluethroat_labs — 2026-08-03 16:20 UTC (2026-08-03 17:20 WAT)
                    
                    - URL: https://x.com/bluethroat_labs/status/2084313356698325268
                    - Metrics (at fetch): bookmark 11, impression 11588, like 139, quote 2, reply 8, retweet 1
                    
                    > We just found a confirmed bug on @immunefi #immunefitribe 
                    >
                    > https://immunefi.com/s/ss/?severity=critical&status=confirmed&gifId=0&programType=bug-bounty
                    
                    **Links in post:** https://immunefi.com/s/ss/?severity=critical&status=confirmed&gifId=0&programType=bug-bounty
                    
                
            
        
    


---

## 2026-08-20 · Post · Nothing more beautiful than seeing the community building on top of open-sourced security public goo


Tags (automatic): TEE / enclave


### Post — @bluethroat_labs — 2026-08-20 13:46 UTC (2026-08-20 14:46 WAT)

- URL: https://x.com/bluethroat_labs/status/2090435200505229793
- Metrics (at fetch): bookmark 0, impression 554, like 4, quote 0, reply 2, retweet 2

> Nothing more beautiful than seeing the community building on top of open-sourced security public goods :)
>
> We are proud to have authored and maintaining The TEE Security Handbook.
>
> Hit us up if you want to contribute to TEE security in web3 :) https://t.co/u7wULv55Eb

**Quoted post (full text):**

    #### Quoted post — @1738660073910509568 — 2026-08-19 15:03 UTC (2026-08-19 16:03 WAT)
    
    - URL: https://x.com/1738660073910509568/status/2090092304103100845
    - Metrics (at fetch): bookmark 8, impression 2758, like 19, quote 3, reply 4, retweet 0
    
    > just built rootward; the first static auditor for web3 TEE protocols thanks to @saxenism for the @bluethroat_labs community.
    >
    > fun fact: supports @eigencloud out the box so you can audit your deployments before final release. 
    >
    > we ran our first public test on dstack and it was https://t.co/AlRYRCiJE5
    
    **Media:**
    - media `3_2090092295978684416` (details not returned by the API)
    


---

## 2026-08-18 · Post · And the streak continues :) https://t.co/8aYLRDZA3G https://t.co/FZTRev3ah1


### Post — @bluethroat_labs — 2026-08-18 21:09 UTC (2026-08-18 22:09 WAT)

- URL: https://x.com/bluethroat_labs/status/2089821971941044602
- Metrics (at fetch): bookmark 2, impression 5193, like 25, quote 2, reply 0, retweet 1

> And the streak continues :) https://t.co/8aYLRDZA3G https://t.co/FZTRev3ah1

**Media:**
- photo: https://pbs.twimg.com/media/HQCJ3FlbsAApZay.jpg — no alt text provided by author

**Quoted post (full text):**

    #### Quoted post — @bluethroat_labs — 2026-08-17 10:46 UTC (2026-08-17 11:46 WAT)
    
    - URL: https://x.com/bluethroat_labs/status/2089302846642831475
    - Metrics (at fetch): bookmark 7, impression 7597, like 61, quote 3, reply 5, retweet 1
    
    > Celebrating another win for Bluethroat Labs with everyone on @immunefi 
    >
    > We have developed a robust, verifiable, deeply technical, human-in-the-loop system that helps us provide extremely deep security to distributed systems.
    >
    > Hit us up if you're looking for security partners :) [pic.x.com/JqGD7CaBxX] https://twitter.com/bluethroat_labs/status/2088147607734702500
    
    **Media:**
    - photo: https://pbs.twimg.com/media/HP6uw8Fa0AAtTLe.jpg — no alt text provided by author
    
    **Links in post:** https://twitter.com/bluethroat_labs/status/2088147607734702500
    
    **Quoted post (full text):**
    
        #### Quoted post — @bluethroat_labs — 2026-08-14 06:16 UTC (2026-08-14 07:16 WAT)
        
        - URL: https://x.com/bluethroat_labs/status/2088147607734702500
        - Metrics (at fetch): bookmark 4, impression 5832, like 46, quote 2, reply 0, retweet 1
        
        > New day, New bounty :)
        >
        > We deeply understand TEEs and distributed systems and everyday we strive to become even better. 
        >
        > And armed with our in-house experts, we are on a war-path to improve security standards acorss web3.
        >
        > Cheers to another bounty for our finding on @immunefi [pic.x.com/G2s8V3qt3S] https://twitter.com/bluethroat_labs/status/2087791137251795005
        
        **Media:**
        - photo: https://pbs.twimg.com/media/HPqW3cgb0AAMcHd.jpg — no alt text provided by author
        
        **Links in post:** https://twitter.com/bluethroat_labs/status/2087791137251795005
        
        **Quoted post (full text):**
        
            #### Quoted post — @bluethroat_labs — 2026-08-13 06:39 UTC (2026-08-13 07:39 WAT)
            
            - URL: https://x.com/bluethroat_labs/status/2087791137251795005
            - Metrics (at fetch): bookmark 1, impression 5747, like 29, quote 2, reply 0, retweet 1
            
            > At Bluethroat, we have a simple objective:
            > Wake up and stack receipts.
            >
            > Cheers on another confirmed finding on @immunefi 
            >
            > Onwards and Upwards [pic.x.com/kJCYiNbthW] https://twitter.com/bluethroat_labs/status/2084313356698325268
            
            **Media:**
            - photo: https://pbs.twimg.com/media/HPlSlkyaUAEK94S.jpg — no alt text provided by author
            
            **Links in post:** https://twitter.com/bluethroat_labs/status/2084313356698325268
            
            **Quoted post (full text):**
            
                #### Quoted post — @bluethroat_labs — 2026-08-03 16:20 UTC (2026-08-03 17:20 WAT)
                
                - URL: https://x.com/bluethroat_labs/status/2084313356698325268
                - Metrics (at fetch): bookmark 11, impression 11588, like 139, quote 2, reply 8, retweet 1
                
                > We just found a confirmed bug on @immunefi #immunefitribe 
                >
                > https://immunefi.com/s/ss/?severity=critical&status=confirmed&gifId=0&programType=bug-bounty
                
                **Links in post:** https://immunefi.com/s/ss/?severity=critical&status=confirmed&gifId=0&programType=bug-bounty
                
            
        
    


---

## 2026-08-17 · Thread · Celebrating another win for Bluethroat Labs with everyone on @immunefi 


Tags (automatic): Platform: Immunefi


### Post — @bluethroat_labs — 2026-08-17 10:46 UTC (2026-08-17 11:46 WAT)

- URL: https://x.com/bluethroat_labs/status/2089302846642831475
- Metrics (at fetch): bookmark 7, impression 7597, like 61, quote 3, reply 5, retweet 1

> Celebrating another win for Bluethroat Labs with everyone on @immunefi 
>
> We have developed a robust, verifiable, deeply technical, human-in-the-loop system that helps us provide extremely deep security to distributed systems.
>
> Hit us up if you're looking for security partners :) [pic.x.com/JqGD7CaBxX] https://twitter.com/bluethroat_labs/status/2088147607734702500

**Media:**
- photo: https://pbs.twimg.com/media/HP6uw8Fa0AAtTLe.jpg — no alt text provided by author

**Links in post:** https://twitter.com/bluethroat_labs/status/2088147607734702500

**Quoted post (full text):**

    #### Quoted post — @bluethroat_labs — 2026-08-14 06:16 UTC (2026-08-14 07:16 WAT)
    
    - URL: https://x.com/bluethroat_labs/status/2088147607734702500
    - Metrics (at fetch): bookmark 4, impression 5832, like 46, quote 2, reply 0, retweet 1
    
    > New day, New bounty :)
    >
    > We deeply understand TEEs and distributed systems and everyday we strive to become even better. 
    >
    > And armed with our in-house experts, we are on a war-path to improve security standards acorss web3.
    >
    > Cheers to another bounty for our finding on @immunefi [pic.x.com/G2s8V3qt3S] https://twitter.com/bluethroat_labs/status/2087791137251795005
    
    **Media:**
    - photo: https://pbs.twimg.com/media/HPqW3cgb0AAMcHd.jpg — no alt text provided by author
    
    **Links in post:** https://twitter.com/bluethroat_labs/status/2087791137251795005
    
    **Quoted post (full text):**
    
        #### Quoted post — @bluethroat_labs — 2026-08-13 06:39 UTC (2026-08-13 07:39 WAT)
        
        - URL: https://x.com/bluethroat_labs/status/2087791137251795005
        - Metrics (at fetch): bookmark 1, impression 5747, like 29, quote 2, reply 0, retweet 1
        
        > At Bluethroat, we have a simple objective:
        > Wake up and stack receipts.
        >
        > Cheers on another confirmed finding on @immunefi 
        >
        > Onwards and Upwards [pic.x.com/kJCYiNbthW] https://twitter.com/bluethroat_labs/status/2084313356698325268
        
        **Media:**
        - photo: https://pbs.twimg.com/media/HPlSlkyaUAEK94S.jpg — no alt text provided by author
        
        **Links in post:** https://twitter.com/bluethroat_labs/status/2084313356698325268
        
        **Quoted post (full text):**
        
            #### Quoted post — @bluethroat_labs — 2026-08-03 16:20 UTC (2026-08-03 17:20 WAT)
            
            - URL: https://x.com/bluethroat_labs/status/2084313356698325268
            - Metrics (at fetch): bookmark 11, impression 11588, like 139, quote 2, reply 8, retweet 1
            
            > We just found a confirmed bug on @immunefi #immunefitribe 
            >
            > https://immunefi.com/s/ss/?severity=critical&status=confirmed&gifId=0&programType=bug-bounty
            
            **Links in post:** https://immunefi.com/s/ss/?severity=critical&status=confirmed&gifId=0&programType=bug-bounty
            
        
    


### Thread part 2 — @bluethroat_labs — 2026-08-17 12:46 UTC (2026-08-17 13:46 WAT)

- URL: https://x.com/bluethroat_labs/status/2089332922600083465
- Metrics (at fetch): bookmark 0, impression 112, like 0, quote 0, reply 0, retweet 0

> @immunefi Thank you ser. 
>
> We appreciate the incredible work that you have done at Immunefi to make things easier for whitehats and protocols alike :)


### Thread part 3 — @bluethroat_labs — 2026-08-17 12:46 UTC (2026-08-17 13:46 WAT)

- URL: https://x.com/bluethroat_labs/status/2089333022516765080
- Metrics (at fetch): bookmark 0, impression 77, like 2, quote 0, reply 0, retweet 0

> @hackerjedi666 @immunefi 🫡🫡


### Thread part 4 — @bluethroat_labs — 2026-08-17 12:46 UTC (2026-08-17 13:46 WAT)

- URL: https://x.com/bluethroat_labs/status/2089333112799207694
- Metrics (at fetch): bookmark 0, impression 94, like 1, quote 0, reply 1, retweet 0

> @0xAbix @immunefi Absolutely. Many more to come :)


### Thread part 5 — @bluethroat_labs — 2026-08-17 12:47 UTC (2026-08-17 13:47 WAT)

- URL: https://x.com/bluethroat_labs/status/2089333188170748116
- Metrics (at fetch): bookmark 0, impression 76, like 1, quote 0, reply 0, retweet 0

> @NancyDahiy_5 @immunefi 🫂🫂


### Thread part 6 — @bluethroat_labs — 2026-08-18 08:33 UTC (2026-08-18 09:33 WAT)

- URL: https://x.com/bluethroat_labs/status/2089631728977731720
- Metrics (at fetch): bookmark 0, impression 29, like 1, quote 0, reply 0, retweet 0

> @bajpaiharsh244 @immunefi Thank you ser :)


---

## 2026-08-14 · Post · New day, New bounty :)


Tags (automatic): Platform: Immunefi


### Post — @bluethroat_labs — 2026-08-14 06:16 UTC (2026-08-14 07:16 WAT)

- URL: https://x.com/bluethroat_labs/status/2088147607734702500
- Metrics (at fetch): bookmark 4, impression 5832, like 46, quote 2, reply 0, retweet 1

> New day, New bounty :)
>
> We deeply understand TEEs and distributed systems and everyday we strive to become even better. 
>
> And armed with our in-house experts, we are on a war-path to improve security standards acorss web3.
>
> Cheers to another bounty for our finding on @immunefi [pic.x.com/G2s8V3qt3S] https://twitter.com/bluethroat_labs/status/2087791137251795005

**Media:**
- photo: https://pbs.twimg.com/media/HPqW3cgb0AAMcHd.jpg — no alt text provided by author

**Links in post:** https://twitter.com/bluethroat_labs/status/2087791137251795005

**Quoted post (full text):**

    #### Quoted post — @bluethroat_labs — 2026-08-13 06:39 UTC (2026-08-13 07:39 WAT)
    
    - URL: https://x.com/bluethroat_labs/status/2087791137251795005
    - Metrics (at fetch): bookmark 1, impression 5747, like 29, quote 2, reply 0, retweet 1
    
    > At Bluethroat, we have a simple objective:
    > Wake up and stack receipts.
    >
    > Cheers on another confirmed finding on @immunefi 
    >
    > Onwards and Upwards [pic.x.com/kJCYiNbthW] https://twitter.com/bluethroat_labs/status/2084313356698325268
    
    **Media:**
    - photo: https://pbs.twimg.com/media/HPlSlkyaUAEK94S.jpg — no alt text provided by author
    
    **Links in post:** https://twitter.com/bluethroat_labs/status/2084313356698325268
    
    **Quoted post (full text):**
    
        #### Quoted post — @bluethroat_labs — 2026-08-03 16:20 UTC (2026-08-03 17:20 WAT)
        
        - URL: https://x.com/bluethroat_labs/status/2084313356698325268
        - Metrics (at fetch): bookmark 11, impression 11588, like 139, quote 2, reply 8, retweet 1
        
        > We just found a confirmed bug on @immunefi #immunefitribe 
        >
        > https://immunefi.com/s/ss/?severity=critical&status=confirmed&gifId=0&programType=bug-bounty
        
        **Links in post:** https://immunefi.com/s/ss/?severity=critical&status=confirmed&gifId=0&programType=bug-bounty
        
    


---

## 2026-08-13 · Post · At Bluethroat, we have a simple objective:


Tags (automatic): Platform: Immunefi


### Post — @bluethroat_labs — 2026-08-13 06:39 UTC (2026-08-13 07:39 WAT)

- URL: https://x.com/bluethroat_labs/status/2087791137251795005
- Metrics (at fetch): bookmark 1, impression 5747, like 29, quote 2, reply 0, retweet 1

> At Bluethroat, we have a simple objective:
> Wake up and stack receipts.
>
> Cheers on another confirmed finding on @immunefi 
>
> Onwards and Upwards [pic.x.com/kJCYiNbthW] https://twitter.com/bluethroat_labs/status/2084313356698325268

**Media:**
- photo: https://pbs.twimg.com/media/HPlSlkyaUAEK94S.jpg — no alt text provided by author

**Links in post:** https://twitter.com/bluethroat_labs/status/2084313356698325268

**Quoted post (full text):**

    #### Quoted post — @bluethroat_labs — 2026-08-03 16:20 UTC (2026-08-03 17:20 WAT)
    
    - URL: https://x.com/bluethroat_labs/status/2084313356698325268
    - Metrics (at fetch): bookmark 11, impression 11588, like 139, quote 2, reply 8, retweet 1
    
    > We just found a confirmed bug on @immunefi #immunefitribe 
    >
    > https://immunefi.com/s/ss/?severity=critical&status=confirmed&gifId=0&programType=bug-bounty
    
    **Links in post:** https://immunefi.com/s/ss/?severity=critical&status=confirmed&gifId=0&programType=bug-bounty
    


---

## 2026-08-05 · Post · Happy to share that Bluethroat Labs helped strengthen @PhalaNetwork’s TEE attestation tooling 🛡️


Tags (automatic): TEE / enclave


### Post — @bluethroat_labs — 2026-08-05 12:25 UTC (2026-08-05 13:25 WAT)

- URL: https://x.com/bluethroat_labs/status/2084979165892382955
- Metrics (at fetch): bookmark 2, impression 1301, like 15, quote 1, reply 0, retweet 2

> Happy to share that Bluethroat Labs helped strengthen @PhalaNetwork’s TEE attestation tooling 🛡️
>
> We reported a certificate-revocation validation gap in the JavaScript DCAP quote verifier. The Phala team fixed it in v0.5.3.
>
> Fruitful collaboration 🤝
>
> https://t.co/vlxx06GWpB


---

## 2026-08-03 · Thread · We just found a confirmed bug on @immunefi immunefitribe 


Tags (automatic): Platform: Immunefi


### Post — @bluethroat_labs — 2026-08-03 16:20 UTC (2026-08-03 17:20 WAT)

- URL: https://x.com/bluethroat_labs/status/2084313356698325268
- Metrics (at fetch): bookmark 11, impression 11588, like 139, quote 2, reply 8, retweet 1

> We just found a confirmed bug on @immunefi #immunefitribe 
>
> https://immunefi.com/s/ss/?severity=critical&status=confirmed&gifId=0&programType=bug-bounty

**Links in post:** https://immunefi.com/s/ss/?severity=critical&status=confirmed&gifId=0&programType=bug-bounty


### Thread part 2 — @bluethroat_labs — 2026-08-05 11:50 UTC (2026-08-05 12:50 WAT)

- URL: https://x.com/bluethroat_labs/status/2084970335376740579
- Metrics (at fetch): bookmark 0, impression 356, like 3, quote 0, reply 1, retweet 0

> @immunefi Thank you for the smooth process :)
>
> Can you help us out a little? We're having problems regarding the KYC for this payout.
>
> We are marked as a novice researcher on Immunefi, so can't open a ticket regarding the same.
>
> Left a message in #sr-help on Discord.


---

## 2026-07-28 · Post · https://t.co/BXO2qwkQFf


### Post — @bluethroat_labs — 2026-07-28 06:30 UTC (2026-07-28 07:30 WAT)

- URL: https://x.com/bluethroat_labs/status/2081990614405837057
- Metrics (at fetch): bookmark 8, impression 4308, like 8, quote 1, reply 0, retweet 0

> https://t.co/BXO2qwkQFf


---

## 2026-07-22 · Post · https://t.co/3qSnhIO7JW


### Post — @bluethroat_labs — 2026-07-22 09:45 UTC (2026-07-22 10:45 WAT)

- URL: https://x.com/bluethroat_labs/status/2079865288611225978
- Metrics (at fetch): bookmark 9, impression 3848, like 10, quote 1, reply 0, retweet 0

> https://t.co/3qSnhIO7JW


---

## 2026-07-21 · Post · Agents handling money on your behalf is NOT the future, it's the present.


Tags (automatic): AI-assisted hunting


### Post — @bluethroat_labs — 2026-07-21 20:52 UTC (2026-07-21 21:52 WAT)

- URL: https://x.com/bluethroat_labs/status/2079670785120293287
- Metrics (at fetch): bookmark 0, impression 363, like 3, quote 0, reply 0, retweet 1

> Agents handling money on your behalf is NOT the future, it's the present.
>
> We might be cookin a public good around this..... https://t.co/zEOwqben8P

**Quoted post** 2079667788692525234: not readable via the API (deleted, private, or withheld).


---

## 2026-05-08 · Post · Our founder @saxenism has been selected to present at @confcompsummit 2026, hosted by @linuxfoundati


Tags (automatic): TEE / enclave


### Post — @bluethroat_labs — 2026-05-08 07:56 UTC (2026-05-08 08:56 WAT)

- URL: https://x.com/bluethroat_labs/status/2052658880581456287
- Metrics (at fetch): bookmark 0, impression 1720, like 6, quote 1, reply 0, retweet 0

> Our founder @saxenism has been selected to present at @confcompsummit 2026, hosted by @linuxfoundation and @opaquesys 
>
> Topic:
> Trusted Execution, Broken Assumptions: Real-World Failures in TEE Attestation Systems
>
> What makes this meaningful is the room itself: CCS is not a Web3 https://t.co/FPieDHSB43

**Media:**
- photo: https://pbs.twimg.com/media/HHyCMVNb0AAYhg2.jpg — no alt text provided by author


---

## 2026-05-08 · Post · Our founder @saxenism has been selected to present at @confcompsummit 2026, hosted by @linuxfoundati


Tags (automatic): TEE / enclave


### Post — @bluethroat_labs — 2026-05-08 07:55 UTC (2026-05-08 08:55 WAT)

- URL: https://x.com/bluethroat_labs/status/2052658741989068997
- Metrics (at fetch): bookmark 0, impression 8, like 0, quote 0, reply 0, retweet 0

> Our founder @saxenism has been selected to present at @confcompsummit 2026, hosted by @linuxfoundation and @opaquesys.
>
> Topic:
> Trusted Execution, Broken Assumptions: Real-World Failures in TEE Attestation Systems
>
> What makes this meaningful is the room itself: CCS is not a Web3 https://t.co/8LpMQVEHIn

**Media:**
- photo: https://pbs.twimg.com/media/HHyCMVNb0AAYhg2.jpg — no alt text provided by author


---

## 2026-04-23 · Post · The next iteration of the TEE Security Handbook is live.


Tags (automatic): TEE / enclave


### Post — @bluethroat_labs — 2026-04-23 12:54 UTC (2026-04-23 13:54 WAT)

- URL: https://x.com/bluethroat_labs/status/2047297939249246343
- Metrics (at fetch): bookmark 3, impression 424, like 7, quote 1, reply 0, retweet 1

> The next iteration of the TEE Security Handbook is live.
>
> We have added a practical AWS Nitro Enclaves Workflow guide covering the full path from setup to attestation, vsock communication, KMS integration, debugging, and production readiness.
>
> The Handbook is an open-source


---

## 2026-04-23 · Post · Our founder, @saxenism, has been recognized as an ETHSecurity Badge holder.


### Post — @bluethroat_labs — 2026-04-23 09:58 UTC (2026-04-23 10:58 WAT)

- URL: https://x.com/bluethroat_labs/status/2047253790739628262
- Metrics (at fetch): bookmark 0, impression 284, like 4, quote 0, reply 0, retweet 0

> Our founder, @saxenism, has been recognized as an ETHSecurity Badge holder.
>
> That is a strong signal of the depth of security expertise behind Bluethroat Labs.
>
> We are here to turn hard-earned experience from the frontlines of Ethereum security into research, audits, and public https://t.co/3lGU3MHaZb

**Quoted post (full text):**

    #### Quoted post — @saxenism — 2026-04-23 09:35 UTC (2026-04-23 10:35 WAT)
    
    - URL: https://x.com/saxenism/status/2047248003497693600
    - Metrics (at fetch): bookmark 0, impression 444, like 10, quote 1, reply 1, retweet 0
    
    > Honoured to be selected as an ETHSecurity Badge holder.
    >
    > Ethereum security public goods do not magically fund themselves. Researchers, tools, education, infra, incident response, all of this needs real support.
    >
    > Glad to play a small part in actually making Ethereum safer. https://t.co/qaZbcel5me
    
    **Quoted post (full text):**
    
        #### Quoted post — @1988994064914739210 — 2026-04-22 15:14 UTC (2026-04-22 16:14 WAT)
        
        - URL: https://x.com/1988994064914739210/status/2046971025443713460
        - Metrics (at fetch): bookmark 3, impression 9230, like 68, quote 6, reply 2, retweet 3
        
        > With no further ado, meet the final 100 ETHSecurity Badge holders:
        >
        > @404ouch
        > @mzargham
        > @neburo
        > @arik_g
        > @ret2jazzy
        > @0xQuit
        > @simon_jentzsch
        > @zigtur
        > @Hudsonjameson
        > @pashov
        > @PabloSabbatella
        > @GalloDaSballo
        > @tanuki42_
        > @aviggiano
        > @claudijd
        > @parithosh_j
        > @saxenism
        > @RMacwha
        > @socrates1024
        > @TrustSecAudits
        > @bbarwik
        > @schaliasosvons
        > @lethalspoons
        > @eladernst
        > @HalbornSteve
        
    


---

## 2026-04-22 · Post · https://t.co/cavCI5Xs50


### Post — @bluethroat_labs — 2026-04-22 10:05 UTC (2026-04-22 11:05 WAT)

- URL: https://x.com/bluethroat_labs/status/2046893226712559797
- Metrics (at fetch): bookmark 2, impression 471, like 4, quote 0, reply 0, retweet 1

> https://t.co/cavCI5Xs50


---

## 2026-04-20 · Post · https://t.co/x363b8SIeR


### Post — @bluethroat_labs — 2026-04-20 09:59 UTC (2026-04-20 10:59 WAT)

- URL: https://x.com/bluethroat_labs/status/2046166797829964025
- Metrics (at fetch): bookmark 0, impression 201, like 3, quote 0, reply 0, retweet 0

> https://t.co/x363b8SIeR


---

## 2026-04-17 · Post · We have been observing the plethora of sophisticated attacks sweeping the entire web3 industry right


### Post — @bluethroat_labs — 2026-04-17 12:09 UTC (2026-04-17 13:09 WAT)

- URL: https://x.com/bluethroat_labs/status/2045112302932987967
- Metrics (at fetch): bookmark 0, impression 604, like 4, quote 0, reply 0, retweet 1

> We have been observing the plethora of sophisticated attacks sweeping the entire web3 industry right now and have been patiently cooking.
>
> Catch our one and only @saxenism for some juicy deets about our endeavours and how we at Bluethroat plan to tackle it. https://t.co/StmgoVifH2

**Quoted post (full text):**

    #### Quoted post — @saxenism — 2026-04-17 11:17 UTC (2026-04-17 12:17 WAT)
    
    - URL: https://x.com/saxenism/status/2045099241547374824
    - Metrics (at fetch): bookmark 0, impression 1034, like 9, quote 1, reply 3, retweet 1
    
    > The Drift hack was the most impactful in our industry in recent times, b/c it forced everyone out of their slumbers.
    >
    > The industry had to pause and notice the new realities of securing web3 protocol.
    >
    > Join me as we have a short discussion around it and the potential solutions. https://t.co/GT842q9Q22
    
    **Quoted post (full text):**
    
        #### Quoted post — @1091285940939571200 — 2026-04-17 08:40 UTC (2026-04-17 09:40 WAT)
        
        - URL: https://x.com/1091285940939571200/status/2045059795942826394
        - Metrics (at fetch): bookmark 2, impression 1445, like 15, quote 1, reply 2, retweet 5
        
        > We’re hosting a Space on the Drift hack today.
        >
        > $285M lost and honestly… it wasn’t even about the code.
        >
        > Going to break down what actually happened and what people are still missing.
        >
        > 🗓️ 17th April, 3:30 PM UTC with @saxenism and @Schnilch
        
        **Media:**
        - media `3_2045059626698518528` (details not returned by the API)
        
    


---

## 2026-04-15 · Post · https://t.co/bV6LjJ0O9P


### Post — @bluethroat_labs — 2026-04-15 09:13 UTC (2026-04-15 10:13 WAT)

- URL: https://x.com/bluethroat_labs/status/2044343290309570806
- Metrics (at fetch): bookmark 0, impression 184, like 4, quote 0, reply 0, retweet 0

> https://t.co/bV6LjJ0O9P


---

## 2026-04-09 · Post · In the era of autonomous exploit agents, only the paranoid survives.


Tags (automatic): AI-assisted hunting


### Post — @bluethroat_labs — 2026-04-09 11:01 UTC (2026-04-09 12:01 WAT)

- URL: https://x.com/bluethroat_labs/status/2042196198694797664
- Metrics (at fetch): bookmark 0, impression 134, like 1, quote 0, reply 0, retweet 0

> In the era of autonomous exploit agents, only the paranoid survives.
>
> Build like someone is already probing every commit you make, every oracle you trust, every library you use, every decision you make.


---

## 2026-04-08 · Post · https://t.co/LqRsWBbDPp


### Post — @bluethroat_labs — 2026-04-08 13:17 UTC (2026-04-08 14:17 WAT)

- URL: https://x.com/bluethroat_labs/status/2041868158571835631
- Metrics (at fetch): bookmark 0, impression 435, like 5, quote 1, reply 0, retweet 0

> https://t.co/LqRsWBbDPp


---

## 2026-04-03 · Post · https://t.co/adO9YthjRM


### Post — @bluethroat_labs — 2026-04-03 10:27 UTC (2026-04-03 11:27 WAT)

- URL: https://x.com/bluethroat_labs/status/2040013262230868171
- Metrics (at fetch): bookmark 2, impression 535, like 5, quote 1, reply 0, retweet 1

> https://t.co/adO9YthjRM


---

## 2026-03-24 · Post · https://t.co/eYEWvqa5fu


### Post — @bluethroat_labs — 2026-03-24 09:23 UTC (2026-03-24 10:23 WAT)

- URL: https://x.com/bluethroat_labs/status/2036373409563812243
- Metrics (at fetch): bookmark 1, impression 883, like 2, quote 1, reply 0, retweet 0

> https://t.co/eYEWvqa5fu


---

## 2026-03-18 · Post · https://t.co/KRvwk5cChh


### Post — @bluethroat_labs — 2026-03-18 09:03 UTC (2026-03-18 10:03 WAT)

- URL: https://x.com/bluethroat_labs/status/2034194089487520134
- Metrics (at fetch): bookmark 2, impression 1424, like 9, quote 1, reply 2, retweet 1

> https://t.co/KRvwk5cChh


---

## 2026-03-17 · Post · Our TEE security agent strikes again.


Tags (automatic): TEE / enclave, AI-assisted hunting


### Post — @bluethroat_labs — 2026-03-17 12:56 UTC (2026-03-17 13:56 WAT)

- URL: https://x.com/bluethroat_labs/status/2033890269553127539
- Metrics (at fetch): bookmark 0, impression 487, like 12, quote 0, reply 3, retweet 2

> Our TEE security agent strikes again.
>
> The agent identified 2 vulnerabilities in @OasisProtocol's live production system.
>
> Both responsibly disclosed &amp; patched.
>
> This is our thesis on domain-specific security at play. 
>
> At Bluethroat Labs, we believe protocols need an ecosystem https://t.co/p2gT0bnm40

**Media:**
- photo: https://pbs.twimg.com/media/HDnScFCbEAAZZ-n.jpg — no alt text provided by author


---

## 2026-03-13 · Post · https://t.co/kZqct9UScu


### Post — @bluethroat_labs — 2026-03-13 06:38 UTC (2026-03-13 07:38 WAT)

- URL: https://x.com/bluethroat_labs/status/2032345609924198619
- Metrics (at fetch): bookmark 7, impression 3630, like 20, quote 1, reply 0, retweet 6

> https://t.co/kZqct9UScu


---

## 2026-03-11 · Thread · Assumptions Kill Systems.


Tags (automatic): Blockchain / L1-L2 / bridge, TEE / enclave, AI-assisted hunting


### Post — @bluethroat_labs — 2026-03-11 11:18 UTC (2026-03-11 12:18 WAT)

- URL: https://x.com/bluethroat_labs/status/2031691249602978019
- Metrics (at fetch): bookmark 9, impression 10698, like 40, quote 1, reply 5, retweet 9

> Assumptions Kill Systems.
>
> Bluethroat Labs is now live.
>
> https://t.co/n5nlEAUnLO https://t.co/nCfZeE2XkQ

**Media:**
- photo: https://pbs.twimg.com/media/HDIAtTRbAAAiePW.jpg — no alt text provided by author


### Thread part 2 — @bluethroat_labs — 2026-03-11 11:18 UTC (2026-03-11 12:18 WAT)

- URL: https://x.com/bluethroat_labs/status/2031691252157251655
- Metrics (at fetch): bookmark 0, impression 469, like 7, quote 0, reply 1, retweet 0

> Most AI security is pattern matching against known vulnerabilities.
>
> We build domain-specific agents that reason about systems they have never seen before.
>
> One agent per domain. All of them sharing intelligence.
>
> An ecosystem of agents compounding knowledge about your system.


### Thread part 3 — @bluethroat_labs — 2026-03-11 11:18 UTC (2026-03-11 12:18 WAT)

- URL: https://x.com/bluethroat_labs/status/2031691254485090579
- Metrics (at fetch): bookmark 0, impression 288, like 7, quote 0, reply 0, retweet 0

> Confirmed findings across major TEE-heavy protocols in Web3.
> Novel vulnerabilities in live consensus codebases.
>
> Two domains. The methodology holds.
>
> More incoming.


---

## 2026-03-05 · Post · Bluethroat has been operating quietly behind the scenes.


Tags (automatic): AI-assisted hunting


### Post — @bluethroat_labs — 2026-03-05 13:14 UTC (2026-03-05 14:14 WAT)

- URL: https://x.com/bluethroat_labs/status/2029546164996235298
- Metrics (at fetch): bookmark 0, impression 1447, like 12, quote 1, reply 0, retweet 2

> Bluethroat has been operating quietly behind the scenes.
>
> Breaking systems.
> Accelerating AI in security.
> Working with teams across the Web3 stack.
>
> Much of that work is still under disclosure.
> But we will be talking about it soon.
>
> New Bluethroat website launches March 7 🛠️🔬 https://t.co/bcXMFUUGtI

**Media:**
- photo: https://pbs.twimg.com/media/HCplbX0bcAEKwvc.png — no alt text provided by author


---

## 2026-01-26 · Thread · 1/ Memory bus attacks: when “encrypted RAM” isn’t enough


Tags (automatic): TEE / enclave, AI-assisted hunting


### Post — @bluethroat_labs — 2026-01-26 14:44 UTC (2026-01-26 15:44 WAT)

- URL: https://x.com/bluethroat_labs/status/2015797898869657749
- Metrics (at fetch): bookmark 0, impression 777, like 4, quote 0, reply 1, retweet 1

> 1/ Memory bus attacks: when “encrypted RAM” isn’t enough
>
> TEEs love to say “don’t worry, memory is encrypted.”
> But there’s a weak link in that story: the path between the CPU and DRAM.
>
> If an attacker can tap the memory bus, they sometimes don’t need to break into your enclave at


### Thread part 2 — @bluethroat_labs — 2026-01-26 14:44 UTC (2026-01-26 15:44 WAT)

- URL: https://x.com/bluethroat_labs/status/2015797910903066930
- Metrics (at fetch): bookmark 0, impression 45, like 1, quote 0, reply 1, retweet 0

> 2/ What is the memory bus, really?
>
> Inside your machine, the CPU doesn’t talk to DRAM by magic.
>
> There’s a high‑speed channel (memory bus) carrying:
> • Addresses (where in RAM to read/write)
> • Data (the actual bytes)
> • Control signals (reads, writes, refresh, etc.)
>
> If an


### Thread part 3 — @bluethroat_labs — 2026-01-26 14:44 UTC (2026-01-26 15:44 WAT)

- URL: https://x.com/bluethroat_labs/status/2015797922877837392
- Metrics (at fetch): bookmark 0, impression 22, like 1, quote 0, reply 1, retweet 0

> 3/ Why TEEs care: the usual promise
>
> TEE marketing pitch:
> • Trust the CPU package
> • Don’t trust DRAM or the rest of the motherboard
> • Use memory encryption so even if someone dumps RAM, they only see ciphertext
>
> The assumption: attackers can see RAM contents, but can’t break


### Thread part 4 — @bluethroat_labs — 2026-01-26 14:44 UTC (2026-01-26 15:44 WAT)

- URL: https://x.com/bluethroat_labs/status/2015797935586656517
- Metrics (at fetch): bookmark 0, impression 17, like 1, quote 0, reply 1, retweet 0

> 4/ Threat model upgrade: from passive to active adversary
>
> Classic model: attacker can read DRAM (cold boot, DIMM yank, DMA, etc.).
>
> Memory bus attacker:
> • Can tap the bus (snoop data in transit)
> • Can sometimes inject or flip bits (active tampering)
> • Might control timing,


### Thread part 5 — @bluethroat_labs — 2026-01-26 14:44 UTC (2026-01-26 15:44 WAT)

- URL: https://x.com/bluethroat_labs/status/2015797947628425568
- Metrics (at fetch): bookmark 0, impression 26, like 1, quote 0, reply 1, retweet 0

> 5/ Why encrypted RAM is not a silver bullet
>
> Even with RAM encryption, bus traffic can leak:
> • Access patterns: Which addresses you touch, in what order
> • Timing: When bursts happen, how long they last
> • Volume: How much data is moved for a given operation
>
> For some TEEs,


### Thread part 6 — @bluethroat_labs — 2026-01-26 14:44 UTC (2026-01-26 15:44 WAT)

- URL: https://x.com/bluethroat_labs/status/2015797959624171971
- Metrics (at fetch): bookmark 0, impression 23, like 1, quote 0, reply 1, retweet 0

> 6/ Passive snooping scenario: confidentiality via patterns
>
> Imagine a TEE doing private key ops:
> • Each key operation touches specific memory regions
> • Different key bits or branches produce distinct access patterns
> • Memory bus probe records: address ranges, burst sequences,


### Thread part 7 — @bluethroat_labs — 2026-01-26 14:44 UTC (2026-01-26 15:44 WAT)

- URL: https://x.com/bluethroat_labs/status/2015797971607331325
- Metrics (at fetch): bookmark 0, impression 14, like 1, quote 0, reply 1, retweet 0

> 7/ Active bus manipulation: replay and substitution
>
> Stronger attacker: can modify traffic on the bus.
>
> Possible tricks:
> • Replay: Capture valid encrypted page/block and later replay it when CPU expects fresh data
> • Swap: Swap ciphertext blocks between addresses to confuse


### Thread part 8 — @bluethroat_labs — 2026-01-26 14:44 UTC (2026-01-26 15:44 WAT)

- URL: https://x.com/bluethroat_labs/status/2015797983724634255
- Metrics (at fetch): bookmark 0, impression 17, like 1, quote 0, reply 1, retweet 0

> 8/ Tee-specific twist: enclaves vs VMs vs worlds
>
> Different TEE designs feel bus attacks differently:
> • Arm TrustZone (world split) Often relies on secure DRAM regions + bus tagging If tags/signals on bus can be spoofed/observed, secure/normal distinction weakens
> • Intel SGX


### Thread part 9 — @bluethroat_labs — 2026-01-26 14:44 UTC (2026-01-26 15:44 WAT)

- URL: https://x.com/bluethroat_labs/status/2015797995741253759
- Metrics (at fetch): bookmark 0, impression 21, like 1, quote 0, reply 1, retweet 0

> 9/ Fault + bus combo: inject, then observe
>
> Memory bus attacks get nastier when combined with fault injection:
> • Glitch voltage / clock so CPU mis-executes one instruction
> • Use bus access to observe which lines reloaded or how data changed
> • Or inject a fault into ciphertext


### Thread part 10 — @bluethroat_labs — 2026-01-26 14:44 UTC (2026-01-26 15:44 WAT)

- URL: https://x.com/bluethroat_labs/status/2015798007762149867
- Metrics (at fetch): bookmark 0, impression 17, like 1, quote 0, reply 1, retweet 0

> 10/ Defenses: moving the trust boundary
>
> Mitigations tend to shift more into the trusted package:
> • Keep encryption engines inside the CPU package (so external bus sees only ciphertext)
> • Add integrity + replay protection (MACs, counters, RMP‑like tables)
> • Bind tweaks/IVs to


### Thread part 11 — @bluethroat_labs — 2026-01-26 14:44 UTC (2026-01-26 15:44 WAT)

- URL: https://x.com/bluethroat_labs/status/2015798019686633799
- Metrics (at fetch): bookmark 0, impression 18, like 1, quote 0, reply 1, retweet 0

> 11/ What this means for using TEEs in practice
>
> If your threat model includes:
> • Physical access to your board / socket
> • Malicious cloud operator with hardware‑level control
> • State‑level adversaries with lab capabilities
>
> …then memory bus attacks are part of the picture.


### Thread part 12 — @bluethroat_labs — 2026-01-26 14:44 UTC (2026-01-26 15:44 WAT)

- URL: https://x.com/bluethroat_labs/status/2015798032097550403
- Metrics (at fetch): bookmark 0, impression 382, like 2, quote 0, reply 1, retweet 0

> As always, a bite sized quiz for you guys
>
> You’re deploying a confidential ML inference service using AMD SEV-SNP to protect your proprietary AI model weights. Your security looks airtight:
>
> The Setup:
> • Full VM memory encrypted with AES-128 using per-VM keys ✅
> • AMD Secure


### Thread part 13 — @bluethroat_labs — 2026-01-26 14:44 UTC (2026-01-26 15:44 WAT)

- URL: https://x.com/bluethroat_labs/status/2015798044227469813
- Metrics (at fetch): bookmark 0, impression 218, like 1, quote 0, reply 0, retweet 0

> The answer for the previous thread is
>
> “Answer: B! 🎯
>
> VoltPillager is a hardware-based fault injection attack that bypasses Intel’s software patches for Plundervolt by directly manipulating the CPU voltage regulator.[securityaffairs]
> The attack breakdown:
>
> Background -


---

## 2026-01-24 · Thread · 1/ Fault injection attacks: when hardware glitches become weapons


Tags (automatic): ZK, TEE / enclave


### Post — @bluethroat_labs — 2026-01-24 14:00 UTC (2026-01-24 15:00 WAT)

- URL: https://x.com/bluethroat_labs/status/2015062050360471976
- Metrics (at fetch): bookmark 1, impression 433, like 4, quote 0, reply 1, retweet 2

> 1/ Fault injection attacks: when hardware glitches become weapons
>
> We've explored TrustZone, SGX, SEV, and side-channels—strong defenses against software threats. But what if an attacker tampers with the hardware itself to force errors?
>
> Enter fault injection: deliberately


### Thread part 2 — @bluethroat_labs — 2026-01-24 14:00 UTC (2026-01-24 15:00 WAT)

- URL: https://x.com/bluethroat_labs/status/2015062062423277649
- Metrics (at fetch): bookmark 0, impression 41, like 2, quote 0, reply 1, retweet 0

> 2/ The core idea: exploiting hardware imperfections
>
> Imagine a vault door with electronic locks. It works perfectly under normal conditions. But if you zap it with electricity or heat it up, the circuits might glitch—skipping a security check or revealing a code.
>
> Fault injection


### Thread part 3 — @bluethroat_labs — 2026-01-24 14:00 UTC (2026-01-24 15:00 WAT)

- URL: https://x.com/bluethroat_labs/status/2015062074389664078
- Metrics (at fetch): bookmark 0, impression 29, like 2, quote 0, reply 1, retweet 0

> 3/ Why TEEs are prime targets: trust in hardware
>
> TEEs like SGX or TrustZone assume the CPU behaves predictably. Faults break that assumption.
> • Transient faults: Temporary glitches that alter one computation without permanent damage.
> • Permanent faults: Rare, but possible with


### Thread part 4 — @bluethroat_labs — 2026-01-24 14:00 UTC (2026-01-24 15:00 WAT)

- URL: https://x.com/bluethroat_labs/status/2015062090697056573
- Metrics (at fetch): bookmark 0, impression 27, like 3, quote 0, reply 1, retweet 0

> 4/ The attacker's arsenal: tools for inducing faults
>
> Fault injection isn't sci-fi—it's practical with off-the-shelf gear:
> • Voltage glitching: Under/over-volt the CPU to cause timing errors in logic gates.
> • Clock glitching: Mess with clock signals to skip instructions or https://t.co/FWvPXrDEG9

**Media:**
- photo: https://pbs.twimg.com/media/G_bwSwRb0AAn_V0.png — no alt text provided by author


### Thread part 5 — @bluethroat_labs — 2026-01-24 14:00 UTC (2026-01-24 15:00 WAT)

- URL: https://x.com/bluethroat_labs/status/2015062103057699248
- Metrics (at fetch): bookmark 0, impression 57, like 2, quote 0, reply 1, retweet 0

> 5/ Targeting ARM TrustZone: breaking the world barrier
>
> In TrustZone's secure/normal split, faults can blur the lines.
> • Fault a Secure Monitor Call (SMC): Glitch the NS bit transition to execute normal code in secure mode.
> • Bypass PIN checks: Induce faults in authentication


### Thread part 6 — @bluethroat_labs — 2026-01-24 14:00 UTC (2026-01-24 15:00 WAT)

- URL: https://x.com/bluethroat_labs/status/2015062115422540023
- Metrics (at fetch): bookmark 0, impression 57, like 2, quote 0, reply 1, retweet 0

> 6/ Hitting Intel SGX: enclave breaches via faults
>
> SGX enclaves protect memory, but faults target the CPU's execution.
> • Voltage attacks: Tools like VoltPillager glitch SGX to skip integrity checks or leak sealed data.
> • Plundervolt (2019): Undervolting Intel CPUs to corrupt


### Thread part 7 — @bluethroat_labs — 2026-01-24 14:00 UTC (2026-01-24 15:00 WAT)

- URL: https://x.com/bluethroat_labs/status/2015062127518925024
- Metrics (at fetch): bookmark 0, impression 40, like 1, quote 0, reply 1, retweet 0

> 7/ Attacking AMD SEV: VM secrets via hardware tricks
>
> SEV's VM encryption relies on the AMD Secure Processor (ASP).
> • Heracles-like extensions: Fault the ASP to replay old ciphertexts or skip RMP checks.
> • CacheWarp (2023): Manipulated SEV cache to induce faults, altering


### Thread part 8 — @bluethroat_labs — 2026-01-24 14:00 UTC (2026-01-24 15:00 WAT)

- URL: https://x.com/bluethroat_labs/status/2015062139590025260
- Metrics (at fetch): bookmark 0, impression 13, like 1, quote 0, reply 1, retweet 0

> 8/ Real-world impacts: from labs to exploits
>
> These aren't just papers—they're demonstrated:
> • Fault attacks on TEE-based wallets: Extract seeds by glitching signature verification.
> • Automotive hacks: Fault ECUs in cars to bypass immobilizers.
> • Cloud scenarios: While harder


### Thread part 9 — @bluethroat_labs — 2026-01-24 14:00 UTC (2026-01-24 15:00 WAT)

- URL: https://x.com/bluethroat_labs/status/2015062151539700212
- Metrics (at fetch): bookmark 0, impression 21, like 1, quote 0, reply 1, retweet 0

> 9/ Defenses: hardening against glitches
>
> No perfect shield, but you can raise the bar:
>
> Software:
> • Redundant computations: Run ops multiple times and vote on results.
> • Control flow integrity: Add checksums to detect skipped instructions.
> • Constant-time code: Already helps,


### Thread part 10 — @bluethroat_labs — 2026-01-24 14:00 UTC (2026-01-24 15:00 WAT)

- URL: https://x.com/bluethroat_labs/status/2015062163594092810
- Metrics (at fetch): bookmark 1, impression 26, like 1, quote 0, reply 1, retweet 0

> 10/ Key takeaways: fault-aware TEE design
>
> Remember when deploying TEEs:
> ✅ Physical security matters—faults often need proximity.
> ✅ Combine with other protections (e.g., anti-tampering sensors).
> ✅ Test for faults: Use tools like ChipWhisperer to simulate attacks.
> ✅ New gens


### Thread part 11 — @bluethroat_labs — 2026-01-24 14:00 UTC (2026-01-24 15:00 WAT)

- URL: https://x.com/bluethroat_labs/status/2015062175581430067
- Metrics (at fetch): bookmark 0, impression 29, like 1, quote 0, reply 1, retweet 0

> Here's a single engaging scenario quiz on fault injection attacks:
>
> 🔐 Fault Injection Attack Challenge
>
> You're running a cryptocurrency hardware wallet using Intel SGX to protect private keys. Your security setup looks bulletproof:
>
> The Setup:
> Private keys stored in SGX enclave


### Thread part 12 — @bluethroat_labs — 2026-01-24 14:00 UTC (2026-01-24 15:00 WAT)

- URL: https://x.com/bluethroat_labs/status/2015062188378280316
- Metrics (at fetch): bookmark 0, impression 381, like 2, quote 0, reply 1, retweet 0

> Answer: B! 🎯
>
> Prime+Probe cache attack can extract AES keys from SGX enclaves by exploiting the table lookup pattern in your S-box implementation.
>
> Here's how it works:
>
> The vulnerability:
> Your code uses sbox which performs a secret-dependent memory access—the array index


### Thread part 13 — @bluethroat_labs — 2026-01-24 14:00 UTC (2026-01-24 15:00 WAT)

- URL: https://x.com/bluethroat_labs/status/2015062200373960871
- Metrics (at fetch): bookmark 0, impression 121, like 2, quote 0, reply 0, retweet 0

> The fix: Constant-time AES
> Modern crypto libraries use bitsliced implementations that avoid table lookups entirely:
>
> // All operations use bitwise logic on registers
> // Execution path independent of key value
>
> Three principles of constant-time crypto:
> Runtime independent of


---

## 2026-01-24 · Post · Quick poll: Which TEE attack sounds scariest to you?


Tags (automatic): TEE / enclave


### Post — @bluethroat_labs — 2026-01-24 13:45 UTC (2026-01-24 14:45 WAT)

- URL: https://x.com/bluethroat_labs/status/2015058253844005112
- Metrics (at fetch): bookmark 0, impression 157, like 3, quote 0, reply 0, retweet 0

> Quick poll: Which TEE attack sounds scariest to you?
>
> A) Foreshadow (speculative execution leaking secrets)
> B) https://t.co/vJBSoMYXfu (memory bus snooping)
> C) Heracles (ciphertext manipulation)
> D) StackWarp (exception handler hijacking)
>
> Vote + tell us why! 👇
>
> #CyberSecurity


---

## 2026-01-24 · Post · 🚨 Breaking: Another week, another SEV-SNP vulnerability


Tags (automatic): Race condition, TEE / enclave


### Post — @bluethroat_labs — 2026-01-24 13:30 UTC (2026-01-24 14:30 WAT)

- URL: https://x.com/bluethroat_labs/status/2015054479129801187
- Metrics (at fetch): bookmark 0, impression 295, like 6, quote 0, reply 0, retweet 1

> 🚨 Breaking: Another week, another SEV-SNP vulnerability
> At this point, “defeated by malicious hypervisor” is becoming a genre of academic papers
>
> https://t.co/kaLKhZ0WCW
>
> The race between TEE vendors and researchers is heating up 🔥
>
> #AMDSEV #ConfidentialComputing #InfoSec


---

## 2026-01-23 · Thread · 1/ Side-channel attacks: when isolation isn't enough


Tags (automatic): Blockchain / L1-L2 / bridge, TEE / enclave


### Post — @bluethroat_labs — 2026-01-23 10:30 UTC (2026-01-23 11:30 WAT)

- URL: https://x.com/bluethroat_labs/status/2014646880156975173
- Metrics (at fetch): bookmark 0, impression 716, like 10, quote 1, reply 1, retweet 4

> 1/ Side-channel attacks: when isolation isn't enough
>
> We've covered TrustZone, SGX, and SEV—all provide strong hardware isolation to protect secrets.
>
> But there's a catch: even when an attacker can't directly read your data, they can sometimes infer it by watching how the


### Thread part 2 — @bluethroat_labs — 2026-01-23 10:30 UTC (2026-01-23 11:30 WAT)

- URL: https://x.com/bluethroat_labs/status/2014646892052045982
- Metrics (at fetch): bookmark 0, impression 71, like 4, quote 0, reply 1, retweet 0

> 2/ The fundamental problem: shared hardware leaks information
>
> Analogy time: Imagine a bank with individual safe deposit boxes (like TEE enclaves).
>
> • You can't see inside someone else's box (isolation works ✅)
> • But you CAN observe: how long they spend at their box, which


### Thread part 3 — @bluethroat_labs — 2026-01-23 10:30 UTC (2026-01-23 11:30 WAT)

- URL: https://x.com/bluethroat_labs/status/2014646908908929035
- Metrics (at fetch): bookmark 0, impression 32, like 5, quote 0, reply 1, retweet 0

> 3/ Why TEEs are vulnerable: the micro-architecture is shared
>
> Remember how we said TEEs create isolated execution contexts? That's true for logical separation.
>
> But underneath, they all share the same physical CPU components:
>
> • L1/L2/L3 caches
> • Branch predictors
> • TLBs https://t.co/LD76QpJnHE

**Media:**
- photo: https://pbs.twimg.com/media/G_V2sAibEAAOe2-.png — no alt text provided by author


### Thread part 4 — @bluethroat_labs — 2026-01-23 10:30 UTC (2026-01-23 11:30 WAT)

- URL: https://x.com/bluethroat_labs/status/2014646921244426569
- Metrics (at fetch): bookmark 0, impression 19, like 3, quote 0, reply 1, retweet 0

> 4/ Cache timing attacks: the classic side-channel
>
> The most common technique: exploiting CPU caches.
>
> How it works:
>
> • Your TEE code accesses memory → data loads into cache (fast)
> • Attacker measures access times to same cache lines from outside
> • Fast access = data was in


### Thread part 5 — @bluethroat_labs — 2026-01-23 10:30 UTC (2026-01-23 11:30 WAT)

- URL: https://x.com/bluethroat_labs/status/2014646933206479007
- Metrics (at fetch): bookmark 0, impression 16, like 3, quote 0, reply 1, retweet 0

> 5/ Speculative execution attacks: Foreshadow and friends
>
> Modern CPUs predict the future to go faster—but get it wrong sometimes.
>
> The attack flow:
> • CPU speculatively executes instructions before knowing if they're allowed
> • Speculative path accesses secret data and loads it


### Thread part 6 — @bluethroat_labs — 2026-01-23 10:30 UTC (2026-01-23 11:30 WAT)

- URL: https://x.com/bluethroat_labs/status/2014646945105772936
- Metrics (at fetch): bookmark 0, impression 23, like 3, quote 0, reply 1, retweet 0

> 6/ The attacker's toolkit: popular side-channel techniques
>
> Different side-channels exploit different shared resources:
>
> Cache-based:
>
> • Prime+Probe: Fill cache, let victim run, measure which lines were evicted
> • Flush+Reload: Flush cache lines, let victim run, time reloads
> •


### Thread part 7 — @bluethroat_labs — 2026-01-23 10:30 UTC (2026-01-23 11:30 WAT)

- URL: https://x.com/bluethroat_labs/status/2014646957046956408
- Metrics (at fetch): bookmark 0, impression 34, like 3, quote 0, reply 1, retweet 1

> 7/ Real-world examples: when theory becomes practice
>
> Foreshadow (2018): Extracted Intel SGX enclave secrets including attestation keys
> • Fixed with microcode updates + disabling hyper-threading
> • Newer CPUs have hardware mitigations
>
> https://t.co/vJBSoMZv52 (2025): Attacked


### Thread part 8 — @bluethroat_labs — 2026-01-23 10:30 UTC (2026-01-23 11:30 WAT)

- URL: https://x.com/bluethroat_labs/status/2014646969021689968
- Metrics (at fetch): bookmark 0, impression 19, like 3, quote 0, reply 1, retweet 0

> 8/ Defense strategies: fighting back against side-channels
>
> Side-channels are hard to eliminate completely, but you can reduce risk:
>
> Software mitigations:
> • Constant-time algorithms: Ensure execution doesn't vary based on secret data
> • Data-oblivious code: Access memory in


### Thread part 9 — @bluethroat_labs — 2026-01-23 10:30 UTC (2026-01-23 11:30 WAT)

- URL: https://x.com/bluethroat_labs/status/2014646980954488888
- Metrics (at fetch): bookmark 0, impression 19, like 3, quote 0, reply 1, retweet 0

> 9/ The hard truth: perfect isolation is impossible
>
> Side-channels exist because of a fundamental tension:
>
> Performance requires:
> • Shared caches (avoid DRAM latency)
> • Speculative execution (hide branch costs)
> • Parallel execution (utilize multiple cores)
>
> Security requires:


### Thread part 10 — @bluethroat_labs — 2026-01-23 10:30 UTC (2026-01-23 11:30 WAT)

- URL: https://x.com/bluethroat_labs/status/2014646992820175261
- Metrics (at fetch): bookmark 0, impression 20, like 3, quote 0, reply 1, retweet 0

> 10/ Key takeaways: building side-channel aware systems
>
> When using TEEs, remember:
> ✅ Hardware isolation stops direct attacks—but not indirect observation
> ✅ Sensitive algorithms need constant-time implementations
> ✅ Physical access expands attacker capabilities significantly
> ✅


### Thread part 11 — @bluethroat_labs — 2026-01-23 10:30 UTC (2026-01-23 11:30 WAT)

- URL: https://x.com/bluethroat_labs/status/2014647004807496034
- Metrics (at fetch): bookmark 0, impression 83, like 4, quote 0, reply 1, retweet 0

> Lets see if you have what it takes to be a hacker.
>
> QUIZ
> You're implementing AES-256 encryption inside an Intel SGX enclave to protect API keys. You've been careful about security:
>
> The Setup:
> • AES encryption runs entirely inside SGX enclave ✅
> • Memory is encrypted by SGX's


### Thread part 12 — @bluethroat_labs — 2026-01-23 10:30 UTC (2026-01-23 11:30 WAT)

- URL: https://x.com/bluethroat_labs/status/2014647017029697604
- Metrics (at fetch): bookmark 0, impression 102, like 5, quote 0, reply 0, retweet 0

> ANSWER TO THE PREVIOUS THREAD :
>
> Answer: B! 🎯
>
> Heracles is a chosen-plaintext attack that exploits fundamental properties of AMD SEV-SNP's AES-XEX encryption scheme.
>
> Here's how it works:
> • Hypervisor can READ encrypted VM memory ciphertext (allowed by design)
> • SEV-SNP uses


---

## 2026-01-21 · Thread · 1/ AMD SEV: VM-level fortresses for the cloud


Tags (automatic): Blockchain / L1-L2 / bridge, TEE / enclave


### Post — @bluethroat_labs — 2026-01-21 15:43 UTC (2026-01-21 16:43 WAT)

- URL: https://x.com/bluethroat_labs/status/2014000942828728633
- Metrics (at fetch): bookmark 2, impression 288, like 5, quote 0, reply 1, retweet 2

> 1/ AMD SEV: VM-level fortresses for the cloud
>
> Shifting from Intel's SGX, AMD Secure Encrypted Virtualization (SEV) takes a different approach—protecting entire virtual machines instead of individual processes.
>
> It's like building secure, isolated buildings instead of just secure


### Thread part 2 — @bluethroat_labs — 2026-01-21 15:43 UTC (2026-01-21 16:43 WAT)

- URL: https://x.com/bluethroat_labs/status/2014000954694332636
- Metrics (at fetch): bookmark 0, impression 54, like 4, quote 0, reply 1, retweet 0

> 2/ SEV basics: confidential VMs (cloud or on-prem)
>
> At its heart, SEV lets you run entire virtual machines where the memory is encrypted, shielding it from the hypervisor and other VMs.
>
> Analogy: Think of a cloud data center as a massive apartment complex.
>
> • Normal VMs =


### Thread part 3 — @bluethroat_labs — 2026-01-21 15:43 UTC (2026-01-21 16:43 WAT)

- URL: https://x.com/bluethroat_labs/status/2014000966706905240
- Metrics (at fetch): bookmark 0, impression 36, like 4, quote 0, reply 1, retweet 0

> 3/ The SEV evolution: three generations of protection
>
> AMD didn't stop at basic memory encryption—SEV evolved across three major versions:
>
> • SEV (Gen 1): Encrypts VM memory with per-VM keys; hypervisor sees only ciphertext
> • SEV-ES (Encrypted State): encrypts/protects guest


### Thread part 4 — @bluethroat_labs — 2026-01-21 15:43 UTC (2026-01-21 16:43 WAT)

- URL: https://x.com/bluethroat_labs/status/2014000978627067945
- Metrics (at fetch): bookmark 0, impression 31, like 4, quote 0, reply 1, retweet 0

> 4/ Hardware architecture: the AMD Secure Processor
>
> AMD doesn't trust software to manage keys—that job goes to dedicated hardware.
>
> • AMD Secure Processor (ASP): A separate security co-processor embedded in the EPYC CPU die that manages encryption keys
> • Per-VM keys: Each VM


### Thread part 5 — @bluethroat_labs — 2026-01-21 15:43 UTC (2026-01-21 16:43 WAT)

- URL: https://x.com/bluethroat_labs/status/2014000990597620067
- Metrics (at fetch): bookmark 0, impression 23, like 4, quote 0, reply 1, retweet 0

> 5/ Memory encryption: protecting data in DRAM
>
> SEV encrypts VM memory at the hardware level, outside software control.
>
> • C-bit in page tables: A special bit marks pages as "encrypted"; hardware automatically encrypts them before writing to DRAM
> • ASID-based keys: The memory


### Thread part 6 — @bluethroat_labs — 2026-01-21 15:43 UTC (2026-01-21 16:43 WAT)

- URL: https://x.com/bluethroat_labs/status/2014001002521977135
- Metrics (at fetch): bookmark 0, impression 24, like 4, quote 0, reply 1, retweet 0

> 6/ SEV-SNP: closing the integrity gap
>
> Original SEV encrypted data but couldn't prevent all memory manipulation attacks. SEV-SNP fixes this.
>
> • Reverse Map Table (RMP): A hardware-managed table that tracks ownership of every physical page, preventing the hypervisor from


### Thread part 7 — @bluethroat_labs — 2026-01-21 15:43 UTC (2026-01-21 16:43 WAT)

- URL: https://x.com/bluethroat_labs/status/2014001020314190303
- Metrics (at fetch): bookmark 0, impression 25, like 4, quote 0, reply 1, retweet 0

> 7/ Attestation: proving your VM is genuine
>
> Like other TEEs, SEV provides cryptographic proof of what's running.
>
> • Launch measurement: During VM boot, the ASP calculates a hash of the initial memory and VM configuration
> • Attestation report: The ASP signs this measurement with https://t.co/ZeYHHJCZK0

**Media:**
- photo: https://pbs.twimg.com/media/G_MrQTmaoAE9VPx.jpg — no alt text provided by author


### Thread part 8 — @bluethroat_labs — 2026-01-21 15:43 UTC (2026-01-21 16:43 WAT)

- URL: https://x.com/bluethroat_labs/status/2014001032687489184
- Metrics (at fetch): bookmark 0, impression 24, like 4, quote 0, reply 1, retweet 0

> 8/ The hypervisor in SEV: powerful but blinded
>
> The hypervisor still controls the VM lifecycle but with limited visibility.
>
> • Still manages: CPU scheduling, memory allocation, I/O, and network
> • Can't see: VM memory contents (encrypted), register state (in SEV-ES), or modify


### Thread part 9 — @bluethroat_labs — 2026-01-21 15:44 UTC (2026-01-21 16:44 WAT)

- URL: https://x.com/bluethroat_labs/status/2014001044955791646
- Metrics (at fetch): bookmark 0, impression 73, like 5, quote 0, reply 1, retweet 0

> DID YOU FOLLOW ALONG ???? let's see
>
> You're running a confidential database workload in an AMD SEV-SNP protected VM on a public cloud. Your setup looks solid:
>
> The Setup:
> VM memory encrypted with per-VM AES-128 key managed by AMD Secure Processor ✅
> SEV-SNP enabled with RMP


### Thread part 10 — @bluethroat_labs — 2026-01-21 15:44 UTC (2026-01-21 16:44 WAT)

- URL: https://x.com/bluethroat_labs/status/2014001057131831472
- Metrics (at fetch): bookmark 0, impression 62, like 4, quote 0, reply 0, retweet 0

> And the answer to Intel SGX quiz is .................
>
> "Answer: B! 🎯
>
> Foreshadow (L1TF - L1 Terminal Fault) is a speculative execution attack that can extract data from SGX enclaves by exploiting how Intel CPUs handle speculative memory accesses.
>
> Here's what happens:
> •


---

## 2026-01-20 · Thread · 1/ Intel SGX: enclaves for app-level fortresses


Tags (automatic): ZK, TEE / enclave


### Post — @bluethroat_labs — 2026-01-20 14:25 UTC (2026-01-20 15:25 WAT)

- URL: https://x.com/bluethroat_labs/status/2013618885699027328
- Metrics (at fetch): bookmark 3, impression 925, like 7, quote 1, reply 1, retweet 1

> 1/ Intel SGX: enclaves for app-level fortresses
>
> Shifting gears from ARM's world-split, Intel Software Guard Extensions (SGX) takes a different tack—focusing on isolating specific parts of applications rather than entire systems.
>
> It’s like carving out secure vaults within a


### Thread part 2 — @bluethroat_labs — 2026-01-20 14:25 UTC (2026-01-20 15:25 WAT)

- URL: https://x.com/bluethroat_labs/status/2013618897635942824
- Metrics (at fetch): bookmark 0, impression 92, like 5, quote 0, reply 1, retweet 0

> 2/ SGX basics: building protected bubbles
>
> At its heart, SGX lets you create "enclaves"—isolated regions of memory where code and data are shielded from everything else, including the OS and hypervisor.
>
> Analogy time: Think of the host system as a bustling apartment building.
> •


### Thread part 3 — @bluethroat_labs — 2026-01-20 14:25 UTC (2026-01-20 15:25 WAT)

- URL: https://x.com/bluethroat_labs/status/2013618909510091165
- Metrics (at fetch): bookmark 0, impression 61, like 5, quote 0, reply 1, retweet 0

> 3/ The enclave lifecycle: from creation to execution
>
> Launching an enclave is a deliberate process to ensure integrity from the start.
> • ECREATE: Sets up the enclave structure.
> • EADD/EEXTEND: Loads code/data pages, measuring (hashing) them as you add more data.
> • EINIT: Seals


### Thread part 4 — @bluethroat_labs — 2026-01-20 14:25 UTC (2026-01-20 15:25 WAT)

- URL: https://x.com/bluethroat_labs/status/2013618924706017456
- Metrics (at fetch): bookmark 0, impression 43, like 4, quote 0, reply 1, retweet 0

> 4/ Hardware shields: CPU as the gatekeeper
>
> Intel doesn't trust software layers; the CPU enforces isolation directly.
>
> • Enclave Page Cache (EPC): Special RAM reserved for enclaves, managed by hardware.
> EPC is carved out of DRAM and protected as Processor Reserved Memory (PRM), https://t.co/Rp0RGpE8bG

**Media:**
- photo: https://pbs.twimg.com/media/G_HPveSagAEBKlh.jpg — no alt text provided by author


### Thread part 5 — @bluethroat_labs — 2026-01-20 14:25 UTC (2026-01-20 15:25 WAT)

- URL: https://x.com/bluethroat_labs/status/2013618940749193513
- Metrics (at fetch): bookmark 0, impression 35, like 4, quote 0, reply 1, retweet 0

> 5/ Memory protection: encryption and integrity in action
>
> Data doesn't sit vulnerable in RAM—SGX scrambles it.
>
> • On-chip encryption: Uses keys derived from hardware (unique per CPU/boot).
> • When pages leave the CPU (to RAM), they're encrypted and MAC'd for integrity.
> • Replay https://t.co/SXnSxpzKNp

**Media:**
- photo: https://pbs.twimg.com/media/G_HPwW8aoAQCrow.png — no alt text provided by author


### Thread part 6 — @bluethroat_labs — 2026-01-20 14:25 UTC (2026-01-20 15:25 WAT)

- URL: https://x.com/bluethroat_labs/status/2013618955831906364
- Metrics (at fetch): bookmark 0, impression 34, like 4, quote 0, reply 1, retweet 0

> 6/ Interfacing with the outside: calls across the boundary
>
> Enclaves aren't hermits—they need I/O, but safely.
>
> Think Linux syscalls : Enclaves call out (OCALLs) to untrusted code for things like file access, without exposing internals.
> • Host app calls in via ECALLs: Defined https://t.co/zKQqLCrXtZ

**Media:**
- photo: https://pbs.twimg.com/media/G_HPxP9aEAAuEVE.jpg — no alt text provided by author


### Thread part 7 — @bluethroat_labs — 2026-01-20 14:25 UTC (2026-01-20 15:25 WAT)

- URL: https://x.com/bluethroat_labs/status/2013618968406434226
- Metrics (at fetch): bookmark 0, impression 26, like 4, quote 0, reply 1, retweet 0

> 7/ Attestation: proving your enclave's pedigree
>
> To build remote trust, SGX provides cryptographic evidence.
>
> • Local attestation: Enclaves verify each other on the same machine.
> • Remote attestation: Generates a "quote" signed by Intel's service, including measurements and


### Thread part 8 — @bluethroat_labs — 2026-01-20 14:25 UTC (2026-01-20 15:25 WAT)

- URL: https://x.com/bluethroat_labs/status/2013618980364394864
- Metrics (at fetch): bookmark 0, impression 27, like 4, quote 0, reply 1, retweet 0

> 8/ The OS in SGX: powerful but blind
>
>  The OS/hypervisor still runs the show but with blinders on.
> • Allocates EPC but sees only ciphertext.
> • Handles paging (evicting enclave pages) but can't tamper undetected.
> • Can deny service (e.g., starve CPU time) but not steal secrets.


### Thread part 9 — @bluethroat_labs — 2026-01-20 14:25 UTC (2026-01-20 15:25 WAT)

- URL: https://x.com/bluethroat_labs/status/2013618992527876394
- Metrics (at fetch): bookmark 0, impression 95, like 5, quote 0, reply 1, retweet 0

> You're building a secure key management service using Intel SGX enclaves to protect cryptographic keys. Your enclave is properly configured:
>
> The Setup:
> Private keys stored in EPC (Enclave Page Cache) ✅
> Memory encryption active with MEE (Memory Encryption Engine) ✅
> Remote


### Thread part 10 — @bluethroat_labs — 2026-01-20 14:25 UTC (2026-01-20 15:25 WAT)

- URL: https://x.com/bluethroat_labs/status/2013619004464865612
- Metrics (at fetch): bookmark 0, impression 97, like 5, quote 0, reply 0, retweet 0

> Did you read the last thread carefully??
> The answer was..
>
> “Answer: B! 🎯
>
> Without an SMMU (System Memory Management Unit) or TZASC (TrustZone Address Space Controller), DMA-capable devices can bypass the NS bit protection and directly access Secure World physical memory.
>
> The NS


---

## 2026-01-19 · Thread · 1/ Before jumping into vendor specifics, remember: a TEE isn't a strict blueprint—it's more like a s


Tags (automatic): TEE / enclave, Memory corruption / native


### Post — @bluethroat_labs — 2026-01-19 15:48 UTC (2026-01-19 16:48 WAT)

- URL: https://x.com/bluethroat_labs/status/2013277489158594716
- Metrics (at fetch): bookmark 1, impression 764, like 6, quote 1, reply 1, retweet 3

> 1/ Before jumping into vendor specifics, remember: a TEE isn't a strict blueprint—it's more like a set of guidelines.
>
> The Confidential Computing Consortium (CCC) lays out key security must-haves, without dictating the exact tech to get there.
>
> Any TEE solution needs to deliver


### Thread part 2 — @bluethroat_labs — 2026-01-19 15:48 UTC (2026-01-19 16:48 WAT)

- URL: https://x.com/bluethroat_labs/status/2013277501523472835
- Metrics (at fetch): bookmark 0, impression 64, like 3, quote 0, reply 1, retweet 0

> 2/ Core guarantees: what every TEE must provide
>
> At minimum, a TEE has to nail these three pillars:
> • Data confidentiality: No unauthorized peeking at data while it's being processed inside the TEE.
> • Data integrity: Outsiders can't sneak in additions, deletions, or tweaks to


### Thread part 3 — @bluethroat_labs — 2026-01-19 15:48 UTC (2026-01-19 16:48 WAT)

- URL: https://x.com/bluethroat_labs/status/2013277518564843843
- Metrics (at fetch): bookmark 0, impression 62, like 3, quote 0, reply 1, retweet 0

> 3/ Vendor showdown: how the big players build TEEs
>
> With those core rules in mind, let's zoom in on the top dogs implementing them.
>
> We’ll look at three families:
> • ARM TrustZone (world split)
> • Intel SGX (process-level enclaves)
> • AMD SEV (VM-level protection)
>
> Starting with https://t.co/AAoFYRIWm1

**Media:**
- photo: https://pbs.twimg.com/media/G_CZO9uXcAA8X6E.jpg — no alt text provided by author


### Thread part 4 — @bluethroat_labs — 2026-01-19 15:49 UTC (2026-01-19 16:49 WAT)

- URL: https://x.com/bluethroat_labs/status/2013277531407802503
- Metrics (at fetch): bookmark 0, impression 27, like 3, quote 0, reply 1, retweet 0

> 4/ ARM TrustZone: two worlds, one chip
>
> Imagine two parallel universes on the same hardware: a Secure World (everything verified and trusted) and a Normal World (where trust is optional, and chaos reigns).
>
> Analogy time: It's like a hospital setup.
> • Normal World = the waiting


### Thread part 5 — @bluethroat_labs — 2026-01-19 15:49 UTC (2026-01-19 16:49 WAT)

- URL: https://x.com/bluethroat_labs/status/2013277543898444206
- Metrics (at fetch): bookmark 0, impression 34, like 3, quote 0, reply 1, retweet 0

> 5/ The magic bit: ARM's secret sauce
>
> The switch between worlds? It's all thanks to the Secure Configuration Register (SCR) and its "Non-secure Bit" (NS).
>
> • NS = 1: You're in the non-secure (Normal) world.
> • NS = 0: Locked into secure mode.
>
> This bit is one of the key anchors


### Thread part 6 — @bluethroat_labs — 2026-01-19 15:49 UTC (2026-01-19 16:49 WAT)

- URL: https://x.com/bluethroat_labs/status/2013277556607246418
- Metrics (at fetch): bookmark 0, impression 25, like 3, quote 0, reply 1, retweet 0

> 6/ Hardware enforcers: the tech that makes it real
>
> ARM doesn't rely on software goodwill; it's hardware all the way down with three key pieces:
>
> • AMBA AXI bus: Divides the whole System-on-Chip (SoC). Carries an extra signal bit (like AWPROT for writes, ARPROT for reads) to tag


### Thread part 7 — @bluethroat_labs — 2026-01-19 15:49 UTC (2026-01-19 16:49 WAT)

- URL: https://x.com/bluethroat_labs/status/2013277576756601211
- Metrics (at fetch): bookmark 0, impression 29, like 3, quote 0, reply 1, retweet 0

> 7/ Bridging the gap: how Normal talks to Secure
>
> If Secure World is so isolated, how does Normal World ever tap into it?
> Think Linux syscalls: User apps (Normal) request kernel (Secure) help for sensitive stuff like network access, without ever touching the raw hardware.
>
> ARM https://t.co/soiYJ234Kn

**Media:**
- photo: https://pbs.twimg.com/media/G_CZSPJXYAAm9lg.png — no alt text provided by author


### Thread part 8 — @bluethroat_labs — 2026-01-19 15:49 UTC (2026-01-19 16:49 WAT)

- URL: https://x.com/bluethroat_labs/status/2013277590060986622
- Metrics (at fetch): bookmark 0, impression 30, like 3, quote 0, reply 1, retweet 0

> 8/ The fine print: nuances in the switch
>
> Crossing from Normal to Secure isn't instant magic—it involves checks galore:
> • System validations to ensure legitimacy.
> • Access controls to block unauthorized jumps.
> • NS bit toggling to enforce the mode shift.
>
> Only trusted


### Thread part 9 — @bluethroat_labs — 2026-01-19 15:49 UTC (2026-01-19 16:49 WAT)

- URL: https://x.com/bluethroat_labs/status/2013277602694176877
- Metrics (at fetch): bookmark 0, impression 87, like 4, quote 0, reply 1, retweet 0

> Quiz time, let's see if you've been following along.
>
> You're a developer building a payment app on an ARM device with TrustZone. Your sensitive PIN validation logic runs in the Secure World, while the rest of your app (UI, networking) runs in the Normal World.
>
> The Setup:
>
> PIN


### Thread part 10 — @bluethroat_labs — 2026-01-19 15:49 UTC (2026-01-19 16:49 WAT)

- URL: https://x.com/bluethroat_labs/status/2013277615117812137
- Metrics (at fetch): bookmark 0, impression 74, like 4, quote 0, reply 0, retweet 0

> Now the answer of the previous thread :
>
> Answer: B! 🎯
>
> While SGX encrypts memory and protects data confidentiality (blocking A, C, D), it can't hide which addresses you access. Attackers monitoring cache/memory bus can infer patterns. This is how attacks like


---

## 2026-01-16 · Thread · 1/ So you don’t trust your own computer…


Tags (automatic): TEE / enclave, AI-assisted hunting


### Post — @bluethroat_labs — 2026-01-16 14:36 UTC (2026-01-16 15:36 WAT)

- URL: https://x.com/bluethroat_labs/status/2012172015260901560
- Metrics (at fetch): bookmark 9, impression 1469, like 14, quote 1, reply 1, retweet 4

> 1/ So you don’t trust your own computer…
>
> You’re running code on a machine where the OS, hypervisor, and even the cloud provider might be compromised.
>
> You still want to keep your keys, models, or data secret. That’s the problem Trusted Execution Environments (TEEs) try to


### Thread part 2 — @bluethroat_labs — 2026-01-16 14:36 UTC (2026-01-16 15:36 WAT)

- URL: https://x.com/bluethroat_labs/status/2012172027285914022
- Metrics (at fetch): bookmark 0, impression 150, like 6, quote 0, reply 1, retweet 0

> 2/ The “safe inside the vault”
>
> Old analogy:
> • Vault = the whole machine
> • Manager = OS/hypervisor
> • Cash = your secrets
> A TEE is like installing a tamper‑resistant safe inside the vault.
>
> The manager still runs the vault, but the safe has its own lock and rules the manager


### Thread part 3 — @bluethroat_labs — 2026-01-16 14:36 UTC (2026-01-16 15:36 WAT)

- URL: https://x.com/bluethroat_labs/status/2012172039193493539
- Metrics (at fetch): bookmark 0, impression 116, like 6, quote 0, reply 1, retweet 0

> 3/ What TEEs actually guarantee (at a high level)
>
> For a generic production TEE, the goals look like this:
> • Code and data inside the TEE stay confidential from the rest of the system.
> • Their integrity is protected: other software can’t modify them arbitrarily.
> • You can


### Thread part 4 — @bluethroat_labs — 2026-01-16 14:36 UTC (2026-01-16 15:36 WAT)

- URL: https://x.com/bluethroat_labs/status/2012172051130560891
- Metrics (at fetch): bookmark 0, impression 83, like 5, quote 0, reply 1, retweet 0

> 4/ Hardware‑enforced isolation, not “software magic”
>
> The key idea: isolation is enforced by the processor, not by the OS.
> • Normal applications run in the “normal world.”
> • TEE applications run in a protected execution context with extra hardware checks.
> • The OS is still


### Thread part 5 — @bluethroat_labs — 2026-01-16 14:36 UTC (2026-01-16 15:36 WAT)

- URL: https://x.com/bluethroat_labs/status/2012172063155609660
- Metrics (at fetch): bookmark 0, impression 74, like 5, quote 0, reply 1, retweet 0

> 5/ Trusted Applications (TAs): who gets to run inside
>
> Code that runs in the TEE is often called a Trusted Application (TA):
> • It must be authorized: usually signed or at least cryptographically measured against some root of trust.
> • Who controls that root depends on the


### Thread part 6 — @bluethroat_labs — 2026-01-16 14:36 UTC (2026-01-16 15:36 WAT)

- URL: https://x.com/bluethroat_labs/status/2012172074975158670
- Metrics (at fetch): bookmark 0, impression 63, like 5, quote 0, reply 1, retweet 0

> 6/ TA isolation: safes within the safe
>
> Inside the TEE, different TAs don’t see each other’s secrets by default:
> • Each TA gets its own isolated memory region.
> • Hardware-level access control stops one TA from reading another TA’s data.
> • The TEE runtime enforces that calls


### Thread part 7 — @bluethroat_labs — 2026-01-16 14:36 UTC (2026-01-16 15:36 WAT)

- URL: https://x.com/bluethroat_labs/status/2012172091983053213
- Metrics (at fetch): bookmark 0, impression 72, like 5, quote 0, reply 1, retweet 0

> 7/ The OS is untrusted but still in the loop
>
> Even in a TEE world, the OS/hypervisor still:
> • Schedules CPU time
> • Manages I/O (network, disk, UI)
> • Handles syscalls on behalf of TEE code in many designs
>
> This means:
> • The OS can still drop or delay requests (DoS).
> • It can https://t.co/je0yXEePPQ

**Media:**
- photo: https://pbs.twimg.com/media/G-yr2rEbgAAQzlQ.png — no alt text provided by author


### Thread part 8 — @bluethroat_labs — 2026-01-16 14:36 UTC (2026-01-16 15:36 WAT)

- URL: https://x.com/bluethroat_labs/status/2012172104314307026
- Metrics (at fetch): bookmark 0, impression 64, like 5, quote 0, reply 1, retweet 0

> 8/ Enclaves: safes in RAM
>
> Many TEEs expose an abstraction often called an enclave (name varies by vendor):
> • Think of an enclave as a protected region of memory plus some code.
> • Data inside is visible in cleartext only while the CPU is executing in that enclave context.
> •


### Thread part 9 — @bluethroat_labs — 2026-01-16 14:36 UTC (2026-01-16 15:36 WAT)

- URL: https://x.com/bluethroat_labs/status/2012172116402339954
- Metrics (at fetch): bookmark 0, impression 65, like 5, quote 0, reply 1, retweet 0

> 9/ Memory encryption: scrambling outside the boundary
>
> To protect data “in use,” TEEs combine access control with memory encryption:
> • When enclave data leaves the CPU and sits in RAM, it’s encrypted with hardware‑managed keys.
> • Those keys are bound to that physical processor


### Thread part 10 — @bluethroat_labs — 2026-01-16 14:36 UTC (2026-01-16 15:36 WAT)

- URL: https://x.com/bluethroat_labs/status/2012172128276373607
- Metrics (at fetch): bookmark 0, impression 65, like 5, quote 0, reply 1, retweet 0

> 10/ Secure boot: how the chain of trust starts
>
> TEEs don’t mean much if the platform can boot arbitrary firmware:
> • Boot starts from a small, immutable root of trust burned into hardware.
> • Each next stage (bootloader, firmware, TEE runtime) is verified with digital signatures


### Thread part 11 — @bluethroat_labs — 2026-01-16 14:36 UTC (2026-01-16 15:36 WAT)

- URL: https://x.com/bluethroat_labs/status/2012172140121055496
- Metrics (at fetch): bookmark 0, impression 66, like 5, quote 0, reply 1, retweet 0

> 11/ Attestation: proving what’s inside the safe
>
> Remote attestation is what lets a remote party trust a TEE:
> • The TEE produces a signed report that includes measurements (hashes) of the code/config running inside.
> • A verifier checks this against known‑good values and the


### Thread part 12 — @bluethroat_labs — 2026-01-16 14:36 UTC (2026-01-16 15:36 WAT)

- URL: https://x.com/bluethroat_labs/status/2012172151969943553
- Metrics (at fetch): bookmark 0, impression 186, like 6, quote 0, reply 1, retweet 0

> 12/ One concept, many shapes
>
> Different vendors implement TEEs at different granularity:
> • Some isolate individual applications or components.
> • Some protect whole VMs.
> • Some split the CPU into a “secure world” and a “normal world.”


### Thread part 13 — @bluethroat_labs — 2026-01-16 14:36 UTC (2026-01-16 15:36 WAT)

- URL: https://x.com/bluethroat_labs/status/2012172169669947760
- Metrics (at fetch): bookmark 2, impression 191, like 8, quote 0, reply 3, retweet 0

> QUIZ TIME
>
> Q) Your company runs an AI model in the cloud that processes sensitive medical data. You're using Intel SGX enclaves to protect it.
>
> The Setup:
> • Model runs inside SGX enclave
> • Cloud provider has full root access to the host OS
> • Memory encryption is active
> • https://t.co/rj2zYM1GEH

**Media:**
- photo: https://pbs.twimg.com/media/G-yr7L8asAAx0Yi.jpg — no alt text provided by author


---

## 2026-01-10 · Post · Some big, heavy words.


Tags (automatic): AI-assisted hunting


### Post — @bluethroat_labs — 2026-01-10 12:38 UTC (2026-01-10 13:38 WAT)

- URL: https://x.com/bluethroat_labs/status/2009968123433357316
- Metrics (at fetch): bookmark 1, impression 178, like 2, quote 0, reply 0, retweet 0

> Some big, heavy words.
>
> But our internal LLM security agent (Asta) is seriously on fire right now, and it uses the same fundamentals.
>
> We are cooking so damn hard with Asta right now that once our work goes public, it will be one for the ages. https://t.co/dRg06i2L0p

**Quoted post (full text):**

    #### Quoted post — @saxenism — 2026-01-10 12:16 UTC (2026-01-10 13:16 WAT)
    
    - URL: https://x.com/saxenism/status/2009962510913536462
    - Metrics (at fetch): bookmark 3, impression 1219, like 15, quote 1, reply 2, retweet 0
    
    > How well you use LLMs in your workflow as a dev &amp; auditor is directly proportional to your ability to break down complex requirements into small, self-contained, well-scoped chunks and articulate their orchestration clearly.
    >
    > This exact set of properties has been the hallmark of
    


---

## 2026-01-10 · Post · How about we build a lint tool that flags common enclave footguns + side-channel anti-patterns? http


Tags (automatic): TEE / enclave


### Post — @bluethroat_labs — 2026-01-10 12:35 UTC (2026-01-10 13:35 WAT)

- URL: https://x.com/bluethroat_labs/status/2009967387765010701
- Metrics (at fetch): bookmark 0, impression 114, like 2, quote 0, reply 0, retweet 0

> How about we build a lint tool that flags common enclave footguns + side-channel anti-patterns? https://t.co/XuKF8UcAib

**Quoted post (full text):**

    #### Quoted post — @saxenism — 2026-01-09 06:50 UTC (2026-01-09 07:50 WAT)
    
    - URL: https://x.com/saxenism/status/2009518067144171826
    - Metrics (at fetch): bookmark 4, impression 1853, like 19, quote 2, reply 2, retweet 5
    
    > Please. If you're building TEE protocols, DO NOT discount microarchitectural side-channel exploits.
    >
    > If your protocol grows to a point where it becomes viable to exploit, you HAVE to assume sophisticated attackers going after you.
    >
    > Do not ignore the bare-minimums.
    > + No early
    


---

## 2025-12-15 · Post · The TEE Security Handbook just got another shoutout from the Eigen security team.


Tags (automatic): TEE / enclave


### Post — @bluethroat_labs — 2025-12-15 10:54 UTC (2025-12-15 11:54 WAT)

- URL: https://x.com/bluethroat_labs/status/2000519705371795847
- Metrics (at fetch): bookmark 0, impression 7841, like 13, quote 1, reply 1, retweet 1

> The TEE Security Handbook just got another shoutout from the Eigen security team.
>
> Amazing to see our work landing in real security conversations. https://t.co/GoCOflRohK

**Media:**
- video: https://pbs.twimg.com/amplify_video_thumb/1999778237334097921/img/6Nd2njNjNEt3NrIS.jpg — no alt text provided by author


---

## 2025-12-02 · Post · Another banger from our superstar!!


### Post — @bluethroat_labs — 2025-12-02 18:35 UTC (2025-12-02 19:35 WAT)

- URL: https://x.com/bluethroat_labs/status/1995924677634785374
- Metrics (at fetch): bookmark 0, impression 625, like 4, quote 0, reply 1, retweet 1

> Another banger from our superstar!!
>
> This is a detailed breakdown of the https://t.co/Z8t9W1LPsj from our security researcher @hackerjedi666 https://t.co/2m9f1ShTqh

**Quoted post** 1992148715084321202: not readable via the API (deleted, private, or withheld).


---

## 2025-12-02 · Post · The star-studded lineup of Bluethroat Labs just keeps on delivering. https://t.co/yv0O0mHryh


### Post — @bluethroat_labs — 2025-12-02 18:19 UTC (2025-12-02 19:19 WAT)

- URL: https://x.com/bluethroat_labs/status/1995920651203272985
- Metrics (at fetch): bookmark 0, impression 533, like 3, quote 0, reply 0, retweet 1

> The star-studded lineup of Bluethroat Labs just keeps on delivering. https://t.co/yv0O0mHryh

**Quoted post** 1990891573257925109: not readable via the API (deleted, private, or withheld).
