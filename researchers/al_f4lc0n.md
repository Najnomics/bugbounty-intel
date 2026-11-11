# @al_f4lc0n — f4lc0n

- X: [https://x.com/al_f4lc0n](https://x.com/al_f4lc0n) (id `1864143484514652164`, created 4 Dec 2024)
- Bio (Nov 2026): "I like catching bugs"
- Linked URL: [github.com/injective-wall-of-shame/bug-any-account-ordering](https://github.com/injective-wall-of-shame/bug-any-account-ordering) (fetched 11 Nov 2026; the page returned almost no technical body)
- Platforms: Immunefi; Attackathon / contest work (Stacks, XRPL)
- Focus: Cosmos-SDK / chain-level bugs

**Handle this file carefully.** He is included because of a serious, publicly described chain-level bug class and a stated contest track record. The Injective bounty itself is **disputed / unpaid per his own later posts**. Do not record $50k (or any other amount) as received for that report.

## Findings

### Injective: any user could drain any account (reported via Immunefi; payout disputed)

- **Platform:** Immunefi, target @injective (his 15 Mar 2026 post)
- **Severity:** Critical (author)
- **Stated impact:** Any user could "directly drain any account on the chain. No special permissions needed. Over $500M in on-chain assets were at risk."
- **What happened next (his account):** He reported through Immunefi. The next day a mainnet upgrade to fix the bug went to a governance vote. He says they offered $50k; he frames that as far below the stated risk. Later posts (3 Sep 2026) say that **to that day Injective still had not paid him any bug bounty**, and that a later Injective incident "has absolutely nothing to do with me."
- **Injective-side public pushback (as he quoted on 18 Mar 2026):** The figures were called misleading; "zero user funds were affected and zero addresses were compromised"; they argued a practical exploit would need several suspicious transactions with "extraordinarily limited impact."
- **His rebuttal (same thread):** On a Cosmos-based chain, a single transaction can pack multiple messages, which he says is enough to drain multiple whale accounts. He also objected to the idea that he should have exploited the bug for "real damage" to prove impact.
- **Root cause / PoC:** Not fully published in the posts reviewed (the GitHub repo name suggests an "any account ordering" bug, but the fetched page had no usable writeup).
- **Takeaways:**
  - On Cosmos-style chains, evaluate impact in terms of **multi-message transactions**, not one message at a time.
  - "No funds were actually stolen" does not automatically make a drain primitive low severity — but programs will argue about exploitability and required preconditions. Document those preconditions honestly.
  - Contest track record he listed in the same March post (treat as self-reported): #1 Attackathon | Stacks; #2 Attackathon | Stacks II; #1 Attackathon | XRPL Lending Protocol; plus 1 critical and 1 high from other bounties (not counting Injective).
- **Sources:** 15 Mar 2026 10:16 WAT [main post](https://x.com/al_f4lc0n/status/2033110168045568434); 18 Mar 2026 [response thread](https://x.com/al_f4lc0n/status/2034125406748741827); 3 Sep 2026 [later statement](https://x.com/al_f4lc0n/status/2095543489920483753)

### Other earnings claim

On 3 Sep 2026 he wrote that he had received about **$300,000** in total from bug bounties and audit contests. Not itemized.

On 3 Jun 2026 he posted angry process advice about submitting criticals to Cosmos SDK-based chains and Cosmos SDK itself (alleging reports were closed because he was a new HackerOne user). That is a complaint, not a technical writeup. [post](https://x.com/al_f4lc0n/status/2062082215962366225)

## Key findings (mined into harness)

_Auto-maintained from `harness/findings.jsonl`. 2 finding(s). Full verbatim posts under `posts/al_f4lc0n/`._

- **Injective MsgBatchUpdateOrders missing subaccount ownership check — any account drain (Critical, disputed $50K)** (`smart-contract`)
  - post: https://x.com/al_f4lc0n/status/2033110168045568434
  - local: `posts/al_f4lc0n/2026-03-15-2033110168045568434.md`
  - bounty: $50,000 (disputed / unpaid per researcher; max program Critical $500K)
- **injective-any-account-ordering-report** (`auth-bypass`)
  - post: https://raw.githubusercontent.com/injective-wall-of-shame/bug-any-account-ordering/main/report.md
  - local: `writeups/al_f4lc0n/injective-any-account-ordering-report.md`
  - bounty: $500
