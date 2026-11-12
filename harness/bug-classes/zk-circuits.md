# Zk Circuits

_Harness check spec. Every signal, payload and automation note below is drawn from the cited local files (full verbatim text under `posts/`, `writeups/`, `projects/`). Nothing here is invented; where a source only states a pattern, no concrete payload is asserted._


_Findings in corpus for this class: **9** (see `harness/findings.jsonl`)._

## Detection signals / takeaways from sources

- In Fiat-Shamir / IPP verifiers, every prover message used in a batched check must be bound into the transcript before challenges are derived. (from ma1fan). Source: [`posts/ma1fan/ARCHIVE.md`](../../posts/ma1fan/ARCHIVE.md), [`data/x_posts.jsonl`](../../data/x_posts.jsonl).
- ZK soundness bugs can become direct bridge theft; battle-test by actually producing a false proof. (from ChainLight_io). Source: [`posts/ChainLight_io/ARCHIVE.md`](../../posts/ChainLight_io/ARCHIVE.md), [`data/x_posts.jsonl`](../../data/x_posts.jsonl).
- When one zkVM has a Fiat-Shamir binding bug, audit every peer implementation for the same pattern. (from osec_io). Source: [`posts/osec_io/ARCHIVE.md`](../../posts/osec_io/ARCHIVE.md), [`data/x_posts.jsonl`](../../data/x_posts.jsonl).
- Publishing PoCs for ZK soundness bugs educates the ecosystem on exploitability beyond 'theoretical'. (from ChainLight_io). Source: [`posts/ChainLight_io/ARCHIVE.md`](../../posts/ChainLight_io/ARCHIVE.md), [`data/x_posts.jsonl`](../../data/x_posts.jsonl).
- Shielded/private ledgers inherit total failure from proof-system soundness bugs. (from osec_io). Source: [`posts/osec_io/ARCHIVE.md`](../../posts/osec_io/ARCHIVE.md), [`data/x_posts.jsonl`](../../data/x_posts.jsonl).

## Method / findings in sources

- **Range-proof soundness: a,b not bound in transcript before c derived (Agave)** — Verifier derives c then takes a and b from self.ipp_proof provided by prover. a and b were not explicitly bound in the transcript before c was derived for the final batched check. Malicious prover can simulate transcript to know c, then choose a,b (and craft IPP) to pass verification for a false statement. Original report by lonelysloth_sec; patch  Source: [`posts/ma1fan/ARCHIVE.md`](../../posts/ma1fan/ARCHIVE.md), [`data/x_posts.jsonl`](../../data/x_posts.jsonl).
- **zkSync Era ZK-circuit soundness bug — malicious prover could forge proofs and drain bridge (~$1.9B flowed after discover** — Critical bug in zkSync Era ZK circuits allowed a malicious prover to produce proofs for invalidly executed blocks that L1 verifier contracts would accept. Discovered 2023-09-15 by ChainLight; patched; first bounty claimed for a ZK-circuit bug on zkSync Era. PoC released after proving false proof with ~100 GPU-hours on A100s. Source: [`posts/ChainLight_io/ARCHIVE.md`](../../posts/ChainLight_io/ARCHIVE.md), [`data/x_posts.jsonl`](../../data/x_posts.jsonl).
- **Same Fiat-Shamir bug in six independent zkVMs — forge impossible statements** — Identical Fiat-Shamir transcript-binding bug across six zkVMs. Attacker can bypass cryptography and prove mathematically impossible statements (e.g. minting $1M out of thin air). Source: [`posts/osec_io/ARCHIVE.md`](../../posts/osec_io/ARCHIVE.md), [`data/x_posts.jsonl`](../../data/x_posts.jsonl).
- **zkSync Era write-query PoC — false proof → token theft (public release)** — Same ChainLight ZK-circuit bug; intentional false proof generation (~100 A100 GPU hours) turned soundness failure into full token-stealing exploit; public PoC released. Source: [`posts/ChainLight_io/ARCHIVE.md`](../../posts/ChainLight_io/ARCHIVE.md), [`data/x_posts.jsonl`](../../data/x_posts.jsonl).
- **dusk-plonk critical soundness bug — forge proofs, mint arbitrary DUSK** — Critical soundness bug in dusk-plonk let a malicious prover forge proofs for arbitrary false statements, minting arbitrary DUSK and bypassing shielded-tx checks. Source: [`posts/osec_io/ARCHIVE.md`](../../posts/osec_io/ARCHIVE.md), [`data/x_posts.jsonl`](../../data/x_posts.jsonl).
- **Missing copy constraint in halo2_gadgets variable-base scalar multiplication allows under-constrained base, breaking Orc** — A soundness vulnerability in the variable-base scalar multiplication gadget of `halo2_gadgets` allowed a malicious prover to produce a valid proof for an Orchard Action with an *under-constrained* base point. Because this gadget enforces the diversified-address-integrity condition of the Orchard Action statement, the flaw let a prover satisfy that  Source: [`projects/zcash/advisories/ghsa-ww9q-8r59-xv46.md`](../../projects/zcash/advisories/ghsa-ww9q-8r59-xv46.md).
- **argument-xyz-riscv-good-bad** — RISC-V ZKVMs: the Good and the Bad On this page The Ethereum Foundation recently announced a formal verification effort for RISC-V ZKVMs, in a landscape where these VMs are increasingly popular, with at least four companies currently developing one. After years of development of EVM-specific ZKVMs by Polygon, ZKSync, Scroll, and others, one might t Source: [`writeups/saxenism/argument-xyz-riscv-good-bad.md`](../../writeups/saxenism/argument-xyz-riscv-good-bad.md).
- **Orchard Action circuit soundness failure (under-constrained base in halo2_gadgets) enables counterfeiting within the Orc** — A critical soundness flaw in the `halo2_gadgets` variable-base scalar-multiplication gadget broke the soundness of the Orchard Action circuit, allowing a malicious prover to produce valid-looking Orchard proofs against an under-constrained base point. Exploitation could have permitted counterfeiting (minting) of funds within the Orchard shielded po Source: [`projects/zcash/advisories/ghsa-ghc3-g8w4-whf9.md`](../../projects/zcash/advisories/ghsa-ghc3-g8w4-whf9.md).
- **polygon-zkevm-node-pr-2048** — This repository was archived by the owner on Feb 17, 2025. It is now read-only. Source: [`writeups/0xiczc/polygon-zkevm-node-pr-2048.md`](../../writeups/0xiczc/polygon-zkevm-node-pr-2048.md).

## Automation (check spec)

```
# Checks derived from 9 documented finding(s) in findings.jsonl for class=zk-circuits
# note: In Fiat-Shamir / IPP verifiers, every prover message used in a batched check must be bound into the transcript before challenges are derived.
# note: ZK soundness bugs can become direct bridge theft; battle-test by actually producing a false proof.
# note: When one zkVM has a Fiat-Shamir binding bug, audit every peer implementation for the same pattern.
# note: Publishing PoCs for ZK soundness bugs educates the ecosystem on exploitability beyond 'theoretical'.
# note: Shielded/private ledgers inherit total failure from proof-system soundness bugs.
```

## Prior harness notes (retained)

_Retained from earlier curated harness file; still cites local sources._

## Detection signals
- Circuit signals that are not fully constrained (missing range checks, missing equality/boolean constraints), letting a prover forge a valid proof for a false statement.
- Verifier logic that accepts malformed or replayed proofs.

## Method seen in sources
- Read circuits line by line AND read verifiers; loss-of-TVL bugs live in both. Source: techniques.md (LonelySloth) and [`researchers/zksecurityXYZ.md`](../../researchers/zksecurityXYZ.md), [`researchers/ChainLight_io.md`](../../researchers/ChainLight_io.md).
- zkEVM node/bridge logic (not the circuit) can also break soundness-adjacent invariants: Polygon zkEVM free-claim branch bug. Source: [`posts/0xiczc/2023-05-26-1662090451493740545.md`](../../posts/0xiczc/2023-05-26-1662090451493740545.md).
- Reference: 0xPARC zk-bug-tracker (not fetched — see sources-log).

## Automation (check spec)
```
for signal in circuit_signals:
  if not fully_constrained(signal): FLAG under-constrained
enumerate verifier branches for free/reverted/replayed proof handling
```

## Added 2026-11-12 — gnark fake-GLV / emulated scalar mul (zkSecurity Zolana #00)

Range-check hinted subscalars to the bit-width the elliptic-curve relation actually consumes. Checking the scalar-field relation on full 256-bit values while only using the low 128 bits in the EC relation lets a malicious prover forge ECDSA acceptance (P-256-owned UTXO spend in Solana Privacy Rings CustomRingP256Circuit). Also review gnark GHSA-7fx8-hmgc-82jp / GHSA-4g5f-3gmm-9q87.
Sources: writeups/zksecurityXYZ/solana-privacy-rings-zolana-audit-2026-08.md, projects/crypto/advisories/gnark-*.md
