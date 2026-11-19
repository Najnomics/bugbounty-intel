# I Built an AI Smart Contract Auditor That Actually Works (Here’s the Proof)

- **Source URL:** https://medium.com/@dhillon.andrew/i-built-an-ai-smart-contract-auditor-that-actually-works-heres-the-proof-61918d2f70f1?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20251030044755/https://medium.com/@dhillon.andrew/i-built-an-ai-smart-contract-auditor-that-actually-works-heres-the-proof-61918d2f70f1
- **Fetched:** 2026-11-19
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/11643 (id 11643)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# I Built an AI Smart Contract Auditor That Actually Works (Here’s the Proof)

The real bounty isn’t finding bugs — it’s building a tool that can.

I spent the last 2 weeks building Aether, an open-source AI-powered smart contract auditing tool that combines static analysis, custom detectors, LLM reasoning, and automatic exploit generation. To test it, I pointed it at the Ethereum Name Service (ENS) contracts — a mature, heavily-audited codebase.

## **What it found**

1\. **Permissionless withdrawal pattern** in ETHRegistrarController (mainnet)

2\. **Missing nonce in signature validation** in L2ReverseRegistrar (L2s)

## **What it generated**

\- Working Foundry exploit PoCs for both findings

- Professional security reports with impact analysis

- Detailed submission-ready documentation

What happened when I submitted? Both got rejected — not because they were wrong, but because they were intentional design decisions by ENS.

That said, the tool did exactly what it should: **identified deviations from security best practices, correctly analyzed attack vectors, and generated working exploits**. The fact that ENS made conscious tradeoffs doesn’t invalidate the tool — it proves it works.

I now have a validated, production-ready security tool that can audit any protocol in \~2 hours. And you can use it too — it’s fully open-source!

## Why I Built This

Bug bounty hunting is a numbers game. You need to:

1. Find targets worth auditing (high payout, realistic chance)
2. Scan fast (competitors are everywhere)
3. Validate findings (most are false positives)
4. Prove exploitability (working PoC / mainnet fork required)

Manual auditing takes is super slow. I wanted something a lot faster.

## What Aether Does

It’s a full audit pipeline combining:

- Static analysis
- Custom detectors (60+ vulnerability patterns)
- LLM analysis (Claude/Gemini for semantic understanding)
- Validation system (filters false positives)
- Automatic PoC generation (Foundry tests with mainnet forking)

It doesn’t just find bugs. It **generates working exploit code** that compiles and runs.

Most security tools fall into two categories:

**Static analyzers (Slither, Mythril, etc.):**

- Fast, deterministic pattern matching
- High false positive rates
- No understanding of business logic
- Can’t generate exploits

**Manual audits:**

- Deep contextual understanding
- Can find complex logic bugs
- Slow (weeks per protocol)
- Expensive ($50k+ per audit)

**Aether combines both:**

- Fast (hours, not weeks)
- Semantic understanding (LLMs reason about code like humans)
- Generates working exploits (proves the bug is real)
- Open source and free (run it yourself)

The LLM layer is what makes this possible. It can:

- Understand contract purpose and context
- Trace complex execution paths
- Reason about attack vectors
- Generate natural language explanations
- Write working Solidity exploit code

Static analysis finds patterns. LLMs understand meaning. Together? **You get speed + accuracy.**

## **Links & Resources**

**Source Code:** [https://github.com/l33tdawg/aether](https://github.com/l33tdawg/aether)

**Twitter:** [https://twitter.com/l33tdawg](https://twitter.com/l33tdawg)

*To everyone building security tools — Share your work. Open-source it. Build in public. The security landscape is too big for any one person or company to secure.*

**PS** If you find a real bug (or another “interesting design decision”) using the tool, tag me :)
