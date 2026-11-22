# SQL Injection

- **Source URL:** https://medium.com/@rajeevranjancom/sql-injection-dc256dd9060e?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20220825134750/https://medium.com/@rajeevranjancom/sql-injection-dc256dd9060e
- **Fetched:** 2026-11-22
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/21 (id 21)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# **SQL Injection**

In this section, I’ll explain what SQL injection is, describe some common examples, explain how to find and exploit various kinds of SQL injection vulnerabilities, and summarize how to prevent SQL injection.

## What is SQL injection (SQLi)?

SQL injection is a web security vulnerability that allows an attacker to interfere with the queries that an application makes to its database. It generally allows an attacker to view data that they are not normally able to retrieve. This might include data belonging to other users, or any other data that the application itself is able to access. In many cases, an attacker can modify or delete this data, causing persistent changes to the application’s content or behavior.

In some situations, an attacker can escalate an SQL injection attack to compromise the underlying server or other back-end infrastructure, or perform a denial-of-service attack.

There are various kinds of SQL injection which are defined based on scope. These are:

Classic SQL injection

Blind SQL injection

Database specific SQL injection

Compound SQLI

SQL injection vulnerability exists because developers do not care about data validation and security. Users’ input must be sanitized before passing into SQL queries, but developers forget to do this or do not properly sanitize. This makes the web application vulnerable to SQL injection attack.

Performing classic SQL injection is easy via browser based attack by injecting queries in various parameters. But it also requires knowledge of SQL queries. For blind SQL injection or another, you need to be an expert with high knowledge of database queries, database architecture and experience. And using manual ways takes a lot of time.

To make the SQL injection attack process easy, developers have also developed SQL injection tools by creating a good detection engine. With every new release, these tools are becoming smarter. These tools take the vulnerable URL as a parameter and then start attacking the target. Based on its detection and attack engine, these tools are capable of detecting the type of attack. Sometimes, a vulnerable URL is protected via session and requires login. So, these tools have also gotten the capability of login into a web application via provided username and password to perform SQL injection in the target application. These tools can perform GET-based, POST-based or cookie-based SQL injection without any problem.

These tools can automatically perform an attack, and in a few minutes, you will get a successful attack result. These tools also allow you to access any table or any column of the database in just a click and attack process. In CLI tools, you can use commands to access data. These tools also let you run SQL queries in the target database. So, you can access, modify or delete data on the target server. These tools also allow attackers to upload or download files from the server.

In this post, we are adding a few open source SQL injection tools. These tools are powerful and can perform automatic SQL injection attacks against the target applications. I will also add the download link to download the tool and try. I tried my best to list the best and most popular SQL injection tools.

# BSQL hacker

BSQL hacker is a nice SQL injection tool that helps you perform a SQL injection attack against web applications. This tool is for those who want an automatic SQL injection tool. It is especially made for Blind SQL injection. This tool is fast and performs a multi-threaded attack for better and faster results.

It supports 4 different kinds of SQL injection attacks:

- Blind SQL Injection
- Time Based Blind SQL Injection
- Deep Blind (based on advanced time delays)
- SQL Injection Error Based SQL Injection

This tool works in automatic mode and can extract most of the information from the database. It comes in both GUI and console support. You can try any of the given UI modes. From GUI mode, you can also save or load saved attack data.

It supports multiple injection points including query string, HTTP headers, POST, and cookies. It supports a proxy to perform the attack. It can also use the default authentication details to login into web accounts and perform the attack from the given account. It supports SSL protected URLs, and can also be used on SSL URLs with invalid certificates.

The BSQL Hacker SQL injection tool supports MSSQL, ORACLE and MySQL. But MySQL support is experimental and is not as effective on this database server as it is for the other two.

# SQLmap

SQLMap is the open source SQL injection tool and most popular among all SQL injection tools available. This tool makes it easy to exploit the SQL injection vulnerability of a web application and take over the database server. It comes with a powerful detection engine which can easily detect most of the SQL injection related vulnerabilities.

It supports a wide range of database servers, including MySQL, Oracle, PostgreSQL, Microsoft SQL Server, Microsoft Access, IBM DB2, SQLite, Firebird, Sybase, SAP MaxDB and HSQLDB. Most of the popular database servers are already included. It also supports various kind of SQL injection attacks, including boolean-based blind, time-based blind, error-based, UNION query-based, stacked queries and out-of-band.

One good feature of the tool is that it comes with a built-in password hash recognition system. It helps in identifying the password hash and then cracking the password by performing a dictionary attack.

This tool allows you to download or upload any file from the database server when the db server is MySQL, PostgreSQL or Microsoft SQL Server. And only for these three database servers, it also allows you to execute arbitrary commands and retrieve their standard output on the database server.

After connecting to a database server, this tool also lets you search for specific database name, specific tables or for specific columns in the whole database server. This is a very useful feature when you want to search for a specific column but the database server is huge and contains too many databases and tables.

# SQLninja

SQLninja is a SQL injection tool that exploits web applications that use a SQL server as a database server. This tool may not find the injection place at first. But if it is discovered, it can easily automate the exploitation process and extract the information from the database server.

This tool can add remote shots in the registry of the database server OS to disable data execution prevention. The overall aim of the tool is to allow the attacker to gain remote access to a SQL database server.

It can also be integrated with Metasploit to get GUI access to the remote database. It also supports direct and reverse bindshell, both TCP and UDP.

This tool is not available for Windows platforms. It is only available for Linux, FreeBSD, Mac OS X and iOS operating systems.

# Safe3 SQL injector

Safe3 SQL injector is another powerful but easy to use SQL injection tool. Like other SQL injection tools, it also makes the SQL injection process automatic and helps attackers in gaining the access to a remote SQL server by exploiting the SQL injection vulnerability. It has a powerful AI system which easily recognizes the database server, injection type and best way to exploit the vulnerability.

It supports both HTTP and HTTPS websites. You can perform SQL injection via GET, POST or cookies. It also supports authentication (Basic, Digest, NTLM HTTP authentications) to perform a SQL injection attack. The tool supports a wide range of database servers including MySQL, Oracle, PostgreSQL, Microsoft SQL Server, Microsoft Access, SQLite, Firebird, Sybase and SAP MaxDB database management systems.

For MYSQL and MS SQL, it also supports read, list or write any file from the database server. It also lets attackers execute arbitrary commands and retrieve their output on a database server in Oracle and Microsoft SQL server. It also supports web path guess, MD5 crack, domain query and full SQL injection scan.

# SQLSus

SQLSus is another open source SQL injection tool and is basically a MySQL injection and takeover tool. This tool is written in Perl and you can extend the functions by adding your own codes. This tool offers a command interface which lets you inject your own SQL queries and perform SQL injection attacks.

This tool claims to be fast and efficient. It claims to use a powerful blind injection attack algorithm to maximize the data gathered. For better results, it also uses stacked subqueries. To make the process even faster, it has multi-threading to perform attacks in multiple threads.

Like other available SQL injection tools, it also supports HTTPS. It can perform attacks via both GET and POST. It also supports cookies, socks proxy, HTTP authentication, and binary data retrieving.

If the access to information\_schema is not possible or the table does not exist, it can perform a brute force attack to guess the name of the table. With this tool, you can also clone a database, table, or column into a local SQLite database, and continue over different sessions.

If you want to use a SQL injection tool against a MySQL attack, you will prefer this tool because it is specialized for this specific database server.

# Mole

Mole or (The Mole) is an automatic SQL injection tool available for free. This is an open source project hosted on Sourceforge. You only need to find the vulnerable URL and then pass it in the tool. This tool can detect the vulnerability from the given URL by using Union based or Boolean based query techniques. This tool offers a command line interface, but the interface is easy to use. It also offers auto-completion on both commands and command arguments. So, you can easily use this tool.

Mole supports MySQL, MsSQL and Postgres database servers. So, you can only perform SQL injection attacks against these databases. This tool was written in Python and requires only Python3 and Python3-lxml. This tool also supports GET, POST and cookie based attacks. But you need to learn commands to operate this tool. Commands are not typical but you need to have them. List those commands or learn, it is your personal choice.

**Impact of SQL injection on your applications:**

- **Steal credentials** — attackers can obtain credentials via SQLi and then impersonate users and use their privileges.
- **Access databases** — attackers can gain access to the sensitive data in database servers.
- **Alter data** — attackers can alter or add new data to the accessed database.
- **Delete data** — attackers can delete database records or drop entire tables.
- **Lateral movement** — attackers can access database servers with operating system privileges, and use these permissions to access other sensitive systems.

# Real-Life SQL Injection Attack Examples

Over the past 20 years, many SQL injection attacks have targeted large websites, business and social media platforms. Some of these attacks led to serious data breaches. A few notable examples are listed below.

# Breaches Enabled by SQL Injection

- **GhostShell attack** — hackers from APT group Team GhostShell targeted 53 universities using SQL injection, stole and published 36,000 personal records belonging to students, faculty, and staff.
- **Turkish government** — another APT group, RedHack collective, used SQL injection to breach the Turkish government website and erase debt to government agencies.
- **7-Eleven breach** — a team of attackers used SQL injection to penetrate corporate systems at several companies, primarily the 7-Eleven retail chain, stealing 130 million credit card numbers.
- **HBGary breach** — hackers related to the Anonymous activist group used SQL Injection to take down the IT security company’s website. The attack was a response to HBGary CEO publicizing that he had names of Anonymous organization members.

# Notable SQL Injection Vulnerabilities

- **Tesla vulnerability** — in 2014, security researchers publicized that they were able to breach the website of Tesla using SQL injection, gain administrative privileges and steal user data.
- **Cisco vulnerability** — in 2018, a SQL injection vulnerability was found in Cisco Prime License Manager. The vulnerability allowed attackers to gain shell access to systems on which the license manager was deployed. Cisco has patched the vulnerability.
- **Fortnite vulnerability** — Fortnite is an online game with over 350 million users. In 2019, a SQL injection vulnerability was discovered which could let attackers access user accounts. The vulnerability was patched.

# Types of SQL Injection Attacks

There are several types of SQL injection:

- **Union-based SQL Injection** — Union-based SQL Injection represents the most popular type of SQL injection and uses the UNION statement. The UNION statement represents the combination of two select statements to retrieve data from the database.
- **Error-Based SQL Injection** — this method can only be run against MS-SQL Servers. In this attack, the malicious user causes an application to show an error. Usually, you ask the database a question and it returns an error message which also contains the data they asked for.
- **Blind SQL Injection** — in this attack, no error messages are received from the database; We extract the data by submitting queries to the database. Blind SQL injections can be divided into boolean-based SQL Injection and time-based SQL Injection.
- SQLi attacks can also be classified by the method they use to inject data:
- **SQL injection based on user input** — web applications accept inputs through forms, which pass a user’s input to the database for processing. If the web application accepts these inputs without sanitizing them, an attacker can inject malicious SQL statements.
- **SQL injection based on cookies** — another approach to SQL injection is modifying cookies to “poison” database queries. Web applications often load cookies and use their data as part of database operations. A malicious user, or malware deployed on a user’s device, could modify cookies, to inject SQL in an unexpected way.
- **SQL injection based on HTTP headers** — server variables such HTTP headers can also be used for SQL injection. If a web application accepts inputs from HTTP headers, fake headers containing arbitrary SQL can inject code into the database.
- **Second-order SQL injection** — these are possibly the most complex SQL injection attacks, because they may lie dormant for a long period of time. A second-order SQL injection attack delivers poisoned data, which might be considered benign in one context, but is malicious in another context. Even if developers sanitize all application inputs, they could still be vulnerable to this type of attack.

# SQL Injection Code Examples

Let’s look at two common examples of SQL injection attacks.

# Example 1: Using SQLi to Authenticate as Administrator

This example shows how an attacker can use SQL injection to circumvent an application’s authentication and gain administrator privileges.

Consider a simple authentication system using a database table with usernames and passwords. A user’s POST request will provide the variables user and pass, and these are inserted into a SQL statement:

sql = “SELECT id FROM users WHERE username=’” + user + “‘ AND password=’” + pass + “‘“

The problem here is that the SQL statement uses concatenation to combine data. The attacker can provide a string like this instead of the pass variable:

password’ OR 5=5

The resulting SQL query will be run against the database:

SELECT id FROM users WHERE username=’user’ AND password=’pass’ OR 5=5'

Because 5=5 is a condition that always evaluates to true, the entire WHERE statement will be true, regardless of the username or password provided.

The WHERE statement will return the first ID from the users table, which is commonly the administrator. This means the attacker can access the application without authentication, and also has administrator privileges.

A more advanced form of this attack is where the attacker adds a code comment symbol at the end of the SQL statement, allowing them to further manipulate the SQL query. The following will work in most databases including MySQL, PostgreSQL, and Oracle:

‘ OR ‘5’=’5' /\*

# Example 2: Using SQLi to Access Sensitive Data

In this example, the following code obtains the current username, and searches for items matching a certain item name, where the owner is the current user.

…

string userName = ctx.getAuthenticatedUserName();

string query = “SELECT \* FROM items WHERE owner = “‘“

\+ userName + “‘ AND itemname = ‘“

\+ ItemName.Text + “‘“;

…

This code has the same weakness as in the previous example — the use of concatenation. After combining the username and item name, the code creates the following query:

SELECT \* FROM items

WHERE owner =

AND itemname = ;

If the attacker provides the following string for itemname:

Widget’ OR 5=5

The SQL statement becomes:

SELECT \* FROM items

WHERE owner = ‘John’

AND itemname = ‘Widget’ OR 5=5';

Which is the same as: SELECT \* FROM items;

This means the query will return the data of the entire table, giving the attacker unauthorized access to sensitive data.

# Example 3: Injecting Malicious Statements into Form Field

This is a simple SQL injection attack based on user input. The attacker uses a form that requires first name and last name as inputs. The attacker inputs:

- First name: malicious’ex
- Last name: Smith

The attacker’s first name variable contains a malicious expression, which we denoted as ‘ex. The SQL statement that processes the form inputs looks like this:

SELECT id, firstname, lastname FROM authors

Once the attacker injects a malicious expression into the first name, the statement looks like this:

SELECT id, firstname, lastname FROM authors WHERE firstname = ‘malicious’ex’ and lastname =’newman’

The database identifies incorrect syntax due to the single apostrophe, and tries to execute the malicious statement.

# SQL Injection Prevention

# Defense Option 1: Prepared Statements (with Parameterized Queries)

Prepared statements are easy to learn and use, and eliminate the problem of SQL injection. They force you to define SQL code, and pass each parameter to the query later, making a strong distinction between code and data.

If an attacker supplies a malicious string like in the above examples, for example providing John’ or 1=1 for a username, the prepared statement will evaluate this as a literal string. It will look for a user named John’ or 1=1 (and fail, because no such user exists) instead of evaluating this statement as code.

Prepared statements are available in all programming languages. Here is an example in Java. To be on the safe side, OWASP recommends validating the input parameter just in case.

// Separate definition of input variable

String custname = request.getParameter(“customerName”);

// Separate definition of SQL statement

String query = “SELECT account\_balance FROM user\_data WHERE user\_name = ? “;

// PreparedStatement command securely combines inputs and SQL syntax

PreparedStatement pstmt = connection.prepareStatement( query );

pstmt.setString( 1, custname);

ResultSet results = pstmt.executeQuery( );

# Defense Option 2: Stored Procedures

Stored procedures are similar to prepared statements, only the SQL code for the stored procedure is defined and stored in the database, rather than in the user’s code. In most cases, stored procedures can be as secure as prepared statements, so you can decide which one fits better with your development processes.

There are two cases in which stored procedures are not secure:

- **The stored procedure includes dynamic SQL generation** — this is typically not done in stored procedures, but it can be done, so you must avoid it when creating stored procedures. Otherwise, ensure you validate all inputs.
- **Database owner privileges** — in some database setups, the administrator grants database owner permissions to enable stored procedures to run. This means that if an attacker breaches the server, they have full rights to the database. Avoid this by creating a custom role that allows storage procedures only the level of access they need.

Here is an example of a stored procedure in Java (Java calls it a CallableStatement). We assume that the sp\_getAccountBalancer stored procedure implements the same logic as the prepared statement in option 1 above.

// Separate definition of user inputs

String custname = request.getParameter(“customerName”);

// Executing the stored procedure sp\_getAccountBalancer

try {

CallableStatement cs = connection.prepareCall(“{call

sp\_getAccountBalance(?)}”);

cs.setString(1, custname);

ResultSet results = cs.executeQuery();

// result set handling

} catch (SQLException se) {

// logging and error handling

}

# Defense Option 3: Allow-list Input Validation

This is another strong measure that can defend against SQL injection. The idea of allow-list validation is that user inputs are validated against a closed list of known legal values.

For example, if a user input is used to select a database table, you can use code like this to ensure that it can only match one of several, known table names:

String tableName;

switch(PARAM):

case “Value1”: tableName = “fooTable”;

break;

case “Value2”: tableName = “barTable”;

break;

…

default : throw new InputValidationException(“unexpected value

Provided” + “ for table name”);

Another safe way to handle user inputs is to convert them to a non-string form. For example, if the user input determines whether the query should be ordered in ascending or descending order, the input can be converted to a boolean. And then this boolean value is used to determine the sort order:

public String someMethod(boolean sortOrder) {

String SQLquery = “some SQL … order by Salary “ + (sortOrder ? “ASC” :

“DESC”);\`

…

# Defense Option 4: Escaping All User-Supplied Input

Escaping means to add an escape character that instructs the code to ignore certain control characters, evaluating them as text and not as code.

This option is the least secure of the four, and should only be used as a last resort. This is because escaping user input is only effective if the code escapes all possibilities of control characters, and attackers come up with numerous creative ways to inject them. **Therefore, OWASP does not recommend this method** and advises the use of options 1 or 2 above.

# Preventing SQL Injection Attack

By shifting DAST scans left, and integrating them into the SDLC, developers and application security professionals can detect vulnerabilities early, and remediate them before they appear in production. Bright completes scans in minutes and achieves zero false positives, by automatically validating every vulnerability. This allows developers to adopt the solution and use it throughout the development lifecycle.

# Conclusion

These are a few automatic SQL injection tools which you can try to perform a SQL injection attack. In case I missed any, please share it with us via comments. A few of these tools also come with penetration testing specific operating systems. If you are using Backtrack or Kali Linux, you already have a few of these tools. So, you can try them in those operating systems.

Note: We do not encourage any illegal activity with these tools. Use these tools only for learning purposes and perform only on websites you own. We will not be responsible for any damage you cause with these tools.
