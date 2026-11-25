# Two Parsers, One Input, Two Different Answers

- **Source URL:** https://kd-200.medium.com/two-parsers-one-input-two-different-answers-0a964c2ae226
- **Fetched from:** https://kd-200.medium.com/two-parsers-one-input-two-different-answers-0a964c2ae226?source=rss-353eb5c447fb------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14968 (id 14968)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** Nitin yadav / Tue, 03 Nov 2026 07:14:14 GMT

Hello, I am Nitin.

If I had to name the one idea that changed how I think about web bugs, it would be this: most serious bugs are not in one system. They are in the gap between two.

A URL gets checked by one library and fetched by another. A request gets read by the CDN and then read again by the backend. An XML document gets verified by one parser and used by a different one. Each component, on its own, is doing its job correctly. The vulnerability is that they do not agree on what they are looking at.

This class of bug has a name: parser differential. Once you start looking for it, you see it everywhere, and it is the thread that runs through the whole first part of this batch.

Every piece of software that reads structured input has to make decisions. Where does the hostname end? Is a backslash a path separator or just a character? If a header appears twice, which one wins? If a JSON key is duplicated, does the parser keep the first value or the last?

Specifications try to answer these questions, but they are long, old and sometimes contradictory. So every implementation answers some of them slightly differently. Most of the time nobody notices, because most input is boring.

The bug appears when a security decision is made by one parser and the action is performed by another. The validator says “this is safe” about the input it saw. The consumer does something dangerous with the input it saw. They were never looking at the same thing.

Orange Tsai’s talk at Black Hat USA 2017, A New Era of SSRF, is still the best introduction to this. He showed that URL parsers across languages and libraries disagree about inputs that look trivially simple.

Picture an application that only allows webhooks to its own domain. It parses the URL, checks the host, and then hands the original string to an HTTP client. Now give it inputs like these:

\<https://allowed.example@evil.test/>

\<https://evil.test#@allowed.example/>

\<https://evil.test\@allowed.example/>

\<https://allowed.example.evil.test/>

The first one is old news. Everything before the @ is user information, so the real host is evil.test. Most validators handle it now.

The second and third are where it gets interesting. A careless validator that grabs whatever comes after the last @ sees allowed.example in both, while a proper HTTP client stops at the # and connects to evil.test. The backslash case splits even good parsers. Browsers, following the WHATWG URL standard, treat a backslash as a slash in http and https URLs, so the host ends at evil.test. Many other parsers treat the backslash as an ordinary character, which means the @ after it still marks the end of the user information and the host becomes allowed.example. If your validator and your fetcher fall on opposite sides of that line, the check passes and the request goes somewhere else.

This matters for open redirects too. There, the consumer is the victim’s browser, and the browser always follows WHATWG rules, whatever the server-side validator thinks.

The fourth input is not a differential at all, just a lazy check that uses “contains” or “starts with”. I include it because it is still the most common mistake I see.

Once you have the idea, it shows up in every layer:

The method is less about payloads and more about drawing the architecture.

**Find where input crosses a boundary.** Any feature where your input is validated in one place and used in another is a candidate: webhooks, link previews, import from URL, redirects after login, file paths, SSO responses, anything that goes through a gateway.

**Work out which components touch it.** Response headers tell you a lot: Server, Via, X-Cache and framework-specific headers. Error pages tell you more. A default 404 page or a stack trace from a specific framework tells you what is parsing your input at that layer.

**Send inputs that sit on known ambiguous edges.** Not random fuzzing. Specific inputs where implementations are known to disagree: backslashes, duplicate parameters, duplicate JSON keys, encoded slashes, mixed case, Unicode lookalikes, extra @ signs, whitespace in odd places.

**Watch for a different outcome, not an error.** The signal you want is not a 500. It is the validator accepting something that the next component treats differently. If the allow-list check passes and the request lands on your collaborator domain, that is the bug.

A quick one for parameters: send the same parameter twice, ?id=1&id=2, and see which value the application uses. Frameworks differ. Some take the first, some take the last, some join them with a comma. If a WAF or gateway checks one value and the application uses the other, you have a bypass.

Parser differential bugs tend to be high impact, because they usually defeat a control someone built on purpose. The company thought about SSRF and wrote an allow-list. The company thought about authorisation and put it in the gateway. You are not pointing out something they forgot. You are showing them that the thing they built does not work.

That also makes the report easier to write. Show the validator’s decision, show the consumer’s behaviour, and show that they disagree. Developers understand this instantly, because both pieces of code look correct on their own.
