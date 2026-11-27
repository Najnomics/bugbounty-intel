# How I Got My First Reflected XSS Bug Bounty!

- **Source URL:** https://papa-hecker.medium.com/how-i-got-my-first-reflected-xss-bug-bounty-c9020081c64e?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20230111225143/https://papa-hecker.medium.com/how-i-got-my-first-reflected-xss-bug-bounty-c9020081c64e
- **Fetched:** 2026-11-27
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/1250 (id 1250)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# How I Got My First Reflected XSS Bug Bounty!

it was way back in 2016 and i was new to this bug bounty thing, alot has changed since then

i saw a disclosed report regarding open redirect on a public program on hackerone website and also there was other disclosed bug regarding XSS too, so i opened the open redirect bug and made an account on the website of the scope of program

and in the other tab i opened bunch of XSS report

the open redirect bug was having a POC like this

`https://www.example.com/account?redirect=EvilDomain.com`
i simply opened my burp suite and sent the request in intruder with sniper payload of list of 500 XSS payloads

in one of them i got 200 OK and there was xss vulnerability

the program rewarded me with bounty
