# 🛡️ Artificial Intelligence is Changing Vulnerability Hunting in Web3

- **Source URL:** https://kritt.ai/technical-review
- **Fetched:** 2026-11-16
- **Channel:** @defendor_eng
- **Telegram message:** https://t.me/defendor_eng/1145 (id 1145)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
Technical Retrospective

# Building Agentic Infrastructure for Zero-Day Vulnerability Research

**TL;DR: We built an agentic AI system that scans real-world codebases and surfaces verified, exploitable, High/Critical zero-day vulnerabilities.**

Vulnerability research today is slow, manual, and hard to scale. Each finding depends on expert intuition, long feedback loops, and hours of trial and error-so output is fundamentally capped by human time and skill.

But what if it wasn't? What if an AI could read code faster than any human, reason about execution paths, and discard non-exploitable noise-at scale? That's what we set out to build. And spoilers, it works.

We built an agentic, multi-step system that mirrors how experienced security researchers think:

1. Identify suspicious behavior or invariant violations
2. Prove reachability (call paths, entrypoints, conditions)
3. Prove controllability (attacker influence on relevant state/data)
4. Determine real-world impact (theft, DoS, privilege escalation, etc.)

The result isn't noisy AI output, but high-confidence vulnerabilities that survive manual review and real exploitation attempts.

This is a technical retrospective: what worked, what didn't, and the engineering principles that mattered most.

## Results so far

We battle-tested the system on [Immunefi](https://immunefi.com) (the largest blockchain bounty platform), [HackenProof](https://hackenproof.com), [Hackerone](https://hackerone.com) (the largest bounty platform in general), and private bug bounty programs. We responsibly disclosed **10+ bugs** in major blockchain projects.

### Highlights

- •The largest finding could have enabled **\~$500M in theft** and was awarded **$250k**. (To our knowledge: the largest AI-assisted vulnerability disclosure reported to date.) [See tweet](https://x.com/immunefi/status/2005957436612448405) 
- •One vulnerability could have crashed projects built with Cosmos, potentially impacting many downstream chains and apps.
- •Our user is ranked **#1 on Immunefi** for the last 90 days (#18 all-time, and climbing fast). [View leaderboard](https://immunefi.com/profile/Blockian/?scope=last90Days) 

## Why vulnerability research is hard (and why agents help)

Real vulnerability research is not a one-shot classification task. It's **long-form reasoning with compounding error**: every step depends on earlier assumptions that might be incomplete, subtly wrong, or context-dependent.

A typical chain looks like:

1. 1.Identify suspicious behavior or invariant mismatch
2. 2.Prove reachability (call paths, entrypoints, conditions)
3. 3.Prove controllability (attacker influence on relevant state/data)
4. 4.Determine impact (theft, DoS, invariant break, privilege escalation)
5. 5.Demonstrate (PoC, simulation, repro, minimized conditions)
6. 6.Explain clearly (reporting, remediation guidance)

If any link is weak, the whole conclusion collapses.

This is exactly the failure mode E literature calls out: "intuitive" reasoning can be locally plausible but globally fragile, and precision decays as chains get longer. The reasoning framing ([arXiv:2412.02441](https://arxiv.org/abs/2412.02441)) is basically a formal version of what every security researcher learns the hard way: you need checkpoints that force correctness, not just more tokens.

## The big unlock: harnesses beat vibes

Progress didn't come from clever prompts. It came from **harnesses**.

A harness is the set of constraints, scaffolding, and checks that forces an agent to:

- •generate hypotheses explicitly (not implicitly)
- •collect evidence before escalating confidence
- •use deterministic tools when possible
- •fail fast and prune dead ends
- •produce artifacts a reviewer can trust

If you want systems that resemble an expert rather than "confident autocomplete," harnesses are the bridge: they turn model skill into expert-like reliability.

## Tooling: cyber work isn't "just coding," and the toolset matters

We learned quickly that "coding agent tools" and "cyber tools" overlap, but they're not the same category.

#### For coding, the best tools optimize for:

- • editing/applying patches
- • running tests
- • refactoring and shipping

#### For cyber, the best tools optimize for:

- • tracing deterministic flows across trust boundaries (e.g., CodeQL)
- • proving reachability + controllability
- • reasoning about invariants and adversarial input
- • validating exploitability

One pattern showed up consistently in our benchmarks and day-to-day iteration:

The best results came when we paired SOTA models with their native toolchains-then augmented them with our own extended cyber toolset.

Concretely:

- •**GPT** → Codex tooling (and we specifically found gpt-5.2-codex outperformed the more general gpt-5.2 for this workload)
- •**Opus** → claude-code
- •**Gemini** → gemini-cli
- •Plus our extended toolset, including cyber-specific tools like CodeQL

This isn't cosmetic. Native toolchains tend to align with the model's learned operating style (how it searches, edits, executes, and recovers). Adding cyber-native determinism on top turns that into something you can actually trust under audit pressure.

## CodeQL as "determinism injection" into long reasoning

One principle became non-negotiable:

Make as much as possible deterministic, and reserve model reasoning for what can't be deterministic.

In vulnerability research, many painful "reasoning" sub-questions become straightforward when you can query semantics:

- "Does taint from this input reach that sink?"
- "Which call paths lead here?"
- "Where is this state mutated, and under what guards?"
- "Are there patterns of missing auth checks / unchecked returns / unsafe casts?"

When CodeQL answers a slice of the problem reliably, the agent doesn't need to "think harder"-it needs to query correctly, then move on with higher confidence and fewer compounding mistakes.

## Test-time compute is not just for math - it's for "search-and-proof"

A major pattern we observed is that our system behaves less like a scanner and more like a **search-and-proof engine**:

- •explore hypotheses (breadth)
- •deepen promising lines (depth)
- •verify aggressively (proof)
- •produce repro artifacts (trust)

This maps cleanly onto the broader trend of scaling test-time compute: performance increases not only from bigger pretrained models, but from allocating more inference-time work to hard instances.

Two references are especially relevant:

- •DeepMind's analysis that compute-optimal test-time scaling can outperform simply scaling model size ([arXiv:2408.03314](https://arxiv.org/abs/2408.03314)).
- •Hugging Face H4's very practical walkthrough of implementing these ideas with open models, including verifier-guided search and tree-search variants.

We apply the same principle in cyber:

- •Not every signal deserves the same spend.
- •Some repos/components need shallow triage; others need deep multi-tool investigation.
- •The system improves when it allocates compute adaptively based on "difficulty" and "promise," instead of treating all code equally.

## Model selection: SOTA-first, not weak-to-strong

One of the biggest "we changed our mind" outcomes:

We are not using smaller models for first-pass generation.

In our internal benchmarks, the best results came from SOTA frontier models-currently:

- • opus 4.5
- • gpt-5.2

They outperformed open-source models in our workload even after we fine-tuned the open-source options.

We also found that **gpt-5.2-codex** (the Codex-oriented variant) performs better for agentic vulnerability research than the more generalist gpt-5.2, especially once you factor in tool use, code navigation behaviors, and the ability to stay consistent across long verification loops.

## Bridging the gap where SCA doesn't deliver (without discarding it)

We still use deterministic scanners and dependency tooling (SCA), but we don't treat them as a complete solution.

In practice, SCA struggles whenever at least one critical part is too contextual to match deterministically:

- •allocation + lifetime complexity
- •multi-step flows that don't match a clean signature
- •boundary interactions where the "pattern" is contextual
- •emergent behavior across modules/contracts

What we're building is a bridge: cover the non-deterministic gaps with agentic reasoning, while keeping everything else as deterministic and verifiable as possible.

## We built our own benchmark (because "looks right" is not a metric)

Security eval is unusually easy to get wrong:

- •false positives can look convincing
- •"interesting" findings can be non-exploitable
- •small environment differences can invalidate a PoC

So we built a benchmark that emphasizes what matters in practice:

- • evidence quality
- • reachability proof
- • exploitability/impact demonstration
- • reproducibility

## Mimicking an experienced auditor, end-to-end

We didn't design the pipeline around what's convenient for an agent. We designed it around what good auditors actually do:

This "auditor-shaped" workflow is how you turn raw model capability into something closer to an expert: domain expertise + precision + disciplined proof.

## Why this works especially well in cyber: verification is built in

Cyber is unusually friendly to agentic systems because so much is **verifiable**:

- "Run the simulation."
- "Execute the PoC."
- "Do we steal money / break invariants / crash the system?"

That verification loop keeps the system grounded. It also makes it easier to reward correctness instead of persuasion-arguably the core requirement if you're aiming for Expert-grade AI rather than just fluent output.

## The "money in, vuln out" machine (a.k.a. the vuln slot machine)

One slightly scary way to describe what we built is a **"money in, vuln out" machine**: the more tokens/compute you feed it, the more verified vulnerabilities it tends to surface. It's not linear forever, and it has diminishing returns, but the direction is real - especially once you have strong harnesses + deterministic verification gates.

The uncomfortable implication is economic: attackers are often rewarded more per vuln than defenders are willing to spend preventing one, so if a blackhat (or a well-funded adversary) had an equivalent machine, they can justify running it harder, longer, and across more targets. That's why we treat this work as fundamentally defensive: scaling verification and responsible disclosure isn't just a productivity win - it's a necessary counterweight in a world where capability increasingly maps to "compute budget × automation."

## Closing

kritt.ai's goal is not to produce more "findings." It's to produce **verified, high-signal vulnerabilities**-the kind a skeptical auditor would sign off on-at a scale that matches modern codebases.

### The core lessons:

- •Long-form vulnerability research needs decomposition into verifiable steps.
- •Harnesses are the difference between occasional brilliance and repeatable output.
- •Cyber tooling (CodeQL, simulation) is essential "determinism injection."
- •Compute scales discovery, so you must allocate it compute-optimally and adaptively.
- •SOTA-first model selection + native toolchains (plus cyber-specific extensions) beat weak-to-strong pipelines for this workload, per our benchmarks.

## References

Thanks to [@Kritt\_AI](https://x.com/Kritt_AI) for helping with architecture ideas for this project.
