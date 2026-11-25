# Finding Sensitive Backend Information Through GraphQL Errors

- **Source URL:** https://medium.com/@ananya.itims/finding-sensitive-backend-information-through-graphql-errors-72f82ad2c27b?source=rss------bug_bounty-5
- **Fetched from:** https://medium.com/@ananya.itims/finding-sensitive-backend-information-through-graphql-errors-72f82ad2c27b?source=rss-f3edf504d2cb------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:**  (id 14852)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** Ananya Rathod / Tue, 25 Aug 2026 19:22:57 GMT

While testing a web application, I was looking at its GraphQL endpoint and started checking how it handled invalid queries.

Nothing unusual so far. GraphQL is expected to return an error when a query contains a field that doesn’t exist.

I tried a simple query with an invalid field:

query {

users {

id

Role

}

The request was rejected, as expected.

What caught my attention was the response.

Instead of returning only the GraphQL validation error, the application was also returning a detailed Node.js stack trace.

The response exposed internal information such as backend file paths, module names, and details about the GraphQL validation process.

What was being exposed?

The response contained information similar to:

/app/node\_modules/graphql/…

/app/node\_modules/…

along with the stack trace showing how the request was being processed internally.

This isn’t information that an external user needs to see.

From a user’s perspective, an error such as:

Cannot query field “Role” on type “User”

is enough.

The additional stack trace doesn’t help the user fix their request, but it does give someone testing the application more information about what’s happening behind the API.

Why does this matter?

This type of issue falls under information disclosure / verbose error handling.

On its own, exposing a stack trace doesn’t necessarily give an attacker direct access to the application.

But it can make reconnaissance easier.

From the response, an attacker can start learning things about:

That information can then be combined with other findings.

For example, knowing the technologies and dependencies an application uses can make it easier to look for known vulnerabilities or identify areas worth testing further.

So while the error itself isn’t an exploit, it is information that the application shouldn’t be giving away.

Reproducing the issue

The issue was straightforward to reproduce.

I sent an invalid GraphQL query to the /graphql endpoint and intentionally requested a field that wasn’t part of the schema.

The server returned a 400 response containing the GraphQL validation error, but also included the internal stack trace.

No authentication bypass or complicated payload was required to trigger the behavior.

The interesting part was simply how much information the error response returned.

What should happen instead?

In production, detailed debugging information should stay on the server.

The client should receive a clean error response, for example:

{

“errors”: \[

“message”: “Cannot query field \”Role\” on type \”User\”.”

\]

The full stack trace can still be captured in server-side logs for developers and security teams.

It just shouldn’t be sent back to the person making the request.

Remediation

The recommended fix is fairly simple:

Closing

This was a good example of why I like testing error handling.

Sometimes you don’t need a complicated payload to find something interesting. A malformed request and a close look at the response can reveal quite a lot about what’s running behind an application.

A 400 Bad Request is expected.

A 400 Bad Request that also tells you how the backend is built is a different story.

If you’re running a GraphQL API in production, it’s worth checking what your errors actually return.

Because your users may not be the only ones reading them.
