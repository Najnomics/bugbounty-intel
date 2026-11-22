# How I Find Cross-Site Scripting (XSS) Vulnerabilities During Bug Bounty Hunting | By Samadhan…

- **Source URL:** https://samadhanshimple.medium.com/how-i-find-cross-site-scripting-xss-vulnerabilities-during-bug-bounty-hunting-by-samadhan-562278fa0872
- **Fetched from:** https://samadhanshimple.medium.com/feed
- **Fetched:** 2026-11-22
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14995 (id 14995)
- **Method:** medium-rss-content readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
### How I Find Cross-Site Scripting (XSS) Vulnerabilities During Bug Bounty Hunting | By Samadhan Shimple

Cross-Site Scripting (XSS) is one of the vulnerabilities I always keep in mind when testing web applications. It may look like a simple client-side issue, but its impact can be serious depending on where the vulnerability exists and who can access the affected page.

When I started learning web application security, I thought finding XSS was mostly about inserting JavaScript into input fields. However, as I explored more applications, I understood that there is much more to it.

The real challenge is understanding how an application handles user input and how that input is displayed in a browser.

In this article, I will explain how I approach XSS testing, the different types of XSS, common places where I look for vulnerabilities, useful tools, and how developers can prevent them.

### 1. What Is Cross-Site Scripting (XSS)?

Cross-Site Scripting, commonly known as XSS, is a web application vulnerability that allows an attacker to inject malicious client-side code into a page viewed by another user.

In most cases, JavaScript is used, although XSS can also involve other forms of executable browser content.

The main problem occurs when an application takes untrusted input and includes it in a webpage without applying the correct output encoding or sanitization.

As a result, the browser may interpret that input as executable code instead of displaying it as normal text.

For example, imagine a website that allows users to submit comments. If the application does not safely handle submitted content, an attacker may be able to introduce HTML or JavaScript that executes when another user visits the affected page.

This is why I pay attention to how applications process and display user-controlled data.

### 2. Why Does XSS Happen?

To understand XSS properly, we need to understand how browsers process HTML and JavaScript.

When a browser loads a webpage, it interprets HTML elements, attributes, and scripts to display the content.

If an application places untrusted input into an unsafe location, the browser may interpret that input as part of the webpage structure or executable code.

Here are some common reasons why XSS vulnerabilities occur.

### 1. Improper Input Handling

Some applications accept user input without properly checking its expected format or purpose.

For example, a search field may accept unexpected characters and later display the submitted value on a results page.

Input validation can help reduce unwanted input, but it is not enough to prevent XSS on its own.

### 2. Missing Output Encoding

This is one of the most important causes of XSS.

Applications sometimes display user-controlled information without encoding it according to the context where it appears.

For example, data displayed inside an HTML body requires different handling from data placed inside a JavaScript string or HTML attribute.

That is why context-aware output encoding is essential.

### 3. Weak Content Security Policy (CSP)

Content Security Policy is an additional browser security mechanism that helps control which resources and scripts a webpage can load or execute.

A weak CSP may allow unsafe script execution or permit resources from untrusted sources.

A properly configured CSP can reduce the impact of some XSS vulnerabilities, but it should never replace secure output handling.

### 4. Unsafe JavaScript Functions

Modern applications use JavaScript to update webpage content dynamically.

Problems can occur when developers use unsafe DOM methods that interpret user-controlled content as HTML.

For example, using innerHTML with untrusted input can create an XSS risk.

Developers should prefer safer methods such as textContent when they only need to display text.

### 3. Understanding the Three Types of XSS

Before starting XSS testing, I always make sure I understand the three main categories.

Each type works differently, and understanding those differences helps me identify where to investigate.

### 1. Reflected XSS

\<text emphasis=”bold”>How it works:\</text>

Reflected XSS occurs when user-controlled input is immediately included in the server’s response without proper handling.

For example, imagine a website with a search feature.

A user enters a search term, and the application displays that same value on the results page. If the application handles the value unsafely, it may create an XSS vulnerability.

This type of XSS is generally non-persistent because the input is not permanently stored by the application.

In many cases, an attacker needs to convince a victim to visit a specially crafted URL or submit a request.

### 2. Stored XSS

\<text emphasis=”bold”>How it works:\</text>

Stored XSS occurs when malicious content is saved by an application and later displayed to other users without proper sanitization or output encoding.

Some common locations I pay attention to include:

- Comment sections.
- User profile information.
- Product reviews.
- Support tickets.
- Chat messages.
- Blog posts.

For example, imagine a website where users can update their profile descriptions.

If the application stores submitted content and displays it unsafely to other visitors, it may create a stored XSS vulnerability.

Stored XSS can have a wider impact because multiple users may encounter the affected content.

### 3. DOM-Based XSS

\<text emphasis=”bold”>How it works:\</text>

DOM-based XSS occurs when client-side JavaScript processes untrusted data and places it into an unsafe location in the Document Object Model (DOM).

Unlike traditional reflected XSS, the vulnerable behavior can happen entirely in the browser.

For example, JavaScript might read information from:

- window.location
- location.hash
- document.referrer
- Other browser-controlled data sources.

If that information is passed to an unsafe DOM method, it may create an XSS vulnerability.

When testing modern web applications, I pay special attention to client-side JavaScript because DOM-based issues are not always obvious from normal HTTP response inspection.

### 4. My Approach to Finding XSS Vulnerabilities

When I start testing an application, I do not immediately try random payloads.

First, I explore the application and understand how its different features work.

I identify places where users can submit information and observe where that information appears afterward.

Here is the general approach I follow.

### Step 1: Identify Input Fields

I begin by exploring different application features.

I pay attention to:

- Search boxes.
- Login and registration forms.
- Contact forms.
- Profile update fields.
- Comment sections.
- Feedback forms.
- URL parameters.
- API request bodies.
- HTTP headers and cookies.

I also inspect requests using Burp Suite to understand how user input travels between the browser and the server.

### Step 2: Understand Where Input Appears

After identifying input fields, I check whether the submitted values appear somewhere in the application.

For example, I may enter a harmless test string into a search field and observe whether the same value appears on the results page.

I also check whether the value appears in the page source, HTML attributes, or dynamically generated content.

This helps me understand the context in which the application uses the supplied input.

### Step 3: Understand the Output Context

This is one of the most important parts of XSS testing.

A value can appear in different locations, such as:

- HTML body content.
- HTML attributes.
- JavaScript code.
- URL parameters.
- CSS properties.
- Dynamically updated DOM elements.

The same input may be handled safely in one location but unsafely in another.

Therefore, I try to understand the exact context before deciding whether an XSS vulnerability may exist.

### Step 4: Verify the Behavior

If I notice suspicious behavior, I investigate further in an authorized testing environment.

I check whether the browser treats the supplied content as normal text or interprets it as HTML or executable content.

I also verify whether the behavior is reflected, stored, or generated through client-side JavaScript.

One important thing I have learned is that seeing an input value reflected in a response does not automatically mean the application is vulnerable.

I need evidence that the application handles the value unsafely.

### 5. Tools I Use for XSS Testing

Manual testing is important, but the right tools can make the process easier and more organized.

Here are some tools I recommend exploring.

### 1. Burp Suite

Website: [https://portswigger.net/burp](https://portswigger.net/burp)

Burp Suite is one of the main tools I use during web application security testing.

Its Proxy feature helps me intercept HTTP requests and understand how user input is processed.

Repeater is useful for modifying requests and comparing responses, while Intruder can help with controlled input testing.

### 2. OWASP ZAP

Website: [https://www.zaproxy.org/](https://www.zaproxy.org/)

OWASP ZAP is an open-source web application security testing tool.

It includes features for crawling applications and identifying potential security vulnerabilities.

It can be useful during the initial assessment of an application, although automated results should always be verified manually.

### 3. Dalfox

Website: [https://github.com/hahwul/dalfox](https://github.com/hahwul/dalfox)

Dalfox is an open-source tool designed for finding and analyzing XSS vulnerabilities.

It supports different testing techniques and can help identify potentially vulnerable parameters.

I consider tools like this useful for supporting manual testing, rather than replacing an understanding of the application’s behavior.

### 4. XSStrike

Website: [https://github.com/s0md3v/XSStrike](https://github.com/s0md3v/XSStrike)

XSStrike is an XSS detection tool that analyzes application behavior and helps identify potential XSS issues.

It is useful as a learning and testing resource, although compatibility and maintenance should be checked before using it in an assessment.

### 5. PortSwigger Web Security Academy

Website: [https://portswigger.net/web-security/cross-site-scripting](https://portswigger.net/web-security/cross-site-scripting)

This is one of the resources I recommend to anyone learning XSS.

It provides detailed explanations and practical labs covering reflected, stored, and DOM-based XSS.

The labs provide a controlled environment where I can understand how different XSS vulnerabilities work.

### 6. Understanding the Impact of XSS

The impact of XSS depends on where the vulnerability exists, who can trigger it, and what privileges are available in the affected browser session.

A successful XSS vulnerability may allow an attacker to perform actions such as:

- Modify webpage content.
- Display misleading information.
- Redirect users to unwanted websites.
- Perform unauthorized actions within the victim’s session, depending on application protections.
- Access sensitive information available to JavaScript.
- Interact with application features using the victim’s browser context.

One important point is that session cookies marked with the HttpOnly attribute cannot normally be accessed through JavaScript.

However, HttpOnly cookies do not completely prevent XSS from being dangerous. Injected scripts may still be able to perform actions through the victim’s authenticated browser session.

This is why I never judge an XSS vulnerability only by whether cookies can be accessed.

I consider the actual application functionality and the demonstrated security impact.

### 7. Real-World XSS Vulnerabilities

XSS is not just a theoretical security issue. Vulnerabilities continue to appear in different types of applications and software.

When researching security issues, I also look at publicly disclosed vulnerabilities to understand how developers introduce XSS and how researchers discover it.

Some examples worth investigating include:

- **CVE-2025–34408:** A reported XSS-related vulnerability associated with MailEnable.
- **CVE-2025–50538:** A reported XSS vulnerability associated with Flowise.
- **CVE-2025–65442:** A reported DOM-based XSS issue.

Before publishing technical claims about individual CVEs, I recommend checking their official CVE records and vendor advisories for the affected versions, root cause, and impact.

Studying real vulnerability reports helps me understand how XSS appears in actual applications rather than only in laboratory examples.

### 8. How Developers Can Prevent XSS

Finding XSS vulnerabilities is important, but understanding how to prevent them is equally valuable.

Here are some security practices developers should follow.

### 1. Use Context-Aware Output Encoding

This is one of the most important defenses against XSS.

Developers should encode untrusted data based on where it will appear.

For example, HTML body content, HTML attributes, JavaScript strings, and URLs require different encoding rules.

### 2. Use Safe DOM Methods

Avoid placing untrusted content directly into dangerous DOM sinks.

For example:

// Safer way to display user-provided text

element.textContent = userInput;

Prefer textContent when displaying plain text instead of using innerHTML.

### 3. Implement a Strong CSP

Content Security Policy provides an additional security layer.

A well-configured policy using nonces or hashes can help restrict which scripts are allowed to execute.

However, CSP should be treated as defense-in-depth, not the main solution.

### 4. Validate User Input

Applications should validate input according to expected formats, lengths, and business requirements.

For example, an email field should follow the expected email format.

However, input validation alone cannot guarantee protection against XSS.

### 5. Use Trusted HTML Sanitization Libraries

Some applications legitimately allow users to submit formatted HTML.

For these features, developers should use trusted and actively maintained HTML sanitization libraries such as DOMPurify.

Writing custom filtering rules using regular expressions is generally not a reliable solution.

### 6. Secure Session Cookies

Developers should configure session cookies with appropriate security attributes.

Important cookie attributes include:

- HttpOnly
- Secure
- SameSite

These settings help reduce certain risks associated with session theft and cross-site requests.

They do not replace proper XSS prevention.

### 9. How I Prepare an XSS Bug Bounty Report

After confirming an XSS vulnerability, I focus on preparing a clear report.

A good report should explain the vulnerable location, the affected users, and the actual security impact.

Here is the structure I generally follow:

**Title:** Clearly mention the XSS type and affected functionality.

**Summary:** Explain where the issue exists and how it occurs.

**Affected Endpoint:** Include the relevant URL or application feature.

**Steps to Reproduce:** Explain the testing process step by step.

**Proof of Concept:** Provide a safe demonstration showing that the browser interprets the content as executable code.

**Impact:** Explain which users are affected and what security consequences are demonstrated.

**Remediation:** Recommend context-aware output encoding, safe DOM APIs, and other relevant protections.

I also include screenshots or short recordings when they help demonstrate the issue.

Most importantly, I avoid exaggerated claims. The severity should reflect the actual impact and the conditions required for exploitation.

### Final Thoughts

XSS is one of those vulnerabilities that teaches us a lot about how browsers and web applications work together.

Finding it is not simply about entering JavaScript into a form and waiting for an alert box.

It requires understanding where user input comes from, how the application processes it, and where that information eventually reaches the browser.

During my bug bounty journey, I have learned that understanding application behavior is much more useful than blindly trying hundreds of payloads.

Tools like Burp Suite, Dalfox, and OWASP ZAP can support the process, but manual investigation and proper verification remain important.

If you are starting your bug bounty journey, I recommend learning the basics of HTML, JavaScript, browser DOM behavior, and HTTP requests before moving toward advanced XSS testing.

**Remember: The real problem is not accepting user input. The problem is allowing untrusted input to become executable code in the browser.**

*AI assistance: I used an AI-powered grammar and spelling checker to review this article. The ideas, research, technical analysis, and final content are my own.*

*Have questions or want to share your own workflow? Drop a comment below or connect with me on :*

🔗Linkdin: [https://www.linkedin.com/company/sam-shield/](https://www.linkedin.com/company/sam-shield/)

🔗Youtube: [https://www.youtube.com/@sam\_shield-w7l](https://www.youtube.com/@sam_shield-w7l)

🔗Medium: [https://medium.com/@samadhanshimple](https://medium.com/@samadhanshimple)
