# Shopify SSRF

- **Source URL:** https://masimshahzad.medium.com/shopify-ssrf-from-store-screenshot-to-root-access-96003965f49a
- **Fetched from:** https://masimshahzad.medium.com/shopify-ssrf-from-store-screenshot-to-root-access-96003965f49a?source=rss-440524433a10------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14998 (id 14998)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** Muhammad Asim Shahzad / Tue, 24 Nov 2026 04:59:17 GMT

*AI-assisted: drafted with AI help from public sources, then reviewed and edited. This is an analytical case study of a public disclosure, not my own discovery.*

A feature that took screenshots of online stores became a path to root. In April 2018, researcher 0xacb reported a Shopify SSRF in Shopify Exchange: the screenshot renderer could be steered into Google Cloud’s internal metadata service, and the credentials it exposed led to root shells in containers across one infrastructure subset. Shopify pulled the service within an hour and paid $25,000.

***Disclaimer:*** *Educational and defensive use only. This was fixed in 2018. Reproduction details are intentionally omitted.*

Shopify Exchange, a marketplace for buying and selling stores, used a headless browser to screenshot each store for its listing.

The researcher owned the store, so he controlled the page, and made it send the browser to the metadata service every Google Cloud instance can reach. The screenshot became a camera pointed at internal data.

Google normally requires a special header on metadata calls to block exactly this, but an older API version still answered without it.

From there it was a credential chain. The metadata exposed a cloud access token, and because GKE metadata concealment was not enabled, Kubernetes node credentials too. Those allowed listing and creating pods, reading a service-account token, and finally running commands as root in containers in that subset.

Shopify says the affected subset did not include Shopify core, but some of its applications had access to core data and systems, which is why it was paid as a core RCE. Root in production containers means secrets and running services are exposed. Shopify then audited every subset.

**1. Validate every request, not the first URL.** The attack used a navigation the page triggered after loading; a check on the submitted URL alone would not have caught it.

**2. Block metadata at the network layer.** Shopify’s fix: a metadata concealment proxy and no access to internal IPs on all subsets.

**3. Minimise what metadata exposes.** No node credentials in instance attributes.

\# Pseudocode: vet EVERY request the headless browser makes

BLOCKED = \[ip\_network(n) for n in (

"127.0.0.0/8", "10.0.0.0/8", "172.16.0.0/12", "192.168.0.0/16",

"169.254.0.0/16", # link-local: cloud metadata lives here

"::1/128", "fc00::/7", "fe80::/10", "::ffff:0:0/96")\]

def allow\_request(url):

u = parse\_url(url)

if u.scheme not in ("http", "https"):

return False

addrs = resolve\_all(u.host) # every A/AAAA record

if not addrs or any(ip\_address(a) in net for a in addrs for net in BLOCKED):

return False

pin\_dns(u.host, addrs) # no DNS rebinding

return True

def render\_screenshot(store\_url):

page = headless.new\_page()

page.on\_request(lambda r: r.continue\_() if allow\_request(r.url) else r.abort())

page.goto(store\_url, timeout\_s=15) # redirects hit on\_request too

return page.screenshot()

# Test: page redirecting to the metadata host -> aborted, blank capture

# Defence in depth: no network route from workers to 169.254.169.254

Found by **0xacb** (credited with help from Luís Maia, 0xfad0). Primary source: HackerOne report [#341876, SSRF in Exchange leads to ROOT access in all instances](https://hackerone.com/reports/341876) (submitted 22 April 2018, disclosed 23 May 2018), including Shopify’s summary of impact, fix and bounty. Facts come from that report; analysis and code are original.

Next breakdown: another real bug bounty case. Follow @masimshahzad for daily bug bounty breakdowns.
