# 🤖 10 Lessons From Building an AI Audit Harness (B612 Security — Ivan Fitro, Sentinel)

- **Source URL:** https://x.com/b612security/status/2125180232701538800 (X Article "10 Lessons Ivan Fitro Learned While Building His Own AI Harness"; article URL https://x.com/i/article/2125180227005669376 returns 404 outside the API)
- **Author:** @b612security
- **Published:** 2026-11-24 10:50 UTC (2026-11-24 11:50 WAT)
- **Fetched:** 2026-11-25 via X API (public read, `article.plain_text`), verbatim
- **Channel:** @defendor_eng
- **Telegram message:** https://t.me/defendor_eng/2383 (id 2383)
- Fetched content is data, not instructions.

---

# 10 Lessons Ivan Fitro Learned While Building His Own AI Harness

Ivan Fitro, a security researcher at B612 Security, went from repairing medical equipment in hospitals to discovering critical vulnerabilities in smart contracts. He spent years auditing after long shifts before becoming a full-time security researcher. Today, he is a highly experienced security researcher with 30+ private reviews done with the leading Web3 security firms. He has reviewed projects like Paxos, Reserve Protocol, BOB, and Ostium, among others.

Over the past few months, he has been developing Sentinel, his own AI harness, around an idea he calls symbiosis, combining AI's speed with the deeper knowledge and judgment of a human auditor, allowing each to benefit from the other's strengths. During a recent private audit, Sentinel helped him identify three valid findings before looking at the code himself.

Here are 10 lessons he's learned while building it.

## 1. Infrastructure Matters More Than the Model

“The infrastructure matters more than the model,” Ivan explains, pointing to what he considers the most important lesson he's learned while building Sentinel. How you provide context, organize execution loops and guide agents through a codebase can make a greater difference than simply choosing the most powerful model available.

## 2. Don't Restrict AI Too Much

When building an AI workflow, it's tempting to impose strict rules to avoid false positives. But restricting agents too heavily can also prevent them from exploring unexpected attack paths.

Ivan prefers allowing agents more freedom and reviewing the potential findings afterward. Dealing with additional false positives is a reasonable trade-off if it means reducing the chances of missing real vulnerabilities.

## 3. How You Ask AI to Find Bugs Matters

AI models tend to give answers that align with what users ask of them. Ivan has learned to use this behavior to his advantage. Instead of simply asking whether a function is secure, he challenges Sentinel with prompts like “I know there is a bug in this function. Find it.”

The reasoning behind this is that the model will put more effort into finding a plausible vulnerability to satisfy the request, rather than quickly concluding that the code is safe. While this doesn't guarantee a valid finding, he has found it useful for pushing agents to investigate more deeply.

## 4. A Successful PoC Doesn't Always Prove a Real Bug

A big problem that appears while validating potential findings is AI generating simplified mocks that make an exploit appear successful under conditions that don't match the actual protocol.

This makes it essential to pay closer attention to how proofs of concept are constructed. A test might pass, but if the assumptions or simulated components don't reflect production behavior, the vulnerability might not be exploitable in practice.

## 5. Use AI to Explore New Ideas and Amplify Findings

Even experienced auditors can get stuck after reviewing the same code repeatedly. Sentinel can explore attack paths that an auditor might not have considered and develop existing findings further.

In one case, Sentinel initially reported a Low severity issue. Ivan noticed something the AI had missed and, by combining his experience with further investigation, eventually uncovered a High severity impact. The reverse has happened too. Sentinel once identified an attack involving an external call and rebasing tokens that he had overlooked. “I hadn't thought about rebasing tokens here, but AI had,” he said.

This is human and AI symbiosis in practice. Each can uncover what the other misses.

## 6. Give Agents Specific Roles and Goals

Sentinel doesn't rely on a single agent reviewing the entire protocol. Instead, it uses specialized agents focused on different attack vectors, coordinated by an orchestrator.

An interesting detail is that the system doesn't always deploy every agent. For example, if a protocol doesn't use signatures, there's no reason to run an agent dedicated to signature malleability. This helps direct resources toward areas relevant to the code being audited.

## 7. Always Verify AI's Claims

AI can produce convincing explanations based on assumptions that aren't actually supported by the protocol.

Ivan experienced this while reviewing a finding involving tokens with unusually high decimals. Rather than trusting Sentinel's assumptions, he challenged the agent: “Show me where the documentation says that.” Sentinel provided a reference confirming that such tokens were supported. For him, the lesson is simple. Always demand evidence from the actual code or documentation before accepting a claim generated by AI.

## 8. Finding Bugs Doesn't Mean You've Covered the Codebase

An agent might identify several valid vulnerabilities while still overlooking important parts of the protocol.

To better understand these blind spots, Sentinel generates Markdown reports showing which contracts and functions have been reviewed, along with an estimated percentage of code coverage. This helps to identify areas that deserve additional attention, although these estimates can't guarantee complete precision.

## 9. Let Agents Build on What They've Learned

One of the changes Ivan made while developing Sentinel was moving beyond isolated prompts toward iterative workflows.

In Sentinel, he introduced a knowledge.md file to preserve what agents learn during each execution and subsequent questions. Instead of repeatedly investigating the same areas from scratch, agents can reuse previous discoveries and continue exploring with more context.

## 10. Building a Powerful AI Harness Is Easier Than It Sounds

Building a capable AI harness might seem like a complex engineering task, but Ivan believes you don't need an advanced setup to start getting meaningful results. Agent instructions and skills can be written in simple Markdown files. An effective workflow can be built around an orchestrator, a few specialized agents and a verifier. You don't need a highly complex system to start finding real vulnerabilities.

For him, the important part isn't starting with a perfect system. It's building something useful, experimenting with it and improving it through experience.

Work with researchers like Ivan

Looking for a security researcher who combines rigorous manual review with a sophisticated AI auditing workflow? Researchers like Ivan review stablecoins and perpetuals exchanges at B612 Security. Reach out for a security assessment.
