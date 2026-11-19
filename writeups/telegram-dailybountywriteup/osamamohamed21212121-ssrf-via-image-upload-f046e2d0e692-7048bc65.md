# SSRF Via Image Upload

- **Source URL:** https://medium.com/@osamamohamed21212121/ssrf-via-image-upload-f046e2d0e692?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20240915082217/https://medium.com/@osamamohamed21212121/ssrf-via-image-upload-f046e2d0e692
- **Fetched:** 2026-11-19
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/7261 (id 7261)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# SSRF Via Image Upload

Hello, my name is Osama Mohammed, and I am a penetration tester and bug hunter.

Hi, welcome back to another blog. In this blog, we’re going to know how I found my (SSRF)in the external program. So, before starting, if you haven’t followed our medium account, do follow, guys. So without wasting time let’s get into the story of the (SSRF).

After thoroughly inspecting and exploring the website, I found the function responsible for changing the profile picture. This is one of my favorite functions because it can lead to the discovery of multiple vulnerabilities.

The first thing I attempted was uploading a shell.php file instead of a profile picture. However, I couldn’t obtain a shell despite trying again and using every bypass technique I knew. In the end, I was unsuccessful.

At that point, I didn’t give up. Instead, I took a few hours to rest due to my continuous effort to get the shell.

Afterward, I tried uploading an image in SVG format, and it worked. The website accepted images in this format. At that moment, I thought of three potential vulnerabilities I could exploit: XXE, Stored XSS, Open redirect and SSRF.

I first tried to find an XXE vulnerability, but unfortunately, I couldn’t exploit it either.

Then I proceeded to find a Stored XSS vulnerability and successfully discovered it. You can find the report on my profile. :)

Next, I started searching for an SSRF vulnerability. I uploaded the SVG image, intercepted the request, injected my payload,

```
<svg xmlns:svg="http://www.w3.org/2000/svg" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="200" height="200"> 
<image height="30" width="30" 
xlink:href="https://gue8agnu95o7210f9n980qf1ksqjed22.oastify.com" /> 
</svg>
```
and completed the image upload process. Then I opened the image I had uploaded in a new tab.

And BOOOOOOOOOOOOOOOOOOM!

I successfully triggered SSRF.

Done

Thank you for watching.

“Don’t hesitate if you have any questions about anything.

I will leave my account for contact.

Follow me.”
