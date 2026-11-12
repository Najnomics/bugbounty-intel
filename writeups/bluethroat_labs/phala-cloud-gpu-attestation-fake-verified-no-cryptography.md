# phala-cloud-gpu-attestation-fake-verified-no-cryptography

- **Source URL:** https://bluethroatlabs.com/reveries/phala-cloud-gpu-attestation-fake-verified-no-cryptography
- **Fetched:** 2026-11-12
- **Researcher:** bluethroat_labs
- **Method:** curl + trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---

Finding 4 of 6

# GPU Attestation Displayed as Verified Without Cryptographic Verification

[@saxenism](https://x.com/saxenism))

**Severity:** High
**Affected component:** dstack trust-center verifier (GPU attestation path)
**Finding ID:** #6 from the dstack/Phala assessment

Phala's trust center told users their GPU workloads were cryptographically verified. The code contained zero cryptography. This write-up covers the technical behavior, the public claims it contradicted, and the regulatory context that made the gap consequential.

The issue was identified by Bluethroat Labs and responsibly disclosed to Phala Network in January 2026.


## Executive Summary

- The trust-center verifier fetched GPU attestation data from the Redpill API and displayed it under "TEE Hardware Verified" alongside CPU attestation.
- `parseAttestationBundle()` deserialized a JSON blob. It performed no cryptographic validation whatsoever: no call to NVIDIA's Remote Attestation Service, no verification of the NVIDIA device certificate chain, no signature validation, no RIM check, no OCSP revocation check.
- The UI explicitly claimed: "This verification uses NVIDIA's Remote Attestation Service (NRAS) to prove that your model is running on genuine NVIDIA hardware in a secure environment." That claim was false.
- This persisted for over six months (July 2025 through early February 2026), during which Phala marketed the platform with claims including "every response cryptographically attested" and "no blind trust required."

## Background

Confidential AI on GPU requires two distinct attestation chains. The CPU side (TDX/SGX) proves the TEE enclave is authentic and unmodified. The GPU side proves that the NVIDIA H100/H200 is genuine hardware running in confidential computing mode, that its firmware is unmodified, and that the device identity traces back to NVIDIA's root CA.

NVIDIA provides a Remote Attestation Service (NRAS) and a local GPU attestation SDK for exactly this purpose. A proper GPU attestation flow validates:

- **Device certificate chain** against NVIDIA's root CA, proving the GPU is genuine hardware
- **Attestation evidence signatures**, proving the evidence was produced by that specific GPU
- **Reference Integrity Manifest (RIM)**, proving the GPU firmware matches NVIDIA's known-good measurements
- **OCSP revocation status**, proving the device has not been revoked
- **Nonce freshness**, proving the attestation is current and not replayed

Without these checks, GPU attestation is a JSON document with no cryptographic backing. Anyone who can serve well-formed JSON matching the expected schema can produce "valid" GPU attestation.

## What Phala Claimed

In July 2025, Phala published a blog titled "GPU TEE is Launched on Phala Cloud for Confidential AI." The post made the following claims:

- "Every response cryptographically attested"
- "No blind trust required"
- "No one -- not the cloud, not the operator, not even Phala -- can see your data, code, or model outside the enclave"
- "Real-time Verification" listed as a differentiator against competitors (marked with a checkmark, while competitors received an X)
- "cryptographic proof that your workload is running inside an authentic TEE"
- "independently verify every inference, every time"

Phala's main site also displays SOC 2 Type I and HIPAA compliance badges, and specifically targets healthcare, finance, and legal verticals with language like "Deploy copilots and AI automation for proprietary or regulated data (health, finance, legal, code)" and "Build SaaS for regulated industries -- turn compliance from a blocker into your unique selling point."

These are not casual marketing claims. They are security representations that regulated organizations use when making procurement and compliance decisions.

## Vulnerability Details

### The Asymmetry

CPU and GPU attestation followed completely different verification paths, but were presented identically in the UI.

CPU attestation was fully verified:

```
// packages/verifier/src/verifiers/phalaCloudVerifier.ts
const quoteData = await this.getQuote()
const verificationResult = await verifyTeeQuote(quoteData)  // Full cryptographic verification
```
`verifyTeeQuote()` invoked `dcap-qvl`, which validated the Intel certificate chain against the root CA, verified the quote signature, checked CRLs, and evaluated TCB status. This is real attestation verification.

GPU attestation was fetched and parsed:

```
// packages/verifier/src/verifiers/phalaCloudVerifier.ts, lines 267-312
public async verifyHardware(): Promise<{
  isValid: boolean
  failures: VerificationFailure[]
}> {
  const quoteData = await this.getQuote()
  const verificationResult = await verifyTeeQuote(quoteData)  // CPU IS verified
  this.attestationBundle = undefined
  // Check for GPU support via Redpill API
  try {
    const models = await PhalaCloudVerifier.getRunningModels()
    const matchingModel = models.find(
      (m: any) => m.metadata?.appid === this.appId,
    )
    if (matchingModel) {
      const attestationUrl =
        `https://api.redpill.ai/v1/attestation/report?model=${matchingModel.id}`
      const response = await fetch(attestationUrl, {
        headers: {
          'Content-Type': 'application/json',
          Authorization: `Bearer test`,
        },
      })
      if (response.ok) {
        const rawAppInfo = await response.json()
        // GPU attestation is ONLY parsed, NOT verified
        this.attestationBundle = parseAttestationBundle(
          rawAppInfo as Record<string, unknown>,
          {
            nvidiaPayloadSchema: NvidiaPayloadSchema,
            eventLogSchema: EventLogSchema,
            appInfoSchema: AppInfoSchema,
          },
        )
      }
    }
  } catch (error) {
    console.warn(
      `Failed to fetch GPU attestation for app ${this.appId}:`,
      error,
    )
  }
  // Unverified data passed directly to display
  const dataObjects = this.dataObjectGenerator.generateHardwareDataObjects(
    quoteData,
    verificationResult,
    this.attestationBundle,  // No verification happened on this
  )
  // ...
}
```
`parseAttestationBundle()` is a JSON deserialization function. It validates that the response matches a TypeScript schema. It does not validate any cryptographic property of the data.

### What Was Never Verified

The `NvidiaPayload` type shows exactly what fields existed and were left unchecked:

```
// packages/verifier/src/types/attestation.ts
export interface NvidiaEvidence {
  /** X.509 certificate for the GPU */
  certificate: string      // Never validated against NVIDIA root CA
  /** Cryptographic evidence from the GPU */
  evidence: string         // Never signature-verified
  /** GPU architecture identifier */
  arch: string
}
export interface NvidiaPayload {
  /** Random nonce for replay protection */
  nonce: string            // Never validated for freshness
  /** List of evidence from multiple GPUs */
  evidence_list: NvidiaEvidence[]
  /** Target architecture for the attestation */
  arch: string
}
```
The verification gap was total:

| Check | CPU (TDX/SGX) | GPU (NVIDIA) | 
|---|---|---|
| Data fetched | Yes | Yes | 
| Certificate chain validated | Yes (Intel root CA) | No | 
| Signature verified | Yes (via dcap-qvl) | No | 
| Revocation checked | Yes (CRL) | No | 
| Any cryptographic operation | Yes | No | 

### The Misleading UI

Both CPU and GPU attestation appeared together under "TEE Hardware Verified":

```
// apps/webapp/src/components/visualization/report-view.tsx
const TRUST_SECTIONS: TrustSection[] = [
  {
    id: 'hardware',
    title: 'TEE Hardware Verified',  // Claims verification
    items: [REPORT_ITEMS['app-gpu'], REPORT_ITEMS['app-cpu']],  // Both listed together
  },
  // ...
]
```
The GPU attestation item went further, explicitly claiming a verification mechanism that was never invoked:

```
// apps/webapp/src/data/report-items.ts
'app-gpu': {
  id: 'app-gpu',
  title: 'GPU Attestation',
  vendorTitle: 'Remote Attestation Service',
  intro:
    "This verification uses NVIDIA's Remote Attestation Service (NRAS) to prove " +
    "that your model is running on genuine NVIDIA hardware in a secure environment. " +
    "You can independently verify the attestation evidence using NVIDIA's public API.",
}
```
This is not incomplete verification. This is a UI asserting that a specific verification mechanism (NRAS) is being used when the code never calls it. The trust center displayed "TEE Hardware Verified" for GPU workloads with zero cryptographic basis.

## Representative Attack Scenario

The bar for exploitation was low. An attacker needed only to serve well-formed JSON.

**Scenario 1: Compromised or spoofed API endpoint.** If the Redpill API was compromised, DNS-hijacked, or intercepted, the attacker could return arbitrary GPU attestation data. The trust center would parse it, display "TEE Hardware Verified," and no alarm would fire. There was no cryptographic check that could fail because there were no cryptographic checks.

**Scenario 2: PCI passthrough MITM.** An attacker with physical or hypervisor-level access could perform a PCI passthrough man-in-the-middle attack, presenting a malicious device that impersonates an NVIDIA GPU in confidential computing mode. Without device identity verification against NVIDIA's root CA, the trust center could not distinguish a genuine H100 from an impostor.

**In both cases:**

```
Attacker serves well-formed JSON matching NvidiaPayload schema
    |
    v
parseAttestationBundle() deserializes JSON ✓
    |
    v
Certificate chain validation — not performed ✗
Evidence signature verification — not performed ✗
NRAS verification — not performed ✗
RIM validation — not performed ✗
OCSP revocation check — not performed ✗
    |
    v
Trust center displays "TEE Hardware Verified"
UI claims NRAS verification occurred
    |
    v
User sees verified badge. No verification happened.
```
## Why This Matters Beyond the Code Bug

This was not a subtle edge case in a verification library. This was a public-facing trust center displaying "verified" to end users for a verification that did not exist, backed by marketing claims of cryptographic attestation.

**The compliance dimension.** Phala's website displays SOC 2 Type I and HIPAA compliance badges. It markets to healthcare, finance, and legal verticals. Organizations in these sectors make procurement and deployment decisions based on attestation guarantees. A hospital deploying a medical AI model on Phala Cloud, seeing "TEE Hardware Verified" and reading "every response cryptographically attested," would reasonably conclude that the GPU running their model has been cryptographically verified. It had not been.

**The duration.** The blog announcing GPU TEE support was published in July 2025. The fix was deployed in early February 2026, after our report. That is over six months during which the trust center displayed cryptographic verification claims with no cryptographic verification backing them.

**The residual gap.** After the fix, the team still does not provide cryptographic proof of binding between the CPU TEE and the GPU. The current verification proves the model ran on "some TEE GPU" -- but not that it was the GPU attached to the specific CPU enclave that was attested. The team was informed of this gap. It was not mentioned in their public security update or added to any documentation.

## Severity Classification

We reported this as **High** severity. The severity reflects three factors:

1. **The gap was total.** This was not a partial verification or a missing edge-case check. Zero cryptographic operations were performed on GPU attestation. The "verification" was JSON deserialization.
2. **The UI actively misrepresented the state.** The trust center did not just omit a warning. It explicitly claimed NRAS verification was being used. That claim was false in the code.
3. **The context was security-critical.** Phala markets attestation as the core trust primitive for confidential AI, targets regulated industries, and holds compliance certifications that depend on the integrity of those trust claims.

Phala accepted this finding during the assessment but later reclassified it as **Low** in their public blog. We maintain our original High classification and let readers examine the evidence above to form their own judgment.

## Fix

The fix should implement actual cryptographic verification of GPU attestation before displaying it as verified. NVIDIA provides the NRAS API for this purpose:

1. Submit the attestation evidence to NVIDIA's Remote Attestation Service for verification.
2. Validate the device certificate chain against NVIDIA's root CA.
3. Verify the Reference Integrity Manifest (RIM) to confirm firmware integrity.
4. Check OCSP revocation status for the device certificate.
5. Validate nonce freshness to prevent replay attacks.

Until cryptographic verification is implemented, GPU attestation should not be displayed under "TEE Hardware Verified" and the UI should not claim NRAS verification is being performed.

Additionally, the CPU-GPU binding gap should be documented: users should understand that current verification proves the GPU is genuine but does not cryptographically bind it to the specific CPU enclave.

## Timeline

| Date | Event | 
|---|---|
| July 2025 | Phala publishes "GPU TEE is Launched on Phala Cloud" blog with cryptographic attestation claims | 
| January 6, 2026 | Finding reported to Phala Network | 
| January 2026 | Acknowledged and triaged | 
| Early February 2026 | Fix deployed | 
| February 2026 | Phala publishes security update blog; reclassifies this finding as Low | 

## Key Takeaway

Displaying "verified" in a trust UI is a security assertion. If the underlying code performs no cryptographic verification, that assertion is false regardless of how well-formed the data is. JSON deserialization is not attestation. Schema validation is not cryptography. And claiming NRAS verification in a user-facing string while never calling NRAS is not a gap in defense-in-depth. It is a false security claim in a component whose entire purpose is to tell users whether they can trust the hardware running their workload.

## References

- Phala GPU TEE blog (July 2025): `https://phala.com/posts/gpu-tee-is-launched-on-phala-cloud-for-confidential-ai`
- NVIDIA Remote Attestation Service: `https://docs.nvidia.com/attestation/`

*This vulnerability was discovered by [Rahul Saxena](https://x.com/saxenism) of [Bluethroat Labs](https://www.bluethroatlabs.com) during a security assessment of the dstack ecosystem. Responsible disclosure was coordinated with Phala Network.*

*For a public timeline of the disclosure process, see: [x.com/saxenism/status/2021943382155899351](https://x.com/saxenism/status/2021943382155899351?s=20).*
