# Understanding Server Side Template Injection (SSTI)

- **Source URL:** https://medium.com/@natarajanck2/understanding-server-side-template-injection-ssti-1cb0465dd46d?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20261111033112/https://medium.com/@natarajanck2/understanding-server-side-template-injection-ssti-1cb0465dd46d
- **Fetched:** 2026-11-19
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/9546 (id 9546)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Understanding Server Side Template Injection (SSTI)

Server Side Template Injection (SSTI) is a vulnerability that arises when user input is improperly handled and directly inserted into server-side templates. This can allow attackers to execute malicious code, access sensitive data or disrupt application functionality.

## Get Natarajan C K’s stories in your inbox

Join Medium for free to get updates from this writer.

In this blog, we’ll break down SSTI with a simple story and application example to help you grasp the concept and understand its potential impact.

## A Story to Explain SSTI

Imagine a hotel named “Template Inn” that offers personalized room decorations. Guests can request a custom message displayed on a screen in their room. The hotel uses a staff member (the server) to craft these messages using a template like this:

`Welcome, {{ guest_name }}!`
When guests check in, they provide their names, which are then inserted into the template. For most guests, it works perfectly:

- Guest name: *John*
- Displayed message: *Welcome, John!*

However, one mischievious guest decides to test the system. Instead of a regular name, they provide the input:

`{{ room_price * 0 }}`
The staff member blindly processes the input and generates the following message:

`Welcome, 0!`
The attacker realizes that the system is vulnerable. They then provide an even more dangerous input:

`{{ shutdown_hotel() }}`
If the hotel’s system is poorly secured, this could trigger a function to shutdown the reservation system, causing chaos. This is an example of SSTI in action: malicious user input being executed as part of the template.

## Technical Example of SSTI

To demonstrate SSTI in a web application, let’s consider a Python Flask application that uses the Jinja2 template engine. Here’s a simplified example:

Vulnerable Code


```
from flask import Flask, request, render_template_string
app = Flask(__name__)
@app.route("/")
def home():
    user_input = request.args.get("name", "Guest")
    template = f"Hello, {user_input}!"
    return render_template_string(template)
if __name__ == "__main__":
    app.run(debug=True)
```
## How It Works

1. A user access the application and provides their username in the URL:
**URL:** [*http://localhost:5000/?name=John*](http://localhost:5000/?name=John)
**Output:** *Hello, John!*
2. An attacker notices that the `name` parameter is used directly in the template. They test the system by injecting:
**URL:** [*http://localhost:5000/?name=*](http://localhost:5000/?name=John)*{{7\*7}}*
**Output:** *Hello, 49!*
3. This confirms the vulnerability. The attacker escalates their attack by injecting more malicious payloads, such as:
**URL:** [*http://localhost:5000/?name=*](http://localhost:5000/?name=John)*{{config.items()}}*
**Output:** *This can expose sensitive configuration data like database credentials.*

## Preventing SSTI

To secure your application against SSTI, follow these best practices:

1. **Avoid direct user input in templates —** Never directly include user input in templates. Always sanitize and validate inputs.
2. **Use safe template engines —** Choose template engines that automatically escape user input or ensure strict security configurations.
3. **Validate and escape inputs —** Sanitize user input using escaping methods to ensure it is treated as plain text.
4. **Implement allow list validation —** Restrict inputs to known, safe values whenever possible.

## Secure Code Example

```
from flask import Flask, request, render_template_string, escape
app = Flask(__name__)
@app.route("/")
def home():
    user_input = request.args.get("name", "Guest")
    sanitized_input = escape(user_input)  # Escapes malicious input
    template = f"Hello, {sanitized_input}!"
    return render_template_string(template)
if __name__ == "__main__":
    app.run(debug=True)
```
Now, if an attacker tries to inject `{{config.items()}}` , it will be treated as plain text:

`Hello, {{config.items()}}`
## Conclusion

SSTI is a critical vulnerability that can lead to severe consequences if left unchecked. By understanding how it works and adopting secure coding practices, you can safeguard your applications against such attacks. Always validate and sanitize user inputs and use secure template engines to ensure a robust defense against SSTI.
