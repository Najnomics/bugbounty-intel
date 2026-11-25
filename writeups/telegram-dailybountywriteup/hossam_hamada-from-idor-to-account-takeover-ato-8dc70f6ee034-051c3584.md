# From IDOR to Account takeover(ATO)

- **Source URL:** https://medium.com/@hossam_hamada/from-idor-to-account-takeover-ato-8dc70f6ee034?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20231012203630/https://medium.com/@hossam_hamada/from-idor-to-account-takeover-ato-8dc70f6ee034?source=rss------bug_bounty-5
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/3591 (id 3591)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# From IDOR to Account takeover(ATO)

--

Hello everyone ,

I’m Hossam Hamada, Today I would like to share with you one of my discoveries in HackerOne ’s program

Let’s say : [https://example.com](https://web.archive.org/web/20231012203630/https://example.com/)

When conducting a test on this website,I found the profile editing function ,I found that I can’t change my email and I can change my password without entering the old password.

I decided to edit the profile and intercepted the request by Burp Suite

I wanted to know how he knew me as his user

I sent the request to the repeater, And I tried to change only the (user\_id), sent the request and found this in the respons “result”:{“result”:-1} and this means that the request is not accepted

Then I tried changing the email only and the result was the same again

I returned everything as it is and then sent the request and found this in the respons “result”:{“result”:1} and this means that the request is accepted.

Here I have concluded that I can enter any password (user\_pw), which is the new password for this account , but I cannot change the email (user\_email) or ID (user\_idx).

Another idea came to me, which was to create another account and take his email(user\_email) and ID(user\_idx)

Then enter them in the previous request

To make sure that he really knows me as a user only through email(user\_email) and id(user\_idx)

And already I did it and the request succeeded.

But a problem appeared in the execution of the attack, you need his email(user\_email) and Id(user\_idx) and this is difficult

But I noticed that the ID(user\_idx) of the last account created in this program is the number of accounts in the program

It was easy to guess the ID(user\_idx) of a particular account because the accounts of this program do not exceed 2500 accounts

I have found a way to find out some dangerous emails that are already registered in the program (this is in order to escalate the risk of vulnerability)

This is the way :

I was able to access the important emails of the organizations through the publications uploaded through them and attached to their emails

I took these emails and started testing whether they are already registered in this program or not by “forgetting a password” for each email.

(If the email already exists, the message “a message has been sent to the email” will appear , if it does not exist, “an error will appear”)

Some of them have already been registered .


And here we appreciate the implementation of the attack :

1- We create an account 

2- Then we log in

3- go to edit profile

4- We open burp suite

5- Then we intercepted to the request to save the modification

6- We’re gonna change the email to the victim’s email And Enter a new password Through the burpsuite

7- Then we send the request to the intruder

8- Now we’re gonna guess the victim’s (user\_idx)

9- We will guess the user\_idx 

10- We will guess the user\_idx from 1 to 2500

11- Another note I noticed when accepting the request will be in the response (“result”:1)and when not accepting it will be (“result”:-1)

12- Therefore, before turning on the intruder, we search for “result”: 1 by Grep in options

13- Then we turn on the intruder

14- We will notice after completion, find the user\_idx of the victim , and the new password has already been set for this account and therefore we can log in with the email and the new password that we created


I finally did it. 

Thanks for reading!
