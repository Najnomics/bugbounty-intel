# @cmichelio

Compiled 11 Nov 2026 (WAT). Full verbatim post text lives under [`posts/cmichelio/`](../posts/cmichelio/).

| Field | Value |
| --- | --- |
| X | [@cmichelio](https://x.com/cmichelio) (user id 4842942297, joined 2016-01-24) |
| Name (profile) | cmichel |
| Followers (11 Nov 2026) | 13230 |
| Bio (verbatim) | blockchain dev & security 🏹🐛 @SpearbitDAO/@cantinaxyz 🖊️  blog @ https://t.co/fEaA2KTfnb DM @cantinaxyz for audit  views are my own |
| Specialty | Web3 audits |
| Platforms | Spearbit / Cantina (bio); historically top Code4rena warden |
| Evidence of valid finds | Blog at cmichel.io; posts on oracle-median manipulation and audit methodology. |
| Links | https://cmichel.io |

## Key findings and analysis

### Median of 11 oracle sources — how many to manipulate?

- Post: https://x.com/cmichelio/status/1800463263433678945 — verbatim: [`posts/cmichelio/2024-06-11-1800463263433678945.md`](../posts/cmichelio/2024-06-11-1800463263433678945.md)
- **Bug class:** Oracle manipulation
- **Root cause:** When sources cluster tightly, moving the median needs ~half (6 of 11) sources; but if sources are spread, fewer manipulated sources can shift the median (UwU Lend context).
- **How it was found:** Reasoning about the median function on real price distributions.
- **Takeaways:** Median oracles are not automatically safe; model the actual price spread.

### Retrain yourself after every bug

- Post: https://x.com/cmichelio/status/1884541645078818897 — verbatim: [`posts/cmichelio/2025-01-29-1884541645078818897.md`](../posts/cmichelio/2025-01-29-1884541645078818897.md)
- **Bug class:** Methodology
- **Root cause:** N/A
- **How it was found:** After each find, reconstruct the minimum reasoning steps that led to it.
- **Takeaways:** Turn each finding into a faster mental pattern.

## All captured posts (verbatim files)

- 2024-06-11 — Your oracle has 11 price sources and takes the median. How many sources must you manipulate for the median to  — [`posts/cmichelio/2024-06-11-1800463263433678945.md`](../posts/cmichelio/2024-06-11-1800463263433678945.md) · https://x.com/cmichelio/status/1800463263433678945
- 2025-11-05 — the founder @0xlawlol openly admitted on the @TaikiMaeda2 podcast that their bug bounty strategy is to: — [`posts/cmichelio/2025-11-05-1985908499424166047.md`](../posts/cmichelio/2025-11-05-1985908499424166047.md) · https://x.com/cmichelio/status/1985908499424166047
- 2024-06-26 — I audit Blast, they announce a million $ competition afterwards. — [`posts/cmichelio/2024-06-26-1805973538987241905.md`](../posts/cmichelio/2024-06-26-1805973538987241905.md) · https://x.com/cmichelio/status/1805973538987241905
- 2025-01-29 — Whenever I find a bug, I look back and ask: How could I have found that faster? I go back, figure out which st — [`posts/cmichelio/2025-01-29-1884541645078818897.md`](../posts/cmichelio/2025-01-29-1884541645078818897.md) · https://x.com/cmichelio/status/1884541645078818897
- 2026-11-04 — Today was my last day at Anthropic. — [`posts/cmichelio/2026-11-04-2117938732909388206.md`](../posts/cmichelio/2026-11-04-2117938732909388206.md) · https://x.com/cmichelio/status/2117938732909388206

## Writeups saved (full text)

- None fetched in this pass.

## Key findings (mined into harness)

_Auto-maintained from `harness/findings.jsonl`. 2 finding(s). Full verbatim posts under `posts/cmichelio/`._

- **Median of 11 oracle sources — how many to manipulate?** (`Oracle manipulation`)
  - post: https://x.com/cmichelio/status/1800463263433678945
  - local: `posts/cmichelio/2024-06-11-1800463263433678945.md`
- **Retrain yourself after every bug** (`Methodology`)
  - post: https://x.com/cmichelio/status/1884541645078818897
  - local: `posts/cmichelio/2025-01-29-1884541645078818897.md`
