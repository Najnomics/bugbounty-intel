# [Web Security Academy] — Server-Side Vulnerabilities / Path Traversal

- **Source URL:** https://medium.com/@v0lts3c/web-security-academy-server-side-vulnerabilities-path-traversal-cf8104faaf1a?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250821193619/https://medium.com/@v0lts3c/web-security-academy-server-side-vulnerabilities-path-traversal-cf8104faaf1a
- **Fetched:** 2026-11-21
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/10280 (id 10280)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# \[Web Security Academy\] — Server-Side Vulnerabilities / Path Traversal

In this write-up, I will walk through a hands-on lab from PortSwigger’s Web Security Academy that demonstrates a Path Traversal vulnerability. This type of vulnerability allows attackers to access arbitrary files on a server by manipulating file path input. I documented this process as part of my learning and to build a portfolio of real-world web security examples.

# 🔍 **What is Path Traversal?**

Path Traversal (also known as Directory Traversal) is a vulnerability that enables an attacker to navigate the file system of a server and access files outside the intended directory, typically by injecting special path characters like \`../\`.


If a web application fails to properly validate user input in file paths, it may allow attackers to access sensitive files — for example, \`/etc/passwd\` on Linux or \`\windows\win.ini\` on Windows — even if those files are not meant to be exposed.

# 🧪 **Lab Walkthrough**

## 🔗 **Lab Link**

## 🎯 Lab Objective

This lab contains a path traversal vulnerability in the display of product images. To solve the lab, retrieve the contents of the \`/etc/passwd\` file.

## 🧩 Initial Functionality Review

Before starting, it’s worth noting that Burp Suite can be used for this lab, but I chose to perform all testing manually for clarity.


Upon launching the lab, a basic online store is displayed. Each product has an image associated with it.

## 🔎 Identifying the Vulnerable Parameter

Using the browser’s developer tools, I inspected the page and found the following HTML snippet responsible for loading product images:


\<img src=”/image?filename=21.jpg”>


This confirms that the application loads image files via the \`filename\` parameter passed in the URL. If the application does not sanitize this input properly, it could be exploited using path traversal.


By replacing the image name with directory traversal sequences (e.g., \`../\`), it may be possible to access sensitive files located outside the allowed directory.

## 🚨 Vulnerability Test

To verify the vulnerability, I modified the \`filename\` parameter as follows:


/image?filename=../../etc/passwd


After sending the request, the server attempted to display the contents of \`/etc/passwd\` as an image. Since it’s a plain text file, the browser displayed an error:


“The image … cannot be displayed because it contains errors.”


This response strongly indicates that the server successfully read the file but could not render it. Therefore, the vulnerability is confirmed.

## ✅ Lab Completion

Upon retrieving the contents of \`/etc/passwd\`, the lab was successfully completed:


“Congratulations, you solved the lab!”

# 🐞 Bug Bounty-Style Report (For Educational Purposes)

## 🧾 Title

**Path Traversal in Image Loader — Arbitrary File Read**

## 📄 Summary

A Path Traversal vulnerability was discovered in the image loader endpoint (`/image?filename=...`).

This flaw allows an attacker to read arbitrary files from the server’s file system by manipulating the `filename` parameter.

## 🔍 Affected Endpoint

`GET /image?filename=`

## ⚠️ Vulnerable Parameter

`filename`

## 🧪 Steps to Reproduce

1. Visit a product page and inspect the image element.
2. Modify the `filename` value in the URL to a traversal payload:

/image?filename=../../etc/passwd

3\. The browser attempts to render the file as an image and fails.

Error message:

*“The image … cannot be displayed because it contains errors.”*

## 🛡 Impact

An attacker can read sensitive files from the server, such as `/etc/passwd`, potentially leading to further exploitation or information disclosure.

## ✅ Recommendation

- Validate and sanitize all user input.
- Use allowlists for permitted file names.
- Ensure the file paths are resolved securely on the server side before access.
