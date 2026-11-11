# @kankodu — full verbatim X archive (security-relevant posts)

_Generated 2026-11-11 from the X API (full-archive search + timeline). Every post below is copied word-for-word; t.co links are expanded; quoted posts are inlined in full; media are listed with alt text when the author provided it. Posts are grouped by conversation (a thread = the author's root post followed by their own replies, oldest first). Groups are newest first. An agent without X access can rely on this file._

- Posts in this file: 57
- Conversations/threads: 57
- Oldest post captured: 2023-07-29
- Newest post captured: 2026-11-08


---

## 2026-11-08 · Reply · @lex_node https://t.co/Z2qrELJ9RX https://t.co/52onkk9Kf1


### Post — @kankodu — 2026-11-08 14:31 UTC (2026-11-08 15:31 WAT)

- URL: https://x.com/kankodu/status/2119437635890577783
- Metrics (at fetch): bookmark 0, impression 175, like 1, quote 0, reply 0, retweet 0

> @lex_node https://t.co/Z2qrELJ9RX https://t.co/52onkk9Kf1

**Quoted post (full text):**

    #### Quoted post — @kankodu — 2026-11-08 13:00 UTC (2026-11-08 14:00 WAT)
    
    - URL: https://x.com/kankodu/status/2119414649204699528
    - Metrics (at fetch): bookmark 18, impression 4602, like 61, quote 1, reply 3, retweet 1
    
    > Uniswap V4 Position Manager is being used as an example of highly used contract that will be broken after Glamsterdam. 
    >
    > Yes, the contract itself is highly used but I couldn't find any immutable contract using the subscribe pattern in the wild for rewards distribution that will be broken. Protocols (including Uniswap Foundation) just use Merkl to provide rewards and they do calculations off-chain.
    


---

## 2026-11-08 · Post · Uniswap V4 Position Manager is being used as an example of highly used contract that will be broken 


### Post — @kankodu — 2026-11-08 13:00 UTC (2026-11-08 14:00 WAT)

- URL: https://x.com/kankodu/status/2119414649204699528
- Metrics (at fetch): bookmark 18, impression 4602, like 61, quote 1, reply 3, retweet 1

> Uniswap V4 Position Manager is being used as an example of highly used contract that will be broken after Glamsterdam. 
>
> Yes, the contract itself is highly used but I couldn't find any immutable contract using the subscribe pattern in the wild for rewards distribution that will be broken. Protocols (including Uniswap Foundation) just use Merkl to provide rewards and they do calculations off-chain.


---

## 2026-10-20 · Post · I have shown multiple teams that simple restrictions on transfers do not prevent trading outside the


### Post — @kankodu — 2026-10-20 00:22 UTC (2026-10-20 01:22 WAT)

- URL: https://x.com/kankodu/status/2112338590235857178
- Metrics (at fetch): bookmark 2, impression 1155, like 25, quote 0, reply 2, retweet 1

> I have shown multiple teams that simple restrictions on transfers do not prevent trading outside their hooks. 
>
> The solutions I’ve suggested looked a lot like URC-5 but they were specific to projects. It’s great that there is now a standard around it. https://twitter.com/standard_rsv/status/2112221351759286660

**Links in post:** https://twitter.com/standard_rsv/status/2112221351759286660

**Quoted post** 2112221351759286660: not readable via the API (deleted, private, or withheld).


---

## 2026-09-12 · Reply · @0xkuncoro I focused on one victim that lost the most for simplicity


### Post — @kankodu — 2026-09-12 07:16 UTC (2026-09-12 08:16 WAT)

- URL: https://x.com/kankodu/status/2098672084339851402
- Metrics (at fetch): bookmark 0, impression 128, like 1, quote 0, reply 1, retweet 0

> @0xkuncoro I focused on one victim that lost the most for simplicity
>
> Victim: 0x69da29127bc31909c26080105b585345dde847d4


---

## 2026-09-12 · Reply · @K_2022_1 @ether_fi @JozefVogel @MikeSilagadze As I said in the post, multiple things have to line u


Tags (automatic): Smart contract / DeFi


### Post — @kankodu — 2026-09-12 07:14 UTC (2026-09-12 08:14 WAT)

- URL: https://x.com/kankodu/status/2098671632160288814
- Metrics (at fetch): bookmark 0, impression 105, like 1, quote 0, reply 0, retweet 0

> @K_2022_1 @ether_fi @JozefVogel @MikeSilagadze As I said in the post, multiple things have to line up for you to be vulnerable. EIP 7702 in itself does not expose you to anything unless you keep leaving hanging approvals to contracts that use bad smart contract patterns.


---

## 2026-09-11 · Post · Today's hack of EtherFi helper contract is a good example of how multiple holes in a system can line


### Post — @kankodu — 2026-09-11 11:46 UTC (2026-09-11 12:46 WAT)

- URL: https://x.com/kankodu/status/2098377603396915590
- Metrics (at fetch): bookmark 36, impression 4455, like 54, quote 0, reply 5, retweet 1

> Today's hack of EtherFi helper contract is a good example of how multiple holes in a system can line up to create a vulnerability.
>
> 1st hole:  the contract with the bad callback pattern. The AtomicQueue contract calls a callback function on a user provided address and assumes that if the call succeeds, the interaction was intentional. The best practise is to require specific return data from the callback.
>
> 2nd hole: a stale approval. More than a year ago the victim interacted with this contract from their EOA and left a hanging approval.
>
> Note that these two holes still aren't enough to steal funds because a callback on a plain EOA simply fails.
>
> 3rd and final blow:  EIP-7702 delegation. 3 months ago they clicked a button in their Coinbase Wallet to start using EIP-7702 capabilities and that's where they became vulnerable. The smart wallet they delegated to silently did nothing when a random function was called on it.
>
> Together, these three things led to the victim losing ~12 ETH today.
>
> Tx Hash: 0x7cbe0b4349513fed6d03ba8bf9ed708e10e07a501d10b5f344a25ae10595599b


---

## 2026-09-11 · Post · Today's hack https://ether.fi helper contract is a good example of how multiple holes in a system ca


### Post — @kankodu — 2026-09-11 11:44 UTC (2026-09-11 12:44 WAT)

- URL: https://x.com/kankodu/status/2098377231110447337
- Metrics (at fetch): bookmark 0, impression 269, like 0, quote 0, reply 0, retweet 0

> Today's hack https://ether.fi helper contract is a good example of how multiple holes in a system can line up to create a vulnerability.
>
> 1st hole:  the contract with the bad callback pattern. The AtomicQueue contract calls a callback function on a user provided address

**Links in post:** https://ether.fi


---

## 2026-08-07 · Reply · @haydenzadams Searchers won't do anything until unclaimed fees equal to amounts needed to increase t


### Post — @kankodu — 2026-08-07 09:27 UTC (2026-08-07 10:27 WAT)

- URL: https://x.com/kankodu/status/2085659140987531412
- Metrics (at fetch): bookmark 0, impression 335, like 1, quote 0, reply 0, retweet 0

> @haydenzadams Searchers won't do anything until unclaimed fees equal to amounts needed to increase the liquidity position by 0.2% + swap fees (if needed) + the required gas + some profit of their own
>
> This is a good design and it can replace the need for privileged roles in many systems


---

## 2026-07-27 · Post · I have been using this tool to visualise codebases ever since it came out. In a text editor, you som


Tags (automatic): Blockchain / L1-L2 / bridge


### Post — @kankodu — 2026-07-27 05:24 UTC (2026-07-27 06:24 WAT)

- URL: https://x.com/kankodu/status/2081611786537877806
- Metrics (at fetch): bookmark 27, impression 3384, like 43, quote 0, reply 2, retweet 1

> I have been using this tool to visualise codebases ever since it came out. In a text editor, you sometimes loose track after going deeper in a complex function. 
>
> Solflow helps in making sure you go through the code similar to how EVM will eventually execute it. Thanks @0xnorah23 https://twitter.com/0xnorah23/status/2068254682515230900

**Links in post:** https://twitter.com/0xnorah23/status/2068254682515230900

**Quoted post** 2068254682515230900: not readable via the API (deleted, private, or withheld).


---

## 2026-06-03 · Reply · @WhiteHatMage I once reported a critical that got closed as a duplicate. When I reached out to the p


**Context — post being replied to:**

#### Parent post — @WhiteHatMage — 2026-06-02 15:38 UTC (2026-06-02 16:38 WAT)

- URL: https://x.com/WhiteHatMage/status/2061834838240350407
- Metrics (at fetch): bookmark 23, impression 10903, like 114, quote 2, reply 19, retweet 9

> I also have another theory about duplicates: some projects and platforms abusing nonsense slop submissions.
>
> You disclose an e2e-proven exploit, but it gets marked as a duplicate because of the "root cause".
>
> The slop report contains the vulnerable lines but no actual proof or https://twitter.com/WhiteHatMage/status/2059330192867291634

**Links in post:** https://twitter.com/WhiteHatMage/status/2059330192867291634

**Quoted post (full text):**

    #### Quoted post — @WhiteHatMage — 2026-05-26 17:45 UTC (2026-05-26 18:45 WAT)
    
    - URL: https://x.com/WhiteHatMage/status/2059330192867291634
    - Metrics (at fetch): bookmark 6, impression 12126, like 75, quote 1, reply 4, retweet 0
    
    > I’d say that getting too many duplicates in old bug bounty programs is a sign that your hunting strategy needs improvement. Duplicates should be rare.
    


### Post — @kankodu — 2026-06-03 15:25 UTC (2026-06-03 16:25 WAT)

- URL: https://x.com/kankodu/status/2062194004994011173
- Metrics (at fetch): bookmark 0, impression 212, like 2, quote 0, reply 0, retweet 0

> @WhiteHatMage I once reported a critical that got closed as a duplicate. When I reached out to the previous bug reporter, I learned that the project had initially closed their report as invalid, but then paid them out of the blue. From the dates we confirmed that the real reason was my report.


---

## 2026-04-24 · Reply · @haydenzadams This misleading claim is not fixed in the new docs. 


### Post — @kankodu — 2026-04-24 05:36 UTC (2026-04-24 06:36 WAT)

- URL: https://x.com/kankodu/status/2047550326404985162
- Metrics (at fetch): bookmark 1, impression 189, like 2, quote 0, reply 0, retweet 0

> @haydenzadams This misleading claim is not fixed in the new docs. 
>
> Decreasing liquidity automatically withdraws ALL of the unclaimed fees for that position. Not just *propotional* unclaimed fees. https://t.co/ezasgvaVcX

**Media:**
- photo: https://pbs.twimg.com/media/HGpbmGgaIAE_ww5.jpg — no alt text provided by author


---

## 2026-04-17 · Reply · @z0r0zzz @ethcforg This but without paying gas to deploy it on mainnet https://t.co/tYeIC6u5on


### Post — @kankodu — 2026-04-17 16:55 UTC (2026-04-17 17:55 WAT)

- URL: https://x.com/kankodu/status/2045184316586795114
- Metrics (at fetch): bookmark 0, impression 66, like 1, quote 0, reply 0, retweet 0

> @z0r0zzz @ethcforg This but without paying gas to deploy it on mainnet https://t.co/tYeIC6u5on

**Quoted post (full text):**

    #### Quoted post — @kankodu — 2025-09-09 17:29 UTC (2025-09-09 18:29 WAT)
    
    - URL: https://x.com/kankodu/status/1965467493000163600
    - Metrics (at fetch): bookmark 12, impression 4312, like 20, quote 1, reply 5, retweet 1
    
    > PSA for web3 frontend devs:
    >
    > Add Foundry/Hardhat to your frontend repo.
    > It’ll save your users time (and frustration).
    >
    > Here’s why 👇
    


---

## 2026-03-24 · Reply · @z0r0zzz Not sure how it works exactly but for https://t.co/BTRwhD1Eyo it’s been better the UX (one 


### Post — @kankodu — 2026-03-24 14:29 UTC (2026-03-24 15:29 WAT)

- URL: https://x.com/kankodu/status/2036450359472980094
- Metrics (at fetch): bookmark 0, impression 62, like 0, quote 0, reply 0, retweet 0

> @z0r0zzz Not sure how it works exactly but for https://t.co/BTRwhD1Eyo it’s been better the UX (one click for otherwise complicated action using EIP 7702), higher the chances of this warning


---

## 2026-03-23 · Post · A big thank you to all the SRs for helping secure the protocol 🙏 https://twitter.com/cantinasecurity


Tags (automatic): Platform: Code4rena / Sherlock / Cantina


### Post — @kankodu — 2026-03-23 17:32 UTC (2026-03-23 18:32 WAT)

- URL: https://x.com/kankodu/status/2036134048087810110
- Metrics (at fetch): bookmark 0, impression 1897, like 10, quote 0, reply 2, retweet 1

> A big thank you to all the SRs for helping secure the protocol 🙏 https://twitter.com/cantinasecurity/status/2036125988602651020

**Links in post:** https://twitter.com/cantinasecurity/status/2036125988602651020

**Quoted post** 2036125988602651020: not readable via the API (deleted, private, or withheld).


---

## 2026-03-23 · Reply · @ThmsSmts @vii_finance @ArcadiaFi Thanks for pointing it out. I edited it to remove the "first" keyw


### Post — @kankodu — 2026-03-23 15:04 UTC (2026-03-23 16:04 WAT)

- URL: https://x.com/kankodu/status/2036096872155353159
- Metrics (at fetch): bookmark 1, impression 81, like 3, quote 0, reply 1, retweet 0

> @ThmsSmts @vii_finance @ArcadiaFi Thanks for pointing it out. I edited it to remove the "first" keyword


---

## 2026-03-23 · Post · VII Finance is now live on Ethereum and Unichain! 


### Post — @kankodu — 2026-03-23 14:35 UTC (2026-03-23 15:35 WAT)

- URL: https://x.com/kankodu/status/2036089539849273823
- Metrics (at fetch): bookmark 15, impression 4568, like 28, quote 0, reply 2, retweet 0

> VII Finance is now live on Ethereum and Unichain! 
>
> Please try it out and lmk if you have any feedback https://twitter.com/vii_finance/status/2036084313553527035

**Links in post:** https://twitter.com/vii_finance/status/2036084313553527035

**Quoted post** 2036084313553527035: not readable via the API (deleted, private, or withheld).


---

## 2026-03-23 · Post · VII Finance is now live on aether and Unichain! 


### Post — @kankodu — 2026-03-23 14:35 UTC (2026-03-23 15:35 WAT)

- URL: https://x.com/kankodu/status/2036089462133006654
- Metrics (at fetch): bookmark 0, impression 52, like 0, quote 0, reply 0, retweet 0

> VII Finance is now live on aether and Unichain! 
>
> Please try it out and lmk if you have any feedback https://t.co/5rvweHStEB

**Quoted post** 2036084313553527035: not readable via the API (deleted, private, or withheld).


---

## 2026-01-27 · Reply · @0xngmi It’s been 7 months since EIP 7702 went live.


Tags (automatic): Smart contract / DeFi


### Post — @kankodu — 2026-01-27 06:40 UTC (2026-01-27 07:40 WAT)

- URL: https://x.com/kankodu/status/2016038501511528655
- Metrics (at fetch): bookmark 0, impression 588, like 2, quote 0, reply 0, retweet 0

> @0xngmi It’s been 7 months since EIP 7702 went live.
>
> Frontends should simply not allow user interactions if user’s wallet doesn’t support it. 
>
> No more hanging approvals and that means there is no need to even audit smart contracts related to dex aggregators.


---

## 2026-01-24 · Post · Only a couple of days left. Make it count! https://t.co/S2I5liFBxc


### Post — @kankodu — 2026-01-24 04:20 UTC (2026-01-24 05:20 WAT)

- URL: https://x.com/kankodu/status/2014916234543063070
- Metrics (at fetch): bookmark 1, impression 1994, like 16, quote 1, reply 1, retweet 1

> Only a couple of days left. Make it count! https://t.co/S2I5liFBxc

**Quoted post (full text):**

    #### Quoted post — @kankodu — 2026-01-16 17:44 UTC (2026-01-16 18:44 WAT)
    
    - URL: https://x.com/kankodu/status/2012219532056645916
    - Metrics (at fetch): bookmark 8, impression 3575, like 19, quote 1, reply 3, retweet 1
    
    > Here's where you can do some weekend bug hunting:
    >
    > https://cantina.xyz/competitions/eb93d215-e328-4d19-99ab-6c510acbb5aa
    
    **Links in post:** https://cantina.xyz/competitions/eb93d215-e328-4d19-99ab-6c510acbb5aa
    


---

## 2026-01-17 · Reply · @techOptimizor 👀


### Post — @kankodu — 2026-01-17 15:42 UTC (2026-01-17 16:42 WAT)

- URL: https://x.com/kankodu/status/2012551210172400059
- Metrics (at fetch): bookmark 0, impression 129, like 1, quote 0, reply 0, retweet 0

> @techOptimizor 👀


---

## 2026-01-16 · Post · Here's where you can do some weekend bug hunting:


Tags (automatic): Platform: Code4rena / Sherlock / Cantina


### Post — @kankodu — 2026-01-16 17:44 UTC (2026-01-16 18:44 WAT)

- URL: https://x.com/kankodu/status/2012219532056645916
- Metrics (at fetch): bookmark 8, impression 3575, like 19, quote 1, reply 3, retweet 1

> Here's where you can do some weekend bug hunting:
>
> https://cantina.xyz/competitions/eb93d215-e328-4d19-99ab-6c510acbb5aa

**Links in post:** https://cantina.xyz/competitions/eb93d215-e328-4d19-99ab-6c510acbb5aa


---

## 2026-01-12 · Post · https://t.co/xDU1xm8p3s


### Post — @kankodu — 2026-01-12 18:17 UTC (2026-01-12 19:17 WAT)

- URL: https://x.com/kankodu/status/2010778298364956949
- Metrics (at fetch): bookmark 0, impression 715, like 5, quote 0, reply 0, retweet 0

> https://t.co/xDU1xm8p3s


---

## 2026-01-12 · Post · The competition is now live! https://t.co/XBNgp2Fpnu


### Post — @kankodu — 2026-01-12 18:17 UTC (2026-01-12 19:17 WAT)

- URL: https://x.com/kankodu/status/2010778112582467606
- Metrics (at fetch): bookmark 1, impression 2534, like 35, quote 0, reply 2, retweet 0

> The competition is now live! https://t.co/XBNgp2Fpnu

**Quoted post (full text):**

    #### Quoted post — @kankodu — 2026-01-08 07:19 UTC (2026-01-08 08:19 WAT)
    
    - URL: https://x.com/kankodu/status/2009163017381167607
    - Metrics (at fetch): bookmark 6, impression 6094, like 51, quote 1, reply 5, retweet 1
    
    > 👀👀 https://t.co/xkMXP0yj80
    
    **Media:**
    - photo: https://pbs.twimg.com/media/G-H7HD_a0AIhs4S.jpg — no alt text provided by author
    


---

## 2026-01-09 · Reply · @0xSlowbug coming right up


### Post — @kankodu — 2026-01-09 12:50 UTC (2026-01-09 13:50 WAT)

- URL: https://x.com/kankodu/status/2009608601233678593
- Metrics (at fetch): bookmark 0, impression 62, like 2, quote 0, reply 0, retweet 0

> @0xSlowbug coming right up


---

## 2026-01-09 · Reply · @4gontuk @cantinaxyz That is coming as well!


Tags (automatic): Platform: Code4rena / Sherlock / Cantina


### Post — @kankodu — 2026-01-09 03:15 UTC (2026-01-09 04:15 WAT)

- URL: https://x.com/kankodu/status/2009464140864344120
- Metrics (at fetch): bookmark 0, impression 89, like 3, quote 0, reply 0, retweet 0

> @4gontuk @cantinaxyz That is coming as well!


---

## 2026-01-08 · Post · 👀👀 https://t.co/xkMXP0yj80


### Post — @kankodu — 2026-01-08 07:19 UTC (2026-01-08 08:19 WAT)

- URL: https://x.com/kankodu/status/2009163017381167607
- Metrics (at fetch): bookmark 6, impression 6094, like 51, quote 1, reply 5, retweet 1

> 👀👀 https://t.co/xkMXP0yj80

**Media:**
- photo: https://pbs.twimg.com/media/G-H7HD_a0AIhs4S.jpg — no alt text provided by author


---

## 2026-01-08 · Post · Any ideas to make sure other SRs can get the context of your protocol quickly?


### Post — @kankodu — 2026-01-08 02:41 UTC (2026-01-08 03:41 WAT)

- URL: https://x.com/kankodu/status/2009092977638166896
- Metrics (at fetch): bookmark 4, impression 2843, like 40, quote 0, reply 8, retweet 0

> Any ideas to make sure other SRs can get the context of your protocol quickly?
>
> I’ve created docs, the code is heavily commented etc. 
>
> Anything else?


---

## 2025-10-28 · Post · A detailed breakdown of how LPs can earn lending interest on top of swap fees using https://t.co/BTR


### Post — @kankodu — 2025-10-28 10:42 UTC (2025-10-28 11:42 WAT)

- URL: https://x.com/kankodu/status/1983122250699272247
- Metrics (at fetch): bookmark 4, impression 3515, like 19, quote 0, reply 1, retweet 2

> A detailed breakdown of how LPs can earn lending interest on top of swap fees using https://t.co/BTRwhD1Eyo https://t.co/YoJxIg2SiB

**Quoted post** 1983121873396502706: not readable via the API (deleted, private, or withheld).


---

## 2025-10-21 · Post · ItsHappening.png https://t.co/fqE4dAcxu1


### Post — @kankodu — 2025-10-21 14:06 UTC (2025-10-21 15:06 WAT)

- URL: https://x.com/kankodu/status/1980636801988767869
- Metrics (at fetch): bookmark 1, impression 1856, like 11, quote 0, reply 0, retweet 0

> ItsHappening.png https://t.co/fqE4dAcxu1

**Quoted post** 1980635184920719778: not readable via the API (deleted, private, or withheld).


---

## 2025-10-18 · Post · I'm really loving this pattern for developing the frontend for @vii_finance!


### Post — @kankodu — 2025-10-18 11:16 UTC (2025-10-18 12:16 WAT)

- URL: https://x.com/kankodu/status/1979506827558781094
- Metrics (at fetch): bookmark 3, impression 2487, like 15, quote 0, reply 1, retweet 1

> I'm really loving this pattern for developing the frontend for @vii_finance!
>
> So the protocol you're integrating uses a custom encoding and decoding scheme to store more data in a storage slot. Do you fetch the encoded data from the chain and replicate the decoding logic in your https://t.co/tYeIC6u5on

**Quoted post (full text):**

    #### Quoted post — @kankodu — 2025-09-09 17:29 UTC (2025-09-09 18:29 WAT)
    
    - URL: https://x.com/kankodu/status/1965467493000163600
    - Metrics (at fetch): bookmark 12, impression 4312, like 20, quote 1, reply 5, retweet 1
    
    > PSA for web3 frontend devs:
    >
    > Add Foundry/Hardhat to your frontend repo.
    > It’ll save your users time (and frustration).
    >
    > Here’s why 👇
    


---

## 2025-10-18 · Post · I'm really loving this pattern for developing the frontend for@vii_finance!


### Post — @kankodu — 2025-10-18 11:15 UTC (2025-10-18 12:15 WAT)

- URL: https://x.com/kankodu/status/1979506644200702116
- Metrics (at fetch): bookmark 0, impression 35, like 1, quote 0, reply 0, retweet 0

> I'm really loving this pattern for developing the frontend for@vii_finance!
>
> So the protocol you're integrating uses a custom encoding and decoding scheme to store more data in a storage slot. Do you fetch the encoded data from the chain and replicate the decoding logic in your https://t.co/tYeIC6u5on

**Quoted post (full text):**

    #### Quoted post — @kankodu — 2025-09-09 17:29 UTC (2025-09-09 18:29 WAT)
    
    - URL: https://x.com/kankodu/status/1965467493000163600
    - Metrics (at fetch): bookmark 12, impression 4312, like 20, quote 1, reply 5, retweet 1
    
    > PSA for web3 frontend devs:
    >
    > Add Foundry/Hardhat to your frontend repo.
    > It’ll save your users time (and frustration).
    >
    > Here’s why 👇
    


---

## 2025-09-27 · Post · Why are you, as a gas obsessed smart contract dev, still storing your constructor parameters in stor


Tags (automatic): Smart contract / DeFi


### Post — @kankodu — 2025-09-27 04:59 UTC (2025-09-27 05:59 WAT)

- URL: https://x.com/kankodu/status/1971801955874840636
- Metrics (at fetch): bookmark 5, impression 2896, like 30, quote 1, reply 1, retweet 1

> Why are you, as a gas obsessed smart contract dev, still storing your constructor parameters in storage just to set them once in the initializer and never write to them again?
> Is it so you can clone it from your factory? 
>
> You can do the same with the Clones with immutable args


---

## 2025-09-27 · Post · Why are you, as a gas obsessed smart contract dev, still storing your constructor parameters in stor


Tags (automatic): Smart contract / DeFi


### Post — @kankodu — 2025-09-27 04:57 UTC (2025-09-27 05:57 WAT)

- URL: https://x.com/kankodu/status/1971801468790354419
- Metrics (at fetch): bookmark 0, impression 25, like 0, quote 0, reply 0, retweet 0

> Why are you, as a gas obsessed smart contract dev, still storing your constructor parameters in storage just to set them once in the initializer and never touch them again?
> Is it so you can clone it from your factory? 
>
> You can do the same with the Clones with immutable args


---

## 2025-09-20 · Post · https://t.co/FVDzKIpSXo


### Post — @kankodu — 2025-09-20 00:31 UTC (2025-09-20 01:31 WAT)

- URL: https://x.com/kankodu/status/1969197698310963555
- Metrics (at fetch): bookmark 0, impression 515, like 2, quote 0, reply 0, retweet 0

> https://t.co/FVDzKIpSXo


---

## 2025-09-20 · Reply · @VII_Finance featured in @UniswapFND Builder update 35 👀 https://t.co/Sk5jmCnG5W


### Post — @kankodu — 2025-09-20 00:31 UTC (2025-09-20 01:31 WAT)

- URL: https://x.com/kankodu/status/1969197693340713315
- Metrics (at fetch): bookmark 0, impression 868, like 6, quote 0, reply 1, retweet 1

> @VII_Finance featured in @UniswapFND Builder update #35 👀 https://t.co/Sk5jmCnG5W

**Media:**
- photo: https://pbs.twimg.com/media/G1P-2_sbQAMUAZC.jpg — no alt text provided by author


---

## 2025-09-18 · Reply · @vii_finance mentioned 👀 https://t.co/m786k0PKjU


### Post — @kankodu — 2025-09-18 02:10 UTC (2025-09-18 03:10 WAT)

- URL: https://x.com/kankodu/status/1968497916928004307
- Metrics (at fetch): bookmark 0, impression 100, like 2, quote 0, reply 0, retweet 0

> @vii_finance mentioned 👀 https://t.co/m786k0PKjU

**Quoted post** 1968313999629389974: not readable via the API (deleted, private, or withheld).


---

## 2025-09-16 · Post · We didn’t want to roll our own lending protocol. We checked all of the existing lending protocols an


### Post — @kankodu — 2025-09-16 14:52 UTC (2025-09-16 15:52 WAT)

- URL: https://x.com/kankodu/status/1967964902859083953
- Metrics (at fetch): bookmark 1, impression 3510, like 33, quote 0, reply 3, retweet 4

> We didn’t want to roll our own lending protocol. We checked all of the existing lending protocols and it turned out the only one flexible enough for what we’re building was Euler.
>
> Shoutout to the Euler team for building a protocol that’s actually developer friendly https://t.co/QRdBDsRiZ8

**Quoted post** 1967953785965383981: not readable via the API (deleted, private, or withheld).


---

## 2025-09-16 · Post · Excited to finally share what we’ve been building 👇 https://t.co/nxaRLfNlHM


### Post — @kankodu — 2025-09-16 14:08 UTC (2025-09-16 15:08 WAT)

- URL: https://x.com/kankodu/status/1967953846380138984
- Metrics (at fetch): bookmark 3, impression 2302, like 23, quote 0, reply 0, retweet 0

> Excited to finally share what we’ve been building 👇 https://t.co/nxaRLfNlHM

**Quoted post** 1967952959268151601: not readable via the API (deleted, private, or withheld).


---

## 2025-09-14 · Post · defi money legos final boss https://t.co/8JWVSBuCXV


Tags (automatic): Smart contract / DeFi


### Post — @kankodu — 2025-09-14 07:20 UTC (2025-09-14 08:20 WAT)

- URL: https://x.com/kankodu/status/1967126198863180281
- Metrics (at fetch): bookmark 6, impression 3587, like 20, quote 0, reply 1, retweet 0

> defi money legos final boss https://t.co/8JWVSBuCXV

**Quoted post** 1967125923087741265: not readable via the API (deleted, private, or withheld).


---

## 2025-09-09 · Post · we have been using this pattern to build @vii_finance frontend and it has been very helpful. Here's 


### Post — @kankodu — 2025-09-09 17:29 UTC (2025-09-09 18:29 WAT)

- URL: https://x.com/kankodu/status/1965467642908832221
- Metrics (at fetch): bookmark 2, impression 531, like 5, quote 0, reply 0, retweet 1

> we have been using this pattern to build @vii_finance frontend and it has been very helpful. Here's where I first learned about this pattern: https://t.co/tyFIMdBHMd


---

## 2025-09-09 · Post · If you have need more data, simply make the change in the VaultLens contract and compile it again. Y


### Post — @kankodu — 2025-09-09 17:29 UTC (2025-09-09 18:29 WAT)

- URL: https://x.com/kankodu/status/1965467631001190704
- Metrics (at fetch): bookmark 0, impression 531, like 3, quote 0, reply 1, retweet 0

> If you have need more data, simply make the change in the VaultLens contract and compile it again. You do not need waste gas to deploy it.


---

## 2025-09-09 · Post · Viem exposes this method directly in readContract method so you do not have to deal with raw eth_cal


### Post — @kankodu — 2025-09-09 17:29 UTC (2025-09-09 18:29 WAT)

- URL: https://x.com/kankodu/status/1965467618967728598
- Metrics (at fetch): bookmark 0, impression 205, like 0, quote 0, reply 1, retweet 0

> Viem exposes this method directly in readContract method so you do not have to deal with raw eth_call. https://t.co/cMDbO7k5NP

**Media:**
- photo: https://pbs.twimg.com/media/G0a-Yi0agAAWwNz.jpg — no alt text provided by author


---

## 2025-09-09 · Post · Here’s my suggestion:


### Post — @kankodu — 2025-09-09 17:29 UTC (2025-09-09 18:29 WAT)

- URL: https://x.com/kankodu/status/1965467602333167630
- Metrics (at fetch): bookmark 0, impression 186, like 0, quote 0, reply 1, retweet 0

> Here’s my suggestion:
>
> Have Foundry/Hardhat setup in your frontend repo. Build the lens contract as you need it and compile it. And then you can use eth_call overrides to ask the RPC to pretend the lens contract is deployed and call the method that you need to get the data


---

## 2025-09-09 · Post · These can work, but they’re rigid. Developers try to anticipate every scenario when writing them, bu


### Post — @kankodu — 2025-09-09 17:29 UTC (2025-09-09 18:29 WAT)

- URL: https://x.com/kankodu/status/1965467590467485847
- Metrics (at fetch): bookmark 0, impression 177, like 1, quote 0, reply 1, retweet 0

> These can work, but they’re rigid. Developers try to anticipate every scenario when writing them, but you may need less more than what’s exposed. You also don’t want to deploy new lens contracts every time your requirements change.


---

## 2025-09-09 · Post · Many protocols solve this by building lens contracts. In our example, developer of the protocol woul


### Post — @kankodu — 2025-09-09 17:29 UTC (2025-09-09 18:29 WAT)

- URL: https://x.com/kankodu/status/1965467577892913539
- Metrics (at fetch): bookmark 0, impression 198, like 0, quote 0, reply 1, retweet 0

> Many protocols solve this by building lens contracts. In our example, developer of the protocol would have developed and deployed VaultLens contract that looks like this: https://t.co/Vd5RgfKUj6

**Media:**
- photo: https://pbs.twimg.com/media/G0a-WIMbgAE4xf1.jpg — no alt text provided by author


---

## 2025-09-09 · Post · This is a very simple example. In real DeFi frontends, dependencies get far more complicated. One va


Tags (automatic): Smart contract / DeFi


### Post — @kankodu — 2025-09-09 17:29 UTC (2025-09-09 18:29 WAT)

- URL: https://x.com/kankodu/status/1965467559895142591
- Metrics (at fetch): bookmark 0, impression 202, like 1, quote 0, reply 1, retweet 0

> This is a very simple example. In real DeFi frontends, dependencies get far more complicated. One value depends on another, which depends on another, and your users end up waiting through a chain of RPC calls before the page even loads.


---

## 2025-09-09 · Post · So far so good. But what if you also want the underlying asset decimals?


### Post — @kankodu — 2025-09-09 17:29 UTC (2025-09-09 18:29 WAT)

- URL: https://x.com/kankodu/status/1965467547333193871
- Metrics (at fetch): bookmark 0, impression 223, like 0, quote 0, reply 1, retweet 0

> So far so good. But what if you also want the underlying asset decimals?
>
> Multicall won’t help here. You’d first need to call asset method to get the address, and then make a second call to the decimals method on that address. Frontend has to make two RPC calls to get the data. https://t.co/6XvEONt6Px

**Media:**
- photo: https://pbs.twimg.com/media/G0a-UXBbQAAM7Uk.jpg — no alt text provided by author


---

## 2025-09-09 · Post · If you’re efficient, you’d use Promise.all so you don’t have to wait for one call to finish before s


### Post — @kankodu — 2025-09-09 17:29 UTC (2025-09-09 18:29 WAT)

- URL: https://x.com/kankodu/status/1965467531025809644
- Metrics (at fetch): bookmark 1, impression 283, like 1, quote 0, reply 1, retweet 0

> If you’re efficient, you’d use Promise.all so you don’t have to wait for one call to finish before starting the other.
>
> But you are smarter. You know about multicall. Instead of two RPC calls, you can send one multicall request that returns for both asset and totalAssets. https://t.co/VPAVySu8TS

**Media:**
- photo: https://pbs.twimg.com/media/G0a-TL5a4AAk7Bu.jpg — no alt text provided by author
- photo: https://pbs.twimg.com/media/G0a-TYpa8AAwwpG.png — no alt text provided by author


---

## 2025-09-09 · Post · Suppose you have an ERC4626 vault address and you want to get the underlying asset address and the t


### Post — @kankodu — 2025-09-09 17:29 UTC (2025-09-09 18:29 WAT)

- URL: https://x.com/kankodu/status/1965467510863790378
- Metrics (at fetch): bookmark 0, impression 330, like 0, quote 0, reply 1, retweet 0

> Suppose you have an ERC4626 vault address and you want to get the underlying asset address and the total assets.
>
> What do you do?
>
> 1. Call the asset method on the ERC-4626 vault to get the asset address.
> 2. Call the totalAssets method.
>
> That’s two separate RPC calls. https://t.co/RzRN0NCrZN

**Media:**
- photo: https://pbs.twimg.com/media/G0a-SPibsAAxyg1.jpg — no alt text provided by author


---

## 2025-09-09 · Post · PSA for web3 frontend devs:


### Post — @kankodu — 2025-09-09 17:29 UTC (2025-09-09 18:29 WAT)

- URL: https://x.com/kankodu/status/1965467493000163600
- Metrics (at fetch): bookmark 12, impression 4312, like 20, quote 1, reply 5, retweet 1

> PSA for web3 frontend devs:
>
> Add Foundry/Hardhat to your frontend repo.
> It’ll save your users time (and frustration).
>
> Here’s why 👇


---

## 2025-09-07 · Post · A weird coincidence when I was testing on a mainnet fork: 


### Post — @kankodu — 2025-09-07 04:59 UTC (2025-09-07 05:59 WAT)

- URL: https://x.com/kankodu/status/1964554138404213243
- Metrics (at fetch): bookmark 2, impression 2991, like 33, quote 0, reply 3, retweet 1

> A weird coincidence when I was testing on a mainnet fork: 
>
> Locally, the contract was deployed to an address that already had some ETH on mainnet. 
> This broke the accounting and took me three days to debug 😅, since I wasn’t expecting the contract to have an initial balance


---

## 2025-09-01 · Post · https://t.co/KhwPInVwPl


### Post — @kankodu — 2025-09-01 08:46 UTC (2025-09-01 09:46 WAT)

- URL: https://x.com/kankodu/status/1962436910078734493
- Metrics (at fetch): bookmark 0, impression 375, like 2, quote 0, reply 0, retweet 0

> https://t.co/KhwPInVwPl


---

## 2025-09-01 · Reply · @vii_finance is using a similar mechanism so that Liquidity Providers can keep earning lending inter


### Post — @kankodu — 2025-09-01 08:46 UTC (2025-09-01 09:46 WAT)

- URL: https://x.com/kankodu/status/1962436849882059139
- Metrics (at fetch): bookmark 1, impression 662, like 6, quote 0, reply 2, retweet 0

> @vii_finance is using a similar mechanism so that Liquidity Providers can keep earning lending interest on top of swap fees without "yield-derived impermanent loss".
>
> The main difference is that it is done using a uniswap v4 hook https://t.co/O9b0HB4PWb

**Quoted post** 1960880396784296013: not readable via the API (deleted, private, or withheld).


---

## 2025-08-27 · Post · https://t.co/zlZgrx7zDY


### Post — @kankodu — 2025-08-27 11:07 UTC (2025-08-27 12:07 WAT)

- URL: https://x.com/kankodu/status/1960660534799499455
- Metrics (at fetch): bookmark 0, impression 506, like 2, quote 0, reply 0, retweet 0

> https://t.co/zlZgrx7zDY


---

## 2025-08-27 · Post · A uniswap v4 hook that I’ve developed for @vii_finance donates accrued interest to the active liquid


### Post — @kankodu — 2025-08-27 11:07 UTC (2025-08-27 12:07 WAT)

- URL: https://x.com/kankodu/status/1960660384031105382
- Metrics (at fetch): bookmark 6, impression 1867, like 18, quote 0, reply 7, retweet 0

> A uniswap v4 hook that I’ve developed for @vii_finance donates accrued interest to the active liquidity providers of the same pool before every add/remove liquidity and swap actions
>
> The hook has to do 6 external calls to pay!!
>
> Can someone suggest a way to reduce the gas cost? https://t.co/u3xW6FNroP

**Media:**
- photo: https://pbs.twimg.com/media/GzWqOaSWkAAqcxN.jpg — no alt text provided by author


---

## 2025-08-05 · Post · cooking something 🧑‍🍳 https://t.co/LZDxTNJJBs


### Post — @kankodu — 2025-08-05 11:52 UTC (2025-08-05 12:52 WAT)

- URL: https://x.com/kankodu/status/1952699297901801649
- Metrics (at fetch): bookmark 1, impression 1884, like 43, quote 0, reply 2, retweet 0

> cooking something 🧑‍🍳 https://t.co/LZDxTNJJBs

**Media:**
- photo: https://pbs.twimg.com/media/GxlhBoIXgAAuN7S.png — no alt text provided by author


---

## 2023-07-29 · Post · A bug that was supposed to be only a good thought experiment inadvertently ended up making me $33.5k


### Post — @kankodu — 2023-07-29 16:05 UTC (2023-07-29 17:05 WAT)

- URL: https://x.com/kankodu/status/1685320718870032384
- Metrics (at fetch): bookmark 320, impression 43492, like 325, quote 9, reply 7, repost 66

> A bug that was supposed to be only a good thought experiment inadvertently ended up making me $33.5k.
> Here are the details 🧵:
