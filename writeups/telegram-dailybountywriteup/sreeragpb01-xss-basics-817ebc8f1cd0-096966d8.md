# XSS Basics!

- **Source URL:** https://medium.com/@sreeragpb01/xss-basics-817ebc8f1cd0?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20251126142343/https://medium.com/@sreeragpb01/xss-basics-817ebc8f1cd0
- **Fetched:** 2026-11-24
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/1923 (id 1923)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# XSS Basics!

Hello folks, Today we are going to discus about the most common Attack vector called Cross Site Scripting aka XSS. So after spending some time here reading this blog will give you the basic understanding of XSS vulnerability, how to find these type of attack vectors on the web applications that you are testing. So cross site scripting is a client side vulnerability when an application render the user input as-is, which is inputted by the user without any validation or sanitization. And it leads application rendering potentially harmful data.

Before jump into the real fun part, we just need to understand some basic things that will expand the knowledge on this vector or topic.

**Types of XSS**

There are mainly 3 types of xss:

1. Reflected XSS.
2. Stored XSS.
3. DOM XSS.

**Reflected XSS:** Reflected XSS is a type of cross site scripting vulnerability, It happens when the malicious user input is reflected on the application. For example: Search queries

**Stored XSS:** Stored XSS happens when the malicious user input is stored and reflected on the application. For example : comment pages, review pages,etc.

**DOM XSS:** DOM XSS is another type of cross site scripting, It happens when the user input is handled by the JavaScript DOM(Document Object Model) without validation.

Basic XSS vulnerabilities are easier to find If we understand the basics. So bare with me for few minutes. And I assure you that after the end this you will have some better understanding of finding these vulnerabilities in the application.


**How to identify XSS vulnerabilities?**

1. Find the right endpoints to inject the payload.
2. Try the payloads w.r.t the context.

- First of all we need to identify the endpoints that may be vulnerable to XSS attack. In which our input gets reflected on the application.
- For example possible entry points are like search bar, comment sections, review sections and where ever the user input gets reflected.
- Once we find our endpoints with above mentioned capability. It’s time to pour those endpoints with the special characters.

**<, >, {, }, ', ", ;
<,>  --> Means closing and ending tag of html.
{, } --> used in function definition of javascript.
',"  --> used to represent the strings.
;    --> Used to represent the end of the statement.**
- Try these characters on the input Field and press submit. If you find these characters are reflected on the page with out any modification and validation or other words those characters reflected on the rendered page as-is. Then it may be vulnerable to the XSS vector.
- So after successful reflection, We need to know what is happening behind the scenes. For that we just need to see the source of the page(in firefox browser you just need to press CTRL+u to view the page source).
- If the characters are shown in same format as the output(since we assume that, we got successful reflection of characters without any change)or input with in the \<div> or any other tags.
- If our target site satisfies all above mentioned symptoms. It is the time to test the actual vector with the payload.

`<script>alert('xss');</script>`
- Now test the input fields with the mentioned payload.
- If it pops an alert window with xss mentioned in it :) whoaala…..
- We find our first xss.

You can also refer the xss cheat sheets / useful payloads from the OWASP.org, portswigger academy, github, etc..

Thank you.
