# How I Found and Claimed a Subdomain Takeover (My First Article)

- **Source URL:** https://medium.com/@algodemo369/how-i-found-and-claimed-a-subdomain-takeover-my-first-article-560bad69d635?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20251027150110/https://medium.com/@algodemo369/how-i-found-and-claimed-a-subdomain-takeover-my-first-article-560bad69d635
- **Fetched:** 2026-11-19
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/11494 (id 11494)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# How I Found and Claimed a Subdomain Takeover (My First Article)

## How I Found and Claimed a Subdomain Takeover

**Author:** Rahul Tandale

**Platforms targeted:** HackerOne, Bugcrowd, Intigriti, YesWeHack (wildcard programs)

**Target:** `subdomain.target.com`

**Discovery date:** 7 sep 2025

## TL;DR

I run a daily automated reconnaissance pipeline across wildcard bug bounty programs (HackerOne, Bugcrowd, Intigriti, YesWeHack). The pipeline enumerates subdomains, checks for takeover candidates, and runs Nuclei templates. One morning I found a `404` on `subdomain.target.com`. A `dig` showed the DNS CNAME pointed to a Heroku hostname. I created a Heroku app, added the custom domain, and served content from the legitimate `subdomain.target.com`, confirming a subdomain takeover. I reported it to the program and the report was triaged.

## Why this matters

A subdomain takeover occurs when a DNS CNAME points to a third-party service that no longer has an active resource bound to the name (for example: Heroku, AWS S3, GitHub Pages, Netlify). An attacker who can claim that third-party resource can host content under the legitimate subdomain. That content can be used for phishing, hosting malicious scripts, or otherwise impersonating the owner domain.

## My target surface

I focused on wildcard programs that allow finding many targets via `*.example.com`:

- HackerOne
- Bugcrowd
- Intigriti
- YesWeHack

I collected all wildcard programs’ root domains into a single file `wildcard.txt` and ran an automated pipeline daily.

## Tools I used

- `subfinder` — fast passive+active subdomain enumeration
- `subzy` — quick identification of takeover/dangling DNS candidates
- `nuclei` — template-driven verification (takeover & provider fingerprints)
- `dig` / `host` — DNS verification
- Heroku dashboard — claim and bind custom domains (proof-of-concept)
- `cron` — scheduling automation to run daily at 06:00

## My automation pipeline (high level)

1. Collect wildcard roots into `wildcard.txt`.
2. Run `subfinder` against entries in `wildcard.txt` and save all subdomains to `subdomain.txt`.
3. Run `subzy` on `subdomain.txt` and save candidate output to `subzy.txt`.
4. Run `nuclei` takeover templates on `subzy.txt` and save to `nuclei.txt`.
5. Inspect `nuclei.txt` each morning; triage any `404` / takeover-like results.

## Sample commands

```
# 1. Enumerate subdomains for all wildcard domains
cat wildcard.txt | while read domain; do subfinder -d "$domain" -o "${domain}_subs.txt"; done
```
\# 2. Consolidate results

cat \*\_subs.txt | sort -u > subdomain.txt# 3. Find takeover candidates

subzy -targets subdomain.txt -o subzy.txt# 4. Run nuclei takeover templates

nuclei -l subzy.txt -t nuclei-templates/takeovers/ -o nuclei.txt

## Scheduling the automation (cron example)

To run the automation every morning at 06:00 (server time), add a cron entry like:

```
# Run at 06:00 every day
0 6 * * * /path/to/your/automation_script.sh >> /var/log/subtakeover.log 2>&1
```
Where `/path/to/your/automation_script.sh` contains the sequence of commands above (and any environment setup or logging you need).

## What happened (step-by-step, factual)

1. **Daily run produced** **nuclei.txt**
**.** I parsed the results and found `https://subdomain.target.com` flagged with a `404` signature and a takeover fingerprint.
2. **DNS verification.** I ran `dig` to confirm DNS:

```
$ dig +short CNAME subdomain.target.com
some-heroku-app.herokuapp.com.
```
This showed the subdomain had a CNAME pointing to a Heroku hostname and that the provider did not have an active app bound.

1. **Proof-of-concept (P.O.C.) claim.** I created a Heroku account, provisioned an app, and added `subdomain.target.com` as a custom domain in the Heroku dashboard. After adding the custom domain and deploying a simple page, visiting `https://subdomain.target.com` returned my content — proving the takeover.
2. **Evidence collection.** I captured:

- `dig` output showing the CNAME
- `curl -I` showing HTTP 404 before claim and `200 OK` after binding
- Relevant `subzy` / `nuclei` output lines

1. **Responsible disclosure.** I submitted a report to the relevant bug bounty program(s) including step-by-step reproduction, evidence, and remediation suggestions. The report was triaged.

## Example reproduction (concise for triage)

1. `subfinder -d target.com -o target_subs.txt`
2. `subzy -targets target_subs.txt -o subzy.txt`
3. `nuclei -l subzy.txt -t nuclei-templates/takeovers/ -o nuclei.txt`
4. Observed `subdomain.target.com` in `nuclei.txt` with a Heroku takeover fingerprint and `404` response.
5. `dig +short CNAME subdomain.target.com` -> `some-heroku-app.herokuapp.com.`
6. Created a Heroku app and added `subdomain.target.com` as a custom domain — site served content under `subdomain.target.com`.
