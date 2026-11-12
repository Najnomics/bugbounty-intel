# GHSA-7fx8-hmgc-82jp: Missing on-curve check in emulated fake-GLV scalar multiplication allows ECDSA / P256Verify signature forgery

| Field | Value |
| --- | --- |
| Repo | Consensys/gnark (Go ZK-SNARK library) |
| GHSA | GHSA-7fx8-hmgc-82jp |
| CVE | none assigned |
| Severity | high |
| CWE | CWE-20, CWE-347 |
| Published | 2026-10-07T10:18:57Z |
| Affected | github.com/consensys/gnark < v0.16.4 (patched: v0.16.4) |
| Credits | oppenheim, sbudella-gco, yelhousni |
| Advisory URL | https://github.com/Consensys-Incorporated/gnark/security/advisories/GHSA-7fx8-hmgc-82jp |
| Captured | 2026-11-12 (WAT) |

## Description (verbatim)

## Description

### Impact

A soundness bug in gnark's emulated short-Weierstrass gadget (`std/algebra/emulated/sw_emulated`) lets a malicious prover produce a valid proof for a circuit that verifies an ECDSA signature which was never produced by the private key. Proofs verify normally with the honest verification key; no trusted-setup or verifier modification is needed.

On curves without an efficient endomorphism — **P-256 (secp256r1), P-384 (secp384r1) and the STARK curve** — variable-base scalar multiplication uses the "fake GLV" method. The result `[s]P` is supplied by the prover as a hint and checked through a relation instead of being computed in-circuit. The circuit did not assert that the hinted point lies on the curve. Together with the prover-supplied scalar decomposition, an off-curve point can satisfy the relation, so the gadget returns a point that is chosen by the prover rather than `[s]P`.

Affected APIs when instantiated over P-256, P-384 or the STARK curve:

- `sw_emulated.Curve.ScalarMul`
- `sw_emulated.Curve.JointScalarMulBase`
- `sw_emulated.Curve.MultiScalarMul`
- `std/signature/ecdsa`: `PublicKey.Verify`, `PublicKey.IsValid`
- `std/evmprecompiles.P256Verify` (EIP-7951 / RIP-7212)

For ECDSA and `P256Verify`, this allows a prover to forge a signature on an arbitrary message under an arbitrary public key, without the private key. Any application that relies on these gadgets for authorization — wallets with passkey/WebAuthn or secp256r1 keys, JWT/ES256 or X.509/eIDAS credential verification, zkEVM P256VERIFY precompile proving — is affected.

Not affected:

- Curves with an efficient endomorphism (secp256k1, BN254, BLS12-381, BW6-761). These use different algorithms. secp256k1/BN254 still receive the same on-curve check in 0.16.4 as defense in depth.
- `ScalarMulBase` / fixed-base scalar multiplication by a constant point. These use the in-circuit fixed-base comb method.
- Native (non-emulated) curve gadgets in `std/algebra/native`.
- Versions before 0.12.0. These computed the scalar multiplication in-circuit.

### Patches

Fixed in **v0.16.4**. The hinted result of the fake-GLV scalar multiplication is now constrained to lie on the curve, and the API documentation now states that `ScalarMul`, `JointScalarMulBase` and `MultiScalarMul` return a point on the curve and in the prime-order subgroup, on every supported curve.

Upgrade with:

```
go get github.com/consensys/gnark@v0.16.4
```

**Circuits must be recompiled and a new setup (proving/verifying keys) must be generated.** The fix adds constraints, so keys generated with an affected version stay vulnerable even after upgrading the library. For Groth16 this means a new circuit-specific setup (new MPC ceremony if applicable); for PLONK, new proving/verifying keys from the universal SRS. Redeploy any verifier contracts that embed the old verifying key.

### Workarounds

There is no workaround for `ecdsa.Verify`, `ecdsa.IsValid` or `evmprecompiles.P256Verify` other than upgrading. The intermediate point is not exposed to the caller.

Callers of `sw_emulated.Curve.ScalarMul` directly on P-256, P-384 or the STARK curve can mitigate by calling `curve.AssertIsOnCurve(res)` on the returned point (handling the `(0,0)` point-at-infinity result as appropriate). This does not cover `JointScalarMulBase` or `MultiScalarMul`.

### References

- Fix: https://github.com/Consensys-Incorporated/gnark/commit/4d476392b169eaffaaafe0796ba750e2a5081652
- Release: https://github.com/Consensys/gnark/releases/tag/v0.16.4
- Fake GLV method: [EEMP25], https://eprint.iacr.org/2025/933
