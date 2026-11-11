# GHSA-9qmm-4mfr-r3wj: Incorrect Calculation in solana_rbpf

| Field | Value |
| --- | --- |
| ID | GHSA-9qmm-4mfr-r3wj |
| Aliases | CVE-2022-23066 |
| Published | 2022-05-10T00:00:21Z |
| Modified | 2023-11-08T04:08:16.094652Z |
| Affected | solana_rbpf: 0.2.26 0.2.28 |

## Details (verbatim)

In Solana rBPF versions 0.2.26 and 0.2.27 are affected by Incorrect Calculation which is caused by improper implementation of sdiv instruction. This can lead to the wrong execution path, resulting in huge loss in specific cases. For example, the result of a sdiv instruction may decide whether to transfer tokens or not. The vulnerability affects both integrity and may cause serious availability problems.

## References

- https://nvd.nist.gov/vuln/detail/CVE-2022-23066
- https://github.com/solana-labs/rbpf/commit/e61e045f8c244de978401d186dcfd50838817297
- https://blocksecteam.medium.com/how-a-critical-bug-in-solana-network-was-detected-and-timely-patched-a701870e1324
- https://github.com/solana-labs/rbpf
- https://www.whitesourcesoftware.com/vulnerability-database/CVE-2022-23066
