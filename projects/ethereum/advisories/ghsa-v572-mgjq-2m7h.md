# GHSA-v572-mgjq-2m7h: `/eth/v1/builder/blinded_blocks` endpoint accepts Fulu blob data without verifying it

| Field | Value |
| --- | --- |
| Repo | sigp/lighthouse |
| GHSA | GHSA-v572-mgjq-2m7h |
| CVE | none assigned |
| Severity | low |
| CWE | n/a |
| Published | 2026-10-26T03:14:13Z |
| Updated | 2026-10-26T03:14:13Z |
| Affected |  <8.3.0 (patched: >=8.3.0) |
| Advisory URL | https://github.com/sigp/lighthouse/security/advisories/GHSA-v572-mgjq-2m7h |

## Description (verbatim)

### Summary
When Lighthouse submits a blinded block to a relay via the endpoint `/eth/v1/builder/blinded_blocks`, it accepts Fulu blob data from the relay and marks it as KZG-verified without actually verifying it. A malicious relay could supply a beacon node with invalid blob data and cause the node to import a block that the honest network rejects. 

### Impact
The attack requires a malicious relay, or an attacker that has successfully gained control of a relay. As relays are a trusted component in the builder flow, this exploit is not likely in practice unless the relay gets compromised. 

### Patches
The `/eth/v1/builder/blinded_blocks` endpoint is deprecated in the [builder-specs](https://ethereum.github.io/builder-specs/?urls.primaryName=dev#/Builder/submitBlindedBlock). Aligned with the upstream repository, we removed the endpoint in Lighthouse. Therefore this exploit is not possible in Lighthouse v8.3.0 and onwards. You may refer to this PR for the details: https://github.com/sigp/lighthouse/pull/10213.

### Credits
This issue was reported by @eclipse07077 to the Ethereum Foundation bug bounty program.
