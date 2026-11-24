# How I was Able To Find Reflected XSS ?

- **Source URL:** https://medium.com/@ozomarzu/how-i-was-able-to-find-reflected-xss-f25fe1ea3134?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20230502041547/https://medium.com/@ozomarzu/how-i-was-able-to-find-reflected-xss-f25fe1ea3134
- **Fetched:** 2026-11-24
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/2507 (id 2507)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# How I was Able To Find Reflected XSS ?

# **Scope:**

First of all the scope it was small Just a Login Page

**1 — So The first thing that came to my mind** Directory **Brute Force**

\- Unfortunately, I didn’t get anything

2- I Tried For , SQLI , user enumeration , Brute force protection , Default Credentials , etc . 

- But also, unfortunately, I didn’t get anything


# As usual, I said Maybe that there are no vulnerability here let me move on

But I said let me check parameter’s So I start for Parameter enumeration

So I found a Parameter Call \[ ?Locale \] ,


What Is XSS ? [https://portswigger.net/web-security/cross-site-scripting](https://portswigger.net/web-security/cross-site-scripting)

So I Start Testing For XSS and Then I put a Normal Payload \[ “>Test \] To see if it is reflected on the Source Code , But unfortunately I Faced this When I Try Open The Source Code


After attempts I found when I Put \[ \</script > In The Parameter There is code reflected on the page Like This >


Then I said sure there is an interaction with the code, let me put a payload \[ \</script> \<script>alert(“omar”)\</script> \]


# Finally I succeeded !!

But I said 100 percent that I will take a duplicate ):

I was surprised when the report was answered. It is not duplicate !

## Takeaways :

1- Don’t Give up

2- take a brake And come back with stronger ideas

**3- Even if the scope is small, try Testing !**

Welcome To Twitter : [https://twitter.com/Omarzzu](https://twitter.com/Omarzzu)
