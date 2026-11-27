# Authentication Bypass -MFA , Account Takeover…

- **Source URL:** https://medium.com/@prakashchand72/authentication-bypass-mfa-account-takeover-32166aedb3b9?source=rss------bug_bounty-5
- **Fetched from:** https://medium.com/feed/@prakashchand72
- **Fetched:** 2026-11-27
- **Channel:** @dailybountywriteup
- **Telegram message:**  (id 6979)
- **Method:** medium-rss-content readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
### Authentication Bypass -MFA , Account Takeover…

This blog is about how I was able to takeover the account and bypass multifactor authentication using manual analysis. Take a seat belt and enjoy, this gonna be long ride.

### Motivation

After a nearly year-long break from bug hunting due to work and Job, I finally decided to resume hunting on weekend so I started searching for platform / application based target rather than wildcard domain. Nearly after a minutes I decided to hunt for app.*redacted*.com as it contained new registration function and others.

### Let us Begin

I always like to go with the steps if I finds registration/signup page I first like to check if I can create anyone’s account with their email bypassing the authentication/verification code/link sent to their email. I also like to play with parameter as much as possible so I did same on this target also. The moment I landed on signup page I tried to register a fresh new account then check all the true cases first. True cases could be response of successful account creation, api/endpoints used and other.

### About Web Application

Knowing about how the application functions is important to bypass anything. So I realized that web application on creating new account it sends xxxx-xxxx-xxxx digit format code to the email and requires to enter to verify and active the account. Also after successfully creating account there is a team section which automatically add you to the team group if you belong to that org/domain. Means if you create a account on platform with lets say *astute@tesla.com* you will automatically be added to its Team group i.e. tesla.com in this case and you can read/write all chats and photos of members sent on team group.

### Analysis and Approach

Now I knew about how application works so I tried to bypass the authentication aiming to create account with anyone’s org/domain email. I created an email lets say *astute@tesla.com and* obviously I don’t have access to that email*.* After playing with all the parameter, I sent a random code which was obviously wrong code and intercepted the request to see the parameters its using and then I saw a very big flaws on its development.

The application was using a parameter called *grant\_type* which was responsible to authenticate or more like tell server how to verify the code so that application server can create account. Lets look at the POC to understand better.

As the POC screenshot might be enough to explain what happened in any case I am writing. So basically I was able to bypass the authentication that I required to enter xxxx-xxxx-xxxx code by just telling server that I want to authenticate the token by not using that token but the password.

Here is the catch, since the password I already knew as its the same password I used to create account on signup page I can now just bypass authencation and can create anyone’s account and join the team and read the chat.

Wait Wait Wait!!

It’s not that easy. Yup I was able to create account but still some mechanism was there and saying it needs to make sure that the right person is accessing. 

As this point I was little disappointed because you know the feeling right when it so close yet so far.

### MFA Bypass

Now it was sending the activation link which on clicking gets activated. I did the basic thing here which comes first to every pentesters mind. I intercepted the request it was sending while making the api call to send the activation code to the email. Here first I tried with my own email to check what kinda activation link it’s generating. Then I realized one more bigger flaws then first one.

Actually the activation link was already reflecting on the response of api call made, so basically I clould active the account without needing access to the victim email.

Now I can create account with anyone’s email and access all of it’s organizations stuff. Preety cool right!

### Bonus

I am adding bonus here for reader, the injection was also possible on the link that get generate for activation. Actually there was a parameter called *content* which is getting reflected to the link on activation. I cloud only inject the text on link itself but the injected text was adding after ? so the activation link remained same which doesn’t led to open redirect or html/xss injection. Let me know what other cloud have been possible on this test case.
