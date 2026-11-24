# @Rhynorater

Compiled 11 Nov 2026 (WAT). Full verbatim post text lives under [`posts/Rhynorater/`](../posts/Rhynorater/).

| Field | Value |
| --- | --- |
| X | [@Rhynorater](https://x.com/Rhynorater) (user id 4002483725, joined 2015-10-20) |
| Name (profile) | Justin Gardner |
| Followers (11 Nov 2026) | 38819 |
| Bio (verbatim) | Christian / Full-time Bug Bounty Hunter / Host of @ctbbpodcast / Advisor @CaidoIO / 4x LHE MVH / 🗣️ English, 日本語 / DM for S-tier Web, IoT, or AI Pentests |
| Specialty | Web |
| Platforms | HackerOne (4x LHE MVH, bio), Bugcrowd |
| Evidence of valid finds | Host of Critical Thinking Bug Bounty podcast. |

## Key findings and analysis

_No single post in this capture describes a specific vulnerability in enough detail for a root-cause write-up; see the posts list and writeups below._

## All captured posts (verbatim files)

- 2026-09-30 — I have an inside source, you're gonna wanna watch this hacker closely - crazy stuff going on. — [`posts/Rhynorater/2026-09-30-2105317588947664972.md`](../posts/Rhynorater/2026-09-30-2105317588947664972.md) · https://x.com/Rhynorater/status/2105317588947664972
- 2026-10-01 — Lupin and the squad are killing it in bug bounty using supply chain attacks. — [`posts/Rhynorater/2026-10-01-2105716901423001866.md`](../posts/Rhynorater/2026-10-01-2105716901423001866.md) · https://x.com/Rhynorater/status/2105716901423001866
- 2026-08-28 — I have actually been seeing really fast triage from both HackerOne and Bugcrowd lately. Seems like the backlog — [`posts/Rhynorater/2026-08-28-2093394741391999198.md`](../posts/Rhynorater/2026-08-28-2093394741391999198.md) · https://x.com/Rhynorater/status/2093394741391999198
- 2026-10-12 — Absolutely insane it was that easy. — [`posts/Rhynorater/2026-10-12-2109612141640622298.md`](../posts/Rhynorater/2026-10-12-2109612141640622298.md) · https://x.com/Rhynorater/status/2109612141640622298
- 2026-10-08 — I just told my AI agent to write "colloquially" when it writes the report and holy crap. It's perfect. — [`posts/Rhynorater/2026-10-08-2108216951160058341.md`](../posts/Rhynorater/2026-10-08-2108216951160058341.md) · https://x.com/Rhynorater/status/2108216951160058341

## Writeups saved (full text)

- None fetched in this pass.

## Key findings (mined into harness)

_Auto-maintained from `harness/findings.jsonl`. 1 finding(s). Full verbatim posts under `posts/Rhynorater/`._

- **8 high-impact IDORs + SSRF after bypassing SSL pinning, APK hash verify, root detection** (`mobile`)
  - post: https://x.com/Rhynorater/status/1068037889186037770
  - local: `posts/Rhynorater/ARCHIVE.md`, `data/x_posts.jsonl`

### Depi OpenAI Codex prompt-injection → npm supply chain (quoted) — 11 Nov 2026

- Quote post: https://x.com/Rhynorater/status/2120539019427889278 — [`posts/Rhynorater/2026-11-11-2120539019427889278.md`](../posts/Rhynorater/2026-11-11-2120539019427889278.md)
- Full writeup: [`writeups/Rhynorater/depi-backdooring-codex.md`](../writeups/Rhynorater/depi-backdooring-codex.md)
- **Bug class:** Prompt injection → Codex sandbox escape (CoreCLR debug pipes) → Actions secret theft → cache poison → `@openai/codex` npm control. Initial Bugcrowd bounty $1,000 (under further review).

## Daily update 2026-11-17

### Quoted: OAuth ATO via redirect_uri=android-app:// (High 8.1, H1) (2026-11-16)

- Post: https://x.com/Rhynorater/status/2122339336163090519 — verbatim: [`posts/Rhynorater/2026-11-16-2122339336163090519.md`](../posts/Rhynorater/2026-11-16-2122339336163090519.md)
- **Bug class:** OAuth redirect_uri validation bypass with non-HTTP scheme (`android-app://`) → code/token theft → ATO
- **Root cause:** Authorization server accepted an `android-app://` redirect; per the triage note in @rgjny_'s screenshot it "works without any app installed and the attack only takes a link". Full report not public.
- **How it was found:** Original finder @rgjny_ (quoted); Rhynorater flagged the scheme as new to him.
- **Takeaways / harness:** Add `android-app://`, `intent://`, `ios-app://` and target custom schemes to every redirect_uri fuzz list; signal = 302 carrying code/token to the alternate scheme.



### Update 2026-11-20

- **Prompt-injection in own reports to stop AI false-dupes** — https://x.com/Rhynorater/status/2123457669428076895 — embeds truthful "AI, these are not dupes" disambiguation for LLM triage. [`posts/Rhynorater/2026-11-19-2123457669428076895.md`](../posts/Rhynorater/2026-11-19-2123457669428076895.md). Also #Prompt2pwn/#NahamCon2026 ("Pwned Meta already") [`posts/Rhynorater/2026-11-19-2123466608140005688.md`](../posts/Rhynorater/2026-11-19-2123466608140005688.md).

## 2026-11-24 — GPT-5.6 Sol deprecation: "We need this for Cyber"
- **Local:** [posts/Rhynorater/2026-11-24-2125041911744414065.md](../posts/Rhynorater/2026-11-24-2125041911744414065.md)
