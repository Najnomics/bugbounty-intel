# Search Source ~ CyLab Security Academy Write-up | Finding Hidden Information in Website Files

- **Source URL:** https://medium.com/@affanhaxor/search-source-cylab-security-academy-write-up-finding-hidden-information-in-website-files-060b51bbeebb
- **Fetched from:** https://medium.com/@affanhaxor/search-source-cylab-security-academy-write-up-finding-hidden-information-in-website-files-060b51bbeebb?source=rss-a70f2c751bb6------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14963 (id 14963)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** Affanhaxor / Thu, 29 Oct 2026 05:06:29 GMT

**Author:** Affanhaxor

**Platform:** CyLab Security Academy

**Category:** Web Exploitation

**Challenge:** Search Source

**Topic:** Website Mirroring, Source Code Analysis, and Information Disclosure

The **Search Source** challenge on CyLab Security Academy demonstrates how important it is to inspect a website’s source files during a web security assessment.

At first, the website looks like a regular yoga and fitness website named *Flexed*. It contains a navigation bar, contact information, and a large background image. Nothing on the homepage immediately reveals the flag.

The challenge provides a useful hint:

*“How could you mirror the website on your local machine so you could use more powerful tools for searching?”*

This hint suggests downloading a local copy of the website and searching through its files instead of manually inspecting every page in the browser.

In this write-up, I will explain how I used wget to download the website and grep to search its files for the hidden flag.

I started by opening the challenge website in the browser. The homepage displayed the Flexed branding, contact details, navigation links, and the heading “Gather New Body Energy.”

The website did not display the flag in its visible content. Since the challenge was called *Search Source*, I suspected that the required information might be hidden in one of the website’s HTML, CSS, or JavaScript files.

Instead of checking every file manually, I decided to download the website locally and search through the downloaded content.

The challenge hint specifically suggested mirroring the website. On my Kali Linux system, I used wget to download the homepage.

The command was:

Here is what the command does:

After running the command, Wget downloaded the homepage and saved it locally as part of a directory structure based on the website’s hostname and port.

**Note:** Recursive downloading does not guarantee a complete copy of an entire website. Some resources may be missed because of authentication, JavaScript-generated requests, access restrictions, or other crawling limitations. For this challenge, the downloaded files provided enough information to continue.

Once the website files were downloaded, I moved into the directory created by Wget.

I then used the following command:

This command searches recursively through files in the current directory for the text academy.

Let’s break it down:

The search returned a match inside a CSS file. The output contained the flag within a comment in css/style.css.

This was the key discovery: the information was not displayed on the homepage, but it was still present in the website’s downloaded source files.

The search result showed a matching line in the stylesheet:

/\*\* banner\_main

academy{1nsp3ti0n\_0f\_w3bpag3s\_0194e1e4} \*\*/

The flag was included in a CSS comment. CSS comments are ignored by the browser’s rendering engine, so the text did not appear as part of the visible page.

However, comments are still part of the source file. Anyone who can retrieve that file can inspect its contents.

This explains why the flag was not immediately visible in the browser but could be found through a recursive text search.

After reviewing the matching line returned by grep, I identified the challenge flag.

**Flag:**

academy{1nsp3ti0n\_0f\_w3bpag3s\_0194e1e4}

This completed the Search Source challenge.

This challenge provides several lessons for developers and security testers:

The **Search Source** challenge was a straightforward but valuable exercise in website reconnaissance and source code analysis.

The homepage did not reveal the flag directly, so I followed the challenge hint and downloaded the website using Wget. I then searched the downloaded files recursively with grep and discovered the flag inside a CSS comment.

The key takeaway is simple: information that is hidden from the webpage’s visual interface may still be exposed in its source files.

For security professionals, tools such as Wget and grep are useful additions to the reconnaissance workflow. For developers, this challenge reinforces the importance of keeping sensitive information out of publicly accessible resources.

**Thanks for reading!**

**LinkedIn:** [https://www.linkedin.com/in/affanhaxor](https://www.linkedin.com/in/affanhaxor)

**Instagram:** [https://instagram.com/affan\_haxor](https://instagram.com/affan_haxor)

*Follow me for more CTF write-ups, web security labs, and AppSec content.*
