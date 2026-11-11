# @bluethroat_labs — Bluethroat Labs

- X: [https://x.com/bluethroat_labs](https://x.com/bluethroat_labs) (id `1975856622380453888`, created 8 Oct 2025)
- Site: [bluethroatlabs.com](https://bluethroatlabs.com/)
- Founder also posts as [@saxenism](https://x.com/saxenism) (Rahul Saxena; bio: Founder @bluethroat_labs, ex-security @zksync)
- Phala's advisory also thanks **GuyPhy** of Bluethroat Labs
- Platforms: Immunefi; also coordinated disclosure directly with protocol teams (dstack / Phala)
- Focus: TEEs, consensus / low-level execution, distributed systems, AI-native tooling (BlueSkills, BluePaper)
- Method they advertise: in-house domain-specific agents, used by human researchers, aimed at invariants and cross-layer failures

This is the richest **Web3 infra** source in the seed set. Several Immunefi payouts still lack a public root cause; the dstack advisory is the best technical writeup.

## Findings with technical detail

### 1. dstack attestation-pipeline issues (critical + highs + lows)

- **Title:** dstack attestation pipeline hardening (vendor disclosure)
- **Platform / program:** Coordinated disclosure to dstack / Phala (the public post does not call this an Immunefi payout)
- **Reported:** January 2026, by Rahul Saxena (Bluethroat Labs); remediations deployed Jan–Feb 2026; public post 10 Feb 2026. No evidence of in-the-wild exploitation, per Phala.
- **Bug classes and root causes (as stated by Phala):**
  1. **QE identity verification — Critical.** The `dcap-qvl` library did not mandate Quoting Enclave identity validation, so a verifier could accept quotes from an unauthorized QE. Fix: make QE identity checks mandatory in the core library (GHSA-796p-j2gh-9m2q).
  2. **TCB status enforcement — High.** TCB (trusted computing base) status was informational; revoked or outdated TCB levels were not rejected by default. Fix: enforce TCB checks by default; deprecate a misleading `is_valid` boolean.
  3. **GPU attestation verification — Low.** GPU attestation was displayed without cryptographic verification of the NVIDIA device certificate chain; CPU↔GPU binding was not enforced at the platform level.
  4. **SSRF via client-controlled PCCS URL — Low.** A `pccs_url` parameter let callers point server-side requests at arbitrary endpoints. Fix: remove the parameter from the public API.
  5. **Event-log verification semantics — Low.** `event_log_verified` could be misunderstood (digest replay vs semantic verification). Fix was documentation / upcoming removal of some event logs.
  6. **TLS verification for PCCS — Low (dangerous default).** Default config skipped TLS certificate verification for PCCS connections (meant for local dev). Bluethroat's LinkedIn explainer added that a network attacker could replay older but still-valid Intel collateral, so yesterday's trust decision could override today's state. This was stale-collateral replay, not full forgery of Intel signatures. Fix: verified TLS is the default; opt-out only for local testing.
- **A related design discussion (not scored as a vuln):** RA-TLS certificate freshness was treated as a design tradeoff, not a bug.
- **How they framed the work:** Study TEE systems from first principles; look at verification defaults, not only "is there a signature somewhere."
- **PoC:** Not published in the advisory. Not invented here.
- **Takeaways:** In attestation and other "verifier" code, freshness and authenticity are security properties. Certificate checks that default to off are in-scope. Client-supplied URLs in verifiers are classic SSRF. Do not treat an informational status field as an enforcement control. "Looks signed" is not the same as "bound to the current, authorized enclave."
- **Sources:** [Phala advisory](https://phala.com/posts/dstack-security-update-attestation-pipeline-hardening) (10 Feb 2026); [LinkedIn explainer](https://www.linkedin.com/posts/bluethroat-labs_56-trusted-execution-over-an-unsafe-transport-activity-7447638926099685376-GKd6) (8 Apr 2026); [bluethroatlabs.com](https://bluethroatlabs.com/)

### 2. Broken deterministic execution (Immunefi bounties #9 and #10)

- **Platform:** Immunefi (program undisclosed)
- **Severity:** #9 confirmed **High**; #10 described as coming from the same root
- **Bounty:** Amounts undisclosed in the posts
- **Bug class:** Consensus / execution non-determinism
- **Root cause (as stated):** Researchers used two in-house agents (low-level execution + consensus) and "were able to break the guarantees of deterministic execution by fiddling with the exact CPU instructions for the same contracts."
- **How found:** Cross-domain follow-through: a failure that only appears when execution and consensus are reasoned about together, with agents assisting specialists.
- **PoC / exact instructions:** Not disclosed.
- **Takeaways:** On L1 / VM / client programs, same contract + different CPU behavior is a research question, not a curiosity. Determinism is an invariant: if two honest clients can disagree, the bug is real even when the "happy path" looks fine.
- **Sources:** 1 Oct 2026 09:51 WAT [bounty #9](https://x.com/bluethroat_labs/status/2105581456550461936); 6 Oct 2026 16:17 WAT [bounty #10](https://x.com/bluethroat_labs/status/2107490499305124027)

### 3. Two layers disagreed on what counts as a quorum — $10,000

- **Platform / program:** "A major L1" offered the bounty (platform not named in the post)
- **Severity:** Undisclosed
- **Bounty:** $10,000 (publicly stated)
- **Bug class:** Consensus invariant mismatch / split-brain on quorum definition
- **Root cause:** Two layers of the system did not agree on what counts as a quorum.
- **Their stated quality bar:** Derive the protocol invariant, reproduce a failure on stock clients, run a matched control, and test recovery.
- **Takeaways:** When reviewing consensus, explicitly write down the quorum rule in each layer (networking, consensus, execution, light clients) and look for disagreements. Reproduction on unmodified clients plus a control run is how you keep the finding honest.
- **Source:** 7 Nov 2026 13:53 WAT — [post](https://x.com/bluethroat_labs/status/2119050683840438658)

### 4. Immunefi bounty #11, downgraded Critical → High

- **Platform:** Immunefi
- **Severity:** Originally reported as critical; downgraded to high "due to a contrived trigger requirement"; they said the team still rewarded appropriately
- **Bounty / root cause:** Undisclosed
- **Source:** 9 Oct 2026 16:07 WAT — [post](https://x.com/bluethroat_labs/status/2108575109535433161)

## Other Immunefi consistency (details undisclosed)

- **28 Oct 2026:** Immunefi announced a **$50,000** bounty for a critical vulnerability; 19 confirmed reports in four months, 3 paid and 16 awaiting payment; #17 on the 90-day leaderboard. [Immunefi post](https://x.com/immunefi/status/2115411377557062016)
- **7 Nov 2026:** Team posted they had moved to **4th** on the Immunefi BBP leaderboard. [post](https://x.com/bluethroat_labs/status/2119030716373832154)
- Earlier 2026 posts describe additional confirmed Immunefi findings (including a medium, a low they accepted, and a report the project re-opened and confirmed themselves). Root causes were not public.

Their site's public scoreboard also mentions, at a high level, "Signed Execute Messages Could Authorize Attacker Code to Read Secret Network Contract State" — no full writeup was fetched in this pass.
