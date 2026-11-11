# Blockchain client bugs (geth, zcashd, zebra, lightwalletd, Agave/rBPF)

_Harness check spec. Drawn from the verbatim advisories under `projects/{zcash,ethereum,solana}/`. Nothing invented._

## Detection signals
- Special-case fee / claim / free-tx logic in rollup or L2 nodes (branch combinations: free×reverted, non-free×reverted).
- P2P message parsing that fails open (malformed blocks/txs accepted or not penalised).
- Consensus / pool-delta persistence that loops on invalid state.
- Memory-safety in C++ clients (use-after-free on stack destruction order).
- Underconstrained circuit gadgets used by the client (Orchard Action circuit).
- Checkpoint / body poisoning that stalls sync until restart.
- gRPC / API resource-exhaustion on light clients (OOM, goroutine leaks, mutex held across I/O).

## Sources (full text)
- Zcash: [`projects/zcash/advisories-index.md`](../../projects/zcash/advisories-index.md) — 76 GHSA (incl. Orchard soundness GHSA-ghc3-g8w4-whf9, zcashd UAF GHSA-fqr9-fxpx-rfpf, Zebra forged-checkpoint GHSA-9hq5-pfgc-cx5h, lightwalletd DoS set).
- Ethereum: [`projects/ethereum/advisories-index.md`](../../projects/ethereum/advisories-index.md) — 34 GHSA (go-ethereum + Lighthouse) + [`solidity-compiler-bugs.md`](../../projects/ethereum/solidity-compiler-bugs.md) (67 compiler bugs).
- Solana: [`projects/solana/advisories-index.md`](../../projects/solana/advisories-index.md) — OSV/RustSec (solana_rbpf, anchor-lang, spl-token-swap).

## Automation (check spec)
```
for advisory in projects/{zcash,ethereum,solana}/advisories/*.md:
  extract affected_versions, root_cause_keywords
  map to check: special-case fee branches | P2P parse | UAF | circuit constraint | gRPC resource bounds
for solidity_bug in solidity-compiler-bugs.md:
  if contract.compiler_version in [introduced, fixed): FLAG compiler-bug
```
