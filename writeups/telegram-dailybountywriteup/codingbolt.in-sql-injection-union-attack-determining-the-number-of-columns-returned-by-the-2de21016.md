# SQL injection UNION attack, determining the number of columns returned by the query

- **Source URL:** https://medium.com/@codingbolt.in/sql-injection-union-attack-determining-the-number-of-columns-returned-by-the-query-f04154bd5b3c?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250504025417/https://medium.com/@codingbolt.in/sql-injection-union-attack-determining-the-number-of-columns-returned-by-the-query-f04154bd5b3c
- **Fetched:** 2026-11-22
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/7440 (id 7440)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
Member-only story

# **SQL injection UNION attack, determining the number of columns returned by the query**

SQL Injection: UNION Attack and Determining Columns

In the world of cybersecurity, SQL injection remains one of the most notorious and common vulnerabilities. Among the various forms of SQL injection attacks, the UNION-based SQL injection is particularly interesting and powerful. By exploiting this technique, attackers can combine the results of two or more SELECT queries into a single result set, gaining access to sensitive information.


But before an attacker can retrieve data, one critical step is figuring out how many columns the target query returns. In this article, we’ll explore the concept of UNION-based SQL injection, how attackers determine the number of columns returned by the query, and what steps organizations can take to protect against it.

**What is SQL Injection?**

SQL Injection occurs when attackers manipulate web application inputs to inject malicious SQL code into queries. This flaw allows them to interact directly with the database, extracting confidential information or altering the database’s content.
