# 2nd Order SQL Injection

- **Source URL:** https://medium.com/@bountyget/2nd-order-sql-injection-e2ac60e792a4?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20240920135527/https://medium.com/@bountyget/2nd-order-sql-injection-e2ac60e792a4
- **Fetched:** 2026-11-22
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/7215 (id 7215)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# 2nd Order SQL Injection

SQL Injection (SQLi) has long been a well-known attack vector that targets the backend database of web applications. While most developers are familiar with First Order SQL Injection attacks, Second Order

SQL Injection (2nd Order SQLi) is often overlooked, even though it can be just as dangerous.

Unlike First Order SQL Injection, where malicious input is executed immediately after being inserted into a query, 2nd Order SQL Injection involves injecting malicious data that is stored by the application and

executed later, during a separate operation. This delayed execution makes it harder to detect because the input seems benign at first, but becomes harmful when retrieved and processed.

**Example Scenario:**

Imagine a user registration system where user inputs are validated and stored securely in the database.

However, at a later stage, perhaps during a profile update or report generation, the stored data is

processed without suLicient validation or escaping, leaving room for exploitation.

**Code Example of 2nd Order SQL Injection:**

**Here’s a simple PHP code snippet to demonstrate how 2nd Order SQL Injection occurs:**

\<?php

function registerUser($username, $password, $pdo) {

$stmt =…
