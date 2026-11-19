# From Exposed API Key to Arbitrary Account Creation

- **Source URL:** https://medium.com/@drizzlehx/from-exposed-api-key-to-arbitrary-account-creation-a-graphql-bug-bounty-walkthrough-af0d26accab3?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250901060127/https://medium.com/@drizzlehx/from-exposed-api-key-to-arbitrary-account-creation-a-graphql-bug-bounty-walkthrough-af0d26accab3
- **Fetched:** 2026-11-19
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/10373 (id 10373)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# From Exposed API Key to Arbitrary Account Creation: A GraphQL Bug Bounty Walkthrough

In the world of bug bounty hunting, sometimes the most impactful vulnerabilities are found by chaining seemingly disparate issues. Recently, during an engagement on a well-known bug bounty platform, I encountered a fascinating case that evolved from a simple information disclosure into a critical access control bypass, allowing for unauthorized user management.

This article delves into how an **AWS AppSync API Key**, inadvertently exposed within a production JavaScript file on an in-scope main domain, became the gateway to a restricted GraphQL API endpoint. While the target endpoint itself was technically out-of-scope, the origin of the critical credential (the API key) being within scope was key to validating the report.

## Proof Of Concept

1. In the redacted.com , there exist a public js file named : chunk-vendors./some\_string/.js at url https://redacted.com/static/chunk-vendors./some\_string/.js
2. Scrolled Down to Find Sensitive Data Exposure of API Key of VUE\_APP\_AWS\_APPSYNC\_API\_KEY along with The Endpoint VUE\_APP\_AWS\_APPSYNC\_ENDPOINT:”https://socket.redacted.com/graphql",VUE\_APP\_NAME:"Redacted".
3. On Intercepting Requests with Burp Suite on the endpoint : https://socket.redacted.com/graphql
4. Then Tried to Validate the endpoint : https://socket.redacted.com/graphql , Change the Request from GET to POST with a valid query without the API-Key.
Requests to https://socket.redacted.com/graphql without the API key return 401 Unauthorized.
5. Adding the exposed key in Header (x-api-key: Api Key Value) grants full access.
6. Successful schema introspection reveals mutable objects.
Not only this the Response Header shows : x-amzn-appsync-TokensConsumed: 1
related to AWS AppSync (GraphQL service), indicating 1 token was consumed. Each request consumes tokens, leading to AWS billing abuse.
7. Using Another Query , Successful Unauthorized Object Manipulation!
8. The exposed API key allows arbitrary GraphQL mutations.
9. As an Attacker I would Craft messages with embedded scripts (XSS) or malicious links that, when clicked by administrators, could :
Hijack admin sessions
Trigger privilege escalation exploits
Gain full system control

The ability to create and update user accounts without proper authorization, directly facilitated by an exposed API key from the in-scope anytask.com domain, represents a Medium, High or Critical vulnerability. This is a clear, actionable security impact, not merely an informational finding.

\~ drizzlehx
