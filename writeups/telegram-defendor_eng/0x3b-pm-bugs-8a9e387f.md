# 🛠️ Main Vulnerabilities of Prediction Markets

- **Source URL:** https://paragraph.com/@0x3b/pm-bugs
- **Fetched:** 2026-11-16
- **Channel:** @defendor_eng
- **Telegram message:** https://t.me/defendor_eng/1242 (id 1242)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
Prediction markets and the protocols building on top of them are booming. If you're one of those teams, this list of bugs should matter to you.

I'm not going to claim this replaces an audit, but every bug here is something we at [Phage Security](https://phagesecurity.com/) have caught in real engagements, and the patterns were consistent enough that I thought they deserved a write up.

In half of the PMs and PM add-ons I've audited there was a re-entrancy bug somewhere. That is pretty common in these products as CTFs are ERC1155 tokens, which have a receive hook when transferred (If you didn't know this it's better to quit, web3 ain't for you D:).

The best way to avoid is to have [nonReentrant](https://github.com/OpenZeppelin/openzeppelin-contracts/blob/master/contracts/utils/ReentrancyGuard.sol) on every function that sends these tokens to the user.

*But what if I have multiple contracts?* `nonReentrant` *won't protect me against multi contract re-entracy.* 

For that my dear friend we need to figure out how to stop re-entrancy without relying on `nonReentrant` modifiers.

The simplest way to do it is to just **transfer the tokens at the end of the whole call**. Save them in memory and just transfer them after everything else is done. There won't be a point in re-entering if there is no difference between it and just another call. It's that simple...

Fundamental in prediction markets. It may seem simple, but it's sometimes not accounted for when you try fancy math with positions, forget that order books have spread or when distributing yield based on YES/NO probabilities and a negative yield surfaces by.

These vulnerabilities are best described with examples, so here we go:

Order books can be used to match users who sell YES and users who buy YES, directly 1 to 1. But they can also match buys of YES and buys of NO, by collecting the USDC and then splitting it to create YES + NO tokens. Same can be done for selling when one users sells NO is matched with another user selling YES, where both tokens are used to merge into USDC and give it back proportionately to the users based on their order prices.

Fundamental feature of orderbooks are their spread. The current probabilities may be 50% / 50%, but some users will place limit orders at 10%, 20% or 30% as stop losses or entries.

Your engine may not be able to match positions that fill up to exactly 100%. Simple examples are to match 2 orders for YES at 0.6 and NO at 0.45 for a total of 1.05, or we collect YES at 0.55 and NO at 0.40 for a total of 0.95.

So what are you gonna do if positions are matched to above or bellow 100%, who is gonna take the profit and who is gonna eat the loss?

To fix the first you should forbid orders from matching above $1.00 (100%). Because the system cannot deliver on them. If we collect 100 YES for 0.6 and 100 NO at 0.45, and merge them then the total is 100 USDC, but we must deliver 60 to the YES holder and 45 to the NO, which will cause insolvency.

For the second case it comes more to a taste. Either one of both orders are matched at a discount, where they will be different from the actual price. When we collect 100 YES at 0.55, 100 NO at 0.40 and merge them we get 100 USDC, deliver 55 USDC to the YES holder and 40 to the NO, the extra 5 USDC can be fees (really big fees). Or if you want to spare your users the huge fees you can overdeliver on one or both sides (i.e. send the extra 5 USDC to them). Essentially deliver positive slippage as one or both parties are gonna receive more USDC than they placed a sell order for.

You may be doing fancy math on yield and splitting it based on YES/NO probabilities.

**Smart cookie!** 

However when farming yield there is always a possibility of negative yield. The black swan event where out of nowhere 70% of one of your Vaults TVL is wiped out. They didn't hack you, but you will still take the L and if you haven't planned for it in advance...

*Well it's gonna be problem. But how do you handle it?*

Well if you farm 100 USDC in yield you can split it 80/20 (or whatever the probabilities are at the time) and deliver 80 USDC to YES holders and 20 to NO.

However if you lose 100 USDC burning 80 YES and 20 NO won't result in the 100 USDC being accounted for. **Matter in fact you made it worse**. You've essentially accounted only for 20 USDC  as the 20 NO + 20 YES = 20 USDC and burned extra 60 YES for nothing.

You must reduce both YES and NO by 100, i.e. not to split the loss, but to account it at 100% for both YES and NO.

When charging fees how exactly would you "charge" them. If a user deposits 1000 YES tokens you can only take a fee on YES, so you take it and keep it, but the market resolves in NO. What now? The user was charged a fee, his assets decreased, but you didn't take a profit too, since all of the YES resulted in being 0$.

Your fees become a bet, and that is no fun. Not only that but your revenue comes at the resolution date of the bet, not whenever users interact with your product. You are building a project that should produce somewhat consistent revenue, not one that bets with the users.

To avoid this you can merge YES+NO in order to have pure USDC.

But merging from time to time will result in the same betting as the market may resolve before you merge. The best solution is right after taking the fee for the system to keep track of it's YES/NO tokens and to try to merge them instantly. This way you will always keep X amount of either YES or NO, but will minimize "betting" and maximize guarantied profit.

Using your position as collateral and borrowing against it may seem fine at a first glance. It's collateral that sits and does nothing, why not utilize it?

However if you dig deeper you will see that prediction have extreme volatility. Volatility doesn't go well with borrowing and lending, that is if you don't wanna get liquidated all the time.

You see some predictions may have an end date in 1 year making them somewhat stable, however they can:

- prematurely end (due to an early resolution)

- get canceled

- flip overnight
- get manipulated

Example:

1. 100k YES on if BTC will hit 100k by the end of 2026 - 60% valuation = 60k coll
2. Loan for 30k, overcollateralization ratio of 200% - pretty solid for normal markets
3. Black swan event occurs and drops BTC price by 10% in a day, market looks bad
4. Suddenly YES is valued at 25%
5. Loan is for 30k, but your coll is worth 25k

You will get liquidated at a win, but the lenders will take that loss.

First thing that comes to mind when you think about borrowing or lending is ~~leverage~~ oracles, yes oracles...

The main problem is that there are no oracles for PM positions. Yes there are deciding oracles like UMA, but no oracles from where you can get the YES/NO price.

This will prevent you from building a reliable product that is dependent on the price of a position.

**What if you make your own oracle?**

Great question! But oracles are not just prices on chain, they have many hidden components, like:

- Few sources to avoid manipulation

- Deep asset liquidity (again to avoid manipulation)
- Instant prices (who cares what the YES price was 1h ago?)

Another issue, not a security one, but user facing is how quick a user can remove and sell their position. If they are farming yield, but decide that YES no longer works for them and want to sell how much would they have to wait to get their tokens?

Some vaults tend to have withdraw periods or lock ups. Which is fine if the user want to hold their token till resolution, but for users that wanna sell when the price increases (or drops too much) that waiting is essentially forcing them to keep their bet when they don't believe in it.

Having such mechanisms will drastically lower their participation in your product.

Building a prediction market or anything that uses it's tokens?

I’m offering a limited number of free 3 day security reviews specifically for PM products.

DM me on [X](https://x.com/0x3b33) about this offer to grab a slot before going mainnet.
