# @kobigurk (Kobi Gurkan)

Compiled 23 Nov 2026 (WAT). Watched for the ZK / cryptography layer; full verbatim archive in [`posts/kobigurk/ARCHIVE.md`](../posts/kobigurk/ARCHIVE.md).

## 2026-11-23 — Formal verification of Rust crypto/encoding code in Lean
- Points to his "conjuring proofs for cryptographic code" thread (arkworks + EthLib Lean spec) in reply to the post "Proving Rust code in Lean with Aeneas" (Ethereum encoding library).
- **Takeaway:** Aeneas (Rust→Lean via Charon) + executable Lean specs can prove Rust crypto/encoding code equivalent to a spec; unsupported features (loops, trait objects, unsafe) mark where manual review must focus.
- **Local:** [posts/kobigurk/2026-11-23-2124712979723874790.md](../posts/kobigurk/2026-11-23-2124712979723874790.md), [writeups/kobigurk/aeneas-proving-rust-in-lean-ethereum-encoding.md](../writeups/kobigurk/aeneas-proving-rust-in-lean-ethereum-encoding.md)
