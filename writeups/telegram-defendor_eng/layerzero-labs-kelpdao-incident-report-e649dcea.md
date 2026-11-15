# 🔍 LayerZero Publishes Full KelpDAO Incident Report

- **Source URL:** https://layerzero.network/blog/layerzero-labs-kelpdao-incident-report
- **Fetched:** 2026-11-15
- **Channel:** @defendor_eng
- **Telegram message:** https://t.me/defendor_eng/1630 (id 1630)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
**Executive Summary**

On April 18, 2026, the KelpDAO rsETH bridge, built on the LayerZero crosschain messaging protocol, was attacked, resulting in the loss of 116,500 rsETH (approximately $292 million). Mandiant, CrowdStrike, and independent security researchers all attribute the attack to DPRK threat actor TraderTraitor also known as UNC4899.

The breach began on March 6, 2026, when an attacker socially engineered a LayerZero Labs developer to harvest session keys, pivot into LayerZero's RPC cloud environment, and poison internal RPC nodes — RPC (Remote Procedure Call) nodes are servers that respond to queries about blockchain state. The attacker patched the running RPC memory with a program that returned correct responses to the LayerZero monitoring tools and tampered RPC responses to the LayerZero Labs DVN (Decentralized Verifier Networks). To further facilitate the attack, the attacker executed a Denial of Service (DoS) attack against an external RPC provider, forcing the LayerZero Labs DVN signing service to rely exclusively on two compromised internal nodes and produce a valid attestation for the forged crosschain message.

The impact was made possible by the affected OApp’s single-verifier configuration. Because no second independent DVN was required to attest, the destination contract accepted the single valid attestation and unlocked rsETH. No other OApps, channels or transactions were compromised.

Following the breach, LayerZero Labs responded as follows:

First, a shift in operating stance. LayerZero Labs has historically been un-opinionated toward OApp builders using its infrastructure: whatever configuration the application's delegate chose, the LayerZero Labs DVN would sign for. That stance has changed. The LayerZero Labs DVN now enforces a baseline security configuration on every channel it participates in, and will refuse to sign as the sole required attestor on any channel. The on-chain protocol is unchanged and continues to enforce whatever each application configures; what changed is which configurations LayerZero Labs, as one worker among many, will participate in.

Second, a full rebuild of the operational infrastructure where the compromise lived. The affected cloud environment was replaced rather than patched, redeployed on hardened baselines with no legacy credentials, service accounts, or configurations carried over. Privileged access requires just-in-time elevation with short-lived credentials, multi-person review for IAM changes, and both device and session validation on every administrative request.

Third, LayerZero Labs has worked closely with partners across the ecosystem to review and harden security configurations, work that continues as a standing focus rather than ending at incident response. We will continue to share updates on these efforts and the broader security posture of LayerZero infrastructure as the work progresses.

LayerZero Labs has been working with law enforcement and retained CrowdStrike and Mandiant, two leading cybersecurity firms, to investigate the incident, provide attribution, elevate LayerZero Lab's security posture, and contribute to this report. LayerZero Labs also retained zeroShadow, which provided corroborating attribution and assisted with token tracking and seizure efforts. LayerZero Labs is sharing these findings in a comprehensive manner so that participants across the ecosystem can understand the realities of these attack vectors and protect against increasingly prevalent state-sponsored attacks.
