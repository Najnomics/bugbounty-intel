# Blind boolean-based SQLi, by manipulating url

- **Source URL:** https://medium.com/@zatikyan.sevada/blind-boolean-based-sqli-by-manipulating-url-96e1e086378c?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250806085733/https://medium.com/@zatikyan.sevada/blind-boolean-based-sqli-by-manipulating-url-96e1e086378c
- **Fetched:** 2026-11-22
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/4947 (id 4947)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
Hello guys, today I will talk about how I’ve found a blind boolean-based SQL-injection, by manipulating url,

Alright so, it appears that modern web apps can fetch information from link itself, I know most of you would know the GET request with parameters, but this didn’t have parameter instead backend has some regexp that get’s the numbers in the url and makes an sql query, from a link like this

```
x.com/resume/doesntmatterwhathere-76541
```
So now as you might guessed anything before the numbers might not matter, and when I tested it — it actually didn’t matter, so now the most simple injections will give us hint if there is possible SQLi(injection)

After testing this url

```
x.com/resume/-76541'
```
I got an error 404 as response status code, and there was a redirect written in JS with window.location, which after was causing redirection to the main page which is just

```
x.com
```
After this I tried another injection really a simple one

```
x.com/resume/-76541'%20OR%20'
```
And it returned actual persons resume, indicating SQL returned true, I was also a bit confused that why a number, is being used in quotes in SQL query but it is what it is, if this was just a number, a payload like this

```
payload: 76541+1-1
payload url-encoded: 76541%2B1%2D1
```
Should return the same content that returns this link below

```
x.com/resume/76541
```
Because let’s imagine the SQL query and you will get it

```
SELECT * FROM users where userID=76541
```
Our payload that does +1–1 basically changes nothing but in our case this was a string like this

```
SELECT * FROM users where userID='76541'
```
OK now it was a little bit hard to get sqlmap return some data for us, as it was unusual case, I get always 404 error code and only when sql statement is returning false I get another HTML response, here I quickly asked chatGPT to help me,

And turns out there are several options like

```
--code, --string, --not-string
```
I only needed these 2 —code and —not-string, first one is for telling what status code to be expected as normal, second telling what exact response to check for to understand that SQL statement returned false, also we can use —random-agent as we might get blocked, and sometiimes cookies as well, but this time there wasn’t need for that, tho sometimes you should run sqlmap verbosly

```
sqlmap ... -v 4
```
Or -v 5, I don’t remember now, to see responses and see if your requests aren’t getting blocked, remember mostly status code 403 is returned whenever WAF blocks but it’s not always like that so checking the response is the best option, and then try —tamper with custom bypass payloads untill you are able to bypass WAF, OK this was it but ah no wait before I tried running sqlmap I actually did manual testing, and

NOTICE: IF I DIDN’T FIND THIS MANUALLY, SQLMAP WOULDN’T FIND IT EVER

Ok so what I did was I tried several payloads, after guessed the column count using ORDER BY, and after prooved rightness of ORDER BY with UNION statement

Here the payloads I used

```
payload: 76541' ORDER BY 38 #
payload url-encoded: 76541'%20ORDER%20BY%2038%20%23
full payload: x.com/76541'%20ORDER%20BY%2038%20%23
```
Sure before testing 38 I went like 2, 7, 24 everything was OK SQL was returning true, but than let’s say 41 would return the error response which is redirection in JS as I told you above, like this (look below)

```
<script>window.location="/";</script>
```
And sure I used this with —not-string

Now back to proving if the columns are actually 38 and not less or more

We can use UNION for this, and in SQL you can select everything + aditionally select something, just the returned columns with union should be exact same as first columns returned by SQL Select statement writen right before UNION.

So I wrote these payloads

```
full payload: x.com/76541'%20UNION%20SELECT%201,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1%20%23
```
Now there are exact 38 1’s here if I wrote one 1 more or less we would get error, by this I finally confirmed the vuln and submited my report additionally giving them their db tables as proof.

Thanks for reading, if you have questions fill free to ask in comments.
