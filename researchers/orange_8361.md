# @orange_8361

Compiled 11 Nov 2026 (WAT). Full verbatim post text lives under [`posts/orange_8361/`](../posts/orange_8361/); full writeups under [`writeups/orange_8361/`](../writeups/orange_8361/).

| Field | Value |
| --- | --- |
| X | [@orange_8361](https://x.com/orange_8361) (user id 179885363, joined 2010-08-18) |
| Name (profile) | Orange Tsai  🍊 |
| Followers (11 Nov 2026) | 67015 |
| Bio (verbatim) | This is 🍊 |
| Specialty | Web / Pwn2Own |
| Platforms | Pwn2Own (DEVCORE); historic MSRC/Exchange findings |
| Evidence of valid finds | Pwn2Own logic-bug full chains; OSEE; Phrack "Art of PHP" (fetch failed — JS-rendered). |
| Links | https://blog.orange.tw |

## Key findings and analysis

### Logic-bugs-only full chain

- Post: https://x.com/orange_8361/status/2054906050143240399 — verbatim: [`posts/orange_8361/2026-05-14-2054906050143240399.md`](../posts/orange_8361/2026-05-14-2054906050143240399.md)
- **Bug class:** Logic bug exploit chain
- **Root cause:** See post and blog (writeups/orange_8361/2026-10-browser-full-chain.md).
- **How it was found:** —
- **Takeaways:** Full chains without memory corruption are possible by chaining logic flaws.

## All captured posts (verbatim files)

- 2026-05-14 — That's my chain — a full chain w/ logic bugs only! No memory corruption, no AI, and of course no collisions at — [`posts/orange_8361/2026-05-14-2054906050143240399.md`](../posts/orange_8361/2026-05-14-2054906050143240399.md) · https://x.com/orange_8361/status/2054906050143240399
- 2026-10-29 — Just dropped a new blog post! 🔥 — [`posts/orange_8361/2026-10-29-2115654457694490902.md`](../posts/orange_8361/2026-10-29-2115654457694490902.md) · https://x.com/orange_8361/status/2115654457694490902
- 2026-05-15 — And this one is human insight w/ LLM-assisted research. Took about one week to finish everything. The AI reall — [`posts/orange_8361/2026-05-15-2055330289652539850.md`](../posts/orange_8361/2026-05-15-2055330289652539850.md) · https://x.com/orange_8361/status/2055330289652539850
- 2025-06-02 — I don't have OSCP—instead, I have OSEE! 🎉 — [`posts/orange_8361/2025-06-02-1929535084316811626.md`](../posts/orange_8361/2025-06-02-1929535084316811626.md) · https://x.com/orange_8361/status/1929535084316811626
- 2025-08-20 — Turns out my #PHRACK article is live! 🔥 — [`posts/orange_8361/2025-08-20-1958068417753411638.md`](../posts/orange_8361/2025-08-20-1958068417753411638.md) · https://x.com/orange_8361/status/1958068417753411638

## Writeups saved (full text)

- [`writeups/orange_8361/2026-10-browser-full-chain.md`](../writeups/orange_8361/2026-10-browser-full-chain.md)

## Key findings (mined into harness)

_Auto-maintained from `harness/findings.jsonl`. 3 finding(s). Full verbatim posts under `posts/orange_8361/`._

- **Logic-bugs-only full chain** (`Logic bug exploit chain`)
  - post: https://x.com/orange_8361/status/2054906050143240399
  - local: `posts/orange_8361/2026-05-14-2054906050143240399.md`, `writeups/orange_8361/2026-10-browser-full-chain.md`
- **Jenkins pre-auth RCE (with Overall/Read) — chains with CVE-2018-1000861 to no-ACL RCE** (`auth-bypass`)
  - post: https://x.com/orange_8361/status/1075492505657925632
  - local: `posts/orange_8361/ARCHIVE.md`, `data/x_posts.jsonl`
- **2026-10-browser-full-chain** (`web`)
  - post: https://blog.orange.tw/posts/2026-10-the-last-proof-of-human-craft-browser-full-chain/
  - local: `writeups/orange_8361/2026-10-browser-full-chain.md`
