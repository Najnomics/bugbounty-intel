# Privilege Escalation

- **Source URL:** https://medium.com/@HBlackGhost/privilege-escalation-member-role-can-change-organization-name-and-photo-702e00786a42?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20251103201638/https://medium.com/@HBlackGhost/privilege-escalation-member-role-can-change-organization-name-and-photo-702e00786a42
- **Fetched:** 2026-11-19
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/10958 (id 10958)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# **Privilege Escalation Allows Member to Change Organization Name and Photo**

لَقَدْ مَنَنَّا عَلَيْكَ مَرَّةً أُخْرَىٰٓ

الحمدلله الذيّ نظُن به خيراً فيُكرمنا بأفضل مِمّا ظننَّا به

One day, my friend **Ahmed Ghazy** and I were looking for a program to test.

We found one that uses role-based permissions — and yes, we love roles!

After disclosing the program and showing its features (OMG, every program wants you to upgrade to access all tabs), we decided to dive deeper and look for any bugs in the role functions.

I browsed the program with the **Owner** role. At this stage, we were still trying to understand the program, so let’s explain the roles we found:

- **Owner** → Has all permissions.
- **Admin** → Has all permissions except adding or removing owners or inviting them.
- **Member →** Can only view the organization and cannot change its configuration

Only the **Owner** and **Admin** roles have permission to modify this tab.

Wait what? Stop right there! Only the Owner and Admin should be able to modify organization data.

Okay, let’s test this with the **Member** role:

1. I logged in with the **Owner** account and changed the organization name, capturing the request.
2. I then modified this request and replaced the cookie with the **Member** account’s cookie.
3. Finally, I sent the request and checked the response

**This is the request used to modify the organization name**

ِI expected this wouldn’t be easy. After more time testing with Have Cup of Tea , While brainstorming ways to achieve a privilege escalation bug, we got an idea: change the request method from `PATCH` to `PUT`

Let’s see what happens.

Yea Bro That’s Great Finding

Here, I can modify the organization’s name without any permissions to do so.

My mind couldn’t stop there, so I decided to check this API endpoint to increase our impact.

Let’s test the API endpoint:

I tried to trigger any kind of error on this endpoint — and I succeeded.

The error message returned: **“Enter your organization name.”**

Okay, next I added the **name** key and searched in response for any other keys that might be useful.

After reviewing the response for this endpoint, I found the **jussy** key.

Let’s test this key in our request by providing an invalid value to see if we can return any information from this endpoint. 

Great Baby Greeeeeat , I received an error: **“This ID of photo is not valid.”**

This shows me that the key **logo\_media\_idMember** account cookie.

But where can I get this ID???

After reviewing the HTTP proxy history, I discovered an endpoint that uploads a photo and returns the photo’s ID in the response.

After using this endpoint to upload a photo and obtain its ID, I added that ID to our malicious request.

**Boooooom! I was able to change both the name and photo of the organization**

وابللللللع 🔥😎

**والسلام عليكم ورحمة الله وبركاته**
