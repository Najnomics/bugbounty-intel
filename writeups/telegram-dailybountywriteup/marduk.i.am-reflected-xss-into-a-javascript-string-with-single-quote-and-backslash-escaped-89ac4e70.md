# Reflected XSS into a JavaScript String with Single Quote and Backslash Escaped

- **Source URL:** https://medium.com/@marduk.i.am/reflected-xss-into-a-javascript-string-with-single-quote-and-backslash-escaped-ba435167b43f?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20240224082042/https://medium.com/@marduk.i.am/reflected-xss-into-a-javascript-string-with-single-quote-and-backslash-escaped-ba435167b43f
- **Fetched:** 2026-11-24
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/5146 (id 5146)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Reflected XSS into a JavaScript String with Single Quote and Backslash Escaped

## [Lab Description](https://portswigger.net/web-security/cross-site-scripting/contexts/lab-javascript-string-single-quote-backslash-escaped):

This lab contains a reflected cross-site scripting vulnerability in the search query tracking functionality. The reflection occurs inside a JavaScript string with single quotes and backslashes escaped.

To solve this lab, perform a cross-site scripting attack that breaks out of the JavaScript string and calls the *‘alert’* function.

## Getting Started:

Access the lab. You will be brought to our simple blog page. This time with a search bar.

One of the first things we do when testing for XSS vulnerabilities is to search for a unique alpha-numeric string, that we know will not show up anywhere else in the page. This helps in identifying how the application processes and reflects user input, allowing us to isolate where the potential vulnerabilities lie.

Enter your search string into the search bar and click *‘Search’*.

Our query is reflected back to the page. Let’s see how. Right-click on your string and select ‘Inspect’ from the drop-down menu to bring up your DOM-browser.

Enter your string again in the DOM search bar and press *‘Enter’*.

Notice your string shows up three times. Once in a \<h1> tag, again in a \<script> tag, and finally in an \<img> tag.

```
<!-- We are interested in this one in the <script> tag -->
<script>
    var searchTerms = 'M4rdukWasH3re';
    document.write('<img src="/resources/images/tracker.gif?searchTerms='+encodeURIComponent(searchTerms)+'">');
</script>
```
## Crafting a Payload:

The obvious starting point here would be, since our string is wrapped in single quotes, to add a single quote to the end of our search string. In theory, this will close the existing JavaScript string and potentially allow us to inject additional JavaScript code outside of the string context, leading to a successful XSS attack.

Try adding a single quote to the end of your string.

```
<!-- DOM result after searching for M4rdukWasH3re' -->
<script>
    var searchTerms = 'M4rdukWasH3re\'';
    document.write('<img src="/resources/images/tracker.gif?searchTerms='+encodeURIComponent(searchTerms)+'">');
</script>
```
As the title of the lab describes, the single quote is being handled (escaped) properly by the addition of the backslash. Normally, we could try to add our own escape backslash in hopes that ‘their’ escape will escape ‘our’ escape, instead of the single quote, which will then break us out of the string context.

Yes, it’s confusing, but as the lab title tells us, the backslash will be escaped as well. We can always try though.

```
<!-- DOM results after searchinf for M4rdukWasH3re\' -->
<script>
    var searchTerms = 'M4rdukWasH3re\\\'';
    document.write('<img src="/resources/images/tracker.gif?searchTerms='+encodeURIComponent(searchTerms)+'">');
</script>
```
As you can see, the backslash is also being escaped properly. So we will need to find another way.

## Lab Solution:

Other characters, sometimes overlooked by developers, are angle brackets ‘\<>’. Since we can not break out of the string context, what if we can close the \<script> tag we are in?

If we add the following to the search bar and hit *‘Enter’* it will do a couple of things.

```
<!-- Payload -->
</script><script>alert(1)</script>
```
- \</script> — Closes the original script tag.
- \<script> — Opens our own script tag.
- alert(1) — Creates a pop-up window with a message of ‘1’.
- \</script> — Closes our tag.

Nice! Congratulations! You solved another one!

Lets check out how our \<script> impacted the DOM. Click ‘OK’ in the pop-up window then bring up your DOM if it is not already.

Here you can see how our \<script> injection worked.

See you next time!
