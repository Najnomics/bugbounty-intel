# $300 Bounty

- **Source URL:** https://medium.com/h7w/300-bounty-limited-lfi-via-markdown-in-gsa-dashboard-34aee1b2de23?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250822105148/https://medium.com/h7w/300-bounty-limited-lfi-via-markdown-in-gsa-dashboard-34aee1b2de23
- **Fetched:** 2026-11-21
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/10270 (id 10270)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
Member-only story

# **$300 Bounty: Limited LFI via Markdown in GSA Dashboard**

## How a Minor Local File Inclusion Could Open the Door for Future Exploits

# Introduction

Insecure user input handling often leads to severe vulnerabilities — even when initial exploitation seems limited. This write-up explores a Local File Inclusion (LFI) vulnerability discovered in the [GSA Project Open Data Dashboard](https://labs.data.gov/), where improper sanitization of a markdown-based file path allowed attackers to read unintended files within the application root.

Although this LFI was constrained by the `.md` file extension, it provides a critical lesson: \*“low risk” bugs today can be *high impact* in chained or future attack scenarios. Let’s dive into the discovery, exploitation steps, and why such a vulnerability should never be overlooked.

# Vulnerability Overview

- **Vulnerability Type:** Limited Local File Inclusion (LFI)
- **Affected Parameter:** `Docs/index/$page`
- **Reporter:** mariuszdeepsec
- **Bounty Program:** GSA Bounty
- **Severity:** Low (but potentially escalatable)

# Root Cause

The `index` function in the `Docs` class builds a file path by concatenating user input into…
