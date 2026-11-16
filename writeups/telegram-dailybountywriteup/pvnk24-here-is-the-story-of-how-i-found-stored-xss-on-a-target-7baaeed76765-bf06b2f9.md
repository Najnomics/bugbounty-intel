# Here is the story of how i found Stored XSS on a target

- **Source URL:** https://medium.com/@pvnk24/here-is-the-story-of-how-i-found-stored-xss-on-a-target-7baaeed76765?source=rss------bug_bounty-5
- **Fetched from:** https://medium.com/feed/@pvnk24
- **Fetched:** 2026-11-16
- **Channel:** @dailybountywriteup
- **Telegram message:**  (id 6684)
- **Method:** medium-rss-content readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
**What is XSS?**

Cross site scripting is vulnerability which Allows an attacker to execute the javascript inside the victim browser

It has 3 main types Reflected, Stored and DOM based. Now i don’t go through all of them.

**Common Scenarios to find XSS:**

When user input is getting reflected back in to the response there you can look for XSS by submitting.

**Here is the story of how i was able to find Stored XSS on an application**

When I was testing on a target, I worked with a subdomain of it, let’s say demo.target.com. It has a lot of functionalities, but I decided to start testing module by module. I began with the team management module.

In this module, you can create and manage teams. My initial goal was to test for XSS by entering a simple payload like test\<h1>hi\</h1>, which is a basic payload to test for XSS. When I entered this and clicked submit, the tags were removed. Here is the chance of getting XSS when we have this kind of filters we can bypass them.

so I started investigating what caused this behavior. I entered the payload test\<h1 and it was saved as it is. However, when I entered test\<h1>, the tags were replaced. I then tested with test\<h1\<h1>>, and the inner \<h1> was removed, but the remaining text was encoded.

The module also has an edit option. After experimenting with it, I observed that having quotes in my payload was breaking the text box value attribute. This presented an opportunity to trigger XSS. After a few minutes, I prepared my payload, something like test"onclick='alert(1)'.

When I saved the team name with this payload, it stored successfully. When someone from the team tried to change the team name, the stored XSS was triggered, successfully executing the attack on the target.

Conclussion:

I was able to find this vulnerability by testing small modules individually. I also tested for other potential vulnerabilities in this module, such as IDOR (Insecure Direct Object References) across different teams.

#### Thanks for reading. Hope you learned something new. Here is my X(twitter) [**link**](https://x.com/pavank_24)
