# XSS Explained

- **Source URL:** https://medium.com/@mazene432/xss-explained-a-complete-guide-to-cross-site-scripting-with-practical-examples-80453349b35f?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250821233711/https://medium.com/@mazene432/xss-explained-a-complete-guide-to-cross-site-scripting-with-practical-examples-80453349b35f
- **Fetched:** 2026-11-21
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/9586 (id 9586)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# XSS Explained: A Complete Guide to Cross-Site Scripting with Practical Examples

# What is XSS and Why It’s One of the Most Dangerous Threats on the Web?

In the world of the web, every time you open a site and enter some data — like your name, email, or even a simple comment — the website is supposed to handle that input safely.

But sometimes, due to poor coding practices, websites fall into a serious security mistake called **Cross-Site Scripting**, or simply **XSS**.

XSS is a vulnerability that allows an attacker to inject **malicious code (usually JavaScript)** into web pages. This code gets executed inside the **victim’s browser** instead of just being displayed as normal text.

In simple terms: the attacker tricks the website into running code on the users’ devices — without them even knowing.

This can lead to dangerous consequences, such as:

-Stealing **cookies** that contain session and login data.

-Performing actions on behalf of the victim (like sending messages, changing settings, or even hijacking accounts).

-Tricking users with fake login forms or pages (**phishing)**

-And sometimes, using it as an entry point for bigger attacks against the system or network.

# A Simple Example:

Imagine visiting a search page and instead of typing a normal keyword, you enter this

`<script>alert('Hacked by mazen');</script>`
If the website reflects this code back into the page without sanitizing it, a popup will appear immediately.

That means the site is vulnerable to XSS!

# Why is XSS Important?

- Because it exists on **millions** of websites worldwide.
- Even tech giants like Google and Facebook have had XSS bugs reported by security researchers.
- It’s considered one of the most dangerous web attacks because of its ease and big impact — and that’s why it’s still listed in the **OWASP Top 10** today.

In this article, we’ll dive deeper into the different types of XSS, how they work, and how security researchers discover and exploit them **legally** in **Bug Bounty** programs.

Let’s get started 👇

# Before We Dive Into XSS Types

Before we explore the different types of XSS vulnerabilities, let’s take a quick look at how these vulnerabilities can appear in the source code.

Often, XSS vulnerabilities arise due to insecure handling of user inputs. On some websites, an attacker might be able to inject malicious JavaScript code into user interaction fields (like search boxes or comment sections), and this code gets sent to the browser to be executed without the user noticing.

Let’s look at a simple example of code that could be vulnerable to XSS

```
<form action="search.php" method="GET">
    <input type="text" name="q" />
    <input type="submit" value="Search" />
</form>
```
In the above code, the website accepts search queries from users, but the **inputs are not sanitized** or **validated** before being displayed on the page. If an attacker enters malicious JavaScript code into the search box, such as:

`<script>alert('XSS Attack')</script>`
In this case, the website will display the code on the page, resulting in the malicious script being executed on the victim’s device. This is one way an attacker could exploit **Reflected XSS**.

Now that we’ve seen how an XSS vulnerability can appear in code, let’s move on to explore the **different types of XSS**.

# Types of XSS

**XSS (Cross-Site Scripting)** is a security vulnerability that allows an attacker to execute malicious **JavaScript** code within the victim’s browser. This malicious code can be used to exploit various systems, whether on websites or applications.

In this context, XSS is divided into five types, each with its own method of exploitation. These types are:

# 1. Reflected XSS (Reflected Cross-Site Scripting)

**Reflected XSS** is a type of XSS vulnerability where an attacker injects malicious JavaScript code into an HTTP request (such as through a URL or submitted form), which is then reflected by the server and displayed in the response sent back to the victim.

# How Reflected XSS Works:

In **Reflected XSS**, the malicious code is sent directly from the browser to the server via the request, and when the server responds, it reflects the injected code back in the page. This causes the code to execute on the victim’s browser. In this type of vulnerability, the malicious code is not stored on the server; it is only processed at the moment the request is made.

# Practical Example:

Let’s assume there is a website with a search form that displays search results based on the user’s input. The code for displaying the result might look like this:

```
<form action="search.php" method="GET">
    <input type="text" name="q" />
    <input type="submit" value="Search" />
</form>
```
In this example, the user enters a search query, and the website displays the results based on that query. However, if the site does not **sanitize** (clean) the inputs properly, an attacker could send a request with malicious JavaScript code.

For example, the attacker might send the following link:

`http://example.com/search?q=<script>alert('XSS Attack');</script>`
When the victim clicks on this link, the server processes the request and returns the results page. Since the input was not sanitized, the page would look like this:

`<h1>Results for: <script>alert('XSS Attack');</script></h1>`
As a result, the malicious JavaScript code is executed, and a pop-up alert with the message **“XSS Attack”** will appear in the victim’s browser.

# Danger of Reflected XSS:

- **Ease of exploitation**: The attacker only needs to craft a link with malicious code and send it to the victim via email, forums, or social media.
- **Instant response**: As soon as the victim opens the link, the code executes immediately. The attacker does not need to store the code on the server, which makes detection harder.
- **No persistence**: The malicious code does not remain on the site or in the database after execution. Once the victim closes the page, the attack is gone.

# How to Prevent Reflected XSS:

- **Sanitize inputs**: Ensure all user inputs are sanitized properly to remove any unwanted JavaScript code.
- **Use Content Security Policy (CSP)**: Enforcing a Content Security Policy can help mitigate the chances of executing malicious JavaScript code.
- **Encoding**: When displaying user inputs in the page, ensure that content is properly encoded to prevent it from being interpreted as JavaScript code.

# 2. Stored XSS (Stored Cross-Site Scripting)

**Stored XSS** is another type of XSS vulnerability that occurs when an attacker injects malicious JavaScript code into a **form or input** that gets stored in the website’s or system’s database, and later retrieved and displayed to other users. In this type, the malicious code is stored on the server for an extended period and remains active even after the attacker leaves the site.

# How Stored XSS Works:

In **Stored XSS**, the malicious code is injected via user inputs (such as form fields or comments) and stored in the website’s database. When a user or victim visits the page displaying this input, the malicious code is retrieved from the database and displayed in the page. The code executes when the page is loaded in the victim’s browser.

# Practical Example:

Let’s assume there is a website that allows users to post comments or have a forum. An attacker might inject malicious JavaScript code in one of the comments, such as:

`<script>alert('XSS Attack');</script>`
If the site doesn’t properly sanitize or encode the content before storing it in the database, this code will be saved as-is in the database. When any user visits the page with this comment, the malicious code will be displayed in their browser and executed.

The page might look something like this:

```
<div class="comment">
    <p>User123: <script>alert('XSS Attack');</script></p>
</div>
```
When the page is loaded in the victim’s browser, the malicious code executes, and a pop-up window with the message **“XSS Attack”** will appear.

# Danger of Stored XSS:

- **Persistent storage**: The malicious code is stored on the server and continues to affect users until it is discovered and removed. This can impact many victims at different times.
- **Wide execution scope**: Since the code is stored on the server, it can execute on anyone who visits the page containing the malicious code.
- **Significant security risks**: The malicious code can be exploited to steal sensitive data from victims, such as cookies, or even manipulate user account contents.

# How to Prevent Stored XSS:

- **Sanitize inputs**: All user inputs should be sanitized to ensure there’s no malicious JavaScript code. Techniques like **encoding** can be used to secure inputs.
- **Use Content Security Policy (CSP)**: Enforcing a Content Security Policy can help mitigate the chances of malicious JavaScript code execution.
- **Filter and encode**: Ensure that inputs are filtered when stored in the database and properly encoded when displayed on pages.

# 3. DOM-based XSS (XSS based on DOM)

Before we dive into the explanation of **DOM-based XSS**, it’s important to first understand what **DOM** is.

# What is the DOM?

**DOM (Document Object Model)** is an API that represents the contents of a webpage in a hierarchical, tree-like structure inside the browser. It’s a logical model that helps represent and interact with the different elements on a page like texts, images, links, forms, and others.

The **DOM** is used by JavaScript to interact with the content displayed on the webpage. In other words, the **DOM** acts as a “map” of the page, allowing developers to modify the page content dynamically without needing to reload it.

**How does the DOM work?**

- When you open a webpage in a browser, the browser loads the page’s HTML and transforms it into the **DOM**.
- Every element on the page (like headings, paragraphs, links, etc.) is represented in the **DOM** as **objects** and **elements**.
- Using JavaScript, you can access and modify these elements. For example, you can change texts, add new content, or even change CSS properties of elements.

**A simple DOM example:**

If you have a simple HTML page like this:

```
<p id="greeting">Hello, World!</p>
<button onclick="changeText()">Change Text</button>
```
With JavaScript, you can interact with this page via the **DOM** to change the text inside the paragraph:

```
function changeText() {
    document.getElementById('greeting').innerText = 'Hello, XSS';
}
```
In this example, we use JavaScript to access the `<p>` element containing the text "Hello, World!" via the **DOM**, and change it to "Hello, XSS" when the user clicks the button.

# DOM-based XSS:

Now that we understand what **DOM** is, we can better understand how **DOM-based XSS** occurs.

**DOM-based XSS** happens when malicious JavaScript code is injected directly into the **DOM** through user interaction with the page, rather than the code being sent to the server. In this type of vulnerability, the malicious code is executed directly in the browser based on the **DOM** contents, making it harder to detect as it is not stored on the server.

# How does the vulnerability occur?

1. **Unfiltered inputs**: Malicious code is injected when a user submits data through input fields or the URL, which is processed by JavaScript. If the input is not properly sanitized or encoded, the browser will execute the malicious code.
2. **Code execution inside the browser**: Once the user opens the page or interacts with it, the malicious code is executed in the browser based on the manipulation of the **DOM**.

# Practical Example:

Suppose you have a webpage with a form to input the username and display a custom greeting after the user enters their name. The JavaScript code might look like this:

```
<input type="text" id="username" />
<button onclick="greetUser()">Greet</button>
```
\<script>

function greetUser() {

var username = document.getElementById('username').value;

document.getElementById('message').innerHTML = 'Hello, ' + username + '!';

}

\</script>\<div id="message">\</div>

In this example, the user enters their name in the text field, and when they click the button, a custom message is displayed in the `div` element using JavaScript.

However, if the **input is not sanitized** properly, an attacker could inject malicious JavaScript code like:

`<script>alert('XSS Attack');</script>`
In this case, when the victim clicks the button, the browser executes the malicious code inside the page because of how the **DOM** is manipulated by JavaScript. As a result, a pop-up message will appear with the text **“XSS Attack”**.

# The Dangers of DOM-based XSS:

- **Code execution inside the browser**: The code is executed directly inside the browser, making the attack harder to detect.
- **Affects only the users**: The attack affects only users who interact with the page containing the malicious code.
- **Ease of exploitation**: Attackers can exploit this type of vulnerability to change the page’s content or execute malicious JavaScript code on users’ devices.

# How to Prevent DOM-based XSS:

- **Sanitize inputs**: Inputs should be properly sanitized to ensure they don’t contain malicious JavaScript code.
- **Use** **innerText**
 **instead of** **innerHTML**
`innerText` instead of `innerHTML` because `innerText` does not interpret inputs as JavaScript code.
- **Validate inputs**: Inputs should be validated to ensure they conform to expected patterns.
- **Use Content Security Policy (CSP)**: Applying a content security policy can help reduce the chance of malicious JavaScript execution in the page.

# 4. Self-XSS (Self Cross-Site Scripting)

**Self-XSS** is a type of **XSS (Cross-Site Scripting)** that occurs when an attacker convinces the victim to execute malicious JavaScript code within their own browser. Simply put, the attacker doesn’t inject the malicious code into the page itself, but rather manipulates the victim into executing it in their browser.

What makes **Self-XSS** different from other types of **XSS** is that the victim is the one who executes the malicious code themselves through direct interaction with their browser.

# How Does Self-XSS Happen?

1. **Convincing the Victim to Run Malicious Code**: The attacker sends a message or link to the victim, saying “If you want to unlock a special feature or something on this website, copy and paste this code into your browser’s console.”
2. **Victim Executes the Code**: The victim then executes the malicious code in the browser’s console. The console is a tool that developers use to write and test JavaScript code directly in the browser.
3. **Browser Executes the Code**: Since the browser doesn’t differentiate between good or malicious JavaScript code when it’s executed from the console, it runs the code, which could lead to malicious actions like stealing data or performing unwanted actions.

# Example of Self-XSS Attack:

Let’s say there’s a website claiming to offer “exclusive offers” and asks users to copy a code and paste it into their browser’s console.

The attacker might send the victim a link or instructions like this:

“If you want to unlock exclusive offers, copy and paste this code into your browser’s console:”

`javascript:alert('XSS Attack');`
When the victim copies and pastes this code into the console, the browser executes it and a pop-up message will appear saying **“XSS Attack”**.

# How Does the Attack Work?

- **The Victim Executes the Attack**: This attack completely relies on the victim. They are the ones running the malicious code in their browser.
- **The Attacker Tricks the Victim**: The attacker doesn’t directly inject malicious code into the website; instead, they trick the victim into running it themselves in the browser.
- **The Browser Doesn’t Block the Code**: Browsers usually don’t block JavaScript from running in the console, which makes this attack easier.

# Why Does Self-XSS Happen?

- **The Victim Doesn’t Understand the Risk**: Often, the victim doesn’t realize that the code could be harmful. They might think they are just following a normal instruction.
- **The Browser Allows the Code to Run**: The browser allows the user to execute JavaScript code from the console, which makes this attack possible.

# How Can We Prevent Self-XSS?

1. **Increase User Awareness**: Users need to be educated not to copy and paste untrusted or unknown code into their browser’s console. It’s crucial to make sure users understand they shouldn’t run code from untrusted sources.
2. **Restrict Console Access**: Some advanced websites can restrict or block access to the browser console, especially if they know there’s a possibility of this attack.
3. **Use Content Security Policy (CSP)**: Websites can implement **Content Security Policy (CSP)**, which helps mitigate the risk of running malicious JavaScript code. **CSP** allows a site to specify from where scripts can be loaded and executed.
4. **Validate Inputs**: Websites can ensure that any input or actions by users are safe before executing them. This includes input in forms or links.

# Key Features of Self-XSS:

- **Hard to Detect**: Since the attacker doesn’t inject the code into the website, but instead tricks the victim into running it, it’s harder to detect early.
- **Relies on Victim’s Interaction**: The attack relies entirely on the victim. The attacker doesn’t need to have access to the site’s backend or inject code into the server.
- **Requires User Awareness**: Users must be educated to not execute unknown or suspicious code.

# Key Points You Need to Know About Self-XSS:

- **Self-XSS** is a trick where the attacker convinces the victim to run malicious code themselves.
- This attack doesn’t require the attacker to inject code into the server; it relies on user interaction.
- It’s very important for users to be cautious and understand they shouldn’t run untrusted code.

# 5. Blind XSS (Blind Cross-Site Scripting)

**Blind XSS** is a type of **Cross-Site Scripting (XSS)** vulnerability where the attacker injects malicious code into a website or application, but cannot see the immediate result or effect of this code. In other words, the attacker injects the code, but its effect is visible in another place or at a later time, not immediately where the attacker is interacting.

In most other types of **XSS** (such as **Reflected XSS** or **Stored XSS**), the attacker sees the immediate impact of the attack. But with **Blind XSS**, the effect is invisible to the attacker and often appears elsewhere or later.

# How Blind XSS Works

1. **Injecting Malicious Code**:
The attacker begins by injecting malicious JavaScript code into an input field that the website accepts, such as forms, comments, or text fields.
2. **No Immediate Effect Visible**:
Once the code is injected, the attacker does not see the immediate result on the page. For example, if the attacker injected code to display an alert (`alert('XSS Attack!')`), they will not see the alert appear immediately.
3. **Effect Appears Later**:
The actual effect of the code appears later when another person (like an admin or another user) visits the page or interacts with the affected content. This can be in an admin panel or a page that contains the data injected by the attacker.

# Example of Blind XSS:

Let’s assume there’s a website that asks users to input a comment on a forum. The attacker injects the following malicious code into the comment field:

`<script>alert('XSS Attack');</script>`
However, instead of seeing the result immediately, the attacker won’t see the effect on the page. Later, when an admin visits the control panel or a page with this comment, they will see the alert message saying “XSS Attack”. This is where the attack is successful.

# Types of Blind XSS:

1. **Server-Side Blind XSS**:
In this type of attack, the attacker injects the malicious code on the server side. The code gets stored in the database or files and shows its effect when someone else (like an admin or another user) interacts with the affected data.
2. **Client-Side Blind XSS**:
This type depends on the interaction with the browser. The attacker injects JavaScript code into an input field, and the code runs only when another person views the page. In this case, the effect depends on the browser’s interaction with the code when loading the page.

# How to Protect Against Blind XSS

1. **Input Validation and Sanitization**:
Always validate and sanitize user input to ensure it is safe. Remove or “neutralize” any untrusted JavaScript code from inputs before storing or displaying it on webpages.
2. **Use Security Measures Like CSP (Content Security Policy)**:
**CSP** is a security mechanism that helps prevent the execution of malicious code by specifying which sources are allowed to load and execute content. Websites can use CSP to restrict loading JavaScript from untrusted sources.
3. **Perform Regular Input Checks**:
Regularly check the inputs that are submitted to the site, whether through forms, comments, or any other kind of input. Ensuring that inputs are safe can prevent attackers from injecting malicious code.
4. **Use Escaping for Inputs**:
**Escaping** is the process of converting special characters in user inputs (like `<`, `>`, `&`, and `"`) into a form that cannot be interpreted as HTML or JavaScript. This prevents malicious code from executing when it is displayed on the web page.

# Importance of Protecting Against Blind XSS

- **Hard to Detect**: Since the attacker does not see the immediate effect, it can be difficult to detect the attack at first.
- **Risk to Other Users**: Even though the attacker doesn’t see the effect immediately, the effect could harm other users or administrators.
- **Exploiting the Site for Malicious Purposes**: The attacker can exploit this vulnerability to gather user data or perform harmful actions after some time.

# Preventive Measures

- **Escaping Inputs**: Always escape user input when rendering it on the page. This converts potentially dangerous characters into a safe representation.
- **Limiting Input Fields**: Restrict where JavaScript can be input, such as in comment fields or text boxes, and sanitize those inputs rigorously.

# Conclusion

**Blind XSS** is a type of **XSS** where the attacker injects malicious code but cannot see the result immediately. The attack relies on other users or administrators interacting with the affected content later. To secure a site, it’s crucial to validate and sanitize inputs, use security mechanisms like **CSP**, and escape user data before rendering it on the page.

# How to Search for XSS Vulnerabilities

**After explaining the different types of XSS vulnerabilities, we will now move on to the important part, which is how to search for these vulnerabilities in applications.** Searching for XSS vulnerabilities requires analyzing inputs and reviewing the code carefully. In this section, we will learn the different methods for discovering **XSS** in websites and applications, and how to test for weak points.

## 1. Searching for Input Fields

The first step in searching for an XSS vulnerability is to look for areas where the user can input data, such as:

- **Forms**: Such as login forms, registration, or search.
- **Comment Fields**: Like comments users leave on articles or products.
- **URLs**: Links may contain parameters that pass data to the website.

## 2. Using XSS Detection Tools

- **Burp Suite**: A well-known tool for detecting XSS vulnerabilities using the **Intruder** feature to test inputs.
- **OWASP ZAP**: A free and open-source tool for security scanning and detecting vulnerabilities.
- **XSSer**: An automated tool to search for XSS vulnerabilities.

## 3. Testing Inputs Using Special Characters

Try entering JavaScript code in any input fields, such as:

- `<script>alert('XSS')</script>`
- `<img src="x" onerror="alert('XSS')">`

If an alert or popup appears, it indicates the presence of **Reflected XSS**.

## 4. Searching in URLs

Try adding JavaScript code to the URL parameters, such as:

- `http://example.com/search?query=<script>alert('XSS')</script>`

If the code is displayed without being filtered or properly handled, it indicates the presence of **Reflected XSS**.

## 5. Inspecting Client-Side Code

Use tools like **Chrome DevTools** or **Firefox Developer Tools** to inspect the client-side code. Look for places where user inputs are displayed without filtering, such as:

- `innerHTML`
- `document.write`

# Real Scenarios for XSS Vulnerabilities

## Scenario 1: Reflected XSS in a Search Function

**Situation:**

A website contains a search box where users enter a query to search the site. However, the website does not properly sanitize the inputs before displaying the search results.

**Exploitation:**

An attacker can send a link with JavaScript code in the query parameter, such as:

- `http://example.com/search?query=<script>alert('XSS')</script>`

When the user visits this link, an alert box will pop up indicating the presence of a vulnerability. In this case, **Reflected XSS** allows the attacker to execute JavaScript code in the victim’s browser.

**How to Test:**

Try entering `<script>alert('XSS')</script>` in the search box and see if the code executes on the page.

## Scenario 2: Stored XSS in a Comment Section

**Situation:**

A website has a comment section where users can leave comments on articles. The website does not properly sanitize the content submitted by users before storing and displaying it to others.

**Exploitation:**

An attacker can post a comment containing JavaScript code, such as:

- `<script>alert('XSS Stored')</script>`

**When the comment is viewed by any user**, the JavaScript code will execute in their browser, resulting in a **Stored XSS** attack. This is particularly dangerous because the code persists on the server and affects every user who views the comment.

**How to Test:**

Try entering JavaScript code in the comment section and then interact with the comments after they’ve been posted to see if the code executes when they are displayed.

## Scenario 3: DOM-based XSS in a Login Form

**Situation:**

A web application contains a login form that dynamically changes the page content based on user input without properly sanitizing the data.

**Exploitation:**

An attacker can modify the URL to include JavaScript code:

- `http://example.com/login?username=<script>alert('DOM XSS')</script>`

In this case, the code is executed directly by the JavaScript in the browser, indicating **DOM-based XSS**.

**How to Test:**

Try entering the code in the input fields or in the URL and check if the code is executed after submitting the form.

## Scenario 4: Self-XSS in a Social Media Platform

**Situation:**

On a social media platform, a user notices that some people are sharing JavaScript code in comments or private messages. In this case, the malicious code isn’t directed at the victim directly, but the user realizes that they executed the code in their browser.

**Exploitation:**

The attacker might send the victim a link containing JavaScript code and convince them to open it (e.g., “Look at this amazing image”).

- `http://example.com/?message=<script>alert('Self XSS')</script>`

If the victim opens the link and runs the code, it will execute in their browser.

**How to Test:**

Try sending JavaScript code to the victim in a convincing way and see if the code is executed when they open the link.

# Key Takeaways from Real Scenarios

- **Reflected XSS** happens when input data is reflected off the server and directly displayed in the response without validation.
- **Stored XSS** involves injecting malicious code that is stored on the server and then executed every time a user accesses that content.
- **DOM-based XSS** occurs when the vulnerability exists in the client-side code (JavaScript), where user input is used to modify the DOM without proper sanitization.
- **Self-XSS** relies on social engineering to convince the user to execute malicious scripts in their browser.
- **Blind XSS** occurs when the attacker injects malicious code into an input field that is stored on the server. The code is not executed immediately but is later triggered when an administrator or other user views the data. This type of attack is often harder to detect because it does not immediately show results to the attacker.

These scenarios provide practical insights into the different types of XSS vulnerabilities and how they can be exploited, helping developers and security researchers recognize the importance of input sanitization and validation to secure their applications.

# Final Thoughts

In this article, we took a deep dive into Cross-Site Scripting (XSS) vulnerabilities and explained the different types with simple examples and real-world scenarios. By now, you should have a solid understanding of how XSS works and why it’s important to secure your applications against it.

Always remember: input validation and output encoding are your first lines of defense against XSS. Stay sharp, keep testing, and never stop learning — because security is a continuous journey.
