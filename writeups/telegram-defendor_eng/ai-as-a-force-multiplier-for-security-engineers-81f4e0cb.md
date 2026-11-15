# 🛡 AI Is Making Security Engineers More Effective, Not Replacing Them

- **Source URL:** https://sigmaprime.io/blog/ai-as-a-force-multiplier-for-security-engineers
- **Fetched:** 2026-11-15
- **Channel:** @defendor_eng
- **Telegram message:** https://t.me/defendor_eng/1742 (id 1742)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# The AI security debate has changed

Previously, the AI debate was: AI will replace security engineers vs AI is overhyped and cannot do serious security work. We've now had months to analyse the outputs and it's clear that AI can do serious security work. The debate has moved to: AI is just a supplementary tool for security reviewers vs will AI-only systems match or exceed the quality of expert engineers.

AI has found real issues, explained unfamiliar code, generated tests, traced dependencies, and accelerated large parts of the review process. But security is not a "mostly correct" discipline; in blockchain security, missing one critical bug can mean failure.

The conclusion we've reached for today is that it is not AI-only security, it is the combination that is most effective: human engineers using AI to increase speed, coverage, and depth while retaining responsibility for judgement, adversarial reasoning, and final conclusions.

AI has not replaced auditors, it has made strong auditors faster and more powerful.

# What AI is already great at

We've found AI is especially strong when the problem resembles something it has seen before or when the task involves navigating, summarising, comparing, or generating supporting material across a large codebase.

## Threat modelling and risk prioritisation

One of the use cases we have for AI is turning a large codebase into zones of high risk code and lower priority code.

We can ask it to highlight risky modules, suspicious code paths, privileged flows, external endpoints, trust boundaries, unusual state transitions, and areas where a protocol's assumptions are concentrated.

It can also help brainstorm attack vectors and compare the code against common vulnerability classes. This does not make the prioritisation automatically correct, but it gives us a faster way to decide where deeper review should begin.

## Known bug classes and pattern recognition

Many real-world bugs are variants of known issue classes. The exact percentage is difficult to measure; an internal sample of past reviews found that, on average, 80% of findings are repeat offenders. AI is well suited to these problems because it is strong at pattern recognition. It can help identify missing checks, inconsistent validation, unsafe assumptions, access control mistakes, accounting errors, suspicious state transitions, and other recurring vulnerability patterns.

We have always used simple searches to find suspicious areas of a codebase: `unsafe`, `panic`, unchecked indexing, ignored errors, unusual casts, unchecked arithmetic, signature replay risks, missing validation, weak error handling, privileged access checks, and other patterns that often appear near bugs.

With AI, we can make this workflow more powerful. It can speed up the raw search, trace how a value reached that point, identify whether the surrounding checks are sufficient, and help prioritise which matches are worth reviewing first. Where a match looks plausible, it can also help sketch a proof of concept test.

AI can help turn a broad pile of potentially interesting code into a priority list, with proof of concept tests and a draft of the impact, likelihood and resolution.

## Specification and differential analysis

We regularly use AI for differential analysis; it is useful when there are multiple descriptions or implementations of the same system.

For example, a protocol may have a specification written in English and an implementation written in Solidity. AI can compare the two and quickly highlight places where the code appears to diverge from the intended behaviour.

The same applies when there are multiple client implementations. If one client is written in Rust and another is written in Go, AI can compare the relevant logic across both codebases and look for discrepancies in validation rules, edge case handling, state transitions, or error conditions.

These differences are not automatically bugs. Sometimes one implementation is simply structured differently. But discrepancies are often where the most interesting questions begin, and AI can surface them much faster than a fully manual comparison.

## Codebase navigation

AI is extremely useful for understanding unfamiliar codebases.

It can summarise files, trace call paths, map dependencies, identify entry points, and help us build a mental model of the system.

This reduces ramp-up time and allows auditors to ask deeper questions earlier.

## Abstraction and hypothesis-driven review

One of AI's most important benefits is that it lets us operate at a higher level of abstraction.

Previously, if we had a potential issue in mind, we'd have to manually understand a large amount of surrounding implementation detail before we could test whether the issue was plausible.

We can start with a bug concept and ask AI to map that concept through the codebase. For example, if the concern is key collisions in a key value database, then we may not need to manually begin by tracing every key generation, hashing, and insertion path. We can describe the risk to the AI and have it identify where keys are constructed, where hashing occurs, where database writes happen, and where a collision could cause incorrect reads, overwritten values, or broken uniqueness assumptions.

The important point is that the engineer still pilots the investigation. AI does not replace the security intuition. It accelerates the exploration once we know what kind of problem to look for. The engineer supplies the hypothesis, AI does the grunt work.

## Report and code generation

AI is also strong at generating the material around a review: draft findings, unit tests, fuzzing harnesses, invariant ideas, proof of concept scaffolding, formal verification and remediation suggestions. This allows us to spend less time on mechanical work and more time on adversarial reasoning.

# What AI still struggles with

AI is strong at accelerating investigation, but it still struggles with the hardest and most important parts of security work.

## Novel business logic

AI can explain what code does, but security often requires understanding what the code should do. Many critical bugs are not violations of generic best practice, but rather violations of protocol-specific intent.

Injecting all protocol assumptions into an AI prompt is a non-trivial task. There is often an almost unbounded number of assumptions, many of which are general knowledge to humans but need to be loaded into context for AI.

## Multi-stage exploits

Serious exploits often require chaining multiple behaviours across a system. A single function may look safe in isolation. The vulnerability appears only when an attacker manipulates state across several steps, combines multiple features, or interacts with the protocol in an unexpected sequence.

## Architectural reasoning

Some vulnerabilities live above the function level. They involve trust assumptions, upgrade paths, permission models, oracle dependencies, cross-chain flows, governance processes, economic design, or protocol invariants. Understanding the full protocol and being able to abstract away the details of non-relevant components while still understanding enough to identify [protocol-level bugs](https://sigmaprime.io/services/blockchain-protocol-audit/) is a challenging task for humans and one AI has not yet fully grasped.

## Creative exploit chains

The hardest part of security is not asking whether a known bug exists.

It is imagining how the system can be made to behave in a way its designers did not expect. AI can assist this process, but experienced security engineers are still better at adversarial creativity, prioritisation, and exploit validation.

# Why blockchain is uniquely difficult

Blockchain security has unusually low tolerance for failure.

In many systems, bugs can be patched after discovery. In blockchain, a missed vulnerability can lead to immediate and irreversible loss of funds. This makes "80-90% coverage" a dangerous benchmark. In most contexts, finding 80-90% of bugs sounds excellent. In blockchain security, the missed 10% may be the only part that matters.

Blockchain systems are also public, adversarial, and highly composable. Attackers can inspect the code, simulate transactions, compose protocols, and exploit vulnerabilities quickly. This is why security remains the last 10% problem.

# AI also amplifies attackers

Defenders are not the only ones using AI; attackers can use AI to understand codebases faster, generate exploit hypotheses, automate reconnaissance, write scripts, and search for known vulnerability patterns. That means AI-only defence is not competing against AI-only attackers, it is competing against AI-assisted humans.

Attackers can run AI scans over numerous codebases and protocols to create a priority list of attack vectors. These potential issues can then be validated manually by the attacker and AI can craft the exploits. We have seen a significant increase in the number of security issues raised through bounties, hacks and security reviews in recent months. It is likely attributable to the cost and speed at which AI based techniques can run over numerous codebases to find the areas of code most likely to contain a vulnerability.

Attackers are AI + human; AI-only defence is strictly weaker.

The defensive answer is not to remove humans from the loop. It is to give expert humans better tools and better workflows.

# What next?

The frontier question is no longer whether AI can be wired into real security reviews. It is the trade-off between cost and quality.

There are three models to compare.

## AI-only

AI-only reviews are economically compelling. They can run in hours rather than weeks and can cost one or two orders of magnitude less than a traditional manual review.

That changes which reviews are economically viable and how much coverage teams can afford. But security is not a throughput benchmark. The quality is not yet where it needs to be for high stakes blockchain systems, where missing one critical issue can matter more than finding many low-severity ones.

AI-only scans have their place as a tool for developers to use in CI during the development process, before moving toward a code freeze and [full security audit](https://sigmaprime.io/services/smart-contract-audit/). Picking up bugs early is always a good thing, just as static analysers should be run, AI scans should be run too.

## AI-assisted security engineers

AI-assisted security engineers are the strongest model today.

The review workflow can be redesigned around AI.

- At the start of the review, AI can help map the codebase, summarise documentation, identify dependencies, inspect previous audits, and highlight likely attack surfaces.
- During the review, AI can help test hypotheses, trace bugs through the codebase, compare similar implementations, generate fuzzing ideas, and explore suspicious behaviours.
- At the end of the review, AI can help draft findings, generate regression tests, deduplicate issues, explain impact, and propose remediation options.

But the human engineer remains responsible for the parts that matter most: deciding what to investigate, understanding protocol intent, constructing realistic exploit paths, validating findings, and judging severity. The strongest teams will be those where engineers know how to pilot AI effectively.

In practice, this is already finding more bugs at a faster rate. AI increases search breadth, speeds up hypothesis testing, generates tests, traces code paths, and surfaces patterns that would be expensive to check manually. The human engineer filters the noise, understands protocol intent, and verifies the issues that matter.

This improves both cost and quality.

## Human-only

Human-only reviews can still be strong, especially when the work depends on protocol understanding, adversarial creativity, and judgement.

But it is slower and more expensive than AI-assisted review. In time-boxed reviews where there is not enough time for all security techniques to be executed (e.g. formal verification, invariant fuzzing and stress testing), it leaves useful coverage on the table.

Additionally, using multiple review techniques increases the chance of finding bugs. Manual review alone can miss issues, but combining manual review with static analysis improves coverage because either technique can surface a bug. Adding AI based techniques expands this further by allowing more hypotheses, code paths, and bug patterns to be checked within the same review window. For example, if a review uses manual analysis, static analysis, AI generated fuzzing, and AI assisted scans, only one of those techniques needs to identify a vulnerability for it to be caught. Since AI operates much faster than humans, it allows more techniques to be applied within the same time constraints.

## Summary

AI has become a standard part of serious security work. The question is how deeply teams can integrate AI while keeping it cost effective, and without introducing review gaps or reducing quality.

For lower-risk software, an AI-only review may be good enough. For blockchain security, where a single missed issue can have immediate and severe consequences, "cheaper and faster" is not the same thing as "strictly better". The strongest model is expert engineers piloting AI systems aggressively, while retaining responsibility for the final security judgement.

Teams that ignore it are falling behind. Teams that rely on AI alone will have gaps. The winning model is AI + experienced security engineer to increase speed, coverage, and depth, without outsourcing judgement and creativity.
