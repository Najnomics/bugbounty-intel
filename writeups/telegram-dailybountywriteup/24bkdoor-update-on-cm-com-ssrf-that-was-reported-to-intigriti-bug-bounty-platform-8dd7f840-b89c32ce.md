# Update on CM.com SSRF that was reported to Intigriti Bug Bounty Platform

- **Source URL:** https://medium.com/@24bkdoor/update-on-cm-com-ssrf-that-was-reported-to-intigriti-bug-bounty-platform-8dd7f840c6a2?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20240105161859/https://medium.com/@24bkdoor/update-on-cm-com-ssrf-that-was-reported-to-intigriti-bug-bounty-platform-8dd7f840c6a2?source=rss------bug_bounty-5
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/4230 (id 4230)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Update on CM.com SSRF that was reported to Intigriti Bug Bounty Platform

How Intigriti ch\*\*ted me out of SSRF like HackerOne did —Educational Ethcical Purposes for Educational stuff

# How it started:

I identified a Server-Side Request Forgery (SSRF) vulnerability on the URL: [https://sso.sandbox.pay.cm.com/auth/realms/master/protocol/openid-connect/auth?scope=openid&response\_type=code&redirect\_uri=valid&state=cfx&nonce=cfx&client\_id=security-admin-console&request\_uri=https://b163–96-127-25-108.ngrok-free.app/](https://web.archive.org/web/20240105161859/https://sso.sandbox.pay.cm.com/auth/realms/master/protocol/openid-connect/auth?scope=openid&response_type=code&redirect_uri=valid&state=cfx&nonce=cfx&client_id=security-admin-console&request_uri=https%3A%2F%2Fb163-86-167-25-178.ngrok-free.app%2F). This vulnerability could potentially allow an attacker to make requests to internal resources within the server environment. Furthermore, it appears that the server is vulnerable to a ping-back SSRF, as it responds to requests made to an external listener.

# What is SSRF?

SSRF occurs when an attacker manipulates a server into making requests to other servers or services, either within the internal network or on the internet. This manipulation can lead to unexpected behaviors, including exposure of sensitive information or denial of service.


# Vulnerability Details:

Vulnerability Type: Server-Side Request Forgery (SSRF)

Affected URL: [https://sso.sandbox.pay.cm.com/auth/realms/master/protocol/openid-connect/auth?scope=openid&response\_type=code&redirect\_uri=valid&state=cfx&nonce=cfx&client\_id=security-admin-console&request\_uri=https://](https://web.archive.org/web/20240105161859/https://sso.sandbox.pay.cm.com/auth/realms/master/protocol/openid-connect/auth?scope=openid&response_type=code&redirect_uri=valid&state=cfx&nonce=cfx&client_id=security-admin-console&request_uri=https%3A%2F%2Fb163-86-167-25-178.ngrok-free.app%2F)[b163–96–127–25–108.ngrok-free.app](https://web.archive.org/web/20240105161859/https://sso.sandbox.pay.cm.com/auth/realms/master/protocol/openid-connect/auth?scope=openid&response_type=code&redirect_uri=valid&state=cfx&nonce=cfx&client_id=security-admin-console&request_uri=https%3A%2F%2Fb163-86-167-25-178.ngrok-free.app%2F)[.ngrok-free.app/](https://web.archive.org/web/20240105161859/https://sso.sandbox.pay.cm.com/auth/realms/master/protocol/openid-connect/auth?scope=openid&response_type=code&redirect_uri=valid&state=cfx&nonce=cfx&client_id=security-admin-console&request_uri=https%3A%2F%2Fb163-86-167-25-178.ngrok-free.app%2F)

Payload Used: I used a simple SSRF payload to demonstrate the vulnerability: [https://b163-86-167-25-178.ngrok-free.app/](https://web.archive.org/web/20240105161859/https://b163-86-167-25-178.ngrok-free.app/)

# Steps to Reproduce:

Navigate to the provided vulnerable URL.

Observe that the server sends a request to the specified request\_uri.

The server’s response includes the content served by the external listener, confirming the SSRF vulnerability.

# Impact:

An attacker could exploit this SSRF vulnerability to perform various attacks, such as scanning internal networks, accessing sensitive resources, or abusing the server’s functionality to attack other systems. The ability to ping back to an external listener indicates a potential security breach. A ping back alone is often not enough so we must explore further.

# Recommendation:

Immediate Action: I strongly recommend disabling external requests from the server to untrusted URLs. Validate and sanitize user-supplied input thoroughly to prevent SSRF attacks.

Detailed Investigation: Conduct a thorough security audit to identify and patch any similar SSRF vulnerabilities across the application.

Educate Developers: Ensure your development team is aware of SSRF risks and security best practices.

# SSRF and its Impact on Gateway Timeouts

[https://sso.sandbox.pay.cm.com/auth/realms/master/protocol/openid-connect/auth?scope=openid&response\_type=code&redirect\_uri=valid&state=cfx&nonce=cfx&client\_id=security-admin-console&request\_uri=https://](https://web.archive.org/web/20240105161859/https://sso.sandbox.pay.cm.com/auth/realms/master/protocol/openid-connect/auth?scope=openid&response_type=code&redirect_uri=valid&state=cfx&nonce=cfx&client_id=security-admin-console&request_uri=https%3A%2F%2Fb163-86-167-25-178.ngrok-free.app%2F)[b163–96–127–25–108.ngrok-free.app](https://web.archive.org/web/20240105161859/https://sso.sandbox.pay.cm.com/auth/realms/master/protocol/openid-connect/auth?scope=openid&response_type=code&redirect_uri=valid&state=cfx&nonce=cfx&client_id=security-admin-console&request_uri=https%3A%2F%2Fb163-86-167-25-178.ngrok-free.app%2F)[/](https://web.archive.org/web/20240105161859/https://sso.sandbox.pay.cm.com/auth/realms/master/protocol/openid-connect/auth?scope=openid&response_type=code&redirect_uri=valid&state=cfx&nonce=cfx&client_id=security-admin-console&request_uri=https%3A%2F%2Fb163-86-167-25-178.ngrok-free.app%2F)

Server-side request Forgery (SSRF) vulnerabilities pose significant risks to web applications, potentially leading to gateway timeouts, especially when attackers exploit these vulnerabilities strategically. Here’s how this scenario unfolds:

***1. Attacker Initiates SSRF:***
 An attacker leverages an SSRF vulnerability to coerce the targeted server into sending requests to other servers or services, either within the internal network or on the internet.

***2. Slow or Unresponsive Service:***
 If the SSRF request is directed towards a slow or unresponsive service, the server might linger, waiting for a response. In cases where the targeted service delays its reply, the SSRF request can take an excessive amount of time to complete.

***3. Resource Exhaustion:***
 When multiple SSRF requests are sent concurrently, or if the slow service blocks resources, it can strain the server’s resources like threads and connections. This resource exhaustion can significantly impact the server’s performance.

***4. Timeouts Occur:***
 Inadequate timeout configurations exacerbate the problem. If SSRF requests lack proper timeout settings, they might linger indefinitely, causing downstream systems like load balancers and proxy servers to wait for responses.

***5. Gateway Timeouts:***
 As a consequence, downstream systems may experience prolonged delays and might fail to receive timely responses from the server due to SSRF-induced delays. This delay often results in gateway timeout errors, indicating that the server couldn’t respond within the expected timeframe.

# Security Implications:

***1. Denial of Service (DoS) Potential:***
 — Impact on Availability: SSRF-exploited gateway timeouts can lead to a Denial of Service (DoS) situation, rendering services inaccessible to legitimate users due to resource exhaustion.


***2. Abuse of Resources:***
 — System Instability: The abuse of server resources by SSRF-induced timeouts can destabilize the system, causing legitimate users to experience degraded service or even system crashes.

***3. Concealed Malicious Activities:***
 — Distraction Tactic: Attackers may intentionally use SSRF to cause gateway timeouts as a distraction. While defenders address timeouts, attackers might execute other malicious activities discreetly, exploiting the chaos caused by the DoS situation.

***4. Evasion of Security Measures:***
 — Interference with Security Systems: SSRF-induced timeouts might interfere with security mechanisms like intrusion detection systems, enabling attackers to evade security monitoring and alerting systems.

# Mitigating SSRF Risks:

To counter SSRF-induced gateway timeouts and their security implications:

\- Proper Timeout Configurations:

— Ensure all SSRF requests have appropriate timeout settings, limiting the impact of slow or unresponsive services on overall system performance.

\- Rate Limiting and Security Controls:

— Implement rate limiting mechanisms and other security controls to prevent abuse of resources, safeguarding against SSRF attacks.

\- Traffic Monitoring:

— Regularly monitor network traffic patterns, especially during peak usage times, to promptly identify and respond to potential SSRF attacks.

By understanding the dynamics of SSRF vulnerabilities and their potential impact on gateway timeouts, organizations can proactively implement robust security measures, fortifying their applications against exploitation and ensuring a secure online environment for all users.

Large companies typically have robust infrastructure and security measures in place to handle a wide array of security threats, including SSRF vulnerabilities. However, the impact of SSRF-induced timeouts or Denial of Service (DoS) attacks can vary based on several factors:


Targeted Services: If an SSRF attack targets a critical internal service or an external service with limited resources, it can lead to timeouts and service degradation.

Volume of Requests: While large companies might handle regular traffic well, a sudden influx of malicious requests can strain even the most robust systems, potentially leading to temporary disruptions.

Duration of Attack: Prolonged attacks can have a more significant impact, especially if they coincide with other high-traffic events, making it challenging for security teams to distinguish legitimate traffic from malicious requests.

Concealed Attacks: Attackers might use SSRF as a distraction, exploiting timeouts to mask other malicious activities within the chaos created by the DoS situation.

Security Architecture: The effectiveness of security measures, such as rate limiting, intrusion detection systems, and monitoring, plays a crucial role. If these defenses aren’t configured optimally, SSRF attacks could bypass them.

While it might not always be immediately apparent to end-users, companies invest heavily in security to prevent and mitigate such attacks. However, the dynamic nature of cybersecurity means that constant vigilance and proactive measures are necessary to stay ahead of evolving threats.

Additionally, even large companies can face SSRF vulnerabilities, especially in complex web applications with numerous components and integrations.

# Expanding on SSRF Vulnerabilities and Their Impact on Large Companies

Server-Side Request Forgery (SSRF) vulnerabilities are intricate and potent, posing significant challenges to the security of web applications, even for large companies with robust infrastructures. When attackers strategically exploit SSRF vulnerabilities, it can lead to a cascade of consequences, especially in the context of large organizations:

## Targeted Services and Resource Strain:

— \*Focused Attacks:\* Attackers may pinpoint critical internal services or external services with limited resources. Targeting such services can lead to server overloads, impacting performance and potentially causing interruptions in service.

— \*Resource Drain:\* Large companies often have numerous interconnected services. A relentless barrage of SSRF requests can strain internal resources, causing slowdowns, resource exhaustion, and degradation of services, affecting not only the targeted service but also interconnected services.

## Handling Massive Traffic Volume:

— \*Resource Allocation Challenges:\* While large companies are equipped to handle regular traffic, a sudden surge in malicious requests can challenge resource allocation. Managing the influx becomes complicated, potentially leading to service disruptions and slowdowns in critical functions.

— \*Load Balancer Impact:\* Load balancers, designed to evenly distribute traffic, may struggle to differentiate between legitimate and malicious requests during high-intensity SSRF attacks. This difficulty can hinder their effectiveness, allowing malicious traffic to bypass normal traffic shaping mechanisms.

## Prolonged Attacks and Concealed Malicious Activities:

— \*Persistence of Attacks:\* Prolonged SSRF attacks compound the impact, making it harder for security teams to mitigate the situation effectively. The continued strain on resources can lead to extended service degradation, negatively affecting user experience.

— \*Distraction and Evasion:\* Attackers exploit SSRF-induced chaos as a distraction. While security teams grapple with mitigating gateway timeouts, attackers may execute other malicious activities, such as exfiltrating sensitive data or planting malware, taking advantage of the security team’s diverted focus.

## Challenges in Security Architecture and Adaptability:

— \*Defensive Measures:\* Large companies employ various security measures, such as rate limiting, intrusion detection systems, and monitoring tools. However, SSRF attacks, especially when crafted to bypass these defenses, can challenge the effectiveness of these security mechanisms.

— \*Complex Web Ecosystems:\* Complex web applications with multiple integrations provide numerous entry points for SSRF vulnerabilities. Identifying and securing each potential weak link demands a meticulous approach, and even a single oversight can lead to exploitation.

# Vigilance and Continuous Improvement:

SSRF vulnerabilities represent a persistent challenge, even for large companies. The ever-evolving landscape of cybersecurity demands continuous vigilance, adaptation, and improvement of security measures. Companies must invest not only in state-of-the-art technologies but also in skilled professionals who can proactively identify vulnerabilities, fortify defenses, and respond swiftly to emerging threats. By embracing a proactive security culture and staying ahead of the curve, even large organizations can navigate the complexities of SSRF vulnerabilities and protect their digital assets effectively.

Server-side request Forgery (SSRF) vulnerabilities pose significant threats to web applications, allowing attackers to manipulate server requests and potentially leading to severe security risks. In this article, we’ll explore the nature of SSRF vulnerabilities, the risks they entail, and the responsible disclosure process.

# Proof of Concept Scenarios:

***1. Fetching Localhost Resources:***
Consider a web application that allows users to input a URL and fetch its content. The vulnerable code might look like this in PHP:

```
<?php
$url = $_GET['url'];
$content = file_get_contents($url);
echo $content;
?>
```
An attacker can exploit this vulnerability by providing a malicious URL, such as \`[http://localhost:8080/admin\`](https://web.archive.org/web/20240105161859/http://localhost:8080/admin`), potentially exposing sensitive information.

***2. Attempting Access to Specific Ports:***
By manipulating the \`request\_uri\` parameter, an attacker can attempt to access different ports on the server. For instance:

\- \`[https://sso.sandbox.pay.cm.com/auth/realms/master/protocol/openid-connect/auth?scope=openid&response\_type=code&redirect\_uri=valid&state=cfx&nonce=cfx&client\_id=security-admin-console&request\_uri=https://5ea1-86-167-25-178.ngrok-free.app/\`](https://web.archive.org/web/20240105161859/https://sso.sandbox.pay.cm.com/auth/realms/master/protocol/openid-connect/auth?scope=openid&response_type=code&redirect_uri=valid&state=cfx&nonce=cfx&client_id=security-admin-console&request_uri=https%3A%2F%2F5ea1-86-167-25-178.ngrok-free.app%2F%60) — This URL attempts to fetch content from a specific endpoint and port, potentially exploiting open ports.

\- \`[https://sso.sandbox.pay.cm.com/auth/realms/master/protocol/openid-connect/auth?scope=openid&response\_type=code&redirect\_uri=valid&state=cfx&nonce=cfx&client\_id=security-admin-console&request\_uri=http://sso.sandbox.pay.cm.com:8000\`](https://web.archive.org/web/20240105161859/https://sso.sandbox.pay.cm.com/auth/realms/master/protocol/openid-connect/auth?scope=openid&response_type=code&redirect_uri=valid&state=cfx&nonce=cfx&client_id=security-admin-console&request_uri=http%3A%2F%2Fsso.sandbox.pay.cm.com%3A8000%60) — Here, the attacker is trying to identify open ports by specifying different port numbers.

# Responsible Disclosure:

When security researchers discover vulnerabilities, responsible disclosure is crucial. It involves reporting the issue to the organization or vendor, allowing them time to fix the problem before public disclosure. However, this process can sometimes be challenging, as not all organizations fully understand the severity of reported vulnerabilities.

# Challenges in Responsible Disclosure:

In some cases, security researchers face challenges in communicating the intricacies of SSRF vulnerabilities to organizations. This was demonstrated when a researcher reported an SSRF vulnerability to an organization. The researcher provided detailed information about the vulnerability, including PoC URLs and possible attack scenarios. Despite the researcher’s efforts, the organization struggled to understand the issue initially, leading to delays in the resolution process.

Consider a web application that allows users to input a URL and fetch its content. The application uses an SSRF-vulnerable function to fetch the content of the provided URL. The vulnerable code might look like this in a server-side scripting language (e.g., PHP):

```
<?php
// Get the URL from user input (vulnerable parameter)
$url = $_GET['url'];
// Fetch content from the provided URL (SSRF vulnerability)
$content = file_get_contents($url);
// Display the fetched content
echo $content;
?>
```
In this scenario, an attacker can manipulate the \`url\` parameter to exploit the SSRF vulnerability. For example, the attacker could craft a malicious URL like this:

`http://localhost:8080/admin`
When this URL is provided as input, the server would attempt to fetch the content of the \`[http://localhost:8080/admin\`](https://web.archive.org/web/20240105161859/http://localhost:8080/admin`) page, potentially exposing sensitive information.

To prevent SSRF attacks, it’s crucial to validate and sanitize user input and restrict the URLs that the application can access. Implementing proper input validation, whitelisting acceptable URLs, and configuring appropriate timeouts are essential security practices to mitigate SSRF vulnerabilities.

# To sum things up:

SSRF vulnerabilities can have far-reaching consequences, making it essential for organizations to have robust security measures in place. Responsible disclosure is a vital aspect of improving web security. While security researchers play a critical role in identifying vulnerabilities, organizations must be receptive and proactive in addressing reported issues to ensure a secure digital environment for users.

# Recap

[https://sso.sandbox.pay.cm.com/auth/realms/master/protocol/openid-connect/auth?scope=openid&response\_type=code&redirect\_uri=valid&state=cfx&nonce=cfx&client\_id=security-admin-console&request\_uri=https://](https://web.archive.org/web/20240105161859/https://sso.sandbox.pay.cm.com/auth/realms/master/protocol/openid-connect/auth?scope=openid&response_type=code&redirect_uri=valid&state=cfx&nonce=cfx&client_id=security-admin-console&request_uri=https%3A%2F%2F5ea1-86-167-25-178.ngrok-free.app%2F)[b163–96–127–25–108.ngrok-free.app](https://web.archive.org/web/20240105161859/https://sso.sandbox.pay.cm.com/auth/realms/master/protocol/openid-connect/auth?scope=openid&response_type=code&redirect_uri=valid&state=cfx&nonce=cfx&client_id=security-admin-console&request_uri=https%3A%2F%2Fb163-86-167-25-178.ngrok-free.app%2F)[/](https://web.archive.org/web/20240105161859/https://sso.sandbox.pay.cm.com/auth/realms/master/protocol/openid-connect/auth?scope=openid&response_type=code&redirect_uri=valid&state=cfx&nonce=cfx&client_id=security-admin-console&request_uri=https%3A%2F%2F5ea1-86-167-25-178.ngrok-free.app%2F) — 504 gateway time out

[https://sso.sandbox.pay.cm.com/auth/realms/master/protocol/openid-connect/auth?scope=openid&response\_type=code&redirect\_uri=valid&state=cfx&nonce=cfx&client\_id=security-admin-console&request\_uri=https://](https://web.archive.org/web/20240105161859/https://sso.sandbox.pay.cm.com/auth/realms/master/protocol/openid-connect/auth?scope=openid&response_type=code&redirect_uri=valid&state=cfx&nonce=cfx&client_id=security-admin-console&request_uri=https%3A%2F%2F5ea1-86-167-25-178.ngrok-free.app)[b163–96–127–25–108.ngrok-free.app](https://web.archive.org/web/20240105161859/https://sso.sandbox.pay.cm.com/auth/realms/master/protocol/openid-connect/auth?scope=openid&response_type=code&redirect_uri=valid&state=cfx&nonce=cfx&client_id=security-admin-console&request_uri=https%3A%2F%2Fb163-86-167-25-178.ngrok-free.app%2F)

[https://sso.sandbox.pay.cm.com/auth/realms/master/protocol/openid-connect/auth?scope=openid&response\_type=code&redirect\_uri=valid&state=cfx&nonce=cfx&client\_id=security-admin-console&request\_uri=http://sso.sandbox.pay.cm.com:8000](https://web.archive.org/web/20240105161859/https://sso.sandbox.pay.cm.com/auth/realms/master/protocol/openid-connect/auth?scope=openid&response_type=code&redirect_uri=valid&state=cfx&nonce=cfx&client_id=security-admin-console&request_uri=http%3A%2F%2Fsso.sandbox.pay.cm.com%3A8000) — this is how we try to see what ports are open

After reporting this to Intigriti, they did not understand what SSRF is. The first handler closed it as N/A. They then reopened it as their fix failed and asked for more information. I gave more information. After a few days, they then closed it as Out of Scope. They then implemented a fix and closed my report.

Now, here we are. Publicly informing you. They are the same as HackerOne and I am showing you this so that you understand why I disclosed.

`curl 'http://sso.sandbox.pay.cm.com:80/auth/realms/master/protocol/openid-connect/auth?scope=openid&response_type=code&redirect_uri=valid&state=cfx&nonce=cfx&client_id=security-admin-console&request_uri=https://5ea1-86-167-25-178.ngrok-free.app/' -t ~/malicious-file -i -L -vvv -A '127.0.0.1'`
\* processing: [http://sso.sandbox.pay.cm.com:80/auth/realms/master/protocol/openid-connect/auth?scope=openid&response\_type=code&redirect\_uri=valid&state=cfx&nonce=cfx&client\_id=security-admin-console&request\_uri=https://](https://web.archive.org/web/20240105161859/http://sso.sandbox.pay.cm.com:80/auth/realms/master/protocol/openid-connect/auth?scope=openid&response_type=code&redirect_uri=valid&state=cfx&nonce=cfx&client_id=security-admin-console&request_uri=https%3A%2F%2F5ea1-86-167-25-178.ngrok-free.app%2F)[b163–96–127–25–108.ngrok-free.app](https://web.archive.org/web/20240105161859/https://sso.sandbox.pay.cm.com/auth/realms/master/protocol/openid-connect/auth?scope=openid&response_type=code&redirect_uri=valid&state=cfx&nonce=cfx&client_id=security-admin-console&request_uri=https%3A%2F%2Fb163-86-167-25-178.ngrok-free.app%2F)[/](https://web.archive.org/web/20240105161859/http://sso.sandbox.pay.cm.com:80/auth/realms/master/protocol/openid-connect/auth?scope=openid&response_type=code&redirect_uri=valid&state=cfx&nonce=cfx&client_id=security-admin-console&request_uri=https%3A%2F%2F5ea1-86-167-25-178.ngrok-free.app%2F)

\* Trying 104.16.121.74:80…

\* Trying \[2606:4700::6812:c314\]:80…

\< HTTP/1.1 301 Moved Permanently

HTTP/1.1 301 Moved Permanently

\< Date: Tue, 24 Oct 2023 18:43:16 GMT

Date: Tue, 24 Oct 2023 18:43:16 GMT

\< Transfer-Encoding: chunked

Transfer-Encoding: chunked

\< Connection: keep-alive

Connection: keep-alive

\< Cache-Control: max-age=3600

Cache-Control: max-age=3600

\< Expires: Tue, 24 Oct 2023 19:43:16 GMT

Expires: Tue, 24 Oct 2023 19:43:16 GMT

\< Location: [https://sso.sandbox.pay.cm.com/auth/realms/master/protocol/openid-connect/auth?scope=openid&response\_type=code&redirect\_uri=valid&state=cfx&nonce=cfx&client\_id=security-admin-console&request\_uri=https://](https://web.archive.org/web/20240105161859/https://sso.sandbox.pay.cm.com/auth/realms/master/protocol/openid-connect/auth?scope=openid&response_type=code&redirect_uri=valid&state=cfx&nonce=cfx&client_id=security-admin-console&request_uri=https%3A%2F%2F5ea1-86-167-25-178.ngrok-free.app%2F)[b163–96–127–25–108.ngrok-free.app](https://web.archive.org/web/20240105161859/https://sso.sandbox.pay.cm.com/auth/realms/master/protocol/openid-connect/auth?scope=openid&response_type=code&redirect_uri=valid&state=cfx&nonce=cfx&client_id=security-admin-console&request_uri=https%3A%2F%2Fb163-86-167-25-178.ngrok-free.app%2F)[/](https://web.archive.org/web/20240105161859/https://sso.sandbox.pay.cm.com/auth/realms/master/protocol/openid-connect/auth?scope=openid&response_type=code&redirect_uri=valid&state=cfx&nonce=cfx&client_id=security-admin-console&request_uri=https%3A%2F%2F5ea1-86-167-25-178.ngrok-free.app%2F)

Location: [https://sso.sandbox.pay.cm.com/auth/realms/master/protocol/openid-connect/auth?scope=openid&response\_type=code&redirect\_uri=valid&state=cfx&nonce=cfx&client\_id=security-admin-console&request\_uri=https://](https://web.archive.org/web/20240105161859/https://sso.sandbox.pay.cm.com/auth/realms/master/protocol/openid-connect/auth?scope=openid&response_type=code&redirect_uri=valid&state=cfx&nonce=cfx&client_id=security-admin-console&request_uri=https%3A%2F%2F5ea1-86-167-25-178.ngrok-free.app%2F)[b163–96–127–25–108.ngrok-free.app](https://web.archive.org/web/20240105161859/https://sso.sandbox.pay.cm.com/auth/realms/master/protocol/openid-connect/auth?scope=openid&response_type=code&redirect_uri=valid&state=cfx&nonce=cfx&client_id=security-admin-console&request_uri=https%3A%2F%2Fb163-86-167-25-178.ngrok-free.app%2F)[/](https://web.archive.org/web/20240105161859/https://sso.sandbox.pay.cm.com/auth/realms/master/protocol/openid-connect/auth?scope=openid&response_type=code&redirect_uri=valid&state=cfx&nonce=cfx&client_id=security-admin-console&request_uri=https%3A%2F%2F5ea1-86-167-25-178.ngrok-free.app%2F)

\< Set-Cookie: \_cfuvid={redacted}

\<

\* Ignoring the response-body

\* Connection #0 to host sso.sandbox.pay.cm.com left intact

\* Clear auth, redirects to port from 80 to 443

\* Issue another request to this URL: ‘[https://sso.sandbox.pay.cm.com/auth/realms/master/protocol/openid-connect/auth?scope=openid&response\_type=code&redirect\_uri=valid&state=cfx&nonce=cfx&client\_id=security-admin-console&request\_uri=https://](https://web.archive.org/web/20240105161859/https://sso.sandbox.pay.cm.com/auth/realms/master/protocol/openid-connect/auth?scope=openid&response_type=code&redirect_uri=valid&state=cfx&nonce=cfx&client_id=security-admin-console&request_uri=https%3A%2F%2F5ea1-86-167-25-178.ngrok-free.app%2F%27)[b163–96–127–25–108.ngrok-free.app](https://web.archive.org/web/20240105161859/https://sso.sandbox.pay.cm.com/auth/realms/master/protocol/openid-connect/auth?scope=openid&response_type=code&redirect_uri=valid&state=cfx&nonce=cfx&client_id=security-admin-console&request_uri=https%3A%2F%2Fb163-86-167-25-178.ngrok-free.app%2F)[/'](https://web.archive.org/web/20240105161859/https://sso.sandbox.pay.cm.com/auth/realms/master/protocol/openid-connect/auth?scope=openid&response_type=code&redirect_uri=valid&state=cfx&nonce=cfx&client_id=security-admin-console&request_uri=https%3A%2F%2F5ea1-86-167-25-178.ngrok-free.app%2F%27)

\* Trying 104.16.121.74:443…

\* Trying \[2606:4700::6812:c314\]:443…

\* Connected to sso.sandbox.pay.cm.com (104.16.121.74) port 443

\* ALPN: offers h2,http/1.1

\* TLSv1.3 (OUT), TLS handshake, Client hello (1):

\* CAfile: /etc/ssl/certs/ca-certificates.crt

\* CApath: /etc/ssl/certs

\<

\* Ignoring the response-body

\* Connection #0 to host sso.sandbox.pay.cm.com left intact

\* Clear auth, redirects to port from 80 to 443

\* Issue another request to this URL: ‘[https://sso.sandbox.pay.cm.com/auth/realms/master/protocol/openid-connect/auth?scope=openid&response\_type=code&redirect\_uri=valid&state=cfx&nonce=cfx&client\_id=security-admin-console&request\_uri=https://](https://web.archive.org/web/20240105161859/https://sso.sandbox.pay.cm.com/auth/realms/master/protocol/openid-connect/auth?scope=openid&response_type=code&redirect_uri=valid&state=cfx&nonce=cfx&client_id=security-admin-console&request_uri=https%3A%2F%2F5ea1-86-167-25-178.ngrok-free.app%2F%27)[b163–96–127–25–108.ngrok-free.app](https://web.archive.org/web/20240105161859/https://sso.sandbox.pay.cm.com/auth/realms/master/protocol/openid-connect/auth?scope=openid&response_type=code&redirect_uri=valid&state=cfx&nonce=cfx&client_id=security-admin-console&request_uri=https%3A%2F%2Fb163-86-167-25-178.ngrok-free.app%2F)[/'](https://web.archive.org/web/20240105161859/https://sso.sandbox.pay.cm.com/auth/realms/master/protocol/openid-connect/auth?scope=openid&response_type=code&redirect_uri=valid&state=cfx&nonce=cfx&client_id=security-admin-console&request_uri=https%3A%2F%2F5ea1-86-167-25-178.ngrok-free.app%2F%27)

\* Trying 104.16.121.74:443…

\* Trying \[2606:4700::6812:c314\]:443…

- Connected to sso.sandbox.pay.cm.com (104.16.121.74) port 443
\* ALPN: offers h2,http/1.1
\* TLSv1.3 (OUT), TLS handshake, Client hello (1):
\* CAfile: /etc/ssl/certs/ca-certificates.crt
\* CApath: /etc/ssl/certs
- The rest is redacted

# What did we find out?

Server-side request Forgery (SSRF) vulnerabilities pose substantial risks to web applications, potentially causing gateway timeouts, especially when attackers exploit these vulnerabilities strategically. Here’s how this scenario unfolds:

***1. Attacker Initiates SSRF:***
 An attacker leverages an SSRF vulnerability to coerce the targeted server into sending requests to other servers or services, either within the internal network or on the internet.

***2. Slow or Unresponsive Service:***
 If the SSRF request is directed towards a slow or unresponsive service, the server might linger, waiting for a response. In cases where the targeted service delays its reply, the SSRF request can take an excessive amount of time to complete.

***3. Resource Exhaustion:***
 When multiple SSRF requests are sent concurrently, or if the slow service blocks resources, it can strain the server’s resources like threads and connections. This resource exhaustion can significantly impact the server’s performance.

***4. Timeouts Occur:***
 Inadequate timeout configurations exacerbate the problem. If SSRF requests lack proper timeout settings, they might linger indefinitely, causing downstream systems like load balancers and proxy servers to wait for responses.

***5. Gateway Timeouts:***
 As a consequence, downstream systems may experience prolonged delays and might fail to receive timely responses from the server due to SSRF-induced delays. This delay often results in gateway timeout errors, indicating that the server couldn’t respond within the expected timeframe.

# Security Implications:

***1. Denial of Service (DoS) Potential:***
 — Impact on Availability: SSRF-exploited gateway timeouts can lead to a Denial of Service (DoS) situation, rendering services inaccessible to legitimate users due to resource exhaustion.

***2. Abuse of Resources:***
 — System Instability: The abuse of server resources by SSRF-induced timeouts can destabilize the system, causing legitimate users to experience degraded service or even system crashes.

***3. Concealed Malicious Activities:***
 — Distraction Tactic: Attackers may intentionally use SSRF to cause gateway timeouts as a distraction. While defenders address timeouts, attackers might execute other malicious activities discreetly, exploiting the chaos caused by the DoS situation.

***4. Evasion of Security Measures:***
 — Interference with Security Systems: SSRF-induced timeouts might interfere with security mechanisms like intrusion detection systems, enabling attackers to evade security monitoring and alerting systems.

# Mitigating SSRF Risks:

To counter SSRF-induced gateway timeouts and their security implications:

\- Proper Timeout Configurations:

— Ensure all SSRF requests have appropriate timeout settings, limiting the impact of slow or unresponsive services on overall system performance.

\- Rate Limiting and Security Controls:

— Implement rate limiting mechanisms and other security controls to prevent abuse of resources, safeguarding against SSRF attacks.

\- Traffic Monitoring:

— Regularly monitor network traffic patterns, especially during peak usage times, to promptly identify and respond to potential SSRF attacks.

By understanding the dynamics of SSRF vulnerabilities and their potential impact on gateway timeouts, organizations can proactively implement robust security measures, fortifying their applications against exploitation and ensuring a secure online environment for all users.

— -

# Expanding on SSRF Vulnerabilities and Their Impact on Large Companies

Server-Side Request Forgery (SSRF) vulnerabilities are intricate and potent, posing significant challenges to the security of web applications, even for large companies with robust infrastructures. When attackers strategically exploit SSRF vulnerabilities, it can lead to a cascade of consequences, especially in the context of large organizations:

***1. Targeted Services and Resource Strain:***
 — \*Focused Attacks:\* Attackers may pinpoint critical internal services or external services with limited resources. Targeting such services can lead to server overloads, impacting performance and potentially causing interruptions in service.

— \*Resource Drain:\* Large companies often have numerous interconnected services. A relentless barrage of SSRF requests can strain internal resources, causing slowdowns, resource exhaustion, and degradation of services, affecting not only the targeted service but also interconnected services.

***2. Handling Massive Traffic Volume:***
 — \*Resource Allocation Challenges:\* While large companies are equipped to handle regular traffic, a sudden surge in malicious requests can challenge resource allocation. Managing the influx becomes complicated, potentially leading to service disruptions and slowdowns in critical functions.

— \*Load Balancer Impact:\* Load balancers, designed to evenly distribute traffic, may struggle to differentiate between legitimate and malicious requests during high-intensity SSRF attacks. This difficulty can hinder their effectiveness, allowing malicious traffic to bypass normal traffic shaping mechanisms.

***3. Prolonged Attacks and Concealed Malicious Activities:***
 — \*Persistence of Attacks:\* Prolonged SSRF attacks compound the impact, making it harder for security teams to mitigate the situation effectively. The continued strain on resources can lead to extended service degradation, negatively affecting user experience.

— \*Distraction and Evasion:\* Attackers exploit SSRF-induced chaos as a distraction. While security teams grapple with mitigating gateway timeouts, attackers may execute other malicious activities, such as exfiltrating sensitive data or planting malware, taking advantage of the security team’s diverted focus.

***4. Challenges in Security Architecture and Adaptability:***
 — \*Defensive Measures:\* Large companies employ various security measures, such as rate limiting, intrusion detection systems, and monitoring tools. However, SSRF attacks, especially when crafted to bypass these defenses, can challenge the effectiveness of these security mechanisms.

— \*Complex Web Ecosystems:\* Complex web applications with multiple integrations provide numerous entry points for SSRF vulnerabilities. Identifying and securing each potential weak link demands a meticulous approach, and even a single oversight can lead to exploitation.

***Conclusion: Vigilance and Continuous Improvement:***
SSRF vulnerabilities represent a persistent challenge, even for large companies. The ever-evolving landscape of cybersecurity demands continuous vigilance, adaptation, and improvement of security measures. Companies must invest not only in state-of-the-art technologies but also in skilled professionals who can proactively identify vulnerabilities, fortify defenses, and respond swiftly to emerging threats. By embracing a proactive security culture and staying ahead of the curve, even large organizations can navigate the complexities of SSRF vulnerabilities and protect their digital assets effectively.

# Responsible Disclosure — A pointless task on this occasion although Intigriti utilized it to help patch and not acknowledge the researcher:

When security researchers discover vulnerabilities, responsible disclosure is crucial. It involves reporting the issue to the organization or vendor, allowing them time to fix the problem before public disclosure. However, this process can sometimes be challenging, as not all organizations fully understand the severity of reported vulnerabilities.

## Challenges in Responsible Disclosure:

In some cases, security researchers face challenges in communicating the intricacies of SSRF vulnerabilities to organizations. This was demonstrated when a researcher reported an SSRF vulnerability to an organization. The researcher provided detailed information about the vulnerability, including PoC URLs and possible attack scenarios. Despite the researcher’s efforts, the organization struggled to understand the issue initially, leading to delays in the resolution process.

# SSRF Vulnerabilities and Responsible Disclosure

SSRF vulnerabilities can have far-reaching consequences, making it essential for organizations to have robust security measures in place. Responsible disclosure is a vital aspect of improving web security. While security researchers play a critical role in identifying vulnerabilities, organizations must be receptive and proactive in addressing reported issues to ensure a secure digital environment for users.

# Recap of the SSRF Exploitation:

The attacker initiates SSRF by leveraging a vulnerability in the server, coercing it to send requests to other servers or services. If the targeted service is slow or unresponsive, the SSRF request lingers, causing resource exhaustion and potential gateway timeouts. Inadequate timeout configurations exacerbate the problem, leading to prolonged delays and gateway timeouts. SSRF-induced timeouts can lead to a Denial of Service (DoS) situation, abuse of resources, and concealed malicious activities.

Responsible disclosure is crucial, but challenges can arise in communicating the severity of SSRF vulnerabilities to organizations. Can organizations afford to overlook these though, even in the absence of data exfiltration?

# **Organizational Responsiveness**

Organizations must be receptive and proactive in addressing reported vulnerabilities to ensure a secure online environment for users.

Update: If you are a but\*hurt person do not troll me. You will look like a Joe Santos. Joe thinks that he knows everything about security, this is Joe

Joe does not know the exploit to SSRF and believes this is only a pingback. Fortunately, even. Intigriti Know more than Joe. Do not be a Joe. Let us be better than that so that we can improve our base knowledge and elevate our skills.
