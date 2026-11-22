# SQL Injection UNION Based Unknown Table X Multi-line Query Issue

- **Source URL:** https://medium.com/@robyfirnandoyusuf/sql-injection-union-based-unknown-table-x-multi-line-query-issue-b70ab3a5c68c?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20230627044100/https://medium.com/@robyfirnandoyusuf/sql-injection-union-based-unknown-table-x-multi-line-query-issue-b70ab3a5c68c
- **Fetched:** 2026-11-22
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/3108 (id 3108)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# SQL Injection *UNION Based Unknown Table X Multi-line* Query Issue

--

A few days ago, I discovered a rather unique SQL Injection bug on a competition website hosted by a college. The website was built using Laravel 10 framework. The SQL Injection attack was actually quite common since it was present in a GET parameter.

When I added a single quote (‘) to the URL, the website went broken and

http://target.com/event/detail/52'


showed me an error debug message and piece of source code like:

*DB*::select(

“

select a.\*, ee.status from tb\_karya a

join entered\_event ee on ee.id = a.event\_id

where a.id = ‘$id’

and ee.status = 1

“

);


Now, here’s the funny part. When I tried doing an ORDER BY until 99999999 to count the number of columns, the website just acted all normal. Like, seriously? So, I had to go old school and manually brute force the UNION SELECT thing. And the number of columns turned out to be freaking 32!

But wait, it gets even crazier. When I actually did the UNION SELECT and used these fancy inline comments ( — -), the website was like, “Whoa, Unknown table ee blahblahblah.”

[http://target.com/event/detail/52'](http://target.com/event/detail/52') union select 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,’2020–02–02 00:00:00',18,19,20,21,22,23,24,25,26,27,28,29,30,31,32 — -


Turns out, it happened because the SQL syntax was written using multiple lines.

select a.\*, ee.status from tb\_karya a

join entered\_event ee on ee.id = a.event\_id

where a.id = ‘$id’

**and ee.status = 1**


The cause of the error was in the clause “and ee.status = 1” because inline comments ( — -) can’t comment on a newline. Using multiline comments , I mean C-style comments (/\*) also can’t solve this issue because they need a closing tag. To fix this, I used a query prefix. Remember, UNION is used to combine queries, and we can manipulate it, so it becomes:

[http://target.com/event/detail/52'](http://target.com/event/detail/52') union select 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32 **from entered\_event ee where ee.status\_seleksi =1**


By adding the query prefix “**from entered\_event ee where ee.status\_seleksi =1**” the messed-up query got fixed!

But we still had one tiny problem. When I executed the query, the website was like “parsetime error at col 17”. Well, it easy to fix. I manipulated the number 17 and turned it into a valid timestamp format, ‘2023–02–02 00:00:00’. Here’s the final malicious query:

UNION SELECT 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,**’2020–02–02 00:00:00'**,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32 from entered\_event ee where ee.status\_seleksi =1 — -


And guess what happened? Boom! The website showed me the vulnerable vulnerable column.

Last, we just need to do DIOS (Dump in one shot).

# Mitigation

So, the reason this bug showed up, even though the developer used the latest version of Laravel, is because they had some seriously bad coding practices going on. I mean, come on! They didn’t bother with variable binding or prepared statements. Look at that leaked source code above. They just threw the $id variable right into the SQL syntax like it’s no big deal. Seriously, they should’ve used the Eloquent Eager load/lazy load feature for a simple join query. It’s way more legit and easier to read than messing around with those DB facades.

That’s all for now. Thanks for reading!

./exit
