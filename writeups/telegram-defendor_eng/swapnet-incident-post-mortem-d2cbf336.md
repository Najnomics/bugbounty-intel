# ⚠️ SwapNet Hack Post-Mortem: $13.4M Losses

- **Source URL:** https://meta.matcha.xyz/SwapNet-Incident-Post-Mortem
- **Fetched from:** https://web.archive.org/web/20260906224431/https://meta.matcha.xyz/SwapNet-Incident-Post-Mortem
- **Fetched:** 2026-11-27
- **Channel:** @defendor_eng
- **Telegram message:**  (id 1149)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# SwapNet Incident Post Mortem

If you have used Matcha Meta with the default setting of One-Time Approval **disabled**, revoke your approvals to the SwapNet contracts immediately across all chains:

`0x616000e384Ef1C2B52f5f3A88D57a3B64F23757e``0x6160006C4AA63Ad1cb8CC075d99127F9D8948BB5`
Use a tool like [Revoke.cash](https://web.archive.org/web/20260906224431/https://revoke.cash/) to check and revoke any outstanding approvals.

If you only used the default One-Time Approval setting, no action is required at this time.

## Summary

On January 25, 2026, SwapNet's smart contracts were exploited. A subset of Matcha Meta users was exposed by disabling the One-Time Approval toggle and granting infinite approval directly to the SwapNet contracts.

This led to $13.43M loss of funds for 18 users, including one user who lost approximately $13.34M.

External news outlets estimated the scope of impact at $16.8M, but that included the full scope of a concurrent $3.4M Aperture Finance incident, which was separate and unrelated.

**Matcha Meta, 0x AllowanceHolder, and 0x Settler smart contracts remain fully secure.**

## Am I Affected?

**The vast majority of Matcha Meta users are unaffected.**

If you use the **default One-Time Approval setting** (routes through 0x's AllowanceHolder contract and accounts for 90% of transactions) **you are not at risk.**

### **You are at risk if:**

- you made an **approval directly to the SwapNet contract**, either an infinite approval or an unused exact approval

## What to do if you may be at risk:

Revoke approvals to the SwapNet contract address listed above with tools such as [Revoke.cash](https://web.archive.org/web/20260906224431/https://revoke.cash/).

## What happened

Matcha Meta's default approval setting, **"One-Time Approval,"** can be bypassed by users, allowing them to:

1. Set direct approvals to an aggregator's contracts
2. Select "Approve Infinite" (as opposed to "Approve Exact")

Users on Matcha Meta who went through this flow for SwapNet became exposed to risk. It's likely an attacker waited until a sufficiently large balance became vulnerable.

This occurred on Base at block [41289829](https://web.archive.org/web/20260906224431/https://basescan.org/block/41289829), in transaction hash:

[0xdf81a643b03c4364dd2740d3ac177d0184c5b4e432257aaa0c277d4eef88a011](https://web.archive.org/web/20260906224431/https://basescan.org/tx/0xdf81a643b03c4364dd2740d3ac177d0184c5b4e432257aaa0c277d4eef88a011)

The attack commenced 12 blocks later, at block [41289841](https://web.archive.org/web/20260906224431/https://basescan.org/block/41289841), in transaction hash:

[0xc15df1d131e98d24aa0f107a67e33e66cf2ea27903338cc437a3665b6404dd57](https://web.archive.org/web/20260906224431/https://basescan.org/tx/0xc15df1d131e98d24aa0f107a67e33e66cf2ea27903338cc437a3665b6404dd57)

After the initial exploit, the attacker began draining as many impacted users as possible.

[Blockaid](https://web.archive.org/web/20260906224431/https://www.blockaid.io/) contributed to incident detection, response, impact analysis, and attribution.

SwapNet paused contracts on Base 45 minutes later, and all other chains were paused shortly thereafter. In the period between the first attack and SwapNet's contract pause, an additional 17 users were affected across 3 chains.

## Product Changes & Response

This incident caused us to fundamentally reevaluate the optionality we provided users. Our original intention—allowing sophisticated users to go direct to aggregators—has proven to grant too much power at the expense of security.

Erring on the side of customizability over security is not a posture we will allow moving forward.

We have made the following changes:

1. **Disabled the toggle** - Users can no longer turn off One-Time Approval
  - which defaults to the most secure flow - all transactions now route through our AllowanceHolder contract
2. **Disabled SwapNet** - Until further notice this aggregator has been removed from Matcha Meta

We're actively working with security firms and industry partners on collecting data and tracing down the funds.
