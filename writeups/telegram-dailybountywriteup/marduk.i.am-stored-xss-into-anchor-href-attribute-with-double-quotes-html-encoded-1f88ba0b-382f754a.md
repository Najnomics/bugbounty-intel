# Stored XSS into anchor href attribute with double quotes HTML-encoded

- **Source URL:** https://medium.com/@marduk.i.am/stored-xss-into-anchor-href-attribute-with-double-quotes-html-encoded-1f88ba0b990f?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20240109162951/https://medium.com/@marduk.i.am/stored-xss-into-anchor-href-attribute-with-double-quotes-html-encoded-1f88ba0b990f?source=rss------bug_bounty-5
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/4855 (id 4855)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Stored XSS into anchor href attribute with double quotes HTML-encoded

--

This is going to be our second lab from PortSwigger Web Security Academy dealing with Stored Cross-site Scripting (XSS). This is a pretty easy lab, where we will be expected to leave a comment on a blog that will store our payload within a href attribute. Our payload is supposed to execute when the victim clicks on the link to our display name.

**Lab description:** This lab contains a [stored cross-site scripting](https://web.archive.org/web/20240109162951/https://portswigger.net/web-security/cross-site-scripting/stored) vulnerability in the comment functionality. To solve this lab, submit a comment that calls the `alert` function when the comment author name is clicked.

Access the lab to be brought to our simple blog page. Click on “View Post” of any of the blogs you like. Scroll down to the bottom an fill out the required fields. Click on “Post Comment”.

Thank you for your comment! Now click on “Back to blog”.

Scroll down to find your comment. Notice your name is a hyperlink. Let’s find out where it’s trying to take us.

Right clicking on your name and selecting inspect will bring up your DOM-browser, with where your name is referenced, highlighted.

```
<section class="comment">
    <p>
        <img src="/resources/images/avatarDefault.svg" class="avatar">
        <a id="author" href="https://blah.com">Marduk</a> | 29 December 2023
    </p>
    <p>Marduk was here!</p>
    <p></p>
</section>
```
Recognize the href? It’s our website we entered into comment form. This will be our injection point.

The value of a href does not have to be a URL like “https://domain.com”. It may contain other protocols like “ftp://”, “mailto:”, “file:” or even “javascript:”!

From here lets fill out another form. This time though, let’s fill in the “Website:” portion with our payload.

In the “Website:” portion of the form we are going to leave the following JavaScript payload:

`javascript:alert(1)`
- **javascript:** — Will let the browser know to execute JavaScript.
- **alert(1)** — JavaScript function that will display a pop-up window on the victim’s screen with the message of “1” whenever someone clicks on our name that contains the payload.

Click “Post Comment”.

Thank you for your comment! Again. And congratulations! You solved the lab!

If you would like to see your payload in action, I always do, click on “Back to blog” and scroll down to see both of your posts.

Right click on your second name and select Inspect to see your payload in the DOM-browser:

```
<section class="comment">
    <p>
        <img src="/resources/images/avatarDefault.svg" class="avatar">
        <a id="author" href="javascript:alert(1)">Marduk</a> | 29 December 2023
    </p>
    <p>Marduk was here AGAIN!</p>
    <p></p>
</section>
```
Click on your second name. There’s our pop-up!

Keep up the great work. Keep it going!

**Up Next:**

Reflected XSS into a JavaScript string with angle brackets HTML encoded

**Previous Labs:**

[Stored XSS into anchor href attribute with double quotes HTML-encoded](https://web.archive.org/web/20240109162951/https://medium.com/@marduk.i.am/reflected-xss-into-attribute-with-angle-brackets-html-encoded-986d943b3fd2)

[DOM XSS in jQuery selector sink using a hashchange event](https://web.archive.org/web/20240109162951/https://medium.com/@marduk.i.am/dom-xss-in-jquery-selector-sink-using-a-hashchange-event-bb3c355b3633)

[DOM XSS in jQuery anchor href attribute sink using location.search source](https://web.archive.org/web/20240109162951/https://medium.com/@marduk.i.am/dom-xss-in-jquery-anchor-href-attribute-sink-using-location-search-source-b1000b4b16b3)

[DOM XSS in innerHTML sink using source location.search](https://web.archive.org/web/20240109162951/https://medium.com/@marduk.i.am/dom-xss-in-innerhtml-sink-using-source-location-search-a3ac4546ca5c)

[DOM XSS in document.write sink using source location.search](https://web.archive.org/web/20240109162951/https://medium.com/@marduk.i.am/dom-xss-in-document-write-sink-using-source-location-search-ae458bc5c85f)
