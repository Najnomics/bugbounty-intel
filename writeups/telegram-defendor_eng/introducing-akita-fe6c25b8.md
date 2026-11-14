# 🔐 LayerZero Launches Akita, a Post-Quantum Polynomial Commitment Scheme

- **Source URL:** https://layerzero.network/blog/introducing-akita
- **Fetched:** 2026-11-14
- **Channel:** @defendor_eng
- **Telegram message:** https://t.me/defendor_eng/2077 (id 2077)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
Today we’re introducing Akita, a new polynomial commitment scheme (PCS) that provides quantum-resistant security for zero-knowledge proving systems. The first production-ready primitive of its kind, Akita delivers post-quantum security alongside proof sizes that are 2x to 8x smaller than current post-quantum alternatives.

Akita is a standalone primitive and can be adopted by any proof system seeking post-quantum security. Its first major deployment will be inside [Jolt](https://layerzero.network/blog/jolt-bytecode-expansion-formal-verification), the ZK proving system developed in partnership with a16z crypto that underpins the Zero blockchain. This makes Jolt the fastest production-grade zero-knowledge virtual machine (zkVM) that offers quantum resistance, all while delivering dramatically smaller proofs - a major step in building Zero for a post-quantum world.

You can read the [full technical paper](https://assets.layerzero.network/pdf/akita.pdf) and explore the [Akita implementation on GitHub](https://github.com/LayerZero-Labs/akita).

### **What is Akita?**

Akita is a polynomial commitment scheme, the foundational component inside a ZK proving system responsible for committing to and proving the correctness of a computation trace. Replacing this component with a quantum-secure alternative secures the entire proving stack, as the rest of the stack is information-theoretically secure.

Akita’s architecture is lattice-based, the same class of mathematics standardized by NIST for post-quantum encryption and signature, currently rolling out to protect all encrypted internet traffic in the near future.

Akita's performance profile is distinct from existing post-quantum proving approaches:

- **Proof size:** Post-quantum proving systems built on hash-based schemes typically produce proofs of 200kb or more. Akita produces proofs that are 65-80kb in size, a 2x to 8x reduction depending on the application.
- **Proving time:** Proving with Akita is 2–3x faster than what Jolt currently delivers.
- **Memory usage:** Akita reduces Jolt's memory usage by \~2x. In fact, beyond storing the polynomial itself, Akita uses sub-linear memory for commitment & proving, allowing the proving system to scale to enormous program sizes without reliance on recursive composition.

### **Lattices over hashes**

There are two primary paths to post-quantum proving systems: hash-based schemes and lattice-based schemes. While hash-based approaches have seen significant development, lattice-based assumptions offer additional upsides:

- Drastic reduction in proof size
- Dramatic performance improvements for sparse workloads
- Simpler integration with the rest of the post-quantum Internet

Akita is the first commitment scheme to bring lattice-based security to a production-ready ZK proving system.

### **A landmark deployment: Jolt**

Akita is an open-source primitive that any proof system can use to enable quantum-resistant proving. Its first deployment will be inside Jolt, the zkVM developed in partnership with a16z crypto. This implementation means that Jolt can deliver post-quantum security while simultaneously decreasing proof size and accelerating prover speed by 2-3x. Akita makes Jolt the state-of-the-art zkVM on most major axes of interest: proof size (amongst post-quantum solutions), prover time, and prover memory.

### **Looking ahead**

Akita represents the first significant step toward a fully quantum-secure Zero stack. As the industry works to harden systems against potential threats from quantum computing to current cryptographic assumptions, building quantum-resistant infrastructure is a critical priority. More work is yet to be done, and will continue as we approach mainnet and beyond.
