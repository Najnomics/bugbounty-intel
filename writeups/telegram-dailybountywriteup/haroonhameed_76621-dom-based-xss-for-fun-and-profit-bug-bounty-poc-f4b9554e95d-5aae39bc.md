# DOM-Based XSS for fun and profit $$$! | Bug Bounty POC

- **Source URL:** https://medium.com/@haroonhameed_76621/dom-based-xss-for-fun-and-profit-bug-bounty-poc-f4b9554e95d?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20261116220710/https://medium.com/@haroonhameed_76621/dom-based-xss-for-fun-and-profit-bug-bounty-poc-f4b9554e95d
- **Fetched:** 2026-11-19
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/1432 (id 1432)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# DOM-Based XSS for fun and profit $$$! | Bug Bounty POC

Hey everyone! This is Haroon Hameed and I’m here to share about our recent finding on Synack Red Team about DOM-based XSS. In this blog post, I’m going to discuss the Bug Bounty report of this discovery.

It was a QR-based target on Synack Red Team

**Vulnerability Analysis:**

Lets begin! Our main focus was on the main domain, which is [https://redacted.com,](https://redacted.com,) so we won’t do any subdomain enumeration and starting looking for juicy JavaScript files and luckily we found two interesting JavaScript file, where we found the following JavaScript function:

```
function saveRegion(regionId, forceReload) {//Save selection
    customer_RegionId = regionId;
    $.ajax({
        type: 'POST',
        url: "/Unauthenticated/SaveRegion",
        data: {
            regionId: regionId
        },
        success: function (response) {
            setCookie('RegionId', regionId, 1);
            $('#select-region-modal').modal('hide');
            var url = getParameterByName('url');
            if (url != null && url != '') {
                createCookie('UAPathway', 'Start', 1);
                setTimeout(function () {
                    window.open(url, '_self');
                }, 1000);
```
In the above code when an unauthenticated user click on **Save Region** it will send Ajax request (An Ajax request is an HTTP request that uses the **XMLHttpRequest** object to exchange data asynchronously with a web server. This allows for dynamic web page updates without the need for a full page reload.) with **POST** type on **/Unauthenticated/SaveRegion** endpoint(s) than this code will save the selected **regionId** (regionId is a parameter passed to the function) to a cookie, then reloads the page (or redirects to a specified URL). It then sets a cookie for the user’s pathway (UAPathway) with a value of “Start”.


The code above is vulnerable to DOM-Based XSS. If an attacker is able to inject malicious JavaScript into the “url” parameter, the resulting code will be executed on the page. The code uses the “getParameterByNam”e function to retrieve the value of the “url” parameter, which is then used in the “window.open” function.

Source:

```
function getParameterByName(name, url = window.location.href) {
    name = name.replace(/[\[\]]/g, '\\$&');
    var regex = new RegExp('[?&]' + name + '(=([^&#]*)|&|#|$)'),
        results = regex.exec(url);
    if (!results) return null;
    if (!results[2]) return '';
    return decodeURIComponent(results[2].replace(/\+/g, ' '));
}
```
In this JavaScript code “getParameterByName()” function, which is used to retrieve parameters from the URL, allows the attacker to execute malicious code on the website by manipulating the “url” parameters.

`window.open(url, '_self');`
The following are some demonstration payloads which can be used to execute JavaScript commands and access DOM elements, such as document.domain and document.cookie:

After understanding the JavaScript code you will clearly see that it will take user-supplied input from ‘url’ parameter and executing it in DOM aka sink.

So we used the following JavaScript payload:

```
javascript:alert(document.domain)
javascript:alert(document.cookie)
```
Hence, We submitted the best quality report to Synack’s Quality Rule program on Synack Red Team and was awarded with 3/3 stars and a bounty of $$$.

Voila! “Sometimes, HACKING is Just someone spending more time on something than anyone else might reasonably expect” it’s always good to look into things that seem to be pointless.

**Social Links:**

We are open to work on any private pentesting projects. If you have any such projects, please feel free to DM any of us. Thank you!

If you like this write-up, Share!

Thank you!
