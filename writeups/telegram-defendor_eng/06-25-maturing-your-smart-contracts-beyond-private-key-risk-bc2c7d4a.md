# 🔐 The Main Threat in Web3: Private Key Compromise

- **Source URL:** https://blog.trailofbits.com/2025/06/25/maturing-your-smart-contracts-beyond-private-key-risk
- **Fetched:** 2026-11-17
- **Channel:** @defendor_eng
- **Telegram message:** https://t.me/defendor_eng/205 (id 205)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Maturing your smart contracts beyond private key risk

“Find *all* the bugs!”

That’s the rallying cry, the dominant approach most protocols take to securing their smart contracts before deployment. Teams heavily invest in audits, contests, fuzzing, and formal verification, all aiming to detect every last vulnerability. But what if I told you that the single biggest cause of crypto hacks last year wasn’t smart contract bugs?

Here’s a hint:

Answer: It was private key compromise!

Private key attacks, where key material is abused to steal assets, are an emerging attack vector that narrowly scoped smart contract audits and contests can miss. How susceptible a protocol is to these attacks depends on its design, particularly the maturity of its access controls. In this blog post, we’ll demonstrate how to design protocols that can safely tolerate private key compromise using controls such as multisigs, timelocks, the principle of least privilege, and design methodologies that minimize private key use in the first place.

## Private key compromise is now the most successful attack out there

According to [Chainalysis’s 2024 report](https://www.chainalysis.com/blog/crypto-hacking-stolen-funds-2025), a staggering 43.8% of all funds stolen via hacks stemmed from compromised keys - more than any other verified attack type by a factor of five. Private key compromise is a clear example of a dangerous emerging threat that every engineer must consider when designing new smart contracts and protocols.

Design dictates risk, and historically, few blockchain protocols have seriously considered authenticated smart contract access a significant risk vector. This oversight is reinforced by how the blockchain security ecosystem operates: audits conducted by blockchain-native firms rarely flag architectural access control issues as formal findings, and contest platforms actively discourage such submissions in favor of code-level vulnerabilities.

This narrow focus stands in contrast to established security practices in other industries, where architectural risks like privilege escalation and access control design are fundamental concerns addressed early in the security engagement process.

At Trail of Bits, our engagements flag architectural access control issues using our [Codebase Maturity Evaluation](https://secure-contracts.com/development-guidelines/code_maturity.html). However, most blockchain protocols only seek outside input and review at the very end of the software development lifecycle, when there is little time and few opportunities to fix systemic access control issues.

This is why we need to shift the conversation earlier in the development lifecycle. The purpose of this blog is to bridge that gap, equipping developers with the understanding needed to design systems that are more resilient to private key compromise from day 1.

## Case study: An overcollateralized lending provider

We’ll use a theoretical overcollateralized lending provider as an example to illustrate the different levels of access maturity. For those less familiar with lending protocols, the following functions often require some level of privileged access control:

- Listing/delisting supported assets (collateral & borrowable)
- Setting risk, interest rate parameters, and oracle sources
- Collecting protocol fees/reserves
- Pausing/unpausing protocol functions in the event of an emergency
- Upgrading contracts

However, the specific design of these access control mechanisms will drastically change the overall system’s vulnerability to private key attacks.

### Level 1: Highly exposed - the single EOA controller

This is the least mature, most basic form of access control. In this setup, a single EOA holds supreme authority over all administrative functions of the lending protocol. Depending on how often this key needs to be used, or how quickly it must be used in an emergency, it may have to live in a software wallet on a computer connected to the internet. This is not ideal, to say the least.

The risk of compromise for a system like this is immense, and the impact of compromise is catastrophic and immediate. Once the private key has been compromised, the attacker can upgrade contracts, steal collateral, and destroy the protocol. Nobody gets a Lambo.

#### How to improve to Level 2

The most immediate step to mitigate this single point of failure is to transition to using a multi-signature wallet, requiring consensus from multiple keyholders for any action.

Note that while this action reduces the risk of compromise, it does not change the potential scope of damage if your private keys are compromised.

### Level 2: Basic mitigation - the centralized multisig

Recognizing the extreme danger of a single EOA controller, the next step in maturity involves transferring administrative powers to a multi-signature wallet, often an M-of-N Safe Wallet or similar construct.

This setup is a definite improvement over Level 1 since compromising a single signer’s key is no longer enough for an attacker to take over the protocol. However, there are still significant risks and potential impact in case enough signers are compromised, collude, or are manipulated into signing a maliciious transaction:

- **Speed of execution**: Once the M-th signature is obtained, a malicious action can be executed immediately, leaving no time for a security response.
- **Single point of control**: While the failure point is now distributed over M keys, the control point is still singular. The multisig as an entity still holds ultimate power over the protocol, and even routine, low-risk transactions require the same signing authority as a protocol upgrade. Some examples of hacks where highly protected single points of control have been exploited include the [Bybit hack](https://learn.bybit.com/this-week-in-bybit/bybit-security-incident-timeline/), [WazirX](https://blog.solidityscan.com/wazirx-hack-analysis-8bc8821928e9), and [Radiant Capital](https://medium.com/@RadiantCapital/radiant-post-mortem-fecd6cd38081). In these hacks, the attackers were able to compromise the single critical control point (the multisig) despite spreading the risk among multiple failure points.

#### How to improve to Level 3

If you aren’t impressed with Level 2, I don’t blame you. Moving from Level 2 to Level 3 is where the real maturity journey starts. To reach the next maturity level, two sets of controls need to be implemented: timelocks and the principle of least privilege (PoLP).

Timelocks are contracts that can create a “delay” between the approval of an action and its execution, allowing time for scrutiny and incident response.

The principle of least privilege involves logically separating roles and responsibilities, granting each role only the minimum permissions needed for its specific function. This ensures that if one control point is compromised, the potential damage is contained and doesn’t grant attackers access to unrelated, critical system functions.

### Level 3: Enhanced controls - timelocks and role separation

This level represents a significant leap in maturity by tackling the core weaknesses of Level 2: the immediacy of execution, which is addressed using timelocks, and the concentration of control, which is addressed using the PoLP. Some examples of Level 3 protocols include Aave, Compound Finance, and Lido.

When an approved action can be executed on-chain immediately, the community, and more importantly, your security team, has no time to respond. Using a timelock contract allows you to create a new, overlapping control: the ability to cancel approved transactions.

When an approved transaction is waiting in the timelock, teams can use off-chain tools like Tenderly to monitor it and scrutinize it against expected approvals. If an unexpected request is signed, the timelock gives your incident response team time to review it, cancel it, and start the incident response process.

Proper monitoring and alerting of the timelock is critical; without it, the control is worthless, as seen in the [Beanstalk hack](https://rekt.news/beanstalk-rekt), where the one-day timelock was unmonitored and led to a preventable hack.

By following the principle of least privilege, we can identify the need for at least four roles in the system that segregate responsibilities of differing levels of risk into different buckets:

- **Core system role**: This role is the most privileged in the system, and as such, has a large multisig threshold and timelock delay. Since this role is limited to a single responsibility (upgrading contracts), it is not likely to be used very often, reducing the operational risk from multisig wallet use for other activities.
- **Operations role**: This role is intended to be used for day-to-day protocol operation and configuration. It uses a medium-length timelock and a medium multisig threshold to reflect the lower impact of a potential compromise.
- **Pause guardian role:** This role is responsible for pausing the protocol in the event of an emergency. It should not be behind any kind of timelock, and its multisig threshold should be relatively low to allow a quick response in an emergency.
- **Cancel guardian role**: This role can cancel an approved transaction that is pending in a timelock. Your security team should use this role to cancel unauthorized approvals. It may be a low-threshold multisig wallet or an EOA, depending on how your incident response process is designed.

The risk of the Level 3 architecture is drastically reduced compared to Level 2. We’ve successfully migrated from one control point to four, and reduced the impact caused by a compromised control point using PoLP. Now, your incident response team can actually stop an incident in the event of a multisig compromise.

However, risks still exist:

- **Complexity risk**: Introducing multiple roles, multiple multisig wallets, and multiple timelocks increases the system complexity, creating new avenues for bugs or misconfigurations if not carefully implemented and thoroughly tested.
- **Over-reliance on pause**: The pause guardian role, while necessary for emergencies, is not a golden bullet. Attackers have become more advanced, and attacks are often conducted in private mempools to prevent proactive identification. The potency of pause as a mechanism to reduce the impact of an attack will likely go down over time as attackers become more advanced.

#### How to improve to Level 4

While most protocols are usually satisfied with Level 3, complexity risk and the decreasing effectiveness of emergency pausing necessitate an even higher level of access maturity. Level 4 represents the endgame for any mature protocol, where maturity is characterized by removing the need for powerful actions altogether and the protocol becomes truly decentralized.

### Level 4: The endgame: Radical immutability and user sovereignty

Level 4 represents the pinnacle of maturity in access control design: eliminating the need for administrative actions altogether. This is the most extreme commitment to decentralization and trust minimization a protocol can make, and it comes with the benefit of categorically eliminating access control from the protocol’s threat model.

Achieving Level 4 requires a drastically different design approach than any other level thus far, and most protocols that target Level 4 are not “pure” Level 4 protocols. Uniswap and Liquity are some of the best examples of protocols that strive for Level 4: they do not require any admin management to facilitate operation, but do have some extremely limited admin controls to allow fee/incentive distribution.

Do not confuse Level 4’s philosophy with simply delegating control to a DAO or other bureaucratic entity; a Level 4 protocol does not need any kind of managed control to operate successfully.

The design shift between Level 3 and Level 4 can be nearly insurmountable for many use cases. Consider a centralized exchange cold wallet: unless the entire exchange becomes a decentralized protocol, there must be some level of administrative access to the wallet to transfer funds to users.

For fully on-chain protocols, Level 4 is possible but still daunting; for our overcollateralized lending system, we need to fundamentally refactor the system’s design. For each component that previously required administrative management, we must design a replacement that requires no management whatsoever:

- **Upgradeability**. In Levels 3 and below, the system’s smart contracts may be upgraded to fix bugs or add new features. In a Level 4 protocol, the system’s smart contracts are fully immutable. To add a new feature to the protocol, an entirely new set of contracts must be deployed, and users must manually move their funds over to the new system.
Since an upgrade cannot fix security bugs, the system’s contracts must be simple, concise, extremely well tested, verified, and reviewed.
- **Listing/delisting assets.** In most overcollateralized lending protocols, listing and delisting assets are administrative actions because if adding collateral were permissionless, a malicious token may be leveraged to steal collateral. For a lending protocol to achieve Level 4, it may support self-contained market deployment. In this system, to add support for a new asset, a completely new, independent version of the lending protocol must be deployed and configured explicitly for that new asset or set of assets. Users must then choose to interact with this separate deployment or with another deployment with different assets.
- **Risk parameters** represent another configuration usually managed by an administrator. In a Level 4 lending protocol, these parameters are either permanently set when the new asset is deployed or are permanently set to follow some kind of algorithmic parameters. Since these values would be set permanently, it’s critically important that their behavior is well-characterized through rigorous modeling, testing, and verification.

Designing a Level 4 protocol has significant tradeoffs: Emergency intervention is not possible; the system is inflexible once deployed; and there is a huge initial burden to verify the security correctness and economic soundness of the design.

Despite these tradeoffs, this design paradigm categorically eliminates access control risk, and many of the design patterns used in Level 4 protocols can improve other aspects of the system’s security.

Level 4 embodies a purist vision of a decentralized cyberpunk ethos, prioritizing immutability and user sovereignty above administrative flexibility.

## Design for resilience, not just reaction

As we’ve journeyed through the levels of access control maturity, from the degen simplicity of a single EOA controller to the radical cyberpunk immutability of Level 4, one singular truth becomes clear: the way you design your protocol fundamentally dictates its vulnerability to private key compromise.

With 43.8% of stolen funds in 2024 resulting from private key compromises, ignoring architectural access control is no longer acceptable. While traditional bug hunting remains essential, these design decisions must be made much earlier in development to be potent.

Here are some proactive steps you can take today:

1. Assess your protocol against the maturity framework. Be honest about where you stand. Most projects begin at Level 1 or 2.
2. Implement timelock contracts for your highest-risk administrative functions. Even this single change significantly improves your security posture. Ensure that these timelock contracts are adequately monitored to ensure you can respond if an unapproved transaction is queued.
3. Map your protocol’s privileged functions and segregate them into logical roles following the principle of least privilege.
4. Consider which components of your system could benefit from Level 4 immutability patterns, even if your overall design requires administrative controls.

At Trail of Bits, we champion this holistic view of security. That’s why we offer services like design reviews and design-stage consulting, tailored specifically for projects early in their development lifecycle. These services allow teams to receive expert guidance and recommendations to address these fundamental issues proactively, complementing traditional code audits that focus on implementation vulnerabilities later on.

Ultimately, building secure decentralized systems requires more than just hunting for bugs. It demands a commitment to designing for operational resilience from day one. By understanding the maturity model and consciously choosing design patterns that minimize trust and limit the potential impact of compromise, you can build protocols that are not only innovative but truly robust against the evolving threats of the decentralized world.
