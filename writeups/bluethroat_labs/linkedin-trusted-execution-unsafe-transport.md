# linkedin-trusted-execution-unsafe-transport

- **Source URL:** https://www.linkedin.com/posts/bluethroat-labs_56-trusted-execution-over-an-unsafe-transport-activity-7447638926099685376-GKd6
- **Fetched:** 2026-11-11
- **Researcher:** bluethroat_labs
- **Method:** curl + trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---

We uncovered in 6 security vulnerabilities in dStack, one of the most prominent TEE infrastructure providers in Web3, including Criticals and Highs. Here’s an easy way to understand one of the bugs we found in dStack’s attestation pipeline: Imagine your security system checks whether a machine is trusted by downloading Intel’s latest status data over HTTPS. Now imagine it does that with TLS certificate verification turned off. That was the issue. The verifier would still receive data that looked signed and legitimate, but a network attacker could sit in the middle and replay older collateral that was still within its validity window. In other words, the attacker could make yesterday’s trust decision override today’s security reality. Important nuance: This was not full collateral forgery. Intel’s offline signatures still blocked that for most collateral types. The real risk was replaying stale-but-valid data, plus denial of service and compounding issues around QE Identity handling. The big lesson: TLS does not just give you encryption. It also gives you authenticity and freshness. And in attestation, freshness is a security property. Full write-up below.
