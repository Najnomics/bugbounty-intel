# How I found Reflected XSS in Users login page on Public Program ?

- **Source URL:** https://medium.com/@who1am1i999/how-i-found-reflected-xss-in-users-login-page-on-public-program-f2c9f6580ed7?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20230613155134/https://medium.com/@who1am1i999/how-i-found-reflected-xss-in-users-login-page-on-public-program-f2c9f6580ed7
- **Fetched:** 2026-11-19
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/2783 (id 2783)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# How I found Reflected XSS in Users login page on Public Program ?

--

here I will discuss some ideas not tools so if you only use tools and don’t have any idea about real hunting please don’t waste your time here

From 2 weeks , I noticed a new public program and No one got anything on it for 5 days I was very excited to take a look on it , After some subdomain enumeration , I got a subdomain which is for the supporting things so I thought about the Sensitive data exposure things , so I started to surf and search the page for any info or disclosure , but here I noticed something !!

How this website don’t have a Sign in page ? I think it’s important to get a sign in page for users to use it when redirect from the website to this support subdomain which make them enable to report problems and search for answers , So I started to search more and more but without any thing , I was so bored and I started to lose hope …

Hmmm…

now I don’t have except one solution , it’s Fuzzing so I started to use it and I got something : /users

so I guess it can be /users/sign\_in , I try it and It was correct

Now its time to check the page for anything , But surprise…

nothing also but their is something so weird ,,

While I surfed this page I used Burp suite to intercept the requests but the weird thing here is that the link example.com/users/sign\_in redirect me to a new page to a same login page so for sure it can get me an open redirect or Xss so why not ??

We gonna try something weird with the weirdo page , but my eyes catched something a parameter called : “ fallback\_url “

and it contains the redirected link and I tried to test if it reflect the value or not and I got it ,, so why not ?? let’s try XSS ,,

so I started to test and after that I got this payload :

”>\<sCrIpT>alert(“WHOAMI?”)\</ScRiPt>

and Booom !!

The point here is to search and search don’t lose hope or build your experince dependent on tools cause something sooo easy like this no tool can catch it , my advice today is to learn and read more write ups ..
