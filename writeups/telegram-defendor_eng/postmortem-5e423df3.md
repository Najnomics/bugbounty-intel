# 🔓 Looking Back: Loopscale's $5.9M Exploit

- **Source URL:** https://blog.loopscale.com/posts/postmortem
- **Fetched:** 2026-11-15
- **Channel:** @defendor_eng
- **Telegram message:** https://t.me/defendor_eng/1755 (id 1755)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
## 

On April 26, 2025, Loopscale was targeted in an attack that exploited the protocol’s pricing logic for RateX-issued tokens. By spoofing the RateX PT market programs, the attacker was able to take out a series of undercollateralized loans, resulting in the unauthorized outflow of 5,726,724.97 USDC and 1,211.4 SOL from the USDC and SOL Genesis Vaults. All funds were subsequently recovered following negotiations.
We take full responsibility for this incident and deeply regret the impact it had on our users. The exploited code path was deployed as part of a new integration with RateX and had not yet undergone a formal third-party audit. This was a clear failure in our review and deployment process. Going forward, no program code will be deployed without external review. Additional security measures are detailed in [Security Improvements](https://blog.loopscale.com#Security-Improvements)below. We want to extend our sincerest gratitude for the critical support of partners across the ecosystem. In particular, we want to thank

[Jonathan](https://x.com/claudijd)from

[Asymmetric Research](https://www.asymmetric.re),

[Sec3](https://www.sec3.dev), the entire

[SEAL 911](https://www.securityalliance.org/seal-911)team, especially

[Nick](https://x.com/bax1337),

[pcaversaccio](https://x.com/pcaversaccio), and

[Tay](https://x.com/tayvano_), XJ from

[Peckshield](https://peckshield.com),

[Robert](https://x.com/NotDeGhost)and

[Renato](https://x.com/GSfilatino)from

[OtterSec](https://osec.io), and

[Francesco](https://x.com/francescpicc)from

[Almanax](https://www.almanax.ai). We’re also deeply thankful to our users for their continued trust and patience as we work to restore full protocol functionality.

## 

The exploit stemmed from an incomplete validation of the RateX program used to price RateX principal tokens (PT tokens). The vulnerable code was introduced on March 27 as part of an upgrade to support RateX collateral markets. [RateX](https://rate-x.io)implements each of its markets as a standalone program exposing a

`get_pt_price` instruction. Loopscale relies on this instruction’s output via cross-program invocation (CPI), in conjunction with Pyth oracle feeds, to calculate collateral value.
While the Loopscale protocol enforced program validations for Exponent PT tokens and RateX PT Loops, it failed to extend the same checks to non-Loop borrows collateralized by RateX tokens. This gap allowed the attacker to deploy a malicious program that spoofed the interface of a valid RateX market. The program returned an artificially inflated PT exchange rate via `get_pt_price`, enabling the series of loans that effectively bypassed health checks.
This was a targeted technical exploit of a specific integration path, not a failure of Loopscale’s economic model or protocol architecture. The core order book logic and vault mechanics functioned as intended and were not compromised.
## 

## 

The exploit impacted the USDC and SOL Genesis Vaults, leading to temporary losses of 5,726,724.97 USDC across 3,126 depositors and 1,211.4 SOL across 2,047 depositors. **All funds were fully recovered through coordinated efforts with ecosystem partners.**Loopscale is reimbursing a $29,000 discrepancy caused by the attacker swapping USDC at less favorable rates than those at which the funds were later reacquired.

**No user deposits incurred any loss.**The vulnerability was limited to loans backed by RateX principal tokens. No other vaults or advanced lending positions were affected. Existing safeguards, including market isolation, collateral segregation, and liquidity buffers, helped contain the impact. In response, protocol functionality was paused. Loan repayments and closure of Loops were re-enabled on April 26, followed by Advanced Lending position management/withdrawals on April 30. Vault withdrawals were enabled today, May 8, with

[24-hour per-user limits](https://x.com/Loopscale/status/1917709358529421496). Borrowing and looping remain paused pending the completion of Sec3’s audit and security improvements.

## 

### 

Several existing protocol safeguards helped contain the impact of the exploit:
- **Market Isolation:** Eligible collateral configurability ensured no other vaults or Advanced Lending positions were affected.
- **Non-Rehypothecated Collateral:** Per-loan collateral segregation ensured the safety of borrower collateral deposits.
- **Liquidity Buffers:** Withdrawal buffers limited the funds at risk.
- **Emergency Protocol Pause:** Core functionality was paused shortly after the exploit occurred.

While these measures helped reduce the scale of the incident, they were far from sufficient. Future releases will include significantly stronger safeguards to prevent similar failures.

### 

Following the exploit, Loopscale engaged SEAL 911 to coordinate incident response. Over the next 12 hours, we shared exploit details with Wormhole Network contributors, notified centralized exchanges and swapping services to restrict off-ramping or swapping, and escalated the case with law enforcement. Due to the sensitive nature of the incident, we cannot comment on the investigation any further for now.
Communications with the attacker were initiated via an on-chain message the morning of April 27, leading to the full return of misappropriated funds over the next 48 hours.
### 

To close the vulnerability, the exploited check was updated to enforce strict validation of RateX program IDs during loan health checks. All related instructions were reviewed to ensure reliability and integrity of program inputs.
These changes eliminate the exploit vector by ensuring that only validated program accounts can be used during loan execution. **The patch was reviewed by Sec3 and two additional third-party security auditors.**

### 

To strengthen protocol security and prevent future exploits, Loopscale is introducing a comprehensive set of technical and operational safeguards:
#### 

- **Expanded Audit Coverage:** Our ongoing engagement with Sec3 covers the full program library, including all collateral pricing integrations. Additional audits are scheduled to be completed in the coming months.
- **Bug Bounty Program:** Following the completion of additional audits, Loopscale will launch a formal bug bounty program.
- **Progressive, Feature-Specific Audits:** No program functionality or updates will be deployed without a formal third-party audit.
- **Operational Monitoring:** While Loopscale has a number of monitoring and alerting systems in place, additional weekly reviews of failed transactions, backend logs (tracked via Sentry), and anomalous RPC activity are now formalized as operational procedures.
- **Program Access Controls:** Market, vault, and oracle parameter updates are now gated by multisig authorization as an additional safeguard against unauthorized changes.

These measures reflect a broader shift toward security-first development we are committed to sustaining across all future releases.

#### 

In the next protocol release, Loopscale will expand risk management functionality for Vaults and Advanced Lending Positions to mitigate systemic risks, manage liquidity flows, and contain abnormal activity. This release will include:
- **Borrow, Supply, and Withdrawal Caps:** Time-based and total limits
- **Collateral Exposure Limits:** Constraints on how much can be borrowed against a single asset to reduce concentration risk
- **Loan Approval Thresholds:** Manual and delayed approval mechanisms for large loans
- **Withdrawal Queues:** FIFO processing for transparent and orderly withdrawals during stressed market conditions

All parameters are optional and configurable per-vault by the Vault Curator and per-position by

[Advanced Lending](https://docs.loopscale.com/using-loopscale/advanced-lend)depositors. Future Vaults curated by Loopscale will adopt a conservative risk profile leveraging this functionality.
