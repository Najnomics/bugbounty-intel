# My First Bounty

- **Source URL:** https://medium.com/@adebayosec/my-first-bounty-a-story-of-a-blind-sql-injection-69d9ad6716b6?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20240829220835/https://medium.com/@adebayosec/my-first-bounty-a-story-of-a-blind-sql-injection-69d9ad6716b6
- **Fetched:** 2026-11-22
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/6704 (id 6704)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
Hello guys! My name is torious, and I want to share how God helped me get my first bounty after lots of N/As, duplicates, and many months of hunting. Before we dive into it, I hope this encourages myself and every beginner bounty hunter reading this to not give up. It seems difficult, but it is not impossible. Consistency and persistence does the magic, you have to keep showing up day by day and believe in yourself now more than ever.

To begin, let’s call the target *redacted.com and* subdomain *sub.redacted.com*. The vulnerability was a Blind SQL injection affecting a subdomain hosting a third party company’s analytics service. In case you wonder what a blind SQL injection is, here’s a short summary.

Blind SQL injection is a technique used by attackers to exploit vulnerabilities in web applications that interact with databases. Unlike traditional SQL injection, where error messages or visible changes in application behavior provide immediate feedback to attackers, blind SQL injection attacks rely on inferential techniques to extract information indirectly.


First step is always recon for me, and I start with subdomain enumeration using the tool **subfinder** and parsing the results to **httpx**. Httpx is a tool used to efficiently identify and analyze web server configurations, verify HTTP responses, and diagnose potential vulnerabilities or misconfigurations. I personally use the -td and -ip flags so the tool can append the technology running on the sub and the IP addresses to the results.

While testing each subdomain, I came across *sub.redacted.com* and it contained an admin login page. The results from httpx showed it ran a PHP and MySQL and also displayed the IP address (which will later be instrumental). In an attempt to sign in, I sent the request to burpsuite. The request was a POST request and the *login\_name* parameter contained the username i previously input.

The parameter was a good point to test for injections as it was parsing it into the database, so I went ahead to append a ‘ to the value and to my surprise it gave me a 500 server error. A 500 server error is a strong pointer of an injection vulnerability, and since I knew it was running MySQL, i decided to try the basic MySQL injection payloads but WAF was blocking them.

Using Godfatherorwa tips of bypassing waf, I attempted to bypass using Origin IP. I decided to try the IP address that was previously discovered by httpx, check it with Shodan and to my surprise, it worked! Accessing the sub from the origin IP made it totally free from the WAF’s security mechanisms. Now, I was able to test the injection properly and directly input the a time-based payload to cause the database to delay for 10 seconds in this case.

`‘XOR(if(now()=sysdate(),(sleep((((10))))),0))XOR’X`
The extra brackets are for waf bypassing but later on, I realized I did not need so many brackets. On sending the request, ths payload worked and the delay occured

I sent the request to Ghauri to further confirm and was able to enumerate database names. Afterwards, I quickly wrote the report, made a video POC and reported to the company. After some weeks, I was rewarded with a bounty of €500.

To my fellow beginner hunters yet to get the first bounty, I hope you were able to learn something new from this and also get motivated to never stop on no account. Special shoutout to my bro Olamdeen for the great help so far. There’s a whole journey ahead of us and I wish us all the best.

I’d love to meet you on LinkedIn and Twitter
