# Race Condition That Created an Undeletable Group Member

- **Source URL:** https://medium.com/@y_shivkumar/race-condition-that-created-an-undeletable-group-member-2e9483541fbf
- **Fetched from:** https://medium.com/@y_shivkumar/race-condition-that-created-an-undeletable-group-member-2e9483541fbf?source=rss-13de31b67c0b------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:**  (id 14882)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** ShivKumar / Wed, 26 Aug 2026 19:23:36 GMT

These Vulnerability describes a **Time-of-Check to Time-of-Use (TOCTOU) race condition** in the original disclosure’s group/member functionality.

The core idea is simple:

*Two requests that modify the same group-member state can arrive at
nearly the same time. The application checks the state before the
previous operation has fully completed, leaving the member in an
inconsistent state.*

**Type:** Race Condition / TOCTOU

**Target:** the original disclosure group/member functionality

**Impact:** A group member could become **undeletable** through normal

application functionality.

Suppose an admin wants to remove **Alice** from a group.

Normally:

Alice is a member

↓

Admin clicks Remove

↓

Server removes Alice

↓

Alice is no longer a member

Now imagine two related requests are processed at nearly the same time.

The server can temporarily see an old state in one request while another request is already changing it.

That timing gap can leave the application in an unexpected state — for example, the member remains present but cannot be removed through the normal workflow.

The root cause is **unsafe handling of shared state during concurrent requests**.

A simplified vulnerable design might look like:

Request A → check member state

Request B → check member state

Request A → change member state

Request B → change member state

Both requests made their decisions using state that could become outdated.

The important point is:

***Checking something and changing it must be synchronized when the operation depends on the check.***

This is why simply validating each request individually may not be enough.

A simplified attack flow is:

Identify group-member operation

↓

Capture the normal HTTP request

↓

Find an operation that changes member state

↓

Send the same/state-related requests concurrently

↓

Application processes overlapping operations

↓

Database/application state becomes inconsistent

↓

Member can no longer be removed normally

The attacker does **not** necessarily need to bypass authentication.

The bug comes from making the server process valid requests at the wrong

time.

When testing a web application, look for operations that modify the same

object:

Then ask:

*“What happens if two valid requests for the same object arrive at
almost exactly the same time?”*

Look for endpoints containing concepts such as:

/member

/group

/invite

/remove

/delete

/join

/leave

/accept

/revoke

First understand the intended behavior.

For example:

Add member

↓

Member appears

↓

Remove member

↓

Member disappears

Do not start with concurrency before understanding the normal workflow.

Use a proxy such as Burp Suite.

Record:

HTTP method

Endpoint

Authentication

Session information

Object IDs

Request body

CSRF protection

The goal is to understand which request changes the state.

Duplicate the relevant request.

Then send multiple copies **at the same time**, rather than one after another.

Conceptually:

Request 1 ──┐

Request 2 ──┤

Request 3 ──┼──> Server

Request 4 ──┤

Request 5 ──┘

Tools that support parallel HTTP requests can help make the timing more reliable.

After the requests finish, inspect the actual application state.

Do not stop at:

HTTP 200 OK

Instead ask:

What changed?

Was the object created?

Was it deleted?

Did the permission change?

Can the action still be performed?

Does the UI agree with the backend?

The final state is the important evidence.

A race-condition payload is usually not about a special malicious

string.

The “payload” is often the **same valid request sent concurrently**.

Request 1 ───────┐

Request 2 ───────┼──> Server

Request 3 ───────┤

Request 4 ───────┘

↓

Shared application state

↓

Unexpected final state

This is why race conditions are different from injection bugs.

You are exploiting **timing and state**, not necessarily malformed

input.

The confirmed impact of this bugs was limited compared with account

takeover or remote code execution.

The practical effect was an **undeletable group member**, creating an

integrity/business-logic problem in the group-management functionality.

Possible consequences of similar race conditions can be much more

serious when the affected operation involves:

So the same bug class can range from **Low** to **Critical**, depending

on what state is being raced.

The key architectural mistake is treating a multi-step state change as

if requests will always arrive one after another.

A safe design conceptually needs:

Check state

+

Change state

+

Commit state

to behave as one atomic operation.

An unsafe implementation can behave like:

Request A: check

Request B: check

Request A: update

Request B: update

Both requests can make decisions using state that is no longer valid.

Do not only ask:

*“Can I send a malicious request?”*

Also ask:

***“Can I send two legitimate requests before the application finishes processing the first?”***

Prioritize:

A strong race-condition candidate usually has a rule such as:

Only once

Maximum 1

Maximum 5

Cannot be repeated

Already exists

Already removed

Already claimed

These rules deserve concurrency testing.

A 200 OK is not proof of success.

The real question is:

*“What state did the server end up in after all concurrent operations
finished?”*

Developers should protect sensitive state transitions with mechanisms

such as:

For example, instead of:

SELECT member

→ check member exists

→ DELETE member

the operation should be designed so the relevant state cannot change

unexpectedly between the check and the update.

**Race conditions are bugs in time, state, and synchronization.**

This case is a good beginner example because the attack

does not require a complicated payload.

The important skill is recognizing:

***“This operation changes shared state. What happens if two valid
requests execute at the same time?”***
