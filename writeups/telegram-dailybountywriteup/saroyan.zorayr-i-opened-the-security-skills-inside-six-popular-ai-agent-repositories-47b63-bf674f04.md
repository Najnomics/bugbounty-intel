# Three security agent skills for three different jobs

- **Source URL:** https://medium.com/@saroyan.zorayr/i-opened-the-security-skills-inside-six-popular-ai-agent-repositories-47b6338857bd
- **Fetched from:** https://medium.com/@saroyan.zorayr/i-opened-the-security-skills-inside-six-popular-ai-agent-repositories-47b6338857bd?source=rss-2b5d67ca61a5------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14956 (id 14956)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** Saroyan Zorayr / Thu, 22 Oct 2026 09:30:22 GMT

*A task-fit shortlist for binary reversing, source-led bounty work, and authorized API testing. I read the linked SKILL.md files; I have not run or benchmarked them.*

A binary trace, a source-path hypothesis, and a two-account API test are different kinds of evidence. These are three agent skills I would inspect first because each gives a useful starting workflow for one of those jobs — not because repository stars prove quality.

[Read the skill file.](https://github.com/morluto/rea/blob/main/.agents/skills/reverse-engineer-anything/SKILL.md) **Use it when the artifact is the question:** a shipped binary, a patch, or a component whose installed behavior may differ from the source you have. The workflow can help follow call paths and record observations from that artifact.

For a parser investigation, I would pin the binary build, feed it a controlled input, and keep the hash, input, and trace together. A plausible decompilation is a lead; it is not recovered source code or proof of exploitability.

[Read the skill file.](https://github.com/affaan-m/ECC/blob/main/skills/security-bounty-hunter/SKILL.md) **Use it when you have source and need to test reachability:** can untrusted input reach a sensitive operation under realistic guards? This is closer to a bounty workflow than a generic list of code smells.

I would give it a pinned commit and a narrow hypothesis, then demand a small reproducer and the exact entry point. A missing check in one function is not yet a finding. Routing, assumptions, and impact still need independent confirmation.

[Read the skill file.](https://github.com/usestrix/strix/blob/main/skills/api-security-testing/SKILL.md) **Use it when a running API is the evidence source:** endpoints, roles, and object-level access are visible through controlled requests. It is a fit for an authorized test with an API schema and test identities.

For example, account A creates an object and account B attempts to retrieve it within the permitted scope. Keep both requests, responses, roles, and negative controls. A single successful request does not establish an authorization bug by itself.

**Selection rule:** match the skill to what you can observe. Pin the target, keep raw evidence, and mark unverified claims as unproven. I checked public skill descriptions and paths, not the safety of running their scripts or their false-positive rates.
