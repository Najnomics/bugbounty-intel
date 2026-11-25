# Day 02

- **Source URL:** https://iamrudhh.medium.com/day-02-understanding-how-the-web-works-3967d9694082
- **Fetched from:** https://iamrudhh.medium.com/day-02-understanding-how-the-web-works-3967d9694082?source=rss-99e5e69fc209------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14919 (id 14919)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** iamrudhh / Mon, 21 Sep 2026 06:38:53 GMT

In Day 01 we covered what bug bounty is. Today we cover the one skill under every web vulnerability: **understanding how browsers and servers talk**.

If you can’t read a request, you can’t break one. Let’s fix that.

Every time you open a website, your browser sends an **HTTP request** and the server sends back an **HTTP response**.

Request:

GET /profile HTTP/1.1

Host: example.com

Cookie: session=abc123

Response:

HTTP/1.1 200 OK

Content-Type: text/html

Set-Cookie: session=abc123; HttpOnly; Secure

A request has a **method**, a **path**, **headers**, and sometimes a **body**. A response has a **status code**, **headers**, and a **body**.

**Hunter’s angle:** every parameter, header and cookie in that request is something you can inspect and test. That’s your attack surface.

**Hunter’s angle:** developers often protect the “main” method and forget the others. Ask yourself:

Only test this on targets you’re authorized to test.

The server’s reply tells you a lot before you even read the page.

**Hunter’s angle:** a **403** on a path is a clue that the path is real. A **500** after unusual input can mean the app isn’t handling that input safely, and error messages sometimes leak internal details. Note the difference between 403 and 404 on the same target.

**Headers** carry extra information with every request and response. **Cookies** are how a site remembers who you are (your session).

Security flags to look for on cookies:

A missing flag on a session cookie is worth noting in your recon. Security headers like Content-Security-Policy and X-Frame-Options are also worth checking.

curl -i https://example.com

***Disclaimer:*** *This series is for educational use only. Test only systems you own or programs that explicitly authorize you, and stay within their scope.*

Setting up your hacking environment: Burp Suite, browser proxy setup, and your Kali Linux workspace.

Follow along so you don’t miss it. I share one bug bounty lesson per day on Instagram [@iamrudhh](https://instagram.com/iamrudhh) and on Medium.

**Tags:** Bug Bounty, Cybersecurity, Ethical Hacking, Web Security, Infosec

Want a Day 03 post in the same format? I can also put this in a file if you prefer.
