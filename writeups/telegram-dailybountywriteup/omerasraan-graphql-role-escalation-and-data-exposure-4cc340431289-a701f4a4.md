# GraphQL Role Escalation and Data Exposure

- **Source URL:** https://medium.com/@omerasraan/graphql-role-escalation-and-data-exposure-4cc340431289?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20251012174739/https://medium.com/@omerasraan/graphql-role-escalation-and-data-exposure-4cc340431289
- **Fetched:** 2026-11-23
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/9881 (id 9881)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# GraphQL Role Escalation and Data Exposure

.بسم الله الرحمن الرحيم, اللهم صلي وسلم وزد وبارك على سيدنا محمد وعلى آله وصحبه وسلم

Hey everyone, it’s Omar here! This is my first write-up, and I’m excited to share how I discovered two impactful bugs in a program using GraphQL Enumeration.

The program “example.com” helps teams work together by creating workspaces where people can collaborate on building websites and web apps without coding, using easy drag-and-drop tools.

First finding: **Publisher Can Invite Admin Users Without Proper Permissions**

Let’s walk into the steps:

1️⃣ I started by using the program as a normal user to understand its logic.

2️⃣ I intercepted the requests using Burp Suite and noticed the program uses **GraphQL** to fetch data.

3️⃣ Using the **InQL extension** in Burp Suite, I gathered all **GraphQL** mutations.

➜ **How to use InQL:**

- Add the URL of the GraphQL endpoint.
- In the request template, select it and click “Analyze.”
- You’ll see all the GraphQL mutations and queries.

4️⃣ While analyzing, I found this mutation: **createWorkspaceInvites**

it looked like this:

```
mutation createWorkspaceInvites($input: CreateWorkspaceInvitesInput!) {
  createWorkspaceInvites(input: $input) {
    workspaceInvites {
      id
      email
      createdAt
      existingUser
      redeemed
      role
      workspaceName
    }
  }
```
Only owners and admins should be able to send invites.

5️⃣ I sent a request as a **Publisher** (who shouldn’t have invite permissions) with this query:

`{"input":{"data":[{"email":"victim@gamil.com","role":"GUEST","workspaceId":"WorkspaceID","createdById":"THE ID OF THE OWNER"}]}}`
6️⃣ At first, I saw this error:

`"message":"Unknown operation named \"InviteUsersCreateWorkspaceInvites\"."`
**This means the server expected that operation name.**

7️⃣ I resent the correct query:

```
mutation InviteUsersCreateWorkspaceInvites($input: CreateWorkspaceInvitesInput!) {
  createWorkspaceInvites(input: $input) {
    workspaceInvites {
      id
      email
      createdAt
      existingUser
      redeemed
      role
      workspaceName
    }
  }
}
```
with the same Variables.

✅ The invite was created successfully — a **Business Logic Access Control** issue.

💣 But it got even worse: I tried sending an invite with the role “ADMIN” — and it **worked**!🔥🔥🔥🔥

A normal user could escalate their privileges by inviting themselves as an admin.

I reported this bug to the program through Bugcrowd.

**Second Finding: Unauthorized Access to Billing and Plan Data**

While testing GraphQL endpoints, I found a critical issue exposing sensitive billing data. Even as an **Editor** (who shouldn’t have this access), I could retrieve full billing and subscription details.

**Steps to Reproduce:**

1️⃣ Log in as an **Owner** and navigate to the billing settings page.

2️⃣ In Burp Suite, intercept the GraphQL request:

➜ The request body includes the `PlanSettingsBillingWorkspace` operation.

3️⃣ Copy the entire request body.

4️⃣ Log out and switch to an **Editor** account in the same workspace.

5️⃣ Resend the exact same request in Burp Suite using the Editor’s session cookies.

✅ The server still responded with full billing data (e.g., customer IDs, invoices, payment methods) — information that should only be accessible by **Owners/Admins**.

**Impact:**

Editors could access **sensitive workspace billing data** that should be restricted to higher-privileged users.

**Clarification:**

Although my report was marked as “Informational” and a “duplicate,” this doesn’t mean the bug wasn’t real or impactful. It only means the team was already aware of it — not that it wasn’t a valid vulnerability.
