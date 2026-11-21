# SQL Injection UNION Attack, Retrieving Data from Other Tables

- **Source URL:** https://medium.com/@marduk.i.am/sql-injection-union-attack-retrieving-data-from-other-tables-38f471813c57?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250920201306/https://medium.com/@marduk.i.am/sql-injection-union-attack-retrieving-data-from-other-tables-38f471813c57
- **Fetched:** 2026-11-21
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/7852 (id 7852)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# SQL Injection UNION Attack, Retrieving Data from Other Tables

## A Portswigger lab

### Lab Description:

This lab contains a SQL injection vulnerability in the product category filter. The results from the query are returned in the application’s response, so you can use a UNION attack to retrieve data from other tables. To construct such an attack, you need to combine some of the techniques you learned in previous labs.

The database contains a different table called *users*, with columns called *username* and *password*.

To solve the lab, perform a SQL injection UNION attack that retrieves all usernames and passwords, and use the information to log in as the *administrator* user.

- **HINT** — You can find some useful payloads on the [***SQL injection cheat sheet***](https://portswigger.net/web-security/sql-injection/cheat-sheet).
- **NOTE:** I will be using [*Burpsuite Community Edition*](https://portswigger.net/burp/communitydownload) to help complete this lab, so you may want to have that up and running. If you’re not sure what Burp is or how to use it, check out this tutorial: [*Burpsuite Basics (FREE Community Edition)*](https://www.youtube.com/watch?v=G3hpAeoZ4ek&t=296s&pp=ygUbQnVycHN1aXRlIENvbW11bml0eSBFZGl0aW9u) by John Hammond.

## Getting Started:

This lab is the third in a series of labs designed to help us understand the process of using ‘*a UNION attack to retrieve data from other tables*”.

In the [***first lab***](/@marduk.i.am/sql-injection-union-attack-determining-the-number-of-columns-returned-by-the-query-a740b76989fe) we learned a method of determining the correct number of columns that a site’s database is using.

In the [***second lab***](/@marduk.i.am/sql-injection-union-attack-finding-a-column-containing-text-ee28ff48eb30) we learned how to determine which column or columns are compatible with string data.

We will also be using techniques used in the lab ‘[***SQL Injection Attack, Listing the Database Contents on Non-Oracle Databases***](/@marduk.i.am/sql-injection-attack-listing-the-database-contents-on-non-oracle-databases-825485566585)’, to determine what type of database the site is using.

In order to solve this lab we need to sign into the administrator’s account using credentials found in the site’s vulnerable database. In order to do that we will:

- Verify the existence of a SQLi vulnerability.
- Determine the correct number of columns used in the database.
- Determine which columns are compatible with string data.
- Determine the type of database being used.
- Find the relevant table and column names.
- Extract credentials used for ‘administrator’.
- Log into the administrator’s account

### #1 — Verify the existence of a SQLi vulnerability.

Let’s get started. Access the lab. The SQLi vulnerability is in the site’s product category filter. Choose anyone you like, I chose ‘Gifts’ this time.

After selecting your filter, head over to Burp and find your request in the target site map on the left-hand side.

Right-click on your request and select ‘Send to Repeater’.

In the Repeater tab you can see your original request on the left-hand side and if you click ‘Send’ you will see the original ‘200 OK’ response.

In Burp Repeater, we can alter and send the request multiple times and see how this affects the response.

Let’s start by seeing if we are in the right spot for a SQLi. In the GET request, replace your product filter with a single quote ( ‘ ) and click ‘Send’. If the server is processing the single quote correctly we will get a ‘200 OK’ response.

Instead, we get a ‘500 Internal Server Error’, meaning this site may be vulnerable to a SQLi attack.

## Crafting Our Payloads:

Determining whether a site is vulnerable to SQL injection can vary across sites and often requires experimentation. You may need to test different approaches and gather information gradually, which can be time-consuming

### #2 — Determine the correct number of columns used in the database.

Using the technique learned in the lab ‘[*SQL Injection UNION Attack, Determining the Number of Columns Returned by the Query*](/@marduk.i.am/sql-injection-attack-listing-the-database-contents-on-non-oracle-databases-825485566585)’, we will figure out the number of columns this database is using.

Looking at the lab’s page, you will notice the site lists a number of product and their descriptions. We should start by guessing two columns. Let’s check by using the following:

```
-- Original payload
' UNION SELECT NULL, NULL --
-- URL encoded payload
'+UNION+SELECT+NULL,+NULL+--
```
- **NOTE** — Be sure to apply URL encoding to your payload before sending your request. Burp makes URL encoding easy, it can be done several ways. I usually highlight my payload and hit ‘Ctrl+u’.

Replace your single quote with our UNION SELECT payload and click ‘Send’.

Looks like we guessed correctly. We got a ‘200 OK’ response. If the database had more or less than two columns, we would have received a ‘500’ response.

### #3 — Determine which columns are compatible with string data.

Next we need to determine which of the columns are compatible with string data. We can do this by injecting our own strings onto the web page.

In your payload, replace the NULL columns with strings wrapped in single quotes. These can be anything you choose, like ‘abc’ and ‘def’.

```
-- Our payload
' UNION SELECT 'M4rduk', 'James' --
-- URL encoded payload
'+UNION+SELECT+'M4rduk',+'James'+--
```
Replace the payloads and click ‘Send’.

Clicking on the ‘Render’ tab shows you the response as the web page. We can see our stings injected at the bottom of the page.

### #4 — Determine the type of database being used.

A few labs back, I published one called ‘[*SQL Injection Attack, Listing the Database Contents on Non-Oracle Databases*](/@marduk.i.am/sql-injection-attack-listing-the-database-contents-on-non-oracle-databases-825485566585)’. In there I walk through how to determine the type and the version of the database a server is using.

You can reference that lab for a more in depth explanation of determining the type and version of a database.

Here we will be using the Portswigger provided [***cheat sheet***](https://portswigger.net/web-security/sql-injection/cheat-sheet). Scroll down to the ‘Database version’ section.

We are going to be using the commands for PostgreSQL. The ‘version()’ will take the place of one of your strings.

We need to modify this command a little for our needs.

```
-- Original payload
SELECT version()
-- Our payload
' UNION SELECT version(), 'M4rduk' --
-- URL encoded payload
'+UNION+SELECT+version(),+'M4rduk'+--
```
- **NOTE** — I knew it wasn’t an Oracle database because I didn’t need a ‘FROM dual’ while we injected our strings onto the page.
- I knew this was not a MySQL database because we didn’t require an extra space after our double hyphen or comment out.
- I tried the ‘@@version’ for Microsoft databases first, but I got a ‘500’ error.

Knowing the database type and version used by a server is valuable when crafting an attack, as different databases have unique query syntax and subtle variations in behavior.

### #5— Find the relevant table and column names.

Refer back to the *cheat sheet****.*** This time look at the ‘Database contents’ section.

Since we are querying a PostgreSQL database we will be using the following two commands:

- `SELECT * FROM information_schema.tables`
- `SELECT * FROM information_schema.columns WHERE table_name = 'TABLE-NAME-HERE'`

The first command helps us identify the tables in the database, while the second provides details on the columns within a specific table.

The ‘*information\_schema.tables*’ is part of the ‘*information\_schema’* schema, a special schema that stores details about the database structure.

We can not use the commands, as is, because we are using a UNION SELECT statement the number of columns used has to match exactly. Instead of an asterisk (\*) we need to specify two columns.

One column can be one of our strings from earlier, or NULL. The other is going to be what we are looking for from ‘*information\_schema’.* The table names.

If you Google ‘PostgreSQL information\_schema’, the first result should lead you [***here***](https://www.postgresql.org/docs/current/information-schema.html). Scroll down until you find ‘Tables’ (35.54) and click on the link.

The SQL identifier ‘*table\_name*’ will be our other column. SQL identifiers are names used to reference database objects like tables, columns, schemas, and other entities.

```
-- Original payload
SELECT * FROM information_schema.tables
--Our payload
' UNION SELECT table_name, NULL FROM information_schema.tables --
-- URL encoded payload
'+UNION+SELECT+table_name,+NULL+FROM+information_schema.tables+--
```
Send your payload to view all the table names contained in this database.

We found our table ‘*users*’, now let’s find what columns are in that table.

Refer back to the ‘Database contents’ section of the [***cheat sheet***](https://portswigger.net/web-security/sql-injection/cheat-sheet).

Again, we can not use this command until we modify it a little.

Head back over to the [*postgresql.org*](https://www.postgresql.org/docs/current/information-schema.html) site we found and scroll down to find ‘*columns*’ (35.17). Click on it. This will give us the identifier we are looking for.

Now to modify the original command. Add ‘*column\_name*’ and *NULL* for your columns and replace ‘TABLE\_NAME\_HERE’ with ‘*users*’.

```
-- Original payload
SELECT * FROM information_schema.columns WHERE table_name = 'TABLE-NAME-HERE'
--Our payload
' UNION SELECT column_name, NULL FROM information_schema.columns WHERE table_name = 'users' --
-- URL encoded payload
'+UNION+SELECT+column_name,+NULL+FROM+information_schema.columns+WHERE+table_name+%3d+'users'+--
```
Here we are asking ‘*information\_schema.columns*’ to give us all the column names where the table name is equal to ‘*users’*.

The server will return the column names we need from the table ‘*users*’.

## Lab Solution:

All that is left to do is craft a simple query with the information that we have gathered.

### #6 — Extract credentials used for ‘administrator’.

Now with a simple query we can select the username and password columns from the users table.

```
-- Original payload
' UNION SELECT username, password FROM users --
-- URL encoded payload
'+UNION+SELECT+username,+password+FROM+users+--
```
Add this final payload to your GET request and click ‘Send’.

### #7 — Log into the administrator’s account.

Take the found credentials and head over to the log on page for the lab. Click on ‘*My account*’.

Use our newly obtained credentials to log in as administrator.

Congratulations! You solved another one! Keep up the great work!

See you next time!

### Up Next:

SQL Injection UNION Attack, Retrieving Multiple Values in a Single Column

### Previous Lab:

[SQL Injection UNION Attack, Finding a Column Containing Text](/@marduk.i.am/sql-injection-union-attack-finding-a-column-containing-text-ee28ff48eb30)
