# How I Turned a Boring Self-XSS into a Real-World Attack Using CSRF

- **Source URL:** https://medium.com/@mostafamhmoud378/how-i-turned-a-boring-self-xss-into-a-real-world-attack-using-csrf-37cf3a78e3da?source=rss------bug_bounty-5
- **Fetched from:** https://medium.com/feed/@mostafamhmoud378
- **Fetched:** 2026-11-18
- **Channel:** @dailybountywriteup
- **Telegram message:**  (id 12583)
- **Method:** medium-rss-content readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
Sometimes, the difference between a low-impact bug and a high-impact vulnerability is just one good idea.

Victim logged in → visits malicious page → browser auto‑submits CSRF POST → payload stored → XSS executes

**🔥 The Beginning – “This is just Self-XSS…”**

While hunting on a private HackerOne program, I stumbled upon a stored XSS vulnerability inside the account settings page.

At first, I was disappointed.

*Why?*

Because:

The payload had to be injected manually by the user

Which means → **Self-XSS**

And self-XSS = low impact + low bounty

Most hunters would stop here, write a quick report, and move on.

But I didn’t.

Because attackers don’t stop when things get boring.

**🧠 Thinking Like an Attacker**

I asked myself one simple question:

What if I could inject this payload into the victim’s account without them touching anything?

So I started reviewing the request carefully.

And then I noticed something beautiful…

**No CSRF token.**

At that moment, everything changed.

**⚡ The Idea – Chaining CSRF + Stored XSS**

The target allowed:

State-changing requests without CSRF protection While the user is authenticated

That meant one thing:

*👉 I can force the victim’s browser to inject my XSS payload for me.*

So now, instead of:

User pastes payload manually

We get:

**Victim just clicks a link – boom, Stored XSS injected.**

That’s a game changer.

**🎯 Target Endpoint**

*/account/settings*

This endpoint updates sensitive personal data such as:

Full name

Phone number

Perfect place for exploitation.

**🧪 The Weapon – CSRF Exploit Page**

I built a malicious HTML page hosted externally.

Once the victim visits it while logged in, their browser silently submits a forged request.

\<html>

\<body>

\<form action="https://target.ee/account/settings" method="POST">

\<input type="hidden" name="fullname" value="mostafa"onmouseover="alert(document.cookie)">

\<input type="hidden" name="mobile" value="010220330">

\</form>

\<script>

document.forms\[0\].submit();

\</script>

\</body>

\</html>

**💣 Payload Used**

mostafa"onmouseover="alert(document.cookie)

Simple. Clean. Effective.

**🧭 Attack Scenario**

Let’s imagine a real-world attack:

Victim logs into the website

Victim clicks a phishing link

CSRF auto-submits the form

XSS payload gets stored in their profile

BOOM 🤯 JavaScript executes inside their session

No warnings.

No alerts.

No interaction.

Just silent compromise.

**💥 Impact**

This transformed:

😴 Boring self-XSS

Into

🔥 Remote stored XSS via CSRF

**Which allows:**

Session hijacking

Account manipulation

Phishing injection

Malicious redirects

Now this is a real vulnerability.

**🛡️ How to Fix It**

Implement CSRF tokens

Enforce SameSite cookies

Proper output encoding

Strong Content Security Policy (CSP)

*Security is not about fixing one bug – it’s about breaking attack chains.*

**🧠 Final Lesson**

*Never underestimate a low-severity bug.*

Sometimes, the most dangerous vulnerabilities are hiding behind:

*“This is just a small issue…”*

Because:

*Real attacks are built by chaining small mistakes.*

**✍️ Author**

**Mostafa Mahmoud**

*Cyber Security Specialist | Penetration Tester*

*Bug Bounty Hunter | HackerOne*

Thanks for reading – and happy hacking 🚀

#CyberSecurity #BugBounty #XSS #CSRF #WebSecurity #HackerOne
