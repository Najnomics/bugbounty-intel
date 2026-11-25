# @al_f4lc0n — full verbatim X archive (security-relevant posts)

_Generated 2026-11-25 from the X API (full-archive search + timeline). Every post below is copied word-for-word; t.co links are expanded; quoted posts are inlined in full; media are listed with alt text when the author provided it. Posts are grouped by conversation (a thread = the author's root post followed by their own replies, oldest first). Groups are newest first. An agent without X access can rely on this file._

- Posts in this file: 13
- Conversations/threads: 13
- Oldest post captured: 2026-03-15
- Newest post captured: 2026-09-03


---

## 2026-09-03 · Post · Regarding the recent attack on @injective, I want to make one thing very clear: this incident has ab


Tags (automatic): Platform: Immunefi, Platform: Code4rena / Sherlock / Cantina


### Post — @al_f4lc0n — 2026-09-03 16:04 UTC (2026-09-03 17:04 WAT)

- URL: https://x.com/al_f4lc0n/status/2095543489920483753
- Metrics (at fetch): bookmark 43, impression 10308, like 144, quote 1, reply 10, retweet 5

> Regarding the recent attack on @injective, I want to make one thing very clear: this incident has absolutely nothing to do with me.
>
> To this day, Injective still has not paid me any bug bounty. I am no longer arguing about this, and I have zero expectations from them anymore. For the past few months, I have been busy researching other things. I have received about $300,000 USD in total from bug bounties and audit contests.
>
> I will use 10% of this money to expose their fraud. However, I have not decided how or when to spend this money yet. I do not plan to put too much of my time and energy into this right now. Because of this, the plan might be delayed for a very long time.
>
> I am currently hunting bugs on @immunefi and @cantinasecurity . Thank you to all the projects that value security and integrity.
>
> - https://immunefi.com/profile/f4lc0n
> - https://cantina.xyz/u/f4lc0n

**Links in post:** https://twitter.com/GoPlusSecurity/status/2095119564409651639, https://immunefi.com/profile/f4lc0n, https://cantina.xyz/u/f4lc0n

**Quoted post (full text):**

    #### Quoted post — @GoPlusSecurity — 2026-09-02 12:00 UTC (2026-09-02 13:00 WAT)
    
    - URL: https://x.com/GoPlusSecurity/status/2095119564409651639
    - Metrics (at fetch): bookmark 30, impression 23837, like 40, quote 2, reply 2, repost 2
    
    > 1/4
    > ⚠️ Exploit Breakdown: #Injective binary options settlement bug
    > On Sept 1, @Injective was exploited via a binary options settlement flaw and drained of ~$4.8M. The attacker bridged funds to Ethereum and swapped into$ETH:0x9137a6b20b083b07b84294d51ebc04a326787a2d
    >
    > Triple-bug combo. Chain halted. Patch shipped.
    >
    > 1. Unbounded market_id string concat → ID collision. An INJ-denominated insurance fund could share the same market_id as a USDC binary options market.
    > https://github.com/InjectiveFoundation/injective-core/blob/b994d6b/injective-chain/modules/exchange/types/market.go#L52
    > https://github.com/InjectiveFoundation/injective-core/blob/b994d6b/injective-chain/modules/insurance/keeper/insurance.go#L398
    >
    > 2. Self-trades minted a fake settlement deficit. Attacker-controlled subaccounts crossed Long/Short orders against themselves to fabricate a non-existent funding gap.
    > https://github.com/InjectiveFoundation/injective-core/blob/5c3143ed621ed4e4a5d74d64ea952f5a8cda4c1f/injective-chain/modules/exchange/keeper/binaryoptions/market.go#L202-L226
    > https://github.com/InjectiveFoundation/injective-core/blob/5c3143ed621ed4e4a5d74d64ea952f5a8cda4c1f/injective-chain/modules/exchange/keeper/binaryoptions/market.go#L253-L264
    >
    > 3. Decimal mismatch. INJ wei (18 decimals) was compared directly against USDC (6 decimals), causing remainingDeficit to round to zero. The haircut was completely bypassed, and positions were refunded at full face value.
    > withdrawalAmount := absoluteDeficitAmount.Ceil().RoundInt() // USDC, 6 decimals
    > if http://insuranceFund.Balance.LT(withdrawalAmount) { ... }       // INJ base units, 18 decimals
    >
    > 4. Following the attack, Injective halted the chain and deployed a patch: https://github.com/InjectiveFoundation/injective-core/commit/b994d6b603eb53a38312e547f7bbe3c69d40495b
    > validateInsuranceFundDenom now strictly enforces that the insurance fund’s DepositDenom matches the market’s QuoteDenom across PayDeficitFromInsuranceFund, TransferFullInsuranceFundBalance, and MoveCoinsIntoInsuranceFund—effectively plugging the exploit vector.
    >
    > This upgrade is a post-exploit fix. Not a coincidence.
    
    **Media:**
    - photo: https://pbs.twimg.com/media/HRMw3DaaAAA2uNz.jpg — no alt text provided by author
    
    **Links in post:** https://github.com/InjectiveFoundation/injective-core/blob/b994d6b/injective-chain/modules/exchange/types/market.go#L52, https://github.com/InjectiveFoundation/injective-core/blob/b994d6b/injective-chain/modules/insurance/keeper/insurance.go#L398, https://github.com/InjectiveFoundation/injective-core/blob/5c3143ed621ed4e4a5d74d64ea952f5a8cda4c1f/injective-chain/modules/exchange/keeper/binaryoptions/market.go#L202-L226, https://github.com/InjectiveFoundation/injective-core/blob/5c3143ed621ed4e4a5d74d64ea952f5a8cda4c1f/injective-chain/modules/exchange/keeper/binaryoptions/market.go#L253-L264, http://insuranceFund.Balance.LT, https://github.com/InjectiveFoundation/injective-core/commit/b994d6b603eb53a38312e547f7bbe3c69d40495b
    


---

## 2026-09-03 · Post · Regarding the recent attack on @injective, I want to make one thing very clear: this incident has ab


Tags (automatic): Platform: Immunefi, Platform: Code4rena / Sherlock / Cantina


### Post — @al_f4lc0n — 2026-09-03 16:02 UTC (2026-09-03 17:02 WAT)

- URL: https://x.com/al_f4lc0n/status/2095543009504825390
- Metrics (at fetch): bookmark 2, impression 893, like 2, quote 0, reply 0, retweet 0

> Regarding the recent attack on @injective, I want to make one thing very clear: this incident has absolutely nothing to do with me.
>
> To this day, Injective still has not paid me any bug bounty. I am no longer arguing about this, and I have zero expectations from them anymore. For the past few months, I have been busy researching other things. I have received about $300,000 USD in total from bug bounties and audit contests.
>
> I will use 10% of this money to expose their fraud. However, I have not decided how or when to spend this money yet. I do not plan to put too much of my time and energy into this right now. Because of this, the plan might be delayed for a very long time.
>
> I am currently hunting bugs on @immunefi and @cantina. Thank you to all the projects that value security and integrity.
>
> - https://immunefi.com/profile/f4lc0n
> - https://cantina.xyz/u/f4lc0n

**Links in post:** https://twitter.com/GoPlusSecurity/status/2095119564409651639, https://immunefi.com/profile/f4lc0n, https://cantina.xyz/u/f4lc0n

**Quoted post (full text):**

    #### Quoted post — @GoPlusSecurity — 2026-09-02 12:00 UTC (2026-09-02 13:00 WAT)
    
    - URL: https://x.com/GoPlusSecurity/status/2095119564409651639
    - Metrics (at fetch): bookmark 30, impression 23837, like 40, quote 2, reply 2, repost 2
    
    > 1/4
    > ⚠️ Exploit Breakdown: #Injective binary options settlement bug
    > On Sept 1, @Injective was exploited via a binary options settlement flaw and drained of ~$4.8M. The attacker bridged funds to Ethereum and swapped into$ETH:0x9137a6b20b083b07b84294d51ebc04a326787a2d
    >
    > Triple-bug combo. Chain halted. Patch shipped.
    >
    > 1. Unbounded market_id string concat → ID collision. An INJ-denominated insurance fund could share the same market_id as a USDC binary options market.
    > https://github.com/InjectiveFoundation/injective-core/blob/b994d6b/injective-chain/modules/exchange/types/market.go#L52
    > https://github.com/InjectiveFoundation/injective-core/blob/b994d6b/injective-chain/modules/insurance/keeper/insurance.go#L398
    >
    > 2. Self-trades minted a fake settlement deficit. Attacker-controlled subaccounts crossed Long/Short orders against themselves to fabricate a non-existent funding gap.
    > https://github.com/InjectiveFoundation/injective-core/blob/5c3143ed621ed4e4a5d74d64ea952f5a8cda4c1f/injective-chain/modules/exchange/keeper/binaryoptions/market.go#L202-L226
    > https://github.com/InjectiveFoundation/injective-core/blob/5c3143ed621ed4e4a5d74d64ea952f5a8cda4c1f/injective-chain/modules/exchange/keeper/binaryoptions/market.go#L253-L264
    >
    > 3. Decimal mismatch. INJ wei (18 decimals) was compared directly against USDC (6 decimals), causing remainingDeficit to round to zero. The haircut was completely bypassed, and positions were refunded at full face value.
    > withdrawalAmount := absoluteDeficitAmount.Ceil().RoundInt() // USDC, 6 decimals
    > if http://insuranceFund.Balance.LT(withdrawalAmount) { ... }       // INJ base units, 18 decimals
    >
    > 4. Following the attack, Injective halted the chain and deployed a patch: https://github.com/InjectiveFoundation/injective-core/commit/b994d6b603eb53a38312e547f7bbe3c69d40495b
    > validateInsuranceFundDenom now strictly enforces that the insurance fund’s DepositDenom matches the market’s QuoteDenom across PayDeficitFromInsuranceFund, TransferFullInsuranceFundBalance, and MoveCoinsIntoInsuranceFund—effectively plugging the exploit vector.
    >
    > This upgrade is a post-exploit fix. Not a coincidence.
    
    **Media:**
    - photo: https://pbs.twimg.com/media/HRMw3DaaAAA2uNz.jpg — no alt text provided by author
    
    **Links in post:** https://github.com/InjectiveFoundation/injective-core/blob/b994d6b/injective-chain/modules/exchange/types/market.go#L52, https://github.com/InjectiveFoundation/injective-core/blob/b994d6b/injective-chain/modules/insurance/keeper/insurance.go#L398, https://github.com/InjectiveFoundation/injective-core/blob/5c3143ed621ed4e4a5d74d64ea952f5a8cda4c1f/injective-chain/modules/exchange/keeper/binaryoptions/market.go#L202-L226, https://github.com/InjectiveFoundation/injective-core/blob/5c3143ed621ed4e4a5d74d64ea952f5a8cda4c1f/injective-chain/modules/exchange/keeper/binaryoptions/market.go#L253-L264, http://insuranceFund.Balance.LT, https://github.com/InjectiveFoundation/injective-core/commit/b994d6b603eb53a38312e547f7bbe3c69d40495b
    


---

## 2026-06-03 · Reply · @FDugaso Paid $0


### Post — @al_f4lc0n — 2026-06-03 12:05 UTC (2026-06-03 13:05 WAT)

- URL: https://x.com/al_f4lc0n/status/2062143717457432690
- Metrics (at fetch): bookmark 0, impression 704, like 6, quote 0, reply 2, retweet 0

> @FDugaso Paid $0


---

## 2026-06-03 · Reply · @v4rvl @0xDestinyae Paid $0, no response. 🤡


### Post — @al_f4lc0n — 2026-06-03 10:15 UTC (2026-06-03 11:15 WAT)

- URL: https://x.com/al_f4lc0n/status/2062115945385214018
- Metrics (at fetch): bookmark 0, impression 181, like 2, quote 0, reply 1, retweet 0

> @v4rvl @0xDestinyae Paid $0, no response. 🤡


---

## 2026-06-03 · Post · 3 tips for Bug Bounty Hunters:


Tags (automatic): Blockchain / L1-L2 / bridge, Platform: HackerOne


### Post — @al_f4lc0n — 2026-06-03 08:01 UTC (2026-06-03 09:01 WAT)

- URL: https://x.com/al_f4lc0n/status/2062082215962366225
- Metrics (at fetch): bookmark 51, impression 18160, like 145, quote 3, reply 8, retweet 5

> 3 tips for Bug Bounty Hunters:
>
> - Don't submit critical bugs to Cosmos SDK based blockchains. Just check my pinned tweet.
> - Don't submit ANY bugs to Cosmos SDK. They will straight-up close your report because you're a new HackerOne user.
> - Fuck Cosmos. https://twitter.com/v12sec/status/2061401842324820205

**Links in post:** https://twitter.com/v12sec/status/2061401842324820205

**Quoted post (full text):**

    #### Quoted post — @v12sec — 2026-06-01 10:57 UTC (2026-06-01 11:57 WAT)
    
    - URL: https://x.com/v12sec/status/2061401842324820205
    - Metrics (at fetch): bookmark 279, impression 407866, like 1315, quote 72, reply 98, repost 120
    
    > We reported a critical loss of funds bug to @Thorchain (32M TVL, 150M FDV)
    >
    > They silently patched it and told us their bug bounty program is permanently retired.
    >
    > We have more Thorchain chain halt DoS vulns. We intend to release them (open disclosure) in the coming few days [pic.x.com/R2jyej5Pnh]
    
    **Media:**
    - photo: https://pbs.twimg.com/media/HJt4O_cbcAAwICo.jpg — no alt text provided by author
    - photo: https://pbs.twimg.com/media/HJt4QlbaUAAHuVO.jpg — no alt text provided by author
    


---

## 2026-03-18 · Post · the figures referenced in the post are entirely misleading. There was no impact realized from this i


Tags (automatic): Blockchain / L1-L2 / bridge, AI-assisted hunting, Platform: Immunefi


### Post — @al_f4lc0n — 2026-03-18 04:31 UTC (2026-03-18 05:31 WAT)

- URL: https://x.com/al_f4lc0n/status/2034125406748741827
- Metrics (at fetch): bookmark 44, impression 67374, like 480, quote 20, reply 37, retweet 32

> the figures referenced in the post are entirely misleading. There was no impact realized from this issue. Zero user funds were affected and zero addresses were compromised.
>
> My response: Are you suggesting I should have actually exploited the bug and caused real damage before coming to talk to you?
>
> For the stated vulnerability to work in practice, it would require execution of several suspicious transactions that would have an extraordinarily limited impact.
>
> My response: You should know better than anyone that on a Cosmos-based chain, a single transaction can pack multiple messages. Just one transaction is more than enough to completely drain multiple whale accounts.
>
> Injective has dynamic rate limiting functionalities which are applied automatically based on our live monitoring systems. This functionality has been live on mainnet since last year and is publicly available in our code base.
>
> My response: First, this has nothing to do with the vulnerability itself. Rate limiting doesn't stop attackers from stealing funds. It only slows them down when they try to bridge those funds over to Ethereum. Second, when I submitted my report, the mainnet configuration for this feature was not set. In other words, this feature wasn't even turned on!
>
> In addition to all of the above, this report was reviewed against the clearly defined terms of our Immunefi program. Based on those terms, issues such as those raised in this report that DO NOT impact block production or consensus are categorized outside of the Blockchain/DLT tier and carry a maximum payout of $50,000.
>
> My response: First, Immunefi has always put the impact of direct fund theft at the very top of its priority list. This is a fact that everyone knows. Second, you changed your bug bounty page after I submitted my report. Here’s the snapshot from November 8, 2025: https://web.archive.org/web/20251108165417/https://immunefi.com/bug-bounty/injective/information/ . And now, there’s an extra line added to your bug bounty page: “IMPORTANT: Within the Assets in Scope table, the injective-core folder is listed for both Blockchain/DLT and Web/App due to overlap between the two within the same folder. However, for a report to be categorized as Blockchain/DLT, the resulting impact has to be directly involved with the block production process or with consensus failures. All reports not dealing directly with either of these are to be categorized as Web/App.” I’d really like to know when this line was added. and do you really value chain consensus more than users' funds?
>
> We remain committed to fair, transparent, and consistent handling of all reports, and to maintaining the highest standards of security for the ecosystem. Injective has done so since its mainnet inception in 2021 and will continue to do so in perpetuity, always putting builders and security first.
>
> My response: You never even replied to my messages, and now you’re blaming me for not requesting mediation? I can post the original report if you agree. I left many messages, but you haven't replied to a single one.
>
> ----------
>
> Finally: Stop making excuses from every angle and trying to use technical jargon to confuse people who aren't developers. That doesn’t work anymore these days. Anyone can just ask an AI to fact-check what both of us are saying. I have no ill intentions toward your project. All I'm asking is for you to be honest and handle this transparently.

**Links in post:** https://twitter.com/bangjelkoski/status/2034099654976241688, https://web.archive.org/web/20251108165417/https://immunefi.com/bug-bounty/injective/information/

**Quoted post (full text):**

    #### Quoted post — @bangjelkoski — 2026-03-18 02:48 UTC (2026-03-18 03:48 WAT)
    
    - URL: https://x.com/bangjelkoski/status/2034099654976241688
    - Metrics (at fetch): bookmark 33, impression 200568, like 231, quote 12, reply 68, repost 35
    
    > Security is paramount at @injective and we take our bug bounty program very seriously.
    >
    > First and foremost, the figures referenced in the post are entirely misleading. There was no impact realized from this issue. Zero user funds were affected and zero addresses were compromised.
    >
    > For the stated vulnerability to work in practice, it would require execution of several suspicious transactions that would have an extraordinarily limited impact. Injective has dynamic rate limiting functionalities which are applied automatically based on our live monitoring systems. This functionality has been live on mainnet since last year and is publicly available in our code base.
    >
    > In addition to all of the above, this report was reviewed against the clearly defined terms of our Immunefi program. Based on those terms, issues such as those raised in this report that DO NOT impact block production or consensus are categorized outside of the Blockchain/DLT tier and carry a maximum payout of $50,000.
    >
    > If the poster had requested a mediation we would explain to him the dynamic rate limiters and monitoring systems we have in place and why his stated figures are misleading. However, he did not do so. We always follow the procedures set forth by the Immunefi program and expect the submitter to do so as well.
    >
    > We remain committed to fair, transparent, and consistent handling of all reports, and to maintaining the highest standards of security for the ecosystem. Injective has done so since its mainnet inception in 2021 and will continue to do so in perpetuity, always putting builders and security first.
    
    **Links in post:** https://twitter.com/al_f4lc0n/status/2033110168045568434
    
    **Quoted post (full text):**
    
        #### Quoted post — @al_f4lc0n — 2026-03-15 09:16 UTC (2026-03-15 10:16 WAT)
        
        - URL: https://x.com/al_f4lc0n/status/2033110168045568434
        - Metrics (at fetch): bookmark 1058, impression 1854052, like 4647, quote 247, reply 507, retweet 528
        
        > I Saved Injective's $500M. They Pay Me $50K.
        >
        > I like hunting bugs on @immunefi . I'm decent at it.
        >
        > - #1 — Attackathon | Stacks
        > - #2 — Attackathon | Stacks II
        > - #1 — Attackathon | XRPL Lending Protocol
        > - 1 Critical and 1 High from bug bounties (not counting this one)
        >
        > Life was good. Then I found a Critical vulnerability in @injective .
        >
        > This vulnerability allowed any user to directly drain any  account on the chain. No special permissions needed. Over $500M in on-chain assets were at risk.
        >
        > I reported it through Immunefi. The next day, a mainnet upgrade to fix the bug went to governance vote. The Injective team clearly understood the severity.
        >
        > Then — silence. For 3 months. No follow up. No technical discussion. Nothing.
        >
        > A few days ago, they notified me of their decision: $50K. The maximum payout for a Critical vulnerability in their bug bounty program is $500K. I disputed it. Silence again. No explanation for the reduced payout. No explanation for the 3 month ghost. No conversation at all. To be clear: the $50K has not been paid either.
        >
        > I've seen others share bad experiences with bug bounty payouts recently.  I never thought it would happen to me. I can't force them to do the right thing. But I won't let this be forgotten.
        >
        > I will dedicate 10% of all my future bug bounty earnings to making sure this story stays visible — until Injective pays what I deserve.
        >
        > Full Technical Report: https://github.com/injective-wall-of-shame/bug-any-account-ordering/blob/main/report.md
        
        **Links in post:** https://github.com/injective-wall-of-shame/bug-any-account-ordering/blob/main/report.md
        
    


---

## 2026-03-16 · Post · Here is my Immunefi profile: https://t.co/VY25CPYmM1


Tags (automatic): Platform: Immunefi


### Post — @al_f4lc0n — 2026-03-16 16:12 UTC (2026-03-16 17:12 WAT)

- URL: https://x.com/al_f4lc0n/status/2033577069872071056
- Metrics (at fetch): bookmark 24, impression 24840, like 176, quote 1, reply 14, retweet 6

> Here is my Immunefi profile: https://t.co/VY25CPYmM1
>
> I submitted my first valid bug report on Immunefi on December 15, 2024.
>
> And, could you help me reach out to @injective ? I want to ask if I’m allowed to public my original report. Alternatively, ask them to have a technical https://t.co/lMGKUXGWKp

**Quoted post** 2033519194197667915: not readable via the API (deleted, private, or withheld).


---

## 2026-03-16 · Reply · @sw0nt Thanks for reading!


### Post — @al_f4lc0n — 2026-03-16 06:09 UTC (2026-03-16 07:09 WAT)

- URL: https://x.com/al_f4lc0n/status/2033425484995080460
- Metrics (at fetch): bookmark 3, impression 1165, like 21, quote 0, reply 10, retweet 0

> @sw0nt Thanks for reading!


---

## 2026-03-15 · Reply · @HatforceSec @wholisticguy @immunefi 99% of the liquidity on Injective is in USDT and INJ. The PoC p


Tags (automatic): Platform: Immunefi


### Post — @al_f4lc0n — 2026-03-15 12:43 UTC (2026-03-15 13:43 WAT)

- URL: https://x.com/al_f4lc0n/status/2033162136244138380
- Metrics (at fetch): bookmark 1, impression 1757, like 13, quote 1, reply 2, retweet 0

> @HatforceSec @wholisticguy @immunefi 99% of the liquidity on Injective is in USDT and INJ. The PoC proves that an attacker can drain USDT from any account, and the same logic applies to INJ. I’m confident this PoC shows that almost all the TVL on the chain is at risk.


---

## 2026-03-15 · Reply · @HatforceSec @immunefi I suggest you read it first. If you've gone through the report and the PoC, I


Tags (automatic): Platform: Immunefi


### Post — @al_f4lc0n — 2026-03-15 12:15 UTC (2026-03-15 13:15 WAT)

- URL: https://x.com/al_f4lc0n/status/2033155123770511704
- Metrics (at fetch): bookmark 1, impression 6025, like 59, quote 0, reply 1, retweet 0

> @HatforceSec @immunefi I suggest you read it first. If you've gone through the report and the PoC, I don't think you’d question the severity of this bug.


---

## 2026-03-15 · Reply · @HatforceSec @immunefi I asked, but they didn't reply. They haven't responded to any of my messages.


Tags (automatic): Platform: Immunefi


### Post — @al_f4lc0n — 2026-03-15 12:10 UTC (2026-03-15 13:10 WAT)

- URL: https://x.com/al_f4lc0n/status/2033153806566146123
- Metrics (at fetch): bookmark 2, impression 31360, like 197, quote 0, reply 4, retweet 0

> @HatforceSec @immunefi I asked, but they didn't reply. They haven't responded to any of my messages.


---

## 2026-03-15 · Reply · @HatforceSec @immunefi Check the 'Full Technical Report' link at the end of the tweet for the end-to


Tags (automatic): Platform: Immunefi


### Post — @al_f4lc0n — 2026-03-15 12:04 UTC (2026-03-15 13:04 WAT)

- URL: https://x.com/al_f4lc0n/status/2033152350911860910
- Metrics (at fetch): bookmark 2, impression 30013, like 58, quote 0, reply 2, retweet 0

> @HatforceSec @immunefi Check the 'Full Technical Report' link at the end of the tweet for the end-to-end PoC.


---

## 2026-03-15 · Post · I Saved Injective's $500M. They Pay Me $50K.


Tags (automatic): Blockchain / L1-L2 / bridge, Platform: Immunefi


### Post — @al_f4lc0n — 2026-03-15 09:16 UTC (2026-03-15 10:16 WAT)

- URL: https://x.com/al_f4lc0n/status/2033110168045568434
- Metrics (at fetch): bookmark 1058, impression 1854052, like 4647, quote 247, reply 507, retweet 528

> I Saved Injective's $500M. They Pay Me $50K.
>
> I like hunting bugs on @immunefi . I'm decent at it.
>
> - #1 — Attackathon | Stacks
> - #2 — Attackathon | Stacks II
> - #1 — Attackathon | XRPL Lending Protocol
> - 1 Critical and 1 High from bug bounties (not counting this one)
>
> Life was good. Then I found a Critical vulnerability in @injective .
>
> This vulnerability allowed any user to directly drain any  account on the chain. No special permissions needed. Over $500M in on-chain assets were at risk.
>
> I reported it through Immunefi. The next day, a mainnet upgrade to fix the bug went to governance vote. The Injective team clearly understood the severity.
>
> Then — silence. For 3 months. No follow up. No technical discussion. Nothing.
>
> A few days ago, they notified me of their decision: $50K. The maximum payout for a Critical vulnerability in their bug bounty program is $500K. I disputed it. Silence again. No explanation for the reduced payout. No explanation for the 3 month ghost. No conversation at all. To be clear: the $50K has not been paid either.
>
> I've seen others share bad experiences with bug bounty payouts recently.  I never thought it would happen to me. I can't force them to do the right thing. But I won't let this be forgotten.
>
> I will dedicate 10% of all my future bug bounty earnings to making sure this story stays visible — until Injective pays what I deserve.
>
> Full Technical Report: https://github.com/injective-wall-of-shame/bug-any-account-ordering/blob/main/report.md

**Links in post:** https://github.com/injective-wall-of-shame/bug-any-account-ordering/blob/main/report.md
