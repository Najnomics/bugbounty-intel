# $1000 for a simple Stored XSS

- **Source URL:** https://medium.com/@snoopy101/1000-for-a-simple-stored-xss-8be7083a7c2d?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20231012153321/https://medium.com/@snoopy101/1000-for-a-simple-stored-xss-8be7083a7c2d?source=rss------bug_bounty-5
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/3524 (id 3524)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
I was hacking on a private program and I couldn't get anything interesting by fuzzing or using the website’s features.

Then I started looking at the JS files till I came across this beautiful code:

Based on the URL and the parameter names, it appears that this request might generate HTML pages containing arbitrary code.

Testing Request:

Simple exploit:

*The “transactionHtmlData” parameter was writing the HTML code inside our new HTML page.*

## Openning the file

*alert(document.domain)*

# Account Takeover

Fortunately the session cookie lacked the “HttpOnly” flag, which allowed me to obtain it using JavaScript and gain access to the victim’s account.

*Bounty:*

*Reach me at:*

LinkedIn:

[https://www.linkedin.com/in/ali-imani-2a896a266/](https://web.archive.org/web/20231012153321/https://www.linkedin.com/in/ali-imani-2a896a266/)

twitter:
