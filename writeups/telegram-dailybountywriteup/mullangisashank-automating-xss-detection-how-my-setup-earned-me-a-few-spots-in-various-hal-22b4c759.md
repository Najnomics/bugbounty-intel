# Automating XSS Detection

- **Source URL:** https://medium.com/@mullangisashank/automating-xss-detection-how-my-setup-earned-me-a-few-spots-in-various-hall-of-fames-cb7f35ebed1e?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20260731213508/https://medium.com/@mullangisashank/automating-xss-detection-how-my-setup-earned-me-a-few-spots-in-various-hall-of-fames-cb7f35ebed1e
- **Fetched:** 2026-11-24
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/2642 (id 2642)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Automating XSS Detection: How My Setup Earned Me a Few Spots in various Hall of Fames

Hello there InfoSec People,

How have you been?

Today let me walk you through my XSS Automation setup which helped me score some hall of fames.

So first things first. Who am I and why should you read this article?

Hi, My name is Mani Sashank who is working as a security analyst and does bug bounty in his free time. By the end of this article you’ll have a readymade script for automating your XSS detection using few open source tools.

Now let’s move on to the XSS automation setup.

Basically there are 3 minor parts to this script:

1. Gathering the waybackurls for the domain.
2. Removing similar and duplicate URL’s.
3. Extracting the links which has parameters in the URL and check if those are vulnerable to XSS or not.

NOTE: For now through out the article let’s assume the domain as example.com

## Step 1: Gathering the waybackurls for the domain

For this we can use tools like [waybackurls](https://github.com/tomnomnom/waybackurls), [gau](https://github.com/lc/gau) for gathering old and archived URL’s of example.com .

```
waybackurls example.com > archive_links
gau example.com >> archive_links
sort -u archive_links -o archive_links
```
The above commands will gather all the old and archived URL’s of example.com and store them in the file “archive\_links”. Then we are removing the duplicate URL’s if any present using the **sort** command.

## Step 2: Removing similar and uninteresting URL’s.

For this we can use a tool called [uro](https://github.com/s0md3v/uro). Using which we can remove similar and uninteresting URL’s.

Installation of uro is pretty simple. You can install it using pip from your system.

Below is a small example of how **uro** works.

So now let’s use uro in our script:

`cat archive_links | uro | tee -a archive_links_uro`
After this we have URL’s which are worthwhile to check for XSS.

## Step 3: Extracting the links which have parameters in the URL and checking if those are vulnerable to XSS or not.

To achieve this we have multiple approaches. I personally do this by using [qsreplace](https://github.com/tomnomnom/qsreplace) and [freq](https://github.com/takshal/freq) tools.

Let me explain in detail about this as this is the juicy part you have been reading for. 😉

So after step 2 now we have the list of URL’s from where duplicate/similar/uninteresting URL’s have been deleted.

Now stay with me here as it might get a little bit confusing. 😅

The 3rd parts flow is as follows:

1. Extract the URL’s with parameters using grep.
2. Replace the parameter values with our payload using qsreplace.
3. Use freq to analyze the URL’s and find valid XSS’es.

The below is the command which does all the above 3 steps in a single line:

`cat archive_links_uro | grep "=" | qsreplace '"><img src=x onerror=alert(1)>' | freq | grep -iv "Not Vulnerable" | tee -a freq_xss_findings`
Now let’s understand the above command:

**Grep**: Using grep “=” we are extracting the URL’s which have some kind of parameters in them.

**Qsreplace**: Using qsreplace we are replacing the parameter value to the specified payload. In our case that is **“>\<img src=x onerror=alert(1)>**

Check this below example to understand the working of Qsreplace.

**Freq**: The output of qsreplace is passed on to freq. What freq does on a brief is like it CURL’s the endpoint and checks for our payload reflection in the response. And then based on freq output I am using grep to supress the invalid findings and give out only vulnerable endpoints as output to file “freq\_xss\_findings” file.

The output of “freq\_xss\_findings” file will be like below:

Now you can just copy them one by one and verify them. Mostly it would be a valid finding but there are cases where this might lead to false positive like if the payload was reflected in the JSON format or something like that. So I suggest you manually verify the finding by visiting the endpoint and then report it. 😊

So to recap what the whole script does is first it gathers the waybackurls of the domains then removes the duplicate/similar/uninterested urls and then using qsreplace and freq the valid XSS’es are found.

```
#!/bin/bash
echo "[+] Running waybackurls"
waybackurls $1 > archive_links
echo "[+] Running gau"
gau $1 >> archive_links
sort -u archive_links -o archive_links
cat archive_links | uro | tee -a archive_links_uro
echo "[+] Starting qsreplace and freq"
cat archive_links_uro | grep "=" | qsreplace '"><img src=x onerror=alert(1)>' | freq | tee -a freq_output | grep -iv "Not Vulnerable" | tee -a freq_xss_findings
echo "[+] Script Execution Ended"
```
Pass the domain as an argument for the script like **“./script.sh example.com”.** After running the above script with the domain as argument you can check the final output in the file “freq\_xss\_findings”

This setup kinda helped me get like around 20–30 Valid XSS’es including various platforms like hackerone, intigriti, bugcrowd and also some public VDPs.

You can tweak the above script according to your requirement like using the script in a **for loop** with taking domain input from a list, etc.

And then you can also use tools like [kxss](https://github.com/tomnomnom/hacks/tree/master/kxss) which tells you if some special characters like \[ “ ‘ \< >\] are being reflected in the response or not, based on which you can manually inject the payloads one by one.

References:

waybackurls: [https://github.com/tomnomnom/waybackurls](https://github.com/tomnomnom/waybackurls)

gau: [https://github.com/lc/gau](https://github.com/lc/gau)

uro: [https://github.com/s0md3v/uro](https://github.com/s0md3v/uro)

qsreplace: [https://github.com/tomnomnom/qsreplace](https://github.com/tomnomnom/qsreplace)

freq: [https://github.com/takshal/freq](https://github.com/takshal/freq)

kxss: [https://github.com/tomnomnom/hacks/tree/master/kxss](https://github.com/tomnomnom/hacks/tree/master/kxss)

modified kxss by Emoe: [https://github.com/Emoe/kxss](https://github.com/Emoe/kxss)

That’s it for this article B&G’s. Feedback to the articles is very much appreciated. You can give a clap or leave a comment here. Hey you can even send me a DM on twitter about the articles feedback or topics on which you want me to explore further. 😉

Social Media Links:

Instagram: [https://www.instagram.com/mani.sashank/](https://www.instagram.com/mani.sashank/)

Twitter: [https://twitter.com/manisashankm](https://twitter.com/manisashankm)

LinkedIn: [https://www.linkedin.com/in/manisashank/](https://www.linkedin.com/in/manisashank/)

In the next blog let’s discuss about a private program where I was able to chain xss + clickjacking + csrf = Account takeover.

Wishing you all the very best and success on your bug bounty journey. 🤞

See you in the next blog. Till then. ✌
