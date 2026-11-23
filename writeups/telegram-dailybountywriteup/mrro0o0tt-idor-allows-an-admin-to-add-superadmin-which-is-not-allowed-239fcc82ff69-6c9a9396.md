# IDOR Allows an Admin to Add SuperAdmin (Which is not allowed)

- **Source URL:** https://medium.com/@mrro0o0tt/idor-allows-an-admin-to-add-superadmin-which-is-not-allowed-239fcc82ff69?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250914141202/https://medium.com/@mrro0o0tt/idor-allows-an-admin-to-add-superadmin-which-is-not-allowed-239fcc82ff69
- **Fetched:** 2026-11-23
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/7993 (id 7993)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# IDOR Allows an Admin to Add SuperAdmin (Which is not allowed)

Hello Hackers,

Already you assumed what I want to share with you guys! Of course my Title gave you the basic idea! Write-ups could be boring…..

Let’s Jump into the real game. I was working on an app, let’s call it hackme.com

My Last research was based on XSSRat’s Methodology & some other manual hunters' methodology too! Who is specially looking for bugs rather recon? 

I also spend less time on recon! But trust me recon is really fun. Even I really enjoy Recon, but the problem is Recon takes a lot of time. In return, it doesn’t generate money for me. Instead when I directly Jump into hacking, I got results. Got paid, that is my GOAL. SO now-a-days I always start by looking for various kind of bugs.

But now I only want to focus on like what I can not do, I mean What the application allows me to do, and what are not permitted/authorized or something like that! AS a hacker it is really fun when you break or bypass something! 

So to break the rule or act the unintended thing/behavior I was digging around the app. And figuring out what unusual I can perform!

Then I find manage staff functions, there I can add staff with total 5 role. 

the highest one was admin role.

Please note, I was doing this stuffs from SuperAdmin role! Then I simply add a admin as a normal user.

Then hacker inside me raise a question to me, “hey Why you don’t try to add another SuperAdmin?” Oh! Shit!! Thanks mate! Let me try!

When I logged in as a admin! There I get almost everything that SuperAdmin has except some features! Like, an Admin can not see other staffs on that Orgainzation. So Admin can not manage other staff’s account, roles etc.

So, There only One thing Admin can do that is to add staffs! So when adding staffs I see a ID on the request. When I see IDs hacker immediately rise up inside me! I change that value to role\_id=5 to role\_id=4 BOOM! It worked! 

I was able to add SuperAdmin! Because SuperAdmin ID was 4 It was totally assumption as Admin’s ID is 4 okay?

So that’s it! I added super admin! That is totally out of logic of this application!! No plan offer this features to add multiple Super Admins!

Only Hackers can do it! So must report it right?

**But Impact?**

NEW SuperAdmin can change any staff’s Password! As this is Superadmin’s Feature.

Good Night!
