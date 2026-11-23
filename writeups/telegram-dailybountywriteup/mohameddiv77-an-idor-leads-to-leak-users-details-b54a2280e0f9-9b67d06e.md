# An IDOR leads to leak users details

- **Source URL:** https://medium.com/@mohameddiv77/an-idor-leads-to-leak-users-details-b54a2280e0f9?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20240925225829/https://medium.com/@mohameddiv77/an-idor-leads-to-leak-users-details-b54a2280e0f9
- **Fetched:** 2026-11-23
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/7365 (id 7365)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# An IDOR leads to leak users details

**Hello Amazing Hackers… Mohamed Ibrahim is Here**

This is my second Article and we will talk about how I was able to get a bounty from duplicated IDOR vulnerability..

First, while searching for a new private bug bounty program(if you have non) I used the method of my friend **Daoud Youssef** to get new private programs:

`waybackurls hackerone .com | grep "embedded_submissions/new"`
So I collected all those urls in one file [here](https://mega.nz/file/tKhGEJxB#9JSppS4lGARoR2ZvFUCBT4Xfbl9NXsvDO7PKWZZC4D4) and picked one of them to start hacking.

I quickly registered a new account on my target and start playing in dashboard section with BurpSuite running in the background .

then I noticed that any request made in the profile section has a **hashId** post parameter that identify the user. Any request like get/update/delete any user information uses this parameter:

So I was thinking about an IDOR in this parameter so I get another user **hashId** and replace it in the original request and send it, But It didn’t work(It’s not that easy).

then I try to delete the cookie header with it’s value to see what will happen.

For my luck the request worked with 200 OK and get all user details.(😃😃)

To confirmed it more, I used a request to update the first name of the other account and it really worked:

Till now it consider a informative issue as the **hashId** of the user is required and it’s not recognizable . Now Let’s see how to find the victim **hashId**.

I back again to the app dashboard and played with all profile features to see if the **hashId** is leaked in somewhere in the app and see the waybackurls of the app to see of the **hashId** is leaked in any parameter or something like that. Then I remembered something in the [zseanos-methodology](https://www.bugbountyhunter.com/methodology/zseanos-methodology.pdf) book of [zseanos](https://twitter.com/zseano):

I used burpsuite search to search for the **hashId** in httphistory and I found that when I uploaded my profile image, It’s uploaded to another website and the url was like:

`https://cam-image-store.target.com/ddm_images/xxx_hashid_xxxxxxxxxxxxxxxxxx`
The **hashId** was leaked in the profile image url :

So that, Let’s go … I got your profile image url →>I got your **hashid** → I can create/update/delete any information in your account….OR use this magic:

```
gau cam-image-store.target.com|cut -d "/" -f 4 >>hashid.txt
waybackurls cam-image-store.target.com|cut -d "/" -f 4 >>hashid.txt
```
I collected all user’s **hashId** in one file. Boom the IDOR is complete now.

**Leaked victim’s hashId leads to IDOR in leaking/changing any account\_details of the victim**

I send the report to the company and got duplicated.

I leaved the app for a week and start again with the profile image section. After many tries that didn’t work, I said let’s try to upload this [image](https://github.com/barrracud4/image-upload-exploits/blob/master/DoS/lottapixel.jpg).

when Uploading a profile image[(lottapixel.jpg)](https://github.com/barrracud4/image-upload-exploits/blob/master/DoS/lottapixel.jpg) to my account, I noticed that all update/modify account details functions are gone and I can not modify any details on my account, even the input fields were not working because the uploaded image. It is Just a typical data compression bomb. When loaded to memory, it will be unpacked as 4128062500 pixels. So it disable the whole dashboard function and I can not make any more updates to my account or modify any thing in it.

So I used the previous IDOR vulnerability to update the victim profile image and prevent him form doing any update/modify action in his profile.

I report it and they close it as Informative and said:

This issue occurs because of the pre-existing IDOR issue on which we are currently working. This becomes void once we fix the IDOR issue as the proposed risk of accessing other user data and updating their profile will not be possible.


All this happened in December 2023.

After 10 months, In one of my military service vacation, I decided to look at my duplicated reports and accidentally open this report and found that it turned into Resolved.

So I said let’s give it a try…

After reviewing the app again, I found that they had removed the **hashId** from the profile image url and used new domain to host user’s image(if you upload your image the url will be clean) and added a jwt token in the cookie header(when trying to update profile information using **hashId** only(vulnerable request), the request didn’t work. all the dashboard actions require the jwt token).

But I found that the jwt token(cookie header) didn’t required in the retrieve user information request. And it is still vulnerable to IDOR with only the **hashId** parameter:

Again I used the old hosting website(cam-image-store.website.com) to collect the **hashId** of the users again (😃😃):

```
gau cam-image-store.target.com|cut -d "/" -f 4 >>hashid.txt
waybackurls cam-image-store.target.com|cut -d "/" -f 4 >>hashid.txt
```
And now we have anew one, IDOR leads to leak users details

I send them the report and this time I send the **hashId** file in the report and fortunately accepted the report and rewarded my with $$$.

Thank you Amazing Hackers for reading my writeup.

For any FAQ or any FeedBack, I’m here:
