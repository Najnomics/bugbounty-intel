# DOM XSS in jQuery anchor href attribute sink using location.search source

- **Source URL:** https://medium.com/@marduk.i.am/dom-xss-in-jquery-anchor-href-attribute-sink-using-location-search-source-b1000b4b16b3?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20240109134625/https://medium.com/@marduk.i.am/dom-xss-in-jquery-anchor-href-attribute-sink-using-location-search-source-b1000b4b16b3?source=rss------bug_bounty-5
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/4773 (id 4773)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# DOM XSS in jQuery anchor href attribute sink using location.search source

--

Welcome to the third lab from PortSwigger Web Security Academy exploring Document Object Model-based Cross-site Scripting (DOM-based XSS). In this lab we are getting introduced to [jQuery](https://web.archive.org/web/20240109134625/https://en.wikipedia.org/wiki/JQuery), an open-source JavaScript library that was developed to help simplify HTML DOM tree traversal and manipulation.

[Lab description](https://web.archive.org/web/20240109134625/https://portswigger.net/web-security/cross-site-scripting/dom-based/lab-jquery-href-attribute-sink): This lab contains a DOM-based cross-site scripting vulnerability in the submit feedback page. It uses the jQuery library’s *$* selector function to find an anchor element, and changes its href attribute using data from *location.search*. To solve this lab, make the “*back*” link alert *document.cookie*.

Access the lab to navigate to our blog page. Same simple blog page with several posts. Click on “Submit feedback”.

We are brought to form page with places for your Name, Email, Subject and message. The vulnerability we are looking for is going to be in the “**\< Back**” link at the bottom right of the page.

Right click on the “**\< Back**” link and select Inspect. This will open up the developer tools and bring up your DOM-browser to where the “**\< Back**” button is referenced.

“Back” is nested between an \<a> anchor tag: *\<a id=”backLink” href=”/”>Back\</a>*. This is saying if you click on the back button you’ll be taken to “/” from “href”. Where are these coming from? In the DOM-browser look below at the \<script>. It shows the following:

```
<script>
    $(function() {
        $('#backLink').attr("href", (new URLSearchParams(window.location.search)).get('returnPath'));
    });
</script>
```
This script is using jQuery to do a couple of things.

- **$(‘#backLink’) —** Is looking for an HTML element id set to “backLink”.
- **.attr(“href”, —** Is a method used to set *href* equal to whatever follows. In this case …
- **(new URLSearchParams(window.location.search)) —** We learned from previous labs, the part of the current URL after the question mark.
- **.get(‘returnPath’)); —** Is looking, in the current URL, after the “?”, if there is a “returnPath” set to anything.

So in short, this script is searching the current URL for “returnPath”. If the script finds it, “href” will be set to whatever that “returnPath” is. Currently *href=”/”.*

In previous DOM-XSS lab we injected JavaScript code into the DOM by posting our script to a comment page. We have broken out of an \<img> element to inject our own element. Here, in the context of this lab, we can not “break out” of this href attribute. Can we manipulate it though? If we can change the “/” at the end of the original URL to JavaScript code, it should change the setting of the href.

We can execute JavaScript within an anchor tag where the href is equal to “javascript:”. JavaScript placed directly after the colon will be executed whenever the back button is pressed.

```
<!--Original URL Ending-->
feedback?returnPath=/
<!--New URL Ending-->
feedback?returnPath=javascript:alert(document.cookie)
```
Replace the original URL ending and press enter. You should be returned to the same form page. However, lets check out that new and improved back button.

Right click on the back button and select Inspect.

Notice href is now set to ”javascript:alert(document.cookie)”! It looks like we did it! Now lets try it out.

Click the back button.

Congratulations!!! Keep up the good work!
