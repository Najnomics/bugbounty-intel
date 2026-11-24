# HackTrick

- **Source URL:** https://medium.com/@rdillon73/hacktrick-stored-xss-via-a-svg-image-3def20968d9?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20260713154046/https://medium.com/@rdillon73/hacktrick-stored-xss-via-a-svg-image-3def20968d9
- **Fetched:** 2026-11-24
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/3366 (id 3366)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# HackTrick: Stored XSS via a SVG image

Stored Cross-Site Scripting (XSS) is a type of security vulnerability that occurs when an attacker successfully injects his code into a web page and the modified page is then stored so that every future visitor will be exposed to it. As an example, consider a blog where visitors can add comments to continue an ongoing discussion. This vulnerability allows the attacker to execute their malicious code within the context of other users’ browsers, potentially leading to various security issues like stealing cookies and, possibly, a user’s session.

The process of a Stored XSS attack generally involves the following steps:

1. **Injection**: The attacker finds an input field in the website that allows the injection of additional code into the application.
2. **Storage:** The malicious code injected by the attacker is stored on the server, typically in a database or some other form of storage.
3. **Serving**: When other users access a specific page or retrieve the stored data containing the malicious script, the server delivers the stored data, including the malicious code, to the user’s browser.
4. **Execution**: The malicious script runs in the context of the user’s browser, potentially allowing the attacker to steal sensitive information, perform unauthorized actions, or carry out other malicious activities on behalf of the user.

Contrary to Reflected XSS, which are served to individual users by the hacker usually in the form of carefully crafted links containing the payload itself, Stored XSS can be much more dangerous as they target every single user that visits the affected website without any additional work from the hacker.

In this post, I want to illustrate this vulnerability slightly differently from what we usually see online: we will deliver a cookie-stealing script hidden in an SVG image that, for example, could be used as the hacker’s signature in an otherwise valid blog post:

```
<!DOCTYPE html>
<html>
<head>
  <title>Example of stored XSS with SVG file </title>
</head>
<body>
<script type="text/javascript">
// Function to set a cookie
function setCookie(cookieName, cookieValue, expirationDays) {
  var date = new Date();
  date.setTime(date.getTime() + (expirationDays * 24 * 60 * 60 * 1000));
  var expires = 'expires=' + date.toUTCString();
  document.cookie = cookieName + '=' + encodeURIComponent(cookieValue) + '; ' + expires + '; path=/';
}
// create a cookie for this page
setCookie('username', 'JohnDoe', 7); // Sets a cookie named 'username' with value 'JohnDoe' that expires in 7 days
</script>
 <svg width="100" height="100" xmlns="http://www.w3.org/2000/svg">
    <circle cx="50" cy="50" r="40" stroke="black" stroke-width="3" fill="red" />
  <script type="text/javascript">
    <![CDATA[
      // JavaScript code embedded in the SVG
      function getUserCookies() {
  
        // Read all cookies
        var allCookies = document.cookie;
        alert("Cookies found:" + allCookies)
      }
      // call the function
      getUserCookies();
    ]]>
  </script>
  </svg>
</body>
</html>
```
You can save and try the previous page yourself (it won’t bite, I promise! :P). The first script creates a new cookie. This is the “secret” information the hacker wants to steal. I trust in your suspension of disbelief here. In real life, this would be something like session-id or other sensitive information.

Then we have our image. just a red circle: it looks innocent enough but the SVG format allows for the insertion of scripts and, here, we write a few lines of javascript to access all the website’s cookies, which are then displayed in the classic alert box that is used in all the typical XSS proofs-of-concept.

An actual attacker would then transmit the stolen information to his own server for later use.

This example is a reminder all input fields in every webpage must be taken care of, sanitizing all inputs, including images!

P.S. For more *“hack tricks”*, have a look at “[The Hacker’s Zibaldone](https://www.amazon.com/Hackers-Zibaldone-Tutorials-Concepts-Cybersecurity-ebook/dp/B0C3WZC84L/)”!
