# Reflected XSS At U.S. Government

- **Source URL:** https://medium.com/@teamm2d007/reflected-xss-at-u-s-government-2a5e254b1a23?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20251126142231/https://medium.com/@teamm2d007/reflected-xss-at-u-s-government-2a5e254b1a23
- **Fetched:** 2026-11-24
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/3633 (id 3633)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Reflected XSS At U.S. Government

Hey there, im mandar parekh from DDU,NADIAD. so basically it’s my first writeup,so i’m not having much experience for it and also im writing this from my heart not from CHAT GPT so please understand if any mistakes ;)

Let’s Get Started……

so after a long time i decided to open second operating system of my laptop called ‘KALI LINUX’ and decided to start hunting for bugs so i picked up one of the target from US Government From BUG CROWD platform

## **STEP 1:**

basically i stated from getting subdomains you can use following tools for it

1.assetfinder

2.subfinder

after doing subdomain enumeration i started ‘altdns’ tool to find anther subdomains from the subdomains which we got from the above two tools

altdns just adds series of names which ca be there used by developers to make new hidden subdomains..

## **STEP 2:**

now i got around 22k subdomains. so we can try screenshoting here if we want but it would be so timetaking so i used another tool named httpq(All these tools are available in github) which just visits all these subdomains and gives you the response statement

Now focus on **200 OK “NONE”** this kind of responces

i picked up one from them let’s tell it xyz.redcated.com

## **STEP 3:**

here comes the main part to find XSS always try to add your name after the url for example:

[https://medium.com/](https://medium.com/p/2a5e254b1a23/edit)\<\<your\_name>>

now chwck for the page source for my target it got reflected on 2 places inside the webpage so i tried with some of basic payloads like

1. \<script>alert(1)\</script>
2. “>\<script>alert(1)\</script>

then again i saw the response and i saw that it interpreates script tag as \<InvalidTag> so it clicked in my mind that this site would be restricting some of the vulnerable tags so i tried this payload finally

\<audio href=1 onerror = alert(1)>\</audio>

and BOOM………………………

i went to the BUG-CROWD and reported it. they trigered the bug after two days of my submission.that’s it for now guys please hit the like button

happy hacking…………………
