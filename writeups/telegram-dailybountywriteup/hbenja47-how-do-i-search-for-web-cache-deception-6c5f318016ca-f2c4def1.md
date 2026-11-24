# How do I search for Web Cache Deception?

- **Source URL:** https://medium.com/@hbenja47/how-do-i-search-for-web-cache-deception-6c5f318016ca?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20251126142633/https://medium.com/@hbenja47/how-do-i-search-for-web-cache-deception-6c5f318016ca
- **Fetched:** 2026-11-24
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/3828 (id 3828)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# How do I search for Web Cache Deception?

One of the methods I use, which can vary depending on the target and scope size, **begins with navigating the target web application and logging everything in Burp**. The next step is to **identify which responses contain sensitive data**. This can be done easily using Burp’s ‘Search’ feature to look for sensitive data only in responses (headers and body). This sensitive data can include the email you registered with, your full name, login cookies, tokens, and more.

Once I’ve identified which responses return sensitive data, I **check if they provide explicit information about the caching mechanism in their headers**, such as ‘no-cache,’ ‘private-cache,’ ‘public-cache,’ ‘max-age,’ etc. The headers can vary depending on the caching mechanism used, and you can read about these headers in Mozilla’s documentation. If you want to specialize in a specific caching mechanism, you can search for that particular documentation. For example, you can explore Cloudflare’s caching documentation. This can provide you with insights on how to cache sensitive data.

Next, I **use static extensions like .png, .css, .js, and many others**. You can find lists of these extensions and even perform fuzzing. I check if the response still returns personal information even after adding such an extension. Sometimes, 404 errors can reveal personal information in the code!

If I don’t have success with this, I **try the path confusion techniqu**e. Here are some examples of it, and you can explore more:

URL encoding can generate confusion between different components:

\n => %0A

;=> %3B

#=> %23

?=> %3F

For example, in

example.com/account.php?name=val we could use example.com/account.php%3Fname=valnonexistent.css

to bypass the CDN, proxy, or WAF.

Another way could be with \n:

example.com/account.php to example.com/account.php%0Anonexistent.css

Using ;

example.com/account.jsp;param to example.com/account.jsp%3Bparamnoexistent.css

And #

example.com/account.php#frag to example.com/account.php%23nonexistent.css

-> Source: [Cached And Confused](https://www.youtube.com/watch?v=czDfMWBsIKw&t=45s)

Once I’ve added the static extension (with or without path confusion) and **retrieved sensitive data in the response**, I **check if the cache response explicitly mentions caching**. Even if I receive cache-related headers like ‘no-cache’ that specify not to cache the response, I **still check if it remains uncached**. How do I do this? I use another browser or an extension like Multi Account Containers in Firefox. It’s crucial to verify whether the response is cached while logged in and while not logged in (using a different account than the one used to attempt caching the information).

If I succeed with this, I **create the URL that I will send to the victim**. Let’s imagine it’s [https://www.example.com/account.do/logo.png](https://www.example.com/account.do/logo.png). I send it by email to myself and open it with the victim’s browser or container. Then, I check with the attacker’s account in another browser or container. I do this because sometimes the response can differ when accessed from a link compared to the response obtained by adding extensions in Burp’s repeater.

I also consider using a VPN and changing my IP after accessing the link as a victim to enter with a different IP than the cached URL as an attacker. This helps me understand if the cache mechanism considers it shared or not due to coming from the same IP. This could be a reason for your report being accepted or not. It’s essential to keep this in mind.

As an extra tip, I’ll share my notes after reading Omer Gil’s article on WCD:

### WCD POC

1. The attacker sends a malicious URL, such as [https://www.example.com/account.do/logo.png](https://www.example.com/account.do/logo.png), to the victim.
2. The victim accesses the URL (they must be logged into their account).
3. The request reaches the proxy, which, not recognizing the file, queries the server.
4. The server sends the content of the victim’s account in a 200 OK response.
5. The caching system receives the file and identifies that the URL ends with a static extension (.png), considering it a public static file and creating a cache folder with the file logo.png.
6. The victim receives their account page as usual.
7. The attacker accesses [https://www.exmaple.com/account.do/logo.png](https://www.exmaple.com/account.do/logo.png), and the request is received by the proxy, which returns the cached victim’s account page.

### What does this imply?

A successful exploitation allows the attacker to obtain the victim’s personal information. The impact can be greater if the response contains session information such as CSRF tokens, security questions, tokens, or session cookies. This could lead to an account takeover.

### Conditions

There are three conditions that must be met to achieve a WCD attack:

1. When adding the path /noexistent.\[SOME\_STATIC\_EXTENSION\] to the page you want to cache, it should return the original content (sometimes it may return a 404 error and still cache victim information).
2. Web cache functionality must be configured to cache files based on their extension.
3. The victim must be authenticated when accessing the malicious URL.

Happy hacking!!!
