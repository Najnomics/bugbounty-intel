# Learning - Part 1 - SQLi

- **Source URL:** https://medium.com/@RainOfDelight/learning-part-1-sqli-c54f8bce463b?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20251126162653/https://medium.com/@RainOfDelight/learning-part-1-sqli-c54f8bce463b
- **Fetched:** 2026-11-22
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/3271 (id 3271)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Learning SQLi

In this series which I will call **Learning** we will learn about different topics, and when I say WE I really mean it. I will learn it and I will try to explain it as well as I can. This way I will understand it better and at the same time it might also help someone along the way. This is not a beginner friendly tutorial as I will jump over the basics. This tutorial might be good to refresh the knowledge or regain it if you already knew some of these tactics but forgot them.

## What is SQLi

SQLi (SQL Injection) is a type of vulnerability in which the attacker can interact with the database in ways he is not supposed to. Most applications need a database in order to store information and retrieve it when needed. From time to time the web server will make a request to the database in order to retrieve SOME SPECIFIC information. When an attacker can execute an SQLi, he can choose to access OTHER SPECIFIC information that he should not be able to access.

Example: A database contains the list of all the items available in the shop. The same database contains also the username and passwords of the users. When the user makes a request to see all the items, the web application talks with the database and retrieve all that information. In some cases, the attacker is able to manipulate the request for the DB and instead of the server asking the database to show all the items, it will ask to see all of the passwords. Anyway all the basic theory is explained far better than I can do in this [portswigger tutorial](https://portswigger.net/web-security/sql-injection). I suggest you learn it from there, and do all the exercises in order to really understand it. Most of the information you see here is taken from their awesome tutorial.

In this tutorial we will take a look at 4 databases:

- Oracle
- Microsoft
- PostgreSQL
- MySQL

## Preliminary steps

Here are the steps you usually take to identify and then explit a SQLi.

1. Check for the presence of SQLi (use ‘ or “ in your parameters and check for errors in the response)
2. Identify the DB
`--comment` not working but
-- comment
`#comment`=>you are in PostgreSQL
`--comment`=>you are in Microsoft/Oracle
3. **Find how many columns does the query you are in have:**
‘ ORDER BY 1--
‘ ORDER BY 2--
‘ ORDER BY 3--
OR
‘ UNION SELECT NULL--
‘ UNION SELECT NULL,NULL--
‘ UNION SELECT NULL,NULL,NULL--
It is very important to use NULL and not other types because NULL are compatible with any type and can be used in place of string, int, bool, etc. Example ‘ UNION SELECT “test”,“test”-- is not useful to understand the number of column because you get an error either if it does not have 2 columns or if one of the 2 columns is not string. Just use NULL and if you get an error you are 100% sure it is because the number of columns is wrong. Anyway the ORDER BY method is the best because you could also research the number of columns using binary search : order by 1, order by 20, order by 10, order by 15…
4. **Find a columns that is a string and you see it in the output:**
‘ UNION SELECT ‘a’,NULL,NULL,NULL--
‘ UNION SELECT NULL,’a’,NULL,NULL--
‘ UNION SELECT NULL,NULL,’a’,NULL--
‘ UNION SELECT NULL,NULL,NULL,’a’--
5. **Read DB type and version:**
‘ UNION SELECT NULL,@@version,NULL,NULL--
But of course, use the right version based on the DB
Oracle: SELECT banner FROM v$version
Oracle: SELECT version FROM v$instance
Microsoft: SELECT**@@version**
PostgreSQL: SELECT**version()**
MySQL: SELECT**@@version**
6. **Find Table names:**
**Oracle**
SELECT \* FROM all\_tables
**PostgreSQL**
SELECT table\_name FROM information\_schema.tables WHERE table\_schema = ‘public’
**Microsoft,MySQL**
SELECT table\_name FROM information\_schema.tables
7. **Find Columns of Table X:**
**Oracle**
SELECT column\_name FROM ALL\_TAB\_COLUMNS WHERE table\_name = ‘your\_table’
**Microsoft, MySQL, PostgreSQL**
SELECT column\_name FROM INFORMATION\_SCHEMA.COLUMNS WHERE table\_name = ‘your\_table’

## **Extracting information**

Extracting Information using UNION.

Scenario: The user asks for the items of category: “toy”. The server asks the database for the items of category toy. The database returns 8 columns(we found that information in step 3), out of which only 4 are visible on the web page(we can see this either empirically or using step 4). The first is the ID and is stored as an integer in the database(we know this thanks to step 4). The second is the price which is also an integer(found in step 4), and the 3rd and 4th columns are strings(found in step 4), which are name and description of the product. Since we can only view those 2 string in the response, we can merge the results of the query with another query we choose, and we must craft this query in such a way that it returns 8 columns, the type of each column match with the original query and in the 3rd and 4th column we put the strings we want to see. More precisely, we could just craft something like

`' UNION SELECT NULL,NULL,name,password,NULL,NULL,NULL,NULL from users--`

As you can see, this input will merge the results of the original query with the data we selected from the DB. In other words, we are reading arbitrary data from the DB.

Scenario 2:

What if the server makes a query that returns ONLY 1 columns, which is a string? How can we read both username and password? 

We can just concatenate this data in a single string. 

**Oracle** -> ‘foo’||’bar’

**Microsoft** -> ‘foo’+’bar’

**PostgreSQL** -> ‘foo’||’bar’

**MySQL** -> ‘foo’ ‘bar’ \[Note the space between the two strings\]

**MySQL** -> CONCAT(‘foo’,’bar’)

The string we can craft would look something like this:

`' UNION SELECT name||~~||passwrod from users- -`

This way we are using a single variable of type string that will look like this:

bob\~\~myPassword882

## Error Based SQLi

Not always you see the results of a query. Sometime the query is executed and you either see an error or not. You have only 1 bit of information. Error/NotError. It worked or it didn’t worked. In this cases other tactics are applied and you can bruteforce the name of the tables, columns and eventually, data inside tables. I will update this part in the future.

## Blind SQLi

Sometimes you don’t even see the error. The injection might work or not and you cannot see it. How do you do in this case? It seems like you don’t even have the single bit of information you had in the Error Based SQLi. But in fact you can create one. You can craft a SQL payload that waits for given amount of seconds in case a condition is verified. You cannot SEE if it worked but you can time the response. If the answer from the server came to you in 2 seconds it means that it worked, if it comes instantly it means it didn’t work. Here you have the single bit of information you needed to apply the same tactics you can apply in the error based SQLi. The only difference is that you will need far more time to get to results.

## Automation

Last thing, you can forget everything and use sqlmap. It is an amazing tool and can do all those checks fast and reliably for you.

Just use **sqlmap -h** to read how to use it.

**sqlmap -u** [**https://mywebsite.com/path?param=aaa**](https://mywebsite.com/path?param=aaa) usually will do the work but it is far better if you also understand what is happening behind the scenes and you how everything works. If you know the theory, you might be able to identify some nice edge cases in which sqlmap do not work as expected.Maybe it’s work learning the theory.

Hope you learned something new. 

Feel free to add information, tips and tricks in the comments and

Have a wonderful day!
