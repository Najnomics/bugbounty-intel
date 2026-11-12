# Tee Attestation

_Harness check spec. Every signal, payload and automation note below is drawn from the cited local files (full verbatim text under `posts/`, `writeups/`, `projects/`). Nothing here is invented; where a source only states a pattern, no concrete payload is asserted._


_Findings in corpus for this class: **6** (see `harness/findings.jsonl`)._

## Method / findings in sources

- **linkedin-trusted-execution-unsafe-transport** — We uncovered in 6 security vulnerabilities in dStack, one of the most prominent TEE infrastructure providers in Web3, including Criticals and Highs. Here’s an easy way to understand one of the bugs we found in dStack’s attestation pipeline: Imagine your security system checks whether a machine is trusted by downloading Intel’s latest status data ov Source: [`writeups/bluethroat_labs/linkedin-trusted-execution-unsafe-transport.md`](../../writeups/bluethroat_labs/linkedin-trusted-execution-unsafe-transport.md).
- **bluethroat-docs-home** — Executive Summary This document is a practical security guide for teams building Web3 protocols with Trusted Execution Environments (TEEs). Throughout the document, we use the terms TEEs and enclaves interchangeably, even though, strictly speaking, cloud "enclaves" (like AWS Nitro) are not full TEEs in the academic sense. This distinction matters,  Source: [`writeups/saxenism/bluethroat-docs-home.md`](../../writeups/saxenism/bluethroat-docs-home.md).
- **dumb-ways-to-get-rekt-with-tees** — Dumb ways to get rekt w/ TEEs Introduction Trusted Execution Environments (TEEs) are often treated as if they provide "hardware-level security" by default, and while physical security of TEEs is a different beast, the moment you move to cloud-managed TEEs (AWS Nitro, Azure Confidential VMs, Google CC, etc.), the threat model changes drastically. Ph Source: [`writeups/saxenism/dumb-ways-to-get-rekt-with-tees.md`](../../writeups/saxenism/dumb-ways-to-get-rekt-with-tees.md).
- **tee-security-handbook** — Version: 1.1 Executive Summary This document is a practical security guide for teams building Web3 protocols with Trusted Execution Environments (TEEs). Throughout the document, we use the terms TEEs and enclaves interchangeably, even though, strictly speaking, cloud "enclaves" (like AWS Nitro) are not full TEEs in the academic sense. This distinct Source: [`writeups/saxenism/tee-security-handbook.md`](../../writeups/saxenism/tee-security-handbook.md).
- **turnkey-whitepaper-foundations** — Verifiable Foundations Abstract Here we dive straight into the depth of Turnkey's foundations and how they allow for Turnkey applications to be independently verifiable. We briefly explain what Trusted Execution Environments (“TEEs”) are and how we use them. On top of strong isolation and confidentiality guarantees, TEEs can prove the software they Source: [`writeups/saxenism/turnkey-whitepaper-foundations.md`](../../writeups/saxenism/turnkey-whitepaper-foundations.md).
- **phala-dstack-attestation-hardening** — As part of dstack’s ongoing security efforts, independent security researcher Rahul Saxena (Bluethroat Labs) identified a series of issues in dstack’s attestation verification pipeline in January 2026. The dstack engineering team worked with the researcher to validate findings, implement fixes, and strengthen the attestation stack. All accepted rem Source: [`writeups/bluethroat_labs/phala-dstack-attestation-hardening.md`](../../writeups/bluethroat_labs/phala-dstack-attestation-hardening.md).

## Prior harness notes (retained)

_Retained from earlier curated harness file; still cites local sources._

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

## Added 2026-11-12 — Bluethroat four checks + Phala GPU fake-verified

1. Physical access → treat TEE compromised (TEE.fail).
2. Attestation ≠ safe code (bugs inside enclave still leak; NEAR AI SGLang RCE).
3. Verifier must authenticate report, validate collateral, check measurements, enforce platform status, bind to endpoint.
4. Auditable source → reproducible build → attested measurement.
5. Diff CPU vs GPU (or other) verification paths; `parseAttestationBundle()`-only paths that still show "TEE Hardware Verified" are false claims.
6. Inside enclaves, bind signed message type to the privileged op (saxenism: "execute" ≠ "migrate").
Sources: posts/bluethroat_labs/2026-11-11-2120528783673299290.md, writeups/bluethroat_labs/phala-cloud-gpu-attestation-fake-verified-no-cryptography.md, posts/saxenism/2026-11-11-2120538169259209027.md
