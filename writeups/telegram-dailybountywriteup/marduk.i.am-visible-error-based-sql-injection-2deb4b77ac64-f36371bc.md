# Visible Error-Based SQL Injection

- **Source URL:** https://medium.com/@marduk.i.am/visible-error-based-sql-injection-2deb4b77ac64?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20251127091204/https://medium.com/@marduk.i.am/visible-error-based-sql-injection-2deb4b77ac64
- **Fetched:** 2026-11-19
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/11198 (id 11198)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Visible Error-Based SQL Injection

## A Portswigger Lab

### [Lab Description:](https://portswigger.net/web-security/sql-injection/blind/lab-sql-injection-visible-error-based)

This lab contains a SQL injection vulnerability. The application uses a tracking cookie for analytics, and performs a SQL query containing the value of the submitted cookie. The results of the SQL query are not returned.

The database contains a different table called *users*, with columns called *username* and *password*. To solve the lab, find a way to leak the password for the *administrator* user, then log in to their account.

- **NOTE:** I will be using [*Burpsuite Community Edition*](https://portswigger.net/burp/communitydownload) to help complete this lab, so you may want to have that up and running. If you’re not sure what Burp is or how to use it, check out this tutorial: [*Burpsuite Basics (FREE Community Edition)*](https://www.youtube.com/watch?v=G3hpAeoZ4ek&t=296s&pp=ygUbQnVycHN1aXRlIENvbW11bml0eSBFZGl0aW9u) by John Hammond.

## Getting Started:

Visible error-based SQLi occurs when your injected payload causes the database to raise an error and the application returns that error text to you.

The returned error often contains useful information (table/column names, type errors, function outputs) that you can use to enumerate schema or leak data.

Returning raw database errors to users can result in an information-disclosure vulnerability. Production apps should surface only a generic error message to users, like ‘*500 Internal Server Error*’, and record full details in server-side logs.

Let’s see what our lab is returning.

With Burp running, accessing the lab will return you to the lab’s shopping page. Click on the ‘*My account*’ link to make sure the ‘*TrackingID*’ cookie is set. We’ll need that page later to solve the lab.

Highlight the ‘/’ GET request in Burp’s target site map. You will notice the vulnerable tracking cookie.

Right-click on your request and select ‘*Send to Repeater*’. In Repeater, you will see your original request. Click ‘*Send*’, then click the ‘*Render*’ tab to view the response rendered as a web page.

From here we can manipulate the ‘*TrackingID*’ cookie to see how the server will respond.

## Crafting Payloads:

Inject a single quote ( ‘ ) at the end of your ‘*TrackingID*’ cookie and click ‘*Send*’. Notice the lengthy error response.

The server responded with the exact query it tried to use. Notice the two single quotes at the end (*…Z’’*). That shows our injected single quote ended the original string and left an unmatched quote, producing an *unterminated string literal*.

Let’s comment out everything after the single quote by using a double hyphen.

The page should load normally. This demonstrates the cookie is being concatenated into a quoted SQL string and confirms a string-context SQL injection.

Next we need to use CAST and a generic SELECT subquery. CAST is a **standard SQL function** used to convert a value from one data type to another.

```
-- Payload
your-trackingid-cookie' AND CAST((SELECT 1) AS int) --
```
Casting is useful when you need to force a particular type, or to trigger type-related behavior or errors. This will come into play later.

Append our payload to the end of your ‘*TrackingID*’ cookie and click ‘*Send*’.

We get an error, *ERROR: argument of AND must be type boolean, not type integer Position: 63*. This is telling us that the AND operator requires a boolean expression.

To fix this we need to add a simple comparison operator (=) before the CAST function.

```
-- Modified payload
your-trackingid-cookie' AND 1=CAST((SELECT 1) AS int) --
```
This is going to compare the results of our subquery to ‘1’. If it is true the page should load as normal. If it is false we should get an error.

As learned in the lab description there is a table called *users*, with columns called *username* and *password.* Let’s try to return usernames from the table users in our SELECT subquery.

```
-- Trying to retrieve usernames from the table users.
your-trackingid-cookie' AND 1=CAST((SELECT username FROM users) AS int) --
```
Append this payload to the end of your ‘*TrackingID*’ cookie and click ‘*Send*’.

Notice the server’s response shows the SQL query was truncated. This suggests the server enforces a maximum query length, so our full injected expression did not reach the database.

Let’s try reclaiming some space by deleting our ‘*TrackingID*’ cookie and clicking ‘*Send*’ again.

Removing the ‘*TrackingID*’ cookie worked. Our expression reached the server, but we are getting a different error message. This error is telling us it is returning too many rows at once.

## Lab Solution:

To fix this, let’s LIMIT our results to one row.

```
-- LIMIT results to just 1 row
' AND 1=CAST((SELECT username FROM users LIMIT 1) AS int) --
```
Add ‘LIMIT 1’ to your payload and resend your request.

The resulting error (*invalid input syntax for type integer: “administrator”*) indicates the database attempted to CAST the username string to an int(integer) and failed. The error also exposes the username value, demonstrating both a type-cast issue and an information disclosure vulnerability.

Now let’s try the same payload, however, instead of ‘*username*’, let’s use ‘*password*’.

```
-- Final payload
' AND 1=CAST((SELECT password FROM users LIMIT 1) AS int) --
```
Replace ‘*username*’ with ‘*password*’ and click ‘*Send*’.

We now have the administator’s password. If you want to copy it to your clipboard you will need to click on the ‘*Pretty*’ tab, on the response side, and scroll down.

All that’s left to do now is paste your find into the log in page of the lab and click ‘*Log in*’.

Congratulations! You are ‘administrator’.

Great work! Keep it up!

See you next time! Happy hacking!

### Previous Lab:

[Blind SQL Injection with Conditional Errors](/@marduk.i.am/blind-sql-injection-with-conditional-errors-7850fe9bc73b)

### Up Next:

Blind SQL Injection with Time Delays
