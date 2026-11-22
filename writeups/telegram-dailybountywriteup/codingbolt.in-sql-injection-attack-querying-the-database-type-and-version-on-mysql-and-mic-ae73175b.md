# SQL injection attack, querying the database type and version on MySQL and Microsoft

- **Source URL:** https://medium.com/@codingbolt.in/sql-injection-attack-querying-the-database-type-and-version-on-mysql-and-microsoft-162715c6cd0e?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250501124323/https://medium.com/@codingbolt.in/sql-injection-attack-querying-the-database-type-and-version-on-mysql-and-microsoft-162715c6cd0e
- **Fetched:** 2026-11-22
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/7398 (id 7398)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
Member-only story

# **SQL injection attack, querying the database type and version on MySQL and Microsoft**

In the world of cybersecurity, SQL Injection (SQLi) is a notorious and widespread attack technique. It allows attackers to manipulate queries sent to the database by injecting malicious SQL code into input fields. A common goal of attackers is to identify the database type and version, which provides critical insights into the target system’s infrastructure, enabling more sophisticated attacks later.


We will explore how attackers use SQL Injection to query and identify the database type and version on MySQL and Microsoft SQL Server — two of the most commonly deployed databases in web applications.

**SQL Injection Basics**

SQL Injection occurs when an application doesn’t properly sanitize user input before including it in an SQL query. The injected code can allow an attacker to interact with the database, bypass authentication, or extract data. Exploiting SQLi to determine the database type and version gives attackers information about how to craft database-specific exploits.

Each database platform — MySQL and Microsoft SQL Server (MSSQL) — has its own syntax, system tables, and functions. By crafting database-specific payloads, attackers can quickly identify the underlying database system and its version.
