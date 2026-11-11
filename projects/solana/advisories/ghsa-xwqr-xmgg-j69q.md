# GHSA-xwqr-xmgg-j69q: Integer overflow in solana_rbpf

| Field | Value |
| --- | --- |
| ID | GHSA-xwqr-xmgg-j69q |
| Aliases | CVE-2021-46102 |
| Published | 2022-01-28T22:59:28Z |
| Modified | 2023-11-08T04:07:25.094752Z |
| Affected | solana_rbpf: 0.2.14 0.2.17 |

## Details (verbatim)

From version 0.2.14 to 0.2.16 for Solana rBPF, function "relocate" in the file src/elf.rs has an integer overflow bug because the sym.st_value is read directly from ELF file without checking. If the sym.st_value is rather large, an integer overflow is triggered while calculating the variable "addr" via `addr = (sym.st_value + refd_pa) as u64`

## References

- https://nvd.nist.gov/vuln/detail/CVE-2021-46102
- https://github.com/solana-labs/rbpf/pull/200
- https://github.com/solana-labs/rbpf/pull/236
- https://blocksecteam.medium.com/new-integer-overflow-bug-discovered-in-solana-rbpf-7729717159ee
- https://github.com/solana-labs/rbpf
- https://github.com/solana-labs/rbpf/blob/c14764850f0b83b58aa013248eaf6d65836c1218/src/elf.rs#L609-L630
- https://github.com/solana-labs/rbpf/releases/tag/v0.2.17
