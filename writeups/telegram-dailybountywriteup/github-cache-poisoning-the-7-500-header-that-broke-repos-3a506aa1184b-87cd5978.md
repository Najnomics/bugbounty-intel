# GitHub Cache Poisoning

- **Source URL:** https://masimshahzad.medium.com/github-cache-poisoning-the-7-500-header-that-broke-repos-3a506aa1184b
- **Fetched from:** https://masimshahzad.medium.com/feed
- **Fetched:** 2026-11-27
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/15000 (id 15000)
- **Method:** medium-rss-content readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
### One malformed header could make GitHub’s cache serve a broken page to every logged-out visitor of a repository. It paid $7,500

*AI-assisted: drafted with AI help from public sources, then reviewed and edited. This is an analytical case study of a public disclosure, not my own discovery.*

One request with a bad header, and a public repository stops loading for everyone who is not signed in. That was a GitHub cache poisoning bug Iustin Ladunca (Youstin) reported, earning $7,500, his highest cache poisoning bounty. It was one of more than 70 cache poisoning reports he made across bug bounty programs.

***Disclaimer:*** *Educational and defensive use only. The researcher states these issues are fixed. Header values and reproduction steps are intentionally omitted.*

### Vulnerability Overview

- **Type:** Cache-poisoned denial of service (CP-DoS) via an unkeyed request header
- **CWE (analytical mapping):** CWE-349 (Acceptance of Extraneous Untrusted Data With Trusted Data), CWE-20 (Improper Input Validation)
- **CVE:** None
- **Bounty:** $7,500 from GitHub

### How the GitHub Cache Poisoning Worked (high level)

A shared cache decides who gets the same stored copy using a cache key, usually built from host, path and a few chosen inputs. Anything that changes the response but is left out of the key is an “unkeyed input”, and a classic poisoning lever.

Ladunca built a scanner that tried many headers against bug bounty targets to spot unkeyed ones. GitHub repository pages kept getting flagged: an invalid value in the Content-Type request header produced a different, broken response, and the cache stored it under the normal key.

At first it would not reproduce in a browser. GitHub included the authentication cookie in its cache key, so each signed-in user effectively had their own copy. Logged-out visitors, however, all shared one copy. Poison that copy and the repository is down for every anonymous reader until the entry expires.

### Business Impact

Anonymous traffic is a lot of GitHub: people reading documentation, pulling READMEs, or following links from search and package registries. Taking a repository offline for them hits open source projects and companies that rely on GitHub as their public face.

Across the research, Ladunca said roughly 80% of his findings were CP-DoS through unkeyed headers. Coverage put his total rewards at around $40,000 for the 70-plus bugs.

### Fixing GitHub-Style Cache Poisoning (my own analysis)

**1. Never share errors.** Ladunca’s own recommendation: disabling caching for error status codes would stop a large share of CP-DoS.

**2. Drop what you don’t key.** If a header can change the response, key on it or strip it at the edge.

**3. Treat the cache key as a security boundary.** Review it like an access rule.

\# Pseudocode: an edge cache that only stores what it can safely share

KEY\_FIELDS = ("host", "path", "query", "accept-encoding")

ORIGIN\_NEEDS = {"accept", "accept-encoding", "cookie", "user-agent"}

def handle(request):

if request.method in ("GET", "HEAD"):

request = request.keep\_headers(ORIGIN\_NEEDS) # Content-Type on a GET never reaches origin

key = cache\_key(request, KEY\_FIELDS, per\_user=request.has\_session())

cached = cache.get(key)

if cached:

return cached

resp = origin.fetch(request)

if shareable(request, resp):

cache.put(key, resp, ttl=resp.max\_age)

return resp

def shareable(request, resp):

if request.method not in ("GET", "HEAD") or resp.status >= 400:

return False # errors are served once, never stored

if {"no-store", "private"} & resp.cache\_directives:

return False

return set(resp.vary) \<= set(KEY\_FIELDS) # never cache on unkeyed variation

# Test: anonymous GET with a garbage header, then a clean GET -> clean GET gets the real page

### Key Takeaways

- Every input that can change a response belongs in the cache key or should be stripped before the origin sees it.
- Bugs that skip logged-in users can look harmless in testing while breaking things for every anonymous visitor.
- Cacheable error pages turn small parser quirks into outages.

### Credit & Sources

Reported by **Iustin Ladunca (Youstin)**. Primary source: [Cache Poisoning at Scale](https://youst.in/posts/cache-poisoning-at-scale/), 23 December 2021. Corroboration: [Dark Reading, 6 January 2022](https://www.darkreading.com/cloud-security/cache-poisoning-of-cdns-allows-dos-attacks-against-cloud-apps). Facts come from those sources; analysis and code are original.

Next breakdown: another real bug bounty case. Follow @masimshahzad for daily bug bounty breakdowns.
