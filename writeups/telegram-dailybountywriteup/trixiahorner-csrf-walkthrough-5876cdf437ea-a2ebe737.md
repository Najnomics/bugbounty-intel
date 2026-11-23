# How I Manipulated A User’s Email

- **Source URL:** https://medium.com/@trixiahorner/csrf-walkthrough-5876cdf437ea?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20261014092926/https://medium.com/@trixiahorner/csrf-walkthrough-5876cdf437ea
- **Fetched:** 2026-11-23
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/7428 (id 7428)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
Member-only story

# How I Manipulated A User’s Email: A CSRF PoC From TCM Academy

🔓Not a Medium member? I want this to be accessible for everyone, so click [**here**](/@trixiahorner/csrf-walkthrough-5876cdf437ea?sk=f916bab79f712db95c508d9c6f7b3b30) to read this story for free.

This write-up is based on a **Cross-Site Request Forgery (CSRF)** bug bounty lab from **TCM Security Academy**. The goal is to explore the process of identifying and exploiting a CSRF vulnerability. In this case, the PoC will simulate an attack in which an unsuspecting user’s email address is changed through a maliciously crafted webpage.

## THE PROBLEM WITH CROSS SITE REQUESTS

Cross-site requests are used to connect multiple websites across the web. A normal cross-site request occurs when a website asks your browser to send a request (such as submitting a form or fetching data) to another site where you’re already logged in. For example, a webpage (not belonging to Medium.com) can include a link to Medium, so when a user clicks on the link, an HTTP request is sent to Medium.

A **Cross-Site Request Forgery (CSRF) Attack** tricks a user’s browser into making an unwanted request to a different site where the user is logged in (like changing a user’s email address.)
