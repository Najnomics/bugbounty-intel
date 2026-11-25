# Unauthenticated pol_round in arc-node

- **Source URL:** https://medium.com/@mgsa112233/unauthenticated-pol-round-in-arc-node-from-hash-preimage-omission-to-state-divergence-387560f71493
- **Fetched from:** https://medium.com/@mgsa112233/unauthenticated-pol-round-in-arc-node-from-hash-preimage-omission-to-state-divergence-387560f71493?source=rss-de788fc65c12------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14931 (id 14931)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** jimmy / Fri, 02 Oct 2026 18:45:26 GMT

During a security review of **arc-node** (commit 2a3e8ab), I identified a critical integrity gap in the block dissemination and proposal validation logic. Specifically, the consensus proposal parts are signed over a hash that omits the pol\_round field carried in the proposal Init.

While this report was ultimately closed as a duplicate of an existing internal/external finding (#4034183), the vulnerability provides a fascinating study in consensus state-machine safety, signature malleability, and cryptographic omission bugs.

In distributed consensus engines like Malachite/Arc, ensuring that proposal components cannot be tampered with in transit is paramount. However, a breakdown occurs across three core components:

Looking at crates/types/src/proposal\_parts.rs, the hash function computes the Keccak-256 hash using only the height, round, and data bytes:

Notice that pol\_round is completely absent from this hash input.

In crates/malachite-app/src/proposal\_parts.rs, the validation function fetches hash = parts.hash() and checks the proposer's Ed25519 signature strictly against that incomplete hash. Because pol\_round is excluded from the hash, modifying it does not invalidate the signature.

Once the tampered parts pass signature verification, assemble\_block\_from\_parts() directly sets:

An attacker-controlled value is thus successfully injected into the node’s consensus state as the valid round.

In Malachite’s core state machine (state\_machine.rs), the prevote\_previous function evaluates the voting guard:

To demonstrate this signature malleability without needing a live network, I wrote a Python PoC using the cryptography library. It shows that a valid Ed25519 signature over ProposalParts::hash() remains valid even when pol\_round is modified from 0 to 5.

You can check out the full code and output files on GitHub:

👉 [https://github.com/Mohammed23200/consensus-signature-coverage-poc](https://github.com/Mohammed23200/consensus-signature-coverage-poc)

Python

\# Excerpt from pol\_round\_malleability.py

def proposal\_parts\_hash(height\_u64, round\_i64, data\_parts):

msg = bytearray()

msg.extend(height\_u64.to\_bytes(8, 'big'))

msg.extend(round\_i64.to\_bytes(8, 'big', signed=True))

for part in data\_parts:

msg.extend(part)

return keccak\_256(bytes(msg))

PoC Output (poc\_output.txt):

Plaintext

============================================================

PoC: pol\_round malleability in arc-node ProposalParts

Ref: github.com/circlefin/arc-node commit 2a3e8ab

============================================================

BEFORE pol\_round=0, AFTER pol\_round=5, SIGNATURE VALID: True

HASH(height, round, data) unchanged: True

Conclusion: pol\_round can be changed freely without

invalidating the proposer signature.

This becomes ConsensusBlock.valid\_round via:

assemble\_block\_from\_parts() line 279

Cryptographic bindings in consensus layer protocols must cover *all* mutable state fields that influence state machine transitions. Omitting fields like pol\_round from proposal hashes opens up powerful relay-based state-manipulation vectors.

*Thank you to the security team at Circle for handling the report.*
