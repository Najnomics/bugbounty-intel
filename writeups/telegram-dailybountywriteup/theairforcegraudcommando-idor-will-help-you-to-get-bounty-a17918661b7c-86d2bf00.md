# IDOR….will help you to get bounty

- **Source URL:** https://medium.com/@theairforcegraudcommando/idor-will-help-you-to-get-bounty-a17918661b7c?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20260425204424/https://medium.com/@theairforcegraudcommando/idor-will-help-you-to-get-bounty-a17918661b7c
- **Fetched:** 2026-11-19
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/13387 (id 13387)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# **IDOR….**will **help you to get bounty**

Welcome to this blog, I’m **Sandeep Singh Rajput** and I’ll define all the methods, tactics and techniques I used to find IDOR in a website. Through this blog you will able to masters in IDOR.

Imagine if you could trick a website to reveal the unusual or sensitive information of the user or website. Means you got the others users information. Boom ! you trigger a IDOR in a website.

IDOR : Information Disclosure Object Reference. IDOR is a web security flaw where an attacker or a pentester will able to get an another user’s information. The information contains sensitive or informational both types. The main thing you will get in IDOR is the information. The bounty, impact, exploitation all tings will depend on the information you got. In IDOR vulnerability a server or web application is not strictly checking the user input or the request where it coming from. and this will allow to get an another user information, modifying, deleting the data they shouldn’t be able to.

Hinglish: koi bhi user dusre user ka data dekh skta hh….. and impact, bounty or exploitation sab apki information or data par depend karta hai ke kya rahega.

Endpoints to check IDOR :

A. Rest API : by changing the 123 → 124, and you hit the idor and access the other’s user data.


```
GET /api/users/123
GET /api/orders/456
GET /api/invoices/789
```
B. Query Parameter : by modifying the id like 999 → 997, and you hit the target.


```
/profile?user_id=123
/download?file_id=999
```
C. GraphQL APIs : By modifying the 123 → to 124. sometimes you got the role parameter here, so you will also change it like user → admin .


```
query {
  user(id: "123") {
    email
  }
}
```
D. File Access Parameter :


```
/files/report_2024.pdf
/media/user_123.png
```
E. PUT/ DELETE request through burpsuite : check whether the users or posts has been deleted or not.


```
PUT /api/users/123      --> DELETE /api/users/123 
DELETE /api/posts/456   --> GET /api/posts/456
```
F. Manually inspecting the website with **robots.txt.** With the help of robots.txt file user will able to get the hidden parameter, their website structure etc.


Impact :

A. Found technical details about the website or infrastructure.

B. Get IP Addresses, API keys or database credentials via files.

C. Get sensitive or financial data of others users.

D. Get high privileges accounts.

E. Get Modifying, Deleting permission of data, files or user accounts.

“Appreciate you taking the time to read this. If you found it useful, share your thoughts or your own bug hunting stories — let’s learn together. Catch you in the next write-up.”

Follow me on :

[https://www.linkedin.com/in/sandeep-singh-tanwar-0605a126a/](https://www.linkedin.com/in/sandeep-singh-tanwar-0605a126a/)

soon will meet on youtube and github also with much info.
