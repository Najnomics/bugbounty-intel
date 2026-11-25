# Authorization Is the Attack Surface

- **Source URL:** https://cyphernova1337.medium.com/authorization-is-the-attack-surface-an-expert-field-guide-to-breaking-modern-access-control-47881b889333
- **Fetched from:** https://cyphernova1337.medium.com/authorization-is-the-attack-surface-an-expert-field-guide-to-breaking-modern-access-control-47881b889333?source=rss-6f03dce4675e------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14963 (id 14963)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** CypherNova1337 / Wed, 28 Oct 2026 20:09:51 GMT

*Flipping admin=0 to admin=1 is dead. Here’s the methodology that replaced it — and the bugs it finds that scanners never will.*

If your access control testing still starts with toggling a query parameter or decoding a Base64 cookie, you’re testing applications that stopped existing years ago. Mature targets in 2026 are SPAs sitting on top of API gateways, which fan out to dozens of microservices. Authentication is usually solid — an OAuth provider, signed JWTs, MFA. Nobody is forging tokens anymore.

Authorization is a different story. Authentication is solved once, at the edge. Authorization has to be solved again in every service, every resolver, every endpoint, by whichever developer wrote it that sprint. Each one is a fresh chance to get it wrong.

This guide isn’t a list of vulnerability classes. You already know what BOLA and BFLA are. It’s a methodology: how to map an application’s permission model, find where enforcement actually lives, and systematically test the seams between client, gateway, and service.

Beginners test endpoints. Experts test a permission model. Before you send a single tampered request, you need to know what the application *thinks* the rules are.

The minimum viable setup is four accounts across two tenants:

With those four, every request you capture can be replayed as a cross-role test (vertical) and a cross-tenant test (horizontal). Most real findings live in one of those two axes, and the nastiest ones live in both.

Next, browse the entire application as the Tenant A admin with Burp running. Click every button, open every modal, submit every form. You’re building a corpus of every privileged request the application can make. Then replay that entire corpus with the low-priv token. Autorize and AuthMatrix automate the replay; your job is to make sure the corpus is complete.

Finally, write the matrix down: rows are actions (create invoice, invite user, export data, change role), columns are roles, cells are “should” and “does.” Every cell where those disagree is a report. Every action you couldn’t trigger at all is a gap in your recon — which is where the next section comes in.

A modern SPA ships its entire feature set to every visitor. The admin panel your low-priv account can’t see is still in the bundle — it just never renders. Your goal is to recover every route, every API call, and every permission string the developers wrote.

Check every JS file for a //# sourceMappingURL= comment and every response for a SourceMap or X-SourceMap header. When the comment is stripped, request the bundle path with .map appended anyway — build pipelines often strip the reference but still deploy the file. A recovered map gives you the original source tree, comments and all. Tools like sourcemapper rebuild it to disk so you can grep it like a repo.

[GitHub - CypherNova1337/sourcemapper: Extract JavaScript source trees from Sourcemap files](https://github.com/CypherNova1337/sourcemapper)

Code splitting means admin-only components live in chunks your browser never requests. They’re still on the CDN. The webpack runtime (or Vite’s preload map in the entry bundle) contains the mapping from chunk IDs to filenames. Extract it, build the URLs, and download every chunk. This is where hidden routes, internal endpoints, and admin API clients live.

Next.js deserves its own checklist:

Once you have readable source, search for the vocabulary of the permission model:

That vocabulary becomes your payload list. Every role name you find is a value to try in mass assignment. Every permission string tells you which endpoints are supposed to be gated.

Disabled introspection is not a security control. Most servers still return “Did you mean…” field suggestions, and Clairvoyance can reconstruct most of a schema from them. Combine that with the operations you pulled from the bundle and you’ll usually have every mutation the admin UI uses.

[GitHub - nikitastupin/clairvoyance: Obtain GraphQL API schema even if the introspection is disabled](https://github.com/nikitastupin/clairvoyance)

The iOS and Android clients often talk to older API versions or separate mobile gateways. Pull the APK, decompile it, and diff its endpoint list against the web app’s. Anything only the mobile app calls deserves a close look.

This is the step that separates experts from everyone else. Every authorization bug is a disagreement between two components about who you are or what you’re asking for. Find the components, then make them disagree.

In a typical stack, a check can live in any of these places:

When a check lives at the gateway, the service behind it often trusts every request it receives. That’s your opening.

If the gateway blocks /api/v2/admin/\* but the backend framework normalizes paths differently, small variations slip through:

A 403 on the clean path and a 200 on a variant is a textbook gateway-bypass finding.

Gateways often authenticate the request and then pass identity downstream in headers like X-User-Id, X-Tenant-Id, X-Roles, or X-Forwarded-User. If the gateway doesn't strip client-supplied versions, you can set them yourself. Also try routing-override headers like X-Original-URL and X-Rewrite-URL, and method overrides like X-HTTP-Method-Override.

When /v2/users/{id} enforces ownership, request /v1/users/{id} and /internal/users/{id}. Check alternate hosts too — api-staging, legacy-api, regional subdomains. Old versions and side doors rarely get the same authorization middleware as the flagship API.

The classic Broken Function Level Authorization example — the UI hides the delete button, you send the DELETE anyway — still works more often than it should. But once you’ve run your admin corpus through Autorize, the easy ones are found. The interesting BFLA lives in the inconsistencies.

Developers often protect the route but not every verb on it. If GET /api/v2/users/{id} is correctly scoped, try PUT, PATCH, and DELETE on the same path even when the UI never sends them. Framework decorators applied to one handler frequently miss its siblings.

The main endpoint is usually protected. The alternate paths to the same outcome often aren’t:

In GraphQL, authorization is per-resolver, and that’s where it breaks. A common pattern: the users query is locked down, but organization { members { email role } } resolves the same data through a nested field with no check. Mutations are worse — teams protect the queries they ship to the UI and forget the mutation that only the admin panel calls. Test every mutation you pulled from the bundle with your low-priv token.

A 403 means a check exists. A 400 with a validation error means you got *past* authorization and hit input validation — the function is reachable. Fix the payload and try again. Many BFLA findings start as a 400 that should have been a 403.

Broken Object Level Authorization is still the most common high-impact API bug. The beginner version is swapping your invoice UUID for someone else’s. UUIDs killed enumeration, so the expert version is about two things: harvesting identifiers, and finding the places where ownership is checked against the wrong value.

UUIDs aren’t secret — they’re just unguessable. Applications leak them constantly:

Also check the ID format itself. UUIDv1 embeds a timestamp and node ID and can be predicted. Relay-style GraphQL global IDs are usually just Base64 of something like User:1042 — decode, change the integer, re-encode.

The most productive BOLA tests don’t swap the obvious ID. They exploit endpoints that receive more than one identifier and check only one of them:

Sometimes you can’t read their object directly — but you can attach it to yours. Reference a victim’s file ID as an attachment on your own ticket, then download it through your ticket. Add a victim’s document ID to your own project, then view it inside the project. The fetch endpoint checks ownership of the container, not of what’s inside it.

Read-only BOLA leaks data. Write BOLA modifies other tenants’ state — changing their payout details, deleting their records, reassigning their resources. Programs pay accordingly. Test every state-changing endpoint with a foreign ID, not just the GETs.

Broken Object Property Level Authorization covers two sides of the same failure: reading properties you shouldn’t see, and writing properties you shouldn’t set. Mass assignment is the write side, and it’s where privilege escalation hides when every endpoint looks locked down.

Don’t guess blindly. Diff what the API returns against what the UI sends:

Try flat, nested, and framework-specific forms:

```
{"name": "test", "role": "admin"}
{"name": "test", "permissions": {"is_admin": true}}
{"name": "test", "organization": {"id": "<other_org>"}}
user[role]=admin
```
The nested organization payload is the dangerous one in multi-tenant apps. ORMs that support nested writes may reassign your account into another tenant outright.

Update endpoints get hardened because everyone tests them. Creation paths often bind more fields: signup, accepting an invite, SSO first-login provisioning, and API key creation. A scopes array on an API key request, or a role on an invite acceptance, is a quieter route to the same escalation.

A 200 on your PATCH doesn’t mean the field stuck. Many APIs echo your input back without saving it. Re-fetch the object from a clean request, then prove the escalation by actually performing an action the new role allows.

Most testers check authorization at a single moment. Real applications change permissions constantly — users get invited, promoted, demoted, removed. Every transition is a place where old and new state can coexist.

Remove your low-priv account from Tenant A, then immediately replay requests with its existing token. Do the same after a demotion from admin to member. Stateless JWTs stay valid until they expire unless the backend checks a revocation list, and permission caches can lag for minutes or hours. A removed user who can still export data is a clean, high-severity finding.

Invites are a tenant boundary that’s crossed on purpose, which makes them fragile:

Apps that let one user belong to multiple orgs often select the active tenant with a header like X-Org-Id or a path segment, separate from the token. If the backend trusts that selector without confirming your membership, you can switch into any tenant whose ID you've harvested.

Seat limits, invite quotas, and role downgrades are often check-then-act operations. Burp Repeater’s single-packet attack lets you send 20 or more requests that land within the same millisecond. Use it to blow past a seat limit, or to fire privileged actions in the window between a demotion being requested and being applied.

Access control bugs get downgraded or closed as “informative” more than any other class, almost always because the report didn’t prove the chain. A 200 status code is not impact.

Keep the reproduction to the minimum number of requests, include them raw, and state exactly which role and tenant each token belongs to.

Scanners like Nuclei and crawlers like Katana are good at what they do: misconfigurations, exposed files, known CVEs. They can’t tell you that a member shouldn’t be able to export the admin report, because they don’t know what a member is.

That knowledge is your edge. Map the permission model. Recover the full feature set from the frontend. Find where each check lives, then find the component that skips it. Test every transition, not just every endpoint.

The vulnerabilities didn’t disappear when the parameter tampering tricks died. They moved into the gaps between services — and that’s exactly where you should be looking.
