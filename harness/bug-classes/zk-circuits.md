# ZK: under-constrained / soundness bugs

_Harness check spec. Every signal, payload and automation note below is drawn from the cited local files (full verbatim text under `posts/` and `writeups/`). Nothing here is invented; where a source only states a pattern, no concrete payload is asserted._


## Detection signals
- Circuit signals that are not fully constrained (missing range checks, missing equality/boolean constraints), letting a prover forge a valid proof for a false statement.
- Verifier logic that accepts malformed or replayed proofs.

## Method seen in sources
- Read circuits line by line AND read verifiers; loss-of-TVL bugs live in both. Source: techniques.md (LonelySloth) and [`researchers/zksecurityXYZ.md`](../../researchers/zksecurityXYZ.md), [`researchers/ChainLight_io.md`](../../researchers/ChainLight_io.md).
- zkEVM node/bridge logic (not the circuit) can also break soundness-adjacent invariants: Polygon zkEVM free-claim branch bug. Source: [`posts/0xiczc/2023-05-26-1662090451493740545.md`](../../posts/0xiczc/2023-05-26-1662090451493740545.md).
- Reference: 0xPARC zk-bug-tracker (not fetched — see sources-log).

## Automation (check spec)
```
for signal in circuit_signals:
  if not fully_constrained(signal): FLAG under-constrained
enumerate verifier branches for free/reverted/replayed proof handling
```

