# $1000 Bounty

- **Source URL:** https://osintteam.blog/1000-bounty-xss-in-phabricators-editor-97fa74b24633?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250502014403/https://osintteam.blog/1000-bounty-xss-in-phabricators-editor-97fa74b24633
- **Fetched:** 2026-11-27
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/9510 (id 9510)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
Member-only story

# $1000 Bounty: XSS in Phabricator Editor

## Injecting XSS via Tag — A Story of Syntax Chaos and Nested Parsing

In the vast world of bug bounty hunting, sometimes it’s not fancy fuzzers or brute-force payloads that lead to gold — sometimes it’s a simple clever abuse of a custom feature. This is one of those times.

In this write-up I’ll walk you through how I discovered a critical Cross-Site Scripting (XSS) vulnerability in Phabricator — specifically in its editor’s handling of meme tags. This bug earned a $1000 bounty and showcased how custom parsing logic can go very wrong with just a little creativity.

## Vulnerability Summary

- Bug Type: Stored XSS via meme tag
- Target: Phabricator editor (meme tag rendering)
- Impact: Arbitrary JavaScript execution for any viewer
- Severity: High (Stored XSS affecting all users)
- Bounty Awarded: $1000
- Reported By: tunnelshade

## Exploiting : Step-by-Step

1. Find a Place with the Editor

Phabricator allows users to add memes using its {meme} tag — kind of like Markdown but for fun images. This functionality is accessible almost anywhere: comments blog…
