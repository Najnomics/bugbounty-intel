# Lab

- **Source URL:** https://medium.com/@Geetanjalijhade/lab-basic-ssrf-against-the-local-server-walkthrough-044727d2c087
- **Fetched from:** https://medium.com/feed/@Geetanjalijhade
- **Fetched:** 2026-11-21
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14994 (id 14994)
- **Method:** medium-rss-content readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
You may or may not know about SSRF(Server-Side Request Forgery) vulnerability. I am gonna give short intro to it. For deeper understanding, visit [portswigger’s academy](https://portswigger.net/web-security/ssrf#what-is-ssrf) or other forums.

**What is SSRF?**

Server-Side Request Forgery is a web vulnerability which allows an attacker to misuse the server-side application to request to the locations or URL which may or may not bypass security verification, give access to attacker of some sensitive resources, or lead to attacker-controlled or unintended destinations.

**Lab Walkthrough**

After Accessing the lab, you get to see this page:

As the lab suggests, **‘stock check’** feature has something to do with the vulnerability. So I click on **‘View Details’** of a product then on **‘Check Stock’** button.

After intercepting the request in burpsuite, I see this:

Here, The stockApi parameter contains the URL that the application uses to fetch stock information. The application reads this URL and sends a request to it to retrieve the stock details

So I URL-Encoded the **http://localhost/admin** with the decoder tab in burpsuite.

Tho it might not have been necessary, I just did it for the fun of the game.

then I replaced the **stockApi** content with the encoded request.

And there you go, We can now see the admin page.

**BUT, We can’t interect with it!!**

**i.e** if you click on the **Delete** button to delete the carlos user, you first need to login and authenticate as the admin **OR** the request needs to come from loopback (localhost) server. Now here is where I got confused. Because I kept on changing the **‘Referer’** URL to localhost, thinking that might mean the request has been referred from localhost.

Obviously, That didn’t work. Because The Referer header indicates the page from which the request was initiated. However, modifying this header does not change the actual network source of the request.

So even if you change the **Referer** OR the **origin** parameter, it will still not work. **BUT** if you changed the **stockApi** value to ***http://localhost/admin/delete?username=carlos*** it will work.

Now, why did this **stockApi** parameter worked while others didn’t?

Because the flow of that request was something like this:

1. You send the stock-check request to the application server.

2\. The application reads the stockApi parameter from the request.

3\. The application server visits the URL provided in that parameter.

So the request sent by us is read by server as “Can you please check **stockApi** parameter and visit whatever the location is thrown there?”

So that **/admin/delete?username=carlos/** is not visited by your browser but the applications server itself.

Although we initiated the attack, the actual request to delete Carlos was made by the application server itself.

Author’s Note: This is my first writeup and walkthrough. Any mistake in understanding the concept or solving the lab which I might have done wrong or wrote about it wrongly, I’m sorry and Improvements are welcome.

#ssrf #labs #portswiggersacademy #BasicSSRFagainstthelocalserver #bug #writeup #bugwriteup #walkthrough #cybersecurity
