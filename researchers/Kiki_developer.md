# @Kiki_developer — Kiki

- X: [https://x.com/Kiki_developer](https://x.com/Kiki_developer) (id `1545461069568622593`, created 8 Jul 2022)
- Bio (Nov 2026): Independent security researcher; prev @GuardianAudits; "$3B+ secured • 50+ audits • 15+ bounties"
- Portfolio: [github.com/devNamedKiki/Audits](https://github.com/devNamedKiki/Audits) (README fetched Nov 2026 now says 4+ years, **80+ audits**, 15+ bounties)
- Sherlock: [CodingNameKiki](https://audits.sherlock.xyz/watson/CodingNameKiki) — search snippet: 6 high / 1 medium total, 10 solo findings, $10.21K contest earnings, 37 payouts, #671 all-time (contest page; bounty work is separate)
- Medium: [8 Common Smart Contract Vulnerabilities…](https://medium.com/@kiki.auditor/8-common-smart-contract-vulnerabilities-found-throughout-audit-contest-d8f19c494f7e)
- Platforms: Immunefi, Sherlock, Code4rena, private audit firms (Enigma Dark, Cyfrin, Bail Security, Burra Sec, Guardian Audits)
- Focus: Smart contracts / DeFi (lending, perps, options, LSTs, vaults, oracles)

Most recent X posts are professional, not writeups. The GitHub bounty folder and the 2024 Medium article are the technical meat. Several bounty files still say "Write up coming someday."

## Findings with technical detail

### 1. Missing access control on the liquidation-threshold function

- **Title:** Attacker Can Liquidate all healthy positions
- **Platform / program:** Undisclosed (listed under Bug Bounties, February 2024, Perpetual, Critical)
- **Severity:** Critical (author's table)
- **Bounty:** Undisclosed
- **Bug class:** Missing access control / authorization on a risk-parameter setter
- **Root cause:** Users could permissionlessly leverage-borrow from vaults and liquidate others. Healthy positions should have been safe, but **access control was missing on the function that set the liquidation threshold**. Anyone could change the threshold so that healthy positions looked underwater and became liquidatable.
- **How found:** Not described beyond the protocol's permissionless liquidation design.
- **PoC:** Not in the public file.
- **Takeaways:** On perps/lending, treat every function that changes risk parameters (thresholds, LTVs, oracles, fees) as admin-grade, even if it "only" returns or adjusts a number. Ask: who can change the definition of "unhealthy"?
- **Source:** [Bounties/013.md](https://raw.githubusercontent.com/devNamedKiki/Audits/main/Bounties/013.md); indexed in the [Audits README](https://github.com/devNamedKiki/Audits)

### 2. Forgotten privileged old contract bypassed cooldown restrictions

- **Title:** (from an X post, not a standalone writeup)
- **Platform:** A bounty program; protocol undisclosed
- **Severity / bounty:** Undisclosed
- **Bug class:** Forgotten privileged asset / leftover access control
- **Root cause:** "A protocol forgot that they gave an old contract privileged access to one of their functions which allowed anyone to bypass their cooldown restrictions." He believed it had been left vulnerable for a couple of years. "It wasn't a complex bug"; he only found it because the privileged relationship was still live.
- **Takeaways:** Inventory every address that still has a privileged role, including deprecated contracts. Time-based restrictions (cooldowns, vesting, withdrawal delays) are only as strong as the functions that can skip them.
- **Source:** 29 Jan 2026 18:24 WAT — [post](https://x.com/Kiki_developer/status/2016925457271361718)

### 3. Immunefi medium-severity payout (Jan 2026)

- **Platform:** Immunefi
- **Severity:** Medium (he later replied "Just a medium. Not the best payout ever but best experience")
- **Bounty:** Amount undisclosed; he praised the program for fixing quickly, paying fairly, and sending updates
- **Bug class / method:** Undisclosed
- **Sources:** 29 Jan 2026 16:38 WAT [paid post](https://x.com/Kiki_developer/status/2016898778209669412) (Immunefi share card: medium, paid); follow-up [30 Jan 2026](https://x.com/Kiki_developer/status/2017310553140826310)

## Other public bounty titles (writeups incomplete or missing)

From the GitHub README bounty table. Use as a checklist of patterns he has actually been paid or credited for, not as verified root causes unless a file exists:

| Title (author) | Date | Area | Sev. | Writeup |
| --- | --- | --- | --- | --- |
| Miscalculation Continuesly Locks Funds in Vault | Aug 2025 | Vault | Medium | [018.md](https://github.com/devNamedKiki/Audits/blob/main/Bounties/018.md) — not fetched in full |
| Artificial Deflation of State Variable Will Lock Funds | Aug 2025 | Vault | High | [017.md](https://raw.githubusercontent.com/devNamedKiki/Audits/main/Bounties/017.md) — "Write up coming someday" |
| Pool Funds can be Siphoned to External Protocol | May 2025 | Leveraged trading | Critical | [016.md](https://raw.githubusercontent.com/devNamedKiki/Audits/main/Bounties/016.md) — "Write up coming someday" |
| Attacker Can Brick Operations In and Out of GMX V2 | Jan 2024 | Lending & borrowing | Medium | 007.md |
| Attacker Can lock all funds | Feb 2024 | Perpetual | Medium | 015.md |
| First Depositor Can Steal Funds From Vault | Nov 2023 | Derivatives | Medium | 003.md |
| Reward tokens Can be Locked | Jan 2024 | Yield aggregator / LST | Medium | 012.md |
| Attacker Can Steal From Options Writers | Aug 2023 | Options | High | 006.md |
| Attacker Can DoS the Settlement of Options | Aug 2023 | Options | High | 005.md |
| Attacker Can Buy Option for 0 Premium | Aug 2023 | Options | High | 004.md |
| Attacker Can Steal Funds With Elastic Supply Tokens | Jun 2023 | Staking launchpad | Low | 002.md |

## Methodology article (not a single bounty)

In Feb 2024 he published a high-level list of common contest findings and the questions he asks: reentrancy (CEI; which functions make external calls and which state they share), DoS (unbounded loops, attacker-inflated arrays, strict conditions that can be broken), `delegatecall` (who controls the target address), unchecked external calls, race conditions / ERC-20 approve races, flash-loan price manipulation, oracle edge cases, and overflow/underflow / unsafe downcasting.

**Source:** [Medium, 1 Feb 2024](https://medium.com/@kiki.auditor/8-common-smart-contract-vulnerabilities-found-throughout-audit-contest-d8f19c494f7e)

## Key findings (mined into harness)

_Auto-maintained from `harness/findings.jsonl`. 2 finding(s). Full verbatim posts under `posts/Kiki_developer/`._

- **8 Common Smart Contract Vulnerabilities Found Throughout Audit Contest** (`smart-contract`)
  - post: https://medium.com/@kiki.auditor/8-common-smart-contract-vulnerabilities-found-throughout-audit-contest-d8f19c494f7e
  - local: `writeups/Kiki_developer/8-common-smart-contract-vulnerabilities-found-throughout-audit-contest.md`
- **bounty-013** (`smart-contract`)
  - post: https://raw.githubusercontent.com/devNamedKiki/Audits/main/Bounties/013.md
  - local: `writeups/Kiki_developer/bounty-013.md`
