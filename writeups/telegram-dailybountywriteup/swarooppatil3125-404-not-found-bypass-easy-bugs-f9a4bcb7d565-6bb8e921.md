# 404 Not Found BYPASS ! Easy Bugs

- **Source URL:** https://medium.com/@swarooppatil3125/404-not-found-bypass-easy-bugs-f9a4bcb7d565?source=rss------bug_bounty-5
- **Fetched from:** https://medium.com/@swarooppatil3125/404-not-found-bypass-easy-bugs-f9a4bcb7d565?source=rss-3064e4c32753------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14871 (id 14871)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** Swarooppatil / Wed, 26 Aug 2026 07:16:05 GMT

The key idea is simple: **a file returning 404 Not Found today doesn't necessarily mean that it was never publicly accessible.**

I started by querying the Wayback Machine’s CDX API to collect historical URLs belonging to the target domain:

curl -G "https://web.archive.org/cdx/search/cdx" \

--data-urlencode "url=\*.example.com/\*" \

--data-urlencode "collapse=urlkey" \

--data-urlencode "output=text" \

--data-urlencode "fl=original" > out.txt

This gives us a list of URLs that have appeared in the Web Archive.

Instead of manually going through thousands of URLs, I filtered the results for commonly interesting file extensions:

cat out.txt | uro | grep -E '\.xls|\.xml|\.xlsx|\.json|\.pdf|\.sql|\.doc|\.docx|\.pptx|\.txt|\.zip|\.tar\.gz|\.tgz|\.bak|\.7z|\.rar|\.log|\.cache|\.secret|\.db|\.backup|\.yml|\.gz|\.config|\.csv|\.yaml|\.md|\.md5|\.exe|\.dll|\.bin|\.ini|\.bat|\.sh|\.tar|\.deb|\.rpm|\.iso|\.img|\.apk|\.msi|\.dmg|\.tmp|\.crt|\.pem|\.key|\.pub|\.asc'

This dramatically reduces the amount of data that needs to be reviewed manually.

Next, I opened some of the interesting URLs.

Many historical files returned responses such as:

A 403 can sometimes indicate an access-control issue, but a 404 deserves attention as well.

If the application currently returns 404, check whether the same URL was previously captured by the Web Archive.

Go to the Wayback Machine (web.archive.org) and enter the URL.

From there, use the **timeline** to identify dates when the resource was archived.

If a snapshot exists from a period when the file was publicly available, the archived version may contain the historical contents of the file.

This technique can reveal historical resources that are no longer linked from the application, including:

However, **finding a historical file does not automatically mean there is a vulnerability**. The security impact depends on what the file contains, whether the information is sensitive, whether it was intentionally public, and the rules of the relevant bug bounty program.

For Zendesk environments specifically, publicly accessible attachments and historical support files can be worth investigating carefully, while avoiding access to data belonging to other users unless the program explicitly authorizes it.

One of the biggest lessons here is:

***Don’t ignore a 404 during recon.***

A resource that disappeared from the live application may still have a historical footprint.

Combining normal endpoint discovery with historical URL collection can therefore uncover interesting attack-surface information that isn’t visible during a normal crawl.

I also made a full video demonstrating the methodology and practical workflow.

You can Watch it here : [https://youtu.be/oT2FhSuMex4?si=O8hsQBsMup4RbpEG](https://youtu.be/oT2FhSuMex4?si=O8hsQBsMup4RbpEG)
