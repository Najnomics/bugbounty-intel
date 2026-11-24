# Desperate XSS

- **Source URL:** https://medium.com/@ramkumarnadar47/desperate-xss-ce3619343f57?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20251126143235/https://medium.com/@ramkumarnadar47/desperate-xss-ce3619343f57
- **Fetched:** 2026-11-24
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/3475 (id 3475)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Desperate XSS

This application was quite secure and it had this mechanism wherein one request can be sent only once, this validation I think was done by the URL query parameter “OWASP\_CSRFTOKEN”. This essentially means you can’t take the request to Repeater and play around with it rather you’re going to have to intercept the request in real-time and inject the payload in the Intercept tab.

The value of the said token was reflected in the response under the context of a comment.

Having had the reflecting value, I tried and injected the payload appending the token, something to this effect:

`.jsp?OWASP_CSRFTOKEN=2F8A-XXXX-XXXX-XXXX/*alert(1)*/`
This logged me out of the application.

After a few trials and errors, I learnt that disturbing or changing the value of the token will most definitely throw me out of the application.

Then I got the idea to use the ampersand (&) and inject the value. Something to the below effect:

`.jsp?OWASP_CSRFTOKEN=2F8A-XXXX-XXXX-XXXX&/*alert(1)*/`
This time I got the reflection of the injected payload and I was not being logged out but the payload was not executing though. I thought the black listing was in play, so I tried many different payloads, but no luck.

Then I began to prepend the payload to try my luck out. Still no cigar.

In my desperation, I injected a new parameter named “xss” and gave it the value of the payload, prepending it to the “OWASP\_CSRFTOKEN”.

`.jsp?xss=*/prompt("XSS")/*&OWASP_CSRFTOKEN=2F8A-XXXX-XXXX-XXXX`
and it worked. Not straight away, but it did.

alert(1) was definitely not working. But prompt(“XSS”) worked before that I actually used another payload. I came under the impression that pop-up payload will just not work with this application, so I researched other ways and found out about this neat payload:

`console.log(document.domain)`
Using the above, you won’t get a pop-up. Rather, you will have to open the Console in the Developer Tools (Ctrl + Shift + I) in Chrome. If you find that the domain of your application is shown in the Console, it means that the above payload worked.

So above was just a brief explanation of the thought process involved. Let me illustrate the steps simply now;

1. This is the original request.

2\. Below marked is the injection point, where the payload was injected.

`Payload: xss=*/prompt("XSS")/*&`
3\. Payload was reflected under the context of a comment. Hence, I had to use the closing comment symbols (\*/) and the opening comment symbols (/\*). This leaves our prompt(“XSS”) uncommented and primed to execute.

This got executed. And we have a reflected XSS in our hands which can be shared with the URL.

Thank you for reading!!!
