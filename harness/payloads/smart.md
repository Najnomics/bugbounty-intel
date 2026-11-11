# Payloads — smart

_Verbatim payload / request patterns extracted from findings in this repo. Nothing invented._

## 1. EtherFi helper contract hack — three holes lined up
- Researcher: @kankodu
- Post: https://x.com/kankodu/status/2098377603396915590
- Sources: `posts/kankodu/2026-09-11-2098377603396915590.md`

```
Chain: unchecked callback return in AtomicQueue + victim stale approval + EIP-7702 delegation so the EOA executes attacker code on callback
```
