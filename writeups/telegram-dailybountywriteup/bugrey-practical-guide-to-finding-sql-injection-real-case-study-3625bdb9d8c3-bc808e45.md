# Practical Guide to Finding SQL Injection (Real Case Study)

- **Source URL:** https://medium.com/@BugRey/practical-guide-to-finding-sql-injection-real-case-study-3625bdb9d8c3?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250502160151/https://medium.com/@BugRey/practical-guide-to-finding-sql-injection-real-case-study-3625bdb9d8c3
- **Fetched:** 2026-11-19
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/8678 (id 8678)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
**Disclaimer:**

*The guidelines in this article are provided for educational purposes and to raise awareness about cybersecurity. The author is not responsible for any use of the information that violates the law or harms others.*


In this tutorial, I will provide step-by-step instructions on how to find an SQL Injection Vulnerability (Error-Based SQLi).

1. First, we need to search for parameters on a website. To find parameters on a website, tools like **Paramspider** and **Arjun** can be used.
However, another way to find parameters on a target website is by using**Google Dorking** techniques.
2. Once you have found parameters on the target website, try testing by injecting a single quote ( ‘ ) at the end of the value in the parameter.
3. After injecting the payload with the single quote (‘) and receiving an error message like: 
**”You have an error in your SQL syntax; check the manual that corresponds to your MariaDB version for the right syntax to use near ‘’21'’’ at line 1.”**
This could indicate the presence of an SQL Injection (Error-Based SQL Injection) vulnerability.

4\. Next, you can inject other SQL injection payloads, such as: 

**’ UNION SELECT 1, version(), 3, 4, 5, 6, 7, 8 — +**

(This payload is used to display the database version), or you can use: 

**’ ORDER BY 9 — +**

(This payload checks the number of columns in the database).

5\. After that, inject this SQL injection payload: 

\*\*’ UNION SELECT 1, table\_name, 3, 4, 5, 6, 7, 8 FROM information\_schema.tables WHERE table\_schema = database() — +\*\* 

(This payload is used to display the names of tables in the database).

So, the tutorial above explains an easy way to find an SQL Injection vulnerability.

Additional References:

[https://github.com/kleiton0x00/Advanced-SQL-Injection-Cheatsheet/tree/main/MSSQL%20-%20Error%20Based%20SQLi](https://github.com/kleiton0x00/Advanced-SQL-Injection-Cheatsheet/tree/main/MSSQL%20-%20Error%20Based%20SQLi) (Error-Based SQL Injection Payloads)

[https://github.com/devanshbatham/ParamSpider](https://github.com/devanshbatham/ParamSpider) (Paramspider Tool)

[https://github.com/s0md3v/Arjun](https://github.com/s0md3v/Arjun) (Arjun Tool)
