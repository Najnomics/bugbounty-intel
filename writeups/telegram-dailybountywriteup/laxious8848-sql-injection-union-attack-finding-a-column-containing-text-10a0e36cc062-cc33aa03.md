# SQL injection UNION attack, finding a column containing text

- **Source URL:** https://medium.com/@Laxious8848/sql-injection-union-attack-finding-a-column-containing-text-10a0e36cc062?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250814083445/https://medium.com/@Laxious8848/sql-injection-union-attack-finding-a-column-containing-text-10a0e36cc062
- **Fetched:** 2026-11-21
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/8062 (id 8062)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# SQL injection UNION attack, finding a column containing text

In this box we will solve the lab containing Union based SQL injection and we have to find a column containing text.

Link of the lab: [https://0aaa00c8042fd4baa5a2c4fb000400c6.web-security-academy.net](https://0aaa00c8042fd4baa5a2c4fb000400c6.web-security-academy.net/)

First of all, we will open up the Foxyproxy and also burpsuite and we will see the sitemap and we will see the product categories and there are various categories as above. And i had this gift category and send this request to repeater.

First of all, we have to find out the no of columns in it. So as the previous lab, we will use the payload UNION select NULL- — and see whats the response.

It shows that there is internal server error. And it is sure that there is one column in it and lets see if there is two columns in it or not.

So this is the second payload that we used to find out if there is second columns in it and lets see whats the response.

So we confirmed that there is 2 columns in it.

Now we will use the payload to find out if there is 3 columns in it or not and lets see whats there response.

We can see that there is no 3 columns in it as there is no internal server error seen in it.

Now use this payload as the value provided says 5xCwkl and lets see if the payload works or not.

Congragulations you have solved the lab…..
