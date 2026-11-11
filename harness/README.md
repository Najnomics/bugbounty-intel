# harness/ — material for a hunting-harness-building agent

This folder turns the knowledge base into material an agent can act on to improve an automated bug-hunting pipeline. It is built **only** from the sources captured in this repo (full verbatim text under [`../posts/`](../posts/) and [`../writeups/`](../writeups/)). Nothing here is invented; every item cites the local file it came from.

## Contents

| Path | What it is |
| --- | --- |
| [recon-methodology.md](recon-methodology.md) | Merged recon workflow. The backbone is Marius du Preez's full phased prompt pack ([`../writeups/mdp_sec/prompts/`](../writeups/mdp_sec/prompts/)), plus cross-researcher recon notes. |
| [bug-classes/](bug-classes/) | One file per bug class: detection signals, recon steps, exact payloads/requests seen in the sources, tools, and an automation (check-spec) block. Each item cites the local post/writeup it came from. |
| [findings.jsonl](findings.jsonl) | Machine-readable, one JSON object per documented finding: `researcher`, `platform`, `bug_class`, `target_type`, `root_cause`, `discovery_method`, `payload`, `bounty`, `source_files`, `post_url`, `profile`. |

## Bug-class files

`auth-bypass`, `blockchain-client`, `crypto-primitives`, `idor-bola`, `sqli`, `ssrf`, `xss`, `request-smuggling`, `cache-poisoning`, `path-normalization`, `dependency-confusion`, `oauth`, `mobile-content-providers`, `smart-contract` (access control, rounding, reentrancy, oracle, signature replay), `zk-circuits` (under-constrained/soundness), `tee-attestation`.

## How to use it

1. Start with `recon-methodology.md` to shape the pipeline's phase order. The single richest source is the verbatim prompt pack under `../writeups/mdp_sec/prompts/` (an 11-phase recon→sweep→triage→validate→gate workflow with real tool invocations).
2. For each vulnerability check, open the matching `bug-classes/<class>.md` for the detection signal, the exact payload/request pattern observed, and a pseudo-code check spec to automate.
3. Load `findings.jsonl` as labelled examples (map target_type + bug_class → discovery_method + payload) and follow `source_files` back to the full verbatim report for context.

## Protocol / crypto advisories

- [`projects/zcash/`](../projects/zcash/) — 76 GHSA (zcashd, zebra, lightwalletd, frost)
- [`projects/ethereum/`](../projects/ethereum/) — 34 GHSA + 67 Solidity compiler bugs
- [`projects/solana/`](../projects/solana/) — OSV/RustSec (rBPF, Anchor, SPL)
- [`projects/crypto/`](../projects/crypto/) — 76 RustSec crypto advisories + 0xPARC ZK bug tracker

## Important caveats (so the harness doesn't over-trust this)

- Marius du Preez explicitly **demotes** systematic SQLi/NoSQLi/command/CSV parameter fuzzing (zero confirmed origins over his last 100 reports / ~107h). Prioritise access control, auth, business logic, and server-side execution. Source: `../writeups/mdp_sec/prompts/phases/phase-02-sweep.md`.
- `findings.jsonl` covers the **analysed** findings in this repo (those with a written root-cause analysis). The raw corpus of ~380 captured posts across researchers (and 422 of Marius's own posts) under `../posts/` is larger; use it for breadth.
- Payloads are only filled where a source states them; otherwise the field is `null`.
- Run only against authorised, in-scope targets, with bounded non-destructive proofs (the sources stress this repeatedly).
