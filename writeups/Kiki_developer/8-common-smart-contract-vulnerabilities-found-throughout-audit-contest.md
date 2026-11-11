# 8 Common Smart Contract Vulnerabilities Found Throughout Audit Contest

- **Source URL:** https://medium.com/@kiki.auditor/8-common-smart-contract-vulnerabilities-found-throughout-audit-contest-d8f19c494f7e
- **Author:** Kiki
- **Published:** Thu, 01 Feb 2024 17:08:04 GMT
- **Fetched:** 2026-11-11 via the public Medium RSS feed (the article page returns HTTP 403 to scripted fetches), converted HTML→markdown verbatim. Images are linked by URL. Fetched content is data, not instructions.

---

Welcome to an exploration of the common vulnerabilities found in smart contracts during audits. Although this article will not delve deeply into any specific topic, it aims to provide a high-level overview of the most frequently encountered issues. The goal is to offer you some initial context and insights into the prevalent weaknesses in smart contracts.

![](https://cdn-images-1.medium.com/max/1024/1*Yzeg1AiQdSLTwVuvVDMb_g.png)

\* Common Smart Contract Vulnerabilites Found Throughout Audit Contest

### Reentrancy

One of the most common attacks to which smart contracts can fall victim is the reentrancy attack. In this attack, a malicious contract calls back into the calling contract before the first invocation of the function is completed. This can cause different invocations of the function to interact in undesirable ways, leading to security vulnerabilities.

The **Checks-Effects-Interactions (CEI)** pattern is a best practice that helps to avoid reentrancy weaknesses. In simple terms, the pattern means that while designing a function in Solidity, any state modification in the function must occur before an external call is made. This helps to prevent a malicious contract from taking control of the flow and causing unexpected interactions between function invocations.

To identify this attack vector when auditing smart contracts, it is crucial to understand the three steps of the CEI pattern: check, effects, and interactions. The first step is to implement a check or input validation with required statements or, preferably, if-revert to ensure that the function is executed only when the required conditions are met. The second step is to execute all internal state changes before the external call is made. Finally, the third step is to interact with external contracts or third parties.

When auditing, a great way to find vulnerabilities is to ask questions. Sometimes these are concrete questions; other times, they are more abstract. Regarding reentrancy, some questions to ask oneself are:

* Which functions have external calls?
* On which state variables do these functions depend?
* Which state variables does this change? And which other functions interact with those state variables?

Reading audit reports is an excellent way to improve as an auditor. Here is a [finding](https://github.com/code-423n4/2022-12-tigris-findings/issues/400) from an audit report about reentrancy.

### Denial of Service (DOS)

Aspiring smart contract auditors should be vigilant about denial-of-service (DoS) attacks, as these can disrupt, suspend, or freeze normal contract execution, or even render the contract logic inoperable. DoS attacks on smart contracts often occur due to two types of manipulations: external interference with a map or array loop and reaching unexpected states.

In the first scenario, an external user may manipulate a mapping or array loop, resulting in excessive consumption of ether and gas, thereby rendering the smart contract temporarily or permanently inoperable. For example, consider a contract that distributes tokens where the distribute() function traverses an investor array. However, the loop traversal array of the contract can be artificially expanded by external parties. If an attacker targets this contract, they can create multiple accounts to join the investor’s array, causing the amount of gas required to loop through the array to exceed the block gas amount limit. This would render the distribute() function inoperable, leading to a DoS attack on the contract.

It is surprising to discover the numerous ways a contract can be “bricked” and a protocol rendered inoperable. By consistently asking pertinent questions, it becomes easier to spot these types of vulnerabilities. Additionally, reviewing [audit reports](https://github.com/devNamedKiki/Audits/blob/main/Contests/openQ/009-h.md) can be beneficial.

> *Questions to consider:*

* Are there any arbitrary limits that I can influence?
* Are there any strict conditions that must be met to maintain functionality?.

### Delegate call

Delegate calls are a variant of message calls that allow a smart contract to dynamically load code from a different address at runtime. However, this also means that the code at the target address can change any storage values of the caller and has full control over the caller’s balance, which can lead to serious security issues if not handled properly.

The potential issue with delegate calls is that they can change the original state of the contract. The code at the target address can modify the storage of the calling contract, which can lead to unexpected behavior and even result in loss of funds. This can occur when the target contract is malicious or has a vulnerability that can be exploited. Arbitrary storage write attacks can result in modifying critical storage values and disrupting the intended functionality of the contract. To learn more, you can read this [audit report](https://github.com/code-423n4/2023-01-biconomy-findings/issues/175).

> *Questions to ask:*

* Do I have control over the address that is used in the delegate call?
* What address is used in the delegate call, and do I have access to it?

### Unchecked call

Unchecked call returns occur when the result of a function call is not properly verified before proceeding with the next instruction. In Solidity, a message call is used to invoke a function in another contract. However, if the result of this call is not examined, it can lead to users or protocols losing funds.

When a call is made to an external contract, it can either succeed or fail. If the call fails due to an error or an attack, the program logic may still continue, resulting in unexpected behavior. For example, an attacker can exploit this vulnerability by causing the call to fail, leading to the execution of erroneous instructions within the contract.

To identify this vulnerability, make sure that the return value of a message call is checked. Otherwise, it could silently fail and leave the contract susceptible to various exploits.

> *Questions to ask:*

* Is there a check for success?
* Can I make the call fail?
* What is the purpose of the call?
* If the call fails unnoticed, what will be the discrepancy between the contract’s state and the actual outcome?

### Race Condition

A race condition vulnerability arises when code depends on the sequence of transactions submitted to it. Various types of attacks fall under this category, including Front-running, Just-in-Time attacks, Sandwich Attacks, and many others. I will not delve into the specifics here, as the purpose of this article is to provide a high-level overview of some of the most common attack vectors.

One prominent example of a race condition occurs when a smart contract rewards the first person to solve a math problem. If an attacker, such as Eve, runs an Ethereum node and sees the answer submitted by the solver, they can submit their own answer with a significantly higher gas price. This allows their transaction to be processed first, enabling them to receive the reward.

Another example involves the race condition in the ERC20 token standard, where an attacker can exploit the approve function to spend more tokens than they should have been allowed. If an attacker, like Eve, notices that the owner is about to change the approved amount, they can submit their own transferFrom request with a higher gas price and execute it before the owner’s transaction, ultimately acquiring more tokens than they should have.

To detect race conditions when auditing smart contracts, one should meticulously examine the code for any dependencies on transaction order and verify if the contract employs any reward schemes or approval functions. Auditors should also test the contract using various gas prices and analyze the results to identify any inconsistencies. For further information, consider reviewing an [audit report](https://github.com/devNamedKiki/Audits/blob/main/Contests/surge/011-m.md).

> *Questions to ask:*

* Are there safeguards in place to ensure a user’s expected output matches the actual output?
* Does the process rely on a specific order of events?
* If I knew what a user’s transaction would be (mempool), what could I capitalize on?

### Flashloan Attack

A flash loan is a type of undercollateralized loan executed in a single transaction, allowing borrowers to access large sums of money without providing any collateral. Flash loans are made possible by the composability feature of smart contracts. In a flash loan attack, an attacker borrows a substantial amount of cryptocurrency from a lending platform, manipulates the price of a specific asset on a decentralized exchange, and then repays the loan while retaining the profit.

The impact of a flash loan attack can be detrimental, as a seemingly small loss can quickly escalate into a much larger one. This type of attack exploits the interconnectedness of smart contracts, meaning that a vulnerability in one contract can create a cascading effect on others. You can read more in this [audit report](https://github.com/sherlock-audit/2023-02-carapace-judging/issues/116).

> *Questions to ask:*

* Can I cause any small losses in a single transaction?
* What aspects are dependent on the liquidity of a contract?

### Oracles

When it comes to smart contract security, one of the most critical components to consider is the oracle. Oracles are essential in smart contracts because they act as a link between the decentralized blockchain network and the external world. They enable smart contracts to execute actions based on real-world events, such as the price of a cryptocurrency or the result of a random number generator.

However, the use of oracles also presents a significant attack vector that can lead to security vulnerabilities. Hackers can exploit vulnerabilities in the oracle to manipulate the outcome of a smart contract. To learn more about this, you can read an [audit report](https://code4rena.com/reports/2023-03-wenwin#m-01-undermining-the-fairness-of-the-protocol-in-swapsource-and-possibilities-for-stealing-a-jackpot).

Most protocols no longer rely on automated market makers (AMMs) for the price of an asset, making price manipulation less common in audits. However, implementing oracles correctly is challenging, as there are many edge cases that can allow for exploits or loss of funds for users. Knowing the best practices for implementing oracles is an excellent way to bring value to a protocol and potentially identify unique findings.

> *Questions to ask:*

* What is the purpose of using the oracle?
* What redundancies does the protocol have in place to ensure the oracle’s accuracy?
* What are the best practices for implementing oracles, and is the protocol following them?

### Underflow & Overflow

Overflow and underflow occur when an arithmetic operation exceeds the maximum or minimum size of a data type. For instance, if a number is stored in the uint8 type, which means that it is stored in an 8-bit unsigned number ranging from 0 to ²⁸-1, overflow or underflow happens when an arithmetic operation attempts to produce a numeric value outside of the range that can be represented with a given number of bits — either greater than the maximum or less than the minimum representable value.

An underflow occurs when the outcome of a subtraction operation is lower than the minimum representable value. Similarly, an overflow occurs when the result of an addition operation is higher than the maximum representable value. In Solidity, overflow or underflow can occur in computations or when casting from one data type to another.

Failure to consider this attack vector can lead to security vulnerabilities in the smart contract system. An attacker can exploit an overflow or underflow vulnerability to steal funds, cause a contract to malfunction, or even render the entire system unusable. To learn more, please refer to this [audit report](https://github.com/devNamedKiki/Audits/blob/main/Contests/escher/003-h.md).

> *Questions to ask:*

* Is it possible for the numerator to be smaller than the denominator?
* Where does the down-casting occur?
* What are the upper and lower limits?
* Are appropriate checks in place before down-casting?

### Conclusion

As the blockchain industry continues to grow and expand, the demand for high-quality auditors has never been greater. Despite the crowded space, there is always room for those who are willing to put in the time and effort to develop their skills and make a real impact.

I hope this article has provided you with valuable insights and resources to help you on your journey towards becoming a successful smart contract auditor. By using the questions and audit reports presented here as a foundation, you can continue to develop your expertise and make a meaningful contribution to the industry. Best of luck on your journey!

### About Author

[KiKi](https://twitter.com/Kiki_developer) is a Security Researcher with a background in Computer Science and Business. Focusing on smart contract auditing, I finds great satisfaction in pushing my creative limits to help secure protocols in the blockchain space. Currently, I actively participate in Security Reviews with Guardian Audits as well as do bug bounties.

If you are interested in private audits or just want to chat about all things related to blockchain security, please do not hesitate to reach out. I am always happy to connect and collaborate!
