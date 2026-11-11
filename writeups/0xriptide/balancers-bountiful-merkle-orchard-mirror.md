# balancers-bountiful-merkle-orchard-mirror

- **Source URL:** https://mirror.xyz/0x2719F6Dfb85086F87319079cC2f7EeFD0e40994D/NWDf5uW1Ve7-TrcPKwmM86xp8ploMSCRGC58A-NSoFY
- **Fetched:** 2026-11-11
- **Researcher:** 0xriptide
- **Method:** curl + trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---

**Security & Bounties**

Let’s talk about bounties for a bit ...

**How to run a good bug bounty program:**

*1) the protocol is a good actor w/ regard to paying bounty hunters fairly and timely 2) bounty amount represents a fair reward compared to the amount of funds at risk*

**How to run a bad bug bounty program:**

\*1) bug is disclosed to protocol and follow-up emails by hacker are ignored/no timely responses 2) payments are confirmed but delayed for weeks/months 3) actual bounty paid is less than advertised bounty amount \*

The existence of a bug bounty should be a positive signal for users/investors when deciding where to put their capital to work. It will attract hackers to the protocol in an attempt to find vulnerabilities, report those vulnerabilities, and get paid for their work. However, behind the scenes of a bounty program can tell a different story that is only known to the hacker, the bounty platform (if applicable), and the protocol team.

If the bounty is $1mm but the funds at risk are $1bn - that is not a good signal for users/investors. Why? **Because the incentive for a hacker to steal outweighs the reward which means you should assign a much higher risk profile when evaluating an investment in this project.** This is a ultimately a poor, short sighted business decision.

If the advertised bounty is $2mm and the actual bounty paid is 25% of that with unlimited user deposits at risk - that is not a good signal for users/investors. Why? **Because the incentive for a hacker to steal will outweigh the reward which means you should assign a much higher risk profile when evaluating an investment in this project.** This is a ultimately a poor, short sighted business decision (which was made by Arbitrum on the massive vulnerability I disclosed last year).

For those unfamiliar with how this ecosystem works: we have black hat hackers (hack and steal), white hat hackers (prevent hacks and earn bounties), grey hat hackers (white hat by day, opportunistic black hat by night), auditors (paid a fee to audit code), users/investors (capital providers), smart contracts (targets for capital accumulation), and the devs/protocols/companies that develop and maintain these smart contracts.

The line between a black hat and white hat hacker (especially in crypto) can be very thin. Independent white hats earn absolutely nothing if they cannot find a bug, have a difficult time getting paid justly (or at all), and then pay tax on those earned bounties. The upside is that you get some credibility in the space, but primarily you do it because it is morally the right thing to do and you want to see this ecosystem thrive. Black hats, on the other hand, can steal millions of dollars while quite easily maintaining their anonymity. That is a fact.

**Apes gonna ape**

So how do we ensure that users/investors can better understand the risk when considering which “secure” and “audited” protocol to invest their funds in? Is the risk of a 3pool 9999% farm on RugChain the same as a VC backed, heavily audited L2? Good question anon … to quote a viewpoint from the great people of Thailand “*your safety is our concern, but ultimately it is your responsibility*”.

There are no investor protections here in the wild west of crypto, but the more educated each user/investor is, the better chance they have of making a sound decision on where to ape.

Recently, I tweeted that we should have something like a “Bug Bounty Wall of Shame” to provide more transparency on which protocol teams have let the bean counters run the show and are faking the funk when it comes to paying out white hats. Low and behold … a few days later some absolute based anon created a simple site to do just that: [https://bug-bounty-wall-of-shame.github.io/](https://bug-bounty-wall-of-shame.github.io/)

While there will always be disputes over bounties, I believe egregious examples of bad behavior should be brought to light in order to provide more transparency to users/investors when considering an investment decision.

If you are a user interested in protecting your funds in this nascent ecosystem you need to have visibility into how protocols act when faced with security risks. **If users discover that a project is treating white hats unfairly they should take their capital and run far,far away!**

*If you want a great example of how you run a bug bounty program and how you approach protocol security look no further than the based gigachads at Balancer whom were a pleasure to work with on this disclosure.*

On to the bug write-up …

**Protocol Background**

Balancer is a well known protocol in the DeFi space that allows anyone to create an AMM pool containing two or more tokens that traders can swap between. Liquidity Providers lock up tokens in the pools in order to collect swap fees that are generated by traders re-balancing the pools by executing swaps. If a protocol desires to attract more liquidity to its pool, it can give LPs a higher aggregate rate of return by providing additional token rewards on top of the existing swap fees.

Balancer has historically been proactive with its stance on security and transparency when [bugs have been discovered](https://medium.com/balancer-protocol/bug-bounty-progress-disclosure-d408d2812791) in its codebase. Four of the top audit firms had already performed a deep dive on the protocol: Trail of Bits, ADBK, OpenZeppelin, and Certora. Yet, the vulnerable contract slipped past many sets of eyeballs and was deployed to Mainnet, Polygon, and Arbitrum for a massive **463 days with tens of thousands of successful transactions**.

Luckily, Balancer had an active bounty program on ImmuneFi which ultimately led me to finding a logic error deep in the the webs of the merkle orchard …

**Merkle Orchard**

In order to add additional token rewards to a pool, the tokens must first be transferred to the `MerkleOrchard` contract at `0xdAE7e32ADc5d490a43cCba1f0c736033F2b4eFca`. The tokens are transferred from the distributor (usually a protocol’s multisig) by calling `createDistribution` which pulls tokens into the `MerkleOrchard` contract and then deposits these assets into the Balancer Vault contract. These deposits in the vault are now attributed to the `MerkleOrchard` contract and linked to the distributor provided merkle tree root.

**The Bug**

Users are able to submit duplicate claims and drain the Balancer Vault contract of the entire `MerkleOrchard` account balance from the Vault contracts on Mainnet, Polygon, and Arbitrum.

In the `MerkleOrchard` contract an existing LP can call `claimDistributions` to receive its allotted token rewards for providing liquidity.

This function importantly allows a user to provide multiple claims to be processed in one call.

`claimDistributions` will call the internal function `_processClaims` which executes the for loop on L228: `for (uint256 i = 0; i < claims.length; i++)`.

L233: `(uint256 distributionWordIndex, uint256 distributionBitIndex) = _getIndices(claim.distributionId)` will return the exact same values if we use the same `claim.distributionId` value as our input. This is a key point because on L235 `if (currentWordIndex == distributionWordIndex)` will evaluate as `true` and bypass the `_setClaimedBits` function which would normally mark the claim as completed and prevent a user from claiming again.

L264: `currentChannelId = _getChannelId(tokens[claim.tokenIndex], claim.distributor)` will keep `currentChannelId` unchanged upon each iteration. This fact, combined with `currentWordIndex == distributionWordIndex` will continue to evaluate as `true` lets us bypass the calling of `_setClaimedBits` and allows us to submit duplicate claims as long as they are all provided within the same transaction.

`setClaimedBits` is finally called on L273-276 when we reach the end of the array which finally disallows the claim from being replayed:

`if (i == claims.length - 1) { _setClaimedBits(currentChannelId, claimer, currentWordIndex, currentBits); _deductClaimedBalance(currentChannelId, currentClaimAmount)`

The function then calls the Balancer vault contract which releases the tokens to the caller.

**Impact**

Balancer Vaults on Mainnet, Polygon, and Arbitrum held (in aggregate) \~$3.2mm of tokens attributed to the `MerkleOrchard` addresses. No other funds in the vaults were at risk outside of the `MerkleOrchard` balances.

**Exploit Scenario**

Any LP provider could execute the same claim multiple times in the same transaction to steal multiples of their initial claim amounts from the vault contract (max likely \~10x per claim due to gas limit). The claimer would only be limited by block gas limit and the `MerkleOrchard` account balance in the vault contract. Thus, large LPs with 6 figure claims could quickly drain the contracts, thus stealing unclaimed yield from other LPs.

Thank you to the Balancer gigachads for the prompt response, remediation, and payment of a 50 ETH bounty on an out-of-scope target.
