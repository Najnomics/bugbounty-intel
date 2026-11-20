# GHSA-x26x-7f4v-cqx7 — snark-verifier: Halo 2 aggregation circuit mishandles point-at-infinity proof elements

Source: GitHub Advisory Database (OSV). Published: 2026-11-20T00:01:59Z  Modified: 2026-11-20T00:01:59Z
Severity: MODERATE  CVSS_V4: CVSS:4.0/AV:N/AC:L/AT:N/PR:N/UI:N/VC:N/VI:L/VA:N/SC:N/SI:N/SA:N  
Aliases: CVE-2026-62337
Fetched: 2026-11-20 (Africa/Lagos)

## Affected
- crates.io `snark-verifier` — ranges: [{"type": "ECOSYSTEM", "events": [{"introduced": "0"}, {"fixed": "0.2.6"}]}]

## Details

### Summary
The Halo 2 aggregation circuit could mishandle proof elements encoded as the point at infinity.

When an assigned proof point appeared in an MSM term with constant scalar one, the Halo 2 loader used a scalar-one shortcut that passed the assigned point directly into the EC sum helper. The EC sum implementation used by that path assumed its inputs were non-identity points, while assigned proof points could represent the encoded identity `(0, 0)`.

### Details
`EcPointLoader::multi_scalar_multiplication` partitions MSM terms by scalar and base type. For `(Value::Constant(ONE), Value::Assigned(_))`, the loader placed the assigned base into the non-scaled variable-base list and later passed those points to `sum_with_const`.

The default Halo 2 shim delegates `sum_with_const` to halo2-lib `EccChip::sum`. In affected versions, that sum helper used incomplete affine addition and assumed that every input point was non-identity. A prover-controlled proof point encoded as `(0, 0)` could therefore enter the final aggregation sum through the scalar-one shortcut and affect the MSM or accumulator computation.

The issue was fixed in halo2-lib by updating `EccChip::sum` to treat encoded identity inputs as no-ops and to return `(0, 0)` when the total sum is the identity. This removes the non-identity input precondition from callers such as the Halo 2 aggregation loader.

### Impact
Recursive aggregation circuits using the Halo 2 loader could compute an MSM or accumulator with an identity proof element in a path whose implementation assumed non-identity inputs. This breaks the expected handling of point-at-infinity proof elements in aggregation.

Practical exploitability depends on the surrounding aggregation and final-decider checks, so this is rated medium severity.

## References
- https://github.com/axiom-crypto/snark-verifier/security/advisories/GHSA-x26x-7f4v-cqx7
- https://nvd.nist.gov/vuln/detail/CVE-2026-62337
- https://github.com/axiom-crypto/halo2-lib/commit/f53be0939e2accf0dd7672b1a4abe80af73dadf3
- https://github.com/axiom-crypto/snark-verifier/commit/364e82654c746b063aff528d8cb660890908278a
- https://github.com/axiom-crypto/snark-verifier/commit/bbfcc721d714bea0d44a27c8fc6c4736e73ca853
- https://crates.io/crates/snark-verifier/0.2.6
- https://github.com/axiom-crypto/snark-verifier
- https://github.com/axiom-crypto/snark-verifier/releases/tag/v0.2.5
