# 📐 Building a ZKVM From Scratch

- **Source URL:** https://www.cyfrin.io/blog/making-sense-of-zk-virtual-machines
- **Fetched from:** https://web.archive.org/web/20261013134325/https://www.cyfrin.io/blog/making-sense-of-zk-virtual-machines
- **Fetched:** 2026-11-25
- **Channel:** @defendor_eng
- **Telegram message:** https://t.me/defendor_eng/1759 (id 1759)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
The Wayback Machine - https://web.archive.org/web/20261013134325/https://www.cyfrin.io/blog/making-sense-of-zk-virtual-machines

A deep dive into how ZKVMs work — from ZK proofs and circuits through arithmetization to building a working STARK-based ZKVM in Rust.

There are plenty of high-level explanations of ZKVMs, and plenty of research papers dense with formal mathematics. What's harder to find is the middle ground: enough theory to understand *why* the pipeline works the way it does, paired with enough code to see *how* it all fits together. This article aims to fill that gap. The first half builds the conceptual foundations: ZK proofs, circuits, arithmetization, and the shift from proving computations to proving machines. The second half makes it concrete by constructing a working STARK-based ZKVM in Rust, walking through execution, trace generation, algebraic constraints, and proof verification step by step.

You can prove a computation was executed correctly without revealing how it was done. Not by obscuring the details or encrypting the output, but by constructing a mathematical argument that convinces the verifier while revealing nothing about the intermediate steps. That property, and the machinery behind it, is what makes everything in this article possible.

In the systems we care about here, a prover runs a computation and produces a small proof. A verifier checks it without re-executing anything. The proof is tiny relative to the computation, and verification is fast relative to execution.

The formal framework rests on three properties:

- **Completeness**: If the prover is honest (the computation really did produce the claimed result), the verifier will always accept. Honest provers never get rejected.
- **Soundness**: If the prover is dishonest (the claimed result is wrong), the verifier will reject with overwhelming probability. A dishonest prover is rejected except with negligible probability.
- **Zero-knowledge**: The proof reveals nothing beyond the truth of the statement. The verifier learns that the result is correct, but gains no information about the intermediate steps or private inputs.

In many blockchain scalability contexts, the zero-knowledge property is secondary. What matters most is succinctness: the proof is small and fast to check, even when the original computation was enormous. For that reason, these systems are often described as validity proofs rather than zero-knowledge proofs. The primary goal is to compress verification, not to hide information. A typical ZK rollup doesn't particularly care about hiding transaction data from the L1 verifier; it cares about not making L1 re-execute every transaction.

Many proof systems follow the same basic pattern: the prover first commits to data, then answers verifier challenges, and consistency across those answers convinces the verifier. In practice, the verifier challenges are derived deterministically from the prover's commitments using hash functions (a technique known as the Fiat-Shamir transform), so the whole protocol becomes non-interactive. The prover produces a single proof object, and the verifier checks it offline. No back-and-forth needed.

This is the foundation everything else builds on. The question is: what exactly is the prover proving?

To prove a computation, you first need to express it in a form that a proof system can reason about. In the proof systems relevant to this article, computation must be expressed as algebraic equations over a finite field. Different systems do this differently. The most widely known representation is the arithmetic circuit: a directed acyclic graph (DAG) of addition and multiplication gates.

A [finite field](https://web.archive.org/web/20261013134325/https://www.cyfrin.io/blog/zk-math-101-rings-and-fields) is a set of numbers where you can add, subtract, multiply, and divide (except by zero), and every operation stays within the set. The simplest example is [integers modulo a prime number](https://web.archive.org/web/20261013134325/https://www.cyfrin.io/blog/zk-math-101-modular-arithmetic) p. If p = 7, then 5 + 4 = 2 (since 9 mod 7 = 2), and every nonzero element has a multiplicative inverse (3 × 5 = 1 mod 7, so 3⁻¹ = 5). Modern SNARKs and STARKs use much larger finite fields, but the arithmetic follows the same rules.

To understand how computation becomes algebra, arithmetic circuits are the clearest starting point. In an arithmetic circuit, computation flows through wires. Each wire carries a field element. Gates take input wires, perform an operation (add or multiply), and produce an output wire. A circuit that computes x² + x + 5 might look like:

Every gate in this circuit produces an algebraic constraint, an equation that must hold. The multiplication gate says `a * b = c`, where a and b are input wires and c is the output wire. The addition gate says `a + b = c`. The whole circuit is a system of polynomial equations over the field.

The witness is the set of all wire values (inputs, intermediates, and outputs) that satisfy every constraint simultaneously. The prover knows the witness; the verifier does not. Proving means demonstrating that you know a satisfying assignment, a set of wire values that makes every gate equation true. In zero-knowledge settings, this can be done without revealing those wire values.

Different proof systems encode these constraints differently. [Groth16](https://web.archive.org/web/20261013134325/https://eprint.iacr.org/2016/260) uses a format called R1CS (Rank-1 Constraint System), where each constraint is written as a product of two linear combinations equaling a third. [Plonk](https://web.archive.org/web/20261013134325/https://eprint.iacr.org/2019/953) uses a gate-based formulation with additional constraints that tie wires together across the circuit. But the underlying idea is the same in all of them: computation becomes a system of polynomial equations, and proving is showing you know a solution.

Here's a concrete example. Suppose you want to prove you know an x such that x³ + x + 5 = 35. The circuit would have:

1. A multiplication gate: v₁ = x \* x (computing x²)
2. A multiplication gate: v₂ = v₁ \* x (computing x³)
3. An addition gate: v₃ = v₂ + x (computing x³ + x)
4. An addition gate: out = v₃ + 5 (computing x³ + x + 5)
5. A constraint: out = 35 (the public output)

Here, 35 is the public output (part of the statement being proved), while x is the private witness. The prover knows x = 3 (since 27 + 3 + 5 = 35) and all intermediate values. In a zero-knowledge setting, the prover can convince the verifier that such an x exists without revealing that x = 3.

Arithmetic circuits are not the only way to represent computation for proving. STARK-based systems, including the one we build later in this article, use a different representation: they record a step-by-step execution trace and express correctness rules as polynomial constraints over that trace (an approach called AIR, which we cover in detail in section 11). The underlying principle is the same: reduce computation to polynomial equations. But the structure of those equations, and the way you build them differs. We start with circuits here because they make the core ideas concrete. The limitations we describe next apply equally to any approach where you hand-craft constraints per computation.

Whether you use arithmetic circuits, AIR constraints, or any other algebraic representation, the traditional model requires a constraint system tailored to each computation class.

If you want to prove a Fibonacci computation, you build a Fibonacci constraint system. If you want to prove a Merkle tree inclusion, you build a Merkle constraint system. If you want to prove a signature is valid, you build a signature constraint system. Each one becomes its own engineering project: design the constraints, audit the system, and test for soundness bugs, meaning mistakes in the constraint system that allow invalid witnesses to pass.

The constraints are even more restrictive in practice. These constraint systems are static and fixed-size. There are no loops and no branches in the traditional sense:

- A "loop" that iterates n times must usually be **unrolled** at compile time into n copies of the loop body. A loop that iterates 1,000 times produces a constraint system roughly 1,000 times larger. And the iteration count must be fixed. You can't have a system that loops "until some condition is met."
- An "if-else" branch is typically encoded by evaluating both candidate outcomes and using a selector to choose the correct one. In other words, conditional logic is compiled into arithmetic rather than executed as a runtime branch. Both branches cost computation, even though only one is logically taken.

As a result, writing constraint systems feels nothing like writing ordinary programs. Developers often rely on specialized languages and toolchains such as [Circom](https://web.archive.org/web/20261013134325/https://docs.circom.io/) or [Noir](https://web.archive.org/web/20261013134325/https://noir-lang.org/) ([course](https://web.archive.org/web/20261013134325/https://updraft.cyfrin.io/courses/noir-programming-and-zk-circuits)). Debugging is difficult: when a constraint is unsatisfied, the error message is "constraint 4,372 failed," not "line 42: index out of bounds." Auditing is hard because the constraint system is far removed from the original computation's intent. And the developer pool is tiny, since constraint engineering requires simultaneous expertise in cryptography, algebra, and the proof system's specific format.

For simple, well-scoped applications like proving a Merkle inclusion or verifying a single signature, this model is practical. But as the computation you need to prove grows in complexity, hand-crafting a fresh constraint system for every new application becomes increasingly impractical.

This was not just a theoretical concern. The limits of custom constraint systems became clear once people started trying to prove systems as large and irregular as Ethereum execution. ZK rollups made this limitation concrete.

Rollups emerged as Ethereum's primary scaling strategy. The idea is straightforward: execute transactions off-chain in batches, post the resulting commitments back to L1 (Ethereum), and include some form of correctness guarantee so L1 doesn't have to re-execute everything. For [ZK rollups](https://web.archive.org/web/20261013134325/https://www.cyfrin.io/blog/what-is-a-zk-rollup), that guarantee is a validity proof: a succinct proof that the batch was executed correctly.

The difficulty is that Ethereum isn't a single-purpose computation. It's a general-purpose smart contract platform. Users deploy arbitrary contracts (DeFi protocols, NFT marketplaces, governance systems, games), and each transaction is a different contract call with different logic. A ZK rollup that wants to be EVM-compatible cannot hand-craft a separate constraint system for each possible contract execution. There's no way to know in advance what contracts users will deploy, and the space of possible computations is unbounded.

To get general EVM compatibility, you have to prove the correctness of EVM execution itself rather than hand-crafting a separate constraint system for each contract. In other words, you need a constraint system for the virtual machine itself.

This is the zkEVM approach, and it is technically very demanding. The EVM has on the order of 140 opcodes, complex gas metering, dynamic memory that can grow at runtime, a persistent storage model with cold/warm access patterns, precompiled contracts for cryptographic operations, and many edge cases accumulated over years of EIPs.

Each opcode needs algebraic constraints that capture its behavior. Gas accounting must also be enforced algebraically. Memory expansion costs must be tracked. The resulting system is enormous, leading to large traces and heavy proving workloads even for modest batches.

Projects like [zkSync](https://web.archive.org/web/20261013134325/https://zksync.io/), [Scroll](https://web.archive.org/web/20261013134325/https://scroll.io/), and [Polygon zkEVM](https://web.archive.org/web/20261013134325/https://polygon.technology/polygon-zkevm) have required years of work and large engineering teams to build these systems. The difficulty is structural: the EVM was designed for deterministic execution, not for provability. Its irregular instruction set, stack-based execution model, dynamic memory and storage behavior, and many edge cases do not map naturally to the regular algebraic structure that proof systems require.

This pattern is not limited to rollups. A recent Ethereum [L1 zkEVM roadmap](https://web.archive.org/web/20261013134325/https://ethereum-magicians.org/t/l1-zkevm-roadmap-2026-integrating-zkevm-proofs-into-ethereums-core-protocol/27595) proposes letting validators verify blocks via a succinct proof rather than re-executing every transaction. Rather than building a monolithic zkEVM circuit, the approach compiles EVM validation logic as a program that runs inside a general-purpose ZKVM. The zkEVM becomes "just a program."

This points to the broader insight the zkEVM effort made unavoidable. Once you commit to proving a virtual machine rather than a specific computation, you have made a conceptual leap. The constraint system no longer encodes "this particular business logic." It encodes "this machine's rules." And if the machine is general-purpose, then any program that runs on it is automatically provable.

That's the idea behind ZKVMs, and it doesn't have to be the EVM.

A ZKVM is a proof system in which the statement being proved is: "this program, executed on this virtual machine, produces these outputs." The constraint system encodes the VM's execution rules (how the program counter advances, how instructions modify registers, how memory reads and writes work), not any specific computation.

The ZKVM pipeline, at a high level, works like this:

1. **Compile** your program into a form the VM can execute. You write in a high-level language (like Rust or C), and a compiler translates it into the VM's low-level instructions.
2. **Execute** the program inside the VM, recording every step as an execution trace: a table where each row is one clock cycle, and columns track the machine's state (program counter, registers, memory, etc.).
3. **Arithmetize** the trace. Encode the VM's transition rules as algebraic constraints over the trace. "The program counter incremented by 1" becomes a polynomial equation. "Register r0 was updated to the sum of r1 and r2" becomes another polynomial equation.
4. **Prove** that the trace satisfies all constraints, using a proof system (SNARK, STARK, etc.) to produce a succinct proof.
5. **Verify** the proof much faster than re-executing the full computation.

The crucial point is where the engineering effort goes. In the per-computation model, every new application requires new constraint engineering. In the ZKVM model, the engineering goes into building the VM's constraint system once, and then any program compiled to that VM is automatically provable. The one-time cost is high (building the ZKVM is a major engineering project), but the marginal constraint-engineering cost per new program drops dramatically.

This is what makes ZKVMs practical for rollups, coprocessors, bridges, and any application where you need to prove arbitrary computation. You don't need a team of constraint engineers for every new use case. You need a compiler toolchain and a ZKVM.

In the next part of this article, we'll make all of this concrete. We'll walk through a complete ZKVM implementation, a minimal but fully functional STARK-based system written in Rust, and trace every step of the pipeline: from defining an instruction set, to executing a program, to generating and verifying a proof. The code is deliberately simple: 6 instructions, 4 registers, no memory. But it still captures the same basic STARK pipeline that larger systems like [RISC Zero](https://web.archive.org/web/20261013134325/https://www.risczero.com/) and [SP1](https://web.archive.org/web/20261013134325/https://github.com/succinctlabs/sp1) build on.

Before we write any code, we need to understand what we're actually proving. A ZKVM proves that *a machine executed correctly*. That starts with how machines actually work under the hood: what instructions are, how state changes step by step, and what it takes to express those rules as equations a proof system can check.

Strip away the operating system, the browser, and the programming languages. At the bottom of the stack, a CPU does one thing in a loop: fetch the next instruction, decode it, execute it, repeat. Every program you've ever run reduces to this loop executing billions of times per second.

The **Instruction Set Architecture (ISA)** is the contract that defines this loop precisely. It specifies what instructions exist (the operations the CPU knows), what state they operate on (registers, memory, the program counter), and how they're encoded in binary. The ISA forms the boundary between software and hardware. A compiler turns high-level code into ISA instructions, the hardware executes them, and neither side needs to know the other's internals.

Three concepts show up in almost every ISA:

**Registers** are the CPU's scratchpad, a small number of fast storage slots that instructions read from and write to. A typical CPU might have 32 general-purpose registers, each holding a single word (32 or 64 bits). Arithmetic instructions take their inputs from registers and write results back to registers.

**Opcodes** name the operations. Each instruction has an opcode that tells the CPU *what to do*: `ADD` means add two values, `MUL` means multiply, `LOAD` means fetch a value from memory into a register, `BEQ` means branch (jump) if two values are equal. The opcode is typically the first few bits of the instruction's binary encoding.

**The program counter (PC)** tracks *where* we are in the program. It holds the address of the current instruction. After executing an instruction, the PC typically advances to the next one, unless the instruction is a branch or jump, in which case the PC is set to a different address.

Together, these give us the fetch-decode-execute cycle:

At each step of execution, the machine's state may change: a register gets a new value, the PC moves forward, maybe a memory location is updated. The full sequence of these state changes is what we'll later call the **execution trace**, and it's exactly what a ZKVM needs to prove is correct.

Recall that a ZKVM works by encoding the VM's rules as algebraic constraints, polynomial equations that every valid execution step must satisfy. This is where ISA design directly impacts provability.

**Fewer instructions means fewer constraints.** Every opcode needs constraints that capture its behavior: ADD needs a constraint that the destination register holds the sum, MUL needs one for the product, and so on. An ISA like x86, with a very large and historically accumulated instruction set, would require an enormous number of constraint sets. A minimal ISA like RISC-V, with just 47 base integer instructions, is far more tractable.

**Uniform instruction format means regular constraint structure.** When every instruction has the same bit layout (opcode here, destination register there, source registers there), you can write one generic constraint template that handles decoding, and specialize it per-opcode. ISAs with variable-length instructions (like x86, where a single instruction can be anywhere from 1 to 15 bytes) would require constraints just to figure out where one instruction ends and the next begins. RISC-V's standard fixed-width base encoding avoids this entirely.

**Simple operations mean lower-degree constraints.** Each constraint is a polynomial equation, and polynomial degree matters. Higher-degree constraints make the proof larger and more expensive. A simple "add two registers" instruction produces a low-degree constraint. A more complex instruction often either leads to more complicated constraints or has to be decomposed into several simpler constrained steps.

This is why [RISC-V](https://web.archive.org/web/20261013134325/https://riscv.org/) has become the dominant choice for general-purpose ZKVMs. It's a modern, open-source ISA designed with the kind of regularity that proof systems reward: few instructions, fixed-width encoding, simple operations. Systems like RISC Zero, SP1, and [zkSync's Airbender](https://web.archive.org/web/20261013134325/https://github.com/matter-labs/zksync-airbender) use RISC-V as a compilation target and prove execution of the resulting traces. You write your program in Rust, the Rust compiler emits RISC-V instructions, and the ZKVM proves those instructions executed correctly.

Some projects go further and design ISAs *specifically* for provability:

- [**Cairo**](https://web.archive.org/web/20261013134325/https://www.cairo-lang.org/) (StarkWare) uses a custom ISA where instructions map almost directly to low-degree AIR constraints. The VM has a single read-only memory, a program counter, and an allocation pointer. Every instruction is designed to be easy to constrain.
- [**Miden VM**](https://web.archive.org/web/20261013134325/https://polygon.technology/polygon-miden) (Polygon) is a stack-based VM. Instead of named registers, values live on a stack. Stack operations map naturally to simple transition constraints.

These custom ISAs can achieve better proving performance than RISC-V (because every instruction is designed with the proof system in mind), but they sacrifice toolchain compatibility. You can't just compile existing Rust code to a Cairo program without a specialized compiler.

The tradeoff is clear: **RISC-V gives you the programming ecosystem; custom ISAs give you proving efficiency.** Both approaches are actively used in production.

With this foundation, we understand what a machine is: a state (registers, PC) evolving over time according to an ISA's rules. A ZKVM needs to prove that this evolution was correct, that every step followed the rules. The next section looks at what "proving correct execution" actually means before we introduce any specific proof machinery.

Before diving into any specific math or cryptography, let's understand the strategy for proving a machine executed correctly at a conceptual level.

When a CPU executes a program, its state changes at each execution step: the program counter moves, registers get new values, and the current instruction changes from step to step. If you record a snapshot of that state at every step and write each snapshot as a row in a table, you get a complete record of everything the machine did.

This table is the **execution trace**. Each row is a complete snapshot. The trace is deterministic. Given the same program and the same inputs, you always get the same table. We'll see the exact column layout when we build our VM in section 9, but the idea is simple: one row per execution step, one column per piece of machine state.

The trace is the central object in the entire ZKVM pipeline. Everything that follows (polynomials, constraints, proofs) exists to answer one question: **is this trace valid?**

A valid trace isn't just any table of numbers. Every pair of consecutive rows must be consistent with the ISA's rules. If the opcode at some row is ADD, then the next row's state must reflect the result of that addition.

Concretely, for each transition from row `i` to row `i+1`, the ISA imposes rules like:

- **The clock advances**: `cycle[i+1] = cycle[i] + 1`
- **The PC updates correctly**: for most instructions, `pc[i+1] = pc[i] + 1`. For a HALT, the PC stays put.
- **The right register changes**: if the opcode is `ADD rd, rs1, rs2`, then the value of register `rd` in row `i+1` must equal the sum of the values of registers `rs1` and `rs2` in row `i`
- **Other registers don't change**: every register that *isn't* the destination must have the same value in row `i+1` as in row `i`

If *every* consecutive pair of rows satisfies *all* of these rules, the trace represents a valid execution. If even one transition violates one rule, the trace is invalid. Something went wrong (or was forged).

This gives us a clean definition: **proving correct execution = proving that every row-to-row transition in the trace satisfies the ISA's rules.**

Here is the key step. Those rules we just described in English ("the clock advances," "the right register changes") can be written as **equations**. Each rule becomes an expression that equals zero when the rule is satisfied:

| Rule (English) | Equation (algebra) | 
|---|---|
| "The clock advances by 1" | `cycle[i+1] - cycle[i] - 1 = 0` | 
| "Register r0 stays the same when the instruction doesn't write to r0" | `(r0[i+1] - r0[i]) × s = 0`, where `s = 0` when r0 is the destination | 
| "The PC increments by 1" | `pc[i+1] - pc[i] - 1 = 0` | 

If we write *all* the rules as equations like this, then a valid trace is one where every equation equals zero at every row.

This is called **arithmetization**: turning computational rules into arithmetic, or more precisely algebraic, equations. It's the key step that bridges the gap between "a computer executed a program" and "a set of mathematical equations are satisfied."

Why is this useful? Because the world of polynomial equations has powerful tools. Once our rules are equations, we can:

1. Encode the trace as polynomials (one polynomial per column, passing through all the values in that column)
2. Express the rules as polynomial identities (equations that must hold for all points in the trace)
3. Use proof systems to verify those identities efficiently

The key property: polynomial equations can be checked efficiently. Rather than verifying every row of the trace individually, the proof system can compress all those checks into a single polynomial relationship that the verifier evaluates at a handful of random points. We'll see exactly how this works in section 10.

Putting it all together, here's the full pipeline that a ZKVM follows, and that we'll build step by step in the coming sections:

Steps 1–4 are the "VM side": defining the computation and encoding its rules as algebra. Steps 5–6 are the "proof side": mathematics and cryptography. We'll build the VM side in full detail. For the proof side, we'll cover enough to understand what each step does and why. The proof machinery is generic infrastructure shared across all STARK systems.

Each step in this pipeline maps to a module in our codebase. Let's start with our own toy instruction set and VM.

Time to open the [codebase](https://web.archive.org/web/20261013134325/https://github.com/ubermensch3dot0/toy-zkvm). Here are the specifics of our toy ZKVM:

- **4 registers** (r0-r3)
- **6 instructions** (NOP, IMM, ADD, MUL, SUB, HALT)
- **No memory**, all data lives in registers
- **All arithmetic in a finite field** (the Goldilocks field, which we'll cover in section 10)

This is a minimal VM built around the same core ideas used in production ZKVMs like RISC Zero or SP1. Everything we learn here maps directly to how those systems work.

Here's the full instruction set, all six opcodes:

| Opcode | Value | Operation | Description | 
|---|---|---|---|
| NOP | 0 | (nothing) | No operation. Used to pad the trace. | 
| IMM | 1 | `rd = imm` | Load an immediate value into a register. | 
| ADD | 2 | `rd = rs1 + rs2` | Add two registers, store the result. | 
| MUL | 3 | `rd = rs1 * rs2` | Multiply two registers, store the result. | 
| SUB | 4 | `rd = rs1 - rs2` | Subtract two registers, store the result. | 
| HALT | 5 | (stop) | End execution. | 

A few things are worth noticing:

**Every arithmetic operation is a field operation**, not a regular integer operation. When we say `rd = rs1 + rs2`, we mean addition modulo the Goldilocks prime. Arithmetic is defined directly modulo the Goldilocks prime, so there is no separate overflow behavior to reason about. The field arithmetic is the semantics. This matters because the proof system works over this field, and the VM must match.

**NOP exists for padding.** The proof system requires power-of-two trace lengths, so short programs are padded with NOP rows (section 9).

**There are no branches or jumps.** Execution is strictly sequential: the PC advances by 1 on ordinary instructions, and HALT terminates execution. This is a major simplification. Real ISAs have conditional branches, function calls, and loops. We omit them because they'd add constraint complexity without teaching new concepts.

In Rust, the opcodes are a simple enum with integer values:

```
#[derive(Debug, Clone, Copy, PartialEq, Eq)]
#[repr(u8)]
pub enum Opcode {
    Nop  = 0,  // No operation (used for trace padding)
    Imm  = 1,  // rd = imm
    Add  = 2,  // rd = rs1 + rs2
    Mul  = 3,  // rd = rs1 * rs2
    Sub  = 4,  // rd = rs1 - rs2
    Halt = 5,  // Stop execution
}
```
The `#[repr(u8)]` attribute ensures each opcode maps to a specific integer. This matters because the trace stores opcodes as numeric field elements, and later the constraint system will use those values to select the right instruction behavior.

Every instruction uses the same uniform format, five fields, always present:

```
pub struct Instruction {
    pub opcode: Opcode,  // which operation (0–5)
    pub rd: u8,          // destination register index (0–3)
    pub rs1: u8,         // first source register index (0–3)
    pub rs2: u8,         // second source register index (0–3)
    pub imm: u64,        // immediate value (used by IMM instruction)
}
```
Not every instruction uses every field. ADD uses `rd`, `rs1`, and `rs2` but ignores `imm`. IMM uses `rd` and `imm` but ignores `rs1` and `rs2`. HALT ignores all of them. But the format is always the same. Every instruction occupies exactly the same "shape" in the trace.

**This uniformity is deliberate and important for the proof system.** If different instructions had different numbers of fields, the trace table would have an irregular structure that is much harder to constrain. With a uniform format, every row of the trace has the same 13 columns, and the constraint system can apply the same polynomial template to every row.

To make programs readable, builder functions let you write instructions naturally:

```
impl Instruction {
    pub fn nop() -> Self {
        Instruction { opcode: Opcode::Nop, rd: 0, rs1: 0, rs2: 0, imm: 0 }
    }
    pub fn imm(rd: u8, value: u64) -> Self {
        assert!(rd < 4, "register index must be 0–3");
        Instruction { opcode: Opcode::Imm, rd, rs1: 0, rs2: 0, imm: value }
    }
    pub fn add(rd: u8, rs1: u8, rs2: u8) -> Self {
        assert!(rd < 4 && rs1 < 4 && rs2 < 4);
        Instruction { opcode: Opcode::Add, rd, rs1, rs2, imm: 0 }
    }
    pub fn mul(rd: u8, rs1: u8, rs2: u8) -> Self {
        assert!(rd < 4 && rs1 < 4 && rs2 < 4);
        Instruction { opcode: Opcode::Mul, rd, rs1, rs2, imm: 0 }
    }
    pub fn sub(rd: u8, rs1: u8, rs2: u8) -> Self {
        assert!(rd < 4 && rs1 < 4 && rs2 < 4);
        Instruction { opcode: Opcode::Sub, rd, rs1, rs2, imm: 0 }
    }
    pub fn halt() -> Self {
        Instruction { opcode: Opcode::Halt, rd: 0, rs1: 0, rs2: 0, imm: 0 }
    }
}
```
Notice the `assert!` guards on register indices. There are only 4 registers (0–3), so any index outside that range is a bug. The unused fields are zeroed out, not left undefined. This is important: when these values land in the trace, they become field elements that feed into constraints. Leaving them garbage would cause constraint violations. Note that these are Rust-level checks on program construction. They do not produce algebraic constraints in the proof, so a malicious prover who constructs a trace directly could bypass them. We omit the corresponding algebraic range checks for simplicity and return to this in section 14.

You might wonder: why not more instructions? Why not memory? Why only 4 registers?

As section 6 explained, fewer instructions means fewer constraints, and simpler operations usually lead to simpler, lower-degree constraint systems. This ISA captures the three essential concerns every ZKVM must handle: opcode dispatch (selectors), register reads/writes (register selectors), and arithmetic correctness, without the accidental complexity of a real ISA. Production systems like RISC Zero operate over much richer ISAs with larger register files and many more instructions, but the underlying constraint patterns are similar. By starting small, we can see them clearly.

With our instruction set defined, the VM follows the fetch-decode-execute cycle from section 6, made concrete:

```
pub fn execute(program: &[Instruction]) -> ExecutionTrace {
    let mut regs: [Fp; 4] = [Fp::ZERO; 4];
    let mut pc: usize = 0;
    let mut rows: Vec<TraceRow> = Vec::new();
    loop {
        let inst = &program[pc];
        let clk = rows.len() as u64;
        // Look up source register values
        let rs1_val = regs[inst.rs1 as usize];
        let rs2_val = regs[inst.rs2 as usize];
        // Record the state BEFORE executing this instruction
        rows.push(TraceRow {
            clk: Fp::new(clk),
            pc: Fp::new(pc as u64),
            opcode: Fp::new(inst.opcode as u64),
            rd: Fp::new(inst.rd as u64),
            rs1: Fp::new(inst.rs1 as u64),
            rs2: Fp::new(inst.rs2 as u64),
            imm: Fp::new(inst.imm),
            r0: regs[0],
            r1: regs[1],
            r2: regs[2],
            r3: regs[3],
            rs1_val,
            rs2_val,
        });
        // Execute the instruction
        match inst.opcode {
            Opcode::Nop  => {}
            Opcode::Imm  => { regs[inst.rd as usize] = Fp::new(inst.imm); }
            Opcode::Add  => { regs[inst.rd as usize] = rs1_val + rs2_val; }
            Opcode::Mul  => { regs[inst.rd as usize] = rs1_val * rs2_val; }
            Opcode::Sub  => { regs[inst.rd as usize] = rs1_val - rs2_val; }
            Opcode::Halt => { break; }
        }
        pc += 1;
    }
    ExecutionTrace::new(rows)
}
```
The state starts zeroed: all registers are `Fp::ZERO`, PC is 0. Each iteration fetches the instruction at `program[pc]`, records the current state as a trace row, executes the instruction, and, for non-HALT instructions, advances the PC. HALT terminates the loop.

There's one subtle but critical detail here: **the trace records the state *before* each instruction executes, not after.** Look at the order: we push the `TraceRow` first, *then* execute the `match`. This means row `i` in the trace shows the machine state at the moment instruction `i` is about to run. The *effect* of that instruction shows up in row `i+1`.

Why? Because the transition constraints relate consecutive rows: they say "given the state in row `i` and the opcode in row `i`, the state in row `i+1` must be such-and-such." If we recorded state *after* execution, we'd need to look *back* a row to find the opcode that caused the change, which complicates the constraint structure.

Each trace row captures the complete VM state in 13 fields:

```
pub struct TraceRow {
    pub clk: Fp,      // Clock cycle (0, 1, 2, ...)
    pub pc: Fp,       // Program counter
    pub opcode: Fp,   // Current instruction's opcode (0–5)
    pub rd: Fp,       // Destination register index
    pub rs1: Fp,      // First source register index
    pub rs2: Fp,      // Second source register index
    pub imm: Fp,      // Immediate value
    pub r0: Fp,       // Register 0 value
    pub r1: Fp,       // Register 1 value
    pub r2: Fp,       // Register 2 value
    pub r3: Fp,       // Register 3 value
    pub rs1_val: Fp,  // Value of register rs1
    pub rs2_val: Fp,  // Value of register rs2
}
```
The first 7 columns (`clk` through `imm`) describe *what's happening*: which instruction is executing and what its operands are. The next 4 (`r0` through `r3`) capture *the machine state*, the value of every register. The last 2 (`rs1_val`, `rs2_val`) are the actual values read from the source registers.

The `rs1_val` and `rs2_val` columns might seem redundant. We already have `r0` through `r3` in the row, and `rs1` tells us which register to read. But the constraint system works with polynomial equations over column values. It has no way to say "look up the register at index `rs1`," because that would require array indexing, and polynomials can't do that. Instead, we store the looked-up values explicitly and use additional constraints to verify they match the right registers. Section 11 covers exactly how.

`(3 + 4)² - (3 + 4) = 42`
Let's trace through a concrete program. Here's the one from `main.rs`. It computes `(3 + 4)² - (3 + 4) = 49 - 7 = 42`:

```
let program = vec![
    Instruction::imm(0, 3),       // r0 = 3
    Instruction::imm(1, 4),       // r1 = 4
    Instruction::add(2, 0, 1),    // r2 = r0 + r1 = 7
    Instruction::mul(3, 2, 2),    // r3 = r2 * r2 = 49
    Instruction::sub(0, 3, 2),    // r0 = r3 - r2 = 42
    Instruction::halt(),          // stop
];
```
Six instructions. Let's walk through execution step by step and see what the trace looks like. Remember, each row records the state *before* the instruction executes:

**Row 0,** `IMM r0, 3`**:** All registers start at 0. The trace records `clk=0, pc=0, opcode=1(IMM), rd=0, imm=3, r0=0, r1=0, r2=0, r3=0`. After execution, `r0` becomes 3.

**Row 1,** `IMM r1, 4`**:** Now `r0=3` from the previous step. The trace records `clk=1, pc=1, opcode=1(IMM), rd=1, imm=4, r0=3, r1=0, r2=0, r3=0`. After execution, `r1` becomes 4.

**Row 2,** `ADD r2, r0, r1`**:** Registers are `r0=3, r1=4`. The trace records `clk=2, pc=2, opcode=2(ADD), rd=2, rs1=0, rs2=1, r0=3, r1=4, r2=0, r3=0, rs1_val=3, rs2_val=4`. After execution, `r2` becomes 7.

**Row 3,** `MUL r3, r2, r2`**:** Registers are `r0=3, r1=4, r2=7`. The trace records `clk=3, pc=3, opcode=3(MUL), rd=3, rs1=2, rs2=2, r0=3, r1=4, r2=7, r3=0, rs1_val=7, rs2_val=7`. After execution, `r3` becomes 49.

**Row 4,** `SUB r0, r3, r2`**:** Registers are `r0=3, r1=4, r2=7, r3=49`. The trace records `clk=4, pc=4, opcode=4(SUB), rd=0, rs1=3, rs2=2, r0=3, r1=4, r2=7, r3=49, rs1_val=49, rs2_val=7`. After execution, `r0` becomes 42.

**Row 5,** `HALT`**:** Registers are `r0=42, r1=4, r2=7, r3=49`. The trace records `clk=5, pc=5, opcode=5(HALT), r0=42, r1=4, r2=7, r3=49`. Execution stops.

Here's the full trace as a table:

| clk | pc | op | rd | rs1 | rs2 | imm | r0 | r1 | r2 | r3 | rs1\_val | rs2\_val | 
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 0 | 1 | 0 | 0 | 0 | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 
| 1 | 1 | 1 | 1 | 0 | 0 | 4 | 3 | 0 | 0 | 0 | 3 | 3 | 
| 2 | 2 | 2 | 2 | 0 | 1 | 0 | 3 | 4 | 0 | 0 | 3 | 4 | 
| 3 | 3 | 3 | 3 | 2 | 2 | 0 | 3 | 4 | 7 | 0 | 7 | 7 | 
| 4 | 4 | 4 | 0 | 3 | 2 | 0 | 3 | 4 | 7 | 49 | 49 | 7 | 
| 5 | 5 | 5 | 0 | 0 | 0 | 0 | 42 | 4 | 7 | 49 | 42 | 42 | 

Notice how adjacent rows encode the ISA rules. Between rows 2 and 3: the opcode is 2 (ADD), `rd=2`, `rs1_val=3`, `rs2_val=4`, and in row 3 `r2` has changed from 0 to 7 (= 3 + 4). Every other register stayed the same. That's exactly what the transition constraints will verify, but algebraically, not by inspection.

Our program produces 6 trace rows. But the proof system needs the trace length to be a power of two (we'll see why in section 10). So 6 rows must become 8.

The padding rows are NOP instructions that do nothing. Registers stay frozen at their last values:

```
pub fn pad_to_power_of_two(&mut self) {
    let target = self.rows.len().next_power_of_two();
    while self.rows.len() < target {
        let clk = self.rows.len() as u64;
        let prev = *self.rows.last().unwrap();
        self.rows.push(TraceRow::padding(clk, &prev));
    }
}
```
Each padding row is constructed from the previous row:

```
pub fn padding(clk: u64, prev: &TraceRow) -> Self {
    TraceRow {
        clk: Fp::new(clk),
        pc: prev.pc,                        // PC stays the same
        opcode: Fp::new(Opcode::Nop as u64), // NOP instruction
        rd: Fp::ZERO,
        rs1: Fp::ZERO,
        rs2: Fp::ZERO,
        imm: Fp::ZERO,
        r0: prev.r0,    // All registers copied from previous row
        r1: prev.r1,
        r2: prev.r2,
        r3: prev.r3,
        rs1_val: prev.r0,  // rs1=0, so rs1_val = r0
        rs2_val: prev.r0,  // rs2=0, so rs2_val = r0
    }
}
```
A few things to note:

- The **clock keeps incrementing**. The constraint system will check that `clk[i+1] = clk[i] + 1` for *every* row, including padding.
- The **PC freezes**. In the padded tail of the trace, NOP rows are treated like a halted state: the PC and registers stay fixed. This is a modeling choice for the AIR, not a claim about how a runtime NOP usually behaves. We collapse both HALT and padding into a "no further state change" case to keep the constraints simple.
- **Register values are copied** from the previous row. Since NOP doesn't modify any register, the "next row has the same register values" constraint is trivially satisfied.
- `rs1_val` **and** `rs2_val` **must be consistent**, since `rs1=0` and `rs2=0` in the padding row, both lookup values must equal `r0`. The padding function sets this correctly.

This last point matters. You can't just fill padding rows with zeros. They still have to satisfy every transition constraint. A padding row that claimed `rs1=0` but had `rs1_val=999` would fail the register lookup constraint. The padding must be *valid under the constraint system*, not just empty space.

After padding, our 6-row trace becomes 8 rows, and the padded trace now satisfies the structural requirements of the proof pipeline.

We've built a VM, executed a program, and produced a trace. Now we need to *prove* the trace is valid, without the verifier re-executing the program. This is where the proof machinery comes in.

The rest of the pipeline uses several mathematical and cryptographic building blocks: finite fields, polynomials, evaluation domains, Merkle trees, a hash-based challenge protocol, and a low-degree testing protocol called FRI. These are generic STARK infrastructure. Variants of these ingredients appear across modern STARK-based systems, usually in much more optimized form.

This section gives you enough intuition about each building block to follow the constraint system (section 11) and the prover/verifier pipeline (section 12). We won't go into implementation details or code. The goal is to understand *what* each piece does and *why* it's needed. If the math doesn't fully click on first read, that's fine. The later sections will make more sense once you've seen the pieces in action.

*For readers wanting the full implementation story: see [StarkWare's STARK 101](https://web.archive.org/web/20261013134325/https://starkware.co/stark-101/), [Vitalik's STARKs series](https://web.archive.org/web/20261013134325/https://vitalik.eth.limo/general/2017/11/09/starks_part_1.html), or the [source code](https://web.archive.org/web/20261013134325/https://github.com/ubermensch3dot0/toy-zkvm) (`src/field.rs`, `src/polynomial.rs`, `src/domain.rs`, `src/merkle.rs`, `src/channel.rs`, `src/fri.rs`).*

We already covered finite fields in section 2: a set of numbers where arithmetic is defined modulo a prime, every nonzero element has a multiplicative inverse, and all operations stay inside the field. The proof pipeline needs all of those properties: fixed-size elements, exact arithmetic (polynomial identities must hold precisely), and universal division (making polynomial division and interpolation well-defined).

The specific field we use is built around the [**Goldilocks prime**](https://web.archive.org/web/20261013134325/https://polygon.technology/blog/plonky2-a-deep-dive): `p = 2^64 - 2^32 + 1`. It was chosen because it fits in a single 64-bit word (fast arithmetic) and supports the power-of-two domain sizes that the proof system needs (as we'll see later in this section). Every value you see typed as `Fp` in the code is a number mod this prime.

The trace is a table of numbers. The proof system works with polynomials. So the first step is to convert each column of the trace into a polynomial. What does that mean?

Take the `clk` column from our 8-row trace: it holds the values `[0, 1, 2, 3, 4, 5, 6, 7]` (the clock increments every row, even during padding). We want a polynomial `P(x)` such that when we evaluate it at 8 specific points, we get back exactly those 8 values. That is:

```
P(d₀) = 0,  P(d₁) = 1,  P(d₂) = 2,  ...,  P(d₇) = 7
```
where `d₀, d₁, ..., d₇` are the points of the **trace domain** (a set of 8 special field elements we'll define shortly in this section). The polynomial encodes the column: its values at the domain points are exactly the column's entries.

Given `n` distinct points and `n` values, there is exactly one polynomial of degree less than `n` that passes through all of them. Finding it is called **Lagrange interpolation**. For our 8-row trace, each column becomes a degree-7 polynomial. We do this for all 13 columns, producing 13 polynomials that fully encode the trace.

Why go through this trouble? Because once the trace is encoded as polynomials, we can express the VM's transition rules as **polynomial equations** (section 11) and then use a powerful fact to check them efficiently.

Here's the key insight: if you pick a random point and two low-degree polynomials give the same value there, they're almost certainly the same polynomial everywhere. This is called the [**Schwartz-Zippel lemma**](https://web.archive.org/web/20261013134325/https://rareskills.io/post/schwartz-zippel-lemma). Why? A degree-`d` polynomial can be zero at most `d` times. So if two degree-`d` polynomials differ, they can only "accidentally" agree at `d` out of `~2^64` field elements, which is vanishingly unlikely for a random check.

This is why checking a polynomial identity at a random point gives overwhelming evidence that it holds everywhere. That's the core of how "verify every row of the trace" compresses into "verify a few random evaluations."

Earlier in this section, we said the trace columns are evaluated at "8 special field elements." What are those elements, and why are they special?

**The trace domain** is the set of points where the trace polynomials take on the actual trace values. We need 8 points (one per row), and we choose them with a very specific structure.

Pick a field element `ω` such that `ω⁸ = 1` but no smaller power of `ω` equals 1. Then the powers `{1, ω, ω², ω³, ω⁴, ω⁵, ω⁶, ω⁷}` are 8 distinct elements that cycle back to 1. This set is called the "8th roots of unity" because each element, raised to the 8th power, equals 1.

To make this concrete, let's work in a tiny field: integers mod 17. Here `ω = 9` is an 8th root of unity because `9⁸ mod 17 = 1`. The 8 domain points are `{1, 9, 13, 15, 16, 8, 4, 2}`. Multiplying by 9 cycles through them: `1 → 9 → 13 → 15 → 16 → 8 → 4 → 2 → 1`. Each multiplication is just `× 9 mod 17`.

We assign trace rows to these points: row 0 at `1`, row 1 at `9`, row 2 at `13`, and so on. The advantage is that "the next row" is always "multiply by `ω`." To compare row `i` with row `i+1`, the constraint system just compares `P(x)` with `P(ωx)`. Select a trace column below and step through to see this in action:

The real system uses the Goldilocks field (`p ≈ 2⁶⁴`), which has roots of unity for any power-of-two size up to `2³²`. The math is identical, just with bigger numbers. We'll see in section 11 how this structure makes constraint checking natural. For a deeper treatment of roots of unity in finite fields, see [this article by RareSkills](https://web.archive.org/web/20261013134325/https://rareskills.io/post/roots-of-unity-finite-field).

In section 11, we'll build a **constraint polynomial** `C(x)` that bundles all 8 of our VM's transition rules into a single polynomial expression. The details of how it's built can wait. For now, the only thing that matters is one property: **if the trace is valid,** `C(x)` **evaluates to zero at every point in the trace domain.**

Every transition rule ("clock increments by 1", "the right register updates", etc.) contributes a term that equals zero when the rule is satisfied. If all rules hold at every row, the entire polynomial is zero at every trace domain point.

So how do we prove that `C(x)` is zero at all 8 trace points without checking each one? This is where a basic fact about polynomials helps. If a polynomial is zero at some point `r`, then `(x - r)` divides it evenly. For example, if `f(x)` is zero at `x = 2`, `x = 3`, and `x = 5`, then `(x - 2)(x - 3)(x - 5)` divides `f(x)` with no remainder. This is just the factor theorem from algebra.

The **vanishing polynomial** `Z_H(x)` is the polynomial that equals zero at exactly the trace domain points. Written out, that's `Z_H(x) = (x - 1)(x - ω)(x - ω²)···(x - ω^{n-1})`. But there's a simplification. Every trace domain point is an n-th root of unity: `(ω^k)^n = (ω^n)^k = 1^k = 1`. That means every trace point satisfies `x^n = 1`, or equivalently `x^n - 1 = 0`. Since `x^n - 1` is a degree-n polynomial with exactly n roots, and those roots are exactly our trace domain points, it must be the same polynomial: `Z_H(x) = x^n - 1`. This compact form is much cheaper to evaluate than multiplying out all n factors.

If `C(x)` is really zero at all those points, then `Z_H(x)` must divide `C(x)` cleanly.

The prover demonstrates this by computing the **quotient**: `Q(x) = C(x) / Z_H(x)`. If the division is exact (no remainder), `Q(x)` is a valid low-degree polynomial. If the trace was invalid and `C(x)` was *not* zero at some trace point, the division wouldn't be clean, and `Q(x)` would not be a proper low-degree polynomial. The proof system would catch this (via FRI, covered later in this section).

The prover needs to compute this quotient at many points to commit to it (via a Merkle tree, covered next). But it can't evaluate `C(x) / Z_H(x)` at the trace domain points, because `Z_H(x) = 0` there, and dividing by zero is undefined. So the prover evaluates on a separate, larger set of points called the **LDE (Low-Degree Extension) domain**. In our construction, this domain is 8× bigger than the trace domain (64 points for our 8-row trace) and *shifted* so that none of its points coincide with the trace domain. The shift guarantees `Z_H(x) ≠ 0` at every LDE point, making the division safe.

The verifier's check at a random point `z` is then: does `C(z) = Q(z) · Z_H(z)`? By Schwartz-Zippel, if this holds at a random point, it holds everywhere with overwhelming probability.

Two pieces of infrastructure tie the algebra to a real proof:

**Merkle trees** let the prover commit to polynomial evaluations. A single 32-byte hash (the tree root) locks in all the data. Later, the prover can reveal any individual value with a short proof path (a chain of sibling hashes from the leaf to the root). The verifier checks that the revealed value matches the committed root. This prevents the prover from changing its data after the fact.

**The Fiat-Shamir transform** replaces the interactive verifier's randomness with deterministic hashes of the prover's commitments. In an interactive proof, the verifier would send random challenges after each prover step. In a non-interactive proof, the prover hashes its own commitments to derive those challenges. Both prover and verifier maintain the same hash-based "channel," feeding in the same commitments and squeezing out the same challenges. This makes the proof a single message from prover to verifier, while ensuring the prover can't "shop for" favorable randomness. For a visual walkthrough, see [this video by KoalateeCtrl](https://web.archive.org/web/20261013134325/https://youtu.be/lYV-d9LzlFI?si=p-bzMM3MQk6vU1AA).

The quotient trick only works if `Q(x)` is actually a low-degree polynomial. A cheating prover could commit (via Merkle trees) to evaluations that do not come from any low-degree polynomial, yet still pass the quotient check at a few sampled points. We need a way to verify that the committed evaluations actually come from a low-degree polynomial.

**FRI** (Fast Reed-Solomon IOP of Proximity) does this. The core idea is repeated compression: the prover takes the polynomial's evaluations and, using random challenges derived via Fiat-Shamir, folds them down in stages. Each stage halves the number of values. If the original evaluations came from a genuine low-degree polynomial, each stage stays consistent. If they didn't, inconsistencies appear. After enough rounds of folding, the remaining object should be extremely low degree; in our toy setting, eventually just a constant.

The verifier spot-checks this process: it picks random query points, opens the values at each folding stage via Merkle proofs, and checks that each fold was computed correctly. In our parameterization, 30 queries gives roughly 90 bits of soundness. For a deeper dive into FRI, see [this video by StarkWare](https://web.archive.org/web/20261013134325/https://www.youtube.com/watch?v=gd1NbKUOJwA).

This is the conceptual heart of the ZKVM. We have a trace table and a set of ISA rules. The **Algebraic Intermediate Representation (AIR)** expresses those rules as polynomial equations over adjacent trace rows. If all equations equal zero at every row, the trace is valid.

This section is where the ZKVM-specific logic meets the proof machinery from section 10. The selectors and constraints here are what make *this particular VM* provable. Different VMs (RISC-V, Cairo, Miden) have different AIRs, but they all follow the same pattern.

In the VM's `execute` function, we used a `match` statement:

```
match inst.opcode {
    Opcode::Add => { regs[inst.rd as usize] = rs1_val + rs2_val; }
    Opcode::Mul => { regs[inst.rd as usize] = rs1_val * rs2_val; }
    ...
}
```
In the AIR, we can't branch. Everything must be a polynomial expression. So how do we handle "do different things for different opcodes"?

**Selector polynomials.** For each opcode value `t`, we need a function that equals 1 when `opcode == t` and 0 for every other valid opcode. Here's a simple way to build one.

Start with the product `(opcode - 0)(opcode - 1)(opcode - 2)(opcode - 3)(opcode - 4)(opcode - 5)`. This equals zero for *every* valid opcode, because one of the factors is always zero. Now remove the factor for the opcode we want to select. For ADD (opcode 2), drop the `(opcode - 2)` factor, leaving `(opcode - 0)(opcode - 1)(opcode - 3)(opcode - 4)(opcode - 5)`. This expression is zero for every opcode *except* 2. When `opcode = 2`, all the remaining factors are nonzero, giving some non-one value. Dividing by that value (a constant we can precompute) normalizes the result to exactly 1.

The result: a function that behaves like a one-hot selector on the valid opcode values 0 through 5. It returns 1 for ADD and 0 for everything else.

| opcode | 0 | 1 | **2** | 3 | 4 | 5 | 
|---|---|---|---|---|---|---|
| sel | 0 | 0 | **1** | 0 | 0 | 0 | 

This is called a Lagrange basis polynomial. In code:

```
pub fn opcode_selector(opcode: Fp, target: u64) -> Fp {
    let mut num = Fp::ONE;
    let mut den = Fp::ONE;
    let t = Fp::new(target);
    for v in 0..NUM_OPCODES {
        if v == target { continue; }
        let fv = Fp::new(v);
        num = num * (opcode - fv);
        den = den * (t - fv);
    }
    num * den.inv()
}
```
This selector has degree 5 (product of 5 linear terms). We need the same trick for registers. When a constraint needs to check whether register `r2` is the destination, it uses a register selector built the same way, but over the set `{0, 1, 2, 3}` (our 4 register indices) instead of `{0, 1, 2, 3, 4, 5}`. These selectors have degree 3:

```
pub fn register_selector(idx: Fp, target: u64) -> Fp {
    let mut num = Fp::ONE;
    let mut den = Fp::ONE;
    let t = Fp::new(target);
    for v in 0..NUM_REGS {
        if v == target { continue; }
        let fv = Fp::new(v);
        num = num * (idx - fv);
        den = den * (t - fv);
    }
    num * den.inv()
}
```
With selectors, we can turn branching into arithmetic. Instead of "if ADD do this, if MUL do that," we compute *every* case, multiply each by its selector, and add them up:

```
result = sel_add * (rs1_val + rs2_val) + sel_mul * (rs1_val * rs2_val) + ...
```
**This assumption is load-bearing but not algebraically enforced.** If the opcode column contains a valid value (0–5), exactly one selector is 1 and the rest are 0 at any given row. Every term except the matching one is multiplied by zero and vanishes. Only the correct operation's result survives. But if a malicious prover placed an out-of-range value like `opcode = 6` in the trace, every selector would evaluate to some nonzero value, and the constraint would see a weighted blend of all operations, not a clean match to any single instruction. The same applies to register indices used in `register_selector`. We omit the algebraic range checks that would prevent this for simplicity and discuss the implications in section 14.

Now let's walk through all 8 constraints. Each one is a polynomial expression over the current row and the next row. A valid trace makes every constraint evaluate to zero at every row.

First, some setup values used by multiple constraints:

```
let op = current[2];     // opcode
let rd = current[3];     // destination register index
let imm = current[6];    // immediate value
let rs1_val = current[11];
let rs2_val = current[12];
// Opcode selectors
let s_nop  = opcode_selector(op, 0);
let s_imm  = opcode_selector(op, 1);
let s_add  = opcode_selector(op, 2);
let s_mul  = opcode_selector(op, 3);
let s_sub  = opcode_selector(op, 4);
let s_halt = opcode_selector(op, 5);
// Is this a writing instruction? (IMM, ADD, MUL, SUB)
let is_write = s_imm + s_add + s_mul + s_sub;
// What value gets written to the destination register?
let write_val = s_imm * imm
    + s_add * (rs1_val + rs2_val)
    + s_mul * (rs1_val * rs2_val)
    + s_sub * (rs1_val - rs2_val);
```
`is_write` equals 1 for any instruction that modifies a register, 0 for NOP and HALT. `write_val` uses the selector trick to compute the correct result for whichever opcode is active. Only one selector is 1, so only the matching term contributes.

**C0, Clock increments by 1:**

```
let c0 = next[0] - current[0] - Fp::ONE;
```
This is the simplest constraint. `clk[i+1] - clk[i] - 1 = 0` at every row, including padding.

**C1, PC update:**

```
let c1 = (s_nop + s_halt) * (next[1] - current[1])
    + (s_imm + s_add + s_mul + s_sub) * (next[1] - current[1] - Fp::ONE);
```
Two cases: NOP and HALT keep the PC unchanged (`next_pc - cur_pc = 0`), while write instructions increment it (`next_pc - cur_pc - 1 = 0`). Recall from section 9 that in this AIR, padded NOP rows are treated like a halted state, so both NOP and HALT leave the PC unchanged. The selectors pick the right case. Since exactly one opcode selector is active, exactly one term is nonzero. If that term is zero, the constraint passes.

**C2–C5, Register updates (one constraint per register):**

```
for i in 0..4 {
    let sel_i = register_selector(rd, i as u64);
    let cur_ri = current[7 + i];
    let next_ri = next[7 + i];
    reg_constraints[i] = next_ri - cur_ri - sel_i * is_write * (write_val - cur_ri);
}
```
This constraint compactly handles all register-update cases. Let's unpack it:

- `register_selector(rd, i)` is 1 if `rd == i` (this register is the destination), 0 otherwise
- `is_write` is 1 if the instruction writes, 0 otherwise (NOP, HALT)
- `write_val - cur_ri` is the *change* that would be applied

The expression `next_ri - cur_ri - sel_i * is_write * (write_val - cur_ri) = 0` means:

- **If this register IS the destination AND the instruction writes:** `sel_i = 1`, `is_write = 1`, so `next_ri = cur_ri + (write_val - cur_ri) = write_val`. The register gets the new value.
- **If this register is NOT the destination:** `sel_i = 0`, so `next_ri = cur_ri`. The register is preserved.
- **If the instruction doesn't write (NOP/HALT):** `is_write = 0`, so `next_ri = cur_ri`. All registers are preserved.

One expression, no branching, handles all cases.

**C6–C7, Register lookup consistency:**

```
// C6: rs1_val must equal the register at index rs1
let rs1_idx = current[4];
let mut rs1_expected = Fp::ZERO;
for i in 0..4 {
    rs1_expected = rs1_expected
        + register_selector(rs1_idx, i as u64) * current[7 + i];
}
let c6 = current[11] - rs1_expected;
// C7: rs2_val must equal the register at index rs2
let rs2_idx = current[5];
let mut rs2_expected = Fp::ZERO;
for i in 0..4 {
    rs2_expected = rs2_expected
        + register_selector(rs2_idx, i as u64) * current[7 + i];
}
let c7 = current[12] - rs2_expected;
```
Remember from section 9: the AIR can't do array indexing. These constraints verify that `rs1_val` and `rs2_val` actually match the right registers. For valid register indices, the selector `register_selector(rs1_idx, i)` is 1 when `rs1 == i`, so the sum `Σ sel(rs1, i) * r_i` picks out exactly the register value at index `rs1`. The constraint checks that `rs1_val` equals this sum.

We have 8 constraints, and we need to check them all. Rather than handling them separately through the entire proof pipeline, we combine them into a **single** composition polynomial using a random linear combination:

```
pub fn evaluate_composition(
    current: &[Fp; NUM_COLUMNS],
    next: &[Fp; NUM_COLUMNS],
    alpha: Fp,
) -> Fp {
    let constraints = evaluate_transition_constraints(current, next);
    let mut result = Fp::ZERO;
    let mut alpha_power = Fp::ONE;
    for c in &constraints {
        result = result + alpha_power * *c;
        alpha_power = alpha_power * alpha;
    }
    result
}
```
The composition is `C(x) = c0 + α·c1 + α²·c2 + ... + α⁷·c7`, where `α` is a random challenge derived from the Fiat-Shamir transcript (section 10).

Why is a random combination safe? If any individual constraint `cᵢ` is nonzero at some point, the composition `C` is nonzero at that point with overwhelming probability, because `α` is random and accidental cancellation between constraints is negligibly unlikely. So, with overwhelming probability over the choice of `α`, checking `C(x) = 0` is enough to enforce all 8 constraints simultaneously.

This reduces the prover's job from "prove 8 polynomials are zero on the trace domain" to "prove 1 polynomial is zero on the trace domain."

The composition polynomial's degree matters because it determines the quotient polynomial's degree, which determines how much work the prover and verifier do.

Opcode selectors have degree 5 (product of 5 linear terms). Register selectors have degree 3. In the register update constraints (C2–C5), we multiply a register selector (degree 3) by `is_write` (sum of opcode selectors, degree 5) by `write_val` (which itself involves opcode selectors times trace values). The resulting constraint polynomial has high degree.

More specifically, the trace polynomials have degree \< `n` (the trace length). In this toy construction, a rough upper bound puts the composition degree around `12n`, and the quotient `Q(x) = C(x) / Z_H(x)` around `11n`. This is why the LDE domain needs to be much larger than the trace. We're evaluating a high-degree polynomial and need enough points to commit to it securely.

All the building blocks are in place: the VM produces a trace, the AIR encodes the VM's rules as algebraic constraints, and the proof toolkit (section 10) provides the mathematical and cryptographic infrastructure. The prover assembles everything into a proof; the verifier checks it cheaply.

Here's how the prover takes an execution trace and produces a compact proof, step by step:

**1. Interpolate:**
The trace is a table of numbers, but the proof system works with polynomials. So the first step is to convert each of the 13 columns into a polynomial that passes through all of that column's values (using the Lagrange interpolation from section 10).
For our 8-row trace, each column becomes a degree-7 polynomial. After this step, the trace is fully encoded as 13 polynomials.

**2. Extend:**
Evaluate those 13 polynomials on the LDE domain (8× more points than the trace domain). The extra evaluations are completely determined by the polynomials, so no new information is added. But they give the verifier many more points to spot-check later.

**3. Commit:**
Build a Merkle tree over the LDE evaluations. Each leaf packs all 13 column values at one LDE point. The Merkle root, a single 32-byte hash, locks in the entire trace. This is the first piece of the proof.

**4. Challenge:**
Feed the program (public input) and the trace root into the Fiat-Shamir channel, then squeeze out `α`, the random challenge for combining the 8 constraints into the composition polynomial (section 11).
Why absorb the program? Because `α`, and every subsequent challenge, now depends on the declared program. If we skipped this, a prover could take a valid proof for program A and relabel it as a proof for program B, since the challenges would be identical. Absorbing the program prevents that post-hoc relabeling trick.
Why absorb the trace root? Because the prover must commit to the trace *before* seeing `α`. If `α` did not depend on the trace commitment, the prover could try to tailor the trace to a convenient challenge rather than answering a random one.
**Caveat:** absorbing the program binds the challenges to the declared program, but nothing in the AIR checks that the committed trace actually matches that program. A malicious prover could still produce a trace derived from a different program, or fabricate a trace directly, and declare yours. Section 14 explains this gap.

**5. Constrain:**
Evaluate the composition polynomial `C(x) = Σ αⁱ · Cᵢ(x)` at every LDE point, using the AIR from section 11. Each evaluation uses trace values from two adjacent rows (current and next) to check all 8 constraints at that point.

**6. Quotient:**
Divide: `Q(x) = C(x) / Z_H(x)` at each LDE point. If the trace is valid, `C(x)` is zero everywhere on the trace domain, so this division is exact and `Q(x)` is a valid low-degree polynomial.
If the trace was invalid, the resulting quotient evaluations will fail the low-degree test.

**7. Commit quotient:**
Build another Merkle tree, this time over the quotient evaluations. Feed its root into the Fiat-Shamir channel.

**8. FRI:**
Prove that `Q(x)` is actually low-degree, not evaluation data that fails to correspond to any low-degree polynomial. This is the repeated folding protocol from section 10: each round folds the evaluations into a smaller representation, reducing the degree bound and halving the domain size, then commits to the result and derives the next challenge.

**9. Open queries:**
Derive random query indices from the channel. At each query, the prover reveals the trace values, the quotient value, and Merkle proofs authenticating all of them. These are the specific points the verifier will check.

The proof bundles everything the verifier needs:

```
pub struct StarkProof {
    pub trace_root: [u8; 32],         // Commitment to trace LDE
    pub quotient_root: [u8; 32],      // Commitment to quotient LDE
    pub fri_proof: FriProof,          // FRI proof that Q(x) is low-degree
    pub query_responses: Vec<QueryResponse>,  // Opened values + Merkle proofs
    pub query_indices: Vec<usize>,    // Which LDE points were queried (convenience; verifier re-derives its own)
    pub program: Vec<Instruction>,    // The program (public input)
    pub outputs: [Fp; 4],            // Claimed register outputs
    pub trace_length: usize,         // Padded trace length
    pub real_trace_length: usize,    // Actual execution length
}
```
Two Merkle roots, a FRI proof, and a handful of opened values with their authentication paths. The verifier receives this proof and checks it without ever seeing the full trace or the full polynomial evaluations.

The verifier never sees the trace. It receives only the proof object and checks it without re-executing the full program:

**1. Re-derive challenges:**
The verifier reconstructs the same Fiat-Shamir channel the prover used: it feeds in the program, the trace root, the quotient root, and the FRI layer roots, squeezing challenges at each stage.
Because both sides hash the same data in the same order, they arrive at the same random challenges. This is how the verifier "replays" the prover's randomness without any communication.

**2. Derive FRI challenges:**
Replay the FRI commit phase by absorbing each layer root and squeezing the folding challenges (betas). This advances the transcript to the same state the prover reached after FRI commit.

**3. Derive query indices:**
Squeeze query indices from the channel. These are the random positions the verifier will check. Because they're derived after all commitments, the prover couldn't have anticipated them.
Crucially, the verifier derives its own query indices rather than trusting the ones in the proof. Otherwise a malicious prover could choose favorable query points or omit queries entirely.

**4. Verify FRI:**
Check that the quotient polynomial `Q(x)` is actually low-degree. For each query point, open the Merkle proofs at each folding layer and check that each fold was computed correctly using the betas from step 2.
If FRI passes, the verifier is convinced `Q(x)` is a genuine low-degree polynomial.

**5. For each query point:**

- **Verify Merkle proofs** for the trace values and the quotient value. This confirms the prover is using values it actually committed to, not values fabricated after seeing the challenges.
- **Re-evaluate the composition polynomial** `C(x)` from the opened trace values using the AIR (section 11). The verifier computes this from scratch at this one point, trusting nothing from the prover.
- **Check the quotient equation:** does `C(z) = Q(z) · Z_H(z)` at this query point? If `C(x)` really is zero on the trace domain, and `Q(x)` is the clean quotient, this equation holds. If anything was tampered with, it fails.

**6. Boundary constraints:**
As an educational simplification, boundary conditions are checked outside the polynomial machinery. The verifier confirms the program ends with HALT, but it does not verify `proof.outputs` against the committed trace at all; the claimed outputs are taken on trust.
In a production system, boundary constraints are polynomial equations evaluated at *specific* trace points (not all adjacent pairs), with their own vanishing terms, folded into the same composition polynomial. For example, "register r0 equals the claimed output at the last real row" becomes a constraint `P_r0(ω^k) - claimed_r0 = 0`, divided by `(x - ω^k)` and combined with the transition constraints. This makes output correctness part of the same cryptographic guarantee as transition correctness.
Our simplified approach means a malicious prover can claim arbitrary outputs and the verifier will accept them. The quotient check doesn't catch it because boundary constraints don't participate in the composition, and the verifier never opens the trace at the specific row where outputs live.

When verification passes, the verifier has established a chain of guarantees:

- **Q(x) is low-degree (FRI)** → `C(x)` is divisible by `Z_H(x)` → constraints hold at all trace rows
- **Opened values are authentic (Merkle proofs)** → the prover used the data it committed to
- **Challenges couldn't be anticipated (Fiat-Shamir)** → the prover couldn't manipulate randomness

Therefore, **a committed trace satisfies all transition constraints.** The verifier is convinced that some execution trace passes the AIR checks, without ever re-executing a single instruction. But note what this does *not* prove in our simplified system: the trace is not constrained to match the declared program (no program-consistency constraints), the claimed outputs are not verified against the trace (no boundary constraints in the composition), and the initial state is unchecked. Section 14 details each gap.

The prover performs substantially more computation: polynomial interpolation (O(n²) in our naive implementation, O(n log n) with NTT), multi-point evaluation, Merkle tree construction, and FRI folding. The verifier checks a handful of Merkle proofs (O(log n) hashes each) and evaluates the constraint equation at those points. This qualitative asymmetry persists as program length grows. A program with a million instructions would produce a longer trace and a bigger proof, but the verifier's work grows only slowly, typically logarithmically or polylogarithmically in the trace length.

This prover-verifier asymmetry is the central property that makes STARKs useful.

Every module is built. Let's put them together and watch the entire pipeline run, from program definition to a verified proof. The demo in `main.rs` is short, but it exercises every stage we've discussed.

The same program from section 9, computing `(3 + 4)² - (3 + 4) = 42` in six instructions. The result (42 in register `r0`) is what the prover will claim as the output. As discussed in section 14, the verifier does not independently verify that these claimed outputs match the committed trace.

```
let mut trace = vm::execute(&program);
trace.pad_to_power_of_two();
```
The VM produces the 6-row trace from section 9, then padding extends it to 8 rows (the next power of two) with NOP instructions that freeze the register state. The two padding rows (rows 6–7) have `opcode=NOP`, the PC frozen at 5, all registers holding their final values, and the clock still incrementing (as the constraint system demands).

Before generating a proof, the demo verifies the constraints directly, a sanity check that our trace is valid:

```
match air::verify_trace_constraints(&trace.rows) {
    Ok(()) => println!("  All transition constraints satisfied!"),
    Err((row, constraint)) => {
        println!("  CONSTRAINT VIOLATION at row {}, constraint {}", row, constraint);
        return;
    }
}
```
This function iterates over every pair of adjacent rows and evaluates all 8 transition constraints. If any constraint returns a nonzero value at any row, execution stops. This is the "honest" way to check: evaluate everything directly, no cryptography involved. It's O(n) and requires the full trace. The STARK proof exists to replace this with something the verifier can check without the trace.

```
let proof = prover::prove(&trace, &program);
```
This single line triggers the entire prover pipeline from section 12: it interpolates 13 columns, evaluates them on the LDE domain, commits via Merkle trees, derives challenges, evaluates constraints, computes the quotient, runs FRI, and opens query points.

```
match verifier::verify(&proof) {
    Ok(()) => {
        println!("  *** PROOF VERIFIED ***");
        println!("  The verifier is convinced that:");
        println!("    - A valid program was executed correctly");
        println!("    - The execution trace satisfies all {} transition constraints",
            air::NUM_CONSTRAINTS);
        println!("    - The quotient polynomial is low-degree (FRI verified)");
        println!("    - Output: r0={}, r1={}, r2={}, r3={}",
            proof.outputs[0], proof.outputs[1], proof.outputs[2], proof.outputs[3]);
    }
    Err(e) => {
        println!("  PROOF REJECTED: {}", e);
    }
}
```
The printed summary overstates what the proof actually guarantees. The transition constraints and FRI check are cryptographically verified, but the claimed program and outputs are not checked against the committed trace. The verifier confirms the declared program ends with HALT and prints `proof.outputs`, but both are taken on trust. See section 14 for the full list of simplifications.

Without ever seeing the full trace, the verifier re-derives the Fiat-Shamir challenges, verifies FRI, checks Merkle proofs and the quotient equation at each query point, and checks that the declared program ends with HALT. When the output reads `*** PROOF VERIFIED ***`, every check has passed.

In this toy parameterization, the verifier is cryptographically convinced, with roughly 90 bits of soundness, that *some* valid execution trace satisfies all transition constraints and is consistent with a low-degree quotient polynomial. The declared program is absorbed into the Fiat-Shamir challenges, and the claimed outputs are carried in the proof and printed by the verifier, but neither is independently checked against the committed trace (see section 14 for details on what this means for soundness).

We've built a complete pipeline (execution, trace, arithmetization, proof, verification) in about 2,500 lines of Rust. The pipeline is complete and produces valid proofs. But it omits many of the features that make production ZKVMs substantially more complex. Understanding these gaps is as important as understanding the pipeline itself, because they define where the real engineering challenges lie.

**No memory.** Our VM has 4 registers and nothing else. Real programs need RAM: arrays, stacks, heaps. In a ZKVM, memory is hard because the trace records sequential execution, but memory accesses can be random (any address, any time). You can't just add a "memory" column and constrain it row-by-row, because a store to address 1000 at cycle 5 might be read at cycle 500,000. Production systems handle this with **memory-checking arguments**: they sort the memory accesses by address and check consistency using permutation arguments or lookup tables (like [LogUp](https://web.archive.org/web/20261013134325/https://eprint.iacr.org/2022/1530) or [Plookup](https://web.archive.org/web/20261013134325/https://eprint.iacr.org/2020/315)). This adds major auxiliary subsystems of constraints and trace columns, and is one of the primary sources of complexity in real ZKVMs.

**No zero-knowledge.** Our proof is not zero-knowledge: it reveals trace information through the opened evaluations. The LDE values, committed via Merkle trees and opened at query points, expose actual trace data. A verifier (or anyone who sees the proof) can learn register values, opcodes, and intermediate state. Production STARKs add **masking polynomials**, random low-degree polynomials added to the trace polynomials to randomize the evaluations without affecting constraint satisfaction. This is what puts the "ZK" in ZKVM. We skipped it because it's orthogonal to understanding the proving pipeline.

**Boundary constraints not folded into composition.** Our verifier performs only a minimal boundary check: it confirms the declared program ends with HALT. It does *not* verify that `proof.outputs` matches the committed trace at the HALT row. The claimed outputs are taken on trust. In a real system, boundary constraints are polynomial equations evaluated at *specific* trace points (not all adjacent pairs), with their own vanishing terms, folded into the same composition polynomial. For example, "register r0 equals the claimed output at the last real row" becomes a constraint `P_r0(ω^k) - claimed_r0 = 0`, divided by `(x - ω^k)` and combined with the transition constraints. This makes them part of the same cryptographic guarantee. Our simplified approach means a malicious prover can claim arbitrary outputs.

**No range constraints on trace columns.** The selector polynomials in section 11 assume that `opcode ∈ {0,1,2,3,4,5}` and `rd, rs1, rs2 ∈ {0,1,2,3}`. But the AIR contains no constraint enforcing these ranges. A Lagrange basis polynomial over {0,1,2,3,4,5} evaluates to 1 at exactly one point and 0 at the others, but only within that set. Feed it a value outside the set (say, `opcode = 6`), and every selector returns a nonzero value. The constraint becomes a weighted blend of all operations, not a clean match to any single instruction. In our system, the Rust-level `assert!` guards on `Instruction` builders prevent this during honest execution, but they are not algebraic constraints. A malicious prover who constructs a trace directly bypasses them. The fix is straightforward: add vanishing polynomial constraints like `opcode · (opcode - 1) · (opcode - 2) · (opcode - 3) · (opcode - 4) · (opcode - 5) = 0` and `rd · (rd - 1) · (rd - 2) · (rd - 3) = 0` (and similarly for `rs1`, `rs2`). These are zero exactly when the value is in the valid set, and nonzero otherwise. We omit them to keep the constraint count at 8, but any production system requires them.

**No program-consistency constraints.** The proof includes the program as a public input and absorbs it into the Fiat-Shamir transcript, which binds all challenges to the *declared* program and prevents a proof from being relabeled after the fact. But the AIR never constrains the trace's instruction columns (`opcode`, `rd`, `rs1`, `rs2`, `imm`) to match the instruction fetched from that public program at the current PC. In a production ZKVM, this is enforced by a **program memory table**: the prover commits to the program as a lookup table mapping `(pc → opcode, rd, rs1, rs2, imm)`, and a cross-table lookup argument (e.g., LogUp) constrains every trace row to fetch its instruction from that table. Without this, the verifier is not actually proving "this exact public program was executed," only that some committed trace satisfied the transition constraints under challenges derived from the declared program. A malicious prover could generate a valid trace from program A, declare program B, and the verifier would accept it.

**No initial-state constraints.** The VM starts execution with `pc = 0` and all registers zeroed, but the verifier never checks that the committed trace starts from this state. Like the output claims, the initial state is a boundary condition that would need to be folded into the composition polynomial (e.g., `P_r0(ω⁰) - 0 = 0`, divided by `(x - ω⁰)`) or verified via a dedicated Merkle opening of the first trace row. Without either mechanism, a malicious prover could start the trace from arbitrary register values and the verifier would not detect it.

**No recursion or aggregation.** Production ZKVMs often need to prove very long computations, millions or billions of cycles. A single STARK proof for that would be enormous. The solution is **recursive proving**: split the execution into segments, prove each segment separately, then prove that the segment proofs are valid. The verifier itself becomes a program that runs inside the ZKVM, generating a "proof of a proof." This technique (used by RISC Zero, SP1, and others) compresses very long computations into a much more succinct proof. It requires the ZKVM to be able to efficiently verify its own proofs, a significant engineering challenge.

**Naive polynomial arithmetic.** Our Lagrange interpolation is O(n²). For each of n basis polynomials, we do O(n) work. Our polynomial multiplication is also O(n²). Production systems use the **Number Theoretic Transform (NTT)**, the finite-field analogue of the FFT, to do interpolation and multiplication in O(n log n). For a trace of 2²⁰ rows (\~1 million), that's the difference between \~10¹² operations and \~2 × 10⁷. NTT is why production provers are fast enough to be practical, and why the Goldilocks prime's large power-of-two subgroup matters. The radix-2 NTT used here requires a power-of-two multiplicative subgroup.

**6 instructions vs. hundreds.** Our ISA has no branches, no jumps, no memory loads/stores, no comparison operations, no function calls. Real RISC-V has 47 base instructions (RV32I) plus extensions for multiplication, atomics, and more. Each additional instruction means more selector polynomials, more constraint cases, and higher constraint degree. A full RISC-V ZKVM like RISC Zero or SP1 has thousands of constraints across dozens of constraint types, organized into multiple AIR tables that interact via cross-table lookup arguments. The constraint engineering alone is a multi-year effort for a team of specialists.

Each of these omissions represents a substantial body of work in production systems. But the *pipeline* (execute, trace, arithmetize, prove, verify) is the same. The six-instruction version and production RISC-V systems follow the same high-level pipeline. The differences are scale, optimization, and engineering depth, not architecture.

We've walked through every stage of the pipeline that makes the ZKVM pattern work. Prove the machine once, and any program compiled to its ISA is automatically provable:

- **An ISA** (section 8) defines what the machine can do: 6 opcodes, 4 registers, a uniform instruction format.
- **A VM** (section 9) executes programs and records an execution trace, a complete table of machine state at every execution step.
- **The proof toolkit** (section 10) provides the mathematical substrate: finite fields, polynomials, evaluation domains, Merkle commitments, Fiat-Shamir challenges, and FRI.
- **The AIR** (section 11) translates the VM's rules into algebra. Selector polynomials replace branching; 8 transition constraints encode the entire ISA. This is where ZKVM-specific engineering lives.
- **The prover and verifier** (section 12) assemble the pipeline: interpolate, evaluate, commit, compose, divide, prove; then verify with a handful of Merkle proofs and one equation per query.

This is the same conceptual pipeline used across production STARK-based ZKVMs: SP1, ZisK, Ceno, Pico, ZKsync Airbender, and others tracked on [ethproofs.org/zkvms](https://web.archive.org/web/20261013134325/https://ethproofs.org/zkvms). The differences are the ISA (RISC-V rv32/rv64 vs. Cairo vs. MIPS vs. custom), the scale (millions of constraints vs. our 8), and the optimizations (NTT, recursion, GPU acceleration). But the underlying conceptual architecture (execute, trace, arithmetize, prove, verify) is the same.

The boundary between these two layers, the ZKVM-specific AIR and the generic proof infrastructure (fields, polynomials, FRI, Merkle trees), is what separates "knows how STARKs work" from "understands how to build a ZKVM."

Ethereum's L1 is actively moving in this direction. Through the [Ethproofs](https://web.archive.org/web/20261013134325/https://www.ethproofs.org/) initiative, the protocol is working toward letting validators verify blocks via succinct proofs rather than re-executing every transaction. The approach follows the same pattern: EVM validation logic compiled as a guest program inside a general-purpose RISC-V ZKVM. Teams building ZKVM provers, including SP1 and others tracked by Ethproofs, are pushing toward real-time Ethereum block proving. The pipeline you just built, execute, trace, arithmetize, prove, verify, is the same pipeline these teams are scaling to production.

The [code](https://web.archive.org/web/20261013134325/https://github.com/ubermensch3dot0/toy-zkvm) is available to run, modify, and experiment with directly. Change the program and watch the trace change. Add a new opcode and see what constraints it needs. Break a constraint and watch the proof fail. The best way to understand a proof system is to build one, and now you have.

**Learning**

- [Fundamentals of Zero-Knowledge Proofs](https://web.archive.org/web/20261013134325/https://updraft.cyfrin.io/courses/fundamentals-of-zero-knowledge-proofs) (Cyfrin Updraft)
- [Noir Programming and ZK Circuits](https://web.archive.org/web/20261013134325/https://updraft.cyfrin.io/courses/noir-programming-and-zk-circuits) (Cyfrin Updraft)
- [ZK Math 101: Modular Arithmetic](https://web.archive.org/web/20261013134325/https://www.cyfrin.io/blog/zk-math-101-modular-arithmetic) (Cyfrin)
- [ZK Math 101: Rings and Fields](https://web.archive.org/web/20261013134325/https://www.cyfrin.io/blog/zk-math-101-rings-and-fields) (Cyfrin)
- [What is a ZK Rollup?](https://web.archive.org/web/20261013134325/https://www.cyfrin.io/blog/what-is-a-zk-rollup) (Cyfrin)
- [RareSkills ZK Book](https://web.archive.org/web/20261013134325/https://rareskills.io/zk-book)
- [StarkWare STARK 101](https://web.archive.org/web/20261013134325/https://starkware.co/stark-101/)
- [Vitalik's STARKs series](https://web.archive.org/web/20261013134325/https://vitalik.eth.limo/general/2017/11/09/starks_part_1.html)
- [Proofs, Arguments, and Zero-Knowledge](https://web.archive.org/web/20261013134325/https://people.cs.georgetown.edu/jthaler/ProofsArgsAndZK.html) (Thaler)

**Production ZKVMs** (see [ethproofs.org/zkvms](https://web.archive.org/web/20261013134325/https://ethproofs.org/zkvms) for live stats)

- [SP1](https://web.archive.org/web/20261013134325/https://github.com/succinctlabs/sp1) (Succinct) — rv64im
- [ZisK](https://web.archive.org/web/20261013134325/https://github.com/0xPolygonHermez/zisk) (ZisK) — rv64ima
- [Ceno](https://web.archive.org/web/20261013134325/https://github.com/scroll-tech/ceno) (Scroll) — rv32im
- [Pico](https://web.archive.org/web/20261013134325/https://github.com/brevis-network/pico) (Brevis) — rv32im
- [ZKsync Airbender](https://web.archive.org/web/20261013134325/https://github.com/matter-labs/zksync-airbender) (Matter Labs) — rv32im
- [Ziren](https://web.archive.org/web/20261013134325/https://www.zkm.io/) (ZKM) — MIPS
- [RISC Zero](https://web.archive.org/web/20261013134325/https://www.risczero.com/) — rv32im
- [Cairo](https://web.archive.org/web/20261013134325/https://www.cairo-lang.org/) (StarkWare) — custom ISA
- [Miden VM](https://web.archive.org/web/20261013134325/https://polygon.technology/polygon-miden) (Polygon) — stack-based

**Ethereum L1 Integration**

**Papers**

Join some of the biggest protocols and companies in creating a better internet. Our security researchers will help you throughout the whole process.
