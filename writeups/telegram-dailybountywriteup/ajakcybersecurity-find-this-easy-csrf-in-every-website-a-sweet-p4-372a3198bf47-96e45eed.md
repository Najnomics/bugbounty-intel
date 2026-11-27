# Find This Easy CSRF in Every Website- A Sweet P4

- **Source URL:** https://medium.com/@Ajakcybersecurity/find-this-easy-csrf-in-every-website-a-sweet-p4-372a3198bf47?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20240604080650/https://medium.com/@Ajakcybersecurity/find-this-easy-csrf-in-every-website-a-sweet-p4-372a3198bf47
- **Fetched:** 2026-11-27
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/5942 (id 5942)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Find This Easy CSRF in Every Website- A Sweet P4🔥

Thank you for 2K Followers, keep showing love :) Hi, Ajak Amico’s welcome back to another blog. Today I will explain how I found an Easy CSRF, which gave me Hall of fame. and you can exploit this in almost every organization,So before starting, if you haven’t subscribed to our channel, do subscribe, guys.

*Follow our Youtube Channel: @ajakcybersecurity (360 Videos)*

*Follow on Instagram:AjakCybersecurity*

**Buy me Coffee: https://buymeacoffee.com/ajak**


# Recon:

As my favourite recon tool for subdomain enumeration **https://subdomainfinder.c99.nl/** and opened every URL via **bulk URL extension,** and in this scenario, I was testing this website for almost 24 hours, found an auth bypass which I will share in the next writeup, and this CSRF flaw, so this page is a community page, where users shares their query about banking and stuffs, and other users can answer, including the employees. Tried IDOR but couldn’t exploit it, it threw me a 403 error.

And for every request and every feature, there was CSRF\_TOKEN implemented, ***but at 2 endpoints,*** the API didn't have, CSRF\_TOKEN

1. **Follow/Unfollow Hashtags.**
2. **Delete Notification.**

# Exploitation:

Now I created 2 accounts to exploit this attacker and victim, I logged in via attacker and visited this URL. and my request looked like this

`https://Target.com/tags.php?tag=travel+insurance`
Once I click on the follow button, I will start to receive notifications, in my mail, whenever, another user creates a post using the travel insurance hashtag, I will receive an Email notification in my mail.

ok, now I started following, now I opened my burp site, clicked on the **unfollow** button, and captured the request.

As you can see there was no CSRF\_Token\_ Implemented. and my response looked like this

Now, I created a CSRF POC Generator, to exploit this via in the victim account.

I saved this request in .HTML format and logged in via the victim account. once I clicked on the file, it gave 200 status ok, as showed in the below screenshot and the victim was now unfollowed from the hashtags, and this was exploitable in the delete notification feature also.

# Escalation:

ok, this doesn’t look so impactful right? just a user will be unfollowed from a followed hashtag and delete a notification? maybe a user might not be so impactful, but exploiting an employee would be so impactful, as I already said earlier, both other users and employees of that organization can reply to the post. now I did a basic OSINT to escalate this, in this website we can see other users' profiles such as name and user photo and their bio just as Instagram feature. just like the screenshot below.

Now I found the community manager user profile to escalate this, as shown below.

Now I just need, to find the email address of the community manager, to do so I just hit the hunter extension, and very easily I found out the community manager's email address, which made the impact bit high.

When I wrote the report, I mentioned, that employees were exploited, since they can’t reply to the community user's query. If this CSRF is exploited, no mail will be received via email, when users mention hashtags in the post. and also mentioned, the relationship and communication between the user’s employees will be affected, by exploiting this flaw which results in reputation damage. now impact sounds like good right? Try this flaw in all organization community pages, you may end up, finding this Sweet P4, if you find out don't forget to buy me a Coffee :) Ok, that’s it, for now, will meet in the next blog.

Submitted: 15th/April/24

Accepted: 23/April/24


## PS: 50 claps for this blog, I will share How I bypassed rate limiting to account takeover in my next writeup.

— — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — —

Hope you would have learned some information from this blog if so, kindly press that follow button for further updates. Best wishes from Ajak Cybersecurity.❤️

**“கற்றவை பற்றவை🔥”**

**Learn Everyday, Happy Hacking 😁🙌**

# [https://www.buymeacoffee.com/Ajak](https://www.buymeacoffee.com/Ajak)

— — — — — — — — — — — — — — — — — — — — — — — — — — — — — —

*Follow our Youtube Channel: @ajakcybersecurity*

*Follow on Instagram: @ajakcybersecurity*
