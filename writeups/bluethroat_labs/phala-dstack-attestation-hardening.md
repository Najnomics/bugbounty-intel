# phala-dstack-attestation-hardening

- **Source URL:** https://phala.com/posts/dstack-security-update-attestation-pipeline-hardening
- **Fetched:** 2026-11-11
- **Researcher:** bluethroat_labs
- **Method:** curl + trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---

As part of dstack’s ongoing security efforts, independent security researcher Rahul Saxena (Bluethroat Labs) identified a series of issues in dstack’s attestation verification pipeline in January 2026. The dstack engineering team worked with the researcher to validate findings, implement fixes, and strengthen the attestation stack. All accepted remediations have been deployed, and we found no evidence of in-the-wild exploitation.

This update reflects a Secure-by-Default posture: previously, some verification policy decisions were left to application-layer configuration; now, defaults are stricter and verifier outputs are clearer to prevent ambiguous ‘green light’ semantics.

## TL;DR

Dstack is moving from a flexible infrastructure model to a "Secure-by-Default" architecture. These updates consolidate verification logic—previously left to user-defined policies—into mandatory, infrastructure-level checks to ensure a higher baseline of security for all deployments.

- All accepted findings have been remediated and deployed.
- No action required for Phala Cloud user. For Dstack **users:** Upgrade **dstack images to v0.5.6**. **dcap-qvl** users should upgrade **dcap-qvl** to the latest version. **DstackApp.sol** users who want to enforce **TCB status = UpToDate** should upgrade to the changes in this PR: [https://github.com/Dstack-TEE/dstack/pull/498](https://github.com/Dstack-TEE/dstack/pull/498).
- Key improvements: QE identity verification, stricter TCB enforcement defaults, verified GPU attestation in Trust Center, removal of client-controlled PCCS URL, TLS verification made explicit opt-in.

## Timeline

1. Jan 2026: Issues reported and triaged with the researcher.
2. Jan–Feb 2026: Fixes implemented, reviewed, and deployed.
3. Feb 2026: Public disclosure (this post).

## Findings & Remediations

### 1) QE Identity Verification (Critical)

**Issue:** The dcap-qvl library lacked mandatory Quoting Enclave (QE) identity validation, which could allow a verifier to accept quotes from an unauthorized QE.

**Remediation:** QE Identity verification is now integrated into the core library as a mandatory check. This shifts the responsibility for QE validation from the application developer to the dstack infrastructure. ([GHSA-796p-j2gh-9m2q](https://github.com/Phala-Network/dcap-qvl/security/advisories/GHSA-796p-j2gh-9m2q)).

### 2) TCB Status Enforcement (High)

**Issue:** The verifier provided TCB status as an informational field but did not enforce rejection policies for revoked or outdated TCB levels, potentially leading to permissive misconfigurations.

**Remediation:** The verifier now adopts an opinionated security posture. TCB status checks are enforced by default, and the `is_valid` boolean has been deprecated to ensure developers explicitly handle security posture assessments.

### 3) GPU Attestation Verification (Low)

**Issue:** GPU attestation data was displayed without cryptographic verification of NVIDIA device certificate chain; CPU↔GPU binding not enforced at platform level.

**Remediation:** Trust Center updated with nonce-based challenge, NRAS quote verification, and JWT validation. Boot-time GPU CC-mode verification is planned for a future dstackOS release.

### 4) SSRF via Client-Controlled PCCS URL (Low)

**Issue:** pccs\_url parameter allowed callers to direct server-side requests to arbitrary endpoints.

**Remediation:** Parameter removed from public API.

### 5) Event Log Verification Semantics (Low)

**Issue:** event\_log\_verified semantics could be misunderstood (digest replay vs semantic verification).

**Remediation:** Documentation clarified. IMR 0–2 event logs removed in upcoming release to eliminate ambiguity.

### 6) TLS Verification for PCCS (Low)

**Issue:** The default configuration bypassed TLS certificate verification for PCCS connections, intended for local development but unsuitable for production.

**Remediation:** The default has been changed to "Verified." TLS certificate verification is now a mandatory requirement unless explicitly opted-out for local testing environments.

### 7) RA-TLS Certificate Freshness (Design Tradeoff)

Assessment: dstack RA‑TLS follows the same architectural model as Intel Gramine’s RA‑TLS. Attestation binds the certificate private key to TEE measurements rather than individual sessions. The proposed scenario requires key extraction from inside a production CVM; in that case the correct remediation is measurement revocation, not session-level freshness.

## Impact

- All accepted findings remediated and deployed.
- No evidence of in-the-wild exploitation.
- **No action required by dstack users or downstream integrators. dcap-qvl users should update to the latest version.**

## Security Hardening Roadmap

- GPU TEE integration: boot-time Confidential Computing mode verification in dstack-os.
- Verifier API improvements: clearer separation between cryptographic validity and security posture assessment.
- Formal bug bounty program: evaluating a structured program.

## Acknowledgment

We thank Rahul Saxena and GuyPhy (Bluethroat Labs) for identifying these issues and for engaging throughout the remediation process. Independent security research is essential to the integrity of TEE infrastructure, and we welcome continued scrutiny of the dstack codebase.
