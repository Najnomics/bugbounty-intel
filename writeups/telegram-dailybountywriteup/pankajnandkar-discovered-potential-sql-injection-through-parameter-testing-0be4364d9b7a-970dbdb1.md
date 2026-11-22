# Discovered potential SQL injection through parameter testing

- **Source URL:** https://medium.com/@pankajnandkar/discovered-potential-sql-injection-through-parameter-testing-0be4364d9b7a?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20240314121438/https://medium.com/@pankajnandkar/discovered-potential-sql-injection-through-parameter-testing-0be4364d9b7a
- **Fetched:** 2026-11-22
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/5460 (id 5460)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Discovered potential SQL injection through parameter testing

After a long break, I resumed bug hunting last week, focusing on a widely used financial website handling payments. While going through numerous pages and inspecting various endpoints, I came across one that takes parameters like userID, merchantCode, currencyType ,transactionDate, PID, SID, DatePublished, and others.

While conducting a simple manual test, I included special characters such as ‘‘“, `') ")` )) –-’and queries like ‘or + =,’ leading to a SQL error. I experimented with various payloads, checking for SQL injection on each parameter using both manual testing and automated tools like Ghauri and Sqlmap.

Often encountering errors due to a Web Application Firewall (WAF), I attempted to uncover the origin IP behind the WAF. Despite using tools like Censys and SecurityTrails, I couldn’t find the origin IP. My next approach involved sending a non-allocated email to the target domain. I crafted a fake email from my own email ID, using a modified address like anonymous@example.com. After sending the email, I received a bounce-back from the target domain after a few minutes.

Upon reviewing the bounce-back email, I successfully identified the origin IP, which is hosted on AWS. To assess its viability for bypassing the WAF, my next step is to confirm whether the IP is static or not. A static IP is crucial for effective bypassing strategies.

After conducting tests using the command

curl -k -H “Host: example.com” [https://123.12.123.12](https://123.12.123.12)


I examined the website header and obtained confirmation of a static IP.

With the confirmed static IP, I proceeded to retest the payloads for SQL injection on every parameter. I conducted both manual testing and automated testing using tools like SQLMap and Ghauri.

After persistent exploration, I gained access to the database names and successfully extracted crucial data. Following this discovery, I promptly reported the issue, and the bug has now been fixed.
