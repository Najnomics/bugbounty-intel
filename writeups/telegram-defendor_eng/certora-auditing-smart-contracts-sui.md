# Auditing Smart Contracts on Sui: Key Security Risks & Findings

- **Source URL:** https://www.certora.com/blog/auditing-smart-contracts-sui
- **Fetched:** 2026-11-14
- **Channel:** @defendor_eng
- **Telegram message:** https://t.me/defendor_eng/2340 (id 2340)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---

[← Blog](/blog)

# Auditing Smart Contracts on Sui

Key security considerations for Sui developers, with real findings from Certora’s audits and formal verification work.

Author:

[Tigran Piliposyan](/author/tigran-piliposyan)

Sui uses an object-centric model in which assets and application state are represented by objects. Move defines how these objects can be created, transferred, and modified, while Sui's transaction model determines how they are accessed and updated.

These properties shape how Sui applications should be reviewed. An audit needs to examine which objects a function accepts, who can access or modify them, how permissions are enforced, and whether relationships between objects remain valid across transactions. The review must also consider application-level logic, including accounting, oracle handling, and interactions with other protocols.

**In short:** A Sui audit starts with the object model and follows the application's state transitions. Object ownership and Move's type system provide important safety guarantees, but they do not establish that application logic is correct. Authorization, capability handling, accounting, and cross-contract assumptions still need to be reviewed against the protocol's requirements.

## How does Sui's object model affect security?

Sui programs are written in Move, but their state model differs from the storage model used by the Ethereum Virtual Machine (EVM). Rather than storing application state in a contract's own storage, Sui represents assets and application data as objects with unique IDs, types, owners, and versions. Transactions take objects as inputs and produce updated or newly created objects as outputs. The [Sui object model documentation](https://docs.sui.io/develop/sui-architecture/object-model) explains these mechanics.

Ownership determines how an object can be used. Address-owned objects are controlled by a specific address. Shared objects can be accessed by transactions from different addresses, subject to the rules implemented by the Move package. Immutable objects cannot be modified. Objects can also be wrapped inside other objects, making their access dependent on the containing object.

These distinctions affect the security assumptions of an application. A shared liquidity pool, for example, can be passed to a transaction by any caller. The fact that the caller can reference the pool does not mean they are authorized to perform every operation on it. The Move function must enforce any additional permissions required for the operation.

An audit should follow important objects through their lifecycle: creation, initialization, transfer, mutation, wrapping, and destruction. It should also check whether every operation receives objects that belong to the intended protocol, user, market, or position.

## How should authorization and capabilities be audited on Sui?

Sui's ownership model provides important protections, but protocols often need permissions beyond ordinary object ownership. Administrative actions, minting, pausing, upgrades, and access to a user's position may require additional authorization.

Move applications commonly represent these permissions using capability objects. A function can require a particular capability as an argument, making possession of that object part of the authorization model. This is often preferable to relying only on the transaction sender, especially when an operation must be authorized for a specific market or position.

The critical question is whether the capability authorizes the operation that receives it. A capability may be valid in isolation but associated with a different object than the one being modified. If a protocol accepts a capability without checking that relationship, it can enforce the wrong permission.

An audit should establish what each capability authorizes, which object or resource it governs, and whether that association is preserved whenever the capability is transferred, borrowed, wrapped, or returned.

The [Sui Move best practices](https://docs.sui.io/develop/write-move/move-best-practices) recommend explicit capabilities for privileged functions and checking the relationship between a capability and the object it governs.

## What does Move's type system guarantee, and what does it leave to the application?

Move's type system and resource model prevent several classes of mistakes. Values cannot be copied or discarded arbitrarily when their types do not permit those operations, and the language enforces rules around resource handling. Sui's object model also makes ownership explicit.

These guarantees do not establish that the program's business logic is correct.

For example, a generic function may accept a pool parameterized by a particular coin type and also accept a separate asset index or configuration value. The type system can ensure that the pool contains the expected coin type, but it does not automatically ensure that the asset index refers to that same asset. If the function uses the index for accounting and the pool for transferring funds, a mismatch can cause the protocol to account for one asset while moving another.

The same principle applies to public functions. A function being callable from another module or package does not mean it should be available without additional authorization. An audit should review visibility modifiers such as `public` and `public(package)`, check which functions can mutate sensitive state, and establish whether their callers are intended to have that access.

Move's explicit references also deserve attention. When working with mutable references, assigning a reference is not the same as assigning the value it points to. Confusing these operations can cause a function to update the wrong field while still compiling and executing. This is especially important in accounting and authorization code, where a small state-update error can change future protocol behavior.

The review should therefore cover both language-level safety and application-level correctness. The former constrains how code can behave; the latter determines whether that behavior matches the protocol's requirements.

## How should shared objects and transaction composition be reviewed?

Sui supports Programmable Transaction Blocks (PTBs), which allow multiple operations to be composed into a single transaction. Objects produced by one operation can be used by later operations in that transaction. This makes it possible to combine protocol actions without requiring a separate transaction for every step.

The audit needs to consider the complete sequence, not just each function in isolation. A receipt may be created by one function and consumed by another. A coin may be split, passed into a protocol operation, and merged with another balance. A capability may be borrowed temporarily and returned later. The security property depends on the relationships preserved throughout that sequence.

Consider a flash loan or another operation that requires a receipt to be returned before the transaction completes. A receipt can enforce that a required step occurs, but it does not automatically prove that the step was performed against the correct pool, position, or asset. If the receipt does not bind the operation to the original object, a caller may satisfy the structural requirement while violating the intended economic condition.

Shared objects introduce another consideration. Because multiple callers can reference them, their entry points must enforce the intended authorization and state-transition rules. The review should identify which functions can change shared state, which objects they depend on, and whether every valid transaction sequence preserves the protocol's assumptions.

The [Sui documentation on Programmable Transaction Blocks](https://docs.sui.io/develop/transactions/prog-txn-blocks) and [object ownership](https://docs.sui.io/develop/objects/object-ownership) describe the relevant execution model.

## How can rounding and accounting bugs affect Sui protocols?

Move's arithmetic rules do not remove the need to verify economic calculations. Lending protocols, vaults, and staking systems maintain relationships between underlying assets, shares, debt, collateral, fees, and exchange rates. Those relationships must remain valid after every supported operation.

A function can use valid integer arithmetic and still produce an incorrect economic result. Rounding direction, intermediate precision, and the order of calculations can affect how much value is credited, debited, or represented by shares.

For example, calculating an exchange ratio and then using that rounded ratio to calculate shares can produce a different result from calculating the share amount with a single multiplication and division. Repeated rounding can also cause stored aggregates to diverge from values recomputed from the underlying position.

An audit should examine the complete accounting flow rather than treating each calculation in isolation. It should check whether share issuance and redemption preserve the relationship with underlying assets, whether debt and collateral values are updated consistently, and whether rounding can create unbacked claims or allow an unhealthy position to pass a safety check.

For lending protocols, this includes collateral valuation, borrowing limits, interest accrual, liquidation thresholds, repayment, and the effect of rounding on small positions. For vaults and staking systems, it includes share issuance and redemption, fees, and the consistency of liabilities with available assets.

## What should an audit check about oracle data?

Oracle-dependent applications must establish that the price used for an operation is valid for that operation. This includes checking freshness, handling invalid or missing data, and ensuring that changes to the configured feed are reflected in the price actually used by the protocol.

Checking a timestamp or validating a feed address is not sufficient on its own. The audit should trace how the price is obtained, validated, stored, refreshed, and consumed by deposits, borrows, withdrawals, and liquidations.

It should also check what happens when an update fails or the data is outside the accepted range. A protocol must not silently use an invalid price, and it should not become permanently unable to perform an otherwise valid operation because its update path cannot recover from stale data.

Configuration changes need particular attention. Updating an oracle address does not necessarily update a cached price or its timestamp. The implementation must ensure that subsequent operations use data from the intended feed and that old values cannot remain valid after the configuration changes.

## What can go wrong in cross-chain protocols built on Sui?

A bridge must preserve the meaning of a message as it moves between chains. That includes the message contents, signatures, nonces, validator permissions, and the conditions under which a transfer or governance action can execute.

The review needs to consider both sides of the bridge. Each implementation may enforce its own rules correctly in isolation, while the combined behavior remains inconsistent. For example, the chains may differ in how they handle blocklisted validators, signature thresholds, message formats, or replay protection.

An audit should trace a message from creation through signature collection, verification, execution, and final asset transfer. It should check that both sides agree on what has been authorized and that a failure at any stage cannot result in duplicate execution, unauthorized transfers, or permanently stuck funds.

## How should package upgrades and privileged configuration be reviewed on Sui?

Published Sui packages are immutable, but a package can be upgraded through Sui's upgrade mechanism when the required authority and policy permit it. The UpgradeCap controls the ability to publish a newer package version, subject to the applicable upgrade policy.

This makes upgrade authority part of the protocol's trust model. An audit should establish who controls the capability, which upgrades are permitted, and whether the upgrade policy provides the guarantees users expect. It should also examine privileged configuration changes, including changes to oracle feeds, risk parameters, supported assets, fees, and pause controls.

Configuration changes can alter the meaning of otherwise valid state. Changing risk parameters can affect existing positions, including their borrowing capacity and liquidation conditions. Changing an oracle feed can also affect how assets are valued.

The review should ask whether an authorized administrator can make a change, whether that change preserves the protocol's safety properties, and how its effects are communicated and monitored.

See the [Sui package upgrade documentation](https://docs.sui.io/develop/upgrade) for the platform's upgrade model.

## What did Certora identify in its review of Suilend?

Suilend is a lending protocol built on Sui. Its application logic manages shared reserves, cTokens, collateral, debt, oracle prices, and liquidations. These operations introduce application-specific security requirements that are not guaranteed by Sui's object model or Move's type system.

During Certora's formal verification of Suilend's Move contracts, the review examined capability handling, share accounting, obligation health calculations, liquidation logic, and oracle updates. The review identified several cases where the implementation needed changes, as well as scenarios that required assessment in the context of Suilend's system design and operational setup.

The Suilend team proactively engaged with Certora throughout the formal verification process and worked closely with our researchers to address the findings. The team promptly implemented fixes for the issues identified in share accounting, obligation health calculations, and oracle handling. Other scenarios, involving capability handling and liquidation thresholds, were discussed in detail with the Suilend team. They provided additional context about their system design and operational setup, demonstrating why these scenarios did not pose a material risk to their deployment. Following these discussions, Certora and Suilend agreed that no code changes were necessary for these cases. See the [Suilend verification report](https://www.certora.com/reports/suilend).

**cToken over-minting due to double rounding.** The deposit calculation first computed an exchange ratio using truncated decimal precision, then used that ratio to calculate the number of cTokens to mint. Rounding down the intermediate ratio could result in slightly more cTokens being minted than the deposit warranted, diluting existing holders. The implementation was changed to calculate the minted amount with a single multiplication and division, followed by one rounding step.

**Obligation health aggregates could drift.** State-changing operations updated an obligation's health aggregates incrementally. Because the calculations used rounded arithmetic, those updates could diverge from recomputing the aggregates from the final position state. An obligation could appear healthy immediately after a borrow or withdrawal, while a later refresh revealed that it was unhealthy. The implementation was changed to calculate the aggregates from the updated obligation state.

**Oracle timestamps in the future could bypass stale-price checks.** The staleness check did not reject a price with a timestamp significantly ahead of the on-chain clock. A compromised or malfunctioning oracle could therefore publish a price that remained usable longer than intended. The implementation was updated to reject timestamps that are too far in the future.

**Changing a price feed could leave the previous reserve price in use.** Updating a reserve's oracle changed the configured price identifier but left cached price data from the previous feed in state. This could allow an operation to use a stale price after the feed had changed. The implementation was updated to refresh the price when the feed is changed.

These examples illustrate application-level risks that can arise in DeFi protocols built on Sui. They concern how a protocol associates permissions with objects, calculates balances, maintains derived accounting values, and consumes oracle data. They do not indicate a weakness in Sui's object model or Move's resource system.

## What did the Sui Bridge review examine?

The Sui Bridge connects Sui and Ethereum. Its security depends on both sides applying consistent rules when verifying messages and validator signatures.

The review examined how the two implementations handle blocklisted validators. On the Sui side, signatures from blocklisted validators were excluded when calculating the approval threshold, but the full signature array was still stored. On the Ethereum side, signatures from blocklisted validators were rejected during verification.

This difference in handling was identified during the review. It highlights the need to ensure that both sides of a bridge apply compatible validation rules throughout the message lifecycle.

See the [Sui Bridge security assessment](https://www.certora.com/reports/sui-bridge) for the review details.

## Which invariants matter for Sui applications?

An invariant is a property that must remain true across every valid state transition. The relevant properties depend on the protocol, but they should describe its authorization and economic requirements rather than merely restating what individual functions do.

For a lending protocol, an obligation must remain associated with the correct owner and market. Borrowing and withdrawal operations must preserve collateral and solvency requirements. Liquidations must reduce or otherwise correctly account for debt and collateral, and rounding must not create unbacked claims.

For a vault, the value of outstanding shares must remain consistent with the assets backing them, within defined rounding bounds. For a bridge, every executed message must satisfy the required authorization and replay protections, and the same message must not be processed inconsistently across chains.

For protocols using capabilities or receipts, the capability must authorize the intended object and operation. Returning a receipt or consuming a resource must not allow a caller to substitute an unrelated object and bypass the original requirement.

These properties should be checked across sequences of operations, including edge cases and state transitions that are easy to overlook in unit tests. A property that holds after a deposit but fails after a withdrawal, liquidation, refresh, or configuration change is not preserved by the protocol.

## How should Sui programs be tested and formally verified?

Tests should cover successful operations as well as invalid objects, unauthorized callers, mismatched asset types, stale oracle data, boundary values, and sequences that change state over time. For lending protocols, tests should include deposits, borrows, repayments, withdrawals, liquidations, and refresh operations in different orders. For receipt-based flows, they should test whether a receipt can be returned with a capability or object different from the one originally supplied.

Formal verification can establish that specified properties hold for the modeled implementation under the assumptions of the verification. It is particularly useful for accounting invariants, authorization conditions, and state transitions that are difficult to cover exhaustively with tests.

The guarantees depend on the properties specified and the code and assumptions included in the verification scope. A proof of one accounting property does not establish that authorization, oracle handling, upgrade governance, and cross-chain execution are all correct. The specification must cover the properties that matter to the protocol.

## What should a team building on Sui prepare before an audit?

Before an audit, a team should document the intended ownership and authorization model, the capabilities required for privileged operations, and the relationships between the objects used by each important function. It should also define the protocol's economic invariants, supported asset types, oracle update behavior, and package upgrade policy.

For systems that use receipts or temporary capabilities, the documentation should explain what each receipt proves and which object or operation it must be tied to. For cross-chain protocols, it should describe how messages are authorized, replay-protected, and processed on each chain.

These details give the audit a clear baseline for checking whether the implementation matches the protocol's intended behavior.

## Further reading

## Frequently asked questions

### What is a Sui smart contract audit?

A Sui audit reviews Move packages, the objects they operate on, the authorization they enforce, and the state transitions they permit. For DeFi protocols, the audit also checks accounting, oracle handling, and the properties that must hold across deposits, borrows, withdrawals, liquidations, and other operations.

### How does auditing Sui differ from auditing EVM contracts?

Sui uses an object-centric model in which transactions explicitly operate on objects, and Move defines how those objects can be used. The audit therefore pays particular attention to object ownership, capabilities, object relationships, and the composition of operations within transactions.

### Does Move eliminate smart contract vulnerabilities?

No. Move's type system and resource model prevent certain classes of errors, but they do not guarantee that application logic is correct. Authorization gaps, mismatched object relationships, accounting errors, stale oracle data, and incorrect cross-chain assumptions can still create vulnerabilities in applications built on Sui.

### Does Certora audit Sui Move contracts?

Yes. Certora has reviewed and formally verified Sui Move contracts, including the Suilend lending protocol and the Sui Bridge. The published reports describe the scope, verification work, and findings for each engagement. Its public reports are available on the [Certora reports page](https://www.certora.com/reports).
