# One Invite Endpoint, One Race Condition — 4 Bugs Later

- **Source URL:** https://medium.com/@raslanco/one-invite-endpoint-one-race-condition-4-bugs-later-b48de71b280c?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20260228113022/https://medium.com/@raslanco/one-invite-endpoint-one-race-condition-4-bugs-later-b48de71b280c
- **Fetched:** 2026-11-19
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/12709 (id 12709)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# One Invite Feature, One Race Condition — 4 Bugs Later

Sometimes the most interesting vulnerabilities don’t require complex payloads or advanced exploitation chains. Sometimes, all it takes is changing one field in a JSON request.

While testing a team-based SaaS platform, I noticed something simple:

The UI strictly limited how many privileged roles (Admins and Creators) a team could have.

Naturally, I wondered:

Is that restriction actually enforced on the server… or just in the frontend?


Here’s exactly how I found out.

— -

\## Step 1 — Understanding the Role Model

The platform allowed multiple user roles:

\- Admin 

- Creator 

- Observer

- Admins and Creators were limited to a fixed number of seats.
- Observers were unlimited.
- The UI blocked adding more Admins/Creators once the seat limit was reached.
- However, Observer invitations continued to work without restriction.

This suggested the possibility that:

\- Seat limits might only be enforced client-side.

- Backend validation might be incomplete.

So I started by inviting several users as Observers through the normal interface.

Everything worked as expected.

— -

\## Step 2 — Direct Role Manipulation via API (Successful Exploit)

After intercepting a role update request:

\- I located the “role” field in the JSON body.

- I modified:

— “observer” → “admin”

— “observer” → “creator”

- I forwarded the request.

- The server returned success.

- The user’s role was upgraded.

- The seat limit was exceeded.

- No backend validation blocked the change.

This confirmed:

- Seat limits were not enforced during role updates.
- The backend trusted the modified role value.
- Privileged users could be created beyond the allowed quota.

— -

\## Step 3 — Testing Race Condition Variants (Mixed Results)

After the initial finding, I explored timing-based scenarios to test enforcement depth.

\### Scenario A — Upgrade Joined Observer + Invite Creator (Failed)

\- One Creator seat remaining.

- Upgrade an existing joined Observer to Creator.

- Simultaneously invite a new Creator.

- Result: ❌ Failed.

— -

\### Scenario B — Downgrade Joined User + Invite Two Creators (Failed)

\- Downgrade one joined Creator.

- Attempt to invite two new Creators quickly.

- Result: ❌ Failed.

— -

\### Scenario C — Upgrade Two Invited Users Simultaneously (Failed)

\- Invite two Observers.

- Attempt to upgrade both to Creator at the same time.

- Result: ❌ Failed.

— -

\### Scenario D — Upgrade Two Joined Observers Simultaneously (Succeeded)

\- Two joined Observers exist.

- One Creator seat remaining.

- Send two upgrade requests simultaneously.

- Result: ✅ Both upgraded successfully.

- Seat limit bypassed.

This indicated:

\- The lock did not properly wrap updates to existing users.

— -

\### Scenario E — Upgrade Joined User + Invite New Creator (Succeeded)

\- Upgrade one joined user to Creator.

- Simultaneously invite a new Creator.

- Result: ✅ Both succeeded.

- Seat limit bypassed again.

This revealed:

\- Invitation creation and role update operations were not protected under a unified lock.

- Quota validation was not atomic.

— -

\### Scenario F — Invite Observers + Upgrade with Race Condition (Succeeded)

\- Invite multiple Observers.

- Immediately send parallel role update requests.

- With proper timing (3–4 attempts required):

— Role escalation succeeded.

— Seat limits were bypassed.

- Result: ✅ Timing-sensitive success.

This confirmed:

- The race condition was real.
- Exploitation required precision but was reproducible.
