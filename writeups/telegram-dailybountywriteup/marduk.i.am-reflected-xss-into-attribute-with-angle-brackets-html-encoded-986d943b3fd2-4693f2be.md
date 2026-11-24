# Reflected XSS into attribute with angle brackets HTML-encoded

- **Source URL:** https://medium.com/@marduk.i.am/reflected-xss-into-attribute-with-angle-brackets-html-encoded-986d943b3fd2?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20240108015149/https://medium.com/@marduk.i.am/reflected-xss-into-attribute-with-angle-brackets-html-encoded-986d943b3fd2
- **Fetched:** 2026-11-24
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/4840 (id 4840)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Reflected XSS into attribute with angle brackets HTML-encoded

--

In this lab we are revisiting Reflected Cross-site Scripting (XSS). Our first lab introduced us to Reflected XSS, however, nothing was encoded. This time is just a little different, as the title reflects(*sorry, lol*), angle brackets will be encoded.

**Lab description:** This lab contains a reflected cross-site scripting vulnerability in the search blog functionality where angle brackets are HTML-encoded. To solve this lab, perform a cross-site scripting attack that injects an attribute and calls the *alert* function.

**Hint:** Just because you’re able to trigger the *alert()* yourself doesn’t mean that this will work on the victim. You may need to try injecting your proof-of-concept payload with a variety of different attributes before you find one that successfully executes in the victim’s browser.

First access the lab, and you’ll find yourself on our simple blog page with a search bar.

Let’s start by seeing how the search is working. Search for a random alpha-numeric string you know will return 0 search results. I went with my usual.

Our entire search string was returned within single quotes on the page. Let’s dig a little deeper. Below is the resulting script from the DOM-browser. Notice how our search string appears twice. Once in an \<h1> tag within single quotes, not too much we can do there. Next, it appears as the value attribute within the \<input> element.

```
<!-- M4rdukWasH3re -->
<section class="blog-header">
    <h1>0 search results for 'M4rdukWasH3re'</h1>
    <hr>
</section>
<section class="search">
    <form action="/" method="GET">
        <input type="text" placeholder="Search the blog..." name="search" value="M4rdukWasH3re">
        <button type="submit" class="button">Search</button>
    </form>
</section>
```
In the lab description, it tells us that angle brackets are encoded. Meaning if we include angle brackets (\<>), anywhere within our search string, they will be represented using their encoded equivalents to prevent us from “breaking out”. In the previous Reflected XSS lab we used:

```
<!-- Previous script -->
<script>alert(document.cookie)</script>
<!-- Used to "Break out" of -->
<h1>0 search results for 'M4rdukWasH3re'</h1>
```
Well, not really “breaking out”, more like “injecting in”. The point is our angle brackets were accepted as part of the search string. They will not be accepted this time. So we need to find another way.

We are going to focus on the second appearance of our search string, in the \<input> element, wrapped in double quotes. Let’s try “breaking out” of the value attribute by adding one set of double quotes at the end of your search string. Let’s look at the results:

```
<!-- M4rdukWasH3re" -->
<section class="blog-header">
    <h1>0 search results for 'MardukWasHere" '</h1>
    <hr>
</section>
<section class="search">
    <form action="/" method="GET">
        <input type="text" placeholder="Search the blog..." name="search" value="MardukWasHere" "="">
        <button type="submit" class="button">Search</button>
    </form>
</section>
```
A couple points of interest: First, on the web page, in the search bar our search string is still there except for the newly added double quotes. But they do appear in the \<h1> tag above the search bar. You can see that in the DOM-browser as well. Also, notice how the end of the value attribute changed at the end of the \<input> element.

It looks like the addition of the double quote closed the value attribute! Now we need to construct and add our payload.

The lab wants us to use the JavaScript function *onmouseover* to solve this lab. *onmouseover* is a JavaScript function that does just as the name implies. When the victim’s mouse pointer drifts over the search bar the script will execute, this time displaying our alert pop-up.

After the double quotes of your search string add the JavaScript function *onmouseover* and let it be equal to alert(1).

`YOUR_SEARCH_STRING" onmouseover="alert(1)`
Enter your payload into the search bar press enter.

Congratulations! You solved the lab! Keep up the good work!

In the “real world” an attacker could send an unsuspecting victim this link and everything will look like the legitimate site. Until they mouse-over the search bar, which will then execute the attacker’s script. Most likely **NOT** just a pop-up alert window.

**Up Next:**

Stored XSS into anchor href attribute with double quotes HTML-encoded

**Previous Labs:**

[DOM XSS in jQuery selector sink using a hashchange event](/@marduk.i.am/dom-xss-in-jquery-selector-sink-using-a-hashchange-event-bb3c355b3633)

[DOM XSS in jQuery anchor href attribute sink using location.search source](/@marduk.i.am/dom-xss-in-jquery-anchor-href-attribute-sink-using-location-search-source-b1000b4b16b3)

[DOM XSS in innerHTML sink using source location.search](/@marduk.i.am/dom-xss-in-innerhtml-sink-using-source-location-search-a3ac4546ca5c)

[DOM XSS in document.write sink using source location.search](/@marduk.i.am/dom-xss-in-document-write-sink-using-source-location-search-ae458bc5c85f)
