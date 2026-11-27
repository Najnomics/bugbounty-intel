# HTML Injection to RCE

- **Source URL:** https://aditya-chauhan17.medium.com/html-injection-to-rce-fa28f8b6f436?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20251128114736/https://aditya-chauhan17.medium.com/html-injection-to-rce-fa28f8b6f436
- **Fetched:** 2026-11-27
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/1715 (id 1715)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# HTML Injection to RCE

HTML injection, also known as cross-site scripting (XSS), is a type of vulnerability that allows attackers to inject malicious code into a website’s HTML code. If this vulnerability is not addressed, it can lead to remote code execution (RCE), which allows attackers to execute code on the server hosting the website. In this blog, we will explore HTML injection to RCE in more detail, and provide an example of how this vulnerability can be exploited.

**HTML Injection to RCE**: An Overview

HTML injection to RCE occurs when an attacker is able to inject malicious code into a website’s HTML code, which is then executed on the server hosting the website. This can occur through a number of methods, such as input fields, cookies, or URLs, and can be used to steal user credentials, redirect users to malicious websites, or even take control of the server hosting the website.

Example of HTML Injection to RCE

To better understand how HTML injection to RCE works, let’s consider a simple example. Suppose we have a website that allows users to submit comments. The website takes the user’s comment and displays it on the page. The HTML code for the page looks like this:

```
<!DOCTYPE html>
<html>
<head>
	<title>Example Website</title>
</head>
<body>
	<h1>Comments</h1>
	<div id="comments">
		<!-- user comments will be inserted here -->
	</div>
	<form action="/submit-comment" method="POST">
		<label for="comment">Add a comment:</label><br>
		<textarea name="comment" id="comment" rows="4" cols="50"></textarea><br>
		<input type="submit" value="Submit">
	</form>
</body>
</html>
```
Suppose an attacker submits a comment that contains the following code:

`<script>alert("Hello, World!");</script>`
This code will be inserted into the website’s HTML code, resulting in the following:

```
<!DOCTYPE html>
<html>
<head>
	<title>Example Website</title>
</head>
<body>
	<h1>Comments</h1>
	<div id="comments">
		<script>alert("Hello, World!");</script>
	</div>
	<form action="/submit-comment" method="POST">
		<label for="comment">Add a comment:</label><br>
		<textarea name="comment" id="comment" rows="4" cols="50"></textarea><br>
		<input type="submit" value="Submit">
	</form>
</body>
</html
```
Now, every time a user visits this page, the “Hello, World!” message will be displayed as an alert box. This may not seem like a serious issue, but it demonstrates how an attacker can inject code into a website’s HTML code.

To take this a step further, suppose an attacker submits the following code as a comment:

`<script>var xhttp = new XMLHttpRequest(); xhttp.open("GET", "/admin/get-user-data", true); xhttp.send();</script>`
This code will create a new XMLHttpRequest object and send a GET request to the server hosting the website. The request will be sent to the “/admin/get-user-data” endpoint, which the attacker assumes will return sensitive information about the website’s users. If the server is not properly secured, this request could allow the attacker to access this sensitive information.

To prevent HTML injection to RCE, it is important to properly sanitize user input and validate all user input before it is used in a website’s HTML code. This can be done by using input validation and sanitization libraries, such as OWASP’s Java Encoder Project or PHP’s HTML Purifier.
