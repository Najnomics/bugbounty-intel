# Smart contract: access control, rounding, reentrancy, oracle, signature replay

_Harness check spec. Every signal, payload and automation note below is drawn from the cited local files (full verbatim text under `posts/` and `writeups/`). Nothing here is invented; where a source only states a pattern, no concrete payload is asserted._


## Detection signals
- Callbacks on user-supplied addresses that assume success = intent.
- Stale/leftover approvals; EIP-7702 delegation turning EOAs into code.
- Median/price oracles whose source spread makes manipulation cheaper than the naive bound.
- Governance/vote accounting that lets one party overwrite another's record.
- Rounding/precision in share math; missing access control on privileged functions; signature/nonce replay.

## Method / findings in sources
- EtherFi: unchecked callback return (AtomicQueue) + stale approval + EIP-7702 chained to theft. Source: [`posts/kankodu/2026-09-11-2098377603396915590.md`](../../posts/kankodu/2026-09-11-2098377603396915590.md).
- Oracle median: model the real price spread; 6/11 is only the naive bound (UwU Lend). Source: [`posts/cmichelio/2024-06-11-1800463263433678945.md`](../../posts/cmichelio/2024-06-11-1800463263433678945.md).
- Governance vote erasure (Solana): any validator could erase delegators' dissenting votes. Source: [`posts/asymmetric_re/2026-10-19-2112236410455597403.md`](../../posts/asymmetric_re/2026-10-19-2112236410455597403.md).
- Frontier EVM wrapped-native insolvency. Source: [`writeups/PwningEth/`](../../writeups/PwningEth/).

## Tools
- Foundry/forge for PoC, static review of callback/approval patterns.

## Automation (check spec)
```
flag callbacks on user-supplied addr lacking required return data
scan for leftover approvals + 7702-delegatable EOAs
for oracle: compute min sources to move median given actual spread (not n/2+1)
for governance: check who can modify another account's vote/record
check share math for rounding-to-attacker; privileged fns for missing authz; sigs for nonce reuse
```

