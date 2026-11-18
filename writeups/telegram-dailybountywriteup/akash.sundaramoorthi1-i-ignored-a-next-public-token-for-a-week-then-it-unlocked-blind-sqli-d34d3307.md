# I Ignored a NEXT_PUBLIC_ Token for a Week. Then It Unlocked Blind SQLi and the Whole Database

- **Source URL:** https://medium.com/@akash.sundaramoorthi1/i-ignored-a-next-public-token-for-a-week-then-it-unlocked-blind-sqli-and-the-whole-database-6b61f3c1e07d
- **Fetched from:** https://medium.com/feed/@akash.sundaramoorthi1
- **Fetched:** 2026-11-18
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14987 (id 14987)
- **Method:** medium-rss-content readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
### *Hey everyone!*

*I’m Akash Sundaramoorthi, a 20 year old bug hunter and this is my very first writeup. Hope you enjoy it.*

So let’s jump straight into the finding.

I was bored one day, scrolling through reels, when an ad for an Indian D2C company popped up. Being the kind of guy who gets curious about anything and everything, I figured I’d poke around their website and see if I could find any vulnerabilities.

I started with the basics. Subdomain enumeration, waybackurls, a bit of JS analysis. Nothing jumped out. So out of pure habit I opened the page source, and there it was sitting in plain sight: a NEXT\_PUBLIC\_ env block with an API key and API url baked right into the HTML. *Jackpot*, I thought. A leaked API key and API url.

I naturally tried throwing it at the gateway:

curl -s https://api.target.in \

-H "Authorization: Bearer \<LEAKED-TOKEN>"

But instead of an expected 401, I got a 400:

```
{"message":"Failed to connect to tenant database: BadRequestException: 
Tenant not found: target","statusCode":400,
"timestamp":"2026-06-25T20:44:54.652Z","path":"/"}
```
That was the interesting part. A 401 would’ve meant the key was dead. A 400 complaining about a tenant database meant the key had already cleared auth, the gateway just didn’t know which database to point it at, and it had guessed “target” from my hostname.

I spent the next few hours trying to guess the right tenant value, the domain, variations of it, watching the site’s own network calls for a hint. Nothing worked, and I eventually thought it was a dead, rotated key. So I moved on to one of the company’s acquisitions instead, since acquisitions often share the same backend.

Acquisitions are underrated because they share the same backend and infra as their parent company. So I ran the same recon I’d done on the parent, and I fed the JS files to Claude and asked it to pull out every API route and endpoint. One of them caught my eye:

/api/member?id=\<id>&fields=given\_name,email\_addr

Looking at that endpoint, I immediately signed up for an account, grabbed my own id, and tried hitting it. It came back with a 401. So I went digging through the JS and replaying requests in Burp, and there it was in one of the calls: X-Tenant-Id: brand-name. I dropped that tenant id into my curl command, hit send, and to no avail, another 401.

Now I was a bit demotivated. I went straight back to the JS to figure out how the request was actually being signed, and again came up with nothing.

Then it hit me: the API key I’d shelved as dead didn’t need a *tenant name*, it needed a *tenant id,* and I now had one, sitting right there in the acquisition’s requests: X-Tenant-Id: brand-name. I’d been treating the key and the tenant id as two separate dead ends. They were two halves of the same lock.

curl -s https://api.acquisition.com/api/member?id=\<my\_id>&fields=given\_name,email\_addr \

-H "X-Tenant-Id: brand-name" \

-H "X-Api-Token: \<LEAKED-TOKEN>"

*BOOM.* It returned my data.

But that on its own isn’t a vulnerability. It only showed *my* details. The interesting part was what I’d glossed over to get here: that fields=given\_name,email\_addr in the URL. The endpoint was letting me name the columns I wanted back.

Poking the parameter:

The first thing I did was feed it a column that obviously doesn’t exist:

GET /api/member?id=\<my\_id>&fields=zzz

X-Tenant-Id: brand-name

X-Api-Token: \<LEAKED-TOKEN>

And the server handed me a gift:

```
{
  "error": "column member.zzz does not exist",
  "query": "SELECT member.zzz FROM member WHERE member.id = <my_id>"
}
```
Two things jumped out. First, my input zzz had gone *straight into the SQL* as a column name, untouched. Second, the server was kind enough to echo back the exact query it built, so I could see precisely where I was landing:

SELECT member.\<MY\_INPUT> FROM member WHERE member.id = \<my\_id>

That was the moment the fields thing made sense. Column names are *identifiers*, not values, and prepared statements can only ever parameterize values. A query that lets you pick columns by name almost always means someone is gluing strings together by hand, with no escaping. Which is exactly what this was. My input was being dropped into the SELECT list behind a fixed member. prefix.

Where my usual payloads fell flat

Reflex kicked in and I reached for the classics OR 1=1, a quick subquery, the stuff every tutorial drills into you. Both failed instantly. Here's why: those payloads assume you're injecting into a WHERE clause, where you're supplying a *value* you can twist into a condition.

SELECT \* FROM member WHERE id = \[INJECTION HERE\]   ← OR 1=1 works here

My injection point was somewhere else entirely — the column list right after SELECT, where the database expects an *identifier*, not a value:

SELECT member.\[INJECTION HERE\] FROM member WHERE id = \<my\_id>   ← OR 1=1 is meaningless here

There’s no condition to flip and no quote to escape. Worse, the app was silently prefixing whatever I sent with member., so a subquery like (SELECT token FROM secrets LIMIT 1) just became member.(SELECT... — garbage to the parser. This is usually where I'd write the bug off as unexploitable. Instead I stopped asking "how do I inject" and started asking "what's actually valid right after SELECT member.?"

Beating the prefix

I couldn’t delete the member. prefix. So instead of fighting it, I decided to change what member even pointed at.

If I rewrite the FROM clause and alias a *different* table back to the name member, then member.\<anything> quietly resolves against that other table:

fields=token,role FROM secrets AS member-- -

The server assembled this:

SELECT member.token, member.role

FROM secrets AS member-- - FROM member WHERE member.id = \<my\_id>

The -- - comments out the app's own trailing FROM ... WHERE ..., and what's left is clean:

SELECT member.token, member.role FROM secrets AS member

The prefix that had been blocking me the whole time was now pointing at a table I was never supposed to see:

`{ "rows": [["tok_demo_INVENTED_0000", "admin"]] }`
An auth token and a role, pouring out of an endpoint that’s only supposed to hand back a name and an email.

Mapping the rest of the database

Same trick, this time aimed at the database’s own catalog instead of a guessed table name:

fields=table\_name FROM information\_schema.tables AS member-- -

And it listed the tables back to me. From there I could walk every table, then every column, and reach just about anything in that database. All of it through one “harmless” fields parameter, on an endpoint that was supposed to return a first name.

This wasn’t scoped to my account or even to one company, the X-Tenant-Id header meant the same injection point worked across every tenant on that backend, including the parent company and its other brands sharing the same infra. One vulnerable fields parameter, multiplied across every customer the platform ran.

Once the injection was confirmed I stopped immediately, wrote up the full findings, and sent the report directly to the CTO. The team responded quickly and we jumped on a call to walk through the methodology together.

The team patched it within a few days and confirmed the fix on retest. Came back as a Critical.
