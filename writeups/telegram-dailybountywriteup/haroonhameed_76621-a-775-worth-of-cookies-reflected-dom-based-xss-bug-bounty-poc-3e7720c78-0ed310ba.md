# A $$$ worth of cookies! | Reflected DOM-Based XSS | Bug Bounty POC

- **Source URL:** https://medium.com/@haroonhameed_76621/a-775-worth-of-cookies-reflected-dom-based-xss-bug-bounty-poc-3e7720c78fbe?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20251004092518/https://medium.com/@haroonhameed_76621/a-775-worth-of-cookies-reflected-dom-based-xss-bug-bounty-poc-3e7720c78fbe
- **Fetched:** 2026-11-19
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/991 (id 991)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# A $$$ worth of cookies! | Reflected DOM-Based XSS | Bug Bounty POC

Hey everyone! This is Haroon Hameed and I’m here to share about my recent finding on Synack Red Team about Reflected DOM-based XSS. In this blog post, I’m going to discuss the Bug Bounty report of this discovery.

It was a QR-based target on Synack Red Team, and whenever there is a QR-based target, my brother [Hannan Haseeb](https://twitter.com/HannanHaseeb11) and I collaborate!

**Vulnerability Analysis:**

Lets begin! My main focus was on the main domain, which is [https://redacted.com,](https://redacted.com,) so I won’t do any subdomain enumeration and starting looking for juicy JavaScript files and luckily I found two interesting JavaScript file, where I found the following JavaScript function:

```
code: function(e) {
                    var a = e.car,
                        t = e.articleUuid,
                        i = e.returnPath,
                        u = e.moreInfoData,
                        m = e.currentUser,
                        o = m.canPrint,
                        d = void 0 === o || o,
                        E = m.canBookmark,
                        b = void 0 === E || E,
                        f = a.uuid,
                        h = i ? "Search Results" : "Car";
                    return l.createElement("div", null, l.createElement("div", {
                        className: "viewer-header"
                    }, l.createElement("div", {
                        className: "car-form-container"
                    }, l.createElement("div", {
                        className: "article-toolbar-container"
                    }, l.createElement("div", {
                        className: "page-width article-toolbar"
                    }, l.createElement(l.Suspense, {
                        fallback: l.createElement("div", null)
                    }, l.createElement(s, a)), l.createElement("ul", {
                        className: "back-to-search-ul"
                    }, l.createElement("li", {
                        className: "back-to-search-results"
                    }, l.createElement("a", {
                        className: "button",
                        href: i || "/car/" + f + "/search"
                    },
```
This code is used for rendering a car viewer component in a React application. The component displays the car details, as well as other information such as a back to search button and a tool bar that allows the user to perform certain actions. DOM based XSS is possible with this code if the href attribute of the “a” tag is not properly sanitized. If user input is not properly sanitized, it is possible for malicious code to be executed, allowing for a DOM based XSS attack.

In 2nd JavaScript file, I found the proper Source and Sink of the Reflected DOM-Based XSS, the following are our Source and Sink:

Source:

```
document.addEventListener("DOMContentLoaded", (function() {
            var e = document.getElementById("search-application-container")
              , t = JSON.parse(e.getAttribute("state")) || window.initialState;
            a.render(r.createElement(rr, t), e)
```
This Source is used for rendering a React component in the DOM. It parses the state from the element with the id “search-application-container” and passes it to the React component. The component is then rendered in the element.

Sink:

```
l.createElement("a", {
                        className: "button",
                        href: i || "/car/" + f + "/search"
                    }
```
The DOM function l.createElement create a HTML tag a and set it’s attribute value to HTML href attribute which is user controllable returnPath parameter.

After understanding the JavaScript code you will clearly see that it will take user-supplied input from returnPath parameter and executing it in DOM aka sink.

So I used the following JavaScript payload:

`javascript:alert(document.domain)`
Hence, I had successfully submitted the best quality report to Synack’s Quality Rule program on Synack Red Team and was awarded with 3/3 stars and a bounty of $$$.

**Social Links:**

**Partner**:

We are open to work on any private pentesting projects. If you have any such projects, please feel free to DM any of us. Thank you!

If you like this write-up, Share!

Thank you!
