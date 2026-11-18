# @Piki_eth — Piki

- X: [https://x.com/Piki_eth](https://x.com/Piki_eth) (id `1565300610504613888`, created 1 Sep 2022)
- Bio (Nov 2026): "full-time dev, part-time bag holder — Bug Hunter | Web3 Security"
- Platforms: HackenProof is the platform he names in 2026 posts
- Focus: Web3 (bridges, wallet-ownership proofs, protocol DoS) plus some web (SSRF)

He posts triage and payout updates more often than full writeups. When he does name a class, it is usually one line. Several reports are **triaged, not confirmed paid**.

## Findings

### 1. Permanent destruction of bridged funds via wallet-ownership proof logic

- **Platform:** HackenProof (program / project not named)
- **Severity:** Not formally labeled in the post; described as a potential vulnerability with serious impact
- **Bounty:** Undisclosed as of the post (triaged / escalated, not "paid")
- **Bug class:** Bridge / wallet-ownership proof logic; impact described as **permanent destruction of bridged funds**
- **Root cause:** Only the one-line description above. No function names, chain, or proof scheme.
- **Status:** Under review since early September 2026; on 29 Oct 2026 he said it was triaged and escalated to the project's team.
- **Takeaways:** On bridges, "proof of wallet ownership" is a high-value surface. Ask not only "can I steal?" but "can I brick or burn funds so they cannot be withdrawn?"
- **Source:** 29 Oct 2026 13:31 WAT — [post](https://x.com/Piki_eth/status/2115783655092277530)

### 2. SSRF found with assistance from a free DeepSeek model — triaged

- **Platform:** HackenProof
- **Severity:** Undisclosed
- **Bounty:** Undisclosed ("now we wait for the bounty update")
- **Bug class:** SSRF
- **How found:** He wrote that he found the SSRF using free DeepSeek, then submitted to HackenProof; it was triaged and escalated. No target or sink details.
- **Takeaways:** Cheap/local models can surface leads, but the public post does not replace manual confirmation (he emphasizes curiosity + hacking, not blind trust in the model).
- **Source:** 26 Oct 2026 17:50 WAT — [post](https://x.com/Piki_eth/status/2114761602025304105)

### 3. DoS confirmed after a local Qwen audit run

- **Platform:** Intended for HackenProof; at the time he lacked the reputation points required to submit
- **Severity:** "Strong DoS" (author)
- **Bounty:** None at the time of the post (could not submit)
- **Bug class:** Denial of service
- **How found:** Local Qwen ran for about five hours on a crypto project; he then **manually reviewed, confirmed the root cause, and reproduced** the issue. Root cause itself was not published.
- **Takeaways:** Treat model output as a draft finding. The manual reproduction step is the actual work. Platform reputation gates can block a ready report — track program rules before spending the audit time.
- **Source:** 28 Aug 2026 07:03 WAT — [post](https://x.com/Piki_eth/status/2093217981732171978)

## Other payout / triage evidence (details undisclosed)

- **8 Nov 2026 09:36 WAT:** Another HackenProof report "TRIAGED in just 30 minutes." [post](https://x.com/Piki_eth/status/2119348331537396059)
- **7 Nov 2026 11:06 WAT:** "Another critical report TRIAGED by HackenProof." Class undisclosed. [post](https://x.com/Piki_eth/status/2119008635946930555)
- **28 Sep 2026 17:51 WAT:** "Ending September with another $1,500 bounty." Platform not named in the body. [post](https://x.com/Piki_eth/status/2104614940502094068)
- **22 Sep 2026 06:22 WAT:** "$1,000 Bounty Secured." [post](https://x.com/Piki_eth/status/2102267347876909515)
- **1 Sep 2026 19:01 WAT:** A company he had dropped a critical on invited him to a private on-demand bounty. [post](https://x.com/Piki_eth/status/2094848073256333483)
- **1 Sep 2026 15:12 WAT:** "The best notification: has been paid" (@HackenProof). [post](https://x.com/Piki_eth/status/2094790419410567631)

On 25 Sep 2026 he alleged that a "well known dex" used his critical fund report to fix an issue and then ghosted him. That is an unverified dispute, not a documented finding. [post](https://x.com/Piki_eth/status/2103571947573686427)

### Update 2026-11-18

- **Two HackenProof reports paid (details undisclosed, titles visible in screenshots)** — https://x.com/Piki_eth/status/2122570832006586557 — [`posts/Piki_eth/2026-11-17-2122570832006586557.md`](../posts/Piki_eth/2026-11-17-2122570832006586557.md): 'Unbound wallet-ownership proof → … executed destruction of bridged funds (add_wallet / action_costing_*)' and 'Ed25519 signature does not bind the executed query — last occurrence verified, first occurrence executed'.
