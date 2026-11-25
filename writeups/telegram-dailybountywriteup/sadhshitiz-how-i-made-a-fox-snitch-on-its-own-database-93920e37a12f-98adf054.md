# How I Made a Fox Snitch on Its Own Database

- **Source URL:** https://medium.com/@sadhshitiz/how-i-made-a-fox-snitch-on-its-own-database-93920e37a12f
- **Fetched from:** https://medium.com/@sadhshitiz/how-i-made-a-fox-snitch-on-its-own-database-93920e37a12f?source=rss-7a7e9b29bbac------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14927 (id 14927)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** Sadhshitiz / Tue, 29 Sep 2026 04:31:03 GMT

***Challenge:*** *Intigriti September Challenge*
***Target:*** *challenge-0926.challenges.intigriti.io*
***Vulnerability:*** *Unauthenticated UNION-based SQL Injection*
***Parameter:*** *pic*

I was looking at an endpoint that seemed pretty harmless:

GET /challenge.php?pic=Zm94

The application decodes Zm94 → fox, looks up some information about the animal, and returns a cute little fox description.

Nothing suspicious, right?

Well…

**I saw the word base64 and immediately became suspicious.**

Because sometimes in bug hunting, you don’t find the vulnerability.

**The vulnerability finds you.**

The application was taking the decoded value and concatenating it directly into a SQL query.

No parameterized queries.

No proper input sanitization.

No escaping.

Just:

**“Here you go, database. Please don’t do anything stupid.”**

The database, unfortunately, did something stupid.

The endpoint looked something like this:

Where:

Zm94 → fox

The response contained the description for the fox.

At first glance, the interesting part was the Base64 encoding.

Now, Base64 itself isn’t a security vulnerability.

But when I see user-controlled data being encoded/decoded before reaching an application sink, I like to ask one question:

***“What happens after it gets decoded?”***

So instead of looking at the Base64 string, I started thinking about the decoded input.

Time to poke the application.

I started with the usual Boolean-based SQL injection tests.

I simply encoded my SQL payloads in Base64 and sent them through the pic parameter.

Decoded input:

fox' AND '1'='1

Result:

✅ Fox description rendered normally.

fox' AND '1'='2

❌

No critter goes by that name yet.

That’s interesting.

The application behaves differently depending on whether my SQL condition evaluates to true or false.

And then came the classic:

fox'

The response was:

💀 Empty 200 OK.

The application wasn’t throwing a nice SQL error at me.

Instead, the error was apparently being swallowed.

Which is fine.

**I don’t need an error message if the application itself is willing to become my Boolean oracle.**

At this point, I had a pretty good indication that my input was reaching a SQL query.

Next, I wanted to figure out the number of columns being returned.

So I tried:

fox' ORDER BY 1-- -

✅ Works.

Then:

fox' ORDER BY 2-- -

❌ Empty response.

So we appear to have:

**One column.**

One beautiful, lonely column.

And that’s exactly what I needed for a UNION-based attack.

Its happning….

Now came the fun part.

I wanted to know whether I could inject my own data into the response.

nonexistent' UNION SELECT 'flagtest'-- -

And…

There it was.

The application’s .desc field rendered:

flagtest

At this point, the application wasn’t really giving me fox facts anymore.

**It was giving me whatever I asked the database to give me.**

That’s generally not a great feature for an application to have.

Since we had UNION-based output, the next logical step was schema enumeration.

I pivoted to information\_schema and used GROUP\_CONCAT to make the database list its own furniture.

The database responded with:

animals

secret\_vault

And honestly…

secret\_vault

is probably the least subtle table name I’ve ever seen.

It’s basically the SQL equivalent of putting:

***DO NOT OPEN THIS DRAWER***

on a drawer.

Obviously, I had to open the drawer.

Next, I enumerated the columns:

id

note

So we had:

secret\_vault

├── id

└── note

Now the question was simple:

**Can I actually retrieve the contents?**

I sent:

nonexistent' UNION SELECT GROUP\_CONCAT(note SEPARATOR '|') FROM secret\_vault-- -

And the application happily rendered:

`INTIGRITI{01a09f56-74a2-700b-a849-ffe6742327b2}`
And just like that…

🦊 **The fox had spilled the secrets.**

Let’s recap the attack chain.

The application effectively allowed this:

User input

↓

Base64 decoding

↓

SQL query construction

↓

User-controlled SQL

↓

UNION injection

↓

information\_schema

↓

secret\_vault

↓

flag

All of this happened without authentication.

And the final result was reflected directly into the page.

No blind timing attack.

No complicated exploitation chain.

No authentication.

No session required.

Just a browser, some carefully crafted SQL, and a Base64 encoder.

The vulnerability allows an unauthenticated attacker to perform UNION-based SQL injection through the pic parameter.

From my testing, I was able to:

The important part here is that the attacker does **not** need an account.

That’s what takes this from:

*“Hmm, interesting SQL bug.”*

to:

***“Yeah… someone should probably fix this.”***

The final decoded payload was:

Base64 encoded:

bm9uZXhpc3RlbnQnIFVOSU9OIFNFTEVDVCBHUk9VUF9DT05DQVQobm90ZSBTRVBBUkFUT1IgJ3wnKSBGUk9NIHNlY3JldF92YXVsdC0tIC0=

Which ultimately returned the flag

All testing was performed against the intended challenge environment.

I kept the exploitation read-only and limited to SELECT-based queries used to demonstrate the vulnerability.

I did **not**:

The goal was simply to demonstrate that the SQL injection could be used to retrieve database contents.

This was a good reminder that **encoding is not sanitization**.

Base64 doesn’t make SQL injection disappear.

It just makes the payload look prettier.

If an application does something conceptually similar to:

$input = base64\_decode($\_GET\['pic'\]);

$query = "SELECT description FROM animals WHERE name = '$input'";

then the Base64 layer isn’t providing any meaningful SQL injection protection.

The database doesn’t care whether your malicious input arrived looking like:

fox' UNION SELECT ...

or:

Zm94JyBVTklPTiBTRUxFQ1QgLi4u

Eventually, it gets decoded.

And if that decoded value is concatenated into SQL…

**Congratulations, you’ve just given the fox a database account.**

What started as:

"Let's see what this pic parameter does."

ended with:

"Why is there a table called secret\_vault?"

and eventually:

"WHY DOES THE FOX KNOW THE FLAG?"

The actual lesson isn’t that Base64 is bad.

It isn’t.

The problem is trusting decoded user input and inserting it directly into a SQL query.

Use parameterized queries / prepared statements.

Validate input where appropriate.

And don’t rely on encoding as a security boundary.

Because if your application’s security model is:

***“The attacker probably won’t decode the Base64.”***

…I’m afraid I have some bad news for you.

**If your application decodes Base64 and glues the result directly into a SQL query, the fox isn’t the one you should be worried about guarding the henhouse.**

Happy hunting. 🫡

*And remember: sometimes the most interesting endpoint is the one that looks completely boring.*

TestResultfox' AND '1'='1Fox description returnedfox' AND '1'='2"No critter goes by that name yet."fox'Empty 200 OKfox' ORDER BY 1-- -Worksfox' ORDER BY 2-- -Emptynonexistent' UNION SELECT 'flagtest'-- -flagtest reflectedGROUP\_CONCAT(...) FROM secret\_vaultSecret value extracted
