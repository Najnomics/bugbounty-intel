# Payloads — supply

_Verbatim payload / request patterns extracted from findings in this repo. Nothing invented._

## 1. $1,200 Bugcrowd dependency confusion
- Researcher: @mdp_sec
- Post: https://x.com/mdp_sec/status/2118803107119325691
- Sources: `posts/mdp_sec/2026-11-06-2118803107119325691.md`, `writeups/mdp_sec/bug-bounty-hunting-prompts-readme.md`, `writeups/mdp_sec/mdpsec-home.md`, `writeups/mdp_sec/mdpsec-privacy.md`, `writeups/mdp_sec/mdpsec-security-test.md`, `writeups/mdp_sec/platform-reports.md`

```
Harvest internal package names from JS bundles/manifests; publish/claim a benign package of the same name on the public registry; confirm resolution with a callback-only PoC
```
