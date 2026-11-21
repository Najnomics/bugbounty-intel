# From “Not Reproducible” to Recognition

- **Source URL:** https://medium.com/@dikstha1409/from-not-reproducible-to-recognition-reflected-xss-on-nasa-1bc008d1d459?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250503090724/https://medium.com/@dikstha1409/from-not-reproducible-to-recognition-reflected-xss-on-nasa-1bc008d1d459
- **Fetched:** 2026-11-21
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/9254 (id 9254)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# From “Not Reproducible” to Recognition: Reflected XSS on NASA

Hello everyone, and welcome to my blog.

In this write-up, I will share how I found my first bug (Reflected XSS) on NASA, submitted the report three times, and finally got it accepted. Before diving into the details, let me give a short introduction about myself.

My name is Dikshya Shrestha, aka GakuXen. I’m a student, a cybersecurity enthusiast, and a beginner bug hunter who recently started bug hunting and is working to improve my skills.

Now, let’s first understand what a Cross-Site Scripting (XSS) vulnerability is:

Cross-site Scripting (XSS) is a type of security vulnerability that allows attackers to inject malicious client-side scripts into web pages viewed by other users. When these scripts execute in victims’ browsers, they can:

- Steal sensitive information like cookies and session tokens
- Hijack user sessions
- Deface websites
- Conduct phishing attacks

There are three main types of XSS:

**1. Reflected XSS:** The malicious script is reflected off a web server, such as in search results or error messages. It’s non-persistent and requires the victim to click a crafted URL.

**2. Stored XSS:** The malicious script is permanently stored on target servers (like in databases) and gets executed when users access the stored data. This is more dangerous as it doesn’t require user interaction.

**3. DOM-based XSS:** The vulnerability exists in client-side code rather than server-side code. The attack payload is executed as a result of modifying the DOM environment in the victim’s browser.

A little background to the story:

One night, after my usual routine, I was scrolling through LinkedIn when I saw a bug bounty hunter receiving a Letter of Recognition from NASA. That’s when I thought, “Maybe I should give it a try too.” And that’s how I started hunting for bugs in NASA’s subdomains.

First, I started with a simple task: collecting as many subdomains as possible. I kept it simple and used “subdomainfinder” to gather the subdomains. I was shocked by the results, it found around 5000 subdomains.

I didn’t do much after that. I just picked one subdomain to work on — let’s say it was subdomain.redacted.com. That night, I was simply exploring the website, understanding its features. I went through actions like creating an account, logging in, updating the account, changing the password, and so on, nothing much, just familiarizing myself with the functionalities of the website.

The next day when I was checking the Change password functionality again trying to find if I could do something on it then I noticed the URL contained a parameter:

*https://subdomain.redacted.com/path/to/change\_password?wid=6*

The parameter wid=6 caught my attention. I wondered if manipulating this parameter would give any interesting results. My first thought was to test for an Insecure Direct Object Reference (IDOR) or something related to that by changing wid=6 to wid=4. But, this only resulted in a simple page refresh with no visible changes.

Since modifying the parameter numerically did not produce any results, I decided to check for XSS. My first attempt was with a basic payload:

*wid=\<script>alert(1)\</script>*

Well the page simply refreshed without any pop-up message which indicated that some form of sanitization might be in place, but I was not ready to give up yet.

Next, I what i tried was

*wid=4"\<script>alert(“GakuXen”)\</script>*

Instead of executing or refreshing, the server just returned a **500 Internal Server Error**. Well that’s interesting, and thought maybe the input I gave was causing some problem on how the code runs.

Now, I needed to know where the `wid` parameter was being used. Using the browser's Inspect Element tool, I searched for `wid` and found that the application was using it like this:

*wid= ‘4’*

This was a something! As my input was being placed within single quotes (`'`), an unescaped single quote could potentially break the HTML structure. I read about it and then thought what if I manually closed the existing attribute and injected my payload?

As i found that the single quote (’) was causing something i decided to keep this payload instead:

*wid=4'”>\<script>alert(“GakuXen”)\</script>*

here what i did was:

- Added the single quote (’) to close the existing value prematurely
- The double quote (`"`) to make sure that any characters were correctly closed.
- The angle bracket (>) would close the HTML tag early.
- And the script tags to for XSS execution.

After i submitted that! **BOOM** the **alert GakuXen** popped up!!

But, after clicking OK it gave 500 internal server error again. Well that’s a problem.

I didn’t think of that and just submitted my first report. They replied, saying that the bug was not reproducible!

Well, ouch… I knew it was reproducible, and it was a Reflected XSS. My report wasn’t good at all, so I thought maybe that was the issue. I made some changes to the report and submitted the same bug again.

Well, this time?

They dropped the severity from P3 (Medium) to P5 (Informational), saying it was a Self-Reflected XSS and not a Non-Self Reflected XSS. I actually felt bad about it because I still knew it was clearly a Reflected XSS.

I took some time to learn more about XSS and why it was causing a 500 Internal Server Error after clicking the OK button. After a while, I figured out why it was behaving that way. So, I decided to change the payload to

*“>\<script>alert(1)\</script>--*

*so it was, wid=4“>\<script>alert(1)\</script>--*

Explanation on why this payload worked:

- No single quote (`'`), so nothing breaks.
- The `">` closes the attribute and starts the script execution.
- The `--` make sures no additional processing happens, preventing any backend syntax errors.

And finally, it worked no more 500 Internal Server Error!

While reporting the bug I kept my payload:

*wid=4“>\<script>alert(document.cookie)\</script>--*

I also learned how to write a proper report, thanks to my seniors who helped me. This time, I submitted the bug correctly. After some waiting, they put my submission in triage.

The happiness I felt at that moment was actually unreal.

And finally, the dream every bug hunter hopes to achieve while testing on NASA:

Finally, I would like to thank everyone who supported me, and a special shoutout to the greatest person in my life, my brother [Apilchand](https://medium.com/u/45e21878f587?source=post_page---user_mention--1bc008d1d459---------------------------------------), who taught me almost everything and helped me get into this field.

A short message to everyone: Stay curious, keep learning, and never lose hope. One rejection doesn’t mean you’re wrong. Just keep trying and learning until you get it right.
