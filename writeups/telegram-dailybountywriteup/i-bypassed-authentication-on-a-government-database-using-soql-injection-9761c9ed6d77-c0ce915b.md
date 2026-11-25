# I Bypassed Authentication on a Government Database Using SoQL Injection

- **Source URL:** https://clarkvoss.medium.com/i-bypassed-authentication-on-a-government-database-using-soql-injection-9761c9ed6d77
- **Fetched from:** https://clarkvoss.medium.com/i-bypassed-authentication-on-a-government-database-using-soql-injection-9761c9ed6d77?source=rss-283f77d6ae07------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14914 (id 14914)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** Clark Voss / Tue, 15 Sep 2026 23:57:09 GMT

I was testing a government data portal running Socrata when I injected an arithmetic expression into a query parameter and got back the computed result. Classic injection. But this wasn’t SQL injection in the traditional sense. It was SoQL injection, Socrata’s own query language that compiles down to PostgreSQL. And nothing in my toolkit could do anything with it.

sqlmap choked. Every payload it sent got rejected by SoQL’s parser before it ever touched the database. NoSQL techniques didn’t apply. The injection was confirmed and completely unexploitable with existing tools.

So I built one.

Socrata runs open data portals for a huge number of government agencies and cities. Their SODA API exposes endpoints that accept SoQL queries, which gets compiled to SQL and executed against Postgres on the backend. When user input hits the $query parameter without proper sanitization, you get SoQL injection.

The problem is that SoQL is not SQL. It has its own parser, its own function whitelist, and its own restrictions. You can confirm injection with simple math:

$query=(select 198766\*667891)

Response: 132754022506. Server did the multiplication. Injection confirmed. But actually extracting anything useful? That's where it gets hard.

I needed a tool that understood the target, so I built soqli\_hunter. Python, single file, speaks SoQL natively. It takes raw request files from Burp with a \* marker for the injection point, same workflow as sqlmap's -r flag.

First order of business was mapping the attack surface. I threw 138 payloads at it across 7 technique categories to figure out what SoQL lets through and what it blocks.

What worked: substring(), length(), upper(), lower(), chr(), || concatenation, CASE WHEN, ::text cast, ::boolean cast.

What didn’t: version(), current\_user, current\_database(), ascii(), pg\_sleep(), stacked queries, basically everything that would let you actually do something interesting. The function whitelist caught it all.

Every standard extraction path was dead. Time to find a new one.

I was testing the :: type cast operator when I hit something interesting. Casting to ::text worked fine. Casting to ::integer got blocked by the SoQL typechecker. But ::boolean? That one sailed right through to Postgres.

And when Postgres tried to evaluate 'actual\_data'::boolean, it couldn't. Non-boolean strings can't cast to boolean. But here's the thing: the error message included the value it was trying to cast.

$query=(select substring(column\_name::text, 1, 50)::boolean)

Response:

```
{
  "code": "soql.pg.query-error",
  "data": {
    "message": "ERROR: invalid input syntax for type boolean: \"actual_column_data\""
  }
}
```
The error code tells the whole story. soql.pg.query-error, not soql.analyzer.typechecker. The cast bypassed SoQL entirely and reached Postgres. And Socrata forwarded the raw Postgres error back to me, extracted value and all.

I built this into soqli\_hunter as the error\_cast extraction method. 50 characters per request, full values come back in one or two calls.

Only problem: the data I was extracting was the same public data the normal API returned. I needed to reach something I wasn’t supposed to have access to.

This one came from a mistake. I was testing Postgres dollar-quoting ($$soqli$$) to see if I could bypass SoQL's string handling. The parser rejected it. But the error message was more interesting than the test:

Expected one of \`)\`, \`|>\`, \`UNION\`, \`INTERSECT\`, \`MINUS\`, \`UNION ALL\`,

\`INTERSECT ALL\`, \`MINUS ALL\`, \`LIMIT\`, \`OFFSET\`, \`ORDER BY\`, ...

UNION. Right there in the parser’s expected token list. I tested it:

(select 1) UNION (select 2)

200 OK. Two records came back.

SoQL supports UNION and I’d never seen it documented anywhere as an injection vector. I could inject fabricated records into API responses alongside real government data. Response manipulation on a government dataset is interesting, but the real question was whether UNION could reach across dataset boundaries.

The FROM clause rejected every dataset identifier I threw at it. Quoted names, backticks, underscores, the internal identifiers that leaked through earlier error messages. Nothing worked as a table reference.

Then I tried Socrata’s @ prefix:

(select 'x') UNION (select \* from @target-dataset limit 1)

Column count mismatch error. But it wasn’t a rejection. The query coordinator had actually resolved the target dataset and compared its schema against my query. Cross-dataset UNION was live.

The column mismatch errors were gold by themselves. Every failed UNION attempt leaked the target dataset’s full schema: column names, types, and internal dataset identifiers. I built an enumeration loop and mapped dozens of datasets through their error messages alone.

I scraped the platform’s catalog and found 50 unpublished datasets. Draft copies, working versions. Tested each one through the @ UNION path. All 50 schemas leaked through error messages.

One of them caught my attention. When I referenced it in a UNION query, the error messages showed the query coordinator resolving it to a different internal dataset ID. I checked that target dataset through the normal API:

GET /resource/\[target-dataset\].json?$limit=1

```
{
  "error": true,
  "message": "You must be logged in to access this resource"
}
```
The exploit chain:

I matched column types, built the UNION query, and sent it:

$query=(select 'a','b','c','d','e','f','g','h','i','j')

UNION (select col1,col2,col3,col4,col5,col6,col7,col8,col9,''

from @unpublished-copy limit 1)

HTTP 200. Data from the restricted dataset sitting right there in the JSON response. Titles, phone numbers, locations, descriptions. All from a dataset that tells you to log in when you try to access it normally.

I almost walked away from this more times than I want to admit. At multiple points during the engagement, I had “injection confirmed, but no exploitable impact”:

Each one of those felt like the end of the road. The finding came from not accepting any of them as the final answer. UNION was hiding in a parser error message. The @ syntax was hiding in Socrata's federation layer. The bypass was hiding in an unpublished dataset's redirect chain.

[GitHub - clarkvoss/soqli\_hunter: A semi-interactive SoQL injection testing toolkit](https://github.com/clarkvoss/soqli_hunter)

I open sourced soqli\_hunter since nothing else exists for this attack surface. 138 payloads, batch and interactive modes, raw Burp request file support, the ::boolean error extraction technique, UNION injection, @ cross-dataset federation, and a dataset scanner that automates the entire redirect bypass detection chain.

\# Confirm, fingerprint, and scan for cross-dataset bypasses

python soqli\_hunter.py -r request.txt --batch --confirm --fingerprint --technique D

\# Error-based extraction

python soqli\_hunter.py -r request.txt --batch --extract "column\_name" \

--extract-method error\_cast --chunk-size 50

I also published a set of Nuclei templates for detecting Socrata endpoints and confirming SoQL injection at scale. Both are on my GitHub.

[GitHub - clarkvoss/Socrata-SoQL-Injection: Socrata SoQL Injection Nuclei Templates](https://github.com/clarkvoss/Socrata-SoQL-Injection)

If you run into a Socrata endpoint on an engagement, these tools will save you the weeks I spent figuring this out.

The injection itself was trivial. Arithmetic in a query parameter. The hard part was turning it into impact when every standard technique was blocked by the SoQL layer.

Error messages were the roadmap the whole way through. The parser grammar leak that revealed UNION, the column mismatch errors that leaked schemas, the internal dataset identifiers that exposed the redirect chain. If the application is going to tell you exactly what it expects, read what it says.

Abstraction layers don’t just block attacks. They create new ones. The SoQL typechecker is solid at blocking Postgres functions. But it lets UNION through, it lets @ cross-dataset references through, and the query coordinator follows redirects without rechecking auth. The vulnerability isn't in any single layer. It's in the gaps between them.

And sometimes the only difference between “confirmed but not exploitable” and a real finding is refusing to stop.

So go out there and **find some bugs!** If I can, so can you. Hope you enjoyed reading this!
