# 🔍 Critical Bug Found in Solana's Optimized Token Program Before Launch

- **Source URL:** https://blog.asymmetric.re/solana-p-token-catching-a-bug-before-mainnet
- **Fetched from:** https://asymmetric.com/blog/solana-p-token-catching-a-bug-before-mainnet/
- **Fetched:** 2026-11-12
- **Channel:** @defendor_eng
- **Telegram message:** https://t.me/defendor_eng/1639 (id 1639)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
[← All posts](https://asymmetric.com/blog/)

# Solana p-token: Catching a Bug Before Mainnet

By Felix Wilhelm

This blog post describes an interesting issue we discovered in p-token, a compute-unit-optimized rewrite of Solana's token program. We found the issue during our ongoing security work with the Anza team, before the planned mainnet launch later this year. We think it's worth highlighting due to its subtlety, potential impact, and longevity in a heavily scrutinized codebase.

## The p-token program

Unlike EVM-based blockchains, where each crypto token has its own deployed smart contract, Solana tokens build on top of the SPL token program (or its somewhat controversial token-2022 relative). This means any token transfer, mint, or burn outside of native SOL requires a call to the token program. While the classic token program works fine, it wasn't developed with compute-unit efficiency in mind. This increases costs for token-related actions, most importantly transfers, and limits how many token transfers can fit in a block.

p-token is a Pinocchio-based rewrite of the SPL token program. It optimizes compute unit usage while remaining fully backwards compatible. Common operations like token transfers now cost over 95% fewer CUs.

Beyond full backwards compatibility, p-token introduces a new `batch` instruction. This allows callers to bundle multiple actions, transfers, approvals, and more, into a single token program call, reducing CU costs even further.

Internally, batch instructions encode inner instructions as part of their instruction data. The batch implementation iterates through them, calling the normal instruction handler one by one:

```
pub fn process_batch(mut accounts: &[AccountInfo], mut instruction_data: &[u8]) -> ProgramResult {
    loop {
        // Validates the instruction data and accounts offset.
        if instruction_data.len() < IX_HEADER_SIZE {
            // The instruction data must have at least two bytes.
            return Err(TokenError::InvalidInstruction.into());
        }
        // SAFETY: The instruction data is guaranteed to have at least two bytes
        // (header) + one byte (discriminator) and the values are within the bounds
        // of an `usize`.
        let expected_accounts = unsafe { *instruction_data.get_unchecked(0) as usize };
        let data_offset = IX_HEADER_SIZE + unsafe { *instruction_data.get_unchecked(1) as usize };
        if instruction_data.len() < data_offset || data_offset == IX_HEADER_SIZE {
            return Err(TokenError::InvalidInstruction.into());
        }
        if accounts.len() < expected_accounts {
            return Err(ProgramError::NotEnoughAccountKeys);
        }
        // Process the instruction.
        // SAFETY: The instruction data and accounts lengths are already validated so
        // all slices are guaranteed to be valid.
        let (ix_accounts, ix_data) = unsafe {
            (
                accounts.get_unchecked(..expected_accounts),
                instruction_data.get_unchecked(IX_HEADER_SIZE..data_offset),
            )
        };
        inner_process_instruction(ix_accounts, ix_data)?;
        if data_offset == instruction_data.len() {
            // The batch is complete.
            break;
        }
        accounts = &accounts[expected_accounts..];
        instruction_data = &instruction_data[data_offset..];
    }
    Ok(())
}
```
## Ownership checks

One way p-token (and other optimized programs) minimizes CU usage is by omitting unnecessary ownership checks. As a quick recap: each Solana account has an owner, which has full control over the data stored in that account. Programs like p-token must verify that all accounts they process have the correct owner, normally the program itself. Otherwise, the program may operate on spoofed accounts that contain data not written by the program and may represent invalid states.

However, these checks can be optimized away under some conditions using a clever trick. Programs can only modify accounts they own. If they try to modify a foreign-owned account, the runtime throws an error and the transaction fails. This means ownership checks are unnecessary as long as the program ensures the account is being modified during execution.

Interestingly, the exact timing of these runtime checks depends on the status of a feature gate in the SVM runtime:

When direct account mapping is enabled, any modification to an externally owned account fails immediately during the write to the mapped account data, regardless of what's being written. When it's disabled (as it currently is on mainnet), modifications are only checked at the end of program execution, and will only error if the data differs from its original state. This creates an interesting gap: if a program skips the ownership check on an externally owned account because it expects a later write, and you can trick it into restoring the original content before returning, the check won't trigger, and the transaction succeeds.

## Attacking the batch instruction

Since careful removal of ownership checks efficiently reduces CU costs during normal execution, p-token relies heavily on the SVM runtime checks to fail with externally owned accounts. For normal transfers (not zero, not self), the `process_transfer` handler doesn't verify the source account's owner; the transfer will modify its account data and trigger an error.

However, this behavior becomes a vulnerability with the new batch instruction. Using a batch, an attacker can perform another transfer back to the malicious source account inside the same program call. This resets the account data to its original state and bypasses the runtime check at the end of execution (as long as direct account mapping isn't enabled).

Here's a simple example: create a fake token account A (owned by the attacker) with a balance of 1,000 tokens.

Create a batch with the following instructions:

- Transfer 1,000 tokens from A → B (real token account)
- Transfer 1,000 tokens from B → A

This succeeds because account A's data remains unchanged after the batch finishes. While this alone gives the attacker no advantage, a slight modification turns it into a loss-of-funds bug for wrapped Solana:

1. Create a fake token account with an arbitrary balance, the native mint address as mint, but the `is_native` field set to `None`. This is account A.
2. Initialize a valid wrapped token account with the same balance. This is account B.
3. Choose an arbitrary target account C. This could be a CEX deposit address or a flash loan repayment account.
4. Create a batch to:
  1. Transfer X wrapped SOL from A to C. This increases the `amount` field in C's account data by X, but doesn't actually move any lamports since A's `is_native` field is `None`.
  2. Transfer X wrapped SOL from B to A. This resets A's `amount` field and moves X native SOL to A, since B's `is_native` is correctly initialized.

After the batch executes, the attacker still controls the same amount of native SOL but has inflated C's token account balance of wrapped SOL without depositing native SOL to it. This works because `transfer` only checks the source account's `is_native` field, which is attacker controlled. Combined with the deferred ownership check, this allows an attacker to use a crafted account with inconsistent state to split the token balance update from the lamport movement.

Inflating the `amount` field of any wrapped SOL token account without transferring the underlying lamports easily escalates into a general loss-of-funds bug. Most DeFi applications on Solana correctly treat the `amount` field as the source of truth. An attacker could exploit this to fake collateral or falsify a flash loan repayment.

## Patch

The Anza team quickly addressed the reported issue by adding dedicated ownership checks to the batch instruction (see [https://github.com/solana-program/token/pull/80](https://github.com/solana-program/token/pull/80))

```
        // Few Instructions require specific account ownership checks when executed
        // in a batch since ownership is only enforced by the runtime at the end of
        // the batch processing.
        //
        // Instructions that do not appear in the list below do not require
        // ownership checks since they either do not modify accounts or the ownership
        // is already checked explicitly.
        if let Some(&discriminator) = ix_data.first() {
            match discriminator {
                // 3 - Transfer
                // 7 - MintTo
                // 8 - Burn
                // 14 - MintToChecked
                // 15 - BurnChecked
                3 | 7 | 8 | 14 | 15 => {
                    let [a0, a1, ..] = ix_accounts else {
                        return Err(ProgramError::NotEnoughAccountKeys);
                    };
                    check_account_owner(a0)?;
                    check_account_owner(a1)?;
                }
                // 12 - TransferChecked
                12 => {
                    let [a0, _, a2, ..] = ix_accounts else {
                        return Err(ProgramError::NotEnoughAccountKeys);
                    };
                    check_account_owner(a0)?;
                    check_account_owner(a2)?;
                }
                // 4 - Approve
                // 5 - Revoke
                // 6 - SetAuthority
                // 9 - CloseAccount
                // 10 - FreezeAccount
                // 11 - ThawAccount
                // 13 - ApproveChecked
                // 22 - InitializeImmutableOwner
                // 38 - WithdrawExcessLamports
                // 45 - UnwrapLamports
                4..=13 | 22 | 38 | 45 => {
                    let [a0, ..] = ix_accounts else {
                        return Err(ProgramError::NotEnoughAccountKeys);
                    };
                    check_account_owner(a0)?;
                }
                _ => {}
            }
```
Since then, we have been continuously reviewing and fuzzing the p-token codebase and are looking forward to its mainnet launch later this year.

## Conclusion

This post described a subtle loss-of-funds vulnerability in p-token, due to the interplay of deferred ownership checks and a newly introduced batch instruction. By crafting a fake token account with an inconsistent `is_native` field and exploiting the `batch` instruction's ability to restore account data before the runtime check, an attacker could inflate a target account's wrapped SOL balance without moving any lamports.

The bug is a good reminder that individually safe optimizations can become vulnerabilities when composed with new functionality. Deferring ownership checks to the runtime works when each instruction executes independently, but batch execution breaks that assumption by allowing multiple state transitions within a single program invocation. The invariant that "any modification to a foreign account will be caught" breaks when modifications can be reversed by the program prior to runtime validation.
