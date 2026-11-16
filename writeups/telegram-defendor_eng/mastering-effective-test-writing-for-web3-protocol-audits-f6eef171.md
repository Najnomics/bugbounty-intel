# 🛡️ Three Mindsets for Securing Web3 Protocols

- **Source URL:** https://mixbytes.io/blog/mastering-effective-test-writing-for-web3-protocol-audits
- **Fetched:** 2026-11-16
- **Channel:** @defendor_eng
- **Telegram message:** https://t.me/defendor_eng/840 (id 840)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
Tell us about your protocol

Author: Dmitry Zakharov, Sergey Boogerwooger

Security researchers at MixBytes

Introduction

Writing tests is fundamental to ensuring the security and reliability of protocols, especially in the world of web3. However, common recommendations, like achieving 100% code coverage, are often misleading, as high coverage doesn’t necessarily equate to security. Another challenging recommendation is to adopt a hacker mindset during test development. The hacker mindset is not easily explained and requires significant experience and specific processes to implement effectively.


Given the current state of the industry, many new protocols struggle to hire highly experienced developers, leaving newcomers to grapple with this concept, often lacking knowledge about the security aspects of contract development.


This article introduces a structured testing framework to help developers write more thoughtful, effective tests aimed at catching severe bugs in their protocols. After conducting a broad analysis of the nature of bugs in audit reports, it was concluded that the hacker mindset alone is not enough to detect severe bugs. In addition to this, two other mindsets can be applied. The framework presented in this article encourages adopting three unique mindsets: the hacker mindset, the invariant mindset (or formal verification mindset), and the system architect mindset. Each mindset is designed to guide the creation of test scenarios that reveal potential vulnerabilities and weaknesses.

The Testing Framework Overview

In our company, we promote an approach to audits that follows this principle: an audit is the process of generating questions about the code and obtaining answers. This may sound simple, but it’s a powerful approach. All attack vectors for any existing bug can be represented as questions about a specific contract or function. More importantly, this approach enables auditors to track the progress of an audit more smoothly, especially with well-written protocols where bugs are hard to find. Tracking progress solely by the number of discovered bugs can be frustrating for security researchers in such cases.


This approach is also easier to explain to new security researchers and web3 protocol developers. For this reason, presenting the testing framework as a set of general questions that can be adapted for each specific project (including examples for various protocols) makes a lot of sense. It allows each mindset in the framework to be adapted straightforwardly.


It’s important to note that the framework should be applied after completing basic unit and integration tests. While the recommendation to have at least 80-90% test coverage and cover all basic user flows is valuable, having only these tests is not enough to ensure your protocol is resilient to attacks. An additional layer of security is needed, and this framework provides that, helping ensure that the protocol not only functions correctly but is also free of vulnerabilities.


As shown in the diagram below, to use the framework, you should select each mindset (one after another) and answer the questions specific to that mindset. The answers to these questions will generate a list of test scenarios to implement. Framework usage will be explained in detail for each mindset with examples.

Hacker Mindset

The hacker mindset can be frustrating for many developers because using it effectively requires experience as a security researcher or a white hat hacker. Even a short but impactful explanation like, “Instead of asking, *How is this supposed to work?, ask, How is this NOT supposed to work?*” doesn’t provide a clear set of actions for applying the hacker mindset (i.e., writing tests that simulate potential attack vectors). Our industry’s goal is to make protocols secure and resilient. Without explaining the hacker mindset to newcomers, achieving this goal becomes challenging.


In this article, we’ve prepared a list of specific questions to guide developers in writing meaningful tests, rather than a list of actions. These questions are designed to help you develop tests that cover severe bugs, using the hacker mindset.

Question 1: What use cases exist for the protocol that should not be accessible to regular users?

This question addresses potential attack vectors caused by poor access management. A key layer of protocol protection is reducing the number of functions accessible to unverified (potentially malicious) users. Consider all possible use cases currently allowed for any user, and prepare tests to ensure that privileged functions can only be accessed by authorized roles controlled by the protocol.


Example: Suppose your protocol has a function intended to be called only by a specific off-chain service controlled by the protocol. This question implies ensuring that this function has an appropriate modifier, and that your tests verify cases where it is called by both a privileged user and a random user.

Question 2: What limitations should be in place for the sequence and frequency of function calls by users?

This question helps identify reentrancy vulnerabilities. Once deployed on the mainnet, any user can call any public function in any order. Testing should confirm that only the allowed flow of contract usage is possible. Think of all the possible use cases that should be restricted, and write tests that verify the protocol blocks disallowed actions.


Example: You might write a test to ensure that a function cannot be called in the same transaction (same block, same time interval) with other functions, affecting the behavior of this one. Such constraints protect the protocol from potential misuse.

Question 3: What constraints should be placed on user input parameters?

This question encourages further restriction of contract usage by unauthorized users. Suppose you’ve already limited access to privileged functions and restricted user flows to only allow predetermined scenarios. Now, think about whether malicious users could pass unexpected values to functions, causing the protocol to process cases the developers did not anticipate.


Example: Imagine a function accepts a uint256 input but internally casts it to uint128, assuming it will work only with values under type(uint128).max. If a malicious user manipulates the input to exceed this limit, the protocol could continue to operate but with potentially negative effects. Anticipate all potential constraints for input parameters and prepare tests to confirm the protocol operates only within allowed ranges. This step will optimize fuzzing and invariant testing by narrowing the range of possible inputs. Also, it's useful to think and potentially test different corner cases for parameter values such as 0, 1, type(uint...).max - 1, etc, to avoid potential errors with rounding and overflows.

Question 4: Which parameters should not be controlled by users when calling the protocol?

This question falls somewhere between the first and third questions. Here, consider input parameters with limited allowable values, sometimes restricted to a predefined list (whitelist) or entirely out of user control. For example, ERC20 token addresses used as function inputs might need restrictions, allowing only tokens on an approved list.


Example: Write a test for a function that performs a swap on a decentralized exchange (DEX) to ensure that users can only conduct swaps on whitelisted DEXs (such as Uniswap, Curve, or Balancer). This question encourages you to think about parameters that should be controlled by a whitelist rather than an open range, or even controlled by the protocol without user input.


As shown, the hacker mindset should prompt you to think about the restrictions your protocol should enforce. Each of these restrictions should be thoroughly tested. Don’t be intimidated by the hacker mindset; just ask yourself these questions and implement the necessary limitations in your protocol.

Invariant Mindset

After restricting your protocol as much as possible, it’s time to ensure that it functions according to its specification. The invariant mindset (or formal verification mindset) is an excellent tool for this. This mindset focuses on identifying unbreakable conditions, or invariants, within the code. An invariant is a condition that should hold true regardless of the protocol’s state. This mindset is particularly useful for functions that perform calculations based on formulas.


Formal verification methods can be used to analytically prove that an invariant always holds. However, the biggest challenge with this mindset is identifying the invariants themselves. Having a detailed protocol specification greatly aids this process, but for many new DeFi protocols aiming for rapid launch, such specifications are often missing.


We want to emphasize that starting protocol design with a clear specification is extremely beneficial. Many issues can be detected and addressed during the specification phase. However, this approach requires additional effort and time, which may be challenging. If you don’t have time to prepare a detailed specification, you should at least compile a list of critical invariants.


The primary question for this mindset is: “What invariants exist in the code?” As mentioned earlier, this question is best applied to functions that involve calculations, as it’s easier to identify meaningful invariants in those cases. For example, if you have a function that calculates how tokens are distributed among multiple actors, an invariant might ensure that the distribution is balanced, or that no tokens remain after distribution. The specific invariant will depend on the function’s logic, so you’ll need to define it carefully.


A common invariant example for Uniswap v4-like protocols, which stores all the balances on one contract and allows different pools to work with these balances, is a check that guarantees the number of tokens output in a swap cannot exceed the specific pool's balance. This invariant is simple to implement and can be adapted to most decentralized exchanges (DEXs), ensuring that user funds remain protected during swaps.


Another useful invariant is one that ensures the variable representing the total amount of tokens controlled by the protocol is always less than or equal to the contract’s token balance. This check uses “less than or equal” because in cases where ERC20 tokens are transferred directly to the contract’s address, a strict equality check would fail.


It’s important to note that while companies offering formal verification services handle the preparation of invariants, fuzzing techniques can also help validate them. However, fuzzing does not guarantee that invariants will hold in all protocol states. If formal verification services are out of reach at this stage, setting up fuzzing tests is essential. Tools like [Echidna](https://github.com/crytic/echidna) or [Foundry](https://book.getfoundry.sh/forge/fuzz-testing) can be highly effective here.

System Architect Mindset

The system architect mindset takes a highly pessimistic view of any protocol integration with another protocol or external service. Unlike the hacker mindset, which focuses on restricting access, the system architect (SA) mindset is about anticipating how external integrations could fail. It requires a touch of hacker-style skepticism but doesn’t merge with the invariant mindset, as it’s impractical to formally verify all potential external integrations a protocol might use.


This mindset considers what would happen if an integrated service or protocol fails, is updated, or is compromised. For example, an off-chain service update could contain a bug causing it to misinterpret milliseconds as seconds. An oracle service might stop updating a price feed once it hits a threshold value (e.g., after the LUNA crash, some oracle providers ceased updating prices after hitting certain thresholds). An external DeFi protocol could release an update that changes the reward distribution logic or adds additional tokens that require a special function to claim. A cross-chain bridge might fail to deliver messages due to incorrect gas pricing or an internal error. In short, the external ecosystem of a protocol could change or be hacked, so the system architect mindset approaches all integrations with a paranoid perspective.


The main question for the SA mindset is: "Which of the protocol’s dependencies are external and could fail?" This question isn’t difficult to answer — it just requires identifying all protocol integrations and assuming they might fail someday. A more challenging question is: "In what ways could each integration fail?" This is where the hacker mindset comes in handy, prompting you to consider possible incorrect behaviors or failures in these integrations.


Example: Imagine your protocol relies on an oracle service, which fails to update the price of an asset for several hours due to high gas costs. Most oracle services provide data showing the last time a price was updated, so it’s not difficult to check within the contract. However, deciding how to handle this scenario is more complex. For instance, if you run a lending protocol and need this price to determine whether to liquidate a user, different solutions (each with pros and cons) may apply, depending on the asset’s parameters. While we won’t explore these options here, they often require detailed consideration.


Besides identifying integrations that could fail, it’s also valuable to note which of these integrations involve upgradeable smart contracts. This consideration is more about protocol architecture than specific testing. The general rule here is to make a contract upgradeable if it integrates with an upgradeable contract.


A best practice for protocols with integrations is to create mocks for all off-chain services interacting with the contract. This allows testing the protocol’s response to off-chain service failures. For example, if you have a mock of a cross-chain bridge and set it to block message transfers, you can simulate a scenario where the cross-chain bridging protocol fails to deliver a message and observe how your protocol reacts.

Conclusion

Test coverage is crucial for developing secure web3 protocols, but high coverage alone doesn’t guarantee safety. The framework discussed in this article encourages writing thoughtful, targeted tests that address potential threats from multiple perspectives. By adopting the hacker, invariant, and system architect mindsets, developers can design test cases that confirm functionality and uncover vulnerabilities.


For the hacker mindset, you should use the following questions:


- What use cases exist for the protocol that should not be accessible to regular users?
- What limitations should be in place for the sequence and frequency of function calls by users?
- What constraints should be placed on user input parameters?
- Which parameters should not be controlled by users when calling the protocol?


For the invariant mindset, there is only one question, but it's a tough one: “What invariants exist in the code?” And for the system architect mindset, the only question is: "Which of the protocol’s dependencies are external and could fail?" The hardest problem with this question is that it also requires determining possible ways of failure for the external integrations to correctly handle them in your protocol.


Remember: Write tests – stay safe!

-  Who is MixBytes?

-  DisclaimerThe information contained in this Website is for educational and informational purposes only and shall not be understood or construed as financial or investment advice.

Other posts
