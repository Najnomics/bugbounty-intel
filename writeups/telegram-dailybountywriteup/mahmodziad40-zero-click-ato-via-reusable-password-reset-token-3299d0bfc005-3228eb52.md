# Zero-Click ATO via Reusable Password Reset Token

- **Source URL:** https://medium.com/@mahmodziad40/zero-click-ato-via-reusable-password-reset-token-3299d0bfc005?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250927043542/https://medium.com/@mahmodziad40/zero-click-ato-via-reusable-password-reset-token-3299d0bfc005
- **Fetched:** 2026-11-21
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/10483 (id 10483)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Zero-Click ATO via Reusable Password Reset Token

Hey Guys and Welcome Back After long time , I Stopped Hunting for 3 months ago and return back again with a **ZERO CLICK ATO** , it seems a traditional bug for the most of hunters but also so many Hunters didn't care to test in Reset Password Functionality , so lets start :

Let’s assume the domain called example.com , First of all I always prefer to test on the main domain first before testing on any subdomain to know more about what the website doing and those stuffs

## **My Testing Methodology :**

### STEP 1

- open Burp Suite and Enable the Foxy Proxy
- I Click on Every Button in the website and go check the HTTP History in Burp

**NOTE:** Don't Forget To Enable the Advanced Scope Option and the Filter in the HTTP History


### **STEP 2**

So Now I have so many request in HTTP History , then I check every request to see what is the parameter that can be test and etc. ..

in this website I have fully focused to Test on the Logic Bugs Like (IDOR,BAC,Broken Authentication,ResetPassword,SignIn,SignUP,Update Profile.. etc)

### **STEP 3**

After checking every request I didn't found any something useful for testing , so I tried to test in the Reset Password Functionality

NOTE : if you going to test on the reset password make to Account one for Attacker and one for Victim to see how its work on both


### STEP 4

After I Registered Two Account on the website , I Clicked on the forget Button to reset the password on the (Attacker) Account just to see How it works

After that I go to Gmail to see And I found A Parameter Called hash

```
hash=FoFTtvpdhqRtg 
// This hash param contain the value of the Token that Check for reset the Password of the attacker
```
As you can see this value seems like it cant be predictable, But Wait !

CAN WE SEND THE REQUEST AGAIN??

I took this Request to the Repeater and send it Again to see if the Value Going to change or not , And I Saw that

THE VALUE REMAIN THE SAME AND DIDNT CHANGE !!

So what Know ?

We Have Tested the Reset Password Functionality on the Attacker Account maybe the token didn't change on the Attacker Account BUT what About the Victim Account ?? How we Gonna chain it to ATO ?

After that I did the same test on the Victim Account and it Gives me the same Hash Value HAHAHAHAHA

We Know from the Previous test that we have this link for resetting the password

`https://www.example.com/shoping/index.php?content=loginresetpasswd&destination=reservedarea&language=en&email=attacker@gmail.com&hash=FoFTtvpdhqRtg`
And this Link have the same Format on the Second test , SO if you just know the email of the victim you can change it in the email parameter and it going to work , but honestly after I tried this it also didn't work LOL .. HOW ??

if you want to take over account you need first to send another new link with the Victim Account like that

And with this way you going to change the email parameter easy and it will open to you like that

now we Can change the password of the Victim easily

After that as you can see below we entered to the Victim Account easily with Zero-Click ATO

Thanks for reading! If you found this write-up helpful or interesting, feel free to share it with others in the security community.

See you After 3 months XD 😘

My Social Media : [(15) Ziad Mahmod | LinkedIn](https://www.linkedin.com/in/ziadmahmod/) [(4) Instagram](https://www.instagram.com/cyberwithzuz/)
