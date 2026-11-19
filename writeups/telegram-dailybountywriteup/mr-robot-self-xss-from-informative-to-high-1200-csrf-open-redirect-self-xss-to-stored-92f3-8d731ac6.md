# Mr. Robot

- **Source URL:** https://ahmadaabdulla.medium.com/mr-robot-self-xss-from-informative-to-high-1200-csrf-open-redirect-self-xss-to-stored-92f371ba3da1?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20260517185617/https://ahmadaabdulla.medium.com/mr-robot-self-xss-from-informative-to-high-1200-csrf-open-redirect-self-xss-to-stored-92f371ba3da1
- **Fetched:** 2026-11-19
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/416 (id 416)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
**If you want to learn bug bounty in an easy and affordable way, visit our website. The course is taught in English.**

**https://www.cybershield.krd/Courses/Course/28**

### Mr. Robot: Self Xss from Informative to high 1200$ ,csrf, open redirect,self xss to stored

Hello all bug bounty hunters sorry for any mistake if I forget something to use this writeup for your RECON or you’re RESEARCHING, I found 2 w 3 bugs with the same idea

I submitted this bug to private programs but I changed everything here name website and panel and photos just to help the new bug bounty hunter it’s not the real name and photos

The first time I found csrf in the first name and last name no have a csrf token but the website not accepted csrf and self xss from the csrf i can change name to any word or payload xss but have no impact and not accepted by the website it’s too bored

after 2 or 3 hours I found a demo panel with the same information when you change the first name will change in the demo i changed to xss payload first name and the last name will be done and worked xss but the website not accepting self xss we need to change to stored xss but how?

ok now we have CSRF to change the profile name to xss and we found a demo website to reflect the xss it’s good

we need to redirect users from the normal website to the demo I found the button to create this redirection from the normal website to the demo website and the xss reflected

and I create two csrf one to change the profile name to xss and two to redirect users to the demo and injection like this

steps like this

1 goto xxx.com change profile name and capture request and create csrf

2 capture request, the button will redirect you to the demo website, and create csrf

done
