# Smart Contract

_Harness check spec. Every signal, payload and automation note below is drawn from the cited local files (full verbatim text under `posts/`, `writeups/`, `projects/`). Nothing here is invented; where a source only states a pattern, no concrete payload is asserted._


_Findings in corpus for this class: **83** (see `harness/findings.jsonl`)._

## Detection signals / takeaways from sources

- Require specific callback return data; revoke stale approvals; re-audit EOA-assumptions after EIP-7702. (from kankodu). Source: [`posts/kankodu/2026-09-11-2098377603396915590.md`](../../posts/kankodu/2026-09-11-2098377603396915590.md).
- Always test share/asset conversion at 1-wei and empty-vault boundaries. (from DevDacian). Source: [`posts/DevDacian/ARCHIVE.md`](../../posts/DevDacian/ARCHIVE.md), [`data/x_posts.jsonl`](../../data/x_posts.jsonl).
- Batch message validators must apply the same ownership check to every embedded sub-order type. (from al_f4lc0n). Source: [`posts/al_f4lc0n/2026-03-15-2033110168045568434.md`](../../posts/al_f4lc0n/2026-03-15-2033110168045568434.md).
- Track upstream patches for IBC/Cosmos and confirm every chain upgrade actually includes them. (from ChainLight_io). Source: [`posts/ChainLight_io/ARCHIVE.md`](../../posts/ChainLight_io/ARCHIVE.md), [`data/x_posts.jsonl`](../../data/x_posts.jsonl).
- Median oracles are not automatically safe; model the actual price spread. (from cmichelio). Source: [`posts/cmichelio/2024-06-11-1800463263433678945.md`](../../posts/cmichelio/2024-06-11-1800463263433678945.md).
- Token/pool setup that trusts freshly deployed ERC20 metadata is front-runnable. (from kankodu). Source: [`posts/kankodu/ARCHIVE.md`](../../posts/kankodu/ARCHIVE.md), [`data/x_posts.jsonl`](../../data/x_posts.jsonl).
- Fee-collection on attacker-controlled token callbacks is classic reentrancy. (from ChainLight_io). Source: [`posts/ChainLight_io/ARCHIVE.md`](../../posts/ChainLight_io/ARCHIVE.md), [`data/x_posts.jsonl`](../../data/x_posts.jsonl).
- Liquidation logic that can be forced against healthy positions is direct theft of PnL. (from 0xriptide). Source: [`posts/0xriptide/ARCHIVE.md`](../../posts/0xriptide/ARCHIVE.md), [`data/x_posts.jsonl`](../../data/x_posts.jsonl).
- Reentrancy still drains TVL in 2023+ deployments — callbacks on value transfer remain mandatory checks. (from ChainLight_io). Source: [`posts/ChainLight_io/ARCHIVE.md`](../../posts/ChainLight_io/ARCHIVE.md), [`data/x_posts.jsonl`](../../data/x_posts.jsonl).

## Method / findings in sources

- **EtherFi helper contract hack — three holes lined up** — AtomicQueue called a callback on a user-provided address and treated a successful call as intent (no required return data); the victim had a year-old hanging approval; EIP-7702 delegation made the victim EOA execute code, so the callback no longer simply failed. Source: [`posts/kankodu/2026-09-11-2098377603396915590.md`](../../posts/kankodu/2026-09-11-2098377603396915590.md).
- **Rounding-down precision loss → repeated 1-wei mint leaching free tokens** — Similar to raft finance exploit: repeatedly minting 1 wei to leach free tokens due to rounding down to zero precision loss in share calculation; also worked in inverse. Source: [`posts/DevDacian/ARCHIVE.md`](../../posts/DevDacian/ARCHIVE.md), [`data/x_posts.jsonl`](../../data/x_posts.jsonl).
- **Injective MsgBatchUpdateOrders missing subaccount ownership check — any account drain (Critical, disputed $50K)** — MsgBatchUpdateOrders ValidateBasic checked ownership for limit/cancel orders but (per full report) missed the check on certain order types, letting any user drain any account. Over $500M on-chain assets stated at risk. Reported via Immunefi; team pushed a mainnet upgrade via governance; payout disputed. Source: [`posts/al_f4lc0n/2026-03-15-2033110168045568434.md`](../../posts/al_f4lc0n/2026-03-15-2033110168045568434.md).
- **Terra $5.3M loss — known IBC-hook timeout-callback reentrancy left unpatched** — Root cause was a known reentrancy in the timeout callback on IBC hook. Cosmos patched in April; Terra did not include the patch in its upgrade. Exploit involved 60M $ASTRO; price crashed >60%. Source: [`posts/ChainLight_io/ARCHIVE.md`](../../posts/ChainLight_io/ARCHIVE.md), [`data/x_posts.jsonl`](../../data/x_posts.jsonl).
- **Median of 11 oracle sources — how many to manipulate?** — When sources cluster tightly, moving the median needs ~half (6 of 11) sources; but if sources are spread, fewer manipulated sources can shift the median (UwU Lend context). Source: [`posts/cmichelio/2024-06-11-1800463263433678945.md`](../../posts/cmichelio/2024-06-11-1800463263433678945.md).
- **Balancer V2 infinite balances via front-running ERC20 deployments ($250k)** — Critical vulnerability allowing attackers to create infinite token balances by front-running ERC20 deployments. $250k reward; later publicly disclosed. Source: [`posts/kankodu/ARCHIVE.md`](../../posts/kankodu/ARCHIVE.md), [`data/x_posts.jsonl`](../../data/x_posts.jsonl).
- **GemPad $1.9M — reentrancy in collectFee via fake-token LP lock callback** — Reentrancy in collectFee of lock contract. Exploiter minted a fake token, locked its LP, re-entered collectFee via callback, drained project vault. Source: [`posts/ChainLight_io/ARCHIVE.md`](../../posts/ChainLight_io/ARCHIVE.md), [`data/x_posts.jsonl`](../../data/x_posts.jsonl).
- **Deri Protocol: force-liquidate healthy position and steal trader PnL (Critical)** — Critical vulnerability allowing an attacker to force liquidate a healthy position and steal a trader's PnL. Writeup on Mirror; Immunefi. Source: [`posts/0xriptide/ARCHIVE.md`](../../posts/0xriptide/ARCHIVE.md), [`data/x_posts.jsonl`](../../data/x_posts.jsonl).
- **Stars Arena second attack — classic reentrancy drained TVL** — Right after first exploit, Stars Arena second attack drained whole TVL; reentrancy pointed as root cause. Source: [`posts/ChainLight_io/ARCHIVE.md`](../../posts/ChainLight_io/ARCHIVE.md), [`data/x_posts.jsonl`](../../data/x_posts.jsonl).
- **YulOptimizerKnowledgeBaseStaleBookkeeping** — ## YulOptimizerKnowledgeBaseStaleBookkeeping - **Severity:** low - **Introduced:** 0.8.19 **Fixed:** 0.8.38 - **Trigger conditions:** {"yulOptimizer": true} - **More info:** https://blog.soliditylang.org/2026/10/22/yul-optimizer-knowledge-base-stale-bookkeeping-bug/ **Summary:** The Yul optimizer could consider two memory or storage locations disti Source: [`projects/ethereum/solidity-compiler-bugs.md`](../../projects/ethereum/solidity-compiler-bugs.md).
- **MisorderedNamedParametersInRequireWithCustomErrors** — ## MisorderedNamedParametersInRequireWithCustomErrors - **Severity:** very low - **Introduced:** 0.8.26 **Fixed:** 0.8.37 - **Trigger conditions:** {"viaIR": true} - **More info:** https://blog.soliditylang.org/2026/09/10/misordered-named-parameters-in-require-with-custom-errors-bug/ **Summary:** Custom error arguments passed to ``require`` using n Source: [`projects/ethereum/solidity-compiler-bugs.md`](../../projects/ethereum/solidity-compiler-bugs.md).
- **MemoryByteArrayElementDeleteClearsWholeWord** — ## MemoryByteArrayElementDeleteClearsWholeWord - **Severity:** low/medium - **Introduced:** (unknown) **Fixed:** 0.8.37 - **Trigger conditions:** {"viaIR": false} - **More info:** https://blog.soliditylang.org/2026/09/10/memory-byte-array-element-delete-clears-whole-word-bug/ **Summary:** Applying ``delete`` to a single element of a ``bytes`` array Source: [`projects/ethereum/solidity-compiler-bugs.md`](../../projects/ethereum/solidity-compiler-bugs.md).
- **SpillSlotCollisionAcrossMutualRecursion** — ## SpillSlotCollisionAcrossMutualRecursion - **Severity:** low/medium - **Introduced:** 0.7.2 **Fixed:** 0.8.37 - **Trigger conditions:** {"viaIR": true} - **More info:** https://blog.soliditylang.org/2026/09/10/spill-slot-collision-across-mutual-recursion-bug/ **Summary:** Local variables of two simultaneously active functions moved to fixed memor Source: [`projects/ethereum/solidity-compiler-bugs.md`](../../projects/ethereum/solidity-compiler-bugs.md).
- **InheritanceOrderReversalOnStorageEndWarning** — ## InheritanceOrderReversalOnStorageEndWarning - **Severity:** medium - **Introduced:** 0.8.29 **Fixed:** 0.8.36 - **More info:** https://blog.soliditylang.org/2026/07/09/inheritance-order-reversal-on-storage-end-warning-bug/ **Summary:** Emitting a warning about storage base location being too close to the storage end unintentionally reversed the  Source: [`projects/ethereum/solidity-compiler-bugs.md`](../../projects/ethereum/solidity-compiler-bugs.md).
- **UnsoundSpillInMutualRecursion** — ## UnsoundSpillInMutualRecursion - **Severity:** medium - **Introduced:** 0.7.2 **Fixed:** 0.8.36 - **Trigger conditions:** {"viaIR": true} - **More info:** https://blog.soliditylang.org/2026/07/09/unsound-spill-in-mutual-recursion-bug/ **Summary:** Local variables of a function involved in mutual recursion may spuriously be moved to fixed memory o Source: [`projects/ethereum/solidity-compiler-bugs.md`](../../projects/ethereum/solidity-compiler-bugs.md).
- **TransientStorageClearingHelperCollision** — ## TransientStorageClearingHelperCollision - **Severity:** high - **Introduced:** 0.8.28 **Fixed:** 0.8.34 - **Trigger conditions:** {"viaIR": true, "evmVersion": ">=cancun"} - **More info:** https://blog.soliditylang.org/2026/02/18/transient-storage-clearing-helper-collision-bug/ **Summary:** Clearing both storage and transient storage variables i Source: [`projects/ethereum/solidity-compiler-bugs.md`](../../projects/ethereum/solidity-compiler-bugs.md).
- **LostStorageArrayWriteOnSlotOverflow** — ## LostStorageArrayWriteOnSlotOverflow - **Severity:** low - **Introduced:** 0.1.0 **Fixed:** 0.8.32 - **More info:** https://blog.soliditylang.org/2025/12/18/lost-storage-array-write-on-slot-overflow-bug/ **Summary:** Operations that involve clearing or copying from arrays that straddle the end of storage could result in silent data retention. **D Source: [`projects/ethereum/solidity-compiler-bugs.md`](../../projects/ethereum/solidity-compiler-bugs.md).
- **VerbatimInvalidDeduplication** — ## VerbatimInvalidDeduplication - **Severity:** low - **Introduced:** 0.8.5 **Fixed:** 0.8.23 - **More info:** https://blog.soliditylang.org/2023/11/08/verbatim-invalid-deduplication-bug/ **Summary:** All ``verbatim`` blocks are considered identical by deduplicator and can incorrectly be unified when surrounded by identical opcodes. **Description:* Source: [`projects/ethereum/solidity-compiler-bugs.md`](../../projects/ethereum/solidity-compiler-bugs.md).

## Payloads / requests seen in sources

- `Chain: unchecked callback return in AtomicQueue + victim stale approval + EIP-7702 delegation so the EOA executes attacker code on callback` — EtherFi helper contract hack — three holes lined up. Source: [`posts/kankodu/2026-09-11-2098377603396915590.md`](../../posts/kankodu/2026-09-11-2098377603396915590.md).
- `Repeatedly mint 1 wei when share calculation rounds down to zero` — Rounding-down precision loss → repeated 1-wei mint leaching free tokens. Source: [`posts/DevDacian/ARCHIVE.md`](../../posts/DevDacian/ARCHIVE.md), [`data/x_posts.jsonl`](../../data/x_posts.jsonl).

See also [`../payloads/smart-contract.md`](../payloads/smart-contract.md) when present.

## Automation (check spec)

```
# Checks derived from 83 documented finding(s) in findings.jsonl for class=smart-contract
# try: Chain: unchecked callback return in AtomicQueue + victim stale approval + EIP-7702 delegation so the EOA executes attacker code on callback
# try: Repeatedly mint 1 wei when share calculation rounds down to zero
# note: Batch message validators must apply the same ownership check to every embedded sub-order type.
# note: Track upstream patches for IBC/Cosmos and confirm every chain upgrade actually includes them.
# note: Median oracles are not automatically safe; model the actual price spread.
# note: Token/pool setup that trusts freshly deployed ERC20 metadata is front-runnable.
# note: Fee-collection on attacker-controlled token callbacks is classic reentrancy.
# note: Liquidation logic that can be forced against healthy positions is direct theft of PnL.
```

## Prior harness notes (retained)

_Retained from earlier curated harness file; still cites local sources._

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

- 2026-11-17: see [2026-11-17 check-specs](2026-11-17-ai-tool-idor-oauth-scheme-roles-module.md)
