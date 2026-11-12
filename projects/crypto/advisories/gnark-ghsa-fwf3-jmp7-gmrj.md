# GHSA-fwf3-jmp7-gmrj: Unconstrained G2 subgroup membership check inside Miller loop computation

| Field | Value |
| --- | --- |
| Repo | Consensys/gnark (Go ZK-SNARK library) |
| GHSA | GHSA-fwf3-jmp7-gmrj |
| CVE | none assigned |
| Severity | medium |
| CWE | n/a |
| Published | 2026-08-24T18:14:13Z |
| Affected | github.com/consensys/gnark <=v0.15.0 (patched: >v0.15.0) |
| Credits | kite-builds |
| Advisory URL | https://github.com/Consensys-Incorporated/gnark/security/advisories/GHSA-fwf3-jmp7-gmrj |
| Captured | 2026-11-12 (WAT) |

## Description (verbatim)

### Impact

The Miller loop method documentation assures that the G2 input would be checked to be in the subgroup. The membership check test was done, but the result was discarded instead of being constrained to be 1.

### Patches

Issue has been fixed in 93b69f0006b7e26eec3a22780160250825165720.

### Workarounds

The user can manually add subgroup membership for the G2 inputs.

---

Issue originally reported by @kite-builds, below the full reported issue

> ### SUMMARY
> The BN254 (ECPair, 0x08, EIP-197) and BLS12-381 (ECPairBLS, 0x0f, EIP-2537) pairing precompiles do not constrain the attacker-supplied G2 input Q to be on the curve/twist. The on-twist check exists but its result is discarded; only the prime-order subgroup relation is asserted. Subgroup membership does NOT imply on-curve, so a malicious prover can submit an off-twist Q that passes validation - a classic invalid-curve setup against a pairing check.
> 
> ### ROOT CAUSE (read from source)
> - std/algebra/emulated/sw_bls12381/pairing.go:346 - IsOnTwist(Q) only RETURNS a bool (computeTwistEquation -> Ext2.IsZero); it adds no constraint. The constraining variant AssertIsOnTwist (pairing.go:341 -> g2.go:537) exists but is not used here.
> - std/algebra/emulated/sw_bls12381/precomputations.go:35 - computeLines calls pr.IsOnTwist(&Qaff) and DISCARDS the return value. The only G2 geometric constraint it asserts is the subgroup relation psi(Q) == [x0]Q (precomputations.go:56). Same pattern in sw_bn254/precomputations.go.
> - computeLines is the sole Q-validation on the precompile path (MillerLoop pairing.go:157,396; millerLoopAndFinalExpResult pairing.go:836). The wrappers std/evmprecompiles/15-blspairing.go and 08-bnpairing.go comment "Check that Qi are on G2 (done in computeLines ...)" but never call AssertIsOnTwist/AssertIsOnG2. AssertIsOnG2 (g2.go:542) correctly does BOTH on-twist AND subgroup; the precompile path does only subgroup.
> 
> ### WHY THE SUBGROUP CHECK DOES NOT SAVE IT (constructive witness)
> psi (g2.go:170) is a fixed semilinear coordinate map that commutes with the sextic-twist scaling iso phi_s:(x,y)->(s^2 x, s^3 y), s in Fp, and so does the affine group law (chord-tangent formulas are b-independent). Take any genuine G2 point Q=(x,y) on the true twist E_b'. Then Q'=(s^2 x, s^3 y) lies on E_{s^6 b'}, a DIFFERENT curve when s^6 != 1. Yet [x0]Q' = phi_s([x0]Q) and psi(Q') = phi_s(psi(Q)) = phi_s([x0]Q) = [x0]Q'. So Q' satisfies the subgroup relation EXACTLY while being off the true twist - an infinite family of invalid-curve witnesses the precompile accepts.
> 
> ### IMPACT
> EIP-197 and EIP-2537 mandate on-curve checks; accepting off-curve points violates the spec and breaks pairing soundness. Any contract relying on the pairing precompile (BLS signature verification, SNARK verifiers, bridges) can be fed a forged "pairing == 1 (success)" via invalid-curve / small-subgroup cancellation in the multi-pairing.
> 
> ### FIX (one line per curve), in sw_bls12381/precomputations.go and sw_bn254/precomputations.go, inside computeLines:
> - pr.IsOnTwist(&Qaff)
> + pr.AssertIsOnTwist(&Qaff)
> (equivalently, have the precompile wrappers call AssertIsOnG2/AssertIsOnTwist on each Q). This restores the intent already documented in the wrapper comments and matches AssertIsOnG2. Note: G1 membership for the BLS precompile was just added in v0.15.0 PR #1591 (May 2026); the symmetric G2 on-curve gap remains at current HEAD.
