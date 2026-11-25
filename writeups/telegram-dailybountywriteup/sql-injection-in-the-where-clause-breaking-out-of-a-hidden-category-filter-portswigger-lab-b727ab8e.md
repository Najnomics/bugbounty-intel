# SQL Injection in the WHERE Clause

- **Source URL:** https://vivek0x.medium.com/sql-injection-in-the-where-clause-breaking-out-of-a-hidden-category-filter-portswigger-lab-09ff7f3621fa
- **Fetched from:** https://vivek0x.medium.com/sql-injection-in-the-where-clause-breaking-out-of-a-hidden-category-filter-portswigger-lab-09ff7f3621fa?source=rss-a3d6c85e9637------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:**  (id 14946)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** Vivek Yadav / Mon, 12 Oct 2026 18:59:25 GMT

SQL injection has been sitting at or near the top of the OWASP Top 10 for over a decade, and yet it’s still one of the most common vulnerabilities found in real-world applications. PortSwigger’s Web Security Academy has a great beginner-friendly lab that illustrates exactly why: **“SQL injection vulnerability in WHERE clause allowing retrieval of hidden data.”** I worked through it recently, and I wanted to write up exactly what I did, step by step, along with *why* the payload works — not just *that* it works.

The lab simulates a simple e-commerce storefront. On the surface, it looks like any product catalog: a home page, a sidebar of product categories, and category pages that list items for sale. The twist is that the store has a category of products that are hidden from regular browsing — they’re marked as unreleased and shouldn’t show up unless you’re specifically allowed to see them. Our job, as the attacker, is to use a SQL injection flaw to make those hidden products appear anyway.

The lab goal is: display the products that belong to a hidden category.

Before touching Burp, it’s worth clicking around the site like a regular user would. I hit “Access the lab,” landed on the home page, and saw a row of product categories in the navigation — things like “Gifts,” “Pets,” “Lifestyle,” and so on. I clicked into the **“Gifts”** category (sometimes shown as “Corporate gifts” depending on the lab instance) just to see what a normal request to that page looked like.

This matters because understanding the “happy path” request is what lets you spot the injection point later. When I clicked the category link, the browser sent a GET request that looked roughly like this:

GET /filter?category=Corporate+gifts HTTP/2

Host: \<lab-id>.web-security-academy.net

That category value is a query parameter in the URL — not an HTTP header, even though it’s easy to mentally lump it in with the rest of the request metadata when you’re staring at Burp’s request pane. It’s the piece of user-controlled input that gets passed straight into a backend SQL query to decide which products to show.

With Burp’s proxy running and the browser configured to route through it, I turned on intercept, clicked the “Gifts” category again, and caught the outgoing GET request. From there, I right-clicked and sent it to **Repeater**, which is the ideal tool for this kind of manual, iterative testing — you can tweak one value at a time and immediately see the server’s response without having to replay the whole browsing flow.

This is the core of the exercise. The original request contained:

From ---> category=Corporate+gifts

I changed that value to:

To ---> category=' OR 1=1--

URL-encoded, that ends up looking something like category=%27+OR+1%3D1--+ in the raw request, which is why it visually resembles '+OR+1=1-- when you’re reading it off the request line in Burp.

I hit **Send**, and the response came back with *every* product in the catalog — including the one that’s supposed to be hidden. Burp flagged the lab as solved.

The application almost certainly builds its SQL query by directly concatenating the category value into a string, something along these lines:

SELECT \* FROM products WHERE category = 'Gifts' AND released = 1

That released = 1 condition is presumably what filters out the hidden/unreleased products from normal view. When the category parameter isn’t sanitized or parameterized, whatever you put there gets dropped straight into that quoted string.

So when I sent ' OR 1=1--, the query the database actually received became:

SELECT \* FROM products WHERE category = '' OR 1=1--' AND released = 1

Breaking that down:

The net effect is that the WHERE clause no longer filters anything meaningfully. The database just returns the entire products table, hidden and unreleased items included. That’s the whole vulnerability in a nutshell: user input was trusted enough to be spliced directly into a query’s logic, which let an attacker rewrite the query’s intent entirely.

The real-world fix is to never build SQL queries by string concatenation with user input. Parameterized queries (prepared statements) solve this cleanly, because the database treats the input strictly as data, never as part of the query’s logic — no matter what characters are in it:

SELECT \* FROM products WHERE category = ? AND released = 1

Here, even if someone submits ' OR 1=1-- as the parameter value, the database just looks for a category literally named ' OR 1=1--, finds nothing, and returns an empty result. The quote, the OR, the comment marker — none of it gets interpreted as SQL syntax.

Input validation and allow-listing (only accepting category values that match a known list) can help as defense in depth, but parameterization is the actual fix — it removes the ambiguity between code and data at the source.

This lab is a good first SQLi exercise precisely because the payload is so short and the result so dramatic — one tweak to a single parameter, and a filter that was supposed to hide data from you just evaporates. It’s a nice reminder that the gap between “working as intended” and “fully compromised” in a lot of real applications is sometimes just one unescaped quote.

GoodByee…
