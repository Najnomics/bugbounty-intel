# 🧩 Homomorphisms — the foundation of zero-knowledge

- **Source URL:** https://www.defendor.xyz/zk-math-101-how-homomorphisms-power-zero-knowledge-proofs
- **Fetched from:** https://web.archive.org/web/20250901084418/https://www.defendor.xyz/zk-math-101-how-homomorphisms-power-zero-knowledge-proofs/
- **Fetched:** 2026-11-25
- **Channel:** @defendor_eng
- **Telegram message:** https://t.me/defendor_eng/496 (id 496)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
[Education](https://web.archive.org/web/20250901084418/https://www.defendor.xyz/tag/education/)

# ZK Math 101: How Homomorphisms Power Zero-Knowledge Proofs

**Source:** [ZK Math 101: Homomorphisms | Cyfrin](https://web.archive.org/web/20250901084418/https://www.cyfrin.io/blog/zk-math-101-homomorphisms?ref=defendor.xyz)

Homomorphisms act as **mathematical bridges** between different algebraic structures, enabling operations on transformed data without losing the original relationships. This property is crucial in zero-knowledge (ZK) proofs, where you want to prove knowledge of secret data **without revealing it**.

## What is a Homomorphism?

A **homomorphism** is a function between two algebraic structures (like groups or rings) that **preserves their operations**. If you think of these structures as different “mathematical worlds,” a homomorphism translates elements from one to the other **without breaking the rules**.

For example, consider two groups, (G, ∘) and (H, ⋆). A function ϕ: G → H is a group homomorphism if for all elements a and b in G:

ϕ(a ∘ b) = ϕ(a) ⋆ ϕ(b)

This means doing the operation first, then mapping, is the same as mapping first, then doing the operation - preserving structure exactly.

## Key Properties of Homomorphisms

When ϕ is a group homomorphism, it also:

- **Preserves identity elements:** The identity in G maps to the identity in H.
- **Preserves inverses:** The inverse of an element maps to the inverse of the image.
- **Preserves powers:** ϕ(aⁿ) = (ϕ(a))ⁿ for integer n.

These ensure the algebraic framework remains consistent under transformation.

## Examples Made Simple

### 1. Exponential Function as Homomorphism

The exponential function, exp, maps real numbers under addition (R, +) to positive real numbers under multiplication (R⁺, ⋅):

exp(x + y) = exp(x) ⋅ exp(y)

This means adding two numbers then exponentiating equals exponentiating each and multiplying - an elegant homomorphic relationship.

### 2. Modulo Reduction as Ring Homomorphism

The function f(a) = a mod n maps integers (Z) to integers modulo n (Z/nZ), preserving addition and multiplication:

- f(a + b) = f(a) + f(b) mod n
- f(a ⋅ b) = f(a) ⋅ f(b) mod n

This shows modulo arithmetic respects the ring structure of integers.

## Homomorphisms in Zero-Knowledge Proofs

In ZK proofs, homomorphisms allow:

- **Committing to secret values** in a way that **hides them but preserves relationships**.
- Performing computations on **commitments** instead of raw data-e.g., C(x₁,r₁) + C(x₂,r₂) = C(x₁ + x₂, r₁ + r₂).
- Ensuring commitments are **binding** (can’t be reversed or forged) and **hiding** (keep inputs secret).

In PLONK and other ZK systems, commitments are often to **polynomials**, enabling complex constraints to be verified publicly without revealing secret inputs, thanks to the homomorphic nature of polynomial operations.

## Why This Matters

Homomorphisms are the **mathematical foundation** that lets ZK proofs “translate” secrets into public commitments, preserving the essential properties for verification **without sacrificing privacy**. This makes them indispensable for secure, private computations in Web3.
