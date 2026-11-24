# XSS

- **Source URL:** https://medium.com/@itsmeliodas/xss-a-fight-with-the-waf-a08a4fc6012c?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20240315154244/https://medium.com/@itsmeliodas/xss-a-fight-with-the-waf-a08a4fc6012c
- **Fetched:** 2026-11-24
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/5439 (id 5439)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
Hi ! My name is Ryan and this article is about a bug I recently discovered in a private program for a well-known billion-dollar company, where an attacker can exploit an XSS vulnerability. Learn about the issue and the steps taken to address this security concern.

## Target

I started to look for a program in Bugcrowd (less competitive) and i found this famous clothing brand, let’s say **redacted.com** . The scope was limited to their main web application. Let the hunting begin!

## Recon

Upon entering the site, I immediately had an eyescontact with the “search” section. I then tested if the conducted search is reflected on the page.

Ok it’s reflected ! What i do usually it’s try some characters to see how the server will handle it :

\<>” ‘ / script


Go in the Developer Tool and see how it’s represented in the source code :

Of course it’s filtered, a famous website like this will undoubtedly protect itself against trivial XSS attacks from the 1990s**.** But wait, tt’s not over yet! This data can be used everywhere and not only in this tag

And here’s is the trick, when searching for another location AND by viewing the source code instead of Inspect Element:

It’s not filtered! You can see our payload ( \<> “ ‘ script ) and nothing is filtered so in consequents our first double quotes closed the content attribute, so we escaped the meta tag. Let’s try to see if the html is rended correctly by the page by trying

“/>test\<title/>


Easy right ? Now we just have to inject the most basic “/>\<script>alert()\</script> \<title> as a proof of concept :

## Fight with the WAF

I struggled durings plenty hours to figure out how can i bypass the WAF, because typically when u trigger the WAF you are ban for few minutes. After one full day i finally found the right payload by escaping an other tag thats was already inside a script tag so i just have to write my JS code, but the WAF was blocking as well some words like “alert” “src” etc…

I finally found the right way to escape :

*Leave some clap if you enjoyed and don’t hesitate to give me your feedback :*)


# Thank you !

Meliodas
