# 21.3 Lab

- **Source URL:** https://cyberw1ng.medium.com/21-3-lab-ssrf-via-openid-dynamic-client-registration-2024-c9ffd445e438?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20241112235702/https://cyberw1ng.medium.com/21-3-lab-ssrf-via-openid-dynamic-client-registration-2024-c9ffd445e438
- **Fetched:** 2026-11-27
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/6122 (id 6122)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# 21.3 Lab: SSRF via OpenID dynamic client registration | 2024

## This lab allows client applications to dynamically register themselves with the OAuth service via a registration endpoint. Some client-specific data is used in an unsafe way by the OAuth service, which exposes a potential vector for SSRF. solve the lab by crafting an SSRF attack to access [http://169.254.169.254/latest/meta-data/iam/security-credentials/admin/](http://169.254.169.254/latest/meta-data/iam/security-credentials/admin/) and steal the secret access | Karthikeyan Nagaraj

# Description

This lab allows client applications to dynamically register themselves with the [OAuth](https://portswigger.net/web-security/oauth) service via a dedicated registration endpoint. Some client-specific data is used in an unsafe way by the OAuth service, which exposes a potential vector for SSRF.

To solve the lab, craft an [SSRF attack](https://portswigger.net/web-security/ssrf) to access `http://169.254.169.254/latest/meta-data/iam/security-credentials/admin/` and steal the secret access key for the OAuth provider's cloud environment.

You can log in to your own account using the following credentials: `wiener:peter`

## Note

To prevent the Academy platform being used to attack third parties, our firewall blocks interactions between the labs and arbitrary external systems. To solve the lab, you must use Burp Collaborator’s default public server.

# Solution

1. Turn on Foxy Proxy and turn off the Intercept,
2. Log in to your own account.
3. In Burp Repeater, create a `POST` request to register your own client application with the OAuth service.
You must at least provide a`redirect_uris` array containing an arbitrary whitelist of callback URIs for your fake application. For example:

```
POST /reg HTTP/1.1
Host: oauth-YOUR-OAUTH-SERVER.oauth-server.net
Content-Type: application/json
{
    "redirect_uris" : [
        "https://example.com"
    ]
}
```
4\. Send the request. Observe that you have now successfully registered your own client application without requiring any authentication. The response contains various metadata associated with your new client application, including a new `client_id`.

5\. If you find a GET request to `/client/CLIENT-ID/logo` then send it to repeater else send a oauth GET request which contains session and cookie, then modify the Request to `/client/CLIENT-ID/logo`

6\. In Repeater, go back to the `POST /reg` request that you created earlier. Add the `logo_uri` property and replace the current `logo_uri` value with the target URL: The final request should look like below

```
POST /reg HTTP/1.1
Host: oauth-YOUR-OAUTH-SERVER.oauth-server.net
Content-Type: application/json
{
    "redirect_uris" : [
        "https://example.com"
    ],
    "logo_uri" : "http://169.254.169.254/latest/meta-data/iam/security-credentials/admin/"
}
```
7\. Send the request to register a new client application and copy the `client_id` from the response.

8\. In Repeater, go to the `GET /client/CLIENT-ID/logo` request that we crafted in 5th Step. Replace the `CLIENT-ID` in the path with the new one you just copied and send the request.

9\. Send this request. Observe that the response contains the sensitive metadata for the OAuth provider's cloud environment, including the secret access key.

10\. Use the “Submit solution” button to submit the access key and solve the lab.

A YouTube Channel for Cybersecurity Lab’s Poc and Write-ups

Telegram Channel for Free Ethical Hacking Dumps

Thank you for Reading!

Happy Ethical Hacking \~

`Author: Karthikeyan Nagaraj ~ Cyberw1ng`
