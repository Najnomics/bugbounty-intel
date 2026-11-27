# How I got a Zero-Click Account Takeover Bounty — Using Nothing But Logic

- **Source URL:** https://itsahmedatef.medium.com/how-i-got-a-zero-click-account-takeover-bounty-using-nothing-but-logic-11a3ae151376?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250418211411/https://itsahmedatef.medium.com/how-i-got-a-zero-click-account-takeover-bounty-using-nothing-but-logic-11a3ae151376
- **Fetched:** 2026-11-27
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/9391 (id 9391)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# How I got a Zero-Click Account Takeover Bounty — Using Nothing But Logic

Hey everyone, I’m back! It’s been quite a while since my last publish, but I’m thrilled to return with something new and really interesting — applying my skills on real-world applications.

Today’s write-up is about how I discovered a **zero-click account takeover** vulnerability without using any tools — just the browser and some **logic**.

I got a message from my colabiration friend, [r00t](https://medium.com/u/e1463903e2df?source=post_page---user_mention--11a3ae151376---------------------------------------), informing me that he had discovered something interesting about a target he had been hunting on for a while. He passed me the details and i looked into it to further investigate.

The target business is based on creating **profiles**, also known as **entries**, allowing users to publish their works, locations, and restaurants to share their products and receive bookings.

On the viewing profile page, you can see the profile’s work and products, and you have options to book, like, or review something. Additionally, there is a button labeled “**Edit Entry**” allows you to manage the profile if you are it’s owner. However, in my case, I got:

So, I created another entry — let’s call it “**Victim’s profile**”.

and i clicked on the “**Click here**” button to attempt taking ownership of the profile and test how far i can get.

I was redirected to another page that asked me to “**email the owner of the profile with a code**” in order to claim ownership access and edit this entry.

I choosed to send the code over the email, and here we come to the interesting part… the Validating **OTP** endpoint is something like this:

`/claiming/{{profile_id}}/verified_claims/{{uuid}}`
Apparently, we (the attacker) will not have **access** to the victim’s email to retrieve the **OTP**. The code is valid for only **5 minutes**, and there are only **3 attempts** to type the correct **OTP code**.

Since the created **UUID** is not something you can guess, and there’s no email parameter you can modify or test for **parameter pollution** or similar attacks. What came to mind was to try sending an **OTP code** to my own profile page (the attacker profile), I tried to use the same code to verify the victim’s profile, but it didn’t work. (The code somehow programmatically verifies whether it is **associated** with this specific endpoint.)

I tried this idea again, but just changed the **UUID** in the url with mine, hoping that the programming code would check whether the **OTP associated with this UUID** exists in the database or not, **regardless** if it’s linked to a specific profile or not — and **bingoooo**, I was right!

# Here is the detailed technical breakdown of the exploit:

I sent an OTP to my profile page, and the server generated a **UUID** linked to that **OTP** and saved them in the **database**, fogetting to check the relation between the **profile id**:

`/claiming/{{my_profile_id}}/verified_claims/{{uuid_created_for_me}}`
I kept this **UUID** and changed the **profile id**:

`/claiming/{{victim_profile_id}}/verified_claims/{{uuid_created_for_me}}`
Then i entered my **OTP code** and it was valid with that **UUID**… and i got access to whatever **profile id** i type in the URL!

# The Impact:

I got ownership and full access to the panel, allowing me to manage this profile entirely. I could control any profile to add photos, update contact information, view customer data, and more — posing a serious threat to the system and business operations of the website. This makes the vulnerability highly **critical**!

We got a nice bounty as a reward for this finding:

# Here’s an example of the vulnerable code:

This is a common mistake many developers make, the absence of verifying whether the **OTP** is actually associated with account or not, I imagine the **SQL query** might look something like this:

``SELECT * FROM `tokens` WHERE `OTP` = '<submitted_OTP>' AND `uuid` = '<uuid_in_the_url>'``
If this query returned data, it will give you access to the {{profile\_id}} in the url!

# Mitigation and fixes:

The table should include a field checking for the **profile\_id**, something like this:

``AND `profile_id`='<profile_id_in_the_url>'``
Not forget to mention to delete the used OTP after that to not use it more than once! Also make sure to review the following rules:

If OTP attempts fail ‘x’ times or succeed, delete the corresponding row from the database.

Is OTP expired? delete it too to clean the database from unnecessary data.


## Final words:

(Take a look at my friend’s profile [r00t](https://medium.com/u/e1463903e2df?source=post_page---user_mention--11a3ae151376---------------------------------------) , he provided detailed explanations of the reconnaissance process and how he discovered this endpoint.)

Don’t forget to reach out to me on LinkedIn! [/in/ItsAhmedAtef](https://www.linkedin.com/in/itsahmedatef/)

For more write-ups and technical articles, feel free to connect!
