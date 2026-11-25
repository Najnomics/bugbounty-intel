# This Simple GraphQL SSRF Bug Earned Me $3,000 (3/30 DAYS)

- **Source URL:** https://medium.com/@zerodaystories/this-simple-graphql-ssrf-bug-earned-me-3-000-3-30-days-9bd13e2c2f9d?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20251025215901/https://medium.com/@zerodaystories/this-simple-graphql-ssrf-bug-earned-me-3-000-3-30-days-9bd13e2c2f9d?source=rss------bug_bounty-5
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/8357 (id 8357)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
Member-only story

# Hi Bug Bounty Hunters !!!

I’m a security researcher, and I’ve taken on the challenge of explaining one bug bounty report every day for the next 30 days — 30 days, 30 reports!

Here’s today’s report: SSRF in GraphQL Query Exposes Internal Network

## How a Researcher Found a Critical SSRF Bug in \*\*\*\*\*

A fellow researcher discovered a critical Server-Side Request Forgery (**SSRF**) vulnerability in a **GraphQL** endpoint of \*\*\*\*\*. This issue allowed attackers to make the server send arbitrary GET requests to external or internal domains. Let’s dive into how it was discovered.

## The Bug: SSRF in the `allTicks` GraphQL Query

The issue lies in the `source` parameter of the `allTicks` query. This parameter accepts a URL and uses it to make server-side GET requests. The server failed to restrict or validate the URLs, leading to SSRF.

Here’s how the bug was found:

1. **Identify the GraphQL Endpoint**
The researcher noticed that the**allTicks**
 query allowed a `source` parameter to be passed as a URL.
2. **Test for External Requests**
By replacing the legitimate URL with a Burp Collaborator domain, the researcher confirmed the server made GET requests to the specified domain. Here’s an example query:
