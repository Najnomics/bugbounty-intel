# Winning QR with DOM-Based XSS | Bug Bounty POC

- **Source URL:** https://medium.com/@haroonhameed_76621/winning-qr-with-dom-based-xss-bug-bounty-poc-4b4048cf285d?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20261116220723/https://medium.com/@haroonhameed_76621/winning-qr-with-dom-based-xss-bug-bounty-poc-4b4048cf285d
- **Fetched:** 2026-11-19
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/821 (id 821)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Winning QR with DOM-Based XSS | Bug Bounty POC

## Background:

*I am passionate Cyber Security enthusiast, with extensive skills in Web Application, API Penetration Testing, currently working as a Bug Bounty hunter on Synack Red Team (SRT), Bugcrowd and Zerocopter from Shahkot, Punjab, Pakistan.*

This blog post describes how I am able to execute DOM-Based XSS on Synack Red Team program and able to win QR aka Quality Rule.

Hope you guys are doing good, the bug was simple to exploit, but it took a while to figure out and make it happen. I’ll try to keep blog simple as possible.

## Understanding the DOM:

In order to understand sources and sinks as it relates to DOM-Based Cross-site scripting, we briefly have to understand the DOM and some of its methods. The Document Object Model is the web browser’s hierarchical representation of the elements of a webpage. In other words, when a browser receives a page to load, it will parse or dissect the page structure and separate the different elements of the page into a tree-like structure with each element and attribute nested in their respective location.

## DOM-Based XSS: Source and Sinks

Now that we have the basics of the DOM and we understand that JavaScript code can make changes to the page in real time, we can discuss DOM-Based XSS as well as source and sinks. Disclaimer: To help with the explanation, I’ll be using a lab from PortSwigger’s Web Academy, which include additional information as well as plenty of labs to practice the concepts discussed. This will be a minor spoiler to one of the labs.

**Source**:

A source function is any JS property or function that accepts user input from somewhere on the page. An example of a source is the location.search property because it reads input from the query string.

Here are some common sources:

\* document.URL

\* document.documentURI

\* document.URLUnencoded

\* document.baseURI

\* location.search

\* document.cookie

\* document.referrer

**Sink**:

A sink is a potentially dangerous JavaScript function that can caused undesirable effects if attacker controlled data is passed to it. Basically, if the function returns input back to the screen as output without security checks, it’s considered a sink. An example of this would be the “innerHTML” property used earlier as that changes the contents of the HTML page to whatever is given to it.

Common sinks include:

\* document.write()

\* document.writeln()

\* document.domain

\* element.innerHTML

\* element.outerHTML

\* element.insertAdjacentHTML

\* element.onevent

**Vulnerability Analysis:**

My main focus was on the main domain, which is [https://redacted.com,](https://redacted.com,) so I won’t do any subdomain enumeration and starting looking for juicy JavaScript files and luckily I found an interesting JavaScript file, where I found the following JavaScript function:

```
function getParameterByName(name, url) {
    if (!url) url = window.location.href;
    name = name.replace(/[\[\]]/g, "\\$&");
    var regex = new RegExp("[?&]" + name + "(=([^&#]*)|&|#|$)"),
        results = regex.exec(url);
    if (!results) return null;
    if (!results[2]) return null;
    return decodeURIComponent(results[2].replace(/\+/g, " "))
```
In this JavaScript function **getParamByName** which is getting two parameter(s) and its value from the URL, it takes two parameter(s) one is **name** which is a string and fetch parameter name from URL which is **target=** in our case and second parameter value will be URL like document.URL, document.location.

In our case following are Source and Sink:

## Get Haroon Hameed’s stories in your inbox

Join Medium for free to get updates from this writer.

**Source**:

`window.location.href`
**Sink:**

`else{cmsService.getClientConfig().then(function(result){if(angular.isDefined(result)){uaService.createAndSetDemographics(result)}$window.location.href=vm.credentials.redirect||"/"})`
After taking the value from the source for the successful execution of JavaScript the following function need to be true:

```
 $location.path("/")
            } else {
                if (result.token) {
                    window.localStorage.wptoken = result.token
                }
                if (result.status == "ACTIONREQUIRED_2FA_SETUP" && result.token) {
                    twoFactorAuthService.requireAuthSetup("login")
                } else if (result.status == "ACTIONREQUIRED_2FA_VERIFICATION" && result.token) {
                    twoFactorAuthService.requireAuthVerification("login")
                } else if (result.success != "true" && result.status.length > 0) {
                    vm.submitted = false;
                    vm.onError(result.status)
                } else {
                    cmsService.getClientConfig().then(function(result) {
                        if (angular.isDefined(result)) {
                            uaService.createAndSetDemographics(result)
                        }
                        $window.location.href = vm.credentials.redirect || "/"
                    })
```
In our case the last statement is true and causing the execution of JavaScript.

After understanding the JavaScript code you will clearly see that it will take user-supplied input from **target** parameter and executing it in DOM aka sink.

So I used the following JavaScript payload:

`javascript:alert(document.domain)`
Hence, it was Quality Rule program on Synack Red Team, I submitted the best quality report to **Synack** and won the quality with 3/3 stars and awarded by $775.00 of bounty.

Whenever you are testing an application for such issues, always check JavaScript file and understand how application handle user-supplied inputs.

Voila! “Sometimes, HACKING is Just someone spending more time on something than anyone else might reasonably expect” it’s always good to look into things that seem to be pointless.

**Social Links:**

**Partner**:

We are open to work, if you have any Private Pentesting project, kindly DM any of us! Thank you!

If you like this write-up, Share!

Thank you!
