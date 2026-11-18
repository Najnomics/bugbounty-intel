# GHSA-2vfg-f2fr-2jrv: IBFT/QBFT: a consensus message whose signature does not recover throws NullPointerException, and on IBFT can drop buffered consensus messages

| Field | Value |
| --- | --- |
| Repo | hyperledger/besu |
| GHSA | GHSA-2vfg-f2fr-2jrv |
| CVE | none assigned |
| Severity | low |
| CWE | CWE-476 |
| Published | 2026-11-18T05:22:53Z |
| Updated | 2026-11-18T05:22:53Z |
| Affected | org.hyperledger.besu:besu <= 26.10.2 (patched: 26.11.0) |
| Advisory URL | https://github.com/besu-eth/besu/security/advisories/GHSA-2vfg-f2fr-2jrv |

## Description (verbatim)

### Summary
IBFT 2.0 and QBFT derive the author of each consensus message, and of each signed entry embedded in one, with `SignedData.create(...)` → `Util.signatureToAddress(...)`. That returns `null` when the signature does not recover to a public key, which is the case for an ECDSA/secp256k1 signature whose `r` lies in `[1, n)` but is not a valid curve x-coordinate. The message decoder accepts such values.

The author is later checked with `validators.contains(author)`. With block-header (vote-based) validator selection the validator set is a natural-ordering `TreeSet`, whose `contains(null)` throws `NullPointerException`. This happens for:
- the author of the message itself, in the known-validator check;
- signed entries embedded in other messages: the prepares in a QBFT round change, the round changes in a QBFT proposal, and the round change certificate in an IBFT proposal. These entries are not covered by the outer message's signature, so a peer can insert one into an otherwise genuine validator message and relay it.

No validator key is required.

### Impact
Message handling catches the exception, so in most cases the crafted message is dropped and an error is logged.

- **IBFT 2.0:** messages for a future block height are buffered and replayed when that height starts. The replay had no per-message error handling, so a single crafted buffered message aborted it, and the genuine consensus messages buffered after it for that height were dropped. This can delay block production at that height until a round change.
- **QBFT:** no consensus impact was found. A crafted message is dropped and logged. A message carrying a crafted embedded entry is relayed to peers before it fails, so the error can be logged across the network.

There is no process crash, permanent or network-wide halt, chain fork, or fund impact.

### Affected configurations
- IBFT 2.0 networks.
- QBFT networks using block-header validator selection.
- QBFT networks using contract-based validator selection are not affected.

The consensus-level impact is limited to IBFT 2.0. QBFT, the more widely deployed of the two, is affected only with block-header validator selection, and only by dropped messages and error logging.

### Patches
`SignedData` now rejects a signature that does not recover to an address when the message is decoded, so a crafted message or embedded entry fails before it is validated or relayed. IBFT now handles errors per message when replaying buffered future-height messages, as QBFT already does.

### Workarounds
None at the protocol level. Restricting which peers may connect to validators (for example with node permissioning) reduces exposure.

## Patches and references

Fixed in Besu 26.11.0.

- Patch commit on `main`: https://github.com/besu-eth/besu/commit/4b87df824a9a004598f9c2f722259da96effe47a
- Release: https://github.com/besu-eth/besu/releases/tag/26.11.0

