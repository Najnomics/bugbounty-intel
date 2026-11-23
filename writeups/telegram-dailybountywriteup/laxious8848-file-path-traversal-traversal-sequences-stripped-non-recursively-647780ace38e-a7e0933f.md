# File path traversal, traversal sequences stripped non-recursively

- **Source URL:** https://medium.com/@Laxious8848/file-path-traversal-traversal-sequences-stripped-non-recursively-647780ace38e?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20241121220923/https://medium.com/@Laxious8848/file-path-traversal-traversal-sequences-stripped-non-recursively-647780ace38e
- **Fetched:** 2026-11-23
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/7936 (id 7936)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
I will not provide you with any sort of definition. If you want definition Just google it. In this lab, it blocks ../../../ . But there isn’t much sanitization in it. So we can just bypass it with ….//….//….//

So, This is the lab.

So just open the foxy proxy and Burpsuite. You just dont need to intercept just go the HTTP history and open the filter section and add images in it too. And just choose a image filename.

In this case i chose filename=10.jpg and right click it and send it to the repeater.

Send this payload to see the response. As it is not proper sanitized, The following payload can bypass it and gives the required info.

So the lab is solved.

Congragulations. Your lab is solved………………..
