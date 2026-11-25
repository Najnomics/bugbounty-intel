# http only sessions no problem ato still lurks via xss d415dec701d0

- **Source URL:** https://kokomagedd.medium.com/http-only-sessions-no-problem-ato-still-lurks-via-xss-d415dec701d0?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20240224184749/https://kokomagedd.medium.com/http-only-sessions-no-problem-ato-still-lurks-via-xss-d415dec701d0?source=rss------bug_bounty-5
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/5360 (id 5360)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# HTTP-Only Sessions: No Problem? ATO Still Lurks via XSS!

Hello, I’m Kyrillos Maged, a cybersecurity student. I’m currently focused on learning and expanding my knowledge in security, but I also engage in bug hunting from time to time

today I want to share a finding with 2 tricks that got me p2, I hope you find them useful.

Note: this Bug is now resolved

Lets reefer to the site as “example.com”, one of the site functions is the site allows you to create collections for your assets (notes,images,…) and sharing them with anyone through a link.

# Steps

1. I created a collection and tried to inject it with XSS stuff, but it was HTML encoded or filtered
2. there are a lot of things to inject more than XSS, so I tried SSTI payloads

3\. as you see, my payload is evaluated. I thought that I got a SSTI, but quickly I realized that it’s Client side template injection (CSTI)

4\. Here’s Tip 1: There are numerous ways to inject JavaScript aside from HTML tags. For example, uploaded files like SVG can also be utilized. Additionally, in our scenario, since the site is using Angular, Client-Side Template Injection (CSTI) is a potential vulnerability as well.

5\. Now we have stored XSS, but we need an impact right ? The best result from XSS is to get another users’ sessions, but the session cookie had HTTP only flag site

6\. Here’s Tip 2: I always check for ‘Remember Me’ cookies if they had HTTP-only flag set when I am testing.

*Did you know that when you log in to a website, you often see a ‘Remember Me’ checkbox? The ‘Remember Me’ token functions exactly like a session token but has a longer expiration time. Sometimes, developers prioritize securing session cookies and overlook the importance of securing ‘Remember Me’ cookies, even though they are equally significant. So if we got ‘Remember Me’ cookie we got Account take over*

7\. here’s the payload that I used to access the ‘Remember Me’ cookie

`{{$on.constructor('alert(document.cookie)')()}}`
8\. now we can share the collection with a trusted URL given by the site to anyone and steal his cookies. In addition to that, any friend of us in site can see the collection name which contains the injection. If the collection was set to public

I hope you found this article useful !

You can follow me in:
