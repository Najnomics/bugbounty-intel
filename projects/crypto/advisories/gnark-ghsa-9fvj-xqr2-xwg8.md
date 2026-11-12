# GHSA-9fvj-xqr2-xwg8: Denial of service when computing scalar multiplication using fake-GLV algorithm

| Field | Value |
| --- | --- |
| Repo | Consensys/gnark (Go ZK-SNARK library) |
| GHSA | GHSA-9fvj-xqr2-xwg8 |
| CVE | CVE-2025-58157 |
| Severity | high |
| CWE | n/a |
| Published | 2025-08-29T17:30:54Z |
| Affected | github.com/consensys/gnark =v0.12.0 (patched: >=v0.13.0) |
| Credits | feltroidprime |
| Advisory URL | https://github.com/Consensys-Incorporated/gnark/security/advisories/GHSA-9fvj-xqr2-xwg8 |
| Captured | 2026-11-12 (WAT) |

## Description (verbatim)

### Impact

For optimizing the scalar multiplication algorithm in circuit for some curves, gnark uses fake-GLV algorithm in case the curve doesn't support true-GLV. For this to work, we need to compute the scalar decomposition using the Half GCD method in gnark-crypto. However, for some of the inputs the algorithm didn't converge quickly enough.

In case the prover accepts untrusted witness, it could lead to denial of service as the prover gets stuck in a very slowly converging loop.

Thanks to @feltroidprime for reporting the issue and proposing a fix.

### Patches

The issue has been patched in gnark-crypto commit https://github.com/Consensys/gnark-crypto/commit/56600883e0e9f9b159e9c7000b94e76185ec3d0d. The dependency update is implemented in gnark commit https://github.com/Consensys/gnark/commit/68be6cede36e387ab760725beabd3c96cc94e6dc.

### Workarounds

This update doesn't require recompiling the circuits as the issue is in the hint function. The users can update the gnark-crypto dependency to the fixed version.

### References

* See bug report https://github.com/Consensys/gnark/issues/1483
* Fake GLV description https://ethresear.ch/t/fake-glv-you-dont-need-an-efficient-endomorphism-to-implement-glv-like-scalar-multiplication-in-snark-circuits/20394

