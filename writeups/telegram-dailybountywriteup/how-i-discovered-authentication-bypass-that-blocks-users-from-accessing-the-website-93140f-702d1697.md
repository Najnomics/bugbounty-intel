# How I Discovered Authentication Bypass That Blocks Users from Accessing the Website ?

- **Source URL:** https://sayedv2.medium.com/how-i-discovered-authentication-bypass-that-blocks-users-from-accessing-the-website-93140fa180ac?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20240705193921/https://sayedv2.medium.com/how-i-discovered-authentication-bypass-that-blocks-users-from-accessing-the-website-93140fa180ac
- **Fetched:** 2026-11-27
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/6591 (id 6591)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# How I Discovered Authentication Bypass That Blocks Users from Accessing the Website ?

Hi amazing hackers ,

Today we gonna talk about authentication bypass vulnerability that i found in a public bug bounty program .

## Let’s start our story

I started hunting on the program and I spent about 3 days to understand it.

The program allows you to create an organization and invite users with different roles

now the organization contains :

**Owner → User 1**

**Admin → User 2**

**Member → User 3**

There is an option for the owner to create a new role so he created a new role called “Test” and gave it to user 3

User 2 (**Admin**) also can reach the role section but he cannot delete the roles .

So first thing came to my mind , what if i tried to delete the new role that the Owner gave to User 3 ??

Lets try ..

I went to the role section with User 2 and pressed on the new role and sent the request to repeater

So i tried to delete the role by replacing the GET with DELETE

but i couldn’t , because the system doesn’t allow to delete a role if a user still have it ..

I spent a lot of time trying to delete it , but i failed .

I saw in the response that the system allow using some different methods in the request

So I said what if i tried to send different method then use DELETE again??

lets try…

I tried all the methods but it didn’t work with me .

But , When I sent PATCH in the request i got information about the role in the response .

So lets try to delete it after the PATCH request.

lets use DELETE again and send the request ….

**BOOOOOM….**

I got ( 204 no content ) response and the role has been deleted…

Now lets see what happened to User 3 when i deleted his role ..

I went to user 3 account and refreshed the page and guess what ??

He can’t even access the website or anything again , he will get error page every time he tries to access the website

# **Timeline**

**27 Jun 2024** → **reported**

**2 July 2024 → awarded $$$**

**Follow me on:**
