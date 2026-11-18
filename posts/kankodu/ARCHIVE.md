# @kankodu — full verbatim X archive (security-relevant posts)

_Generated 2026-11-18 from the X API (full-archive search + timeline). Every post below is copied word-for-word; t.co links are expanded; quoted posts are inlined in full; media are listed with alt text when the author provided it. Posts are grouped by conversation (a thread = the author's root post followed by their own replies, oldest first). Groups are newest first. An agent without X access can rely on this file._

- Posts in this file: 166
- Conversations/threads: 80
- Oldest post captured: 2022-07-26
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


**Context — conversation root by another account:**

#### Root post — @WhiteHatMage — 2026-06-02 15:38 UTC (2026-06-02 16:38 WAT)

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

## 2026-01-12 · Thread · The competition is now live! https://t.co/XBNgp2Fpnu


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
    


### Thread part 2 — @kankodu — 2026-01-12 18:17 UTC (2026-01-12 19:17 WAT)

- URL: https://x.com/kankodu/status/2010778298364956949
- Metrics (at fetch): bookmark 0, impression 715, like 5, quote 0, reply 0, retweet 0

> https://t.co/xDU1xm8p3s


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

## 2025-09-20 · Thread · @VII_Finance featured in @UniswapFND Builder update 35 👀 https://t.co/Sk5jmCnG5W


### Post — @kankodu — 2025-09-20 00:31 UTC (2025-09-20 01:31 WAT)

- URL: https://x.com/kankodu/status/1969197693340713315
- Metrics (at fetch): bookmark 0, impression 868, like 6, quote 0, reply 1, retweet 1

> @VII_Finance featured in @UniswapFND Builder update #35 👀 https://t.co/Sk5jmCnG5W

**Media:**
- photo: https://pbs.twimg.com/media/G1P-2_sbQAMUAZC.jpg — no alt text provided by author


### Thread part 2 — @kankodu — 2025-09-20 00:31 UTC (2025-09-20 01:31 WAT)

- URL: https://x.com/kankodu/status/1969197698310963555
- Metrics (at fetch): bookmark 0, impression 515, like 2, quote 0, reply 0, retweet 0

> https://t.co/FVDzKIpSXo


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

## 2025-09-09 · Thread · PSA for web3 frontend devs:


Tags (automatic): Smart contract / DeFi


### Post — @kankodu — 2025-09-09 17:29 UTC (2025-09-09 18:29 WAT)

- URL: https://x.com/kankodu/status/1965467493000163600
- Metrics (at fetch): bookmark 12, impression 4312, like 20, quote 1, reply 5, retweet 1

> PSA for web3 frontend devs:
>
> Add Foundry/Hardhat to your frontend repo.
> It’ll save your users time (and frustration).
>
> Here’s why 👇


### Thread part 2 — @kankodu — 2025-09-09 17:29 UTC (2025-09-09 18:29 WAT)

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


### Thread part 3 — @kankodu — 2025-09-09 17:29 UTC (2025-09-09 18:29 WAT)

- URL: https://x.com/kankodu/status/1965467531025809644
- Metrics (at fetch): bookmark 1, impression 283, like 1, quote 0, reply 1, retweet 0

> If you’re efficient, you’d use Promise.all so you don’t have to wait for one call to finish before starting the other.
>
> But you are smarter. You know about multicall. Instead of two RPC calls, you can send one multicall request that returns for both asset and totalAssets. https://t.co/VPAVySu8TS

**Media:**
- photo: https://pbs.twimg.com/media/G0a-TL5a4AAk7Bu.jpg — no alt text provided by author
- photo: https://pbs.twimg.com/media/G0a-TYpa8AAwwpG.png — no alt text provided by author


### Thread part 4 — @kankodu — 2025-09-09 17:29 UTC (2025-09-09 18:29 WAT)

- URL: https://x.com/kankodu/status/1965467547333193871
- Metrics (at fetch): bookmark 0, impression 223, like 0, quote 0, reply 1, retweet 0

> So far so good. But what if you also want the underlying asset decimals?
>
> Multicall won’t help here. You’d first need to call asset method to get the address, and then make a second call to the decimals method on that address. Frontend has to make two RPC calls to get the data. https://t.co/6XvEONt6Px

**Media:**
- photo: https://pbs.twimg.com/media/G0a-UXBbQAAM7Uk.jpg — no alt text provided by author


### Thread part 5 — @kankodu — 2025-09-09 17:29 UTC (2025-09-09 18:29 WAT)

- URL: https://x.com/kankodu/status/1965467559895142591
- Metrics (at fetch): bookmark 0, impression 202, like 1, quote 0, reply 1, retweet 0

> This is a very simple example. In real DeFi frontends, dependencies get far more complicated. One value depends on another, which depends on another, and your users end up waiting through a chain of RPC calls before the page even loads.


### Thread part 6 — @kankodu — 2025-09-09 17:29 UTC (2025-09-09 18:29 WAT)

- URL: https://x.com/kankodu/status/1965467577892913539
- Metrics (at fetch): bookmark 0, impression 198, like 0, quote 0, reply 1, retweet 0

> Many protocols solve this by building lens contracts. In our example, developer of the protocol would have developed and deployed VaultLens contract that looks like this: https://t.co/Vd5RgfKUj6

**Media:**
- photo: https://pbs.twimg.com/media/G0a-WIMbgAE4xf1.jpg — no alt text provided by author


### Thread part 7 — @kankodu — 2025-09-09 17:29 UTC (2025-09-09 18:29 WAT)

- URL: https://x.com/kankodu/status/1965467590467485847
- Metrics (at fetch): bookmark 0, impression 177, like 1, quote 0, reply 1, retweet 0

> These can work, but they’re rigid. Developers try to anticipate every scenario when writing them, but you may need less more than what’s exposed. You also don’t want to deploy new lens contracts every time your requirements change.


### Thread part 8 — @kankodu — 2025-09-09 17:29 UTC (2025-09-09 18:29 WAT)

- URL: https://x.com/kankodu/status/1965467602333167630
- Metrics (at fetch): bookmark 0, impression 186, like 0, quote 0, reply 1, retweet 0

> Here’s my suggestion:
>
> Have Foundry/Hardhat setup in your frontend repo. Build the lens contract as you need it and compile it. And then you can use eth_call overrides to ask the RPC to pretend the lens contract is deployed and call the method that you need to get the data


### Thread part 9 — @kankodu — 2025-09-09 17:29 UTC (2025-09-09 18:29 WAT)

- URL: https://x.com/kankodu/status/1965467618967728598
- Metrics (at fetch): bookmark 0, impression 205, like 0, quote 0, reply 1, retweet 0

> Viem exposes this method directly in readContract method so you do not have to deal with raw eth_call. https://t.co/cMDbO7k5NP

**Media:**
- photo: https://pbs.twimg.com/media/G0a-Yi0agAAWwNz.jpg — no alt text provided by author


### Thread part 10 — @kankodu — 2025-09-09 17:29 UTC (2025-09-09 18:29 WAT)

- URL: https://x.com/kankodu/status/1965467631001190704
- Metrics (at fetch): bookmark 0, impression 531, like 3, quote 0, reply 1, retweet 0

> If you have need more data, simply make the change in the VaultLens contract and compile it again. You do not need waste gas to deploy it.


### Thread part 11 — @kankodu — 2025-09-09 17:29 UTC (2025-09-09 18:29 WAT)

- URL: https://x.com/kankodu/status/1965467642908832221
- Metrics (at fetch): bookmark 2, impression 531, like 5, quote 0, reply 0, retweet 1

> we have been using this pattern to build @vii_finance frontend and it has been very helpful. Here's where I first learned about this pattern: https://t.co/tyFIMdBHMd


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

## 2025-09-01 · Thread · @vii_finance is using a similar mechanism so that Liquidity Providers can keep earning lending inter


### Post — @kankodu — 2025-09-01 08:46 UTC (2025-09-01 09:46 WAT)

- URL: https://x.com/kankodu/status/1962436849882059139
- Metrics (at fetch): bookmark 1, impression 662, like 6, quote 0, reply 2, retweet 0

> @vii_finance is using a similar mechanism so that Liquidity Providers can keep earning lending interest on top of swap fees without "yield-derived impermanent loss".
>
> The main difference is that it is done using a uniswap v4 hook https://t.co/O9b0HB4PWb

**Quoted post** 1960880396784296013: not readable via the API (deleted, private, or withheld).


### Thread part 2 — @kankodu — 2025-09-01 08:46 UTC (2025-09-01 09:46 WAT)

- URL: https://x.com/kankodu/status/1962436910078734493
- Metrics (at fetch): bookmark 0, impression 375, like 2, quote 0, reply 0, retweet 0

> https://t.co/KhwPInVwPl


---

## 2025-08-27 · Thread · A uniswap v4 hook that I’ve developed for @vii_finance donates accrued interest to the active liquid


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


### Thread part 2 — @kankodu — 2025-08-27 11:07 UTC (2025-08-27 12:07 WAT)

- URL: https://x.com/kankodu/status/1960660534799499455
- Metrics (at fetch): bookmark 0, impression 506, like 2, quote 0, reply 0, retweet 0

> https://t.co/zlZgrx7zDY


---

## 2025-08-05 · Post · cooking something 🧑‍🍳 https://t.co/LZDxTNJJBs


### Post — @kankodu — 2025-08-05 11:52 UTC (2025-08-05 12:52 WAT)

- URL: https://x.com/kankodu/status/1952699297901801649
- Metrics (at fetch): bookmark 1, impression 1884, like 43, quote 0, reply 2, retweet 0

> cooking something 🧑‍🍳 https://t.co/LZDxTNJJBs

**Media:**
- photo: https://pbs.twimg.com/media/GxlhBoIXgAAuN7S.png — no alt text provided by author


---

## 2025-03-26 · Thread · How to drain an entire lending protocol when a new asset is accepted as collateral 🧵


Tags (automatic): Platform: Immunefi


### Post — @kankodu — 2025-03-26 09:03 UTC (2025-03-26 10:03 WAT)

- URL: https://x.com/kankodu/status/1904821401510699389
- Metrics (at fetch): bookmark 182, impression 14812, like 175, quote 3, reply 6, retweet 13

> How to drain an entire lending protocol when a new asset is accepted as collateral 🧵
>
> And no, it’s not just another Compound fork. https://t.co/1ALDCjseh0

**Media:**
- photo: https://pbs.twimg.com/media/Gm9I-FZa4AA48BW.png — no alt text provided by author


### Thread part 2 — @kankodu — 2025-03-26 09:03 UTC (2025-03-26 10:03 WAT)

- URL: https://x.com/kankodu/status/1904821413745487874
- Metrics (at fetch): bookmark 12, impression 5488, like 22, quote 1, reply 1, retweet 0

> I reported this issue in @vesuxyz through @immunefi bug bounty program and was classified as High.
>
> Take a look at here to see how the team fixed it: https://t.co/KblcXvRs85
>
> This fix has been audited. You can take a look at the audit report here: https://t.co/VjY2tIWmL6


### Thread part 3 — @kankodu — 2025-03-26 09:03 UTC (2025-03-26 10:03 WAT)

- URL: https://x.com/kankodu/status/1904821425808331025
- Metrics (at fetch): bookmark 0, impression 1438, like 3, quote 0, reply 1, retweet 0

> @vesuxyz is a lending protocol developed in Cairo. It can deploy multiple pools, each being its own lending market with various collateral-debt asset pairs. The max ltv for a pair determines if collateral can be used to borrow debt assets.


### Thread part 4 — @kankodu — 2025-03-26 09:03 UTC (2025-03-26 10:03 WAT)

- URL: https://x.com/kankodu/status/1904821437837566158
- Metrics (at fetch): bookmark 0, impression 1512, like 3, quote 1, reply 1, retweet 0

> This enables various lending market configurations. The Genesis pool, currently the only pool with significant TVL, is set up like a traditional lending market with rehypothecation.
>
> By completing three steps, we can deplete this pool when a new asset is added. How?


### Thread part 5 — @kankodu — 2025-03-26 09:03 UTC (2025-03-26 10:03 WAT)

- URL: https://x.com/kankodu/status/1904821454811914344
- Metrics (at fetch): bookmark 1, impression 1411, like 3, quote 0, reply 2, retweet 0

> Step 1. Mint a tiny amount of shares and donate to reserves making the shares valuable enough to borrow all the protocol's assets.
>
> - The problem is when the total shares is zero, the protocol mints 1000 shares to a dead address. https://t.co/YcQtrdpzBZ

**Media:**
- photo: https://pbs.twimg.com/media/Gm9JBLTacAAlizr.jpg — alt text: "https://github.com/vesuxyz/vesu-v1/blob/85e5552f4a8d4ed036240723375fe38f92625a2c/src/singleton.cairo#L609-L622"


### Thread part 6 — @kankodu — 2025-03-26 09:03 UTC (2025-03-26 10:03 WAT)

- URL: https://x.com/kankodu/status/1904821467294162994
- Metrics (at fetch): bookmark 0, impression 1216, like 3, quote 0, reply 1, retweet 0

> This check makes the vault share inflation attack very expensive and not worth it. What if there were a way to circumvent this check?
>
> If we really look for it, we can find it.


### Thread part 7 — @kankodu — 2025-03-26 09:03 UTC (2025-03-26 10:03 WAT)

- URL: https://x.com/kankodu/status/1904821484671164478
- Metrics (at fetch): bookmark 0, impression 1182, like 3, quote 0, reply 1, retweet 0

> When lenders earn interest, the protocol takes a cut as protocol fees. The protocol mints collateral shares equivalent to the fee amount, increasing total shares directly without minting shares to a dead address. https://t.co/MvUar2V5X5

**Media:**
- photo: https://pbs.twimg.com/media/Gm9JC6VbYAU65Ac.jpg — alt text: "https://github.com/vesuxyz/vesu-v1/blob/85e5552f4a8d4ed036240723375fe38f92625a2c/src/singleton.cairo#L578-L593"


### Thread part 8 — @kankodu — 2025-03-26 09:03 UTC (2025-03-26 10:03 WAT)

- URL: https://x.com/kankodu/status/1904821496968863762
- Metrics (at fetch): bookmark 0, impression 1040, like 4, quote 0, reply 2, retweet 0

> An attacker can donate to the reserves when the total shares is zero and borrow from the donated tokens long enough for &lt;500 wei of fee shares to be minted to the protocol.


### Thread part 9 — @kankodu — 2025-03-26 09:03 UTC (2025-03-26 10:03 WAT)

- URL: https://x.com/kankodu/status/1904821508956152097
- Metrics (at fetch): bookmark 0, impression 997, like 3, quote 0, reply 1, retweet 0

> Now that the total shares is non-zero, the attacker can then mint &lt;500 wei of shares and donate a large amount to the reserves, This makes this tiny shares worth a lot.
>
> Step 2. Legally borrow all the protocol's assets against your tiny but highly valuable collateral shares.


### Thread part 10 — @kankodu — 2025-03-26 09:03 UTC (2025-03-26 10:03 WAT)

- URL: https://x.com/kankodu/status/1904821520792506615
- Metrics (at fetch): bookmark 1, impression 953, like 3, quote 0, reply 1, retweet 0

> Step 3. Retrieve the donated amount without repaying the borrowed assets in Step 2.
>
> This is crucial. Otherwise, it’s not really an attack. Attacker needs to be creative and find a loophole in the protocol to accomplish this.


### Thread part 11 — @kankodu — 2025-03-26 09:03 UTC (2025-03-26 10:03 WAT)

- URL: https://x.com/kankodu/status/1904821537305469250
- Metrics (at fetch): bookmark 0, impression 980, like 6, quote 0, reply 1, retweet 0

> The attacker can exploit the protocol's mechanism that resets the total supply to zero when it is less than or equal to 1000 wei during withdrawal. This mechanism, intended to reset the share/assets ratio but it can be weaponized to retrieve the donated amount. https://t.co/LBIHrU6Oxj

**Media:**
- photo: https://pbs.twimg.com/media/Gm9JF_PbYAIdlC2.jpg — alt text: "https://github.com/vesuxyz/vesu-v1/blob/85e5552f4a8d4ed036240723375fe38f92625a2c/src/common.cairo#L402-L406"


### Thread part 12 — @kankodu — 2025-03-26 09:03 UTC (2025-03-26 10:03 WAT)

- URL: https://x.com/kankodu/status/1904821549498327233
- Metrics (at fetch): bookmark 0, impression 891, like 4, quote 0, reply 1, retweet 0

> The attacker starts using a seperate account now. Using this new account they can deposit and withdraw 1 wei to trigger this logic. Since the total shares is &lt; 1000 wei (&lt;500 wei to the protocol as fee shares + &lt;500 wei minted by the attacker), the total supply will reset to zero


### Thread part 13 — @kankodu — 2025-03-26 09:03 UTC (2025-03-26 10:03 WAT)

- URL: https://x.com/kankodu/status/1904821561372356623
- Metrics (at fetch): bookmark 0, impression 1602, like 7, quote 0, reply 1, retweet 0

> The attacker then simply mints a small amount of shares. This time, the attacker doesn't care that 1000 wei are being sent to zero. They will mint enough shares such that 1000 wei becomes insignificant compared to the shares minted at a 1:1 ratio.


### Thread part 14 — @kankodu — 2025-03-26 09:03 UTC (2025-03-26 10:03 WAT)

- URL: https://x.com/kankodu/status/1904821573284225458
- Metrics (at fetch): bookmark 0, impression 1506, like 9, quote 0, reply 1, retweet 0

> This small amount of shares will be worth a large amount of tokens since there are no other the attacker is the only holder of all existing shares. This way, attacker can recover all of their donated amounts to complete the attack without repaying all of funds taken in Step 2 !!!


---

## 2025-03-08 · Post · Had a great time talking to @0xriptide about all things bug hunting! Give it a listen: https://t.co/


### Post — @kankodu — 2025-03-08 15:52 UTC (2025-03-08 16:52 WAT)

- URL: https://x.com/kankodu/status/1898401342860750933
- Metrics (at fetch): bookmark 7, impression 3429, like 29, quote 0, reply 0, retweet 1

> Had a great time talking to @0xriptide about all things bug hunting! Give it a listen: https://t.co/UWH3KUDEoh

**Quoted post (full text):**

    #### Quoted post — @1877728835216568321 — 2025-03-08 14:35 UTC (2025-03-08 15:35 WAT)
    
    - URL: https://x.com/1877728835216568321/status/1898381975477469334
    - Metrics (at fetch): bookmark 13, impression 6621, like 53, quote 2, reply 4, retweet 4
    
    > BOUNTYHUNT3RZ Episode 6: w/ @kankodu 
    >
    > @0xriptide &amp; @kankodu discuss his bug hunting techniques to keep him in the top #20 of the immunefi leaderboard, a deep dive on his recent $250k Balancer bug writeup that he kept under wraps for 2 years, bounty negotiations and how to shoot https://t.co/RtdCylPS69
    
    **Media:**
    - media `7_1898380897306460160` (details not returned by the API)
    


---

## 2025-02-22 · Post · ... an attacker deposits a infinite amount of non-existent ERC20. The Vault’s safeTransferFrom succe


Tags (automatic): Smart contract / DeFi


### Post — @kankodu — 2025-02-22 07:48 UTC (2025-02-22 08:48 WAT)

- URL: https://x.com/kankodu/status/1893206329411424442
- Metrics (at fetch): bookmark 2, impression 1995, like 13, quote 0, reply 1, retweet 0

> ... an attacker deposits a infinite amount of non-existent ERC20. The Vault’s safeTransferFrom succeeds (no code existence check), and increases attacker's internal balancer by infinity. Once the ERC20 is actually deployed and real users deposit, the attacker drains the funds.


---

## 2025-02-22 · Post · I examined common ERC20 helper libraries. Solmate's safeTransferFrom function didn't verify if the E


Tags (automatic): Smart contract / DeFi


### Post — @kankodu — 2025-02-22 07:48 UTC (2025-02-22 08:48 WAT)

- URL: https://x.com/kankodu/status/1893206323350630661
- Metrics (at fetch): bookmark 2, impression 1611, like 11, quote 0, reply 1, retweet 0

> I examined common ERC20 helper libraries. Solmate's safeTransferFrom function didn't verify if the ERC20 address had code (at the time), posing potential risks. In contrast, OpenZeppelin's SafeERC20 included this crucial check, ensuring safety from such issues. https://t.co/ktP2vF7zn9

**Media:**
- photo: https://pbs.twimg.com/media/GkYBQ4LXMAAMfWD.jpg — no alt text provided by author


---

## 2025-02-22 · Thread · Two years ago, I discovered a critical vulnerability in Balancer V2 that allowed attackers to create


Tags (automatic): Smart contract / DeFi


### Post — @kankodu — 2025-02-22 07:48 UTC (2025-02-22 08:48 WAT)

- URL: https://x.com/kankodu/status/1893206310105080058
- Metrics (at fetch): bookmark 273, impression 21014, like 386, quote 3, reply 8, retweet 35

> Two years ago, I discovered a critical vulnerability in Balancer V2 that allowed attackers to create infinite token balances by front-running ERC20 deployments.
>
> This bug earned me a $250k reward and was recently disclosed publicly: https://t.co/Xysko69K6s

**Media:**
- photo: https://pbs.twimg.com/media/GkYAHuAWQAEgu5J.png — no alt text provided by author


### Thread part 2 — @kankodu — 2025-02-22 07:48 UTC (2025-02-22 08:48 WAT)

- URL: https://x.com/kankodu/status/1893206315104641521
- Metrics (at fetch): bookmark 5, impression 1973, like 15, quote 0, reply 1, retweet 0

> My journey began with a simple question: What happens when `call` is made to an address without code? While Solidity adds a check that causes failure if the address lacks code, low level call returns success. 
>
> This can cause problem with helper libraries we use to pull funds. https://t.co/0KKsy2xZom

**Media:**
- photo: https://pbs.twimg.com/media/GkYBFQhaIAArpHq.jpg — no alt text provided by author


---

## 2024-12-28 · Post · Another good year on @immunefi https://t.co/LFMliy3rjj


Tags (automatic): Platform: Immunefi


### Post — @kankodu — 2024-12-28 14:47 UTC (2024-12-28 15:47 WAT)

- URL: https://x.com/kankodu/status/1873017953790378233
- Metrics (at fetch): bookmark 14, impression 6288, like 151, quote 0, reply 4, retweet 5

> Another good year on @immunefi https://t.co/LFMliy3rjj

**Media:**
- photo: https://pbs.twimg.com/media/Gf5LZXBWcAAmZZ7.jpg — no alt text provided by author


---

## 2024-10-20 · Post · A whitehat finds a bug in a permissioned DEX where attackers can transact before an asset is listed 


### Post — @kankodu — 2024-10-20 08:22 UTC (2024-10-20 09:22 WAT)

- URL: https://x.com/kankodu/status/1847916295666225575
- Metrics (at fetch): bookmark 4, impression 2993, like 10, quote 1, reply 2, retweet 0

> A whitehat finds a bug in a permissioned DEX where attackers can transact before an asset is listed to gain infinite internal balance and later withdraw it for real assets from LPs. 
>
> Current TVL: $100M
> An asset got $10M of deposits in the first 20 days.
>
> What’s the right payout?


---

## 2024-10-17 · Post · A whitehat finds a way to empty the entire lending protocol ($10 million at risk) when a new asset i


### Post — @kankodu — 2024-10-17 19:48 UTC (2024-10-17 20:48 WAT)

- URL: https://x.com/kankodu/status/1847001695919714360
- Metrics (at fetch): bookmark 7, impression 6753, like 18, quote 1, reply 7, retweet 1

> A whitehat finds a way to empty the entire lending protocol ($10 million at risk) when a new asset is accepted as collateral.
>
> How much should this bug disclosure be paid?


---

## 2024-07-29 · Post · Check out my profile on @immunefi


Tags (automatic): Blockchain / L1-L2 / bridge, Platform: Immunefi


### Post — @kankodu — 2024-07-29 15:58 UTC (2024-07-29 16:58 WAT)

- URL: https://x.com/kankodu/status/1817952969276457276
- Metrics (at fetch): bookmark 5, impression 5717, like 68, quote 1, reply 5, retweet 2

> Check out my profile on @immunefi
> #OnchainDefender 
>
> https://t.co/HYRy89gJ0S


---

## 2024-05-30 · Thread · I found an interesting bug in a lending market where an invariant check, made for the safety of the 


Tags (automatic): Smart contract / DeFi


### Post — @kankodu — 2024-05-30 10:13 UTC (2024-05-30 11:13 WAT)

- URL: https://x.com/kankodu/status/1796122807773904959
- Metrics (at fetch): bookmark 92, impression 8801, like 97, quote 0, reply 3, retweet 10

> I found an interesting bug in a lending market where an invariant check, made for the safety of the protocol, could have been used against it to permanently freeze the funds in the protocol.
>
> A small thread ⬇️🧵


### Thread part 2 — @kankodu — 2024-05-30 10:13 UTC (2024-05-30 11:13 WAT)

- URL: https://x.com/kankodu/status/1796122811360055305
- Metrics (at fetch): bookmark 2, impression 1723, like 4, quote 0, reply 1, retweet 0

> The bug was in @InterlayHQ , which has a lending market similar to Compound. We know that making the exchange rate very high by donating tokens results in the next user receiving zero tokens due to rounding error. https://t.co/5a3kbtlIRt

**Media:**
- photo: https://pbs.twimg.com/media/GO0bIstWMAMj8VS.png — alt text: "Interlay lending market"


### Thread part 3 — @kankodu — 2024-05-30 10:13 UTC (2024-05-30 11:13 WAT)

- URL: https://x.com/kankodu/status/1796122818867822666
- Metrics (at fetch): bookmark 2, impression 1742, like 2, quote 0, reply 1, retweet 0

> Interlay introduced a check to ensure that the exchange rate should start at 0.02 and shouldn't exceed 1. An exchange rate of 1 is very high if everything operates as usual. https://t.co/Qe6ng95ujo

**Media:**
- photo: https://pbs.twimg.com/media/GO0bz97XEAAGIaW.jpg — no alt text provided by author


### Thread part 4 — @kankodu — 2024-05-30 10:13 UTC (2024-05-30 11:13 WAT)

- URL: https://x.com/kankodu/status/1796122821510234565
- Metrics (at fetch): bookmark 1, impression 1730, like 3, quote 0, reply 1, retweet 0

> For example, given current lending rates, it would take at least ~3 centuries for a USDT exchange rate to start from 0.02 and reach 1 due to normal interest accrual. This means this check does solve a problem, but an attacker can exploit it to create another issue.


### Thread part 5 — @kankodu — 2024-05-30 10:13 UTC (2024-05-30 11:13 WAT)

- URL: https://x.com/kankodu/status/1796122823737376990
- Metrics (at fetch): bookmark 2, impression 2160, like 6, quote 0, reply 1, retweet 0

> When the market is empty, an attacker can supply 1 wei of underlying tokens (in exchange for 50 loan tokens because the initial exchange rate is 0.02) and transfer 48 wei of underlying tokens directly to the loan token address.


### Thread part 6 — @kankodu — 2024-05-30 10:13 UTC (2024-05-30 11:13 WAT)

- URL: https://x.com/kankodu/status/1796122826002337884
- Metrics (at fetch): bookmark 1, impression 1846, like 1, quote 0, reply 1, retweet 0

> This results in the exchange rate being very close to 1 but not equal to 1 (49/50 = 0.98). Everything works correctly until, after ~six months, the exchange rate exceeds 1.


### Thread part 7 — @kankodu — 2024-05-30 10:13 UTC (2024-05-30 11:13 WAT)

- URL: https://x.com/kankodu/status/1796122828212765153
- Metrics (at fetch): bookmark 2, impression 1796, like 8, quote 0, reply 1, retweet 0

> At that point, everything gets frozen as the exchange rate is calculated before every operation (lend, borrow, repay, liquidate), and the invariant check fails.
>
> The takeaway is to ensure that the solution to a bug doesn't inadvertently introduce new bugs.


---

## 2024-03-22 · Thread · Here's a 🧵 about a bug pattern I've used to get paid across 5 bug reports totaling $150k. This very 


Tags (automatic): Smart contract / DeFi


### Post — @kankodu — 2024-03-22 17:35 UTC (2024-03-22 18:35 WAT)

- URL: https://x.com/kankodu/status/1771229163942474096
- Metrics (at fetch): bookmark 492, impression 40312, like 278, quote 8, reply 9, retweet 45

> Here's a 🧵 about a bug pattern I've used to get paid across 5 bug reports totaling $150k. This very bug pattern has been the culprit behind significant hacks, leading to losses of $464k in Wise lending and a staggering $6M in MIM (the protocols I missed 😅) [pic.x.com/1bPtYzgXbd]

**Media:**
- photo: https://pbs.twimg.com/media/GJSriZAacAEMNEu.png — no alt text provided by author


### Thread part 2 — @kankodu — 2024-03-22 17:35 UTC (2024-03-22 18:35 WAT)

- URL: https://x.com/kankodu/status/1771229168233259312
- Metrics (at fetch): bookmark 1, impression 3501, like 13, quote 0, reply 1, retweet 0

> Let's take a simple lending protocol that has a share-based calculation. The lenders are expected to deposit an underlying asset to the protocol, and in turn, they get minted shares based on the current totalAssets and totalSupply (of shares) ratio.


### Thread part 3 — @kankodu — 2024-03-22 17:35 UTC (2024-03-22 18:35 WAT)

- URL: https://x.com/kankodu/status/1771229171622244829
- Metrics (at fetch): bookmark 1, impression 3350, like 9, quote 0, reply 1, retweet 0

> As interest accrues in the protocol, the value of a share in underlying terms increases, and this mechanism allows the protocol to distribute the interest proportionally to every lender without looping over all the existing lenders.


### Thread part 4 — @kankodu — 2024-03-22 17:35 UTC (2024-03-22 18:35 WAT)

- URL: https://x.com/kankodu/status/1771229174998659202
- Metrics (at fetch): bookmark 2, impression 3278, like 6, quote 0, reply 1, retweet 0

> When a user deposits some amount in the protocol, the shares they get minted are given by the formula shareToBeMinted = (amount * totalSupply) / totalAssets. Here, the division that happens, solidity rounds down by default.


### Thread part 5 — @kankodu — 2024-03-22 17:35 UTC (2024-03-22 18:35 WAT)

- URL: https://x.com/kankodu/status/1771229178433794055
- Metrics (at fetch): bookmark 1, impression 3127, like 7, quote 0, reply 1, retweet 0

> That means that if totalAssets are greater than the (amount * totalSupply), then the shareToBeMinted is zero.


### Thread part 6 — @kankodu — 2024-03-22 17:35 UTC (2024-03-22 18:35 WAT)

- URL: https://x.com/kankodu/status/1771229181608882303
- Metrics (at fetch): bookmark 0, impression 3052, like 8, quote 0, reply 1, retweet 0

> Now, if totalAssets is being read by using the current balance of the lending contract, then an attacker can mint 1 share when totalSupply is 0, donate a large amount of underlying tokens directly to the protocol to inflate the price of 1 wei of share to a large amount.


### Thread part 7 — @kankodu — 2024-03-22 17:35 UTC (2024-03-22 18:35 WAT)

- URL: https://x.com/kankodu/status/1771229184926577154
- Metrics (at fetch): bookmark 2, impression 3218, like 7, quote 1, reply 2, retweet 0

> How would the attack inflate the price even if totalAssets were being tracked internally? The answer is that if 1 wei can be donated, then why not a million ethers.
>
> Let's take an initial condition of totalSupply = 1 and totalAssets = 2.


### Thread part 8 — @kankodu — 2024-03-22 17:35 UTC (2024-03-22 18:35 WAT)

- URL: https://x.com/kankodu/status/1771229188290408457
- Metrics (at fetch): bookmark 1, impression 2965, like 5, quote 0, reply 1, retweet 0

> We will talk about how to achieve this initial condition later. For now, if a user deposits 1 wei of assets, then the shares minted to them would be (amount * totalSupply )/ totalAssets = 1 * 1 / 2 = 0.5 = 0 (due to rounding down)


### Thread part 9 — @kankodu — 2024-03-22 17:35 UTC (2024-03-22 18:35 WAT)

- URL: https://x.com/kankodu/status/1771229199136878856
- Metrics (at fetch): bookmark 1, impression 3071, like 5, quote 0, reply 1, retweet 0

> Now the totalAssets would have been increased to 2+1 = 3, and totalSupply stays at 1+0= 1. See below table to see what happens if a user continues to deposit an amount = totalAssets -1 in a loop. [pic.x.com/sC7qIZY0F0]

**Media:**
- photo: https://pbs.twimg.com/media/GJSrkWZacAAB9ox.jpg — no alt text provided by author


### Thread part 10 — @kankodu — 2024-03-22 17:35 UTC (2024-03-22 18:35 WAT)

- URL: https://x.com/kankodu/status/1771229203100496037
- Metrics (at fetch): bookmark 0, impression 2887, like 4, quote 0, reply 1, retweet 0

> Every time, the user gets minted amount * totalSupply / totalAssets = (totalAssets - 1) * 1 / totalAssets = 0 shares, and totalAssets almost double.


### Thread part 11 — @kankodu — 2024-03-22 17:35 UTC (2024-03-22 18:35 WAT)

- URL: https://x.com/kankodu/status/1771229211216543992
- Metrics (at fetch): bookmark 0, impression 2972, like 6, quote 0, reply 1, retweet 0

> With every loop, totalAssets increase exponentially following the function 2^(iteration count + 1). See below to visualize it. With only 75 loops, it increases to more than 10k ether. [pic.x.com/dhm5ylCdd8]

**Media:**
- photo: https://pbs.twimg.com/media/GJSrlHjacAAfqO1.png — no alt text provided by author


### Thread part 12 — @kankodu — 2024-03-22 17:35 UTC (2024-03-22 18:35 WAT)

- URL: https://x.com/kankodu/status/1771229214978765011
- Metrics (at fetch): bookmark 1, impression 3017, like 6, quote 0, reply 1, retweet 0

> Using this, the attacker can inflate the price of a share even if total assets are being tracked internally.
>
> Now, how to achieve the initial condition mentioned earlier?


### Thread part 13 — @kankodu — 2024-03-22 17:35 UTC (2024-03-22 18:35 WAT)

- URL: https://x.com/kankodu/status/1771229218606837979
- Metrics (at fetch): bookmark 1, impression 2770, like 7, quote 1, reply 1, retweet 0

> Let's say we want to achieve the initial condition of totalSupply = 1 and totalAssets = 2 for a lending protocol. When totalSupply is zero, we can take the below steps.


### Thread part 14 — @kankodu — 2024-03-22 17:35 UTC (2024-03-22 18:35 WAT)

- URL: https://x.com/kankodu/status/1771229222163697878
- Metrics (at fetch): bookmark 1, impression 2838, like 6, quote 0, reply 3, retweet 0

> Deposit some assets and borrow those assets by putting up some collateral. At this point, there will be no rounding error because totalSupply would be equal to totalAssets. After a block passes when at least 1 wei has been accumulated, rounding errors would be introduced.


### Thread part 15 — @kankodu — 2024-03-22 17:35 UTC (2024-03-22 18:35 WAT)

- URL: https://x.com/kankodu/status/1771229225879761204
- Metrics (at fetch): bookmark 0, impression 2682, like 4, quote 0, reply 1, retweet 0

> Now, if you repay all of the assets and redeem all but 1 wei of shares, the totalSupply will be 1 and totalAssets = 2.


### Thread part 16 — @kankodu — 2024-03-22 17:35 UTC (2024-03-22 18:35 WAT)

- URL: https://x.com/kankodu/status/1771229229210038637
- Metrics (at fetch): bookmark 1, impression 2696, like 7, quote 0, reply 1, retweet 0

> It's because when some interest has accrued, totalAssets would be greater than totalSupply, and when the protocol calculates how many assets to return to the user, it will undercalculate by 1 wei due to a rounding error.


### Thread part 17 — @kankodu — 2024-03-22 17:35 UTC (2024-03-22 18:35 WAT)

- URL: https://x.com/kankodu/status/1771229232649367965
- Metrics (at fetch): bookmark 5, impression 3202, like 7, quote 0, reply 1, retweet 0

> assetsToBeWithdrawn = (shares * totalAssets) / totalSupply = (totalSupply -1 ) * totalAssets / totalSupply.


### Thread part 18 — @kankodu — 2024-03-22 17:35 UTC (2024-03-22 18:35 WAT)

- URL: https://x.com/kankodu/status/1771229235891564726
- Metrics (at fetch): bookmark 2, impression 1974, like 4, quote 0, reply 1, retweet 0

> As totalAssets is greater than totalSupply, the numerator would be just a few weis less than the (totalAsset - 1) multiple of totalSupply, and that means due to rounding down, the answer would be (totalAssets - 2), leaving 2 wei of totalAssets and 1 wei of totalSupply.


### Thread part 19 — @kankodu — 2024-03-22 17:35 UTC (2024-03-22 18:35 WAT)

- URL: https://x.com/kankodu/status/1771229239402197187
- Metrics (at fetch): bookmark 9, impression 3781, like 8, quote 0, reply 1, retweet 0

> This is how the initial condition can be achieved to carry out the inflation of share price. Such inflation opens up various attack vectors, particularly in lending protocols. See how it was done in wise lending here: https://twitter.com/danielvf/status/1746303616778981402

**Links in post:** https://twitter.com/danielvf/status/1746303616778981402

**Quoted post (full text):**

    #### Quoted post — @5678 — 2024-01-13 22:50 UTC (2024-01-13 23:50 WAT)
    
    - URL: https://x.com/5678/status/1746303616778981402
    - Metrics (at fetch): bookmark 583, impression 109809, like 607, quote 24, reply 22, retweet 103
    
    > Yesterday's complete hack of Wise Lending was far more complex than reported. Very worth examining.
    >
    > The protocol had added explicit defenses against this style of attack, which the attack then either bypassed or used against the protocol.    🧵 1/21 [pic.x.com/n8mtQGVcvP]
    
    **Media:**
    - media `3_1746303300801003521` (details not returned by the API)
    


### Thread part 20 — @kankodu — 2024-03-22 17:35 UTC (2024-03-22 18:35 WAT)

- URL: https://x.com/kankodu/status/1771229243189653884
- Metrics (at fetch): bookmark 19, impression 3316, like 20, quote 0, reply 0, retweet 0

> There are some protocols that use shares calculation for calculating interest owed from the user. By exploiting the rounding being done in protocol's favor in similar manner, see how the hacker was able to get away with $6M dollars from MIM protocol. https://twitter.com/kankodu/status/1752581744803680680

**Links in post:** https://twitter.com/kankodu/status/1752581744803680680

**Quoted post (full text):**

    #### Quoted post — @kankodu — 2024-01-31 06:37 UTC (2024-01-31 07:37 WAT)
    
    - URL: https://x.com/kankodu/status/1752581744803680680
    - Metrics (at fetch): bookmark 412, impression 77833, like 462, quote 12, reply 13, retweet 92
    
    > A 🧵 on how yesterday's @MIM_Spell attack worked. The protocol did everything right. They rounded in the protocol's favour whenever they should but one additional function, meant to only reduce the user's funds, ended up enabling the attack. How? [pic.x.com/61bHWJlhZT]
    
    **Media:**
    - photo: https://pbs.twimg.com/media/GFJrzsnbkAAaBMy.png — no alt text provided by author
    


---

## 2024-03-09 · Post · Two of the bug patterns that I discovered got a mention in this. Feeling grateful to be included in 


### Post — @kankodu — 2024-03-09 12:13 UTC (2024-03-09 13:13 WAT)

- URL: https://x.com/kankodu/status/1766437092169597070
- Metrics (at fetch): bookmark 20, impression 5032, like 57, quote 0, reply 0, retweet 1

> Two of the bug patterns that I discovered got a mention in this. Feeling grateful to be included in the list, even if it's at the very end of it. https://t.co/LugP8WUjQq

**Quoted post (full text):**

    #### Quoted post — @765981595383857152 — 2024-03-08 14:32 UTC (2024-03-08 15:32 WAT)
    
    - URL: https://x.com/765981595383857152/status/1766109683402592509
    - Metrics (at fetch): bookmark 184, impression 54690, like 192, quote 9, reply 3, retweet 74
    
    > The Top 10 Blockchain Hacking Techniques 2nd Edition is out.
    >
    > The industry’s compilation of the 10 most novel, interesting, and unexpected smart contract hacks and bugs. 
    >
    > From the governance hack of Tornado Cash using metamorphic contracts, to the billion-dollar exploit https://t.co/FPzoiKK20G
    
    **Media:**
    - media `3_1766109677832564736` (details not returned by the API)
    


---

## 2024-01-31 · Thread · A 🧵 on how yesterday's @MIM_Spell attack worked. The protocol did everything right. They rounded in 


### Post — @kankodu — 2024-01-31 06:37 UTC (2024-01-31 07:37 WAT)

- URL: https://x.com/kankodu/status/1752581744803680680
- Metrics (at fetch): bookmark 412, impression 77833, like 462, quote 12, reply 13, retweet 92

> A 🧵 on how yesterday's @MIM_Spell attack worked. The protocol did everything right. They rounded in the protocol's favour whenever they should but one additional function, meant to only reduce the user's funds, ended up enabling the attack. How? [pic.x.com/61bHWJlhZT]

**Media:**
- photo: https://pbs.twimg.com/media/GFJrzsnbkAAaBMy.png — no alt text provided by author


### Thread part 2 — @kankodu — 2024-01-31 06:37 UTC (2024-01-31 07:37 WAT)

- URL: https://x.com/kankodu/status/1752581748758815030
- Metrics (at fetch): bookmark 1, impression 6917, like 9, quote 0, reply 1, retweet 0

> The protocol used shares mechanism to calculate the current debt of a user. Note: In the codebase, borrow shares are referred to as base/part and borrow assets amounts are referred to as elastic/amount.


### Thread part 3 — @kankodu — 2024-01-31 06:37 UTC (2024-01-31 07:37 WAT)

- URL: https://x.com/kankodu/status/1752581752206557683
- Metrics (at fetch): bookmark 1, impression 6402, like 8, quote 0, reply 1, retweet 0

> When a user borrows certain funds, they get minted borrow shares based on the current totalBorrowAssets and totalBorrowShares ratio.  As interest is owed from the user, totalBorrowAssets increases without totalBorrowShares increasing and in turn it increases...


### Thread part 4 — @kankodu — 2024-01-31 06:37 UTC (2024-01-31 07:37 WAT)

- URL: https://x.com/kankodu/status/1752581755415281835
- Metrics (at fetch): bookmark 1, impression 6011, like 9, quote 0, reply 1, retweet 0

> ...the proportional amount that the user has to repay as well.  The culprit function was the repayForAll function. This allowed anyone to repay everyone's debt.  To accomplish this, the protocol reduced totalBorrowAssets without totalBorrowShares in repayForAll function.


### Thread part 5 — @kankodu — 2024-01-31 06:37 UTC (2024-01-31 07:37 WAT)

- URL: https://x.com/kankodu/status/1752581764021948430
- Metrics (at fetch): bookmark 1, impression 5761, like 9, quote 0, reply 1, retweet 1

> The attacker borrowed funds using a fllashloan and use the repayForAll function first. [pic.x.com/425c7Q8IX4]

**Media:**
- photo: https://pbs.twimg.com/media/GFJr0z3awAAAruT.jpg — no alt text provided by author


### Thread part 6 — @kankodu — 2024-01-31 06:37 UTC (2024-01-31 07:37 WAT)

- URL: https://x.com/kankodu/status/1752581768383955446
- Metrics (at fetch): bookmark 1, impression 5862, like 9, quote 0, reply 1, retweet 0

> The attacker couldn't repay all of the amount as there was a check that totalBorrowAssets needed to be greater than 1000 ether.  Regardless, the attacker repaid as much as they could, which reduced totalBorrowAssets such that totalBorrowAssets:totalBorrowShares was ~ 1:26.


### Thread part 7 — @kankodu — 2024-01-31 06:37 UTC (2024-01-31 07:37 WAT)

- URL: https://x.com/kankodu/status/1752581778140012657
- Metrics (at fetch): bookmark 1, impression 4769, like 6, quote 0, reply 2, retweet 0

> Now, the attacker repaid all the existing loans for all the borrowers.
>
> For the last remaining borrower, the user repaid all but 100 wei of shares.
>
> At that point, totalBorrowedAssets were 100, and totalBorrowShares were 3. [pic.x.com/iqofiUwkVd]

**Media:**
- photo: https://pbs.twimg.com/media/GFJr1kaasAEn6PL.jpg — no alt text provided by author


### Thread part 8 — @kankodu — 2024-01-31 06:37 UTC (2024-01-31 07:37 WAT)

- URL: https://x.com/kankodu/status/1752581782393045255
- Metrics (at fetch): bookmark 2, impression 4442, like 8, quote 0, reply 3, retweet 0

> The attacker repaid 1 wei of share 3 times, which meant totalAssets reduced to 0, and totalBorrowShares were 97. Now the attacker started borrowing 1 wei from their account.  At this point, TotalBorrowAssets is 1, and totalBorrowShares is 98.


### Thread part 9 — @kankodu — 2024-01-31 06:37 UTC (2024-01-31 07:37 WAT)

- URL: https://x.com/kankodu/status/1752581791402373577
- Metrics (at fetch): bookmark 0, impression 4327, like 9, quote 0, reply 1, retweet 0

> Attacker put up a very low amount of collateral (100 wei) and in a loop, started borrowing 1 wei of assets and repaying 1 wei of borrow shares. [pic.x.com/JG25bDpHlT]

**Media:**
- photo: https://pbs.twimg.com/media/GFJr2WAbMAA6JkN.jpg — no alt text provided by author


### Thread part 10 — @kankodu — 2024-01-31 06:37 UTC (2024-01-31 07:37 WAT)

- URL: https://x.com/kankodu/status/1752581795948957948
- Metrics (at fetch): bookmark 0, impression 3988, like 9, quote 0, reply 1, retweet 0

> Since totalBorrowShares are greater than totalBorrowAssets, borrowing 1 wei of assets minted a lot of borrow shares.


### Thread part 11 — @kankodu — 2024-01-31 06:37 UTC (2024-01-31 07:37 WAT)

- URL: https://x.com/kankodu/status/1752581799090512125
- Metrics (at fetch): bookmark 0, impression 3946, like 8, quote 0, reply 1, retweet 0

> However, since the protocol rounds up in its favour, when the attacker repaid 1 wei of borrow share, even though it is worth near 0, the protocol makes the attacker repay 1 wei of assets.


### Thread part 12 — @kankodu — 2024-01-31 06:37 UTC (2024-01-31 07:37 WAT)

- URL: https://x.com/kankodu/status/1752581802324263305
- Metrics (at fetch): bookmark 0, impression 3871, like 9, quote 0, reply 1, retweet 0

> So at the end of this loop, totalBorrowAssets stays at 1, but totalBorrowShares increase exponentially.
>
> The attacker made totalBorrowShares go up to infinity while keeping totalBorrowAssets at 1.


### Thread part 13 — @kankodu — 2024-01-31 06:37 UTC (2024-01-31 07:37 WAT)

- URL: https://x.com/kankodu/status/1752581805646229675
- Metrics (at fetch): bookmark 1, impression 3774, like 9, quote 0, reply 1, retweet 0

> Now, they repaid 1 wei of share to make the totalBorrowAssets go to zero, and totalBorrowShares are still at infinity. Now, the attacker borrowed all of the funds in the protocol for collateral worth almost nothing using another account, and the protocol let it.


### Thread part 14 — @kankodu — 2024-01-31 06:37 UTC (2024-01-31 07:37 WAT)

- URL: https://x.com/kankodu/status/1752581812608770182
- Metrics (at fetch): bookmark 1, impression 3910, like 12, quote 0, reply 1, retweet 0

> Why?
>
> The attacker borrowed all of their funds, but the borrow shares that they got minted were at the ratio of 1:1. [pic.x.com/ajphmFzU7Q]

**Media:**
- photo: https://pbs.twimg.com/media/GFJr3slaoAAY7s9.jpg — no alt text provided by author


### Thread part 15 — @kankodu — 2024-01-31 06:37 UTC (2024-01-31 07:37 WAT)

- URL: https://x.com/kankodu/status/1752581816169754735
- Metrics (at fetch): bookmark 0, impression 3709, like 5, quote 0, reply 1, retweet 0

> Because in the borrow function when assets get converted in borrow shares, if totalBorrowAssets are zero, borrow shares minted are equal to the asset amount.  So, the attacker borrowed a finite amount (all of the available borrowable amount), and they got finite borrow shares.


### Thread part 16 — @kankodu — 2024-01-31 06:37 UTC (2024-01-31 07:37 WAT)

- URL: https://x.com/kankodu/status/1752581819445469535
- Metrics (at fetch): bookmark 0, impression 3758, like 9, quote 0, reply 1, retweet 0

> Remember, at this point, totalBorrowShares are still infinite.  So when the protocol checks the health of this attacker account, they convert borrow shares into borrow amount to see how much they have borrowed.


### Thread part 17 — @kankodu — 2024-01-31 06:37 UTC (2024-01-31 07:37 WAT)

- URL: https://x.com/kankodu/status/1752581822662553793
- Metrics (at fetch): bookmark 0, impression 4365, like 10, quote 0, reply 1, retweet 0

> This comes out to almost nothing as the shares that this attacker account has are nothing compared to shares that the other attacker account has.  The protocol thinks that the other account, which has infinite borrow shares, has borrowed almost all the funds and not this account.


### Thread part 18 — @kankodu — 2024-01-31 06:37 UTC (2024-01-31 07:37 WAT)

- URL: https://x.com/kankodu/status/1752581825837625617
- Metrics (at fetch): bookmark 19, impression 7057, like 51, quote 2, reply 1, retweet 1

> And the health check passes.
>
> Fix: For lending protocols that use shares calculation to calculate owed interest, make sure there is no way to reduce totalBorrowShares less than totalBorrowAssets.


---

## 2024-01-14 · Post · Usually, there are three recommended ways to prevent the vault inflation attack:


### Post — @kankodu — 2024-01-14 07:50 UTC (2024-01-14 08:50 WAT)

- URL: https://x.com/kankodu/status/1746439595053789217
- Metrics (at fetch): bookmark 27, impression 3779, like 30, quote 0, reply 2, retweet 2

> Usually, there are three recommended ways to prevent the vault inflation attack:
> 1. Internal Balance accounting
> 2. Maintain some minimum total supply
> 3. Virtual shares calculation
>
> We now know the first one doesn't work https://t.co/9k2AZUXQKR

**Quoted post (full text):**

    #### Quoted post — @5678 — 2024-01-13 22:50 UTC (2024-01-13 23:50 WAT)
    
    - URL: https://x.com/5678/status/1746303616778981402
    - Metrics (at fetch): bookmark 583, impression 109809, like 607, quote 24, reply 22, retweet 103
    
    > Yesterday's complete hack of Wise Lending was far more complex than reported. Very worth examining.
    >
    > The protocol had added explicit defenses against this style of attack, which the attack then either bypassed or used against the protocol.    🧵 1/21 [pic.x.com/n8mtQGVcvP]
    
    **Media:**
    - media `3_1746303300801003521` (details not returned by the API)
    


---

## 2023-12-13 · Post · it was a gud year on @immunefi 


Tags (automatic): Platform: Immunefi


### Post — @kankodu — 2023-12-13 15:45 UTC (2023-12-13 16:45 WAT)

- URL: https://x.com/kankodu/status/1734962657248350432
- Metrics (at fetch): bookmark 10, impression 12228, like 145, quote 3, reply 5, retweet 10

> it was a gud year on @immunefi 
> #ImmunefiWrapped https://t.co/1N4zwnPSoz

**Media:**
- photo: https://pbs.twimg.com/media/GBPSdnkacAA7RDT.jpg — alt text: "Kankodu ImmuneFi Wrapped"


---

## 2023-09-05 · Thread · How I Unknowingly Caused the $200M Euler Hack 🧵👇


Tags (automatic): Smart contract / DeFi


### Post — @kankodu — 2023-09-05 09:33 UTC (2023-09-05 10:33 WAT)

- URL: https://x.com/kankodu/status/1698992717089604064
- Metrics (at fetch): bookmark 240, impression 126137, like 418, quote 18, reply 18, retweet 78

> How I Unknowingly Caused the $200M Euler Hack 🧵👇
>
> TL;DR: The fix for a bug that I reported ended up introducing a function responsible for the hack! https://t.co/qpNlGbVt7H

**Media:**
- photo: https://pbs.twimg.com/media/F5QI3wRb0AAltZL.png — no alt text provided by author


### Thread part 2 — @kankodu — 2023-09-05 09:33 UTC (2023-09-05 10:33 WAT)

- URL: https://x.com/kankodu/status/1698992720637997305
- Metrics (at fetch): bookmark 0, impression 6361, like 10, quote 1, reply 1, retweet 0

> In July '22, I reported the 'first deposit bug' in Euler, a permissionless lending protocol. Lenders deposit `x` underlying tokens and get `x / exchange rate` ETokens. The exchange rate is calculated as the current underlying balance divided by the total EToken supply.


### Thread part 3 — @kankodu — 2023-09-05 09:33 UTC (2023-09-05 10:33 WAT)

- URL: https://x.com/kankodu/status/1698992723209171356
- Metrics (at fetch): bookmark 0, impression 6169, like 12, quote 0, reply 1, retweet 0

> An attacker can exploit this system by minting 1 wei of ETokens, then sending `x` tokens to artificially inflate the exchange rate. This causes the first lender to get (x/x+1 =) 0 ETokens due to rounding, allowing the attacker to withdraw all tokens.


### Thread part 4 — @kankodu — 2023-09-05 09:33 UTC (2023-09-05 10:33 WAT)

- URL: https://x.com/kankodu/status/1698992725797028064
- Metrics (at fetch): bookmark 1, impression 5906, like 14, quote 0, reply 1, retweet 1

> Euler paid me $50k for submitting this bug. Here's the fix that they went with:
> In Euler, reserves (fees that governance collects) are denominated in ETokens. The protocol was modified so that all new ETokens are initialised with a total supply and reserve of 1 million wei.


### Thread part 5 — @kankodu — 2023-09-05 09:33 UTC (2023-09-05 10:33 WAT)

- URL: https://x.com/kankodu/status/1698992732998619464
- Metrics (at fetch): bookmark 0, impression 5686, like 14, quote 2, reply 1, retweet 1

> This results in first lender contributing a minor amount of tokens to reserves. This fix is effective as long as there is a check to make sure governance can't withdraw the last 1 million wei. The solution mirrors Uniswap V2's approach, making the attack economically infeasible. https://t.co/fBTV9NgkmC

**Media:**
- photo: https://pbs.twimg.com/media/F5QI4lCbAAAPYra.jpg — no alt text provided by author


### Thread part 6 — @kankodu — 2023-09-05 09:33 UTC (2023-09-05 10:33 WAT)

- URL: https://x.com/kankodu/status/1698992736152715320
- Metrics (at fetch): bookmark 1, impression 5222, like 8, quote 0, reply 1, retweet 0

> The fix is effective for future ETokens. For existing ones, two scenarios exist.
> Case I: For tokens with reserves greater than 1 million wei already, no extra steps are needed. Governance can't access the last 1 million wei, ensuring the total supply remains above zero.


### Thread part 7 — @kankodu — 2023-09-05 09:33 UTC (2023-09-05 10:33 WAT)

- URL: https://x.com/kankodu/status/1698992738770035170
- Metrics (at fetch): bookmark 1, impression 8719, like 11, quote 1, reply 1, retweet 0

> The $200M hack exploited a function meant to address the second case: existing ETokens with reserves under 1 million wei. A `donateToReserves` function was added and audited, and the team used it to increase reserves above 1 million wei for such ETokens.


### Thread part 8 — @kankodu — 2023-09-05 09:33 UTC (2023-09-05 10:33 WAT)

- URL: https://x.com/kankodu/status/1698992741617996114
- Metrics (at fetch): bookmark 18, impression 6220, like 22, quote 0, reply 1, retweet 4

> The patch fixed the first deposit bug for all ETokens but inadvertently enabled a larger $200M hack. Watch this video by @Jun1on to see how the attacker exploited the `donateToReserves` function and Euler's unique liquidation mechanism to commit the theft.
> https://t.co/5J469M6hCe


### Thread part 9 — @kankodu — 2023-09-05 09:33 UTC (2023-09-05 10:33 WAT)

- URL: https://x.com/kankodu/status/1698992744298119281
- Metrics (at fetch): bookmark 1, impression 5304, like 21, quote 0, reply 1, retweet 2

> An innocent-looking function, designed only to reduce a user's funds, ended up compromising the entire protocol. This serves as an expensive lesson to treat even small bug fixes with the same level of importance as major updates like v2.


---

## 2023-07-29 · Post · For this bug to be exploitable, many things needed to come together: a yield-generating vault share 


### Post — @kankodu — 2023-07-29 16:06 UTC (2023-07-29 17:06 WAT)

- URL: https://x.com/kankodu/status/1685320793025294338
- Metrics (at fetch): bookmark 0, impression 2833, like 8, quote 0, reply 2, retweet 0

> For this bug to be exploitable, many things needed to come together: a yield-generating vault share token that is accepted as collateral in a protocol offering flash loan functionality, with the attacker having control over all the vault share tokens outside of the protocol.


---

## 2023-07-29 · Post · Interestingly, I discovered that @daejunpark had already brought up a similar attack issue in OpenZe


### Post — @kankodu — 2023-07-29 16:06 UTC (2023-07-29 17:06 WAT)

- URL: https://x.com/kankodu/status/1685320790127026176
- Metrics (at fetch): bookmark 9, impression 2300, like 10, quote 0, reply 2, retweet 0

> Interestingly, I discovered that @daejunpark had already brought up a similar attack issue in OpenZeppelin's ERC4626 implementation: https://t.co/x1JYR7LISy.
>
> It would be intriguing to learn their thought process for arriving at this bug pattern.


---

## 2023-07-29 · Post · The AAVE team rewarded $20k for responsible disclosure.


### Post — @kankodu — 2023-07-29 16:06 UTC (2023-07-29 17:06 WAT)

- URL: https://x.com/kankodu/status/1685320787384037376
- Metrics (at fetch): bookmark 3, impression 1928, like 12, quote 0, reply 1, retweet 1

> The AAVE team rewarded $20k for responsible disclosure.
>
> You can check out the details here: https://t.co/QeedgCU2Ks
>
> Check out the original bug report here: https://t.co/Zc7GO9ssVR.


---

## 2023-07-29 · Post · However, by resetting the share price, an attacker can recover the donated tokens. After significant


### Post — @kankodu — 2023-07-29 16:06 UTC (2023-07-29 17:06 WAT)

- URL: https://x.com/kankodu/status/1685320784758325248
- Metrics (at fetch): bookmark 0, impression 1971, like 6, quote 0, reply 1, retweet 0

> However, by resetting the share price, an attacker can recover the donated tokens. After significant research, I found AAVE V2 accepted GUniUSDCUSDT as collateral, susceptible to such manipulation. The funds at risk amounted to $2.83M, but the exploit likelihood was low.


---

## 2023-07-29 · Post · Donating underlying tokens to the vault address can inflate the price, but nobody would do that beca


### Post — @kankodu — 2023-07-29 16:06 UTC (2023-07-29 17:06 WAT)

- URL: https://x.com/kankodu/status/1685320782103384064
- Metrics (at fetch): bookmark 0, impression 1968, like 6, quote 0, reply 1, retweet 0

> Donating underlying tokens to the vault address can inflate the price, but nobody would do that because the donated tokens are automatically distributed among the vault share token holders, and the attacker never gets them back.


---

## 2023-07-29 · Post · Usually, this type of vault share token price is calculated on-chain with the underlying token price


Tags (automatic): Blockchain / L1-L2 / bridge


### Post — @kankodu — 2023-07-29 16:06 UTC (2023-07-29 17:06 WAT)

- URL: https://x.com/kankodu/status/1685320779574190080
- Metrics (at fetch): bookmark 0, impression 1998, like 5, quote 0, reply 1, retweet 0

> Usually, this type of vault share token price is calculated on-chain with the underlying token price sourced from off-chain oracles.


---

## 2023-07-29 · Post · I assumed that this was as far as this bug pattern would go. I was wrong, yet again. I started ponde


### Post — @kankodu — 2023-07-29 16:05 UTC (2023-07-29 17:05 WAT)

- URL: https://x.com/kankodu/status/1685320776822427648
- Metrics (at fetch): bookmark 0, impression 2055, like 6, quote 0, reply 1, retweet 0

> I assumed that this was as far as this bug pattern would go. I was wrong, yet again. I started pondering what would happen if such vault tokens were accepted as collateral.


---

## 2023-07-29 · Post · This wasn't a bug in the Balancer's flashloan functionality since they couldn't account for this in 


### Post — @kankodu — 2023-07-29 16:05 UTC (2023-07-29 17:05 WAT)

- URL: https://x.com/kankodu/status/1685320774054518784
- Metrics (at fetch): bookmark 0, impression 2112, like 7, quote 0, reply 1, retweet 0

> This wasn't a bug in the Balancer's flashloan functionality since they couldn't account for this in their code. Balancer conducted an exhaustive search and found five other vulnerable tokens with around $10k at risk. They kindly rewarded me with $1k for finding it.


---

## 2023-07-29 · Post · I realised that numerous other tokens within the https://t.co/72MwK3Xhl3 ecosystem were at risk. Ins


### Post — @kankodu — 2023-07-29 16:05 UTC (2023-07-29 17:05 WAT)

- URL: https://x.com/kankodu/status/1685320771353366528
- Metrics (at fetch): bookmark 3, impression 2204, like 8, quote 0, reply 1, retweet 0

> I realised that numerous other tokens within the https://t.co/72MwK3Xhl3 ecosystem were at risk. Instead of reporting each individually, I submitted the pattern to Balancer, requesting them to address it.


---

## 2023-07-29 · Post · I decided to submit anyway, and the team agreed to pay me a minimum of what a critical bug is reward


### Post — @kankodu — 2023-07-29 16:05 UTC (2023-07-29 17:05 WAT)

- URL: https://x.com/kankodu/status/1685320768392163328
- Metrics (at fetch): bookmark 0, impression 2378, like 9, quote 0, reply 1, retweet 0

> I decided to submit anyway, and the team agreed to pay me a minimum of what a critical bug is rewarded, $12.5k. https://t.co/cpWpSHmXTe

**Media:**
- animated_gif:  — no alt text provided by author


---

## 2023-07-29 · Thread · A bug that was supposed to be only a good thought experiment inadvertently ended up making me $33.5k


Tags (automatic): Blockchain / L1-L2 / bridge, Platform: Immunefi


### Post — @kankodu — 2023-07-29 16:05 UTC (2023-07-29 17:05 WAT)

- URL: https://x.com/kankodu/status/1685320718870032384
- Metrics (at fetch): bookmark 320, impression 43492, like 325, quote 9, reply 7, repost 66

> A bug that was supposed to be only a good thought experiment inadvertently ended up making me $33.5k.
> Here are the details 🧵:


### Thread part 2 — @kankodu — 2023-07-29 16:05 UTC (2023-07-29 17:05 WAT)

- URL: https://x.com/kankodu/status/1685320727464206336
- Metrics (at fetch): bookmark 3, impression 4354, like 21, quote 0, reply 2, retweet 1

> Consider an ERC4626-like vault. When its total supply is zero, the vault's share-to-underlying token ratio is 1:1. As the vault generates yield, the value of a share increases. https://t.co/eEns5ZGAeZ

**Media:**
- photo: https://pbs.twimg.com/media/F2N2RINbwAA8Q9N.jpg — no alt text provided by author


### Thread part 3 — @kankodu — 2023-07-29 16:05 UTC (2023-07-29 17:05 WAT)

- URL: https://x.com/kankodu/status/1685320730521538560
- Metrics (at fetch): bookmark 0, impression 4231, like 7, quote 0, reply 1, retweet 0

> Let's contemplate what would transpire if all vault share tokens were in a protocol that offers flash loans. Flashloan providers don't care what you do with the tokens as long as you return the same amount of tokens at the end of the transaction.


### Thread part 4 — @kankodu — 2023-07-29 16:05 UTC (2023-07-29 17:05 WAT)

- URL: https://x.com/kankodu/status/1685320733315256320
- Metrics (at fetch): bookmark 0, impression 3698, like 8, quote 0, reply 1, retweet 0

> If an attacker flash loans all the vault share tokens, withdraws them for underlying tokens, and then mints them again to repay the flash loan, they stand to profit. How?!


### Thread part 5 — @kankodu — 2023-07-29 16:05 UTC (2023-07-29 17:05 WAT)

- URL: https://x.com/kankodu/status/1685320735978590210
- Metrics (at fetch): bookmark 0, impression 3337, like 7, quote 0, reply 1, retweet 0

> Suppose the current vault share to underlying token ratio is 2:3. When the attacker burns all of the vault share tokens for the underlying tokens, the total supply, as per the ERC4626 vault, is now zero. That means the ratio is now reset to 1:1.


### Thread part 6 — @kankodu — 2023-07-29 16:05 UTC (2023-07-29 17:05 WAT)

- URL: https://x.com/kankodu/status/1685320745898102784
- Metrics (at fetch): bookmark 0, impression 3733, like 7, quote 1, reply 1, retweet 0

> When the attacker mints share tokens to repay the flashloan, they have to spend fewer underlying tokens to mint the same amount of share tokens. This results in the attacker profiting (current share price - 1) * total underlying balance`. https://t.co/UEbkXGeTud

**Media:**
- photo: https://pbs.twimg.com/media/F2N2SDca4AAl8L0.jpg — no alt text provided by author


### Thread part 7 — @kankodu — 2023-07-29 16:05 UTC (2023-07-29 17:05 WAT)

- URL: https://x.com/kankodu/status/1685320749249429504
- Metrics (at fetch): bookmark 0, impression 2639, like 7, quote 0, reply 1, retweet 0

> I thought of this pattern a while ago. I thought, "Yeah, it's a good thought experiment and maybe I will design a CTF around it," but there were too many conditions that need to come together to make the bug exploitable in practice. I was wrong.


### Thread part 8 — @kankodu — 2023-07-29 16:05 UTC (2023-07-29 17:05 WAT)

- URL: https://x.com/kankodu/status/1685320751879241729
- Metrics (at fetch): bookmark 0, impression 2522, like 5, quote 0, reply 1, retweet 0

> In the end of March, I decided to take a look on-chain. I focused on Balancer as it is a singleton contract that has flashloan functionality and, unlike Uniswap, it has pools that support selling yield-generating tokens efficiently.


### Thread part 9 — @kankodu — 2023-07-29 16:05 UTC (2023-07-29 17:05 WAT)

- URL: https://x.com/kankodu/status/1685320754521600000
- Metrics (at fetch): bookmark 0, impression 2476, like 7, quote 0, reply 1, retweet 0

> By merely exploring Etherscan without any automation, I discovered a token with 100% of its total supply in Balancer. A quick POC ensured that the attack functioned as expected. It was in https://t.co/YXNMpZav14's v2, not covered by their ImmuneFi bug bounty program at that time.


---

## 2023-07-04 · Post · Some bugs exist for which you cannot attach a specific number and say, "this is how much would have 


### Post — @kankodu — 2023-07-04 15:48 UTC (2023-07-04 16:48 WAT)

- URL: https://x.com/kankodu/status/1676256606110224384
- Metrics (at fetch): not returned

> Some bugs exist for which you cannot attach a specific number and say, "this is how much would have been at risk."
>
> Here's what I wish I had known before the discussion about such a bug concluded, with the project paying me approximately $300k.
>
> A short thread 🧵:


---

## 2023-06-16 · Post · On April 28th, I discovered a bug in Silo Finance's codebase. It was swiftly rectified, with the pro


### Post — @kankodu — 2023-06-16 22:26 UTC (2023-06-16 23:26 WAT)

- URL: https://x.com/kankodu/status/1669833829203476480
- Metrics (at fetch): not returned

> On April 28th, I discovered a bug in Silo Finance's codebase. It was swiftly rectified, with the project awarding me $100k. Here's a detailed thread on the thought process that led to the bug's discovery.
>
> A long thread 🧵:


---

## 2023-04-19 · Post · Be me


### Post — @kankodu — 2023-04-19 15:55 UTC (2023-04-19 16:55 WAT)

- URL: https://x.com/kankodu/status/1648716908529848321
- Metrics (at fetch): not returned

> Be me
> &gt; Find a critical at the start of every month in 2023
> &gt; Jan - 20k payout 
> &gt; Feb - 35k + 5k
> &gt; March - Biggest bug bounty I’ve ever received
> &gt; April - 12k + ??
>
> Profit ???


---

## 2023-04-16 · Post · To all the Compound forks, send 1000 Wei of cTokens to a dead address to make this attack economical


### Post — @kankodu — 2023-04-16 01:17 UTC (2023-04-16 02:17 WAT)

- URL: https://x.com/kankodu/status/1647408860569780225
- Metrics (at fetch): not returned

> To all the Compound forks, send 1000 Wei of cTokens to a dead address to make this attack economically infeasible. https://t.co/uMksaS9KQ8

**Links in post:** https://t.co/uMksaS9KQ8

**Quoted post** 1647401085412446209: not readable via the API (deleted, private, or withheld).


---

## 2023-02-03 · Post · This is a really good tip! 


Tags (automatic): Smart contract / DeFi


### Post — @kankodu — 2023-02-03 06:38 UTC (2023-02-03 07:38 WAT)

- URL: https://x.com/kankodu/status/1621397698124423168
- Metrics (at fetch): not returned

> This is a really good tip! 
> One more advantage of thinking in bug classes is that they are universal. I don't have expertise outside of Solidity, yet I've reported bugs in Vyper, Rust, and more recently in Move smart contracts while searching for a specific bug pattern. https://twitter.com/TrustSecAudits/status/1618186163235475458

**Links in post:** https://twitter.com/TrustSecAudits/status/1618186163235475458

**Quoted post (full text):**

    #### Quoted post — @TrustSecAudits — 2023-01-25 09:57 UTC (2023-01-25 10:57 WAT)
    
    - URL: https://x.com/TrustSecAudits/status/1618186163235475458
    - Metrics (at fetch): not returned
    
    > (1/3)
    > auditing alpha tip #2:
    > Don't think bugs, think bug classes
    >
    > Bugs aren't interesting. They are the result of a very specific mutation in a particular codebase which in all likelihood will not repeat in that exact way. [pic.x.com/leHIsIllu9]
    
    **Media:**
    - media `3_1618185511985725440` (details not returned by the API)
    


---

## 2023-01-11 · Post · Watch as I strive to maintain my position among the top 20 @immunefi  whitehat hackers on the leader


Tags (automatic): Platform: Immunefi


### Post — @kankodu — 2023-01-11 10:02 UTC (2023-01-11 11:02 WAT)

- URL: https://x.com/kankodu/status/1613114006868205569
- Metrics (at fetch): not returned

> Watch as I strive to maintain my position among the top 20 @immunefi  whitehat hackers on the leaderboard in this live footage! [pic.x.com/zQdc87qHu9]

**Media:**
- animated_gif:  — no alt text provided by author


---

## 2023-01-01 · Post · 2022: The journey from reporting my first bug on @immunefi to being ranked 19 on the WhiteHat leade


Tags (automatic): Platform: Immunefi


### Post — @kankodu — 2023-01-01 04:33 UTC (2023-01-01 05:33 WAT)

- URL: https://x.com/kankodu/status/1609407360602378241
- Metrics (at fetch): not returned

> 2022: The journey from reporting my first bug on @immunefi to being ranked #19 on the WhiteHat leaderboard was very exciting! 
> Feeling very grateful 😇


---

## 2022-11-22 · Post · In top 3 for @golom_io 's @code4rena audit !!


Tags (automatic): Platform: Code4rena / Sherlock / Cantina


### Post — @kankodu — 2022-11-22 08:03 UTC (2022-11-22 09:03 WAT)

- URL: https://x.com/kankodu/status/1594964780108124160
- Metrics (at fetch): not returned

> In top 3 for @golom_io 's @code4rena audit !!
> Full report coming soon ... [pic.x.com/w5D7DUZhoA]

**Media:**
- photo: https://pbs.twimg.com/media/FiJzegzaAAE6SdF.png — no alt text provided by author


---

## 2022-11-05 · Post · 19. Nice! Wen Immunefi merch? https://twitter.com/immunefi/status/1588489884939223042


Tags (automatic): Platform: Immunefi


### Post — @kankodu — 2022-11-05 03:10 UTC (2022-11-05 04:10 WAT)

- URL: https://x.com/kankodu/status/1588730413832634373
- Metrics (at fetch): not returned

> #19. Nice! Wen Immunefi merch? https://twitter.com/immunefi/status/1588489884939223042

**Links in post:** https://twitter.com/immunefi/status/1588489884939223042

**Quoted post (full text):**

    #### Quoted post — @immunefi — 2022-11-04 11:14 UTC (2022-11-04 12:14 WAT)
    
    - URL: https://x.com/immunefi/status/1588489884939223042
    - Metrics (at fetch): not returned
    
    > We’re proud to release the Immunefi Whitehat Leaderboard showing the top 20 whitehats in web3! 
    >
    > Whitehats who earn their spot through genius and hard work are eligible for further rewards, exclusive merch, paid trips, speaking opportunities, and more. 
    >
    > https://immunefi.com/leaderboard [pic.x.com/rU7SdURzZz]
    
    **Media:**
    - media `3_1588487166916714496` (details not returned by the API)
    
    **Links in post:** https://immunefi.com/leaderboard
    


---

## 2022-09-22 · Post · I finally found a bug worthy of this legendary title!! [pic.x.com/ytS3KDfo2Q]


### Post — @kankodu — 2022-09-22 15:27 UTC (2022-09-22 16:27 WAT)

- URL: https://x.com/kankodu/status/1572970965042339840
- Metrics (at fetch): not returned

> I finally found a bug worthy of this legendary title!! [pic.x.com/ytS3KDfo2Q]

**Media:**
- photo: https://pbs.twimg.com/media/FdRQulwakAMAtPM.jpg — alt text: "Immunefi bug report screenshot"


---

## 2022-07-26 · Post · Really happy with how @yield team handled this bug report! https://twitter.com/yield/status/15451198


### Post — @kankodu — 2022-07-26 09:25 UTC (2022-07-26 10:25 WAT)

- URL: https://x.com/kankodu/status/1551861199897505793
- Metrics (at fetch): not returned

> Really happy with how @yield team handled this bug report! https://twitter.com/yield/status/1545119888309567489

**Links in post:** https://twitter.com/yield/status/1545119888309567489

**Quoted post** 1545119888309567489: not readable via the API (deleted, private, or withheld).
