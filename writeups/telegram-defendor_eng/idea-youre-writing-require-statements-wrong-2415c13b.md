# 🛡️ Proper use of require in DeFi for protocol security

- **Source URL:** https://www.nascent.xyz/idea/youre-writing-require-statements-wrong
- **Fetched from:** https://web.archive.org/web/20260719205849/https://www.nascent.xyz/idea/youre-writing-require-statements-wrong
- **Fetched:** 2026-11-25
- **Channel:** @defendor_eng
- **Telegram message:** https://t.me/defendor_eng/1112 (id 1112)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# You're writing require statements wrong

A new pattern for DeFi Smart Contract Security

DeFi

Security

30.6.23

DeFi

Security

30.6.23

# TL;DR

Don't just write `require` statements for a specific function; write `require` statements for your *protocol*. `Function Requirements-Effects-Interactions + Protocol Invariants` or the `FREI-PI` pattern can help make your contracts safer by forcing developers to focus on protocol level invariants in addition to function level safety.

## Motivation

In March of 2023, Euler Finance was hacked for $200 million. Euler Finance is a lending market where users can post collateral and borrow against it. It has some unique features but effectively they are a lending market comparable to Compound Finance and Aave.

You can read a post-mortem about this hack [here](https://web.archive.org/web/20260719205849/https://medium.com/@omniscia.io/euler-finance-incident-post-mortem-1ce077c28454). The tl;dr of it though was a missing health check in a particular function that allowed a user to break the fundamental invariant of a lending market.

## Fundamental Invariants

Most DeFi protocols have an invariant, a property of the program state that is expected to always be true, at their core. They may have multiple invariants, but generally they are built around a single core idea. Some examples:

- Lending markets: `A user can take no action that puts any account into an unsafe or more unsafe collateral position` ("more unsafe" meaning it was already lower than the minimum safety threshold and thus cannot be drawn down further)
- AMMs: `x * y == k`, `x + y == k`, etc.
- Liquidity Mining Staking: `A user should only ever be able to withdraw the number of staking tokens they deposited`

Where Euler went wrong wasn't necessarily that they added functionality, didn't write tests, or weren't following conventional best practices. They audited the upgrade and have tests but it was missed. No, the core issue was that they forgot the core invariant of lending markets (as did the auditors!).

*note: I don't mean to pick on Euler, they are a talented team but it is a recent motivating example*

## The Heart of the Issue

You may be thinking: "well, duh. That's why they got hacked; they forgot a `require` statement". Yes and no.

*Why* did they forget the require statement there, though?

### Where `Checks-Effects-Interactions` goes wrong

A common pattern recommended for solidity developers to use is the `Checks-Effects-Interactions` pattern. It can be extremely useful for removing reentrancy related bugs, and generally increases the number of developers performing input validation. *But*, it hides the forest for the trees.

It teaches developers: "First I write my require statements, then I do the effects, and then maybe I do any interactions, and presto I am safe". The issue is that normally, it turns into a co-mingling of checks and effects - fine right? Interactions are still last so reentrancy isn't an issue. But it forces the user to focus on the specific function and individual state transitions, in exchange for less of the broader context. That is to say:

**The Checks-Effects-Interactions pattern alone causes developers to forget their protocol's core invariants**.

It is still a great pattern for developers generally, but always should be subservient to ensuring protocol invariants (seriously, you should still use CEI!).

## Doing it right: the FREI-PI pattern

Take this snippet from dYdX's `SoloMargin` contract ([source](https://web.archive.org/web/20260719205849/https://github.com/dydxprotocol/solo/blob/0412e9457c113f663117fa6ce1048a06839ba388/contracts/protocol/impl/OperationImpl.sol)), which was a lending market and leveraged trading contract awhile back. This is a beautiful example of what I call the `Function Requirements-Effects-Interactions + Protocol Invariants` pattern, or FREI-PI pattern.

Consequently, I believe this is the only lending market from this early era of lending markets to not have had any market associated exploits. Compound and Aave didn't directly, but forks of their code [did](https://web.archive.org/web/20260719205849/https://rekt.news/agave-hundred-rekt/). And bZx was [hacked multiple times](https://web.archive.org/web/20260719205849/https://rekt.news/bzx-rekt/).

Examining the code below, notice the following abstraction:

1. Input requirements (`_verifyInputs`)
2. Actions (data transformation, state manipulation)
3. State requirements (`_verifyFinalState`)

```
 function operate(
     Storage.State storage state,
     Account.Info[] memory accounts,
     Actions.ActionArgs[] memory actions
 )
     public
 {
     Events.logOperation();
     _verifyInputs(accounts, actions);
     (
         bool[] memory primaryAccounts,
         Cache.MarketCache memory cache
     ) = _runPreprocessing(
         state,
         accounts,
         actions
     );
     _runActions(
         state,
         accounts,
         actions,
         cache
     );
     _verifyFinalState(
         state,
         accounts,
         primaryAccounts,
         cache
     );
 }
```
The commonly used `Checks-Effects-Interactions` is still performed. Notably, `Checks-Effects-Interactions` with an additional `Checks` is not equivalent to `FREI-PI` - they are similar but serve fundamentally different goals. Therefore, developers should think of them as different: FREI-PI acting as a higher abstraction aimed at protocol safety and CEI for function safety.

The structure of this contract is really interesting - the user can perform as many actions in a row as they want (deposit, borrow, trade, transfer, liquidate, etc). Want to deposit 3 different tokens, withdraw a 4th, and liquidate an account? It is a single call.

This is the power of FREI-PI: a user can do *whatever* they want to inside the protocol, as long as the core lending market invariant holds at the end of the call: `A user did not take any action that put any account into an unsafe or more unsafe collateral position`. For this contract, that is performed in `_verifyFinalState`, checking every affected account's collateralization and making sure the protocol is better off than at the start of the transaction.

There are some extra invariants included in that function that are supplemental to the core invariant, that facilitate ancillary features like closing a market, but what *really* kept the protocol safe was the core check.

## Entity-Centric FREI-PI

An additional wrinkle in FREI-PI is the concept of entity-centricity. Take a lending market, and the presupposed core invariant:

`A user can take no action that puts any account into an unsafe or more unsafe collateral position`

Technically, that is not the only invariant, but it is for the *user entity* (it still is the *core* protocol invariant and generally the user invariant is the core protocol invariant). A lending market also will generally have 2 additional entities:

1. Oracles
2. Admins/Governance

Each additional invariant makes a protocol that much more difficult to secure, and therefore the fewer, the better. This is effectively what Dan Elitzer was saying in his somewhat clickbait-titled article: [Why DeFi is Broken and How to Fix It, Pt 1: Oracle-Free Protocols](https://web.archive.org/web/20260719205849/https://www.nascent.xyz/idea/why-defi-is-broken-and-how-to-fix-it-pt-1-oracle-free-protocols) (hint: this article isn't actually saying oracles are the problem).

### Oracles

For oracles, take the $130 million [Cream Finance exploit](https://web.archive.org/web/20260719205849/https://rekt.news/cream-rekt-2/) as an example. The core invariant for an oracle entity:

`The oracle provides accurate and (relatively) live information`

Oracles prove tricky to verify at runtime with FREI-PI, but it can be done and requires some forethought. In general, Chainlink is a good choice and can [mostly be relied upon](https://web.archive.org/web/20260719205849/https://blog.chain.link/improving-and-decentralizing-chainlinks-feature-release-and-network-upgrade-process/?ref=blog.synthetix.io), to satisfy most of the invariant. It may be beneficial to have safeguards that reduce liveness in favor of accuracy in the rare case of manipulation or accidents (like a check that the last know value is not hundreds of percent larger than the current). Again, dYdX's `SoloMargin` system did an excellent job [here](https://web.archive.org/web/20260719205849/https://github.com/dydxprotocol/solo/blob/0412e9457c113f663117fa6ce1048a06839ba388/contracts/external/oracles/DaiPriceOracle.sol#L289-L309) with their DAI oracle (in case you can't tell, I think it is the best written complex smart contract system in history).

For more on oracle evaluation, and highlighting the Euler team's ability, they wrote a great piece on calculating the price of [Manipulating Uniswap V3 TWAP Oracles](https://web.archive.org/web/20260719205849/https://github.com/euler-xyz/uni-v3-twap-manipulation/blob/master/cost-of-attack.pdf).

### Admins/Governance

Administrators are the trickiest entity to create invariants for. This is largely due to most of their role being to *change* how other invariants may be held. That said, if you can avoid having administrative roles, you should.

Fundamentally, a core invariant of an admin entity might be:

`An admin can take any action if and only if the effects maintain all other invariants or intentionally removes or changes an invariant`

Unpacking that: an admin can do things that should result in no invariants breaking *unless* they are changing things so drastically in an effort to safeguard user funds (e.g.: moving assets out to a rescue contract is a removal of invariants). An admin should also be considered a user, so the core lending market user invariant should hold for them as well (meaning they cannot rug other users or the protocol). Some admin actions are currently impossible to verify at runtime via FREI-PI, but with strong enough invariants elsewhere, hopefully most issues can be mitigated. I say currently, because one could imagine using a zk proof system to potentially check the entire state of the contract (every user, every oracle, etc).

As an example of an admin breaking an invariant, take the Compound governance action that [borked the cETH market](https://web.archive.org/web/20260719205849/https://medium.com/chainlight/the-suspension-of-compound-finances-ceth-market-causes-and-solutions-b106c2e1c922) that happened in August 2022. Fundamentally, this upgrade broke the oracle invariant: `The oracle provides accurate and (relatively) live information`. Due to the missing function, the oracle could provide *no* information. A runtime FREI-PI verification, checking that the affected oracle could provide live information would have prevented the upgrade from happening. This could be baked into the `_setPriceOracle`, checking that all assets receive live information. The benefit of FREI-PI for admins, is that admins are relatively price insensitive (or at least should be), so heavier gas usage shouldn't be as big of a deal relative to users.

### Complexity is Dangerous

So while the most important invariant is the core invariant of the protocol, there can be entity-centric invariants that must hold for the core invariant to hold. But the simplest (and smallest) set of invariants are likely the safest. And a shining example of simplicity being better is...

## Why Uniswap has never been hacked (Probably)

AMMs can have the simplest fundamental invariant of any DeFi primitive: `tokenBalanceX * tokenBalanceY == k` (e.g. constant product). Every function in Uniswap V2 is based around this simple invariant:

1. Mint: add to `k`
2. Burn: subtract from `k`
3. Swap: shift `x` and `y` leaving `k` untouched
4. Skim: realign `tokenBalanceX * tokenBalanceY` to be equal to `k` by trimming extra

Uniswap V2's secret to security: 1 simple invariant at its core, all functions in service of it. The only arguable other entity is governance which can flip a fee switch, which doesn't touch the core invariant, just distribution of ownership of token balances. That simplicity in their security statement is why Uniswap has never been hacked. Not to do a disservice to the wonderful developers of Uniswap's smart contracts - it takes great engineers to find simplicity.

## The Gas Problem

My twitter mentions are already filled with optimizooor screams of horror and pain about these checks being unnecessary and inefficient. Two points on that matter:

1. You know what else is inefficient? Having to send ~~[Laurence](https://web.archive.org/web/20260719205849/https://twitter.com/functi0nZer0)~~ North Korean hackers messages via etherscan using ETH transfers with threats of FBI involvement
2. You probably already loaded all the needed data from storage anyway so it's a few require statements with warm data at the end of the call. Would you rather your protocol be negligibly more expensive or die a fiery death?

If it is prohibitively expensive, reconsider the core invariant and try to simplify.

## What does this mean for me?

As a developer, define and vocalize the core invariant early and often in the development process. As a concrete recommendation: have the first function you write be `_verifyAfter` that verifies your invariant after each call to your contract. Keep it in your contract and deploy with it there. Supplement this invariant (and other entity-centric invariants) with broader invariant tests that are checked pre-deployment ([Foundry guide](https://web.archive.org/web/20260719205849/https://book.getfoundry.sh/forge/invariant-testing?highlight=invariant#invariant-testing)).

Transient storage opens up some interesting optimizations & improvements that Nascent will be experimenting with - I would recommend thinking about how you could use transient storage as a tool for even better cross-call-context security, as well.

Not much time was spent on the input validation side of the FREI-PI pattern in this article, but it is very important as well. Defining the bounds of inputs can be a challenging task to avoid overflows and the like. Consider checking out and following the progress of our tool: [pyrometer](https://web.archive.org/web/20260719205849/https://github.com/nascentxyz/pyrometer) (currently in beta, drop us a star while you're there). It can give insight into and help find where you might not be performing input validation.

## Conclusion

Above any catchy acronyms or pattern names, the real important bit:

Find simplicity in the core invariant of your protocol. And work like hell to ensure it never breaks (or catch it before it does).

## Thanks

Many thanks to [@plotchy](https://web.archive.org/web/20260719205849/https://twitter.com/plotchy) and [@Dan Elitzer](https://web.archive.org/web/20260719205849/https://twitter.com/delitzer) for their stimulating thoughts on this. Thanks to [@Matt Solomon](https://web.archive.org/web/20260719205849/https://twitter.com/msolomon44) for his valuable feedback and review of this article and help on branding of FREI-PI.

And thanks to [@Brendan Chou](https://web.archive.org/web/20260719205849/https://twitter.com/B_Chou) and [@Antonio Juliano](https://web.archive.org/web/20260719205849/https://twitter.com/AntonioMJuliano) from dYdX for writing the `SoloMargin` margin contract (and generally being helpful early on in my solidity explorations) - the contract may be EOL, but it lives on in a new way and taught me a lot.

Previous Idea

There is no previous post

[Back to all Ideas](https://web.archive.org)

Next Idea

There is no next post

[Back to all Ideas](https://web.archive.org)

[19.2.2026NFTSFrom DeFi to NeoFiRead](https://web.archive.org/web/20260719205849/https://www.nascent.xyz/idea/from-defi-to-neofi)

DeFi

NeoFi

[24.7.2024NFTSInvesting in YupRead](https://web.archive.org/web/20260719205849/https://www.nascent.xyz/idea/yup-open-social-aggregation)

Web3

Social

[2.11.2022NFTSWhy UNIChain is Inevitable on Bankless \[PODCAST\]Read](https://web.archive.org/web/20260719205849/https://www.nascent.xyz/idea/unichain-is-inevitable-on-bankless-podcast)

DeFi

Blockchain

Web3
