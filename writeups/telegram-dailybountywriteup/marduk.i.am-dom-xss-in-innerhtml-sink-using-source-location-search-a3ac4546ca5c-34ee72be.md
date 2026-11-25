# DOM XSS in innerHTML sink using source location.search

- **Source URL:** https://medium.com/@marduk.i.am/dom-xss-in-innerhtml-sink-using-source-location-search-a3ac4546ca5c?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20240105161739/https://medium.com/@marduk.i.am/dom-xss-in-innerhtml-sink-using-source-location-search-a3ac4546ca5c?source=rss------bug_bounty-5
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/4762 (id 4762)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# DOM XSS in innerHTML sink using source location.search

--

This is the second lab from PortSwigger Web Security Academy exploring Document Object Model-based Cross-site Scripting. DOM-based XSS allows an attacker to manipulate the DOM through JavaScript script injections usually through user-controlled data, often found in the site’s own URL.

The description states: This lab contains a DOM-based cross-site scripting vulnerability in the search blog functionality. It uses an *innerHTML* assignment, which changes the HTML contents of a *div* element, using data from *location.search*. To solve this lab, perform a cross-site scripting attack that calls the ***alert*** function.

Going into this lab I thought it would be more involved but it is pretty straight forward. Starting out, everything looks the same. Simple blog page with a search bar. Throw a random string into the search bar. One you know will not get any results.

Right click on the result and choose Inspect from the drop-down menu. Your search query should now be highlighted in your DOM-browser. If not use the search bar for your DOM-browser to find your query.

I notice my query is nested within it’s own \<span> element just how I typed it ( \<span id=”searchMessage”>***MardukWasHere***\</span> ).

If you are not familiar with innerHTML and outerHTML let me explain for a minute. If you are all ready familiar feel free to jump ahead. In the DOM-browser, right click on the \<h1> element. In the drop-down menu find *copy.* You will be given options. In Firefox you can choose to either copy outer or innerHTML. I’ll choose innerHTML and paste it here.

`<span>0 search results for '</span><span id="searchMessage">MardukWasHere</span><span>'</span>`
If I would have chosen outerHTML it would have included the \<h1> tags as well. That is what the lab description was referring to when it said “It uses an *innerHTML* assignment”. \<span> is the “innerHTML assignment”. Since [innerHTML](https://web.archive.org/web/20240105161739/https://medium.com/@verity.carlos/why-you-shouldnt-use-innerhtml-and-what-to-use-instead-ed99d064a416) can add content that includes actual bits of HTML code rather than simple strings, it may pose a security risk.

OK, we’re back. Building off of the last [DOM lab](https://web.archive.org/web/20240105161739/https://medium.com/@marduk.i.am/dom-xss-in-document-write-sink-using-source-location-search-ae458bc5c85f) (actually “taking off”), I decided to use a variation of the payload we used to solve the lab. I’m going to remove the first two characters (“>) from the payload leaving:

```
<!--Original Payload-->
"><img src=x onerror=alert('MardukWasHere')>
<!--New Payload-->
<img src=x onerror=alert('MardukWasHere')>
```
Imagine the payload inserted like this:

`<span id="searchMessage"><img src=x onerror=alert('MardukWasHere')></span>`
I was thinking that since my search query is already nested between two tags (…>MardukWasHere\<…), there was no need to “break out” of anything. I entered the shortened payload into the search bar.

```
<h1>
    <span>0 search results for '</span>
    <span id="searchMessage">
        <img src="x" onerror="alert('MardukWasHere')">
    </span><span>'</span></h1>
<script>
    function doSearchQuery(query) {
        document.getElementById('searchMessage').innerHTML = query;
    }
    var query = (new URLSearchParams(window.location.search)).get('search');
    if(query) {
        doSearchQuery(query);
    }
</script>
<hr>
```
And that’s it. Lab solved! Congratulations!
