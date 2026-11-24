# Finding Reflected XSS + WAF Bypass As My first Bug!

- **Source URL:** https://medium.com/@Thigh_GoD/finding-reflected-xss-waf-bypass-as-my-first-bug-b79671f40de2?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20251126142304/https://medium.com/@Thigh_GoD/finding-reflected-xss-waf-bypass-as-my-first-bug-b79671f40de2
- **Fetched:** 2026-11-24
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/3731 (id 3731)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Finding Reflected XSS + WAF Bypass As My first Bug!

## Introduction:

I started out my hackerone journey somewhere in July of 2023, with very little experience (I started learning pentesting part-time in January 2023).

Before finding the bug, I was looking through a bunch of random programs trying to find anything I could work on, but to no success.

A while later, I suddenly got a private invitation to a Vulnerability Disclosure Program (VDP) and thought that since I didn’t have any experience and VDPs were usually easier to find bugs in, I might as well give it a shot.

The first couple of websites I enumerated had nothing of importance to look at, with most either being static sites (like blogs) or very little functionality (no login/register endpoints).

It was then that I discovered a website for google dorking common vulns like XSS, open redirect, etc.

## The Hunt Begins

This [website](https://taksec.github.io/google-dorks-bug-bounty/) was extremely convenient as it allowed me to quickly dork any domain I wanted to.

Despite some of these dorks returning absolutely nothing, I started putting every single In-Scope domain inside these dorks in the hopes of finding anything interesting at all.

Eventually, I came across an extremely suspicious endpoint we can call `example.php` .

The weird thing about this endpoint was that the domain it was found in, I had actually enumerated and tried finding bugs in before. In fact, it was a website that I’d already noticed to be largely unmaintained or looked very old.

The fact that this endpoint suddenly appeared out of nowhere when I wasn’t able to find it before, led me to believe this could be an unmaintained or hidden feature.

I looked at the `example.php` and realized that the page was empty.

However, looking at the source code via Ctrl + U showed me a couple hidden href attributes that indicated the intended usage of this endpoint, which was as an embedding tool.

(I don’t have a screenshot so here’s an example.)

`<a href=https://www.REDACTED.com/example.php?t=test&p=test&s=test&u=https://www.REDACTED.com/sumtingwong.php>`

The endpoint would essentially take a couple parameters such as the url of whatever I wanted to embed, and the title of the embed and create an embed out of it. I will show examples of how this looked like later on.

However, it seems like this tool was not intended to have user-controlled input, but instead utilize the pre-built ones I saw in the hidden href tags.

So the parameters were `t` , `p` and `s` . The `t` parameter controlled the title of the embed, but the `p` and `s` didn’t have any obvious usage.

Regardless, I started by trying a simple HTML payload in all the parameters, to which I found out that the `p` parameter was reflected directly into the HTML code without sanitzation or escaping.

What did this mean? It was possible to run payloads such as this:

`?t=somethingsomethingsomething&p=”/><a href=testing>THIS IS AN INJECTED HTML LINK</a>”&s=something`
In the actual HTML code of the website, it looked like this:

Rendered on the website itself:

The reason why there was a `"/>` at the start of the payload, was to escape from the meta tag, such that the new tags would be rendered as well.

Of course, this isn’t considered XSS until you get the classic alert or prompt popup box.

At first I tried something like `<script>alert(1)</script>` and `<img src=x onerror=alert(1)>` but as you can tell from the title, there was a WAF!

The WAF more specifically was cloudfare, and tbh I thought all hope was lost, I used just about every bypass method on [Hacktricks](https://book.hacktricks.xyz/pentesting-web/xss-cross-site-scripting) and [Portswigger](https://portswigger.net/web-security/cross-site-scripting/cheat-sheet), and then I attempted to fuzz the possible tags and events like `<img>` or `onload` respectively.

Found out that literally all of them were filtered and blocked by the WAF….except for my original payload.

`”/><a href=testing>THIS IS AN INJECTED HTML LINK</a>”`
Now, you may be wondering, how can you trigger XSS from this?

Well, if you don’t know, `<a>` and `href` allows for javascript execution like this `<a href="javascript:alert(1)">` , but as I suspected, this payload was also blocked, mainly because of the keywords `javascript` and `alert` .

So we need a way to obfuscate them.

I did some research and inside [Hacktricks](https://book.hacktricks.xyz/pentesting-web/xss-cross-site-scripting), there’s a section on `Blacklist Bypass` which details methods of bypassing WAFs that utilize a blacklist to block certain tags or events.

This was exactly what I needed as the WAF was blacklisting both javascript and alert keywords.

I tested all the payloads and found out that when you used a url encoded carriage return like `%0D` inside the quotation `"` of the payload I mentioned before: `<a href="javascript:alert(1)">` , you could achieve something like `<a href="ja%0Dva%0Dscr%0Dipt:aler%0Dt(1)">` and HTML would parse it as the original payload, however what appears on both the HTML source code and in the WAF’s eyes is something like this:

```
<a href="ja
va
scr
ipt:aler
t(1)">
```
Now this may seem weird, but the payload actually executes.

## Post-Exploitation

Further experimentation showed that it didn’t matter where the `%0D` was placed, so long as it was within the quotation marks `"` , and the payload would still work.

I tried for awhile to get a zero-interaction payload to work, as this payload required the user to click on the link, but as I’ve mentioned before, it seems like `<a>` was the only tag I could use, and all events like `onload` were filtered and didn’t work with `%0D` as they weren’t enclosed in quotation marks.

However, since this was an Embedding tool, I could actually showcase how an attacker could make this XSS more “phish-able”.

Firstly, I’ve mentioned before that there were other parameters in the vulnerable endpoint.

Mainly, there was a title `t` parameter that allowed me to put the title as the embed into anything I wanted.

So if I sent a phishing email with the title set to something extremely long, the link would look something like this:

Since the `t` parameter is an actual valid parameter, I could put something that seemed legitimate in there (that was long enough to hide the payload), while the actual payload would not be shown.

Not only that, but in platforms such as discord, you could also create embeds that completely hide the payload. 

(Example still shows the payload since it’s not a full embed, but it’s still rather hard to tell.)

With that, I concluded my bug hunting and decided to send the report to the triage team on hackerone.

They got back to me within a couple days and verified my report. It took 1 month for me to get the report resolved, but only a couple days to get thanks. (Since this was a VDP)

## Conclusion

I am still a beginner in Bug Bounty hunting so I may have missed a couple obvious payloads, but I managed to get Reflected XSS with WAF Bypass as my first bug, and am truly glad to have learnt about WAF bypassing and google dorking from this experience.

I hope you enjoyed this writeup, and sorry for the lack of images, the VDP purged the endpoint as it was deprecated so I can’t go back to get example screenshots.

Here’s more details on the report and the final severity rating they gave me.

Btw, there was an open redirect in the same endpoint as well, but I had no proof of additional impact so I just ignored it.

Also, my next blog will probably be on my personal docker container project, I only made this article because it got resolved today lol.

Edit: Thanks to for telling me I had a screenshot which leaked the VDP’s domain.
