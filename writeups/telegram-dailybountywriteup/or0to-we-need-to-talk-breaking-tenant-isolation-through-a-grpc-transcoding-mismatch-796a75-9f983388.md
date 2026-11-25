# We Need to Talk — Breaking Tenant Isolation Through a gRPC Transcoding Mismatch

- **Source URL:** https://medium.com/@or0to/we-need-to-talk-breaking-tenant-isolation-through-a-grpc-transcoding-mismatch-796a75231fd2
- **Fetched from:** https://medium.com/@or0to/we-need-to-talk-breaking-tenant-isolation-through-a-grpc-transcoding-mismatch-796a75231fd2?source=rss-d90b0356d800------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14910 (id 14910)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** Ali Essam / Sun, 13 Sep 2026 22:59:03 GMT

***A toxic relationship is just a protocol mismatch with extra feelings.***

That was the first line of the challenge description.

At first, it sounded like typical CTF flavor text.

By the end of the challenge, it turned out to be the most important clue.

The application was called **TenantExchange**, and its entire security model revolved around keeping tenants isolated from each other. The objective was to retrieve a sealed incident packet belonging to another tenant.

The final exploit chain combined:

The target was:

http://16.192.186.119:4000/

The application was built with Phoenix/Elixir and initially presented a normal registration and login flow.

I created a fresh analyst account and authenticated successfully.

Instead of giving direct access to the application, the server redirected me to:

*Email verification required*

The next step was an OTP verification flow.

Naturally, the first question was whether the OTP could be leaked through the Phoenix session or some development mail functionality.

I inspected the session cookie and looked for possible email-preview endpoints.

Nothing useful.

The OTP itself wasn’t exposed.

At this point, it would have been easy to conclude that the OTP needed to be brute-forced.

That would have been the wrong direction.

While inspecting the OTP page, I noticed that it contained a link to:

/notifications

I accessed it **without completing OTP verification**.

It worked.

Not just partially.

The full dashboard was accessible.

The application had effectively implemented:

Password authentication

↓

OTP verification required

↓

Full application access

but several sensitive routes behaved more like:

Password authentication

↓

Full application access

The OTP state wasn’t consistently enforced.

This wasn’t really an authentication bypass. The session was authenticated, but the **step-up authorization boundary was broken**.

The notifications dashboard immediately became much more interesting.

It exposed several useful endpoints:

/api/v1/tenants/acme-corp/documents/\<uuid>

/exchange/lookup?q=IR-4472

/docs/

And the dashboard contained an important clue:

*Blocked external: 1*

There was apparently one external object belonging to another tenant.

That was the object I needed.

The /docs/ endpoint looked innocent.

It wasn’t.

Instead of a normal documentation interface, it exposed a directory listing.

Inside were files including:

mix.lock

schema.sql

tenantexchange.protoset

That was an enormous amount of information for an unauthenticated documentation directory.

The database schema revealed the application’s data model.

The dependency information exposed the technology stack.

And the .protoset file was particularly interesting.

It contained the protobuf descriptors for the application’s gRPC interface.

After decoding the descriptor, the important service appeared:

Documents.GetDocument

with an HTTP mapping equivalent to:

`GET /api/v1/tenants/{tenant_id}/documents/{doc_id}`
Now the challenge description started making more sense.

*“messages go through the right channels”*

*“protocol mismatch”*

This wasn’t just a normal REST API.

There was a gRPC service sitting behind an HTTP transcoding layer.

That distinction would eventually break the tenant boundary.

But first, I needed the ID of the Initech document.

My account belonged to:

acme-corp

The target document belonged to another tenant:

initech-inc

Trying to access an Initech document through the obvious path:

GET /api/v1/tenants/initech-inc/documents/\<uuid>

returned:

403 Forbidden

The behavior was actually encouraging from a defensive perspective.

The gateway was clearly performing a tenant check.

Conceptually:

session tenant = acme-corp

path tenant = initech-inc

↓

DENIED

I tried the obvious path manipulation ideas.

Encoding tricks didn’t help.

Changing capitalization didn’t help.

Alternate routes didn’t help.

The important observation was that the 403 happened **before the document UUID was even parsed**.

The policy layer was clearly checking the tenant from the URL.

So the obvious route was protected.

The question became:

*Is the tenant that gets authorized the same tenant that eventually reaches the backend?*

That is a very different question.

The /exchange/lookup endpoint initially appeared to be nothing more than a delivery-status lookup:

/exchange/lookup?q=IR-4472

The challenge description mentioned a sealed incident packet, and the dashboard explicitly referenced:

IR-4472

So this endpoint was clearly relevant.

While experimenting with the query parameter, I noticed unusual behavior.

The application wasn’t performing a simple equality check.

It behaved like a SQL ILIKE query:

ILIKE '%' || q || '%'

That meant SQL LIKE wildcards were being interpreted.

For example:

%

could match multiple characters, while:

\_

could match a single character.

More importantly, the parameter was injectable.

A boolean SQL condition could influence whether the lookup returned a matching result.

The endpoint had become a **blind SQL injection oracle**.

The important part wasn’t simply proving SQL injection.

It was understanding the exact SQL context.

The parameter wasn’t inserted into a traditional:

LIKE '%INPUT%'

string.

The application was effectively constructing:

That meant the injection syntax needed to break out of the expression correctly.

Once that was understood, boolean conditions could be used to ask the database questions.

Does condition X evaluate to TRUE?

If yes:

response A

If no:

response B

That gave me a character-by-character extraction primitive.

From there, database metadata could be extracted.

The schema revealed five tables, including:

tenants

users

sessions

documents

and another application-specific table.

More importantly, I could query the tenant table.

The tenant slugs were:

acme-corp

initech-inc

The next target was the documents table.

I queried for documents whose tenant was **not** Acme.

That produced an Initech document UUID:

55c72cdd-ea23-4251-bdae-21df4cb81529

The first document was:

Customer Success Welcome

That was enough to prove that the database enumeration was working.

But it wasn’t the target.

I continued enumerating the Initech documents and eventually identified:

f424286d-bbb4-42f2-b038-3dc8a64ac927

with the title:

Incident IR-4472 Escalation

This was the sealed packet.

Now I had the document ID.

The remaining problem was much more interesting:

*How do we make an Acme-authorized request return an Initech document?*

This was where the challenge description finally clicked.

The API exposed a route like:

The gateway performed authorization based on the tenant appearing in the **path**.

For my session:

/api/v1/tenants/acme-corp/...

passed the policy check.

But the request was ultimately translated into a protobuf message for:

And the transcoding layer also allowed protobuf fields to be supplied through query parameters.

That created two different sources of truth.

The policy looked at:

/path/tenant\_id

The gRPC request could receive:

?tenant\_id=...

?doc\_id=...

Those values became fields in the backend request message.

So the same HTTP request could effectively say:

Authorization:

"I'm requesting an Acme object."

Backend:

"Actually, use this Initech tenant and this Initech document."

That is the protocol mismatch.

The two layers were validating different representations of the same request.

The final request used an Acme tenant in the path:

GET /api/v1/tenants/acme-corp/documents/x

That satisfied the gateway’s tenant check.

But the query string supplied the actual backend values:

?tenant\_id=initech-inc

&doc\_id=f424286d-bbb4-42f2-b038-3dc8a64ac927

So the complete request was:

GET /api/v1/tenants/acme-corp/documents/x?tenant\_id=initech-inc&doc\_id=f424286d-bbb4-42f2-b038-3dc8a64ac927

The important distinction was:

HTTP request

│

▼

┌─────────────────────────┐

│ Policy Layer │

│ │

│ path tenant = acme-corp │

│ session tenant = acme │

│ │

│ ALLOW │

└────────────┬────────────┘

│

▼

┌─────────────────────────┐

│ gRPC Transcoding │

│ │

│ tenant\_id = initech-inc │

│ doc\_id = restricted ID │

└────────────┬────────────┘

│

▼

┌─────────────────────────┐

│ Database │

│ │

│ Initech document │

│ │

│ RETURNED │

└─────────────────────────┘

The authorization layer said:

*“This is an Acme request.”*

The backend received:

*“Fetch this Initech document.”*

And because the backend trusted the transcoded protobuf message, the tenant boundary disappeared.

The request returned:

The restricted document contained the flag.

The final flag was:

`CATF{pr3_07p_535510n_bl1nd_5ql1_grpc_73n4n7_0v3rr1d3}`
Interestingly, the flag itself summarizes the exploitation chain:

pr3\_07p\_535510n

↓

blind SQL injection

↓

grpc

↓

tenant override

The challenge wasn’t built around one isolated vulnerability.

It was a chain.

The application required OTP verification after login, but sensitive routes such as:

/notifications

/exchange/lookup

/docs/

didn’t enforce the OTP-verified state.

That provided access to the application’s internal attack surface.

The /docs/ directory exposed:

schema.sql

mix.lock

tenantexchange.protoset

This revealed the database structure and gRPC service contract.

The lookup endpoint:

/exchange/lookup?q=

was vulnerable to boolean-based SQL injection through its ILIKE expression.

This allowed extraction of:

tenant names

document UUIDs

database metadata

The HTTP gateway authorized the tenant using the URL path, while the transcoded gRPC request accepted tenant and document values from query parameters.

This created inconsistent security decisions between the gateway and backend.

Finally:

Acme path

+

Initech query parameters

=

Initech document

The restricted incident packet was returned to an Acme user.

The most interesting part of this challenge wasn’t the SQL injection.

It wasn’t the exposed directory listing either.

It was the fact that the final authorization bypass was created by **two individually reasonable components disagreeing about where the request’s identity came from**.

The gateway trusted:

path tenant

while the backend trusted:

protobuf tenant

Both components were behaving consistently according to their own assumptions.

The vulnerability existed **between them**.

This is an important class of bug in modern architectures.

When REST, gRPC, API gateways, protocol translators, service meshes, and authorization middleware are combined, developers need to be extremely careful about parameter precedence and request normalization.

A security decision made against one representation of a request is useless if a later layer can reinterpret that request.

There are several clear fixes for this application.

Step-up authentication must be enforced at the authorization boundary, not just by redirecting users to an OTP page.

Every sensitive route should verify something equivalent to:

session.otp\_verified == true

before processing the request.

The following should never have been publicly browsable:

schema.sql

mix.lock

\*.protoset

Static documentation directories should contain only intended public documentation.

Directory indexing should also be disabled where it isn’t required.

The lookup endpoint should never construct SQL using attacker-controlled input.

The correct approach is to use Ecto/query parameters or equivalent prepared statements rather than concatenating user-controlled values into SQL expressions.

Most importantly, authorization and backend execution must operate on the **same normalized request values**.

If:

tenant\_id

is present in the URL path, the backend should not independently allow a query parameter to redefine it.

For example, the application could reject:

?tenant\_id=...

when tenant\_id is already bound by the HTTP route.

Even better, authorization should be performed against the exact request object that will be passed to the backend.

HTTP request

↓

Normalize parameters

↓

Construct GetDocumentRequest

↓

Authorize THAT request

↓

Execute THAT request

rather than:

HTTP path

↓

Authorize

query parameters

↓

Construct different backend request

**“We Need to Talk”** was a great example of why complex applications can fail even when individual security controls appear to work.

The tenant authorization check wasn’t simply missing.

The API wasn’t simply unauthenticated.

The database wasn’t simply exposed.

Instead, the vulnerabilities formed a chain:

OTP authorization gap

↓

Internal endpoint access

↓

Exposed gRPC contract

↓

Blind SQL injection

↓

Initech document discovery

↓

gRPC parameter confusion

↓

Tenant isolation bypass

↓

Restricted incident packet

↓

FLAG

And the challenge’s opening sentence turned out to describe the root cause almost perfectly:

The two sides weren’t communicating about the same tenant.

That was enough to break the boundary.

**Flag:**

*All exploitation described above was performed against the provided CTF target. The solve process and extracted values are based on the challenge execution log.*
