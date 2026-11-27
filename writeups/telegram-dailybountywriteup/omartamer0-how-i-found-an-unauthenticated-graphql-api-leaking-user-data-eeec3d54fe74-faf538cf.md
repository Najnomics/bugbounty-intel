# How I Found an Unauthenticated GraphQL API Leaking User Data

- **Source URL:** https://medium.com/@OmarTamer0/how-i-found-an-unauthenticated-graphql-api-leaking-user-data-eeec3d54fe74
- **Fetched from:** https://medium.com/feed/@OmarTamer0
- **Fetched:** 2026-11-27
- **Channel:** @dailybountywriteup
- **Telegram message:**  (id 14943)
- **Method:** medium-rss-content readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
### GraphQL shifts a lot of power to the client. One endpoint, one POST request, and the caller decides exactly which objects and fields come back. That flexibility is the feature. It is also why a single missing authorization check does not leak one record, it leaks the graph.

This article is based on one of my own bug bounty findings: an unauthenticated GraphQL API that exposed user data at scale. The company stays unnamed and identifying details are generalized, but the methodology is exactly what I used: fingerprinting, schema discovery, locating the missing-authorization bug, proving impact at scale, and writing it up so the severity is undeniable.

### Why GraphQL fails differently

In REST, each resource sits behind its own route, and authorization is usually checked route by route. In GraphQL, a single endpoint resolves an arbitrary tree of fields. Authorization has to be enforced at the **resolver** level, on every field, for every object. Teams frequently authenticate the *endpoint* (“you need a token to call /graphql”) but forget to authorize the *resolvers* (“should this token see this specific object’s email field?”).

The result is two recurring bug classes:

- **Missing authentication**: the endpoint answers sensitive queries with no credentials at all.
- **Broken object-level authorization (BOLA)**: you are authenticated, but you can request objects that are not yours by supplying their identifiers.

Both come from the same root cause: the server was built to answer questions without deciding *who is allowed to ask them*.

### Step 1: Confirm and fingerprint the endpoint

During recon I came across an endpoint that looked like GraphQL. Before anything else, I confirmed it with a minimal valid query:

POST /graphql HTTP/1.1

Content-Type: application/json

`{"query":"{__typename}"}`
It answered with {"data":{"\_\_typename":"Query"}}, confirming a live GraphQL API.

Next, I fingerprinted the implementation, because the engine determines how it leaks. Different servers behave differently under malformed input: some echo distinctive error strings, some expose a specific set of default fields, some enable introspection or field suggestions by default and others do not. Sending a deliberately invalid query and studying the exact shape and wording of the error told me which discovery technique would pay off before I spent time on it.

### Step 2: Map the schema with introspection

Introspection is GraphQL’s built-in self-description, and it is the first thing I check. When it is on, the server hands you the entire schema:

`{"query":"query{__schema{types{name kind fields{name args{name} type{name kind ofType{name}}}}}}"}`
That response is a map: every type, every query and mutation, every field and argument. Loading it into a visualizer shows how the types connect, and from that point you are no longer guessing. The target has documented its own attack surface for you.

### Step 3: When introspection is disabled

Disabling introspection is the usual first hardening step, and it is not a dead end. The schema can often be rebuilt indirectly:

- **Field suggestions.** Many engines, even with introspection off, still respond to a wrong field with “Did you mean email?” Each hint reveals a real field name. Tooling automates this into a near-complete schema reconstruction.
- **Client-side artifacts.** Front-end bundles, mobile apps, and documented operations contain real queries. Captured traffic shows the field names and arguments the application itself uses.
- **Error-driven enumeration.** Type mismatches and argument errors leak structure one message at a time.

Introspection being off reduces convenience, not exposure.

### Step 4: Find the query with no guard

With the schema mapped, the real work begins: for each query and mutation that returns something sensitive, test whether authorization is actually enforced.

The method is systematic. I took the query that returns user data and sent it with every credential stripped: no Authorization header, no session cookie, nothing that identifies a user.

POST /graphql HTTP/1.1

Content-Type: application/json

`{"query":"{ users { id username name createdAt } }"}`
It returned data. No token, no session, and the response contained user records: internal IDs, usernames, full names, and account creation dates. The finding was binary and undeniable: personal data, no authentication. When an endpoint does require a session, the next move is BOLA: authenticate as a low-privilege user and request objects by identifiers that should not belong to you.

`{"query":"{ user(id: 1337) { id email role } }"}`
The highest-value gap is often the difference between what the UI renders and what the resolver returns. An interface may only show a display name, while the underlying type still exposes email, role, internal flags, or tokens to anyone who asks for those fields.

### Step 5: Prove scale

A single leaked record is a finding. The entire user base is a severity multiplier. The vulnerable query supported cursor-based pagination, so proving scale took nothing more than following the cursor:

`{"query":"{ users(first: 100, after: \"<cursor>\") { edges { node { id email } } pageInfo { endCursor hasNextPage } } }"}`
Walking the cursor page by page showed that every user record was reachable in bulk. The query also accepted a search parameter, which meant an attacker could look up specific people by name instead of only dumping everything. Documenting “this query returns the full set, paginated, with no authentication” is what turns a shrug into a critical.

### Step 6: Extend the impact

Before writing it up, I checked the adjacent issues that frequently accompany the core bug:

- **Mutations without authorization.** Write operations outrank reads. A mutation that changes state unauthenticated is a far higher-impact finding than a read.
- **Query batching.** Some servers accept an array of operations in one request. Where they do, per-request rate limits on sensitive actions can be bypassed by batching many attempts into a single call.
- **Depth and complexity.** Deeply nested, recursive selections with no depth or cost limit can exhaust server resources, a denial-of-service vector distinct from data exposure.
- **Verbose errors.** Stack traces and internal paths in error responses leak implementation detail useful for further attacks.

### Step 7: Write it up so the severity is undeniable

The technical work is only half the job; a strong report is what gets a finding resolved instead of dismissed. I anchor every GraphQL exposure report on four points:

1. **No authentication required**: the full request, with every credential removed, so there is no ambiguity.
2. **Exactly what is exposed**: the specific fields and why they matter (PII, internal identifiers, authentication material).
3. **Scale**: the pagination proof showing how much data is reachable, not just a sample.
4. **A realistic attacker scenario**: who can do this (anyone on the internet) and what they walk away with.

Then I include remediation, because demonstrating you understand the fix elevates the report:

- Enforce authentication and **object-level authorization at the resolver**, on every field, not only at the gateway.
- Disable introspection and field suggestions in production.
- Apply query depth and complexity limits, and rate-limit batched operations.
- Return only the fields each role is entitled to, and never rely on the UI to conceal data the API still serves.

### The pattern underneath

Across every GraphQL exposure I have looked at, the flaw is not an exotic exploit. It is a design decision that was never consciously made: the API was built to answer questions, and no one decided which questions, from whom. As teams ship more code faster, that gap keeps widening, and the recon-to-impact path above keeps working.

The bug I found did not need a clever chain or an exotic payload. It only needed someone to ask the API a question that nobody had decided it should refuse.

### About the author

I’m Omar Tamer, an offensive security specialist and penetration tester based in Cairo. I hold OSCP+, CPENT, LPT Master and CEH Master, and I serve on EC-Council’s CPENT Scheme Committee, helping shape the exam that tests real-world penetration testing skills.

This finding is the kind of work those certifications are meant to prove: methodical recon, understanding how an application is built, and turning a technical flaw into clear, provable impact.

[How I Found an Unauthenticated GraphQL API Leaking User Data](https://infosecwriteups.com/how-i-found-an-unauthenticated-graphql-api-leaking-user-data-eeec3d54fe74) was originally published in [InfoSec Write-ups](https://infosecwriteups.com) on Medium, where people are continuing the conversation by highlighting and responding to this story.
