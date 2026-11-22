# sql injection in login field

- **Source URL:** https://medium.com/@guravtushar231/sql-injection-in-login-field-a9073780f7e8?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20251126142844/https://medium.com/@guravtushar231/sql-injection-in-login-field-a9073780f7e8
- **Fetched:** 2026-11-22
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/3788 (id 3788)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# sql injection in login field

Date: August 26, 2023

Reported By: Tushar rajendra Gurav (guravtushar231@gmail.com)

Summary:

During a security assessment of the Zoo Management, I identified a critical SQL injection vulnerability in the login functionality. This vulnerability could potentially allow an attacker to execute malicious SQL queries and gain unauthorized access to the system. I am submitting this report as part of the bug bounty program to assist in resolving the issue and ensuring the security of the application.

Vulnerability Details:

Vulnerability Type: SQL Injection

Affected Component: Login functionality

Affected Versions: All versions prior to the latest release (v1.0)

CVE ID: CVE-2023–41615

Description:

The login functionality of the Zoo Management does not properly sanitize user input before constructing SQL queries. This allows an attacker to inject malicious SQL code into the login fields and manipulate the query logic, potentially gaining unauthorized access to the system.

Steps to Reproduce:

Navigate to the login page of the Zoo Management .

Enter the following payload in the username or password field:

‘ OR ‘1’=’1' — -

This payload is designed to manipulate the query to always evaluate to true, effectively bypassing the authentication process.

Impact:

Successful exploitation of this vulnerability could allow an attacker to:

Bypass authentication and gain unauthorized access to the application.

Retrieve sensitive information from the database.

Modify or delete records within the database.

Potentially execute further malicious actions depending on the application’s functionality.

Recommendation:

To mitigate this vulnerability and enhance the security of the Zoo Management, I recommend the following steps:

Input Validation and Sanitization: Implement proper input validation and sanitization techniques to prevent SQL injection attacks. Use parameterized queries or prepared statements to ensure that user input is treated as data, not executable code.

Least Privilege Principle: Ensure that the database user account used by the application has the least privileges necessary to perform its tasks. This can minimize the potential impact of a successful attack.

Error Handling: Implement appropriate error handling mechanisms to prevent detailed error messages from being exposed to users. Detailed error messages can provide attackers with valuable insights into the application’s underlying structure.

Security Testing: Conduct thorough security testing, including code reviews and penetration testing, to identify and address potential security vulnerabilities before releasing updates.

Proof of Concept:

As this is a sensitive security issue, I have refrained from providing a detailed proof of concept in this report. The steps to reproduce provided above should be sufficient for your team to validate and address the issue.

Timeline:

August 25, 2023: Vulnerability discovered during security assessment.

August 26, 2023: Bug bounty report submitted to the Zoo Management team.

Disclaimer:

This report is submitted as part of the bug bounty program with the intention of responsibly disclosing the identified vulnerability. No malicious activities were performed during this assessment.

Thank you for your prompt attention to this matter, and I look forward to your response.

Sincerely,

Tushar Rajendra Gurav

guravtushar231@gmail.com
