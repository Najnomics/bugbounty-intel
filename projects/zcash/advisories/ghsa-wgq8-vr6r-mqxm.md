# GHSA-wgq8-vr6r-mqxm: frost-core: refresh shares with smaller min_signers will reduce security of group

| Field | Value |
| --- | --- |
| Repo | ZcashFoundation/frost |
| GHSA | GHSA-wgq8-vr6r-mqxm |
| CVE | CVE-2025-58359 |
| Severity | medium |
| CWE | n/a |
| Published | 2025-09-03T13:56:25Z |
| Updated | 2025-09-03T13:56:25Z |
| Affected | frost-core >= 2.0.0, < 2.2.0 (patched: 2.2.0) |
| Advisory URL | https://github.com/ZcashFoundation/frost/security/advisories/GHSA-wgq8-vr6r-mqxm |

## Description (verbatim)

### Impact

It was not clear that it is not  possible to change `min_signers` (i.e. the threshold) with the refresh share functionality (`frost_core::keys::refresh` module). Using a smaller value would not decrease the threshold, and attempts to sign using a smaller threshold would fail. Additionally, after refreshing the shares with a smaller threshold, it would still be possible to sign with the original threshold; however, this could cause a security loss to the participant's shares. We have not determined the exact security implications of doing so and judged simpler to just validate `min_signers`. 

 If for some reason you have done a refresh share procedure with a smaller `min_signers` we strongly recommend migrating to a new key. 

### Patches

Updating to 2.2.0 will ensure that the `min_signers` parameter will be validated. However it won't restore the security of groups refreshed with a smaller `min_signers` parameters.

### Workarounds

You don't need to update if you don't use the refresh share functionality, or if you didn't try to change the `min_signers` parameter using the refresh share functionality.

### References

Thank you [BlockSec](https://blocksec.com/) for reporting the finding
