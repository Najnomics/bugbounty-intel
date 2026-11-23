# #2. Bug Bounty POC

- **Source URL:** https://cyb3rmind.medium.com/2-bug-bounty-poc-time-based-sql-injection-to-dump-database-f8cfa089f393?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20251009224624/https://cyb3rmind.medium.com/2-bug-bounty-poc-time-based-sql-injection-to-dump-database-f8cfa089f393
- **Fetched:** 2026-11-23
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/6091 (id 6091)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# #2. Bug Bounty POC: Time-Based SQL Injection to Dump Database

Hello👋 and welcome, fellow cyber explorers!. Today, I’m excited to share my latest write-up on time-based SQL injection💉, where I’ll walk you through the method of extracting data from a database through Time-Based SQL Injection.

## Description:

Time-based SQL injection is a type of SQL injection attack where the attacker manipulates the SQL query execution time to infer information from the database. Unlike traditional SQL injection attacks that directly return data in the response, time-based attacks exploit the delay in server response caused by specific SQL query constructs.


## Impact of Time-Based Blind SQL Injection

1. Data Extraction: Attackers can use time-based techniques to extract sensitive data from the database slowly. By injecting carefully crafted queries that introduce delays, they can retrieve information character by character, such as usernames, passwords, or other confidential data.
2. Database Discovery: Through time delays, attackers can gain insights into the database schema and structure. They can use this information to understand how the database is designed, the types of tables, and potentially the relationships between different data entities.
3. Denial of Service (DoS): Time-based SQL injection attacks can also be used to degrade the performance of the database or the application itself by causing excessive load. By injecting long-running queries, attackers can impact the responsiveness of the system and many more.

**Let’s start …**

So, I was testing an Android application for one of the program. I’ve reported different findings with the app, but I thought to write an article on this vulnerability.

At first I installed the app and tried to login but the application was not allowing me to login and thrown me an error of “Something Went Wrong”, this happened because of SSL pinning. Then, I used the Frida to bypass the SSL pinning which was half way bypassed but still there was **okhttp3** related pinning which I was unable to bypass it.

When I checked the http history in Burpsuite, there was the login request with few other API requests.

## Steps to Reproduce:

1. The activity which caught my attention is the **EMP\_ID** parameter after trying to login using the random values.

2\. The discovered endpoint was **/api/business/business\_kpi** which was having the employee ID parameter.

3\. There I tried to add the “ **’** ”, where it gave 500 Internal server error.

4\. Then I added ***EMP\_ID=3710+AND+1=0 —*** , I noticed that in response the data is changed by adding.

5\. By checking the behavior, further I used **SQLMAP** with the burp POST request, I got the below vulnerable payload which I tried in burp request and observed a delay as shown in the screenshot below.

**Vulnerable Payload:** EMP\_ID=4727 AND 4900=DBMS\_PIPE.RECEIVE\_MESSAGE(CHR(114)||CHR(105)||CHR(105)||CHR(113),5)&LEVEL=UH&UNIT=BHAG

9\. To retrieve the information, I saved the burp request and run the *SQLMAP* using below command.

**sqlmap -r burprequest.txt -technique=T — dbs**


By using the tool, I was able to retrieve the database and further sensitive information.

**sqlmap -r burprequest.txt -technique=T -D \<database\_name> — tables**


Further, I tried extracting the details within the databases.

**sqlmap -r burprequest.txt -technique=T -D \<database\_name> -T — columns**


At last I reported the vulnerability to the program with all the details and impact. Looking at the criticality the program responded back and within a day they fixed the issue.

**NOTE: Extracted data was deleted ;)**

So, that’s it for now and thanks for reading and I appreciate you taking the time to read. For other such writeups do visit the [**writeups**](/).

If you found it useful, please click the button 👏and share it with others who have similar interests! + Feedback is always appreciated!!😊
