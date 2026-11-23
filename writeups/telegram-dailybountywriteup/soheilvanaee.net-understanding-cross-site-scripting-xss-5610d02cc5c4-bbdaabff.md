# Understanding Cross-Site Scripting (XSS)

- **Source URL:** https://medium.com/@soheilvanaee.net/understanding-cross-site-scripting-xss-5610d02cc5c4?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20240819131440/https://medium.com/@soheilvanaee.net/understanding-cross-site-scripting-xss-5610d02cc5c4
- **Fetched:** 2026-11-23
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/6859 (id 6859)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Understanding Cross-Site Scripting (XSS)

Cross-Site Scripting (XSS) is a common security vulnerability that allows attackers to inject malicious scripts into web pages viewed by other users. These scripts can steal data, hijack user sessions, or perform other malicious actions. In this article, we’ll explore how XSS works, provide simple examples of XSS vulnerabilities and exploits, and discuss ways to protect against XSS attacks.

## Types of XSS Attacks

There are three main types of XSS attacks:

1. **Stored XSS:** The malicious script is permanently stored on the target server, such as in a database.
2. **Reflected XSS:** The malicious script is reflected off a web server, such as in a search result or error message.
3. **DOM-based XSS:** The vulnerability exists in the client-side script rather than the server-side code.

# Simple XSS Vulnerability Example

Let’s consider a basic web application where users can submit comments. Here’s a simplified example of a vulnerable web page:

**HTML (index.html):**

```
<!DOCTYPE html>
<html>
<head>
    <title>Comment Section</title>
</head>
<body>
    <h1>Leave a Comment</h1>
    <form action="/submit-comment" method="post">
        <input type="text" name="comment" placeholder="Your comment here" />
        <button type="submit">Submit</button>
    </form>
    <h2>Comments:</h2>
    <div id="comments">
        <!-- Comments will be displayed here -->
        <p>Good article!</p>
        <p>Very informative.</p>
        <p>Nice work!</p>
    </div>
</body>
</html>
```
**Server-Side Script (Python/Flask Example):**

```
from flask import Flask, request, render_template_string
app = Flask(__name__)
comments = [
    "Good article!",
    "Very informative.",
    "Nice work!"
]
@app.route('/')
def index():
    comments_html = "".join(f"<p>{comment}</p>" for comment in comments)
    return render_template_string(open('index.html').read().replace("<!-- Comments will be displayed here -->", comments_html))
@app.route('/submit-comment', methods=['POST'])
def submit_comment():
    comment = request.form['comment']
    comments.append(comment)
    return index()
if __name__ == '__main__':
    app.run(debug=True)
```
# Exploiting the Vulnerability

An attacker could submit a comment with a malicious script, such as:

`<script>alert('XSS Attack!');</script>`
When this comment is rendered on the web page, the script will execute, showing an alert box with the message “XSS Attack!”.

# Preventing XSS

To prevent XSS attacks, you should sanitize and encode user inputs before displaying them. Here are some best practices:

1. **Sanitize Input:** Remove or escape potentially harmful characters from user inputs.
2. **Use HTTPOnly Cookies:** This helps prevent JavaScript from accessing session cookies.
3. **Content Security Policy (CSP):** Use CSP headers to restrict sources of executable scripts.
4. **Escape Output:** Ensure that any data outputted to the browser is appropriately escaped.

**Example of Escaping Output in Python/Flask:**

```
from markupsafe import escape
@app.route('/')
def index():
    comments_html = "".join(f"<p>{escape(comment)}</p>" for comment in comments)
    return render_template_string(open('index.html').read().replace("<!-- Comments will be displayed here -->", comments_html))
@app.route('/submit-comment', methods=['POST'])
def submit_comment():
    comment = escape(request.form['comment'])
    comments.append(comment)
    return index()
```
# Conclusion

Cross-Site Scripting is a prevalent and dangerous vulnerability that can lead to severe security breaches. By understanding how XSS works and implementing best practices to sanitize and encode user inputs, developers can protect their web applications from such attacks. Always be vigilant and proactive in securing your web applications to ensure the safety of your users and their data.
