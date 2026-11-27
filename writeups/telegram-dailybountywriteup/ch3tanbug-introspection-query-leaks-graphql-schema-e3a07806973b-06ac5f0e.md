# Introspection Query leaks Graphql schema

- **Source URL:** https://medium.com/@ch3tanbug/introspection-query-leaks-graphql-schema-e3a07806973b?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20251126142303/https://medium.com/@ch3tanbug/introspection-query-leaks-graphql-schema-e3a07806973b
- **Fetched:** 2026-11-27
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/3122 (id 3122)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Introspection Query leaks Graphql schema

## Introduction

Hey i’m back again with a new bug that i found recently. Those who don’t know me i’m *Chetan Kashyap* a Bug-Bounty hunter from INDIA. So without wasting any time let’s start.

So lately i decided to hunt on [bugcrowd](https://www.bugcrowd.com/) but i wasn’t getting any program that had good scope and good functionality. So i decided to leave [bugcrowd](https://www.bugcrowd.com/) and find some VDP’s through google dorking. So after entering my first dork i checked out some of the websites and finally i got a website ( *let’s call it redacted.com* ) that was looking good to hunt on, however the website was in dutch language I had to use google translate extension the whole time while hunting.

So when i was reading the responsible disclosure rules i came to know that all the findings on the website had to be submitted through [bugcrowd](https://www.bugcrowd.com/) to a third party vendor who later will submit and mitigate those vulnerabilities on the target. I became happy because initially too i want to hunt on programs on [bugcrowd](https://www.bugcrowd.com/) because VDP’s take a long time to respond.

So i started with the recon process and ran my custom recon script that i made which usually finds subdomains by combining all tools that are available and filters the live domains and their titles and saves the output to a new file. While the script was running i went ahead to the main website and tried checking all the functionality while my burp was saving the request history. After spending almost half an hour i didn’t found anything interesting. So i decided to look for login panels. I went to google and used the dork **“site:\*.redacted.com inurl:login” .** I found a subdomain *“works.redacted.com”* that allowed to raise support tickets and check status of the support tickets. When i tried to raise any ticket it said me to login or register but even after registering it showed account didn’t exist. I spent a lot of time on this subdomain even grepped all the urls from waybackurls but found nothing interesting. My whole day was spent trying to figure a way to get the support tickets of the other users but unluckily i didn’t get any success.

Next day i woke up with a fresh mind and checked all the domains my script has collected. I found an interesting domain “wiki.redacted.com” that contain the information regarding how to use a particular software that the target was selling. I tried to fuzz the subdomain and found an endpoint /admin. When i checked that endpoint it was a admin login page, as usual the default creds didn’t work so I entered wrong creds and intercepted the request in BURP. To my surprise the website was sending a POST request to /graphql endpoint.

I remembered the article i read from [YesWeHack](https://blog.yeswehack.com/yeswerhackers/how-exploit-graphql-endpoint-bug-bounty/) regarding Graphql exploitation. I copied the introspection query from that article pasted it in my repeater and BOOM the request leaked the Graphql schema. Now there are numerous attacks that can be performed from this stage. An introspection can completely reveal the backend system defined by developers including arguments,fields,types,description and so on. The schema serves as an attack ground for attackers for crafting queries and leaking sensitive information but in my case mutations were also possible.

I quickly prepared a poc and submitted the report to [bugcrowd](https://www.bugcrowd.com/) but it turns out they aren’t accepting any domains besides the main domain that is “redacted.com” the traiger suggested to report the vulnerability directly to the VDP through email as they can only accept reports on their behalf which are on the main domain. So i sent an email with all the details and the reply is yet to come.

## Conclusion

So i was a little upset because the bug was not traiged but this bug helped me to know more about graphql and now im trying to increase the impact of the bug with the help of circular queries in graphql (still learning) which can lead to an internal DOS. Nevertheless bug-hunting is all about patience and learning and i hope you liked my article. You can ask me any questions if you want and if i wasn’t able to explain anything correctly kindly forgive me because im not used to writing articles. Thank you for reading and don't forget to give a clap.
