# One Pending Invitation Was Enough to Restore Revoked Admin Privileges

- **Source URL:** https://cyghost.medium.com/one-pending-invitation-was-enough-to-restore-revoked-admin-privileges-9408c10f83d2
- **Fetched from:** https://cyghost.medium.com/one-pending-invitation-was-enough-to-restore-revoked-admin-privileges-9408c10f83d2?source=rss-8116f81382d0------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14951 (id 14951)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** seif nasr / Sat, 17 Oct 2026 23:59:40 GMT

During a web application security assessment, I was testing a team management system with different roles and permission levels.

Team owners could assign administrators, while administrators could invite new users and grant them roles.

Everything appeared to work as expected. But while examining the authorization logic, I started asking a different question:

**Does revoking a user’s privileges also prevent previously initiated actions from granting those privileges later?**

I decided to test this using accounts under my control.

First, I used an administrator account to invite another account and assign it the Admin role. I left the invitation pending.

Next, I switched to the team owner’s account and downgraded the original administrator to Member.

At this point, the original account no longer had administrative privileges. It should no longer have the same authority to manage team permissions.

But what would happen to the invitation created before the downgrade?

I accepted the existing invitation using the second account.

The result was unexpected: the invited account successfully obtained Admin privileges, even though the original inviter had already lost that role.

I then verified the new account’s actual permissions. It could modify the roles of other team members, including the original administrator whose privileges the owner had revoked.

**That was where the real security impact became clear.**

Consider a team using the application to manage its members and resources.

An administrator can invite additional accounts and assign them administrative privileges. Later, the owner decides that this administrator should no longer have that level of access and downgrades the account.

If previously issued invitations can still grant Admin privileges, revoking the original administrator’s role may not fully prevent further administrative access. An account invited earlier could accept its pending invitation afterward and gain the ability to change other team members’ permissions.

In other words, the owner revoked the original administrator’s authority, but the application still allowed an existing invitation to create a new path to administrative control.

The issue wasn’t simply that an invitation link remained valid or that pending invitations were not clearly displayed in the interface.

**The core problem was that a previously issued invitation could still grant administrative privileges after the inviter’s permissions had changed.**

This raises an important question in authorization design: should permissions be checked only when an operation is initiated, or should they also be considered when that operation is completed?

In this case, testing revealed that a pending operation could have security consequences even after the initiating user’s privileges had been revoked.

I documented the reproduction steps, verified the impact using controlled test accounts, and recorded a proof-of-concept video demonstrating the complete scenario.

**The takeaway:**

Access control testing isn’t just about checking whether a Member can perform an Admin-only action. It’s also about testing what happens when roles change and whether previously initiated operations can still grant privileges that are no longer authorized.

Sometimes, the problem isn’t the permission itself. It’s when the application checks it.
