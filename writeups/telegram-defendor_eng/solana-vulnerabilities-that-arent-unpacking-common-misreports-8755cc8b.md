# 📚 Solana Security Misinformation Is Spreading Through Official Docs and LLMs

- **Source URL:** https://blog.asymmetric.re/solana-vulnerabilities-that-arent-unpacking-common-misreports
- **Fetched from:** https://asymmetric.com/blog/solana-vulnerabilities-that-arent-unpacking-common-misreports/
- **Fetched:** 2026-11-12
- **Channel:** @defendor_eng
- **Telegram message:** https://t.me/defendor_eng/1555 (id 1555)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
[← All posts](https://asymmetric.com/blog/)

# Solana Vulnerabilities That Aren’t: Unpacking Common Misreports

By John Saigle

The most persistent security misinformation doesn't come from obscure corners of the internet, but from official documentation, recommended learning resources, and the LLMs that auditors and developers use every day.

If a bug class is stated confidently enough, it is likely to propagate widely via a recursive feedback loop: outdated or incorrect documentation enters LLM training data, and those same LLMs are then used to write new documentation and educational content.

This information then reaches developers and auditors who are seeking to learn how to secure Solana. Learning a new skill necessarily involves a stage where the learner is limited to copying and comparing with their existing mental models. If the materials and tools contain errors, the student won't realize this until they make a poor design decision or report an invalid finding. This is an unnecessary waste of scarce time and talent.

All of the examples below come from real-world sources: educational content specializing in Solana security, social media channels devoted to auditors and bug bounty hunters, recommendations from older LLM models, and official Solana documentation. The goal isn't to name and shame, but to serve as an updated reference for secure code review in Solana. Explicitly noting illegitimate vulnerability classes can improve the educational content for those interested in securing Solana code, help correct insufficient training data in LLMs, and raise the floor for the process of Solana program security review in general.

## The Misreports

### Reentrancy

Reentrancy as a bug class haunts the world of blockchain security, given its initial prevalence and massive impact within Solidity. The general idea is:

1. A vulnerable `contract A` both performs a sensitive action (e.g. withdrawal of funds) and calls into an attacker-controlled `contract B` before debiting their withdrawal
2. `Contract B` calls back into `contract A` recursively, such that `contract A` again calls `contract B` – but still using the old balance
3. This loop continues until e.g. enough withdrawals have occurred to break the loop, leaving the attacker with all the funds.

Fortunately, this is usually not a problem in Solana due to a couple of related security controls. Solana uses a stack to track CPI calls and checks performed on the stack's contents:

- The [available CPI depth is 4 for non-system Solana programs](https://github.com/anza-xyz/agave/blob/master/program-runtime/src/execution_budget.rs#L7), preventing unbounded nested CPI calls. *(Note:* [*SIMD-0268*](https://github.com/solana-foundation/solana-improvement-documents/blob/666aef1a6dc6b3a566ee4ad49d51beef8a792a93/proposals/0268-raise-cpi-nesting-limit.md) *increases this limit to 8 for Agave version 3 and higher.)*
- [Invocation reverts if a program attempts to perform CPI into a program that appears above them in the stack](https://github.com/anza-xyz/agave/blob/ceb02a8e6d26259aa590d1f90315e5f257f51c87/program-runtime/src/invoke_context.rs#L257-L275).

Taken together, this breaks the `A → B → A` flow necessary for reentrancy attacks: the initial call back to `contract A` cannot occur, and anyway, only 4 CPIs are possible before the transaction reverts (thus restoring the state).

In very rare circumstances, *self-reentrancy* can be a problem: the above constraints still allow a program to call itself. (i.e. do `A → A`)

### Closing Anchor accounts safely involves setting the 'Closed Account Discriminator'

Anchor doesn't even have a closed account discriminator! Not [in the last year and a half](https://github.com/otter-sec/anchor/blob/master/CHANGELOG.md) anyway...

The account closing issue arising from Anchor was [fixed nearly three years ago](https://github.com/otter-sec/anchor/blob/master/CHANGELOG.md#0260---2022-12-15). The closed account discriminator stuck around for a while, but even those vestiges were purged in Anchor `v0.30.0`.

Safely closing accounts is a sensitive operation, to be sure. Removing all of the funds and data from an account can go horribly wrong, especially in the context of a complex application flow. (For a recent example, [check out Felix’s recent post about marginfi’s flash loan bug](https://asymmetric.com/blog/threat-contained-marginfi-flash-loan-vulnerability/).) But developers and auditors don't need to go to great lengths to close Anchor accounts properly in most cases.

Developers writing native Solana without the use of Anchor still need to close accounts carefully. They don’t need to use the discriminator pattern, but they do need to ensure that it’s impossible for a user to force the account to stay open.

How? [Creating an account is a three-step process](https://github.com/anza-xyz/agave/blob/v3.1/programs/system/src/system_processor.rs#L147):

- Transfer funds to cover rent
- Allocate size for the data
- Assign ownership from the System program to the new owner

We just need to make sure we do the inverse:

- Transfer funds out of the account
- Allocate the size to 0
- Relinquish the account back to the System program

Anchor does this automatically. Native Solana contract developers can reuse [this safe account closing pattern](https://github.com/solana-program/token/blob/84769ca25bbf67aed7712dc3a3acac16e7415e81/program/src/processor.rs#L1035-L1039) from the Token Program.

### Floats lead to non-determinism issues

This is an important consideration when working with validator software, but within the Solana run-time, we don't need to worry about determinism issues for floating-point numbers. Floating point operations may differ at the *hardware* level, but not within the context of Solana programs.

The reason is that the floating point operations are not strictly supported (there are no opcodes in the [SBPF interpreter](https://github.com/anza-xyz/sbpf/blob/ade3dd1f6d373006fc10fe3eb9203496b76e7310/src/interpreter.rs)). Instead, the floating-point arithmetic will be emulated by LLVM with the available opcodes. As a result, Solana contracts aren't able to natively access floating-point operations, which has the downside of being expensive in terms of CU but also has the upside that hardware non-determinism isn't a concern for devs and auditors working at Solana's application layer.

So, non-determinism in particular is not something we need to worry about, though floats remain tricky. Auditors should still watch out for accuracy problems and logical errors when it comes to doing float arithmetic, as well as providing appropriate bounds checks on inputs and outputs. Because that interest rate calculation really shouldn't yield NaN or negative infinity... right?

An example of this comes from the [ScaledUiAmount Token2022 extension](https://github.com/solana-program/token-2022/blob/9cbf7a1e9bab57aabb71b4b84fc84e3670108573/interface/src/instruction.rs#L541-L547), where conversions to and from the "UI Amount" and the real Amount field may be inconsistent.

### Self-transfers of tokens always succeed

*It's important to note that when the source and destination of a Transfer are the same, the Transfer will always succeed.
https://www.solana-program.com/docs/token#transferring-tokens*

This juicy line of text conjures dozens of ideas for the fledgling Solana hacker looking for a big bug:

- What if a user transfers funds to themselves instead of to a vault account to get around paying for a bid?
- Can I delegate or stake funds to myself and earn rewards?
- Can I pretend to transfer way more funds than I actually have, tricking the amount calculation?

The fun never ends.

However, the token program does not contain such a silly bug. A lot of logic surrounds whether a token transfer is successful: the source and destination token accounts must share a mint; the source account must be solvent; neither account can be frozen; and so on. This becomes ever more complex with Token Extensions, which dramatically change the way two token accounts might interact.

Simply put, it's not the trivial success that the documentation warns of. Ultimately, developers should consider checking whether source and destination are equivalent, and what impacts this may have, but this succeeds only after the final step of a long series of checks, not as a total short-circuit of token logic. For more information, refer to the [process\_transfer function in the Token2022 program](https://github.com/solana-program/token-2022/blob/e703317851a70db200bf0545ca3cea5dcd0e1492/program/src/processor.rs#L300-L305) or the [equivalent function in the traditional SPL program](https://github.com/solana-program/token/blob/main/program/src/processor.rs#L252).

### Use of load\_instruction\_at or load\_current\_index

This claim is, of course, valid, though outdated. This is an issue that, relative to the speed of blockchain development, is absolutely prehistoric. (i.e. it was fixed in 2022)

The initial remediations involved changing the visibility of the dangerous  load\_instruction\_at and load\_current\_index functions. This made them inaccessible to developers at the application layer. [https://docs.rs/solana-instructions-sysvar/2.2.2/src/solana\_instructions\_sysvar/lib.rs.html#151-153](https://docs.rs/solana-instructions-sysvar/2.2.2/src/solana_instructions_sysvar/lib.rs.html#151-153)

Now, they're totally removed. Thankfully, these instructions and the nightmares they caused are long behind us.

### Partial state commitment

Most smart contract runtimes don't work this way. If a transaction reverts, all of the state should be rolled back. This is the case in Solana, as outlined above: there is no partial state commitment. An account is written to if and only if the entire transaction succeeds.

As with the unchecked return value case, this type of bug is more likely to be reported by LLMs these days than by auditors.

**Caveat**: This programming pattern can still be important to verify in other runtimes. For example, NEAR’s contract environment does *not* have this guarantee. Also, state roll backs can be complicated and may not be done correctly. You can check out other blog posts from our team for instances of this kind of issue [occurring in IBC](https://asymmetric.com/blog/cosmos-ibc-reentrancy-infinite-mint/) as well as [in Evmos.](https://asymmetric.com/blog/evmos-precompile-state-commit-infinite-mint/)

### Not checking the return value of a CPI call

This likely comes from auditors trying to understand Solana by pattern matching on the way Solidity works. In that ecosystem, it can be important to check the return value of an external contract call. Depending on the called contract's programming style, it may revert on error, or else return a boolean indicating whether an error has occurred. This is one of the sources of problems with using ERC20 tokens historically and is one of the motivations for the SafeERC20 libraries that are now widely used.

Luckily, we don't have to worry about this when reviewing Solana code. If an error occurs in a CPI, the transaction reverts. You can confirm this by starting with [the function comment for invoke in the Agave SDK](https://github.com/anza-xyz/solana-sdk/blob/ae3b4e7bdab8d701f7a928fe2e9194229f36cce3/cpi/src/lib.rs#L70-L73) and following the execution from there.

As with the EVM, transactions in SVM are all-or-nothing. The difference is that errors in cross-contract calls can be caught in EVM but failing CPIs are always fatal in Solana.

It's very common for developers to rely on this property. Doing so allows them to simplify the code and improve performance around error handling. Essentially, we can proceed safely after a CPI, as any errors automatically revert. This is closely related to why using assert or unwrap() is generally an acceptable practice in Solana.

Even in the happy path, the new state resulting from CPI calls is typically read from the modified accounts rather than as a return value of the CPI. However, it *is* possible to [return data directly](https://github.com/anza-xyz/solana-sdk/blob/master/cpi/src/lib.rs#L339C8-L339C23).

## The Misreport Pipeline

Some of the bug classes discussed above really were issues in the past, but improvements in Solana and Anchor mean that we don’t need to worry about them anymore.

There are even more security fixes coming soon. The important security issues of today will become the noise of the future. Such is the way.

Some developments to keep an eye on:

### **`Access violation in stackframe` stack overflow issue**

Complex programs written in Anchor have been overflowing the stack for some time. This is surprising to learn as an auditor, and unfortunately, it has surprised many developers, too.

Stack protections were enabled in Solana mainnet but disabled by default in test environments. This caused developers using anchor-test-validator as their testing infrastructure to overflow the program’s stack without knowing it, only to deploy their programs and have them self-DoS in mainnet!

Fortunately, [recent versions of Anchor](https://www.anchor-lang.com/docs/updates/release-notes/0-31-0#stack-memory-improvements) seem to have addressed this for the most part.

### **Duplicate mutable accounts**

Anchor programs using multiple arguments of the same type could accidentally overwrite data if one of the arguments were duplicated, and both were written to.

For example, you have two arguments a and b, both of type mut T, Anchor doesn't stop you from passing values where a == b. (That is, they reference the same underlying data.) If you set a to 1, then later set b to 2, the result would be that both a *and* b would ultimately end up with the value 2.

This was a tricky bug that required fairly in-depth knowledge of Anchor’s internals to detect and prevent. Fortunately, this has been [addressed upstream](https://github.com/otter-sec/anchor/issues/3825) and will be fixed in the 1.0 release.

## Conclusion

Blockchain development is advancing quickly. So too must security methodology. Beginners in Solana auditing should be cautious of Top Tips guides and the curricula of auditing boot camps and courses. While these resources can be a great starting point, content that’s only a few months old may not accurately reflect the chain's actual behavior. LLMs, too, are stuck in the past. Each runtime must be considered on its own terms. The security patterns from other blockchains may not apply. Solana is not Solidity.

Even experienced Solana auditors should be diligent about staying current with the latest releases. In this space, docs and specs do not determine how code is written, but trail it like a wake. There is no authority but the source code.
