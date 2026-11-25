# DOM XSS in jQuery

- **Source URL:** https://medium.com/@codingbolt.in/dom-xss-in-jquery-the-danger-of-href-attribute-with-location-search-source-b2d883cbec59?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20240927170326/https://medium.com/@codingbolt.in/dom-xss-in-jquery-the-danger-of-href-attribute-with-location-search-source-b2d883cbec59?source=rss------bug_bounty-5
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/7335 (id 7335)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# DOM XSS in jQuery: The Danger of \`href\` Attribute with \`location.search\` Source

When it comes to web security vulnerabilities, Cross-Site Scripting (XSS) is among the most notorious. While traditional XSS attacks target server-side code, DOM-based XSS occurs entirely on the client side, relying on how the browser handles and modifies the Document Object Model (DOM). One specific DOM-based XSS attack vector revolves around how jQuery interacts with DOM elements, particularly the \`href\` attribute of an anchor (\`\<a>\`) tag, using unsanitized user input from \`location.search\`.

Let’s break down the mechanics behind this vulnerability and explore how an innocent-looking jQuery assignment can open up doors to attackers.

**The Vulnerability: jQuery, \`href\`, and \`location.search\`**

**The Source: \`location.search\`**

In this scenario, the source is \`location.search\`, which refers to the query string of a URL — everything that comes after the \`?\`. This query string can be manipulated by attackers to insert malicious content. Since \`location.search\` is often under user control, it can be a potent source for injecting dangerous data into web applications if not handled properly.

The Sink: jQuery’s \`href\` Attribute
