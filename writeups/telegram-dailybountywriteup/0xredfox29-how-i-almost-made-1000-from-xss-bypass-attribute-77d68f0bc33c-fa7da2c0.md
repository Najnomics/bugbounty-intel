# How I almost made $1000 from XSS bypass attribute

- **Source URL:** https://medium.com/@0xRedFox29/how-i-almost-made-1000-from-xss-bypass-attribute-77d68f0bc33c?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250908200125/https://medium.com/@0xRedFox29/how-i-almost-made-1000-from-xss-bypass-attribute-77d68f0bc33c
- **Fetched:** 2026-11-21
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/9652 (id 9652)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# How I almost earned $1000 from XSS bypass attribute

Hello everyone

In this post, I would like to share an interesting experience when I discovered a Cross-Site Scripting (XSS) vulnerability in a site listed on the Bugcrowd program. Although I didn’t get the $1000 bounty as reward because the report was marked as a duplicate, the discovery process was quite interesting and taught me a lot.

As a security enthusiast who is still actively learning and exploring, this experience was one of those moments that fueled my passion for bug hunting. Maybe you’ve been in a similar situation — that tense moment when you find a valid bug, only to realize that a friend of yours has already reported it, and his report is still in the queue and hasn’t been closed or resolved by the analyst team. this is purely my fault because I couldn’t be patient and wait a little longer to make sure I could submit the report without duplicates and be eligible for the bounty.

I got this vulnerability because I saw my friend uploading his achievements when he succesfully to get a bug similar to mine, then I asked the name of the company registered in the **Bugcrowd** bug bounty program then I examined all the features on the website and got a subdomain that was not included in the “in scope” category but I still tried to report it and the team confirmed it as a valid finding report in terms of subdomains, attack vectors and payloads that I used.

I tried inserting a simple payload, such as **“>\<Svg On Only=1 Onload=alert(origin)>** the response successfully bypasses the website security system but does not display a pop up alert.

After an hour I tried to modify the payload by adding attributes, something like this **page=”1">\<Svg On Only=2 Onload=alert(origin)>** and bingoo I successfully to bypass the website’s security system and get a pop up alert that shows the website is still vulnerable to xss attacks with a simple payload

I apologize that I used JSON.stringify(localStorage) but actually just using document.domain is enough and can be accepted by the analyst team.

Then I tried my friend’s payload, still with the same technique of bypassing the security system by adding attributes and close tags like this

**page=”1">\<Svg On Only=1 Onload=alert(origin)>** 200 OK ✅ with pop up

**test”ONxss=>\<details open ontoggle=prompt(JSON.stringify(localStorage))+x** 200 OK ✅ with pop up

I was in a bit of a hurry to submit the report without taking the time to discuss it with my friend — turns out, her report wasn’t closed or resolved by the team and yups my report was marked as a duplicate. haha

hopefully this write up can be an additional reference for friends as bug hunters and make this a lesson and experience for me in the future.

Thank you for reading this article! I hope this provides some insight for those trying to bypass complex WAFs or even find a trick to bypass them using a simple custom payload
