# Bug Bounty Hunter — When CORS is not Configured Correctly / JSONP Attack

- **Source URL:** https://medium.com/@batuhanaydinn/bug-bounty-hunter-when-cors-is-not-configured-correctly-jsonp-attack-e2cad3ecf9de?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20251126141931/https://medium.com/@batuhanaydinn/bug-bounty-hunter-when-cors-is-not-configured-correctly-jsonp-attack-e2cad3ecf9de
- **Fetched:** 2026-11-27
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/3304 (id 3304)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Bug Bounty Hunter — When CORS is not Configured Correctly / JSONP Attack

Hello Folks,

In today’s interconnected web ecosystem, communication and data sharing between websites have become increasingly common. However, this communication process can introduce security vulnerabilities and weaknesses. In this article, we will discuss a type of attack called JSONP (JSON with Padding) attacks, which exploit flawed configurations of the Cross-Origin Resource Sharing (CORS) mechanism.

CORS, a mechanism that allows websites to access resources with different origin domains, serves the primary purpose of controlling resource requests based on the browser’s security policies. Web servers can use CORS headers to specify which origin domains they will accept or reject resource requests from.

However, when CORS is misconfigured or left incomplete, websites can be exposed to security vulnerabilities. JSONP attacks specifically take advantage of these misconfigurations. JSONP, although now replaced by CORS in modern browsers, is a method that enables websites to access resources from a different domain. Yet, flawed CORS configurations can still result in security vulnerabilities.

JSONP attacks involve an attacker leveraging JSONP to inject malicious code into a target website or gain access to sensitive data. The attacker creates a malicious web page and invokes the target website through this page. Due to the way JSONP works in browsers, which allows cross-domain requests, the attacker’s code becomes executable within the context of the target website.

To execute this type of attack, the attacker first needs to identify a JSONP-supporting API on the target website. JSONP often relies on the browser’s \<script> tag to fetch external resources. The attacker creates a \<script> tag on their own website and calls the API of the target website, appending their malicious code to this call. The browser interprets and executes this code as part of the API call from the target website.

## Let’s create a Simulation

Those who have been following me for a long time know that, in my opinion, one of the main ways to achieve understanding is by simulating an attack method and explaining it clearly. Therefore, let’s create a simulation and step-by-step examine how the attack surface works.

### Backend Code:

server.js

api-data-endpoint.js

I have developed a small simulation above.

Set up the server: Run the first code snippet to set up a server using Express. This server will have an endpoint /api that returns a JSONP response.

Make a request to the JSONP endpoint: Open a web browser and visit [http://localhost:3000/api?callback=attackerFunction](http://localhost:3000/api?callback=attackerFunction). This URL makes a request to the JSONP endpoint with the callback query parameter set to attackerFunction. This is where the vulnerability lies.

Create an HTML file named attack\_code.html and include the following code:

When you run the code and look at the developer console (F12), you will be greeted with the following statement.

Indeed, in this specific simulation, the data we retrieve is limited to our own data, making it more of a controlled scenario rather than a realistic attack scenario. It’s true that solely observing our own data does not definitively indicate a JSONP attack. However, if we modify the **attack\_code.html** as you mentioned and realize that we can retrieve data from external sources, we become aware of its potential effectiveness.

By modifying the **attack\_code.html** file, we can craft a script that sends the retrieved data to a remote server under our control or performs other malicious actions. This highlights the significance of properly configuring CORS and understanding the potential risks associated with JSONP vulnerabilities. In real-world scenarios, such attacks can be more impactful and exploit sensitive data or compromise user security.

In this code, an **attackerFunction** is defined, which utilizes the retrieved data for malicious purposes. Within the function, the data is logged to the console and then sent to another server controlled by the attacker using **XMLHttpRequest**.

By doing so, we have updated the original code to perform a JSONP attack. When you open the HTML file in a browser, the JSONP request will occur, and the callback function, **attackerFunction**, will receive the data and send it to another server controlled by the attacker.

JSONP attacks target vulnerabilities in the JSONP (JSON with Padding) mechanism commonly used in web applications. Despite the widespread adoption of more modern and secure alternatives like CORS (Cross-Origin Resource Sharing), these attacks can still pose a risk in older systems.

In this article, we have covered the fundamental aspects of JSONP attacks. We have explored how JSONP attacks work and the potential for attackers to steal data from target websites or utilize it for malicious purposes. Additionally, we have examined how JSONP attacks can be simulated.

To be notified of my next article, you can subscribe to my e-mail newsletter or follow me on Medium. Take care of yourselves.

Best Regards
