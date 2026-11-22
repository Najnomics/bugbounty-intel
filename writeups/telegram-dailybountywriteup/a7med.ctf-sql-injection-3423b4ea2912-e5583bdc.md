# Sql injection

- **Source URL:** https://medium.com/@a7med.ctf/sql-injection-3423b4ea2912?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250920004533/https://medium.com/@a7med.ctf/sql-injection-3423b4ea2912
- **Fetched:** 2026-11-22
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/2841 (id 2841)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Sql injection

**Hi, guys! I wanted to share my recent finding with you. It’s a SQL injection, but the response of the query doesn’t appear on the page. Instead, the server downloads a file containing the result of the query. Let’s take a look!**


**First what is sql injection:**

SQL injection is a type of attack that exploits security vulnerabilities in web applications which use SQL (Structured Query Language) databases. The attacker injects malicious SQL code into input fields or parameters used by the web application, tricking the application into executing unintended SQL commands. This can lead to unauthorized access or modification of sensitive data, such as usernames and passwords, credit card numbers, or other valuable information. SQL injection attacks can be prevented by properly sanitizing user input and using parameterized queries instead of directly embedding user input in SQL statements.

**So now lets start:**


Lets call our domain [target.com](http://target.com/). My approach involves collecting as many endpoints and parameters as possible, and then manually reviewing them or using Nuclei. During my assessment, I came across the endpoint [target.com/display\_resource.php?id=](http://target.com/display_resource.php?id=) and upon visiting it, I observed

As you can see, we are able to view the SQL statement due to an error made by the developer. When any number is entered in the ‘id’ field, a file named ‘display\_resource.php’ is downloaded but it is empty. After trying to use boolean-based SQL injection, I realized that whether the SQL statement is true or false, it always returns the same file.so i going to try union based attack

So we need to determine number of columns.. they are six columns

when i used this payload:

union select NUll,NULL,NULL,NULL,NULL,NULL — ;

‘display\_resource.php’ is dowanloaded now our sql statement is correct.

It remains to retrieve the version as proof of concept. First, we need to determine which column is selected and whether the response will be different after some tries i found the 4th column is selcted

using union select NUll,NULL,NULL,‘a’,NULL,NULL — ;

file name is a and content is a

Finally we can easy get version by the same way
