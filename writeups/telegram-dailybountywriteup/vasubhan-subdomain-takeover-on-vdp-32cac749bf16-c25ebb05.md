# Subdomain Takeover on VDP

- **Source URL:** https://medium.com/@vasubhan/subdomain-takeover-on-vdp-32cac749bf16?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250822145827/https://medium.com/@vasubhan/subdomain-takeover-on-vdp-32cac749bf16
- **Fetched:** 2026-11-23
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/9472 (id 9472)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Subdomain Takeover on VDP

# 1. Summary

A subdomain of Target, `heyo.redacted.target.com`was pointing to an unclaimed Acquia service endpoint, but remains unclaimed.

Although an actual takeover could not be demonstrated because Acquia requires an active paid subscription for domain assignment, the misconfiguration still presents a **serious security risk**.

An attacker with an Acquia subscription could claim this subdomain and host malicious content under the trusted `*.target.com` domain.

# 2. Technical Details

# A. DNS Resolution

`$ dig heyo.redacted.target.com CNAME````
;; ANSWER SECTION:
heyo.redacted.target.com. 3395 IN CNAME heyo.redacted.target.com..cdn.cloudflare.net
```
The subdomain `heyo.redacted.target.com` points to `heyo.redacted.target.com.cdn.cloudflare.net`. Typically, it indicates a connection with a service hosted behind Cloudflare.

# B. Web Response

`$ curl -I https://heyo.redacted.target.com````
HTTP/2 404
date: Sat, 26 Apr 2025 18:25:00 GMT
content-type: text/html
server: cloudflare
cf-ray: 93681ec7bd1e7b59-IAD
cf-cache-status: DYNAMIC
```
The web server returns a “404 Not Found”, confirmation that no active web application is linked to the subdomain.

# C. Screenshot

# D. Attempt to Claim

An attempt was made to create an Acquia site and add the domain. However:

- Acquia requires a **paid subscription** to add custom domains.
- No free trial or complimentary access was available.
- As such, a full exploitation (i.e., practical domain claim) was **not completed**.

Nevertheless, in a real-world threat scenario, an attacker could easily subscribe to Acquia, claim the subdomain, and perform malicious activities under `*.target.com`.

# 3. Impact

If exploited, the attacker could:

- **Host phishing pages** under a trusted Target domain.
- **Deliver malware payloads** to employees or customers.
- **Exploit SSL trust** (because the subdomain has a valid DNS/SSL path through Cloudflare).
- **Damage brand reputation** if malicious activities are linked to Target’s domain.

# 4. Recommendation

- Immediately **remove** or **correct** the DNS CNAME record for `heyo.redacted.target.com` If it is no longer needed.
- Alternatively, **claim and properly configure** the subdomain within the Acquia platform to prevent external abuse.
- **Audit other DNS records** for similar misconfigurations to prevent future occurrences.

Thanks for reading.

./Keep-Hacking
