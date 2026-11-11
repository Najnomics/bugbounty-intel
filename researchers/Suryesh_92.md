# @Suryesh_92 — Dhananjay Kumar Suryesh

- X: [https://x.com/Suryesh_92](https://x.com/Suryesh_92) (id `1761704057029226497`, created 25 Feb 2024)
- Display name: Suryesh
- Site / content: [hackwithsuryesh.netlify.app](https://hackwithsuryesh.netlify.app/), [Medium](https://hackwithsuryesh.medium.com/), [YouTube @hackwithsuryesh](https://youtube.com/@hackwithsuryesh)
- LinkedIn (from web search): Dhananjay Kumar Suryesh
- Platforms: Posts and hashtags name HackerOne, Bugcrowd, and Intigriti; specific program names are often undisclosed
- Focus: **Thick-client / desktop apps** (2026 RCEs), plus web (XSS, file upload, BAC, 2FA bypass, dependency confusion, third-party search keys)

He is the seed hunter who consistently works a niche most people skip. Several older Medium writeups have real technical detail; the 2026 thick-client RCEs do not, yet, in public.

## Findings with technical detail

### 1. Overprivileged Algolia API key in frontend JavaScript — $1,000 P2

- **Title:** Algolia API Key Exploitation leads to $1000 Bounty (P2) on private program
- **Platform / program:** Private program (platform undisclosed)
- **Severity:** P2 (author)
- **Bounty:** $1,000
- **Bug class:** Overprivileged third-party API key / broken access control on a search backend
- **Root cause:** An Algolia key shipped in `main.js`. Keys can carry ACLs such as `listIndexes`, `editSettings`, `addObject`, or `deleteObject`. A key that can list indexes may expose internal documents; `editSettings` can be abused to change how search results are rendered (the writeup describes this as a path to script injection in the search UI). A search-only key is much lower impact.
- **How it was found:** Reading frontend JS, then checking the key's ACL and indexes against Algolia's API.
- **PoC:** The writeup includes command-line examples; the full verbatim text is now stored in this repo under `posts/` (see the post file linked from this researcher index).
- **Takeaways:** Treat third-party keys in JS as credentials. Check the actual ACL, not just that "a search key is supposed to be public." Do not demonstrate impact by deleting indexes — he explicitly says programs prohibit destructive PoCs.
- **Sources:** [Medium](https://hackwithsuryesh.medium.com/algolia-api-key-exploitation-leads-to-1000-bounty-p2-on-private-program-2e147f052ff0) (11 Feb 2025). Report 14 Jun 2024, rewarded 30 Jun 2024, triaged 3 Jul 2024 (dates as in the post).

### 2. Dependency confusion leading to code execution and local file read

- **Title:** How I Chained RCE Via Dependencies Confusion to LFI
- **Platform / program:** Undisclosed
- **Severity:** Author describes impact as critical if a hostile package is installed in a build
- **Bounty:** Undisclosed in the writeup
- **Bug class:** Dependency confusion / supply chain, chained to local file read
- **Root cause:** A private package name appeared in manifest/lock/debug files (`package.json`, `package-lock.json`, `yarn.lock`, npm/yarn logs) but was not reserved on the public npm registry. Installers that resolve the public registry first can be tricked into fetching an attacker-controlled package of the same name (often at a higher version). A `preinstall` script then runs in the build or developer environment. He showed that the same hook can also read local files.
- **How it was found:** Hunting those manifest and log paths, then checking whether the name is unpublished (`npm info` / the "Confused" tool).
- **PoC:** The writeup includes a full install-hook script; the full verbatim text is now stored in this repo under `posts/` (see the post file linked from this researcher index).
- **Takeaways:** Always inventory internal package names and verify they are claimed on public registries. Confirm impact in a controlled way; many programs want a harmless callback, not a destructive payload.
- **Sources:** [Medium](https://hackwithsuryesh.medium.com/how-i-chained-rce-via-dependencies-to-lfi-348315aa17e8) (17 Sep 2024).

### 3. Reflected XSS + client-side template injection via a polyglot, after a WAF 403

- **Title:** Rxss + CSTI In Search Field Via Polygot Payload
- **Platform / program:** A help-center style subdomain (`help.target.com` pattern); program undisclosed
- **Severity:** XSS / CSTI; the report was marked **duplicate of his own earlier report** (same payload, two XSS reports)
- **Bounty:** None (duplicate)
- **Bug class:** Reflected XSS, client-side template injection, WAF bypass
- **Root cause:** A search field reflected input. Basic XSS probes were blocked by nginx with 403. A more complex polyglot still executed in the page. He then showed that a template-style expression was evaluated (CSTI), not only a script sink.
- **How it was found:** Start with simple probes, don't leave after 403, try polyglots, then test whether the sink is also a client-side template.
- **PoC:** Payload is in the writeup; the full verbatim text is now stored in this repo under `posts/` (see the post file linked from this researcher index).
- **Takeaways:** A WAF 403 is not "not vulnerable." If two reports share a payload, expect a duplicate.
- **Sources:** [Medium](https://hackwithsuryesh.medium.com/rxss-csti-in-search-field-via-polygot-payload-65ca1a8be8ba) (29 Oct 2024).

### 4. File upload to stored XSS, double MIME type — $1,000

- **Title:** (from the post) File upload to stored XSS
- **Platform / program:** Undisclosed
- **Severity:** Undisclosed
- **Bounty:** $1,000 (publicly stated)
- **Bug class:** Stored XSS via file upload / MIME confusion
- **Root cause / method:** Only a short tip was published: use a double MIME type, example given as `application/pdf,text/html`. Full mechanics undisclosed.
- **Takeaways:** Upload filters that trust the Content-Type header, or that accept a list of types, may be confused by multiple MIME values.
- **Source:** 24 Jan 2026 01:19 WAT — [post](https://x.com/Suryesh_92/status/2014855434696597734)

## 2026 thick-client and other bounty posts (method undisclosed)

He has been unusually consistent on **installed desktop / thick-client** targets:

- **3 Nov 2026 13:42 WAT:** "Another new Thick Client finding accepted and rewarded" (hashtags include `#rce`). [post](https://x.com/Suryesh_92/status/2117598354641482125)
- **9 Sep 2026 15:15 WAT:** Another thick-client RCE bounty. Running tally in the post: 2 RCEs paid to him, 1 RCE given to a friend who was also paid, 3 RCEs marked duplicates of his reports. [post](https://x.com/Suryesh_92/status/2097690285799313440)
- **10 Sep 2026:** Replied that a (related) report was more than 1,200 lines, and that "thick client pentest depends on source code analysis capabilities." [post](https://x.com/Suryesh_92/status/2097850230930862237)
- **24 Jul 2026:** After multiple RCEs and other bugs with @OreoB1scuit, "they paused their bug bounty program." Program undisclosed. [post](https://x.com/Suryesh_92/status/2080593128982188513)
- **30 Jun 2026:** "Another bounty" with `#rce` hashtag. [post](https://x.com/Suryesh_92/status/2071781463767580756)
- **22 Jun 2026 14:04 WAT:** First accepted RCE, "found RCE directly in thick client"; "got lowest bounty" but first RCE. [post](https://x.com/Suryesh_92/status/2069043943640301896)

Other 2026 web claims, method undisclosed:

- **3 Feb 2026:** 2FA bypass on password change, amount given only as `$$$`. [post](https://x.com/Suryesh_92/status/2018672994436948257)
- **29 Jan 2026:** Broken access control, amount `$$$`. [post](https://x.com/Suryesh_92/status/2016865602749813209)
- **20 Jan 2026:** A bounty increased to 3500 CHF (he converted this as $4,424). [post](https://x.com/Suryesh_92/status/2013636881272184929)
- **19 Jan 2026:** First 2026 bounty, 1500 CHF (he converted as $1,877). "Impact comes from process, not luck." [post](https://x.com/Suryesh_92/status/2013196581994946685)
