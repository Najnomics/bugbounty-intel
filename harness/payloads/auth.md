# Payloads — auth

_Verbatim payload / request patterns extracted from findings in this repo. Nothing invented._

## 1. /./ path normalisation past a login wall into an admin console
- Researcher: @mdp_sec
- Post: https://x.com/mdp_sec/status/2120338219841544604
- Sources: `posts/mdp_sec/2026-11-11-2120338219841544604.md`, `writeups/mdp_sec/bug-bounty-hunting-prompts-readme.md`, `writeups/mdp_sec/mdpsec-home.md`, `writeups/mdp_sec/mdpsec-privacy.md`, `writeups/mdp_sec/mdpsec-security-test.md`, `writeups/mdp_sec/platform-reports.md`

```
Append /./ (also //, trailing dots, %2e) to a 403/login-gated path: /admin/./ passes the exact-match auth check then normalises to /admin at the router
```

## 2. $8,000 auth bypass on HackerOne — token signature not verified
- Researcher: @mdp_sec
- Post: https://x.com/mdp_sec/status/2118435683329310786
- Sources: `posts/mdp_sec/2026-11-05-2118435683329310786.md`, `writeups/mdp_sec/bug-bounty-hunting-prompts-readme.md`, `writeups/mdp_sec/mdpsec-home.md`, `writeups/mdp_sec/mdpsec-privacy.md`, `writeups/mdp_sec/mdpsec-security-test.md`, `writeups/mdp_sec/platform-reports.md`

```
Tamper JWT/token claims and signature (strip, alter, alg=none, self-sign) and confirm the server still accepts it
```
