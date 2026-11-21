# SQL Injection via ORDER BY Parameter

- **Source URL:** https://medium.com/@mfthylmaz/sql-injection-via-order-by-parameter-a7cb7d04017f?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20241222171031/https://medium.com/@mfthylmaz/sql-injection-via-order-by-parameter-a7cb7d04017f
- **Fetched:** 2026-11-21
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/8241 (id 8241)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
Hi Guys In this blog post, I’ll share the details of an SQL Injection vulnerability I discovered while exploring a web application.

The target application is a platform similar to Udemy, designed for offering online courses. Initially I registered on the platform to access a course, and while interacting with the application, certain API parameters caught my attention.

# Discovery of the Vulnerability

While navigating through the site’s links, I was simultaneously monitoring the outgoing requests with Burp Suite. During this process, I stumbled upon an interesting API request:

`/api/categories?cacheId=undefined&parentId=null&orderBy=priority:asc`

In another write-up (I can’t find it right now), I read about an SQL injection vulnerability related to API parameters. When I saw this, it reminded me to test the `orderby` parameter.

This API endpoint was responsible for fetching course categories. Naturally, I decided to test the `orderBy` parameter to see if it was vulnerable. When I modified its value to `asc+LIMIT+1+--`, the response returned only a single value. This was an immediate indicator that my SQL queries were being processed on the backend.

To further explore, I started experimenting with additional variations of SQL syntax to refine my understanding of how the application handled inputs. Each modification provided a new piece of the puzzle, leading me to confirm that the parameter was vulnerable to SQL injection.

# Proving Exploitation

By experimenting with different queries, I identified that the application was using *PostgreSQL* as its database management system. This information opened up new possibilities for crafting targeted attacks.

At this point, I attempted to use **sqlmap** to automate attacks tailored to PostgreSQL.

I utilized **time-based SQL Injection** by leveraging the `pg_sleep()` function. This demonstrated that my crafted queries were indeed interacting with the database. **And BOOM!** I finally got the response I was looking for from the server!

After documenting all findings, I submitted a detailed report to the responsible team, including the steps to reproduce the vulnerability and proof of exploitation.

Thanks for reading,and remember the best bugs are the ones you find after a good hunt.
