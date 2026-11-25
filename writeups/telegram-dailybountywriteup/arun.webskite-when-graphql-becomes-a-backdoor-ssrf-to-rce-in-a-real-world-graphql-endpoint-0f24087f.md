# When GraphQL becomes a backdoor

- **Source URL:** https://medium.com/@arun.webskite/when-graphql-becomes-a-backdoor-ssrf-to-rce-in-a-real-world-graphql-endpoint-b4ab3b14573f?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20251126142306/https://medium.com/@arun.webskite/when-graphql-becomes-a-backdoor-ssrf-to-rce-in-a-real-world-graphql-endpoint-b4ab3b14573f?source=rss------bug_bounty-5
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/11243 (id 11243)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# When GraphQL becomes a backdoor: SSRF to RCE in a real-world GraphQL endpoint.

How an unsafe GraphQL mutation allowed server-side request forgery and remote code execution — and the defensive steps every GraphQL app should have.

## TL;DR

I discovered a chained vulnerability in a GraphQL endpoint that allowed user-controlled data to be turned into outbound requests and — via unsafe server-side handling — into remote code execution on the app server. This post explains the root cause, measurable impact, detection techniques, and straightforward mitigations you can apply today to harden your own GraphQL services. I avoid posting exploit code; this is a defensive write-up meant to help developers and security teams.

## Background: GraphQL, flexibility, and risk

GraphQL gives clients powerful, flexible control over the data they ask for and the operations they perform. That flexibility is a huge developer win — and also a source of attack surface if inputs are not treated as untrusted.

Two common patterns that increase risk in GraphQL services:

1. Accepting and using arbitrary URLs or payloads supplied by clients (e.g., webhook URLs, avatar URLs, or callback endpoints).
2. Passing user-controlled strings into server-side operations that invoke network requests or shell commands.

When those two patterns are combined without sufficient validation and containment, attackers can manipulate a server into contacting internal resources (SSRF) and — in worst cases where the server evaluates or executes results unsafely — cause code execution (RCE).

## Impact

- **SSRF (Server-Side Request Forgery):** attacker-controlled requests to internal-only services, metadata endpoints, cloud provider metadata (if accessible), or internal admin APIs.
- **RCE (Remote Code Execution):** if server-side code uses user-controllable data insecurely in command execution or evaluation contexts, an attacker can achieve code execution.
- **Data exfiltration & lateral movement:** once SSRF is possible, internal services and secrets become reachable, which amplifies risk.
- **Hard-to-detect abuse:** SSRF often looks like legitimate outbound traffic; detection requires good logging and egress controls.
