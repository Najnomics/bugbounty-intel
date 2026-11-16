# Stored XSS via File upload(using .svg file Extension )

- **Source URL:** https://ch4ndan.medium.com/stored-xss-via-file-upload-using-svg-file-extension-515e23536d4d?source=rss------bug_bounty-5
- **Fetched from:** https://ch4ndan.medium.com/feed
- **Fetched:** 2026-11-16
- **Channel:** @dailybountywriteup
- **Telegram message:**  (id 7247)
- **Method:** medium-rss-content readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
### How I Find Stored XSS (using .svg file Extension )

### Hello Everyone,

**I’**m very Happy For good response my all [**article**](https://ch4ndan.medium.com/how-i-got-sensitive-directory-using-shodan-10e5b91cda86) U can read

**This** is my 4rth article. in this article I will talk about how to find store xss vulnerability using .svg file extension. Let’s introduce myself I’m **C**h4ndan **d**as & I’m web penetration tester, From India | My English is not well so please don’t mind it.

### Lets start !

**I** pick hackerone target let’s call target.com then start hunting only file upload functionality. If you also want to find this bug then U need to find all upload Fn you can use this google dork for find upload Fn

1\. **site:\*.target.com intitle:”upload file” OR intitle:”file upload” OR intitle:”choose file”**

2**. site:\*.target.com ”choose file”**

I think manual this the best way for find upload functionality. and don’t forget to check **contact us** , **upload profile** , you can also check in **chat bot** Fn.

Then u find all upload Fn. simply search svg xss payloads and save .svg extension. u can use this code for check vulnerable via .svg

**\<svg version=”1.1" baseProfile=”full” xmlns=”http://www.w3.org/2000/svg"> \<polygon id=”triangle” points=”0,0 0,50 50,0" fill=”#009900" stroke=”#004400"/> \<script type=”text/javascript”> alert(“XSS by ch4ndan”); \</script> \</svg>**

save this payload like this xss.svg then upload and see success fully uploaded 90% chance xss (If don’t know .svg extension u can search on google & chat gpt )

In my case I find upload function in chat bot, then send svg file success fully execute, then I quickly make poc and report on hackerone *u can view in image*

But again Duplicate 😌

Then I choose another target & find upload Fn in contact us form simply upload svg file and success fully uploaded then I make poc & report it *u can see in image*

**Thank you everyone for Reading 🧡**

***U can view my*** [***LinkedIn Profile***](https://www.linkedin.com/in/ch4ndan-das-hacker/)

*join my* [***telegram***](https://t.me/ch4ndandas) *channel*

**H**appy **H**unting **:)**))
