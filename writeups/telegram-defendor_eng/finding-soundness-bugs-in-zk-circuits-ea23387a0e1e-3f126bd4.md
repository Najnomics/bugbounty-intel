# 🔐 Soundness Errors in ZK Schemes and Their Risks

- **Source URL:** https://muellerberndt.medium.com/finding-soundness-bugs-in-zk-circuits-ea23387a0e1e
- **Fetched from:** https://web.archive.org/web/20260302124124/https://muellerberndt.medium.com/finding-soundness-bugs-in-zk-circuits-ea23387a0e1e
- **Fetched:** 2026-11-25
- **Channel:** @defendor_eng
- **Telegram message:** https://t.me/defendor_eng/1083 (id 1083)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# A Practical Guide to Finding Soundness Bugs in ZK Circuits

*Zero-knowledge proofs are a core building block for blockchain scaling and privacy. In real-world deployments, the weakpoint is usually the circuit: the constraints developers write. Small omissions or “obvious” assumptions can turn into soundness bugs, letting an attacker prove an invalid computation. In this article, I’ll walk through common classes of circuit bugs in and how to spot them.*

## ZK circuit basics

Before diving into actual bugs, let’s review what we’re dealing with. An [arithmetic circui](https://web.archive.org/web/20260302124124/https://rareskills.io/post/arithmetic-circuit)t encodes a computation as a system of polynomial constraints over a finite field. The circuit has three types of values:

- Private inputs (witness): Values known only to the prover. These are the “secrets” being proven about.
- Public inputs/outputs: Values visible to both prover and verifier. These anchor the proof to something concrete.
- Intermediate signals: Internal values computed during the proof.

The prover’s job is to find values for all signals such that every constraint is satisfied. The verifier checks a *succinct* proof that such values exist, without learning the private inputs.

A common language for writing circuits is [Circom](https://web.archive.org/web/20260302124124/https://github.com/iden3/circom) by iden3. Let’s start with a simple Circom example that checks if an input equals zero (you can copy/paste the code into [zkREPL](https://web.archive.org/web/20260302124124/https://zkrepl.dev/) to test it).

```
pragma circom 2.1.6;
include "circomlib/poseidon.circom";
template IsZero() {
  signal input in;
  signal output out;
  signal inv;
  inv <-- in != 0 ? 1/in : 0;
  out <== 1 - in*inv;
  in*out === 0;
}
component main { public [ in ] } = IsZero();
/* INPUT = {
    "in": "0"
} */
```
There’s a critical distinction here: `<--` runs *only* during witness generation. It computes a value, but it doesn’t bind that value to the circuit in any way. In contrast, `<==` and `===` *do* emit polynomial constraints: they turn your intent into equations the prover must satisfy and the verifier ultimately enforces.

Think of it this way: witness generation produces a candidate assignment for all signals. Constraints are the rules that makes that assignment checkable. If a value is computed in witness generation but never constrained, it’s effectively unconstrained degrees of freedom, so a malicious prover can swap in whatever value is convenient while still satisfying the rest of the circuit.

Let’s trace through how `IsZero` works. The template takes one input `in` and produces one output `out`. There’s also an intermediate signal `inv`.

First, witness generation computes `inv`. If `in` is non-zero, `inv` becomes its multiplicative inverse (`1/in` in the field). If `in` is zero, `inv` is set to 0.

Then we have two constraints:

- `out <== -in * inv + 1` constrains `out` to equal `-in * inv + 1`
- `in*out === 0` requires either `in` or `out` to be zero

If in is non-zero, then `inv = 1/in`, so `out = -in*(1/in) + 1 = -1 + 1 = 0`. The second constraint is satisfied because `out = 0`.

If `in` is zero, then `out = -0*inv + 1 = 1`. The second constraint is satisfied because `in = 0`.

A malicious prover can’t cheat here because any deviation from the correct values would violate one of the constraints. For example, if `in = 5` and a malicious prover tried to set `out = 1` (claiming 5 equals zero), the constraint `in*out === 0` would fail: `5*1 = 5 ≠ 0`.

### Under-constrained circuits

A common zk fail is that the developer computes the right value but forgets add an explicit constraint. In that case the proof is only showing “there exists some satisfying assignment,” while the meaningful output remains attacker-controlled.

Here’s a basic example for a broken withdrawal circuit. Given `oldBal` and withdrawal `amount`, the circuit’s public output `newBal` should be exactly `oldBal - amount` (and also enforce `amount <= oldBal`). The trap is computing the correct new balance, but never binding it to the public output.

```
pragma circom 2.1.6;
include "circomlib/comparators.circom";
template WithdrawBug(n) {
  // public inputs: oldBal, amount, newBal
  signal input oldBal;
  signal input amount;
  signal input newBal;
  // Enforce amount <= oldBal (so this isn't just "overdraft")
  component le = LessEqThan(n);
  le.in[0] <== amount;
  le.in[1] <== oldBal;
  le.out === 1;
  // Compute the correct next balance...
  signal computedNew;
  computedNew <== oldBal - amount;
  // BUG: computedNew is never constrained to equal newBal.
  // The prover can claim ANY newBal and still satisfy constraints.
}
component main { public [ oldBal, amount, newBal ] } = WithdrawBug(32);
/* INPUT = {
  "oldBal": "100",
  "amount": "40",
  "newBal": "100"
} */
```
With that one missing equality, a prover can withdraw 40 while claiming the stored balance stays at 100. Then they can do it again, and again. This is the zk version of computing the correct value in a local variable, but writing an attacker-controlled value to storage.

To fix the issue, we add the actual constraint:

```
pragma circom 2.1.6;
include "circomlib/comparators.circom";
template WithdrawFixed(n) {
(...)
  computedNew <== oldBal - amount;
  // FIX: bind the public output the verifier/contract uses
  newBal === computedNew;
}
```
### Arithmetic edge cases in finite fields

Finite-field arithmetic is not integer arithmetic. Inside a SNARK, every signal lives in a field, and equalities are checked modulo a prime. If your application logic assumes integers (especially division, comparisons, ranges), you must explicitly constrain the integer semantics. Otherwise you’re proving a different statement than you think.

For example, a very tempting “division” gadget only enforces the algebraic identity `a = b * q + r`. But that’s a statement in the finite field, not the integer-division semantics you probably intend. In the buggy circuit below, `q` is presented as the quotient, yet the prover is free to choose any `r` that makes the equality hold, even if `r` is larger than `b`.

```
pragma circom 2.1.6;
template DivBug() {
  // public inputs: a, b, q
  signal input a;
  signal input b;
  signal input q;
  // private witness: r
  signal input r;
  // BUG: this alone does not define integer division
  a === b*q + r;
}
component main { public [ a, b, q ] } = DivBug();
/* INPUT = {
  "a": "13",
  "b": "5",
  "q": "1",
  "r": "8"
} */
```
For example, with `a = 13` and `b = 5`, the witness `q = 1, r = 8` satisfies `13 = 5·1 + 8`, so the proof verifies, despite `q = 1` not being `floor(13/5)`.

The fix is to constrain the missing semantics: range-limit values into the intended bit-width and enforce `0 ≤ r < b` (and typically `b ≠ 0`) so `q` and `r` actually represent an integer division.

```
pragma circom 2.1.6;
include "circomlib/bitify.circom";
include "circomlib/comparators.circom";
template DivFixed(n) {
  signal input a;
  signal input b;
  signal input q;
  signal input r;
  // Still required
  a === b * q + r;
  // Treat them as n-bit integers (common "bridge" to integer semantics)
  component aBits = Num2Bits(n); aBits.in <== a;
  component bBits = Num2Bits(n); bBits.in <== b;
  component qBits = Num2Bits(n); qBits.in <== q;
  component rBits = Num2Bits(n); rBits.in <== r;
  // Reject b = 0 (if required by spec)
  component bz = IsZero();
  bz.in <== b;
  bz.out === 0;
  // Enforce 0 <= r < b
  component lt = LessThan(n);
  lt.in[0] <== r;
  lt.in[1] <== b;
  lt.out === 1;
}
component main { public [ a, b, q ] } = DivFixed(32);
/* INPUT = {
  "a": "13",
  "b": "5",
  "q": "2",
  "r": "3"
} */
```
The takeaway is: **a circuit only enforces what you explicitly constrain. Every “obvious” assumption you leave implicit becomes prover-controlled.**

In normal code, you can lean on types, control flow, and the runtime’s integer semantics; in a ZK circuit, none of that exists unless you encode it as constraints.

## Real-world case study: Kakarot zkEVM

Let’s look at a real-world example that got me a nice $5k payout in an audit contest. This bug combines missing constraints with a nice arithmetic field underflow.

The target was [Kakarot](https://web.archive.org/web/20260302124124/https://www.kakarot.org/), a zkEVM written in [Cairo](https://web.archive.org/web/20260302124124/https://www.cairo-lang.org/). Cairo’s basic numeric type is a [felt](https://web.archive.org/web/20260302124124/https://www.starknet.io/cairo-book/ch02-02-data-types.html#felt-type)`felt_to_bytes_little()`, which converts a felt into a little-endian byte array and is reused by other conversions (`felt_to_bytes()`, various `uint256_to_bytes*()` helpers, `bigint_to_bytes_array()`, etc.). These helpers show up in places like `get_create_address()` / `get_create2_address()`, so if you can spoof their output you can end up spoofing derived addresses.

The core loop looks like this:

```
body:
let range_check_ptr = [ap - 3];
let value = [ap - 2];
let bytes_len = [ap - 1];
let bytes = cast([fp - 4], felt*);
let output = bytes + bytes_len;
let base = 2 ** 8;
let bound = base;
%{
    memory[ids.output] = res = (int(ids.value) % PRIME) % ids.base
    assert res < ids.bound, f'split_int(): Limb {res} is out of range.'
%}
let byte = [output];
with_attr error_message("felt_to_bytes_little: byte value is too big") {
    assert_nn_le(byte, bound - 1);
}
tempvar value = (value - byte) / base;
tempvar bytes_len = bytes_len + 1;
jmp body if value != 0;
```
The function uses a prover-side hint to write the next byte into memory, range-checks that it’s a byte (`<= 255`), then updates `value = (value - byte) / 256` and repeats until `value == 0`. The mistake is that the circuit never enforces that the hinted byte is *the correct byte* for the current `value`.

We can now trigger a targeted field underflow. Near the end of the loop, the remaining `value` is small. If the remaining value is `1` but the prover makes the hint return `2`, then `value - byte` wraps modulo `STARKNET_PRIME` into a huge value. The loop condition is `value != 0`, so the loop keeps running instead of terminating.

In the subsequent iterations the prover can keep returning essentially arbitrary bytes. They don’t have to correspond to the original input felt; they just need to eventually steer `value` back to zero at some point so the function terminates.

The prover can take as many iterations as needed, but there’s one extra hurdle: `bytes_len` must end at a “special” value to pass the function’s final minimal-length check. Here, the exploit becomes really fun. The function checks that `bytes_len` is the minimal length needed to represent the original value by reading bounds from `pow256_table` at offset `bytes_len`. This table access can land somewhere into the code segment, and a malicious prover can aim for any nearby position where the Cairo bytecode happens to contain a zero. If `pow256_table[bytes_len]` resolves to `0`, the bounds check becomes trivially satisfiable for almost any `initial_value`.

In the proof-of-concept, I dumped part of the memory segment and found multiple offsets in the code segment that contain zeros, then brute-forced the stopping point until the minimal-length check passed reliably. If you want the full PoC, see the [contest submission](https://web.archive.org/web/20260302124124/https://github.com/code-423n4/2024-09-kakarot-findings/issues/118).

## Real-world case study: zkSync Era

In September 2023, [ChainLight disclosed a critical soundness vulnerability in zkSync Era’s ZK circuits](https://web.archive.org/web/20260302124124/https://blog.chainlight.io/uncovering-a-zk-evm-soundness-bug-in-zksync-era-f3bc1b2a66d8). The bug allowed a malicious prover to produce “proofs” for invalidly executed blocks, which the verifier contracts on L1 would have accepted. Matter Labs deployed a fix and awarded ChainLight a 50K USDC reward.

[zkSync Era](https://web.archive.org/web/20260302124124/https://www.zksync.io/) is a ZK-rollup that runs a ZK-EVM: a zero-knowledge circuit that verifies EVM-like execution. The circuit must ensure that every state transition follows the VM semantics exactly. Any deviation could allow an attacker to execute invalid transactions.

One thing the circuit needs to handle correctly is memory. On a normal VM, when you store a value and later load it, you expect consistency. In zkSync’s EraVM, memory operations are represented as “memory queries” and are later packed and checked inside the circuit.

The bug here is another variant of the *under-constrained value* theme: the circuit constructs a `LinearCombination` that is clearly intended to enforce a relationship, but never actually turns it into constraints.

When handling a memory write instruction, zkSync’s circuit code constructs a `MemoryWriteQuery` from a 256-bit register value and later converts it into a packed `RawMemoryQuery`.

A 256-bit `Register<E>` is stored as two `UInt128<E>` limbs (`lowest_128` and `highest_128`). When constructing the `MemoryWriteQuery`, the code further splits `highest_128` into two `u64` chunks (`u64_word_2`, `u64_word_3`) and then builds a linear combination that looks like it’s trying to enforce:

`u64_word_2 + 2^64 * u64_word_3 == highest_128`

Here is the relevant code:

```
pub(crate) fn from_key_and_value_witness<CS: ConstraintSystem<E>>(
  cs: &mut CS,
  key: MemoryKey<E>,
  register_output: Register<E>,
) -> Result<Self, SynthesisError> {
  let [lowest_128, highest_128] = register_output.inner;
  let tmp = highest_128
    .get_value()
    .map(|el| (el as u64, (el >> 64) as u64));
  let (u64_word_2, u64_word_3) = match tmp {
    Some((a, b)) => (Some(a), Some(b)),
    _ => (None, None),
  };
  let u64_word_2 = UInt64::allocate_unchecked(cs, u64_word_2)?;
  let u64_word_3 = UInt64::allocate(cs, u64_word_3)?;
  let shifts = compute_shifts::<E::Fr>();
  let mut minus_one = E::Fr::one();
  minus_one.negate();
  let mut lc = LinearCombination::zero();
  lc.add_assign_number_with_coeff(&u64_word_2.inner, shifts[0]);
  lc.add_assign_number_with_coeff(&u64_word_3.inner, shifts[64]);
  lc.add_assign_number_with_coeff(&highest_128.inner, minus_one);
  // BUG: lc is never enforced
  ...
}
```
Note that constraints only get produced by functions that take a `cs`parameter and actually emit gates. This code never does that. It never calls something like `lc.enforce_zero(cs)`, and it never converts `lc` into a constrained value. As a result, the “split correctness” relationship is not enforced.

Later, `MemoryWriteQuery::into_raw_query` packs pieces of the write query into a `RawMemoryQuery`:

- `lowest_128` and `u64_word_2` are packed into `value`
- `u64_word_3` is stored as `value_residual`

```
pub(crate) fn into_raw_query<CS: ConstraintSystem<E>>(
  &self,
  cs: &mut CS,
) -> Result<RawMemoryQuery<E>, SynthesisError> {
  let shifts = compute_shifts::<E::Fr>();
  let mut lc = LinearCombination::zero();
lc.add_assign_number_with_coeff(&self.lowest_128.inner, shifts[0]);
  lc.add_assign_number_with_coeff(&self.u64_word_2.inner, shifts[128]);
  let value = lc.into_num(cs)?;
  let new = RawMemoryQuery {
    timestamp: self.timestamp,
    memory_page: self.memory_page,
    memory_index: self.memory_index,
    rw_flag: Boolean::constant(true)
    value_residual: self.u64_word_3,
    value,
    value_is_ptr: self.value_is_ptr,
  };
  Ok(new)
}
```
Because the earlier recombination constraint never existed, the prover can effectively tamper with the high bits represented by these split components while still producing a proof that verifies. The bug allows a prover to arbitrarily change the high 128 bits of any value stored in memory by a store instruction without changing the validity of the proof.

On L2, zkSync burns `msg.value`, then constructs a bytes message encoding the withdrawal and sends it to L1:

```
function withdraw(address _l1Receiver) external payable override {
  uint256 amount = _burnMsgValue();
bytes memory message = _getL1WithdrawMessage(_l1Receiver, amount);
  L1_MESSENGER_CONTRACT.sendToL1(message);
  emit Withdrawal(msg.sender, _l1Receiver, amount);
}
function _getL1WithdrawMessage(address _to, uint256 _amount) internal pure returns (bytes memory) {
  return abi.encodePacked(IMailbox.finalizeEthWithdrawal.selector, _to, _amount);
}
```
The key detail is that `abi.encodePacked(...)` materializes the message in memory. The compiled EraVM code writes the selector, `_to`, and `_amount` into heap memory using `st.1` memory stores. When storing `_amount`, the VM performs a misaligned store, which the EraVM translates into two aligned `MemoryWriteQuery:`

```
/// store `_amount` parameter into memory at `r1+56`
st.1    r2, r5
// misaligned store -> translated into two aligned write queries:
{
  memory_page: CUR_HEAP_PAGE,
  memory_index: (r1 + 56) // 32,
  value: (uint256(_to) << 64) | (_amount >> 192)
},
{
  memory_page: CUR_HEAP_PAGE,
  memory_index: (r1 + 56) // 32 + 1,
  value: (_amount << 64)
}
```
Once you can tamper with the high bits of values written by store instructions, you can aim straight at the encoded `_amount`. See [ChainLight’s writeup](https://web.archive.org/web/20260302124124/https://blog.chainlight.io/uncovering-a-zk-evm-soundness-bug-in-zksync-era-f3bc1b2a66d8) for full exploit details.

## Conclusion and ZK circuit audit checklist

We’ve now seen the same failure mode show up in different variants: the code computes something but doesn’t bind it to the output, relies on an “obvious” property (like integer division semantics) without defining explicit constraints. In normal software, a missing check might cause a revert or a weird edge case that you can patch after the fact. In a circuit, the exact opposite happens: the prover gets to choose the witness, so the missing check becomes a *degree of freedom that* can turn into a forgeable proof for an invalid computation. As an auditor, make sure to check the following:

- **Start by writing the exact statement the proof is supposed to establish.** Be explicit about what’s public, what’s private, and what *valid* means (state transition, signature validity, balance update, Merkle inclusion, etc.). Most circuit bugs happen because the author only ensures that “the program runs,” while the verifier actually checks “some witness satisfies these constraints.”
- **Bind every security-critical value end-to-end.** Track anything the verifier/contract uses (public outputs, roots, hashes, calldata/message bytes, `amount`, `to`, `index`, `nullifier`, etc.) and make sure it is *explicitly constrained* to the internal computation. Red flags are computed values that never get equated to the public value, or “outputs” that come from a witness that’s only range-checked.
- **Assume all witnesses and hints are hostile, then eliminate degrees of freedom.** For every witness-derived intermediate, ask “can the prover set this arbitrarily without breaking constraints?” This is where you catch missing equalities, linear combinations that are constructed but never enforced, and conditional constraints that don’t fire for certain selector values or ordering edge cases.
- **Make the semantics match the real world: integers, bytes, and control flow are not free.** Any time the app logic assumes integers (ranges, comparisons, division/mod/remainder, byte packing, ABI encoding), you must range-limit and constrain the semantics explicitly (`r < b`, no division-by-zero unless allowed, correct endianness/canonical encoding). Likewise, any selector/flag/opcode must be boolean-constrained and must gate constraints correctly so attackers can’t “turn off” checks.
- **Attack the circuit in English, then map it to a missing constraint.** For each high-risk area (outputs, hashing/Merkle, state linking, arithmetic edge cases, padding/last-row logic), try to describe a fake witness that would pass while changing meaning (“withdraw more,” “spoof address,” “reuse nullifier,” “read value B after writing A”). If you can articulate the cheat, you can usually locate the one missing constraint or gating condition that makes it real.
