# how i made easy information disclosure bugs in graphql

- **Source URL:** https://medium.com/@eyaalgabay/how-i-made-easy-information-disclosure-bugs-in-graphql-82284b05d7b4?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20240219030414/https://medium.com/@eyaalgabay/how-i-made-easy-information-disclosure-bugs-in-graphql-82284b05d7b4
- **Fetched:** 2026-11-27
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/5310 (id 5310)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# how i made easy information disclosure bugs in graphql

--

this is a way to find easy information disclosure bugs in any graphql api that uses postgresql database

Hi everyone 😉

always remember that you…

but today we are talking about a website with database.

lets call the website “example.com”

what can i do in example.com?

1. see on every parameter if it goes throught the database or not.
2. get the database query if errors are visible in the response, such as:
“select \* from passwords where password = mypassword”
3. know if parameter have the potential of being vulnerable to sqli. or if the parameter is prepered statment (if error shown witch is very common).

## but why i can do all this thing?

The reason that you are able to do all of those thing is because every website that builtin using nodejs, graphql, and postgresql is vulnerable by **default!** to something that i call “null byte injection”.

## what is “null byte injection”?

null byte injection is simply adding null byte to the string. such as \u0000 or %00 or any other way that the program will read a null byte.

lets see an example of error that i have gotten by adding null byte to the request:

## bug after sent to bugcrowd program

## bonous

on every website that vulnerable to above vulnerability its very easy to check for sqli. not only this, also when we get sqli its very easy to know what explait we need to insert because we see the query.

lets say that we found sqli, with postgresql its very very easy can escalate to full RCE vulnerability! as you can execute below query:

`COPY table_name (column_name) FROM PROGRAM 'echo "i am executing bash"'`
