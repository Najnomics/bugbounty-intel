# Bypassing Login with SQL Injection

- **Source URL:** https://vivek0x.medium.com/bypassing-login-with-sql-injection-portswigger-lab-walkthrough-210087fb87cf
- **Fetched from:** https://vivek0x.medium.com/bypassing-login-with-sql-injection-portswigger-lab-walkthrough-210087fb87cf?source=rss-a3d6c85e9637------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:**  (id 14948)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** Vivek Yadav / Wed, 14 Oct 2026 14:46:10 GMT

If you’re going through PortSwigger’s Web Security Academy, the “SQL injection vulnerability allowing login bypass” lab is one of the first proper hands-on labs that shows you just how fragile authentication logic can be when raw user input gets concatenated straight into a SQL query. It’s a short lab, but it’s a great one for building intuition about *why* SQL injection in login forms is dangerous — not because you’re stealing data this time, but because you’re walking straight through the front door without a password.

Here’s how I solved it, step by step, along with what’s actually happening under the hood.

The goal, as stated by PortSwigger, is simple: log in as the administrator user without knowing their password. The lab environment gives you a standard login page with a username and password field, and somewhere in the backend, the application is almost certainly building a SQL query like this:

SELECT \* FROM users WHERE username = 'admin' AND password = 'admin'

If that query returns a row, you’re authenticated. If it doesn’t, you get bounced back to the login page. The vulnerability exists because the app trusts the username and password fields enough to drop them directly into that query without sanitizing or parameterizing anything.

I clicked “Access the lab” and landed on the login page. Before touching anything, I made sure Burp Suite’s proxy was intercepting traffic through the browser, since the whole point of this lab is to manipulate the request after the browser builds it — not to guess payloads blindly in the UI.

I typed in administrator as the username and administrator’ — as the password (a throwaway guess, since I obviously didn’t have real credentials) and hit submit. Burp caught the POST request to /login before it ever reached the server.

With the request sitting in Burp’s Proxy tab, I right-clicked and sent it to Repeater. This is the natural move for this kind of testing — Repeater lets you tweak individual fields and resend the request over and over without having to go back through the browser and re-intercept each time. Much faster feedback loop.

The request body looked roughly like this:

`username=administrator&password=administrator%27--  (' --> %27)`
This is the core of the lab. I changed the username parameter from admin to:

administrator'--

and left the password field as administrator (the lab requires *some* value in the password field, even though it ends up being irrelevant — more on that below).

Sending this, the backend query becomes something like:

SELECT \* FROM users WHERE username = 'administrator'--' AND password = 'administrator'

The single quote closes off the string literal that the application wrapped around our input, and -- is a SQL comment marker. Everything after it — including the entire AND password = '...' clause — gets commented out and never evaluated by the database. So the query the database actually executes is functionally:

No password check at all. If a user named administrator exists (and in this lab, they do), this query returns their row, and the application treats that as a successful login — regardless of what password was submitted.

When I sent that modified request through Repeater, I got back a **302 Found**, redirecting to /my-account. That status code is the tell — a 302 here means the server accepted the login and is sending you off to the authenticated area of the app, whereas a failed login on this lab typically returns a 200 with the login form again.

Repeater confirms the vulnerability exists, but it doesn’t give you a live session in your browser — Burp and your browser don’t automatically share cookies in this context. So to actually *see* the solved state and get the lab to register as complete, I went back to the real login page in the browser and entered:

Submitted it, and landed straight in the administrator’s account. Lab solved.

The root cause is string concatenation in SQL query building instead of parameterized queries (prepared statements). The application never validates that username is just a plain string — it blindly stitches it into the query, which means any character with special meaning in SQL (like ' or --) gets interpreted by the database rather than treated as literal data.

The ' breaks out of the intended string boundary, and -- tells the SQL engine “ignore everything after this on the line.” Combine the two, and you’ve surgically removed the password check from the authentication logic without needing to know a single real credential.

GoodByee…
