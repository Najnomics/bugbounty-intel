# GHSA-2x4w-pxqw-58v9: Unbounded Orchard proofs can be used to impose large bandwidth and storage costs without paying adequate ZIP 317 fees.

| Field | Value |
| --- | --- |
| Repo | zcash/zcash |
| GHSA | GHSA-2x4w-pxqw-58v9 |
| CVE | none assigned |
| Severity | low |
| CWE | n/a |
| Published | 2026-07-13T17:04:40Z |
| Updated | 2026-07-13T17:04:40Z |
| Affected | zcashd <=6.12.3 (patched: 6.20.0) |
| Advisory URL | https://github.com/zcash/zcash/security/advisories/GHSA-2x4w-pxqw-58v9 |

## Description (verbatim)

### Impact
The problem identified in https://github.com/zcash/zcash/issues/7162 does not present any consensus violation or divergence risk, but it does allow the circumvention of ZIP 317 fees by way of creating large, padded Orchard proofs that might include arbitrary data unbounded in size. This can be used to permanently store unwanted data on-chain at minimal cost.

### Patches
Not yet patched.

The agreed-upon solution to this problem is two-phased: first, block template construction for both zcashd and zebrad should be adjusted to reject transactions containing Orchard actions with proof data at sizes greater than the canonical maximum. Then, this rule should be enforced by a consensus soft-fork at an agreed upon block height. This does not require a full network upgrade, but ideally such a soft fork would be activated by patched nodes after the existing zcashd end-of-service halt; otherwise, it could lead to consensus divergence.

### References
https://github.com/zcash/zcash/issues/7162

