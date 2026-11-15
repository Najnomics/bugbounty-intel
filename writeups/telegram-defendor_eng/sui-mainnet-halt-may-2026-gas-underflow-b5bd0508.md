# 🚨 Bug in Sui v1.72 Caused Mainnet Halt

- **Source URL:** http://exvul.com/blog/sui-mainnet-halt-may-2026-gas-underflow
- **Fetched from:** https://exvul.com/blog/sui-mainnet-halt-may-2026-gas-underflow
- **Fetched:** 2026-11-15
- **Channel:** @defendor_eng
- **Telegram message:** https://t.me/defendor_eng/1667 (id 1667)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
Affected component: sui-execution (execution\_engine.rs, gas\_charger.rs), sui-framework (accumulator.move, accumulator\_settlement.move) | Category: Liveness (not solvency) | Versions affected: 1.72.0 | Fixed in: emergency patch on releases/sui-v1.72.0, forward-ported as commit 124c64e

@SuiNetwork — May 28, 2026, 10:29 PM: Sui Mainnet is currently experiencing a network stall. The Sui Core team is actively working on a solution. Be aware that transactions may be paused at this time. Updates will be shared as soon as they are available.

@SuiNetwork: Activity on Sui mainnet has resumed after a halt due to a crash bug in the gas charging logic introduced by the 1.72 release. A full incident review will be shared in the coming days.

The two tweets above bracket the entire public picture of the May 28, 2026 Sui mainnet incident. Behind them is a single sharply-scoped bug at the seam of two new features — **Address Balance** and **coin reservations** — that allowed a perfectly ordinary user-submitted transaction to plant a poisoned `AccumulatorEvent` into a checkpoint, causing the per-checkpoint settlement system transaction to abort and every honest validator to stall at the same block.

The fix landed as an out-of-band emergency patch to `releases/sui-v1.72.0`, and was forward-ported to `main` as commit [`124c64e`](https://github.com/MystenLabs/sui/commit/124c64e643a2fea059cb369cc6b96b565fadea7d) ("Land #26816 gas-underflow fix in main (#26828)"). The forward port touches just two files: a 16-line change to `execution_engine.rs` and a regression test in `address_balance_compatibility_tests.rs`. The brevity of the fix is itself a useful data point: the underlying invariant was simple, and the bug was a missing case, not a structural problem.

This post walks the bug end-to-end: why a failed transaction could emit settlement-impacting side effects, why the existing safety net did not catch this shape, what exactly the patch does, and what the incident says about layering side-effects in a system that defers state changes to a separate Move-executed system transaction.

If you want to read the actual source while going through this post, pin this ref — git commit: `818f8d78f222b9279cb966a5754fb0a2c21d58b1`.

## TL;DR

A transaction that the adapter was already going to fail with `InsufficientFundsForWithdraw` (IFFW) still ran the **gas smashing** step before being aborted. Gas smashing for an Address Balance coin-reservation entry emits an accumulator `Split` event for the reservation amount. That `Split` was then handed to the per-checkpoint **accumulator settlement** system transaction, which calls `sui::accumulator_settlement::settle_u128`, which calls `U128.update(merge, split)`:

`public(package) fun update_u128(u128: &mut U128, merge: u128, split: u128) {    u128.value = u128.value + merge - split;}`
With the Address Balance already drained to 0, `merge == 0` and `split > 0`, so Move's checked arithmetic underflowed and aborted the settlement transaction. Because settlement is a \*system\* transaction whose contents are deterministically derived from the checkpoint, every honest node hit the same abort at the same checkpoint — and mainnet stalled.

The fix removes Address Balance reservation entries from `gas_data.payment` whenever execution is going to early-abort with `InsufficientFundsForWithdraw`, so smashing never runs over them and the bad `Split` is never produced in the first place.

It is worth being precise about the threat model: this was **not** a fund-theft bug. Move's checked arithmetic refused to apply the underflow, so no balance was silently moved. The damage was to **liveness**: the chain could not produce/apply checkpoints past the offending one until the patched binary was deployed.

## Background

### Address Balance and accumulators

Address Balance is Sui's account-style balance model layered on top of its object model. Rather than holding SUI exclusively as discrete `Coin` objects, a user can hold a balance at the address level. On-chain, that balance lives under a single shared `AccumulatorRoot` object as a dynamic field whose value is a `U128`:

`public struct U128 has store {    value: u128,}`
Crucially, user transactions do not mutate that field directly. Doing so would serialize every transaction in the network on the shared `AccumulatorRoot`. Instead, user transactions emit `AccumulatorEvent`s — `Merge` for a deposit, `Split` for a withdrawal — and the actual mutation is deferred to a per-checkpoint **system transaction** that aggregates all events and applies the net change. This indirection is what keeps Address Balance compatible with Sui's parallel execution model.

### The settlement system transaction

After a checkpoint's user transactions are executed, the validator builds a settlement transaction from their `AccumulatorEvent`s. The aggregation logic walks every transaction's effects, sums `Merge` and `Split` separately per `(accumulator_obj)`, and then emits a Move call for each updated accumulator:

`builder.programmable_move_call(    SUI_FRAMEWORK_PACKAGE_ID,    ACCUMULATOR_SETTLEMENT_MODULE.into(),    ACCUMULATOR_ROOT_SETTLE_U128_FUNC.into(),    vec![address.ty.clone()],    vec![root, address_arg, merge_amount, split_amount],);`
The builder packages these calls as a `TransactionKind::ProgrammableSystemTransaction`, and the execution engine dispatches that variant into the PTB executor with the Move VM:

`TransactionKind::ProgrammableSystemTransaction(pt) => {    SPT::execute::<execution_mode::System<Mode::Error>>(        protocol_config, metrics, move_vm, temporary_store, ...        gas_charger, None, pt, trace_builder_opt,    )}`
This is the critical layering: **all accumulator state changes go through Move**. Rust orchestrates which calls to make, but the calls themselves run inside the Move VM and are bound by Move's checked arithmetic and `assert!` semantics. The Move callee in `accumulator_settlement.move` is the only code authorized to write the accumulator value:

`fun settle_u128<T>(    accumulator_root: &mut AccumulatorRoot,    owner: address,    merge: u128,    split: u128,    ctx: &TxContext,) {    assert!(ctx.sender() == @0x0, ENotSystemAddress);    assert!((merge == 0) != (split == 0), EInvalidSplitAmount);     let name = accumulator_key<T>(owner);    if (accumulator_root.has_accumulator<T, U128>(name)) {        let is_zero = {            let value: &mut U128 = accumulator_root.borrow_accumulator_mut(name);            value.update(merge, split);            value.is_zero()        };        if (is_zero) { ... }    } else {        assert!(split == 0, EInvalidSplitAmount);        ...    };}`
And the actual arithmetic, in `accumulator.move`:

`public(package) fun update_u128(u128: &mut U128, merge: u128, split: u128) {    u128.value = u128.value + merge - split;}`
Move's integer arithmetic is checked. Any expression where `split > value + merge` aborts the call — and since the call is the body of the settlement system transaction, the abort bubbles up to abort the whole system transaction.

### Coin reservations and gas smashing

Sui has long supported paying gas from a list of coin objects, "smashing" them together: the first coin in the list becomes the primary, the others have their balances folded into it, and the others are deleted. With Address Balance, that mechanism was extended so that a gas-payment entry can be a **coin reservation** — a synthetic `ObjectRef` whose digest, when decoded with `ParsedDigest::try_from`, represents "treat this entry as a `reservation_amount()` withdrawal from the owner's address balance" rather than as a real coin object. The classification is in `execution_engine.rs`:

`if let Ok(parsed) = ParsedDigest::try_from(entry.2) {    PaymentMethod::AddressBalance(gas_data.owner, parsed.reservation_amount())} else {    PaymentMethod::Coin(*entry)}`
Smashing for a `PaymentMethod::AddressBalance` cannot delete an object — there is no object — so instead it emits a negative-balance `AccumulatorEvent` (a `Split`) for the reservation amount:

`PaymentMethod::AddressBalance(sui_address, reservation) => {    let event = AccumulatorEvent::from_balance_change(        *sui_address,        balance_type,        i64::try_from(*reservation).unwrap().checked_neg().unwrap(),    ).expect("...");    temporary_store.add_accumulator_event(event);}`
That event is exactly the kind of event that the settlement aggregator later sums into a `split` value passed to `settle_u128`. Everything is wired correctly — \*for a transaction that actually runs\*.

### The existing IFFW guard and why it did not catch this

Sui already has an IFFW guard, in `gas_charger.rs`:

`if execution_result.as_ref().err().map(|err| matches!(        err.kind(),        sui_types::execution_status::ExecutionErrorKind::InsufficientFundsForWithdraw    )).unwrap_or(false)    && matches!(gas_payment_location, Some(PaymentLocation::AddressBalance(_))){    return GasCostSummary::default();}`
This guard does two things: it triggers only when the **final gas charge location** (after smashing) is Address Balance, and it short-circuits the gas charge itself. It is about \*not double-charging the AB when the AB withdrawal failed\*. It says nothing about the `Split` events that smashing emitted for the non-primary entries before this guard runs. That is the seam the bug slipped through.

## Root cause

Two preconditions had to line up:

- The transaction had to be admitted at signing/certificate-check time. Pre-execution checks validate a coin reservation against the AB observed at signing time. If the sender's AB is 20M and the reservation is 10M, the check passes.
- By the time the transaction actually executes, another transaction had to have drained the AB to 0. In the regression test, this is achieved by submitting both transactions in a single soft bundle so the executor processes them in order in the same batch.

Given those, the adapter sees an insufficient AB during execution, sets `execution_params = Err(InsufficientFundsForWithdraw)`, and routes through the early-abort branch in `execution_engine.rs` so that no PTB body runs.

The problem: `GasCharger::new` runs **before** that abort branch is reached. Its constructor calls `payment_kind(&gas_data, ...)` → `PaymentKind::smash(...)` → `SmashMetadata::smash_gas(...)`, and that smashing pass walks every entry in `gas_data.payment`. For any coin-reservation entry it writes an `AccumulatorEvent::Split` into the `TemporaryStore`. Those events are part of the transaction's effects, even though the transaction itself is going to fail.

Concretely, with a `gas_data.payment` of `[real_coin_a, real_coin_b, coin_reservation(R)]`:

- The smash target is `real_coin_a` (a real coin), so `gas_payment_location` is `Coin`, not `AddressBalance`. The existing IFFW guard quoted above never fires.
- During smashing, `real_coin_b` is folded into `real_coin_a` and deleted. `coin_reservation(R)` is converted into a `Split` event of `R` against the sender's `Balance` accumulator.
- Execution then aborts with `InsufficientFundsForWithdraw`. Object writes are reset, but the accumulator event from smashing is already in the effects.

Checkpoint settlement now aggregates this transaction's effects. The sender's `Balance` accumulator picks up `merge = 0`, `split = R`. The settlement transaction calls `settle_u128`, which after netting calls `U128.update(0, R)`:

`u128.value = 0 + 0 - R;  // checked underflow → abort`
Move aborts the settlement system transaction. Because system transaction digests are derived deterministically from the checkpoint, every honest validator and full-node trying to apply that checkpoint hits the exact same abort. Settlement does not progress. Checkpoint application does not progress. Mainnet halts.

This is precisely the picture the second tweet describes: "a crash bug in the gas charging logic introduced by the 1.72 release." The 1.72 release introduced the Address Balance / coin-reservation gas-payment plumbing; the bug is a missing case in that plumbing for the IFFW early-abort path.

## Impact

The impact is liveness, not solvency. Concretely:

- **No funds were stolen and no balance was silently moved.** Move's checked arithmetic refused the underflow. The settlement transaction aborted \*instead of\* applying a bad update. The accumulator state on disk was never corrupted.
- **The chain stalled at the offending checkpoint.** Validators and full-nodes could not produce/apply the settlement transaction for that checkpoint, so the chain could not advance past it. End users observed transactions being "paused" as the first tweet described.
- **The condition was reachable by a non-privileged user.** Constructing the trigger required only the ability to fund an Address Balance and submit a soft bundle of two transactions with a particular gas-payment shape. Nothing here required validator keys, admin privileges, or unusual protocol-level access.
- **Resolution required a binary patch.** Because settlement transactions are deterministically derived from checkpoint contents and execution-layer logic, the only path forward was to deploy the patched adapter on every validator. The second tweet's "Activity on Sui mainnet has resumed" corresponds to the cluster being upgraded to the patched binary.

## The fix

The diff in `execution_engine.rs` changes `gas_data` from `GasData` to `mut GasData` in `execute_transaction_to_effects` and inserts this prune step before `GasCharger::new`:

``// On an IFFW abort, drop the address-balance gas payments (keeping real coins) so the// pruned list flows into `payment_kind`/`compute_input_reservations` with no special// handling.if matches!(    execution_params,    Err(ExecutionErrorKind::InsufficientFundsForWithdraw)) && gas_data.payment.len() > 1    && ParsedDigest::try_from(gas_data.payment[0].2).is_err(){    gas_data        .payment        .retain(|entry| ParsedDigest::try_from(entry.2).is_err());}``
Three things are worth highlighting about this patch:

**Where the cut happens.** The pruning runs before `payment_kind` and before `compute_input_reservations`. Both functions iterate `gas_data.payment` and classify reservation entries. By removing reservations upstream, the rest of the pipeline — `payment_kind`, gas smashing, input-reservation accounting, the final IFFW guard in `gas_charger.rs` — does not need any new IFFW-aware branches. There is exactly one decision point for this whole class of bug.

**What is kept vs. dropped.** Only coin-reservation entries (those whose digest \*does\* decode via `ParsedDigest::try_from`) are dropped. Real coin entries (where `ParsedDigest::try_from(...).is_err()`) are retained. The failing transaction therefore still has a valid gas-payment list and goes through normal gas charging, storage rebates, and effect generation. The user still pays for the failed attempt; only the spurious `Split` events disappear.

**The two preconditions.** The condition `gas_data.payment.len() > 1 && ParsedDigest::try_from(gas_data.payment[0].2).is_err()` matches exactly the dangerous shape: more than one payment entry, and the smash target is a real coin (so the existing IFFW guard in `gas_charger.rs` does \*not\* fire). If gas is paid purely from AB (smash target is itself a reservation), the older guard already short-circuits gas charging. If there is only one payment entry, there is nothing to smash.

The commit message also flags what was intentionally left out: "This is the unconditional fix only. The follow-up stacked PR adds the protocol-version + mainnet accumulator-version gating so the rollout is safe and mainnet replay stays bit-for-bit correct — kept separate so that gating diff reads cleanly against this fix."

This is the right call for an execution-layer change. Effects determinism is non-negotiable: replaying a historical checkpoint must produce byte-identical effects. Any change that alters the contents of `gas_data` mid-execution must be gated by protocol version so that pre-fix checkpoints replay the pre-fix behavior. The unconditional patch landed first because the bug was already taking down mainnet; the determinism-preserving gating ships in a clean follow-up.

## The regression test

The regression test `address_balance_compatibility_tests.rs` is the minimal reproducer, and its comments are unusually blunt about the impact:

- Enable coin reservations via a protocol-config override; build a test cluster.
- Fund the sender's AB with `initial_ab = 20_000_000`. Per-tx reservations must be `≤ initial_ab` to pass signing validation.
- **TX1**: pay gas from a real coin and withdraw the full `initial_ab` from AB to a dummy address. Succeeds and leaves AB at 0.
- **TX2**: `gas_data.payment = [real_coin_a, real_coin_b, coin_reservation(initial_ab / 2)]`. The reservation is structurally legal (`≤ initial_ab`), but the AB is 0 by the time TX2 runs. Two real coins are deliberately included so smashing would normally delete `real_coin_b`; the test transitively asserts (via SUI conservation) that this does not happen.
- Both transactions are submitted in `sign_and_execute_txns_in_soft_bundle` so the executor processes them in order in a single batch.
- The test asserts TX1 succeeds, TX2 fails with `InsufficientFundsForWithdraw`, and then calls `wait_for_tx_settlement(&[tx1_digest, tx2_digest])`. The wait is the actual failure surface — without the fix, settlement aborts.

The in-source comment makes the impact explicit: "Without the fix the settlement transaction aborts trying to split `reservation` from a 0-balance AB, crashing the node."

The final assertion `assert_eq!(final_ab, 0)` confirms that the failed TX2 did not touch the AB either way.

## Lessons

A few things make this incident more interesting than just "we forgot a case."

**Side effects of failed transactions are first-class state.** It is easy to assume that "the transaction failed" means "nothing in the temporary store matters." That is approximately true for object writes (the gas charger calls `reset` on error) and almost true for gas charging itself (Sui resets and re-smashes on certain failure paths). But `AccumulatorEvent`s created during smashing are part of effects and survive into checkpoint settlement. Any feature that adds new side-effect channels needs to audit \*every\* early-abort path. The fix is small precisely because the design — events emitted by smashing, applied later by a system transaction — was sound. The bug was a single missing case in the early-abort path.

**Reservations are not objects, and that matters.** A real gas coin can be smashed, mutated, deleted — operations that are reversible within a single tx's `TemporaryStore`. A coin reservation is a \*promise\* to withdraw from an accumulator that lives outside the transaction's owned-object set; it is materialized as an event that \*another\* (system) transaction will consume. Once that event is in the effects, only the settlement code can decide what to do about it — and the settlement code has no concept of "this came from a failed transaction." The right place to suppress it is at the source.

## Key Takeaways

##### Failed-tx side effects are real state

Smashing-emitted accumulator events survived the IFFW early-abort and made it into checkpoint settlement.

##### Move's checked arithmetic prevented a silent solvency bug

The underflow aborted settlement loudly rather than corrupting balances — turning a potential theft into a liveness incident.

##### Fix at the source, not at the sink

Pruning reservation entries from gas\_data before smashing is the correct layer; clamping or returning a bool in the Move settlement code would have hidden a real invariant violation.

##### Determinism-preserving rollout matters

The emergency fix landed unconditionally to restore mainnet; protocol-version gating ships separately to keep historical replay bit-for-bit correct.

## References

- Incident tweets: [stall announcement](https://x.com/SuiNetwork/status/2060005543406899294), [resumption announcement](https://x.com/SuiNetwork/status/2060097006610305368)
- Forward-port commit to `main`: [`124c64e`](https://github.com/MystenLabs/sui/commit/124c64e643a2fea059cb369cc6b96b565fadea7d) ("Land #26816 gas-underflow fix in main (#26828)")
- Original emergency fix: PR #26816 against `releases/sui-v1.72.0`
