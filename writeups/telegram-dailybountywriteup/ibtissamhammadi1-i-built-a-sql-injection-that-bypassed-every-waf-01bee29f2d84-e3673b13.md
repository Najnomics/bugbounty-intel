# I Built a SQL Injection That Bypassed Every WAF

- **Source URL:** https://medium.com/@ibtissamhammadi1/i-built-a-sql-injection-that-bypassed-every-waf-01bee29f2d84?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250902173918/https://medium.com/@ibtissamhammadi1/i-built-a-sql-injection-that-bypassed-every-waf-01bee29f2d84
- **Fetched:** 2026-11-19
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/10544 (id 10544)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
Member-only story

# I Built a SQL Injection That Bypassed Every WAF

While testing an API endpoint with a colleague, a single quote accidentally slipped into a parameter — and the server responded differently. No errors appeared on the frontend, but something felt *off*.

When we tried classic SQL injection payloads, Cloudflare’s WAF instantly blocked us. Yet, the anomaly persisted.

Days later, a PostgreSQL-specific trick — using the `ILIKE` operator—allowed us to extract sensitive emails without triggering a single alert. This wasn’t a brute-force attack; it was a logic puzzle that exposed how WAFs often miss subtle query manipulations.

Here’s how a Boolean-Based Blind SQLi technique bypassed every filter, why most testers overlook it, and how you can protect your applications.

### How a Single Quote Broke the Query (And Why Others Missed It)

Most developers assume that no frontend errors = no vulnerabilities. But in this case, the API responded with subtle behavioral changes — a 200 OK status, but slightly slower responses for certain inputs. Manual testers might dismiss this as network latency, but for a trained eye, it was a red flag.

The vulnerability existed because user input was directly concatenated into a SQL query without sanitization. Classic payloads like `' OR`…
