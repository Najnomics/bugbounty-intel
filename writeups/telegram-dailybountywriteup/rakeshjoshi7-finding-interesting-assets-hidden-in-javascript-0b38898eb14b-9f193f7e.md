# Finding Interesting Assets Hidden in JavaScript

- **Source URL:** https://medium.com/@Rakeshjoshi7/finding-interesting-assets-hidden-in-javascript-0b38898eb14b
- **Fetched from:** https://medium.com/@Rakeshjoshi7/finding-interesting-assets-hidden-in-javascript-0b38898eb14b?source=rss-a32f2a443db2------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14932 (id 14932)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** Rakesh Joshi / Sun, 04 Oct 2026 06:34:29 GMT

For bug bounty hunters, this makes JavaScript reconnaissance one of the most valuable ways to expand an application’s attack surface.

***Core idea:*** *Don’t just look at what the application shows you. Analyze what the browser is being instructed to do.*

JavaScript files can contain references to assets that aren’t immediately visible through normal browsing.

You may discover:

For example, a JavaScript bundle might contain something conceptually similar to:

const API\_BASE = "https://api.example.com";

```
const endpoints = {
    profile: "/api/v2/profile",
    billing: "/api/v2/billing",
    export: "/api/v2/export"
```
The /api/v2/export endpoint may never appear as a clickable link in the application.

That’s exactly why JavaScript analysis is useful.

Before performing reconnaissance, read the program’s scope carefully.

Determine:

This is particularly important when JavaScript reveals third-party infrastructure.

**Discovery does not automatically mean authorization to test.**

If a script references:

https://external-service.example

don’t automatically treat that host as part of the bug bounty target.

Open the target normally and inspect the resources loaded by the browser.

In Chromium-based browsers:

**DevTools → Network → JS**

You can also inspect:

**DevTools → Sources**

Look for files such as:

main.js

app.js

runtime.js

vendor.js

chunk.js

bundle.js

Modern frameworks often split JavaScript into many chunks:

main.8a72.js

chunk-1.91ab.js

chunk-2.21fd.js

runtime.31ac.js

Don’t assume that main.js contains everything.

The interesting functionality may live inside a lazily loaded chunk.

Your first objective is simple:

***Build a complete inventory of JavaScript resources belonging to the in-scope application.***

Think of this as an asset inventory.

For every JavaScript file, record:

FileSourceInteresting?main.jsApplicationYesvendor.jsThird-party librariesLowadmin.chunk.jsApplicationHighbilling.chunk.jsApplicationHighanalytics.jsThird partyLowsettings.chunk.jsApplicationHigh

Prioritize application-specific JavaScript over generic vendor libraries.

Once you’ve identified relevant JavaScript files, inspect them locally.

For example:

curl -O https://target.example/app/main.js

Then search through the file:

grep -Eoi 'https?://\[^"'\'' \]+' main.js

Search for API-related keywords:

grep -Ei 'api|graphql|swagger|admin|internal|debug|upload|export' main.js

Search for interesting paths:

grep -Eo '"/\[^"\]+"' main.js

The exact extraction technique depends heavily on how the JavaScript is bundled, so don’t rely on a single regex.

One of the highest-value searches is for absolute URLs.

Look for patterns such as:

https://api.example.com

https://admin.example.com

https://staging.example.com

https://storage.example.com

```
const services = {
    users: "https://api.example.com/users",
    reports: "https://reports.example.com",
    websocket: "wss://socket.example.com"
};
```
This immediately expands your understanding of the application’s architecture.

Again, **only test assets that are actually authorized by the program.**

JavaScript frequently reveals API routes.

Look for strings containing:

/api/

/v1/

/v2/

/graphql

/rest/

/users

/accounts

/admin

/internal

`fetch("/api/v2/account/settings")`
or:

`axios.get("/api/v1/users")``client.post("/graphql", query)`
These references can help you map the application’s API surface.

Don’t just search for URLs.

Search for how those URLs are used.

Common patterns include:

GET

POST

PUT

PATCH

DELETE

You may encounter code such as:

```
fetch("/api/v2/profile", {
    method: "PATCH"
});
```
This tells you considerably more than simply finding /api/v2/profile.

You now know that the client expects to modify profile data through that endpoint.

That can become useful during **authorized access-control and business-logic testing**.

JavaScript can reveal frontend routes that aren’t visible in the normal navigation.

Search for patterns such as:

/admin

/dashboard

/settings

/billing

/reports

/debug

/internal

/maintenance

```
{
    path: "/admin/reports",
    component: AdminReports
}
```
This doesn’t automatically mean the page is accessible.

Instead, you’ve discovered a **candidate attack surface** that can be investigated within scope.

GraphQL applications can expose particularly useful information through JavaScript.

Search for:

graphql

GraphQL

query

mutation

subscription

You might discover:

```
fetch("/graphql", {
    method: "POST",
    body: JSON.stringify({
        query: USER_QUERY
    })
});
```
You can then investigate the application’s authorized GraphQL functionality and understand:

Modern applications increasingly use WebSockets.

ws://

wss://

WebSocket

socket

Example:

const socket = new WebSocket(

"wss://socket.example.com/realtime"

);

This can reveal another part of the application’s architecture that isn’t obvious from ordinary HTTP navigation.

This is one of my favorite areas of JavaScript reconnaissance.

Look for strings such as:

dev

development

test

testing

staging

stage

qa

uat

prod

production

internal

You may encounter:

```
const environments = {
    production: "https://api.example.com",
    staging: "https://staging-api.example.com"
};
```
The important point isn’t that every staging URL is vulnerable.

The important point is:

***The JavaScript has revealed another potential asset that deserves scope verification and investigation.***

Configuration data can reveal a surprising amount about an application’s architecture.

Look for objects containing:

baseURL

apiURL

endpoint

host

domain

service

region

environment

bucket

```
const config = {
    apiBaseUrl: "https://api.example.com",
    uploadUrl: "https://uploads.example.com",
    realtimeUrl: "wss://socket.example.com"
```
Create an inventory from these references rather than immediately interacting with everything you find.

One particularly valuable JavaScript artifact is the source map.

You may see:

//# sourceMappingURL=main.js.map

If the corresponding .map file is publicly accessible, it may provide a much easier-to-read representation of the application's original source structure.

Depending on how the application was built, source maps can expose:

A source map isn’t automatically a vulnerability.

Its security significance depends on what information it exposes and the program’s policy.

Keyword searching can dramatically speed up manual analysis.

Useful categories include:

auth

login

logout

token

session

oauth

jwt

refresh

password

admin

administrator

moderator

management

internal

staff

export

download

upload

delete

update

backup

restore

debug

development

test

verbose

trace

mock

stripe

github

slack

aws

s3

firebase

oauth

The goal isn’t to blindly search for secrets.

The goal is to understand **what functionality exists and where trust boundaries may exist**.

Endpoints become much more interesting when you understand their parameters.

/api/user?id=

/api/account?accountId=

/api/document?documentId=

/api/export?format=

Parameters can reveal object identifiers and functionality that deserves deeper authorization testing.

GET /api/document?documentId=123

might suggest an opportunity to investigate whether authorization is properly enforced when accessing objects belonging to another account.

**Do this only within the program’s authorized testing boundaries and with accounts/data you are permitted to use.**

Don’t leave your discoveries scattered across terminal windows.

Create a structured inventory.

EndpointMethodFunctionAuth?Priority/api/v1/profileGETProfileYesMedium/api/v2/exportPOSTData exportYesHigh/api/admin/reportsGETReportsYesHigh/graphqlPOSTAPIYesHigh/api/uploadPOSTUploadYesHigh

This turns JavaScript analysis into an actual reconnaissance process.

This is where the methodology becomes much more powerful.

Suppose JavaScript reveals:

/api/v2/export

but you never see the browser request it.

Ask:

**Why does this endpoint exist?**

Possible explanations:

Use browser DevTools or an authorized intercepting proxy to understand legitimate application behavior.

Feature flags can expose functionality that isn’t currently displayed.

featureFlags

features

experiments

beta

enabled

disabled

rollout

```
if (features.advancedExport) {
    enableExport();
}
```
This tells you that an **advanced export feature exists**, even if it isn’t visible in the current interface.

That’s valuable reconnaissance.

The real power isn’t any individual discovery.

It’s correlation.

Imagine you find:

staging-api.example.com

/api/v2/export

/admin/reports

/graphql

wss://socket.example.com

Individually, these are just observations.

Together, they provide a much clearer picture of the application’s architecture.

Think like this:

JavaScript

↓

Endpoint

↓

Functionality

↓

Authentication

↓

Authorization

↓

Business Logic

↓

Potential Security Impact

Don’t investigate every discovered string equally.

A useful prioritization model is:

This keeps your testing focused.

A simple workflow can look like this:

TARGET

↓

Collect JS

↓

Identify first-party bundles

↓

Search URLs

↓

Extract API endpoints

↓

Identify routes

↓

Find parameters

↓

Find environments

↓

Inspect source maps

↓

Identify authentication boundaries

↓

Build endpoint inventory

↓

Compare against live traffic

↓

Prioritize interesting functionality

↓

Perform authorized security testing

↓

Validate impact

↓

Write report

Modern applications frequently use code splitting.

**Better:** collect all first-party chunks.

A discovered endpoint is **attack surface**, not automatically a finding.

Source maps can dramatically improve visibility into application structure.

Interesting functionality may use:

graphql

socket

rpc

upload

download

export

Knowing that /export exists isn't enough.

Understanding whether it’s GET, POST, PUT, or DELETE gives you more context.

A JavaScript file may reference dozens of external services.

**Discovery ≠ authorization.**

The biggest mindset shift is this:

**Don’t ask:**

*“What vulnerabilities are inside this JavaScript file?”*

Instead ask:

***“What functionality and trust relationships does this JavaScript reveal?”***

From there, investigate:

What assets exist?

↓

What endpoints exist?

↓

What functionality do they expose?

↓

Who is allowed to use it?

↓

What objects can they access?

↓

What assumptions does the application make?

↓

Can those assumptions be violated?

That is where JavaScript reconnaissance transitions into genuine vulnerability research.

JavaScript is more than frontend code.

For a bug bounty hunter, it can act as an **architectural map of the application**.

A disciplined JavaScript reconnaissance process can reveal:

The objective isn’t to collect the largest number of endpoints.

**The objective is to discover the most interesting attack surface and understand how the application trusts its users.**

***Good recon finds assets. Great recon finds relationships between assets. Excellent bug hunting turns those relationships into security hypotheses.***
