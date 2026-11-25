# $$$ I Tried a Simple Registration Endpoint… and Accidentally Found a Critical Admin Account…

- **Source URL:** https://alfazhossain0.medium.com/i-tried-a-simple-registration-endpoint-and-accidentally-found-a-critical-admin-account-9af2b90cf4a3
- **Fetched from:** https://alfazhossain0.medium.com/i-tried-a-simple-registration-endpoint-and-accidentally-found-a-critical-admin-account-9af2b90cf4a3?source=rss-514e629fc3e6------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14886 (id 14886)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** Alfaz Hossain / Sat, 29 Aug 2026 07:41:53 GMT

**No login. No authorization. One API request. And suddenly… I had an administrator account.**

*Sometimes the most interesting vulnerabilities don’t start with a fancy exploit.*

*Sometimes you just change one value in a JSON request.*

While testing a development environment, I came across an API endpoint responsible for user registration.

At first glance, it looked completely normal.

A registration endpoint.

Nothing exciting.

I sent a normal request, checked the response, and started looking at how the application handled the newly created account.

Then I noticed something interesting.

The API was accepting a role value from the client.

And that immediately made me stop.

When hunting APIs, one of the things I normally pay attention to is **what the server actually trusts from the client**.

A registration request might look something like:

POST /api/auth/register

Content-Type: application/json

```
{
  "username": "testuser",
  "email": "test@example.com",
  "password": "********"
}
```
Pretty standard.

The server creates the account, and the user gets a normal account.

Nothing unusual.

But while looking at the request body, I noticed a parameter related to the user’s role.

Something like:

```
{
  "username": "testuser",
  "email": "test@example.com",
  "password": "********",
  "role": "USER"
}
```
That raised the first question:

***Why is the client allowed to tell the server what role the new account should have?***

For a normal registration flow, the server should decide that.

The client should not be able to say:

*“Hey server, please make me an administrator.”*

😅

First Attempt — Change the Role

I decided to test the obvious case.

Instead of the normal low-privileged role, I changed the value to a privileged role.

For example:

```
{
  "username": "testadmin",
  "email": "testadmin@example.com",
  "password": "********",
  "role": "ADMIN"
}
```
Then I sent the request.

I wasn’t expecting much.

Maybe the API would return:

```
{
  "error": "Unauthorized"
}
```
Or:

```
{
  "error": "Invalid role"
}
```
Or simply ignore the parameter.

But…

The server accepted the request.

```
{
  "message": "User created successfully",
  "userId": "REDACTED"
}
```
Okay.

That was interesting.

“Wait… Did It Actually Create an Admin?”

At this point, I wasn’t ready to call it a vulnerability.

An application accepting an ADMIN value doesn't necessarily mean that the account actually has administrator privileges.

So I needed to verify what happened **after registration**.

I authenticated with the newly created account and inspected the authentication response/token claims.

The resulting authorization data indicated that the account had privileged permissions.

Something conceptually similar to:

```
{
  "role": "ADMIN",
  "roles": [
    "SUPER_ADMIN"
  ]
}
```
And this was the moment where the finding became much more serious.

The application wasn’t simply accepting an unusual registration parameter.

It was actually **granting privileged authorization based on attacker-controlled input**.

Now came the important part.

Could this account actually access administrative functionality?

I opened the application’s administrative area using the newly created account.

And…

It worked.

No existing administrator account.

No invitation.

No approval.

No special authorization flow.

Just:

Registration

↓

role = ADMIN

↓

Account Created

↓

Privileged Authentication

↓

Administrative Dashboard

At this point, I stopped testing randomly and started documenting everything carefully.

Getting an administrator account is already a critical issue.

But the next question was:

***What can this administrator actually do?***

I started going through the available administrative functionality.

The account was able to access multiple sensitive areas of the application, including functionality related to:

The exact accessible functionality depends on the affected environment, but the important point was clear:

**The attacker-controlled registration flow could lead directly to privileged application access.**

I Didn’t Stop at the Dashboard

This is an important part of vulnerability research.

Once you discover a potentially critical vulnerability, don’t immediately start clicking everything just because you can.

The goal is to **verify impact with the minimum necessary access and data**.

During controlled verification, I confirmed that the privileged account could access sensitive business functionality and records.

This included areas containing information such as:

I also confirmed that certain administrative exports could be generated.

Obviously, sensitive records and personal/business information are **redacted from this article**.

While testing some administrative functionality, I encountered verbose error responses.

The errors exposed information about the application’s internal database implementation.

In particular, debug output revealed details related to the application’s **Prisma database schema**.

This was not the primary vulnerability.

But it was a useful reminder:

*A critical authorization bug can turn seemingly harmless debug information into a much more valuable source of intelligence.*

An attacker who already has administrative access has a very different threat model from an unauthenticated user.

The core issue is simple:

The application trusted a security-sensitive value supplied by the client.

Conceptually, the vulnerable logic looked like:

Client

|

| role = ADMIN

v

Registration API

|

| "Sure, sounds good."

v

Create privileged account

The correct architecture should be:

Client

|

| registration data

v

Registration API

|

| Server decides role

v

Create LOW-PRIVILEGE account

The client should never be the authority for authorization.

This is one of those API security lessons that sounds obvious after you’ve seen it.

If a request contains:

```
{
  "role": "ADMIN"
}
```
the server must **not** assume that the client is allowed to create an administrator.

The attacker controls the request.

They can modify:

So simply hiding a field from the frontend is not security.

If the backend accepts it, it can potentially be manipulated.

This isn’t just a normal broken access control issue.

The attack begins with an **unauthenticated attacker**.

There is no requirement for an existing account.

There is no requirement for an existing administrator.

The vulnerable flow effectively allows:

Unauthenticated Attacker

↓

Public Registration

↓

Attacker-Controlled Role

↓

ADMIN Account

↓

Privileged JWT

↓

Administrative Dashboard

↓

Sensitive Business Data

This can impact all three major security properties:

An attacker may access sensitive employee, client, financial, and operational information.

An attacker with sufficient privileges may modify users, configuration, business records, or other application data.

Whenever I find a registration or account-management endpoint, I like to ask a few questions:

Look for security-sensitive parameters:

role

roles

permissions

isAdmin

isStaff

accountType

organizationId

tenantId

status

verified

Don’t assume that frontend validation is enough.

Intercept the request and test what the backend accepts.

Don’t stop at:

200 OK

Check what permissions the newly created account actually receives.

A successful registration isn’t necessarily a vulnerability.

The important part is the resulting authorization state.

Think in terms of:

Input

↓

Account creation

↓

Authentication

↓

Authorization

↓

Sensitive functionality

That’s often where the real impact becomes visible.

The fix is conceptually straightforward.

The server should assign a safe default role:

New Registration

↓

USER

Not:

New Registration

↓

Whatever role the client requested

Administrator creation should require:

Even if the frontend doesn’t expose:

"role": "ADMIN"

the backend should still reject or ignore it if supplied manually.

After fixing the vulnerability, the organization should review accounts created through the vulnerable endpoint.

Any unexpectedly privileged accounts should be investigated and removed or downgraded as appropriate.

Finding one instance of client-controlled privilege assignment should trigger a broader review.

Look for the same pattern in:

/register

/users

/invite

/team

/company

/roles

/permissions

/admin

One broken authorization check can sometimes indicate a broader design problem.

This finding was a good reminder that you don’t always need a sophisticated exploit to find a critical vulnerability.

Sometimes you just need to ask:

***“Why does the server trust this value?”***

That’s the question that changed this test from a normal registration check into a **critical account-takeover finding**.

The entire attack chain started with an unauthenticated registration request.

A small parameter led to a privileged account.

The privileged account led to administrative functionality.

And administrative functionality exposed access to highly sensitive business operations.

So the next time you’re testing an API and see something like:

```
{
  "role": "USER"
}
```
don’t immediately move on.

Ask yourself:

**“What happens if I change it?”**

You might be surprised.

**Linkedin**: [https://www.linkedin.com/in/alfazhossain/](https://www.linkedin.com/in/alfazhossain/)

**Bye bye — Allah Hafiz.**
