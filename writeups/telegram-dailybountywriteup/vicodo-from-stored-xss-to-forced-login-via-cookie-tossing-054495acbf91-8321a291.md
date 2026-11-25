# From Stored XSS to Forced Login via Cookie Tossing

- **Source URL:** https://medium.com/@vicodo/from-stored-xss-to-forced-login-via-cookie-tossing-054495acbf91
- **Fetched from:** https://medium.com/@vicodo/from-stored-xss-to-forced-login-via-cookie-tossing-054495acbf91?source=rss-cf0c40b75f54------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:**  (id 14974)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** vicodo / Sat, 07 Nov 2026 17:16:51 GMT

Hi, I’m Vicodo, a security researcher and part-time bug bounty hunter. In this post, I’ll share how I discovered a stored XSS vulnerability and what I learned while investigating its impact. lets get into it🧀

\### Finding the Stored XSS

While exploring the app.target.com, the profile picture upload feature immediately caught my attention. File upload forms are notorious for security quirks, so I asked myself: \*”Why not try an SVG?”\* I crafted an SVG payload and triggered the upload while intercepting the traffic in Burp Suite. Interestingly, the application was offloading file uploads directly to \*\*Amazon S3\*\* using presigned URLs.

After uploading the file, I noticed the server blindly accepted it without sanitizing the content or checking the \`Content-Type\`. Nice! 

The file was hosted on \`public.cdn.target.com\`. 

When I opened the image, it downloaded directly instead of rendering.

So I checked the file upload response in Burp Suite and noticed this header:

**\`Content-Disposition: attachment\`**

I intercepted the response, changed it to:

**\`Content-Disposition: inline\`** 

And forwarded it. 

When I opened the image again, the browser finally rendered the SVG and executed the payload!

\### Gadget Chain

Finding a Stored XSS on a CDN is cool, but a simple alert box doesn’t give you a real impact by itself. I needed to escalate it.

First, I tried stealing the user’s session cookies on app.target.com via JavaScript, but they were protected with the \`HttpOnly\` flag — dead end. 

Then, I looked for CORS misconfigurations to make requests on behalf of the victim or stealing victims PII, but the server headers were locked down tight. There was no direct API access from the CDN origin to steal data.

Next, I dove into the JavaScript files to find any vulnerable \`postMessage\` handlers that I could abuse, but came up empty-handed. 

So, I pivoted to **\*\*Cookie Tossing\*\*** on \`app.target.com\`. 

I managed to toss an attacker-controlled cookie, i tried forcing my own session cookies onto the victim, but it didn’t give me any session hijacking. But when the victim opened it, it just kicked them out of their account entirely and forced a clean login. 

Honestly, I thought, *\*“Meh, that’s lame and not worth reporting by itself.”\** Or was it? 

If you’re wondering where Cookie Tossing actually saved the day… hold on, grab a seat, and let’s jump into the next section.

\### Exploitation

After some extra recon, I found another subdomain: \`courses.target.com\`. Turned out it was running on WordPress (PHP). 

I ran the same playbook here: tried stealing cookies (blocked by \`HttpOnly\`), tested for CORS misconfigurations, checked \`postMessage\` handlers, and looked for CSRF — nothing. Everything was locked down. Then it hit me: *\*What if I try Cookie Tossing here, on the WordPress instance?\**

After poking around \`courses.target.com\`, I checked how WordPress handles sessions after a successful login. It drops two main cookies:

— \`wordpress\_logged\_in\_hash\` 

— \`wordpress\_sec\_hash\` 

The second one (\`wordpress\_sec\_hash\`) is the key to authenticating requests inside the admin panel (\`/wp-admin/profile.php\`), specifically when editing user profile details.

So, I crafted a custom SVG file to inject the session cookies into the victim’s browser:

\<svg xmlns="http://www.w3.org/2000/svg" width="1" height="1">

\<script type="text/javascript">

document.cookie = "wordpress\_logged\_in\_hash=attackers-cookie; Domain=.target.com; path=//;";

document.cookie = "wordpress\_sec\_hash=attackers-cookie; Domain=.target.com; path=/wp-admin/;";

\</script>

\</svg>

*Note:* I made sure to explicitly specify the proper path (like path=/) for the cookies. Due to browser cookie scoping policies, if you don’t set the path right, the application won’t attach them to the requests, and the whole Cookie Tossing attack falls apart.

I uploaded the malicious SVG file to \`public.cdn.target.com\`, opened the link in another browser acting as the victim, and… boom. The victim was successfully logged into *\*my\** attacker-controlled account. Session hijacked via a smooth Stored XSS to Cookie Tossing chain!

I reported the finding, and the triage team marked it as a **\*\*P2\*\***.

\### Impact 

By chaining Stored XSS on the CDN with Cookie Tossing:

\*\*Session Fixation on courses.target.com:\*\* An attacker can force victims into an attacker-controlled account. Once inside, any personal info entered, courses completed, or actions taken are logged under the attacker’s account — not the victim’s.

\*\*Bypassing HttpOnly Defenses:\*\* Cookie Tossing doesn’t require reading cookies via JavaScript. Instead, it overwrites them from a trusted sibling subdomain, completely bypassing HttpOnly protections.

\*\*Attack Vector:\*\* Delivered via the internal chat feature — victims click what appears to be a legitimate file from a trusted target domain.

***Final Thoughts:*** Always do recon after finding a Stored XSS for a better exploit chain.

Thanks for reading , make sure to follow me for more write ups😊
