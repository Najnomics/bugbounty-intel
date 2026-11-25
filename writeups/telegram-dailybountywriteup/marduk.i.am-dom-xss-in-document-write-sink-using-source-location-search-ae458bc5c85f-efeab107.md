# DOM XSS in document.write sink using source location.search

- **Source URL:** https://medium.com/@marduk.i.am/dom-xss-in-document-write-sink-using-source-location-search-ae458bc5c85f?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20240105163352/https://medium.com/@marduk.i.am/dom-xss-in-document-write-sink-using-source-location-search-ae458bc5c85f?source=rss------bug_bounty-5
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/4744 (id 4744)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# DOM XSS in document.write sink using source location.search

--

This is the [third lab](https://web.archive.org/web/20240105163352/https://portswigger.net/web-security/cross-site-scripting/dom-based/lab-document-write-sink) in a series from PortSwigger Web Security Academy, focusing on cross-site scripting (XSS).

The description states: This lab contains a DOM-based cross-site scripting vulnerability in the search query tracking functionality. It uses the JavaScript ***document.write*** function, which writes data out to the page. The ***document.write*** function is called with data from ***location.search***, which you can control using the website URL. To solve this lab, perform a cross-site scripting attack that calls the ***alert*** function.

This lab is a little more involved than the [reflected](https://web.archive.org/web/20240105163352/https://medium.com/@marduk.i.am/reflected-xss-into-html-context-with-nothing-encoded-8d3fb3a9eaf5) and [stored](https://web.archive.org/web/20240105163352/https://medium.com/@marduk.i.am/stored-xss-into-html-context-with-nothing-encoded-e0ba5f2a1952) XSS labs. I will be taking more of a “scenic route” in solving this lab so we really understand what is happening.

A little context before we start. A [Document Object Model](https://web.archive.org/web/20240105163352/https://en.wikipedia.org/wiki/Document_Object_Model) (DOM) tree is a hierarchical representation of an HTML or XML document. In your browser’s developer tools look for the Inspector tab or your browser’s equivalent. I’m using Firefox, if you are using Chrome look for Element.

This is the DOM-browser. It allows you to easily navigate though the workings of a web page. The DOM tree is not JavaScript, however, it can be manipulated by it. Manipulated by scripts and special characters like we used in the [reflected](https://web.archive.org/web/20240105163352/https://medium.com/@marduk.i.am/reflected-xss-into-html-context-with-nothing-encoded-8d3fb3a9eaf5) and [stored](https://web.archive.org/web/20240105163352/https://medium.com/@marduk.i.am/stored-xss-into-html-context-with-nothing-encoded-e0ba5f2a1952) XSS labs.

In this lab we are taken to another blog page with a search bar similar to our [reflected](https://web.archive.org/web/20240105163352/https://medium.com/@marduk.i.am/reflected-xss-into-html-context-with-nothing-encoded-8d3fb3a9eaf5) XSS lab. Might as well check to see if the reflected XSS vulnerability was fixed. I entered *\<script>alert(document.cookie)\</script>* into the search bar to see how the page would respond.

Our entire script, including tags, was returned on the web page. Let’s see what is happening in the DOM browser. Right click on your search result and select Inspect from the drop-down.

Notice our script appears twice in the DOM browser. Once in the *\<h1>* tag, within single quotes, and once again in the *\<img src=…>* tag. But why? Look above the *\<img>* tag at the contents of the *\<script>* tag.

```
<script>
function trackSearch(query) {
    document.write('<img src="/resources/images/tracker.gif?searchTerms=' + query + '">');
}
var query = (new URLSearchParams(window.location.search)).get('search');
if (query) {
    trackSearch(query);
}
</script>
```
Let’s break this down a little bit.

- ***function trackSearch(query)*** — Defines a function that takes a *‘query’* as a parameter.
- ***document.write*** — creates *‘\<img src=”/resources/images/tracker.gif?searchTerms=’* adding whatever the variable *‘query’* is after the = sign.
- **var query** — creates a variable named *‘query’*. It will *.get* this from the *‘search’* property in the current query string *‘window.location.search’* using the *‘URLSearchParams’* object.
- **‘window.location’** — Current URL of the browser
- **‘.search’** — is a property of *‘window.location’* that returns the query string of the URL (the part of the URL after the question mark ?).

This script is designed to track the search queries in the URL. If a ‘search’ parameter is present in the URL, it calls the `trackSearch` function to generate an image tag with a tracking URL that includes the search query. This is commonly used for analytics or logging user interactions on a website.

Our original reflected XSS script didn’t work. But why not? We need to “break out” of the site’s script so we can inject our own script. The key to “breaking out” of this context will involve manipulating the value of ‘*query’* or *‘.search’.*

I am going to switch our query to something a little more easy to read, but I will add a double quote to the beginning to see what happens. To start with I search for: *“ MardukWasHere*

Notice the injection of the double quote at the beginning of the search parameter prematurely closes the *src* attribute value.

We “broke out” of the *src* attribute! Now if we change *mardukwashere* to an executable script tag, we may be able to solve this lab.

Going to use the following payload:

`"><img src=x onerror=alert('MardukWasHere')>`
Here’s the break down:

- **“>** — Closes the first *src* attribute and *img* element.
- **\<img** — Opens a new *img* element.
- **src=x** — Sets new image source to a non-existent resource (x), triggering …
- **onerror** — Attribute of the img element. When the source fails …
- **alert()** — Creates pop-up window
- alert(**‘MardukWasHere’**) — Specific message to be displayed within single quotes.

It worked! Congratulations!

You can see the script injection worked. We were able to break out of one img element and create a new one. Our payload triggered an onerror event, our pop-up window, effectively injecting and executing our own script within the page. This exercise underscored the importance of understanding the inner workings of the Document Object Model (DOM) and how it can be manipulated to exploit vulnerabilities.

Thank you for reading!

**Reflected XSS Lab:** [https://medium.com/@marduk.i.am/reflected-xss-into-html-context-with-nothing-encoded-8d3fb3a9eaf5](https://web.archive.org/web/20240105163352/https://medium.com/@marduk.i.am/reflected-xss-into-html-context-with-nothing-encoded-8d3fb3a9eaf5)

**Stored XSS Lab:** [https://medium.com/@marduk.i.am/stored-xss-into-html-context-with-nothing-encoded-e0ba5f2a1952](https://web.archive.org/web/20240105163352/https://medium.com/@marduk.i.am/stored-xss-into-html-context-with-nothing-encoded-e0ba5f2a1952)
