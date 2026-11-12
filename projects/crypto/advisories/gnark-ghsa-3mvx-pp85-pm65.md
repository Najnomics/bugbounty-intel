# GHSA-3mvx-pp85-pm65: Soundness issues in gnark/std circuit components

| Field | Value |
| --- | --- |
| Repo | Consensys/gnark (Go ZK-SNARK library) |
| GHSA | GHSA-3mvx-pp85-pm65 |
| CVE | none assigned |
| Severity | critical |
| CWE | n/a |
| Published | 2026-08-24T18:12:59Z |
| Affected | github.com/consensys/gnark <v0.16.2 (patched: >=v0.16.2) |
| Credits | n/a |
| Advisory URL | https://github.com/Consensys-Incorporated/gnark/security/advisories/GHSA-3mvx-pp85-pm65 |
| Captured | 2026-11-12 (WAT) |

## Description (verbatim)

## Summary

A set of independent soundness bugs were found across gnark's standard
library gadgets. The common thread is **hint outputs that are consumed by the
constraint system without a binding or range constraint**, letting a malicious
prover substitute forged witness values that satisfy every constraint while
encoding a false statement. Each bug is independently exploitable; several
compose into the building blocks of higher-level protocols (KZG openings,
Pedersen commitments, BLS signatures, EVM precompiles, recursive verifiers,
hash-based transcripts).

Affected consumers include `std/commitments/kzg`, `std/commitments/pedersen`,
`std/signature/bls`, `std/signature/ecdsa`, `std/evmprecompiles` (MODEXP,
BLS12_G1MSM, KZG point evaluation), `std/recursion`, and the SHA-2 / SHA-3 /
Keccak / RIPEMD-160 hash gadgets built on `std/math/uints`.

---

## Fixed vulnerabilities

### 1. Unconstrained carry in emulated-field deferred checks — CRITICAL

**Component:** `std/math/emulated` (`Mul`, `MulMod`, `AssertIsEqual`, `Reduce`,
`Div`, `Inverse`, `Sqrt`, `Eval`, `ModMul`, `ModAssertIsEqual`), transitively all
of `std/algebra/emulated` and `std/evmprecompiles`.

The deferred multiplication / zero / evaluation checks verify
`a(X)·b(X) = r(X) + k(X)·p(X) + (2^t − X)·c(X)` at a random challenge `γ` in the
native field `q`. The carry polynomial `c` came from a hint and was **never
range-checked**. A malicious prover picks the quotient `k` and carry `c` so the
two sides differ by a multiple of the native modulus `q`; that difference
vanishes mod `q` at *every* challenge, so the Schwartz–Zippel check passes
identically for a false statement. Demonstrated end-to-end (setup → prove →
verify) on BN254, BLS12-377, BLS12-381 and BW6-761, on both Groth16 and PLONK.

**Fix:** per-call honest carry bounds (`mulCarryBound` / `mvCarryBound`), a
batched signed range check over all committed carry limbs inside the deferred
multicommit callback, a tightened overflow ceiling
(`maxOverflowReducedResult`), and a hard `carryMaxBits` guardrail for the
previously-silent extreme regime.

---

### 2. BLS12-377 torus `PairingCheck` is vacuous — CRITICAL

**Component:** `std/algebra/native/sw_bls12377` (torus-based pairing), reached
from `std/commitments/kzg`, `std/commitments/pedersen`, `std/signature/bls`.

The torus scaling factor `s` was read from a hint and never constrained. The
single `E6` verification equation is affine-linear in `s`, so a prover solves
for `s` for **any** `P, Q`, making the pairing check accept false statements.
Breaks KZG/Pedersen openings and BLS signature verification in the
BLS12-377-in-BW6-761 recursion stack.

**Fix:** the torus-compressed path was removed; the check uses the
over-determined `E12` form in which `s` is fully constrained.

---

### 3. Grumpkin scalar multiplication: GLV decomposition not bound to the scalar — CRITICAL

**Component:** `std/algebra/native/sw_grumpkin` (`ScalarMul`, `ScalarMulBase`,
`MultiScalarMul`, joint GLV).

The GLV sub-scalars `s1, s2` were tied only to an unconstrained hint value
`semu` (`s1 − λ·s2 ≡ semu`), never to the actual scalar variable `s`. The
circuit computed `[s1 − λ·s2]Q` for arbitrary prover-chosen `s1, s2` — an
arbitrary multiple of `Q` unrelated to `s`. Verified: `ScalarMul(P, 12345)`
proven equal to `[999999]P`.

**Fix:** recompose the scalar in the native field from the canonical bit
decomposition and bind `semu` to `s` (`api.ToBinary` → `FromBits`), eliminating
the free hint value.

---

### 4. Variable-modulus remainder not reduced mod the runtime modulus — CRITICAL

**Component:** `std/math/emulated` (`ModMul`, `ModExp`, `ModAssertIsEqual`),
reachable via `std/evmprecompiles/05-expmod.go` (EIP-198).

For custom-modulus operations the remainder limbs were range-checked against the
*type* modulus width, not the *runtime* modulus `m` (a witness). A prover
returns `r' = (a·b mod m) + m`, congruent to the true result and passing every
check but non-canonical. Even the *honest* hint could return `r + m`
(malleability). Breaks RSA/CRT/verification logic that assumes a unique
representative.

**Fix:** `Field.assertLessThanModulus` performs a runtime-modulus bound check;
applied to `ModExp`'s output and exposed as `Field.ModMulCanonical`.

---

### 5. BLS12-381 scalar multiplication admits a small-torsion (cofactor) offset — CRITICAL

**Component:** `std/algebra/emulated/sw_emulated`
(`scalarMulGLVAndFakeGLV`), reachable via `std/evmprecompiles/12-blsg1msm.go`
(EIP-2537) and any BLS12-381 G1 scalar mul.

The GLV+fake-GLV check verifies `[V](Q − [s]P) = O` on the full curve
`E(Fp)`, whose order is `h·r` with `h` divisible by `3²` for BLS12-381 G1.
`V ≢ 0 mod r` does not force the torsion component of `Q − [s]P` to vanish, so a
prover returns `[s]P + T₀` for a 3-torsion point `T₀` and passes all
constraints.

**Fix:** cofactor-clearing subgroup binding (`CofactorClearing` constants,
widened to all reachable primes), and routing all BLS12-381 G1 public paths
through classic GLV whose computed output is inherently in-subgroup.

---

### 6. GLV Φ-table carries the wrong sub-scalar sign — CRITICAL

**Component:** `std/algebra/emulated/sw_emulated` (`scalarMulGLV` and
`jointScalarMulGLVUnsafe`), reachable on BLS12-381 G1 (complete mode) and all
GLV curves in incomplete mode.

The Φ-table entries were built by re-signing the *non-Φ* table, so the `[3]Φ(Q)`
entry picked up the sign of the *first* sub-scalar `s1` as a spurious factor.
Because the circuit only pins `±s1 + λ·(±s2) ≡ s (mod r)` with both
`|si| < 2^nbits`, a prover selects a malicious lattice representation with
`s1 < 0` and gets a wrong accumulator accepted. Verified end-to-end on BLS12-381
G1.

**Fix:** `tablePhiQ[2]` is now derived from `triple(tablePhiQ[1])` so each Φ
entry carries only its own sub-scalar's sign.

---

### 7. `AssertFinalExponentiationIsOne` accepts the all-zero residue witness — HIGH

**Component:** `std/algebra/emulated/sw_bn254` and
`std/algebra/emulated/sw_bls12381` (and the classical native BLS12-377 path).

The check verifies `x · cubicNonResiduePower == residueWitness^λ` but never
constrains `residueWitness ≠ 0`. The all-zero hint satisfies `0 == 0` for any
`x`, so the exported method proved nothing about `x`.

**Fix:** the residue witness is constrained invertible (`Inverse`, asserting
`w·w⁻¹ == 1`).

---

### 8. Byte-wise ops (`uints`) result not range-checked — table-key collision — HIGH

**Component:** `std/math/uints` (`twoArgFn`, `Not`), consumed by SHA-2, SHA-3 /
Keccak, RIPEMD-160, BLS-signature and EVM-KZG gadgets.

`twoArgFn` packs the table key linearly as `a + 2^8·b + 2^16·c` and trusted that
the lookup result is in range. The log-derivative argument only constrains
*membership of the packed value*, which cannot distinguish an in-range `c` from
an out-of-range `c` that collides with a valid key: `Xor(1,0)` committed as
`1/256` gives `1 + 0 + 2^16/256 = 257 = 0x000101`, the valid key for
`(a=1,b=0,c=1)`; `And(1, 1/256) := 0` gives `2 = 0x000002`, the valid key for
`(1,0,0)`. Net effect: the circuit "proves" `1 & (1 ^ 0) == 0`. PoC-confirmed
on Groth16 and PLONK.

**Fix:** range-check the result of every table query (`bf.rchecker.Check(ret,
8)`) before packing, in `twoArgFn` and `Not`.

---

### 9. Pairing Miller loop divides by zero when `Q = 0` — HIGH

**Component:** `std/algebra/emulated/sw_bls12381`, `sw_bn254`, `sw_bw6761`, and
native `sw_bls12377` pairing code.

A zero/`(0,0)` `Q` (or a `Q` at infinity mishandled by the affine Miller loop)
makes the line-evaluation `DivUnchecked` a `0/0` at every loop step, turning the
line coefficients into free prover variables and the pairing value
prover-controlled.

**Fix:** `Q = 0` produces deterministic line coefficients; division-by-zero is
guarded.

---

### 10. Wrong exponent in BW6-761 `finalExpHint` — HIGH

**Component:** `std/algebra/emulated/fields_bw6761` / `sw_bw6761`.

The final-exponentiation hint used an incorrect exponent (misplaced Frobenius
and flipped sign relative to the circuit relation), so the witness did not match
the value the circuit checked.

**Fix:** the exponent in `finalExpHint` was corrected to match the circuit.

---

### 11. Top recode bit unconstrained in native fixed-base scalar multiplication — MEDIUM

**Component:** `std/algebra/native/sw_bls12377` (fixed-base comb scalar mul).

The scalar recoding pinned `2c + b0 = s + 2^n` over the integers but left the
top bit of `c` unconstrained, permitting a native-field wrap-around. Constraining
the top bit to `1` proves `2c + b0 ≥ 2^n` and excludes the wrap.

**Fix:** constrain the top recode bit.


---

## Credit

Internal Consensys security audit (August 2026) and community reporter(s).
Special thanks to zkSecurity and zkao for some bug reports.

