# HackerOne Hacktivity — all publicly disclosed reports

Captured 2026-11-12 (Africa/Lagos): **12,754 of 12,754** reports that HackerOne's public Hacktivity index lists as disclosed (2013-12 → 2026-11-13), 0 fetch failures. State and cursor: [`data/h1_state.json`](../data/h1_state.json).

- 10,008 have the reporter's **full original report** (`vulnerability_information`) public.
- 2,746 are "limited disclosure": only the team/researcher summaries are public; those summaries are stored in full. Nothing beyond what HackerOne publishes is available.
- 278 also exist as fetched writeups in `writeups/telegram-dailybountywriteup/` (marked in each report header).

## Files

| Path | Contents |
| --- | --- |
| `data/h1/disclosed_<year>.jsonl` | One JSON object per report: `id url title program program_name state substate severity_rating severity(score/metrics) weakness(id,name,CWE) asset(structured scope) reporter bounty formatted_bounty has_bounty created_at submitted_at disclosed_at cve_ids visibility vote_count vulnerability_information summaries[category,author,content,updated_at,attachments] attachments original_report_id` |
| `hackerone/reports/<year>/<id>.md` | Readable report: header metadata, every public summary, then the original report verbatim |
| `hackerone/BY_WEAKNESS.md` | All reports grouped by HackerOne weakness, sorted by bounty |
| `hackerone/BY_PROGRAM.md` | All reports grouped by program |
| `hackerone/TOP_BOUNTIES.md` | Top 500 by bounty |
| `harness/payloads/h1-*.md` | Verbatim code blocks / raw HTTP requests from the top 40 reports per bug class |
| `harness/findings.jsonl` | records with `"source":"hackerone-hacktivity"` (600 top reports) |

Year = disclosure year. Bounty amounts are as published by HackerOne; reports with hidden bounties show `none/undisclosed`.

## Search tips

- `rg -l -i 'request smuggling' hackerone/reports/` · `jq -c 'select(.weakness.name=="Server-Side Request Forgery (SSRF)") | {id,title,bounty}' data/h1/*.jsonl`
- By program: `rg '"program":"gitlab"' data/h1/`; by reporter: `rg '"reporter":"<username>"' data/h1/`; with CVE: `jq -c 'select(.cve_ids|length>0)|{id,cve_ids}' data/h1/*.jsonl`.

## Daily incremental procedure

1. Enumerate new disclosures: POST `https://hackerone.com/graphql` with `search(index: CompleteHacktivityReportIndex, query_string: "disclosed:true AND disclosed_at:[<last_disclosed_at date> TO <today>]", sort: {field: disclosed_at, direction: ASC}, from, size:100)` (`tools/intel-pipeline/h1_enum.py`; windows must stay < 10,000 results).
2. Fetch each new id from `https://hackerone.com/reports/<id>.json` (`h1_fetch.py`; ≤ 6 threads, 60 s pause on HTTP 429, failures to `failed.jsonl`).
3. `h1_build.py` (rewrites shards, markdown, indexes), then `h1_harness.py` (appends only new findings), update `data/h1_state.json` (`write_state.py`), commit, push.
4. Re-disclosures/edits: reports already captured are re-fetched only if HackerOne shows a newer `disclosed_at`.
