# GHSA-m886-r6ch-pjvr: QBFT/IBFT2 message decode performs unbounded eager signature recovery before the validator check, letting any peer stall the consensus thread (DoS)

| Field | Value |
| --- | --- |
| Repo | hyperledger/besu |
| GHSA | GHSA-m886-r6ch-pjvr |
| CVE | none assigned |
| Severity | high |
| CWE | CWE-400, CWE-770 |
| Published | 2026-10-13T02:15:58Z |
| Updated | 2026-10-13T02:15:58Z |
| Affected | org.hyperledger.besu:besu <= 26.8.0 (patched: 26.8.1) |
| Credits | n/a |
| Advisory URL | https://github.com/besu-eth/besu/security/advisories/GHSA-m886-r6ch-pjvr |
| Captured | 2026-11-12 (WAT), daily update |

## Description (verbatim)

## Impact

Any peer negotiating the `istanbul/100` devp2p sub-protocol can send a crafted `RoundChange` or `Proposal` message containing an unbounded embedded list (the `prepares` or `round-changes` list). QBFT and IBFT2 decode these lists and perform an eager `ecrecover` (public-key recovery) for **every** entry **before** the sender is checked against the validator set. A single large message (about 10.5 MB) costs roughly **4 seconds of consensus-thread CPU**, and no valid validator key is required, so any connected devp2p peer can send such messages repeatedly and stall BFT consensus — a denial of service against block production on QBFT/IBFT2 networks.

## Patches

Fixed in Besu **26.8.1**. A bounded `readList` overload checks the element count from the RLP list header before iterating and throws immediately if it exceeds the limit; `Proposal.decode` and `RoundChange.decode` cap the `prepares` and `round-changes` lists at 512 entries. IBFT2 additionally enforces a total decode budget derived from the validator count, because IBFT2 messages can be nested whereas QBFT messages are flat.

## Workarounds

Restrict BFT/devp2p connectivity to trusted peers at the network layer. Upgrade to Besu 26.8.1 or later for the actual fix.

## References

Fixed in PR #11214

Identified during internal security review of the QBFT/IBFT2 message decoding path.

