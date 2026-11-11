# Sqli

_Harness check spec. Every signal, payload and automation note below is drawn from the cited local files (full verbatim text under `posts/`, `writeups/`, `projects/`). Nothing here is invented; where a source only states a pattern, no concrete payload is asserted._


_Findings in corpus for this class: **4** (see `harness/findings.jsonl`)._

## Detection signals / takeaways from sources

- When a WAF blocks SQLi, understand the DB dialect and whether verbose 500s leak data — a 500 can be an output channel. (from infinitelogins). Source: [`posts/infinitelogins/2026-10-14-2110355630133322159.md`](../../posts/infinitelogins/2026-10-14-2110355630133322159.md).
- His tip: in any "come back to your saved thing later" flow, go straight for lookup fields; if one field writes and another reads it back, treat it as an oracle. Read API specs for endpoints marked unauthenticated. (from mdp_sec). Source: [`posts/mdp_sec/2026-11-10-2120066429223317560.md`](../../posts/mdp_sec/2026-11-10-2120066429223317560.md), [`writeups/mdp_sec/bug-bounty-hunting-prompts-readme.md`](../../writeups/mdp_sec/bug-bounty-hunting-prompts-readme.md), [`writeups/mdp_sec/mdpsec-home.md`](../../writeups/mdp_sec/mdpsec-home.md).
- DB-backend-specific SQLi means Postgres scopes need different probes than MySQL. (from infosec_au). Source: [`posts/infosec_au/2026-05-21-2057484346093887921.md`](../../posts/infosec_au/2026-05-21-2057484346093887921.md).
- SQLi in file-transfer appliances often chains to RCE via DB/file write primitives. (from infosec_au). Source: [`posts/infosec_au/ARCHIVE.md`](../../posts/infosec_au/ARCHIVE.md), [`data/x_posts.jsonl`](../../data/x_posts.jsonl).

## Method / findings in sources

- **Unauthenticated BigQuery SQLi via WAF-bypassing error-channel extraction ($4,000)** — A public analytics API passed user input directly into BigQuery SQL. The WAF blocked UNION/SELECT/AND/OR but missed BigQuery scripting (IF/ASSERT) and EXECUTE/**/IMMEDIATE. Verbose HTTP 500 errors exposed query results via RAISE USING MESSAGE; REVERSE() reconstructed blocked keywords like INFORMATION_SCHEMA at runtime. Source: [`posts/infinitelogins/2026-10-14-2110355630133322159.md`](../../posts/infinitelogins/2026-10-14-2110355630133322159.md).
- **Unauthenticated SQL injection in a public quote flow ($4,000)** — A JSON field on a public "retrieve" endpoint was concatenated into a SQL string literal; the endpoint had zero auth (its own API spec said so); one shared backend table served several front ends, so the blast radius covered the whole quote system. Source: [`posts/mdp_sec/2026-11-10-2120066429223317560.md`](../../posts/mdp_sec/2026-11-10-2120066429223317560.md), [`writeups/mdp_sec/bug-bounty-hunting-prompts-readme.md`](../../writeups/mdp_sec/bug-bounty-hunting-prompts-readme.md), [`writeups/mdp_sec/mdpsec-home.md`](../../writeups/mdp_sec/mdpsec-home.md).
- **Drupal pre-auth SQLi on Postgres backend (SA-CORE-2026-004 / CVE-2026-9082)** — Pre-auth SQLi only affecting Drupal with Postgres as DB backend. SLCyberSec published writeup. Source: [`posts/infosec_au/2026-05-21-2057484346093887921.md`](../../posts/infosec_au/2026-05-21-2057484346093887921.md).
- **MOVEit Transfer SQLi → RCE (CVE-2023-34362) — Assetnote approach** — Assetnote writeup for MOVEit Transfer SQL injection to RCE; different approach from Rapid7. Source: [`posts/infosec_au/ARCHIVE.md`](../../posts/infosec_au/ARCHIVE.md), [`data/x_posts.jsonl`](../../data/x_posts.jsonl).

## Payloads / requests seen in sources

- `JSON param with `'`; boolean: `IF TRUE THEN ASSERT FALSE; END IF;` → 500 vs FALSE → 200; extract: `RAISE USING MESSAGE = <query result>`; WAF bypass: `EXECUTE/**/IMMEDIATE` and `REVERSE('AMEHCS_NOITAMROFNI')`` — Unauthenticated BigQuery SQLi via WAF-bypassing error-channel extraction ($4,000). Source: [`posts/infinitelogins/2026-10-14-2110355630133322159.md`](../../posts/infinitelogins/2026-10-14-2110355630133322159.md).
- `POST JSON to the public /retrieve endpoint; inject into the reflected field; stage a record under a controlled reference; GET the reference back to read DB-evaluated columns (second-order / write-then-read-back)` — Unauthenticated SQL injection in a public quote flow ($4,000). Source: [`posts/mdp_sec/2026-11-10-2120066429223317560.md`](../../posts/mdp_sec/2026-11-10-2120066429223317560.md), [`writeups/mdp_sec/bug-bounty-hunting-prompts-readme.md`](../../writeups/mdp_sec/bug-bounty-hunting-prompts-readme.md), [`writeups/mdp_sec/mdpsec-home.md`](../../writeups/mdp_sec/mdpsec-home.md).

See also [`../payloads/sqli.md`](../payloads/sqli.md) when present.

## Automation (check spec)

```
# Checks derived from 4 documented finding(s) in findings.jsonl for class=sqli
# try: JSON param with `'`; boolean: `IF TRUE THEN ASSERT FALSE; END IF;` → 500 vs FALSE → 200; extract: `RAISE USING MESSAGE = <query result>`; WAF bypass: `EXECUTE/*
# try: POST JSON to the public /retrieve endpoint; inject into the reflected field; stage a record under a controlled reference; GET the reference back to read DB-eval
# note: DB-backend-specific SQLi means Postgres scopes need different probes than MySQL.
# note: SQLi in file-transfer appliances often chains to RCE via DB/file write primitives.
```

## Prior harness notes (retained)

_Retained from earlier curated harness file; still cites local sources._

## Detection signals
- A field is concatenated into a query; its value comes back evaluated by the DB (write-then-read-back / second-order).
- Error messages, boolean/time differences on injected input.

## Payloads / requests seen in sources
- Unauthenticated second-order SQLi on a public quote flow: POST a JSON body to the public retrieve endpoint where one field is concatenated into a SQL string literal; stage a record under a controlled reference; GET it back and the field returns DB-evaluated columns (PII + resume tokens), $4,000. Source: [`posts/mdp_sec/2026-11-10-2120066429223317560.md`](../../posts/mdp_sec/2026-11-10-2120066429223317560.md).

## Tools
- Manual payload crafting on surfaced params; sqlmap only opportunistically. OOB listener for blind cases (Marius du Preez's sweep class matrix: [`writeups/mdp_sec/prompts/phases/phase-02-sweep.md`](../../writeups/mdp_sec/prompts/phases/phase-02-sweep.md), OOB listener section).

## Automation (check spec)
```
for field in fields_written_then_read:        # highest value
  plant = unique_sql_marker()
  write(field, plant); v = read_back(field)
  if v shows DB-evaluation (quote break, concat, subselect result): FLAG second-order-sqli
# only after higher classes:
for param in already_surfaced_params:
  opportunistic_injection(param)
```

## Related findings
- `harness/findings.jsonl`: mdp_sec second-order SQLi ($4,000).
