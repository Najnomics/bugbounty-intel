# Subdomain takeover on open.itu.edu via Shopify

- **Source URL:** https://medium.com/@wrinnsec/subdomain-takeover-on-open-itu-edu-via-shopify-6b83ea970f3d?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20230311135740/https://medium.com/@wrinnsec/subdomain-takeover-on-open-itu-edu-via-shopify-6b83ea970f3d
- **Fetched:** 2026-11-27
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/1856 (id 1856)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Subdomain takeover on open.itu.edu via Shopify

Hello everyone! This article was originally written around December of 2022. After writing the draft I started to become more busy with school and had less time to work on write ups. I hope to get back into this soon and work and collaborate with some fellow security researchers. Thanks for reading.


A little over a month ago, I became very interested in finding my very own Subdomain Takeover vulnerability. For those who have never heard of an Subdomain Takeover, the concept is quite simple.

Pictured above is a subdomain takeover for a azure hosting service. As shown at the top the first CNAME entry is running smoothly, the subdomain is pointed towards the azure server and the azure server is online and operational, the content from the server is successfully being displayed on the website! In the second CNAME entry there is an issue, the server that the CNAME is pointing towards **does not exist** meaning that anyone could register it and effectively takeover the subdomain. In the third entry, this is exactly what happened. A malicious user has taken over the azure service and hosted his own malicious content, which will then be displayed on the effected subdomain.

Now that you understand the basics of a subdomain takeover, here is how I found one effecting the International Technology University(itu.edu). As I mentioned earlier, I became interested in subdomain takeovers for their little effort high reward tendency, the process to find these vulnerabilities can be very easily streamlined and automated. First I purchased a remote server that could be used for scanning for these vulnerabilities. To target the highest impact targets, I scraped a list of the most popular .edu domains. After that, I used the GO tool [Subjack](https://github.com/haccer/subjack) to automatically check the A records of each domain to see if it could identify any dangling dns records. And to my surprise, I was able to find 100s of apparent vulnerabilities ONLY effecting US .edu domains. After taking multiple days manually going through each one, I learned a very important lesson about subdomain takeovers: **Edge Cases**

# What is an Edge Case?

When referring to subdomain takeovers, edge cases are primarily when a takeover may be possible, but the only way to find out is to attempt to takeover the subdomain, and see if any common issues stop you from taking the subdomain over.

Edge cases and their common issues can be very different for each service that is vulnerable to subdomain takeovers.

For example, on Github.com a website primarily for sharing and uploading code, they offer website hosting that lots of websites will point their subdomains toward. If this DNS record is dangling, and the github site shows no content. It *may or may not* be vulnerable to a takeover. The only way to find out is to register a github account with the same username as the name of the github site. If you are still a little confused on what I mean, or if you are interested in identifying vulnerable subdomains I highly recommend you check out

So sadly, a majority of the vulnerabilities were Edge Cases… many ended up not vulnerable, many made it very very difficult to takeover. A lot of them would have costed me $1000s of dollars, because it required a takeover on a paid service. Being a student, I didn’t have the money or the time to work with these cases. Luckily I was able to find a subdomain vulnerable to a Shopify subdomain takeover.

Open.itu.edu


After looking at its A DNS record, I saw it pointed towards shops.myshopify.com and the website displayed the following message:

using what I had learned from *Can i take over xyz* specifically the shopify section: [https://github.com/EdOverflow/can-i-take-over-xyz/issues/32](https://github.com/EdOverflow/can-i-take-over-xyz/issues/32)

I was able to create a shopify account, and choose the cheapest plan of a few dollars a month, I went to my settings and under “Connect domain” I linked “open.itu.edu”

**It worked!** I now had nearly full control of “open.itu.edu”. I made a simple webpage using shopify in order to show impact and inform the university:

# Reporting

Ethically reporting a vulnerability is very important. You must convey in detail the problem, impact and solution. It’s incredibly important to make sure you are talking to the right person and you keep the information as secretive as possible until the company feels comfortable with information on the vulnerability being made public.

Itu.edu only lists emails for Admissions, Education Verification and General inquiries. I decided to report my findings in a email to Itu.edu’s General inquiries email address: [info@itu.edu](mailto:info@itu.edu). After 30 days of no response I emailed ITU’s Computer Science Department Chair Dr Mamoun Samaha whom I chose because ITU’s website mentions his areas of interest such as applications, iOS, IoT, cybersecurity and ethical hacking. After 4 days of no response, I came home to find the vulnerability patched but my inbox empty. I attempted to contact ITU once more in an attempt to get any sort of response but as of 2/28/2023 I still have not gotten a response.

# **Timeline.**

- 12–2–22 Draft of this article is written.
- 12–3–22 Reported the bug to their general inquiries email.
- 1–5–23 After roughly 30 days of no contact I reported it to their computer science department head.
- 1–9–23 Bug is fixed, subdomain is taken offline.
- 1–9–23 I reach out to verify the problem is fixed.
- 2–28–23 No response from University.
- 2–28–23 Article is published.

Thanks for taking the time to read this report, I learned a lot on my mission to find a subdomain takeover and hopefully you will too.
