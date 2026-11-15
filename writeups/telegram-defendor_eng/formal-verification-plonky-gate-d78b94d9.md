# 🛡 Zellic Formally Verified Plonky2 Gates for Lighter

- **Source URL:** https://www.zellic.io/blog/formal-verification-plonky-gate
- **Fetched:** 2026-11-15
- **Channel:** @defendor_eng
- **Telegram message:** https://t.me/defendor_eng/1728 (id 1728)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
Formal verification provides mathematical guarantees that constraints correctly enforce their intended computation.
In this post, we describe our approach to formally verifying arithmetic circuits.
We illustrate this with an example from an engagement with [Lighter↗](https://lighter.xyz), a decentralized exchange with fully verifiable trading operations.
The example verifies a gate written in [Plonky2↗](https://crates.io/crates/plonky2) (a recursive proof system by Polygon).

## What Is a Gate?[](https://www.zellic.io/blog/formal-verification-plonky-gate#what-is-a-gate)

In Plonky2, a *gate* is the fundamental building block of a circuit.
Each gate defines a set of polynomial constraints that must be satisfied by the witness values.
Gates encode small computational steps, like integer addition and multiplication.

The complete witness for a circuit is organized as a two-dimensional table.
Multiple *rows*, each containing a fixed number of *wire* values.
A gate operates on a single row at a time, so when reasoning about gate constraints, we can focus on one-dimensional vectors of wire values.
For the formal verification of a gate, we can therefore focus on a single row.

The entire circuit is constructed by combining many gates together. Complex business-logic computations are broken down into thousands of individual gate operations, each enforcing a small piece of the overall logic. The circuit’s correctness depends on the correctness of these building blocks. If a single gate has a bug in its constraint definitions, the entire circuit could be vulnerable. A malicious prover might exploit the flaw to generate valid proofs for false statements. By proving that each gate correctly enforces its intended behavior, we establish a foundation of trust that propagates to the entire circuit.

Because rows have a fixed width, but many gates require fewer wires than this fixed length, gates use *slots* to pack multiple independent computations into a single row.
For example, if a row has 80 wires and a U32 addition needs only 20 wires, the gate can have four slots performing four independent additions in parallel within the same row.
For clarity, our presentation focuses on a single slot, but the verification approach generalizes to all slots.

We present as an example the verification of the `U32AddManyGate`.
This gate computes the sum of multiple 32-bit unsigned integers and is representative of the verification approach we used for all gates used in Lighter’s project.

### Why U32 Addition Needs a Dedicated Gate[](https://www.zellic.io/blog/formal-verification-plonky-gate#why-u32-addition-needs-a-dedicated-gate)

The circuit internally employs a finite field for its computations.
We call this the *native field* of the circuit.
Addition in circuits is inherently cheap when working with native field elements.
This addition has the drawback that it wraps at the *characteristic prime $p$* of the native field.
But most business-logic build needs non-wrapping addition.
To build more complete non-wrapping arithmetic computations, Lighter uses *32-bit unsigned integer* addition, which introduces two challenges:

1. **Multi-limb output.** The sum of multiple 32-bit integers does not fit in 32 bits.
For example, adding two values near $2^{32}$ produces a result approaching $2 \times 2^{32}$.
The gate must split this into a 32-bit sum and a carry and prove that both parts are correctly bounded.
2. **Field overflow.** Plonky2 uses the Goldilocks field ($p = 2^{64} - 2^{32} + 1$).
While this is large enough to hold intermediate sums without wrapping, the circuit must *prove* that the declared sum and carry are correct.
Without range checks, a malicious prover could exploit field arithmetic to produce incorrect outputs that satisfy the constraints.

The `U32AddManyGate` addresses both challenges.
It enforces the arithmetic relationship $\texttt{carryOut} \times 2^{32} + \texttt{sum} = \texttt{carryIn} + \sum_i \texttt{addends[i]}$ and uses limb decomposition with range checks to prove that $\texttt{sum}$ and $\texttt{carryOut}$ are properly bounded integers.

In general, the size of the native field limits the number of addends. The constraints on the output limbs must ensure that the output computation does not wrap. If the addition result cannot be represented by the available output limbs, no valid witness exists. This is a completeness problem: an honest prover would be unable to generate a valid proof. However, this is not a practical concern. With a nearly 64-bit prime like the Goldilocks prime, one can safely add approximately $2^{32}$ numbers before this becomes an issue.

## Overview of the Approach[](https://www.zellic.io/blog/formal-verification-plonky-gate#overview-of-the-approach)

Our verification strategy has four main components:

1. **Export the constraints.** We wrote a Rust exporter that extracts the polynomial constraints from Plonky2’s gate implementation and generates Lean definitions.
2. **Generalize the exports.** We created constraint generating functions that specialized to the exports of the gate constraints for all parameters the gate was instantiated with.
3. **Write a specification.** We wrote human-readable definitions in Lean that capture what the gate *should* compute, independent of the circuit implementation.
4. **Prove soundness and completeness.** We proved that
  - if the constraints are satisfied, then the specification holds (**soundness**).
  - if the specification holds, there exist witness values that satisfy the constraints (**completeness**).

## 1. Exporting the Constraints[](https://www.zellic.io/blog/formal-verification-plonky-gate#1-exporting-the-constraints)

Plonky2 gates are defined in Rust and define polynomial constraints functions that must equal zero for valid witnesses. The first step is to extract the constraint polynomials from these functions into Lean definitions that we can reason about.

We built a Rust exporter that symbolically evaluates the gate’s `eval_unfiltered` method.
Here is an example of the exported constraints for a `U32AddManyGate` with two addends:

```
import Mathlib.Data.Fin.VecNotation
import Mathlib.Data.ZMod.Defs
import LighterCore.Gate
/-!
U32AddManyGate
- num_addends = 2
- num_ops = 1
-/
namespace LighterExportGate.U32AddManyGate
set_option linter.style.longLine false in
def constraints_2_1 : LighterCore.Gate.WireAssertions (ZMod 18446744069414584321) 0 23 21 :=
  fun _c w => ![
    -- Arithmetic constraint
    (((w 4 * 4294967296) + w 3) - ((w 0 + w 1) + w 2)) = 0,
    -- Limb range checks
    (((w 22 * (w 22 - 1)) * (w 22 - 2)) * (w 22 - 3)) = 0,
    (((w 21 * (w 21 - 1)) * (w 21 - 2)) * (w 21 - 3)) = 0,
    (((w 20 * (w 20 - 1)) * (w 20 - 2)) * (w 20 - 3)) = 0,
    (((w 19 * (w 19 - 1)) * (w 19 - 2)) * (w 19 - 3)) = 0,
    (((w 18 * (w 18 - 1)) * (w 18 - 2)) * (w 18 - 3)) = 0,
    (((w 17 * (w 17 - 1)) * (w 17 - 2)) * (w 17 - 3)) = 0,
    (((w 16 * (w 16 - 1)) * (w 16 - 2)) * (w 16 - 3)) = 0,
    (((w 15 * (w 15 - 1)) * (w 15 - 2)) * (w 15 - 3)) = 0,
    (((w 14 * (w 14 - 1)) * (w 14 - 2)) * (w 14 - 3)) = 0,
    (((w 13 * (w 13 - 1)) * (w 13 - 2)) * (w 13 - 3)) = 0,
    (((w 12 * (w 12 - 1)) * (w 12 - 2)) * (w 12 - 3)) = 0,
    (((w 11 * (w 11 - 1)) * (w 11 - 2)) * (w 11 - 3)) = 0,
    (((w 10 * (w 10 - 1)) * (w 10 - 2)) * (w 10 - 3)) = 0,
    (((w 9 * (w 9 - 1)) * (w 9 - 2)) * (w 9 - 3)) = 0,
    (((w 8 * (w 8 - 1)) * (w 8 - 2)) * (w 8 - 3)) = 0,
    (((w 7 * (w 7 - 1)) * (w 7 - 2)) * (w 7 - 3)) = 0,
    (((w 6 * (w 6 - 1)) * (w 6 - 2)) * (w 6 - 3)) = 0,
    (((w 5 * (w 5 - 1)) * (w 5 - 2)) * (w 5 - 3)) = 0,
    -- Limb reconstruction
    ((
      (4 * ((4 * ((4 * ((
        4 * ((4 * ((4 * ((4 * ((
          4 * ((4 * ((4 * ((4 * ((
            4 * ((4 * ((4 * ((4 * w 20) + w 19)) + w 18)) + w 17)
          ) + w 16)) + w 15)) + w 14)) + w 13)
        ) + w 12)) + w 11)) + w 10)) + w 9)
      ) + w 8)) + w 7)) + w 6)) + w 5
    ) - w 3) = 0,
    (((4 * w 22) + w 21) - w 4) = 0
  ]
end LighterExportGate.U32AddManyGate
```
The comments in the code above were added for presentation; the actual export contains only the raw constraints. In general, the function of each constraint must be reverse-engineered from the polynomial expressions.

The exported constraints are parameterized by the field modulus (here 18446744069414584321, the Goldilocks prime $p = 2^{64} - 2^{32} + 1$).
The wire function `w : Fin numWires → ZMod p` maps wire indexes to field elements.

One can understand how the gate functions by separating these constraints into three groups:

1. **Arithmetic constraint.** The main constraint $\texttt{carryOut} * 4294967296 + \texttt{sum} = \texttt{addend0} + \texttt{addend1} + \texttt{carryIn}$.
2. **Limb range checks.** Each constraint $w * (w-1) * (w-2) * (w-3) = 0$ forces the wire to be in $\{0, 1, 2, 3\}$. This polynomial equals zero if and only if $w$ is one of these four values.
3. **Limb reconstruction.** These verify that the witness limbs (base-4 digits) correctly reconstruct the sum and carry values. Each constraint decomposes a value into base-4 digits using the Horner scheme.

The range checks on the limbs, combined with the reconstruction constraints, prove that $\texttt{sum}$ and $\texttt{carryOut}$ are bounded. If each limb is in $\{0,1,2,3\}$, then the reconstructed value is at most $4^{16} - 1 = 2^{32} - 1$ for the sum (16 limbs) and $4^2 - 1 = 15$ for the carry (two limbs).

## 2. Generalizing the Exports[](https://www.zellic.io/blog/formal-verification-plonky-gate#2-generalizing-the-exports)

The exported constraints are specific to particular parameter choices (e.g., $\texttt{num\_addends} = 2$).
For verification, we want to reason about the gate generically, for any number of addends.
We also want to separate the low-level constraint encoding from a high-level specification that captures the *intended* behavior.

### Structuring Wire Values[](https://www.zellic.io/blog/formal-verification-plonky-gate#structuring-wire-values)

First, we give meaningful names to the wire values. The gate has two kinds of wires:

- **Public wires,** the inputs and outputs visible to the circuit (`addends`, `carryIn`, `sum`, `carryOut`)
- **Witness wires,** internal values the prover computes (the limb decompositions)

```
/-- Public wire values: the gate's inputs and outputs -/
structure PubValues (F : Type*) (num_addends : Nat) where
  addends : Fin num_addends → F
  carryIn : F
  sum : F
  carryOut : F
/-- The addends together with carryIn as a single indexed function -/
def PubValues.addendsAndCarryIn {F : Type*} {num_addends : Nat} (pv : PubValues F num_addends) :
    Fin (num_addends + 1) → F :=
  fun k => if h : k.val < num_addends then pv.addends ⟨k.val, h⟩ else pv.carryIn
/-- All wire values: public wires plus witness limbs -/
structure AllValues (F : Type*) (num_addends : Nat) extends PubValues F num_addends where
  sumLimbs : Fin 16 → F      -- 16 base-4 limbs for the 32-bit sum
  carryOutLimbs : Fin 2 → F  -- 2 base-4 limbs for the carry
```
We added a joint access function for `addends` and `carryIn` to avoid edge cases in the constraint definitions if `num_addends` is zero.

There are more refined ways to split the wire values. We could further divide the public wires into *inputs* and *outputs*:

- **Input wires,** values provided to the gate (`addends`, `carryIn`)
- **Output wires,** values computed by the gate (`sum`, `carryout`)

For this gate, that would give us a three-level hierarchy, `InputValues` (`addends`, `carryIn`) → `PubValues` (extends with `sum`, `carryOut`) → `AllValues` (extends with witness limbs).
Just as we extend `PubValues` to `AllValues` by computing the witness limbs, we could extend `InputValues` to `PubValues` by computing the outputs from the inputs.

This finer split is useful when one wants to prove that outputs are uniquely determined by inputs, or when composing gates where one gate’s outputs feed into another’s inputs.
Here the bound on the number of addends would appear.
Extending inputs to outputs requires proving that valid outputs *exist*, which fails when the number of addends is too large.
In the simpler presentation here, this constraint is invisible, since we never construct the outputs ourselves.

However, for this blog post we focus on the simpler public/witness split, which suffices to demonstrate the core verification approach.

### Generic Constraints[](https://www.zellic.io/blog/formal-verification-plonky-gate#generic-constraints)

We define the constraints using helper functions that mirror the exported structure:

```
-- Range check: w ∈ {0, 1, 2, 3}
abbrev constraint_range_3_check (w : ZMod p) :=
  (((w * (w - 1)) * (w - 2)) * (w - 3)) = 0
-- Limb reconstruction using Horner's method (recursive definition of horner omitted here)
abbrev constraint_limbs (b : Nat) (limbs : Fin (L+1) → ZMod p) (value : ZMod p) :=
  horner (b : ZMod p) limbs - value = 0
-- Main arithmetic constraint
abbrev constraint_add_u32 {num_addends : Nat}
  (addends_and_carryIn : Fin (num_addends + 1) → ZMod p) (sum : ZMod p) (carryOut : ZMod p) :=
  carryOut * (b1e32 : ZMod p) + sum - (fin_sum addends_and_carryIn) = 0
def constraints {p : Nat} {num_addends : Nat} (av : AllValues (ZMod p) num_addends) :
    Fin (numConstraints num_addends) → Prop :=
  ![
    constraint_add_u32 av.toPubValues.addendsAndCarryIn av.sum av.carryOut,
    constraint_range_3_check (av.carryOutLimbs 1),
    constraint_range_3_check (av.carryOutLimbs 0),
    constraint_range_3_check (av.sumLimbs 15),
    constraint_range_3_check (av.sumLimbs 14),
    constraint_range_3_check (av.sumLimbs 13),
    constraint_range_3_check (av.sumLimbs 12),
    constraint_range_3_check (av.sumLimbs 11),
    constraint_range_3_check (av.sumLimbs 10),
    constraint_range_3_check (av.sumLimbs 9),
    constraint_range_3_check (av.sumLimbs 8),
    constraint_range_3_check (av.sumLimbs 7),
    constraint_range_3_check (av.sumLimbs 6),
    constraint_range_3_check (av.sumLimbs 5),
    constraint_range_3_check (av.sumLimbs 4),
    constraint_range_3_check (av.sumLimbs 3),
    constraint_range_3_check (av.sumLimbs 2),
    constraint_range_3_check (av.sumLimbs 1),
    constraint_range_3_check (av.sumLimbs 0),
    constraint_limbs 4 av.sumLimbs av.sum,
    constraint_limbs 4 av.carryOutLimbs av.carryOut
  ]
```
We let Lean verify that the constraints generated by this function agree with the exports for the relevant parameter values. This allows us to prove statements for each export by proving a generic statement for the constraints generated by this function for all parameter values. In addition to avoiding redundant work proving statements about the individual exports, this also makes proving easier and the resulting proof more transparent, as it avoids coincidences for specific parameter values.

## 3. The Specification[](https://www.zellic.io/blog/formal-verification-plonky-gate#3-the-specification)

The specification states what the gate *should* compute, expressed in terms of natural number arithmetic rather than field elements:

```
structure Assumptions {p : Nat} {num_addends : Nat} (pv : PubValues (ZMod p) num_addends) :
    Prop where
  -- All addends and carryIn are valid u32
  h_addendsAndCarryIn_u32 : (∀ n, IsU32 (pv.addendsAndCarryIn n).val)
  -- carryIn is at most 15
  h_carryIn_le : pv.carryIn.val ≤ 4 ^ 2 - 1
structure Spec {p : Nat} {num_addends : Nat} (pv : PubValues (ZMod p) num_addends) :
    Prop where
  -- Sum is a valid u32
  h_sum_u32 : IsU32 pv.sum.val
  -- Carry-out is a valid u32
  h_carryOut_u32 : IsU32 pv.carryOut.val
  -- Carry-out is at most 15
  h_carryOut_le : pv.carryOut.val ≤ 4 ^ 2 - 1
  -- Arithmetic relation holds
  h_arith :
    pv.carryOut.val * 2 ^ 32 + pv.sum.val = fin_sum (fun k => (pv.addendsAndCarryIn k).val)
```
The `Assumptions` structure captures what must be verified by constraints outside of this gate.
The `Spec` structure captures the logic enforced by the gate’s constraint.

Note that `.val` extracts the canonical representative of a `ZMod p` element as a natural number in $\{0, \ldots, p-1\}$.
The specification is stated in terms of these natural number values, which lets us express properties like “is a valid u32” directly.

The specification expresses conditions as propositions rather than polynomial constraints. By using `.val` to extract natural numbers from field elements, we lift the reasoning from native field arithmetic to U32 arithmetic, effectively black-boxing the field operations. This is the abstraction we want to use for reasoning at a higher level, for example when verifying gadgets that use this gate.

## 4. Proving Soundness and Completeness[](https://www.zellic.io/blog/formal-verification-plonky-gate#4-proving-soundness-and-completeness)

Now we come to the core verification. We prove that the constraints correctly enforce the specification.

### Structured Constraints[](https://www.zellic.io/blog/formal-verification-plonky-gate#structured-constraints)

We package the raw constraints into a structure that’s easier to work with in proofs:

```
structure Constraints {p : Nat} {num_addends : Nat} (av : AllValues (ZMod p) num_addends) :
    Prop where
  arith : constraint_add_u32 av.toPubValues.addendsAndCarryIn av.sum av.carryOut
  range_sum : ∀ n : Fin 16, constraint_range_3_check (av.sumLimbs n)
  range_borrow : ∀ n : Fin 2, constraint_range_3_check (av.carryOutLimbs n)
  recon_sum : constraint_limbs 4 av.sumLimbs av.sum
  recon_carry : constraint_limbs 4 av.carryOutLimbs av.carryOut
```
Just as `PubValues` and `AllValues` add meaning to wire values, this structure adds meaning to the constraints and groups them by functionality. For example, the single field `range_sum : ∀ n : Fin 16, constraint_range_3_check (av.sumLimbs n)` captures all 16 individual range-check constraints for the sum limbs. Simple lemmas show that this structure is equivalent to the raw constraints given above.

### Soundness[](https://www.zellic.io/blog/formal-verification-plonky-gate#soundness)

The soundness theorem says that if the constraints hold, then the specification holds. This is the critical security property. It guarantees that a valid proof implies correct computation.

```
lemma soundness {p : Nat} [Fact (Nat.Prime p)] {num_addends : Nat}
    {av : AllValues (ZMod p) num_addends}
    (hp : p > (num_addends + 1) * (2 ^ 32 - 1) ∧ p > (4 ^ 2 - 1) * 2 ^ 32 + (2 ^ 32 - 1))
    (ha : Assumptions av.toPubValues) (hc : Constraints av) :
    Spec av.toPubValues := by sorry -- proof omitted
```
Of course, in the result of our engagement with Lighter, in place of `sorry` (which is Lean’s placeholder for a missing proof), an actual proof was created.
While proof strategies have been relevant for us to produce such a proof, its content is not relevant afterwards — the point of formal verification is that there *is* a proof that a machine verified so you only need to read the statement that was proved.

### Completeness[](https://www.zellic.io/blog/formal-verification-plonky-gate#completeness)

The completeness theorem says that if the specification holds, then there exist witness values that satisfy the constraints. This ensures that an honest prover can always generate a valid proof. The structure of the completeness statement is given as follows:

```
/-- Compute witness values from public values -/
def PubValues.addWitnessValues {p : Nat} {num_addends : Nat}
    (pv : PubValues (ZMod p) num_addends) : AllValues (ZMod p) num_addends where
  toPubValues := pv
  sumLimbs := fun k => (padded_digits 4 pv.sum.val 16 k : ZMod p)
  carryOutLimbs := fun k => (padded_digits 4 pv.carryOut.val 2 k : ZMod p)
lemma completeness {p : Nat} [Fact (Nat.Prime p)] {num_addends : Nat}
    {pv : PubValues (ZMod p) num_addends} (hs : Spec pv) :
    Constraints pv.addWitnessValues := by sorry -- proof omitted
```
The first function defines how we choose the values of the witness wires. Here, the witness values must be the base-4 digits of the result values. The lemma then states that these choices indeed fulfill the polynomial constraints.

## Uncovering Hidden Assumptions[](https://www.zellic.io/blog/formal-verification-plonky-gate#uncovering-hidden-assumptions)

In addition to confirming correctness, the formal verification process exposed an important insight about implicit assumptions in the gate’s interface.

When proving that the assumptions and specification are consistent with the constraints, we discovered that the gate relied on the undocumented assumption `carryIn.val` $\leq 15$.
However, the calling code uses a `U32Target` for the carry wires, which permits values up to $2^{32}-1$.
For these large values the gate would be incomplete.

## Conclusion[](https://www.zellic.io/blog/formal-verification-plonky-gate#conclusion)

We have shown how to formally verify a Plonky2 gate by

1. **Exporting** the constraints from Rust to Lean
2. **Modeling** the specification in terms of natural number arithmetic
3. **Proving soundness** — constraints imply specification
4. **Proving completeness** — specification implies satisfiable constraints

Following this approach allows us to formally verify the gates used in Lighter’s project, thereby laying a trustable foundation for the verification of the complete circuits. Discovering deviations between intended specification and implemented constraints allows our client to react and improve the security stance of the project.
