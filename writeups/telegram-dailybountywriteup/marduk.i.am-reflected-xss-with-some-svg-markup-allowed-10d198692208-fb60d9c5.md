# Reflected XSS with some SVG markup allowed

- **Source URL:** https://medium.com/@marduk.i.am/reflected-xss-with-some-svg-markup-allowed-10d198692208?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250809040042/https://medium.com/@marduk.i.am/reflected-xss-with-some-svg-markup-allowed-10d198692208
- **Fetched:** 2026-11-24
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/5128 (id 5128)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Reflected XSS with some SVG markup allowed

**Lab description:** This lab has a simple reflected XSS vulnerability. The site is blocking common tags but misses some SVG tags and events. To solve the lab, perform a cross-site scripting attack that calls the *‘alert()’* function.

- NOTE: Burp Suite will be needed for this lab. You may want to have Burp running before we start.

This PortSwigger Web Security Academy lab is similar to the previous two labs in that we are going to be using Burp Intruder. Most tags are going to be blocked, but with the use of Burp Intruder we can easily see which tags will go through.

## Getting Started:

Let’s begin. Access the lab. We are brought back to our simple web page with a search bar.

Attempting a simple \<img> tag injection reveals that our request is blocked by the site’s web application firewall (WAF)

```
<!-- Our simple XSS payload -->
<img src=0 onerror=alert(1)>
```
Our query is not even reaching the server. This is a JSON response saying that this particular tag, *\<img>*, is not allowed.

We need to find a tag that *IS* allowed. This is where Burp Intruder will come in handy.

Open up Burp and click on the *‘Target’* tab. Locate our search on the left hand column.

If you do not see your search, click on the filter tab just above, and make sure the *‘4xx \[request error\]’* box is checked. Click apply.

Back on the Burp target tab, right-click on our search request and select *‘Send to Intruder’* from the drop-down menu. The Intruder tab should light up orange when you do. Click on the *‘Intruder’* tab.

Our request is at the bottom. Our search string is highlighted in yellow and encoded.

We first need to alter our search string. Replace the highlighted string with empty angle brackets, \<>. Make sure your cursor is between the brackets, then click the *‘Add §’* twice.

This adds ‘*§§*’ to our search string which acts as a placeholder for all the tags Burp is going to cycle through. Your altered GET request should look like the following:

`GET /?search=<§§> HTTP/1.1`
On the [lab description](https://portswigger.net/web-security/cross-site-scripting/contexts/lab-some-svg-markup-allowed) page, in the ‘Solution’ tab, there is a link for the [XSS Cheat Sheet](https://portswigger.net/web-security/cross-site-scripting/cheat-sheet). On the Cheat Sheet, click on *‘Copy tags to clipboard’*.

Once the tags are copied, head back over to Burp Intruder and click on the *‘Payloads’* tab.

In the ‘Payloads’ tab, under *‘Payload settings \[Simple list\]’*, click *‘Paste’*. All of the tags we just copied are now listed here.

Next, click the orange *‘Start attack’* button in the upper right corner.

When our attack is complete, a few minutes with the community edition, filter by *‘Status codes’*. We are looking for the 200’s. These are tags that will go through the WAF.

There is our \<svg> tag we can use along with *‘animatetransform’*.

## SVG:

[SVG](https://developer.mozilla.org/en-US/docs/Web/SVG) is short for Scalable Vector Graphics. But what does that mean?

1. It is *‘Scalable’*, meaning the graphics can be resized without losing quality because …
2. It *is ‘Vector’*-based. SVG graphics are defined using mathematical equations rather than pixels.

This makes SVG particularly suitable for graphics like logos, icons, and illustrations.

SVG is also XML-based, (eXtensible Markup Language), making SVG files easy to create, read, and manipulate using text editors or scripting languages.

Its combination of scalability, vector-based design, and support for interactivity and animation makes it a popular choice among designers and developers.

```
<!-- Simple basic SVG example -->
<svg width="100" height="100" xmlns="http://www.w3.org/2000/svg">
  <circle cx="50" cy="50" r="40" fill="red" />
</svg>
```
## Back to the Lab:

When crafting an XSS payload for testing purposes, it’s important to aim for payloads that can automatically trigger without requiring user interaction.

As shown in our Intruder results from earlier, we know we can use *‘animatetransform’* as an element in a \<svg> tag. But what attributes of *‘animatetransform’* are available to use that would not require user interaction? Back to Burp.

In the Burp Intruder tab, we need to change our search string again. This time, since we know *‘\<svg>’* will go through, change *‘\<§§>’* to *‘\<svg>’*. Then we need to add the *‘animatetransform’* element, the encoded version of the space character (%20), and our payload marker, *‘§§’*, set equal to 1.

```
<!-- Change GET request from: -->
GET /?search=<§§> HTTP/1.1
<!-- To the following: -->
GET /?search=<svg><animateTransform%20§§=1> HTTP/1.1
```
Click on *‘Payloads’*.

Head back over to your [XSS Cheat Sheet](https://portswigger.net/web-security/cross-site-scripting/cheat-sheet). This time copy all the events to your clipboard.

In Burp Intruder, click *‘Clear’*, then *‘Paste’* all of the newly copied events.

Click the orange *‘Start Attack’* button.

The attribute *‘onbegin’* of the element *‘animatetransform’* is getting a 200 response meaning it will go through.

So adding *‘onbegin’* with our *‘alert(1)’* function to the payload will look like the following:

`<svg><animateTransform onbegin='alert(1)'>`
Now that we have our payload, paste it into the search bar on our blog page and click *‘Search’*. We should see our pop-up alert window.

Congratulations! You solved another one! Keep up the great work!
