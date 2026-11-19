# Server Side Request Forgery (SSRF) Attacks

- **Source URL:** https://medium.com/@rajeevranjancom/server-side-request-forgery-ssrf-attacks-e8bdc5e17a68?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20221002063057/https://medium.com/@rajeevranjancom/server-side-request-forgery-ssrf-attacks-e8bdc5e17a68
- **Fetched:** 2026-11-19
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/47 (id 47)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# **Server Side Request Forgery (SSRF) Attacks**

Server-side request forgery (SSRF) attacks exploit software vulnerabilities that could allow an attacker to trick the server-side application to allow access to the server or modify resources. The attack can be successful if the target application supports data import from URLs or reads data from the URLs without proper safeguards (more on that later).

The attacker manipulates the URLs to make HTTP requests to arbitrary domains of their choosing by tampering with URL path traversal or by replacing it altogether. SSRF attacks can exploit URLs linking to internal services within the organization’s infrastructure that should not be exposed to users or external systems that should not be accessible to users.

If successful, an SSRF attack can lead to unauthorized actions or unauthorized access to the organization’s sensitive data, such as login credentials, for example. These can affect the web application itself, the back-end systems it relies on, or external servers with which the application communicates.

While not necessarily the first exploit that comes to mind when thinking about online attacks, SSRF attacks are serious business. According to hackerone.com, in 2020, SSRF attacks ranked fourth (out of ten) in terms of the amount spent on bug bounties, coming in at just under $3 million. And its year-on-year growth is estimated at 103%.

# Server SSRF attacks

The key to an SSRF attack is to exploit the trust relationships the web application maintains with other parts of the organization’s infrastructure or with external services.

To pull off a server SSRF attack, an attacker attempts to exploit the process used by a web browser (or any other client app) to access a URL on the server. The attacker either modifies or replaces the original URL with a malicious URL they crafted themselves. The malicious URL typically uses the 127.0.0.1 IP address or the “localhost” hostname, which points to the server’s local file system. If the server accepts the request and routes it, the attacker has successfully penetrated the server’s filesystem, leading to all sorts of potential damage and data loss.

Here’s an example. Suppose we host a weather website. The way it would work is that the web application would query a trusted server for the current weather conditions of a given region and display them. This can be achieved by using a REST API, which passes a URL with an API request from a user’s browser to the server. The request could look something like this:

POST /meteorology/forecasts HTTP/1.0

Content-Type: application/x-www-form-urlencoded

Content-Length: 113

weatherApi=http://data.weatherapp.com:8080/meterology/forecasts/check%3FcurrentDateTime%3D6%26cityId%3D1

The attacker could change the above URL as follows:

weatherApi=http://localhost/admin

The above would cause the server to grant the attacker access to the contents of the /admin folder. And because the request originated from within the server’s file system, it bypasses normal access controls and exposes the information despite the attacker being unauthorized.

# Back-end SSRF attacks

As mentioned above, SSRF attacks can also target the server’s back-end component, with which it has a trusted relationship. That would be another machine located on the internal network from which the server fetches content. Suppose the server has full access rights once connected to the back-end. In that case, an attacker could modify the API call URL to gain access to sensitive information or perform any number of unauthorized actions. Back-end components typically have weaker security mechanisms in place because they’re considered protected by being located inside the network perimeter.

Building upon the above example, an attacker could replace the API call as follows:

weatherApi=http://192.168.100.5/etc/passwd

Suppose the server connects to a back-end component on IP address 192.168.100.5 and has the proper permissions to access the /admin directory on that component’s file system. In that case, the attacker will be able to access and view the contents of the /admin directory.

# How SSRF works:

# SSRF on localhost

Let’s say you have an e-commerce website that has different servers on the backend. The application has different categories with various products in each category, and the specifications for a product are stored on a different service. So, when you click on a product, the current server (where the application is hosted) sends a request to the other server to get specifications for the product. For simplicity, let’s consider that the request is as follows:

https://bestproducts.com/products?url=https://productspecs.com/specs?id=34

So the server is sending a request to the productspecs server to send details for the product with id 34. When this request is made, the productspecs server will find details for that product and send it to the main server. And the main server will display the contents. This setup is vulnerable to SSRF.

In this example of a request, hackers can manipulate the URL parameter to make malicious requests. For example, let’s say the hacker modifies the request as follows:

https://bestproducts.com/products?url=file:///etc/passwd

If there’s no protection from SSRF and if this request is executed, then the contents of the /etc/passwd file would be displayed. This is an example where SSRF is on the server making the request. But SSRF can be used on other servers as well. Let’s look at an example of that scenario.

# SSRF on internal/external systems

Consider the same example of an e-commerce web application and its setup. Now, instead of the request to get product specifications, you can get access to the admin portal by crafting the request as follows:

https://bestproducts.com/products?url=https://productspecs.com/admin

If this request is executed successfully, then a hacker would get access to the admin portal that’s supposed to be accessible only from the local network. Furthermore, the hacker can get access to admin actions. And, needless to say, all kinds of nefarious activity could happen if hackers got ahold of such privilege.

# SSRF for port scanning

In many network architectures, most internal servers aren’t accessible to external networks. Only trusted internal servers can access them. In such cases, if someone wants to hack the restricted internal servers, they need to find a way to find information about them from within the internal network. SSRF can be used for port scanning of such internal servers. Hackers can craft requests to different ports on the server, and based on the response, they can conclude whether there’s a service running on that particular port or not.

Take a look at this request:

https://bestproducts.com/products?url=192.168.1.10:21

Based on the response from the server, a hacker can understand whether the server 192.168.1.10 has an FTP service on port 21 or not. They can send multiple requests to servers by changing the port number. And from the results, they’d get a list of which ports are open and can understand which services are running on that server.

We can keep giving examples, but then this post would never end. Your imagination is the limit on how a hacker can craft a request for an SSRF attack.

# Types of SSRF attacks

1. **Blind SSRF**: In a Blind SSRF, the attacker is unable to control the data of packets sent to a trusted internal network application. The attacker has complete control over the server’s IP address and ports. We must supply a URL followed by a colon and a port number to attack this sort of SSRF; we can determine the open and closed ports of the server by analyzing responses and error messages from the server. To verify the status of the various ports, we used this approach.
2. **Partial Response SSRF**: We get a restricted response from the server with this form of SSRF, such as the title of the page or access to resources, but we can’t see the data. This type of vulnerability can be leveraged to read local system files such as **/etc/config, /etc/hosts**, etc/passwd, and many others by controlling only certain parts of the packet that arrive internal program. We can read files on the system using the file:/ protocol. In some circumstances, XXE injection and DDoS vulnerabilities like these can be used to exploit partial SSRF vulnerabilities.
3. **Full Response SSRF**: We have complete control over the Packet in Full SSRF. Now we may access the internal network’s services and look for vulnerabilities. We can use protocols like file:/, dict:/, [HTTP://,](http://HTTP://,) gopher:/, and so on with this form of SSRF. We have a lot of freedom here to make different requests and abuse the internal network if there are any weaknesses. By submitting huge strings in the request, the whole SSRF vulnerability might cause the application to crash due to buffer overflow.

# How to prevent the attacks?

SSRF can be avoided by employing some or all the defense-in-depth controls listed below:

**From Layer of the Network:**

- To decrease the impact of SSRF, segment remote resource access capabilities into different networks at the network layer.
- To prevent all except critical intranet traffic, use “deny by default” firewall settings or network access control rules.
- Establish a lifetime and ownership for security system rules depending on apps.
- Firewalls should keep track of all permitted and banned network flows.

**From Layer of the Application:**

- All client-supplied input data should be sanitized and validated.
- With a positive allow list, enforce the URL schema, port, and destination.
- Clients should not receive raw answers.
- HTTP redirections should be disabled.

# Risks of SSRF attacks

When successful, SSRF attacks enable an attacker to manipulate a web server into performing actions it shouldn’t perform or displaying information it shouldn’t display. Both of these outcomes can have serious consequences. Here’s a short list of some of the typical targets associated with SSRF attacks.

# Exposing sensitive data

We’ve covered this already, but we’re still mentioning it because crafting a malicious URL to obtain sensitive data is probably the most common SSRF payload. Obtaining sensitive credentials can allow an attacker to wreak all sorts of havoc on the server. And the more permissions the credentials have, the bigger the risk. An attacker who manages to obtain the credentials of the server administrator, for example, could potentially take over the entire server.

# Cross-Site Port Attacks (XSPA)

As we’ve established, SSRF attacks don’t need to return any data to the attacker. However, specific metadata, such as response times to requests, can allow the attacker to determine whether or not a request was successful. If they can pinpoint a valid port and host pair, the attacker could port scan the application server’s network using this metadata in a Cross-Site Port Attack (XSPA).

The timeout for a network connection typically remains unchanged, regardless of the host or port. Because of that, an attacker could put through a request they know will fail and use this as a baseline for future response times. Successful requests will usually be much shorter than the baseline.

With that knowledge, attackers can fingerprint the services running over the network, allowing them to initiate a protocol smuggling attack.

# Denial of Service (DoS) attacks

A denial of service attack is an attack in which requests flood a server to the point that it can no longer cope with the load and crashes. There are many examples of these kinds of attacks in the wild — they’re pretty common. The SSRF version of a DoS attack would target the network’s internal servers.

The volume of requests received by the internal servers is usually much lower than the traffic to public-facing servers. Because of that, they tend to be configured for lower bandwidth than their public-facing counterparts. An attacker could mount an SSRF to flood the internal servers with large amounts of traffic to eat up all their available bandwidth and crash the internal servers, resulting in an internal DoS attack.

# Embedding malware

We won’t dwell on this one too much, as it’s relatively obvious. But if an attacker gains access to your internal servers, through SSRF or otherwise, they can embed malware onto the servers and infect any machines that connect to the now compromised server.

# Remote Code Execution (RCE)

Some modern web services are designed to be interfaced entirely via HTTP. Without proper safeguards over the control of URLs, an attacker may gain access to your servers by exploiting some of your running services. Gaining access to a server can mean, in certain circumstances, being able to execute arbitrary code (RCE), which could have any number of consequences — none of them good.

# SSRF attack Example

# CapitalOne

In 2019, CapitalOne fell victim to an SSRF attack. It remains one of the most well-known successful SSRF attacks today and it led to the leaking of over 100 million customer records. The attack was successful because of a mix of poor security practices and the presence of bugs within its infrastructure.

The CapitalOne site was hosted on Amazon’s AWS platform in which an SSRF vulnerability was present. The vulnerability allowed the attacker to obtain AWS credentials by using the application server itself, as AWS enables the application to obtain its own metadata. Once the attacker had secured the credentials, they could funnel the stolen data using AWS management tools, such as the command-line interface (CLI) and E3 storage.

A notable point about this attack is that the web application firewall (WAF) failed to identify and block the attack. We don’t know whether the attacker used a WAF bypass or if it was turned off. Couple that with the fact that the access credentials were too permissive, and you had the perfect conditions for a successful SSRF attack.

# Defending against SSRF attacks

Here are a few things you should be doing to mitigate SSRF attacks effectively. As usual, this will not provide 100% protection, but it’ll skew the odds to something more in your favor.

**Don’t trust user input** — This is true for many different types of attacks. Do not allow user input without validating it first. Regardless of where it comes from: authenticated users, internal users, and public users treat it as untrusted input and perform input validation.

**Perform allowlist checks** — You should perform allowlist validation on IP addresses and DNS names to which your application requires access. That way, an attacker won’t be able to redirect requests to unauthorized locations.

**Hard-code allowed file extensions** — Only provide access to permitted file extensions. You can hard-code allowed file extensions as follows:

\<?php

include($\_GET\[‘file’\] . ‘.html’);

?>

**Configure user authentication on internal resources, too** — Don’t assume that your internal resources are safe simply because they’re not directly exposed to the internet. User authentication mechanisms are your first line of defense in keeping malicious actors out of your infrastructure. Take the time to configure them properly for both external and internal resources.

**Implement the principle of least privilege** — The principle of least privilege is an IT security policy that prescribes that only the minimum necessary rights should be assigned to a user that requests access to a resource. The principle also states that those rights should be in effect for the shortest time possible.

Make sure only to provide users with the minimum necessary permissions to legitimately interact with the network.

**Enable logging** — Make sure your systems are configured to log any changes on the server. Also, make sure you’re able to track file change dates. That will help you detect any malicious code, infected files, and unauthorized access to your server.

**Use proper threat/intrusion detection software** — A threat detection application won’t necessarily save you from an SSRF attack attempt. However, such an application will alert you that something’s amiss much sooner than if you aren’t using one. The faster you get into damage control mode, the better off you and your organization will be.

**Update your software** — Always make sure to update your software as soon as the updates are available. Never use outdated or unsupported software. That will reduce the risk of your servers being compromised and make it more difficult for an attacker to exploit them.

**Use a firewall** — This one is quite simply unavoidable. Install a website application firewall (WAF) for your web server/site/application. It will help you prevent common automated attacks and may save you from more sophisticated attacks. Do not operate a web server without employing a firewall.
