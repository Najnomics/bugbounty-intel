# Payloads — cross chain bridge

_Verbatim payload / request patterns extracted from findings in this repo. Nothing invented._


## 1. Polygon zkEVM: reverted non-free claim txs mark deposit counts and block L1→L2 claims (Immunefi)
- Researcher: @0xiczc
- Post: https://x.com/0xiczc/status/1662090451493740545
- Sources: `posts/0xiczc/2023-05-26-1662090451493740545.md`, `writeups/0xiczc/certik-evm-cosmos-convergence-part-2.md`, `writeups/0xiczc/evmos-advisory-GHSA-3fp5-2xwh-fxm6.md`, `writeups/0xiczc/polygon-zkevm-node-pr-2048.md`

```
Submit a non-free (gas>0) claim tx that reverts: it falls into the else branch, is pooled and marks its deposit count used, blocking the legitimate L1->L2 claim and DoSing the sequencer
```

## 2. 🔬 HOT Bridge / NEAR Intents $3.86M Exploit Analysis
- Source: `telegram writeups (verbatim excerpts)`

```
let requested_refund = requested_refund.unwrap_or(*deposited);
let balance_left = receiver.token_balances.amount_for(&token_id);
let refund_amount = balance_left.min(requested_refund);
```

## 3. 🔬 HOT Bridge / NEAR Intents $3.86M Exploit Analysis
- Source: `telegram writeups (verbatim excerpts)`

```
let refund_amount = requested_refund.min(*deposited).min(balance_left);
```
