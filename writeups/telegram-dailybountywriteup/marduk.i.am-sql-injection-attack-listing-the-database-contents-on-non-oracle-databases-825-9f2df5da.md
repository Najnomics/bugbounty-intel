# SQL Injection Attack, Listing the Database Contents on Non-Oracle Databases

- **Source URL:** https://medium.com/@marduk.i.am/sql-injection-attack-listing-the-database-contents-on-non-oracle-databases-825485566585?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20251005114956/https://medium.com/@marduk.i.am/sql-injection-attack-listing-the-database-contents-on-non-oracle-databases-825485566585
- **Fetched:** 2026-11-22
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/7218 (id 7218)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# SQL Injection Attack, Listing the Database Contents on Non-Oracle Databases

## A Portswigger Lab

### [**Lab Description**](https://portswigger.net/web-security/sql-injection/examining-the-database/lab-listing-database-contents-non-oracle)**:**

This lab contains a SQL injection vulnerability in the product category filter. The results from the query are returned in the application’s response so you can use a UNION attack to retrieve data from other tables.

The application has a login function, and the database contains a table that holds usernames and passwords. You need to determine the name of this table and the columns it contains, then retrieve the contents of the table to obtain the username and password of all users.

To solve the lab, log in as the administrator user.

- Hint — You can find some useful payloads on our [***SQL injection cheat sheet***](https://portswigger.net/web-security/sql-injection/cheat-sheet).
- **NOTE:** I will be using [*Burpsuite Community Edition*](https://portswigger.net/burp/communitydownload) to help complete this lab, so you may want to have that up and running. If you’re not sure what Burp is or how to use it, check out this tutorial: [*Burpsuite Basics (FREE Community Edition)*](https://www.youtube.com/watch?v=G3hpAeoZ4ek&t=296s&pp=ygUbQnVycHN1aXRlIENvbW11bml0eSBFZGl0aW9u) by John Hammond.

## Getting Started:

This is a good lab. We know, from the lab description, there is a SQL injection (SQLi) vulnerability in the product category filter and that the database IS NOT Oracle. That’s it.

First, let’s create a list of what we need to accomplish in order to solve this lab.

1. Verify SQLi vulnerability injection point.
2. Determine the exact number of columns AND data types.
3. Determine the type of database that is being used.
4. Determine the relevant table name within that database.
5. Determine the relevant column names within the table.
6. Find credentials for ‘administrator’.
7. Log in to the site as ‘administrator’.

Start by accessing the lab with Burpsuite running. We are brought to our familiar shopping page with multiple products. We are looking for our SQL injection point, which is in the product category filters. Select anyone you like.

After selecting a filter, head over to Burp and find your filter selection in the site map of the ‘Target’ tab.

Right-click on your filter and select ‘Send to Repeater’. Repeater will allow us to alter and send multiple requests to the target.

Click on the Repeater tab and your request should be there on the left-hand side. If you click send, you will get a ‘200 OK’ response in the right-hand column. This is the way it is supposed to work.

Now, let’s check to see if this is where our SQLi vulnerability is by appending a single quote (‘) to the end of the filter and clicking ‘Send’ again. This is number 1 on our to do list.

You should get a ‘500 Internal Server Error’ meaning that the server may be susceptible to a SQLi attack.

Number 2 on our to do list in to find out how many columns are going to be in our database. In order to use a ‘UNION SELECT’ attack the number of columns AND the data types must match exactly.

The information displayed on the site should give a clue as to how many columns there are. Like before, there is a product listing and it’s description. Both are text data types, but let’s see how we verify this.

In Burp Repeater, add the following, original payload, to your GET request:

```
-- Original payload
' ORDER BY 1 --
-- URL encoded
'+ORDER+BY+1+--
```
Before hitting ‘Send’ make sure to URL encode your payload. You can easily do this in Burp by highlighting your payload and hitting Ctrl+u. The top line of your GET request should look something like:

`GET /filter?category=Pets'+ORDER+BY+1+-- HTTP/2`
This payload is telling the server to order the results by column 1, if there is a column 1. A ‘200 OK’ response tells us that there is indeed 1 column.

Now change the payload to order the results by column 2. You should get the same ‘200 OK’ response telling us that, yes, there is 2 columns in this database.

```
-- Original payload
' ORDER BY 2--
-- URL encoded
'+ORDER+BY+2+--
```
We know there is at least two columns but what about three?

```
-- Original payload
' ORDER BY 3--
-- URL encoded
'+ORDER+BY+3+--
```
That ‘500 Internal Server Error’ is telling us that there is NOT a third column in this database.

Now that we know how many columns we are dealing with, let’s check to make sure the data types are ‘text’. To do this we are going to use a ‘UNION SELECT’ to inject strings onto the page.

```
-- Original payload
' UNION SELECT 'Marduk','James'--
-- URL encoded
'+UNION+SELECT+'Marduk','James'--
```
- **TIP** — If you only put the payload, not the filter + payload, you won’t get all the products and their descriptions. This will make it easier to read the response. I left the filter in, though, for this lab.

We have just verified that, one, this site IS susceptible to SQLi and, two, that the database here, has two columns that are type text. Let’s move on to the third step on our list.

## Crafting Our Payloads:

Now we need to verify what kind of database the site is using. All we know is that it is NOT Oracle. Open up the provided [*cheat sheet*](https://portswigger.net/web-security/sql-injection/cheat-sheet) and scroll down to the ‘Database version’ section.

Since we know this is not an Oracle database let’s start with Microsoft. You can not just send ‘SELECT @@version’ as your request. Remember we are doing a UNION SELECT and we have two columns. ‘@@version’ will be the first column but we still need that second column.

Replace one of your strings with ‘@@version’ and leave the other one. Instead of a string, the second column can just be ‘NULL’.

```
-- Original payload
' UNION SELECT @@version,'James'--
-- OR
' UNION SELECT @@version,NULL--
-- URL encoded
'+UNION+SELECT+%40%40version,'James'--
-- OR
'+UNION+SELECT+%40%40version,NULL--
```
Click send. If you get a ‘200 OK’ response that means we are dealing with a Microsoft database and in the response it will also show you the version of the database.

This is not the case. We got a 500 response telling us that this NOT a Microsoft database.

Let’s try PostgreSQL the same way.

```
-- Original payload
' UNION SELECT version(),'Marduk'--
-- URL encoded
'+UNION+SELECT+version(),'Marduk'--
```
We got it! A ‘200 OK’ response and the version of the database is displayed.

Next we need to have the server give us the names of all the tables within this database. Head back over the the [*cheat sheet*](https://portswigger.net/web-security/sql-injection/cheat-sheet) again and scroll to the ‘Database contents’ section.

Different databases contain subtle differences in the syntax used to make queries? This is why it is important to know which one you are dealing with.

Just like querying for the database version, here we also need to adjust this query to fit our UNION SELECT needs. We can’t ‘SELECT \*’(all) from the database. We have to specify what two columns we are looking for.

- **NOTE** — If you Google ‘PostgreSQL information\_schema.tables’, the first result should be: [https://www.postgresql.org/docs/current/infoschema-tables.html](https://www.postgresql.org/docs/current/infoschema-tables.html). Here you can find all you need on the information schema of PostgreSQL.

First, we are looking for the relevant table name. From the cheat sheet we will use the first one listed in the ‘Database contents’ for PostgreSQL.

```
-- Original
SELECT * FROM information_schema.tables
-- 2 columns, table_name and 'Marduk', take place of *
-- You can also use NULL instead of a string like 'Marduk'
' UNION SELECT table_name,'Marduk' FROM information_schema.tables--
-- URL encoded
'+UNION+SELECT+table_name,'Marduk'+FROM+information_schema.tables--
```
Sending this URL encoded query in your GET request should provide the list of all table names within that database.

Scroll down to find the relevant table. The table name will begin with ‘users\_’. The string of characters that follow will be random that will very from lab to lab. If your lab times out and you start a new one they will be different.

Now we took care of the fourth step, finding the table name. On to the fifth, finding the column names we need from that table.

From the cheat sheet we are going to use the second query for PostgreSQL.

```
-- Original
SELECT * FROM information_schema.columns WHERE table_name = 'TABLE-NAME-HERE'
-- 2 columns, column_name and 'Marduk', take place of *
-- You can also use NULL instead of a string like 'Marduk'
-- Remember to replace 'TABLE-NAME-HERE' with your exact table name
' UNION SELECT column_name,'Marduk' FROM information_schema.columns WHERE table_name = 'users_zqdiez'--
-- URL encoded
'+UNION+SELECT+column_name,'Marduk'+FROM+information_schema.columns+WHERE+table_name+%3d+'users_zqdiez'--
```
Send your Burp request again using your URL encoded query. The response will provide all the column names in that table.

Scroll down in the response to find your results. The column names you are searching for begin with ‘username\_’ and ‘password\_’. Just like with the table name, the ending string of characters will be randomized.

We have found the table name we need and also the column names. For step six all we need to do is a query those column names from that table.

## Lab Solution:

For our final query, plug in our column names and table name into a simple SELECT statement.

```
-- Simple SELECT query
SELECT * FROM table-name
-- Input our found info
-- Remember your column and table names will be different
' UNION SELECT username_zgglyq, password_wibgme FROM users_zqdiez--
-- URL encoded
'+UNION+SELECT+username_zgglyq,+password_wibgme+FROM+users_zqdiez--
```
This final query sent in Burp will provide you a list of all usernames and passwords found in that table.

Jackpot! We found the login credentials.

Head back to the lab and click on the ‘My account’ link in the upper right-hand corner. On the login page copy and paste your found credentials and click ‘Log in’.

We are now logged in as ‘administrator’!

Congratulations! You solved another one! Keep up the amazing work!

See you next time!
