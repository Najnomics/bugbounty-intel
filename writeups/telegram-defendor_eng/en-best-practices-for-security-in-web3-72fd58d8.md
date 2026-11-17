# 🛡️ Best Security Practices in Web3

- **Source URL:** https://www.bnbchain.org/en/blog/best-practices-for-security-in-web3
- **Fetched:** 2026-11-17
- **Channel:** @defendor_eng
- **Telegram message:** https://t.me/defendor_eng/218 (id 218)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
Chains

MAIN CHAINS

BNB Beacon Chain

Sunset Complete

BNB ecosystem’s staking & governance layer

SHAPE THE CHAIN

Staking

Earn rewards by securing the network

Connect

2025.3.6  •  8 min read

Web3 presents opportunities for financial independence, but it also introduces unique security risks. In our [<u>previous blog</u>](https://www.bnbchain.org/en/blog/what-is-blockchain-security), we explored the fundamentals of blockchain security. Today, let's familiarize ourselves with some best practices that can help both individuals and developers protect their digital assets and communities.

Your wallet is your entry point into Web3, so selecting a secure and well-maintained wallet is crucial.

- Choose well-known wallets with a proven track record and security features.
- Ensure your wallet supports secure signature schemes and transaction previews to protect your assets and enhance transaction transparency. Secure signature schemes can help prevent unauthorized access and fraud, while transaction previews allow you to review details before confirming, reducing the risk of signing malicious or incorrect transactions.
- Download wallets from official sources (wallet provider’s website, browser extension stores, or app stores).
- Keep your wallet software updated to receive the latest security fixes.
- Consider using a cold wallet, which is a type of cryptocurrency wallet that stays completely offline and is never connected to external sites or the internet. Unlike hot wallets, which are connected online and more vulnerable to hacks, cold wallets store your private keys securely on a device like a hardware wallet or even a piece of paper. This greatly reduces the risk of cyberattacks, keeping your assets safe from phishing scams and malware.

Smart contracts are the foundation of decentralized applications (Dapps), but they can introduce risks if not properly reviewed.

- Before interacting with a smart contract, check if a reputable security firm has audited it (e.g. [<u>Slowmist</u>](https://www.slowmist.com/), [<u>Beosin</u>](https://beosin.com/), [<u>Zokyo</u>](https://zokyo.io/), and [<u>HashDit</u>](https://www.hashdit.io/en)).
- Review the contract’s source code when possible or seek guidance from someone with coding expertise.
- Use block explorers like Etherscan or Blockscout to verify contract authenticity.
- Start with small transactions when interacting with a new contract.

Phishing remains a common attack vector in Web3

- Always verify website URLs to ensure you are on the official domain. Check for small misspellings, extra characters, or unusual domain endings (e.g., ".net" instead of ".com"). Always type the URL manually or use bookmarks for trusted sites instead of clicking on random links. You can also check for HTTPS encryption (the padlock icon in the address bar) and cross-reference the URL with official sources, such as the project's verified social media or website.
- Avoid clicking on unsolicited links in emails, social media, or messaging platforms like Discord and Telegram.
- Only sign transactions you are 100% aware of and understand completely. Do not simply trust the platform or wallet user interface (UI).
- Users should check the whole address, not just the beginning and end, to avoid scams. This helps make sure the address is correct and prevents falling for tricks where scammers use similar-looking addresses.

Your private key and seed phrase are the most sensitive aspects of your Web3 security.

- Never share your private key or seed phrase with anyone.
- Store keys offline using a hardware wallet or a securely stored paper backup.
- Write down your seed phrase and store it in a safe location.
- Avoid accessing your wallet on public Wi-Fi or unsecured networks.

A strong password policy reduces the risk of unauthorized access.

- Use a password manager to generate and store complex passwords.
- Enable two-factor authentication (2FA) with an authenticator app or a hardware key instead of SMS-based authentication.
- Consider using passkeys where available.
- Regularly update your passwords and avoid reusing them across different platforms.

When interacting with Dapps, review and manage permissions diligently.

- Only grant permissions necessary for the Dapp’s functionality.
- Regularly check and revoke permissions for Dapps you no longer use (tools like Revoke can assist with this).

Trading cryptocurrencies comes with risks, so using reputable platforms and secure trading practices is essential.

- Trade only on trusted exchanges with robust security, and only keep what you’re prepared to lose on exchanges.
- Enable additional security features like withdrawal whitelists and trade confirmations.
- Start with small trades to familiarize yourself with the process before committing larger amounts.
- Only approve transactions for known addresses and limit approvals to the amount needed for this transaction (avoid setting unlimited approvals). Make sure to revoke any unused approvals promptly.

Staying updated on the latest security threats is an essential part of Web3 security.

- Educate yourself and your community about common fraud tactics.
- Remain cautious when engaging with new platforms or offers that seem too good to be true.
- Never interact with any get-rich-quick schemes promising high returns, especially those reaching out through Telegram, WhatsApp, or other social media platforms. These schemes are often fraudulent and designed to steal personal information or funds.
- Always be skeptical of anyone reaching out to you with offers such as job opportunities, NFT trades, or requests to download software. Verify the source, research the offer, avoid downloading unverified software, do not share personal information, use official communication channels, and report suspicious activity to protect yourself from potential scams

Failing to address smart contract security risks early can lead to costly setbacks or even total project failure. Below are essential recommendations for writing secure smart contracts:

- Utilize the latest stable version of Solidity.
- Leverage well-established libraries to minimize risks and reduce audit complexity.
- Validate the return values of external calls, including functions like transfer, transferFrom, send, call, and delegatecall.
- Use events to log changes in critical parameters, aiding in security monitoring and emergency response.
- Use the Checks-Effects-Interactions pattern or reentrancy guards to prevent attacks where a malicious contract repeatedly withdraws funds before the previous transaction is completed.
- Carefully manage arithmetic operations to prevent precision loss due to rounding.
- On-chain block data can be predicted, allowing malicious actors to manipulate fairness
- Avoid sourcing price data from a single provider, as it can be manipulated using flash loans; consider decentralized oracles.
- Minimize the use of lengthy or unbounded loops to optimize gas costs and transaction efficiency.
- Follow Solidity naming conventions to enhance code clarity and maintainability.
- Include an emergency suspension mechanism to mitigate potential exploits in real-time.
- Validate all inputs in external or public facing functions to prevent unexpected control flow.
- Ensuring that developers use proper price oracles instead of relying on liquidity pools for price data. Choosing reputable and reliable price oracles that aggregate data from multiple sources to provide accurate and tamper-resistant price information.

Even with secure coding practices, testing remains essential to identify vulnerabilities before deployment. Robust testing ensures that smart contracts function as intended and comply with business logic. Follow these key testing practices:

- Aim for near 100% unit test coverage, with 100% coverage of core functionalities.
- Conduct functional usability testing to validate business logic and interactions.
- Perform automated security analysis using tools like [<u>Salus</u>](https://salusec.io/auto-detection/) to detect vulnerabilities early.

Even if the smart contract is free from vulnerabilities, weaknesses in Web2 infrastructure can still result in financial losses. To enhance security, consider the following:

- Regular security assessments for both Web2 and Web3 components should be conducted through specialized firms.
- Traditional penetration testing may not be sufficient for Web3 applications; Web3-specific security audits are recommended.
- Use services like Salus for penetration testing, which evaluates vulnerabilities in networks, cloud services, and middleware interactions.
- Ensure credentials like private keys are well stored in an encrypted environment like AWS Secrets Manager.
- Make sure employees or developers that have access to Keys or Tokens follow the Principle of least privilege.
- Regularly evaluate the trust model for infrastructure access to ensure that only authorized personnel have the appropriate level of access to critical systems and data.
- Providing regular training and awareness programs for employees to understand the importance of secure access practices and how to follow them.
- Conducting thorough screening and background checks for new employees before granting them access to critical systems and data. This includes verifying their identity, employment history, criminal record, and any other relevant information to ensure they are trustworthy and do not pose a security risk.

Security audits are an essential step in Web3 development, particularly for smart contracts that handle significant financial transactions. However, audits can be costly and time-consuming, often requiring months of preparation. To maximize audit efficiency, teams should complete the following pre-audit checklist:

- Finalize contract code and provide a commit hash for audit reference.
- Ensure there are no compilation errors or warnings.
- Confirm that all test cases pass successfully.
- Remove outdated comments and unused functions to maintain clean code.
- Document functions and parameters thoroughly.
- Convert public functions to external where applicable to optimize gas usage and reduce cognitive load for auditors.
- Clearly document why unchecked blocks are used, as they disable Solidity's built-in overflow and underflow protection to save gas.
- Highlight key areas of the codebase for auditors to focus on.

Selecting a reputable security firm is equally important. Teams should research security incidents in their sector, compare audit reports across firms, and assess past client feedback before making a decision.

Before deploying a project, teams must ensure all security measures are in place. Consider the following pre-launch actions:

- Address all recommendations and rectifications outlined in the audit report, ensuring all Critical and High Issues are resolved
- If substantial modifications were made post-audit, consider a secondary audit.
- Establish a bug bounty program through platforms like [<u>Code4rena</u>](https://code4rena.com/), [<u>Immunefi</u>](https://immunefi.com/), [<u>BugRap</u>](https://bugrap.io/), or [<u>HackenProof</u>](https://hackenproof.com/).
- Implement real-time monitoring and alert systems covering sensitive information on-chain, such as Ownership Change, and off-chain, such as Front End Compromise.
- Develop an incident response plan, which should include the personnel who are in charge, the immediate actions, the business continuity plans, etc.
- Prepare emergency action scripts to pause contracts in case of an exploit.

Once a Web3 project goes live, ongoing monitoring is critical to detect and address security threats promptly. A robust incident response strategy can significantly reduce potential damages and maintain user trust.

**Real-Time Security Monitoring**

Proactive monitoring helps identify security threats before they escalate. Key monitoring practices include:

- Tracking events triggered by critical processes to detect anomalies.
- Regularly reconciling blockchain events and transactions to uncover potential business logic issues.

**Emergency Response Strategy**

To minimize damage in the event of an attack, teams should follow a structured emergency response protocol:

1. Activate emergency pause mechanisms based on the severity of the issue.
2. Notify users and provide regular updates as new information emerges.
3. Preserve evidence by taking a snapshot of the compromised server.
4. Analyze exploit transactions to determine vulnerabilities and work with security experts on a resolution.
5. Publish a post-mortem report detailing the root cause, financial impact, corrective actions, and ongoing mitigation efforts.
6. Develop and deploy patches following best security practices.

BNB Chain has introduced several measures to enhance blockchain security, including [<u>AvengerDAO</u>](https://www.avengerdao.org/) and DappBay’s [<u>Red Alarm</u>](https://dappbay.bnbchain.org/red-alarm/dapp).

AvengerDAO is a community-driven initiative designed to help protect BNB Chain users from scams, exploits, and malicious threats. It includes:

- Meter – a passive API system for security insights
- Watch – a subscription-based alert system
- Vault – a programmable fund management tool

This initiative is supported by multiple Web3 security firms, such as [<u>Certik</u>](https://www.certik.com/), [<u>SlowMist</u>](https://www.slowmist.com/), [<u>BlockSec</u>](https://blocksec.com/), [<u>GoPlus</u>](https://gopluslabs.io/), [<u>Zokyo</u>](https://zokyo.io/), [<u>Verichains</u>](https://verichains.io/), [<u>Hashdit</u>](https://www.hashdit.io/en), and others.

DappBay helps users explore Web3 projects and includes the Red Alarm feature, which evaluates the risk level of decentralized applications in real-time.

Users can check whether a smart contract has security issues or potential fraud risks.

In 2024, these security efforts contributed to a [<u>64% reduction</u>](https://hashdit.github.io/hashdit/blog/bsc-2024-end-of-year-report/) in security incidents compared to 2023.

Additionally, BNB Chain runs a [<u>bug bounty program</u>](https://bugbounty.bnbchain.org/), offering rewards of up to $100,000 for identifying security vulnerabilities.

As Web3 technology advances, security threats will continue to evolve. Staying informed about emerging risks and adopting the latest best practices are essential for maintaining project security.

[<u>Website</u>](https://www.bnbchain.org/en?ref=binance.ghost.io) | [<u>Twitter</u>](https://twitter.com/BNBCHAIN?ref=binance.ghost.io) | [<u>Telegram</u>](https://t.me/bnbchain?ref=binance.ghost.io) | [<u>Instagram</u>](https://www.instagram.com/bnbchain/?ref=bnbchain.ghost.io) | [<u>Facebook</u>](https://www.facebook.com/profile.php?id=61550857610291) | [<u>dApp Store</u>](https://dappbay.bnbchain.org/?ref=binance.ghost.io) | [<u>YouTube</u>](https://www.youtube.com/@BNBChainOfficial?ref=binance.ghost.io) | [<u>Discord</u>](https://discord.gg/bnbchain?ref=bnbchain.ghost.io) | [<u>LinkedIn</u>](https://www.linkedin.com/company/bnbchaininnovation/?ref=binance.ghost.io) | <u>Build N' Build Forum</u>
