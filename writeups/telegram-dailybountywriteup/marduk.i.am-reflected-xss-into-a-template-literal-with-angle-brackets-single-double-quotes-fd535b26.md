# Reflected XSS into a Template Literal with Angle Brackets, Single, Double Quotes, Backslash, and…

- **Source URL:** https://medium.com/@marduk.i.am/reflected-xss-into-a-template-literal-with-angle-brackets-single-double-quotes-backslash-and-d5cf41f25b02?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20251005114657/https://medium.com/@marduk.i.am/reflected-xss-into-a-template-literal-with-angle-brackets-single-double-quotes-backslash-and-d5cf41f25b02
- **Fetched:** 2026-11-24
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/5214 (id 5214)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Reflected XSS into a Template Literal with Angle Brackets, Single, Double Quotes, Backslash, and Backticks Unicode-Escaped

### Lab Description:

This lab contains a reflected cross-site scripting vulnerability in the search blog functionality. The reflection occurs inside a template string with angle brackets, single, and double quotes HTML encoded, and back-ticks escaped. To solve this lab, perform a cross-site scripting attack that calls the *‘alert’* function inside the template string.

### Template Literals (Template Strings):

Template literals, also known as template strings, are used for string interpolation in JavaScript. They allow for creating strings that span multiple lines and include expressions or variables within them.

Template literals are delimited by back-ticks (\`\`) instead of single quotes (‘’) or double quotes (“”). **Within template literals, placeholders indicated by ${} syntax can be used to *embed expressions* or variables dynamically.** When the template literal is evaluated, these placeholders are replaced with the corresponding values.

```
// Example:
const name = "Marduk";
const age = 2200;
const message = `Hello, my name is ${name} and I am ${age} years old.`;
console.log(message);
// Output: Hello, my name is Marduk and I am 2200 years old.
```
In the example above, the *‘${name}’* and *‘${age}’* within the template literal are placeholders that get replaced with the values of the name and age variables when the template literal is evaluated. This makes template literals a powerful tool for generating strings dynamically and concisely. Especially when you start including expressions!

## Getting Started:

Access the lab and you’ll be brought back to our simple blog page. The search bar back this time so, as usual, a good place to start will be searching for an alpha-numeric string you know will return zero results.

Enter your string in the search bar and click *‘Search’*.

Our search string is reflected back to us on the results page. We can find out how it got there by right-clicking on our string. Select ‘Inspect’ from the drop-down menu.

You can use the search bar in the DOM to easily find your string. It appears two times.

Our DOM-browser shows two results for our string: the first within an \<h1> tag, and the second below within the \<script> tag.

```
<!-- DOM-browser -->
<section class="blog-header">
    <h1 id="searchMessage">0 search results for 'M4rdukwasH3re'</h1>
    <script>
        var message = `0 search results for 'M4rdukwasH3re'`;
        document.getElementById('searchMessage').innerText = message;
    </script>
    <hr>
</section>
```
There is the template literal the lab title was telling us about. It is being defined as the variable *‘message’*.

## Lab Solution:

Remember earlier in the template literal definition it was stated: “…**placeholders indicated by ${} syntax can be used to *embed expressions* or variables dynamically.”.**

This is *‘interpolation’*. It is the ‘good’ version of ‘injection’. Interpolation refers to the process of inserting values or expressions into a string. Whereas injection refers to the process of inserting malicious code or unintended data into a system or program.

In the context of a template literal enclosed within back-ticks, placing the *‘alert(1)’* function within curly braces, {}, will be interpreted as valid JavaScript code by the browser, triggering the pop-up.

```
// Final payload
${alert(1)}
```
Add our final payload to the search bar and click *‘Search’*.

Congratulations! You solved another one! Keep up the great work!

Check the DOM-browser to see how it worked.

```
<!-- DOM-browser. Notice our alert() is valid JavaScript! -->
<section class="blog-header">
    <h1 id="searchMessage">0 search results for 'undefined'</h1>
    <script>
        var message = `0 search results for '${alert(1)}'`;
        document.getElementById('searchMessage').innerText = message;
    </script>
    <hr>
</section>
```
See you next time!
