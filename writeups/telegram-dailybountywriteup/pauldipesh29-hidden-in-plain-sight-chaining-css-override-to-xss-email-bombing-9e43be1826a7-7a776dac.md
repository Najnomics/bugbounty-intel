# Hidden in Plain Sight

- **Source URL:** https://medium.com/@pauldipesh29/hidden-in-plain-sight-chaining-css-override-to-xss-email-bombing-9e43be1826a7?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20251010190909/https://medium.com/@pauldipesh29/hidden-in-plain-sight-chaining-css-override-to-xss-email-bombing-9e43be1826a7
- **Fetched:** 2026-11-19
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/11233 (id 11233)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# **Hidden in Plain Sight**: Chaining CSS Override to XSS **& Email Bombing**

**📌about-me‼️**


Hello guys, I am [Dipesh Paul](https://linkedin.com/in/the-genetic) (aka thegenetic), a dedicated cybersecurity professional and part-time bug hunter🫠. With expertise in uncovering vulnerabilities like injection, account takeover, sensitive information disclosures, and broken access control, I’ve helped multiple organization secure there online assets by reporting multiple vulnerabilities till date.🥷

After a routine assessment of a [Intuiface’s](https://www.intuiface.com/) login page, I uncovered a chain of vulnerabilities that, while simple individually, created a significant security risk when combined. This write-up details the journey from spotting a subtle code issue to achieving a successful Cross-Site Scripting (XSS) exploit by manipulating a hidden client-side feature.

### 1. Detection

The investigation began with a review of the client-side code. A quick glance at the JavaScript sources revealed a significant red flag: the use of the `eval()` function.

- `eval()` is a powerful but dangerous JavaScript function that executes a string of code passed to it. If user-controlled input finds its way into an `eval()` call, it can lead to arbitrary code execution. While my final exploit didn't directly exploit `eval`, its presence signaled a codebase where dynamic code execution was used, increasing the overall attack surface.

More pertinent to the final exploit was the discovery of a function named `resendVerificationEmail()`. Intriguingly, the HTML element that triggered this function was not visible on the page. A look at the DOM revealed why:

`<a id="ResendEmail" href="javascript:__doPostBack('ResendEmail','')" style="display:none"></a>`
- The CSS property `display: none` is used to completely remove an element from the page's visual layout. The element exists in the DOM but is not rendered on the screen and cannot be interacted with by a regular user. It's a client-side visibility control, not a security control.

The presence of this hidden, yet functional, element immediately presented a question: What happens if we force it to become visible and usable?

### 2. Bypassing the Client-Side Cloak

The first step was to activate this hidden functionality. This is trivially achieved using any modern browser’s Developer Tools (F12).

**Action:**

1. Navigated to the login page
2. Opened the Inspector tab in Developer Tools.
3. Located the `<a id="ResendEmail">` element.

4\. Double-clicked the `style="display:none"` attribute and deleted it or changed it to `style=""`.

5\. Added the text “Click Here” between the anchor tags to make it a visible, clickable link.

**The Result:**

The element was now fully visible and functional on the page. This simple act demonstrated a critical security principle:

**Security must be enforced on the server-side. Client-side controls, like hidden form fields or CSS, are easily bypassed and should never be trusted for access control.**


### 3. The Core Vulnerability: Unsanitized Reflection

With the “Resend Email” link now active, the next step was to understand the data flow. I entered a email and clicked the link while intercepting the traffic with Burp Suite.

The intercepted request was a POST that triggered a `__doPostBack` function. Crucially, in the server's HTTP response, I observed that the email address I had provided was being reflected directly within the HTML.

- **Reflected Cross-Site Scripting (XSS)**
Reflected XSS occurs when a web application takes user input from a request and immediately includes it in the response without proper validation or encoding. An attacker can craft a malicious URL containing a script. When a victim clicks the link, the script is sent to the vulnerable server, reflected back, and executed in the victim’s browser within the context of the target site.

The application was taking my input and placing it directly into the HTML output without any sanitization. This was the vulnerability’s root cause.

### 4. Crafting and Executing the Exploit

The final step was to prove the vulnerability by injecting a malicious payload.

**Action:**

In the intercepted Burp Suite request, I modified the email parameter to a basic XSS payload and forwarded the request.

`<email-id>"</b><script>propmpt(3)</script>`
**The Result:**

Upon viewing the server’s response in a browser, the `prompt` event fired, and an alert box popped up. The XSS was successful.

### The Complete Attack Chain

The entire exploit can be visualized as a simple chain:

1. **Bypass Client-Side Control:** Use browser tools to remove `display:none` from the `ResendEmail` link.
2. **Trigger the Vulnerable Function:** Click the now-visible link to trigger the `__doPostBack` request.
3. **Inject Malicious Payload:** Supply a crafted XSS payload in the email parameter.
4. **Server-Side Failure:** The server fails to sanitize the input and reflects the payload directly in its HTML response.
5. **Code Execution:** The victim’s browser receives the malicious HTML and executes the JavaScript payload.

### The Accompanying Rate Limit Bypass

It’s important to note that the same vulnerable `ResendEmail` endpoint was also missing critical server-side protection. Since the function's availability was solely controlled by the client-side `display:none` property, an attacker who bypassed this, as demonstrated could submit an unlimited number of requests. By using a tool like Burp Suite's Intruder to repeatedly send the `__doPostBack` request for a known, valid email address, the server would obligingly generate and send a verification email for each request. This lack of server-side rate limiting opened the door to email bombing attacks, allowing an attacker to spam a user's inbox or potentially drain the application's email service resources through a simple automated script.

### Key Takeaway

1. Fixes like disabling or hiding elements via css is a temporary solution not the final fix, it could be easily bypassed. Always ensure input sanitzation & output encoding.
2. Server-Side Authorization & Rate Limiting, the visibility of the `ResendEmail` function should be a UI decision, but its execution must be guarded by server-side checks, such as a robust rate limit (e.g., a maximum of 3 emails per hour per email address) and session validation, to prevent abuse.

Finally, I would like to thank the security team at [Intuiface](https://www.intuiface.com/) for their prompt and professional response in addressing this issue and for the [recognition](https://www.intuiface.com/info/vdp-hall-of-fame).

Connect with me on [LinkedIn](https://www.linkedin.com/in/the-genetic/) and also on [X](https://x.com/DipeshPaul19)

**Stay paranoid, stay safe.** 🚀

*Thank you for reading! If my content has helped you in any way, consider buying me a coffee to show your support* [***here***](https://buymeacoffee.com/thegenetic)!

Adios!
