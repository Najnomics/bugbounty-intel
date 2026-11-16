# *$$$$ How I Turned a ‘Low Severity’ Reflected XSS into Full Admin Account Takeover

- **Source URL:** https://medium.com/@asharm.khan7/how-i-turned-a-low-severity-reflected-xss-into-full-admin-account-takeover-42ff5ab31230?source=rss------bug_bounty-5
- **Fetched from:** https://medium.com/feed/@asharm.khan7
- **Fetched:** 2026-11-16
- **Channel:** @dailybountywriteup
- **Telegram message:**  (id 13563)
- **Method:** medium-rss-content readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
Hello hackers! It’s me Ashar, here again. 👨💻

While testing redacted.com, I came across what initially looked like a very ordinary reflected XSS vulnerability.

Honestly… at first, I wasn’t very excited. 😅

The application had already implemented HttpOnly cookies correctly, meaning the classic:

document.cookie

approach was practically useless. And as bug hunters, we’ve all been there before…

You find an XSS!

You try stealing cookies, HttpOnly ruins the fun. 😭

So initially, I thought:

***“Alright… probably just a Low or Medium severity finding.”***

But something about the application architecture kept bothering me. 🤔

That’s when I decided to go deeper instead of stopping at the obvious.

And eventually…

That “**harmless**” reflected XSS turned into a complete **admin account takeover.**

### The Discovery

During reconnaissance, I noticed an endpoint reflecting user-controlled input directly into the HTML response without proper sanitization.

The vulnerable endpoint looked like this:

https://redacted.com/dashboard?next=">\<img src=x onerror=alert(document.cookie)>

As soon as I visited the page, paylaod executed successfully!!

Boom. Reflected XSS confirmed, But then came the disappointment…

### The “Dead End”

When I attempted to access session cookies:

document.cookie

the sensitive authentication cookies were missing.

The application had implemented HttpOnly protections properly.

At this point, most of us would probably classify the issue as low impact and move on.

And honestly…

For a few minutes, even I thought the same. 😅 But then a simple thought crossed my mind:

***“What if I don’t actually need to read the cookies?”***

That single question completely changed the direction of the entire assessment.

### Digging Deeper 👀

At this point, the vulnerability looked interesting… but not critical.

The HttpOnly cookies had already killed the classic cookie theft approach.

So instead of trying to steal sessions directly, I started exploring the application’s authenticated functionality more carefully.

And that’s when things became REALLY interesting.

While browsing through Burp history and analyzing API requests, I noticed that the application heavily relied on **JSON-based** API calls for sensitive account operations.

One particular request immediately caught my attention.

POST /account/change-email HTTP/1.1

Host: redacted.com

Cookie: REDACTED

Content-Type: application/json

{

"email":"attacker@redacted.com","reqToken":"redactedrandomstring"

}

Now normally, endpoints like these are difficult to abuse through traditional CSRF attacks because they require:

- application/json
- custom request headers
- authenticated browser context

A normal HTML form cannot naturally send requests like this. Which meant a classic CSRF attack was practically useless here.

But then I realized something VERY important, my JavaScript payload wasn’t executing from an external attacker-controlled domain…

https://redacted.com

Which meant:

**The browser itself could be weaponized against the victim.**

### Turning XSS into Account Takeover

Now the reflected XSS became MUCH more dangerous. Instead of trying to steal cookies, I decided to abuse the victim’s authenticated browser session directly.

As I already had my eyes on email change API calls so I curated a JS payload to fire this call within victim’s session.

```
fetch('https://redacted.com/account/change-email', {
    method: 'POST',
    credentials: 'include',
    headers: {
        'Content-Type': 'application/json'
    },
    body: JSON.stringify({
        email: 'attacker@redacted.com'
    })
})
```
Because the payload executed from the trusted origin itself, the browser automatically included the administrator’s authenticated session cookies.

Which means:

✅ The request was treated as legitimate

✅ The administrator’s email changed silently

✅ The attacker gained password reset control

No cookie theft required.

Once the email was changed, I could simply trigger the “Forgot Password” functionality and completely take over the administrator account.

Leading to:

- Full admin account compromise
- Persistent access
- Access to internal functionality
- Potential organization-wide impact

And the best part?

The victim would likely have absolutely no idea anything happened.

### The Final Payload

To make exploitation cleaner, I base64-encoded the payload using:

btoa(payload)

Then executed it using:

`<img src=x onerror=eval(atob('BASE64_PAYLOAD'))>`
Final exploit URL:

`https://redacted.com/dashboard?next="><img src=x onerror=eval(atob('BASE64_PAYLOAD'))>`
Just one click from a logged-in administrator… And the account was gone!!

### Why HttpOnly Wasn’t Enough

This finding demonstrated an important security misconception.

Many developers believe that HttpOnly cookies significantly reduce the impact of XSS vulnerabilities.

But once JavaScript executes inside the trusted origin, it can still perform authenticated actions on behalf of the victim.

In this case, the reflected XSS allowed same-origin JavaScript execution against sensitive JSON API endpoints, ultimately leading to full administrator account takeover.

Like & drop a comment if you found this helpful — happy to answer any questions! Follow for more like this one.

### 🔗 For More, Follow Me:

- **LinkedIn:** [asharmahmood](https://www.linkedin.com/in/asharmahmood)
- **Twitter (X):** [@Hx\_0p](https://twitter.com/Hx_0p)
- **Website:** [asharmahmood.com](https://asharmahmood.com/)
