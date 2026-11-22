# Avoid ‘OR 1=1’ while doing SQL Injection, Why?

- **Source URL:** https://medium.com/@aaftaba.k47/avoid-or-1-1-while-doing-sql-injection-why-5e7cc0716ef3?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20240708164443/https://medium.com/@aaftaba.k47/avoid-or-1-1-while-doing-sql-injection-why-5e7cc0716ef3
- **Fetched:** 2026-11-22
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/6629 (id 6629)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Avoid ‘OR 1=1’ while doing SQL Injection, Why?

**Note to Readers:**

This blog is intended for individuals who already have a basic understanding of SQL injection attacks. It delves into more advanced concepts and examples, making it best suited for those who are familiar with SQL injection techniques and want to deepen their knowledge. If you are new to SQL injection, we recommend starting with introductory resources before diving into this content.

**Introduction to Sql Injection at a Pizza Store.**


Imagine your favourite pizza place allows you to order online, where you can choose toppings like cheese, pepperoni, or mushrooms. Now, suppose someone enters a request like this: “extra cheese’; DROP TABLE orders;”. Instead of just adding extra cheese, this malicious request could delete all the orders from the system!

This is an example of SQL injection. It’s like sneaking in a harmful request that can do more than intended, potentially causing serious issues for the pizza store. Therefore, it’s crucial for the pizza place to ensure they only accept safe and clear instructions to prevent such attacks.

*Understanding SQL Injection and Prevention Techniques*


**Practice SQL Skills:**

Explore [Dbfiddle.UK](https://dbfiddle.uk) to learn and practice with various databases like SQL, MySQL, PostgreSQL, Oracle, etc.

**Example of SQL Injection Error:**Consider the following SQL

`UPDATE` statement, which contains an error due to the incorrect use of an apostrophe in the `password` attribute:```
UPDATE users SET password = 'newpass' ' WHERE email = 'xyz@example.com'
Error: You have an error in your SQL syntax; check the manual that 
corresponds to your MySQL server version for the right syntax 
to use near 'xyz@example.com'' at line 1
```
**The main rule to find an SQL injection, first we need to trigger an SQL Injection error as mentioned below.**


```
Error: You have an error in your SQL syntax; check the manual that 
corresponds to your MySQL server version for the right syntax 
to use near 'xyz@example.com'' at line 1
```
**We have an SQL database with a simple version to understand it more practically.**


We have a code which runs a basic SQL statement to update the **password** for **xyz@example.com**.

**Impact of '****OR 1=1':**`'OR 1=1'` in the update statement:

This query updates the password for all email addresses, as `'OR 1=1'` always evaluates to true. This makes `'OR 1=1'` dangerous and demonstrates a basic form of SQL injection.

**Using Comments to Break Queries:**

A similar issue arises when using **comments** to break out of the `WHERE` condition:

This query also updates the password for all email addresses.

**Comparison with AND 1=1**

You might be questioning if we use `AND 1=1` instead of `OR 1=1`: then what?

This query behaves as intended without altering the logic, because `AND 1=1` does not change the query's logic.

# **Preventing SQL Injection with UNION Statement:**

To avoid harmful effects, let’s use a `UNION` statement:

`SELECT 'hacker' , 1337;`
The above query creates a **Psuedo** table that doesn’t exist without any table name creation because SQL says: OKAY, You want to make a **SELECT** query with columns and rows let make it but it will not be saved! That’s how the Database works.

This query creates a pseudo table without altering the database. Using `UNION` ensures safe data retrieval without updates or deletions.

**Example :**

Assume the below database module for your reference.

We can see the Union Statment below which creates Dummy data in the table

Likewise, more examples can be seen for more understanding of the **Union** Statement.

In the below example lab, we know that the Lifestyle category has 3 assets and the main motive of the lab is to bring more hidden assets by using **the ‘OR 1=1'** payload instead we will use a **UNION** statement to break the **OR** query for the safer side.

You can see the difference between the **original** request and the **‘OR 1=1’** payload which solves the lab easily.

`GET /filter?category=lifestyle'OR 1=1 -- -'`
As seen above **‘OR 1=1’** worked perfectly let see by using the UNION statement which will prevent the use **OR** statement by updating or deleting the database in it. As **UNION** doesn’t work for an update or delete function.

While Using the **UNION** statement we need to know the columns of the database by using the **ORDER** statement as follows **ORDER BY 1-** till we find an Internal server error as shown below.

As we know there are **8 columns** in the database let move with the **UNION** statement as follows:

`UNION SELECT NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL --`
This creates dummy data safely. Replace `NULL` with meaningful data to test without affecting the database:

`Gifts'+OR+1%3d1+UNION+SELECT+'1','2','hacker',NULL,NULL,NULL,NULL,NULL+-+-`
Using `UNION` prevents the harmful effects of `OR` statements, ensuring the database remains intact. As it will not break the database by updating or deleting with an OR statement.

## Conclusion:

This blog aims to help you understand safe query practices, especially in testing production environments. Avoiding harmful payloads like `OR 1=1` and using `UNION` ensures database integrity. More content on SQL injection techniques, such as **error-based** and **blind-based** injection attacks, will be posted soon.
