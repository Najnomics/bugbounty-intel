# 🚨 Security Incident in SagaEVM

- **Source URL:** https://medium.com/sagaxyz/sagaevm-security-incident-investigation-update-29a1d2a6b0cd
- **Fetched from:** https://medium.com/feed/sagaxyz
- **Fetched:** 2026-11-16
- **Channel:** @defendor_eng
- **Telegram message:** https://t.me/defendor_eng/1125 (id 1125)
- **Method:** medium-rss-content readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
*January 21, 2026 Status: Ongoing Investigation*

### Overview

On January 21, 2026, Saga identified and responded to a security incident affecting the **SagaEVM chain**.

The incident involved a coordinated sequence of contract deployments, cross-chain activity, and subsequent liquidity withdrawals.

Out of an abundance of caution, the **SagaEVM chain was paused at block height 6593800** while the issue is actively being investigated and mitigated.

This update reflects our current understanding based on ongoing forensic analysis.

### What We Can Confirm Right Now

Saga has identified a security incident affecting the SagaEVM chain. SagaEVM remains paused while our engineering and security teams work through a full remediation process.

Our current focus:

- Stop further impact by keeping SagaEVM paused while mitigation is implemented.
- Validate the full blast radius using archive data and execution traces.
- Harden the relevant components before any restart.
- Communicate only confirmed facts as they are locked in.

We recognize that a pause is disruptive. We made this decision because the safety of our community comes first.

**Once remediation is complete, we will publish a more comprehensive technical post-mortem.**

### Scope and Impact

### Affected

- SagaEVM chainlet
- Colt and Mustang

### Not Affected

- Saga SSC mainnet (remains operational)
- Saga protocol consensus
- Validator security
- Other Saga chainlets

### Impact:

- Nearly \~$7,000,000 in USDC, yUSD, ETH, and tBTC were transferred to Ethereum Mainnet
- Exploiters wallet has been identified as 0x2044697623afa31459642708c83f04ecef8c6ecb

We are working with exchanges and bridges to blacklist this wallet and reclaim the tokens extracted.

There has been **no consensus failure**, validator compromise, or signer key leakage.

The broader Saga network remains structurally sound.

### Response and Mitigation

Upon confirmation of the incident:

- The SagaEVM chainlet was paused
- Engineering teams initiated a full forensic investigation using archive nodes and execution traces
- Cross-chain activity relevant to the incident was reviewed and restricted where appropriate
- Additional safeguards were introduced to prevent similar coordinated attack patterns

SagaEVM will remain paused until mitigation is complete and the team is confident that no further risk remains.

### Next Steps

- Complete root cause validation
- Patch and harden affected cross-chain and deployment components
- Coordinate with ecosystem partners where relevant
- **Publish a comprehensive technical post-mortem**

### Commitment to Transparency

Saga is committed to clear, accurate communication, especially during incidents like this.

Our approach is to communicate **only confirmed information**. During active investigation, that means prioritizing correctness and user safety.

Once the investigation concludes and remediation is complete, we will publish a comprehensive technical post-mortem outlining our findings, the actions taken, and the safeguards introduced.

*For further information, follow us on Twitter, join our Discord and* [*Telegram*](https://xyz.us10.list-manage.com/track/click?u=ca44fab3b7b6185f64afb274a&id=f450024c8d&e=4c17c9cc64), *and subscribe to our Medium.*

[SagaEVM Security Incident: Investigation Update](https://medium.com/sagaxyz/sagaevm-security-incident-investigation-update-29a1d2a6b0cd) was originally published in [Saga AI Labs](https://medium.com/sagaxyz) on Medium, where people are continuing the conversation by highlighting and responding to this story.
