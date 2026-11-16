# 🛡️ 9 Most Common Vault Bugs from Real Audits

- **Source URL:** https://paragraph.com/@0x3b/9-common-vault-bugs
- **Fetched:** 2026-11-16
- **Channel:** @defendor_eng
- **Telegram message:** https://t.me/defendor_eng/1271 (id 1271)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
1. First depositor attack
2. Being first pays too well
3. Front running bad debt
4. Gaming the lock up with 1 wei
5. How dust becomes insolvency

1. Your withdraw order is killing your yield
2. `convertToAssets + convertToShares == wrecked`
3. Tokens sitting there, unclaimed, forever
4. Idle assets are stealing yield from your users

"**I already know it**",  "**will skip this part**" is what you are thinking. **Then skip the whole article dumbass**, because I am not only gonna talk about the basic bug, but will also include it's other variants. Now with that attitude out of the way lets continue.

The most common attack for vaults, done when there are no virtual shares or offset mechanism. The main problem is how shares are calculated:

Solidity rounds down and if `totalShares` is really small (like 1 wei) and `totalAssets` bigger than `assets`, then `shares` will round down to 0.

The common patterns is:

1. Attacker deposits 1 wei asset for 1 share
2. Attacker sends 1000e18 assets to the vault
3. Vault share ratio is 1 share = 1000e18 + 1 assets
4. Victim deposits 1000e18 assets, gets minted 0 shares
5. Attacker's share is worth 2000e18 assets

**Stopping points:**

0 shares cannot be minted

Donate 51% of the victim assets in order for him to mint 1 share and you will steal 25% of his assets (2 total shares - 1500e18 total assets, 1 share is worth 750e18).

Vault does not track assets by balance - look around any find if there is a way to increase that variable without increasing the shares. Some interesting variations I've noticed trough the years are:

- deposit and round with down withdraw to receive less assets and                       increase `totalAssets` (repeat that a few dozen times)

- Liquidate your position so that you have less shares and the vault has extra assets (the vault had some extra functionality)

Offset of 1 with `shares = assets * (totalShares + 1) / (totalAssets + 1)` - The attack is no longer profitable, however the shares value can still be increased in order to grief the vault.


Bigger offset - Neither profitable, nor it changes the ratio that much, is not considered an attack.

**Fix:**

[OZ have made a really simple and easy to implement fix](https://github.com/OpenZeppelin/openzeppelin-contracts/blob/master/contracts/token/ERC20/extensions/ERC4626.sol#L245-L257) which uses `_decimalsOffset` to make virtual shares. But basically you can redo `_convertToShares` and `_convertToAssets` to be:

The problem here is that most vault that distribute rewards do it time based (epochs or dripping), but they don't account for the fact that sometimes there may be no one to claim them (no depositors).

The common patter for this is:

1. Vault is creased and immediately starts distributing rewards
2. The first depositor/staker comes after X hours/days
3. No matter how much he stakes, since he controls 100% of the shares he gets all of the rewards for that X hours/days where there were no stakers

**Stopping points:**

They may handle this, but what if everyone leaves the vault for some time and one user deposits, will rewards be paused or will he receive all of them for that missed time.

Distributing rewards based on depositor enter time - what about the rewards that were generated when no one was in the vault, do they get stuck?

**Fix:**

There is no code specific fix as the issue is more of a design/business logic related. However structurally it should distribute rewards only when `shares > 0` and track the start reward time the moment the first user joins.

If the vault has any external factors that will result in a profit or loss, but can't be put on chain with real time access, or can be observed before they happen, then share price can get MEVed.

This description complicates the issue a lot, but it comes to:

1. User1 will get liquidate and will result in bad debt for the vault
2. User2 front-runs the liquidation TX and withdraws
3. User1 is liquidated, lowering the share price from 1 to 0.9
4. User2 deposits again

User2 avoided the bad debt socialization and essentially MEV  the vault in order to keep his assets safe from bad debt.

**Stopping points:**

Bad debt is not socialized - that's another issue. What happens to the losses if they are not accounted then they will lead to insolvency.

**Fix:**

If such events can be observed before they happen, then consider making users request to withdraw, followed by some time delay (1h, 24h, etc...), when after this time they will be able to withdraw.

Deposit -> your assets are locked up -> after T time you can hold or instantly withdraw. The most common issue I've noticed with vesting is that the vest is usually set once on the first deposit/withdraw (D/W for short) and every D/W after just adds more amount. This can be exploited by D/W 1 wei and when the vest expires to do the rest.

Example:

1. User1 deposits 1 token
2. His token is locked for 1 week
3. He can now withdraw, but he deposits the rest 99 tokens
4. He has a deposit of 100 tokens and can withdraw any time

Same for when deposits are instant, but you need to vest in order to withdraw

**Stopping points:**

Every action resets your vest - can we D/W for someone else and reset their vest?

Each D/W is it's own position with it's own vest time and amount - Accounting can get really messy as for each user we need to track multiple positions and their total combined value. Adds a lot of extra logic.

Fix:

Best recommendation is to reset the D/W vest on every new instance and prevent other users from making deposits.

However if you want users to D/W any time without punishing them with the lock, then consider making each D/W into it's own position, and track user total into a mapping. This will add a lot of complexity, but when done right it's the best solution.

By far the most common of them all. But what is it?

As we already know solidity math is not precise, all divisions round down and if you are rounding down on how much shares to burn then you are essentially "rewarding" the user (even though the amounts are dust).

Simplest example is right here, where the share price changes and we may burn 1 less shares, essentially giving the user 1 more asset.

But how can 1 wei be dangerous? Usually it can't and these issues are Low or Info, however in rare circumstances it can cause insolvency. That's usually when the assets are fixed and accounted separate from vault balances (i.e. a variable instead                               of  `usdc.balanceOf(vault)`).

**Stopping points:**

But it also rounds in deposits, so it negates itself! - yeah as if there are gonna be the exact amount of deposits to withdraws. Users can deposit once and withdraw 1000 times.

**Fix:**

Simplest solution would be to use [OZ Math](https://github.com/OpenZeppelin/openzeppelin-contracts/blob/master/contracts/utils/math/Math.sol) and and simply round in favor of the system.

In favor of the system means that you always give less assets to the user and burn more users shares.

Another simple, yet often missed vault bug. When using vaults as yield, or any other group of yield earning entities for that matter it's important on how and when you deposit to each and how and when you withdraw from each, aka your sorting of priority.

Simplest example is when projects have a basic FIFO (first in first out) order, where usually this order is like:

1. Vault1 - 15% APY
2. Vault2 - 10% APY
3. Vault3 - 5% APY

From first impression this looks fine. We deposit and fill up the first vault as it has the highest yield, then the second and the third.

But if you are a smart cookie you will notice that for withdraws it's the same. We always withdraw from the highest APY vault, meaning it's never fully filled. This will in turn decrease yield significantly.

Example:

- All vaults have caps of 100k
- Vault1 and Vault2 has reached it's cap
- Vault3 is filled with 50k

1. We earn `15% * 100k + 10% * 100k + 5% * 50k = 27.5k`
2. User withdraws 50k
3. Vault1 `totalAssets` are decreased to 50k
4. Now we earn `15% * 50k + 10% * 100k + 5% * 50k = 20k`

Where as if we have withdrawn from Vault3 we would have made

`15% * 100k + 10% * 100k + 5% * 0 = 25k`

**Fix:**

Instead of using FIFO use FILO (first in last out) and sort the array based on the APY we earn in order to optimize for highest yield.

Imagine that you would need to figure out how many assets your shares represent. What function would your contracts? Most obviously `convertToAssets`, the name suggests that it will convert our shares to assets right?

That's the wrong answer.

The problem with it is they don't account for any withdraw fees or swap slippage, meaning that it will return an overinflated amount of assets.

MUST NOT be inclusive of any fees that are charged against assets in the Vault.


**Fix:**

The correct function to convert shares to assets is `previewWithdraw`. It will return an exact version of what you would withdraw if you called withdraw, but without accounting any vault or user limits (aka. returns how many assets you have).

Same is true for the reverse functions - `convertToShares` and  `previewDeposit`.

It's really common for vaults to not only distribute yield in the form of share price increases, but to also reward some sort of incentive tokens to given strategies. Simplest example and one that we cough recently on an audit is a vault that farms yield on Morpho, but does not handle [Morpho rewards](https://docs.morpho.org/learn/concepts/rewards/).

**Are reward tokens even handled?**

The most basic mistake — the vault integrates a protocol that emits reward tokens, and simply never claims or distributes them. They accumulate, sit there and get stuck forever.

**What tokens, and can they change?**

Protocols can add or rotate incentive tokens at any time. Does your vault hardcode them to one token - not good. Would recommend a map for reward tokens.

**Who can trigger the claim?**

Some protocols let anyone call the claim function, which means reward tokens can be sent directly to your contract address without warning. If your vault isn't built to handle an unexpected token transfer, those rewards are stuck.

Another easy to find (if you know it) bug is that some vaults have max caps. Be it for one reason or another they do not let more than X amount of assets be deposited.

Simple, so what's the problem here?

The issue is in the way most developers integrate with such vaults, as they don't know or consider that there is a possibility of the vault filling up and deposits to it to revert.

Sometime it's not checked and deposits are just reverting, even if there is some space still left in the vault.

Example:

1. Index vault deposits to other vaults
2. There is space for 5000 assets to be deposited
3. User calls deposit for 8000 assets, but the TX reverts
4. User leaves

Some developers fix it by implementing `maxDeposit` Now we make sure to fill the vault up and all assets are utilized!

But is that a fix? Do you see the issue here?

This bug wasn't about deposit reverting when the vault fills up, but for when it doesn't. The issue here is that after the final deposit where the internal vault is filled up we are still allowing more deposits. These extra assets are not gonna be used in a yield generating way, but will take part of that yield. This is best shown with math

1. Index vault1 has 100k assets

1. 50k are deposited to 15% APY vault
2. 50k are deposited to 5% APY vault
3. Users earn 10% APY

vs.

1. Index vault2 has 120k assets
2. 50k are deposited to 15% APY vault
3. 50k are deposited to 5% APY vault
4. 20k are idle as both vaults are filled up
5. Users earn 8.3% APY

**Fix:**

Fill up all vaults to 100% and then prevent more users from depositing.

Building a vault or anything that deals with shares?

If you have a mainnet launch, upgrade, or token event in the next 60 days and your contracts haven’t been re‑audited, you’re running on luck.

Book a security audit review call with us here:

[https://phagesecurity.com/request-audit](https://phagesecurity.com/request-audit)

or hit me up in my TG at <u>[@Pyro3b](https://x.com/@Pyro3b)</u>.
