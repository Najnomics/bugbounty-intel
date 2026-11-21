# Understanding DOM-based XSS

- **Source URL:** https://medium.com/@evyeveline1/understanding-dom-based-xss-70ea74401e7b?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250918195338/https://medium.com/@evyeveline1/understanding-dom-based-xss-70ea74401e7b
- **Fetched:** 2026-11-21
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/9345 (id 9345)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Understanding DOM-based XSS

I am fairly new to coding, and while I understand the basics I’m still getting familiar with classes and their functions. When I came across to DOM-based XSS I found it quite difficult since often requires analysis of the source code. However I started to understand it more and realized many others might encounter this difficulty. This article is for those who are just starting out or anyone who finds DOM-based XSS hard to discover and exploit. I am hoping this could be helpful for you.

First of all we must know what is the difference between DOM-based XSS and Stored and Reflected XSS. Unlike the other two, DOM-based XSS doesn’t reach the server at all, it all happens on the client-side. The vulnerability occurs when the website’s Javascript manipulates the DOM(Document Object Model) based on unsanitized or unfiltered user input.

**What is DOM?**

In simple terms DOM is like a map of the website made of different nodes( elements of the page like images, text, etc.). When a web page is loaded in the browser, the browser converts the HTML, XML or CSS into a tree-like structure known as DOM. This structure allows JavaScript to interact with the page dynamically, so technically we are able to change the page’s content and structure without having to reload the page.

**Sink and Source Concept**

If we want to understand DOM-based XSS we must first understand what source and sink are.

The source is any place on a web page where user input can be added and later might be used in the page’s content. Those can be url parameters, user input like comments or posts, cookies, local storage and any other input where untrusted data can be entered by a user.

The sink is essentially where the data inserted in the source goes, in our case we are interested where the data is inserted into the DOM. Few examples are JavaScript functions, JQuery methods or event handlers.

If this data isn’t properly sanitized it can lead to a DOM-based XSS vulnerability.

To fully understand DOM-based XSS vulnerabilities, we need to bring together the concepts of source, sink, and how JavaScript interacts with the DOM.

Common Sources:

- window.location — URL of current page
- document.cookie -cookies stored in the browser for the site
- setTimeout()/setInterval() -functions that delay execution of code
- \<user> \<textarea> \<select> \<img src> — user input field and html attributes
- windows.location.href — full URL of current page
- windows.location.hash -fragment identifier of the URL(after the #)
- window.search -query string (after ?)
- document.referrer -the referring URL
- localStorage/ sessionStorage -stores data on the client-side
- document.title — page title

Commun Sinks:

- innerHTML -adds or modifies content inside a HTML element on the web page
- outerHTML — modifies the entire HTML element( it replaces it with a new HTML)
- document.write()- adds HTML or JavaScript to the document
- eval()-executes JavaScript that is passed to a string
- setAttribute() — sets an attribute of an HTML element
- set Timeout() / setInterval()-executes code after a delay
- window.location -modifies current page’s URL
- onload .onclick — triggers JavaScript code when an event occurs

As we can see, some elements can be both sources and sinks because many JavaScript objects and methods can accept untrusted data from users and then process and execute that data in a way that can lead to vulnerabilities like XSS. Those elements are called multi-role elements and have dual-purpose.

Let’s take this lab as an example : [https://portswigger.net/web-security/cross-site-scripting/dom-based/lab-document-write-sink-inside-select-element](https://portswigger.net/web-security/cross-site-scripting/dom-based/lab-document-write-sink-inside-select-element)

If we open our DevTools with F12 we can analyse the source code on the client-side and see how the source “window.location.search” it’s taking the value after storeID which goes to the sink “document.write()” which is writing data directly on the webpage.

In simple terms the value of sotreID in the URL is used in the document.write() statement inserting it into the webpage without sanitization. If we can successfully manipulate the string after StoreId (StoreId=xss payload) the vulnerability happens because document.write() is executing it.

However StoreId is a hidden parameter, this won’t be visible on the page by deafult but can be added by us in the URL. 

URL of the vulnerable page : [https://0a0900ca047e805981cb8ad600aa004e.web-security-academy.net/product?productId=2](https://0a0900ca047e805981cb8ad600aa004e.web-security-academy.net/product?productId=2)

What shall we add to test it: [https://0a0900ca047e805981cb8ad600aa004e.web-security-academy.net/product?productId=2](https://0a0900ca047e805981cb8ad600aa004e.web-security-academy.net/product?productId=2)&storeId=vfnvdrknfcdkfcnek

Our value was inserted into the HTML without proper sanitization and it affects the page content dynamically. Hence the value was added to \<select> element we triggered the page to insert data as part of DOM. If we use a malicious payload the page would execute it. Normally, only predefined values such as “London,” “Paris,” and “Milan” should be allowed.

In fact inject this payload : \<img%20src=1%20onerror=”alert(1)”> triggered the alert window which proves that the page is vulnerable to DOM-based XSS.

Here is a cheat sheet with some useful DOM-based XSS obfuscated payload :

\<iframe src=”[https://victim.com#](https://vulnerable-website.com#)" onload=”this.src+=’\<img src=x onerror=alert(1)>’”>\</iframe>

javascript:alert(document.cookie)

javascript:String.fromCharCode(97,108,101,114,116,40,49,41)

\<img src=”x” onerror=”alert(1)”>

document.write(‘\<img src=”x” onerror=”alert(1)”>’)

\<scRipt src=”javascript:alert(1)” />

javascript:eval(atob(‘YWxlcnQoMSk=’))

And you can also find plenty on here : [https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/XSS%20Injection/README.md#dom-based-xss](https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/XSS%20Injection/README.md#dom-based-xss)

DOM-Based XSS can be difficult to detect by automatic tools because it happens on the client-side so it’s important to understand the source code and how JavaScript interacts with the DOM.
