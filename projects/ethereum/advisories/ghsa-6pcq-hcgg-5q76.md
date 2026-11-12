# GHSA-6pcq-hcgg-5q76: IBFT Accepts Oversized Base Fees That Can Stop Block Production

| Field | Value |
| --- | --- |
| Repo | hyperledger/besu |
| GHSA | GHSA-6pcq-hcgg-5q76 |
| CVE | none assigned |
| Severity | medium |
| CWE | n/a |
| Published | 2026-11-10T04:40:47Z |
| Updated | 2026-11-10T04:40:47Z |
| Affected | org.hyperledger.besu:besu <= 26.10.1 (patched: 26.10.2) |
| Credits | CertiK4Audit, macfarla |
| Advisory URL | https://github.com/besu-eth/besu/security/advisories/GHSA-6pcq-hcgg-5q76 |
| Captured | 2026-11-12 (WAT), daily update |

## Description (verbatim)

### Summary
The IBFT 2.0 header ruleset does not validate the base-fee value. A malicious current validator can introduce an oversized base fee that later reaches a signed numeric conversion during block creation and stops block production in the tested configuration.

### Details
In Besu 26.7.1 at commit `49026aaf059f832a93f964d8d27191de2f0580e9`, `IbftBlockHeaderValidationRulesetFactory` does not add the base-fee validation rule present in `MainnetBlockHeaderValidator`. A later block-creation path calls `calculateExcessBlobGasForParent`, which converts the parent header base fee with `toLong()`.

An oversized base fee can therefore be admitted by IBFT and later cause the numeric conversion during block creation to fail.

### PoC
Use four IBFT 2.0 validators running Besu 26.7.1 with a London-only schedule and `zeroBaseFee` enabled. One Byzantine current validator proposes the test block. First run a no-file control and confirm normal production on all four nodes. Then use a base fee of `2^63 - 1`; require the block to be admitted on all victims and require height to continue advancing.

For the fault case, use a base fee of `2^63`. Confirm that all victims admit the canonical block, then observe the subsequent block-creation failure and lack of height advancement across the four validators. Capture the block-creation error and compare the affected interval with the advancing controls.

### Impact
A current validator can stop block production in the stated four-validator, London-only, `zeroBaseFee` IBFT configuration. The result is a prolonged liveness failure in that configuration. It does not claim permanence, a same-height fork, fund impact, QBFT impact, or applicability to default fee-market configurations.

### Suggested remediation
Apply an IBFT base-fee value validation rule equivalent to the relevant mainnet rule and make numeric conversion total or guarded so an admitted header cannot break subsequent block creation.

## Patches and references

Fixed in Besu 26.10.2.

- Patch commit on `main`: https://github.com/besu-eth/besu/commit/18c3946c17bf5772fe3f22df7543d2f98e6df50a
- Release: https://github.com/besu-eth/besu/releases/tag/26.10.2

