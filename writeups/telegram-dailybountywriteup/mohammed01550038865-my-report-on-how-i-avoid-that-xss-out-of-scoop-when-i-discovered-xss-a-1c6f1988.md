# My Report on How I avoid That XSS out of Scope when I discovered XSS and How can I convert it to…

- **Source URL:** https://medium.com/@mohammed01550038865/my-report-on-how-i-avoid-that-xss-out-of-scoop-when-i-discovered-xss-and-how-can-i-convert-it-to-a17ac5ef16c6?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20230311134008/https://medium.com/@mohammed01550038865/my-report-on-how-i-avoid-that-xss-out-of-scoop-when-i-discovered-xss-and-how-can-i-convert-it-to-a17ac5ef16c6
- **Fetched:** 2026-11-24
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/1899 (id 1899)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# My Report on How I avoid That XSS out of **Scope** when I discovered XSS and How can I convert it to Steal Credit Card Info!

Hellllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllo Hackers,

first I am Start with collecting information about my tatrget. I collected Subdomains && endpoints I am used assesetfinder && findomain && sublist3r && subfinder for collecting Subdomains and am used katana && && ffuf with my private world-list

after Recon I found subdomin looks like : [https://target.com/blog](https://target.com/blog) when i visited this subdomain I can see search box I am start with test XSS first I injected this payload \<h1>HTML Tag Injected\</h1> but got nothing after that I injected this payload “>\<h1>HTML Tag Injected \</h1> but this time the payload got executed After that I try to inject this paylod “>\<img src=x onerror=alert()> the payload got executed this XSS but when i looking forward to the out of scoop I can see XSS out of scoop this means if i Report this bug will be mark as NA so I asked myself the question of how can I convert it to another bug to avoid it being out of scoop.

After that, I collected more information about the target, and I noticed that this target uses payments services a lot, so I thought, is it possible to steal the credit card info?

after that I try to inject “>\<input type=”text”> but I got nothing but when I see the source code of HTML Page i Can see the payload injected Successfully but I can't see this on the page But after thinking I noticed that the The default background color is white, same as the page color, so I can’t see the ‘input’ After that I try to change the background color of my paylod and injected the payload aging Now I can see the input injected successful Now I understand the trick. We need to change the background color of the input.

After That I create form for stealing user name and password . then i Create my PoC as Shwon in the image

when I opened this on my PC I can see

after that i inject my PoC on the vuln search box Ican see

after that I send this link to the victim and open my server once the victim enter the username && password I can steal this info as shown in the image

In the same way, I made a form to steal the credit card info.

Now the security team can’t tell me it’s out of scoup, I’m able to steal the crdit card info.

How can I steal the credit card info? I send the link to the victim and tell him that if you buy from this link, there is an 80% discount. Once the victim puts the credit card information, I will have it on my server.

Submission accepted without The security team says anything on it is out of scoop

I hope this Report is useful for U!

Thanks,

Smallest Hacker!
