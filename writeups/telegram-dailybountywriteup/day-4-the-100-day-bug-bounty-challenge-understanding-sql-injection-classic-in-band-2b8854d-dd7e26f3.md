# Day 4. The 100-Day Bug Bounty Challenge

- **Source URL:** https://mahhesshh.medium.com/day-4-the-100-day-bug-bounty-challenge-understanding-sql-injection-classic-in-band-2b8854d2e0e5?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250505120957/https://mahhesshh.medium.com/day-4-the-100-day-bug-bounty-challenge-understanding-sql-injection-classic-in-band-2b8854d2e0e5
- **Fetched:** 2026-11-21
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/8485 (id 8485)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Day 4. The 100-Day Bug Bounty Challenge: Understanding SQL Injection Classic(In-band)

Welcome to Day 4 of my 100-day bug bounty challenge! Today, we’ll discuss one of the most infamous and impactful vulnerabilities in web security: SQL Injection (SQLi). This vulnerability can give attackers access to sensitive data and, in some cases, complete control over a database. Let’s dive into what SQL injection is, how it works, and explore real-life examples.

# What is SQL Injection?

SQL Injection happens when an attacker manipulates a web application’s database query by injecting malicious SQL code through input fields or URL parameters. The root cause of SQLi is insufficient input validation or poor handling of user-provided data in SQL queries.

## In simpler terms:

1. Applications use databases to store and retrieve data.
2. SQL queries are used to interact with the database.
3. If user inputs are not handled properly, attackers can modify these queries to:

- Extract sensitive data (like usernames and passwords).
- Delete or modify data.
- Take control of the database.

# How SQL Injection Works

Consider a login form where users enter their username and password. A typical SQL query might look like this:

`SELECT * FROM users WHERE username = 'user' AND password = 'pass';`
If the input fields are not sanitized, an attacker can inject malicious SQL code. For example, entering the following username:

`' OR '1' = '1`
And leaving the password blank might result in the following query:

`SELECT * FROM users WHERE username = '' OR '1' = '1' AND password = '';`
The condition `'1' = '1'` is always true, so the attacker gains unauthorized access without knowing the username or password.

# Real-Life Example 1: Bypassing Login Forms

Imagine a vulnerable website with the following login query:

`SELECT * FROM users WHERE username = '$username' AND password = '$password';`
An attacker enters:

- **Username**: `' OR '1' = '1`
- **Password**: `anything`

The query becomes:

`SELECT * FROM users WHERE username = '' OR '1' = '1' AND password = 'anything';`
Since `'1' = '1'` is always true, the attacker logs in without valid credentials.

## Impact:

1. Unauthorized access to user accounts.
2. Potential data theft or manipulation.

## POC Video:

[Login Panel Bypass by cybersec](https://www.youtube.com/watch?v=ImhPl50NUrY)

## Prevention:

Use **parameterized queries** (prepared statements):

```
$stmt = $conn->prepare('SELECT * FROM users WHERE username = ? AND password = ?');
$stmt->bind_param('ss', $username, $password);
$stmt->execute();
```
# Real-Life Example 2: Extracting Data with UNION

Attackers often use the `UNION` keyword to combine results from multiple queries. For example:

## Vulnerable URL:

`https://example.com/products?id=1`
The SQL query:

`SELECT name, price FROM products WHERE id = 1;`
An attacker changes the URL to:

`https://example.com/products?id=1 UNION SELECT username, password FROM users;`
The query becomes:

`SELECT name, price FROM products WHERE id = 1 UNION SELECT username, password FROM users;`
This combines product data with user credentials, exposing sensitive information.

## Impact:

1. Attackers gain access to usernames, passwords, or other sensitive data.
2. Data breaches and compliance violations.

## Prevention:

1. Validate and sanitize all inputs.
2. Restrict database permissions to limit the impact of SQLi.

# Real-Life Example 3: Deleting Data with SQLi

Attackers can exploit SQLi to delete or modify data. Consider a query that deletes user accounts:

## Vulnerable Code:

`$query = "DELETE FROM users WHERE id = '$id';";`
An attacker submits:

`$id = 1; DROP TABLE users;`
The query becomes:

`DELETE FROM users WHERE id = 1; DROP TABLE users;`
This deletes the user with ID 1 and then drops the entire `users` table, causing significant damage.

## Impact:

1. Loss of critical data.
2. Disruption of business operations.

## Prevention:

1. Use parameterized queries.
2. Implement database backups and recovery mechanisms.

# How to Test for SQL Injection

1. **Manual Testing**:

- Enter common SQL payloads in input fields or URL parameters, such as:
- `' OR '1' = '1`
- `' UNION SELECT null, null;--`

3**. Automated Tools**:

- Tools like SQLMap can identify and exploit SQL injection vulnerabilities.

4\. **Check Error Messages**:

- Look for database error messages that reveal query structures.

# Mitigation and Best Practices

1. **Parameterized Queries**:

- Always use prepared statements to separate SQL code from user input.

2\. **Input Validation**:

- Validate and sanitize all user inputs.

3\. **Least Privilege Principle**:

- Limit database user permissions to minimize the impact of SQLi.

4\. **Web Application Firewalls (WAFs)**:

- Use a WAF to detect and block SQLi attempts.

5**. Error Handling**:

- Hide detailed error messages from users to avoid leaking query information.

# Bonus

1. **Learning Resources: (click on the Text to redirect)**

2\. **Payloads Cheat-sheet**:

3\. **Reports:**

# Tools to Help You

- **SQLMap**: Automated SQL injection exploitation.
- **Ghauri:** Automated SQL injection exploitation.
- **Burp Suite**: Test for SQLi vulnerabilities during pen testing.
- **OWASP ZAP**: Identify security flaws in web applications.

# Conclusion

SQL Injection is a critical vulnerability that can have devastating consequences for businesses and users. By understanding how it works and implementing proper security measures, developers can protect their applications and data. As a bug bounty hunter, it’s essential to test for SQLi responsibly and report your findings to help improve web security.

That’s it for Day 4! Tomorrow, we’ll tackle another exciting topic. Stay tuned and keep learning.
