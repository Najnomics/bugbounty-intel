# The Story Of A Strange / Stored IDOR.

- **Source URL:** https://medium.com/@hf6452/a-story-of-a-strange-stored-idor-b6f2769bb6cb?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20221116171544/https://medium.com/@hf6452/a-story-of-a-strange-stored-idor-b6f2769bb6cb
- **Fetched:** 2026-11-24
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/832 (id 832)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# The Story Of A Strange / Stored IDOR.

## Story :

My name is Hassan Farooq (Hack3rOn3) . IAM From Pakistan. I am 18 year old bug hunter . I started bug hunting at 16 age.

(Kindly Ignore My English Mistakes as it is not my Primary language)

Now I come to the story of what I found and how. As I told, I started bug hunting at 16 but before this I was like learning new stuff (still learning) and opening random websites to test my skill.

It was a normal day actually it was the night time , I opened a bank website and started to search for something like I also don’t know 😂 . I spent 2 hours in the site testing every functionality and every parameter and at that time I found 3 vulnerabilities like (getting access to bank mail service, OTP verification Bypass and xss).

Then After This I created an digital account in the banking website used fake number as I was able to bypass otp And then just open my profile and start to check for IDOR. Opened my burp , refresh the page and capture the request of the profile, I found out that there are alot of parameter’s which can be vulnerable to IDOR so normally I send the request to repeater and started to test every parameter at that time I found nothing. I tried many ways but found nothing but I at that time I thought

let’s give it another try .


Then I again started to check and then I just don’t know why removed the last name from the profile and click on the save button , intercepted the request change the parameter value like \_id=1211221 to \_id=1211220 and forward the request.

## The Result was shocking as I don’t know how my profile last name got automatically filled with some others name .

Then I again tried by removing the last name and then click on the save button without intercepting the request it shows me error like last name is blank . Then I again clicked the save button and intercepted the request this time I changed the id parameter to \_id=1211219 and again it Got automatically filled.

It was very strange for me at that time because I had never experienced this kind of IDOR.

As Now I just have to make all the areas blank and just have to change the id parameter, The other users data can be seen there so easily.

After some time I found other endpoints leaking other information like cc data etc .

Now it’s time to report this to the bank .

But the result was Sad.

This Was The Complete Story of Finding An IDOR which was Very strange For Me as I was able to save data to others users profile and was able to escalate xss and also can store their data to my profile but they didn’t even replied .
