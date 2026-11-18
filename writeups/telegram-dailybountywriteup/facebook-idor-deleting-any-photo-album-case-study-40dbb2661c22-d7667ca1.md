# Facebook IDOR

- **Source URL:** https://masimshahzad.medium.com/facebook-idor-deleting-any-photo-album-case-study-40dbb2661c22
- **Fetched from:** https://masimshahzad.medium.com/feed
- **Fetched:** 2026-11-18
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14987 (id 14987)
- **Method:** medium-rss-content readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
### Facebook IDOR: How Any Photo Album Could Be Deleted

### A $12,500 bug bounty case where a privileged app token and a missing ownership check met on a single Graph API call

*AI-assisted: drafted with AI help from public sources, then reviewed and edited. This is an analytical case study of a public disclosure, not my own discovery.*

Your photos could vanish without you touching a thing. In early 2015, Laxman Muthiyah reported a [Facebook IDOR](https://thezerohack.com/how-i-hacked-your-facebook-photos) that let one user delete photo albums owned by other users, Pages or groups, as long as the album was visible to them. Facebook shipped a fix in under two hours after acknowledging the report and paid $12,500.

***Disclaimer:*** *Educational and defensive use only. This was fixed in 2015. Request formats, token types and reproduction details are intentionally omitted.*

### Vulnerability Overview

- **Type:** Insecure direct object reference (IDOR) / broken object-level authorization on a delete operation
- **CWE (analytical mapping, not from the source):** CWE-639 (Authorization Bypass Through User-Controlled Key), CWE-862 (Missing Authorization)
- **CVE:** Not reported
- **Severity/CVSS:** Not reported. Bounty: $12,500, source-reported

### How the Facebook IDOR Worked (high level)

Facebook’s Graph API is the shared back end for its own apps and for third-party developers. Each access token carries the capabilities of the app that issued it. Public developer documentation said albums could not be deleted through the API, and a normal developer token was refused with a message saying the app lacked that capability.

That refusal was a clue. It implied *some* app had the capability. The researcher tried a token belonging to Facebook’s own mobile app, which is more privileged, and the delete worked on his own album. The real question came next: would it work on an album that was not his?

It did. The endpoint checked whether the calling *app* was allowed to delete albums, but not whether the calling *user* owned the album named in the request. Album IDs are not secret, so anything a user could view became something they could erase.

### Impact

Per the researcher, an attacker could delete any album they could see: public albums of individuals, plus albums owned by Pages and groups. For people, that is permanent loss of memories. For brands and communities, it is destructive vandalism at scale, with no social engineering needed.

### Preventing Facebook-Style IDOR in Your API (my own analysis)

**1. Authorize the object, not just the caller.** App capability, token scope and user identity are separate checks. Every read, update and delete must confirm that this user may act on this specific object.

**2. Centralize the policy.** Put ownership and role logic in one authorization layer that every client path calls, including first-party apps.

**3. Give destructive actions extra friction.** Soft-delete with a restore window, rate-limit bulk deletes, and log actor plus owner for every removal.

\# Pseudocode: object-level authorization on delete

def delete\_album(album\_id, ctx):

album = albums.get(album\_id)

if album is None:

raise NotFound()

if not ctx.app.has\_capability("album:delete"):

raise Forbidden("app not permitted")

if not policy.can\_delete(actor=ctx.user, resource=album):

audit.log("denied\_delete", ctx.user.id, album.owner\_id)

raise NotFound() # don't confirm existence to non-owners

albums.soft\_delete(album\_id, by=ctx.user.id, restore\_days=30)

audit.log("album\_deleted", ctx.user.id, album.owner\_id)

def can\_delete(actor, resource):

return (resource.owner\_id == actor.id

or actor.is\_admin\_of(resource.owner\_id)) # page/group admins

### Key Takeaways

- “This app may delete albums” and “this user may delete this album” are different questions; answer both.
- First-party clients are not a trust boundary. Their tokens reach the same API attackers can.
- Error messages that reveal hidden capabilities are a map for testers; keep them generic.

### Credit & Sources

Research by **Laxman Muthiyah**: [Deleting any photo albums — How I Hacked Your Facebook Photos](https://thezerohack.com/how-i-hacked-your-facebook-photos) (originally published February 2015; the page now shows a later update date). Facts come from that source; analysis and code are original.

Next breakdown: the Stripe session lockout that missed one server-side check. Follow @masimshahzad for daily bug bounty breakdowns.
