# GHSA-443g-gwgp-49x4: getblocks/getheaders locator CPU amplification via uncapped vector length

| Field | Value |
| --- | --- |
| Repo | ZcashFoundation/zebra |
| GHSA | GHSA-443g-gwgp-49x4 |
| CVE | none assigned |
| Severity | low (CVSS 3.7) |
| CWE | CWE-770 |
| Published | 2026-05-29T07:44:02Z |
| Updated | 2026-05-29T07:44:02Z |
| Affected | zebrad <= 4.4.1; zebra-chain <= 6.0.2 |
| Advisory URL | https://github.com/ZcashFoundation/zebra/security/advisories/GHSA-443g-gwgp-49x4 |

## Description (verbatim)

### Am I affected

You are affected if:

1. You run `zebrad` up to and including `v4.4.1`.
2. Your node accepts inbound P2P connections.

### Summary

The `read_getblocks` and `read_getheaders` codec paths accepted block locator vectors up to approximately 65,535 entries (the generic `TrustedPreallocate` ceiling derived from `MAX_PROTOCOL_MESSAGE_LEN`), rather than the protocol-specification limit of 101 entries (matching zcashd's `MAX_LOCATOR_SZ`). Each entry in the locator vector triggers a per-hash chain lookup (`HashMap::contains_key` + `RocksDB::contains_hash`) in `find_chain_intersection` on a tokio blocking-pool thread.

A single maximally-sized `getblocks` message occupies one blocking-pool thread for approximately 10–65ms. Under sustained load from multiple peers, this can degrade state-read performance for block validation, RPC, and mempool lookups.

### Details

The `read_headers` codec path already implements the correct pattern: it reads the CompactSize count, validates against `MAX_HEADERS_PER_MESSAGE = 160` before deserialization, and rejects oversized messages. The `read_getblocks` and `read_getheaders` paths were missing this pre-deserialization count check and instead relied on the generic `block::Hash::max_allocation()` bound, which allows `(MAX_PROTOCOL_MESSAGE_LEN - 1) / 32 = 65,535` hashes.

A legitimate block locator is logarithmic in chain length (approximately 30 hashes for the current ~3M-block Zcash chain). Zebra's own send-side cap is `MAX_FIND_BLOCK_HASHES_RESULTS = 500`.

The practical impact requires significant attacker bandwidth (approximately 2 MiB per request) and multiple Sybil peers to meaningfully degrade the blocking pool, which limits real-world exploitability.

### Patches

Patched in Zebra 4.4.2. The fix caps `block::Hash::max_allocation()` at `MAX_BLOCK_LOCATOR_LENGTH = 101`, matching zcashd's `MAX_LOCATOR_SZ`. This causes the deserializer to reject oversized locators before any allocation or iteration occurs.

### Workarounds

No specific workaround is needed. Existing backpressure mechanisms (load shedding, sequential per-peer message processing, connection limits) constrain the practical impact.

### Impact

Under sustained load from multiple Sybil peers, oversized locator vectors can occupy blocking-pool threads and degrade state-read performance. The effect is bounded by connection limits and requires significant attacker bandwidth.

### Credit

Vulnerability identified by `@dingledropper`, who submitted the fix in [PR #10570](https://github.com/ZcashFoundation/zebra/pull/10570). Downstream CPU/blocking-pool impact analysis contributed by `@ouicate`.

### References

- [CWE-770: Allocation of Resources Without Limits or Throttling](https://cwe.mitre.org/data/definitions/770.html)
- [CWE-400: Uncontrolled Resource Consumption](https://cwe.mitre.org/data/definitions/400.html)
