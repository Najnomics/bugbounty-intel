# SQL / NoSQL / command injection

_Harness check spec. Every signal, payload and automation note below is drawn from the cited local files (full verbatim text under `posts/` and `writeups/`). Nothing here is invented; where a source only states a pattern, no concrete payload is asserted._


## Detection signals
- A field is concatenated into a query; its value comes back evaluated by the DB (write-then-read-back / second-order).
- Error messages, boolean/time differences on injected input.

## Priority note (important, from source)
- Marius du Preez demotes *systematic parameter fuzzing for SQLi/NoSQLi/command/CSV injection*: across his last 100 reports / ~107 hours it produced **zero** confirmed origins, so it is opportunistic-only, on already-surfaced params, after everything higher. Source: Marius du Preez's sweep class matrix: [`writeups/mdp_sec/prompts/phases/phase-02-sweep.md`](../../writeups/mdp_sec/prompts/phases/phase-02-sweep.md) (Injection, demoted subset). The high-value SQLi he did find was a **logic/second-order** path, not blind fuzzing.

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

