# Stored XSS at Nvidia via Angular JS template injection

- **Source URL:** https://xthemo.medium.com/stored-xss-at-nvidia-via-angular-js-template-injection-3c9793218860?source=rss------bug_bounty-5
- **Fetched from:** https://xthemo.medium.com/feed
- **Fetched:** 2026-11-27
- **Channel:** @dailybountywriteup
- **Telegram message:**  (id 327)
- **Method:** medium-rss-content readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
### Stored XSS in Nvidia via Angular JS template injection

**Hello security folks , I’m going talk about how I got Stored XSS in Nvidia**

### Summary :-

**Client-side template injection vulnerabilities arise when applications using a client-side template framework dynamically embed user input in web pages. When a web page is rendered, the framework will scan the page for template expressions, and execute any that it encounters. An attacker can exploit this by supplying a malicious template expression that launches a cross-site scripting (XSS) attack. As with normal cross-site scripting, the attacker-supplied code can perform a wide variety of actions, such as stealing the victim’s session token or login credentials, performing arbitrary actions on the victim’s behalf, and logging their keystrokes.**

#### **At first I create a new account and use the website as normal user , I found create post function so I tried to create a new post and see how the request was**

- **I tested normal XSS payload \<img only=1 src=x onerror=alert(1)> & \<svg/onload=confirm(1)> but there wasn’t any alert and the payloads were printed as text .**
- **Then I tried {{ 2\*10 }} , { 2\*10 } , ${2\*10} , ${{2\*10}} , #{2\*10} , \<%=2\*10%> , \<%@2\*10%> because the website uses Java and Node js languages**

- The post was published like that and the {{}} was only executed

- **The {{ 2\*10 }} was executed then I said it’s maybe get SSTI or XSS , I tested SSTI payloads like {{config.items()}} but I found an angular error in console with it’s version 1.8.3 and there was no output of the payload**
- **So I realized it can get XSS via Angular**
- **I Tried {{constructor.constructor(‘alert(1)’)()}}**

- **Then I found the payload worked and it got alert**

- document.cookie

And Finally, I got Nvidia Hall of fame.

Thanks, everyone for reading:)
