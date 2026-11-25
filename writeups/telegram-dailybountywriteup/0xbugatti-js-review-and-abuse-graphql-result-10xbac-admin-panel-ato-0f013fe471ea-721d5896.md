# JS Review and Abuse GraphQL Result 10xBAC + Admin Panel ATO

- **Source URL:** https://medium.com/@0xbugatti/js-review-and-abuse-graphql-result-10xbac-admin-panel-ato-0f013fe471ea?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250413031009/https://medium.com/@0xbugatti/js-review-and-abuse-graphql-result-10xbac-admin-panel-ato-0f013fe471ea?source=rss------bug_bounty-5
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/7995 (id 7995)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# JS Review and Abuse GraphQL Result 10xBAC + Admin Panel ATO

Dear Guys

Here I will Demonstrate a part of My Methodology Related to NodeJS + React AKA MERN Apps

After Mapping the Scope I found dashboard for Administration Don’t Have any Clear Registration function

And I started to play

Started to

- Fuzz Register Endpoint -> X

- Replace Login with Register In Request -> XX

Also Failed

Then I took step back Get more Mind and technology

I observed that there is GraphQL , React , NJS

This stack always used to be Vulnerable to Logic Bugs But Needs some JavaScript Digging

I need to create user

after well examination In JS Console

I observed GraphQL errors Upon Authentication Process

There is Interaction between React & Back End As Usual

I started to Search about the Important Javascript File Contain 

The needed functions

searched with `user` Keyword

6 JS Files Found 

I decided to search with another Keyword to Decrease the scope of search

I searched with `login`

there is 2 mentula files

Start my Work from

`next/static/chunks/pages/users-b48829712ecbd6a6.js`
Using Used \`JS Beutify\` Extention

After DeObfuscate the Code and Revieing it Using ChatGPT

I Crafted All GraphQL needed Mutations & Operations

then I decided to Avoid **Delete| Update** Operation To Avoid Business affect

Then I will try to add my Own User and Test them

I got Error

I got Error after Search I found that is because wrong User role **ADMIN**

I modified the Role to

`"role" :"ADMINISTRATION"`
And Resend

And Bingoooooooo! Admin Panel Access

and Here I found A lot of Misauthoriztion bugs

All With Tip of 

**Remove Authorization Token -> 200 OK**

**DELETE , UPDATE , CREATE , SHOW \[USER , ORDER , STORE\]**
