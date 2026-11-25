# DOM XSS in AngularJS expression with angle brackets and double quotes HTML-encoded

- **Source URL:** https://medium.com/@marduk.i.am/dom-xss-in-angularjs-expression-with-angle-brackets-and-double-quotes-html-encoded-62bc9a167c8e?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20240219022434/https://medium.com/@marduk.i.am/dom-xss-in-angularjs-expression-with-angle-brackets-and-double-quotes-html-encoded-62bc9a167c8e?source=rss------bug_bounty-5
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/4994 (id 4994)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# DOM XSS in AngularJS expression with angle brackets and double quotes HTML-encoded

--

In this lab from PortSwigger Web Security Academy we start diving into the world of AngularJS. The solution to this lab is very quick, however, understanding *why* it works will take more time. I think this time we are going to just solve the lab, then we will go into seeing the “*how’s*” and the “*why’s*”.

**Lab description:** This lab contains a DOM-based cross-site scripting vulnerability in a AngularJS expression within the search functionality.

AngularJS is a popular JavaScript library, which scans the contents of HTML nodes containing the ng-app attribute (also known as an AngularJS directive). When a directive is added to the HTML code, you can execute JavaScript expressions within *double curly braces*. This technique is useful when angle brackets are being encoded.

To solve this lab, perform a cross-site scripting attack that executes an AngularJS expression and calls the *alert* function.

Access the lab. You’ll be brought back to our simple blog page with a search bar.

Solving this lab is simple. It’s just inputting the right code string into the search bar. Input the following, from the “Solutions” tab, into the search bar and press Enter:

```
// This executes an AngularJS expression that calls the alert function.
{{$on.constructor('alert(1)')()}}
```
There it is. Done. Solved!

OK. Now that the easy part is out of the way, let’s see how this works.

First things first. How do we know we are working with AngularJS? There are some browser extensions you can add that will let you know, like [Wappalyzer](https://web.archive.org/web/20240219022434/https://www.wappalyzer.com/), or you can check the page source.

Right-click on the lab’s web page and select View page source from the drop-down menu. This will open the page source for easy inspection.

Below is the top few lines of our lab’s page source. A few things to point out here.

```
<!DOCTYPE html>
<html>
    <head>
        <link href=/resources/labheader/css/academyLabHeader.css rel=stylesheet>
        <link href=/resources/css/labsBlog.css rel=stylesheet>
        <script type="text/javascript" src="/resources/js/angular_1-7-7.js"></script>
        <title>DOM XSS in AngularJS expression with angle brackets and double quotes HTML-encoded</title>
    </head>
    <body ng-app>
        <script src="/resources/labheader/js/labHeader.js"></script>
        <div id="academyLabHeader">
```
1. AngularJS is typically loaded as an external script. Check for script references, and look for URLs containing “angular” or a specific version number. \<script type=”text/javascript” src=”/resources/js/**angular\_1–7–7.js**”>
2. In our lab, look for the \<body> tag, and you’ll see the attribute *‘ng-app’* declared, it indicates the usage of AngularJS. This attribute specifies the root element of the AngularJS application.
3. Not in this lab, but out in the wild, AngularJS often uses directives in HTML attributes to extend the functionality of elements. Look for attributes starting with *‘ng-’* within the HTML code, such as *‘ng-controller’*, *‘ng-model’*, or *‘ng-repeat’*. The presence of these directives suggests AngularJS integration.

Now that we know how to identify the use of AngularJS, how can an attacker exploit that to their advantage?

JavaScript frameworks, such as AngularJS, often evaluate the content contained inside double curly braces ( {{ }} ). We can check this by adding a simple expression inside a pair of double curly braces and searching for it on our blog page.

`{{2+2}}`
Check out the search result. It actually solved the expression! This will happen if developers use improper coding practices and or user input is not being properly sanitized and validated.

This simple test highlights a security flaw in the AngularJS framework when it comes to handling expressions, allowing attackers to inject and execute malicious code.

Can we just put our *alert()* function within the double curly braces to solve the lab? Something like the previous labs {{*javascript:alert()*}}.

Nope. That would be too easy. We need to find another way.

In JavaScript, you can define a function on the page by:

```
// Original
function test(){
    console.log('Marduk was here.')
}
test();
// Or this would do the same but dynamically!!
let test = Function('console.log("Marduk was here.")')();
```
Both will display a “Marduk was here.” to the console, however it is generally not recommended to use the *Function()* constructor in this way due to security concerns and potential issues with code maintainability.

In JavaScript, every object has a *‘constructor’* property, which refers to the constructor function that was used to create the object. This property is automatically created for every object, by the framework, and it can be accessed to determine the type or constructor function of an object.

- In the the original *function test()* method, the *‘constructor’* property of that function will reference the built-in *Function()* constructor.
- With the one-liner, *Function()*, the resulting function’s *‘constructor’* property still points to the *Function()* constructor.

So, in our payload, the *.constructor* is referring to the *Function()* constructor of the $on method. Let’s take a look at the exploded view of our payload.

`{{$on.constructor('alert(1)')()}}`
- **{{ }}** — We already know these encapsulate an expression we want to execute in AngularJS.
- $ — Let’s you know it’s part of the framework and not user defined.
- **on** — Method provided by the framework.
- **.constructor** — Property of an object that refers to the constructor function that created the object.
- **()** — Calls the newly created function.

But why the *$on* method? It doesn’t have to be. The main characteristic we need, in this case, is that it is a function. There are other preloaded methods available within the prototype, $on just creates a simple listening event.

I hope this article gives you more insight into what is actually occurring behind the scenes in this lab and the AngularJS framework. Some key learning opportunities of this lab include:

1. **Framework Familiarity:** Understanding different frameworks is crucial. How they accept, manipulate, and return data forms the foundation of effective web security practices.
2. **Function() vs. function:** Distinguishing between function and Function is not merely semantics. It’s a nuanced exploration of how JavaScript constructs functions, providing insights into security considerations.
3. **Testing for Vulnerabilities:** The simplicity of testing with expressions like {{2+2}} unveils potential vulnerabilities. This quick check can be a first step in identifying areas that need closer scrutiny.
4. **Identifying AngularJS:** From scrutinizing the page source to recognizing AngularJS-specific attributes like ng-app, we’ve gained tools to identify the presence of AngularJS in web applications.

For more information about this lab, check out a very well done and informative video from [*z3nsh3ll*](https://web.archive.org/web/20240219022434/https://www.youtube.com/watch?v=QpQp2JLn6JA&t=945s). His videos are great!

Also check out [*MDN Web Docs*](https://web.archive.org/web/20240219022434/https://developer.mozilla.org/) reference pages. Easy to navigate and is a unified place for documentation about open web standards.
