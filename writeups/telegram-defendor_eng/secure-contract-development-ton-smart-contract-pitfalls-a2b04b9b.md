# 🛡️ Secure Smart Contract Development in TON: 9 Major Mistakes

- **Source URL:** https://cantina.xyz/blog/secure-contract-development-ton-smart-contract-pitfalls
- **Fetched from:** https://web.archive.org/web/20260711145236/https://cantina.xyz/blog/secure-contract-development-ton-smart-contract-pitfalls
- **Fetched:** 2026-11-26
- **Channel:** @defendor_eng
- **Telegram message:** https://t.me/defendor_eng/394 (id 394)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
## Introduction

As of July 2025, Tact remains a first-class smart contract language within [The Open Network](https://web.archive.org/web/20260711145236/https://ton.org/) (TON) ecosystem. With more than 28,000 contracts deployed and about a third written in Tact, the language has gained momentum for its expressiveness, safety-focused design, and formal type system.

[Tact](https://web.archive.org/web/20260711145236/https://docs.ton.org/v3/documentation/smart-contracts/tact) offers developers a modernized experience that simplifies smart contract creation. It features static typing, intuitive syntax, and an expanding set of developer tools. Visual Studio Code integration now includes syntax highlighting, diagnostics, code completion, and templated scaffolding, allowing for robust workflows.

These capabilities are backed by a maturing ecosystem. The Tact language, compiler, and standard libraries have undergone formal assessments, and a growing number of security reviews are scoped specifically to Tact-based codebases. TON Studio’s investment in security and documentation continues to support this trajectory.

This article outlines common pitfalls and implementation issues observed in contract reviews and security assessments across the TON ecosystem, offering examples and strategic guidance for developers building in Tact today.

### 1. Smart Contract Lifecycle in TON

Unlike Ethereum, TON enforces decentralized, parallel transaction execution. Contract communication is inherently asynchronous, and developers must treat each message as an isolated computation unit.

This has several implications:

- **No shared global state** between messages.
- **Partial execution** is common; some actions may succeed while others silently fail.
- **Gas management** is the responsibility of the contract, not the protocol.

### 2. Bounced Message Processing and Balance Recovery

In TON, when a contract tries to send a message with value (TON coins) and that message fails to reach the recipient, the value is not simply lost — it's bounced back to the sender contract.

This bounced message comes with a special flag and can be handled using an onBounce handler. Below is a canonical bounce handler in Tact:

This protects against jetton loss when a transfer fails and refunds the sender’s balance.

### 3. Type-Safe Struct Design and Serialization Pitfalls

Tact's serialization system is powerful, but it can easily break if you're not explicit about types.

By default, Int serializes as a 257-bit signed integer, which may cause deserialization errors if the receiver expects uint256. For any public-facing or standard-compliant reply, explicit typing is required.

### 4. Gas Accounting with Defensive Defaults

Without strict gas control, contract logic may partially execute, leading to inconsistent state and lost funds.

The following example outlines a common deposit handler:

**Key highlights:**

1. **Gas Precheck:** The contract uses printTransactionFees() to dynamically assess required gas before proceeding.
2. **Carry-Value Forwarding:** Excess gas is forwarded to the sender, preventing silent fund loss or storage bloat.
3. **Safe State Update:** self.balance is only updated after the gas requirement is satisfied, ensuring transactional integrity.

### 5. State Management via Nested Storage Blocks

Flattened storage leads to bloated load\_data() statements and gas inefficiencies. Instead, use nested records to isolate logical blocks:

### 6. Message Race Conditions and Value-Carry Design

Unlike the EVM, TON contracts operate in a fully asynchronous execution model. Message order is non-deterministic. You cannot assume that messages will be handled in the order they were sent.

This requires developers to avoid relying on stored state to pass context between messages. State can be overwritten or misaligned, especially when multiple messages are processed in parallel.

Safer design uses carry-value:

**Consequence:**

If multiple TransferNotification messages are received in close succession, the stored received\_jetton\_amount may be overwritten before the next action executes. This opens the door to logic errors, double-spending, or value misattribution.

**Key takeaways:**

- Never rely on global state to persist user-specific context between asynchronous messages.
- Always carry critical values within the message payload itself.
- Design every message handler to be self-contained and stateless wherever possible.

The carry-value pattern ensures correctness and avoids cross-message interference. Assume any state read could be outdated by the time the next message arrives.

### 7. End-to-End Example: Tact Jetton Transfer Handler

A reliable transfer handler forms the backbone of Jetton-compatible contracts in production. This is a safe, reusable baseline pattern you can depend on when building Tact applications at scale.

This approach limits attacker control and preserves expected balances even under failure.

### 8. Developer Guidance: From Prototyping to Production

Tact improves developer ergonomics, but unsafe assumptions carry over from Solidity and FunC:

- Avoid unchecked int/uint serialization.
- Don’t trust message order.
- Always use explicit gas estimation.
- Prefer carry-value and message-bound payloads.
- Don’t assume Excesses messages will arrive.

Use test environments like @ton/sandbox and include gas-printing tools in dev flows.

### 9. Leverage Tooling to Enforce Correctness

Use the VS Code plugin for syntax validation, @ton/sandbox for flow simulation, and printTransactionFees() for gas planning. Tact now powers \~33% of deployed contracts on TON.


### Conclusion

TON’s parallel execution architecture unlocks performance and composability but demands disciplined smart contract engineering. Language abstractions like Tact help with clarity, but correctness depends on a deep understanding of message isolation, failure recovery, and gas-aware design.

Spearbit’s engagement model enables organizations building on TON to validate flows, harden state management, and enforce safe communication patterns across contract clusters.

[Contact us](https://web.archive.org/web/20260711145236/https://cantina.xyz/solutions/spearbit) to scope a review and build resilient infrastructure on TON.
