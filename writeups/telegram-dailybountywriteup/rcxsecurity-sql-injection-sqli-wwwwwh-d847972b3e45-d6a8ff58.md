# SQL Injection (SQLi)

- **Source URL:** https://medium.com/@rcxsecurity/sql-injection-sqli-wwwwwh-d847972b3e45?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20240105193556/https://medium.com/@rcxsecurity/sql-injection-sqli-wwwwwh-d847972b3e45
- **Fetched:** 2026-11-22
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/4868 (id 4868)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# SQL Injection (SQLi): WWWWWH?

--

In the second installment of **WWWWWH** ([first article here](https://www.cyberseccafe.com/post/reflected-cross-site-scripting-xss-wwwwwh)), a series covering the **W**ho, **W**hat, **W**hen, **W**here, **W**hy, and **H**ow of different web vulnerabilities, we’ll be diving into SQL Injection (**SQLi**). The purpose of this exercise is to not only understand how to perform vulnerabilities, but to understand them from a holistic, end-to-end perspective. Many people understand the basics of *How* to perform a vulnerability, but don’t necessarily think about the rest of the equation.

# SQL Injection

SQL Injection is a vulnerability that allows an attacker to interfere with the queries that an application makes to a database. SQLi vulnerabilities commonly happen when developers don’t properly validate or escape user input. You can detect it through visible responses in the application, but most cases of SQLi are blind and will require more complicated techniques. Malicious actors can attempt SQLi to achieve varying goals surrounding sensitive data, and these attacks generally have critical implications.

# WWWWWH Analysis

**Who?**

After finding an SQLi vulnerability in an application, it’s time to find a target. You’ll be looking to direct this attack at whoever owns the sensitive data of interest. This could be the customer of an application the vulnerability was found in, or, even the root website where all user activity occurs. The idea will be to target the instance that has access to restricted information of interest.

**What?**

SQLi is a server-side vulnerability targeting a database through the client-side application. The attacker makes calls to the database through the API endpoints that execute the queries against the server.

**When?**

This vulnerability offers opportunities to access restricted data, so ideal timing will generally be during off-hours. Since main use cases of this attack would be data exfiltration or accessing sensitive data, performing this attack when the victim is less likely to be looking at alerts is paramount. This means the Incident Response team may also take longer to flag it as malicious activity and shut it down.

**Where?**

This vulnerability occurs within the application when parameterized values aren’t being sanitized correctly in a query against a database. Look for actions where queries are being used to retrieve information, show sensitive data, or even user logins. Testing values in URL parameters, HTTP Request bodies, and request headers are a great place to start.

**Why?**

The ramifications of an SQLi vulnerability for an organization can be devastating. Most attacks are focused on sensitive data access, exfiltration, or deletion. But, the attack can also be used to subvert application logic to bypass authentication. Malicious actors can use SQLi to sensitive data like credentials, financial information, or other restricted information in a database and use it to blackmail/extort organizations for ransom.

**How?**

After finding an application with a valid attack vector, you’ll want to start delivering payloads against the input, probing for a valid SQLi vulnerability. As the attacker, it is ideal if the SQLi vulnerability reflects any messages in the application or response. However, as mentioned before, most SQLi vulnerabilities will be blind, meaning you’ll have to use different techniques to infer what is happening behind the scenes. Let’s take a look at some sample SQLi injection techniques.

For example, imagine a fictional shopping application that has an endpoint of interest: A filter for products using a “type” field. An example of the URL looks like this:

*https://store.com/shop?type=Athletics*

Now, imagine that the SQL query also has an “active” parameter to decide whether to show or hide items in the shop. This “type” parameter is placed into the query like the following:

`SELECT * FROM shop WHERE type = 'insert_type' and active = 1`
**\~ Simple Boolean \~**

A simple boolean could hit this endpoint to reveal hidden data. If we inject the query with a boolean that evaluates to true with a comment after, it will comment out the remainder of the query, and display everything as a result. The attack will look something like:

*https://store.com/shop?type=Athletics’+OR+1=1–*

This will cause the query to evaluate to always true:

``SELECT * FROM shop WHERE type = 'Athletics` OR 1=1–' and active = 1``
**\~ UNION Attack \~**

A Union attack can be used to retrieve data from another table within the database. In our example shopping application, there is another table named “users” that contains all usernames and passwords stored for the website. In order for this to work, you’ll need to ensure that the column counts for both queries match up. In the application, you find a list view that uses the same query, returning the name and vendor of products. So, you assume the query looks like the following:

``SELECT name, vendor FROM shop WHERE type = 'Athletics` and active = 1``
You can craft up a UNION attack to target the “users” table of the database, and exfiltrate the usernames and passwords with the following payload:

*https://store.com/shop?type=Athletics’+UNION+SELECT+username,password+FROM+users–*

This causes the query to now look like the following, and would now display usernames and passwords within the list view.

``SELECT name, vendor FROM shop WHERE type = 'Athletics` UNION SELECT username, password FROM users–' and active = 1``
**\~ Time Delays \~**

Time delays are a great way to test blind SQLi vulnerabilities. You’ll need to pair the delay with a conditional boolean that will trigger a delay if the condition is met. This means it will cause a visible delay in loading the application if the condition evaluates to true. We can inject the following into the URL:

*https://store.com/shop?type=Athletics’;+IF+(SELECT+COUNT(username)+FROM+users+WHERE+username=’administrator’+AND=SUBSTRING(password,1,1=’a’)=1+WAITFOR+DELAY+’0:0:10’--*

This much more complex injection method uses a boolean to test what the first character of the password is for the user “administrator”. If the first character is the “a” character, a 10 second time delay will trigger.

`SELECT name, vendor FROM shop WHERE type = 'Athletics'; IF (SELECT COUNT(username) FROM users WHERE username='administrator' AND=SUBSTRING(password,1,1='a')=1 WAITFOR DELAY '0:0:10' - ' and active = 1`
While not ideal, an attacker can use this to brute force a user’s password, guessing one letter at a time until it is complete.

# WWWWWH

As you can see, SQL Injection can have very dangerous implications. There are many different SQLi techniques outside of what was covered in the How? section, and often takes some creativity to exploit the vulnerability. From a defensive perspective, it’s important for developers to consider best practices like using prepared SQL statements, validating user input where necessary, implementing a WAF to detect/block injection attempts, and to limit privileges.

If you’ve enjoyed this dive into the SQL Injection vulnerability and want to explore some more cybersecurity content, you can read more on my blog [here](https://www.cyberseccafe.com/). Or, if you want more insights on the InfoSec and Tech industries, you can find more from me on [Twitter/X](https://twitter.com/rcxsecurity)!
