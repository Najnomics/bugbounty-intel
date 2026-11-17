# 🛡️ Aave V4 introduces Risk Premiums for precise risk assessment

- **Source URL:** https://aave.com/blog/aave-v4-risk-premiums
- **Fetched:** 2026-11-17
- **Channel:** @defendor_eng
- **Telegram message:** https://t.me/defendor_eng/327 (id 327)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
One significant change coming to Aave V4 are Risk Premiums. Risk Premiums solve a fundamental problem that has existed in DeFi lending for a while: uniform borrowing rates that don't reflect actual collateral risk.

Different collaterals are tied to risk based on their market behavior, liquidity profiles, and counterparty risks. Protocols typically fail to adjust the rate environment to reflect the true risk that collateral creates accurately, and they struggle to price risk alongside market changes.

This post will explain what Risk Premiums are in the context of V4, how they work, and why V4 will use them for accurate risk management.

## Aave V3's Uniform Rates

In lending, interest rates reflect loan risk. Borrowers with better credit scores receive lower rates because they're less likely to default. Those with poor credit histories pay higher rates to compensate lenders for increased risk. This risk-based pricing is fundamental to lending markets, but has been largely absent from DeFi lending protocols.

Aave V3's borrowing rates are set by supply and demand for each asset within a market. Risk is priced at the market level, not the individual level, so all borrowers in the same market pay the same rate regardless of their collateral.

A user borrowing USDC against ETH collateral pays the same rate as someone borrowing USDC against a riskier token, as long as they're in the same market. While this creates simplicity, it means that users with higher-quality collateral compositions subsidize riskier borrowers.

This approach also limits the protocol's ability to support diverse collateral types. Adding riskier assets to a market affects the risk profile for all users in that market, making it challenging to balance accessibility with safety. When lenders sense increased risk, their only remedy is to withdraw funds from the market, creating rate instability and liquidity fragmentation.

## The Risk Premium System in V4

*If you're unfamiliar with V4's architecture, read our overview here.*

Aave V4 solves this problem by introducing Risk Premiums. In this new system, Risk Premiums create borrowing rates based on your collateral quality. Instead of everyone paying the same rate like in V3, your borrowing cost reflects the actual risk of your collateral.

Here's how it works. The Liquidity Hub sets a base borrowing rate for each asset that adjusts based on supply and demand, just like V3's rate calculation. Users with the highest quality collateral, like ETH on Ethereum, pay the base rate with no additional charges. Everyone else pays an extra amount on top of the base rate, depending on the risk of collateral.

For example, if the base rate for borrowing GHO is 5% and you're using WETH as collateral, you pay exactly 5% since WETH has a 0% Collateral Risk. If you're using LINK as collateral with a 30% Collateral Risk, you accumulate additional premium debt equal to 30% of your base debt accumulation. Using UNI as collateral with a 40% Collateral Risk means you accumulate additional premium debt equal to 40% of your base debt accumulation.

This creates a tiered system where borrowing costs reflect actual risk. Users with stronger collateral get better rates, while those using riskier assets pay premiums that match how risky their collateral is.

## The Three Levels of Risk Premiums

Risk Premiums operate at three different levels in Aave V4, each serving a specific purpose in the overall risk management system.

Asset Liquidity Premiums form the foundation. Each asset gets assigned a risk score when it's listed on the protocol, ranging from 0% for the highest quality assets to 1000% for the riskiest. ETH might have a 0% Asset Collateral Risk, while a newer token might have a 200% Asset Liquidity Premium. Governance can adjust these scores over time as market conditions change.

User Risk Premiums represent your risk profile. If you're using multiple types of collateral, the system calculates an average based on the dollar value and Asset Liquidity Premium of each asset you're using. Someone using $10,000 of ETH and $5,000 units of a riskier token would have a User Risk Premium somewhere between the two individual Asset Liquidity Premiums, weighted by their dollar amounts.

Spoke Risk Premiums represent the average risk across all users in a particular Spoke. Each Spoke calculates its own average Risk Premium based on user activity within that Spoke. Since different Spokes can have different risk profiles and user bases, this allows the system to account for the overall risk environment within each Spoke.

## Risk Premiums Across Spokes

Different Spokes in Aave V4 can implement their own Risk Premium configurations, allowing for specialized risk management approaches.

EMode Spokes, which focus on assets that tend to move together in price like liquid staking tokens, can use custom Risk Premium settings that reflect the lower risk of these asset relationships. Proven tokens like stETH get the lowest premiums and best rates. Newer restaking tokens with more risk get higher premiums. This way, users with stronger collateral get better terms, even within similar asset types.

RWA Spokes that support real-world assets as collateral can apply Risk Premium configurations that account for the unique characteristics of these assets. Tokenized treasury bills might receive favorable Risk Premium treatment due to their stability, while other real-world assets might have premiums that reflect their liquidity constraints.

This flexibility allows each Spoke to optimize its Risk Premium approach for its specific use case while maintaining the overall benefits of the unified liquidity in Aave V4.

## Benefits of Risk Premiums

Risk Premiums introduce several important improvements to DeFi lending that benefit both users and the broader ecosystem.

Users with high-quality collateral get rewarded with better borrowing rates. This creates an incentive to provide better collateral to the protocol, which improves overall system stability. Instead of paying extra to cover the costs of riskier borrowers, users with ETH and other top-tier assets can access the most competitive rates available. And suppliers now earn returns that match the risk of the collateral behind each borrow, making the market more balanced for both sides.

The protocol can now properly price risk across different asset types and user profiles. Newer tokens can be supported with appropriate risk premiums, while established assets maintain their preferential treatment. This creates a more efficient market where rates better reflect actual risk levels.

Risk Premiums also enable innovation in specialized markets. Different Spokes can implement custom risk approaches that would be difficult to achieve in a one-size-fits-all system. This opens the door for new types of lending markets while maintaining the benefits of shared liquidity.

By properly pricing risk and rewarding quality collateral, Risk Premiums allow Aave V4 to support significantly more diverse use cases while maintaining the stability and efficiency that users expect from a leading DeFi protocol. This system also creates a sustainable revenue model for the Aave DAO, as higher risk premiums directly translate to increased protocol fees.
