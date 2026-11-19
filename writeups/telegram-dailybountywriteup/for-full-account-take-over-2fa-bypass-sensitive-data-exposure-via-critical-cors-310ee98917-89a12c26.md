# $$$$ For Full Account Take-over, 2fa bypass, Sensitive data Exposure via Critical CORS…

- **Source URL:** https://mr-pwner.medium.com/for-full-account-take-over-2fa-bypass-sensitive-data-exposure-via-critical-cors-310ee989179a?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250511233436/https://mr-pwner.medium.com/for-full-account-take-over-2fa-bypass-sensitive-data-exposure-via-critical-cors-310ee989179a
- **Fetched:** 2026-11-19
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/9090 (id 9090)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# $$$$ For Full ATO, 2fa bypass, Sensitive data Exposure via Critical CORS Misconfigurations & Broken Session Management.

Hello Gents,

I haven’t been in the habit of writing about my findings, but I’ve decided to start sharing some of the more interesting ones from time to time.

This is my first write-up for one of my last findings, so any suggestions or questions are more than welcome!

In this write-up, I’ll walk you through how a CORS misconfiguration led to full account takeover (ATO) and 2FA bypass.

Without further ado, let’s dive into the story.

I’m going to redact the target(popular one), but one of its businesses involves a security mechanism that protects websites and applications while prioritizing user privacy. Designed to prevent automated abuse, it helps ensure interactions remain legitimate without excessive tracking or data collection.

# **Methodology**

I didn’t conduct any recon; instead, I focused directly on the root domain. I started by visiting *https://target.com/signup*

The target offers various pricing plans, ranging from **free** services to **enterprise** solutions. I opted for the **pro** version and activated the free trial.

Once registered, I logged in with my credentials and was redirected to *https://dashboard.target.com***profile settings**, I enabled **2FA** and added a **passkey** as an additional authentication method, allowing login without requiring a password each time. 

With my account set up, I continued exploring the application as a regular user while proxying traffic through Burp Suite.

After some time navigating back and forth on the dashboard, I came across a`GET` request in the burp history to the endpoint*https://accounts.target.com/auth/pro/allowed-accounts*`user-type`, `email address`, `encrypted_email`, `is_favorite`, and the `banned` parameters.

The most critical issue, however, was that the response also included a valid session token in the `Set-Cookie` response header—where the real chaos began.

Up to this point, everything seemed quite normal. However, seeing `Access-Control-Allow-Origin:`  along with *https://accounts.target.com*`Access-Control-Allow-Credentials: true` in the server response immediately caught my attention. That’s when I stopped everything else and started testing for a potential CORS issue.

# Understanding CORS Misconfigurations and Their Impact on Web Security

**Description:** Cross-Origin Resource Sharing (CORS) is a security mechanism enforced by web browsers to control how resources are accessed across different origins, complementing the Same-Origin Policy (SOP).

Misconfigurations occur when a server improperly allows cross-origin requests, potentially exposing sensitive data to unauthorized websites. This typically happens when wildcard origins (`*`), trusted subdomains, or improperly configured `Access-Control-Allow-Origin` and `Access-Control-Allow-Credentials` headers grant unintended access. Attackers can exploit this to steal user data, hijack sessions, or perform unauthorized actions on behalf of a victim, bypassing the protections of SOP.

The original request and response looked like this:

I extensively tampered with the `Origin` header in an attempt to trigger a CORS misconfiguration, but all my attempts were rejected—the response consistently refused unauthorized origins. However, when I replaced the `Origin` header with a domain that the target explicitly trusted, I noticed it was reflected in the response (brute-forced a list of trusted origins). Interestingly, this was the **only subdomain** that got accepted.

I then retried all my previous techniques to manipulate the `Origin` header, but nothing changed. In each attempt, `Access-Control-Allow-Origin` and `Access-Control-Allow-Credentials` were simply omitted from the response when the origin was invalid.

The breakthrough came when I discovered that appending(concatenating) any string to the trusted subdomain (takeover) still resulted in the request being accepted. This worked with both `https` and `http` schemes, like so:

`Origin:` *https://blablasub.target.com*

`Origin:` *http://blablasub.target.com*

That was all I needed to craft a proof of concept. I created an `XMLHttpRequest` to the vulnerable endpoint including the creds with the request and successfully read the sensitive response from my arbitrary origin. To demonstrate the impact, I hosted a harmful script on my server that originates the request(https://**bla**sub.target.com) to fetch the data and extract the response.

## The script looked like this below:

```
<!DOCTYPE html>
<html>
<body>
<center>
<h1>CORS PoC Exploit</h1>
<div id="demo">
<button type="button" onclick="cors()">Click Me</button>
</div>
</center>
<script>
function cors() {
  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
      document.getElementById("demo").innerHTML = alert(this.responseText);
    } else if (this.readyState == 4) {
      document.getElementById("demo").innerHTML = document.write("Error: " + this.status);
    }
  };
  var url = "https://accounts.target.com/auth/pro/allowed_accounts";
  xhttp.open("GET", url, true);
  xhttp.withCredentials = true;
  var requestBody = JSON.stringify({
  });
  xhttp.send(requestBody);
}
</script>
</body>
</html>
```
## PoC from my origin

At this point, I had a **CORS misconfiguration leading to sensitive data disclosure to arbitrary origins**, which would most likely be accepted as a medium to high-severity issue. However, instead of reporting it right away, I decided to dig deeper — hoping to escalate it into a full **Account Takeover (ATO).**

**Funny Note:** As seen in the screenshot above, the request requires the *X-Csrf-Token*

**Important Note:** Whenever you come across a CORS issue, especially when the **Origin** is dynamically reflected in the response, don’t rush to report it — take a closer look. You might just uncover something even more impactful.


# The Login Mechanism

Just to remind you, after enabling the **2fa**, **passkey** the login process to the application would be like this:

1. The user visits [**https://target.com/login**](https://target.com/login).

2. The application prompts the user to choose a login method:

**2.1. Passkey Authentication**

- The user enters the passkey (a pre-defined word, biometric verification, etc.).
- If successful, they are logged in.

**2.2. Two-Factor Authentication (2FA)**

- The user enters their email address.
- The user enters their password.
- The user provides the 2FA code.
- If all steps are successful, they are logged in.

# **Pre-account Take-over**

As mentioned earlier, the response includes a valid session cookie, which is flagged as **HttpOnly** to prevent JavaScript from accessing it.

Normally, this would protect the cookie from being stolen via client-side scripts. However, in my case, the response itself leaked the session token in the **response headers**. Although the cookie was automatically sent with each request, the server **regenerate it in the response**, effectively exposing it. This meant I didn’t need to use any backend language to retrieve it — it was already logged in my server logs.

# Account Take-over

Now, I was just **one step away from a full Account Takeover (ATO)** since the application relied entirely on this session cookie for user authentication.

With the leaked session token in hand, I opened a new **incognito tab** using different browser and manually injected the cookie into the browser’s **cookie jar**. After refreshing the page, I was successfully logged in as the victim — gaining **full control over their account** while **completely bypassing the authentication process, including 2FA and Passkey mechanisms.**

You might be thinking the same thing I did — **could this be a false positive?** To verify, I switched to a different network with a new IP address and retried using the session cookie.

**Surprisingly, it still worked.** The session remained valid, allowing me to log in as the victim again. This was unexpected because, according to the application’s **security policy**, session tokens were supposed to be **IP-locked** and **non-reusable** after login. Clearly, that wasn’t the case.

At this point, I documented all the details and compiled a thorough report, outlining the vulnerabilities and their potential impact. I then informed the company about the issues, ensuring they were aware of the risks and could take appropriate action to mitigate them.

# **📌 Report Timeline**

- **Report Date:** Wednesday, Feb 19, 2025–10:26 AM
- **First Response:** Wednesday, Feb 19, 2025–1:51 PM
- **Triaged:** Wednesday, Feb 19, 2025–10:03 PM *(Partial fix applied, resolving the CORS issue)*
- **Resolved:** Sunday, March 9, 2025–9:13 AM
- **Bounty Awarded:** $$$$ — Saturday, March 14, 2025–1:57 PM
- **Status:** ✅ Resolved

Thank you for taking the time to read my write-up! I hope you found it insightful. This definitely won’t be my last — more write-ups are coming soon! If you enjoyed it and want to see more, feel free to follow me on my new account for future posts.
