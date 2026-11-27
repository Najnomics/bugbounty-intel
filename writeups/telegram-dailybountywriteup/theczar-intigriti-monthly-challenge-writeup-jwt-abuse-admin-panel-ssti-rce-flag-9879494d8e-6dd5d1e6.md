# Intigriti Monthly Challenge writeup JWT Abuse → Admin Panel → SSTI → RCE → Flag

- **Source URL:** https://medium.com/@TheCzar/intigriti-monthly-challenge-writeup-jwt-abuse-admin-panel-ssti-rce-flag-9879494d8e00?source=rss------bug_bounty-5
- **Fetched from:** https://medium.com/feed/@TheCzar
- **Fetched:** 2026-11-27
- **Channel:** @dailybountywriteup
- **Telegram message:**  (id 11738)
- **Method:** medium-rss-content readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
### This writeup is how I solved the November INTIGRITI challenge

[https://challenge-1125.intigriti.io](https://challenge-1125.intigriti.io)

At first the page looked like a normal shopping site , nothing seemed interesting so i signed up and was redirected to my profile (/dashboard)

I started browsing the web app like I normally do while I ‘m doing bug hunting ,capturing trafic through CAIDO ( similar to Burpsuite)

There was not much functionality so i went back to the my profile dashboard where something caught my attention

Did you get It ? it was The ROLE Assigned to me which was **user** 

Now that’s interesting ,next question is ,Where did that come from ?

Now browsing The Traffic in Caido there was nothing indicating where it was assigned ,except The JWT assigned to Me at sign-up ,so I knew we had to abuse it somehow To access something we shouldn’t access .

Next step was a directory brute-force , I prefer using Kali for That ,so I fired up the VM And started an ssh connection to it from my terminal 

Then a simple **dirsearch**(using the default wordlist ,GET requests and no headers at all ) revealed The anticipated path /admin which was redirecting us to login

Going back to the Caido traffic the only thing that was telling the app that we are a normal user is The JWT (interesting)

Now the questing that comes to mid is what are the other roles ,the one that comes to mind is admin but how can we verify that ,what I did is I went through the js files ,but there was nothing .

Next i decided to sign-up with a username of **admin** and The app seemed to refuse it ,now thats what we are looking for 

Bug hunter insticts kicked in so i tried some payloads like

aDmin

admin%00

ádmín

…

But Nothing worked ,now I knew for sure that the Horizontal privilage escalation to admin was to be done through some JWT abuse somehow

First thing I noticed was The HS256 alg ,interesting ,Time for a secret brute-force using hashcat ,so I copied The jwt to a file called jwt.txt then ran hashcat .

hashcat -m 16500 -a 0 jwt.txt SecLists-master/Passwords/Leaked-Databases/\*

Couldn’t crack it At all ,so next step in testing the JWT was Algorithm downgrade to ‘none’

Caido makes this task easy (same with burp tbh using the JWT editor) Using JWT analyzer plugin ,so we select the **‘none’ algorithm** attack as shown bellow and we make sure to change both the username/role to “admin” and to be safe from the token expiring we extend **exp** time as well

we copy and paste the New JWT in the token value using the developper tools

Now guess what ,we get access to new functionality as well as admin panel

Poking around the admin features there was nothing interesting ,as almost all buttons were disabled (lol) which made me go to My profile section in /admin/profile that had display name change ,lets poke around there too

next step was to test some **htmli** and **xss** ,which they seemed to work just fine as there was no sanitization at all ,but since the challenge clearly stated that no user interaction was required to solve it I knew XSS was a dead end .

Time to change the plan ,Whenever we find xss It is always advised to test **SSTI** (server site template injection) which turned out to be our lead to **RCE**

**Payload :**

`{{7*'7'}}`
Did you see that ,the template rendered our payload successfuly which confirmed SSTI .What’s next is playbook rules 

Visiting the Treasure trove of hackers At 

[https://book.hacktricks.wiki/en/pentesting-web/ssti-server-side-template-injection/index.html](https://book.hacktricks.wiki/en/pentesting-web/ssti-server-side-template-injection/index.html)

Poking around and using different payloads , I finally understood it was probably using [Jinja2 (Python)](https://book.hacktricks.wiki/en/pentesting-web/ssti-server-side-template-injection/index.html#jinja2-python) for rendering .

next was testing RCE using one of HackTricks payloads ,and Boom RCE ,No questions asked

`{{ self._TemplateReference__context.cycler.__init__.__globals__.os.popen('id').read() }}`
Welp that was pretty easy .now all we had to do is discover The hidden flag .Linux commands come into play now ,since CTFs (intigriti) usually store the flag at .txt files my next step was to find and “cat” all the .txt files

`{{ self._TemplateReference__context.cycler.__init__.__globals__.os.popen('find . -type f -name "*.txt" -exec cat {} \;').read() }}`
And we successfully retrieve our flag ! Nice .

I was curious what the name of the file was ,since we have the flag and it starts with ‘ INTIGRITI{ ’ my next command was

`{{ self._TemplateReference__context.cycler.__init__.__globals__.os.popen("grep -Ril 'INTIGRITI{' .").read() }}`
Explanation

- grep -R → recursive
- -i → case‑insensitive
- -l → print **only file names**, not contents

Well thats all I have got For you now , hope you enjoyed reading this as much as I did making it !

### Final Thoughts

This challenge is a perfect example of how vulnerabilities stack and why we should always try to escalate low/medium severity bugs into more serious one as often as possible.

1. **JWT “none” algorithm** → instant role escalation
2. **Admin access** → feature exposure
3. **Stored XSS** → distraction
4. **SSTI in Jinja2** → breakout to Python
5. **OS command execution** → full system compromise
6. **Recursive file search** → flag extraction

When one bug doesn’t look impactful, chain it.

When the UI looks boring, dig deeper.

And when the backend trusts unsigned JWTs… well, the challenge is already over.

### Resources :

[https://book.hacktricks.wiki/en/index.html](https://book.hacktricks.wiki/en/index.html)

[https://www.intigriti.com/researchers/blog/hacking-tools/exploiting-jwt-vulnerabilities](https://www.intigriti.com/researchers/blog/hacking-tools/exploiting-jwt-vulnerabilities)

[https://portswigger.net/web-security/server-side-template-injection](https://portswigger.net/web-security/server-side-template-injection)
