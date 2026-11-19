# How a Simple Google Dork Led Me to Find Reflected XSS & HTML Injection on NASA and Earn a Letter of…

- **Source URL:** https://medium.com/@itss4leh/how-a-simple-google-dork-led-me-to-find-reflected-xss-html-injection-on-nasa-and-earn-a-letter-of-83075852de42?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20260728220134/https://medium.com/@itss4leh/how-a-simple-google-dork-led-me-to-find-reflected-xss-html-injection-on-nasa-and-earn-a-letter-of-83075852de42
- **Fetched:** 2026-11-19
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14455 (id 14455)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# How a Simple Google Dork Led Me to Find Reflected XSS & HTML Injection on NASA and Earn a Letter of Recognition \[April 2026\]

## Disclaimer

This write-up is published strictly for educational and awareness purposes and to share knowledge with security researchers and the wider cybersecurity community.

I do not encourage unauthorized testing, illegal activity, or unethical security practices. All testing described in this article was conducted responsibly and reported through NASA’s Vulnerability Disclosure Program.

Security researchers should always obtain proper authorization, remain within the defined scope, follow responsible disclosure guidelines, and comply with all applicable laws and program policies.

## Introduction

In this write-up, I will share how a simple Google Dork led me to discover Reflected Cross-Site Scripting (XSS) and HTML Injection vulnerabilities on a NASA subdomain in April 2026.

The vulnerability existed in a hidden parameter named `popup_flag`.

By manually adding the parameter to an intercepted request, I discovered that its value was reflected inside the HTML response without proper sanitization or encoding. This allowed me to break out of the original HTML context and inject arbitrary HTML and JavaScript.

The vulnerability was validated by Bugcrowd, fixed by NASA, and assigned a final priority of **P4**. I was also listed in NASA’s Hall of Fame and received an official Letter of Recognition.

## Phase 1: Reconnaissance (The Power of Google Dorks)

On April 2, 2026, I started searching for publicly indexed NASA assets using several simple Google Dorks.

**Queries Used:**

```
site:nasa.gov
site:nasa.gov -www
site:*.*.*.nasa.gov
site:*.*.*.nasa.gov -www
site:nasa.gov ext:pl
```
These queries helped me discover indexed subdomains and pages that were not easily accessible from NASA’s main website.

After reviewing the search results, I discovered an application hosted on a NASA subdomain:

`https://cce-signin.gsfc.nasa.gov`
The application allowed users to create an account, so I registered, activated my account, and logged in to explore the authenticated functionality.

## Phase 2: Discovery & Analysis

After logging in, I began inspecting the application for parameters that were not normally visible to users.

## Searching for Hidden Parameters

I opened the page source using:

`CTRL + U`
Then I used `CTRL + F` and searched for the following patterns:

```
hidden
type=hidden
type="hidden"
```
Hidden inputs are not displayed in the normal user interface, but their names and values can still exist inside the HTML source code.

For example:

`<input type="hidden" id="custId" name="custId" value="3487">`
A simple example of an HTML hidden field can be viewed here:

[W3Schools — HTML input type=”hidden”](https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_input_type_hidden)

While reviewing the application’s page source, I discovered a hidden parameter named:

`popup_flag`
## Testing the Hidden Parameter

I submitted the form and intercepted the request to inspect the parameters being sent to the server.

Interestingly, the `popup_flag` parameter existed inside the page source, but it was not included with the other parameters in the request.

To determine whether the backend still processed it, I manually added the parameter using a unique value:

```
Hidden parameter: popup_flag=ItsS4LEH
FULL URL: https://[REDACTED].nasa.gov/[REDACTED]?param1=val1¶m2=val2¶m3=val3&popup_flag=ItsS4LEH
```
The server accepted the parameter and reflected `ItsS4LEH` inside the HTML response.

## Breaking the HTML Context

After confirming the reflection, I tested whether special HTML characters were properly encoded.

I used the following input:

`">`
The double quotation mark closed the existing HTML attribute, while the greater-than character escaped the intended HTML context.

The characters were reflected without being encoded or filtered, confirming that I could inject additional HTML elements into the page.

## Phase 3: Proof of Concept (PoC)

After successfully breaking the HTML context, I tested both Reflected XSS and HTML Injection.

## Reflected XSS Payload

```
XSS Payload: ItsS4LEH"><img src=x onerror=alert(document.cookie)><div style="
FULL URL: https://[REDACTED].nasa.gov/[REDACTED]?param1=p1¶m2=p2¶m3=p3&popup_flag=ItsS4LEH"><img src=x onerror=alert(document.cookie)><div style="
```
## Result

The browser executed the injected JavaScript and displayed an alert containing cookies accessible through:

`document.cookie`
This confirmed that the hidden `popup_flag` parameter was vulnerable to Reflected XSS.

## HTML Injection Payload

```
HTML Injection Payload: ItsS4LEH"><h3><a href="https://example.com/">Click Here to Re-Authenticate.</a></h3><div style="
FULL URL: https://[REDACTED].nasa.gov/[REDACTED]?param1=p1¶m2=p2¶m3=p3&popup_flag=ItsS4LEH"><h3><a href="https://example.com/">Click Here to Re-Authenticate.</a></h3><div style="
```
## Result

The browser rendered the attacker-controlled re-authentication message as a clickable link inside the legitimate NASA page.

Because the content appeared on an official NASA domain, it could potentially be used to create convincing phishing messages or redirect users to an external website.

## Steps

1. Register and log in to the application.
2. Open the page source using `CTRL + U`.
3. Search for `hidden`, `type=hidden`, and `type="hidden"`.
4. Discover the hidden `popup_flag` parameter.
5. Submit the form and intercept the request.
6. Manually add the `popup_flag` parameter.
7. Use `">` to escape the HTML context.
8. Insert the XSS or HTML Injection payload.
9. Submit the modified request and observe the result.

## Proof of Concept Video

## Impact

A successful attack could allow an attacker to perform:

**JavaScript Execution:** Execute arbitrary JavaScript within an authenticated user’s browser.

**HTML Injection and Phishing:** Inject fake login forms, re-authentication messages, or malicious links into a trusted NASA page.

**Cookie Access:** The session cookie was protected by the `HttpOnly` flag and could not be accessed through JavaScript. However, other cookies without `HttpOnly` protection remained accessible through `document.cookie`.

**Page Manipulation:** Modify the visible page content or redirect users to an external website.

Because the injected content was rendered on an official NASA domain, it could appear more trustworthy to potential victims.

## Recognition & Appreciation

After the report was validated, my submission appeared in NASA’s CrowdStream on Bugcrowd with a final priority of **P4**.

I was also honored to have my name, **ItsS4LEH**, listed in NASA’s Hall of Fame.

After the vulnerability was resolved, NASA sent me an official Letter of Recognition in appreciation of my efforts in identifying and responsibly reporting the issue.

The letter was signed by **Kelvin Taylor**, NASA’s Senior Agency Information Security Officer.

Receiving recognition from an organization such as NASA is a great motivation for me to continue learning, hunting, and helping secure the web!

## Timeline & Resolution

**April 2, 2026:** Vulnerability reported through NASA’s Bugcrowd VDP.

**April 23, 2026:** Report successfully validated and moved to Triaged.

**April 24, 2026:** Submission accepted and displayed in NASA CrowdStream.

**July 15, 2026:** Vulnerability confirmed as fixed and the report marked Resolved.

**July 16, 2026:** Final priority updated to **P4**.

**July 16, 2026:** Official NASA Letter of Recognition received.

## Contact me:

**LinkedIn:** [https://www.linkedin.com/in/saleh16abdullah/](https://www.linkedin.com/in/saleh16abdullah/)

**X (formerly Twitter):** [ItsS4LEH](https://x.com/ItsS4LEH)

**Telegram Channel:** [ItsS4LEH](https://t.me/+ylDx8zGNLEwzMWU8)

Thank you for reading! If you enjoyed this write-up, feel free to follow for more security research and findings.

**By: ItsS4LEH**

**Tags:** Bug Bounty, Bug Bounty Writeup, Infosec, Cybersecurity, XSS Attack
