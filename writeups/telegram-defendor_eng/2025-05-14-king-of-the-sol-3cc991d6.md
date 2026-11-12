# 👑 Dangers of Transferring Lamports in Solana

- **Source URL:** https://osec.io/blog/2025-05-14-king-of-the-sol
- **Fetched from:** https://osec.io/blog/king-of-the-sol/
- **Fetched:** 2026-11-12
- **Channel:** @defendor_eng
- **Telegram message:** https://t.me/defendor_eng/364 (id 364)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Solana: the hidden dangers of lamport transfers

[Nicola Vella](https://osec.io/authors/nicola/)

[#solana](https://osec.io/tags/solana/)

[#rent](https://osec.io/tags/rent/)

Solana’s lamport transfer logic hides dangerous edge cases — from rent-exemption quirks to write-demotion traps. We dissect a deceptively simple smart contract game to expose how transfers to arbitrary accounts can silently fail, brick your program, or crown an eternal king.


## Introduction

Is it safe to transfer lamports to an arbitrary address on Solana? The answer might surprise you.

In this post, we explore a deceptively simple smart contract game inspired by [King of the Ether](https://www.kingoftheether.com/thrones/kingoftheether/index.html). Through it, we’ll highlight subtle pitfalls in Solana’s account model that can brick your program — especially when it comes to transferring lamports.

## The game: King of the SOL

The game works like this:

- Anyone can become the **king** by bidding at least 2× the previous bid.
- The old king is reimbursed 95% of their bid.
- The remaining 5% goes into a prize pot.
- If the reigning king survives for 10 days without being dethroned, they can claim the entire pot.

Simple, right?

This is the core logic:

Note this comment:

any writable account is allowed as a new king.


…Is our assumption correct?

## The bugs lurking beneath

### Bug 1: the rent-exemption trap

On Solana, all accounts must maintain a **minimum balance** of lamports to remain rent-exempt. Specifically, an account can be in one of two states:

- **Uninitialized**: `lamports = 0`
- **Initialized**: `lamports >= rent-exempt threshold`

This rent model exists to prevent low-cost DoS attacks on validators. The key idea is that even an account with no data (i.e., zero-length data buffer) still consumes on-chain resources; specifically, **account metadata** like its public key, owner, or lamport balance. That metadata must be stored persistently by validators, and that storage isn’t free.

So “persistent state” on Solana doesn’t just mean your program’s data — it includes the base account structure itself. Even accounts with `data.len() == 0` must meet a minimum rent threshold to remain alive and avoid garbage collection by the runtime.

This is enforced at the runtime level; the relevant logic lives in [`svm_rent_collector.rs`](https://github.com/anza-xyz/agave/blob/7a1e57469a5b1aeed617457c0519803620ba953f/svm-rent-collector/src/svm_rent_collector.rs#L117-L136):

You can check the rent-exemption threshold for a zero-data account with the CLI:

#### Fix 1: only reimburse if rent-exempt

We don’t want to donate anything to an unfair king! So let’s update our program to reimburse only if the old king will be rent-exempt after the transfer:

But is rent-exemption the only thing that can cause a lamport transfer to fail? Not quite.

### Bug 2: writable but untouchable — `set_lamports` fails

Let’s look at [`BorrowedAccount::set_lamports`](https://github.com/anza-xyz/agave/blob/f389dd23067e37d756c3f9d2f3d50e339dad7053/transaction-context/src/lib.rs#L863-L885):

Turns out: even writable, rent-exempt accounts can still reject lamport transfers.

Specifically, **executable accounts** cannot receive or send lamports — the runtime treats them as immutable.

## Note (What’s the executable flag anyway?)

The `executable` flag is a legacy mechanism marking accounts that hold program code. Historically, an account with this flag was assumed to either contain immutable BPF bytecode or to be a proxy to a built-in program, and therefore it made sense to consider it read-only for performance reasons.

This behavior became problematic with the introduction of the **Upgradeable BPF Loader**. A workaround was used to maintain compatibility with the existing runtime logic. The program data containing BPF bytecode was split into a separate account, ProgramData, with the program account now only containing an address pointing to the ProgramData account:

Eventually, the `executable` flag will be removed entirely as proposed in [SIMD-0162](https://github.com/solana-foundation/solana-improvement-documents/blob/main/proposals/0162-remove-accounts-executable-flag-checks.md). The reasoning is simple: an account’s owner and its content are sufficient to determine if it’s a valid program — the `executable` flag is redundant.

This change is also a **hard requirement for supporting the new loader-v4**. Unlike the upgradeable loader, which relies on a separate `ProgramData` proxy account, loader-v4 stores all program data directly in the program account itself.

As a result, it becomes impossible to modify the account’s size after deployment, or to [migrate](https://github.com/anza-xyz/agave/blob/7a1e57469a5b1aeed617457c0519803620ba953f/programs/bpf_loader/src/lib.rs#L1411) from the upgradeable loader to loader-v4 — without hitting the `ExecutableLamportChange` restriction.

#### Fix 2: reject program accounts

To avoid this footgun, let’s explicitly skip any executable account:

Now we’re safe…right?

### Bug 3: the write-demotion trap

On Solana, accounts passed as **writable** in a transaction can be **silently downgraded to read-only**. This behavior occurs during message sanitization — even before your program runs.

Let’s walk through the logic for legacy messages<sup>[1](https://osec.io#user-content-fn-1)</sup>:

As you can see, there are two main causes of write-demotion:

1. The account appears in the [reserved account list](https://github.com/anza-xyz/agave/blob/cd76bf6b8da8ec3739f0df4e087de0e50028b034/reserved-account-keys/src/lib.rs#L142-L182).
2. The account is invoked as a program without the upgradeable loader being present in the transaction.

The second case is generally covered by the `executable` check implemented previously.

The first case, however, is far more dangerous — it can silently break your program logic without any obvious cause. Let’s dig deeper into that.

#### The reserved account list

The Solana runtime maintains a [reserved account list](https://github.com/anza-xyz/agave/blob/cd76bf6b8da8ec3739f0df4e087de0e50028b034/reserved-account-keys/src/lib.rs#L142-L182), which includes addresses with special semantics — such as built-in programs, precompiles, and sysvars.

These accounts may initially behave like normal accounts. However, once they become reserved after a [feature gate is activated](https://github.com/anza-xyz/agave/blob/0e6d9bf8c81cd94dfdedb500af4ac17328cf7a43/runtime/src/bank.rs#L6469-L6474), the runtime will **automatically demote them to read-only**, even if the transaction marked them as writable:

#### Consequences: silent failures and bricked programs

This behavior is especially dangerous when you constrain a program to be writable. For example, with Anchor, it’s pretty common to use the `#[account(mut)]` constraint:

This works fine — until one day, `old_king` is silently demoted. Suddenly, the `#[account(mut)]` constraint fails, and your program is bricked. Even though you’re passing a writable account in the transaction, the runtime has made a unilateral decision to override that.

#### Real-world example: write-demotion with `secp256r1_program`

Here’s a concrete example of the write-demotion trap playing out on mainnet — involving `secp256r1_program`, a precompiled program gated behind a feature flag:

Before the `enable_secp256r1_precompile` feature is activated, this account behaves like any ordinary one. You can assign `secp256r1_program::id()` as the king in a contract.

But once the feature is flipped on, the runtime silently marks it as read-only, blocking any future writes. As a result, `secp256r1_program::id()` becomes the eternal king, and no one can dethrone it.

#### Fix 3: preventing write-demotion pitfalls

Alright, let’s try to fix *yet another* edge case — and hopefully close the book on it.

##### Attempt 1: block known reserved accounts

One naive solution is to reject any known reserved account, for example:

This works in the short term, but doesn’t scale — you can’t predict all future additions to the `ReservedAccount` list. The moment a new reserved account is introduced, your program becomes vulnerable again.

##### Attempt 2: use a PDA vault

A more future-proof fix is to avoid **transferring lamports to arbitrary accounts** altogether.

A clean approach would be to store the refund lamports in a PDA vault owned by your program. This prevents your logic from depending on accounts you don’t have complete control over, and sidesteps any risk of write-demotion or future account restrictions.

## Final thoughts

Transferring lamports on Solana is not always straightforward and carries potential risks. Account constraints alone are insufficient to ensure safety, especially when dealing with runtime-specific edge cases.

We can safely transfer lamports to an account under the following conditions:

- It’s not executable.
- Its balance, after the transfer, remains rent-exempt.
- It’s not a reserved account.

This issue is not purely theoretical; it has impacted real-world programs. One significant case was recently reported to Jito via the bug bounty, which could have resulted in incorrect tip payments.
