# 🛡️ Top 10 DeFi Attacks in 2025: Old Code and Rounding Errors

- **Source URL:** https://2025-recap.decurity.io/
- **Fetched:** 2026-11-12
- **Channel:** @defendor_eng
- **Telegram message:** https://t.me/defendor_eng/977 (id 977)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
On June 26, 2025, Resupply lost nearly $9.8M in an ERC-4626 first deposit attack.
                        The attack unfolded in just 95 minutes after a new cvcrvUSD vault was deployed.

The newly deployed wstUSR market went live at 00:18 UTC with an empty crvUSD Curve Vault.
                        Just 95 minutes later at 01:53 UTC, an attacker using a 4,000 USDC flash loan from Morpho,
                        converted the funds to crvUSD and exploited the empty vault's initialization bug.
                        The attack flow was to donate 2,000 crvUSD directly to the empty vault contract, then
                        deposit 2 crvUSD to mint just 1 wei of cvcrvUSD shares.

This single wei of shares now represented the entire 2,000+
                        crvUSD deposit, creating a massively inflated price-per-share of approximately 2e36.

The vulnerability was in the ResupplyPair contract's \_updateExchangeRate() function.
                        It calculated the exchange rate using:

`_exchangeRate = 1e36 / IOracle(_exchangeRateInfo.oracle).getPrices(address(collateral))`

When the oracle returned the inflated price (exceeding 1e36), Solidity's integer division
                    rounded down the result to zero. The contract didn't check that the exchange rate was greater than
                    zero, which allowed an invalid value to be stored.

The zero exchange rate was used by the \_isSolvent() function, which calculates the LTV ratio by:

`_ltv = ((_borrowAmount * _exchangeRate * LTV_PRECISION) / EXCHANGE_PRECISION) / _collateralAmount`

A zero exchange rate broke the LTV check, making every position look solvent.
                    Using just 1 wei of collateral, the attacker borrowed 10 million reUSD tokens.

Apparently the attacker monitored governance proposals and noticed an empty vault
                        in the configuration parameters of the new market - the same pattern as in Compound fork hacks, e.g. Sonne Finance and Onyx.
