# 🐛 Bug Bounty Writeup

- **Source URL:** https://pwnxotus.medium.com/httpx-a-deep-dive-into-the-http-probing-engine-359f29662b24
- **Fetched from:** https://pwnxotus.medium.com/httpx-a-deep-dive-into-the-http-probing-engine-359f29662b24?source=rss-3a12af026389------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14922 (id 14922)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** PWNXOTUS / Wed, 23 Sep 2026 22:58:44 GMT

There’s a moment every hacker hits early on: you’ve got a text file with three thousand subdomains in it, pulled from subfinder, amass, certificate transparency logs, whatever. And now you're staring at it thinking — *okay, but which of these are actually worth my time?*

Before tools like this existed, people wrote bash loops around curl. It's an obvious first instinct, and it breaks down almost immediately once you're dealing with real internet-scale target lists:

httpx solves all four by building on top of retryablehttp, a Go HTTP client library specifically designed to survive messy real-world conditions — automatic retries with backoff, connection pooling, and graceful protocol fallback — while still being fast enough to probe tens of thousands of hosts in minutes.

The flag list in httpx -h can feel overwhelming at first glance, but almost every flag falls into one of four pipeline stages:

INPUT  →  PROBE  →  MATCH/FILTER  →  OUTPUT

Once that clicks, the tool stops feeling like memorization and starts feeling like composition — you’re just deciding what goes in, what gets measured, what gets kept, and what shape it comes out in.

httpx will happily eat almost any shape of target data:

echo "example.com" | httpx

cat subdomains.txt | httpx

httpx -l hosts.txt

httpx -u https://example.com

httpx -l cidrs.txt # expands and probes entire CIDR ranges

httpx -l hosts.txt -p 80,443,8080,8443

This flexibility is *why* it sits in the middle of almost every recon chain rather than at the start or end:

subfinder -d example.com -silent | httpx -silent

This is where the depth really lives, and where most people only scratch the surface. By default, httpx already tracks a surprising amount internally — URL, IP, CNAME, status code, title, content length, TLS certificate data, web server header, word count even if it doesn’t print everything unless you ask.

Let’s go probe-by-probe, because *why* each one matters is more useful than just knowing it exists.

**-sc / -status-code** — the baseline. But status codes lie constantly: soft-404s that return 200, WAFs that return 403 for everything, load balancers that return 503 under specific conditions. Never trust status code alone as your filter — more on this below.

**-title** — the page \<title> tag. Sounds trivial, but it's one of the highest signal-to-noise probes in the whole tool. Default install pages ("Welcome to nginx!", "Apache2 Ubuntu Default Page"), admin panel titles, staging environment banners, and forgotten Jenkins/Grafana/Kibana instances all announce themselves here before you've made a second request.

**-td / -tech-detect** — Wappalyzer-based fingerprinting. This is httpx doing pattern matching against response headers, cookies, script tags, and meta tags to guess the tech stack: WordPress version, a specific CMS, a JS framework, a load balancer vendor. It's not perfect fingerprint databases go stale — but it's the fastest way to triage "which of these three thousand hosts are running something with known CVEs" before you commit to deeper testing.

**-location** — where redirects actually go. This one's underrated for a specific reason: internal hostnames leak through Location headers constantly. A public-facing load balancer redirecting to internal-app.corp.local tells you something about the internal network topology that no amount of subdomain enumeration would have surfaced.

**-favicon** — computes an mmh3 hash of /favicon.ico. This sounds like a party trick until you realize favicon hashes are indexed by search engines like Shodan against known products — a matching hash can instantly tell you "this is a Jenkins instance" or "this is a specific IoT vendor's admin panel" without httpx needing its own fingerprint database entry for it.

**-jarm** — a TLS server fingerprint (JARM, developed by Salesforce's security team) that clusters hosts by their TLS stack configuration rather than their content. Two domains with completely different content but the same JARM hash are very likely running the same backend infrastructure same load balancer, same TLS termination point, sometimes literally the same server. This is a favorite for mapping shared infrastructure behind a scattered set of brand domains, or spotting suspicious infrastructure in blue-team contexts.

**-hash md5,sha1,sha256,simhash** — body hashing at scale. Straight hashes (md5/sha256) are useful for exact-duplicate detection spotting when hundreds of "different" hosts are all serving the identical default page. simhash is more interesting: it's a *fuzzy* hash, meaning near-identical pages (say, the same soft-404 page with a dynamically inserted timestamp) still cluster together even though a literal SHA256 would differ every time.

**-cdn** — flags whether the resolved IP belongs to a known CDN/WAF provider (Cloudflare, Akamai, Fastly, etc.). This single flag answers a question that changes your entire approach: if a host is CDN-fronted, a "200 OK" doesn't mean you're touching the origin server you're touching an edge node, and any direct-IP attack surface (open ports, server misconfig) is invisible to you until you find the real origin.

**-asn** — resolves the IP to its ASN (Autonomous System Number) and owning organization. Useful for infrastructure mapping: are these forty subdomains actually all hosted on the target's own infra, or scattered across AWS, GCP, and three third-party SaaS vendors? That distinction matters a lot for scoping what's actually attackable.

**-ip / -cname** — the resolved DNS answers themselves, which matter for spotting subdomain takeover candidates (a CNAME pointing at a deprovisioned cloud resource) long before you'd need a dedicated takeover-scanner tool.

Chain a handful of these together and one httpx pass gives you a structured recon dataset that used to take multiple separate tools and manual correlation:

httpx -l hosts.txt -sc -title -td -cdn -asn -ip -favicon -jarm -json -o recon.json

Here’s the mistake I see constantly: people pipe raw httpx output into grep and jq for everything, when httpx already has native filtering that's faster and more precise, because it filters *during* the probe rather than after.

httpx -l hosts.txt -mc 200,301,302     # match only these status codes

httpx -l hosts.txt -fc 404,403 # filter these OUT

httpx -l hosts.txt -mr "admin|login" # match response body against regex

httpx -l hosts.txt -mt "WordPress" # match on detected tech

httpx -l hosts.txt -ml 1000 # match by content length

httpx -l hosts.txt -mct "application/json" # match content-type

The real depth here is -mdc matching on a *combination* of conditions simultaneously, which is exactly how you defeat the single most common false-positive trap in recon: soft-404 pages that return 200 OK for literally every path.

echo target.com | httpx -path '/.well-known/security.txt' \

-mc 200 -mct 'text/plain' -mr 'Contact:'

Read that as a sentence: “check /.well-known/security.txt, and only tell me it exists if the status is 200, the content-type is genuinely plaintext, *and* the body actually contains a Contact: line." Any one of those three checks alone would be fooled by a catch-all page. Together, they're close to airtight. This compositional filtering — rather than a dedicated -check-security-txt flag — is a deliberate philosophy choice in the tool: build primitives, not special cases, and let users compose them for whatever well-known file or endpoint they're hunting.

httpx -l hosts.txt -silent -o alive.txt        # plain list of alive URLs

httpx -l hosts.txt -json -o results.json # structured, everything included

-json is the one that matters once you're operating at any real scale, because it turns httpx from "a tool you read" into "a tool you query":

cat results.json | jq 'select(.tech\[\]? == "WordPress")'

cat results.json | jq 'select(.cdn == false and .status\_code == 200)'

And because JSON-lines is the shared language of the ProjectDiscovery suite, this is also how you chain straight into a vulnerability scanner:

subfinder -d target.com -silent \

| httpx -silent \

| nuclei -t cves/ -t exposed-panels/

That three-tool chain — enumerate, probe, scan — is close to the canonical “hello world” of this entire ecosystem, and it works *because* each tool’s output was designed with the next tool’s input in mind.

httpx -l hosts.txt -threads 100 -rate-limit 150 -timeout 10 -retries 2

On an authorized pentest against fragile internal infrastructure, you turn these *down* a crashed production service because your recon tool hammered it is a bad day for everyone, and outside any agreed rules of engagement. On wide-scope bug bounty recon against resilient internet-scale infra, you turn them *up*, because speed is the entire point of using this over curl.

**Vhost enumeration via raw Host headers.** Shared IPs sometimes host forgotten internal applications alongside the public-facing one:

httpx -u https://1.2.3.4 -H "Host: internal.target.com" -sc -title

**Raw request replay** for anything default probing can’t express — custom auth headers, non-standard methods, specific bodies:

httpx -request raw\_request.txt -u https://target.com

**Visual triage at scale.** Reading three thousand page titles is tedious; scanning three thousand thumbnails is fast:

httpx -l hosts.txt -screenshot -srd screenshots/

httpx doesn’t find the vulnerability for you, and it’s not trying to. What it does and does better than almost anything else in the space is take a chaotic pile of raw hostnames and turn it into structured, filterable, chainable *data*. In an industry where the overwhelming majority of the actual work is “figure out what exists before you can attack it,” that’s not a small thing it’s the foundation everything else in your pipeline stands on. Learn its filtering primitives and JSON output properly, and recon stops being a manual chore you dread and becomes a fast, repeatable, almost boring pipeline which, honestly, is exactly what you want it to be, so your actual attention goes to the 5% of findings that are genuinely
