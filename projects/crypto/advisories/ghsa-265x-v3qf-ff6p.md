# GHSA-265x-v3qf-ff6p: snark-verifier accepts non-canonical KZG accumulator limb encodings

| Field | Value |
| --- | --- |
| Repo | axiom-crypto/snark-verifier |
| GHSA | GHSA-265x-v3qf-ff6p |
| CVE | CVE-2026-61618 |
| Severity | medium |
| CWE | CWE-20, CWE-1284 |
| Published | 2026-11-18T16:13:34Z |
| Updated | 2026-11-18T16:13:36Z |
| Affected | snark-verifier < 0.2.5 (patched: 0.2.5) |
| Advisory URL | https://github.com/advisories/GHSA-265x-v3qf-ff6p |

## Description (verbatim)

### Summary
KZG accumulator public-instance limbs were decoded without consistently enforcing canonical limb bounds before reconstructing elliptic-curve coordinates.

In the generated EVM verifier, accumulator coordinates were reconstructed from public-instance limbs using shifted additions before point validation. The verifier checked the reconstructed point, but did not independently check that every limb was below the configured limb bound before reconstruction.

### Details
`PlonkProof::read` takes accumulator public-instance scalars selected by `accumulator_indices` and passes them into `AccumulatorEncoding::from_repr`. For the EVM loader, `LimbsEncoding::from_repr` forwards those limbs to `EvmLoader::ec_point_from_limbs`, where each coordinate was reconstructed with `shl` and `add` before `validate_ec_point` was applied. That validation checked the reconstructed affine point, not whether the original limb encoding was canonical.

The native verifier path had a related robustness issue: malformed accumulator limb encodings could reach assertion or unwrap-based decoding and panic instead of returning a verification error.

The affected code is in `snark-verifier/src/loader/evm/loader.rs` and `snark-verifier/src/pcs/kzg/accumulator.rs`, specifically `EvmLoader::ec_point_from_limbs` and `LimbsEncoding::from_repr`.

### Impact
For standard SDK aggregation circuits, accumulator limbs are expected to be constrained by the circuit before reaching the verifier boundary, which limits practical exploitability. The missing verifier-side checks nevertheless allowed non-canonical encodings at the boundary, and the native verifier path could be crashed by malformed accumulator public inputs.

## References

- https://github.com/axiom-crypto/snark-verifier/security/advisories/GHSA-265x-v3qf-ff6p
- https://nvd.nist.gov/vuln/detail/CVE-2026-61618
- https://github.com/axiom-crypto/snark-verifier/commit/d6aaf66d4706f5317cf61d5dbe00c14e7fbdbb70
- https://github.com/axiom-crypto/snark-verifier/releases/tag/v0.2.5
- https://github.com/advisories/GHSA-265x-v3qf-ff6p
