# Day 28 of 30 Day — 30 Vulnerabilities | DOM-based XSS

- **Source URL:** https://medium.com/@kumawatabhijeet2002/day-28-of-30-day-30-vulnerabilities-dom-based-xss-e7bfadc56b2f?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20240907130717/https://medium.com/@kumawatabhijeet2002/day-28-of-30-day-30-vulnerabilities-dom-based-xss-e7bfadc56b2f
- **Fetched:** 2026-11-23
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/7186 (id 7186)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Day 28 of 30 Day — 30 Vulnerabilities | **DOM-based XSS**

**Day 28: Mastering DOM-based XSS — Essential Tricks & Techniques Based on Personal Experience and Valuable POCs**

*In collaboration with Sunil Kumawat (LinkedIn | Twitter)*

Hey security enthusiasts, Abhijeet ([Twitter](https://x.com/AbhijeetKumaw10)) back with another deep dive into web security. Today, we’re focusing on a tricky yet common vulnerability — DOM-based Cross-Site Scripting (XSS). This form of XSS is often harder to detect but can have severe consequences if exploited. Let’s explore its mechanics and mitigation strategies.

# 1. Brief Description

**What is DOM-based XSS?**

DOM-based XSS is a type of cross-site scripting vulnerability that occurs when the client-side script (JavaScript) manipulates the DOM (Document Object Model) based on untrusted user input. Unlike traditional XSS, which occurs on the server side, DOM-based XSS is purely client-side, making it more challenging to detect and mitigate.

**How Does It Work?**

DOM-based XSS typically arises when a web application’s JavaScript directly uses or modifies DOM elements with untrusted data. If an attacker can control the data being passed into these DOM operations, they can inject malicious scripts into the page. This leads to the execution of these scripts in the context of the victim’s browser, potentially resulting in session hijacking, data theft, or even full control of the user’s account.

# 2. Where to Detect

**JavaScript Functions Handling User Input:**

- Focus on JavaScript functions like `innerHTML`, `document.write()`, `eval()`, or `setTimeout()` that process or reflect user-controlled data.

**URL Parameters & Fragment Identifiers:**

- Examine how your application processes URL parameters, hash fragments (e.g., `window.location.hash`), or any other part of the URL that can be manipulated by an attacker.

**Event Handlers & Callbacks:**

- Investigate event handlers that might process user inputs, such as `onclick`, `onload`, or other DOM events that interact with user data.

# 3. How to Detect

**Manual Testing:**

- Manually review the JavaScript code to identify areas where user input is being directly processed or reflected. Inject payloads like `<script>alert(1)</script>` into various input fields or URL parameters to see if they are executed.

**Automated Tools:**

- Utilize tools like DOM Invader (part of Burp Suite), or custom scripts to automate the discovery of potential DOM-based XSS vulnerabilities by analyzing the DOM and detecting insecure JavaScript patterns.

**In-Browser Testing:**

- Use browser developer tools to dynamically alter DOM elements or JavaScript variables during testing. This approach helps simulate attacks in real-time, giving you insights into how the application might behave under an actual attack.

# 4. Basic & Advanced Payloads

**Basic Payloads:**

- **Simple Script Injection:** Inject a basic script tag into input fields or URL parameters, e.g., `<script>alert('XSS')</script>`, to see if the script gets executed.
- **Event Handler Injection:** Use JavaScript event handlers to trigger code execution, e.g., `"><img src=x onerror=alert(1)>`.

**Advanced Payloads:**

- **DOM Property Injection:** Inject payloads that exploit specific DOM properties, e.g., modifying `window.location` or `document.referrer` to include malicious scripts.
- **JavaScript Protocol Injection:** Use `javascript:` URLs in places where the application processes links or redirects, e.g., `javascript:alert(1)`.

# 5. Defense Bypass Techniques

**Encoding & Decoding:**

- Bypass filters by encoding your payloads in different formats (e.g., URL encoding, Base64) or by using techniques that trigger the decoding of these payloads during processing.

**Contextual Injections:**

- Inject payloads into different contexts within the DOM, such as attributes, event handlers, or JavaScript code blocks, to bypass basic sanitization measures.

**Chaining Exploits:**

- Combine multiple vulnerabilities or flaws, such as exploiting weak input validation and then using DOM-based XSS to escalate the attack’s impact.

# 6. POC Section

**POC 1: URL Parameter-based DOM XSS**

**A. Description:**

- Exploit a vulnerable application that processes URL parameters to execute arbitrary JavaScript within the victim’s browser.

**B. Steps to Reproduce:**

- Identify a URL parameter that is reflected in the DOM without proper sanitization.
- Inject a payload like `https://vulnerable-site.com/page?name=<script>alert('XSS')</script>`.
- Observe the execution of the script when the page is loaded.

**C. Impact:**

- The attacker can execute arbitrary JavaScript, leading to session hijacking, credential theft, or defacement of the website for the victim.

**POC 2: Hash Fragment-based DOM XSS**

**A. Description:**

- Exploit a DOM-based XSS vulnerability using the hash fragment part of the URL.

**B. Steps to Reproduce:**

- Identify a portion of the application that reads or modifies the `window.location.hash` without sanitizing it.
- Inject a payload like `https://vulnerable-site.com/#<script>alert('XSS')</script>`.
- The script executes when the page processes the hash fragment.

**C. Impact:**

- Attacks like these can be used in phishing campaigns where users are tricked into clicking on a malicious link that automatically executes code in their browser.

**POC 3: DOM Event Handler-based XSS**

**A. Description:**

- Target DOM event handlers that execute based on user interactions, such as clicking a button.

**B. Steps to Reproduce:**

- Identify an element with an `onclick` event handler that processes user input.
- Inject a payload such as `https://vulnerable-site.com/#" onclick="alert(1);`.
- Observe the script execution when the element is clicked.

**C. Impact:**

- This method can be used to execute malicious scripts as soon as a user interacts with the vulnerable element.

# 7. Conclusion

**Mitigation Strategies:**

- **Avoid Dangerous Functions:** Refrain from using functions like `innerHTML`, `document.write()`, or `eval()` with untrusted data. Instead, use safe alternatives like `textContent` or `setAttribute`.
- **Sanitize Input:** Ensure that any user input processed in the DOM is properly escaped and sanitized, reducing the risk of script injection.
- **Content Security Policy (CSP):** Implement a robust Content Security Policy to restrict the execution of unauthorized scripts, providing an additional layer of defense.
- **Regular Audits:** Regularly audit your JavaScript code for potential XSS vulnerabilities, particularly in areas that handle user input.

**Final Thoughts:** DOM-based XSS is a subtle yet dangerous vulnerability that can have significant security implications if not properly managed. By understanding its mechanics and implementing strong defenses, you can safeguard your web applications from this threat (OWASP, PortSwigger).

Thank you for reading the blog!

You can also follow me on [Twitter](https://x.com/AbhijeetKumaw10) & [LinkedIn](https://www.linkedin.com/in/abhijeet-kumawat/) for more write-ups.

Follow & subscribe for daily write-up updates via mail on Medium.

Stay tuned for Day 29, where we’ll explore another critical vulnerability!
