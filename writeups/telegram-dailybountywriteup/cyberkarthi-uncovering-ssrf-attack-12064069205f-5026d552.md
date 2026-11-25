# Uncovering LFI Attack ‍

- **Source URL:** https://medium.com/@cyberkarthi/uncovering-ssrf-attack-12064069205f?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20240110133314/https://medium.com/@cyberkarthi/uncovering-ssrf-attack-12064069205f?source=rss------bug_bounty-5
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/4862 (id 4862)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Uncovering LFI Attack 👨🏽💻

--

Let’s dive into how to identify and safeguard against Local File Inclusion (LFI) bugs, understand their occurrence, and effectively mitigate the risk.

What is LFI? 🚨

Local File Inclusion (LFI) is a web vulnerability that arises when a web application includes a local file based on user input. This vulnerability can lead to unauthorized access to sensitive files on the server, which poses a high security impact.

Understanding LFI 🤔

To illustrate, consider a basic index.php file:

*\<?php $page = isset($\_GET\[‘page’\]) ? $\_GET\[‘page’\] : ‘home’; include($page . ‘.php’); ?>*


In this code, the lack of proper input validation and sanitization allows user input to be directly used in file inclusion operations.

Mitigating LFI 🛡️

*\<?php $page = filter\_input(INPUT\_GET, ‘page’, FILTER\_SANITIZE\_SPECIAL\_CHARS); $allowedPages = \[‘home’, ‘about’, ‘contact’\];*

*if ($page && in\_array($page, $allowedPages)) { include($page . ‘.php’); } else { header(“Location: default.php”); exit(); } ?>*


**filter\_input:** Utilizes filter\_input to get and sanitize input. This ensures that the ‘page’ parameter is treated as a string.

**Allowed Pages:** Maintains an array of allowed pages to include. Adjust the array according to your application’s structure.

**Validation:** Checks if the requested page is in the list of allowed pages. If yes, include the page. If not, redirect to a default page or show an error message.

Key Note 🔑:

It’s crucial to keep the list of allowed pages updated and ensure user input is thoroughly validated and sanitized. This helps prevent various types of injection attacks, including LFI.

Now, we can able to resolve the LFI attack.

I hope now you will have a better understanding of how LFI occurs and how to mitigate the occurrence ✌

Keep an eye out for the upcoming writeups and join me in the quest for a more secure digital world.

Thank you for reading,

# Connect with me:

*Instagram:* [https://www.instagram.com/cyber\_karthi/](https://web.archive.org/web/20240110133314/https://www.instagram.com/cyber_karthi/)

***Linkedin*** : [https://www.linkedin.com/in/cyber-karthi/](https://web.archive.org/web/20240110133314/https://www.linkedin.com/in/cyber-karthi/)
