# PortSwigger Lab

- **Source URL:** https://medium.com/@arhamhaiderr99999/portswigger-lab-unprotected-admin-functionality-solution-6fc091c14c1b
- **Fetched from:** https://medium.com/@arhamhaiderr99999/portswigger-lab-unprotected-admin-functionality-solution-6fc091c14c1b?source=rss-0451664b60f0------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14885 (id 14885)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** Arham Hyder Bhatti / Thu, 27 Aug 2026 18:43:15 GMT

Before diving directly into the lab, let’s first understand the basics of **Access Control**.

**Access control** determines **who is allowed to access something or perform an action** in an application.

For example, on a university website, a student can view their grades, while an administrator can add or delete student accounts.

Access control works together with:

When access control is poorly implemented, users may be able to access things they shouldn’t.

**Vertical privilege escalation** happens when a user gains access to functionality meant for a user with higher privileges.

For example, if a normal user can access an **admin panel** and delete other users, that would be vertical privilege escalation.

In simple words:

***A low-privileged user gains access to higher-privileged functionality.***

One common cause of vertical privilege escalation is **unprotected functionality**.

For example, a website may have an admin page that isn’t visible to normal users. However, if the application doesn’t properly check permissions, a normal user might still be able to access the page directly.

This leads to an important security lesson:

***Hiding an admin link is not access control.***

The application must actually check the user’s permissions before allowing access.

Attackers may discover hidden functionality through places such as robots.txt, predictable URLs, or common paths.

Now that we understand the basics of **Access Control** and **Vertical Privilege Escalation**, let’s put them into practice.

The lab we’ll be solving is:

**Lab: Unprotected admin functionality**

The lab contains an unprotected admin panel. Our objective is to **delete the user carlos**.

First, access the lab. You’ll be taken to a dummy shopping website that looks like this:

At first glance, everything looks normal. There is no obvious admin panel available to us.

So, let’s see if we can find anything interesting.

Instead of randomly guessing admin URLs, let’s check the website’s robots.txt file.

Add: robots.txtto the end of the website’s address and press **Enter**.

A new page will open.

Look through the contents of the page.

We can see a **Disallow** entry pointing to an administrator panel.

Copy that administrator path.

Now remove robots.txt from the address and replace it with the administrator path we found in the previous step.

Press **Enter**.

You should now be taken to the **administrator panel**.

The admin panel gives us two options: deleting **carlos** or **wiener**.

Our objective specifically tells us to delete carlos.

Click the **Delete** option next to carlos.

And that’s it!

🎉 **Congratulations! You have successfully solved the lab.**

We found the hidden administrator functionality and used it to delete the required user.

Poor Carlos didn’t stand a chance. 😭

This lab demonstrates how **unprotected functionality** can lead to **vertical privilege escalation**.

The administrator panel was accessible without properly checking whether the current user had administrator privileges.

The robots.txt file also gave us a clue about where the administrator functionality was located.

The key takeaway is:

***Sensitive functionality should never rely on being hidden. It must be protected with proper server-side authorization checks.***

This was a simple but useful introduction to **Broken Access Control** and **Vertical Privilege Escalation**.

We discovered an administrator panel, accessed functionality that should have been restricted to administrators, and deleted the required user to complete the lab.

If you found this walkthrough helpful, make sure to follow me for more **PortSwigger Web Security Academy lab solutions**, cybersecurity content, and hands-on web security learning.

**Signing off. 👋**
