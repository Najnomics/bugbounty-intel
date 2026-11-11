# Cryptographic primitive bugs (nonce reuse, RNG, padding oracle, malleability, curves, ZK)

_Harness check spec. Drawn from RustSec crypto advisories and the 0xPARC ZK bug tracker. Nothing invented._

## Detection signals
- Nonce / IV reuse in AES-GCM, ChaCha20-Poly1305, or ECDSA/Ed25519.
- Weak or predictable RNG seeding.
- Padding-oracle-shaped APIs (error distinguishes padding vs MAC).
- Signature malleability (ECDSA s-value, Ed25519 cofactor).
- Missing point validation / bad curves / twist attacks.
- Timing-variable comparisons on secrets (`subtle` / constant-time failures).
- ZK: underconstrained signals, missing range/boolean constraints, verifier free/replay branches.

## Sources (full text)
- [`projects/crypto/advisories-index.md`](../../projects/crypto/advisories-index.md) — 76 RustSec crypto advisories (aes-gcm, chacha20, curve25519-dalek, ed25519-dalek, ring, rustls, rsa, blake2, argon2, …).
- [`projects/crypto/zk-bug-tracker-readme.md`](../../projects/crypto/zk-bug-tracker-readme.md) — 0xPARC ZK bug tracker.
- Zcash Orchard underconstrained circuit: [`projects/zcash/advisories/ghsa-ghc3-g8w4-whf9.md`](../../projects/zcash/advisories/ghsa-ghc3-g8w4-whf9.md).
- Harness ZK/TEE classes: [`zk-circuits.md`](zk-circuits.md), [`tee-attestation.md`](tee-attestation.md).

## Automation (check spec)
```
for crate in crypto_deps:
  if rustsec_advisory(crate): FLAG
scan for AES-GCM/ChaCha with caller-supplied nonce reused across messages
scan ECDSA for missing low-s / nonce determinism (RFC 6979)
for circuit_signal: if not fully_constrained: FLAG underconstrained
```
