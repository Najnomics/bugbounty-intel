# I Thought SQL Injection Was a Myth — Until I Found One

- **Source URL:** https://medium.com/@akkadnus/i-thought-sql-injection-was-a-myth-until-i-found-one-1866b6f94de5?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20251230145747/https://medium.com/@akkadnus/i-thought-sql-injection-was-a-myth-until-i-found-one-1866b6f94de5
- **Fetched:** 2026-11-19
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/12301 (id 12301)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# **I Thought SQL Injection Was a Myth — Until I Found One**

When I was learning and reading blogs about SQL injection, I always thought it’s definitely an urban legend and its nowhere in the wild, turns out it exists!

It feels great to move from reading write-ups to writing my own. As this is my first write-up and SQLi ended up being my first vulnerability to report, bear with my grammar and words.

Without further due, let’s jump into my entire thought process.

Let’s keep the target as redacted.gov.in. I opened the link, it was a login page, with username and password input. As always, I opened wappalyzer and saw nothing fishy.

I tried default and random creds, nothing worked. I thought let’s check for SQLi(usually its less common and I never got it in any login). I tested with `'` nothing happened, alert popped up with “try again”. OK let’s inspect the HTML page to look for some endpoints I thought, console tab was opened and, luckily noticed 500 internal error there.

When login was clicked, GET request was made to this endpoint:

[https://redacted.gov.in/redacted/createKey.php?username=admin'](https://redacted.gov.in/redacted/createKey.php?username=admin%27)

I opened this URL in new tab and tried again with random username. An error message in JSON format saying “user not found” was displayed on the frontend.

I thought, if I put actual username, I would get a different response. But I don’t know the actual creds and I don’t want to bruteforce with my i3 7th gen. So I didn’t know what the success response looks like.

Continuing my SQLi testing, I tried all basic payloads

like

 `' or 1=1'`

 `' or '1'='1'#`

 `' or 1=1;`

 `' or 1=1;-- -`

The last one worked, which means the remaining part is successfully commented out. A JSON reponse with some hashkey came.


I’m not sure what the hash is for, may be session, userid, or even for password encryption. But each time it was different.

Ok now check which type it is.

tried sleep() payloads — no delays

tried union payloads — nothing came

Now,

checked `' or 1=1;-- -` gives success message(true)

checked `' or 1=2;-- -` gives user not found message(false)

Yeah!!! You guessed it, it’s boolean-based.

Now the problem is what db it is, so i researched common functions for database names like database(), db\_name(),…etc.

now how to check it?

tried 

`' or db_name()=db_name();-- -` = false

`' or current_database()=current_database();-- -` = false

`' or database()=database();-- -` = true

So this is used by MySQL or MariaDB. Also used the same method to check for `version()` and `@@version` availability.

Before that I checked if `substring()` was working or not, because WAF may block, in my case it didn’t.

just checked `' or substring(‘hello’,1,1)='h';-- -` = true

Now the actual dilemma, what I need to show for impact? version or db name or something else.

OK, I can use `length()` function to determine which is shorter but I need to check one by one with `>`, `<` and `=`. Wait a minute I know DSA, lol.

Thanks to my DSA staff who taught me binary search, instead of iterating up to n where time complexity is O(n) I can use binary search which takes O(logn).

I narrowed it down to `length(verion())=36` and `length(database())=8`.

WHATT!!, version length is more.

I used intruder like this

`' or substring(version(),§a§,1)='§b§';-- -` where `a = [1–36]` and `b=[a-z0–9*_-#$@.]`

You can use whatever fuzzing tool you love, like ffuf or turbo intruder.

I filtered all the 200 responses, and found out the db was MariaDB.

I thought, this doesn’t show any big impact, I have seen write-ups showing db names using sqlmap.

I asked with my mentor whether I can run sqlmap to get db names and he approved.

Finally I was satisfied with manual checking, now its time for sqlmap. As I know it is boolean, the command used was

`sqlmap -r req.txt -p username --technique=B --dbs --threads=10`
After few minutes I got 26 db names.

Now time to report, crafted a proper report and sent to CERT-In.

Damn!!! Got response within 3hrs, I was surprised.

Later while reading the js file, majority of endpoints needed authorization headers in their request, two endpoints didn’t. It was to fetch some user data on their leave and export. I tested with `'`, yes again SQLi.

So SQLi existed on same endpoint but in two different parameters. Again reported this together. Got an acknowledgement.

Please drop your feedback, which will help me to learn and correct myself. As a beginner and to all beginners out there, keep grinding.
