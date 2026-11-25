# CTF Writeup — MarkdownSmartPreview (EJS SSTI) — Steps & PoC

- **Source URL:** https://medium.com/@8wv/ctf-writeup-markdownsmartpreview-ejs-ssti-steps-poc-4eb2670c8db7?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20251104140506/https://medium.com/@8wv/ctf-writeup-markdownsmartpreview-ejs-ssti-steps-poc-4eb2670c8db7?source=rss------bug_bounty-5
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/11549 (id 11549)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# CTF Writeup – MarkdownSmartPreview (EJS SSTI) – Steps & PoC

1 min readOct 26, 2025

## Intro

I worked on the **MarkdownSmartPreview** CTF challenge — a Markdown preview feature that supports “smart variables.” That hinted at server-side template processing. I identified an SSTI (Server-Side Template Injection) in an **EJS** template and used a practical, obfuscated PoC to read the flag.

## Steps (practical)

1. Recon: found `POST /post/preview` and the note “This preview supports smart variables.”
2. Identify engine: confirmed the template engine is **EJS**.
3. Plan: use `constructor` → `global.process.mainModule.require` to get `child_process` or `fs`.
4. Bypass WAF: the app blocks literal keywords (`require`, `process`, `cat`, `fs`), so build those strings at runtime (e.g. `String.fromCharCode(...)` or `['r','e','q'].join('')`).
5. Read flag: execute `base64 /flag.txt` (since `cat` was blocked), capture base64 output, decode locally.

## PoC (short note)

Used an EJS payload that builds sensitive identifiers with `String.fromCharCode` and runs `base64 /flag.txt`, printing the base64 result with `<%- ... %>` so output isn’t escaped. (Put full PoC in the article body — obfuscated to evade trivial filters.)

## Result

Decoded output:

`FlagY{be3903f6b50395022c57377f455e88a6}`
## Quick fixes (one-liners)

- Disable execution of user-controlled templates or sandbox the template environment.
- Remove access to `Function`/`constructor` and block `require` inside template context.
- Run services with least privilege and restrict filesystem access.
