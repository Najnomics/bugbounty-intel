# 🛡️ Vulnerability in Beraborrow LP tokens

- **Source URL:** https://getrecon.substack.com/p/the-dark-side-of-the-lp
- **Fetched:** 2026-11-17
- **Channel:** @defendor_eng
- **Telegram message:** https://t.me/defendor_eng/378 (id 378)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
## Introduction

Sometimes you can be doing everything right but still be subject to potential novel exploit paths. This was the case for the Beraborrow team who in-spite of following best practices and using the safest known formula available for pricing LP tokens were subjected to a pricing issue in their borrowing protocol related to redemptions.

The issue which we’ll discuss here was found by the Recon team ([Issue H-7: StableBexFeed uses post-expected-arbitrage pricing on the LP possibly leading to massive loss on redemption](https://1570492309-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FffzDCMBDa391vIMqruBP%2Fuploads%2FIVPBIGmtusrrunGtrg0K%2FRound%202%20Final%20-%20Beraborrow%20Collaborative%20Audit%20Report.pdf?alt=media&token=a6f031fc-5143-4e3e-9fa6-16923e315047)) during a Sherlock collaborative audit for Beraborrow using manual review and whose impact was escalated using fuzzing.

The issue relates to the use of Berachain’s native exchange ([BEX](https://docs.bex.berachain.com/)) feeds for pricing LP tokens provided as collateral in the [Beraborrow](https://beraborrow.gitbook.io/docs) protocol, which caused them to leak value when a user redeems a borrow position.

The BEX price feeds in which the issue was discovered were tested during development and audits but, due to the issue discussed here, an alternative pricing approach using a [Chronicle](https://chroniclelabs.org/) oracle was ultimately implemented in production instead.

## What is Beraborrow

Beraborrow is [Liquity V1](https://docs.liquity.org/liquity-v1) fork borrowing protocol built on Berachain that allows users to access liquidity for their assets without having to sell them. Users do this by depositing their collateral assets into “Dens” which allows them to mint NECT, an over-collateralized stablecoin.

Particularly of interest for the vulnerability discussed here is that users can deposit LP tokens (representing a liquidity position in a liquidity pool) as their underlying collateral which allows them to borrow against these tokens while still also earning yield from liquidity pool swap fees.

Beraborrow allows users to provide LP tokens representing liquidity from the native Berachain BEX exchange.


Because the protocol allows users to borrow against these LP tokens, a mechanism to accurately price them was needed, and while seemingly trivial at first, we’ll see how the added complexity of pricing a token representing a pool with variable token quantities ended up being the root cause of the vulnerability discovered.

## Naive Off-Chain Pricing

Pricing of an LP token in a non-adversarial environment is somewhat simple. It can be calculated as the value of the assets in the pool divided by the total supply of the LP token.

This gives us the pro-rata value of each LP token, but historically every protocol that has used this pricing formula has been exploited because liquidity pools are fundamentally manipulatable when priced this way, where attackers can add significant liquidity to assets in the pool to overvalue the LP token. This is made even simpler on the attacker side with the use of flashloans.

Projects that assumed the pool’s reserves were unmanipulatable using the naive formula have also been exploited via view-reentrancy (including [Balancer](https://forum.balancer.fi/t/reentrancy-vulnerability-scope-expanded/4345) and [Curve](https://www.chainsecurity.com/blog/curve-lp-oracle-manipulation-post-mortem)).

Ultimately the only safe LP pricing mechanism consists of pricing fair reserves, which are “fair” because they are unmanipulatable via flashloans or temporary forced imbalancing meaning they ignore pre-arbitrage values.

In this [Secureum Workshop](https://www.youtube.com/watch?v=3A7aa5B8aak) [Alex](https://x.com/GalloDaSballo) showed how pre-arbitrage LP pricing can be exploited.


## A Better Approach: the Fair Price Ratio

To prevent the types of exploits mentioned above when pricing LP tokens, protocols often use the fair reserve formula, originally made popular by [this post](https://blog.alphaventuredao.io/fair-lp-token-pricing/).

The gives us the lower bound value for the LP token, based on the balance of assets in the liquidity pool and oracle reported prices of the tokens being LP’d:

In the above formula the fair price of one of the pool assets can be found using an oracle or TWAP.

This formula gives us the value of the LP token which we can use when determining borrowing power (the amount of borrowed assets that should be received for a given amount of collateral), which most importantly is unmanipulable, preventing a user from artificially increasing the price and therefore making the LP token more valuable by unbalancing the pool.

However, as we’ll see below, the downside of this formula is that it leaks value when pricing redemptions (where it should ideally overprice the value of the LP token as to avoid opening up opportunities for arbitrage), allowing users to gain leaked value when redeeming LP tokens.

## Finding the Arbitrage

The Beraborrow team correctly applied the fair-reserves formula in their protocol to the price feeds associated with a given LP pair in the BEX and included checks for view-reentrancy which could allow altering reserves while only some tokens had been transferred, resulting in abnormal pricing. This meant that by all metrics, the calculated value of an LP token was correct when opening a borrowing position.

However, after digging deeper using the Echidna fuzzer, Alex was able to demonstrate that this pricing formula can leak substantial value when used for calculating the value of a redemption.

The key to understanding the issue is in noticing that pricing LPs via the fair reserve formula takes the *minimum* theoretical value that the LP token can have. Notably, this undervalues the LP token if the liquidity pool has tokens that are unbalanced or don't have a symmetrical reserves to price ratio. In these scenarios the fair reserve formula will under-price the LP token which is fine for valuing positions when they’re opened, but causes problems in redemptions.

Take the following example:

- Assume we have a 1:1 USDC | USDT LP token.
- The pool which the token represents is unbalanced and actually has 1.1USDC and 0.91 USDT.
- Redeeming said LP token for the underlying assets will result in 1.1 + 0.91 = 2.01 assets, whereas the nominal value given by the fair price formula would be 2 USD.

Therefore using the minimum value (2 USD) in redemptions is leaking the excess value that comes from the reserves being unbalanced (.01 USD) from the protocol because the LP token is underpriced.

## Escalating the Bug

To determine an upper bound for the value leak, we used Echidna’s [optimization mode](https://secure-contracts.com/program-analysis/echidna/advanced/optimization_mode.html?highlight=optimization%20mode#finding-local-maximums-using-optimization-mode) to identify an approximation of the maximum possible difference between the expected price and the redeemable price which was generated into a POC.

The setup consisted of using the actual on-chain factories provided by Balancer (BEX is an implementation of Balancer on Berachain) to deploy a new pool into a forked fuzz testing environment:

With a pool deployed into the test environment, we could then expose the following target function [handlers](https://book.getrecon.xyz/using_recon/building_handlers.html#what-are-handlers) which allowed the fuzzer to explore interesting states on the pool:

The following function could then be used to return a value that would allow Echidna to optimize the difference between the value on redemption calculated using the fair price formula and any excess value that would be leaked:

## Interpreting the Results

A long duration fuzzing run was then executed using the Recon Pro [job runner](https://book.getrecon.xyz/using_recon/running_jobs.html) and produced the following POC using our [echidna log scraper](https://book.getrecon.xyz/free_recon_tools/echidna_scraper.html) tool:

We can see that when it comes to the formula leaking value, the maximum difference between the value actually in the pool and the value reported by the oracle of \~1.81e21 is very high.

It should be noted that the value in the above test is hypothetical as the fuzzer was passing unclamped values to the target functions, allowing it to reach more extreme values, meaning the maximum impact in practice would be smaller as it would be limited by the liquidity an attacker could supply to unbalance the pool. However the principle still holds and demonstrates that the value can be manipulated leading to value to be leaked from the protocol. This result led us to recommend to the Beraborrow team to not proceed with an on-chain pricing mechanism.

## Conclusion

We hope we’ve demonstrated how even when you think you could be doing everything right, when applying existing mechanisms in DeFi to novel use cases you can open up the possibility for novel threat vectors that can only be found by careful review. In this case the issue was discovered manually but fuzzing was used to escalate the possible impact and demonstrate the possible value that could be lost.

The above-mentioned issue was categorized as high impact during the competition because without a very high redemption fee, the given collaterals could be subject to continuous arbitrage against depositors.

Ultimately, given the complexities of on-chain pricing discussed above and the risks for value leak, we recommended Beraborrow not to proceed with allowing BEX LP tokens as collateral.

However, through their collaboration with Chronicle (an oracle for pricing the LP tokens), and by raising the minimum redemption fee to a threshold that matches or surpasses the inaccuracies and delays of said fees, they can now offer BEX LP Tokens as collateral without exposing Den owners to arbitrage risks.

If you want help finding these types of unique vulnerabilities that others may have missed by combining a skilled security researcher and a powerful invariant testing suite for your codebase, [reach out to us](https://tally.so/r/w2Vqxb)!
