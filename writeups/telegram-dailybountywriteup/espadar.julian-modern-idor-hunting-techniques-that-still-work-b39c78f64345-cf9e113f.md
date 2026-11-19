# Modern IDOR Hunting Techniques That Still Work

- **Source URL:** https://medium.com/@espadar.julian/modern-idor-hunting-techniques-that-still-work-b39c78f64345
- **Fetched from:** https://web.archive.org/web/20261006212001/https://medium.com/@espadar.julian/modern-idor-hunting-techniques-that-still-work-b39c78f64345
- **Fetched:** 2026-11-19
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14916 (id 14916)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Modern IDOR Hunting Techniques That Still Work (Bug Bounty guide)

Most people learn IDOR with the same example.

A URL contains:

`GET /api/user/123`
You replace `123` with `124` and suddenly you're looking at someone else's data.

The problem is that modern applications rarely look like that anymore.

After spending countless hours hunting for authorization issues in bug bounty programs, I noticed something interesting: the vulnerability class hasn’t disappeared. It has simply evolved.

Developers started replacing sequential IDs with UUIDs.

Applications moved to GraphQL.

SaaS platforms became multi-tenant.

APIs became more complex.

Yet the underlying mistake remains exactly the same:

*The application trusts a user-supplied object reference without properly verifying ownership.*


This article summarizes some of the techniques that consistently produced results for me when testing modern targets.

## 1. Stop Looking Only at GET Requests

One of the biggest mistakes I made early on was focusing almost exclusively on read operations.

I would inspect:

```
GET /profile/123
GET /orders/456
GET /documents/789
```
and attempt classic object swapping.

Nowadays, many applications protect read endpoints reasonably well.

The interesting bugs often live in write operations.

Examples:

```
PATCH /api/profile
PUT /api/document
POST /api/share
DELETE /api/resource
```
Instead of asking:

*“Can I view another user’s object?”*

I started asking:

*“Can I modify another user’s object?”*

Write-based IDORs often lead to significantly higher impact because they affect integrity rather than confidentiality.

A leaked record is bad.

Modifying somebody else’s record is usually worse.

## 2. Hunt Relationships, Not Objects

Modern applications are built around relationships.

Instead of testing a single object identifier, I focus on how objects connect.

For example:

```
{
  "userId": "...",
  "teamId": "...",
  "workspaceId": "...",
  "projectId": "..."
}
```
Most testers immediately attack the visible object.

I prefer attacking the relationship.

Questions I ask:

- Can I move an object between tenants?
- Can I assign resources to another account?
- Can I reference a foreign workspace?
- Can I add myself to someone else’s project?

Many authorization failures appear when ownership is checked for the primary object but forgotten for a related object.

This pattern appears surprisingly often in SaaS environments.

## 3. UUIDs Are Not Protection

When I first encountered UUIDs everywhere, I assumed IDORs would become rare.

They didn’t.

The misconception comes from equating enumeration with authorization.

A UUID only makes guessing harder.

It does not validate ownership.

If I can obtain another user’s UUID from:

- logs
- exports
- invitations
- notifications
- shared resources
- API responses

then authorization becomes the only thing that matters.

I no longer ask:

*Can I guess the identifier?*


I ask:

*What happens if I already know it?*


That mindset shift alone uncovered several interesting findings.

## 4. Second-Order IDORs

These are some of my favorite bugs.

Nothing appears vulnerable during the initial request.

The issue only becomes visible later.

Example workflow:

1. Create a resource.
2. Modify a hidden reference.
3. Wait for a background process.
4. Observe the result elsewhere.

At first glance everything looks normal.

## Get julichaan’s stories in your inbox

Join Medium for free to get updates from this writer.

Hours later another feature consumes the manipulated object and suddenly accesses data belonging to another user.

Many hunters ignore asynchronous workflows because they require patience.

That’s exactly why they are worth investigating.

## 5. GraphQL Is an Authorization Goldmine

GraphQL changed how I test authorization.

Instead of dozens of endpoints, everything often lives behind a single endpoint.

The challenge becomes understanding relationships between objects.

Typical questions:

- Which queries accept object IDs?
- Which mutations accept foreign references?
- Which nested objects are returned automatically?

One recurring pattern is a correctly protected top-level query combined with an unprotected nested resolver.

The first authorization check succeeds.

The second one never happens.

As a result, data becomes accessible several levels deeper inside the graph.

Whenever I find GraphQL, I spend considerable time mapping object relationships before attempting fuzzing.

The results are often worth it.

## 6. Multi-Tenant Boundary Testing

Modern SaaS applications are built around tenants:

```
Organization
 ├── Users
 ├── Projects
 ├── Files
 └── Settings
```
Developers frequently implement user-level checks.

The mistake happens at tenant boundaries.

I always create multiple isolated environments and ask:

- Can Tenant A reference Tenant B resources?
- Can invitations cross organizations?
- Can exports contain foreign data?
- Can API filters escape tenant scope?

Many severe authorization issues originate from a missing tenant validation rather than a missing user validation.

## 7. Hidden IDs in Request Bodies

One lesson bug bounty taught me:

Never assume the URL contains the interesting identifier.

Today I spend more time inspecting JSON than URLs.

Fields like:

```
{
  "ownerId": "...",
  "organizationId": "...",
  "accountId": "...",
  "memberId": "...",
  "createdBy": "..."
}
```
often reveal more than path parameters.

Developers tend to validate visible identifiers while forgetting about secondary references buried inside request bodies.

The vulnerability isn’t always obvious.

Sometimes a single overlooked field changes everything.

## 8. Mass Assignment + IDOR

This combination deserves special attention.

The workflow usually looks like:

1. Find an endpoint that updates an object.
2. Discover fields the frontend never exposes.
3. Send additional attributes manually.
4. Observe unexpected behavior.

The impact increases dramatically when authorization weaknesses and excessive field binding collide.

Instead of merely viewing another object, the attacker gains influence over properties that were never intended to be user-controlled.

## 9. Follow the Business Logic

The best authorization bugs I found weren’t discovered by fuzzing.

They were discovered by understanding the application.

Questions that helped me:

- How does a customer invite another customer?
- How does billing work?
- How are files shared?
- How are reports generated?
- How are approvals handled?

Every workflow that moves data between users becomes an authorization test case.

The more business-critical the process, the more valuable the finding tends to be.

## Final Thoughts

If there’s one lesson bug bounty taught me, it’s this:

Modern IDOR hunting is no longer about changing numbers in URLs.

It’s about understanding relationships.

Understanding ownership.

Understanding how objects move through a system.

The highest-impact findings usually appear when you stop looking at endpoints and start looking at how the application models trust.

Identifiers changed.

Frameworks changed.

Architectures changed.

But authorization mistakes remain surprisingly human.

And that’s exactly why IDORs continue to be one of the most rewarding bug classes to hunt.
