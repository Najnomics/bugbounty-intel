# DOM XSS in jQuery selector sink using a hashchange event

- **Source URL:** https://medium.com/@marduk.i.am/dom-xss-in-jquery-selector-sink-using-a-hashchange-event-bb3c355b3633?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20240105164306/https://medium.com/@marduk.i.am/dom-xss-in-jquery-selector-sink-using-a-hashchange-event-bb3c355b3633?source=rss------bug_bounty-5
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/4819 (id 4819)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# DOM XSS in jQuery selector sink using a hashchange event

--

This is going to be PortSwigger Web Security Academy’s forth lab exploring Document Object Model-based Cross-site Scripting or DOM-based XSS. This time we will be introducing the concept of a hashchange event. A hashchange event is an event triggered in JavaScript when the URL’s hash has changed (i.e. domain.com/page1#foo to domain.com/page1#bar). This lab is going to be a little more involved, but I will try to keep this as easy to follow as I can. Let’s get into it!

[Lab description:](https://web.archive.org/web/20240105164306/https://portswigger.net/web-security/cross-site-scripting/dom-based/lab-jquery-selector-hash-change-event) This lab contains a DOM-based cross-site scripting vulnerability on the home page. It uses jQuery’s *$()* selector function to auto-scroll to a given post, whose title is passed via the *location.hash* property. To solve the lab, deliver an exploit to the victim that calls the *print()* function in their browser.

**NOTE:** If you are just looking to solve the lab jump down to the bottom. Look for “SOLUTION”. Solving the lab is very easy and quick. If you want to know how it works, keep reading.

First, access the lab. You’ll be brought to our simple blog page again. From the description we know the vulnerability is somewhere on the home page, but our home page doesn’t give us a lot of options. We need to see what’s happening in the page source.

Right click anywhere on the page and select View Page Source. If you scroll down to the bottom you will find the following script:

```
<script>
    $(window).on('hashchange', function(){
        var post = $('section.blog-list h2:contains(' + decodeURIComponent(window.location.hash.slice(1)) + ')');
        if (post) post.get(0).scrollIntoView();
    });
</script>
```
There is our “location.hash”, from the lab description, but what is the script doing? It is jQuery. We know that from the jQuery selector, “$()”, beginning. Let’s break it down.

- **$(window)** — jQuery selector is selecting that window.
- **.on(‘hashchange’, function(){** — If there is a ‘hashchange’ event it going to create a function. Basically, in the site’s URL, it’s looking for anything after the hashtag (#). If there is one.
- **var post =** — Defining a variable that will be equal to the following:
- **$(‘section.blog-list h2:contains(** — Is looking for a \<h2> element within a \<section> that has a class equal to “blog-list” that contains the following:
- **‘ + decodeURIComponent(window.location.hash.slice(1)) + ‘)’);** — If the site’s URI contains a # then take the string after the # and assign it to the variable “post”.
- **if (post) post.get(0).scrollIntoView();** — This checks if the variable “post” has a value (if the matching element was found). If true, it scrolls the first matching element into view.

So, this script looks to see if there is any change to the URL after the hash. If so, it assigns that change to the variable “post”, then searches the page’s “blog-list” section for an \<h2> element that contains a match. If it finds a match it then will scroll to that part of the page.

Now, if you look at the current URL of the target site, there is no hash (#). We have to add our own. Scroll down and pick a unique word from one of the blog titles and add it to the end of the URL following a forward slash and a hash. You can use multiple words from the title, just remember to add single quotes around them. The blog page has random blogs each time, choose whichever blog title you like. Your new URL should look like the following: *web-security-academy.net/#Chosen\_blog\_title*

The page should jump to the blog title you chose. This is the way the hashchange function should work. Like a search function. The jQuery document states that this argument needs to be a string.

Let’s open our developer tools to see what the page is doing. Right-click anywhere on the blog page and select Inspect from the drop-down menu. In your dev tools window, select the Console tab.

In the console we are first going to see how this script is **supposed** to work. Below, change “*Chosen\_blog\_title*” to your blog title choice and copy this part of the script. Paste it to your console.

`$('section.blog-list h2:contains(Chosen_blog_title)');`
You should get a jQuery object returned with a length property of 1. Meaning, yes, there was one match. If we assign it to the variable “post”, we can then call the .get() method to expose the DOM element.

First, assign the jQuery selector to the variable “post” then call .get() with index of 0:

```
var post = $('section.blog-list h2:contains(Chosen_blog_title)');
post.get(0);
```
You can now see the exposed DOM element. This is the way it should be. We *know* that this DOM element exists, *and* we used a string for the hashchange event in the URL.

But what happens if we “search” for something we know is not going to be there? Let’s find out.

I’m going to remove the “ee” from my argument “(Volunteering)”, because we know that there is not supposed to be a blog title containing the string “Voluntring”. See what happens?

```
//Create variable
var post = $('section.blog-list h2:contains(Voluntring)');
//Look at post
post;
//Checking to see if post exists
if (post) {console.log('true');}
```
An object was still returned. It says “Length: 0”, but it is still there. Why? It is not supposed to be there. This, in part, is the vulnerability. As it is now, it will only return an error. Not too serious. However, what if we use the contains method and introduce tags to our string? This will turn out to be the other part of the vulnerability.

We’re going to do the same thing, but adding \<h1> tags to the argument.

Add these lines, one at a time, to your dev console. Just replace *Your\_Random\_String* with whatever you like:

```
//Create variable
var post = $('section.blog-list h2:contains(<h1>Your_Random_String</h1>)');
//Look at post
post;
//Call .get() method
post.get(0);
```
It actually returned a match! But how? We know there is no \<h1> element on the page that contains our text. The object says it has a “Length: 1” so we can call the .get() method, with index of 0, to expose the DOM element.

We created a DOM element! The \<h1> element even contains our text. Within the argument of the contain method you should only be able to use a string, This contains method is allowing us to create a \<h1> element using tags.

Our \<h1> DOM element is not visible on the page because it is not attached to anything yet. As you can see above, it’s “*parentElement*” is null. In order to make our \<h1> element visible on the page, we need to attach the *child* to a “*parentElement*”.

For this open up the page source again. Find a \<div> where you want to attach your \<h1> element. I’m choosing the first one I see, \<div id=”academyLabHeader”>.

Once you have the “div id” you are going to use, we need to do a few things:

- Reassign “post” to our DOM element “post.get(0)”.
- Create a parent node. *document.getElementById()* is vanilla JavaScript. As you type in your dev console or code editor choices will pop up to help guide you. We are going to add our “div id” as the argument for the *getElementById() method.*
- Assign our variable “post”, as a child, to our node using the *appendChild()* method.

```
//Reassigning post variable
post = post.get(0);
//Create variable mynode using vanilla JavaScript
var mynode = document.getElementById('academyLabHeader');
//Look at node
mynode;
//Append post to node
mynode.appendChild(post);
```
Our text is now visible! Needless to say, we should not be able to do this!

So what about tags that require a source. Meaning they need to reach out to another server to retrieve the information. Like an image tag. Here is where we actually start to solve the lab.

Now, lets go back to our original selector function $(). Remember, “Chosen\_blog\_title” comes from the URL:

```
//Original
$('section.blog-list h2:contains(Chosen_blog_title)');
//Chosen_blog_title comes from the URL
YOUR_LAB_SESSION.web-security-academy.net/#Chosen_blog_title
```
If we can insert an \<img> tag inside the contains method we can get an alert to pop-up on the page. Let’s try, but we are going to add our payload to the URL directly. The ending or your URL should look like:

```
//Add /#PAYLOAD to the end
YOUR_LAB_SESSION.web-security-academy.net/#<img src="0" onerror="alert()">
```
Here, we insert our image tag with a source of 0. That, we know, will cause an error. Then on error, our alert will pop-up. With your payload at the end of the URL, hit Enter.

This does not solve the lab though.

**SOLUTION:**

On the [lab description](https://web.archive.org/web/20240105164306/https://portswigger.net/web-security/cross-site-scripting/dom-based/lab-jquery-selector-hash-change-event) page, open the solution tab. It tells us to open the exploit server (see above, red arrow). Go to the exploit server. Scroll down and replace “Hello, world!” with the payload from the solutions tab. Do not forget to change “`YOUR-LAB-ID`” in the payload.

`<iframe src="https://YOUR-LAB-ID.web-security-academy.net/#" onload="this.src+='<img src=x onerror=print()>'"></iframe>`
Click “View Exploit”

It worked! The *print()* function in the payload triggered the print pop-up.

All that is left to do is “Deliver exploit to victim”. Return back to the exploit server and click “Deliver exploit to victim”.

Congratulations! You have solved the lab!

**Up Next:**

[Reflected XSS into attribute with angle brackets HTML-encoded](https://web.archive.org/web/20240105164306/https://medium.com/@marduk.i.am/reflected-xss-into-attribute-with-angle-brackets-html-encoded-986d943b3fd2)

**Previous Labs:**

[DOM XSS in jQuery anchor href attribute sink using location.search source](https://web.archive.org/web/20240105164306/https://medium.com/@marduk.i.am/dom-xss-in-jquery-anchor-href-attribute-sink-using-location-search-source-b1000b4b16b3)

[DOM XSS in innerHTML sink using source location.search](https://web.archive.org/web/20240105164306/https://medium.com/@marduk.i.am/dom-xss-in-innerhtml-sink-using-source-location-search-a3ac4546ca5c)

[DOM XSS in document.write sink using source location.search](https://web.archive.org/web/20240105164306/https://medium.com/@marduk.i.am/dom-xss-in-document-write-sink-using-source-location-search-ae458bc5c85f)

**Helpful Links:**

[z3nsh3ll](https://web.archive.org/web/20240105164306/https://www.youtube.com/watch?v=5OiWO5Qr-iI) — This guy is great. Walkthroughs are very detailed.
