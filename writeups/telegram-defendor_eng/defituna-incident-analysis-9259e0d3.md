# 🔍 DefiTuna Exploit Root Cause Analysis

- **Source URL:** https://www.certik.com/blog/defituna-incident-analysis
- **Fetched:** 2026-11-15
- **Channel:** @defendor_eng
- **Telegram message:** https://t.me/defendor_eng/1858 (id 1858)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
## Incident Summary

On 16 July 2026, [DeFiTuna (opens in a new tab)](https://x.com/DeFiTuna) was exploited for **$569,601 USDC** on Solana. The attackers created a highly illiquid TUNA/USDC pool and used it as the destination for borrowed USDC routed through Jupiter. Because the swap returned only a negligible amount of TUNA, DeFiTuna’s value calculation rounded the position’s total assets down to zero. The protocol then incorrectly treated the position as healthy, allowing the attackers to bypass the solvency check and withdraw the USDC through attacker-controlled liquidity positions.

## Key Addresses

| Address | Label | 
|---|---|
| 9ytGWP8tCRF1keREJ5VHqBpSuM9MZYwm3oFQQa1SvESb | Attacker 1 | 
| 917DKTphW3rhBG5gsJpwKsNGisNV2dx74uUFd8HBEjtg | Attacker 2 | 
| 7hiHL8AgDuLNVDQLfN3GHdLAEeCN1F7uz6nSANRvFJst | Attacker 3 | 
| BK9aTnKfPNnnj45Me5ACrky2vexzUrZHRzr4BjmQpH3c | Attacker 4 | 
| 8P3H7Hy98LWhw5QhuXdoigVdAzPCYRTYjdtQQKhGwvqD | Attacker 5 | 
| GrXBhM6Ty6YxubFp8zubtJF12WXmKj1dhMyakRPeaDpo | Attacker 6 | 
| F4xUroPaHro4gb2JAqa3e93E7DdZytRQJ4L2cHT5E53p | Attacker 7 | 
| ETGhosPrFApbiiKXDpxrhBz7J2MdTA3dxnL2Nkio9vEX | Attacker 8 | 
| 4ZKkGZuoXqgSHbmsJXUib3dgn5WNhzbPEXrxuMYJ5oQ3 | Attacker 9 | 
| tuna4uSQZncNeeiAMKbstuxA9CUkHH6HmC64wgmnogD | DefiTuna | 
| D76dDcSU5HnAGqVEZCDLyGgLpTp4xZuqeZyVDtUdDv55 | Damaged USDC vault | 
| 917DKTphW3rhBG5gsJpwKsNGisNV2dx74uUFd8HBEjtg | Fake Pool | 

## Attack Flow

**Jul-16-2026 05:48:12** - [Txn (opens in a new tab)](https://solscan.io/tx/124ibr7NU7AtJdeZ1WJjJy5YathNiBtCnV554uwJtkc7qEXeF64dmCziv4QoiEEMRG6EmCRx8ec2LkARpWH3kvEG)

1. The attackers created a nearly empty TUNA/USDC Fusion pool. They set its initial price close to the legitimate oracle price, so DeFiTuna’s pre-swap price-deviation checks passed.
2. Then placed two attacker-controlled limit-order positions in that pool at abnormally high tick 208,640, adding 0.000526 + 0.000526 = 0.001052 TUNA. These positions were owned by 7hiH…FJst and BK9a…QpH3c. They were designed to receive the USDC entering the pool.
3. Call DefiTuna: Open\_and\_increase\_tuna\_spot\_position\_jupiter
Decoding the Instruction Data referencing [tuna.json (opens in a new tab)](https://github.com/DefiTuna/tuna-sdk/blob/6a0e6b80b089e86cf4f59391ea7e10ee983c483e/target/idl/tuna.json#L3662-L3812) get
That the attacker opened the opened a DeFiTuna spot position with zero collateral
The 570K USDC borrowed from lending pool minus fee were routed through Embedded Jupiter Router, and the 47 bytes instruction specified the swap path.
The path is to swap 569,601 USDC, which is all USDC borrowed minus the fees, for TUNA through the prepared thin pool
The exact swap is at tick 208640 as they are the only non-empty ones, considering 0.1% fee,  the output amount is 569601/(1.0001)^208640\*(1-0.001) = 0.000494845, rounded down to 0.000494 TUNA.

After receiving those 494 raw units, DeFiTuna valued the position at its pre-swap/oracle price 0.001837534 in is\_healthy() -> compute\_total\_and\_debt()  ([tuna\_position.rs (opens in a new tab)](https://github.com/DefiTuna/tuna-sdk/blob/6a0e6b80b089e86cf4f59391ea7e10ee983c483e/rust-sdk/client/src/implementation/tuna_position.rs#L41-L70)).
At line51, 494 × 0.0018375338 = 0.9077417.

At line 53, to\_num:\<u64>() converts the positive fixed-point value to an integer by discarding the fractional part, so the result is zero.

Then the zero ‘total’ was evaluated under the assumption that “the leverage of an empty position is always 1.0x.” and the position is considered healthy.

1. The USDC now belonged economically to the two malicious limit-order positions. So each attacker called DecreaseLimitOrder to withdraw 284,280.483231 USDC each.

## Vulnerability

In TunaPosition.ishealthy() solvency check, the zero ‘total’ value was evaluated under the assumption that “the leverage of an empty position is always 1.0x.” and the position is considered healthy. The self.compute\_total\_and\_debt() uses a reference sqrt\_price and round down the result in its calculation at line 53. The attacker engineered a very skewed pool that after routing USDC assets to the pool through an arbitrary swap path, the returning asset value is so small that the rounding in to\_num::\<u64>() reduced the total to zero, effectively bypassing the solvency check.

## Fund Flow

From 7hiHL8AgDuLNVDQLfN3GHdLAEeCN1F7uz6nSANRvFJst and BK9aTnKfPNnnj45Me5ACrky2vexzUrZHRzr4BjmQpH3c funds were [bridged (opens in a new tab)](https://explorer.mayan.finance/trader/0xb2cD3E99E45F8ab15fee77a014A3D82F9FE05f3E) from Solana to Ethereum network via Mayan. On Ethereum, 140 ETH was deposited into [Railgun (opens in a new tab)](https://etherscan.io/tx/0xbbb20a9c80a9a6ffbf1b93315ae06b2562dfe1c96c2c74a10da76c1a245b4085), while 291,696 DAI and 5 ETH remains in wallet 0x509B9D094A6C26D716aaC131E8aDee5B16B86d3e as of 20 July.

To keep up to date on the latest incident alerts and statistics, follow [@certikalert (opens in a new tab)](https://x.com/CertiKAlert) on X, or read our latest analysis on [certik.com](https://www.certik.com/blog).
