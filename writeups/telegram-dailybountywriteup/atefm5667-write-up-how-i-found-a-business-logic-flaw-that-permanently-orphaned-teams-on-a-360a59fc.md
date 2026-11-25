# Write-Up

- **Source URL:** https://medium.com/@atefm5667/write-up-how-i-found-a-business-logic-flaw-that-permanently-orphaned-teams-on-a-developer-platform-6be675083192
- **Fetched from:** https://medium.com/@atefm5667/write-up-how-i-found-a-business-logic-flaw-that-permanently-orphaned-teams-on-a-developer-platform-6be675083192?source=rss-238701c40f72------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14949 (id 14949)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** Mohamed Atef / Fri, 16 Oct 2026 02:16:57 GMT

**Author:** Mohamed Atef **Date:** October 2026 **Program:** Disclosed via Private Bug Bounty Program (HackerOne) — Pending Public Disclosure **Severity:** High (CVSS v4.0: 8.3) **Status:** Reported — Awaiting Triage **CWE:** CWE-862 — Missing Authorization

Bug bounty hunting is not always about finding memory corruption bugs or SQL injections. Some of the most impactful findings come from understanding how a system *should* work — and then proving that the backend doesn’t agree with the frontend.

This write-up covers a **business logic vulnerability** I discovered on a private developer portal during an authorized bug bounty engagement on HackerOne. The vulnerability allowed a team **Owner** to permanently downgrade their own role through a direct API call, completely bypassing the GUI restriction — leaving the team with **zero owners** and no recovery path.

I am not disclosing the program name or domain at this time, in line with responsible disclosure practices.

The platform I was testing is a **developer portal** where organizations create teams to manage applications, API credentials, and integrations. Teams follow a three-tier role model:

OWNER  >  ADMIN  >  MEMBER

**Key business rules (as documented in the GUI):**

The platform’s backend was built on **GraphQL**, powered by **Hasura** — an open-source GraphQL engine that auto-generates CRUD mutations over a PostgreSQL database.

While testing the team management features, I navigated to the **Team Settings → Members** page. I noticed I could edit the roles of other team members as an Owner, but my own row had the edit option restricted — as expected.

My first instinct was: *“Is this restriction only in the frontend?”*

I opened **Burp Suite** and intercepted the GraphQL request that fires when legitimately changing another member’s role. The request looked like this:

POST /api/v1/graphql HTTP/2

Host: \[REDACTED\]

Cookie: \_\_session\_0=\<JWT\_SESSION\_TOKEN>

Content-Type: application/json

{

"operationName": "EditRole",

"variables": {

"membershipId": "\<TARGET\_MEMBERSHIP\_ID>",

"role": "ADMIN"

},

"extensions": {

"clientLibrary": {

"name": "@apollo/client",

"version": "4.2.7"

}

},

"query": "mutation EditRole($membershipId: String!, $role: role\_enum) {\n update\_membership\_by\_pk(pk\_columns: {id: $membershipId}, set: {role: $role}) {\n role\n \_\_typename\n }\n}"

}

The mutation being called — update\_membership\_by\_pk — is a **Hasura auto-generated mutation**. This immediately caught my attention. Hasura auto-generates powerful CRUD operations, and if the row-level permission rules aren't carefully configured, they can be abused.

Before I could test self-modification, I needed my own membershipId. I fetched the team members list through the GraphQL API (another query the frontend calls normally). The response included my own membership record:

```
{
  "id": "memb_[REDACTED]",
  "role": "OWNER",
  "user": {
    "email": "[MY_EMAIL]",
    "name": "[MY_NAME]"
  }
}
```
With my own membershipId in hand, I moved to the Repeater tab in Burp Suite.

I modified the membershipId in the EditRole mutation to point to my **own** membership ID — keeping everything else the same, including my own Owner session cookie:

```
{
  "operationName": "EditRole",
  "variables": {
    "membershipId": "memb_[MY_OWN_ID]",
    "role": "ADMIN"
  }
}
```
I hit **Send**.

HTTP/2 403 Forbidden

{

"error": "You cannot modify your own owner role."

}

HTTP/2 200 OK

{

"data": {

"update\_membership\_by\_pk": {

"role": "ADMIN",

"\_\_typename": "membership"

}

}

}

The server returned 200 OK and confirmed my role was now ADMIN.

I refreshed the Team Members page. Here’s what changed:

Member A: Admin

Member B: Member

Me: **Owner**

Member A: Admin 

Member B: Admin

Me: **Admin Zero owners remaining**

The team now had **no owner**. I then tested whether I could promote myself back to Owner as an Admin:

***Result: Blocked.*** *The server correctly rejected the escalation attempt — only an Owner can assign the Owner role, and there was no longer one.*

The team was **permanently orphaned** with no in-platform recovery path.

At first glance, this might seem like a user hurting themselves. But the real impact is much broader:

Once there are zero owners, **no team member** — regardless of their role — can:

The team owned registered applications with API credentials and production integrations. With zero owners:

The only way to restore an owner is through out-of-band support contact. There is no self-service recovery. The broken state persists indefinitely.

A departing team owner (disgruntled employee, former contractor) could deliberately trigger this to **permanently lock an organization out of their developer resources** before leaving.

During testing, I found a related UI bug: when a **non-owner** (Admin) attempts to change a member’s role through the GUI, the interface shows **“Edit role successfully”** — but the backend silently rejects the operation and nothing actually changes. This false success message was reported separately as a Low severity issue.

The vulnerability stems from a **missing server-side authorization check** in the EditRole GraphQL mutation.

The platform uses **Hasura** as its GraphQL engine. Hasura auto-generates the update\_membership\_by\_pk mutation, and its row-level permission rules for the membership table were missing three critical checks:

Missing Check — — — -Consequence

requester.membership\_id != target.membership\_id:Owner can modify their own role

if target.role == OWNER AND ownerCount == 1 → reject:Team can have zero owners

Minimum-one-owner database invariant: Core business rule silently violated

The GUI enforced these rules in **JavaScript** — but JavaScript is client-side. Any user with Burp Suite can bypass it in seconds. The server should be the **single source of truth** for authorization decisions.

This is worth noting for developers using Hasura: **auto-generated mutations are powerful but dangerous if not properly gated.**

Hasura’s permission system allows you to define row-level rules per role. For the update permission on the membership table, the correct configuration should:

Without these rules, the Hasura mutation layer simply executes whatever valid SQL the client sends — as long as the user is authenticated. **Authentication ≠ Authorization.**

Add a filter to the update permission for the membership table:

```
{
  "filter": {
    "_and": [
      { "id": { "_neq": "X-Hasura-Membership-Id" } },
      {
        "_or": [
          { "role": { "_neq": "OWNER" } },
          {
            "team": {
              "memberships_aggregate": {
                "count": { "predicate": { "_gt": 1 } },
                "filter": { "role": { "_eq": "OWNER" } }
              }
            }
          }
        ]
      }
    ]
  }
}
```
Add a database-level constraint to ensure at least one OWNER exists per team at all times — making it impossible for the broken state to persist even if application-layer checks are bypassed.

This vulnerability is a reminder that **business logic flaws can be as impactful as technical exploits**. The platform had the right idea — the GUI correctly blocked self-demotion. But a security control that only lives in JavaScript is not a security control at all.

By intercepting a single GraphQL request and changing one parameter, it was possible to permanently destroy a team’s management capability and freeze all its production applications — with no way to recover without contacting support.

Always test what the GUI says you can’t do. Sometimes the server disagrees.

*This write-up was published following responsible disclosure via HackerOne. The program name and domain are withheld pending public disclosure authorization.*
