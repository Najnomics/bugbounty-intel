# Irish-Name-Repo 3

- **Source URL:** https://medium.com/@affanhaxor/irish-name-repo-3-cylab-security-academy-write-up-understanding-rot13-and-sql-injection-39f6f0681833
- **Fetched from:** https://medium.com/@affanhaxor/irish-name-repo-3-cylab-security-academy-write-up-understanding-rot13-and-sql-injection-39f6f0681833?source=rss-a70f2c751bb6------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:**  (id 14955)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** Affanhaxor / Thu, 22 Oct 2026 05:24:20 GMT

Web applications often use login forms to protect administrative features. However, when user input is handled insecurely, an attacker may be able to manipulate the database query and bypass authentication.

In this write-up, I will explain my approach to solving **Irish-Name-Repo 3** on CyLab Security Academy. The challenge builds on the previous Irish-Name-Repo challenges, but introduces an additional layer: the application transforms the password input using ROT13 before using it in an SQL query.

By examining the login behavior and enabling the application’s debug option through Burp Suite, we can understand this transformation and see why it does not prevent SQL injection.

After opening the challenge, I was presented with a website titled “List ‘o the Irish!” featuring several portraits and a navigation menu.

At first glance, the page did not expose any obvious functionality related to the challenge. I started by exploring the available navigation options to locate the administrative login page.

I opened the navigation menu and found two options: **Support** and **Admin Login**. Since the challenge involved authentication, I selected Admin Login to investigate the protected area.

The login page contained a password field and a Login button. Unlike a typical login form, there was no username field, which suggested that the application used a different authentication mechanism for the administrator.

I first submitted a normal password to observe how the application responded. The server returned a simple message:

Login failed.

This confirmed that the application was processing the submitted password, but it did not explain how the authentication check worked.

Instead of trying random passwords, I moved on to inspect the HTTP request and response to understand the application’s server-side behavior.

I intercepted the login request using Burp Suite. The request was sent to /login.php using the POST method, and its body contained two parameters:

The presence of the debug parameter was particularly interesting. I decided to change its value to 1 and compare the server's response.

After changing debug=0 to debug=1, I forwarded the request and inspected the response.

The application displayed additional diagnostic information, including the SQL query it had constructed. The query contained a transformed version of the submitted password. For example, the text Admin appeared as Nqzva.

This was an important clue: the application was applying a letter transformation to the input before placing it into the SQL query.

The transformation matched **ROT13**, a simple substitution cipher that rotates each letter by 13 positions in the alphabet.

ROT13 replaces each letter with the letter 13 positions later in the alphabet. For example:

OriginalROT13ANdqmzobre

That explains why Admin becomes Nqzva and why the SQL keyword OR becomes BE.

The important detail is that ROT13 changes letters but leaves digits, spaces, apostrophes, and hyphens unchanged.

Consequently, a SQL injection payload containing the keyword OR will not work as intended if the application transforms it into BE before executing the query.

However, ROT13 is reversible. By submitting the ROT13-transformed version of a payload, the application can transform it back into the intended SQL expression.

Once I understood the transformation, I used the login request to test an SQL injection payload in its ROT13 form. The key idea was to account for the application’s input transformation rather than submit the ordinary payload unchanged.

For example, the following SQL injection expression:

' OR 1=1 --

has this ROT13-transformed form:

' BE 1=1 --

When the application applies ROT13 to the transformed input, the SQL keyword returns to OR. In an application that builds SQL queries through unsafe string concatenation, this can alter the query's logic and potentially bypass the password check.

After submitting the appropriately transformed input in the challenge, the application accepted the login and returned the flag.

The challenge displayed the following flag after successful authentication:

academy{3v3n\_m0r3\_SQL\_8f489750}

This challenge demonstrated several important web application security concepts:

The most important lesson is that encoding or transforming input is not a replacement for secure database query construction.

Developers can reduce the risk of SQL injection by following these practices:

**Use parameterized queries.** Prepared statements keep user input separate from SQL instructions instead of combining the two into a query string.

**Avoid relying on encoding as a security control.** ROT13 and similar reversible transformations do not prevent malicious input from changing SQL logic.

**Restrict debug functionality.** Detailed SQL queries and internal diagnostic messages should not be exposed to ordinary users or in production environments.

**Validate input appropriately.** Apply server-side validation according to the expected format of each field, while remembering that validation alone cannot replace parameterized queries.

**Handle authentication securely.** Password verification should follow established secure authentication practices and must not depend on a user-controlled value being inserted directly into an SQL statement.

Irish-Name-Repo 3 demonstrates how a seemingly simple transformation can create a false sense of security. By inspecting the request, enabling debug output, and recognizing the ROT13 transformation, I was able to understand why a conventional SQL injection payload did not work as expected and how the challenge could be solved.

The key takeaway is straightforward: **secure query construction matters more than hiding or transforming user input.** Parameterized queries and properly restricted diagnostic features are essential for protecting applications against SQL injection.

This challenge was a useful exercise in combining HTTP request analysis, encoding concepts, and SQL injection fundamentals in a controlled learning environment.

**LinkedIn:** [https://www.linkedin.com/in/affanhaxor](https://www.linkedin.com/in/affanhaxor)

**Instagram:** [https://instagram.com/affan\_haxor](https://instagram.com/affan_haxor)

*Follow me for more CTF write-ups, web security labs, and AppSec content.*
