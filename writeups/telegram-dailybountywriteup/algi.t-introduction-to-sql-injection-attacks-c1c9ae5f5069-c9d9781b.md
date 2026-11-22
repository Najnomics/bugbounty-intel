# Introduction to SQL Injection Attacks

- **Source URL:** https://medium.com/@Algi.T/introduction-to-sql-injection-attacks-c1c9ae5f5069?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20230614171639/https://medium.com/@Algi.T/introduction-to-sql-injection-attacks-c1c9ae5f5069
- **Fetched:** 2026-11-22
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/2790 (id 2790)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Introduction to SQL Injection Attacks

--

Most web servers and application servers interact with database servers to store, retrieve, change, or delete data through SQL (Structured Query Language) commands. While this functionality is essential for the proper functioning of web applications, it also introduces a significant security risk known as SQL injection (SQLi).

# What is SQLi?

SQL injection occurs when malicious actors exploit vulnerabilities in web applications to manipulate or gain unauthorised control over databases. By cleverly constructing and injecting malicious SQL code alongside the legitimate SQL statements that the site or application expects, attackers can deceive the web application into behaving in unexpected and dangerous ways.

# Types of SQLi

1. Union-based SQL Injection: In this method, the attacker employs the UNION operator to combine additional SQL statements with the original query’s result. By doing so, they can extract data from other database tables, gaining unauthorised access to sensitive information.
2. Boolean-based SQL Injection: Attackers exploit boolean conditions in SQL queries to gather insights into the database structure or extract data based on true/false responses. By manipulating these conditions, they can bypass security measures and retrieve data they shouldn’t have access to.
3. Error-based SQL Injection: This technique involves intentionally triggering errors in SQL queries to extract valuable information contained in the error messages. Attackers can gain insights into the database structure or identify vulnerabilities that may exist within the application.
4. Time-based SQL Injection: Attackers exploit delays in SQL queries to infer information or extract data based on the time it takes for the query to execute. By introducing time delays, they can gather details about the database structure or retrieve specific data.

## Example of Union-based SQLi

One of the most common types of SQL injection (SQLi) is the Union-based SQL injection. In this type of attack, the attacker leverages the UNION operator to combine additional SQL statements with the original query’s result, enabling them to extract data from other database tables.

Here’s a breakdown of how Union-based SQL injection works:

1. Identifying Vulnerability: The attacker identifies a web application that is vulnerable to SQL injection, typically due to improper input validation or lack of parameterisation in the application’s code.
2. Crafting the Malicious Input: The attacker enters carefully crafted input, including SQL statements, into user input fields such as search forms, login forms, or URL parameters. They manipulate the input to include the UNION operator and construct a query that retrieves data from other tables.
3. Manipulating the Query Structure: The injected SQL code alters the original query’s structure to accommodate additional SELECT statements. The UNION operator merges the attacker’s crafted query with the legitimate query, combining the results into a single result set.
4. Extracting Data: The combined result set contains data from the original query as well as the additional SELECT statements crafted by the attacker. This allows them to retrieve sensitive information from different database tables, such as usernames, passwords, or other confidential data.

Suppose a web application uses a SQL query like:


The attacker enters the following input to exploit the Union-based SQLi vulnerability:


The crafted input modifies the original query to become:


The UNION operator combines the attacker’s SELECT statement with the original query, resulting in a merged result set that includes usernames, emails, passwords, and credit card numbers.

# Impacts of SQLi attacks

SQL injection (SQLi) can have various potential impacts on a web application and its underlying systems. Here are some of the potential consequences of a successful SQL injection attack:

1. Unauthorised data access: Attackers can gain access to sensitive information like usernames, passwords, personal data, financial details, or other confidential data stored in the database.
2. Data Manipulation: Attackers can alter records, delete data, change the structure of the database, or even inject malicious code, leading to data corruption or manipulation.
3. Denial of Service (DoS): SQL injection attacks can overload or crash the database server by executing resource-intensive queries or malicious commands, resulting in service disruptions.
4. Privilege Escalation: If the application’s database has different user accounts with varying privileges, a successful SQLi attack can enable attackers to elevate their privileges, gaining administrative access or higher-level privileges. This opens the door for further exploitation.
5. Full System Compromise: In some cases, a successful SQLi attack can extend beyond the database server, compromising the entire underlying operating system or web server. This grants attackers unauthorised access to the entire system, enabling arbitrary commands execution or the installation of backdoors for future exploitation.

One of the largest and most recent SQLi cases in the UK was the TalkTalk Data Breach (2015). Attackers exploited SQLi vulnerabilities to compromise TalkTalk’s networks over 14,000 times in a single month. This incident is extensively covered in Jack’s Darknet Diaries Episode 4 called ‘Panic! at the TalkTalk Board Room’.

# Further reading

The below resources cover a range of topics, from understanding SQL injection techniques to implementing preventive measures. They provide valuable insights and guidance for securing web applications against SQL injection vulnerabilities.

1. “The Web Application Hacker’s Handbook: Finding and Exploiting Security Flaws” by Dafydd Stuttard and Marcus Pinto.
2. “SQL Injection Attacks and Defense” by Justin Clarke.
3. “OWASP Testing Guide” by The Open Web Application Security Project (OWASP).
4. “SQL Injection: Attacks and Defense” (Whitepaper) by Chris Anley.
5. “Preventing SQL Injection Attacks in [ASP.NET](http://ASP.NET)” (Microsoft Documentation).
6. “SQL Injection Prevention Cheat Sheet” by OWASP.
7. “SQL Injection Walkthrough” (Tutorial) by PortSwigger.

Thank you for reading 🚶♂️
