# two-rights-might-make-a-wrong

- **Source URL:** https://samczsun.com/two-rights-might-make-a-wrong/
- **Fetched:** 2026-11-11
- **Researcher:** samczsun
- **Method:** curl + trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---

# Two Rights Might Make A Wrong

*Also published on [Paradigm](https://www.paradigm.xyz/writing/two-rights-might-make-a-wrong).*

A common misconception in building software is that if every component in a system is individually verified to be safe, the system itself is also safe. Nowhere is this belief better illustrated than in DeFi, where composability is second nature to developers. Unfortunately, while composing two components might be safe most of the time, it only takes one vulnerability to cause serious financial damage to hundreds if not thousands of innocent users. Today, I’d like to tell you about how I found and helped patch a vulnerability that put over 109k ETH (\~350 million USD at today’s exchange rate) at risk.

# The Encounter

*9:42 AM*

I was offhandedly browsing through the LobsterDAO group on Telegram when I noticed a discussion between [@ivangbi\_](https://twitter.com/ivangbi_) and [@bantg](https://twitter.com/bantg) about a new raise on SushiSwap’s MISO platform. I typically try to avoid drama in public, but I couldn’t help but do a quick Google search to see what it was all about. The results I got back weren’t particularly interesting to me, but I pressed onward, driven by a feeling there was something interesting to be found here if I just kept looking.

The MISO platform operates two types of auctions: Dutch auctions and batch auctions. In this case, the raise was being held with a Dutch auction. Naturally, the first thing I did was open up the contract on [Etherscan](https://etherscan.io/address/0x4c4564a1FE775D97297F9e3Dc2e762e0Ed5Dda0e).

*9:44 AM*

I quickly skimmed through the DutchAuction contract per the participation agreement and checked each interesting function. The commit functions (`commitEth`, `commitTokens`, and `commitTokensFrom`) all seemed to be implemented correctly. The auction management functions (`setDocument`, `setList`, etc) also had the proper access controls. However, near the bottom I noticed that the `initMarket` function had no access controls, which was extremely concerning. Furthermore, the `initAuction` function it called also contained no access control checks.

I didn’t really expect this to be a vulnerability though, since I didn’t expect the Sushi team to make such an obvious misstep. Sure enough, the `initAccessControls` function validated that the contract had not already been initialized.

However, this led me to another discovery. While scrolling through all of the files, I noticed the `SafeTransfer` and `BoringBatchable` libraries. I was familiar with both of these, and I was immediately struck with the potential that the `BoringBatchable` library introduced.

For those who aren’t familiar, `BoringBatchable` is a mixin library which is designed to easily introduce batch calls to any contract which imports it. It does this by performing a delegatecall on the current contract for each call data provided in the input.

Looking at this function, it appeared to be implemented correctly. However, something in the corner of my mind was nagging at me. That’s when I realized I had seen something very similar in the past.

# The Discovery

*9:47 AM*

A little over a year ago today, I was in a Zoom call with the Opyn team, trying to figure out how to recover and protect user funds after a devastating hack. The hack itself was simple but genius: it exercised multiple options using a single payment of ETH because the Opyn contracts used the `msg.value` variable in a loop. While processing token payments involved a separate `transferFrom` call for each loop iteration, processing ETH payments simply checked whether `msg.value` was sufficient. This allowed the attacker to reuse the same ETH multiple times.

I realized that I was looking at the exact same vulnerability in a different form. Inside a delegatecall, `msg.sender` and `msg.value` are persisted. This meant that I should be able to batch multiple calls to `commitEth` and reuse my `msg.value` across every commitment, allowing me to bid in the auction for free.

*9:52 AM*

My instincts were telling me that this was the real deal, but I couldn’t be sure without verifying it. I quickly opened up Remix and wrote a proof-of-concept. To my dismay, my mainnet fork environment was completely busted. I must’ve accidentally broken it during the London hard fork. With how much money was at risk though, I didn’t have the luxury of time. I quickly threw together a poor man’s mainnet fork on the command line and tested my exploit. It worked.

*10:13 AM*

I pinged my colleague, [Georgios Konstantopoulos](https://twitter.com/gakonst), to get a second pair of eyes on this before reporting it. While I waited for a response, I went back to the contract to look for ways to elevate the severity. It was one thing to be able to participate in the auction for free, but it would be another to be able to *steal* all of the other bids too.

I had noticed there was some refund logic during my initial scan but thought little of it. Now, it was a way to get ETH out of the contract. I quickly checked what conditions I would need to meet in order to get the contract to provide me with a refund.

To my surprise (and horror), I found that a refund would be issued for any ETH sent which went over the auction’s hard cap. This applied even once the hard cap was hit, meaning that instead of rejecting the transaction altogether, the contract would simply refund all of your ETH instead.

Suddenly, my little vulnerability just got a lot bigger. I wasn’t dealing with a bug that would let you outbid other participants. I was looking at a 350 million dollar bug.

# The Disclosure

*10:38 AM*

After verifying the bug with Georgios, I asked him and [Dan Robinson](https://twitter.com/danrobinson) to try and reach out to Joseph Delong from Sushi. Within minutes, Joseph had responded and I found myself in a Zoom call with Georgios, Joseph, Mudit, Keno, and Omakase. I quickly debriefed the participants on the vulnerability and they left to coordinate a response. The entire call lasted mere minutes.

*11:10 AM*

Joseph got back to Georgios and I with a Google Meet room. I joined as Georgios was in the middle of debriefing Joseph, Mudit, Keno, and Omakase, as well as Duncan and Mitchell from Immunefi. We quickly discussed next steps.

We had three options:

1. Leave the contract and hope no one notices
2. Rescue the funds using the exploit, probably using Flashbots to hide the transaction
3. Rescue the funds by purchasing the remaining allocation and immediately finalizing the auction, requiring admin permissions

After some quick debate, we decided that option 3 was the cleanest approach. We broke out into separate rooms in order to work on comms and ops separately.

# The Preparation

*11:26 AM*

Inside the ops room, Mudit, Keno, Georgios, and I were busy writing a simple rescue contract. We decided that it would be cleanest to take a flash loan, purchase up to the hard cap, finalize the auction, then repay the flash loan using proceeds from the auction itself. This would require no upfront capital, which was very nice.

*12:54 PM*

We ran into a problem. What was originally supposed to be a simple rescue operation had just turned into a ticking time bomb that couldn’t be defused, because there was *another* active auction. This was a batch auction, which meant that we couldn’t just buy up to the hard cap because there was no hard cap at all. Fortunately, the lack of a hard cap also meant there was no way to drain ETH from the contract because no refunds were offered.

We quickly discussed the pros and cons of performing a whitehat rescue on the first contract and ultimately decided that even though the batch auction had 8 million USD committed, those 8 million USD weren’t at risk, while the 350 million USD in the original Dutch auction was very much still at risk. Even if someone was tipped off by our forced halting of the Dutch auction and found the bug in the batch auction, we would still save the majority of the money. The call to proceed was made.

*1:36 PM*

As we wrapped up work on the rescue contract, we discussed next steps for the batch auction. Mudit pointed out that there was a points list which could be set even while the auction was live, and it was called during each ETH commitment. We immediately realized this could be the pause function we were looking for.

We brainstormed different ways to make use of this hook. Immediately reverting was an obvious solution, but we wanted something better. I considered adding a check that every origin could only make one commitment per block, but we noticed that the function was marked as view, which meant that the Solidity compiler would have used a static call opcode. Our hook wouldn’t be allowed to make any state modifications.

After some more thinking, I realized that we could use the points list to verify that the auction contract had enough ETH to match the commitments being made. In other words, if someone tried to exploit this bug, then there would be more commitments than there was ETH. We could easily detect this and revert the transaction. Mudit and Keno began working on writing a test to verify.

# The Rescue

*2:01 PM*

The comms breakout team merged with the ops breakout team to sync on progress. They had made contact with the team performing the raise, but the team wanted to finalize the auction manually. We discussed the risks and agreed that there was minimal likelihood that an automated bot would notice the transaction or be able to do anything about it.

*2:44 PM*

The team performing the raise finalized the auction, neutralizing the immediate threat. We congratulated each other and went our separate ways. The batch auction would finalize later in the day to little fanfare. No one outside of the circle of trust knew what scale of crisis had just been averted.

# The Reflection

*4:03 PM*

The past few hours feel like a blur, almost as though no time has passed at all. I had gone from encounter to discovery in a little over half an hour, disclosure in 20 minutes, war room in another 30, and a fix in three hours. All in all, it took only five hours to protect 350 million USD from falling into the wrong hands.

Even though there was no monetary damage, I’m sure that everyone involved would have much preferred to not have gone through this process in the first place. To that end, I have two main takeaways for you.

First, using `msg.value` in complex systems is hard. It’s a global variable that you can’t change and persists across delegate calls. If you use `msg.value` to check that payment was received, you absolutely cannot place that logic in a loop. As a codebase grows in complexity, it’s easy to lose track of where that happens and accidentally loop something in the wrong place. Although wrapping and unwrapping of ETH is annoying and introduces extra steps, the unified interface between WETH and other ERC20 tokens might be well worth the cost if it means avoiding something like this.

Second, safe components can come together to make something unsafe. I’ve preached this before in the context of composability and DeFi protocols, but this incident shows that even safe contract-level components can be mixed in a way that produces unsafe contract-level behavior. There’s no catch-all advice to apply here like “check-effect-interaction,” so you just need to be cognizant of what additional interactions new components are introducing.

I’d like to thank Sushi contributors, Joseph, Mudit, Keno, and Omakase for their extremely quick response to this issue as well as my colleagues Georgios, Dan, and Jim for their help throughout this process, including reviewing this post.
