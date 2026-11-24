# XSS drag Drop in Google worth $6,999

- **Source URL:** https://medium.com/@aliraza879612345/xss-drag-drop-in-google-worth-6-999-8c75c44fb4a4?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20230506021259/https://medium.com/@aliraza879612345/xss-drag-drop-in-google-worth-6-999-8c75c44fb4a4
- **Fetched:** 2026-11-24
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/2568 (id 2568)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# XSS drag Drop in Google worth $6,999

Trying to understand the issue, I read on the comments and there’s someone mentioned it is possible due to different format copied from OpenOffice such that. And Dr. Mario share his research on this and it is really interesting. [http://www.slideshare.net/x00mario/copypest](http://www.slideshare.net/x00mario/copypest)

Then, end of last year, noticed there’s an XSS discovered by Harry in Google Docs using the drag drop technique. And due to improper validation HTML code read by Google Docs, the XSS can be executed

I tried to look around Google Docs. Harry’s submission did resolved, however, there’s a module in Google Docs/Sheets/Drawing/Presentation where it allow a user to create a drawing. This module however does not fix yet.

Create a simple HTML file with our XSS payload, drag and drop into the drawing module, and the XSS is there :)

What make it interesting is that, I did take a look on the response given by the Google whenever a valid image or other different payload used. There were differ!

The drawing module was actually only looking for a valid image where it can come from user’s computer or external source. If the source contain a valid image, the image then will be uploaded and properly embedded. If the image is broken, then it is broken. This is where the XSS payload below take in place.

\<img src=nonvalid.jpg onerror=alert(0)>


This is because, the payload will execute if the source is broken (error). I tried using another payload such as onload,onmouseover etc, the XSS would not working! So here’s a challenge. How we are going to make sure the image is loaded on victim’s side, but once the victim drag into Google Docs, the image then will broken? Simple thought I used the valid image that exist in most of Windows users computer..yes..in C:\Users\Public\Pictures\Sample Pictures :)

It was not in Google Images :)

Thanks!

bounty : $$$$ ❤
