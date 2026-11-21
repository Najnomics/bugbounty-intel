# sha256-collisions-verifier

- **Source URL:** https://collisions.zksecurity.xyz/
- **Fetched:** 2026-11-21
- **Researcher:** zksecurityXYZ
- **Method:** curl + trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---

One digest.

A hash function turns any input into a short fingerprint. No two inputs should get the same one. Here are 123 pairs that do, and you can run every one.

When a hash gets broken, you usually hear a claim and a number like 2<sup>63</sup>. That's hard to check. A collision is easy: hash both inputs and look.

15 pairs break full hash functions, including MD5 and SHA-1. The other 108 use weakened or modified versions. The SHA-256 and SHA-3 examples do not break the full hashes.
