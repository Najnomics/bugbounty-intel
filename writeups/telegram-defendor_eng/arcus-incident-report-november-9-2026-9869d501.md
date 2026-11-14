# 🚨 Arcus Exchange Loses $2.23M to a Subaccount Transfer Bug

- **Source URL:** https://arcus.xyz/blog/arcus-incident-report-november-9-2026
- **Fetched:** 2026-11-14
- **Channel:** @defendor_eng
- **Telegram message:** https://t.me/defendor_eng/2331 (id 2331)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
Current page

Arcus

On November 9, Arcus identified an accounting bug which enabled a user to withdraw funds they were not entitled to. We detected and fixed the bug within one hour and have covered the full shortfall. No user balances were affected and trading and withdrawals are operating normally.

#### What happened

On November 9 at around 10:07 PM ET, a newly created account exploited a bug in how the exchange handled transfers between a user’s own subaccounts. Under specific conditions, the bug let the account record a balance far larger than it actually held. It then requested withdrawals against that inflated balance.

The incident only involved a single account; no other accounts were affected.

#### Impact

- $2,234,391 USDG was withdrawn on-chain before withdrawals were stopped.
- A further $3M of requested withdrawals was held by the bridge’s on-chain rate limit, never paid out, and later reversed.
- No other user balances, positions, or orders were affected.
- The temporary shortfall has been fully covered by Arcus Labs from the company's treasury.

#### How we responded (all times in ET from 11/09 to 11/10)

- **10:10 PM:** The bridge’s withdrawal rate limit automatically capped payouts and held back $3M of further requests.
- **10:15 PM:** Monitoring flagged the withdrawals and the team began investigating.
- **11:07 PM:** Platform-wide withdrawals were paused and the [status page](https://status.arcus.xyz/) was updated.
- **11:37 PM:** The bug fix was deployed.
- **11:43 PM:** The exploiter’s addresses were blocked from trading, transferring, and withdrawing.
- **4:26 AM:** Platform-wide withdrawals were re-enabled.
- **5:02 AM:** Pending withdrawals from the exploiter were reversed.
- **12:28 PM:** The shortfall was covered from the Arcus Labs company treasury.

#### What we fixed and what's changing

- The bug has been fixed, and the fix was reviewed by our security partners, along with related checks across the codebase.
- We're continuing to make improvements to our risk management systems for detecting and mitigating suspicious activity.

#### Recovering the funds

We are working with blockchain investigators and will coordinate with law enforcement as appropriate. The withdrawn funds are being tracked on-chain. The initial address of the exploiter is: 

`0xeFbf442599310E5CeE1A4EDd5c66334c5f30b3Dd`. 

We ask exchanges and service providers to flag any funds received from it.

#### Looking ahead

Following this incident, our team moved quickly to resolve the issue, restore normal operations, and implement additional safeguards.

We remain committed to improving our systems and continuously increasing the security and reliability of our product. What we’ve learned will make the platform stronger.

*If you have any questions, contact us at [\[email protected\]](https://arcus.xyz/cdn-cgi/l/email-protection).*
