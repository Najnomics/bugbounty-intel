# trailofbits — Trail of Bits (security research / audit firm)

Org account, in the watch list for OSS-vulnerability and Web3/crypto research. Not a bounty hunter per se, but a strong source of real-world bug patterns and tooling.

- Platforms / focus: OSS vulnerability research (Patch the Planet), audits, fuzzing, formal methods, Web3.

## Findings / notes

### Patch the Planet — 506 fixes / 100 CVEs across 75 OSS projects — 12 Nov 2026

- Posts: https://x.com/trailofbits/status/2120943246587392210 and https://x.com/trailofbits/status/2121009628855357931 — verbatim: [`posts/trailofbits/2026-11-12-2120943246587392210.md`](../posts/trailofbits/2026-11-12-2120943246587392210.md), [`posts/trailofbits/2026-11-12-2121009628855357931.md`](../posts/trailofbits/2026-11-12-2121009628855357931.md)
- Writeup (dashboard, full CVE list + recurring patterns): [`writeups/trailofbits/patch-the-planet-dashboard-2026-11.md`](../writeups/trailofbits/patch-the-planet-dashboard-2026-11.md)
- **Recurring patterns:** parser/capture DoS (truncated PDU closes whole session), unbounded-state memory exhaustion, vLLM multimodal amplification (request-controlled sizing before size guards), revision-pin drops (supply chain), curl cross-origin credential/cookie/TLS leakage, TLS state-machine bugs, AI-agent trust-boundary bugs (OpenClaw).
- Also released two open-source AI agent patch-generation plugins (distilled from Patch the Planet + Codex sessions).
