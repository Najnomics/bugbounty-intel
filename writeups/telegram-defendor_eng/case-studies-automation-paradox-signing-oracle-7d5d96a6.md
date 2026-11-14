# 🔑 QuillAudit Finds Open Signing Oracle Behind a Payment Protocol's Multisig

- **Source URL:** https://www.quillaudits.com/case-studies/automation-paradox-signing-oracle
- **Fetched:** 2026-11-14
- **Channel:** @defendor_eng
- **Telegram message:** https://t.me/defendor_eng/2186 (id 2186)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
Join 1500+ leaders who secured themselves from losing Billion Dollars

A payment infrastructure protocol, bridging partner payment flows through two upgradeable on-chain programs, engaged us to conduct a comprehensive operational security review of its live custody and settlement stack. The protocol custodies a multi-million dollar operational float and settles automatically at high frequency roughly every few minutes around the clock.

While the on-chain architecture was deliberately robust, featuring disjoint three-of-four multisig authorities, distinct administrative role keys, hard-bounded beneficiary whitelists, and pause-guarded fund movers, the operational layer that actually touched the keys told a very different story. We approached the engagement through two lenses: first, an independent verification of the on-chain control plane and governance logic; second, a deep review of the off-chain signing service, settlement orchestrator, and delivery pipeline. The result was a tale of two postures. We confirmed numerous strong controls, including correctly implemented signature introspection, immutable mint whitelists, and cosigned container images. Simultaneously, we identified two critical design risks in the signing layer, four high-severity issues spanning custody centralization and settlement reliability, and multiple infrastructure and governance hygiene gaps. The most consequential finding: the service holding the hot automation key exposed an unauthenticated network surface that could be reached by any peer, effectively offering an open signing oracle over a multi-million dollar pool.

Automating settlement on a high-speed blockchain is one of the hardest operational security problems in Web3. Human signers cannot convene a multisig ceremony every few minutes at 3:00 AM. The protocol’s architects solved this with an off-chain orchestrator and a dedicated signing service that holds a hot automation key, an architectural choice that is common, necessary, and inherently dangerous. The tension is architectural. On-chain, the protocol is a fortress: multisig governance, time-locked role rotations, beneficiary whitelisting, and program-upgrade authorities all held behind genuine thresholds. Off-chain, the runtime is a single hot key invoked by a service that must be reachable, responsive, and always-on. Our challenge was to trace the entire path from a partner payment request to a signed on-chain transaction, and to answer a single question: does the fortress around the multisig matter if the service feeding it can be reached by anyone on the network?

We examined four interconnected domains where operational failures could translate into loss of funds, duplicate disbursements, or protocol capture:

1. On-Chain Control Plane: Two upgradeable programs managing an operational pool and a satellite vault. Governance, upgrades, and sensitive configuration changes route through separate multisig authorities. Fund egress is theoretically bounded to pre-approved beneficiaries.
2. Off-Chain Signing and Orchestration: A fastlane signing service that receives settlement requests, resolves key names to a key-management backend, and signs transactions. This service is the runtime heart of the protocol, the machine that actually holds and uses the automation key.
3. Settlement Pipeline and Idempotency: The confirm-and-retry logic that ensures a payment is executed exactly once, with status caching, blockchain confirmation polling, and congestion-driven retry heuristics.
4. Delivery Pipeline and Infrastructure: The continuous integration workflows, container build process, secret handling, and network edge that compile, package, and deploy the signing service image.

Independent On-Chain Verification: We treated the client’s operational security specification as a hypothesis, not evidence. Every role assignment, authority, threshold, and configuration value was read directly from the live network. This revealed a striking anomaly: the on-chain reality was more locked down than the documentation claimed. The specification described weaker governance thresholds and a secondary-wallet consensus for fund movement that did not exist in the deployed code, while the live programs used proper three-of-four multisigs.

Architectural and Process Tracing: We traced how a settlement request traveled from the orchestrator to the signing service, how the service resolved key identities, and how the signed transaction reached the chain. We examined the remote procedure call surface, key resolution logic, and transaction relayer behavior.

Infrastructure and Supply-Chain Review: We assessed the container build, deployment pipeline, secret handling, and network edge controls, areas explicitly excluded from prior code audits but critical when the container holds credentials to a hot signing key. Standards-Based Benchmarking: We mapped findings against recognized custody control frameworks, including web3OPSEC v3.0 controls for treasury operations, dual authorization, tiered thresholds, and cold-reserve segregation.

Precedent Mapping: We tied findings to independently verified real-world patterns: unauthenticated internal services leading to lateral movement, supply-chain compromises of build pipelines, and settlement double-spends in high-frequency payment systems.

The findings told a coherent story of a fortress with an unguarded service entrance.

**An Unauthenticated Signing Oracle**

The off-chain signing service exposed an insecurely-bound, unauthenticated remote endpoint on a network-reachable interface. The service accepted caller-supplied metadata to determine which key to use, defaulting to the production automation signer. With no transport-layer authentication and no caller authorization, any network-reachable peer could invoke the service. More severely, certain exposed methods allowed an unauthenticated caller to supply arbitrary transaction instructions and select any named key - including administrative keys, which the service would then sign and relay. Another method allowed arbitrary message signing, producing raw detached signatures with no domain separation. Together, these turned the key-management infrastructure into an unauthenticated signing oracle over the entire keyring.

**The Hot Key with No Guardrails**

The automation key was a single hot keypair, invoked continuously by the orchestrator, and was the sole on-chain authority required to move the entire operational custody pool. There was no in-program per-transaction cap, no rolling velocity limit, no second signer, and no time lock on egress. The full float sat in one hot-key-reachable pool with no cold or reserve segregation. While beneficiary whitelisting prevented drains to arbitrary attacker-owned addresses, a compromised automation key could still force the entire pool to legitimate destinations beyond off-chain limits, creating an insolvency or availability crisis. Furthermore, the same hot key held membership in a governance multisig, meaning its compromise reduced by one the number of additional independent compromises needed to approve a new attacker-controlled destination.

**Settlement Idempotency and Double-Spend Risk**

The settlement retry logic relied on a volatile, clearable in-memory cache with a long stale-acceptance window. Status checks that returned inconclusive results were cached as “did not land,” triggering fresh resends. The idempotency key was caller-supplied and could default to empty, stored only process-locally and subject to cache eviction under memory pressure. Under normal network congestion, RPC latency, or orchestrator restart, the system could duplicate customer payments. For a payment rail, a double-spend is not a theoretical bug, it is a direct loss of funds.

**Governance Hygiene and Documentation Drift**

The operational security specification was materially out of date, describing weaker governance thresholds and a fund-movement consensus mechanism that did not exist in the code. While the live deployment was actually stronger than documented, stale specifications are an operational liability: incident responders may contact the wrong signers, and future “corrections” might accidentally weaken the live configuration. Additionally, certain governance actions could bypass time-lock delays through acknowledgement shortcuts, and some request slots could be occupied by unexecutable actions, creating governance friction during incident response.

**Supply-Chain and Infrastructure Exposure**

The deployment pipeline allowed force-merging of pull requests with administrative override, bypassing review gates. The container build copied the entire workspace into the image, baking in CI-generated environment files and unencrypted private keys into the published layers. The network edge allowed direct reachability to backend origins, bypassing the Web Application Firewall layer.

Several aspects of this engagement required reasoning beyond standard vulnerability scanning. The Documentation Paradox: In most audits, documentation paints a rosier picture than reality. Here, the opposite was true. The specification described single-key upgrade authorities and weaker guardian thresholds, while the chain showed proper three-of-four multisigs. This “optimistic documentation” is still dangerous: it trains operators to expect weaker controls than exist, and it means incident playbooks may be written for the wrong architecture.

Dead Code as a Tell: The signing service contained commented-out authentication interceptors and network guards. Their presence as dead code suggested the team knew what controls were needed but had not activated them, likely for operational convenience during development. This is a common pattern in fast-moving infrastructure: the security control is “almost there,” which creates a false sense of safety.

The Idempotency Cache as a Financial Control: We did not treat the settlement cache as a mere performance optimization. In payment systems, idempotency is a financial control. Analyzing the cache eviction policy, the null-status handling, and the process-local storage revealed that the system lacked durable, pre-send reservation semantics, the gold standard for preventing duplicate disbursements.

The Migration Risk: The protocol was actively wiring a new version of its custody program. The new version’s administrative authority was bound to a single hot key co-located in the same keyring as every other signer. While the new program was currently unfunded, the migration path meant that the same unauthenticated signing surface would soon control an unbounded custody pool. This is a forward-looking risk that standard audits often miss: assessing not just today’s state, but tomorrow’s architecture.

Findings were organized into a prioritized remediation roadmap:

Immediate: Terminate the insecure network bind; enforce mutual transport-layer authentication and per-caller authorization; remove or tightly restrict arbitrary-instruction and arbitrary-message signing primitives; authenticate all proposal creation; and add network policies restricting reachability to the signing service.

Short-Term: Introduce in-program per-transaction caps and rolling velocity limits on the automation key; require a second independent signer or short time lock on large egress; segregate the float by sweeping the majority to a cold or multisig-gated reserve; fix settlement idempotency with durable pre-send reservations and mandatory non-empty request identifiers; and remove force-merge capabilities from the pipeline.

Medium-Term: Separate the automation manager key from the governance multisig; enforce role distinctness in-program; add non-bypassable minimum delays on role rotations; update the operational specification to match on-chain reality; implement authenticated origin pulls and proper secret mounting at runtime; and add a global circuit breaker to the satellite vault program.

A multisig is only as strong as the weakest path to its keys. Elegant on-chain governance can be undermined by a single unauthenticated service holding the automation key.

In payment infrastructure, idempotency is a financial control, not a performance feature. Volatile caches and loose retry logic are direct paths to duplicate disbursements.

Documentation that understates reality is still a liability. Incident response depends on accurate specifications; drift in either direction creates risk.

The CI/CD pipeline is part of the trust boundary. When the container holds hot signing credentials, every build step, merge gate, and baked secret becomes a potential compromise vector. Forward-looking architecture review matters. Assessing an unfunded but wired-up new program version prevented a future unbounded custody migration.

Dead code is a signal. Commented-out security controls often indicate where the team intended to harden but stopped short and attackers know to look there.

The protocol received a clear, actionable security roadmap. The critical signing-surface issues were acknowledged for immediate remediation. The team gained visibility into the settlement double-spend vectors and the forward migration risk. We validated numerous strong controls: properly implemented multisig authorities, correct cryptographic signature introspection, hard-bounded beneficiary whitelisting, pause-guarded fund movers, and container image signing in the pipeline. The engagement shifted the team’s security focus from on-chain correctness to operational resilience ensuring that the machine holding the keys was as well-guarded as the vault it served.

In high-frequency settlement systems, security architects often focus on making the chain final and the governance multisig robust. But the real question is: what happens at 3:00 AM when the orchestrator wakes up, connects to the signing service, and asks it to move a million dollars? If the answer is “it signs, because no one ever authenticated the request,” then the multisig was just theater. The future of operational security in automated custody belongs to those who harden not just the vault door, but every millimeter of the wire that connects the machine to the key.

From day-zero risk mapping to exchange-ready audits, QuillAudits helps projects grow with confidence. Smart contracts, dApps, infrastructure, compliance: secured end to end.
