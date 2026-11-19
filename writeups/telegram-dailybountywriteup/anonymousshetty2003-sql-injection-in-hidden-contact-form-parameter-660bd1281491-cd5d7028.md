# SQL Injection in hidden Contact Form Parameter

- **Source URL:** https://medium.com/@anonymousshetty2003/sql-injection-in-hidden-contact-form-parameter-660bd1281491?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20251009124433/https://medium.com/@anonymousshetty2003/sql-injection-in-hidden-contact-form-parameter-660bd1281491
- **Fetched:** 2026-11-19
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/10233 (id 10233)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# SQL Injection in hidden Contact Form Parameter

During a private bug bounty program, I came across an issue that reinforced one of the most important lessons in web security: never ignore the obvious. The vulnerability wasn’t in a complex API or behind a login panel. It was sitting in a basic contact form — something most developers build and forget.

This write-up explains how I found a SQL injection vulnerability in a contact form parameter, how I verified it, and why such issues continue to exist even today.

**How It Started**

While testing the private program application, I noticed a standard contact form with the usual fields: name, email, subject, and message. These forms are usually assumed to be low-risk, especially since they’re often unauthenticated and only meant to collect feedback. But I always test every input field, regardless of how routine it seems.

Out of habit, I filled in each input field and submitted the form. When I did this in the "subject" field, the UI showed a blank page so i checked the request in my BURP. While inspecting i saw a new parameter that was not shown in the UI. So, I entered a single quote (`'`) in the parameter which gave a MYSQL error.

**Digging Deeper**

To test further, I tried the following value in the subject field:

`test' AND 1=1 (200 OK)`

`test' AND 1=2 (200 OK with MYSQL error)`

The response changed. There was no longer a generic error, but rather a shift in how the page behaved. This was a sign that the input was being interpreted in a SQL context.

(To show impact i used SQLMAP, but u can also use GHAURI:

```
sqlmap -u "https://[REDACTED]/assessment/index.php?p=saveuser&firstname=test" --level=3 --risk=2 --user-agent -v3 --tamper="between,randomcase,space2comment" --batch
#p was the vulnerable parameter
```
**Understanding the Root Cause**

Based on the behavior, the backend was likely inserting the submitted form data directly into a SQL query using string concatenation. The application did not perform server-side input sanitization or use prepared statements for the subject field.

This is a common mistake. Developers are usually more cautious with login forms, registration inputs, or payment fields. But secondary components like contact forms are often treated as less critical and don’t always receive the same level of security attention.

**What Could Go Wrong**

The immediate risk was that an attacker could manipulate the database query. In this case, the contact form likely stored user submissions in a backend table. A successful SQL injection here could lead to data leakage, full table access, or in some configurations, even remote code execution depending on database permissions.

Even if the attacker couldn’t extract data immediately, the ability to influence database queries without authentication is serious. In larger systems, such a vulnerability might allow pivoting into more critical areas.

**Reporting the Issue**

I reported the vulnerability through the private platform with detailed steps, the payloads used, and suggested mitigations. The development team responded promptly. They confirmed the issue was caused by raw string insertion in the SQL layer and acknowledged the lack of input validation.

**Lessons Learned**

1. Every input field is a potential entry point. Treat contact forms, newsletter signups, and feedback boxes with the same scrutiny as login forms.
2. SQL injection remains a threat, especially in places developers might not think to defend.
3. Use parameterized queries for all database operations. Never build SQL queries by concatenating user input.

**Conclusion**

If you’re a developer, it’s worth taking a second look at those older forms you haven’t touched in years. And if you’re a researcher, don’t skip the boring inputs — they might be doing more behind the scenes than you think.
