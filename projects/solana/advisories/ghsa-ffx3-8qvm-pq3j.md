# GHSA-ffx3-8qvm-pq3j: Integer overflow in solana_rbpf

| Field | Value |
| --- | --- |
| ID | GHSA-ffx3-8qvm-pq3j |
| Aliases | CVE-2022-31264 |
| Published | 2022-05-22T00:00:32Z |
| Modified | 2023-11-08T04:09:30.237687Z |
| Affected | solana_rbpf: 0 0.2.29 |

## Details (verbatim)

Solana solana_rbpf before 0.2.29 has an addition integer overflow via invalid ELF program headers. elf.rs has a panic via a malformed eBPF program.

## References

- https://nvd.nist.gov/vuln/detail/CVE-2022-31264
- https://github.com/Ainevsia/CVE-Request/tree/main/Solana/1
- https://github.com/solana-labs/rbpf
- https://github.com/solana-labs/rbpf/releases/tag/v0.2.29
