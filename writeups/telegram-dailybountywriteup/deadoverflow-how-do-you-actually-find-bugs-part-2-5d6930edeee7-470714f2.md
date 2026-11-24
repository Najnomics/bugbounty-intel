# XSS is hard to find… or is it? (How to you find bugs)

- **Source URL:** https://medium.com/@deadoverflow/how-do-you-actually-find-bugs-part-2-5d6930edeee7?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20251124181142/https://medium.com/@deadoverflow/how-do-you-actually-find-bugs-part-2-5d6930edeee7
- **Fetched:** 2026-11-24
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/5129 (id 5129)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# XSS is hard to find… or is it? (How do you find bugs)

In the last blog post I explained how do you find CSRF and today I will be explaining how to find XSS.

Firstly I want to thank everyone for all the support! It really means a lot and I am sorry if I cannot answer your messages. I get a lot of them daily and I try my best to answer all of them.

**Instagram**: [@deadoverflow](https://instagram.com/deadoverflow)

I already made a video on YouTube about this and further explaining how to find XSS. You can find it in the link below and it would mean a lot if you would subscribe since I am planning on giving my book for free. I am planning also to upload a lot of educative hacking related content on that channel!

Youtube XSS video: [https://youtu.be/tqSK50xo9yE?si=0yVngoL53LTWPesM](https://youtu.be/tXWoRK7JiHk)

In case you want to read, here is the blog post for you, enjoy!

**XSS — (Cross Site Request)**

This is another vulnerability that I struggled to find even after finding my first few bugs. It was just not happening. I really tried hard to find it and then I developed a really good strategy on finding XSS.

Be aware that websites sometimes implement a really good protection against XSS and it could be difficult to find it. Just look for it everywhere.

Again, I will be showing this on an actual target and showcasing and actual vulnerability I found and reported.

XSS is a little bit trickier to find however, I still am relying on Chrome Developer Tools.

As for any other bug, you have to rely on your logic mostly because you will experience a lot of different websites that could be exploitable. My advice, or how I approach this, is by pasting this **\<>/’”\<img>** in input fields or somewhere where I want to test just to see how the website would respond.

So I will try and enter this in a password field for my router.

Button “Click here to display” is responsible for displaying the currently entered password.

Let me paste now what I usually do in this input field.

After I pasted it, I will click the button to display the password and monitor what is happening.

It opens a new window and in there it displays the password. However I entered this **\<>/’”\<img>** and I can see that the **\<img>** is missing. I will open Developer tools on this window to see what happened.

As you can see in the elements tab, there is the **\<img>** element parsed as HTML. Now I will try my exploit: **\<img src=x onerror=alert(1)>**

Once I paste this in the password field I will press the button again and this happens:

And just like that, there is reflected XSS on this router’s web interface.

However not always It will be this easy, sometimes you need to be creative.

For example, I wrote a write up about this a while ago you can find it here:

As you can see in the image below, the router’s web interface was encoding this symbol ‘ so it prevents attackers from executing code on 192.168.1.1 by just setting a wifi name to be something malicious.

But even tho this symbol ‘ was encoded, \<> these weren’t.

So I changed the name of the wifi to: **\</script>\<script>alert(1);//**

After I connected to my network and visited the router’s web interface I was greeted with this:

To actually see what happened, here is the source code of the page:

My exploit closed the existing script tag, and opened a new one with my attack payload. This technique I learned from Portswigger so I highly recommend you check them out.

Thanks for making it all the way here!

Hopefully this briefly summarizes how I hunt for XSS vulnerabilities and hopefully you will learn something from this. If you have any questions, you can reach out to me via email [ihusanovic3@gmail.com](mailto:ihusanovic3@gmail.com) or on Instagram [@deadoverflow](https://instagram.com/deadoverflow)

I will try to be answering any questions you may have!
