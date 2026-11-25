# DOM XSS in document.write sink using source location.search

- **Source URL:** https://medium.com/@kcaaditya976/dom-xss-in-document-write-sink-using-source-location-search-cc0ba7b461c2?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20241117210716/https://medium.com/@kcaaditya976/dom-xss-in-document-write-sink-using-source-location-search-cc0ba7b461c2?source=rss------bug_bounty-5
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/7895 (id 7895)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
DOM-Based Cross-Site Scripting (DOM XSS) is a type of XSS vulnerability where the malicious script is executed **entirely in the browser**, without any changes to the server’s response. It occurs when JavaScript in the web page processes user-controlled input (such as query parameters, fragments, or cookies) in an unsafe way and modifies the **DOM (Document Object Model)** to include executable code.

This is the DOM based XSS lab.

We can solve this lab with the help of DOM invader.

Open Burpsuite and open the browser without intercept. And on the extension section, you will find the burpsuite and then and then go to the DOM invader and open it. Now, you go to the lab .

Now, open inspect and then you will find out the DOM invader and then in it you will find out the canary. You just have to copy the canary and then put it into the input field.

Now you will find out where the real problem is using DOM invader .Then, you have to choose the option exploit. And if you have to see where the DOM vulnerability is just go to the option stack strace.

If you click the option exploit. In my condition, the exploit worked and the lab was automatically solved without any hindirance.
