# @ryotkak

Compiled 11 Nov 2026 (WAT). Full verbatim post text lives under [`posts/ryotkak/`](../posts/ryotkak/).

| Field | Value |
| --- | --- |
| X | [@ryotkak](https://x.com/ryotkak) (user id 1114004787324805120, joined 2019-04-05) |
| Name (profile) | RyotaK |
| Followers (11 Nov 2026) | 11687 |
| Bio (verbatim) | Security researcher? / Icon: @MelvilleTw / Private: @RyotaK_Private / Misskey: https://t.co/63E5Rpv2pk / Blog: https://t.co/c7NFQXhV90 |
| Specialty | Web / supply chain |
| Platforms | GMO Flatt Security; Pwn2Own entrant |
| Evidence of valid finds | Rails RCE CVE, Claude Code supply-chain bug. |
| Links | https://flatt.tech |

## Key findings and analysis

### Ruby on Rails arbitrary code execution (fixed 7.2.3.2 / 8.0.5.1 / 8.1.3.1)

- Post: https://x.com/ryotkak/status/2082484740494684250 — verbatim: [`posts/ryotkak/2026-07-29-2082484740494684250.md`](../posts/ryotkak/2026-07-29-2082484740494684250.md)
- **Bug class:** RCE
- **Root cause:** See post (Japanese).
- **How it was found:** —
- **Takeaways:** Upgrade promptly.

### Claude Code supply-chain attack

- Post: https://x.com/ryotkak/status/2061434879309664575 — verbatim: [`posts/ryotkak/2026-06-01-2061434879309664575.md`](../posts/ryotkak/2026-06-01-2061434879309664575.md)
- **Bug class:** Supply chain
- **Root cause:** See linked article.
- **How it was found:** —
- **Takeaways:** —

## All captured posts (verbatim files)

- 2026-07-29 — Ruby on Railsに深刻な脆弱性を報告し、先程修正バージョンが公開されました。一般的な構成において、任意コード実行に繋がるものです。 — [`posts/ryotkak/2026-07-29-2082484740494684250.md`](../posts/ryotkak/2026-07-29-2082484740494684250.md) · https://x.com/ryotkak/status/2082484740494684250
- 2026-07-17 — 【注意】WordPress本体において、未認証で任意コード実行に繋がる脆弱性が修正されています。 — [`posts/ryotkak/2026-07-17-2078257717983236594.md`](../posts/ryotkak/2026-07-17-2078257717983236594.md) · https://x.com/ryotkak/status/2078257717983236594
- 2026-05-08 — Does anyone have a direct contact at @thezdi? I've been trying to register my Pwn2Own entries for the past 3 w — [`posts/ryotkak/2026-05-08-2052881664909660521.md`](../posts/ryotkak/2026-05-08-2052881664909660521.md) · https://x.com/ryotkak/status/2052881664909660521
- 2026-06-01 — Claude Codeに対してサプライチェーン攻撃を行うことが可能だった脆弱性についての記事を公開しました！ — [`posts/ryotkak/2026-06-01-2061434879309664575.md`](../posts/ryotkak/2026-06-01-2061434879309664575.md) · https://x.com/ryotkak/status/2061434879309664575

## Writeups saved (full text)

- None fetched in this pass.

## Key findings (mined into harness)

_Auto-maintained from `harness/findings.jsonl`. 2 finding(s). Full verbatim posts under `posts/ryotkak/`._

- **Ruby on Rails arbitrary code execution (fixed 7.2.3.2 / 8.0.5.1 / 8.1.3.1)** (`RCE`)
  - post: https://x.com/ryotkak/status/2082484740494684250
  - local: `posts/ryotkak/2026-07-29-2082484740494684250.md`
- **Claude Code supply-chain attack** (`Supply chain`)
  - post: https://x.com/ryotkak/status/2061434879309664575
  - local: `posts/ryotkak/2026-06-01-2061434879309664575.md`
