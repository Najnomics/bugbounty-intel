# @galnagli

Compiled 11 Nov 2026 (WAT). Full verbatim post text lives under [`posts/galnagli/`](../posts/galnagli/); full writeups under [`writeups/galnagli/`](../writeups/galnagli/).

| Field | Value |
| --- | --- |
| X | [@galnagli](https://x.com/galnagli) (user id 1205537370331918336, joined 2019-12-13) |
| Name (profile) | Nagli |
| Followers (11 Nov 2026) | 48578 |
| Bio (verbatim) | hacker; head of offensive ai @wiz_io, now at @google; agentic pentesting, post-training & gemini cyber; $3,000,000 bug bounty hunter; arsenal |
| Specialty | Web / AI pentesting |
| Platforms | HackerOne, Bugcrowd ($3M+ per bio); Wiz Research |
| Evidence of valid finds | php2shell PHP core RCE (writeups/galnagli/wiz-php2shell-php-rce.md). |

## Key findings and analysis

### Critical PHP RCE (php2shell)

- Post: https://x.com/galnagli/status/2112902206152167640 — verbatim: [`posts/galnagli/2026-10-21-2112902206152167640.md`](../posts/galnagli/2026-10-21-2112902206152167640.md)
- **Bug class:** RCE in PHP core
- **Root cause:** See writeup.
- **How it was found:** —
- **Takeaways:** —

## All captured posts (verbatim files)

- 2026-10-22 — It took 17 minutes to turn the Gitlab RCE to a working HEAP exploit using Gemini 4 Argon and the advisory, the — [`posts/galnagli/2026-10-22-2113185093871095893.md`](../posts/galnagli/2026-10-22-2113185093871095893.md) · https://x.com/galnagli/status/2113185093871095893
- 2026-10-21 — As the embargo is now lifted, find all the information needed on  - the critical RCE vulnerability our researc — [`posts/galnagli/2026-10-21-2112902206152167640.md`](../posts/galnagli/2026-10-21-2112902206152167640.md) · https://x.com/galnagli/status/2112902206152167640
- 2026-11-10 — Gemini 4 Carbon is now publicly available - It's the world SOTA model on ExploitGym and pentesting. We used th — [`posts/galnagli/2026-11-10-2120191027525067042.md`](../posts/galnagli/2026-11-10-2120191027525067042.md) · https://x.com/galnagli/status/2120191027525067042
- 2026-10-27 — woke up to this page on my lovely php honeypot :( — [`posts/galnagli/2026-10-27-2115095994811732269.md`](../posts/galnagli/2026-10-27-2115095994811732269.md) · https://x.com/galnagli/status/2115095994811732269
- 2026-09-24 — Today we're launching Scan for Good in partnership with @GoogleDeepMind. — [`posts/galnagli/2026-09-24-2103111505860497685.md`](../posts/galnagli/2026-09-24-2103111505860497685.md) · https://x.com/galnagli/status/2103111505860497685

## Writeups saved (full text)

- [`writeups/galnagli/wiz-php2shell-php-rce.md`](../writeups/galnagli/wiz-php2shell-php-rce.md)

## Key findings (mined into harness)

_Auto-maintained from `harness/findings.jsonl`. 5 finding(s). Full verbatim posts under `posts/galnagli/`._

- **Critical PHP RCE (php2shell)** (`RCE in PHP core`)
  - post: https://x.com/galnagli/status/2112902206152167640
  - local: `posts/galnagli/2026-10-21-2112902206152167640.md`, `writeups/galnagli/wiz-php2shell-php-rce.md`
- **OpenAI ChatGPT critical account takeover — view chats + billing (fixed)** (`auth-bypass`)
  - post: https://x.com/galnagli/status/1646550421123522560
  - local: `posts/galnagli/ARCHIVE.md`, `data/x_posts.jsonl`
- **DoD website IDOR → account takeover (blog writeup)** (`idor-bola`)
  - post: https://x.com/galnagli/status/1325073898401107969
  - local: `posts/galnagli/ARCHIVE.md`, `data/x_posts.jsonl`
- **$20,000 OAuth bug (live hacking event) — lab replica with NahamSec/HackingHub** (`oauth`)
  - post: https://x.com/galnagli/status/1762153856127930493
  - local: `posts/galnagli/ARCHIVE.md`, `data/x_posts.jsonl`
  - bounty: $20,000
- **wiz-php2shell-php-rce** (`xss`)
  - post: https://www.wiz.io/blog/php2shell-php-rce
  - local: `writeups/galnagli/wiz-php2shell-php-rce.md`

### Update 2026-11-18

- **CVE-2026-21601 (Jira Service Management DC, BASM)** — https://x.com/galnagli/status/2122787201176019399 — [`posts/galnagli/2026-11-17-2122787201176019399.md`](../posts/galnagli/2026-11-17-2122787201176019399.md); advisory [`writeups/galnagli/atlassian-JSDSERVER-16892-CVE-2026-21601.md`](../writeups/galnagli/atlassian-JSDSERVER-16892-CVE-2026-21601.md); Wiz Scan for Good [`writeups/galnagli/wiz-scan-for-good-critical-ai-exposures.md`](../writeups/galnagli/wiz-scan-for-good-critical-ai-exposures.md). Pre-auth act-as-another-user; reported via Atlassian bug bounty; request details not public.
