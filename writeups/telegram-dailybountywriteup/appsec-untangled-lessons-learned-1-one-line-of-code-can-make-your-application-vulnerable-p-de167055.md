# Lessons Learned #1

- **Source URL:** https://medium.com/appsec-untangled/lessons-learned-1-one-line-of-code-can-make-your-application-vulnerable-pre-auth-rce-in-metabase-a8579ca0102d?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20240903125459/https://medium.com/appsec-untangled/lessons-learned-1-one-line-of-code-can-make-your-application-vulnerable-pre-auth-rce-in-metabase-a8579ca0102d
- **Fetched:** 2026-11-19
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/7152 (id 7152)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Lessons Learned #1: One line of code can make your application vulnerable (Pre-Auth RCE in Metabase CVE-2023–38646)

Welcome all to this new series “Lessons Learned”. In this series, I plan to share some real-world vulnerabilities from the eyes of an application security engineer. There are many resources where you can find vulnerability write-ups which mostly focus on the exploitation techniques used to discover and exploit the vulnerability. This is usually pretty cool but is more relevant to security researchers/pentesters/bug bounty hunters.

However, In this series, I will take a different angle that is more relevant to application security engineers and developers, so I will focus instead on the underlying root causes and the measures we can take to prevent similar issues in our applications.

Of course, I will leave links for the vulnerabilities write-up if you are also interested in the exploitation techniques.

So Let’s start with the first vulnerability!

# Pre-Auth RCE in Metabase (CVE-2023–38646)

[Metabase](https://github.com/metabase/metabase) is a popular open-source business intelligence tool. A vulnerability was discovered around July 2023 and assigned [CVE-2023–38646](https://www.metabase.com/blog/security-advisory) (you can find the full write-up [here](https://www.assetnote.io/resources/research/chaining-our-way-to-pre-auth-rce-in-metabase-cve-2023-38646)) which had a devastating impact of pre-auth RCE (Remote code execution) which means an unauthenticated user with network access to any instance of the web application could run code on the servers the application is running on. So Let’s discover what went wrong!

# Issue #1: Authentication Bypass

Like many applications, Metabase uses a setup token during the initialization of the application. Once the application is initialized, the setup token should no longer be useable, and instead, the user should use the credentials created during the initialization process.

This was working as expected until one day a developer pushed a [PR](https://github.com/metabase/metabase/commit/0526d88f997d0f26304cdbb6313996df463ad13f#diff-44990eafd7da3ac7942a9f232b56ec045c558fdc3c414a2439e42b5668eced32L140-L141) (pull request), and for some reason removed the line of code clearing the setup token after init is done, this wasn’t caught in the code review, and as a result for this version of Metabase and subsequent ones, the setup token was available after being in production for anyone that has network access.

Any attacker that can find the setup token, can use it to bypass authentication and login to the web application.

# Issue #2: SQL Injection

As Metabase is a business intelligence application, it has to connect to multiple database, one of which is the [H2](https://www.h2database.com/html/main.html) database. The security researchers in this case found a 0-day vulnerability (undiscovered vulnerability) affecting the H2 database driver allowing SQL injection.

You can see the SQL injection payload in the screenshot below, and you can find more details about how it works in the [write-up](https://www.assetnote.io/resources/research/chaining-our-way-to-pre-auth-rce-in-metabase-cve-2023-38646) itself. However, the thing to note here is that the reason this SQL injection was possible, is the fact that the application was taking the connection string itself as input which allowed the security researchers a lot of room to experiment and find ways to exploit.

# Lessons Learned

**1. Authentication bypass**: The setup token issue is a business logic issue, very specific to Metabase. This means that no security scanning tool (SAST, DAST, IAST, .. etc) could have detected this issue. For this class of issues, your best bet is always:

- **Threat modeling**: Spending time during the design phase of any project to decide what could go wrong would be a good place to discuss business logic issues and what can be done to avoid them (the mitigations). For more about threat modeling you can check my series [Threat Modeling Handbook](/@mohamed.osama.aboelkheir/list/threat-modeling-handbook-309a70ec273f).
- **Security tests**: It is equally important to make sure the mitigations discussed during threat modeling, and any security controls are being covered by tests. This could be a unit test, an integration test, or a security tool scan depending on the situation. For example, in this case, an integration test verifying the setup token was no longer available after initialization would have detected the issue before being pushed.

**2. SQL injection**: In this case, the vulnerability was not in the code itself, but in the library used for H2 database connection. As this was a 0-day, SCA tools (e.g. Dependabot) couldn’t have helped. However, two things could have helped here:

- **Not taking complex input** such as the connection string: The exploit would have been much less likely to work if we only took the host, port, and other details needed for the connection and used them to build the connection string within the code, making it harder to provide the payload needed for SQL injection to work.
- **Input validation**: besides not taking complex, input it is always important to perform input validation that doesn’t allow unneeded special characters, this could be in the form of a pattern constraint (regular expression), a list of allowed values, or a list of allowed characters. This also makes it nearly impossible to provide the payload needed for SQL injection to work. You can find more about input validation in my previous story [How to make “Input validation” easy for your devs](/appsec-untangled/how-to-make-input-validation-easy-for-your-devs-b31a4e8595cb).

# Conclusion

Always remember that even one line of code could make your application vulnerable, and while code reviews work, you can’t fully rely on them. You should also make sure that any security control is covered by a test that is running during build or periodically to make sure new code changes don’t break the control.

Stay tuned for the next episode of “Lessons Learned”!
