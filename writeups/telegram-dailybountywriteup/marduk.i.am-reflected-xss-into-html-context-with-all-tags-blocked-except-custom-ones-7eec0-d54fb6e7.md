# Reflected XSS into HTML context with all tags blocked except custom ones

- **Source URL:** https://medium.com/@marduk.i.am/reflected-xss-into-html-context-with-all-tags-blocked-except-custom-ones-7eec0b6b146f?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250221153851/https://medium.com/@marduk.i.am/reflected-xss-into-html-context-with-all-tags-blocked-except-custom-ones-7eec0b6b146f
- **Fetched:** 2026-11-24
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/5112 (id 5112)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Reflected XSS into HTML context with all tags blocked except custom ones

Lab description: This lab blocks all HTML tags except custom ones. To solve the lab, perform a cross-site scripting attack that injects a custom tag and automatically alerts *‘document.cookie’*.

In our previous lab, [*Reflected XSS into HTML context with most tags and attributes blocked*](/@marduk.i.am/reflected-xss-into-html-context-with-most-tags-and-attributes-blocked-4266c6c473ad), we learned how to use Burp Intruder to help discover all the tags we could use to bypass the site’s web application firewall (WAF).

This lab is similar to the previous one in that, if the title of the lab had not told us, we could use Burp Intruder to find what tags we can use to bypass the WAF.

However, we already know that we are going to have to use custom tags in order to solve this lab, so I will not be going into using Burp this time.

## Custom Tags

Unlike standard HTML tags that are part of the HTML specification, custom tags are unique to a particular project or website. Developers can use them to make their code more readable and maintainable.

```
<!-- Examples -->
<my-custom-tag></my-custom-tag>
<video-player src="xyz.mp4">My Video</video-player>
```
In general, use lower case and a hyphen, along with standard HTML naming practices, when naming your custom tag and you will be good.

For a more in depth look at custom tags check out this article by Matthew James Taylor: ‘*Custom HTML Tags (18 Things To Know Before Using Them)’.*

## Lab Solution

Access the lab and you’ll be brought to the simple blog page. In the search bar create your own custom tag and click *‘Search’*.

```
<!-- I used -->
<my-tag>
```
Notice the ‘Go to exploit server’ button. We will use that in a minute.

Even though nothing is returned to the page here, we still received a response from the server, so it worked.

Let’s check the DOM to see what’s happening. Right click on the (‘’) and select *‘Inspect’* from the drop-down menu.

Now if we can add attributes to our tag, we can get our *‘alert(document.cookie)’* to pop-up.

Here is what we are going to use and then I will explain each part:

`<my-tag onfocus='alert(document.cookie)' id='x' tabindex='1'>`
- *onfocus* — Event that is triggered when an element becomes the active element in the document, meaning it is selected for interaction. This can occur through various user actions, such as clicking on the element with the mouse, tabbing to the element using the keyboard, or tapping on the element on touch-enabled devices.
- *alert(document.cookie)* — This code triggers an alert dialog displaying the value of the document’s cookie.
- *id=’x’* — The id attribute uniquely identifies an element within the document, which can be useful for targeting the element with CSS or JavaScript.
- *tabindex=’1'* — This attribute specifies the order in which elements receive focus when navigating the page using the keyboard’s Tab key.

Now that we have our payload, let’s enter it into the search bar and press ‘Search’.

It went through! If you click between the single quotes on the page you’ll trigger the pop-up.

Click ‘OK’, then right click between the single quotes and select ‘Inspect’ from the drop-down menu.

This does not solve the lab though. What we have done is, create a URL we can send to our ‘victim’, with the addition of two more characters: ‘#’ and ‘x’.

At the end of your lab’s URL, add ‘#x’, so it will look like the following:

```
// Replace 'YOUR-LAB-ID' with your lab id from your URL 
https://YOUR-LAB-ID.web-security-academy.net/?search=<my-tag+onfocus%3D'alert(document.cookie)'+id%3D'x'+tabindex%3D'1'>#x
```
Adding ‘#x’ to the end of your URL is telling the browser to open this page, then immediately ‘tab’ to ‘id=x’. And this will trigger our pop-up.

Copy your URL and click on *‘Go to exploit server’* I mentioned earlier.

In the ‘Body’ section of the exploit server, we are going to need and opening and closing \<script> tags. In between the \<script> is where you will put your URL. The ‘Body’ section should look like:


<script>

location = 'https://YOUR-LAB-ID.web-security-academy.net/?search=%3Cmy-tag+onfocus%3D%27alert(document.cookie)%27+id%3D%27x%27+tabindex%3D%271%27%3E#x'

</script>
Then click ‘Deliver exploit to victim’.

Congratulations!

Keep up the good work! See you next time!

## More Information on Custom Tags:

[https://www.w3schools.com/htmL/html5\_syntax.asp](https://www.w3schools.com/htmL/html5_syntax.asp)

Reference Article by Matthew James Taylor: [Custom HTML Tags (18 Things To Know Before Using Them)](https://matthewjamestaylor.com/custom-tags)
