# Master and Find XSS Easily

- **Source URL:** https://medium.com/@shellreaper/master-and-find-xss-easily-5c76982dcec3?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20251126143614/https://medium.com/@shellreaper/master-and-find-xss-easily-5c76982dcec3
- **Fetched:** 2026-11-24
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/3646 (id 3646)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Master and Find XSS Easily

Hi , I’m shellreaper again and today I’m gonna explain to you RXSS(Reflected XSS) and SXSS(Stored XSS ) in a simple way.

first we need to understand what is an xss attack ?

## XSS ( Cross-Site Scripting ) :

xss occurs when a javascript code gets executed in the user’s browser by the attacker ( the user who visits the web application) . so simply an attacker forces the victim’s browser to run a javascript code .

## Why Does XSS Have a High Risk ?:

there’s so much can be done with javascript , for example :

 **you can hook a browser ( takeover the whole browser and control it)** 

**you can steal cookies ( cookies are simply what identifies the user’s account in the website) , if it gets stolen an attacker could hijack it and access the victim’s account  you can use it to force the browser to download a malware , etc**

## Reflected XSS :

now we have a basic understanding of what xss is , let’s explain the first type ( reflected cross-site scripting ).

reflected xss occurs when the javascript payload gets executed only one time at a specific visit which includes the payload in it .

for example :

let’s assume there’s a search functionality that takes the user’s input and reflects it in the page

if we view the source page we’ll find the input looking like this

`<h1>0 search results for 'test1234'</h1>`
so it’s just a simple html \<h1> tag , how do we make it run a javascript code ?

we need to break out the quotes , and enter a javascript code to exploit a prompt for example , by using the following payload .

`'><script> alert("test") </script>`
this is will be the result :

your payload will look like this :

`www.redacted.com/?search='><script>+alert("test")+</script>`
it’s just that simple .

## Stored XSS :

now we’ve covered reflected xss , let’s move to stored xss.

stored xss are as simple as the reflected xss but much harder to find . 

when do you have a stored xss ? when your input get’s stored in the source code of the page as a part of the code , and when does that happen ? for example a comment section in a forum that a user can post a commnets in . exploiting it is just as simple as the reflected xss but you have to find an input point that gets stored in the source code of the page .

every user that visits your comment will have the payload executed on their browser , unlike the reflected xss which you have to send the url including the payload to the victim in order to get the payload executed.

## Tools and Techniques to find XSS in the real world:

my favorite technique is using a crawler tool that finds multiple parameters that get reflected . 

I personally use GXSS

how can we combine it to find xss ?

you can use a spider such as gospider or a waybackmachine tool such as gau

for example :

`gau --subs www.redacted.com | grep "=" | Gxss -c 100 | sort -u > reflected.txt`
you also have to consider input fields when you’re testing manually to find stored xss vulnerabilities .

I hope you enjoyed this article .
