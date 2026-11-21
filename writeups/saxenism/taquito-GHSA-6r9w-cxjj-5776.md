# taquito-GHSA-6r9w-cxjj-5776

- **Source URL:** https://github.com/ecadlabs/taquito/security/advisories/GHSA-6r9w-cxjj-5776
- **Fetched:** 2026-11-21
- **Researcher:** saxenism
- **Method:** curl + trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---

### Summary

In `@taquito/sapling` (`<= 25.1.2`), `SaplingTransactionBuilder` reused a single commitment trapdoor (`rcm`) across every output description in a shielded or Sapling transaction (including the sender's automatic payback/change output) and reused a single spend rerandomizer (`ar`) across all spend inputs in `prepareSaplingSpendDescription`.

In a multi-output transaction (`createShieldedTx` or `createSaplingTx`), any recipient who decrypted their own output note obtained the shared `rcm` and could recompute `cmu = ValueCommitment(value, rcm)` for candidate co-payee `(address, value)` pairs against the other public `cm` values in the same transaction.

### Technical Details

1. **Output Commitment Trapdoor (`rcm`) Reuse:**  - In `SaplingTransactionBuilder.createShieldedTx()` and `SaplingTransactionBuilder.createSaplingTx()` (`packages/taquito-sapling/src/sapling-tx-builder.ts`), `await sapling.getRandomCommitmentTrapdoor()` was called once at the top of the transaction builder and passed inside `Omit<ParametersSaplingOutputDescription, 'amount' | 'paymentAddress' | 'memo'>` to `prepareSaplingOutputDescription()`.
  - `prepareSaplingOutputDescription()` mapped over `outputs` (plus the payback/change output added when input balance exceeded the sum of outputs) and passed the same `randomCommitmentTrapdoor` into `sapling.preparePartialOutputDescription()` and `this.encryptPlainText()` for every output.
  - Because the output note plaintext encrypted under `K_enc` contains `(diversifier, value, rcm, memo)`, any recipient in the transaction learned `rcm` upon decrypting their own note. If that recipient knew or could enumerate candidate `(paymentAddress, amount)` pairs for another output in the same transaction, they could compute the candidate note commitment with the shared `rcm` and compare it directly against the public `cm` field on-chain.
2. **Spend Public Key Rerandomization (`ar`) Reuse:**  - In `SaplingTransactionBuilder.prepareSaplingSpendDescription()`, `await sapling.getRandomPublicKeyReRandomization()` was sampled once outside the `inputsToSpend` loop and reused across every `sapling.prepareSpendDescription()` call in a multi-input spend.

### Practical Impact and Scope

- **Single-recipient exact-balance transactions:** Unaffected by co-recipient `rcm` disclosure (only one output exists).
- **Single-recipient transactions with change:** The recipient learned the `rcm` also used for the sender's payback/change output; if the recipient already knew the sender's Sapling address, they could test candidate change amounts against the payback output's commitment.
- **Multi-recipient transactions:** A co-recipient could test candidate `(paymentAddress, amount)` pairs for other outputs in the same transaction.
- **External observers (non-recipients):** Unaffected by `rcm` reuse, as `rcm` remains encrypted inside the note ciphertexts.
- **Mainnet exposure:** On Tezos mainnet, Sapling pools have negligible real-world transaction volume, making practical exploitation in production largely academic.

### Patches

Fixed in `@taquito/sapling@25.1.3` on `release/v25.1.x` ([PR #3588](https://github.com/ecadlabs/taquito/pull/3588), commit [`dcf8514b`](https://github.com/ecadlabs/taquito/commit/dcf8514b06b54b2c4baeb3bb284f0318ab459ab4)) and on `main` ([PR #3587](https://github.com/ecadlabs/taquito/pull/3587), commit [`80d22c4f`](https://github.com/ecadlabs/taquito/commit/80d22c4f3143b5ab254be6b9840c0932eb1ae91c)):

- `prepareSaplingOutputDescription()` now calls `await sapling.getRandomCommitmentTrapdoor()` inside the per-output loop so every recipient output and any payback/change output receives an independent `rcm`.
- `prepareSaplingSpendDescription()` now calls `await sapling.getRandomPublicKeyReRandomization()` inside the per-input loop so every spend description receives an independent rerandomizer.

### Timeline

- **2026-11-13:** Issue identified by Rahul Saxena (Bluethroat Labs).
- **2026-11-15:** Validated locally by the reporter against a private Octez 25.3 / `PtUshuai` (`U025`) sandbox (`tezos-taquito-sapling-two-payee-privacy-v3-20261115.zip`) and submitted to `security@tezos.com`.
- **2026-11-20 14:23 UTC:** `security@tezos.com` forwarded a summary of the 2026-11-15 report to `security@ecadlabs.com`.
- **2026-11-20 15:20 UTC:** Fix PRs opened by ECAD Labs on `main` ([#3587](https://github.com/ecadlabs/taquito/pull/3587)) and `release/v25.1.x` ([#3588](https://github.com/ecadlabs/taquito/pull/3588)).
- **2026-11-20 15:34 UTC:** Reporter shared the original reproduction bundle (`tezos-taquito-sapling-two-payee-privacy-v3-20261115.zip`) directly with ECAD Labs.
- **2026-11-20 16:40 UTC:** Reporter independently verified both fix branches (`dcf8514b` and `80d22c4f`) against the Octez 25.3 / `U025` replay harness.
- **2026-11-20 17:00 UTC:** `@taquito/sapling@25.1.3` published to npm (`latest`) and GitHub ([`v25.1.3`](https://github.com/ecadlabs/taquito/releases/tag/v25.1.3)).

To avoid routing delays on future reports affecting `@taquito/*` or `@ecadlabs/beacon-*`, researchers are encouraged to include `security@ecadlabs.com` directly when submitting reports.

### Downstream Fork Status

Downstream forks of `@taquito/sapling` (including `@tezos-x/octez.js-sapling` `<= 25.0.1` and `<= 25.1.0-rc.1`) inherited the same `SaplingTransactionBuilder` implementation and had not published a fix at the time of this advisory.

### Credits

Discovered, reported, and independently verified against the patched branches by **[Rahul Saxena (@saxenism)](https://x.com/saxenism)** of **[Bluethroat Labs](https://bluethroatlabs.com/)**.

## Summary

In

`@taquito/sapling`(`<= 25.1.2`),`SaplingTransactionBuilder`reused a single commitment trapdoor (`rcm`) across every output description in a shielded or Sapling transaction (including the sender's automatic payback/change output) and reused a single spend rerandomizer (`ar`) across all spend inputs in`prepareSaplingSpendDescription`.
In a multi-output transaction (

`createShieldedTx`or`createSaplingTx`), any recipient who decrypted their own output note obtained the shared`rcm`and could recompute`cmu = ValueCommitment(value, rcm)`for candidate co-payee`(address, value)`pairs against the other public`cm`values in the same transaction.
## Technical Details

Output Commitment Trapdoor (`rcm`) Reuse:`SaplingTransactionBuilder.createShieldedTx()`and`SaplingTransactionBuilder.createSaplingTx()`(`packages/taquito-sapling/src/sapling-tx-builder.ts`),`await sapling.getRandomCommitmentTrapdoor()`was called once at the top of the transaction builder and passed inside`Omit<ParametersSaplingOutputDescription, 'amount' | 'paymentAddress' | 'memo'>`to`prepareSaplingOutputDescription()`.`prepareSaplingOutputDescription()`mapped over`outputs`(plus the payback/change output added when input balance exceeded the sum of outputs) and passed the same`randomCommitmentTrapdoor`into`sapling.preparePartialOutputDescription()`and`this.encryptPlainText()`for every output.`K_enc`contains`(diversifier, value, rcm, memo)`, any recipient in the transaction learned`rcm`upon decrypting their own note. If that recipient knew or could enumerate candidate`(paymentAddress, amount)`pairs for another output in the same transaction, they could compute the candidate note commitment with the shared`rcm`and compare it directly against the public`cm`field on-chain.Spend Public Key Rerandomization (`ar`) Reuse:`SaplingTransactionBuilder.prepareSaplingSpendDescription()`,`await sapling.getRandomPublicKeyReRandomization()`was sampled once outside the`inputsToSpend`loop and reused across every`sapling.prepareSpendDescription()`call in a multi-input spend.
## Practical Impact and Scope

Single-recipient exact-balance transactions:Unaffected by co-recipient`rcm`disclosure (only one output exists).Single-recipient transactions with change:The recipient learned the`rcm`also used for the sender's payback/change output; if the recipient already knew the sender's Sapling address, they could test candidate change amounts against the payback output's commitment.Multi-recipient transactions:A co-recipient could test candidate`(paymentAddress, amount)`pairs for other outputs in the same transaction.External observers (non-recipients):Unaffected by`rcm`reuse, as`rcm`remains encrypted inside the note ciphertexts.Mainnet exposure:On Tezos mainnet, Sapling pools have negligible real-world transaction volume, making practical exploitation in production largely academic.
## Patches

Fixed in

`@taquito/sapling@25.1.3`on`release/v25.1.x`(PR #3588, commit`dcf8514b`) and on`main`(PR #3587, commit`80d22c4f`):`prepareSaplingOutputDescription()`now calls`await sapling.getRandomCommitmentTrapdoor()`inside the per-output loop so every recipient output and any payback/change output receives an independent`rcm`.`prepareSaplingSpendDescription()`now calls`await sapling.getRandomPublicKeyReRandomization()`inside the per-input loop so every spend description receives an independent rerandomizer.
## Timeline

2026-11-13:Issue identified by Rahul Saxena (Bluethroat Labs).2026-11-15:Validated locally by the reporter against a private Octez 25.3 /`PtUshuai`(`U025`) sandbox (`tezos-taquito-sapling-two-payee-privacy-v3-20261115.zip`) and submitted to`security@tezos.com`.2026-11-20 14:23 UTC:`security@tezos.com`forwarded a summary of the 2026-11-15 report to`security@ecadlabs.com`.2026-11-20 15:20 UTC:Fix PRs opened by ECAD Labs on`main`(#3587) and`release/v25.1.x`(#3588).2026-11-20 15:34 UTC:Reporter shared the original reproduction bundle (`tezos-taquito-sapling-two-payee-privacy-v3-20261115.zip`) directly with ECAD Labs.2026-11-20 16:40 UTC:Reporter independently verified both fix branches (`dcf8514b`and`80d22c4f`) against the Octez 25.3 /`U025`replay harness.2026-11-20 17:00 UTC:`@taquito/sapling@25.1.3`published to npm (`latest`) and GitHub (`v25.1.3`).
To avoid routing delays on future reports affecting

`@taquito/*`or`@ecadlabs/beacon-*`, researchers are encouraged to include`security@ecadlabs.com`directly when submitting reports.
## Downstream Fork Status

Downstream forks of

`@taquito/sapling`(including`@tezos-x/octez.js-sapling``<= 25.0.1`and`<= 25.1.0-rc.1`) inherited the same`SaplingTransactionBuilder`implementation and had not published a fix at the time of this advisory.
## Credits

Discovered, reported, and independently verified against the patched branches by

Rahul Saxena (@saxenism)ofBluethroat Labs.
