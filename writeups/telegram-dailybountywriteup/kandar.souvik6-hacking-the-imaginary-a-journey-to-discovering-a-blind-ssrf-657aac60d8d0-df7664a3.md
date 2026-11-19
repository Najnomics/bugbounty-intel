# Hacking the Imaginary

- **Source URL:** https://medium.com/@kandar.souvik6/hacking-the-imaginary-a-journey-to-discovering-a-blind-ssrf-657aac60d8d0?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20240612173244/https://medium.com/@kandar.souvik6/hacking-the-imaginary-a-journey-to-discovering-a-blind-ssrf-657aac60d8d0
- **Fetched:** 2026-11-19
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/6383 (id 6383)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Hacking the Imaginary: A Journey to Discovering a Blind SSRF

Hey there, fellow cyber sleuths! Today, I’m taking you on a fun and exciting journey of discovering a blind Server-Side Request Forgery (SSRF) vulnerability in the Imaginary application. Get ready to laugh, learn, and maybe even score a bounty. Let’s dive in!

**Subdomain Enumeration:**

So, I was doing my usual recon (a fancy word for poking around), and I found a subdomain: imaginary.example.com. It was running the Imaginary application, an open-source image processing app you can find on GitHub here.([https://github.com/h2non/imaginary](https://github.com/h2non/imaginary))

**Endpoint Discovery**

Next, I tried brute-forcing some endpoints (basically, guessing the URL paths). No luck. So, I decided to check out the source code of the Imaginary application. And there it was:

fit?url=[https://i.ibb.co/j6ZgKvm/new-512-ori.png&width=300&height=200&gravity=center](https://i.ibb.co/j6ZgKvm/new-512-ori.png&width=300&height=200&gravity=center)

The url parameter caught my eye — it looked perfect for testing SSRF.

Me, realizing the url parameter could be the key to an SSRF exploit: “Bingo! This is it!”

**Testing for SSRF**I started testing the url parameter by trying different URLs. After a few tries, I managed to perform blind SSRF using the localhost URL in octal format:

[http://0177.0.0.1/](http://0177.0.0.1/)

In octal notation, 0177.0.0.1 is the same as 127.0.0.1.

**Internal Port Scanning:**With SSRF working, I scanned internal ports using burpsuite and found that ports 80 and 443 were open.

I reported the vulnerability to the organization, and they acknowledged it. Then, I received a bounty. Victory!

Thats all for today, bye
