# Personal Browsing Gone Wild

- **Source URL:** https://medium.com/@josekuttykunnelthazhebinu/personal-browsing-gone-wild-xss-idor-in-the-same-spot-6ab3e0ea6190?source=rss------bug_bounty-5
- **Fetched from:** https://medium.com/feed/@josekuttykunnelthazhebinu
- **Fetched:** 2026-11-17
- **Channel:** @dailybountywriteup
- **Telegram message:**  (id 12097)
- **Method:** medium-rss-content readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
It’s been a while since I wrote my last article! I hope all my fellow hunters and infosec friends are doing great.

It’s 26th december 2025 today. Even though I planned to hunt on some targets I was not in the right mood.

So I thought to write something to keep myself engaged. Also if its helping someone I will be happy.

Recently, while browsing some websites for personal reasons, my testing instincts kicked in (as always). Even when I’m not actively hunting, I can’t help but notice certain things URL patterns, redirects, and request structures.

Whether I’m booking train tickets or checking movie schedules, I have this habit of observing every detail in the browser, even without Burp Suite running!

As usual, I tried a few payloads on reflected pages, but nothing interesting popped up. Then I moved on to exploring the career section of one site. I noticed an option to upload a CV (PDF or DOC) as part of the user profile. That immediately grabbed my attention.

I decided to upload a PDF containing a basic XSS payload (more about this payload later in the article). Once uploaded, the platform provided a feature to view the uploaded resume directly from the web interface — and that’s where things got interesting.

Another tip, when testing if you don’t have an option to open the file you uploaded, try to right click on the file and try to open in a new tab, or somehow you need to find the path where the file is uploaded.

Upon clicking *“View Uploaded Resume”*, my payload successfully triggered, and the XSS pop-up appeared. At this point, I knew there was stored XSS happening through the uploaded file.

### Digging Deeper: The Curious URL

I don’t know how many of you noticed the url in the previous url image, the url was something like this:

https://www.xyz.com/xyz/media/user\_details/431879/resume.pdf

My first thought that numeric part (431879) looks like a user ID or some identifier related to stored files.

Out of curiosity (and as a common security instinct), I tried changing the ID to 431878. That returned a 404 Not Found.

To analyze it systematically, I captured the request in Burp Suite and used Intruder to fuzz the numeric value, iterating IDs between 430000 and 440000.

As expected, I saw multiple 404 responses, but then some 200 OKs appeared in the results.

On reviewing those successful responses in the browser, I was shocked to find that other users’ resumes were accessible simply by manipulating the ID.

At this point, it was clear there was an Insecure Direct Object Reference (IDOR) vulnerability.

It allowed anyone to access other users’ private files by modifying the numeric identifier in the URL.

### Impact

This kind of issue is serious. A combination of Stored XSS and IDOR means:

- Attackers could potentially upload malicious files.
- Sensitive personal documents (like resumes) could be exposed to unauthorized users.

If you guys wants to download the xss injected pdf file, go to [https://gist.github.com/GugSaas/3e12c57cf22f745d009e31266f441e07](https://gist.github.com/GugSaas/3e12c57cf22f745d009e31266f441e07) and download it…

So that's it, I hope you guys got something helpful. I find this so easy to exploit. Hopefully, it helps someone notice similar patterns during their own hunts.

I’m definitely not a big writer or anything, just another random dude poking around the internet for bugs. So until we see again, happy hunting and take care!
