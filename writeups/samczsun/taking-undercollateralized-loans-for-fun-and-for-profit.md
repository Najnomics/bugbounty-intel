# taking-undercollateralized-loans-for-fun-and-for-profit

- **Source URL:** https://samczsun.com/taking-undercollateralized-loans-for-fun-and-for-profit/
- **Fetched:** 2026-11-11
- **Researcher:** samczsun
- **Method:** curl + trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---

# Taking undercollateralized loans for fun and for profit

# tl;dr

By relying on an on-chain decentralized price oracle without validating the rates returned, [DDEX](https://margin.ddex.io) and [bZx](https://bzx.network) were susceptible to atomic price manipulation. This would have resulted in the loss of liquid ETH in the ETH/DAI market for DDEX, and loss of all liquid funds in bZx. Fortunately, no funds were actually lost.

# What is decentralized lending?

First, let's talk about traditional lending. When you take out a loan, you typically need to provide some sort of collateral so that if you default on your loan, the lender can then seize the collateral. In order to determine how much collateral you need to supply, the lender typically knows or can reliably calculate the fair market value (FMV) of the collateral.

In decentralized lending, the same process occurs except now the lender is a smart contract that is isolated from the outside world. This means that it can't simply "know" the FMV of whatever collateral you're trying to provide.

To solve this problem, developers instruct the smart contract to query an *oracle*, which accepts the address of a token and returns the current price of that token in a desired currency (for example, ETH or USD). Different DeFi projects have taken different approaches to implementing this oracle, but they can generally all be classified in one of five ways (although some implementations blur the lines more than others):

1. Off-chain Centralized Oracle
This type of oracle simply accepts new prices from an off-chain source, typically an account controlled by the project. Due to the need to quickly update the oracle with new exchange rates, the account is typically an EOA and not a multisig. There may be some sanity checking to ensure that prices don't fluctuate too wildly.[Compound Finance](https://compound.finance) and [Synthetix](https://www.synthetix.io) mainly use this type of oracle for most assets
2. Off-chain Decentralized Oracle
This type of oracle accepts new prices from multiple off-chain sources and merges the values through a mathematical function, such as an average. In this model, a multisig wallet is typically used to manage the list of authorized sources.[Maker](https://makerdao.com/feeds/) uses this type of oracle for ETH and other assets
3. On-chain Centralized Oracle
This type of oracle determines the price of assets using an on-chain source, such as a DEX. However, only a central authority can trigger the oracle to read from the on-chain source. Like an off-chain centralized oracle, this type of oracle requires rapid updates and as such the triggering account is likely an EOA and not a multisig.[dYdX](https://dydx.exchange) and [Nuo](https://nuo.network) use this type of oracle for certain assets
4. On-chain Decentralized Oracle
This type of oracle determines the price of assets using an on-chain source, but can be updated by anyone. There may be some sanity checking to ensure that prices don't fluctuate too wildly.[DDEX](https://margin.ddex.io) uses this type oracle for DAI, while [bZx](https://bzx.network) uses this type of oracle for all assets
5. Constant Oracle
This type of oracle simply returns a constant value, and is typically used for stablecoins. Nearly all projects mentioned above use this type of oracle for USDC due to its guaranteed peg

# The problem

While searching for additional vulnerable projects, I came across this tweet.

[I'm honestly worried they're using it as a price feed. If my hunch is right that's so attackable....](https://x.com/VitalikButerin/status/1098168793178820609)

Someone asked for clarification, and the Uniswap project responded with the following.

These tweets explain the problem very clearly, but it's important to note that this problem exists for any oracle which can provide the FMV on-chain, not just Uniswap.

In general, if a price oracle is completely decentralized, then an attacker can manipulate the apparent price at a specific instant with minimal to no loss in slippage fees. If an attacker can then convince a DeFi dApp to check the oracle at the instant when the apparent price has been manipulated, then they can cause significant harm to the system. In the case of DDEX and bZx, it was possible to take out a loan that appeared to be sufficiently collateralized, but was in fact undercollateralized.

# DDEX (Hydro Protocol)

DDEX is a decentralized exchange platform but are in the process of expanding into decentralized lending so that they can offer their users the ability to create leveraged long and short positions. They're currently beta testing their decentralized margin exchange.

On September 9th 2019, DDEX added DAI as an asset to their margin trading platform and enabled the ETH/DAI market. For the oracle, they specified [this](https://etherscan.io/address/0xeB1f1A285fee2AB60D2910F2786E1D036E09EAA8) smart contract which returns the value of DAI/USD by calculating `PriceOfETHInUSD/PriceOfETHInDAI`. The value of ETH/USD is read from the Maker oracle, while the value of ETH/DAI is read from either Eth2Dai, or if the spread is too great, Uniswap.

In order to trigger an update and cause the oracle to refresh its stored value, a user simply has to call `updatePrice()`.

## The attack

Let's assume we can manipulate the apparent value of DAI/USD. If this is the case, we would like to use this to borrow all of the ETH in the system while providing as little DAI as possible. To achieve this, we can either lower the apparent value of ETH/USD or increase the apparent value of DAI/USD. Since we're already assuming that the apparent value of DAI/USD is manipulable, we'll choose the latter.

To increase the apparent value DAI/USD, we can either increase the apparent value of ETH/USD, or decrease the apparent value of ETH/DAI. For all intents and purposes manipulating Maker's oracle is impossible, so we'll try decreasing the apparent value of ETH/DAI.

The oracle will calculate the value of ETH/DAI as reported by Eth2Dai by taking the average of the current asking price and the current bidding price. In order to decrease this value, we'll need to lower the current bidding price by filling existing orders and then lower the current asking price by placing new orders.

However, this requires a significant initial investment (as we need to fill orders then make an equivalent number of orders) and is non-trivial to implement. On the other hand, we can drop the Uniswap price simply by selling a large amount of DAI to Uniswap. As such, we'll aim to bypass the Eth2Dai logic and manipulate the Uniswap price.

In order to bypass Eth2Dai, we need to manipulate the magnitude of the spread. We can do this in one of two ways:

1. Clear out one side of the orderbook while leaving the other alone. This causes spread to increase positively
2. Force a crossed orderbook by listing an extreme buy or sell order. This causes spread to decrease negatively.

While option 2 would result in no losses from taking unfavorable orders, the use of SafeMath disallows a crossed orderbook and as such is unavailable to us. Instead, we'll force a large positive spread by clearing out one side of the orderbook. This will cause the DAI oracle to fallback to Uniswap to determine the price of DAI. Then, we can cause the Uniswap price of DAI/ETH to drop by buying a large amount of DAI. Once the apparent value of DAI/USD has been manipulated, it's trivial to take out a loan like as usual.

### Demo

The following script will turn a profit of approximately 70 ETH by:

1. Clearing out Eth2Dai's sell orders until the spread is large enough that the oracle rejects the price
2. Buying more DAI from Uniswap, dropping the price from 213DAI/ETH to 13DAI/ETH
3. Borrowing all the available ETH (\~120) for a small amount of DAI (\~2500)
4. Selling the DAI we bought from Uniswap back to Uniswap
5. Selling the DAI we bought from Eth2Dai back to Eth2Dai
6. Resetting the oracle (don't want anyone else abusing our favorable rates)

### Solution

The DDEX team fixed this by deploying a [new oracle](https://etherscan.io/address/0xe6f148448b61339a59ef6ab9ab7378e9200fa745) which places sanity bounds on the price of DAI, currently set to `0.95` and `1.05`.

# bZx and Fulcrum

[bZx](https://bzx.network) is a decentralized margin-trading protocol, while [Fulcrum](https://fulcrum.trade/#/) is a project built by the bZx team on top of bZx itself. One feature of Fulcrum is the ability to take a loan on an *iToken* (read more about that [here](https://medium.com/bzxnetwork/introducing-fulcrum-tokenized-margin-made-dead-simple-e65ccc82393f)) using any\* other token as collateral. In order to determine how much collateral is needed, bZx uses the [Kyber Network](https://kyber.network) as an on-chain decentralized oracle to check the conversion rate between the collateral token and the loan token.

\* if it's tradable on Kyber

However, it's important to first understand how the Kyber Network functions. Unlike most other DEXes, the Kyber Network derives liquidity from *reserves* (read more about that [here](https://developer.kyber.network/docs/Reserves-Intro/)). When a user wants to make a trade between two tokens A and B, the main Kyber contract will query all registered reserves for the best rate between A/ETH and ETH/B, then perform the trade using the two reserves selected.

Reserves can be listed automatically through the *PermissionlessOrderbookReserveLister* contract, which will create a *permissionless* reserve. Reserves can also be listed by the Kyber team on behalf of a market maker after KYC and legal requirements are met. In this case, the reserve will be a *permissioned* reserve. When conducting a trade using Kyber, traders have the option of only using permissioned reserves, or using all available reserves.

## The attack

When bZx checks the price of a collateral token, it specifies that only permissioned reserves should be used. This decision was made based on the Kyber whitepaper at the time, with the logic being that permissioned reserves had to undergo review and so the rates should be "correct".

This means that if we can somehow increase the rate reported by a permissioned reserve, we can trick Fulcrum into thinking our collateral is worth more than it really is.

### A permissioned OrderbookReserve

On June 16 2019, the Kyber team listed an OrderbookReserve for the WAX token as a permissioned reserve in [this transaction](https://etherscan.io/tx/0xce7df57e6b6d5589f19125b9298bbb36e672d373196d7610073540f59220c318). This was interesting because the statement "an OrderbookReserve is always permissioned" was considered to be axiomatic.

After this reserve was listed, the Kyber Network itself continued to perform according to specifications. However, we can now significantly affect the apparent exchange rate between WAX and ETH simply by listing an order, which means that we can trick any project which relies on Kyber to provide an accurate FMV.

#### Demo

The following script will turn a profit of approximately 1200ETH by:

1. Listing an order buying 1 WAX for 10 ETH, increasing the price from 0.00ETH/WAX to 10ETH/WAX
2. Borrowing DAI from bZx using WAX as a collateral
3. Cancelling all orders and converting all assets to ETH

#### Solution

The bZx team blocked this attack by whitelisting tokens which can be used as collateral.

### Eth2Dai

Now that there's a whitelist on the tokens that can be used as collateral, we'll need to through all the permissioned reserves to see if there's anything else that we can abuse. It turns out that DAI, one of the whitelisted tokens, has a permissioned reserve which integrates with Eth2Dai. As Eth2Dai allows users to create limit orders, this is essentially the previous attack but with more steps.

Interestingly, we first observe that although the Eth2Dai contract is titled `MatchingMarket`, it's not strictly true that all new orders will be automatically matched. This is because while the functions `offer(uint,ERC20,uint,ERC20,uint)` and `offer(uint,ERC20,uint,ERC20,uint,bool)` will trigger the matching logic, the function `offer(uint,ERC20,uint,ERC20)` does not.

Furthermore, we observe that even though the comments seem to suggest that only authorized users can call `offer(uint,ERC20,uint,ERC20)`, there's no authorization logic at all.

While in practice lack of authorization is irrelevant as arbitrage bots will quickly fill any orders that can be automatically matched, in an atomic transaction we can create and cancel arbitrage-able orders and no bots will be able to fill them.

All that's left is to slightly modify our script from the previous attack to place orders on Eth2Dai instead of the OrderbookReserve. Note that in this case we will need to call both `order(uint,ERC20,uint,ERC20)` to submit the order to Eth2Dai without it being atomically matched, and then `insert(uint,uint)` in order to manually sort the order without triggering matching.

#### Demo

The following script will turn a profit of approximately 2500ETH by:

1. Listing an order buying 1 DAI for 10 ETH, increasing the price from 0.006ETH/DAI to 9.98ETH/DAI.
2. Borrowing ETH from bZx using DAI as collateral
3. Cancelling all orders and converting all assets to ETH

#### Solution

The bZx team blocked this attack by modifying the oracle logic such that if the collateral and loan token were both either DAI or WETH, then the exchange rate would be loaded directly from Maker's oracles.

However, this solution was incomplete because of the way Kyber resolves the best rate. If you'll recall, Kyber determines the best rate for A/B by determining the best rate for A/ETH and ETH/B, then calculating the amount of B that could be bought with the ETH received by trading A.

This meant that if we were to attempt to borrow a non-ETH token such as USDC using DAI as collateral, Kyber would first determine the best exchange rate for DAI/ETH, then the best rate for ETH/USDC, and finally the best rate for DAI/USDC. Because we can artificially increase the exchange rate for DAI/ETH, we can still manipulate the exchange rate for DAI/USDC even though we don't control a permissioned USDC reserve.

The bZx team blocked this attack in two ways:

1. If either the loan token or collateral token wasn't ETH, then bZx would manually determine the exchange rate between the token and ETH, unless
2. The loan token or collateral token was a USD-based stablecoin, in which case bZx would use the rate from Maker's oracle

### Uniswap

An astute reader may notice at this point that bZx's solution still does not handle incorrect FMVs for arbitrary tokens. This means that if we can find another permissioned reserve which can be manipulated, we can take out yet another undercollateralized loan.

After sifting through all the registered permissioned reserves for the whitelisted tokens, we notice that the REP token has a reserve which integrates with Uniswap. We already know from our attacks on DDEX that Uniswap's prices can be manipulated, so we can re-purpose our previous attack and substitute Eth2Dai and DAI for Uniswap and REP.

#### Demo

The following script will turn a profit of approximately 2500ETH by:

1. Performing a large order buy on Uniswap's REP exchange, increasing the price from 0.05ETH/REP to 6.05ETH/REP
2. Borrowing ETH from bZx using REP as collateral
3. Cancelling all orders and convert all assets to ETH

#### Solution

The bZx team reverted their changes for the previous attack and instead implemented a spread check, such that if the spread was above a certain threshold then the loan would be rejected. This solution handles the generic case so long as both tokens being queried has at least one non-manipulable reserve on Kyber, which is currently the case for all whitelisted tokens.

# Key Takeaways

## Don't use an on-chain decentralized oracle without some sort of validation

Due to the nature of on-chain decentralized oracles, ensure that you're validating the rate being returned, whether it's by taking the order (thereby nullifying any gains which may have been realized), comparing the rate against known good rates (in the case of DAI), or comparing the rate in both directions.

## Consider the implications of dependencies on third-party projects

In both cases, DDEX and bZx assumed that Uniswap and Kyber would be a source of accurate price data. However, an accurate rate for a DEX means that a trade can be made using that rate, while an accurate rate for a DeFi project means that it is close to or equal to the FMV. In other words, an accurate rate for a DeFi project is an accurate rate for a DEX, but the opposite might not be true.

Furthermore, bZx's second attempt at solving this problem was insufficient due to a misunderstanding in how the Kyber Network internally calculates the exchange rate between two non-ETH tokens.

As such, before introducing a dependency on a third-party project, consider not only whether the project has been audited, but also whether the project's specifications and threat model align with your own. If you have the time, taking an in-depth look at their contracts also doesn't hurt.
