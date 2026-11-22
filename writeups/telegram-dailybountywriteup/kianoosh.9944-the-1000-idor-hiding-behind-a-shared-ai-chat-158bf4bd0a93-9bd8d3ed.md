# The $1000 IDOR Hiding Behind a Shared AI Chat

- **Source URL:** https://medium.com/@kianoosh.9944/the-1000-idor-hiding-behind-a-shared-ai-chat-158bf4bd0a93
- **Fetched from:** https://medium.com/feed/@kianoosh.9944
- **Fetched:** 2026-11-22
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14995 (id 14995)
- **Method:** medium-rss-content readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
### *How a shared conversation exposed a private skill identifier, and an overlooked endpoint turned that identifier into confidential instructions.*

***Disclosure note:*** *The target hostname, authentication material, real UUIDs, and private contents are redacted. API paths and response field names are preserved for educational purposes. All testing described here used accounts under the researcher’s control.*

### A shared conversation should not mean shared secrets

In July 2026, I reported an authorization flaw in an AI workflow platform that allowed one regular user to retrieve another user’s **private skill instructions**.

The surprising part was not that a shared chat referenced a skill. It was that the reference could be passed to a different API endpoint, which returned information the same user was explicitly forbidden to access elsewhere.

The issue required no administrator privileges, UUID brute-forcing, or access to the victim’s account. It involved **two regular users in the same customer organization**, a chat the victim chose to share, and one API endpoint that did not enforce the expected object-level access control.

The report was eventually accepted and resolved, with a **bounty awarded on 20 November 2026**.

### Understanding the trust boundary

The application supported reusable AI *skills* containing instructions, descriptions, and related configuration. Some skills were private and scoped to a particular counsel or repository. Users could also share chats with colleagues in their customer organization.

Those are two different permissions:

- **Can view a shared chat:** Permission to see the conversation that was shared.
- **Can read a private skill:** Permission to access the underlying skill’s private configuration and instructions.

A shared conversation should not silently grant the second permission.

The vulnerable flow crossed precisely that boundary:

Victim creates a private skill

|

Victim uses it in a chat

|

Victim shares the chat customer-wide

|

Attacker reads the shared chat feed

|

Feed reveals private skill UUID

|

Attacker calls POST /skills/{uuid}/diagram

|

API returns private instructions and metadata

### Reproducing the issue with two accounts

For this test, I used two accounts belonging to the same customer:

- **Account A:** A regular user acting as the attacker.
- **Account B:** A regular user acting as the victim.

Account B created a **non-shared, counsel-scoped private skill** with a unique marker in its instructions, used that skill in a chat, and shared the chat with coworkers. Crucially, the secret marker was **not** present in the shared conversation itself.

All request examples below use the redacted host https://\[REDACTED-HOST\]. The UUIDs and response values are illustrative placeholders.

### Step 1: Read the shared chat feed

As Account A, I requested the shared session’s user feed:

```
GET /api/backend/v1/sessions/{shared_chat_uuid}/user_feed HTTP/1.1
Host: [REDACTED-HOST]
Cookie: <ACCOUNT_A_SESSION>
```
The feed included a reference to the victim’s private skill:

```
{
  "manually_selected_skill_ids": [
    "VICTIM_PRIVATE_SKILL_UUID"
  ]
}
```
This was the discovery point. **I did not need to enumerate or guess skill identifiers.** The application supplied the UUID as part of a resource Account A was allowed to view.

Importantly, learning an object ID should not be equivalent to receiving permission to read the object.

### Step 2: Confirm the usual access checks worked

Before testing the diagram functionality, I tried related resources with Account A’s session:

```
GET /repositories/{victim_repository_uuid}  -> 403 Forbidden
GET /skills/{victim_skill_uuid}/versions    -> 403 Forbidden
GET /skills/{victim_skill_uuid}/permissions -> 403 Forbidden
```
These responses showed the application **did recognize the skill and repository as private** in other areas of the API.

### Step 3: Call the diagram endpoint

I then supplied the same private skill UUID to a different endpoint, still using Account A’s credentials:

```
POST /api/backend/v1/skills/{victim_skill_uuid}/diagram HTTP/1.1
Host: [REDACTED-HOST]
Cookie: <ACCOUNT_A_SESSION>
Content-Type: application/json
```
`{}`
Instead of denying access, the server responded with **HTTP 200 OK** and returned private information associated with Account B’s skill. The following is a sanitized representation of the fields observed:

```
{
  "description": "Victim-only description: <PRIVATE_MARKER>",
  "instructions": "Victim-only instruction: <PRIVATE_MARKER>",
  "visibility": "counsel",
  "user_id": "<VICTIM_USER_UUID>",
  "counsel_id": "<VICTIM_COUNSEL_UUID>",
  "repository_name": "<PRIVATE_REPOSITORY_NAME>",
  "is_shared": false,
  "can_manage": false
}
```
That response established the authorization failure: **Account A could read Account B’s private instructions even though the skill was not shared and related endpoints returned 403.**

The key observation was the private marker appearing in the diagram response, **not** in the shared chat. This ruled out the simpler explanation that the victim had deliberately shared those instructions in the conversation.

### Why this was an IDOR, not merely a UUID leak

Exposing a UUID can be undesirable, but an identifier is not an access token. Secure APIs should still verify whether the requesting user is authorized to access the referenced object.

Here, the diagram endpoint appeared to retrieve and serialize skill information without applying the same private-skill read checks enforced by other endpoints. The exact internal implementation was not visible to me; this conclusion came from the contrasting API responses.

The result was a **horizontal authorization bypass**: one ordinary user accessed another ordinary user’s private resource within the same customer organization.

This was **not** a demonstrated cross-tenant compromise, and I did not need to claim one to show real impact.

### What could an attacker learn?

Depending on what an organization stored in a private skill, the exposed data could include:

- Confidential system or workflow instructions and prompt logic.
- Proprietary descriptions and internal operating procedures.
- Private repository or counsel names and configuration context.
- Identifiers linking the skill to its owner and organizational context.
- Additional reference or installation metadata, where present.

For teams using private skills to encode legal or client-specific workflows, disclosure could reveal information that was intentionally restricted to a smaller audience. The demonstrated impact was **unauthorized read access**; I did not demonstrate account takeover or cross-tenant access.

### Fix verification and resolution

During follow-up, triage reported that it could no longer reproduce the bug because the diagram request returned **403 Forbidden**.

I retested on **26 August 2026** with two separate users and a newly created private skill containing a fresh marker. This time, Account A received 403 responses from the related private endpoints **and** from:

`POST /skills/{victim_skill_uuid}/diagram -> 403 Forbidden`
The private instructions and marker were no longer disclosed. I confirmed to triage that the issue was no longer reproducible on the deployment I tested. I cannot establish the exact date or code change that fixed it, but the observed behavior was consistent with a successful remediation.

After the report was forwarded to the company, the final acceptance and payout arrived on **20 November 2026**.

- **27 July 2026:** Original vulnerability report submitted.
- **25 August 2026:** Triage requested a fresh reproduction after observing 403.
- **26 August 2026:** Retest confirmed the endpoint no longer exposed private skill data.
- **20 November 2026:** Report accepted, $1000 bounty awarded, and status changed to resolved.

### What developers and hunters can take away

The fix is conceptually straightforward, although applying it consistently across an application requires care:

1. **Authorize the object, not just the endpoint.** Before producing a skill diagram, check whether the caller has read access to that specific skill.
2. **Apply the same checks to derived views.** Diagrams, previews, exports, summaries, and metadata responses can all disclose protected source data.
3. **Do not treat UUID secrecy as an authorization control.** Shared resources, logs, and API responses may reveal identifiers through legitimate product behavior.
4. **Minimize unnecessary references in shared data.** If the shared-chat feed does not need to expose a private skill UUID, omit it.
5. **Test with two real user contexts.** A useful regression test is: User A can view a shared session, but cannot retrieve User B’s private skill through any nested endpoint.

For bug bounty hunters, the interesting signal here was **inconsistent access control**. The application’s main private-resource endpoints returned 403, yet a less obvious, derived-data endpoint returned 200 and disclosed the protected content.

### Final thoughts

This case reinforced an important lesson: **a correctly protected primary API does not guarantee that every alternate representation of the same resource is protected.**

One user could legitimately see a shared chat. That did not mean they should be able to retrieve the private skill powering it. A leaked identifier made the object easy to reference; the missing authorization check made it vulnerable.

The issue has since been retested as no longer reproducible, and the report was rewarded with **$1000**. For me, the best part of this finding was the clear authorization boundary: one request returned 403, another returned private data, and the difference was enough to demonstrate a concrete security problem.

*Thanks for reading.* Happy hacking.
