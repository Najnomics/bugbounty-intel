# Stored XSS via Image Upload

- **Source URL:** https://medium.com/@osamamohamed21212121/stored-xss-via-image-upload-b75edecf1e54?source=rss------bug_bounty-5
- **Fetched from:** https://medium.com/feed/@osamamohamed21212121
- **Fetched:** 2026-11-27
- **Channel:** @dailybountywriteup
- **Telegram message:**  (id 7260)
- **Method:** medium-rss-content readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
Hello, my name is Osama Mohammed, and I am a penetration tester and bug hunter.

Hi, welcome back to another blog. In this blog, we’re going to know how I found my( Stored XSS) in the external program. So, before starting, if you haven’t followed our medium account, do follow, guys. So without wasting time let’s get into the story of the (Stored XSS ).

After thoroughly inspecting and exploring the website, I found the function responsible for changing the profile picture. This is one of my favorite functions because it often allows me to discover multiple vulnerabilities.

The first thing I attempted was uploading a shell.php file instead of a profile picture. However, I was unable to obtain a shell, despite trying again and using all the bypass techniques I knew. In the end, I couldn't succeed.

At that point, I didn’t give up, but I took a few hours to rest due to my continuous efforts to get the shell.

Afterward, I tried uploading an image in SVG format, and it worked. The website accepted images in this format. At that moment, I thought of three potential vulnerabilities I could exploit: **XXE**, **Stored XSS**, and **SSRF**.

I first attempted to find an **XXE** vulnerability, but unfortunately, I couldn’t exploit it either.

Then, I moved on to the **Stored XSS** vulnerability. I uploaded the SVG image, intercepted the request, injected my payload,

and continued with the image upload process. Afterward, I opened the image I had uploaded in a new tab.

And BOOOOOOOOOOOOOOOOOOM!

I successfully triggered **Stored XSS**.

Done

Thank you for watching.

“Don’t hesitate if you have any questions about anything.

I will leave my account for contact.

Follow me.”

*LinkedIn Profile :*
