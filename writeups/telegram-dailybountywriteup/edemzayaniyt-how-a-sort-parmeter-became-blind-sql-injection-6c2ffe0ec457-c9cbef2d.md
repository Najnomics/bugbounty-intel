# How a Sort Parmeter Became Blind SQL Injection

- **Source URL:** https://medium.com/@edemzayaniyt/how-a-sort-parmeter-became-blind-sql-injection-6c2ffe0ec457
- **Fetched from:** https://medium.com/@edemzayaniyt/how-a-sort-parmeter-became-blind-sql-injection-6c2ffe0ec457?source=rss-e09ff558ed9c------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:**  (id 14910)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** Adem_Zayani / Sun, 13 Sep 2026 20:50:54 GMT

Hello everyone 👋

While testing a web application in scope for a private program, I came across a REST API endpoint used to return a list of records (counties, in this case). Nothing fancy — just a simple “get all” endpoint with two query parameters:

GET https://\[REDACTED\].com/wp-json/counties/v1/all?sort\_by=CountyName&sort\_dir=asc

At first glance it looked completely harmless , a sort parameter .But I wanted to see what the backend actually did with it.

I started by confirming that sort\_by genuinely controlled the ordering of the response, using two legitimate values.

sort\_by=CountyName  → first record: Appling County

sort\_by=CountyID → first record: Bartow County

Two different, predictable orderings. That told me the value was being used directly to build the query — which made me want to test whether it was being validated at all.

So instead of a real column name, I sent a SQL expression:

sort\_by=(CASE WHEN 1=1 THEN CountyName ELSE CountyID END)

The response came back ordered by CountyName.

Then I flipped the condition:

sort\_by=(CASE WHEN 1=2 THEN CountyName ELSE CountyID END)

This time it came back ordered by CountyID.

That was the confirmation. The database was evaluating my CASE WHEN expression directly , no authentication, no sanitization — just raw SQL injection in the ORDER BY clause.

At this point I had a working boolean oracle: depending on whether my condition was true or false, the response ordering flipped between two known states. That’s enough to ask the database anything, one true/false question at a time.

Using LENGTH() and ASCII(SUBSTRING(...)) inside the same CASE WHEN, I extracted real values character by character:

sort\_by=(CASE WHEN (LENGTH(DATABASE())=14) THEN CountyName ELSE CountyID END)

sort\_by=(CASE WHEN (ASCII(SUBSTRING(DATABASE(),1,1))=119) THEN CountyName ELSE CountyID END)

Repeating this for each position, I was able to recover:

Item value database name\[REDACTED\]Current DB user\[REDACTED\]@127.0.0.1DB server hostname\[REDACTED\]Total tables in schema 155 Users tablewp\_users (confirmed to exist) User account count 71

All of it, unauthenticated.

The root cause was simple : the sort\_by value was being concatenated straight into the SQL ORDER BY clause with no allowlist and no validation.

The application effectively trusted:

sort\_by=\<anything the client sends>

instead of checking:

Is this one of the columns we actually allow sorting by?

Prepared statements don’t help here — you can parameterize a *value*, but not a column name or expression. Without an explicit allowlist, anything goes.

The Attack Flow

Send a normal request with a known sort\_by value

↓

Confirm the ordering changes as expected

↓

Replace sort\_by with a CASE WHEN boolean expression

↓

Observe which ordering comes back

↓

Use that as a true/false oracle

↓

Extract data character-by-character with LENGTH() / ASCII(SUBSTRING())

↓

Automate it

I ended up scripting the whole extraction (Python and PowerShell versions) so the triage team could reproduce it themselves without trusting a wall of manual curl commands.

This gave an unauthenticated attacker a reliable SQL injection primitive against the production database, with no rate limiting slowing it down. In practice that meant:

No login, no session, no prior access required — just the endpoint and a query string.

I reported the vulnerability through HackerOne to the responsible program. It was validated, escalated to Critical severity, and the fix was later confirmed via retest — the report is now closed as Resolved.

I’m sharing this write-up for educational purposes, to show how something as small and overlooked as a sort parameter can turn into a full unauthenticated database extraction primitive when input isn’t validated against an allowlist.
