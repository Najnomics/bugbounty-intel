# Reflected DOM XSS

- **Source URL:** https://medium.com/@marduk.i.am/reflected-dom-xss-fdf60de841cb?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20240222174045/https://medium.com/@marduk.i.am/reflected-dom-xss-fdf60de841cb?source=rss------bug_bounty-5
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/5013 (id 5013)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Reflected DOM XSS

For years, it was commonly believed that there were only three types of cross-site scripting (XSS): reflected, stored, and Document Object Model-based (DOM). In reality they can and often do overlap. In this lab by PortSwigger Web Security Academy we are going to tackle a Reflected DOM-based XSS.

**Lab description:** This lab demonstrates a reflected DOM vulnerability. Reflected DOM vulnerabilities occur when the server-side application processes data from a request and echoes the data in the response. A script on the page then processes the reflected data in an unsafe way, ultimately writing it to a dangerous sink. To solve this lab, create an injection that calls the *‘alert()’* function.

**Note:** I am going to be using [Burp Suite](https://web.archive.org/web/20240222174045/https://portswigger.net/burp) Community Edition to help solve this lab. If you have Burp installed, you may want to have it running while we explore the site. Burp Suite is a software security application used for penetration testing of web applications. Both a free and a paid version of the software are available.

Let’s see what needs to be done. Access the lab. You will be brought to our simple blog page, again, with a search bar.

In the search bar add your alpha-numeric search string that will yield 0 results. I’ll be using my usual M4rdukWasH3re.

Our search string is *reflected* back, in full, to the web page. Now we need to see where in the DOM our search string is showing up and how it is being processed. This will give us more information on how to solve this lab.

Right-click on your returned search string and select Inspect from the drop-down menu. This will bring up your DOM-browser with your search string highlighted.

```
<script src="/resources/js/searchResults.js"></script>
<script>search('search-results')</script>
<section class="blog-header">
    <h1>0 search results for 'M4rdukWasH3re'</h1>
    <hr>
</section>
```
See our reflected search string in the \<h1> tag? Also, check out the \<script> tags above our search string. These two scripts are processing our search string, then returning it in the \<h1> tag below. But how are they doing that?

The *‘src=/resources/js/searchResults.js’* is an external JavaScript file. Think of it as a dry cleaner doing your laundry instead of doing it at your house. The web page is processing our string “off-site” then returning the results to the page with *‘search(‘search-results’)’*.

But we still don’t see *how* our string is being processed. To do that, click on the ‘Network’ tab in your dev tools, shown below.

Refresh the blog page in order to see all the different connections the page is making.

Remember the two \<script> tags from earlier? The first one, *‘\<script src=”/resources/js/searchResults.js”>\</script>’*, let’s us know where we need to start looking.

Click on *searchResults.js.* Another window will show up with several different tabs. You’ll be on the *‘Headers’* tab to begin with , but we need to see it’s response.

Click on *‘Response’.*

Let’s take a look at the JavaScript code that processes our search string.

```
function search(path) {
    var xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            eval('var searchResultsObj = ' + this.responseText);
            displaySearchResults(searchResultsObj);
        }
    };
    xhr.open("GET", path + window.location.search);
    xhr.send();
```
The JavaScript is straightforward, without any obfuscation. But what’s it doing?

1. **function search(path)** — Declaring a function called search that accepts one parameter, path. This function gets called by the second \<script> from earlier, *‘\<script>****search****(‘search-results’)\</script>’.* Here, *‘search-results’* is being passed in as ‘*path’*.
2. **var xhr = new XMLHttpRequest();** — It uses the *‘XMLHttpRequest’* object to make a request to a specified *‘path’* plus the current URL’s search parameters.
3. **xhr.onreadystatechange = function() {…}** — Sets up a callback function to be executed whenever the *‘readyState’* property of the XMLHttpRequest changes.
4. **if (this.readyState == 4 && this.status == 200){…}** — Checks if the request has been completed (‘readyState == 4’) and if the response status is OK (‘status == 200’).
5. **eval(‘var searchResultsObj = ‘ + this.responseText);** — Uses the ‘eval()’ function to interpret and execute the response text as JavaScript code. It effectively creates a variable named ‘searchResultsObj’ and assigns it the value of the response.
6. **xhr.open(“GET”, path + window.location.search);** — Configures the XMLHttpRequest to make a GET request to the specified ‘path’ plus the current URL’s search parameters (‘window.location.search’).
7. **xhr.send();** — Sends the HTTP request.

In the breakdown above, #5 is actually our vulnerability. The title of this lab could have been ‘The Evils of eval()!’. Below is from [MDN Web Docs](https://web.archive.org/web/20240222174045/https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/eval):

## Back to the lab.

The object *‘xhr’* was created and an HTTP ‘GET’ request was sent to:

(“GET”, path + window.location.search)

OR

(*‘search-results’ + ‘?search=M4rdukWasH3re’)*

Clicking on *‘search-results?search=M4rdukWasH3re’* and looking at the Response tab you’ll see the response in JSON. Our results are also enclosed in double quotes.

We need to play around with our search string in order to see how certain characters effect our JSON response. This is where Burp Suite comes in.

Here we can see both the Request and the response from *‘search-results?search=M4rdukWasH3re’* in Burp.

From this point, you can right-click in the request box and select *‘Send to Repeater’*. Next, click on the Repeater tab.

On the left side of Burp Repeater you can alter your search string to try to ‘break-out’ of the response. Since our ‘searchTerm’ results are in double quotes, we are going to start by adding a single double quote to the end of our search string and our *alert()* function.

```
<!-- "-" is used instead of "+" because "+" is usually URL encoded. -->
M4rdukWasH3re"-alert(1)
```
Look what happens in Burp.

The backslash that shows up is an escape character used to say ‘ignore the next character’ so it does not terminate the *‘searchTerm’.*

See, the double quote is still returned on the page.

However, if we add our own escape character, before the double quote, what will happen?

`M4rdukWasH3re\"-alert(1)`
Look how our search string was processed in Burp.

Now our double quote has terminated our search string and our *‘-alert(1)’* has been broken out!

But it’s still not a valid payload. We still have the closing double quote and curly brace that is supposed to close the JavaScript object.

In order to have a usable payload we have to manually close the JavaScript object by adding a closing curly brace *’}’* to our payload. Then comment out everything following with *‘//’*.

```
<!-- In JavaScript using double forward slashes comments out everything after them -->
<!-- Final payload looks like -->
M4rdukWasH3re\"-alert(1)}//
```
Enter the payload into Burp Repeater and hit Send. Check out the results

We’ve done it! It looks like it is working.

Copy and paste the payload from the Burp Request into our blog page search bar and hit Enter.

Congratulations! By successfully manipulating the search string, you’ve demonstrated how vulnerabilities like these can be exploited. Feel free to explore more labs to enhance your understanding of web security.
