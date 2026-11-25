# Find Stored XSS & HTML Injections Easily

- **Source URL:** https://skynettools.medium.com/find-stored-xss-html-injections-easily-83d6903c2692?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20230124064728/https://skynettools.medium.com/find-stored-xss-html-injections-easily-83d6903c2692?source=rss------bug_bounty-5
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/1371 (id 1371)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Find Stored XSS & HTML Injections Easily

This is a short tutorial to find stored XSS & HTML Injections easily. HTML injections occur when input isn’t sanitized to check or remove code thus, allowing potentially malicious code to execute on a web page.

**1.** On a search engine such as Google, search, site:target.com inurl:”contact” | inurl:”contact-us” | inurl:”contactus” | inurl:”contcat\_us” | inurl:”contact\_form” | inurl:”contact-form” | inurl:”newsletter\_signup” | inurl:”newsletter”

Using these operators Google will display indexed results from the target domain that contains any variation of contact us or newsletter listed above in the URL. You can remove the site operator and target URL for a broader search and instead enter a keyword.

**2.** Once you’ve found the page it’s time to test payloads. Fill in the first and last name form inputs with an HTML Payload such as “Name\<a href=”HTTP://testing.com">Test\</a>".

**3.** Upon submitting a contact form or joining a website’s newsletter wait for a message in your mail. If it is executed correctly you will see the HTML changes made in the email in place of your name. Based on the example in step two, successful execution will be indicated by a clickable link “Test” in the name portion of the email.

Original Article: [https://skynettools.com/find-stored-xss-html-injections-easily/](https://web.archive.org/web/20230124064728/https://skynettools.com/find-stored-xss-html-injections-easily/)
