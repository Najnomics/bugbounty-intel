# Bypassed Input Escaping for XSS

- **Source URL:** https://medium.com/@kush.kira/bypassed-input-escaping-for-xss-d39b7b7ab284?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20231012160056/https://medium.com/@kush.kira/bypassed-input-escaping-for-xss-d39b7b7ab284
- **Fetched:** 2026-11-24
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/3821 (id 3821)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
Hey, bounty hunters hope you all doing great in hunting and securing the internet.

It’s likely that you’ve heard about cross-site scripting, even if you’re new to cybersecurity. Cross-site scripting is still a significant issue in many web applications, and it can have devastating consequences. Everyone should be concerned about cybersecurity; it’s not only for security experts.

I won’t go through the many varieties of XSS with you because you should already be familiar with them.

In this write-up, I’ll discuss a situation I ran across that I think is **legen**-wait for it-**dary** because it tests how well you understand XSS and how browsers work.

You must first understand **input escaping**:

“**Escaping is the process of adding or changing characters in the user input to prevent them from being interpreted as code or commands by the browser or the server**.”

One basic scenario of XSS is where the reflection is reflected in the **Input tag.**

XSS in hidden inputs is frequently very difficult to exploit because typical JavaScript events like onmouseover and onfocus can’t be triggered due to the element being invisible.

Well, the application was blocking \< and > but accepting “ which was all I needed to exploit it.

Now render on web browser and Press ALT+SHIFT+X on Windows or CTRL+ALT+X on OS X to trigger the payload.

I started to investigate the patch the developer had released to address this after it was pushed out (which was ludicrous).

I was surprised to see that they were doing **input validation**, which can be bypassed, depending on how an application handles your payload.

After a lengthy analysis of five minutes, the application allowed three double quotes and blocked four double quotes.

Here, they came up with “**don’t let four double quotes be in parameter**”

`They must have done a through analysis of the payload xD and determined taht it had four double quotes, therefore let's do input validation and block anytime 4 double quotes are supplied as a parameter. really wise, huh?`

`" accesskey="X" onclick="alert(1)`
I made a payload with 1 quote (which is completely unbalanced at all) just to escape the value tag.

`" accesskey=X onclick=alert(1)`
And the reflection goes by

`<input type="hiden" name="1vHeading" value="kira" accesskey=X onclick=alert(1)"/>>`
So the concept goes as the browser will balance it for us (some of you might know it already but some may not, it's for you to keep in your knowledge).

As you can see application HTML encoded the last quote which was added by the browser hence XSS won’t trigger here.

How to tackle this? Simple as making a sunny-side-up egg, just need to add a random tag after the alert so that the payload gets balanced; the rest is irrelevant.

See, it’s all done, After this you you can show impact however you want.

I hope this article has taught you something new.

Written by: [Kira](https://twitter.com/kush_kira/)
