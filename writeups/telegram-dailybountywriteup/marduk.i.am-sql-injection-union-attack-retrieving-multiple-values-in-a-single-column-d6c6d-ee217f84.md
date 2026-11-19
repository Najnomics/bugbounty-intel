# SQL Injection UNION Attack, Retrieving Multiple Values in a Single Column

- **Source URL:** https://medium.com/@marduk.i.am/sql-injection-union-attack-retrieving-multiple-values-in-a-single-column-d6c6d91be74d?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250913075534/https://medium.com/@marduk.i.am/sql-injection-union-attack-retrieving-multiple-values-in-a-single-column-d6c6d91be74d
- **Fetched:** 2026-11-19
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/9079 (id 9079)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# SQL Injection UNION Attack, Retrieving Multiple Values in a Single Column

## A Portswigger Lab

### [Lab Description](https://portswigger.net/web-security/sql-injection/union-attacks/lab-retrieve-multiple-values-in-single-column):

This lab contains a SQL injection vulnerability in the product category filter. The results from the query are returned in the application’s response so you can use a UNION attack to retrieve data from other tables.

The database contains a different table called *users*, with columns called *username* and *password*.

To solve the lab, perform a SQL injection UNION attack that retrieves all usernames and passwords, and use the information to log in as the *administrator* user.

- **HINT** — You can find some useful payloads on our [***SQL injection cheat sheet***](https://portswigger.net/web-security/sql-injection/cheat-sheet).
- **NOTE:** I will be using [*Burpsuite Community Edition*](https://portswigger.net/burp/communitydownload) to help complete this lab, so you may want to have that up and running. If you’re not sure what Burp is or how to use it, check out this tutorial: [*Burpsuite Basics (FREE Community Edition)*](https://www.youtube.com/watch?v=G3hpAeoZ4ek&t=296s&pp=ygUbQnVycHN1aXRlIENvbW11bml0eSBFZGl0aW9u) by John Hammond.

## Getting Started:

In this lab, we’ll build on what we learned in the previous labs to find and use the administrator’s credentials to log into their account. While the task is similar — retrieving credentials — the method we’ll use here is slightly different.

Here’s the twist: the database table we’re targeting (*users*) has two columns: *username* and *password*. However, only one of the columns in the query result is compatible with text data. This means we can only retrieve either the username or the password at a time.

Lucky for us there is a workaround: **concatenation**. Concatenation is the process of joining strings together, and we’ll use it to combine the username and password into a single column. This way, we can retrieve both pieces of information at once.

In order to get to that point we are going to have to do the following:

- Verify the existence of a SQL injection point.
- Verify the number of columns in the database.
- Verify which column is compatible with text type data.
- Retrieve ‘username’ and ‘password’ from the ‘users’ table.
- Use retrieved credentials to log in as ‘administrator’.

Let’s dive in!

### #1 — Verify the existence of a SQL injection point.

When you access the lab, you’ll be taken to a shopping website. The SQL injection point is located in the product category filter, just like in the previous labs.

To begin, select a category from the filter — I chose ‘Pets’ for this example. After selecting a category, the website will display the relevant products, and you’ll be able to see the corresponding HTTP request in Burp Suite’s **Target Site Map**.

Next, right-click on the request and select ‘**Send to Repeater**’. Burp Repeater is a powerful tool that allows us to modify and resend HTTP requests, making it perfect for testing SQL injection vulnerabilities.

Now that the request is in Repeater, let’s test for a SQL injection vulnerability. Replace the product category filter value (Pets) with a single quote (‘) and click ‘**Send**’.

### #2 — Verify the number of columns in the database.

Now that we’ve confirmed the SQL injection point, the next step is to determine the number of columns being used by the database. To do this, we’ll use a UNION SELECT attack with NULL values. The idea is to start with one NULL and incrementally add more until the server returns a ‘200 OK’ response, indicating that the number of columns matches.

```
-- Here is how the payloads will look
' UNION SELECT NULL --
' UNION SELECT NULL, NULL --
' UNION SELECT NULL, NULL, NULL --
```
We’ll start with the first payload:

```
-- Our first payload
' UNION SELECT NULL --
-- URL encoded
'+UNION+SELECT+NULL+--
  -- OR
'%20UNION%20SELECT%20NULL%2c%20--
```
In Repeater, append our first payload, from above, to your GET request after the equal sign and click ‘**Send**’.

- **NOTE** — Do not forget to URL encode your payload before sending the request. Burp provides several ways to accomplish this. Highlighting the payload and hitting ‘Ctrl+u’ is the easiest. I’ll show another way later on.

If the server responds with a ‘500 Internal Server Error’, it means the number of columns in our payload (one) doesn’t match the number of columns in the database. This tells us there are more than one column.

Next, let’s try the payload with two NULL columns:

```
-- Our payload
' UNION SELECT NULL, NULL --
-- URL encoded
'+UNION+SELECT+NULL,+NULL+--
  -- OR
'%20UNION%20SELECT%20NULL%2c%20NULL%20--
```
Append this payload to your GET request and click Send.

This time, you should receive a ‘200 OK’ response, which confirms that the database has two columns.

### #3 — Verify which column is compatible with text type data.

Now that we know the database has two columns, the next step is to determine which column is compatible with text data.

When performing a UNION SELECT attack, not only do we need to know the number of columns, but the data types of those columns must also match the data we’re trying to extract (in this case, text).

To test this, we’ll replace the NULL values in our payload with a string (‘M4rduk’) and check the server’s response. We’ll do this one column at a time.

Let’s start by testing the first column. Replace the first NULL with a string of your choosing, keeping the second column as NULL:

```
-- Our payload
' UNION SELECT 'M4rduk', NULL --
-- URL encoded
'+UNION+SELECT+'M4rduk',+NULL+--
  -- OR
'%20UNION%20SELECT%20'M4rduk'%2c%20NULL%20--
```
Let’s talk about that other way to URL encode a payload in Burp I mentioned earlier.

In Burp Repeater:

- In your request, highlight the payload you want to edit. The Inspector panel will appear on the right.
- Ensure that ‘Decoded from:’ is set to ‘**URL encoding**’.
- You can now edit your payload in the bottom box.
- After making your changes, click ‘Apply Changes’. The URL-encoded version in the top box will replace your highlighted payload in the request. It’s quick and easy!

After applying the changes, click ‘**Send**’. If the server responds with a ‘500 Internal Server Error’, it means the first column is not compatible with text data.

Since the first column isn’t compatible with text data, let’s test the second column. Modify your payload to set the first column back to NULL and replace the second column with a string:

```
-- Our payload
' UNION SELECT NULL, 'M4rduk' --
-- URL encoded
'+UNION+SELECT+NULL,+'M4rduk'+--
  -- OR
'%20UNION%20SELECT%20NULL%2c%20'M4rduk'%20--
```
Apply the changes and click ‘**Send**’. This time, you should receive a ‘200 OK’ response, which confirms that the second column is compatible with text data.

To see the result of the injection, switch to the Render tab in Burp Repeater. You should see your string displayed on the webpage, proving that the injection was successful.

## Crafting Our Payload:

Now that we have the needed information, we can begin to craft our final payload.

### #4 — Retrieve ‘username’ and ‘password’ from the ‘users’ table.

The lab description tells us that we’re targeting a table named **users**, which contains two columns: **username** and **password**. Normally, we could use a straightforward UNION SELECT query like this:

`' UNION SELECT username, password FROM users --`
However, in this lab, only the second column is compatible with string data. This means we can’t retrieve both columns directly in a single query.

One approach is to retrieve the columns individually using two separate requests:

```
-- To retrieve username:
' UNION SELECT NULL, username FROM users --
-- To retrieve password
' UNION SELECT NULL, password FROM users --
```
While this method works, it’s time-consuming and makes it difficult to match usernames with their corresponding passwords.

This lab teaches us a more efficient and accurate way to retrieve the data using **concatenation**.

Open up the lab provided [***cheat sheet***](https://portswigger.net/web-security/sql-injection/cheat-sheet) and you will see the first section covering ‘String concatenation’.

- **NOTE** — I won’t go into how we know we are using Oracle, I have covered that in previous labs. Just know there are subtle differences in the characters, so knowing the type of database being used is very helpful.

In Oracle, the concatenation operator is the double pipe character (||). While we could simply concatenate the **username** and **password** columns like this:

```
-- Our payload
' UNION SELECT NULL, username||password FROM users --
--URL encoded
'%20UNION%20SELECT%20NULL%2c%20username%7c%7cpassword%20FROM%20users%20--
```
This would combine the **username** and **password** into a single string without any separation, making it difficult to distinguish where one ends and the other begins.

Let’s further improve upon this payload.

## Lab Solution:

Now that we’ve successfully retrieved the username and password data, let’s make it easier to read by adding a separator between the two fields. This will help us clearly distinguish where the username ends and the password begins.

To improve readability, we can inject a custom separator between the **username** and **password** fields. For this example, we will use the string `'<-->'` as our separator. Here’s how the payload looks:

```
-- Our payload
' UNION SELECT NULL, username||'<-->'||password FROM users --
-- URL encoded
'%20UNION%20SELECT%20NULL%2c%20username%7c%7c'%3c--%3e'%7c%7cpassword%20FROM%20users%20--
```
These character/characters can be anything you like, just make sure they are encased within single quotes.

Now we have all of the usernames and their corresponding passwords.

Head back over to the lab’s page in your browser. Click on the ‘*My account*’ link in the upper right of the page.

Log in as ‘administrator’ with the newly found credentials.

Congratulations! You solved another one! Keep up the great work!

See you next time.
