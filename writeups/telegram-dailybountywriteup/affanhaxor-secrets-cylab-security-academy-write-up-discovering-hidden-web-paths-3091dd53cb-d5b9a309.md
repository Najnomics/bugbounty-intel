# Secrets

- **Source URL:** https://medium.com/@affanhaxor/secrets-cylab-security-academy-write-up-discovering-hidden-web-paths-3091dd53cbcb
- **Fetched from:** https://medium.com/@affanhaxor/secrets-cylab-security-academy-write-up-discovering-hidden-web-paths-3091dd53cbcb?source=rss-a70f2c751bb6------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14962 (id 14962)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** Affanhaxor / Wed, 28 Oct 2026 05:18:14 GMT

**Author:** Affanhaxor

**Platform:** CyLab Security Academy

**Category:** Web Exploitation

**Challenge:** Secrets

**Topic:** Directory Discovery, Source Code Inspection, and Hidden Content

The **Secrets** challenge on CyLab Security Academy is a practical example of how hidden web directories and publicly accessible resources can reveal information that is not immediately visible on a website.

At first, the website looks like a simple page with a navigation bar and a security-related image. However, by inspecting the page source, reviewing the loaded resources, and following clues in the website structure, we can discover hidden paths that eventually lead to the flag.

In this write-up, I will explain the steps I followed, the observations that helped me move forward, and the security lessons we can learn from this challenge.

I started by opening the challenge website. The homepage displayed a navigation bar with Home, About, and Contact links, along with the message:

*“If security wasn’t your job, would you do it as a hobby?”*

The page also contained a security-related word-cloud image. Since the homepage did not display the flag, I decided to inspect the website’s resources using the browser’s Developer Tools.

The first important step was opening the **Sources** tab in Developer Tools. This showed files associated with the website, including index.css and an image named DX1KYM.jpg. The resource tree also revealed a directory named secret/assets.

This was a useful clue because developers sometimes leave interesting paths or resources accessible through the website, even when they are not linked directly from the homepage.

After discovering the secret/assets path, I opened it in the browser to see whether the directory contents were accessible.

The server returned:

A 403 response means the server understood the request but refused to allow access to the requested resource. It does not necessarily mean that the directory is empty or that every resource within it is inaccessible.

In this challenge, the directory listing was blocked. Instead of stopping there, I used the path structure as a clue and examined the parent directory.

I navigated to /secret/ and found a different page.

The /secret/ page displayed the message:

*“Finally. You almost found me. you are doing well”*

An image appeared below the message, but the flag was not immediately visible.

At this stage, the message suggested that I was following the correct path. I returned to the browser’s Developer Tools and inspected the files associated with this page.

The Sources panel showed another directory structure containing a stylesheet named file.css under the hidden path.

This demonstrated why it is useful to inspect loaded resources rather than relying only on the visible content of a webpage. HTML, CSS, JavaScript, and other resource references can provide clues about how a site is organized.

The next clue came from the directory structure visible in Developer Tools. I followed the discovered path to:

/secret/hidden/

This opened a page titled **“Login with Social Media or Manually.”** It included a Facebook login option and a section for manual sign-in.

Although the page looked like a login interface, I did not need to submit credentials to continue investigating the challenge. Instead, I inspected the resources associated with the page.

The Sources panel revealed another directory named superhidden, along with a stylesheet called login.css.

This was the next important clue. The directory name suggested that the challenge contained another level of hidden content.

The lesson here is that a page’s visible functionality may not be the only source of useful information. Its resource paths can also reveal the structure of the application.

Using the directory structure discovered during inspection, I navigated to:

/secret/hidden/superhidden/

The page displayed another message:

*“Finally. You found me. But can you see me”*

This message indicated that I had reached the intended location, but I still needed to inspect the page to locate the flag.

I opened the page’s source through Developer Tools. The source showed a simple HTML structure containing a heading and another element with the CSS class flag.

The important discovery was that the flag was present directly in the page’s HTML source. It was not necessary to find a complex authentication bypass or exploit a server-side vulnerability to retrieve it.

After inspecting the HTML, I found the flag inside the element marked with the flag class.

**Flag:**

academy{succ3ss\_@h3n1c@10n\_7d8bae24}

The flag was available in the source code even though it was not obvious from the initial homepage.

This completed the challenge.

The challenge demonstrates several important web security concepts.

Web applications often contain directories that are not linked from the main page. These paths may be discovered through source inspection, resource references, application behavior, or authorized content discovery.

In this challenge, following the directory structure led from the homepage to /secret/, then to /secret/hidden/, and finally to /secret/hidden/superhidden/.

Developer Tools help testers inspect a website’s HTML, CSS, JavaScript, network requests, and loaded resources.

The Sources panel was particularly useful here because it exposed the resource tree and provided clues about the hidden directories.

A 403 Forbidden response indicates that access to the requested resource is denied. It does not automatically mean that all related paths are protected.

In this challenge, the directory listing was forbidden, but other pages under the broader path could still be accessed.

The final flag was embedded in the page’s HTML. If sensitive information is included in content delivered to a browser, users can generally inspect it through Developer Tools or the page source.

**Important security principle:** Hiding content with CSS, placing it in an HTML element, or using an obscure URL does not provide reliable access control.

This challenge highlights several defensive practices for web developers:

The **Secrets** challenge was a useful exercise in web reconnaissance and source code inspection. Starting from a simple homepage, I examined the loaded resources, followed clues in the directory structure, explored the hidden pages, and inspected the final HTML to retrieve the flag.

The main takeaway is that a website’s visible interface does not always show everything that is delivered to the browser. Reviewing source code and resource paths can uncover important information that would otherwise be overlooked.

From a defensive perspective, sensitive content should be protected through proper server-side authorization rather than hidden URLs or client-side presentation techniques.

This challenge reinforced the value of methodical investigation, careful observation, and understanding how web applications expose their resources.

**Thanks for reading!**

**LinkedIn:** [https://www.linkedin.com/in/affanhaxor](https://www.linkedin.com/in/affanhaxor)

**Instagram:** [https://instagram.com/affan\_haxor](https://instagram.com/affan_haxor)

*Follow me for more CTF write-ups, web security labs, and AppSec content.*
