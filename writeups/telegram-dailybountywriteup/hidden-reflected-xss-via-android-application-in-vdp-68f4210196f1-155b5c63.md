# Hidden Reflected XSS via Android Application in VDP

- **Source URL:** https://cyb3rc4t.medium.com/hidden-reflected-xss-via-android-application-in-vdp-68f4210196f1?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250506010510/https://cyb3rc4t.medium.com/hidden-reflected-xss-via-android-application-in-vdp-68f4210196f1?source=rss------bug_bounty-5
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/7581 (id 7581)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Reflected XSS via Android Application -VDP

**Hello Everyone**, I’m back with a new blog about my recent finding, XSS via a hidden endpoint in an Android application. For security reasons, I would like to refer to the domain as redacted.com.

Initially, I selected one vdp and began examining its scope. It had a very limited scope, covering only one domain and its Android and iOS applications.

I started by testing the web application first, After creating an account, I began crawling the URLs and examining all the functionalities. However, I found that all areas were very secure, and none of my test cases were effective due to the implementation of tokens throughout the application.

Tried using the [**Fuzzuli**](https://web.archive.org/web/20250506010510/https://github.com/musana/fuzzuli) tool on the web application to search for any backup files. I generated a custom wordlist with the [**DirtyWords**](https://web.archive.org/web/20250506010510/https://github.com/un4gi/dirtywords) tool based on the subdomains of the target domain and attempted fuzzing with my favorite tool, Feroxbuster, but no luck. 🥲

After checking all possible test cases on the target, I decided to stop testing. A little while later, I fired up Android Studio and began analyzing the target Android application.

After spending about 10 minutes examining the application, I discovered an interesting endpoint that retrieves files from a subdomain, which was formatted as ‘***?filelocation=***’.

I copied the path from Burp Suite and entered it into my browser console, replacing the file location with evil.com. To my surprise, the application page redirected to **evil.com** 🤩

Every time I encountered an open redirect, I immediately placed a `javascript:prompt(document.domain)` payload in place of the URL. If any target blocks it, I go for bypasses that I found on Twitter.

After placing the payload, I received a beautiful popup, and I was super excited to report this, so I went ahead and reported it.

Within 24 hours, they patched the issue and added my name to the hall of fame. ( target name in one of my linkedin posts )

*Support and Follow*


If you found this article insightful, please leave a clap and share your feedback in the comments. Follow me for more exciting findings and cybersecurity tips!

*Find me on Linkedin: @suryaarigela*


Thank you for your continued support. Keep clapping, commenting, and sharing your thoughts!
