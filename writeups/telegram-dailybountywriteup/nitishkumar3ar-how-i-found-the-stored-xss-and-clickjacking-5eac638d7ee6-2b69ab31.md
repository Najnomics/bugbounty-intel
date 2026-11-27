# How I found the Stored XSS and Clickjacking.

- **Source URL:** https://medium.com/@nitishkumar3ar/how-i-found-the-stored-xss-and-clickjacking-5eac638d7ee6?source=rss------bug_bounty-5
- **Fetched from:** https://medium.com/feed/@nitishkumar3ar
- **Fetched:** 2026-11-27
- **Channel:** @dailybountywriteup
- **Telegram message:**  (id 251)
- **Method:** medium-rss-content readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
Hello everyone! I’m Nitish, this is my first write-up. Hope you all are doing great.

#### **About XSS:**

Cross-Site Scripting (XSS) attacks are a type of injection, in which malicious scripts are injected into otherwise benign and trusted websites. XSS attacks occur when an attacker uses a web application to send malicious code, generally in the form of a browser-side script, to a different end user.

**STEP 1** — Go to [https://target.com/search-area-code-exchange-detail](https://www.telcodata.us/search-area-code-exchange-detail)

**STEP 2** — First enter “> this parameter in both boxes.

**STEP 3** — The input value box will display more space to enter the values.

**STEP 4** — And then inject the script “>\<script>alert(1)\</script> in both the boxes.

**STEP 6** — Then see the response in the browser and the popup will appear.

**How to Prevent XSS:**

To keep yourself safe from XSS, you must sanitize your input. Your application code should never output data received as input directly to the browser without checking it for malicious code.

**And the second bug I found is Clickjacking.**

Clickjacking, also known as a “UI redress attack”, is when an attacker uses

multiple transparent or opaque layers to trick a user into clicking on a button or link on another page when they were intending to click on the top-level page.

**Method 1:**

1. Open notepad

2. enter the following script

\<html>

\<head>

\<title>Clickjacking test page\</title>

\</head>

\<body>

\<iframe src=”[https://www.target.com/](https://www.telcodata.us/)" width=”500" height=”500"\</iframe>

\</body>

\</html>

3. Save this as test.html

4. open with a browser and the website gets successfully loaded

which proves it is vulnerable to Clickjacking.

**Method 2:**

1. Go to [www.lookout.net/test/clickjacking](http://www.lookout.net/test/clickjacking)

2. enter https:[https://www.target.com/](https://www.telcodata.us/)

3. Website gets successfully loaded.

**Countermeasures:**

X-Frame-options is a security header to prevent clickjacking

Go to .htaccess file (Shared web hosting)

X-FRAME-OPTIONS “SAME-ORIGIN”

Go to httpd.conf file in apache and enter the following

X-FRAME-OPTIONS “SAME-ORIGIN”

That’s all, thank you very much for reading it till the last. Hope you would have enjoyed it.
