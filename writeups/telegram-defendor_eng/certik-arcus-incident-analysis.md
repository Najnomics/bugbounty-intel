# Arcus Incident Analysis

- **Source URL:** https://www.certik.com/blog/arcus-incident-analysis
- **Fetched:** 2026-11-14
- **Channel:** @defendor_eng
- **Telegram message:** https://t.me/defendor_eng/2338 (id 2338)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---

## Incident Summary

On November 10, 2026 UTC, nine Arcus BridgeVault payouts transferred **2,234,391 USDG** to the published incident wallet on Robinhood Chain. The project’s [report is named November 9 (opens in a new tab)](https://arcus.xyz/blog/arcus-incident-report-november-9-2026), while the relevant ledger and chain executions occurred on November 10 UTC. The token quantity is not an independently valued dollar loss or attacker profit.

The saved account records contain three exact signed64 wraparound residuals. That identifies a representation-level anomaly; the production value used by collateral validation remains unverified. The representative historical transactions connect an applied withdrawal to a published vault entitlement and payment, while leaving the upstream authorization unresolved.

Arcus [reports (opens in a new tab)](https://arcus.xyz/blog/arcus-incident-report-november-9-2026) that its treasury covered the shortfall and other user balances were unaffected. The [status record (opens in a new tab)](https://status.arcus.xyz/incidents/yjgqy2g9508z) corroborates a pause and resumption; recovery and incident-linked treasury replenishment have not been independently established.

## Key Transactions

## Key Addresses

| **Address** | **Label** | 
|---|---|
| [0xefbf442599310e5cee1a4edd5c66334c5f30b3dd (opens in a new tab)](https://robinhoodchain.blockscout.com/address/0xefbf442599310e5cee1a4edd5c66334c5f30b3dd) | Published incident wallet; payout recipient | 
| [0x14b107cf534239c59571b066cb6497a321da897c (opens in a new tab)](https://robinhoodchain.blockscout.com/address/0x5fc5360d0400a0fd4f2af552add042d716f1d168) | Arcus BridgeVault proxy | 
| [0x5fc5360D0400a0Fd4f2af552ADD042D716F1d168 (opens in a new tab)](https://robinhoodchain.blockscout.com/address/0x5fc5360d0400a0fd4f2af552add042d716f1d168) | USDG token | 
| [0x4FdBDaF4800fc28c22a967d23a343aCCE34315a4 (opens in a new tab)](https://robinhoodchain.blockscout.com/address/0x4fdbdaf4800fc28c22a967d23a343acce34315a4) | Payout wrapper / USDG transfer source | 
| [0xA49f317086368dA903EA40a286Ad675664c9e123 (opens in a new tab)](https://robinhoodchain.blockscout.com/address/0xa49f317086368da903ea40a286ad675664c9e123) | Publication executor | 
| [0x9d032106aE6e41F36132Fff1e7b0d973B4e55Da8 (opens in a new tab)](https://robinhoodchain.blockscout.com/address/0x9d032106ae6e41f36132fff1e7b0d973b4e55da8) | Validator consensus proxy in publication path | 
| [0xA3D46D248224070f58C5F750E1f2fcA2123DF487 (opens in a new tab)](https://robinhoodchain.blockscout.com/address/0xa3d46d248224070f58c5f750e1f2fca2123df487) | Checkpoint Manager in publication path | 
| [0x71fCE0590D6cE46D92e9fD982e1d65BB8Aac6319 (opens in a new tab)](https://robinhoodchain.blockscout.com/address/0x71fce0590d6ce46d92e9fd982e1d65bb8aac6319) | Vault implementation observed for first creation and payout | 
| [0x08fC299b608c6c37a601834152e2EAb986d4dB34 (opens in a new tab)](https://robinhoodchain.blockscout.com/address/0x08fc299b608c6c37a601834152e2eab986d4db34) | Implementation named by later upgrade | 

## Attack Flow

### Background

Arcus is a [perpetuals exchange (opens in a new tab)](https://docs.arcus.xyz/concepts/exchange-architecture) whose documented design combines an off-chain central limit order book, a permissioned validator appchain, and an EVM rootchain. A sequencer orders requests; the exchange state machine updates balances and positions. Custody and final token settlement occur on the rootchain, so an exchange balance and a wallet token payment are distinct stages.

A wallet can use up to ten [subaccounts (opens in a new tab)](https://docs.arcus.xyz/concepts/subaccounts), each with independent positions, orders and collateral. [Quote cash (opens in a new tab)](https://docs.arcus.xyz/api-reference/public/get-account.md) aggregates account and position cash. Equity also reflects open-position value and, where applicable, spot collateral and interest. Negative cash alone therefore does not establish insolvency; displayed free collateral can also be negative in a healthy spot-backed account.

A [withdrawal response (opens in a new tab)](https://docs.arcus.xyz/api-reference/exchange/submit-withdrawal.md) marked **202 PENDING** means queued. The later [**APPLIED** outcome (opens in a new tab)](https://docs.arcus.xyz/api-reference/public/get-account-transfer-updates.md) means the engine operation succeeded and balances changed. The documented collateral rule rejects a withdrawal or transfer before persistence if its amount exceeds **accountEquity − requiredMargin**, leaving account state unchanged. Validators then publish withdrawal effects through the Checkpoint Manager; BridgeVault stores the resulting entitlement, and a separate execution call pays it. Queuing, application, publication and payment are different boundaries: an applied request is not, by itself, a completed token outflow. These documents were captured after the incident and do not authenticate the historical engine build or risk input.
*Exhibit 1. Browser capture of the current [transfer-update documentation (opens in a new tab)](https://docs.arcus.xyz/api-reference/public/get-account-transfer-updates): a withdrawal or transfer exceeding free collateral should be rejected before persistence. Captured November 12, 2026; this describes intended behavior and does not establish the incident build's guard execution.*

### The historical sequence

1. **The recipient begins with a small recorded entitlement.** Returned account-1 history reconciles exactly: 6 deposits + 13 internal inflow − 11.789000001 internal outflow − 6.668396 withdrawals − 0.042603055 trading PnL = 0.500000944 quote units. This uses returned operator history and does not establish lifetime completeness or source equity.
2. **An internal transfer produces two extreme reported balances.** At 03:07:10.104964 UTC, sequence 10096155419, the source and recipient record the same applied transfer. After the same-sequence interest adjustment, source cash is −2,156.277510656 and recipient cash is +0.500000944; the reported post-transfer figures are +9,223,369,880.577265153 and −9,223,372,036.354774865. The feed does not establish instruction order.
3. **A one-token withdrawal crosses into on-chain entitlement.** At 03:08:46.831236 UTC, sequence 10096382839, the recipient’s applied 1 USDG withdrawal changes its reported cash to +9,223,372,036.354776751. At 03:08:51, the publication transaction creates BridgeVault record 39755, fixing the recipient, wrapper, 1,000,000 raw USDG, and true execution flag. At 03:08:52, eight rootchain blocks later, the payout consumes that ID and transfers 1 USDG. Matching ID, amount and recipient anchor this representative creation-to-payment sequence.
4. **Further withdrawal requests produce real token payments.** The remaining fourteen applied debits reconcile against the recorded positive balance. Fifteen applied requests total 5,234,391 USDG; nine successful payouts total 2,234,391 USDG. Six requests totaling 3,000,000 USDG have no matching payout through finalized block 111,322,906, November 11 at 01:13:26 UTC. Arcus attributes the held requests to its limiter and later reversal. *Figure 1. The representative first withdrawal, entitlement publication and payment. Solid arrows show observed ordering; the dashed boundary marks the unresolved question of whether collateral validation consumed a wrapped value.* *Exhibit 2. Browser capture of the first [payout receipt, log 3 (opens in a new tab)](https://robinhoodchain.blockscout.com/tx/0x534b430d8b651bff2849e249cef93cf031af5ac531e4c7272bc6a3a6b3f3ee29?tab=logs). The USDG transfer value is 1,000,000 raw units, or 1 USDG at six decimals. This is payment evidence; it does not expose the engine's arithmetic.*

## Vulnerability

### The arithmetic fingerprint

For an internal transfer of Δ, ordinary bookkeeping is source\_after = source\_before − Δ and recipient\_after = recipient\_before + Δ. A withdrawal then subtracts its debit from the recipient balance. Collateral approval is a separate decision; these equations describe the recorded balance transitions.

A signed 64-bit integer ranges from −2^63 to 2^63−1. In two's-complement arithmetic, a result outside that range wraps modulo 2^64. For intuition, eight-bit −128 − 1 is represented as +127: the discrepancy is one full cycle, 2^8. This illustrates the arithmetic only; languages and runtimes differ in their overflow behavior.

The Arcus quote scale is [1e9 quantums per quote unit (opens in a new tab)](https://docs.arcus.xyz/api-reference/exchange/submit-internal-transfer.md), so M = 2^64 equals **18,446,744,073.709551616 quote units.** The saved transfer records satisfy:

| Recorded transition | Residual versus ordinary arithmetic | 
|---|---|
| Source after transfer | **+M = +2^64** | 
| Recipient after transfer | **−M = −2^64** | 
| Pair total | **0** | 

The source and recipient reported balances therefore retain the same combined total, **−2,155.777509712 quote units**, even though each individual result has crossed a signed boundary. A pair-conservation check can miss that pattern.

### Why the next debit matters

The next recipient debit is 1 USDG. Its reported balance is just above the signed64 minimum, so ordinary subtraction crosses that boundary:

| Recipient cash transition | Quote units | 
|---|---|
| Reported cash before debit | −9,223,372,036.354774865 | 
| Ordinary result after subtracting 1 | −9,223,372,037.354774865 | 
| Reported result | +9,223,372,036.354776751 | 
| Reported minus ordinary | **+18,446,744,073.709551616 = M / 1e9** | 

This is signed underflow, within the broader integer-overflow class. Unlike the paired transfer, the debit has no opposite leg to cancel the residual. The result is an exact anomaly in the recorded cash transition, not evidence of additional deposited collateral.
*Figure 2. Analyst reconstruction from the saved source and recipient histories. The three residuals are exact reported-record identities, not a recovered production execution trace.*

### What the records support

The exact power-of-two residuals are more specific than a generic balance error. They identify a wrapping signature in the reported path; the layer is unresolved. The recipient history independently reconciles to 0.500000944 with returned ETH/SPY positions flat, which weakens an ordinary prior-entitlement explanation within that history's coverage. It does not establish complete lifetime history or source equity.

The pinned [public decoder (opens in a new tab)](https://github.com/arcus-xyz/da-reader/blob/0d34949ced3713d6c4a5e553cfd4218092b6825f/src/transfers.ts#L239) reads the amount and quote balances as signed 64-bit values. That supports the wire-format interpretation; it does not establish historical engine storage, arithmetic or an incident DA frame.
*Exhibit 3. The pinned decoder is a consumer-side source view. It does not identify the production arithmetic expression or the value consumed by collateral validation.*

The records establish a wrapping signature in the reported accounting path and a real entitlement and payment, but they do not identify which component performed the wrapping or show that the collateral guard consumed the wrapped value.

## Fund Flow

*Figure 3. Nine paid withdrawals establish 2,234,391 USDG of Arcus outflow. Six applied requests totaling 3,000,000 USDG had no matching payout through finalized block 111,322,906, November 11, 2026 at 01:13:26 UTC, and are excluded from that outflow.*

[Nine deposits (opens in a new tab)](https://api.relay.link/requests/v2?user=0xefbf442599310e5cee1a4edd5c66334c5f30b3dd&limit=20&startTimestamp=1794280020&endTimestamp=1794284000) sent **2,852,928.439519 USDG** gross into Relay. Two refunds returned **618,509.991541 USDG** to the incident wallet; they are not Arcus recoveries. Seven successful fill inputs total **2,234,418.439519 USDG**, exceeding the verified Arcus payouts by **27.439519 USDG.** Gross deposits include refunded and reused funds, so they must not be added to the incident outflow.

The [Relay request records (opens in a new tab)](https://docs.relay.link/references/api/get-requests-v2) associate seven fills with **1,052.212688526003007096 ETH** delivered on Ethereum. Independent receipts confirm the matched transactions succeeded, not their internal native-ETH values. The extra successful input prevents allocating all ETH solely to Arcus payouts; later custody and recovery remain outside the established trace.

Arcus’s [timeline (opens in a new tab)](https://arcus.xyz/blog/arcus-incident-report-november-9-2026) places monitoring detection at 03:15, pause at 04:07, fix at 04:37, reopening at 09:26, reversal at 10:02, and treasury top-up at 17:28 UTC on November 10. The reported fix is about ninety minutes after onset; the pause is the roughly one-hour milestone. Verified payouts continued through 03:53:56. Public status corroborates service interruption and restoration, while patch deployment, reversal accounting and treasury coverage still need independent evidence.

To keep up to date on the latest incident alerts and statistics, follow [@certikalert (opens in a new tab)](https://x.com/CertiKAlert) on X, explore our [incident dashboard](/certik-report/dashboard), or read our latest analysis on [certik.com](/blog).
