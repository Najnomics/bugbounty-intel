# Abusing CORS for an XSS on Flickr

- **Source URL:** https://medium.com/@proseizala/abusing-cors-for-an-xss-on-flickr-a820e3f28083?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20240715150338/https://medium.com/@proseizala/abusing-cors-for-an-xss-on-flickr-a820e3f28083?source=rss------bug_bounty-5
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/6666 (id 6666)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# [Abusing CORS for an XSS on Flickr](https://web.archive.org/web/20240715150338/https://whitton.io/articles/abusing-cors-for-an-xss-on-flickr/)

# Learn More About Cyber Security , Hacking And Get Your First Certificate For Free On : [https://alison.com/tag/it-security?utm\_source=alison\_user&utm\_medium=affiliates&utm\_campaign=40731788](https://web.archive.org/web/20240715150338/https://alison.com/tag/it-security?utm_source=alison_user&utm_medium=affiliates&utm_campaign=40731788)

lets get started :

I recently found an XSS on the mobile version of Flickr ([http://m.flickr.com](https://web.archive.org/web/20240715150338/http://m.flickr.com/)). Due to the way the bug is triggered, I thought it deserved a write-up.

Whilst browsing the site, you’ll notice that pages are loaded via AJAX with the path stored in the URL fragment (not as common these days now that [pushState](<https://web.archive.org/web/20240715150338/https://developer.mozilla.org/en-US/docs/Web/Guide/API/DOM/Manipulating_the_browser_history#The_pushState().C2.A0method>)

When the page is loaded, a function, `q()` (seen below), is called which will check the value of `location.hash`, and call `F.iphone.showSelectedPage()`.

In order to load pages from the current domain, it checks for a leading slash. If this isn’t present, it prepends one when calling the next function, `F.iphone.showPageByHref()`.

This function then performs a regex on the URL (line 160) to ensure that it’ll only load links from `m.flickr.com`. If this check fails, and the URL starts with a double slash (relative protocol link), it prepends it with [http://m.flickr.com](https://web.archive.org/web/20240715150338/http://m.flickr.com/)

Incase you didn’t notice, the first regex doesn’t anchor it to the start of the string. This means we can bypass it providing our own URL contains `m.flickr.com`.

We can get our own external page loaded by passing in a URL like so:

`//fin1te.net/flickr.php?bypass=m.flickr.com`

The code will check for a leading slash (we have two :)), which it’ll pass, then checks for the domain, which will also pass, then load it via AJAX.

Since we now have [CORS](https://web.archive.org/web/20240715150338/https://en.wikipedia.org/wiki/Cross-origin_resource_sharing) in modern browsers, the browser will send an initial OPTIONS request to the page (to ensure it’ll allow it to be loaded), then the real request.

All we need to do is specify a couple of headers (the additional options in the `Access-Control-Allow-Headers` are to prevent syntax errors in the Javascript), along with our payload.

The next part of the Javascript dumps the response into an element with `innerHTML`.

Which leads to our payload being executed.

# Fix

This issue is now fixed by anchoring the regex to the start of the string, and also running another regex to check if it starts with a double slash.
