# How to Find Escalating HTML to SSRF. I instantly got the Hall of Fame within 5minutes.

- **Source URL:** https://medium.com/@whitehatcyber404/how-to-find-escalating-html-to-ssrf-i-instantly-got-the-hof-within-5minutes-805f173c34e4?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20221217220546/https://medium.com/@whitehatcyber404/how-to-find-escalating-html-to-ssrf-i-instantly-got-the-hof-within-5minutes-805f173c34e4
- **Fetched:** 2026-11-19
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/685 (id 685)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# How to Find Escalating HTML to SSRF. I instantly got the Hall of Fame within 5minutes.

Hello Awesome Hackers, I hope you all doing well!


Today I’m sharing a vulnerability that I found a while ago, which I believe is quite interesting.

*Server Side Request Forgery through Html Injection:*

There are many endpoints, functionalities and different ways to look at an SSRF vulnerability but today I will talk about only looking for SSRF through HTML Injection and more specifically HTML Injections in Contact form Functionalities.

# **Testing If SSRF attack could be possible here:**

Usually have to fill in some parameters or sometimes some parameters like your name, message etc are reflected in the target website. 

You have to inject a simple HTML code like \<b>TESTING\</b> into these inputs and see whether the server is rendering it as an HTML or not.

If the code is getting rendered then you have move to the next step and now try to inject payload.

`<img src="http://<YOUR IP:PORT">`
So now to test the endpoint further, you have to open your Burp Collaborator or you can also use your own server if you have one. Burp Collaborator is a network tool that is a part of professional version of Burp Suite, and this tool can be used to monitor the request that are made from any host or server.

## **Let’s talk about how I find this scenario, carfully listening :**

*Steps to Reproduce:*

**1-** Navigate [https://www.target.com/contact](https://www.target.com/contact)

**2-** Then fill out the form and added with payload

\<img src=”http://\<YOUR IP:PORT”>


**3-** check Email inbox HTML tag will be executed.

**4-** You can see that. Netcat terminal triggered a victim Ip exposed

Finally ! You can trace the victim’s IP address by emailling the victim with target website.

For better understanding, I have attached videos.

**POC :** https://youtu.be/lfOx7YKo7RY

Thanks ! I hope you enjoyed reading :)

Happy Hacking 🥂🥂
