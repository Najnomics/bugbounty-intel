# Payloads — sql

_Verbatim payload / request patterns extracted from findings in this repo. Nothing invented._

## 1. Unauthenticated SQL injection in a public quote flow ($4,000)
- Researcher: @mdp_sec
- Post: https://x.com/mdp_sec/status/2120066429223317560
- Sources: `posts/mdp_sec/2026-11-10-2120066429223317560.md`, `writeups/mdp_sec/bug-bounty-hunting-prompts-readme.md`, `writeups/mdp_sec/mdpsec-home.md`, `writeups/mdp_sec/mdpsec-privacy.md`, `writeups/mdp_sec/mdpsec-security-test.md`, `writeups/mdp_sec/platform-reports.md`

```
POST JSON to the public /retrieve endpoint; inject into the reflected field; stage a record under a controlled reference; GET the reference back to read DB-evaluated columns (second-order / write-then-read-back)
```
