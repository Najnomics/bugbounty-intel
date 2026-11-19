# HackTheBox Saturn

- **Source URL:** https://medium.com/@leomsec/hackthebox-saturn-explaining-ssrf-072234ab5ce3?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20240219025515/https://medium.com/@leomsec/hackthebox-saturn-explaining-ssrf-072234ab5ce3
- **Fetched:** 2026-11-19
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/5085 (id 5085)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
Here I’m going to do a walkthrough of HackTheBox saturn web challenge and use it to talk a little bit about SSRF (Server-Side Request Forgery).

When we enter the page of *Saturn Proxy* we can pass a URL in a input field that loads the page, you can test it passing google’s URL, but of course our goal here is to get the *flag* not the google page.

Hack The Box let us download the files of the challenge to analyse the code, so let’s see the code and try to find a way to exploit this vulnerability.

In this piece of code above, we can see that we have a route “*secret*” where we will find the flag, but it can only be accessed by *127.0.0.1* a.k.a the *localhost*, if we go back to the challenge and pass “*http://127.0.0.1/secret*” as the URL it shows a message “*Malicious input detected*”, so we need to use some kind of bypass here, going back to the code we can see that it’s using “*SafeURL*”, so that’s what is blocking the request.

# Bypass:

One of the ways to bypass SSRF protection is using a redirection, in this case I have used a *url shortener* website to bypass it, as we see in the code, the app is running on port *1337* so we just pass “*http://127.0.0.1:1337/secret”* to the url shortener (*some url shortener might not allow it*) copy the url it gives us, and passing it to the Saturn Proxy it returns the *flag*.

# Other ways a ssrf could be bypassed:

A different way but following the *same logic* used in this challege that could be used to bypass a SSRF would be to find a “*open redirect*” on the same website and pass it with the localhost (or anything else that you want to access) and it will be redirected.

*Example: http://exploitedsite.com/?redirect=http://localhost:1337*

Something that I have tried in this challenge and sometimes can work too is using some of the different ways to access the localhost (if it’s your goal), you can find a list on “*payload all the things*” with a lot of different ways to refer to the localhost.

Depending on the verification that is applied on the website, for example, if it’s using a not well implemented regex to verify if the parameter is sending to a allowed website, we can try to exploit it like this -> “[*https://evilsite.com/exploitedsite.com*](https://evilsite.com/exploitedsite.com)” , because if the regex was not well implemented it will just check if “exploitedsite.com” is part of the parameter, and to verify it is just playing with the url and seeing when it will block the request or not, you won’t aways have access to the code so you need to kind of reverse engineer it.

# What a SSRF can be used to:

A SSRF can be used to access places that should not be accessed by someone out of the lan that the website is running on (like in the Saturn challenge that the endpoint can only be accessed throught localhost), it can also give you access to the cloud that the website is using, you might be able to have access to private data whe accessing it, so SSRF can be a very critical vulnerability.
