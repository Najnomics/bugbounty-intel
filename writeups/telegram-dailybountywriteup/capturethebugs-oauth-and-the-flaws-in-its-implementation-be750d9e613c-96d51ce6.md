# OAuth and the flaws in its implementation

- **Source URL:** https://medium.com/@capturethebugs/oauth-and-the-flaws-in-its-implementation-be750d9e613c?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20221211122220/https://medium.com/@capturethebugs/oauth-and-the-flaws-in-its-implementation-be750d9e613c
- **Fetched:** 2026-11-24
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/896 (id 896)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# OAuth and the flaws in its implementation

What is OAuth?

Open Authorization (also known as OAuth) is an open-source framework that allows you to create accounts on websites without having to create a different user account for each website. They rely on authentic third-party websites, such as Facebook or Google, to perform the authentication process for them.

It is:

1. It is used to log into websites without the need to form an account first.
2. Resource sharing is performed through this method.
3. SSO is also utilised in businesses and enterprise networks for a variety of purposes (Single Sign On)

Isn’t it intriguing to think about? But what are the options for gaining access to something without having to create an account? Let’s see how well it works out for you.

**How OAuth Works?**

To simplify the work flow let’s first isolate the entities involved.

They are:

1. User (i.e., you)
2. Application that you want to access
3. Authorization Server

For example, you go to example.com. To access its services, the site tells you to login. But you don’t want to create a separate account and deal with the hassle of creating a new user account and remembering the password. But there’s an option of login using Facebook. Since, you have an account on Facebook, you choose to go with Facebook and avoid the pain of create a new account and remembering the password of different services.

What you just did was accomplished using OAuth. It reduced our workflow, and we should thank the developer for creating such a framework. But just like any framework present in the market, based on how it’s configured it can lead to account takeovers. Let’s understand how.

From the example taken above, you are the user, example.com is the application that you want to access, and since it’s using Facebook that you decided to login through, the Authorization and the Resource server will belong to Facebook.

When you click on the login with Facebook button, there are a series of steps that occur before you can be allowed to access example.com

Let’s first understand the workflow:

1. You click on the login with the Facebook button.
2. You will be taken to Facebook authorization server, where you might be asked to login.
3. Once logged in, it’ll ask you to authorise Facebook to provide your details (like Profile pic, username, etc.) to example.com, the scope is predefined and facebook will shows you the information that the third-party website is asking for.
4. Once you click on yes, it’ll redirect you to example.com and send a unique token to example.com using which example.com can fetch your details from the Facebook resource server.

Let’s go through them one by one.

Step1:

When logging in through Facebook, you might find that you are being redirected to a URL, that appears something like:

Let’s go through the parameters:

1. client\_id: To avail login using Facebook button on their website, example.com will have to register itself to facebook.com. Facebook will then provide example.com with a unique id. Here it is ot99ay3jjhmhmj64jmhx6. Facebook keeps track of all activities, such as the access tokens that are fetched by the website and what information the client or third party can obtain from Facebook, among other things.
2. redirect\_uri: It is the URL to which Facebook will have redirect to, once it confirms that it is indeed you and you provide permission to example.com to share your profile and email. Facebook will redirect to the URL with an access token which provides the third-party website authorization to fetch the corresponding information from the Facebook to which you have authorized them.
3. response\_type: It can be either of code type of token type. In the token type, Facebook’s Authorization server will directly grant example.com a token using which it can access your account details from the Resource server. In the code type, Facebook will return a code to example.com and then example.com will again make a request to Facebook using the code. Facebook will check the code and then return a token.
4. scope: This is exactly what example.com is looking for from Facebook. We can see that it is requesting our profile information as well as our email address. It can request a variety of information, such as gender, date of birth, and so on.
5. state: This performs the function of a CSRF Token. It should be chosen at random.

The end result of this step is you being taken to Facebook where you will first login and then grant the permission

Step2:

Once you are redirected to the login page, you can enter your Facebook username and password, and once Facebook validates the username and password, it redirects you to a page that displays the information that the website is requesting from Facebook, as well as whether you agree to allow the website to fetch this information from Facebook. After that Facebook generates a token that is attached to your account and then returns it to example.com/oauth, the example.com might use or save the token for further use. For instance, let the token be token=w1kcu82\_23ce

Step3:

exampe.com will make a request to the Facebook resource servers using the token generated and fetch your profile and email and other information which you permitted.

**Vulnerabilities due to misconfiguration of OAuth**

Incorrect OAuth implementation, if not properly configured, can result in a complete account takeover. This will not only compromise the account of the user, but it will also bring damage to the company’s reputation as a result of the incident.

Let’s quickly go over a few bugs.

**Redirect URI**

Look at the URL:

If the Redirect URL is incorrectly defined, for example, if the whitelisting is too broad or not properly configured, the redirect will perform poorly. Imagine that example.com is using the OAuth implementation and that users were being directed to example.com/oauth/token.php with a token, but that instead of configuring an absolute URL they simply whitelisted example.com, so if the attacker has control over several pages such as the profile or other, he can use this to redirect users to those pages and capture the token, as demonstrated in the following example. In addition, when combined with the open redirect, it becomes really intriguing, and the attacker might get a great deal of advantage as a result.

This above URL will redirect user to attack\_domain.com after the user completes the authentication.

**Missing or improperly configured State Parameters**

The state parameter is used as a CSRF token in order to prevent the CSRF from being executed. When the user is forwarded to the authorization server and when the authorization server refers the user back to the website, it is required to ensure that the user is the same as before and that the request is made with the same credentials. As a result, a CSRF token is required, which can be issued by the website and then verified by the website once the user returns to the website. So when the user is redirected to the authorization server, a random state parameter will be appended to the request, and when the user completes the authorization and is redirected back to the website, the website will check whether the token is the same or not, and if it is not, the request will be dropped.

**Attack Scenarios:**

The attacker can initiate a login by sending a social media request and then performing the login himself. The attacker copies the authorization token once the website generates it and then drops the request, ensuring that the token remains valid and does not expire. He delivers the link to the user in the majority of cases as a CSRF form. Upon clicking on the link, an attacker’s social media account will be linked to the user’s account, and the attacker will be able to take over the user’s account by logging in with his own social media account.

Several factors contribute to its vulnerability, including the absence of state parameters, the low entropy of state parameters, and the generation of identical state parameters on a consistent basis.

**Conclusion:**

OAuth has considerably decreased the amount of work we have to do, but it has also increased the amount of work required on the developer’s end. This can result in a large number of problems, which can result in a substantial shift in the course of events, which can result in an unpleasant scenario for the firm.

As a result, it is critical for developers to be on the lookout for the common attack scenarios listed above.
