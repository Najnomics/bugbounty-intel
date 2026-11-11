# GHSA-r33q-22hv-j29q: LES Server DoS via GetProofsV2

| Field | Value |
| --- | --- |
| Repo | ethereum/go-ethereum |
| GHSA | GHSA-r33q-22hv-j29q |
| CVE | CVE-2020-26264 |
| Severity | medium |
| CWE | n/a |
| Published | 2020-12-11T08:07:23Z |
| Updated | 2020-12-11T08:07:23Z |
| Affected | github.com/ethereum/go-ethereum < 1.9.25 (patched: >= 1.9.25) |
| Advisory URL | https://github.com/ethereum/go-ethereum/security/advisories/GHSA-r33q-22hv-j29q |

## Description (verbatim)

### Impact

A DoS vulnerability can make a LES server crash via malicious `GetProofsV2` request from a connected LES client.

### Patches

The vulnerability was patched in https://github.com/ethereum/go-ethereum/pull/21896. 

### Workarounds

This vulnerability only concerns users explicitly enabling `les` server; disabling `les` prevents the exploit. 
It can also be patched by manually applying the patch in https://github.com/ethereum/go-ethereum/pull/21896. 


### For more information
If you have any questions or comments about this advisory:
* Open an issue in [go-ethereum](https://github.com/ethereum/go-ethereum)
* Email us at [security@ethereum.org](mailto:security@ethereum.org)
