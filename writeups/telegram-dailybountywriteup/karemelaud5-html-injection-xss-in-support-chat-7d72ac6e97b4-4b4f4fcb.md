# Html Injection & xss in support chat

- **Source URL:** https://medium.com/@karemelaud5/html-injection-xss-in-support-chat-7d72ac6e97b4?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20231108222141/https://medium.com/@karemelaud5/html-injection-xss-in-support-chat-7d72ac6e97b4
- **Fetched:** 2026-11-24
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/4197 (id 4197)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Html Injection & xss in support chat

--

Hi Everyone ,

it’s my first writeups on medium ,

In this simple writeup i will explain how i got HTML injection in the support chat,

if you have any chat have some feature like adding a link or adding images , style text , or header h1, h2, like the following chat :

always think to use the features that the website provide against it , 

let’s explain how is it !!

as example we will use the ‘B’ against website


Steps :

- first lt’s try to inject any thing for text like “>Hi to know there was any reflected char or not .

as you see the devolper filter the tag , so you will not be able to injection anything .

Ok , Let’s start

- write anything like “Hi” and use the ‘B’ to bold the word
- Intercept the request with burpsuite
- you will find your text as follow :

- replace the value “\<b>Hi\</b1>” to :

`<h1 onmouseover="alert('Hi')" style="color: red;">Hi</h1>`
- send the requet
- the response is :

- you can inject any html tag with the same technique .

if the website doesn’t block the events you will got Reflected XSS

but my target blocked the events so i got Html Injection


# Nice Bounty

I hope you benefited and did not waste your time


**Thanks for reading**
