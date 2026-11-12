# 🛡️ Move Smart Contract Audit Checklist

- **Source URL:** https://hacken.io/discover/move-smart-contract-audit-checklist
- **Fetched:** 2026-11-12
- **Channel:** @defendor_eng
- **Telegram message:** https://t.me/defendor_eng/1114 (id 1114)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
Move is now used across multiple chains – including Sui, Aptos, and IOTA – and while they share the same language, they don’t share the same assumptions. Their architectures differ (object-centric execution vs. optimistic concurrency vs. hybrid DAG ledger), so the audit surface shifts with the platform.

This guide breaks down the essential checklist for auditing Move [<u>smart contracts</u>](https://hacken.io/discover/what-are-smart-contracts/), covering general best practices, logical pitfalls, and chain-specific nuances.

What you’ll get out of this post:

- A quick mental model for how Sui, Aptos, and IOTA differ in ways that affect audits
- A Move audit baseline (abilities, access control, inputs, dependencies, errors)
- A shortlist of Move-specific logical pitfalls (ownership, capabilities, integer division, atomicity)
- Chain-specific add-ons for Aptos, Sui, and IOTA

## Know The Chain You’re Auditing

You can’t audit Move in a vacuum. The same pattern can be safe on one chain and exploitable on another because of how storage, ownership, and transaction inputs work.

### Sui

Sui relies on Narwhal-Tusk DAG consensus with an object-centric architecture where transactions can run in parallel when they touch different objects, and assets are modeled as programmable objects with distinct identifiers.

**Audit implication:** treat every shared or immutable object input as attacker-controlled. Ownership checks must be explicit (more on that below).

### Aptos

Aptos uses an optimistic parallel execution engine (Block-STM) and a MoveVM with Aptos-specific features like governance-driven module upgradeability and formal verification support.

**Audit implication**: pay extra attention to borrow\_global\<T> / borrow\_global\_mut\<T> flows and ensure borrowing happens from the intended account/object address (not a user-controlled address).

### IOTA

IOTA combines a DPoS blockchain with the Tangle DAG, supports MoveVM for L1 contracts, and has EVM compatibility via L2.

**Audit implication:** model economic + state effects: storage deposits/refunds and “many calls in one transaction” batching can break assumptions about “one action per tx.”

## General Security Best Practices

Security starts with the basics. Before diving into complex logic, you must ensure the fundamental building blocks of your Move modules are sound.

### Use Move Abilities Correctly

1. Use *key* only for global storage–type assets (pools, vaults).
2. Use *store* only when global persistence is actually needed.
3. Avoid *drop* for critical assets (tokens, staking pools).

### Lock Down Access Control (Including Object Ownership)

1. Restrict balance/config-modifying functions to admin/governance.
2. Put extra friction on privileged actions (multi-sig or time delays).
3. Move platforms that use objects (Aptos and SUI), and verify that the transaction sender owns any resource or object being acted upon. Every Object\<T> can potentially be passed to a function by anyone, so the code must validate that object::owner(&obj) equals the caller’s address (or other expected owner).
4. Audit *friend* usage: only trusted modules should be granted *friend* access. Ensure any declared friend modules are trustworthy. Verify all *public(friend)* functions to prevent exposure of critical functionality to untrusted code.
5. Always verify the signer/caller is the expected account before state changes.
6. Explicitly verify ownership for resources or objects passed as arguments to prevent unauthorized access or manipulation.

**Code snippet (ownership validation pattern):**

Access control vulnerabilities were responsible for [<u>58% of all losses in 2025</u>](https://hacken.io/insights/2025-security-report/), making these the top priority for any audit.

### Avoid Hardcoded Addresses And Constants

1. No hardcoded admin addresses; use capability-based access control.
2. Make governance addresses updateable when needed.

### Secure External Calls And Dependencies

1. Validate return values from *option, vector, object*, and cryptographic functions.
2. Pin external dependencies; avoid “latest” or testnet revisions.

### Use Secure Error Handling

1. Use specific error codes for different failure cases.
2. Implement fail-safe behavior for critical errors.

### Validate Inputs And Types

1. If a function expects a specific generic type T, assert it matches what you intend (for example via *TypeInfo*).
2. Treat all external input as potentially malicious; validate lengths/counts and ensure addresses/references point to the correct resources.
3. Validate numeric inputs (e.g., lengths, counts) are within safe ranges, and that addresses or references point to the correct kinds of resources before use.

## Move-Specific Logical Vulnerabilities

These issues are “Move-shaped”: they show up because of Move’s semantics and common ecosystem patterns.

### Integer Overflow And Underflow Checks

1. Use checked arithmetic where needed.

### Treat Integer Division As A Footgun

1. Move division truncates (rounds down). That can turn fees/interest into zero or cause systematic value loss if you don’t account for precision.
2. Explicitly handle negative divisions if they are possible inputs, and ensure calculations like fee percentages or interest rates don't inadvertently truncate to zero or yield unexpected negative results.

### Keep Critical Flows Atomic

1. If a state transition needs multiple steps, keep it in a single transaction to avoid inconsistent intermediate states.

### Prevent Capability Leakage

1. Capabilities (e.g., WithdrawCapability or ConstructorRef) should remain internal. Make sure no function exposes them outside the intended trust boundary.

### Validate Loan And Yield Math

1. Validate APR/APY formulas to prevent negative yield outcomes or broken accounting.

### Audit **drop** Paths Like Burns

1. Ensure no code path “drops” or forgets assets unless it’s an intended burn mechanic.
2. While Move’s architecture mitigates some [<u>legacy</u>](https://www.researchgate.net/publication/399142425_Understanding_MoveVM_and_Its_Role_in_Blockchain_Scalability) issues, it is still vital to understand the broader landscape. For a comparison with standard EVM pitfalls, check our guide on the [<u>Top 10 Smart Contract Vulnerabilities</u>](https://hacken.io/discover/smart-contract-vulnerabilities/).

## Storage And Gas Checks That Prevent DoS

A lot of issues labeled as ‘security’ problems are really design flaws that lead to high gas costs for users, rather than attacks by a malicious party.

1. Optimize storage (efficient vectors; batch processing).
2. Prevent gas exhaustion: avoid unbounded loops; make reward/staking logic gas-efficient.
3. Cap vector sizes (example: limit stored orders in an order book).

For example, [<u>order books</u>](https://hacken.io/insights/order-book-security-vulnerabilities/) often face specific gas pitfalls related to batching and matching logic. And here are our [<u>Solidity gas optimization tips</u>](https://hacken.io/discover/solidity-gas-optimization/).

## Chain-Specific Add-Ons

Once the baseline checks are done, switch to chain-mode.

### Sui Smart Contract Security Audit Checklist

**Object ownership and transfers**

- Owned objects require the owner’s signer; shared objects are globally accessible by reference.
- If a struct should never be globally shareable, it likely shouldn’t have *store* (prefer *key* only).
- If a struct has both *key* and *store*, it can be nested/transferred/frozen in ways you may not intend.
- Objects with *store* can be frozen (immutable, no owner) and then used by anyone as an immutable input – ensure users can’t freeze what must remain mutable.
- Review transfer module usage and custom transfer logic; ensure *transfer::public\_transfer* doesn’t bypass checks.

**Object abilities and types**

- Any struct with key must have an *id: UID* field; don’t add *key + UID* to structs that don’t need to be on-chain objects.

**Dynamic fields**

- If using *dynamic\_field*, ensure keys are deterministic/unique enough to avoid collisions.
- If a parent object may be deleted, make sure dynamic children are transferred out or deleted too.

**Coin type handling**

- When merging coins via *join*, ensure the “merged-in” coin is actually destroyed; if manual destruction exists, verify total sum preservation.
- If the contract holds coins inside another object (e.g., a Vault object contains a Coin\<T> field), transferring the parent object will also transfer the coin ownership.
- Ensure there’s no accidental/unnecessary global access to *TreasuryCap\<T>*.
- Trace complex flows where objects hold multiple coin types or nested coins.

### Aptos Smart Contract Security Audit Checklist

1. **Resource grouping**: if multiple resources are stored under the same account and belong to the same resource group, transferring one may unintentionally transfer others.
2. **Constructor references**: never leak *ConstructorRef* (it can enable adding child resources or obtaining transfer capabilities).
3. **Coin registration**: ensure recipient accounts are registered to hold the coin type (*CoinStore\<Token>* must exist before deposits/withdrawals).
4. **Borrow checks**: for *borrow\_global\<T> / borrow\_global\_mut\<T>*, confirm the signer matches the owner or the object was explicitly shared.
5. **Aptos vs. Sui storage assumptions**: Sui requires objects to be passed as inputs, while Aptos can borrow globals if the type is accessible – so verify borrowing happens from the correct intended address.

### IOTA Smart Contract Security Audit Checklist

**Storage deposit**

- Creating/holding on-chain data locks a storage deposit; ensure the transaction includes enough tokens to cover it and that refunds are handled on object destruction.

**Batching**

- IOTA MoveVM supports calling many Move functions in one atomic batch; ensure no combination of calls breaks invariants (e.g., repeating withdraw many times in one transaction).
- If your protocol assumes “one-at-a-time” actions (one loan at once per user), batching can violate that assumption unless you enforce it.
- Watch “micro transaction” behavior that can produce dust-level accounting issues.
- If *call1* and *call2* in the batch are meant to be independent, ensure that *call1* commit doesn’t unexpectedly enable *call2* to do something.

## Conclusion

Securing Move smart contracts requires more than just checking for standard bugs; it requires understanding the specific architecture of the chain you are deploying on. From SUI’s object inputs to IOTA’s batch execution, the context matters.

While this checklist is a powerful starting point, it doesn't replace a comprehensive review. For protocols handling significant value, [<u>professional smart contract audit services</u>](https://hacken.io/services/blockchain-security/smart-contract-security-audit/) are the industry standard to ensure every edge case is covered.
