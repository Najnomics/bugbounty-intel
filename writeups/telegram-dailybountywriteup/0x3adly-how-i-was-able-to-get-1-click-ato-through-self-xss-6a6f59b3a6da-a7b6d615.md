# How I Got 1-Click ATO through self-XSS

- **Source URL:** https://medium.com/@0x3adly/how-i-was-able-to-get-1-click-ato-through-self-xss-6a6f59b3a6da?source=rss------bug_bounty-5
- **Fetched from:** https://medium.com/feed/@0x3adly
- **Fetched:** 2026-11-20
- **Channel:** @dailybountywriteup
- **Telegram message:**  (id 5364)
- **Method:** medium-rss-content readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ

in the name of Allah, the most gracious, the most merciful.

This time I want to write about how I was able to escalate a self-XSS to gain a 1-click full account takeover.

Let Us Begin.

For Non-Disclosure's sake, let's call the website www.xyz.com

the website is a hotel booking platform that allows you to browse and book different hotels across cities,

so I started testing different functionalities around the website like sign-up, sign-in, forget password, and booking a hotel. but nothing was found.

so I started testing in the profile section and I noticed the update profile API doesn’t contain a CSRF token, so I created the POC and sent the request to the victim, and BOOM CSRF where I can change the victim’s profile information.

Unfortunately, this finding alone is useless as the user can just change his data back.

so I started looking for ways to escalate this finding for better impact, then one of my friends pointed out that the name parameter was vulnerable to stored self-XSS using this payload

X"> \<Svg Only=1 Onload=alert(document.cookie)>

so I can simply inject the XSS payload using the CSRF and steal the user’s cookies for a full account takeover

so I updated my CSRF payload to include the XSS in the name parameter and BOOM the XSS payload is injected into the victim’s profile

now the attacker can alter the XSS payload to send the victim’s cookies to himself and gain a full account takeover

this demonstrates how you can chain 2 simple findings to gain the most impact.

Hope you gained new information and learned something new.

Follow me on Social Media :
