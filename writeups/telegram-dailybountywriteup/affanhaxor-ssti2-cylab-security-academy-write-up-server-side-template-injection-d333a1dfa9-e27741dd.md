# SSTI2 ~ CyLab Security Academy Write-up | Server-Side Template Injection

- **Source URL:** https://medium.com/@affanhaxor/ssti2-cylab-security-academy-write-up-server-side-template-injection-d333a1dfa9aa
- **Fetched from:** https://medium.com/@affanhaxor/ssti2-cylab-security-academy-write-up-server-side-template-injection-d333a1dfa9aa?source=rss-a70f2c751bb6------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:**  (id 14973)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** Affanhaxor / Sat, 07 Nov 2026 04:35:08 GMT

**Author:** Affanhaxor

**Platform:** CyLab Security Academy

**Challenge:** SSTI2

**Category:** Web Security

**Topic:** Server-Side Template Injection (SSTI), Jinja2, Flask

Server-Side Template Injection (SSTI) is a web vulnerability that occurs when user-controlled input is interpreted as part of a server-side template rather than being treated as ordinary text.

Template engines are commonly used in web applications to generate dynamic HTML pages. However, when an application processes user input as a template, an attacker may be able to execute template expressions and potentially access sensitive information.

In this CyLab Security Academy challenge, the website allows users to submit an announcement. By testing how the application processes input, I identified template expression evaluation and used it to investigate the server-side environment and retrieve the challenge flag.

The challenge starts with a simple webpage titled **Home**. It contains a message:

*I built a cool website that lets you announce whatever you want!*

The page provides a text field where users can enter an announcement and submit it using the **Ok** button.

At first glance, this looks like a basic input functionality. However, any user input that is processed by a server-side template engine should be examined carefully during a security assessment.

To check whether the application was evaluating template expressions, I entered the following expression into the announcement field:

`{{7*7}}`
This is a simple mathematical expression commonly used to identify template injection vulnerabilities.

If the application treats the input as ordinary text, the expression should appear exactly as submitted. If the template engine evaluates it, the output should be the result of the calculation.

After submitting the expression, the application displayed:

This confirmed that the server evaluated the expression instead of displaying it as plain text.

This was an important finding because it indicated that user-controlled input was being interpreted by a server-side template engine.

The behavior was consistent with Jinja2, a template engine commonly used with Python Flask applications.

Jinja2 supports expressions enclosed in double curly braces:

`{{ expression }}`
For example:

The template engine evaluates the expression and inserts its result into the rendered page.

The successful mathematical test suggested that the application was processing user input within a template context. This established the possibility of Server-Side Template Injection.

After confirming expression evaluation, I continued testing the template context to understand which application objects and attributes were accessible.

The screenshot shows a Jinja-style expression using the request object and attribute access.

`{{request|attr('application')|attr('\x5f\x5fglobals\x5f\x5f')|attr('\x5f\x5fgetitem\x5f\x5f')('\x5f\x5fbuiltins\x5f\x5f')|attr('\x5f\x5fgetitem\x5f\x5f')('\x5f\x5fimport\x5f\x5f')('os')|attr('popen')('ls')|attr('read')()}}`
In Flask applications, the request object represents the current HTTP request. Template context objects may expose useful application information depending on how the application is configured.

The important security issue is that template expressions should not be allowed to access sensitive application objects through untrusted input.

Further template evaluation revealed information about files present in the application directory.

The output included:

\_\_pycache\_\_

app.py

flag

requirements.txt

This indicated that the template context could be used to access information beyond the intended announcement functionality.

The presence of app.py suggested that the application was implemented using Python. The flag entry was particularly relevant because the challenge required retrieving the flag.

This stage demonstrated how SSTI can potentially expose server-side application information and sensitive resources.

After investigating the template context and available application resources, I reached the final challenge output.

`{{request|attr('application')|attr('\x5f\x5fglobals\x5f\x5f')|attr('\x5f\x5fgetitem\x5f\x5f')('\x5f\x5fbuiltins\x5f\x5f')|attr('\x5f\x5fgetitem\x5f\x5f')('\x5f\x5fimport\x5f\x5f')('os')|attr('popen')('cat flag')|attr('read')()}}`
The application displayed the flag:

The flag confirmed that the challenge had been completed.

The root cause of this challenge was unsafe handling of user input within a server-side template.

A secure application should treat user-provided announcements as data. A vulnerable application may instead insert the input into a template in a way that causes the template engine to interpret it as code.

For example, a dangerous pattern would be dynamically creating a template from user input:

from jinja2 import Template

```
user_input = request.form.get("announcement")
rendered = Template(user_input).render()
```
In this example, the user input becomes the template itself. Expressions such as {{7\*7}} can therefore be evaluated.

The exact implementation of the challenge may differ, but the observed behavior is consistent with this vulnerability.

Depending on the template engine, configuration, and application privileges, SSTI may lead to:

The impact depends on the template engine and the objects or functions available within its execution context.

User-provided content should be treated as data, not as template source code.

Avoid dynamically creating templates from untrusted input.

Keep template files under developer control and pass user input as variables.

return render\_template(

"announcement.html",

announcement=user\_input

)

The template should display the value without interpreting it as a new template.

Avoid exposing sensitive objects, functions, configuration values, or internal application resources to templates unnecessarily.

The web application should run with limited filesystem and operating-system permissions. This reduces the impact of a successful template injection vulnerability.

Use appropriate input handling and output escaping to prevent other injection vulnerabilities. However, escaping alone is not a replacement for avoiding unsafe template construction.

This challenge demonstrated several important concepts:

SSTI2 was a useful challenge for understanding how server-side template engines process user input.

The initial mathematical expression confirmed that the application evaluated user-controlled template syntax. Further investigation revealed application information and eventually led to the challenge flag.

The main lesson is that user input must never be treated as template source code. Proper template design, restricted context access, and least-privilege execution are essential for preventing Server-Side Template Injection.

**LinkedIn:** [https://www.linkedin.com/in/affanhaxor](https://www.linkedin.com/in/affanhaxor)

**Instagram:** [https://instagram.com/affan\_haxor](https://instagram.com/affan_haxor)

*Follow me for more CTF write-ups, web security labs, and AppSec content.*
