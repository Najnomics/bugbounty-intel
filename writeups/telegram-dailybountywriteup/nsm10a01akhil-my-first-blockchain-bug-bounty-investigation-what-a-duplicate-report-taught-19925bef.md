# My First Blockchain Bug Bounty Investigation

- **Source URL:** https://medium.com/@nsm10a01akhil/my-first-blockchain-bug-bounty-investigation-what-a-duplicate-report-taught-me-about-security-20065a0e7ae0
- **Fetched from:** https://medium.com/@nsm10a01akhil/my-first-blockchain-bug-bounty-investigation-what-a-duplicate-report-taught-me-about-security-20065a0e7ae0?source=rss-2f46eb55db88------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14948 (id 14948)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** Ak-4!7 / Wed, 14 Oct 2026 21:11:55 GMT

*An honest account of exploring a Rust codebase, investigating an Engine API validation hypothesis, testing locally, and learning that finding a vulnerability is only half the battle.*

When I started exploring bug bounty hunting, I thought the process was relatively straightforward: find suspicious code, investigate it, reproduce the issue, and submit a report.

My recent experience investigating the ar\*-\*\*de repository challenged that assumption.

I explored a blockchain node implementation, investigated address-denylist enforcement, traced execution paths, ran automated tests, and built a local proof of concept with AI assistance.

Eventually, I submitted a report to Hac\*\*\*One.

The result?

**My report was marked as a duplicate of an existing finding.**

Although this was disappointing, the experience taught me important lessons about source-code analysis, proof-of-concept testing, vulnerability validation, and the responsible use of AI in security research.

This is the story of that investigation and what I learned from it.

I began working with the Circle ar\*-\*ode repository in an Ubuntu environment running through Windows Subsystem for Linux (WSL).

As someone still learning bug bounty hunting, navigating a large Rust codebase was challenging.

I needed to understand how different components interacted, where security checks were implemented, and whether those checks were consistently enforced across different execution paths.

Instead of immediately searching for a vulnerability, I started examining the code responsible for address-denylist enforcement.

The relevant components included:

Each component played a different role in validation, configuration, transaction processing, execution, or testing.

This taught me an important lesson: understanding a vulnerability often requires following the flow of data across multiple components rather than examining one function in isolation.

The central question behind my investigation was:

**Could a transaction targeting a denylisted address be accepted through the Engine API even though transaction-pool validation checks denylisted addresses?**

To investigate this, I examined the denylist implementation and its use during transaction validation.

I found that transaction-pool validation called is\_denylisted() and checked relevant transaction addresses, including the sender and recipient. The implementation also handled EIP-7702 authorization authorities.

I then explored the EVM execution path and the Engine API validation logic.

One function I examined was:

execute\_transaction\_without\_commit()

In the code path I inspected, the function checked the remaining block gas before executing a transaction through:

self.evm.transact(tx\_env)

I did not find an equivalent denylist check directly in that function.

This raised a potential enforcement gap worth investigating.

However, there is an important distinction between identifying a suspicious code path and proving a vulnerability. A check that is absent from one function might be enforced elsewhere, so the entire execution path must be understood before drawing conclusions.

That became the next step in my investigation.

Rather than relying exclusively on static code analysis, I examined the repository’s end-to-end tests.

I used Cargo, Rust’s build system and package manager, to list and run the relevant tests.

For example:

cargo test -p arc-execution-e2e --test e2e -- --list

This command listed the available tests in the selected test target.

I then ran the denylist-related tests:

cargo test -p arc-execution-e2e --test e2e denylist -- --nocapture

And:

cargo test -p arc-execution-e2e --test e2e eip7708\_denylist -- --nocapture

The relevant existing tests passed.

These results helped establish that the existing test cases behaved as expected. They did not prove that every possible transaction-processing path enforced the denylist.

That distinction is essential in security testing.

**A passing test proves that a particular test passed under its tested conditions. It does not prove that the entire system is secure.**

The next step was to investigate the suspected behavior in a controlled local environment.

With AI assistance, I worked on an end-to-end test involving a producer node and a validator node.

The test examined whether a transaction targeting a denylisted address could be included in an execution payload produced by one node and subsequently accepted through another node’s Engine API.

The general testing process involved:

During this process, I encountered a problem with the initial test recipient. It corresponded to a test-only panic precompile, and the payload-building process evicted the transaction.

I changed the recipient to a normal address and reran the test.

The modified test passed in the local environment.

This provided evidence about the behavior of the specific configuration and execution path being tested.

However, it was not proof that a live network was vulnerable. The result depended on the test setup, and the security implications still needed to be evaluated carefully.

I also want to be transparent about my process: **AI assisted me with the investigation and test construction.** I followed instructions that I did not fully understand at the time, which later became an important part of my learning experience.

After investigating the suspected issue, I submitted a report to HackerOne.

The report details were:

The report described the suspected difference between transaction-pool denylist enforcement and execution-payload validation.

I believed the behavior could allow a validator to accept a payload containing a transaction targeting a denylisted address.

I had spent time exploring the repository, reading source code, running tests, and investigating the behavior locally.

Naturally, I hoped the report would be considered a new finding.

Instead, the report was closed as a duplicate.

The triager identified the report as a duplicate of existing report **#4034\*\*\*.**

The existing finding covered the same underlying issue: a denylist enforcement gap that could allow validator nodes to accept execution payloads containing transactions targeting denylisted addresses when supplied by a Byzantine block proposer.

This was disappointing.

I had investigated the code, worked through the testing process, and submitted a report, only to discover that the underlying issue had already been reported.

However, a duplicate decision does not necessarily mean the technical investigation was worthless or that the suspected behavior was invalid.

It means the report did not establish a new, separately reportable finding.

Looking back, I realized that my process needed a stronger focus on novelty and independent verification before submission.

I also needed to understand the limits of my evidence more clearly.

One of the most important aspects of this experience was my reliance on AI.

AI helped me navigate the repository, identify relevant source files, understand parts of the execution flow, and construct tests.

That assistance was valuable, especially because I was working with unfamiliar Rust code.

However, I also noticed a weakness in my own approach: I sometimes copied commands and followed instructions without fully understanding the underlying concepts.

I was able to run a test, but that did not necessarily mean I could independently explain every part of its implementation or interpret all its security implications.

This made me reconsider what effective AI-assisted learning should look like.

For security research, an AI assistant should not merely provide commands. It should help the researcher understand:

AI can accelerate code exploration, but the researcher must still understand and verify the conclusions.

**The objective should be to become more capable of independent security analysis, not simply more capable of executing commands.**

This experience has changed how I want to approach future bug bounty investigations.

Instead of searching broadly for suspicious code, I want to identify a specific security property and understand how the system is supposed to enforce it.

Finding a missing check in one function is not enough.

I need to determine whether another component performs the same validation, whether the check is applied before or after execution, and what happens when the relevant validation fails.

Before writing a proof of concept, I want to state exactly what I am trying to demonstrate.

I should be able to explain the expected behavior, the observed behavior, the assumptions involved, and the security consequences.

A successful test does not automatically establish a security vulnerability.

I need to determine whether the behavior violates a security boundary or protocol requirement and whether an attacker can realistically trigger it.

Where the program’s policies and available information permit, I want to review known issues, documentation, previous disclosures, and relevant reports before submitting a finding.

A vulnerability can be technically valid while still being ineligible for a reward because it has already been reported.

Most importantly, I want to understand every important step of the investigation.

If I cannot explain why a test works or what its output means, I need to pause and learn before moving forward.

I have not stopped investigating ar\*-\*\*de.

After the duplicate decision, I began examining other areas of the repository, including the Engine API validator and patterns such as unwrap() and expect() in Rust.

That investigation is still ongoing, and I have not established another vulnerability.

I want my next finding, if I discover one, to be based on a clear security hypothesis, reproducible evidence, a well-understood impact, and a careful assessment of novelty.

I also want to be more independent in my technical work.

The goal is not simply to submit more reports. It is to become better at understanding systems, identifying meaningful weaknesses, and explaining why those weaknesses matter.

My first blockchain bug bounty investigation did not result in a new finding eligible for a reward.

But it taught me lessons that I might not have learned as clearly from a successful submission.

I learned that source-code analysis requires patience, that tests must be interpreted carefully, that a proof of concept must support a specific security claim, and that novelty is an essential part of bug bounty research.

I also learned that AI is most useful when it helps me understand a problem rather than merely telling me what to do next.

I am continuing to develop my skills in Rust, blockchain security, execution-path analysis, and vulnerability research.

**A duplicate report is not the result I hoped for, but it has given me a clearer idea of the researcher I want to become.**

This is one step in a much longer learning journey.
