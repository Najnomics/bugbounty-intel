# 🔒 Silent Protocol: Solving the State Denial Problem in Web3

- **Source URL:** https://threesigma.xyz/blog/infrastructure/silent-protocol-state-denial-web3-privacy
- **Fetched:** 2026-11-16
- **Channel:** @defendor_eng
- **Telegram message:** https://t.me/defendor_eng/919 (id 919)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
## Introduction

Every day’s blockchains are not anonymous, but pseudonymous. Your real identity doesn’t appear, but all your actions are linked to addresses that anyone can correlate with usage patterns, schedules, counterparties and metadata to see all your movements, know what you do or know how much money you have.

Keeping the user's state exposed solves transparency, verifiability, and composability but at the cost of the user's privacy.

On the other hand, some chains offer strong anonymity at the user or state level by using zero-knowledge proofs to update application state without revealing data (e.g. Aleo, Mina) or by encrypting contract execution and state inside TEEs (e.g. Secret Network). There, privacy is real, but composability often suffers because hiding application state deprives other programs of the shared view they need, leading to state denial.

In short, encrypting application state causes state denial.

To remedy this, there are two different approaches; batching flows and splitting flows. With these solutions, instead of locking user state, messages are passed to the target contract and executed in an async manner to keep user data private.

Let’s dig a little bit more into these two concepts.

## Batching Flows

In batching flows, the user proves eligibility to claim the result of a specific action and sends an unencrypted instruction to the target contract, allowing users to keep private data offchain. The contract gathers many such messages and updates its state in a batch and issues a temporary artifact for each user's intent, (e.g. a token or NFT) that only the owner can burn. Once the batch settles, each participant redeems a pro rata output using their claim proof (the artifact). This approach introduces latency because a batch needs multiple users, or repeated calls to the same function before it can run, so users have to choose between time and privacy.

However, there is a more important problem: that this also fragments the application into per-function subspaces, so flows stay confined to their bridge or function context and horizontal composability with other functions and contracts weakens.

## Splitting Flows

Splitting flows keeps sensitive data off chain and breaks a transaction into independent intents that execute asynchronously. Each intent sends a message to the target contract, which runs publicly like any normal call. When an intent settles, an anonymous access channel appends the resulting outputs to the user’s primary account state. With this approach, the application keeps a shared and readable state for composability, and the user preserves privacy over identity and balances.

This is the path that Silent Protocol follows to solve the state denial problem and bring Web3 strong privacy.

Silent Protocol works as a privacy co-processor for transparent chains and enables privacy-preserving transactions on smart contracts without modifying those. This is possible thanks to its renode network for threshold-based anonymous verification and EZEE Signals (Economical Zero-Knowledge Execution Environment) to move intents between the primary account (private) and secondary accounts (public).

Their solution is based on two components, the Ghost Layer and EZEE signals.

Ghost Layer serves as the encryption layer and behaves like a “Layer 1.5,” executing privacy logic and anchoring security and validity to the underlying L1, while EZEE Signals open anonymous access channels from Ghost Layer to secondary accounts, which interact with end contracts (0dapps) in the public execution layer, bringing strong privacy and allowing composability.

In short, messages fan out across secondary accounts, run in public, and return via EZEE Signals to be appended in Ghost Layer to the user’s primary account.

## Conclusion

State denial appears when the network can’t access an application’s state. Silent avoids that outcome by leaving execution on the public side, with this approach contracts remain unchanged, emit events, and update storage in the open, so routers, oracles, liquidators, and other smart contracts keep reading the same shared view and can compose freely.

Privacy moves to the user side instead of living inside the application. Ghost Layer holds balances and sensitive information in private while user transactions are split across secondary accounts which call target contracts as ordinary EOAs. In that way, results settle in public and EZEE Signals append those outputs back to the user’s primary account in Ghost Layer.

By moving privacy to the user side, Silent preserves the shared state that DeFi needs, allowing privacy, verifiability and composability to coexist.
