# GHSA-4g5f-3gmm-9q87: Unsound emulated scalar multiplication on BLS12-381 / BW6-761 (exceptional GLV addition, missing subgroup checks)

| Field | Value |
| --- | --- |
| Repo | Consensys/gnark (Go ZK-SNARK library) |
| GHSA | GHSA-4g5f-3gmm-9q87 |
| CVE | none assigned |
| Severity | high |
| CWE | CWE-345, CWE-682 |
| Published | 2026-11-09T22:39:04Z |
| Affected | github.com/consensys/gnark < 0.16.5 (patched: >= 0.16.5) |
| Credits | DicksonWu654, Ectario, LeonPaulSchneider |
| Advisory URL | https://github.com/Consensys-Incorporated/gnark/security/advisories/GHSA-4g5f-3gmm-9q87 |
| Captured | 2026-11-12 (WAT) |

## Description (verbatim)

## Summary

In a circuit, `std/algebra/emulated/sw_emulated` `Curve.ScalarMul` on BLS12-381 G1 and BW6-761 G1 is not sound: a malicious prover can make `ScalarMul(P, s)` return a point other than `[s]P`. There are two independent causes:

1. **Exceptional addition in the classic GLV loop** (reported by Ectario). The GLV decomposition `s = s1 + λ·s2` comes from a prover hint. The circuit range-checks it and checks it modulo `r`, but nothing forces it to be the honest one. Some bounded dishonest decompositions make the main loop call the incomplete `doubleAndAdd(U, U)` with two equal inputs. The chord-slope constraint then becomes `λ·0 = 0`, so the slope is free and the prover chooses the output.
2. **No subgroup check on the input** (reported by Dickson Wu). The classic GLV branch does not check that `P` lies in the prime-order subgroup. The doc comment said an on-curve check was enough. For an on-curve point `P` outside the subgroup, a circuit that does `AssertIsOnCurve(P); AssertIsEqual(ScalarMul(P, s), Q)` accepts some `Q ≠ [s]P`.

The reporter demonstrated end-to-end Groth16 forgeries for both curves. On BLS12-381 the attack goes through the EVM precompile gadget `std/evmprecompiles.ECG1ScalarMulSumBLS` (EIP-2537 G1MSM). On BW6-761 it goes through the generic `ScalarMul`. The only thing the prover overrode was the decomposition hint.

While fixing these, we reviewed the related code paths and fixed further issues of the same kind. They are listed under "Related issues fixed in the same patch".

## Affected version

- Issues 1 and 2 on BLS12-381 / BW6-761 G1 through the default path: v0.16.0 – v0.16.4. `PreferClassicGLV` was introduced in v0.16.0.
- `sw_bw6761.AssertIsOnG2` 3-torsion: all versions that have the method.
- Incomplete-arithmetic and native-primitive issues: long-standing.

## Details

### 1. Exceptional addition in classic GLV (`scalarMulGLV`)

BLS12-381 G1 and BW6-761 G1 set `PreferClassicGLV: true`, so the default `ScalarMul`, `ScalarMulBase`, `JointScalarMul` and `MultiScalarMul` dispatch to `scalarMulGLV`. The hinted sub-scalars are only constrained by `signed(s1) + λ·signed(s2) ≡ s (mod r)` and their bit-length bounds. Any vector of the GLV lattice `{(a, b) : a + λb ≡ 0 mod r}` that is short enough to stay within the bounds can be added to the honest decomposition.

Here is the reporter's BLS12-381 vector:

- λ = 228988810152649578064853576960394133503
- s = 9(λ+1), with s1 = 2λ + 9 and s2 = 7

Both sub-scalars are positive and fit the 129-bit range, and the decomposition holds exactly. In the last loop iteration the accumulator doubles to `[3(λ+1)]P`. The table entry selected by the sub-scalar bits is `[3]P + [3]Φ(P)`, which is the same point. The incomplete `doubleAndAdd` therefore adds a point to itself, `ratioHint` returns 0 for the 0/0 slope, and the circuit is satisfied with an arbitrary result.

The main loop always used incomplete arithmetic. Complete (`AddUnified`) arithmetic was used only for the final low-bit corrections, even though the documentation said the default `ScalarMul` was complete. The same construction works on BW6-761 with a 189-bit signed decomposition.

### 2. Missing input subgroup check

The GLV+fake-GLV path already asserts subgroup membership, but the classic GLV path did not. On curves with a cofactor (BLS12-381 G1, BW6-761 G1), an on-curve point `P = P₀ + T` with a small-order component `T` lets the prover get an output inconsistent with `[s]P`. `PLONK` recursion and other callers feed proof elements into `MultiScalarMul` before any subgroup check, so this is reachable from proof inputs.

For BW6-761 G1 there was no in-circuit subgroup check at all: `AssertIsInSubgroup` panicked. One has been added.

## Related issues fixed in the same patch

These were found during the review of the reported code paths:

- **`sw_bw6761.Pairing.AssertIsOnG2` accepts points with a 3-torsion component.** It used the endomorphism relation `[x₀+1]Q == [−x₀³+x₀²−1]ϕ(Q)`. That relation has norm `3r`, and the G2 cofactor is divisible by 3. As a result, `Q + T` with `T = (0, ±2)` of order 3 passes the check. The Groth16 recursion verifier uses this check on the proof element `B` when subgroup checks are forced. The check now uses the exact relation `[w]([x₀²](ϕQ − Q) + [2]Q + ϕQ) == ϕ²(Q)` with `w = (x₀−1)/3`, whose norm is exactly `r`. `G2.ScalarMul` now checks its input in the same way. The native check in gnark-crypto had the same flaw and is fixed separately: gnark-crypto PR #931, which also covers BW6-633 G1.
- **Incomplete arithmetic paths in `sw_emulated` (opt-in via `algopts.WithIncompleteArithmetic`).** These affect secp256k1, BN254, BLS12-381 and other curves.
  - In `jointScalarMulGLVUnsafe`, a crafted decomposition forces an equal-input chord. We demonstrated this on secp256k1, BN254 and BLS12-381.
  - The incomplete merge in `MultiScalarMul` hits an equal-input chord even with honest hints. Example: points `(G, 2G, (3/2)G)` with scalars `(1, 1, 2)`.

  These modes were documented as "may be unsatisfiable on edge cases". In fact they could be satisfiable with a wrong result. All of their chords are now guarded by an x-coordinate inequality, so an edge case now makes the circuit unsatisfiable instead of returning a wrong result. On PreferClassicGLV curves, the incomplete option is now ignored and the complete path is used.
- **Native `sw_bls12377` (G1, G2) and `sw_grumpkin`: equal-input `AddAssign` / `DoubleAndAdd` and `Double` of a point with `y = 0`.**
  - These exported primitives used `DivUnchecked` for the slope. For `P == Q`, or for doubling a point with `y = 0`, the slope was unconstrained (0/0).
  - They now use checked division, so the slope is constrained. G2 checks the denominator is nonzero through its norm.
  - The default `ScalarMul` of `sw_bls12377` is not affected for G1 inputs.
  - In `sw_grumpkin`, `ScalarMul` uses a generator offset. An equal-input step is reachable for inputs `Q = [q]G` with a specific `q`. LeonPaulSchneider independently reported this with an end-to-end PLONK forgery of the default `ScalarMul`.

## Proof of concept

The reporter's BLS12-381 vector is given under Details: s = 9(λ+1), with s1 = 2λ + 9 and s2 = 7. Overriding only the GLV decomposition hint with these values makes `ScalarMul(P, s)` satisfiable with an output other than `[s]P`.

The regression tests below reproduce every issue. With `test.IsSolved` and a hint override, each test shows that the unpatched circuit accepts a wrong result, and that the honest control is rejected where applicable:

- `TestClassicGLVExceptionalAddForgery` (BLS12-381, BW6-761)
- `TestClassicGLVOffSubgroupInput` (BLS12-381, BW6-761)
- `TestAssertIsOnG2Torsion` and `TestScalarMulG2OffSubgroupInput` (BW6-761 G2)
- `TestJointScalarMulGLVUnsafeForgery` and `TestMultiScalarMulIncompleteMergeForgery` (incomplete arithmetic)
- `TestChordEqualInputs` and `TestDoubleInfinity` (native BLS12-377, grumpkin)

## Impact

A circuit that uses any of the following can accept a proof for a statement where the computed point is not `[s]P`:

- `sw_emulated` scalar multiplication on BLS12-381 G1 or BW6-761 G1: `ScalarMul`, `ScalarMulBase`, `JointScalarMul`, `MultiScalarMul`. This includes BLS12-381 G1 in `sw_bls12381`, `std/evmprecompiles` `ECG1ScalarMulSumBLS`, and emulated KZG / PLONK / Groth16 recursion over these curves.
- `sw_bw6761` `AssertIsOnG2` / `G2.ScalarMul`.
- The incomplete-arithmetic options above, or the native primitives listed above, when inputs are attacker-controlled.

Depending on the application, this can allow forged precompile results, forged signature or commitment checks, or forged recursive proof verification. Circuits on BN254 or secp256k1 that use the default (complete) arithmetic are **not** affected by issue 1 or 2. Their default path is GLV+fake-GLV, which we analysed and found sound.

## Is this vulnerability public or being exploited?

No. The issues were reported privately, and we are not aware of any exploitation.

## Patches

Fixed in [v0.16.5](https://github.com/Consensys-Incorporated/gnark/releases/tag/v0.16.5), commit [`ecbe370`](https://github.com/Consensys-Incorporated/gnark/commit/ecbe370034d2c8debb6520382b64f604026ac22b). The native gnark-crypto BW6-761 G2 / BW6-633 G1 subgroup check is fixed in [Consensys-Incorporated/gnark-crypto#931](https://github.com/Consensys-Incorporated/gnark-crypto/pull/931) (commit [`c1cb9b4`](https://github.com/Consensys-Incorporated/gnark-crypto/commit/c1cb9b4629e659854a1be51aeffae7302870176c)); gnark v0.16.5 depends on a gnark-crypto version that includes it.

- **Classic GLV.** Every accumulator gets a fixed point `T₀` of small odd prime order outside G1 added to it: order 3 on BLS12-381, order 127 on BW6-761. The known final multiple of `T₀` is removed with complete addition. For an input in G1, every accumulator has the form `G + [c]T₀` with `c ≢ 0`, so no loop step can be exceptional, whatever decomposition the prover supplies.
- **Input subgroup check.** `scalarMulGLV` now asserts that the input is in the subgroup, unless the caller passes `algopts.WithNoSubgroupMembershipCheck()` after checking membership itself. Constant inputs are checked at compile time. BW6-761 G1 now has an in-circuit endomorphism subgroup check. Its relation is exact on G1, since gcd(h₁, N) = 1.
- **BW6-761 G2.** The subgroup relation is replaced with the exact one described above.
- **Incomplete paths.** All chords are guarded.
- **Native `sw_bls12377` / `sw_grumpkin`.** The slope divisions are checked.
- **Documentation.** Doc comments are corrected to state the actual preconditions.

Regression tests fail on the unpatched code and pass after the fix:

- `std/algebra/emulated/sw_emulated/classic_glv_test.go`
- `std/algebra/emulated/sw_emulated/joint_glv_unsafe_test.go`
- `std/algebra/emulated/sw_bw6761/g1_membership_test.go`
- `std/algebra/emulated/sw_bw6761/g2_membership_test.go`
- `std/algebra/native/sw_bls12377/chord_guard_test.go`
- `std/algebra/native/sw_grumpkin/chord_guard_test.go`
- `std/algebra/native/sw_grumpkin/glv_offset_test.go`

### Constraint impact (R1CS)

| Operation | Before | After | After, with `WithNoSubgroupMembershipCheck` |
|---|---:|---:|---:|
| BLS12-381 G1 `ScalarMul` | 136,537 | 193,048 | 138,980 |
| BW6-761 G1 `ScalarMul` | 371,608 | 743,186 | 376,325 |
| BW6-761 G2 `ScalarMul` | 371,608 | 670,000 | — |
| BW6-761 `AssertIsOnG2` | 357,082 | 360,064 | — |
| secp256k1 / BN254 incomplete joint scalar mul | | +10.3% | |
| BLS12-377 native G1 / G2 `ScalarMul` | 1,514 / 3,541 | 1,642 / 3,925 | |
| Grumpkin native `ScalarMul` | 2,216 | 2,345 | |

Most of the increase comes from the new subgroup check. Callers that already check membership, for example with `AssertIsOnG1`, can pass `algopts.WithNoSubgroupMembershipCheck()`. The EIP-2537 precompile gadget now does this.

## Workarounds

There is no workaround for issue 1 other than upgrading. For issue 2, call `AssertIsInSubgroup` (BLS12-381) on every input point before scalar multiplication. Do not use `WithIncompleteArithmetic` with inputs that may be adversarial.

## Credits

- Ectario: classic GLV exceptional addition and end-to-end forgeries.
- Dickson Wu: missing subgroup check in the classic GLV branch.
- LeonPaulSchneider: `sw_grumpkin` `ScalarMul` 0/0 slope forgery.



