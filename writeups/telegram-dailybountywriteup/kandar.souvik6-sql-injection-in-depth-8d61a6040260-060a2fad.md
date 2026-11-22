# SQL injection in Depth

- **Source URL:** https://medium.com/@kandar.souvik6/sql-injection-in-depth-8d61a6040260?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20230124064736/https://medium.com/@kandar.souvik6/sql-injection-in-depth-8d61a6040260
- **Fetched:** 2026-11-22
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/1399 (id 1399)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# SQL injection in Depth

SQL injection is a type of security vulnerability that occurs when an attacker is able to insert malicious code into an SQL statement, allowing them to gain unauthorized access to a database. This type of attack can have serious consequences, as it can potentially allow an attacker to steal sensitive information, delete or modify data, or even take control of a system.

One of the main reasons why SQL injection attacks are so successful is because they take advantage of a common oversight in the way that web applications are developed. When a web application receives user input, it often constructs an SQL statement using that input and sends it to the database for execution. If the input is not properly validated or sanitized, it is possible for an attacker to insert malicious code into the SQL statement, which can then be executed by the database.

Let’s take a look at an example of how an SQL injection attack can occur. Consider the following script, which is designed to retrieve a user’s account information from a database:

`Copy code``import mysql.connector`
\# Connect to the database

cnx = mysql.connector.connect(user='username', password='password', host='host', database='database')# Get the user input

username = input("Enter your username: ")# Construct the SQL statement

query = "SELECT \* FROM users WHERE username = '" + username + "'"# Execute the SQL statement

cursor = cnx.cursor()

cursor.execute(query)# Print the results

for (username, password) in cursor:

print("Username: " + username)

print("Password: " + password)

As you can see, this script takes user input and directly includes it in the SQL statement. If an attacker were to enter the following as their username:

`' OR '1'='1`
The SQL statement would become:

`SELECT * FROM users WHERE username = '' OR '1'='1'`
This would allow the attacker to see all the data in the table, since the where clause would always be true.

To prevent this type of SQL injection attack, we can use parameterized queries. This involves separating the SQL statement from the user input, so that the input is passed as a separate parameter rather than being directly included in the SQL statement. Here’s an example of how the script would look with parameterized queries:

`import mysql.connector`
cnx = mysql.connector.connect(user='username', password='password', host='host', database='database')username = input("Enter your username: ")query = "SELECT \* FROM users WHERE username = %s"

cursor = cnx.cursor()

cursor.execute(query, (username,))for (username, password) in cursor:

print("Username: " + username)

print("Password: " + password)

In this example, the user input is passed as a separate parameter to the cursor.execute() function, which ensures that it is properly sanitized before it is executed.

Another effective method of preventing SQL injection attacks is to use an Object Relational Mapping (ORM) library. ORM libraries provide a higher-level abstraction over the database, which makes it easier to separate the SQL statement from the user input. Additionally, ORM libraries typically provide built-in validation and sanitization of user input, which further reduces the risk of SQL injection attacks.

In addition to these prevention techniques, it
