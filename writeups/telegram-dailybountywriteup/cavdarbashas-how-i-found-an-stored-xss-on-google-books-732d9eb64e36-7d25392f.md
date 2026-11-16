# How i found an Stored XSS on Google Books

- **Source URL:** https://medium.com/@cavdarbashas/how-i-found-an-stored-xss-on-google-books-732d9eb64e36?source=rss------bug_bounty-5
- **Fetched from:** https://medium.com/feed/@cavdarbashas
- **Fetched:** 2026-11-16
- **Channel:** @dailybountywriteup
- **Telegram message:**  (id 3898)
- **Method:** medium-rss-content readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
Hello Hackers, I’m Sokol Çavdarbasha, I’m 20 years old from Kosovo and welcome to my first story about a vulnerability that i found on Google Books.

Great. Now that we’re done with that, we can get to the real thing this article’s about.

One day I decided to hunt for vulnerabilities on Google.I was looking to find XSS (Cross Site Scripting) . So i start to digg into google.com and i was focused on Google Books.

So i thought why no to try here for XSS, and i type in search bar the following payload “>\<img src=x onerror=alert(1)>, and i got an book that another Security Researcher uploaded it to [https://play.google.com](https://play.google.com)

so i press the “Preview” button and the XSS gets triggered

the XSS triggered successfully, so i quickly report it to Google VRP Team at [https://bughunters.google.com](https://bughunters.google.com), and they responded quickly with a …

i was so happy that i got an “Nice catch” response from Google VRP Team with Priority P1 and Severity S1, and got rewarded $XXXX as this is my first valid bug that i reported to Google.

PoC:

I hope that you enjoyed reading this article and sorry if there are things that are not clear.

Thanks for Reading : )

Sincerely,

Sokol Çavdarbasha.

You Can Follow me on :

Instagram: [https://www.instagram.com/sokolcav](https://www.instagram.com/sokolcav)

Linkedin: [https://www.linkedin.com/in/sokol-%C3%A7avdarbasha-845426232/](https://www.linkedin.com/in/sokol-%C3%A7avdarbasha-845426232/)

Twitter: [https://twitter.com/sokolicav](https://twitter.com/sokolicav)
