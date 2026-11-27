# MY First Bounty | Pre Account take Over via respon manipulation| Pre ATO

- **Source URL:** https://nervhym.medium.com/my-first-bounty-pre-account-take-over-via-respon-manipulation-pre-ato-ababd7ca46aa?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20260322024710/https://nervhym.medium.com/my-first-bounty-pre-account-take-over-via-respon-manipulation-pre-ato-ababd7ca46aa
- **Fetched:** 2026-11-27
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/10047 (id 10047)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Pre Account take Over via respon manipulation| Pre ATO

Hello everyone, today is a special day for me, i am very happy because this is the first time a got a bug and paid, so i want to share a little about this finding, ok just go ahead.

So my finding is otp bypass lead to acount take over via respon manipulation, that day i was confused because everyday i always get informative bug, even out of scope because i don’t read the information in the program guidelines hahaha 😅😅.

After after reading a lot of writeups, watching some poc on youtube, i finally found a website that intrested me, i finally hunted there, and it turned out that the website required otp verification via email and number phone, i also remembered the poc that i had watched, then i rushed to try it

**Step to reproduce**:

1. first,In the target web app, i creat acoount using email normally, in the register respon section, there is a json succes respon, then i save it.

```
Response
HTTP/2 200 OK
 
{
  "data":{
     "loginEmailVerify":{
                "code":200,
                "success":true,
                "message":"Successfully Verified Email",
                "user":{"id":"[id]",
                "email":"example@mail.com"
     },
     "source":"EMAIL"
    }
  }
}
```
2.After that, i create new account and in the otp section i using random otp.

3.Before sending the otp, turn on burpsuite intercept, then click send

4.In the otp request section, right-clik and do intercept, then forward

5.Then in the response section, change the json error to json succes that we saved earlien in the step 1. then forward again

6.And well, the account succesfully created and can do account registeration as usual

Note: Usually pre account take over many do not accept it, but maybe this is a financial services company, and there is an otp that protects it, so they accept it.

thanks for reading.
