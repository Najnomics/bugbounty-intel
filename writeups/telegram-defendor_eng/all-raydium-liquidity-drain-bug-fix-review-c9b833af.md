# 💧 Critical Vulnerability in Raydium: Liquidity Drain

- **Source URL:** https://immunefi.com/blog/all/raydium-liquidity-drain-bug-fix-review
- **Fetched:** 2026-11-12
- **Channel:** @defendor_eng
- **Telegram message:** https://t.me/defendor_eng/182 (id 182)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
*•*4 min read

# Raydium Liquidity Drain Bug Fix Review

### Summary

A critical vulnerability was identified and reported by whitehat @Lastc0de in the Raydium protocol on March 10, 2025.

This vulnerability, found in the `cp-swap` program allowed an attacker to exploit the liquidity management functionality (specifically, adding liquidity) to drain funds from liquidity pools.

A bounty of $505,000 in USDC was awarded to the whitehat for this discovery. Raydium, an AMM built on the Solana blockchain, quickly addressed and resolved the issue.

### What is Raydium?

Raydium is an AMM with an integrated central order book system, currently in its V3 iteration. Users can provide liquidity, perform swaps on the exchange, and stake the RAY token for additional yield.

A fundamental aspect of Raydium is the Concentrated Liquidity Market Maker (CLMM) design.

### Vulnerability details

Vulnerability arises in the `fn deposit()` due to the lack of validation for input amounts sent by the user.

The `deposit` function is using `fn lp_tokens_to_trading_tokens` to calculate the value of input parameters `amount0` and `amount1` of tokens to be transferred into the liquidity pool from the user.

```
pub fn lp_tokens_to_trading_tokens(
    lp_token_amount: u128,
    lp_token_supply: u128,
    swap_token_0_amount: u128,
    swap_token_1_amount: u128,
    round_direction: RoundDirection,
) -> Option<TradingTokenResult> {
    let mut token_0_amount = lp_token_amount
        .checked_mul(swap_token_0_amount)?
        .checked_div(lp_token_supply)?;
    let mut token_1_amount = lp_token_amount
        .checked_mul(swap_token_1_amount)?
        .checked_div(lp_token_supply)?;
    let (token_0_amount, token_1_amount) = match round_direction {
        RoundDirection::Floor => (token_0_amount, token_1_amount),
        RoundDirection::Ceiling => {
            let token_0_remainder = lp_token_amount
                .checked_mul(swap_token_0_amount)?
                .checked_rem(lp_token_supply)?;
            // Also check for 0 token A and B amount to avoid taking too much
            // for tiny amounts of pool tokens.  For example, if someone asks
            // for 1 pool token, which is worth 0.01 token A, we avoid the
            // ceiling of taking 1 token A and instead return 0, for it to be
            // rejected later in processing.
            if token_0_remainder > 0 && token_0_amount > 0 {
                token_0_amount += 1;
            }
            let token_1_remainder = lp_token_amount
                .checked_mul(swap_token_1_amount)?
                .checked_rem(lp_token_supply)?;
            if token_1_remainder > 0 && token_1_amount > 0 {
                token_1_amount += 1;
            }
            (token_0_amount, token_1_amount)
        }
    };
    Some(TradingTokenResult {
        token_0_amount,
        token_1_amount,
    })
}
```
The problem lies in the calculations part, where the proportion of LP tokens to trading tokens is calculated. It can be outlined easily in a test pool with the following parameters: 

- LP token supply = 122

- Amount of token 0 in the pool = 150

- Amount of token 1 in the pool = 100

- Exchange rate: 1,5

Now, let’s dive in the step-by-step attack process:

1. Call deposit function with the following parameters:

`(lp_token_amount = 1; maximum_token_0_amount = 2; maximum_token_1_amount = 0)````
pub fn deposit(
    ctx: Context<Deposit>,
    lp_token_amount: u64,
    maximum_token_0_amount: u64,
    maximum_token_1_amount: u64,
) -> Result<()> {
    let pool_id = ctx.accounts.pool_state.key();
    let pool_state = &mut ctx.accounts.pool_state.load_mut()?;
    if !pool_state.get_status_by_bit(PoolStatusBitIndex::Deposit) {
        return err!(ErrorCode::NotApproved);
    }
    let (total_token_0_amount, total_token_1_amount) = pool_state.vault_amount_without_fee(
        ctx.accounts.token_0_vault.amount,
        ctx.accounts.token_1_vault.amount,
    );
    let results = CurveCalculator::lp_tokens_to_trading_tokens(
        u128::from(lp_token_amount),
        u128::from(pool_state.lp_supply),
        u128::from(total_token_0_amount),
        u128::from(total_token_1_amount),
        RoundDirection::Ceiling,
    )
```
1. When `deposit` function calls `lp_tokens_to_trading_tokens` with the following inputs:

`(lp_token_amount = 1; lp_token_supply = 122; swap_token_0_amount = 150; swap_token_1_amount = 100; round_direction = Ceiling)````
pub fn lp_tokens_to_trading_tokens(
    lp_token_amount: u128,
    lp_token_supply: u128,
    swap_token_0_amount: u128,
    swap_token_1_amount: u128,
    round_direction: RoundDirection,
) -> Option<TradingTokenResult> {
    let mut token_0_amount = lp_token_amount
        .checked_mul(swap_token_0_amount)?
        .checked_div(lp_token_supply)?;
    let mut token_1_amount = lp_token_amount
        .checked_mul(swap_token_1_amount)?
        .checked_div(lp_token_supply)?;
    let (token_0_amount, token_1_amount) = match round_direction {
        RoundDirection::Floor => (token_0_amount, token_1_amount),
        RoundDirection::Ceiling => {
            let token_0_remainder = lp_token_amount
                .checked_mul(swap_token_0_amount)?
                .checked_rem(lp_token_supply)?;
            // Also check for 0 token A and B amount to avoid taking too much
            // for tiny amounts of pool tokens.  For example, if someone asks
            // for 1 pool token, which is worth 0.01 token A, we avoid the
            // ceiling of taking 1 token A and instead return 0, for it to be
            // rejected later in processing.
            if token_0_remainder > 0 && token_0_amount > 0 {
                token_0_amount += 1;
            }
            let token_1_remainder = lp_token_amount
                .checked_mul(swap_token_1_amount)?
                .checked_rem(lp_token_supply)?;
            if token_1_remainder > 0 && token_1_amount > 0 {
                token_1_amount += 1;
            }
            (token_0_amount, token_1_amount)
        }
    };
    Some(TradingTokenResult {
        token_0_amount,
        token_1_amount,
    })
}
```
Token\_0\_amount = `lp_token_amount (1) * swap_token_0_amount (150) / lp_token_supply (122) will be equal 1`. It is important to highlight that Token\_0\_amount is an integer type, so instead of 1.22 it will be equal to one (no floating point is possible in integer types). 

3. However, the most important calculation is the calculation of `Token_1_Amount`, it will be rounded down to 0:

`Token_1_amount = lp_token_amount (1) * swap_token_1_amount (100) / lp_token_supply (122) = 0`

4. Because RoundDirection was set as Ceiling, we then execute the `Ceiling` part of the function.

After that, `token_0_remainder` is calculated:

`Token_0_remainder = lp_token_amount (1) * swap_token_0_amount (150) % lp_token_supply (122)`
This will be equal to 28.

1. After that, the following check is being executed:

```
if token_0_remainder (28) > 0 && token_0_amount (1) > 0 {
                token_0_amount += 1;
```
Because the condition is true (both values in the `if` statement are greater than 0), `token_0_amount` (1) is being increased by 1 and equals 2. 

6. After that, `token_1_remainder` is being calculated:

`Token_1_remainder = lp_token_amount (1) * swap_token_1_amount (100) % lp_token_supply (122)`
This will be equal to 100.

The next check will not pass, because `token_1_remainder` is 100 and `token_1_amount` is equal to 0.

```
if token_1_remainder (100) > 0 && token_1_amount (0) > 0 {
                token_1_amount += 1;
```
Because of that, `token_1_amount` will be equal to 0.

Thus, the function `lp_tokens_to_trading_tokens` will return 2 and 0 as a result.

To sum up, the liquidity provider initializes a pool with 150 token0 and 100 token1, and receives 22 LP tokens. 100 LP tokens would be reserved. Thus, a malicious user can add 2 token0 to the pool and receive 1 LP token without sending any token1 at all. 

After 18 repetitions only 36 token0 would be spent and 18 LP would be minted. After that, the attacker can call `withdraw` 18 times, which will result in the transfer of 23 token0 and 12 token1 to the attacker.

Since the price of token0 is 1,5 token1, the attacker's exact profit will be 23 token0 + 12 token1 = 23 token0 + 18 token0 = 41 token0.

Thus, the attacker sent 2\*18=36 token0, but received 41 token0 after withdrawal.

Continuing the attack would only increase the attacker’s profit, because after the first stage of withdrawals, the price of token0 would rise from 1.5 to 1.82.

### Mitigation/Fix

The implemented fix is quite simple: the Raydium team added `require` statements with checks to ensure that `amount_out_less_fee`, `token_0_amount`, `token_1_amount`, and `lp_token_amount` variables are not equal to zero.

### Closing Acknowledgements

We would like to thank the whitehat [@Lastc0de](https://x.com/thel4stc0de?s=11&ref=immunefi.com) for doing an amazing job in responsibly disclosing such an important bug. Big props to the Raydium team for their quick response and patch.

If you’re a developer or whitehat interested in a lucrative bug-hunting career in web3 — this message is for you. With 10–100x the rewards commonly found in web2, your efforts will pay off exponentially by switching to web3.

Check out the [Web3 Security Library](https://github.com/immunefi-team/Web3-Security-Library?utm_source=immunefi), and start earning rewards on Immunefi — the leading bug bounty platform for web3 with the world’s biggest payouts.
