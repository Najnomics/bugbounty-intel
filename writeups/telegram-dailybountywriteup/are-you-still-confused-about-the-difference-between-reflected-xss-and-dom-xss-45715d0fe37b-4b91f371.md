# Are you still confused about the difference between Reflected XSS and DOM XSS?

- **Source URL:** https://gentilsecurity.medium.com/are-you-still-confused-about-the-difference-between-reflected-xss-and-dom-xss-45715d0fe37b?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250815221319/https://gentilsecurity.medium.com/are-you-still-confused-about-the-difference-between-reflected-xss-and-dom-xss-45715d0fe37b?source=rss------bug_bounty-5
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/6289 (id 6289)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
Member-only story

# Are you still confused about the difference between Reflected XSS and DOM XSS?

Today, we will explain the most challenging type of XSS vulnerability, which is DOM-Based XSS. However, today’s explanation will make this type easier for you, just read attentively. We will explain using the Portswigger Lab to simplify the information delivery. The LAB’s title we will be working on is “DOM XSS in document.write sink using source location.search”.

If you prefer watching a video explanation on YouTube to understand the information more clearly and quickly, I recommend watching this video, which explains in detail what is being discussed here in this article.

## ***First Step:***

# We will conduct a DOM analysis

After entering the LAB, we will input any value not present on the site, for example, ‘gentil’. When we type ‘gentil’ into the search box, we will notice that it is printed twice within the DOM, once between the \<h1> tag and another time within the \<img> tag, specifically within the src.
