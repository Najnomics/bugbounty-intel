# 🔬 HOT Bridge / NEAR Intents $3.86M Exploit Analysis

- **Source URL:** https://www.certik.com/blog/hot-bridge-near-intents
- **Fetched:** 2026-11-12
- **Channel:** @defendor_eng
- **Telegram message:** https://t.me/defendor_eng/2230 (id 2230)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
## Incident Summary

On 30 September 2026, HOT Omni Bridge on NEAR was exploited, resulting in five observed BSC treasury payouts totaling $3.86M USD.

The attacker used a large pre-existing balance of a custom auxiliary token to request refunds far greater than the amounts in a new deposit. Recording the resulting large decimal amounts expanded the refund event beyond NEAR's 16384 bytes log limit and failed the Intents deposit resolver. HOT subsequently returned the original deposited backing, including USDT, while the Intents credit created by an earlier successful receipt survived.

## Addresses and roles

| Chain | Address or account | Established role | 
|---|---|---|
| BSC | [0x09fd1f5d9f185067a92493e43aa259ea4ab3ad37 (opens in a new tab)](https://bscscan.com/address/0x09fd1f5d9f185067a92493e43aa259ea4ab3ad37) | Exploiter, receiving $3.865M | 
| BSC | [0x233c5370CCfb3cD7409d9A3fb98ab94dE94Cb4Cd (opens in a new tab)](https://bscscan.com/address/0x233c5370CCfb3cD7409d9A3fb98ab94dE94Cb4Cd#code) | HOT Bridge treasury | 
| NEAR | [20e6bfe4685d99004fc2095d3a0fc6158cd810ce8f801196141e183ed6e19d65 (opens in a new tab)](https://nearblocks.io/address/20e6bfe4685d99004fc2095d3a0fc6158cd810ce8f801196141e183ed6e19d65) | Exploiter, initiating the batch deposits and cash-out requests; recipient of returned backing. | 
| NEAR | [dd1fe58ec316ada5b673b88c14fe2fa2b7ede82080440901dfbd64b994241757 (opens in a new tab)](https://nearblocks.io/address/dd1fe58ec316ada5b673b88c14fe2fa2b7ede82080440901dfbd64b994241757) | Exploiter contract, internal credit recipient and notification callback contract. | 
| NEAR | [873518f0f5cf120d7a8e2a416337bba16d7ae622e91f7da3862f07e89dc2ba9e (opens in a new tab)](https://nearblocks.io/address/873518f0f5cf120d7a8e2a416337bba16d7ae622e91f7da3862f07e89dc2ba9e) | Exploiter contract Later internal credit recipient in the verified October 1 sequences. Abbreviated 8735…. | 
| NEAR | [v2\_1.omni.hot.tg (opens in a new tab)](https://nearblocks.io/address/v2_1.omni.hot.tg) | HOT's bridge contract and NEP-245 multi-token representation ledger. | 
| NEAR | [intents.near (opens in a new tab)](https://nearblocks.io/address/intents.near/contract/code) | Intents Verifier contract and internal user-balance ledger. | 

## Background

HOT Bridge, also called HOT Omni Bridge, connects external-chain assets to NEAR and integrates with NEAR Intents for exchanges. Its public SDK is @hot-labs/omni-sdk. Three accounting layers are relevant: Actual external-chain asset in HOT treasury → HOT-issued token representation on NEAR → User's internal balance in intents.near

A normal inbound deposit works as follows:

1. The user deposits the actual asset on its source chain
2. HOT validates the deposit and authorizes its NEAR claim.
3. HOT creates the corresponding representation on NEAR.
4. Those tokens are deposited into Intents, which credits the user’s internal balance.

The Intents deposit code also supports an optional receiver notification. It credits the account first, then calls the receiving application, which may request that some deposited amounts be refunded.
For a normal refund, Intents must **remove the corresponding internal credit before returning its backing**. Its resolver burns the unused credit and reports the unused amounts to HOT; HOT then returns those representations to the original sender. Accepting a 10-USDT deposit should leave both 10 USDT of backing and 10 USDT of internal credit. Refunding it fully should leave neither additional backing nor additional credit.

The incident broke the connection between the second and third layers: **HOT returned the NEAR representation backing a deposit while Intents retained the user’s credit**. Subsequent bridge withdrawals could then draw on treasury assets through ordinary withdrawal machinery.

## Attack Flow

**1. Preparation**

On 29 September, the attacker claimed 10 BSC USDT on NEAR through [*9SiSBv…* (opens in a new tab)](https://nearblocks.io/txns/9SiSBvDea9TGUgZ7LDaEPtEB6FwLnKnXmZhjWrMc7gW7).
The attacker also bridged **97 × 10^36 + 97** raw units of the custom auxiliary asset *ctfhote6ae2a90d1836ef1* from Gonka. The [source deposit (opens in a new tab)](https://gonka.hyperfusion.io/chain-rpc/tx?hash=0x41982DF35E5A584EF6D8853F26660CC901C14B308CB1E439696284A163873035) matches the subsequent NEAR claim, [*Fmwao…* (opens in a new tab)](https://nearblocks.io/txns/FmwaoRNDU6BubkHZFy3ucSPpXVUrGUWkRVQwJAiJZZi3), which minted the HOT representation to *20e6…*.
In [*4wf2…* (opens in a new tab)](https://nearblocks.io/txns/4wf2FWcEhRadpqGUUc9nPLs8TUaCsFsqgqrDgtNe1m57), the attacker deposited **97 × 10^36** auxiliary units into Intents for attack receiver contract *dd1…*, leaving **97 raw units** outside Intents.

This established the large internal balance needed to support the oversized refund requests.

**2. Exploit**

The first verified exploit, [*3k91…* (opens in a new tab)](https://nearblocks.io/txns/3k91uDpUiezxUe7hBgAR7kc3TBkToMZKGAiv6GqbtKiC/execution), began on **29 September at 16:14:19.280 UTC**:

1. The attacker called HOT’s *mt\_batch\_transfer\_call*, depositing **97 auxiliary entries of one unit each**, **plus 10 USDT**, into Intents.
2. Intents successfully credited *dd1…* before notifying the receiver (attacker) contract.
3. The receiver returned **97 auxiliary refund requests of *10^36* each**, followed by **zero requested USDT refund**.
4. The vulnerable resolver limited refunds by the available balance but omitted the current deposit amount. [https://github.com/near/intents/blob/35044fd1795b0de9d1ac269c6aa28a0d6a7efdfa/contracts/defuse/src/contract/tokens/mod.rs#L183-L199 (opens in a new tab)](https://github.com/near/intents/blob/35044fd1795b0de9d1ac269c6aa28a0d6a7efdfa/contracts/defuse/src/contract/tokens/mod.rs#L183-L199)

The prepared balance therefore allowed enormous refund amounts into the burn event.

Here, **balance\_left** is the receiver’s **entire internal balance for that asset**, including previous deposits. The calculation checks whether the receiver has sufficient balance, but never limits the refund to *deposited*-the amount contributed by the current entry.
Consequently, an entry depositing only **one unit** could generate a refund of ***10^36*** units, provided the receiver’s existing balance covered it.

Each non-zero calculated refund is then appended to the burn event (line 198,199 above):

1. The resulting event measured 16,495 bytes, specifically

| Component | Calculation | Bytes | 
|---|---|---|
| 97 full token identifiers, each 125 characters | *97 × (125 + 2 quotes) + 96 commas* | 12,415 | 
| 97 refund amounts, each a quoted 37-digit string | *97 × (37 + 2 quotes) + 96 commas* | 3,879 | 
| EVENT\_JSON: prefix, metadata, owner ID, memo and remaining JSON punctuation | Fixed overhead 201 | 201 | 
| **Total** | **12,415 + 3,879 + 201** | **16,495** | 

exceeding NEAR’s **16,384-byte log limit** by just 11 bytes. Emitting it failed the resolver and rolled back that receipt’s attempted burns.

1. Failure during event emission reverted the resolver’s preceding balance deductions.

HOT then refunded the **entire original batch**, including the 10 USDT.

The [deposit handler (opens in a new tab)](https://github.com/near/intents/blob/a2dd140892b68140bf7e70814604d3ba074d656c/contracts/defuse/src/contract/tokens/nep245/deposit.rs#L66-L95) had called *self.deposit(...)* **before** scheduling the receiver notification and subsequent *mt\_resolve\_deposit*.

These executions occur in separate receipts and failure of a later call does not automatically revert the earlier caller’s changes. ([NEAR doc (opens in a new tab)](https://docs.near.org/smart-contracts/anatomy/crosscontract#what-happens-if-the-function-i-call-fails))
The Intents credit from the earlier successful receipt survived.

**3. Scaling**

The net result of the prior sequence is that **the attacker retained 10 USDT of internal Intents credit while receiving the original 10-USDT backing back**.

That enables two forms of amplification:

- **Reuse**: deposit the refunded USDT again, accumulating more internal credit.
- **Compounding**: redeem the retained credit into HOT USDT, then use that enlarged balance in a larger batch.

A later call [https://nearblocks.io/txns/3mst2uZ32KPuCs7wc8rJqEtCrZqugCy4yDSZ3df8KPm3 (opens in a new tab)](https://nearblocks.io/txns/3mst2uZ32KPuCs7wc8rJqEtCrZqugCy4yDSZ3df8KPm3) deposited **649,984 USDT**,requesting redemption of exactly 649,984 USDT back to the sender.

The collected history contains **23 batch calls associated with failed resolvers**, with complete retained-credit/backing-refund accounting canonically confirmed for six.

**4. Cash out**

The attacker subsequently submitted HOT cash-out requests on NEAR specifying the BSC recipient *0x09fd…ad37*. Five requests match successful USDT payouts from HOT’s BSC treasury *0x233c…4Cd*:

| **BSC payout time UTC** | **USDT** | **NEAR request** | **BSC payout** | 
|---|---|---|---|
| Sep 30, 23:54:30 | 800,000 | [A1tNAg… (opens in a new tab)](https://nearblocks.io/txns/A1tNAg5w3NVrDGheG9zTNmrXeWd4249nYyVLF8ekK3Xh) | [0x9fe58… (opens in a new tab)](https://bscscan.com/tx/0x9fe58e031f73bbd880c782bc9e7446bcda32cadb304a729209871a4a81856c4c) | 
| Oct 1, 00:24:02 | 1,200,000 | [799Tea… (opens in a new tab)](https://nearblocks.io/txns/799TeaBfrtCcmJ5dMT6fqupqLHyZQAqm2ksKoEfyMj7J) | [0x038126… (opens in a new tab)](https://bscscan.com/tx/0x0381265d6a1bb09de899f49f410a8b907cd548358a7e3c91076c3a52656b8220) | 
| Oct 1, 00:50:42 | 1,500,000 | [GJ65… (opens in a new tab)](https://nearblocks.io/txns/GJ65AKDXN9ov7DTFgmgvbykNww1B5J7jK42A4QfbHgon) | [0x69d1… (opens in a new tab)](https://bscscan.com/tx/0x69d1c68c7e961a0199d3c9f3b6a31cb168ed775ef34b51a42762253ac1efcceb) | 
| Oct 1, 01:46:20 | 330,000 | [E4gE… (opens in a new tab)](https://nearblocks.io/txns/E4gEvzNSPjeiah5c6pvUWTXkUmiiwjkbWr2zzQWsz6it) | [0x9c10… (opens in a new tab)](https://bscscan.com/tx/0x9c10b967da0c85631ec105e3b322c0a851fcd01b69ff390ff58f860e5cce003a) | 
| Oct 1, 06:08:26 | 35,000 | [Avf5… (opens in a new tab)](https://nearblocks.io/txns/Avf5qSFyndojAP7aYYMw2sCUZj2JSHUxYhK8CVGisy8B) | [0x16dd… (opens in a new tab)](https://bscscan.com/tx/0x16ddfa695b9525662b8e57c35723f44af89b4e7fc2dedc3634f730caf8b90c02) | 
| **Total** | **3865000** |  |  | 

## Vulnerability

1. Credit is committed before the receiver's refund response:
The [Intents incoming-deposit implementation (opens in a new tab)](https://github.com/near/intents/blob/a2dd140892b68140bf7e70814604d3ba074d656c/contracts/defuse/src/contract/tokens/nep245/deposit.rs#L66-L95) first calls:

```
self.deposit(
receiver_id.clone(),
core_token_ids
.clone()
.zip(amounts.iter().map(|amount| amount.0)),
Some("deposit"),
)
.unwrap_or_else(|err| err.panic());
```

For a notification deposit, it then schedules the receiver call and a later *mt\_resolve\_deposit*. The receipt that creates internal credit can succeed before that later resolver fails. The returned promise exposes the later failure to HOT even though the earlier credit already exists.

1. The vulnerable calculation accepts refunds larger than the current deposit:
NEAR's October 1 commit *[35044fd… (opens in a new tab)](https://github.com/near/intents/commit/35044fd1795b0de9d1ac269c6aa28a0d6a7efdfa)*, titled *chore: TEMP change that reflects deployed state*, reconstructs the refund logic as:

```
let requested_refund = requested_refund.unwrap_or(*deposited);
let balance_left = receiver.token_balances.amount_for(&token_id);
let refund_amount = balance_left.min(requested_refund);
```

Source: [resolve\_deposit\_internal (opens in a new tab)](https://github.com/near/intents/blob/35044fd1795b0de9d1ac269c6aa28a0d6a7efdfa/contracts/defuse/src/contract/tokens/mod.rs#L183-L218).

This calculation respects the available balance but omits the current deposited amount.
The loop appends each nonzero refund to a burn event and subtracts it from the receiver balance and internal total supply. It then emits:

```
MtEvent::MtBurn([burn_event].as_slice().into()).emit();
```

Those accounting changes are attempted within the resolver receipt. If emission fails, they roll back with it.

1. possible deployment/source discrepancy:
The missing deposited-amount cap was fixed in the public repository on **23 March 2026, at 12:47:07 UTC**, in [PR #240 / commit 015fa811… (opens in a new tab)](https://github.com/near/intents/commit/015fa811f9bfe05c92f1c0ce76949acba1fd34d6), titled *"fix: cap notify refunds by the original amounts"*:

```
let refund_amount = requested_refund.min(*deposited).min(balance_left);
```

For the observed one-unit auxiliary entries, this limits each refund to at most one unit regardless of prior balance. It prevents the oversized-number amplification used in this construction. It also restores the central deposit invariant: a refund for the current transfer cannot consume earlier deposits.
The October 1 temporary reconstruction commit removes that cap to model deployed behavior. NEAR's [October regression-test explanation (opens in a new tab)](https://github.com/near/intents/blob/0c1a530c8da337008e28baa9987a816249d707e6/tests/src/tests/defuse/tokens/nep245/mt_deposit_resolve_gas.rs#L433-L436) explicitly says that oversized refund logs caused the callback failure “as happened to the deployed revision.” [PR #362 (opens in a new tab)](https://github.com/near/intents/pull/362) adds regression coverage and audit tooling; Its final production diff does not introduce the original March cap.
\_\_These observations support a deployment/source discrepancy. \_\_

## Response and Recovery

A post-incident upgrade is visible in [*FPLaCtd…* (opens in a new tab)](https://nearblocks.io/txns/FPLaCtdyhKMHBFB6GZB1sexi4e1fJAAyFWSkjJ7XyqrN/execution). Its root transaction at **2 October 20:31:41.711 UTC** calls *ctl-intents.near.upgrade* for *intents.near*. The controller event identifies release **0.4.4**. A [successful nested deployment receipt (opens in a new tab)](https://nearblocks.io/txns/FPLaCtdyhKMHBFB6GZB1sexi4e1fJAAyFWSkjJ7XyqrN/execution#HHUzMtUDMSRXhwiy7dphJm9G12jkef9L1r6UhspMxxok) at **20:31:45.442** deploys code and executes *state\_migrate*.
Alex Shevchenko [publicly stated (opens in a new tab)](https://x.com/AlexAuroraDev/status/2106049685928677585) that the $3.86M was returned in full.
