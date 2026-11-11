# GHSA-v927-8q6p-vjx2: Fork choice promotes stale checkpoints after slashings

| Field | Value |
| --- | --- |
| Repo | sigp/lighthouse |
| GHSA | GHSA-v927-8q6p-vjx2 |
| CVE | none assigned |
| Severity | low |
| CWE | n/a |
| Published | 2026-10-15T04:54:53Z |
| Updated | 2026-10-15T04:54:53Z |
| Affected |  <8.2.0 (patched: >= 8.2.0) |
| Advisory URL | https://github.com/sigp/lighthouse/security/advisories/GHSA-v927-8q6p-vjx2 |

## Description (verbatim)

### Summary
In Lighthouse's fork choice, a same-epoch child block uses its parent’s unrealized justified and finalized checkpoints. If the child block contains slashings, Lighthouse does not exclude the votes of the slashed validators. Consequently, a node can treat a checkpoint as having enough votes even though it no longer does.

### Impact
Consider a chain that has barely exceeded the 2/3 requirement for finality. An attacker who controls a proposing validator and some other validators can intentionally slash themselves. If the slashed stake is large enough, it can cause the votes for the checkpoint to fall below the 2/3 requirement. Lighthouse wrongly assumes that the parent's justified checkpoint from prior to the slashing remains valid, however the slashing itself reverts the justification.

This attack requires the attacker to control the block proposer of the child block, and also to control the validators being slashed. The attack also requires that participation is around the 2/3 vote threshold, which makes the attack difficult to execute in practice as most networks have high participation rate. Additionally, in a mostly honest network, once honest attestations accumulate sufficient votes in the next epoch, the node will return to the correct chain. Therefore, the effect is temporary in a realistic network.

### Patches
The fix is to add a condition to check if there is a slashing when using the parent's checkpoint. We also added a test to prevent any regression. You may refer to this PR for the details: https://github.com/sigp/lighthouse/pull/9471

### Credits
The vulnerability was reported by Pranamya Keshkamat to the Ethereum Foundation bug bounty program.
