# How i got Bug -XSS

- **Source URL:** https://medium.com/@basxth/how-i-got-bug-xss-8eec781ab58b?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20240715150354/https://medium.com/@basxth/how-i-got-bug-xss-8eec781ab58b
- **Fetched:** 2026-11-23
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/6672 (id 6672)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# How i found an XSS Bug

***Hello HACKERS***, Today I made the decision to share a post about how I got XSS(*Cross-Site Scripting)* bug.

First and foremost, we are all capable of finding bugs. *If you put effort it will reflect*.

The first thing I did was , I dorked some websites that are capable of bug bounty. I then visited the website “https://www.victim.com". I read the scope first, and I realized that xss is conceivable.

*Google dork command i used :*

`inurl:security "reward"`
*What is Google Dorking?*

*Google dorking refers to using advanced search operators in Google (or other search engines) to find specific information that is not readily accessible through normal searches. It involves crafting search queries with specific operators to uncover sensitive data or content that is not typically indexed or easily found by the average user. This technique can be used for various purposes, including cybersecurity research, gathering competitive intelligence, or even finding vulnerable websites.*


Tip: After we’ve found the website .We all need to review the scope of the website. To know which all are in scope and which is not .

Let me begin:

I thoroughly researched the website and discovered some good stuffs.

I found a search box on the webpage. I decided to inject HTML injection, SSTI, and so forth… After injecting, I received no suspicious results.

And I decided to do xss in the website.

**What is XSS ?**

*XSS stands for Cross-Site Scripting. It’s a type of security vulnerability typically found in web applications where attackers inject malicious scripts into web pages viewed by other users.*


Sample XSS payload “\<script>alert(1)\</script>”. I tried many payloads and I inspect (Q) the elements after that, its been modified by seeing the inspect code (eg: by putting closing tag etc…). However, it didn’t work. But I didn’t chose to quit. Then I decided to include different JavaScript payload in the URL. I had no confidence that this payload would reflect.

*“https://www.example.com/search/#q=\<xss\_stuffs>”* in this URL’s (search parameter) after equal to i put the payload such as:

*“https://www.example.com/search/#q=\<input type=text value=\<input type=text value=jaVasCript:/\*-/\*\`/\*\\\`/\*’/\*”/\*\*/(/\* \*/oNcliCk=alert(document.cookie) )//%0D%0A%0D%0A//\</stYle/\</titLe/\</teXtarEa/\</scRipt/ — !>\x3csVg/\<sVg/oNloAd=alert()//>\x3e>\</input>”*

After injecting this payload , **BOOM it got reflected.**

*Reflected Payload i used :*

``<input type=text value=jaVasCript:/*-/*`/*\`/*'/*"/**/(/* */oNcliCk=alert() )//%0D%0A%0d%0a//</stYle/</titLe/</teXtarEa/</scRipt/ - !>\x3csVg/<sVg/oNloAd=alert()//>\x3e></input>``
Really, I was shocked and proud of myself.

I hope you gained anything new from my experience. Please share your thoughts on this. I believe that you enjoyed this post.

**Happy Hacking :)**
