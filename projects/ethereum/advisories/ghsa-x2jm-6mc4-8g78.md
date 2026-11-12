# GHSA-x2jm-6mc4-8g78: QBFT/IBFT validator forgets its prepared certificate when the round advances by any route other than its own timer, weakening the quorum-intersection argument

| Field | Value |
| --- | --- |
| Repo | hyperledger/besu |
| GHSA | GHSA-x2jm-6mc4-8g78 |
| CVE | none assigned |
| Severity | medium |
| CWE | n/a |
| Published | 2026-10-29T02:02:00Z |
| Updated | 2026-10-29T02:02:00Z |
| Affected | org.hyperledger.besu:besu <= 26.9.0 (patched: 26.10.0) |
| Credits | jflo |
| Advisory URL | https://github.com/besu-eth/besu/security/advisories/GHSA-x2jm-6mc4-8g78 |
| Captured | 2026-11-12 (WAT), daily update |

## Description (verbatim)

### Impact

A QBFT or IBFT validator that has **prepared** a block in round *r* stops reporting that fact if it advances to a later round by any route other than its own round timer expiring. Its next `RoundChange` claims it has prepared nothing.

The prepared certificate was captured in exactly one place, on the round-expiry path. But the routine that replaces the current round is also reached when a valid future-round `Proposal` arrives, and when a round-change quorum is received - the latter being the **default** configuration. Neither path passed through the capture, so the round state holding the prepared flag was simply discarded.

This is more than under-reporting. The BFT safety argument rests on quorum intersection: to propose a different block in a later round, a proposer must present 2f+1 round-changes, and because a prepared block was prepared by 2f+1 validators, any such set intersects the prepared set in at least f+1 members, at least one of them honest - whose report binds the proposer to re-propose that block. That guarantee is discharged *by the reporting*. An honest node that has forgotten its certificate occupies its slot in the intersection while contributing nothing, which is exactly the case the argument was built to exclude. At n=4, f=1 this is reachable with a single amnesiac honest node, provided the Byzantine validator itself participated in preparing.

**No fork has been demonstrated.** The step from the amnesia to an accepted conflicting block is an analytical argument from the code and the protocol; it additionally requires a Byzantine validator, control of message scheduling, and the victim not re-preparing in the new round. What is demonstrated is the amnesia itself.

This is a long-standing deviation present in both BFT engines, inherited from IBFT 2.0. It is not a regression.

### Patches

The certificate is now latched whenever the current round is replaced, so every path that abandons a prepared round preserves it. Applied to both the QBFT and IBFT block-height managers.

### Workarounds

None.

### Credits

Reported through the Besu bug bounty programme.

## Patches and references

Fixed in Besu 26.10.0.

- Patch commit on `main`: https://github.com/besu-eth/besu/commit/24a8040f3e13
- Reconciled to `main` in https://github.com/besu-eth/besu/pull/11642

