# SQL injection UNION attack, determining the number of columns returned by the query

- **Source URL:** https://medium.com/@Laxious8848/sql-injection-union-attack-determining-the-number-of-columns-returned-by-the-query-4792d89ad93f?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250504092916/https://medium.com/@Laxious8848/sql-injection-union-attack-determining-the-number-of-columns-returned-by-the-query-4792d89ad93f
- **Fetched:** 2026-11-21
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/8033 (id 8033)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# **SQL injection UNION attack, determining the number of columns returned by the query**

**Union-based SQL Injection** is a technique that exploits vulnerabilities in web applications by using the `UNION` SQL operator to combine the results of multiple `SELECT` queries into a single output. This allows an attacker to retrieve additional data from the database that was not intended to be displayed by the application.

Link of the lab: [https://0ac0009d03d438d3826ca1b50084005b.web-security-academy.net](https://0ac0009d03d438d3826ca1b50084005b.web-security-academy.net/)

So in this lab, there is UNION based sqli. So we have to find the number of columns in it. So there are different ways that we can find out the no of columns in it. So in this lab we gonna use the payload UNION select NULL — . So if there is single columns which i am guessing shouldn’t be there. IF it is it should show the same webpage and if there is not only 1 column. It will show internal server error.

As it says in the description of the lab, the UNION based sqli is present in the product category filter. So we gonna turn on the Foxy Proxy and we will see the HTTP history in Burpsuite.

And there would be different category inside product but i chosed gift and i select this request and send it to the repeater.

When i add a ‘ in the product category in the URL. It shows the internal server error.

SO i add ‘Union select NULL- — and i encode it using CTRL + U and it does this.

And the response is internal server error

And again we use the payload UNION select NULL, NULL- — . It checks whether it has 2 columns or not. IF there is no 2 columns. It will show internal server error.

It again show Internal server error.

And again we use the payload UNION select NULL, NULL, NULL- — . We will again see what the output is.

IT gives 200 response. So we can confirm that there is 3 columns in it.

And your lab is solved…….. Congragulations…………….
