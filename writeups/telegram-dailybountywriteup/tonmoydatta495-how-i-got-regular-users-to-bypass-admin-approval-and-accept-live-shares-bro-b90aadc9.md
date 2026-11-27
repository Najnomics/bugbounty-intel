# How I Got Regular Users to Bypass Admin Approval and Accept Live Shares (Broken Access Control) —…

- **Source URL:** https://medium.com/@tonmoydatta495/how-i-got-regular-users-to-bypass-admin-approval-and-accept-live-shares-broken-access-control-c4e086da86ec
- **Fetched from:** https://medium.com/feed/@tonmoydatta495
- **Fetched:** 2026-11-27
- **Channel:** @dailybountywriteup
- **Telegram message:**  (id 14905)
- **Method:** medium-rss-content readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
### How I Got Regular Users to Bypass Admin Approval and Accept Live Shares (Broken Access Control) — $250 Bounty

A writeup of a Broken Access Control / Privilege Escalation bug I found and got rewarded for. Target is referred to as \`redacted.com\` since disclosure of specific target details isn’t public.

**TL;DR**

While testing a role-based access control (RBAC) system on \`redacted.com\`, I found that the permission to “accept inbound live shares” — which is supposed to be locked to Organization Admins and Account Admins only — could actually be exercised by a plain regular user. Once that regular user hit “Accept,” the shared test data became visible to \*every\* member of their org, admins and non-admins alike, with zero admin approval in the loop. Reported it, got triaged, and it landed a P4 / $250 reward.

**Some Background: What’s a “Live Share” Anyway?**

The platform lets one organization run a network/app synthetic test and then share a live, real-time view of that test with people outside the org — think of it like sharing a live dashboard with a partner company or a client. Because this data can include internal network paths, target endpoints, and other testing details, the app’s permission model deliberately restricts \*accepting\* an inbound share to admin-level roles. The idea is simple: a regular employee shouldn’t be able to unilaterally pull in external test data and expose it to the whole org — that decision should sit with someone who has oversight.

At least, that’s the intent.

**How I Stumbled Onto It**

I was mapping out the RBAC matrix for the app — going role by role through what a regular user can and can’t touch, versus what’s gated behind Org Admin / Account Admin. Sharing and invitations are always an interesting attack surface for this kind of test, because they usually involve a state transition (invited → pending → accepted) that spans two different organizations. Anytime a workflow crosses an org boundary like that, it’s worth checking whether **both** sides of the handshake are actually enforcing the same permission checks, or whether only the “sending” side got the RBAC treatment and the “receiving” side was an afterthought.

That’s basically what happened here.

**The Actual Bug**

The permission gate existed — but only on paper (or more precisely, only in the UI for other flows). When I set up two separate orgs and sent a live share invite from one to a **regular user** in the other, the regular user’s invitation email led to an “Accept Invitation” action that… just worked. No redirect to “ask your admin,” no disabled button, no server-side check kicking it back. The share got accepted, and immediately every member of that second org — regular users included — could see the live share.

So in short:

- **Intended behavior**: only Org Admin / Account Admin can accept an inbound live share; everyone else in the org only sees it after that admin approves.

- **Actual behavior:** any regular user who receives the invite can accept it directly, and that single action exposes the share to the entire org.

**Steps to Reproduce**

1\. From Org A, create a test and send a live share invite to a user in Org B.

2. Make sure the recipient in Org B is a **regular user**, not an admin.

3. That regular user opens the invitation email and clicks Accept.

4. The live share is now visible org-wide in Org B — including to other regular users — without any admin ever touching the approval step.

I put together a short PoC video and a screenshot showing the regular user’s account role (confirmed via the org’s Users and Roles page) alongside the successful accept action, just to remove any ambiguity about privilege level during triage.

**Why This Actually Matters**

This isn’t just “a button worked that shouldn’t have.” A few concrete consequences:

**Privilege escalation via workflow, not exploit code:** The regular user didn’t need to break anything technically clever — they just used a normal feature flow that happened to skip a server-side authorization check. That’s the classic shape of a broken access control bug: the front door works fine, it’s just not checking who’s walking through it.

**Data integrity / governance:** Orgs that rely on this RBAC boundary to control what external test data gets pulled into their environment lose that control entirely. A regular employee can single-handedly bring in a live external test feed that leadership never approved.

**Compliance exposure:** For organizations with strict access-control requirements (SOC 2, internal audit policies, whatever their flavor of governance is), a gap like this between the documented permission model and actual enforcement is exactly the kind of thing that fails an audit.

**The Fix (Conceptually)**

The right fix is straightforward in principle: the “accept live share” action needs a server-side role check, not just a client-side / workflow-level assumption that only admins will ever reach that endpoint. Whoever is calling the accept action needs their role validated against Org Admin / Account Admin before the share is materialized org-wide — the UI hiding a button for regular users elsewhere in the app isn’t a substitute for that check existing on the actual accept path.

**Timeline**

\- \*\*Nov 25, 2025\*\* — Submitted the report.

- \*\*Dec 2025\*\* — Program requested more info; provided clarification.

- \*\*Jan 8, 2026\*\* — Program asked for a walkthrough on how to set up a test in the first place (fair — not every triager works in this exact product daily); I sent over a step-by-step with screenshots.

- \*\*Jan 12, 2026\*\* — Triaged and confirmed reproducible.

- \*\*Jan 13, 2026\*\* — Rewarded $250 / 5 points, marked resolved on the researcher side.

**Takeaways**

A couple of things I keep relearning from bugs like this:

**Check both sides of any invite/accept flow:** RBAC bugs love to hide in the “receiving” half of a two-party workflow, because teams often harden the initiating action and forget the acceptance action needs the same scrutiny.

**A hidden button isn’t an access control:** If the only thing stopping a regular user is that the UI doesn’t show them the option, that’s not enforcement — it’s obscurity. Always try hitting the underlying action directly (or via the flow it’s actually reachable from, like an email link) rather than trusting that a missing UI element means the path is closed.

**Patience pays in triage:** This one took about seven weeks from submission to reward, including a holiday shutdown gap. Worth following up politely rather than assuming it fell through the cracks.

— -

If you’re hunting on programs with sharing/invite features, this pattern — check what happens on the accept side, not just the invite side — is worth adding to your checklist.
