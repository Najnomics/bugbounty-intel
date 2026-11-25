# BOLA in the Wild

- **Source URL:** https://medium.com/@neel.chauhan09/bola-in-the-wild-reading-another-users-full-profile-by-changing-one-uuid-e05ee078aa0e
- **Fetched from:** https://medium.com/@neel.chauhan09/bola-in-the-wild-reading-another-users-full-profile-by-changing-one-uuid-e05ee078aa0e?source=rss-dc15ab41b8c5------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14920 (id 14920)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** Neel Chauhan / Mon, 21 Sep 2026 20:11:48 GMT

**CWE-639: Authorization Bypass Through User-Controlled Key CWE-284: Improper Access Control CVSS 3.1: 6.5 (Medium)** — AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:N/A:N

Broken Object Level Authorization can’t be tested with a single account. You need two separate identities, so you can prove the server is failing to check *ownership*, not just failing to check *authentication*. I created two test accounts specifically for this, and used one to attack the other’s data.

```
GET /api/profile/{own-user-id} HTTP/2
Cookie: session=<authenticated as Account A>
```
HTTP/2 200 OK

Content-Type: application/json

```
{
  "ok": true,
  "profile": {
    "id": "{own-user-id}",
    "username": "account_a",
    "email": "account_a@example.com",
    "role": "user"
  }
}
```
Expected behavior. My session, my ID in the URL, my data back.

The question that defines a BOLA test is simple: does the server check that the {user-id} in the URL path belongs to the session making the request, or does it just look up whatever ID it's handed and return it?

I obtained a second account’s UUID (in this case, straightforward to get through the application’s own normal use, though in a real-world attacker scenario this could come from enumeration, a leaked ID in some other response, or brute-forcing a UUID structure if it turned out to be predictable). Then, still authenticated as Account A, I substituted that ID into the same request:

GET /api/profile/122b172f-f3cc-440a-820b-2b722ce596ea HTTP/2

Cookie: session=\<STILL authenticated as Account A>

```
{
  "ok": true,
  "profile": {
    "id": "122b172f-f3cc-440a-820b-2b722ce596ea",
    "username": "account_b",
    "email": "account_b@example.com",
    "full_name": "account_b",
    "bio": null,
    "avatar_url": null,
    "role": "user"
  }
}
```
Full profile object for an account I have no relationship to whatsoever, returned to a session that was never granted any access to it. No error, no 403, no ownership check at all. The server authenticated the request (confirmed I was logged in as *someone*), but never authorized it (never confirmed I was logged in as the *right* someone).

javascript

// vulnerable

function getProfile(req, res) {

const user = db.findById(req.params.id); // trusts the path param outright

return res.json({ ok: true, profile: user });

}

There’s no line anywhere in this handler that touches req.session.userId. The authenticated session and the requested resource are two completely disconnected values as far as this endpoint is concerned.

This finding is more than a generic data leak because of one specific field in the response: role. That turns a straightforward information disclosure into a reconnaissance tool. An attacker can iterate through UUIDs (or any other way of discovering them) and build a map of which accounts on the platform are administrators before ever attempting to compromise any of them, which meaningfully sharpens the targeting for a subsequent attack, like the privilege escalation and account-takeover findings I documented separately in this same engagement.

Beyond that, at scale, this endpoint alone is enough to harvest emails, usernames, and full names across the platform’s entire user base, which has obvious downstream value for phishing and credential-stuffing target lists.

I also tested whether the same pattern existed on the session-audit endpoint, since it dealt with per-user data too:

GET /api/sessions/audit HTTP/2

Cookie: session=\<Account A, with Account B's session/user identifiers substituted where applicable>

This came back correctly scoped, only ever returning Account A’s own session records, no cross-account leakage. Worth documenting as a negative result: it shows the BOLA issue on /api/profile/{id} isn't a platform-wide pattern repeated everywhere, it's specific to that endpoint's implementation, which is useful context for prioritizing the fix and checking whether other similarly-structured endpoints need the same review.
