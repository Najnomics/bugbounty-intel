# Server-Side Template Injection in an Unknown Language with a Documented Exploit — SSTI…

- **Source URL:** https://medium.com/@rcxsecurity/server-side-template-injection-in-an-unknown-language-with-a-documented-exploit-ssti-de01a069b946?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20241112050741/https://medium.com/@rcxsecurity/server-side-template-injection-in-an-unknown-language-with-a-documented-exploit-ssti-de01a069b946
- **Fetched:** 2026-11-21
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/7837 (id 7837)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Server-Side Template Injection in an Unknown Language with a Documented Exploit — SSTI Vulnerability

Welcome back for another Pentesting Methodology Lab Walkthrough at the Cybersec Cafe. Today, I’ll be approaching an SSTI vulnerability and detailing my methodology. These writeups are from controlled environment to explain my methodology in order to help you learn how to test applications yourself.

# Objective

identify the template engine being used and execute arbitrary code to delete *morale.txt* from the user Carlos’s home directory

# What We Know

The lab is vulnerable to a doucmented SSTI exploit online for this templating engine.

# What is a Server-Side Template Injection Vulnerability?

Server-Side Template Injection (SSTI) is a vulnerability that occurs when an application improperly handles user input in templates used for server-side rendering. This flaw allows attackers to inject malicious code into the template, leading to remote code execution or unauthorized access to sensitive data on the server.

If you want to be the first to see these articles, consider **subscribing** to the [Cybersec Cafe](https://www.cyberseccafe.com/) on Substack for *free*. I post content there first, and here second.

My goal is to deliver you value in various cybersecurity topics and to become your ultimate destination for expanding your expertise or for any aspiring cybersecurity professionals to break into the field.

# Methodology

Want to give the lab a try yourself and follow along? You can check it out on PortSwigger’s website [here](https://portswigger.net/web-security/server-side-template-injection/exploiting/lab-server-side-template-injection-in-an-unknown-language-with-a-documented-exploit) for free.

# The Recon

Upon opening the application, we can see the typical shop that we have in a majority of labs we attack.

Let’s click around to see if we can find anything glaringly obvious or different.Clicking the first product returns an error message, whereas the second product opens up a product page.

The difference in behavior immediately makes me think that we found our attack vector.

We can open up the Site map in Burp and find that the message is displayed using a *message* parameter under the root request.

Let’s send this over to the Repeater and start testing with it.

# Testing

Since we already know this is a template injection vulnerability, we can inject a testing string into the parameter.

`${{<%[%'"}}%\`

This will test commonly used syntax in different template languages.

We can inject this into our parameter with the hope it returns a detailed error message.

Exactly what we were expecting.

Looking at the message, we can see this has returned an error message showing us this application is using Handlbars.

Time for some OSINT.

Let’s look up SSTI in HackTricks — my go-to first stop when looking for information on vulnerabilities.

If you navigate to the SSTI page, *Command+F* to search for [Handlebars](https://book.hacktricks.xyz/pentesting-web/ssti-server-side-template-injection) and we can see a payload.

Let’s grab it and throw it in our IDE.

# Exploitation

We can see that the exploit contains two payloads: the raw payload and a URL encoded version.

Lets use the raw payload to determine where we can make our changes, then make them in the URL encoded version since we’ll have to pass it through a GET request parameter.

We can see that there is a whomai command being executed.

This is where we’ll want to inject our command.

Considering the objective or deleting the morale.txt file in carlos’ home directory, we can assume that the payload will be: *rm /home/carlos/morale.txt*

Let’s use *Command+F* in our IDE to find where *whoami* is in the URL encoded version and swap out our command.

Make sure to URL encode the space: *rm%20/home/carlos/morale.txt*

Here is the payload:

Let’s input this into the message parameter in our Repeater and click Send.

Bingo — lab solved!

# What We’ve Learned

OSINT is a powerful tool. There are many cases where you can find documented exploits for vulnerabilities with a quick search. At the very least, you can read documentation and get information on the technology being used, possibly pointing to holes.

—

Remember: The Cybersec Café gets articles first. Subscribe for free [here](https://www.cyberseccafe.com/).

Interested in getting into Cybersecurity? I have a course called the [Security Sip](https://securitysip.cyberseccafe.com/). The curriculum is designed to help you build skills progressively over 12 sections, 85 modules, and 155 exercises. With rapidly evolving threats and technologies widening the skill gap, it’s time to secure your future in cybersecurity. **Available Now!**

Oh, and if you want even more content and updates, hop over to Ryan G. Cox on [Twitter/X](https://twitter.com/ryangcox_). Can’t wait to keep sharing and learning together!
