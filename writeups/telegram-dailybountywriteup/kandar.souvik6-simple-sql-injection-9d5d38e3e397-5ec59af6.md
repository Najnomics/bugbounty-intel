# Simple SQL Injection

- **Source URL:** https://medium.com/@kandar.souvik6/simple-sql-injection-9d5d38e3e397?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20230111225059/https://medium.com/@kandar.souvik6/simple-sql-injection-9d5d38e3e397
- **Fetched:** 2026-11-22
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/1259 (id 1259)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Simple SQL Injection

Sql injection is a very critical vulnaribility for any organization.An attacker can get hold of internal data through sql dump.

For sql injection at first we need parameters.Generally I go for reflected parameters,it does not matter if the request is GET or POST. Then Iuse sqlmap to automate the sql test.

To install in linux -

sudo snap install sqlmap

To find parameters of the target I use wayback urls.After getting a valid url with parameter simply use the command-

sqlmap -u “http://site.com/sads?asdasd=”

Now to do sql injection on POST request-

Simply save the entire request to a text file(for example test.txt) and go to the endpoint in terminal and run the command-

sqlmap -r test.txt
