# 🔬 Certora Finds Critical Bug in Solana's $8.45B Stake Pool via Formal Verification

- **Source URL:** https://www.certora.com/blog/formal-verification-solana-stake-pool
- **Fetched:** 2026-11-12
- **Channel:** @defendor_eng
- **Telegram message:** https://t.me/defendor_eng/1862 (id 1862)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
[← Engineers' Hub](https://www.certora.com/blog/engineers-hub)

# How Formal Verification Strengthened Solana’s Most Battle-Tested Staking Protocol

Manual review + formal methods allowed Certora to surface a number of issues that had not previously been identified.

Author:

[Nisarg Patel](https://www.certora.com/author/nisarg)

The [SPL Stake Pool program](https://www.solana-program.com/docs/stake-pool) has been live for nearly five years and today helps manage roughly $8.45 billion worth of staked SOL across the largest Solana stake pools. Its complexity and on-chain interactivity make it one of the most challenging Solana programs to reason about formally. In June 2025, Certora conducted a manual audit and [formal verification](https://www.certora.com/blog/what-is-formal-verification) of the Solana Stake Pool program.

**Combining manual review with formal methods** allowed the team to go deeper than traditional audits alone, s**urfacing a number of issues that had not previously been identified.** The formal verification effort also led to the formulation of 11 invariants that now define the safety boundaries of the protocol. **The Solana Stake Pool team responded quickly, remediating all critical issues and implementing fixes promptly.**

## **Solana Stake Pool Program**

At its core, the Stake Pool aggregates users’ SOL, delegates it across validators, and distributes staking rewards.

Its apparent simplicity hides significant complexity:

- It must interact directly with the **Solana Stake Program**, handling validator and transient stake accounts outside its full control. This includes a *reserve* stake account that the pool uses for the purposes of deposit and withdraw of staked SOL.
- These accounts can change state due to cluster restarts, rewards accumulation, or even hijacking (where a malicious attacker can reinitialize or repurpose an uninitialized account).

In order to treat all such events correctly, the pool performs detailed internal accounting to keep track of the reserve and validator stake accounts. The internal accounting tracks not only balances, but also the statuses of validators’ stake, that is, whether a stake is activating or deactivating, whether it is ready for removal, etc. The validator stake account’s status determines how much of its balance is actually staked. This delicate interplay between virtual accounting (the pool’s internal records) and physical accounting (actual lamports on-chain) is precisely why proving correctness of the Stake Pool is challenging.

## **How invariants demystify a complex system**

Formal verification helps demystify a complicated system like the Stake Pool Program using *invariants*. Invariants are mathematical properties about the state that must hold under every possible sequence of protocol operations, that is any state that is reachable by some computation, the invariant must be true.

One such invariant that Certora’s FV audit focused on is **solvency**, that is, can the system’s assets cover all of its debts In the case of the Stake Pool, this, in simplified terms, translates to “the number of shares issued by the program is less than or equal to the total funds managed by the program”. Solvency is crucial as it protects users from losing their funds by guaranteeing that the Stake Pool can always honour withdrawals.

Due to the complexity of the system, the formalization of this property is not straightforward. We first need to identify and differentiate between both assets and shares that are physically held by the validators and virtually accounted for by the pool. 

To do so, we define a few relevant terms t where the suffix t\_v signifies a virtual amount tracked by the Stake Pool and the suffix t\_p indicates physical amounts. We have:

- **shares_p**
- **validatorBalance_v**
- **validatorBalance_p**
- **reserveBalance_p**
- **totalLamports_v**
- **totalLamports_p**
**totalLamports_p == reserveBalance_p + ∑ validatorBalance_p.**

Solvency can now be precisely expressed as the property

`shares_p ≤ totalLamports_p.`

To achieve the proof of this property, we compose three invariants relating virtual accounting with the physical accounting that imply solvency for the Solana Stake Pool program:

**(Inv. 1) `shares_p ≤ totalLamports_v`** - relating shares to the Stake Pool’s virtual accounting of assets.

**(Inv. 2) `totalLamports_v ≤ reserveBalance_p + ∑ validatorBalance_v`** - relating the virtual accounting with physical accounting in the reserve stake account and virtual balances of validators. Readers familiar with the technical details of the Stake Pool Program might be able to see why strict equality does not hold here.

**(Inv. 3) `validatorBalance_v ≤ validatorBalance_p`** for each validator - adding the missing piece of relating virtual and physical accounting.

Invariants 1-3 not only imply solvency, but form a clear mathematical relationship between the physical state of the stake accounts and the virtual accounting by the pool.

Note that the proof of Solana Stake Pool upholding invariants 1-3 requires establishing a number of additional invariants that relate the status of stake accounts with their balances. The most notable of these is the following invariant:

**(Inv. 4) The pool must always be able to withdraw from the reserve stake account.**

Invariants 4 may seem simple, but they were crucial towards uncovering high-severity issues!

## **Uncovering bugs with invariants**

When evaluating the Stake Pool against Invariant 4, it is violated by the WithdrawStake instruction. Consider the following code snippet:

When the stake is to be withdrawn from the reserve stake account, the protocol checks that the reserve stake account has enough minimum balance for rent. However, the protocol fails to check that the reserve stake will not be drained fully.

It is critical that the reserve stake account is never drained fully because of a possibility that an attacker may hijack it: once an account is drained of its lamports, the Solana runtime removes it at the end of the transaction. However, an attacker can airdrop on a closed account before the end of transaction, preventing its deletion. The attacker can thus revive the stake account and use it to maliciously interact with the Stake Pool.

Draining the reserve account fully allows an attacker to hijack and take hold of the reserve

stake account. This can have dire consequences. For example, the attacker can deposit stake to the reserve, leading the Stake Pool to mint new shares for the attacker. However, since the attacker still retains the ability to withdraw the lamports from reserve, the shares are basically issued to the attacker for free. The attacker now possesses the ability to manipulate the share price. In addition to the aforementioned attack vector, the attacker can also steal any funds deposited to the reserve stake by the victims.

## **Conclusion**

Certora’s audit of the Solana Stake Pool illustrates how formal verification goes beyond traditional auditing. Simply by establishing the important properties and mapping out their proofs can help identifying severe attack vectors that only arise from logically dissecting the code base.

Thanks to mathematical proofs of the protocol’s solvency invariants, we identified deep structural risks invisible to surface-level testing. The final result: 15 total issues found, and 11 mathematical invariants that will guide the future changes to the Stake Pool Program.

With these invariants, Solana’s most battle-tested staking protocol is now also formally verified. Detailed discussion of invariants and findings are available in the full report: [https://www.certora.com/reports/solana-stake-pool](https://www.certora.com/reports/solana-stake-pool)
