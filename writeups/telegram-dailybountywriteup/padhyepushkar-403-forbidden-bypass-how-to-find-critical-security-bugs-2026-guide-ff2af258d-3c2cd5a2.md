# "403 Forbidden Bypass

- **Source URL:** https://medium.com/@padhyepushkar/403-forbidden-bypass-how-to-find-critical-security-bugs-2026-guide-ff2af258d882
- **Fetched from:** https://medium.com/@padhyepushkar/403-forbidden-bypass-how-to-find-critical-security-bugs-2026-guide-ff2af258d882?source=rss-7f768e2cc329------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14918 (id 14918)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** Pushkar Padhye / Sun, 20 Sep 2026 05:58:03 GMT

You find an interesting endpoint.

You send the request.

And the server responds:

403 Forbidden

You try again.

Still 403.

Different endpoint?

Admin panel?

At this point, the server might as well be saying:

***“Nice try, buddy.”***

But here’s the thing:

**403 is not always the end of the road.**

Sometimes, it’s the beginning.

A 403 tells you that *something* understood your request and decided you weren’t allowed to continue.

The interesting question is:

***Who made that decision & did every layer of the application make the same decision?***

That’s where things get fun.

HTTP status codes are basically the internet way of leaving sticky notes on your requests.

200 → Here's what you asked for.

301 → Go somewhere else.

404 → I can't find that.

403 → I know what you want. No.

500 → Something exploded.

A 403 usually means the server understood your request but refused to fulfill it.

But modern applications aren’t usually:

Browser → Server

They’re more like:

Browser

↓

CDN

↓

WAF

↓

Reverse Proxy

↓

Web Server

↓

Application

↓

API

And here’s the interesting part:

**These layers don’t always interpret a request identically.**

If one layer sees:

/admin

while another eventually interprets the request as:

/admin/

you have a potential discrepancy.

And security bugs love discrepancies.

Let’s get one thing out of the way.

Suppose you start with:

/admin → 403

You try something weird and get:

/admin/ → 200

Your brain immediately screams:

***“BYPASS!”***

Slow down.

That 200 could be:

The interesting result isn’t:

403 → 200

It’s:

Unauthorized

↓

Protected functionality

↓

Accessible

That’s the difference between an interesting response and a vulnerability.

Now let’s actually test some things.

Don’t think of these as magic strings.

Think of each payload as a **question you’re asking the application**.

Test Example What you’re investigating Trailing slash/admin/Path normalization Double slash//admin//Proxy/backend parsing Dot segment/admin/./Canonicalization Encoded character/%61dminURL decoding Encoded slash/admin%2fSeparator handling Double encoding/%2561dminMultiple decoding stages Forwarded IPX-Forwarded-For: 127.0.0.1Proxy trust Rewrite header X-Original-URL: /adminURL rewriting Alternate method Post /adminMethod-level authorization Duplicate parameter?role=user&role=adminParser differences Semicolon/admin;Framework-specific parsing

Let’s break down the interesting ones.

Start with:

GET /admin HTTP/1.1

Host: target.example

You get:

Now try:

GET /admin/ HTTP/1.1

Host: target.example

Why?

Because different components may normalize paths differently.

You can also investigate:

/admin//

/admin/./

Imagine:

WAF

↓

"That's not exactly /admin."

Backend

↓

normalizes it

↓

/admin

That disagreement is what you’re hunting.

Here’s a classic.

The character:

a

can be represented as:

%61

So:

becomes:

/%61dmin

Try:

GET /%61dmin HTTP/1.1

Host: target.example

You can also investigate encoded separators:

/admin%2f

The interesting question isn’t:

*“Does %2f bypass the WAF?"*

***“Does the WAF decode this the same way the backend does?”***

That’s a much more powerful way to think about bypass research.

Now we go one level deeper.

You know:

%2f

represents /.

So what happens when the % itself is encoded?

%252f

Conceptually:

%252f

↓

%2f

↓

/

If multiple layers decode the request at different stages, you can occasionally get:

Security layer → sees one thing

Backend → sees another

And that’s where parser confusion becomes interesting.

Now let’s talk about something beginners often overlook.

HTTP headers aren’t just boring metadata.

Sometimes applications make security decisions based on them.

For example:

X-Forwarded-For: 127.0.0.1

or:

X-Real-IP: 127.0.0.1

Why test this?

Because badly configured applications can sometimes trust attacker-controlled proxy information.

You

↓

X-Forwarded-For: 127.0.0.1

↓

Application

↓

"Internal request!"

If that actually changes authorization behavior, you’ve found something worth investigating.

Don’t assume it works.

**Prove that the application is making a security decision based on the header.**

Here’s another one that can produce some interesting behavior in proxy-heavy architectures.

Try comparing:

GET / HTTP/1.1

Host: target.example

with:

GET / HTTP/1.1

Host: target.example

X-Original-URL: /admin

You might get:

Normal request → 200

Modified request → 403

Or:

Normal request → 200

Modified request → different response

Or, in a badly configured environment:

Modified request → protected content

The last case is where things get spicy.

Don’t forget that HTTP has more than GET.

GET

POST

PUT

PATCH

DELETE

HEAD

OPTIONS

Suppose:

GET /admin HTTP/1.1

returns:

403

You can investigate whether authorization is consistently enforced for another supported method:

POST /admin HTTP/1.1

If the response changes, investigate why.

For state-changing requests, keep your tests non-destructive and follow the target’s rules.

The interesting finding isn’t:

GET → 403

POST → 200

***An unauthorized user can actually perform functionality that should require authorization.***

Here’s a fun one.

Suppose you have:

/account?role=user

What happens if you send:

/account?role=user&role=admin

Different components may disagree about which value wins.

WAF

↓

uses first value

↓

role=user

Application

↓

uses last value

↓

role=admin

Or vice versa.

This is called **parameter pollution**, and it can become interesting when duplicate parameters influence authorization, redirects, account selection, or other security-sensitive behavior.

Again:

**The bug isn’t the duplicate parameter.**

The bug is the inconsistent interpretation that produces security impact.

This is where theory becomes much more fun.

Send your request to **Burp Repeater**.

Start with a baseline:

GET /admin HTTP/1.1

Host: target.example

Cookie: session=...

Record:

Status: 403

Length: 1234

Now change **one thing**.

GET /admin/ HTTP/1.1

Compare.

Reset.

GET /%61dmin HTTP/1.1

Try a relevant header:

X-Original-URL: /admin

You’re no longer randomly throwing payloads.

You’re running experiments.

And that’s a much better skill.

Here’s the part many beginners don’t think about.

You may assume the WAF only sees:

URL

Headers

Cookies

Body

But modern security systems can also use **connection-level signals**, including characteristics of the TLS handshake.

So you might see:

Browser → Target → 200

Burp → Target → 403

Even though you’re sending what appears to be the same HTTP request.

That should make you curious.

Because your HTTP request isn’t necessarily the only thing that’s different.

In current Burp versions, you can find TLS-related configuration under:

Settings

↓

Network

↓

TLS

There you can inspect/configure how Burp negotiates TLS with upstream servers, including supported protocols and cipher suites.

Don’t think:

*“I’ll randomly change ciphers until the WAF gives up.”*

Think:

***“Is the target treating Burp differently because of the connection characteristics?”***

That’s a much more interesting experiment.

Burp also has **TLS pass-through**.

Look under:

Settings

↓

Proxy

↓

TLS pass through

For an authorized target, you can configure a host to pass through without Burp terminating the TLS connection.

That gives you an interesting comparison:

Normal Burp

↓

Browser → Burp → Target

↓

403

versus:

TLS pass-through

↓

Browser → Burp → Target

↓

?

Now you can ask:

***Is the target reacting to the browser’s original TLS characteristics?***

That’s a completely different dimension of testing.

And suddenly your 403 investigation has gone from:

"Maybe I need another URL."

to:

"Wait... what exactly is the WAF fingerprinting?"

That’s the kind of rabbit hole bug bounty gets fun for.

TLS isn’t the only layer worth investigating.

Modern browsers commonly use HTTP/2 when supported.

Burp can also work with HTTP/2, and you can investigate HTTP/1 versus HTTP/2 behavior.

HTTP/1.1 → 403

HTTP/2 → ?

Or the reverse.

Again, you’re looking for differences in how the request is processed.

Sometimes a security control understands one representation correctly and another imperfectly.

Sometimes nothing happens.

That’s fine.

You’re learning how the target works.

Let’s say you’ve finally reached something interesting.

Now what?

Look for information disclosure.

A website can accidentally reveal:

Places worth understanding include:

/.env

/.git/config

/debug

/status

/health

And don’t forget backup files:

index.php.bak

config.old

app.js\~

backup.zip

These aren’t magic URLs.

They’re **common examples of things that have historically been exposed through poor deployment practices**.

If you find something, verify what it actually contains and what impact it has.

Open the application’s JavaScript.

Seriously.

Modern frontend applications often reveal a surprising amount of information.

Search for things like:

/api/

/graphql

/admin

/internal

/debug

token

key

secret

You might discover:

And sometimes you’ll encounter something that looks like a secret.

But remember:

"Looks like a key"

doesn’t automatically mean:

"Valid credential"

If it’s actually usable for unauthorized access, **now you’ve got something worth reporting.**

Now put the pieces together.

/api/internal/users

You investigate the request processing.

You discover a parsing difference.

You verify that an unauthorized request reaches the protected endpoint.

Then the endpoint returns information it shouldn’t.

Maybe internal user data.

Maybe configuration.

Maybe something even more sensitive.

Now you’ve chained:

Access-control weakness

+

Information disclosure

=

Meaningful security impact

That’s much more interesting than simply getting a different status code.

Here’s the whole process:

/admin

/internal

/api/internal/...

Don’t modify ten things at once.

/admin/

/admin//

/admin/./

/%61dmin

X-Forwarded-For

X-Real-IP

X-Original-URL

Where appropriate:

GET

POST

PUT

PATCH

HTTP/1.1

HTTP/2

Normal Burp

TLS pass-through

Check responses, JavaScript, error messages, and other **in-scope** resources.

Don’t submit:

*“I got 200!”*

Submit:

*“An unauthorized request can access X, which exposes Y.”*

That’s a bug bounty report.

And here’s something worth remembering in 2026.

AI can help you understand a target.

It can explain an HTTP response.

It can suggest hypotheses.

It can help write your report.

But don’t let it do your thinking for you.

If an AI tells you:

*“This is definitely a critical 403 bypass.”*

Ask:

***“Show me the evidence.”***

If you can’t reproduce it, don’t report it.

If you can’t explain it, don’t pretend you understand it.

A clean, reproducible finding beats a pile of AI-generated guesses.

Here’s your homework.

Find a legal lab or an in-scope bug bounty target.

Find a 403.

Then don’t immediately Google:

*“403 bypass payload”*

Instead, build a little experiment.

Baseline

↓

Path

↓

Encoding

↓

Headers

↓

Methods

↓

HTTP/1 vs HTTP/2

↓

TLS behavior

Record what changes.

Then ask the question that matters:

***“Why?”***

If you can answer that question, you’re no longer just throwing payloads at a website.

You’re learning how its security architecture works.

The best bug bounty hunters aren’t necessarily the people with the biggest wordlists.

They’re the people who notice something weird and refuse to stop at:

*“Huh. That’s strange.”*

They ask:

***“What happens if…?”***

What happens if I add a slash?

What happens if I encode the path?

What happens if the proxy sees a different URL?

What happens if the application sees a different HTTP method?

What happens if Burp and the browser negotiate the connection differently?

And eventually:

***“What exactly is the WAF seeing that I’m not?”***

That’s where things get interesting.

So the next time you see:

don’t close the tab.

Open Burp.

Send it to Repeater.

Change one thing.

Watch what happens.

Because sometimes **Forbidden isn’t the answer.**

It’s the question.

Pick an authorized target or lab, fire up Burp, find a 403, and start experimenting.

And when you discover that the response changes?

**Don’t celebrate yet.**

Figure out *why*.

That’s where the real bug is hiding.

***Disclaimer:*** *Only test systems you have explicit permission to test. Bug bounty programs authorize testing only within their stated scope and rules. Keep testing non-destructive, respect rate limits, and follow the program’s disclosure requirements.*
