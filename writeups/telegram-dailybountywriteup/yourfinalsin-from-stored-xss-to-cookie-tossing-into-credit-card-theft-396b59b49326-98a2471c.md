# From Stored XSS to Cookie Tossing into Credit Card Theft

- **Source URL:** https://medium.com/@YourFinalSin/from-stored-xss-to-cookie-tossing-into-credit-card-theft-396b59b49326?source=rss------bug_bounty-5
- **Fetched from:** https://medium.com/feed/@YourFinalSin
- **Fetched:** 2026-11-16
- **Channel:** @dailybountywriteup
- **Telegram message:**  (id 13071)
- **Method:** medium-rss-content readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
Hello Everyone, we are back again!

A couple of months ago, I discovered a pretty interesting client-side vulnerability chain on a large SaaS platform, a public program on HackerOne.

This issue was marked as informative and when I requested disclosure, it was denied (what a coincidence).

So, I will have to redact all identifying details and simply refer to the platform as **company.com**.

### Quick Explanation on How the Platform Operated

Before getting into the actual chain, there is one important thing to understand about how this platform worked.

Different users could have different instances, but uploaded SVG files were still served from the same shared asset subdomain, just on different paths. So the attacker could have their own instance, the victim could have a different one, and the attacker could simply send the victim a link to the malicious SVG hosted on something.company.com.

Once the victim opened that SVG, the JavaScript executed on the shared asset domain and started the chain described below. So, the attacker would basically prepare everything on the attacker instance and then send the victim the malicious link.

### Initial Discovery

While playing around with the admin panel and exploring different features, I eventually landed on some functionality that allowed comments, where users were also able to upload files.

So I tried uploading a SVG file containing a simple alert() payload and it actually uploaded successfully.

After the upload I opened the malicious SVG file and got the alert() popup, confirming the stored XSS.

The problem here was now that the JavaScript executed on the domain ***something.company.com***, but the juicy data was on ***admin.company.com***.

### Thinking About Impact and Building the Chain — Cookie Tossing!

Since the execution happened on a sibling domain, the obvious first thought was:

**Can I somehow influence the main admin session?**

So I started looking into cookie scoping and noticed that authentication cookies were scoped broadly enough to .company.com.

This instantly opened the door for **Cookie tossing.** If you don’t know what Cookie tossing is, you can read up here [Cookie Tossing | Application Security Cheat Sheet](https://0xn3va.gitbook.io/cheat-sheets/web-application/cookie-security/cookie-tossing)

After looking around the admin panel for a bit, I found that one of the most valuable targets there would be the provided credit card information, which an admin could enter on the billing page.

At this point the chain was pretty clear:

**Step 1 ->** Trigger the stored XSS on the sibling domain

**Step 2 ->** Create cookie jar pressure with junk cookies

**Step 3 ->** Inject attacker-controlled session cookies

**Step 4 ->** Scope those attacker cookies only to the billing route

**Step 5 ->** Send the victim to the billing page

What made this interesting was that I did not need to override the whole admin session, I only needed to affect the billing flow.

A cookie can be limited to a specific route by using the Path attribute. For example:

document.cookie = "session\_id=ATTACKER\_SESSION; path=/instance/attacker/settings/billing; domain=.company.com; Secure; SameSite=None";

That means the browser will only send this cookie on requests matching: instance/attacker/settings/billing

Therefore, I only set the attacker cookies for the **billing path,** because that’s where the credit card data is provided. That means from the victim’s perspective, everything still looked legitimate, but any payment method entered there would actually be saved into the attacker-controlled instance.

But once the admin opened the billing page, the browser would send the attacker-controlled cookies for that route, so the billing page would resolve in the attacker’s instance context instead.

### Some Snippets

To Overflow the cookie jar, you can use a simple for loop, like

```
for (let i = 500; i--;) {
  document.cookie = `overflow${i}=${i}; path=/; domain=.company.com; Secure`;
}
```
The goal here was not to wipe out the whole session completely, but to create cookie pressure so that broadly scoped cookies would no longer be relied on in the same way.

Then I set the attacker cookies only for the billing path:

document.cookie = "koa.sid=ATTACKER\_VALUE; path=/instance/attacker/settings/billing; domain=.company.com; Secure; SameSite=None";

document.cookie = "koa.sid.sig=ATTACKER\_SIG; path=/instance/attacker/settings/billing; domain=.company.com; Secure; SameSite=None";

That means the browser would only send these cookies on requests to: instance/attacker/settings/billing

So, I did not need to hijack the entire application session, I only needed to affect the exact billing route.

Finally, I embedded a lure inside the SVG (SVGs can include and display valid HTML as well), which is served on the trusted sibling domain something.company.com:

\<a href="https://admin.company.com/instance/attacker/settings/billing" target="\_blank">

Add new Payment Method

\</a>

Once the admin opened that page, the billing flow resolved in the attacker’s instance context.

### Here a Final Summary

To summarize the full attack flow, the attacker first uploads a malicious SVG file inside their own instance. That file is then served from the shared asset subdomain something.company.com, which allows the attacker to simply send the victim administrator a link to it.

Once the victim opens the SVG, the stored XSS is triggered on the shared asset domain and the JavaScript starts the cookie tossing chain by creating cookie jar pressure and planting attacker-controlled cookies for the billing route.

The SVG then displays a fake **“Add new Payment Method”** button on the trusted sibling domain something.company.com. When the victim clicks it, they are sent to the billing page of the attacker’s instance. Because the attacker-controlled cookies are scoped to that route, the billing page resolves in the attacker-controlled context.

The victim then enters credit card information believing they are still inside their own instance, but the payment method is actually saved in the attacker’s instance instead.

So from the victim’s perspective everything still looked normal, but the final billing action happened in the attacker-controlled instance.

This report was marked as ***informational,*** when asked for a reason, they just said ***“due to policy change”.***

After requesting disclosure, they denied it:

Thank you for reading.

**If you want to follow along on X**, you can do so here: [3NVZ (@YourFinalSin) / X](https://x.com/YourFinalSin)

**If you want to support me**, you can do so here: [buymeacoffee.com/3NVZ](https://buymeacoffee.com/3nvz)
