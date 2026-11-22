# How I Got 4 SQLI Vulnerabilities At One Target Manually Using The Repeater Tab

- **Source URL:** https://medium.com/@bug4y0u/how-i-got-4-sqli-vulnerabilities-at-one-target-manually-using-the-repeater-tab-ed4eb1f84147?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20251129175941/https://medium.com/@bug4y0u/how-i-got-4-sqli-vulnerabilities-at-one-target-manually-using-the-repeater-tab-ed4eb1f84147
- **Fetched:** 2026-11-22
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/3910 (id 3910)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# How I Got 4 SQLI Vulnerabilities At One Target Manually Using The Repeater Tab

*Hi everyone, I’m Yousseff, A Junior Computer Science Student, and Cyber Security Enthusiast, Always hungry for a deep understanding of the things I work with and exploit, I come from a Different background which is Network Pentesting and AV Evasion Techniques and AD Attacks :), I learned a lot from writeups and noticed that most of the people don’t hunt on SQLI Manually except few people that are experts that do those bypasses and obfuscation Techniques, so Today I’m gonna put you on the road of understanding how you should think when testing Manually for SQLI, and if you understand every single word in this writeup all you need is just sharp your skills at obfuscations and encoding bypasses techniques to bypass WAFs, by the time you could increase your bypasses skills from an advanced Writeups and bypass Complex WAFs Writeups, but for today you need to know how to think when you need to Test it Manually.*

since the target is a private, let’s call it: ***bug4y0u.com,*** let’s jump into the SQLI without wasting any time :)


For the sake of your valuable time, if you are a SQLI Hunter professional who comes here looking for payloads that worked with me, go and read from the second bug until the fourth bug and leave the first bug cuz I explained in it a very useful principle details to those that are not hunting Manual at all, so yeah it’s trivial if you are a skillful SQLI Manual Hunter.

## *First Bug:*

*1st Step*

here is an endpoint that was used for downloading audio of some music.


but think with me what would happen if we put a single quote?


ahhh, the results changed completely there is no audio coming back within the response so yeah that will be your first hit, putting a single quote or a double quote at the parameters you face and observe the response if there is any tiny change, it will be definitely vulnerable to SQLI, cuz this will indicate that the backend didn’t sanitize the inputs properly, and Literlay I mean it *(tiny change), but in some cases there’s a targets that configured manually when recieves those dangerous character it will give you back 200OK but it’s a custom page telling you that the resource is not found on the server or something like that, I didn’t mean this change, I mean the change within the same response’s endpoint not different response’s comes from another endpoint,* this includes changing within response’s length, response’s content, and sometimes response’s time since there are some cases the backend would handle the query in a different way that makes it takes much time if there’s an error in the SQL Syntax or the input is a very large string or number, so yeah just detect any abnormal behavior in the response, and you will go from here as I will explain in a couple of minutes here with you.


### 2nd Step:

Nice, until this point, we know that injecting a single quote will break the SQL Syntax and result in not giving us the audio in response, so now we observed that we are inside the SQL Statement that is closed with a single quote, but what if we put ***AND 1=1'+ — +-*** besides the number id of the audio to comment the rest of the Query like:


still doesn’t work :(

what about the hash ***#*** sign?


same :(

but what if we just trying to inject AND 1=1 only and didn’t comment anything after the Query.


ahhh, now it works xD

so now we know that from here we can continue the exploitation phase with Boolean-based SQLI without any need to break the SQL Statment or close quotes, just think deeply what you can do to acheive your objective, cuz in your situation might be a must to close a single qutoe to work with you and getting back the same response from the server, it might be a must to url encode the hash char # like %23 or even double decode it like %2523 along with a single quote or double quote, we are here think what is the situation and injection cababilties we have to craft our exploit payload, cuz oneday you will face a situation when you blocked by WAF but you can inject:

“ ‘ /\*\*/ AND OR FROM SELECT UPDATE INSERT SLEEP

someday you could inject those by themselves but when combining them with an exploitation payload you end up 403 Forbidden by Mr. WAF.

you can inject those fine at any place without getting blocked, and you might face a situation when you getting blocked if you put the parentheses () but with unicode one of them ( you will be able to bypass it without any blocking, so basically your first objective is trying to identify what you can inject and where you can inject at which location in the SQL Query, here you should have a far imagination about the query inserted at the backend and assuming lots of ideas, like see the parameter name and observe what the developer thinks when he implemented parameter with this name?

is he trying retreive audios with some sort of other parameters that he combined them with UNION query? or he just trying to save your update results on the database with INSERT query?

once you deeply understand your situation and what characters are works with you and what doesn’t work, you crossed half of the road now, cuz from my POV the rest of the half would be bypassing techniques.


now getting to this point first thing you need to do is extract the Database version from the database to decide what the next step which is the INFORMATION\_SCHEMA payload that is responsible for fetching the database names should look like:

my methodology here of getting the database version is by a bunch of trials, what you can do is basically fuzz on the database version with a bunch of each technique for every type of database, Ok fine now we know our injection point and how to inject and if it needs any obfuscation or not, until here we could try to dump the database version by the following techniques:

Oracle ==> SELECT banner FROM v$version

Microsoft SQL Server ==> SELECT @@version

PostgreSQL ==> SELECT version()

MySQL ==> SELECT @@version


now you should try it with the SUBSTRING Method:

first understand the SUBSTRING Method:

with SUBSTRING, you can extract part of a string, from a specified offset with a specified length, Each of the following expressions will return the string **y0**

Oracle ==> SUBSTR(‘bug4y0u’, 5, 2)

Microsoft SQL Server ==> SUBSTRING(‘bug4y0u’, 5, 2)

PostgreSQL ==> SUBSTRING(‘bug4y0u’, 5, 2)

MySQL ==> SUBSTRING(‘bug4y0u’, 5, 2)

‘bug4y0u’ *here*

5 is the starting position (counting from 1, not 0), so it starts at the fifth character ‘y’

*2*


now our crafted payloads that will work with US is:

```
MySQL & MSSQL:       ?lugu=316+AND+(SELECT+SUBSTRING(@@version,1,1))='4'
Oracle:              ?lugu=316+AND+(SELECT+SUBSTR(version(),1,1)+FROM+DUAL)='4'
PostgreSQL:          ?lugu=316+AND+(SELECT SUBSTRING(version(), 1, 1) = '4'
```
So we will try fuzzing the first character of the database version here in these different payloads with the intruder tab and one of them should work.

and start the Attack:

Nice, observe that it works with us with the

`SELECT+SUBSTRING(@@version,1,1)`
which is indicates that it’s a MySQL or MSSQL Database.

and the first character of the database version is 5

now we need to repeat the same process to fuzz for the next character, but with a tiny change in the payload.

Keep close attention below here on the SUBSTRING we fuzzing on the second character here, the SUBSTRING Method will return the first 2 characters starting from the 1st character, as described above in the SUBSTRING Explanation.


and start the Attack:

nice now we know the first two characters of the database version are (5.) and all we need is just repeat the same idea until we get the full version of the database.

until this point you can report immediately before anyone uses sqlmap since sqlmap sends a lot of known traffic known by most WAFs and sqlmap could give you an error even if it’s the endpoint is vulnerable but the WAF Blocks you after some malicious requests, and you know what? I have a friend from India who reported SQLI from sqlmap and literally was about to get 6K Bounty but the trigger told him that this issue was known internally by the team and working on it, Hundred percent the Blue team here had seen all of this weird sqlmap traffic and pass it to pen-testers and checked it and find that it’s actually vulnerable, so yeah that’s why I like Manual test, to keep my traffic as low as possible plus learning more and more obfuscations and bypasses techniques, cuz let’s be realistic, if it’s that easy everyone can do it and report with sqlmap, that’s why companies pay thousands of dollars for SQLI Vulnerabilities, you wouldn’t get this with sqlmap buddy, you will get it by understanding how the query works and where you can inject and what malicious characters you can inject, and from here you could obfuscate and bypass the WAF, fortunally in my case here there is no WAFs or bypasses or obfuscation Techniques.

fine, the IMPORTANT tip here is to think of your cababilites of injection and where you can inject those and how you can inject them (url encoded or unicode encoded or puts along with the payload comment like /\*\*/ or even encode just one character in the payload)

let’s get back into my bug.

You can report it as Database Version of course, but if you need to show more impact, let’s dump the database names

Now we know that @@version the one that worked with us by observing from the above payload that is the one that worked from the 3 above payloads, let’s get into documentation to check how to retrieve database names from the information\_schema.

check the docs: [https://dev.mysql.com/doc/refman/5.7/en/information-schema-schemata-table.html](https://dev.mysql.com/doc/refman/5.7/en/information-schema-schemata-table.html)

First, you need to understand this Query in MySQL:


`SELECT 1 FROM INFORMATION_SCHEMA.SCHEMATA WHERE SCHEMA_NAME LIKE 'a%'`
INFORMATION\_SCHEMA.SCHEMATA : is the system catalog table where database metadata is stored.

SCHEMA\_NAME : is the column in this table that stores the database names.

`LIKE 'a%' :` is the condition that filters the database names, returning only those that start with the letter 'a'.

so overall this query will return 1 if there is a database starts with the (a) character


### so let’s jump into injection example :)

the payload:

`AND+(SELECT+1+FROM+INFORMATION_SCHEMA.SCHEMATA+WHERE+SCHEMA_NAME+LIKE+'a%')%3d1`
so now we should fuzz on the characters that are on the SQL statement, to get the right first character of the database names that are inside the INFORMATION\_SCHEMA Table.

here in my payload, the results that are inside () would be 1 if there is any database starting with the letter (a) then if it actually there is a database named starts with the letter (a) the query would evaluate like:

316 AND (1)=1


and as you know from the very beginning this one works fine with us :)

so yeah now we are at a point where we need to fuzz on the database name, let’s do it with Intruder.

and start the Attack


### Results:

now we observed that there a two different databases the first one his name starts with (i) and the second one starts with (k)

so getting back into the Repeater tab:


yeah it works :)

now we were able to observe that there is a database that their first character is (k) so you could repeat the same process by going to the intruder and trying to detect the second character and so on..

and repeat the same process until you get the full database names.


so until this point, it’s a very detailed POC of having the ability to dump all the database names, you can report now buddy.

However, if you really interested in extracting the table names it will be something like this:

```
SELECT table_name
FROM information_schema.tables
WHERE table_schema = 'your_database_name';
```
Both MySQL and PostgreSQL support the use of the `information_schema` catalog to query metadata about tables, schemas, and databases. The query I provided is a common way to retrieve table names from a specific database regardless of whether your target using MySQL or PostgreSQL, and of course, you will combine it with the boolean-based ***and 1=1*** like this one:

`?lugu=316+AND+(SELECT+1+FROM+INFORMATION_SCHEMA.TABLES+WHERE+TABLE_SCHEMA+%3d+'your_database_name'+AND+TABLE_NAME+LIKE+'w%';)%3d1`
*this final payload will check if there’s a table name in this database that starts with the letter (w) and the same process to continue dumping the whole table name as described earlier using the intruder tab, and also if you need to dump columns so refer to MYSQL Docs for more info about dumping column names it’s the same idea like INFORMATION\_SCHEMA.COLUMNS and move from there if you like but for me, I’m Done, of course, no time to dump the column names so reported it immediately and got triaged in almost 8 or 5 minutes if my memory is good.*

The First report is DONE!


## Second bug:

Here it’s another endpoint that is responsible for searching for items in the store from the database, Fortunately, the parameter of the search here is not sanitized properly at the backend :)

Looks fine hah?

let’s put our magic single quote :)

as you see it’s vulnerable easily, not like the first one that was boolean-based and if you put any single quote you will see an error of mysql\_fetch\_array() method xD


ok fine, let’s fire some payloads:

guess which payload works :)

this one:

`bug4y0u'+AND+(SELECT+1+FROM+(SELECT(SLEEP(10)))a)+AND+'bug4y0u'%3d'bug4y0u`
but it’s blocked by I think some Firewall rules Not WAF at all cuz the bypass I did is URL encoding in some characters on it, with some comments like /\*\*/ I didn’t need Unicode encode at all.

after almost 1 hour of being detected, here is the final payload:

`bug4y0u'+AND+/**/(%53ELEcT+1+/**/+fRoM/**/+(SE%4cEC%54(sL%45%45P(3%29%29%29a)+A%4ed+'bug4y0u'%3d'bug4y0u`
Just URL encode some characters and put some comments /\*\*/ easy!

in most cases, this payload will be blocked by Modern WAFs now in 2023, but yeah it’s an awesome one, I see another researcher did it in 2020 and it works with him and he got 2.2k Bounty, so it depends on your target and the firewall rules implemented besides the WAF, so add it to your wordlist :)

It works with me a lot of times when finding an old endpoint with the waybackurls tool, most of the time the developers ignore removing the useless php files or the old files from the servers, and you can literally find those endpoints with it’s parameters on a plate of gold with the waybackurls tool, for me I do the -dates switch to check the time of the files and go for the old date :)

`echo 'bug4y0u.com' | waybackurls -dates`
this landed me with very old endpoints that the developers forgot to remove from the server and are still accessible to the public and Vulnerable.

However here is the POC:

Forced the Database server to sleep for 3 seconds and 8 seconds.

## Third bug:

Here it’s another endpoint that is responsible for retrieving audio information about some attributes related to the audio, Fortunately, the parameter of the audio here is not sanitized properly at the backend :)

Here I really want to show you how powerful to observe any changing happens in the response as I said earlier in tips at the First Bug.

Do you see this?

No No Not the Response’s length, I mean the response’s body, pay close attention to the response at the two pictures, it looks the same in the two cases and that’s the point here that a lot of researchers move on when they see no difference in the repeater tab or on the response on their browser, but the reality here that this endpoint just retrieves the audio information in HTML format response in a small size at the end of the page, that is Stored in the Database and just print it’s name and some other attrbuites related to that audio like (name of the file, author of the audio, date of the uploaded audio etc…) on HTML Content so yeah when injecting single quote it seems like the developer handles this situation at the backend when injecting any malicious character, he exit from the query at all and didn’t execute it and didn’t give back any informations about that audio, that’s my assuming about why the response’s length decreased almost 2500 bytes, so yeah that’s how you need to think of any functionality you testing, so the difference here actually is in the response’s body but Below at the end of the HTML response, not obvious in your screen you should scroll down to see the whole response, that’s why I told you from the very beginning at the tips in First bug that to observe any *(tiny change)* and I literally meant it, Difference in (Response’s length, Response’s content, Responses Delay time) if you wonder about the response’s content I wanna surprise you that in some situations when you inject single quote or double quote as described, you would find the server responses with the same response’s length but with completely different response’s body.

I hope these tips find you well on your side of the screen :)


back to my bug:

now we know that it’s vulnerable since there is a change in the response’s length, let’s goooooooooo.

the final payload works with me after lots of payloads and concatenation stuff:

`bug4y0u'|(IF((now())LIKE(sysdate()),SLEEP(6),0))|'bug4y0u`
I tried lots of obfuscation techniques to dump anything from the database and I couldn’t, so sent it to one of my Indian friends to collab with him and make the impact a little bit higher, he also couldn’t dump anything even the banner, and I’m not Indian btw but I have a lot of friends from India in this field :), very friendly and hard work people ❤, so yeah reported it as it is (Time-Based SQLI)

## Fourth bug:

Here it’s another endpoint that is responsible for retrieving some information related to the author of the audio uploaded to the database.

As Always, the first hit is injecting a single quote or double quote and observing any changes in the response :)

the error here in the picture reveals the column name lang\_id, the table name cms\_objects, and the object\_id which is another column name also from the database, all of this should be not retrieved like that, so I was thinking of error-based SQLI, and here are the results:

My Methodology when I face an error-based SQLI:


The first thing I try to inject:

`' || (select '') || '`
both of the || here are used for concatenating the strings in SQL Syntax, Google it if you don’t know how it works.

if it gives 200OK this will means that it’s a MySQL or MSSQL, but if it gives an error in the response this will indicate that it’s not MSSQL or MySQL, so based on my experience this is a valid query in MSSQL and MySQL but it’s not at Oracle, since Oracle requires the clause FROM and it’s not exceptional.

summary of the tip: If we don’t write the FROM clause with the Oracle database, we’ll get an error.

### and the second step is to inject:

`' || (select '' from dual) || '`
if it gives a 200OK that means it’s an Oracle Database, so what is the dual word?

In Oracle SQL, the `DUAL` table is a one-row, one-column table that is often used when you need to perform calculations or retrieve single values without referencing an actual table. It serves as a convenient way to evaluate expressions, functions, or subqueries.

You typically use `DUAL` in cases where you want to select or manipulate data that doesn't come from a table, such as the result of a function or expression. For example:


`SELECT 1 + 2 FROM DUAL;`
so yeah basically if it gives 200OK in the response, I will know that it’s an Oracle.

and the third step is to inject:

`' || (select '' from bug4y0u) || '`
since the bug4y0u string here makes no sense from the perspective of the Database, this should retrieve an error, just wanna ensure that I’m working fine with a deep understanding of the case I work on.

the above-injected payloads sometimes I encoded some multiple encoded formats on them, or added some comments between the whole payload like /\*\*/ comment, till this point I disclosed all of my thoughts and ideas while testing :)

let’s get back to the bug.


it gave me 200OK which indicates it’s an Oracle, and indicated that It’s a completely different response’s length, and I got confused, even till now still don’t get why the server responds with a different length, so I’m not really ninja at error-based and hope if anyone professional at it to ping me on Twitter for collab next time if you like, but for it landed with me Time-Based and worked fine, and reported it.

until here I got confused with the above trials of those payloads cuz the response’s length changed, so I shut down my mind from error-based and was thinking about Time-Based to report it fast.

after a bunch of trials with Time-Based here is the payload that worked with me.

`?id=708'+ANd+E%4cT/**/(1337%3d1337,/**/sL%45EP%283*4)/**//**//**/)+OR+/**/'1337'%3d'bug4y0u`
how it works:


- `ELT(1337=1337,SLEEP(12))`: This part of the string is an attempt to use the `ELT` function to execute a time-based SQL injection attack. It tries to make the database server pause for 12 seconds if the condition `1337=1337` is true.
- `OR`: This is used to combine conditions, but it's part of the payload.
- `'1337'='`Bug4y0u`'`: This part of the string just trying to evaluate 1337 with the Bug4y0u string, and of course in this case it will return false, However, since there’s an AND & OR operations, the AND that are from the left would evaluate first before the OR, so yeah adding the OR part here at the very end of the payload looks like useless ???????????
- in some cases, this trivial technique of adding the OR operation with wrong evaluation like ‘1337’=’Bug4y0u’ would give you the ability to bypass the firewall rules sometimes, or even you can make ‘1’=’2' just any wrong condition with OR operation along with your payload, and for sure sometimes you will need proper encoding and a little obfuscation on it to pass.

so yeah ended up with me Time-Based not Error-Based :)

## We are done!

Really, hope you learned how to think when testing for SQLI Manually, based on my experience if you got all of my above ideas in the 4 bugs you will just need to read more and more writeups about bypassing WAFs and obfuscation Techniques.

Thanks :)

Twitter: [https://twitter.com/bug4you](https://twitter.com/bug4you)

GitHub: [https://github.com/y0usSs3F](https://github.com/y0usSs3F)
