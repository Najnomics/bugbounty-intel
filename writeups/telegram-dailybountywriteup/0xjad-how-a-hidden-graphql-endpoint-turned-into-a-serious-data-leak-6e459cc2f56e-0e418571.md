# How a Hidden GraphQL Endpoint Turned Into a Serious Data Leak

- **Source URL:** https://medium.com/@0xJad/how-a-hidden-graphql-endpoint-turned-into-a-serious-data-leak-6e459cc2f56e?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20260518062315/https://medium.com/@0xJad/how-a-hidden-graphql-endpoint-turned-into-a-serious-data-leak-6e459cc2f56e
- **Fetched:** 2026-11-19
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/13550 (id 13550)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# How a Hidden GraphQL Endpoint Turned Into a Serious Data Leak

I want to walk you through one of the most interesting bugs I’ve found recently, a hidden GraphQL endpoint that ended up leaking billing data across tenants on a multi-tenant platform.

When I first started looking at this target, I had no idea this was even there. There was no “click here to test me” sign. The interesting endpoint was buried inside a JavaScript file, didn’t appear in any documentation, and wasn’t linked from anywhere on the site.

So I want to break down exactly how I went from looking at a normal website to finding this. Let’s walk through it.

## Step 1: Spotting the First Clue in JavaScript

The first thing I always do on a new target is dig through the JavaScript files.

Modern websites or anything built with React, Vue, Angular ship a lot of JavaScript to the browser. And inside those files, you’ll often find references to the API endpoints the site uses. Things like:

`fetch("/api/graphql")`
or:

`axios.post("/api/users")`
So my workflow looks like this:

1. Open the website
2. Find the JavaScript files
3. Search inside them for API paths

On this target, the JavaScript referenced **two** GraphQL endpoints:

```
/api/graphql
/api/graphql/somethingweird
```
The first one was expected, the normal public GraphQL endpoint. But the second one made me pause. `/somethingweird` sounds like something internal. That was my first real lead.

## Step 2: Confirming the Endpoint Was Alive

The first thing I wanted to know was simple: does this endpoint even respond? And does it actually behave like a GraphQL server?

The smallest possible GraphQL query you can send is this:

```
{
  __typename
}
```
If the server replies with proper GraphQL-shaped JSON, you know you’re talking to a real GraphQL endpoint.

I sent that query, and it came back fine.

So now I knew:

- `/api/graphql/somethingweird` exists
- It accepts GraphQL queries
- It’s reachable from the internet

*So what can I actually* do *on this endpoint?*

## Step 3: Asking GraphQL What It Supports (Introspection)

GraphQL has a built-in feature called introspection.

It lets you ask the API: *“Hey, what queries do you support?”*

When introspection is enabled, you can send a special query that returns the entire schema, everything the API can do. The schema includes:

- All available queries
- All available fields
- What arguments each query needs
- What types each query returns

So I introspected both endpoints and compared them:

Endpoint \`/api/graphql\` had a much smaller schema. \`/api/graphql/somethingweird\` had several times as many queries.

And when I scanned through the query names, a lot of them looked internal, thing like billing jobs, customer details, job status, reprocessing jobs, support tools. Nothing a regular logged-in user should be touching.

## Step 4: The Sweep

There were a lot of query fields. Testing them by hand would have been miserable, so I wrote a script to do it for me.

The script did this for every query:

1. Pull the field definition from the introspection result
2. Figure out what arguments the query needed
3. Build a minimal valid query
4. Send it without any cookies or auth tokens
5. Check the response

The responses fell into a few clear buckets:

- **User is not authenticated** → The query is properly protected.
- **Validation errors** → I probably built the query wrong. Skip or retry.
- **Backend errors** → Interesting. The query ran but something inside it broke.
- **Returned data** → Very interesting. The query ran and gave me something.

That last bucket is the one I cared about.

## Step 5: Why `__typename` Was So Useful Here

When you’re testing a lot of unknown queries, you don’t know what each one returns. You don’t know which fields to ask for.

But you don’t need to. You just need to know if the query *runs at all*.

This is where `__typename` shines. `__typename` is a meta field that asks the server *"what type is this object?"* and it works on any GraphQL object.

So instead of guessing field names, my script just sent:

```
{
  someQuery {
    __typename
  }
}
```
If the server returned a valid response with a type name, that told me three things at once:

- The resolver executed
- It didn’t block the request
- It might be reachable without auth

I didn’t need to know everything about the query yet. I just needed to know if the door opened.

## Step 6: The Results

After the sweep finished, most of the queries came back as expected protected, asking for authentication. But some didn’t.

A small group of queries returned real data with no cookies, no tokens, nothing. And when I looked at their names, they were all related:

- Cloud billing jobs
- Customer details
- Job status
- Raw usage counts
- Reprocessing jobs

It wasn’t one random query that someone forgot to protect. It was a whole group of related queries, all from the same backend module, all missing the auth check.

That tells you a lot about the root cause. Instead of:

*One developer forgot to add a check on one query*


it looks more like:

*An entire backend module was deployed without the right authorization filter in front of it*


That’s a much stronger story to tell in the report, and a much more dangerous bug.

## Step 7: Finding the Entry Point

One of the exposed queries returned a list of billing/usage processing jobs. This was my entry point because it gave me job IDs.

The response had fields like:

```
jobId
tenant
status
usage counts
start time
end time
```
The important one was `jobId`. Job IDs are like keys, they unlock data in other queries. Once you have a real, valid ID, you can plug it into resolvers that take that ID as input and see what they give you back.

This is where the bug went from “I can see a list” to something much bigger.

## Step 8: Chaining the Queries

The first query gave me job IDs. Then those IDs unlocked the next query. And the next one. And the next.

The chain looked like this:

```
Call billing jobs query  (unauthenticated)
        ↓
Get jobId values
        ↓
Use jobId in customer details query  (unauthenticated)
        ↓
Get customer usage and cost data
        ↓
Use jobId in job status query  (unauthenticated)
        ↓
Get total tenant cost and account count
        ↓
Use jobId in job details query  (unauthenticated)
        ↓
Get internal processing details
```
This is what turned a moderate bug into a serious one.

## Step 9: Why Cross-Tenant Access Is a Big Deal

The platform was multi-tenant. Different companies all using the same system, each with their own data:

```
Tenant A
Tenant B
Tenant C
Tenant D
```
The whole point of multi-tenancy is isolation. A user from Tenant A should never see Tenant B’s data. Ever.

This isn’t a small information leak. It’s business-sensitive data, pricing, customer relationships and internal operations. Being readable across tenant boundaries by anyone on the internet.

## Step 10: A Java Stack Trace Falls Into My Lap

While I was testing, I sent some bad input, a fake job ID that didn’t exist. The query itself was valid GraphQL, but the backend choked on the input and returned a verbose error.

The error response included a backend stack trace with internal package and class names from the GraphQL resolver layer.

The backend was leaking a stack trace, the internal trail of where the error happened in the code.

Production APIs should never expose stack traces. They should return a clean, generic error like:

`{ "error": "Internal server error" }`
But when they do leak stack traces, it’s a gift to a hunter. You learn:

- The backend language
- Package names
- Class names
- Internal module structure
- Sometimes internal service names
- Sometimes private IPs

In my case, the stack trace confirmed that all the vulnerable resolvers were inside the same backend GraphQL module. The pattern I’d guessed at from the query names was now visible in the code structure.

## Final Takeaway

For me, this bug is a perfect example of how bug bounty isn’t always about clever payloads or zero-day tricks. A lot of the time, it’s much simpler than that:

*Find hidden surface. Map it properly. Test access control carefully. Follow the data. Explain the impact clearly.*


*If you enjoyed this write-up, please give it a clap and follow me. Feel free to reach out. I’m always happy to chat about breaking things (responsibly).*
