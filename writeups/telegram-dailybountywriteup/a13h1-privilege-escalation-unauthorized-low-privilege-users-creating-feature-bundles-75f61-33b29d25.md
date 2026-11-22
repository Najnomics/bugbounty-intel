# Privilege Escalation

- **Source URL:** https://medium.com/@a13h1/privilege-escalation-unauthorized-low-privilege-users-creating-feature-bundles-75f6125eec78?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20231120060529/https://medium.com/@a13h1/privilege-escalation-unauthorized-low-privilege-users-creating-feature-bundles-75f6125eec78
- **Fetched:** 2026-11-22
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/4464 (id 4464)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Privilege Escalation: Unauthorized Low-Privilege Users Creating Feature Bundles

--

Discover how low-privilege users are able to create feature bundles in Examtegg (an Private Program), bypassing system security, and get paid 500$ in this exploration of an important vulnerability.

**Understanding Target and Feature:**


Examtegg (Virtual name of Private Program) is a platform that offers various services and features to help companies manage their applications more effectively. Among these features, there’s a critical one called “Feature Bundles.” Feature Bundles allow administrators and authorized personnel to group specific functionalities or components together, making it easier to manage user access to these features. It’s a useful tool for ensuring that the right people have access to the right functionalities within an application.

**The Vulnerability: Unauthorized Creation of Feature Bundles**


The security hiccup here is that users with low privileges, who shouldn’t be able to create these bundles, can do so. This means that unauthorized users can tinker with configurations they shouldn’t be allowed to, compromising security and risking the stability of the entire system.

## Steps to Reproduce:

To recreate this issue, you’ll need two accounts: one with administrative access and another with limited, low-level permissions. Here’s how the vulnerability is reproduced:

1. Begin with your low privilege user account on Frontegg. This is the one with restricted access, like having the keys to the office, but not the entire building.
2. Obtain the Authorization Bearer Token linked to this low privilege user account. Think of this as your key to that restricted office area.
3. Now, it’s time to use that key. Craft a POST request of /entitlements/resources/feature-bundles/v1 endpoint using the Authorization Bearer Token you’ve acquired.
4. That request looks like the below request :-

```
POST /entitlements/resources/feature-bundles/v1 HTTP/2 
Host: api.au.examtegg.com 
Content-Length: 103 
Authorization: Bearer [Your Authorization Bearer Token] 
Content-Type: application/json 
Accept: application/json, text/plain, */*  
{"name":"test122","assignOnSignup":false,"defaultTimeLimitation":null,"description":"","metadata":"{}"}
```
Now, you might be wondering how I managed to create that POST request. Well, I used an admin account initially to create a feature bundle. I captured the request generated during this process, and then I cleverly employed that same request from the low-level user account. It’s a bit like borrowing the keys from the admin and using them to open doors that should remain locked to you. This clever workaround reveals a significant security flaw.


5\. Send this request, and you’ll receive a response with a status code of 201 — Created.

6\. Switch to your admin account, the one with full access. Go to the feature bundle section. There, you’ll find the bundle you just created.

**Why It’s a Problem:**


- Unauthorized Creation of Feature Bundles: Users who shouldn’t have this power can now make feature bundles.
- The system’s security settings are being ignored, and that’s a problem.
- The administrators have to clean up the mess, and that’s more work.
- Unauthorized feature bundles might contain settings that are not safe, and that’s a risk.
- The platform loses its control, and that affects its overall security.

**The Bounty Reward:**


The Security Team recognized the importance of this find and rewarded me 500$ for it. That’s because it’s important to fix issues like this and keep everything safe.

**Takeaway**


The key takeaway from this scenario is to remember that sometimes you can access powerful features and perform actions meant for admins, even when you’re just a low-level user. Always explore and test various features, settings, and requests from your account to understand the full scope of your access and discover any hidden vulnerabilities.

*Leave some clap if you enjoyed this read, leave your feedback in comment and consider following me for more exciting findings.*


*Find me on Twitter: @a13h1\_*


# Thank you everyone

Keep Supporting, Keep Clapping, Keep Commenting.
