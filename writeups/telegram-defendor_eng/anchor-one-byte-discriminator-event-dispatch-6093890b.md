# 🛡️ Vulnerability in Anchor: Short Discriminators Can Disable Event Handling

- **Source URL:** https://exvul.com/blog/anchor-one-byte-discriminator-event-dispatch
- **Fetched:** 2026-11-15
- **Channel:** @defendor_eng
- **Telegram message:** https://t.me/defendor_eng/1303 (id 1303)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
Affected component: lang/syn/src/codegen/program/dispatch.rs, idl/src/build.rs | Category: Framework hardening (developer footgun) | Versions affected: 0.31.0+ | Tested on: 0.32.1

## Introduction

Anchor is the most widely used framework for building Solana programs. At the heart of every Anchor program is a `dispatch()` function — auto-generated code that routes incoming transaction data to the correct instruction handler based on a discriminator prefix.

By default, Anchor uses an 8-byte discriminator derived from `sha256("global:")[..8]`. Since all default discriminators share the same length, the `starts_with()` matching used in dispatch is unambiguous and safe.

However, since version 0.31.0, Anchor supports **custom discriminators** via the `#[instruction(discriminator = [...])]` attribute. This feature introduced a subtle gap: the framework performs **no validation** on custom discriminator values — no minimum length, no prefix-collision check, and no comparison against internal sentinel bytes. This creates a developer footgun where a carelessly chosen discriminator can silently disable critical framework functionality.

## Background: How Anchor Dispatch Works

Every Anchor program compiles down to a `dispatch()` function that checks each global instruction's discriminator using `starts_with()`. The key observation: **global instructions are checked first, and the Event CPI sentinel is checked last.** When all discriminators are 8 bytes, this ordering is fine — no 8-byte sequence can be a prefix of another 8-byte sequence.

`fn dispatch(program_id: &Pubkey, accounts: &[AccountInfo], data: &[u8]) -> Result<()> {    // 1. Check each global instruction's discriminator    if data.starts_with(instruction::Foo::DISCRIMINATOR) {        return __private::__global::foo(program_id, accounts, &data[8..])    }    if data.starts_with(instruction::Bar::DISCRIMINATOR) {        return __private::__global::bar(program_id, accounts, &data[8..])    }     // 2. Check the Event CPI sentinel (checked AFTER all global instructions)    if data.starts_with(anchor_lang::event::EVENT_IX_TAG_LE) {        return __event_dispatch(program_id, accounts, &data[8..])    }     // 3. Fallback    Err(ErrorCode::InstructionFallbackNotFound.into())}`
But what happens when a custom discriminator is shorter than 8 bytes?

## The Discovery

The `Overrides` parser in `lang/syn/src/lib.rs:83–104` accepts any arbitrary byte sequence as a custom discriminator with no validation whatsoever:

`"discriminator" => {    let value = match &arg.value {        Expr::Lit(lit) if matches!(lit.lit, Lit::Int(_)) => quote! { &[#lit] },        Expr::Array(arr) => quote! { &#arr },        expr => expr.to_token_stream(),    };    attr.discriminator.replace(value)  // No validation whatsoever}`
There is no check for: (1) Minimum length — even an empty `[]` discriminator is accepted, (2) Cross-instruction prefix collisions — a 1-byte discriminator can shadow an 8-byte one, (3) System sentinel collisions — a discriminator can collide with `EVENT_IX_TAG_LE`.

Meanwhile, the existing collision check in `idl/src/build.rs:372–390` only compares within the same category — accounts vs accounts, events vs events, instructions vs instructions. It never compares instruction discriminators against the system-level `EVENT_IX_TAG_LE` constant (`[0xe4, 0x45, 0xa5, 0x2e, 0x51, 0xcb, 0x9a, 0x1d]`).

## Root Cause Analysis

### 1. Dispatch ordering (dispatch.rs:19–85)

The generated `dispatch()` checks global instruction discriminators first, and the `EVENT_IX_TAG_LE` sentinel last. When a custom instruction has discriminator `[0xe4]` — the first byte of `EVENT_IX_TAG_LE` — the `starts_with(&[0xe4])` check matches before `starts_with(&[0xe4, 0x45, ...])` ever gets a chance:

`// event_hijacker checked firstif data.starts_with(instruction::EventHijacker::DISCRIMINATOR) {  // &[0xe4]    return event_hijacker(...)}// ... other instructions ... // EVENT_IX_TAG_LE checked later — DEAD CODEif data.starts_with(anchor_lang::event::EVENT_IX_TAG_LE) {  // &[0xe4, 0x45, ...]    return Err(EventInstructionStub.into());}`
### 2. Missing cross-category check (idl/src/build.rs)

The existing collision check (added in PR #3157) does not compare instruction discriminators against internal sentinel values like `EVENT_IX_TAG_LE`.

### 3. No constraint on custom discriminators (lang/syn/src/lib.rs)

The `Overrides` parser accepts any byte sequence without validation. Combined with (1) and (2), there is nothing preventing a developer from accidentally choosing discriminator bytes that shadow system functionality.

## Proof of Concept

### Minimal program

`use anchor_lang::prelude::*; declare_id!("HYFvCMUDQNu2iniPh7wpDYAscUkEs7aTorebutFsYB7Q"); #[program]pub mod discriminator_shadowing {    use super::*;     // discriminator [0xe4] = first byte of EVENT_IX_TAG_LE    // Shadows the event CPI dispatch handler    #[instruction(discriminator = [0xe4])]    pub fn event_hijacker(ctx: Context<BasicCtx>) -> Result<()> {        let log = &mut ctx.accounts.log;        log.last_handler = "event_hijacker".to_string();        Ok(())    }     pub fn initialize(ctx: Context<InitCtx>) -> Result<()> {        ctx.accounts.log.last_handler = String::new();        Ok(())    }}`
### Key test

`it("sending EVENT_IX_TAG_LE data dispatches to event_hijacker", async () => {  const eventTag = Buffer.from([0xe4, 0x45, 0xa5, 0x2e, 0x51, 0xcb, 0x9a, 0x1d]);   const ix = new anchor.web3.TransactionInstruction({    keys: [      { pubkey: provider.wallet.publicKey, isSigner: true, isWritable: false },      { pubkey: logPda, isSigner: false, isWritable: true },    ],    programId: program.programId,    data: eventTag,  });   const tx = new anchor.web3.Transaction().add(ix);  await provider.sendAndConfirm(tx);   const handler = await getLastHandler();  assert.strictEqual(handler, "event_hijacker");  // ^^^ PROVES: Event CPI tag was intercepted by event_hijacker});`
## Impact Assessment

This issue is **not an externally exploitable security vulnerability**. Custom discriminators are set at compile time by the program author — an external attacker cannot modify them. The Anchor development team has confirmed this assessment.

However, it is a **meaningful developer footgun** worth hardening against:

##### Silent event system breakage

A developer who chooses a short custom discriminator starting with 0xe4 will unknowingly disable their program's entire event system. The program compiles, the IDL builds, and it deploys with zero warnings.

##### Prefix shadowing between instructions

A short custom discriminator can shadow other instructions. For example, #\[instruction(discriminator = \[0xb7\])\] would intercept any instruction whose default sighash starts with 0xb7. The shadowed instruction becomes unreachable dead code.

##### Deserialization confusion

When a short discriminator shadows a longer one, the dispatch function strips only the short discriminator's bytes before passing data to the handler, causing unpredictable deserialization behavior.

##### Edge case — empty discriminator

The framework currently accepts discriminator = \[\]. Since \[\].starts\_with(&\[\]) is always true, an empty discriminator would match every incoming instruction, making all subsequent handlers unreachable.

## Suggested Hardening

- Minimum length check: Reject discriminators shorter than a minimum (e.g., 8 bytes) in Overrides::parse, or at least emit a compile-time warning for short discriminators.
- Prefix-collision check at IDL build time: Extend the existing check\_discriminator\_collision! to detect when one instruction's discriminator is a prefix of another's.
- System sentinel collision check: Compare custom discriminators against known internal sentinels (EVENT\_IX\_TAG\_LE) and reject or warn on prefix collisions.

## Timeline

- Discovery: Identified during review of custom discriminator handling introduced in PR #3137
- PoC: Built and verified on Anchor 0.32.1
- Disclosure: Reported via GitHub issue #4272
- Developer response: Acknowledged as worth hardening, not classified as a security issue
