# CVE / advisory / exploit layer

Built 2026-11-12 (Africa/Lagos) for an agent that **cannot browse**. Everything here is the full public record copied as data; nothing is summarised or invented. Machine-readable files live under `data/`, readable markdown under `cves/`. Markers for the daily run are in [`data/cve_state.json`](../data/cve_state.json).

## Layout

| Path | What | Count (2026-11-12) |
| --- | --- | --- |
| `data/cve/all/<year>/CVE-<year>-<N>xxxx.jsonl` | **Every** CVE record 1999–2026 from CVEProject/cvelistV5 (published + rejected). Fields: `id state assigner published updated title description cwe metrics(CNA+ADP CVSS/SSVC) affected references credits solutions workarounds exploits`, joined `kev` (CISA KEV entry) and `exploitdb` (EDB ids) | 424,534 (405,375 published, 19,159 rejected) |
| `data/cve/vendors/<vendor>/<year>.jsonl` | Same full records, filtered per vendor (37 vendors: linux-kernel, php, google, google-chrome, android, apple, microsoft, mozilla, openssl, nodejs, apache, gitlab, wordpress, cisco, fortinet, ivanti, …) | see `cves/vendors/*/` headers |
| `cves/vendors/<vendor>/<year>.md` | Readable high-value subset: CVSS ≥ 7, CISA KEV, Exploit-DB PoC, or CISA SSVC exploitation active/poc | |
| `data/cve/linux-kernel-cna/<year>.jsonl` | Linux kernel CNA (git.kernel.org `vulns.git`): announcement text (`message`), `fix_commits`, `vulnerable_commits`, `dyad` (introduced-version:commit:fixed-version:commit pairs), `files` touched | 18,563 |
| `data/nvd/<year>.jsonl` | NVD analysis enrichment only (vulnStatus, every CVSS v2/v3.x/v4 metric per source, CWE, vulnerable CPE criteria with version ranges, tagged references e.g. `Exploit`, `Patch`, `Third Party Advisory`). Descriptions are in `data/cve/all` | see `data/cve_state.json` |
| `cves/kev/<year>.md` (KEV fields also joined into every `data/cve/all` record as `kev`) | CISA Known Exploited Vulnerabilities, readable, joined with the CVE record | 1,779 (catalog 2026.11.10) |
| `data/ghsa/<ecosystem>/<year>.jsonl` / `cves/ghsa/<ecosystem>/<year>.md` | GitHub Advisory Database, reviewed advisories, full OSV JSON; markdown for HIGH/CRITICAL | 37,715 |
| `data/osv/<ecosystem>/<year>.jsonl` / `cves/osv/` | OSV.dev records that are not GHSA duplicates: Android Security Bulletins, Go vulndb, PYSEC, RustSec, OSS-Fuzz, FriendsOfPHP, Hex | 23,801 |
| `data/exploitdb/<type>/<year>.jsonl` (+ `.md`) | Exploit-DB full catalog with the **exploit/PoC source code inlined** (`code`), CVE aliases, verified flag | 47,182 |
| `cves/google-project-zero/` | `blog/` 258 Project Zero posts verbatim; `itw-sheet/` 0day "In the Wild" tracking sheet (15 tabs); `0day-RCAs/` root-cause analyses | |
| `data/repo-advisories/`, `cves/repo-advisories/` | Repository security advisories: php/php-src (66), electron/electron (70), WordPress/wordpress-develop (54) | 190 |
| `data/zdi/<year>.jsonl`, `cves/zdi/<year>.md` | Zero Day Initiative published advisories: full index (vendor/product, CVE, CVSS, dates) and full advisory text where fetched | see `data/cve_state.json` → `zdi` |
| `hackerone/`, `data/h1/` | All publicly disclosed HackerOne reports — see [hackerone/README.md](../hackerone/README.md) | 12,750 |
| `harness/cve-index.md` | **Start here for patterns:** bug class / CWE → strongest KEV, verified Exploit-DB, GHSA-critical, HackerOne and Project Zero examples, each pointing at a local file | |

## How to search it (no network needed)

- One CVE: `rg -N '"id":"CVE-2024-3094"' data/cve/all/2024/` (file is `CVE-2024-3xxxx.jsonl`). NVD enrichment: `rg '"id":"CVE-2024-3094"' data/nvd/2024.jsonl`. Exploit code: `rg -l 'CVE-2024-3094' data/exploitdb/`.
- By CWE: `rg '"CWE-918' data/cve/all/2025/ | jq -c '{id,title,description}'`.
- Exploited in the wild: `rg '"kev":\{' data/cve/all/2026/` or read `cves/kev/2026.md`.
- By vendor/product: `data/cve/vendors/<vendor>/` (jsonl) or `cves/vendors/<vendor>/` (md). Kernel fix commits: `data/cve/linux-kernel-cna/`.
- Package ecosystems (npm, PyPI, Go, Maven, crates.io, Packagist …): `data/ghsa/<eco>/` then `data/osv/<eco>/`.
- Bug-class examples with PoCs: `harness/cve-index.md`, `harness/payloads/h1-*.md`, `harness/findings.jsonl`.
- Every jsonl line is one complete JSON object; files are < 50 MB each. Use `jq -c` / Python `json.loads` per line.

## Daily incremental procedure

Run from `/workspace/raw` with scripts in [`tools/intel-pipeline/`](../tools/intel-pipeline/). Read `data/cve_state.json` first; update it last (`tools/intel-pipeline/write_state.py`).

1. **cvelistV5** – download the latest `*_delta_CVEs_at_*` (or the day's cumulative) release zip from github.com/CVEProject/cvelistV5/releases; records with `dateUpdated` > `max_dateUpdated` replace their line in `data/cve/all/<year>/…`; re-run `cve_build.py` to refresh vendor layers and markdown.
2. **NVD** – `lastModStartDate=<max_lastModified>`; merge into `data/nvd/` via `nvd_build.py`. Respect 6 s between requests without an API key.
3. **CISA KEV** – refetch the JSON feed; if `catalogVersion` changed, re-join and rebuild `cves/kev/`.
4. **GHSA** – GitHub REST `/advisories?type=reviewed&sort=updated` back to `max_modified` (`ghsa_osv_build.py`).
5. **OSV** – per-ecosystem `modified_id.csv` newer than `max_modified`.
6. **Exploit-DB** – `git pull` the gitlab mirror; new ids from `files_exploits.csv`.
7. **Linux kernel CNA** – `git pull` vulns.git; `kernel_cna_build.py`.
8. **Project Zero** – new blog posts after `last_post_file`; itw-sheet refresh (`p0_fetch.py`).
9. **ZDI** – while `zdi.status` is `pending`, fetch the next batch of advisory pages without text (`zdi_fetch.py`), then `zdi_build.py`; afterwards only the current year's published table.
10. **HackerOne** – see `hackerone/README.md`.
11. Re-run `cve_index.py` and `h1_harness.py` (appends only new findings), commit in small batches, `git pull --rebase`, push.

Failures are recorded in `data/cve_state.json` (`status: pending` plus a cursor), never silently dropped.
