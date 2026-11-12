# GHSA-rjjm-x32p-m3f7: Range checker gadget allows wider inputs up to word alignment

| Field | Value |
| --- | --- |
| Repo | Consensys/gnark (Go ZK-SNARK library) |
| GHSA | GHSA-rjjm-x32p-m3f7 |
| CVE | none assigned |
| Severity | low |
| CWE | n/a |
| Published | 2023-11-10T17:05:28Z |
| Affected | github.com/consensys/gnark <0.9.2 (patched: 0.9.2) |
| Credits | ultrainstinct30, ivokub, gbotrel |
| Advisory URL | https://github.com/Consensys-Incorporated/gnark/security/advisories/GHSA-rjjm-x32p-m3f7 |
| Captured | 2026-11-12 (WAT) |

## Description (verbatim)

### Impact

gnark provides a gadget in the standard library to allow optimized checking of the bitwidth of the inputs. The gadget works by constructing a fixed lookup table containing all valid entries, partitioning the input and checking that all parts are inside the lookup table. The range checker gadget did not take into account that the highest partition may be less than the width limit, allowing the inputs to be up to 16 bits wider than checked.

Range checking gadget is extensively used in field emulation. Users using any dependant gadget (ECDSA verification, proof recursion etc.) is impacted.

We consider the impact of the vulnerability being low as the number of attacker-modifiable bits is significantly smaller compared to the bit-width of scalar field modulus and it won't be possible to construct inputs which would allow to overflow the scalar field.

### Patches

The issue has been patched in the stable branch of gnark. 

Due to low severity of the issue no emergency release will be issued and we follow the existing release plan. Versions v0.9.2 and higher are patched.

### Workarounds

We consider the issue very hard to exploit and do not recommend manual remediation. However, it is possible to perform manual bit decomposition using `std/math/bits` gadget.

### References

Initial issue https://github.com/Consensys/gnark/issues/897

### Acknowledgement

The issue was reported by [@ultrainstinct30](https://github.com/ultrainstinct30).
