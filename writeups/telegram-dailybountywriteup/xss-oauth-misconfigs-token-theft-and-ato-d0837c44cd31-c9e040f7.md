# XSS + OAuth Misconfigs = Token Theft and ATO

- **Source URL:** https://7odamoo.medium.com/xss-oauth-misconfigs-token-theft-and-ato-d0837c44cd31?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250501113402/https://7odamoo.medium.com/xss-oauth-misconfigs-token-theft-and-ato-d0837c44cd31?source=rss------bug_bounty-5
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/7425 (id 7425)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
The story begins with finding XSS at `sub1.target.com` The problem was that the program was paying lower bounties for this subdomain, so our target was to escalate this XSS to ATO on the main target app `app.target.com`since the program was paying much more for this subdomain.

Looking at the auth mechanism of `sub1.target.com`, we found that it was authenticated via a `cookie-based JWT token`, while the auth mechanism in `app.target.com` was via an `Authorization header-based JWT`. The JWT value on the two subdomains was different, but surprisingly, the JWT from `sub1.target.com` worked for authentication on `app.target.com`!

So, if we could leak the JWT auth token from `sub1.target.com`, we could use it for authentication on `app.target.com`.

Unfortunately, the cookie-based JWT token on `sub1.target.com` was protected with an `HttpOnly` flag, so it wasn't possible to access it via the XSS. However, during our analysis of the target’s oauth flow, we found another way to leak these JWT tokens!

We found this request, which had the JWT token in the response from another subdomain, `auth.target.com`.

After further analysis, we found interesting behavior on the previous request. We found that if we changed the `response_mode` parameter value from `post` to `get`, the response will be different. Additionally, we could set any value for the `state` and `nonce` parameters and the server would still return the auth token.

Now with the XSS in `sub1.target.com`, we can create an iframe that loads the OAuth endpoint on `auth.target.com`. Fortunately there weren't any `X-Frame-Options` or `CSP` in place to prevent framing of this endpoint, However, the SOP will prevent access to the `contentWindow` object of an iframe from a different origin.

We considered if both subdomains set `document.domain = 'target.com'`, putting them into the "same origin" state.

This technique was used to relax SOP between subdomains under the same second-level domain. If both subdomains explicitly set the `document.domain` property to the parent domain `domain.com`, they will share the same origin, allowing cross-origin access.


However, this technique is no longer supported by modern browsers like [chrome](https://web.archive.org/web/20250501113402/https://developer.chrome.com/blog/immutable-document-domain/)

Instead, we found that when we navigated to `https://auth.target.com/oauth?client_id=redacted&redirect_uri=https://auth.target.com/endpoint.jsp&response_mode=get&response_type=code&scope=redacted&state=redacted&nonce=redacted`, it redirected us to `https://sub1.target.com#token=`. As a result, the page is now considered to have the same origin, allowing us to access the `location.href` property of the window and extract the token from the URL fragment.

```
var auth = document.createElement('iframe');
xe.setAttribute('src',' https://auth.target.com/oauth?client_id=redacted&redirect_uri=https://auth.target.com/endpoint.jsp&response_mode=get&response_type=code&scope=redacted&state=redacted&nonce=redacted');
auth.setAttribute('id','lol')
token = new URLSearchParams(document.getElementById("lol").contentWindow.location.hash.split('#')[1]).get('token');
```
After initiating the request to get the token fragment from the URL, we can send it to the attacker’s server.

Since the JWT auth token was stolen from the authentication flow at `auth.target.com` using XSS on `sub1.target.com`, we can then include the stolen JWT auth token in requests to change victims' email addresses on `app.target.com`to achieve ATO.

The full attack flow can be shown as following:
