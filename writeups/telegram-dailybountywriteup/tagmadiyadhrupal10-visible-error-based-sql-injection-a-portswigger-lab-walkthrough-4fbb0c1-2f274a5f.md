# Visible Error-Based SQL Injection

- **Source URL:** https://medium.com/@tagmadiyadhrupal10/visible-error-based-sql-injection-a-portswigger-lab-walkthrough-4fbb0c13d9cf
- **Fetched from:** https://medium.com/@tagmadiyadhrupal10/visible-error-based-sql-injection-a-portswigger-lab-walkthrough-4fbb0c13d9cf?source=rss-a8e2bb93853a------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:**  (id 14942)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** Dhrupal Tagmadiya / Sun, 11 Oct 2026 06:44:27 GMT

*Learning how SQL errors can become an information-disclosure channel.*

In this PortSwigger Web Security Academy lab, the objective was to exploit a visible error-based SQL injection vulnerability to retrieve the administrator’s password and log in to the administrator account.

In this technique, the application does not need to display database query results directly. Instead, verbose database error messages can reveal useful information about the query or its data.

In this write-up, I will explain how I identified the injection point, what I initially tried, where I got stuck, and how I eventually understood the exploitation methodology.

I monitored the application traffic through **Proxy → HTTP history** to understand which requests were being sent to the server.

Initially, I tried to identify inputs that might interact with a database. While inspecting the requests, I noticed a cookie named TrackingId.

I decided to investigate this cookie rather than focusing only on visible form fields or URL parameters.

I modified its value by appending a single quote (') and sent the request again. The application returned an HTTP 500 Internal Server Error.

*Figure 1: The modified TrackingId cookie and the resulting HTTP 500 response.*

After examining the response body, I found a more informative error message indicating an unterminated SQL string literal. The error also revealed part of the SQL query being executed.

*Figure 2: The database error revealing the SQL query context and the unclosed string literal.*

This was my first important observation: the cookie value appeared to be inserted into a SQL query, and the database error was revealing information about how that query was constructed.

At this point, I had a promising injection point, but I still needed to understand how to retrieve information from the database.

After identifying TrackingId, I spent around 30 minutes investigating the possible injection point and trying to create a payload of my own.

My initial idea was to retrieve the administrator’s username and password directly from the users table.

However, my attempted payload did not work. I was trying to write a SELECT statement without fully understanding how my input fitted into the application’s existing SQL query.

Looking back, my attempt had several problems:

I also learned from the lab hints that the TrackingId input had a character limit, which could truncate a longer payload. Removing the original cookie value provided more space for the test expression.

Instead of continuing to guess, I decided to follow the hints one step at a time and understand why each change was necessary.

The first useful step was to understand the quotation marks and SQL comments.

A single quote could close the string in which the cookie value was being used. SQL comment syntax (--) could then comment out the remaining part of the original query.

This helped me understand how to produce a syntactically valid query rather than simply inserting an independent SQL statement.

The next challenge was retrieving useful information when the application did not directly display query results.

The lab guided me toward a PostgreSQL technique involving CAST().

The purpose of CAST(value AS int) is to convert a value to an integer. If the value is text that cannot be converted, PostgreSQL can return an error containing that value.

For example, attempting to convert the string administrator to an integer can produce an error that reveals the original string.

This became the key idea behind the lab: use a conversion error as an information-disclosure channel.

The hints also helped me understand that the expression needed to fit the surrounding Boolean condition. A comparison such as 1 = CAST(...) produces a Boolean result, whereas the CAST() expression by itself produces an integer.

Instead of jumping directly to the administrator’s credentials, I first needed to validate the query structure using a simple subquery and then adapt it to retrieve actual database values.

Once I understood the technique, I replaced the simple test value with a subquery that retrieved a username from the users table.

The important observation was that a subquery used as a single value should return one row. The LIMIT 1 clause helped restrict the result to a single row.

When I sent the modified request, the database error revealed the username administrator.

*Figure 3: The integer-conversion error reveals the administrator’s username.*

This was an important turning point. I was no longer simply triggering an SQL error; I was using the error message to retrieve information from the database.

After identifying the administrator’s username, I applied the same principle to the password column.

The underlying technique remained the same. The subquery retrieved a different value, and the integer conversion failed, exposing that value through the database error.

*Figure 4: The modified query retrieves the password value through the database error.*

With the retrieved credentials, I logged in as the administrator and successfully completed the lab.

The observed behavior suggests that the application incorporates client-controlled cookie input into a SQL query without safely separating data from SQL syntax. This allows specially crafted input to influence query execution.

The detailed database errors make the situation worse by exposing information that the application should not disclose to users.

The main remediation measures are:

Simply hiding error messages is not enough to fix the underlying SQL injection vulnerability.

This lab taught me several lessons.

**First, injection-point discovery is only the beginning.** Finding a suspicious parameter does not automatically mean I understand how to exploit it.

**Second, the surrounding SQL context matters.** Quotation marks, comments, Boolean expressions, return types, and subquery results all affect whether a payload works.

**Third, errors can become an information channel.** Even when an application does not display query results directly, its error messages may reveal sensitive information.

**Finally, hints are more useful when I understand the reason behind each step.** I initially struggled because I was trying to construct a complete payload before validating the individual parts. Breaking the problem into smaller tests helped me understand the technique.

This lab demonstrated how a vulnerable cookie parameter and verbose database errors could be combined to retrieve database information and ultimately access an administrator account.

Although I did not solve the lab independently on my first attempt, working through the hints helped me understand the reasoning behind the exploitation process.

My biggest takeaway is that SQL injection is not just about memorizing payloads. It is about understanding the SQL context, forming a hypothesis, testing it systematically, and learning from the server’s response.

**Keep learning, keep testing , and happy hacking!**
