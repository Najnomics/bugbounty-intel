# My Bug Bounty Toolkit

- **Source URL:** https://medium.com/@cossackrider8/my-bug-bounty-toolkit-3-tools-that-changed-how-i-hunt-477b69593f02
- **Fetched from:** https://medium.com/@cossackrider8/my-bug-bounty-toolkit-3-tools-that-changed-how-i-hunt-477b69593f02?source=rss-fb77fbf7fe16------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14923 (id 14923)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** 0n!_GI1tch / Fri, 25 Sep 2026 04:04:27 GMT

*A breakdown of the recon pipeline, scanner, and business logic tool I actually use in live engagements — including my exact commands.*

Most bug bounty writeups talk about *one* find. This one’s about the toolkit behind the finds — three tools I built or adopted to go from “read policy → guess what to run → hope for the best” to a structured, repeatable pipeline.

**The problem:** every program has different rules. Flipkart bans automated scanners. Shopify allows full automation. Get it wrong and you’re banned, not paid.

**The fix:** a pipeline that reads the raw policy text first, decides what’s allowed, and only runs those phases.

**How it works:**

1\. Create targets/\<name>/

2. Drop policy text → policy.txt

3. List in-scope domains → scope.txt

4. Run: ./scripts/recon-smart.sh targets/\<name>

The policy-parser.sh component reads the policy and auto-generates flags — "no automated scanners" disables Nuclei/ffuf/content discovery, "no port scanning" disables Naabu, rate limits get detected and respected. The main pipeline (recon-smart.sh) then runs 30+ phases, each gated by those flags — banned phases are skipped with the reason logged, not silently dropped.

**Coverage:** subdomain enum (subfinder, assetfinder, chaos, crt.sh) → DNS/ASN mapping → ports (naabu, policy-gated) → HTTP probing (httpx) → content discovery (ffuf, policy-gated) → historical URLs (gau, waybackurls, waymore) → JS analysis (subjs, LinkFinder, SecretFinder) → parameter classification (gf patterns for XSS/SSRF/IDOR/SQLi) → cloud bucket checks → subdomain takeover → vuln scanning (nuclei, policy-gated) → deep OSINT via Osmedeus + BBOT.

**Output** is organized by vuln type, not just by tool:

\~/recon-output/\<target>/

├── 00-SUMMARY.md

├── 09-params/

│ ├── xss.txt

│ ├── ssrf.txt

│ ├── idor.txt

│ └── sqli.txt

└── 12-nuclei/results.txt

Manual testing becomes: pick a vuln file, load it into Burp, go. No policy-reading marathon, no accidental bans.

AKCA is an open-source Go scanner (Apache-2.0) that does what most first-pass scanners *should* do: capture proof, not just alerts. Every finding ships with the raw HTTP request/response, payload, cURL repro, CWE/OWASP mapping, and a confidence score — so I can verify before I ever write a report line.

**What it covers:**

**My actual workflow:**

bash

\# Recon

subfinder -d target.com -silent -o subdomains.txt

cat subdomains.txt | httpx -silent -o live.txt

gau target.com > gau.txt

waybackurls target.com > wayback.txt

cat \*.txt | sort -u > all-urls.txt

\# Passive scan (through Burp)

akca -u[https://target.com](https://target.com) -m passive -p [http://127.0.0.1:8080](http://127.0.0.1:8080) -k \

--rate-limit 3 --concurrency 2 --request-budget 2000 --time-budget 20m \

-f json -o passive.json

\# Active scan

akca -u[https://target.com](https://target.com) -m sql,xss,rce,ssrf,auth,api -p [http://127.0.0.1:8080](http://127.0.0.1:8080) -k \

--rate-limit 3 --concurrency 2 --request-budget 5000 --time-budget 45m \

-f html -o full-scan.html

\# Cross-validate

cat live.txt | nuclei -severity critical,high,medium -rate-limit 5 -o nuclei.txt -silent

\# Manual verification

akca replay --finding \<id>

Routing through -p http://127.0.0.1:8080 -k means every request lands in Burp's proxy history for manual review. The --rate-limit, --concurrency, and --\*-budget flags keep the scan inside program rules.

AKCA isn’t a Burp replacement — it’s the force multiplier that handles crawling and evidence collection so I spend my time chaining exploits and hunting the logic bugs no scanner catches.

Install: go install github.com/akha-security/akca/engine/cmd/akca@latest

Repo: github.com/akha-security/akca

SQLi and XSS get caught by scanners. IDOR, price manipulation, race conditions, and workflow bypass don’t — they need semantic understanding of *how the app is supposed to work*. That’s the gap BLFinder fills.

**My workflow:**

**What it catches:**

SeverityFindingsCriticalIDOR/BOLA, price manipulation, race conditions, mass assignment, JWT alg:none, state machine abuse, BFLAHighBlind IDOR (5-oracle), MFA/workflow bypass, coupon abuse, integer overflow, time logic bypass, soft delete bypassMediumGraphQL introspection, account enumeration, parameter pollution, HTTP method overrideAdd-onsSSRF (4-tier), active CSRF replay, source code exposure, OTP rate-limit testing

The two-token setup is what makes cross-user IDOR confirmation real instead of theoretical. Findings persist in SQLite, so duplicates get auto-filtered across multi-day engagements — useful when a program stays open for weeks.

**Setup:**

git clone https://github.com/Steven5233/BLfinder.git

cd BLfinder

pip install aiohttp aiosqlite --break-system-packages

python3 blfinder/blfinder.py --help

**Honest take:** it throws false positives, and a module will occasionally crash. Treat it as an extra pair of eyes, not a verdict. If 70%+ of its findings turn out true positive against a target, it earns a permanent slot in your workflow.

Put together, this is roughly the flow on any authorized target:

Policy → Smart Recon Pipeline (policy-gated, full surface map)

→ AKCA (passive + active scan, evidence-backed)

→ Nuclei (cross-validation)

→ BLFinder (business logic, two-account IDOR/BOLA)

→ Manual verification (Burp Suite / curl)

→ Report

None of these tools replace manual testing. They exist to compress the boring parts — enumeration, probing, first-pass detection — so more time goes into chaining exploits and finding the bugs automation can’t see.
