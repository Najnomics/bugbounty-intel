# Utilizing Historical URLs of an Organization to successfully execute SQL queries — Blind SQLi

- **Source URL:** https://medium.com/@ar_hawk/utilizing-historical-urls-of-an-organization-to-successfully-execute-sql-queries-blind-sqli-3526d9c3863d?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20230826101604/https://medium.com/@ar_hawk/utilizing-historical-urls-of-an-organization-to-successfully-execute-sql-queries-blind-sqli-3526d9c3863d
- **Fetched:** 2026-11-22
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/2816 (id 2816)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Utilizing Historical URLs of an Organization to successfully execute SQL queries — Blind SQLi

--

# TL;DR

I was working on a target and asked to find something but not taking much time, so this time I decided not to do deep reconnaissance and only start with the target domain which is their main web application. While analyzing I found one URL with a parameter `id=` which I exploited and found it vulnerable to **Time based Blind SQL Injection**.

As I mentioned this time, I didn’t performed any recon, but I have adapted a different methodology though a very basic but definitely worth to try once.


# Methodology — Getting Started with Target Domain

- Let’s take the target domain as `redacted.com`.
- I started with visiting the target domain like a normal user of the web application. The web application don’t have much features and functionality to test with but has *some products that can be viewed and searched*.
- Then I have used **wayback machine** to find out all the URLs associated with that domain. Typically, I have used `waybackurls` tool to find out URLs via Command-line.

`$ echo redacted.com | waybackurls | anew urls.txt`
- Now, I have all the urls saved in a file called `urls.txt`. I start with gathering the interesting URLs such as ***URLs with id parameter, redirect parameter, url parameter, etc***. Sometimes, I also use the following wordlist to FUZZ for parameters on interesting subdomains “ [*https://github.com/PortSwigger/param-miner/blob/master/resources/params*](https://github.com/PortSwigger/param-miner/blob/master/resources/params) ”

`$ cat urls.txt | grep "id=" | anew temp-sqli.txt`
- From the file `temp-sqli.txt` I found an interesting URL something like `https://www.redacted.com/?attachment_id=123` .

# Analyzing the ID Parameter — Hacking Started

- I started with appending a *single quote(‘) and double quote(“)* at the end of the URL but didn’t found any SQL Error or DB Error. But as this looks interesting to me, I wanted to give a try for all type of SQL Injections.

```
https://www.redacted.com/?attachment_id=123'
https://www.redacted.com/?attachment_id=123"
```
- From the wappalyzer, I found the web application is using the **MySQL DB**. I wanted to try SQLi, so I gathered some SQLi payloads and tried them on the above URL.

- I have used Burp Suite to send the request and check the time difference if any while executing Time based SQLi payloads. Though I can use browser to check, but for the PoC purpose I have used Burp Suite. Below request has no SQLi payload and taking less time in generating response.

- I have found a payload `" AND 4564=(SELECT 4564 FROM PG_SLEEP(11)) OR "04586"="4586--` that worked for me and successfully had a sleep of ***11 seconds*** on the web application indicating the successful execution of **Time-based Blind SQL Injection** attack. The complete URL with payload looks like:

`$ curl https://www.redacted.com/?attachment_id=123" AND 4564=(SELECT 4564 FROM PG_SLEEP(11)) OR "04586"="4586--`
- From the above screenshot, It was clearly found the increment in time taken to complete the request with the SQLi payload which confirms the presence of the vulnerability. Also the web application was taking time while loading on the web browser.

*Note: I didn’t exploited it further because of time constraint I have during the testing, but I guess I can exploit it to find some sensitive information.*

# Conclusion & Tips

- I would recommend to always check **wayback machine** to find interesting URLs and parameters to get a starting point for finding vulnerabilities and misconfiguration.
- The vulnerability is basic and easy to find in this case at-least 😆, but the impact of it depends on the web application, say if *a web application which is used in generating the revenue of that organization (simply in the product application of the organization), then it would affect the business of that organization which will lead to financial loss and bad user experience*.

*Thanks for reading, hope you enjoyed and learned something from this blog.*

*If you have any questions, DM at https://twitter.com/AayushVishnoi10.*
