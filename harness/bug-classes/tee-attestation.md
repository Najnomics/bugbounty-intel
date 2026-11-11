# TEE: attestation pipeline and enclave trust

_Harness check spec. Every signal, payload and automation note below is drawn from the cited local files (full verbatim text under `posts/` and `writeups/`). Nothing here is invented; where a source only states a pattern, no concrete payload is asserted._


## Detection signals
- Attestation verification that is informational rather than enforced.
- Missing TLS checks on collateral/PCCS fetches; replayable stale-but-valid collateral.
- Caller-supplied verifier URL (SSRF); an `is_valid`/`event_log_verified` flag that is a UI hint, not a cryptographic fact.

## Method seen in sources
- Phala dstack attestation-pipeline hardening questions (enforced TCB? TLS on collateral? stale-collateral replay? SSRF on verifier URL? is "valid" cryptographic?). Source: [`writeups/bluethroat_labs/phala-dstack-attestation-hardening.md`](../../writeups/bluethroat_labs/phala-dstack-attestation-hardening.md) and techniques.md.
- Academic TEE/side-channel background: [`researchers/jovanbulck.md`](../../researchers/jovanbulck.md) (Foreshadow, LVI, SGX-Step).

## Automation (check spec)
```
check: is attestation enforced or only logged?
check TLS verification on collateral/PCCS fetch; attempt stale collateral replay
check if verifier URL is caller-controlled (SSRF)
confirm "valid" maps to a verified cryptographic quote, not a flag
```

