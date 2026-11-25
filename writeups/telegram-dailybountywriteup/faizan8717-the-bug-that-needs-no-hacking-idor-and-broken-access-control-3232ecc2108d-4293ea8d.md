# The Bug That Needs No Hacking

- **Source URL:** https://medium.com/@faizan8717/the-bug-that-needs-no-hacking-idor-and-broken-access-control-3232ecc2108d
- **Fetched from:** https://medium.com/@faizan8717/the-bug-that-needs-no-hacking-idor-and-broken-access-control-3232ecc2108d?source=rss-61f9e476555e------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:**  (id 14930)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** Faizan Baig / Thu, 01 Oct 2026 19:15:09 GMT

*One number. Someone else’s data.*

The first time you find an IDOR, it almost feels like you did something wrong.

You’re looking at a URL like this:

https://shop.example.com/invoice?id=1042

You change 1042 to 1043.

And there it is.

Someone else’s invoice. Their name. Their address. What they bought.

No exploit. No payload. No complicated trick.

You just changed a number in the address bar.

That’s the whole bug and it’s still one of those vulnerabilities that developers and security testers need to take seriously.

I recently cleared the **OSCP**, and honestly, OSCP focuses heavily on infrastructure and Active Directory. Web access-control issues like IDOR aren’t always the main focus.

But one habit OSCP definitely reinforces is:

***Enumerate everything. Don’t ignore the boring stuff.***

And that mindset is exactly what makes you notice bugs like this.

So let’s talk about IDOR properly.

**IDOR** stands for **Insecure Direct Object Reference**.

The idea is simple:

*An application uses an identifier supplied by the user to access an object, but fails to check whether that user is actually authorized to access it.*

For example:

GET /api/invoices/1042

The application sees 1042 and retrieves that invoice.

But what happens if you change it to:

GET /api/invoices/1043

and the server returns an invoice belonging to another user?

That’s a potential IDOR vulnerability.

The application asked:

*“Which invoice do you want?”*

But forgot to ask:

***“Are you allowed to see it?”***

That’s the important part.

IDOR is commonly associated with **Broken Access Control**, which is a much broader security problem.

Access control is basically the set of rules that determines:

When those rules aren’t properly enforced, you have a broken access-control issue.

IDOR is one example of this.

Other examples include:

This is one of the most important concepts to understand.

**Authentication** answers:

*“Who are you?”*

**Authorization** answers:

*“What are you allowed to do?”*

An application can correctly authenticate a user while completely failing to authorize their actions.

For example, imagine Alice logs into an application.

The server sees that Alice has a valid session and thinks:

User is authenticated ✓

But when Alice requests another user’s invoice, the server also needs to check:

Is Alice authorized to access this invoice?

If that second check is missing, you have a problem.

Being logged in doesn’t automatically mean you’re allowed to access everything.

Let’s say an application has three users:

UserIDAlice101Bob102Charlie103

Alice requests her own profile:

GET /api/users/101

The server returns Alice’s profile.

Everything looks normal.

Now Alice changes the ID:

GET /api/users/102

If the server returns Bob’s private information, the application has failed to enforce authorization.

The server shouldn’t only ask:

*“Does user 102 exist?”*

It should ask:

***“Is Alice allowed to access user 102?”***

That’s the core idea behind IDOR.

IDOR isn’t limited to numbers in URLs.

When testing an application, I pay attention to anything that looks like an object reference.

GET /api/orders/5521

If your account can access order 5521, what happens when you access another test account's order?

Modern applications rely heavily on APIs, so this is one of the first places worth checking.

You might see something like:

```
{
    "user_id": 88,
    "address": "New Address"
}
```
If the server trusts user\_id without checking authorization, changing it could potentially modify another user's information.

This can be more serious than a simple read because you’re dealing with a **write operation**.

Look for things such as:

/download/receipt\_2291.pdf

or APIs that accept:

file\_id

document\_id

invoice\_id

Download and export functionality is worth paying attention to because applications often expose direct references to files and documents.

Some of the interesting bugs aren’t in the main application.

Look at features such as:

Developers may protect the main application correctly while overlooking an older or less-used endpoint.

Sometimes the problem isn’t accessing another user’s data.

It can be accessing an administrative function as a normal user.

POST /admin/deleteUser

If the endpoint only relies on the frontend hiding the button, that’s not real security.

A user can send the HTTP request directly.

**Hiding a button is not access control.**

You don’t need fancy tooling to understand the basic IDOR testing process.

The easiest approach is to use two accounts that you are authorized to control.

Account A → Alice

Account B → Bob

Make sure both accounts have their own test data.

Log in as Alice and access one of her resources.

GET /api/invoices/5001

Capture the request using a proxy such as **Burp Suite**.

Log in as Bob and access one of Bob’s own resources first.

This gives you a baseline for what Bob is normally allowed to access.

Now, while authenticated as Bob, request Alice’s test object:

If Bob receives Alice’s invoice even though Bob has no permission to access it, you’ve potentially found an IDOR / Broken Access Control issue.

Look at:

The goal isn’t simply to prove that an ID can be changed.

The goal is to determine whether **the server correctly enforces authorization**.

***Only perform these tests on applications you own, intentionally vulnerable labs, or systems where you have explicit authorization.***

A typical workflow looks like this:

Capture request

↓

Identify object reference

↓

Switch to another test account

↓

Replay request

↓

Compare response

For example, you might capture:

GET /api/orders/1001 HTTP/1.1

Host: lab.example

Cookie: session=...

Then, in your authorized lab, test another object:

GET /api/orders/1002 HTTP/1.1

Host: lab.example

Cookie: session=...

Then compare the responses.

You’re looking for a difference between:

Expected:

Access denied

and:

Unexpected:

Another user's resource is returned

One mistake beginners often make is checking only whether they can **read** another user’s data.

IDOR can also affect actions that modify or delete data.

GET /api/profile/102

**Potential impact:** Unauthorized information disclosure.

PUT /api/profile/102

**Potential impact:** Unauthorized modification.

DELETE /api/document/102

**Potential impact:** Unauthorized deletion.

That’s why, when your authorized scope allows it, it’s worth checking different operations rather than stopping after finding a read-only issue.

Random IDs are useful.

They’re just not a replacement for authorization.

You might see an application using sequential IDs:

1001

1002

1003

1004

and think:

*“The IDs are predictable, so the application has IDOR.”*

Not necessarily.

Predictable identifiers can make enumeration easier, but they aren’t the root cause.

Even if the application uses UUIDs:

550e8400-e29b-41d4-a716-446655440000

the server still needs to check authorization.

If that UUID is leaked through an email, shared link, log, or another API response, anyone who obtains it shouldn’t automatically gain access to the resource.

**Unpredictable IDs are an additional layer. Authorization is the real security control.**

Sometimes an IDOR doesn’t look particularly dangerous at first.

Imagine an endpoint that exposes:

Name

Email

User ID

That might initially appear to be a limited information disclosure.

But vulnerabilities don’t always exist in isolation.

For example, if an application has another weak endpoint that uses the exposed email address in a sensitive workflow, the two issues could potentially be chained.

The important lesson is:

***Don’t stop at “I can access this.” Ask what that access enables.***

When writing a vulnerability report, explain the actual impact instead of simply saying:

*“IDOR exists.”*

Show what an unauthorized user can actually **read, modify, or delete**.

The fix is usually straightforward.

The difficult part is making sure it’s applied consistently.

Don’t only check:

Is the user logged in?

Also check:

Does this user have permission to access this specific object?

\# Vulnerable

invoice = db.get\_invoice(request.args\["id"\])

return invoice

A safer approach is to scope the lookup to the authenticated user:

\# Better

invoice = db.get\_invoice(

request.args\["id"\],

owner=current\_user.id

)

if not invoice:

return "Not found", 404

return invoice

The exact implementation depends on the application’s authorization model, but the principle remains the same.

Anything sent by the browser can be modified.

For example, don’t blindly trust:

```
{
    "user_id": 88
}
```
to determine who the current user is.

Where possible, derive the authenticated identity from the server-side session or validated authentication token.

If a new endpoint is created, access shouldn’t automatically be granted to everyone.

Define who can access it and what they can do.

If every endpoint implements its own permission logic, someone will eventually forget a check.

Use shared middleware, policies, or authorization functions where appropriate.

Create automated tests where:

User A → tries to access User B's resource

The expected result should be denial.

These tests can catch authorization problems before they reach production.

One reason IDOR can be difficult for automated scanners to identify is that authorization depends heavily on **application context**.

A scanner can send strange characters to an input and potentially identify things like SQL injection.

But how does it know that:

Invoice #1043

belongs to another user?

That’s a business-logic question.

The scanner may not know:

That’s where manual testing and understanding the application’s behavior become important.

If you build applications:

***A logged-in user is not automatically an authorized user.***

Check authorization on the server, for every protected resource.

If you test applications:

***Get curious about every ID you see.***

Change it. Replay the request. Compare the response. Try different authorized test accounts.

The important question isn’t:

*“Can I change this ID?”*

It’s:

***“What happens when I change it, and does the server correctly enforce authorization?”***

That’s the mindset that helps uncover Broken Access Control vulnerabilities.

And if you’re new to web security, IDOR is a great vulnerability to learn.

You don’t need an exploit toolkit.

You need two test accounts, a proxy, and the habit of asking:

***“Wait… what happens if I change this?”***

Sometimes the answer is more interesting than it should be.

*I’m a cybersecurity student and OSCP holder writing about what I learn along the way. If you enjoyed this breakdown, follow along for more practical web security content and let me know which vulnerability I should cover next.*
