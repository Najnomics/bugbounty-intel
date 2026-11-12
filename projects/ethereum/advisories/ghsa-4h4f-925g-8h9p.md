# GHSA-4h4f-925g-8h9p: EIP-7702 and sender signature recovery skips the secp256k1 curve-order bound, so native and BouncyCastle backends recover different authorities (consensus split)

| Field | Value |
| --- | --- |
| Repo | hyperledger/besu |
| GHSA | GHSA-4h4f-925g-8h9p |
| CVE | none assigned |
| Severity | high |
| CWE | CWE-436, CWE-1288 |
| Published | 2026-10-14T00:13:39Z |
| Updated | 2026-10-14T00:13:39Z |
| Affected | org.hyperledger.besu:besu <= 26.7.1 (patched: 26.8.0) |
| Credits | n/a |
| Advisory URL | https://github.com/besu-eth/besu/security/advisories/GHSA-4h4f-925g-8h9p |
| Captured | 2026-11-12 (WAT), daily update |

## Description (verbatim)

## Impact

EIP-7702 code-delegation signature recovery skips the secp256k1 curve-order bound. `CodeDelegationSignature.create()` bounds `r`/`s` only by `2^256`, and recovery never enforces `1 <= r,s < n`. For a signature `r` in the band `n < r < p` (curve order < r < field prime), Besu's two signature backends disagree about the tuple:

- native libsecp256k1 recovers **no** authority;
- BouncyCastle recovers a **usable** authority.

Recovered authority feeds consensus-critical state mutation in `CodeDelegationProcessor`, so a network that mixes nodes running with `--Xsecp256k1-native-enabled=true` and `false` computes a **different world state** from the same transaction — a chain split.

A wider instance of the same defect affects **ordinary transaction sender recovery** too: for any `r` that is a valid scalar but not the x-coordinate of a curve point (which includes many values inside `[1, n)`), BouncyCastle throws `IllegalArgumentException` where native returns an empty result, again diverging by backend.

## Patches

Fixed in Besu **26.8.0**: `r` and `s` are bounded to `[1, n)` at recovery time, and an unrecoverable point returns empty on both backends, so the two backends agree.

## Workarounds

No reliable workaround. Ensuring every node on a network uses the same `--Xsecp256k1-native-enabled` setting reduces the divergence surface but does not eliminate the underlying inconsistency. Upgrade to Besu 26.8.0 or later.

## References

Reported by an external security researcher through the Besu bug bounty program. The weakness has been present since EIP-7702 support was introduced.

