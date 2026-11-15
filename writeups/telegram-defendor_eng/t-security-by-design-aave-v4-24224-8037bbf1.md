# 🛡 Aave V4 Security Program Overview

- **Source URL:** https://governance.aave.com/t/security-by-design-aave-v4/24224
- **Fetched:** 2026-11-15
- **Channel:** @defendor_eng
- **Telegram message:** https://t.me/defendor_eng/1314 (id 1314)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# **Introduction**

Aave V4 was built under a security-first framework. Security was never treated as a final gate before deployment. Instead, security controls were layered across the entire development lifecycle, starting from early architectural decisions and continuing through to post-audit fix validation.

The result: approximately **345 days of cumulative security review** across manual audits, formal verification, invariant testing, fuzzing, and a public security contest. The program was backed by a **USD 1.5 million dedicated security budget** ratified by the DAO.

This document provides full transparency into the approach, process, and outcomes of the Aave V4 security program, under the custodianship of Aave Labs.

# **Our Approach**

## **Security Design Consultation**

The Certora team attended the March 2025 Aave Onsite and worked alongside Aave Labs developers on V4’s design. The sessions helped align on foundational assumptions and shaped the verification framework used throughout the rest of development.

Separately, independent security researchers with deep Aave protocol experience were brought in early. At that stage, their role was closer to design consultation than traditional auditing. Critical design choices benefited from adversarial review before they became costly to change.

## **Security Over Speed**

Security has always taken precedence over speed as a core value of Aave Labs. Although the V4 was completed on schedule in June 2025 at the conclusion of the Aave V4 development stream, additional time has been dedicated to rigorous security hardening prior to launch to ensure the highest standards of robustness and resilience. In keeping with our commitment to building in public, we are sharing this process transparently with the community.

## **Threat Modeling**

A formal threat model was maintained as a living document throughout the program. It was updated as the codebase evolved and new features like *Risk Premiums* were introduced. Trust assumptions between system components were explicitly documented and shared with all audit teams so that trust boundaries were directly tested, not assumed correct.

# **Audit Tendering**

Aave Labs ran a structured Request for Quotation (RFQ) process in two rounds to select audit partners. The process generated over 19 proposals from audit firms, independent security researchers, and tooling providers.

Each proposal was evaluated on DeFi audit experience, team composition, proposed methodology, timeline flexibility, and value. Aave Labs held detailed conversations with every candidate to assess their understanding of the protocol and ensure genuinely independent, complementary perspectives.

Despite industry-wide audit price increases since the Aave V3 cycle in 2021–2022, V4’s smaller codebase and the competitive RFQ process resulted in per-auditor costs coming in lower than historical benchmarks. The full program was delivered under the approved USD 1.5 million budget and the remainder will be returned to the DAO.

It is worth noting that Certora’s Continuous Security Services proposal is not constrained to this budget, and they will continue to support the protocol through collaboration and availability even after Aave V4 is live and in production.

# **Timeline & Engagements**

The security program spanned approximately 12 months from initial engagement to final report delivery:

| Phase | Period | Activities | 
|---|---|---|
| Inception & FV | March 2025 | Certora engaged at inception. Formal verification runs alongside development. Certora joins the 2025 Aave Onsite. | 
| Early Reviews | Mid 2025 | Private manual reviews by independent security researchers (Stermi, Deadrosesecxyz, Josselin, Kurt Barry). | 
| Feature Complete | July 2025 | V4 reaches feature completeness. RFQ process initiated. | 
| 1st Audit Round | Sep–Nov 2025 | Manual audits: ChainSecurity, Trail of Bits, Blackthorn, Stermi, Certora and Trail of Bits. | 
| Invariant Tests | Sep–Nov 2025 | Enigma Dark and Trail of Bits invariant testing. | 
| Security Contest | Nov 2025–Jan 2026 | Six-week public contest on Sherlock. 900+ verified participants. 950+ findings submitted. No Critical or High findings reported. | 
| Fix Validation | Jan–Feb 2026 | Fix review for first-round of audits, and security contest. | 
| 2nd Audit Round | Feb 2026 | Second audit round: ChainSecurity, Blackthorn, Stermi and Josselin. Cross-review of all issues from prior phases. | 
| Reports Published | Feb 2026 | Trail of Bits, Blackthorn, and ChainSecurity reports made public. No high-severity vulnerabilities. As more reports are finalised they will also be published. | 

## **Audit Firms & Researchers**

The first round engaged four firms and four independent researchers, deploying 15 security researchers over 275 cumulative audit days:

| Auditor | Type | Researchers | Duration | Scope | 
|---|---|---|---|---|
| Certora | Firm | 2 SRs | 8 weeks | Manual review + formal verification | 
| ChainSecurity | Firm | 2 SRs | 4 weeks | Manual review | 
| Trail of Bits | Firm | 3 SRs | 2 weeks | Manual review + invariant testing | 
| Blackthorn | Firm | 4 SRs | 3 weeks | Manual review | 
| Stermi | SR | 1 SR | 5 weeks | Advisory + manual review | 
| Deadrosesecxyz | SR | 1 SR | 3 weeks | Early-stage manual review | 
| Josselin | SR | 1 SR | 3 weeks | Early-stage manual review | 
| Kurt Barry | SR | 1 SR | 2 weeks | Early-stage manual review | 

## **Security Contest**

Following the first audit round, a six-week public security contest was hosted on Sherlock.xyz starting December 1st, 2025. The goal was to expose the codebase to a far wider range of perspectives and methodologies than any fixed team could provide.

Over 900 verified participants submitted more than 950 findings. Even with such a large volume of interaction from the community, no critical or high findings were surfaced and the majority of the submitted findings were invalid. Invariant test suites developed during the audit program were shared with contestants to provide coverage context and push researchers to explore beyond already-verified properties.

## **Second Round Review**

The second round brought back ChainSecurity, Blackthorn, Josselin and Stermi for an additional round of audits, ending with fix validation. That added 80 audit days focused on verifying that all remediations were correctly implemented and did not introduce new issues.

# **Tooling & Automated Verification**

## **Formal Verification**

Certora’s engagement covered both a dedicated formal verification effort and an extended manual review component with senior researchers.

The Certora Prover identified findings during development that were resolved before the code reached audit readiness. This demonstrated the value of embedding formal methods from day one. Alongside this, the team developed a rigorous suite of edge-case scenario and unit tests to complement the invariant and formal verification tests, ensuring appropriate behavior of the system throughout the development life cycle.

## **Invariant Testing & Fuzzing**

Enigma Dark was engaged to develop a tailored actor-based invariant testing suite for the Aave V4 protocol, kicking off September 30, 2025. Their scope covered the core protocol components: the Hub (the central liquidity manager handling global and per-spoke accounting), the Spoke modules (the core borrowing module managing supply, withdraw, borrow, repay, and liquidation flows), the AssetInterestRateStrategy, TreasurySpoke, SpokeConfigurator, HubConfigurator, and AaveOracle.

The engagement used both Echidna and Medusa fuzzers with a modular, extensible setup similar to the invariant suite Enigma Dark had previously built for V3. Multiple rounds of invariant brainstorming ensured coverage across reserve accounting, interest rate model consistency, liquidation mechanics, and hub-spoke interaction boundaries. The core team later reviewed and extended this suite, adding ERC-4626 properties for the tokenization spoke and a hub-level suite for validating external spoke contributions.

Trail of Bits independently developed their own invariant test suite as part of their audit. Having two independent suites built from different starting points gave the team confidence that coverage was both overlapping and complementary. These suites from EnigmaDark and Trail of Bits were later used to build a combined invariant test suite integrated into the codebase and CI/CD (with adaptations). This includes a separate suite with abstracted hub components such that it can be reused to validate new spoke designs.

## **AI-Assisted Review**

As a complementary layer, Aave Labs ran a structured evaluation of AI-powered smart contract auditing tools, deploying three tools across V4’s repositories. This was positioned as a supplement to human-led review, not a replacement, serving as an early investment in understanding how AI can support future audit cycles. We felt that it was important to start engaging with AI and agentic-based scanning systems for V4 now but internally decided that we would not allocate any of the DAO supplied budget to these endeavours. We are actively tracking the capabilities of various tools and will be implementing them going forward.

# **Codebase & Results**

The Aave V4 codebase is smaller in lines of code than V3. This was a deliberate result of the hub-and-spoke redesign, and it contributed to more focused audit engagements. That structural discipline was reflected in the feedback from early reviewers.

Security Researchers who had early access to the code base noted publicly that it was the cleanest pre-audit codebase they had seen, citing careful design, consistent application of best practices such as explicit rounding and checked casts, and a detailed test suite leveraging fuzzing and invariants.

The codebase reached feature completeness in July 2025. Between that milestone and the first audit round, the team focused on internal review, test coverage expansion, gas optimizations and preparing comprehensive documentation that was shared with all audit teams ahead of their engagements.

The [published audit reports](https://github.com/aave/aave-v4/tree/main/audits) from Trail of Bits, Blackthorn, and ChainSecurity confirm that no high-severity vulnerabilities were identified. All findings across every phase of the program have been addressed and validated in the second audit round. Reports are publicly available in the *Aave V4 repository under the Audits [folder](https://github.com/aave/aave-v4/tree/main/audits)*. As we finalise more audit reports that will be added to the repository.

# **Risk Provider Involvement**

Risk providers were treated as stakeholders in the security design process, not just future consumers of the protocol. Their operational experience managing risk configurations on Aave V3 gave them a unique vantage point on failure modes, edge cases, and parameter sensitivity that internal teams and traditional auditors are structurally less likely to surface.

Engagement began informally, early in the development cycle. Design decisions around the hub-and-spoke architecture, liquidity accounting, and the Risk Premiums mechanism were discussed with service providers as concepts were still being formed. That early dialogue influenced how certain features were scoped and constrained before they were committed to code.

Formal engagement started at EthCC 2025, where Aave Labs hosted an on-site V4 Demo with risk providers. This session marked the transition from informal consultation to structured collaboration. Providers reviewed the protocol’s core mechanics in depth and offered direct feedback on configurability, risk surface, and the implications of architectural changes for their day-to-day operations.

Following EthCC, Aave Labs initiated a series of dedicated online sessions covering: a full V4 codebase walkthrough, a presentation on Aave V4 Risk Config and its parameter model, and open-agenda Office Hours, open to all Service Providers, designed to surface any outstanding concerns without a fixed scope.

Across all of these interactions, risk providers contributed perspectives that shaped both protocol design and the security hardening approach. Their input on trust assumptions, parameter boundaries, and operational risk helped identify areas where additional safeguards were warranted, complementing what formal auditors and independent researchers contributed through code-level review.

# **Integrator Consulting**

Integrators interact with the Aave protocol differently from end users: they build on top of it, meaning their failure modes, surface area, and security assumptions are different in kind, not just in degree. Engaging them early was a deliberate choice.

Aave Labs held structured conversations with prospective V4 integrators throughout the development cycle, focused on understanding their implementation requirements, identifying friction points from V3, and ensuring that V4’s architecture actively facilitated rather than complicated the workflows they depend on.

One concrete output of this engagement was the introduction of the Tokenization Spoke. Integrator feedback surfaced the need for a cleaner, more composable interface for building advanced vault structures on top of the protocol. The Tokenization Spoke was designed to meet that requirement directly, providing a standardized, auditable layer that simplifies integration and reduces the custom scaffolding integrators would otherwise need to build and maintain themselves.

Security posture was also shaped by integrator input. Their concerns introduced an integrator-level threat model alongside the end-user one, covering how integrating systems interact with protocol state, where trust boundaries sit between layers, and which failure modes propagate upward into integrator contracts. This expanded the scope of what the security program was expected to cover and influenced the framing given to audit teams.

The result is a V4 security model that accounts for both the user who interacts with the protocol directly and the builder who intermediates that interaction. Both surface areas were treated as in-scope.

# **Going Forward**

Five commitments Aave Labs will carry forward from this program:

- **Embed formal verification early.** Certora’s involvement from inception allowed formal methods to shape architecture, not just validate it. We will continue this approach for all major protocol development.
- **Layered methodologies**. No single approach is sufficient at Aave’s scale. Manual review, formal verification, invariant testing, leveraging AI, fuzzing, and a public contest each surfaced findings the others missed. Future programs will maintain this breadth.
- **Maintain continuous coverage.** The formal verification framework will continue running alongside development. Invariant test suites will be maintained and expanded as the protocol evolves.
- **Bug Bounty.** Setup an ongoing bug bounty program to provide continuous coverage from the broader security community.
- **Mature AI scanning.** Building on what we learnt from the AI tests, we will continue to hone AI scanning for future releases.

# **Acknowledgments**

This program was made possible by the expertise and commitment of many individuals and teams. Aave Labs extends its gratitude to ChainSecurity, Trail of Bits, and the Blackthorn team (0x52, pkqs90, Tapir, 0xSimao) for their rigorous audit work; to Stermi, Deadrosesecxyz, Josselin, and Kurt Barry for their independent review contributions; to Certora for embedding formal verification from day one as well as their manual audit review and their continuous review, feedback and assistance; and to Enigma Dark for their invariant testing suite.

The Sherlock community of security researchers demonstrated the value of public contests. And the Aave Labs development team, who made the entire program possible through their responsiveness and rigour.

Thank you to the Aave DAO for ratifying the security budget and investing in security at this scale. That commitment sets a standard for accountability in decentralized governance.
