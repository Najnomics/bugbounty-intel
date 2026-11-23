# OAuth Impersonation Attack

- **Source URL:** https://medium.com/@security.tecno/oauth-impersonation-attack-misconfiguration-of-facebook-and-google-oauth-leading-to-account-9f838439de31?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20240813232706/https://medium.com/@security.tecno/oauth-impersonation-attack-misconfiguration-of-facebook-and-google-oauth-leading-to-account-9f838439de31
- **Fetched:** 2026-11-23
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/6920 (id 6920)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# OAuth Impersonation Attack: Misconfiguration of Facebook and Google OAuth Leading to Account Takeover Crisis

By Md Rafi Ahamed

I am **Md Rafi Ahamed(Rafi Ahamed (Leonidas D. Ace))**, a Cyber Security Researcher, Bug Bounty Hunter, and Penetration Tester from Bangladesh. In 2022, I had the honor of being recognized as the **4th Top Researcher** on [**TECNO SRC**](https://security.tecno.com/dashboard). Today, I will discuss a web security vulnerability case related to OAuth vulnerabilities. During my bug bounty journey, I have discovered such vulnerabilities in many applications, including Facebook and Google OAuth. For ease of understanding, we will focus on the Facebook OAuth vulnerability in this article. Let’s dive right into the topic.

# 1. Background — OAuth

OAuth is one of the fastest-adopted technologies in the Web, Android, and iOS application domain. OAuth (Open Authorization) is an open standard for access delegation that allows websites or applications to access user information without requiring passwords. This enables third-party services to exchange information on behalf of users, facilitating features like social media logins and secure data sharing between platforms. Users can specify which data to share, rather than giving third parties full control of their accounts. Major OAuth providers include **Google, Facebook, Microsoft, Twitter, GitHub, and LinkedIn**.

# 2. How does OAuth verification work?

OAuth verification works through a process called the OAuth authorization flow. Here’s a simplified explanation:

**① Client Request:** The client application (e.g., a third-party app) requests authorization from the user to access their data.

**② User Authorization:** The user is redirected to the OAuth provider’s authorization server (e.g., Google, Facebook), where they log in and grant permission.

**③Authorization Code:** Once the user grants permission, the authorization server redirects the user back to the client application with an authorization code.

**④Token Exchange:** The client application sends the authorization code to the OAuth provider’s token endpoint, along with its client credentials (client ID and secret).

**⑤Access Token:** The OAuth provider verifies the authorization code and client credentials, then issues an access token to the client application.

**⑥ API Requests:** The client application uses the access token to make API requests on behalf of the user, accessing the authorized data.

**⑦ Token Expiry and Refresh:** Access tokens are typically short-lived for security. If they expire, the client application can use a refresh token (if provided) to obtain a new access token without re-authenticating the user.

# 3. Breaking down Facebook OAuth misconfiguration

As mentioned earlier, when the server receives a token, it sends an API request to Facebook to obtain the user’s identity.

# 3.1 How secure is the Facebook OAuth process?

According to Facebook, it’s the developer who is responsible for the verification of the access token. Developers should always debug the token and before then implement the production application. Facebook even gives test users permission for that before the app is accepted by Facebook. However, most of the developers fail to properly implement the OAuth login before implementing the application on production web, android, and iOS applications.

# 3.2 Identifying vulnerability

In one of TecnoSRC’s assets, I found that they were using some popular OAuths in most of their applications.

I targeted Facebook and Google OAuth of the application. In the Facebook OAuth, when user’s logged into the application a request was made to **graph.facebook.com** containing an *access\_token*.

According to Facebook documentation, when an application receives the access token, it should verify that the token was generated for its application by calling the [https://graph.facebook.com/debug\_token](https://graph.facebook.com/debug_token) API or [https://developers.facebook.com/tools/debug/accesstoken/.](https://developers.facebook.com/tools/debug/accesstoken/.)

As Facebook doesn’t automatically verify this, it’s the developer’s responsibility. However, our target application does not verify the token, allowing an attacker to use an access token generated for another application.

# 4. Exploitation of vulnerability

To exploit the vulnerability, the attacker would need to create a malicious web application to collect the access token of the Facebook OAuth users.

# Prerequisites

To complete the attack, an attacker needs to have the following components:

① Attacker’s application that has Facebook OAuth login

② Vulnerable application does not properly verify the token.

③The affected user is a user of both the vulnerable application and the attacker’s application.

➡️Imagine the attacker creating a malicious website named **Leonidas.hunter.**

➡️The attacker presents **Leonidas.hunter** as a legitimate site and offers diverse products to attract users. Many people would use social media accounts to sign into new websites, assuming minimal security risk since they only share their email addresses.

➡️If thousands of users use OAuth on the attacker’s web application now the attacker would have access to thousands of access tokens representing real users, generated for **Leonidas.hunter**.

In most cases, the **Facebook OAuth access token** would look like the access token below:

`EAAMTaVTBC4IBAHZBnqjxavPsTw7CVTJzsfHuoxDTZCjsJvZB1vSGfL5OOZCH673jCzXnw75O6E3oDkNTGaG8meu9sVOuIOAYnWWmzCf5x5Itjp4BonY6WDnJffZC40Qtf6qrkAxgWdMBl0l69OAy7XhKw1AKQ1gnooXZATjhYVqQj3qLvQYGxtIVYCqYGWq4LuP2YIZBYQztwZDZD`
Using **Facebook’s token debugger**, one can see all the information about the access token. If the attacker uses this token on our vulnerable application, which has an account on **Leonidas.hunter**, then the attacker will take over the account of the users. By promoting **Leonidas.hunter** to many vulnerable application users, the attacker could generate many such credentials and take over thousands of accounts.

The attack worked as the user has an account on our vulnerable application and the attacker uses the token from **Leonidas. hunter** to completely take over the user’s account on the vulnerable application.

# 5. Steps to reproduce made simple

① Try logging in using Facebook on a **vulnerable application**.

② Enter your login credentials to validate & capture the request with Burp.

③ Now replace the access token of the vulnerable application from any other website’s access token such as **Leonidas.hunter** which is the attacker’s website. (For this you can create your own Facebook app & generate your access token.)

④ Replace the access token of the vulnerable application with the attacker-controlled website’s access token.

⑤ This will log you into the user’s account on the vulnerable application and you can simply take over the user’s account on the vulnerable application.

# 6. Implementing a secure Facebook OAuth for preventing Impersonation & other attacks

The features of Facebook Login, such as **access tokens** and **permissions** make it safe and secure for people and apps to use, **but there are some security steps that the developer of apps needs to implement themselves.**

- Security Checklist
- The App Secret
- Secure Server-side Calls with appsecret\_proof
- Secure Client-side Calls with Short-term Tokens and Code Flow
- Token Hijacking
- Check Access Token Validity Regularly
- State Parameter
- Enable Strict Mode
- Use Https
- Enable JavaScript SDK for Facebook Login
- How Redirect URI Checking Works
- Lock Down Your Facebook App Settings

# 7. Conclusion

OAuth is a widely adopted and powerful technology for access authorization, enabling seamless and secure data sharing across different platforms. However, as shown in this article, even robust systems like Facebook OAuth can lead to serious security vulnerabilities due to misconfigurations. The vulnerability case discussed here underscores the importance of adhering to the security best practices and guidelines provided by OAuth providers.

**As developers, we must:**

- Diligently validate access tokens to ensure the security of server-side and client-side calls,
- Regularly check the validity of tokens, and
- Follow strict security measures, such as using HTTPS and enabling strict mode.
