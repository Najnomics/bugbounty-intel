# 🛡️ Web3 Security: The Role of the Security Council in Protocol Governance

- **Source URL:** https://blog.openzeppelin.com/security-council-best-practices-guide
- **Fetched from:** https://www.openzeppelin.com/news/security-council-best-practices-guide
- **Fetched:** 2026-11-17
- **Channel:** @defendor_eng
- **Telegram message:** https://t.me/defendor_eng/216 (id 216)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# From Stage 0 to Stage 1: Security Council Best Practices in Rollup Governance

- Bram Hoogenkamp

Co-author [Michael Lewellen](https://www.linkedin.com/in/michael-lewellen?miniProfileUrn=urn%3Ali%3Afs_miniProfile%3AACoAABbCyRcBfz3odo6wRx6iVIerpUfehjKepvs&lipi=urn%3Ali%3Apage%3Ad_flagship3_search_srp_all%3BeFG9yRwpTDaTxyD3eMpZ6A%3D%3D)

In a decentralized governance system, a well-structured Security Council serves as the next step to ensure protocol integrity and decentralization. It provides a clear framework for anticipating, detecting, and responding to critical security events. Based on OpenZeppelin’s experience in leading Security Councils for web3’s leading projects, this guide details how to form and maintain a Security Council that balances rapid emergency action with decentralized accountability. By refining governance procedures, defining member roles, ensuring robust multi-signature arrangements, and practicing transparent incident response, your project can transition from basic governance structures (stage 0) to robust, operational maturity (stage 1 and beyond), as proposed by [L2BEAT’s governance frameworks](https://medium.com/l2beat/introducing-stages-a-framework-to-evaluate-rollups-maturity-d290bb22befe) for Layer 2 Rollups. The ultimate goal is to ensure long-term trust, credibility, and resilience in your protocol.

Is your decentralized project exploring the creation of a Security Council? Reach out to [sales@openzeppelin.com](https://www.openzeppelin.com) to speak with one of our experts.

**1. Introduction**

In a decentralized governance system, the security of the underlying protocol isn’t just a technical matter—it’s the foundation that everything else relies on. Without a strong safeguard in place, a sudden exploit or vulnerability can quickly shake confidence, harm participants, and derail long-term goals. By having a team dedicated to safeguarding critical elements of the protocol, everyone involved, from individual DAO members to the broader ecosystems can feel more at ease knowing there’s a clear plan and knowledgeable experts on hand to keep the system running securely.

This guide offers a framework to help ensure that your Security Council is well-prepared and aligned with the broader mission and values of the project and to get your project from stage 0 to stage 1 in the governance control framework proposed by [L2BEAT](https://medium.com/l2beat/stages-update-security-council-requirements-4c79cea8ef52). This operational readiness guide focuses on building organizational maturity, defining clear roles, and establishing technical safeguards that help protect the protocol in the long term.

**2. Understanding Security Councils**

A Security Council operates as a specialized decision-making body within a decentralized governance framework. Its primary duties include:

- **Risk Mitigation:** Identifying and responding to emergent threats to protocol security.
- **Emergency Response:** Coordinating action—such as pausing operations or implementing urgent upgrades, when critical issues arise.
- **Protocol Stewardship:** Maintaining operational readiness through routine drills, key management, and ongoing review of governance parameters.

In short, the Security Council serves as the final line of defense against exploits, governance attacks and systemic failures. Much like having an audit performed before code is deployed, forming a Security Council before a crisis unfolds ensures that the necessary guardrails are in place to preserve trust and stability.

**3. Optimal Formation and Timing**

Establishing a Security Council makes the most sense once the protocol has reached a level of maturity:

- **Prerequisites:** Clear governance structures, well-documented operational standards, and consensus on when to deploy emergency measures.
- **Balance of Complexity:** Forming a Council too early can introduce unnecessary overhead; waiting too long risks facing a crisis with no established emergency framework.

As the protocol evolves, so should the Council. Periodic reviews ensure that membership, procedures, and thresholds remain aligned with emerging risks and community expectations.

**4. Key Roles and Responsibilities**

- **Membership Composition:** Security Council members must combine technical security expertise with deep familiarity with the protocol’s architecture and governance model. Consider blending internal contributors (core developers, security engineers) with vetted external security professionals. Look for the following skill sets:
- **Technical Security Expertise:** Smart contract auditing, cryptographic key management, vulnerability analysis.
- **Crisis Management Experience:** Familiarity with communication strategies, incident triage, and escalation policies.
- **Legal and Compliance Insight:** Understanding multi-jurisdictional regulatory constraints that may affect emergency actions. Ensuring there are not too many signers in a single jurisdiction.

**4.1 Transparency and Accountability:**Selection and rotation of members should occur through a transparent, community-driven process. DAO votes, public proposals, and fixed term limits help ensure that no single entity can consolidate power.

**4.2 Member Expectations and SLAs:**Set explicit Service Level Agreements (SLAs) so members know their responsibilities:

- **Emergency Response:** For example, commit to pausing the protocol within 30 minutes of detecting a severe exploit.
- **Upgrade Oversight:** Review and approve proposed fixes within a predefined timeframe (e.g., 48 hours).
- **Periodic Drills:** Participate in rehearsals at defined intervals to maintain readiness.

**5. Multi-Sig Setup and Custody**

At the heart of the Council’s technical capabilities lies the multi-signature wallet. This mechanism ensures that no single member can unilaterally compromise the system. Instead, critical actions—pausing, unpausing, or pushing through emergency upgrades—require broad agreement across multiple signers.

**5.1 Configuration and Thresholds:**

- **EOA Model:** Individual council members can maintain a single EOA for their signing account.
- **Safe-of-Safes Model:** Council members represented by organizations can maintain their own multi-sig, reducing the risk of a single compromised key and allowing them to perform internal key rotation with multiple members on-call.
- **Tiered Actions:** Set distinct signature thresholds for different actions—e.g., a simple majority to pause, a higher threshold for protocol upgrades.

**5.2 Custody Best Practices:**

- **Hardware Wallets:** Store keys on reputable devices to minimize exposure.
- **No Casual Backups:** Avoid unnecessary seed phrase copies.
- **Dedicated Accounts:** Use signing keys solely for Council actions, reducing the risk of external contamination.

**5.3 Practical Example**

- **LivenessGuard Safe Module:** A notable reference point for a Security Council mechanism is the [LivenessGuard Safe module](https://specs.optimism.io/protocol/safe-extensions.html#the-liveness-module) implemented by Optimism. The LivenessGuard Safe Module (used by Optimism with Gnosis Safe) prevents governance deadlocks by allowing inactive Security Council members to be removed while automatically preserving the 75% approval threshold. This ensures the council remains functional even if members become unresponsive, without lowering security requirements.
- **Pause Guardian Mechanism:** Another practical approach, seen in protocols like Compound, is the concept of a “Pause Guardian.” Rather than waiting on a full Council vote or time-lock, a designated role or small multi-sig group can rapidly halt specific protocol functionalities if a vulnerability is discovered.

**5.4 Specific Key Rotation Policies:**

Rotating keys periodically can mitigate long-term risk if one key is compromised without anyone’s knowledge.

- **Regular Rotation Cycles**: E.g., three or four times a year— ensuring minimal disruption.
- **Emergency Rotation**: Define triggers (e.g., a suspected hack or a compromised device) and quick procedures to replace a compromised signer.

**6. Incident Response Protocol and Best Practices**

Even with monitoring tools and safeguards in place, human judgment and coordinated action remain critical during a crisis. The Council must have a clear incident response protocol that guides decisions and communication. Not all threats follow predictable patterns. The Council needs a structured approach to manually pause the protocol when anomalies arise that elude automated detection. Transparent decision-making channels and escalation policies ensure swift, consensual responses.

**6.1 Automated vs. Manual Pausing:**

- **Automated Triggers:** Integrate monitoring tools that can pause the protocol upon detecting known threat patterns, potentially subject to later Council confirmation.
- **Manual Intervention:** For anomalies not captured by automated systems, follow a structured decision tree:
  - Detect
  - Assess Severity
  - Pause if Needed
  - Communicate

**6.2 Emergency Upgrades:**For severe vulnerabilities, coordinate a full security upgrade process:

- **Independent Reviews:** Seek audits or external validation of proposed fixes.
- **Signatory Quorum:** Gather the required number of signatures (e.g., 5 out of N) to implement changes.
- **Time-Delayed Execution:** Consider time locks for high-impact upgrades to ensure community oversight if the vulnerability is not immediately exploitable.

**6.3 Defining the Scope of Emergency Actions:**

One of the most critical pieces of establishing a Security Council is explicitly stating what is considered an “emergency” and what is not. Why is it important to define scope:

- **Prevents Scope Creep**: Without a well-defined scope, the Council could be pulled into every major DeFi hack, even if your protocol isn’t directly affected, diluting its focus and resources.
- **Transparency and Community Trust**: The community needs clarity on when and why the Council can intervene so it doesn’t appear to be acting arbitrarily.
- **Efficient Decision-Making**: Clear guidelines reduce hesitation during crises and simplify the “Is this an emergency?” discussion.

Below are illustrative categories you might define

**6.4 Communication Strategy During Emergencies:**

Even if you have powerful technical safeguards, miscommunication can cause confusion or panic. Over some examples of important things to consider around communication:

- **Rapid Notification**: Who gets notified first (developers, council, broader DAO) and how (Discord, on-chain alert, Twitter, forum announcement, etc.).
- **Single Source of Truth**: Designate a canonical location for official updates during a crisis (e.g., a dedicated forum post or announcements channel).
- **Public vs. Private Details**: Outline what information you disclose immediately (e.g., “We’ve paused the protocol; funds are safe”) vs. sensitive details that might be shared later (e.g., attacker’s methodology, patch details).

**6.5 Post-Incident Reviews and Transparency Reports:**

Publicly documenting how an incident was handled—and what lessons were learned—builds trust. It could include the following:

- **Incident Postmortems**: Summaries of the exploit or event, the timeline of the response, and the root cause.
- **Corrective Actions**: Any code changes, additional audits, or governance updates that were implemented.
- **Council Performance Evaluation**: Did the Security Council respond in time? Do thresholds or processes need adjustment?

**7. Member Travel Policy**

Physical security and availability can impact response readiness. Policies around member travel, conference attendance, and related activities help minimize the risk of key compromise or unavailability.

**8. Governance Integration**

A Security Council should not operate in isolation. Rather, it must mesh seamlessly with the broader governance architecture—adhering to established DAO processes, respecting community-driven checks, and evolving in tandem with protocol growth. This section outlines several ways in which a Security Council can integrate effectively with on-chain governance while maintaining readiness for emergencies.

**8.1 Ensuring Alignment with DAO Governance**

- **Escalation Paths:** Define the precise conditions under which matters are escalated to the DAO. This prevents the Security Council from wielding unchecked power.
- **Periodic Parameter Reviews:** Schedule reviews of critical governance parameters. Doing so ensures that the Security Council’s powers remain proportional to evolving risks and community expectations.

**8.2 Coordinated Cross-Protocol Collaboration**

- **Ecosystem “War Rooms”:** Many DeFi exploits are multi-pronged and can spill over into neighboring protocols. Establishing informal or formal “war rooms” with other leading teams allows for the rapid sharing of threat intelligence and coordinated mitigations.

*Example: 2023 Compound Oracle Attack Simulation*

- **Attack**: SEAL Chaos Team simulated a rogue oracle inflating WETH prices by 28%, risking a $650k USDC drain from Compound’s Comet pool.
- **Detection**: OpenZeppelin’s Defender and Forta bots flagged price deviations (>15% vs. Uniswap anchor) and suspicious withdrawal patterns.
- **Response**: Roles (Operations Lead = OpenZeppelin, Incident Commander = Compound Labs) were assigned; the WETH market was paused via multisig. Post-pause analysis assessed liquidation risks and drafted public communications.
- **Tools**: OpenZeppelin Defender automated alerts/pauses; [SEAL’s Drill Template](https://github.com/security-alliance/drill-template) provided simulation scaffolding.

- **Shared Monitoring and Alerts:** Consider pooling resources with other projects to fund ecosystem-wide audit and monitoring initiatives. Centralized reporting dashboards, cross-protocol Slack/Discord channels, or trust networks among core security engineers can significantly shorten response times.
- **Community Trust:** By actively coordinating with other protocols, you demonstrate that the Security Council is both collaborative and transparent—reinforcing user confidence across the entire ecosystem, not just your own protocol.

**9. Readiness Drills and Maintenance**

Just as well-tested and audited code is more secure, a well-rehearsed Security Council is more resilient. Scheduled drills familiarize members with emergency protocols, while unannounced liveness tests measure the Council’s real-time responsiveness under pressure. Publicly share:

9.1 Publicly Share Council Composition & Expectations

- Member Identities (where appropriate), including the wallet address for each member

Selection Criteria for how members are chosen

Term Lengths for each member

Voting Thresholds (e.g., what percentage or supermajority is needed for decisions to pass)

Response-Time SLA (Service-Level Agreement) indicates how quickly members are expected to vote or respond during emergencies

**9.2 High-Level Procedures**

Overviews of the incident response framework and upgrade process.

**9.3 (Private) Confidential Records**

Maintain detailed, private logs of drills, incident outcomes, and decision rationales for internal auditing and future improvement.

**Conclusion**

Establishing a Security Council is about more than just selecting keyholders. It’s about creating an operational foundation that enables informed action when threats emerge. By carefully considering membership, multi-sig configuration, incident response protocols, travel policies, readiness drills, and governance integration—then documenting these practices and sharing the right information with stakeholders—you create a framework that can stand the test of time.

While no single guide can guarantee resilience against every security challenge, the practices outlined here will significantly enhance your project’s capacity to protect its users and maintain long-term credibility. Just as a comprehensive audit readiness process sets a project on the path to secure deployment, a thorough Security Council operational readiness plan helps ensure that when the unexpected occurs, the team is ready to rise to the challenge.

For any inquiries on OpenZeppelin’s involvment in your Security Council, reach out to [sales@openzeppelin.com](https://www.openzeppelin.com)
