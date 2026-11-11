# harness/ — material for a hunting-harness-building agent

This folder turns the knowledge base into material an agent can act on to improve an automated bug-hunting pipeline. It is built **only** from the sources captured in this repo (full verbatim text under [`../posts/`](../posts/), [`../writeups/`](../writeups/), [`../projects/`](../projects/)). Nothing here is invented; every item cites the local file it came from.

## Contents

| Path | What it is |
| --- | --- |
| [recon-methodology.md](recon-methodology.md) | Merged recon workflow. Backbone: Marius du Preez's phased prompt pack ([`../writeups/mdp_sec/prompts/`](../writeups/mdp_sec/prompts/)), plus cross-researcher recon notes. |
| [bug-classes/](bug-classes/) | One file per bug class: detection signals, recon steps, exact payloads/requests seen in the sources, tools, and an automation (check-spec) block. Each item cites the local post/writeup/advisory it came from. **36 class files.** |
| [payloads/](payloads/) | Deduped payload / request lists per class, extracted verbatim from findings. |
| [tools.md](tools.md) | Every tool mentioned across findings and posts, with how researchers used it (cited). |
| [findings.jsonl](findings.jsonl) | Machine-readable, **399** JSON objects (one per documented finding): `researcher`, `platform`, `bug_class`, `target_type`, `root_cause`, `discovery_method`, `payload`, `bounty`, `source_files`, `post_url`, `profile`. |

## Bug-class files

`auth-bypass`, `blockchain-client`, `business-logic`, `cache-poisoning`, `cloud-s3`, `consensus-dos`, `cors`, `cross-chain-bridge`, `crypto-primitives`, `csrf`, `dependency-confusion`, `deserialization`, `file-upload`, `governance`, `graphql`, `idor-bola`, `jwt`, `llm-prompt-injection`, `mev`, `mobile`, `mobile-content-providers`, `oauth`, `path-normalization`, `prototype-pollution`, `race-condition`, `request-smuggling`, `smart-contract`, `sqli`, `ssrf`, `ssti`, `subdomain-takeover`, `tee-attestation`, `web`, `xss`, `xxe`, `zk-circuits`.

## How to use it

1. Start with `recon-methodology.md` to shape the pipeline's phase order. The single richest source is the verbatim prompt pack under `../writeups/mdp_sec/prompts/` (an 11-phase recon→sweep→triage→validate→gate workflow with real tool invocations).
2. For each vulnerability check, open the matching `bug-classes/<class>.md` for the detection signal, the exact payload/request pattern observed, and a pseudo-code check spec to automate. Cross-check `payloads/<class>.md`.
3. Load `findings.jsonl` as labelled examples (map target_type + bug_class → discovery_method + payload) and follow `source_files` back to the full verbatim report for context.
4. Use `tools.md` to decide which scanners/plugins the harness should shell out to.

## Protocol / crypto advisories (also mined into findings.jsonl)

- [`projects/zcash/`](../projects/zcash/) — GHSA (zcashd, zebra, lightwalletd, frost)
- [`projects/ethereum/`](../projects/ethereum/) — GHSA + Solidity compiler bugs
- [`projects/solana/`](../projects/solana/) — OSV/RustSec (rBPF, Anchor, SPL)
- [`projects/crypto/`](../projects/crypto/) — RustSec crypto advisories + 0xPARC ZK bug tracker

## Important caveats (so the harness doesn't over-trust this)

- Marius du Preez explicitly **demotes** systematic SQLi/NoSQLi/command/CSV parameter fuzzing (zero confirmed origins over his last 100 reports / ~107h). Prioritise access control, auth, business logic, and server-side execution. Source: `../writeups/mdp_sec/prompts/phases/phase-02-sweep.md`.
- `findings.jsonl` covers **mined** findings (posts with concrete root-cause writeups, local writeups, and project advisories). The raw corpus under `../posts/` and `../data/x_posts.jsonl` is larger (~13k posts); use it for breadth when a class file is thin.
- Payloads are only filled where a source states them; otherwise the field is `null`.
- Run only against authorised, in-scope targets, with bounded non-destructive proofs (the sources stress this repeatedly).

_Last harness mine note: findings.jsonl grew to 399 records; payloads/ and tools.md generated from the same mine. Corpus posts remain the source of truth._
