# Using Wayback And DNS rebinding For SSRF

- **Source URL:** https://medium.com/@amnotacat/using-wayback-and-dns-rebinding-for-ssrf-a5a16f611acc?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20240224125758/https://medium.com/@amnotacat/using-wayback-and-dns-rebinding-for-ssrf-a5a16f611acc
- **Fetched:** 2026-11-19
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/5368 (id 5368)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
Lets start

I use waybackurls by tomnomnom a lot [https://github.com/tomnomnom/waybackurls](https://github.com/tomnomnom/waybackurls) and while looking for endpoints i might of missed i use -dates it might provide old and new endpoints.now while running waybackurls one thing i do sometimes is i put all the domains in scope of the program in one txt file and i then run “cat /root/all-inscope-domains.txt | waybackurls -dates | grep “https://” | grep “url=” | egrep -v “(.txt|.js|.svg|.jpeg|.jpg|.woff|.woff2|.eot|.css|.png|.ttf|.gif)””.

Now am sure i came across this endpoint before but due to me not paying attention i missed it and so did every other hacker in the program this program has been running for years so this endpoint was there for at least around a year with out no one finding it including me so what i do is a lot of manual work and i don't run much automation i feel is more efficient for me.

So after running waybackurls i look at each endpoint and each url yes each url one by one so i don't miss anything after checking the endpoint which looked like “/en-us/api?url=” it would redirect to the main domain but if you took out “en-us” you could fetch any domain with out redirecting.so i immediately checked to see if we can fetch google.com and after seeing that fetching google was successful i all-ready knew that i had a high chance of SSRF here but it was not going to be so simple.

See we weren't going to be able to fetch the metadata so easily because Akamai was going to block it so i had an idea since it was only trusting IP’s that were maybe whitelisted all i needed was to get the IP that it trusts and then use DNS rebinding to try to fetch the metadata.

So i setup a simple nc -lvnp 1337 and got the IP i then used [https://lock.cmpxchg8b.com/rebinder.html](https://lock.cmpxchg8b.com/rebinder.html) to fetch 169.254.169.254 and the result.

Thank you for reading.
