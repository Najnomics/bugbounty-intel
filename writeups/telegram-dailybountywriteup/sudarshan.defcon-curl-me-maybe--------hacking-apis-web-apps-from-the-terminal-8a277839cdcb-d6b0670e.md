# curl Me Maybe? ➡️ ⬅️Hacking APIs & Web Apps From the Terminal

- **Source URL:** https://medium.com/@sudarshan.defcon/curl-me-maybe-%EF%B8%8F-%EF%B8%8Fhacking-apis-web-apps-from-the-terminal-8a277839cdcb
- **Fetched from:** https://medium.com/@sudarshan.defcon/curl-me-maybe-%EF%B8%8F-%EF%B8%8Fhacking-apis-web-apps-from-the-terminal-8a277839cdcb?source=rss-08202f7f94bd------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14892 (id 14892)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** Sudarshan Patel / Tue, 01 Sep 2026 04:56:02 GMT

curl is my first move, not my last resort

If you spend enough time in cybersecurity, you eventually realize something:

*The coolest-looking tool is rarely the tool you use the most.*

And curl is probably the best example. 😄

No fancy dashboard.

No attack graph.

No neon-green hacker UI.

Just:

curl https://target.example.com

Yet somehow, this tiny command-line tool can become one of the most useful things in your pentesting and bug-bounty toolbox.

Headers? ✅

APIs? ✅

Authentication testing? ✅

GraphQL? ✅

IDOR/BOLA testing? ✅

Host-header manipulation? ✅

Automation? ✅

Weird malformed requests? Also ✅

The best part?

curl mostly stays out of your way.

You tell it what request to send.

It sends it.

The server responds.

You stare at the response and start asking uncomfortable questions. 🕵️

Browsers try very hard to be helpful.

They may:

Normally, that’s great.

During security testing?

Sometimes you want the opposite.

You want to know exactly what was sent and exactly what came back.

That’s where curl shines.

Think of it as a remote control for HTTP.

And once you learn roughly a dozen useful flags, you can do a surprising amount of testing without touching anything heavier.

You don’t need to memorize the entire man page.

Start here.

curl -v https://target.example.com/

This shows the request and response conversation.

You’ll see lines like:

\> GET / HTTP/1.1

> Host: target.example.com

\< HTTP/1.1 200 OK

\< Content-Type: text/html

If something behaves strangely, -v is often the first thing I reach for.

curl -i https://target.example.com/

Useful when you want both:

If you only want headers:

curl -I https://target.example.com/

⚠️ Small warning:

-I sends a HEAD request.

Some servers treat HEAD differently from GET, so don't immediately assume the behavior is identical.

curl -sS https://target.example.com/

-s removes the progress meter.

-S keeps useful error messages.

For scripts, this combination is beautiful. 🤌

curl -L https://target.example.com/

Useful normally.

But when testing redirects?

Leave it off.

Otherwise this:

302 → attacker.example

might disappear because curl immediately follows it.

curl -k https://target.example.com/

Useful for:

Don’t confuse this with fixing TLS problems though.

You’re simply telling curl:

*“Yes, I know the certificate looks suspicious. Continue anyway.” 😅*

curl https://target.example.com/ \

-H 'X-Test: hello'

Stack as many as you want:

curl https://target.example.com/api \

-H 'Authorization: Bearer TOKEN' \

-H 'Content-Type: application/json' \

-H 'X-Forwarded-For: 127.0.0.1'

This flag alone opens the door to a ridiculous number of security tests.

curl https://target.example.com/login \

-d 'username=test&password=test'

For JSON:

curl https://target.example.com/api/login \

-H 'Content-Type: application/json' \

-d '{"username":"test","password":"test"}'

curl -X PUT https://target.example.com/api/profile

You can test:

GET

POST

PUT

PATCH

DELETE

OPTIONS

…and whatever else the application exposes.

Instead of manually fighting with characters like:

&

=

?

%

+

you can use:

curl -G https://target.example.com/search \

--data-urlencode 'q=test value'

Very handy when you’re experimenting with parameters.

Now we get to the fun part.

One quick request can already tell you quite a bit.

curl -sI https://target.example.com | \

grep -iE 'strict-transport|content-security|x-frame|x-content-type|referrer-policy|permissions-policy'

You’re looking for things like:

Strict-Transport-Security

Content-Security-Policy

X-Frame-Options

X-Content-Type-Options

Referrer-Policy

Permissions-Policy

Missing headers don’t automatically mean:

*🚨 CRITICAL SECURITY INCIDENT 🚨*

Context matters.

But they’re useful signals when assessing the application’s overall security posture.

Applications occasionally expose HTTP methods nobody expected to be reachable.

Try:

for m in GET POST PUT DELETE PATCH OPTIONS TRACE; do

printf '%s: ' "$m"

curl -s -o /dev/null \

-w '%{http\_code}\n' \

-X "$m" \

[https://target.example.com/admin/config](https://target.example.com/admin/config)

done

Example output:

GET: 403

POST: 403

PUT: 200

DELETE: 405

PATCH: 405

OPTIONS: 204

TRACE: 405

That PUT: 200 deserves attention. 👀

A 200 alone doesn't prove a vulnerability.

But it tells you:

*“Hey… investigate me.”*

Because curl lets us control headers directly, testing Host-header behavior is easy.

curl -s https://target.example.com/password-reset \

-H 'Host: test.example'

Also try common proxy headers:

curl -s https://target.example.com/password-reset \

-H 'X-Forwarded-Host: test.example'

Other headers worth checking in an authorized assessment include:

Forwarded

X-Forwarded-Host

X-Original-Host

X-Host

You’re interested in places where the application generates absolute URLs from attacker-controlled headers.

For example:

https://test.example/reset?token=...

instead of:

https://target.example.com/reset?token=...

If sensitive links are constructed this way, you may have a Host-header injection or password-reset-poisoning issue.

Normally, curl may normalize parts of the URL.

During path traversal testing, that’s sometimes exactly what you **don’t** want.

Use:

curl --path-as-is \

'https://target.example.com/assets/../../test.txt'

--path-as-is basically tells curl:

*“Don’t clean my URL. Send the weird thing exactly how I wrote it.”*

Very useful when testing how reverse proxies, web servers, and application routers interpret paths differently.

Those differences are where interesting bugs sometimes hide. 🐛

This flag deserves more love.

Syntax:

curl --resolve HOST:PORT:IP https://HOST/

Example:

curl -sk \

--resolve target.example.com:443:203.0.113.10 \

https://target.example.com/

curl connects to:

203.0.113.10

while still requesting:

target.example.com

This is useful when validating:

Use this carefully and only against infrastructure explicitly included in scope.

APIs are basically structured HTTP requests.

curl speaks HTTP fluently.

Which makes the combination almost unfair. 😄

The classic authenticated request:

curl -s https://target.example.com/api/v1/me \

-H 'Authorization: Bearer YOUR\_TOKEN' \

-H 'Content-Type: application/json' | jq

And yes:

Install jq.

Please.

Your eyes deserve better than one-line minified JSON. 😂

curl -s https://target.example.com/api/v1/me | jq

Turns this:

`{"id":42,"name":"John","email":"john@example.com","role":"user"}`
into something humans were actually meant to read.

Broken Object Level Authorization remains one of the most important API weaknesses to look for.

Imagine your account can access:

/api/v1/users/42

What happens with:

/api/v1/users/43

…???!!!

Start manually:

curl -s \

-H 'Authorization: Bearer YOUR\_LOW\_PRIV\_TOKEN' \

https://target.example.com/api/v1/users/43 | jq

If you have authorization to test multiple known test objects, comparing response metadata can also help:

for id in 40 41 42 43 44; do

printf '%s: ' "$id"

curl -s \

-o /dev/null \

-w '%{http\_code} %{size\_download}\n' \

-H 'Authorization: Bearer YOUR\_TOKEN' \

"https://target.example.com/api/v1/users/$id"

done

40: 403 81

41: 403 81

42: 200 387

43: 200 421

44: 403 81

Why is 43 returning a different result?

That’s where the investigation begins.

A different response size is **not proof** of IDOR.

Actually verify whether unauthorized data or functionality becomes accessible.

False positives are boring.

Reproducible authorization failures are not. 🎯

Imagine the application expects:

```
{
  "email": "me@example.com",
  "name": "Tester"
}
```
What happens if you send additional properties?

For a controlled test account:

curl -s -X PATCH \

https://target.example.com/api/v1/profile \

-H 'Authorization: Bearer YOUR\_TOKEN' \

-H 'Content-Type: application/json' \

-d '{

"name":"Tester",

"role":"admin",

"isAdmin":true

}'

The important question is **not**:

*Did the server return 200?*

The real question is:

*Did the server actually persist or honor a property the current user should never be able to control?*

That’s the difference between noise and a finding.

Servers sometimes have multiple request parsers.

And occasionally those parsers disagree.

curl -s -X POST \

https://target.example.com/api/v1/example \

-H 'Content-Type: application/x-www-form-urlencoded' \

-d '{"test":true}'

You can compare behavior between:

application/json

application/x-www-form-urlencoded

multipart/form-data

text/plain

Why?

Because validation middleware may inspect the request one way while application code parses it another way.

And whenever two components disagree about what they’re looking at…

security researchers start smiling. 😏

Found something like:

/graphql

/api/graphql

/v1/graphql

One of the first things worth checking is whether schema introspection is enabled.

curl -s -X POST \

https://target.example.com/graphql \

-H 'Content-Type: application/json' \

-d '{"query":"{\_\_schema{types{name fields{name}}}}"}' | jq

If introspection is available, you may learn about:

Remember:

But during an assessment?

It’s one hell of a map. 🗺️

For an authenticated endpoint, compare behavior under different legitimate test conditions.

curl -i https://target.example.com/api/v1/account

curl -i https://target.example.com/api/v1/account \

-H 'Authorization: Bearer invalid'

curl -i https://target.example.com/api/v1/account \

-H 'Authorization: Bearer EXPIRED\_TEST\_TOKEN'

curl -i https://target.example.com/api/v1/admin \

-H 'Authorization: Bearer LOW\_PRIV\_TOKEN'

This simple matrix catches a surprising number of:

The server should not merely ask:

*“Do you have a token?”*

It should ask:

*“Is this token valid, and is this identity actually allowed to perform this action?”*

Huge difference.

One clever request is nice.

But real security assessments involve hundreds or thousands of requests.

That’s where shell scripting makes curl much more powerful.

Instead of manually copying an authentication token every five minutes:

TOKEN=$(curl -s -X POST \

https://target.example.com/api/v1/login \

-H 'Content-Type: application/json' \

-d '{"username":"testuser","password":"TEST\_PASSWORD"}' \

| jq -r '.token')

Then:

curl -s https://target.example.com/api/v1/me \

-H "Authorization: Bearer $TOKEN" | jq

Much cleaner.

Just remember:

Future-you will thank present-you.

One of the most underrated curl features:

-w

curl -s \

-o /dev/null \

-w 'status=%{http\_code} time=%{time\_total}s size=%{size\_download}b\n' \

https://target.example.com/api/v1/health

Output:

status=200 time=0.184s size=742b

Now we’re measuring:

Why does that matter?

Because sometimes the vulnerability isn’t visible in the response body.

The clue might be:

200 → 403

or:

421 bytes → 6,841 bytes

0.2 sec → 5.1 sec

Tiny differences can tell you where to look deeper.

Yes, tools like ffuf, feroxbuster, and dirsearch are much better for serious content discovery.

But knowing how the underlying logic works is still useful.

while read -r path; do

code=$(curl -s \

-o /dev/null \

-w '%{http\_code}' \

"https://target.example.com$path")

echo "$code  $path"

done \< paths.txt

Sample output:

200 /login

200 /robots.txt

403 /admin

404 /backup

302 /dashboard

Congratulations.

You just built the world’s saddest directory scanner. 😂

But now you understand exactly what tools such as ffuf are doing at a much higher speed.

And understanding the primitive is always useful.

Whenever possible, provide a minimal reproducible curl command in your vulnerability report.

curl -i \

-H 'Authorization: Bearer LOW\_PRIVILEGE\_TEST\_TOKEN' \

https://target.example.com/api/v1/orders/TEST\_OBJECT\_ID

Then clearly explain:

Expected:

403 Forbidden

Actual:

200 OK containing another test user's order information

This is much better than writing three paragraphs saying:

*“An attacker may potentially under certain circumstances possibly access unauthorized resources…”*

Nobody has time for that. 💀

Give developers:

If they can reproduce the issue in 30 seconds, your report becomes much harder to misunderstand.

If I had to survive an assessment with only a few commands, these are the ones I’d remember:

curl -v URL

See everything.

curl -i URL

Headers + body.

curl -sS URL

Clean output.

curl -L URL

Follow redirects.

curl -k URL

Ignore certificate validation.

curl -H 'Header: value' URL

Manipulate headers.

curl -X METHOD URL

Change HTTP method.

curl -d 'data' URL

Send request bodies.

curl --path-as-is URL

Preserve unusual URL paths.

curl --resolve HOST:443:IP https://HOST/

Control DNS resolution.

`curl -w '%{http_code} %{time_total} %{size_download}' URL`
Measure responses.

Master those first.

Everything else comes naturally.

curl survives because it solves a very simple problem extremely well.

It puts almost nothing between **you** and **HTTP**.

And that’s incredibly valuable when your job is figuring out why an application behaves differently from how its developers expected it to behave.

You don’t need 200 flags memorized.

Start with:

-v

-i

-sS

-L

-k

-H

-d

-X

-G

--data-urlencode

--path-as-is

--resolve

-w

Learn what each one actually changes.

Then combine them.

Then put them into loops.

Then start comparing responses.

That’s when curl stops feeling like a command-line downloader and starts feeling like a pentesting instrument. 🧪⚔️

And once it becomes muscle memory?

You’ll probably catch yourself opening the terminal before opening half the security tools installed on your machine.

Sometimes the old tools are still around because they’re simply that damn good. 😄

Thanks a lot for reading! ❤️

I hope this made curl feel a little less boring and a lot more useful.

If you found this helpful, feel free to share it with others who are learning web security. Stay curious, stay ethical, and keep hacking responsibly 🚀🔐.

See you in the next Writeups or Walkthroughs📡 🛰️

**Happy hacking!** 🚀

**Stay curious, keep learning**📚✨🧠📖

**Crafted by: Sudarshan Patel** 👨💻

**Connect with me on LinkedIn:** [www.linkedin.com/in/sudarshan-patel](http://www.linkedin.com/in/sudarshan-patel)

**Follow my Tweets on X:** [@loneliestwolf3](https://x.com/loneliestwolf3)
