# SSTI Attacks Explained: When {{7*7}} Returns 49, You Have a Problem

- **Source URL:** https://medium.com/@vigneshkumaroffsec/ssti-attacks-explained-when-7-7-returns-49-you-have-a-problem-d8ad37d11123
- **Fetched:** 2026-11-26
- **Channel:** @dailybountywriteup
- **Telegram message:**  (id 14999)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** Vigneshkumaroffsec / Wed, 25 Nov 2026 01:12:53 GMT

*If user input lands inside a server-side template, the template engine may run it as code — and that road often ends in remote code execution. Here’s how SSTI works, how to detect it, and how to fix it. Authorized testing only.*

By Vignesh Kumar | Security Researcher

Here’s a quiet, high-severity bug hiding in a convenience almost every app uses: **templates.** Apps build pages, emails and documents from templates — “Hi {{name}}, welcome back.” The engine (Jinja2, Twig, Freemarker, Velocity, ERB…) fills in the variables. That’s fine *when the template is fixed and the user data is just a value.* It goes very wrong when **user input becomes part of the template itself**, because template engines don’t just substitute — they **evaluate expressions.**

That’s **Server-Side Template Injection (SSTI)**, and because template expressions can reach objects, classes and ultimately the operating system, SSTI frequently escalates to **remote code execution**. This guide covers how it works, how to *detect* it safely, and how to fix it — all for systems **you own or are explicitly authorized to test.**

There’s a critical difference between these two:

\# Safe: user data is passed as a VALUE into a fixed template

render\_template("hello.html", name=user\_input)

# Vulnerable: user data is concatenated INTO the template source

render\_template\_string("Hello " + user\_input)

In the second case, whatever the user types becomes part of the template *code*. If they type template syntax, the engine executes it. name was supposed to be data; now it's logic. And template logic, in most engines, can walk the object graph — from a harmless string, to its class, to built-in functions, to running shell commands.

That’s the whole arc of SSTI: **data crosses into code, and template code can reach the OS.**

The beauty of SSTI detection is that you can prove it with **arithmetic**, no harm done.

**1. Inject a math probe.** Put a simple expression where your input is reflected and see if the server *computes* it:

```
{{7*7}}      → 49    (Jinja2, Twig)
${7*7}       → 49    (Freemarker, some JSP/EL)
#{7*7}       → 49    (Velocity-style, some engines)
<%= 7*7 %>   → 49    (ERB)
```
If the page renders **49** instead of the literal {{7\*7}}, the input is being evaluated server-side. That 49 is your proof — unambiguous, and completely benign.

**2. Confirm it’s server-side, not client-side.** Client-side template frameworks (some front-end libs) also evaluate {{...}}. Confirm the evaluation happens on the *server* (e.g., it shows up in the raw HTML response, before any JS runs), so you're not chasing a client-only quirk.

**3. Fingerprint the engine.** Different engines use different syntax and fail differently. Which probe worked ({{ }} vs ${ } vs #{ }), and how error strings look, tells you whether it's Jinja2, Twig, Freemarker, Velocity, ERB, etc. The engine determines everything about escalation.

**4. Assess impact carefully.** From the 49 proof, SSTI *typically* escalates to RCE via engine-specific object traversal — reaching built-in classes and command execution. For a responsible report, **demonstrate the capability minimally** (e.g., read a benign value or show the engine evaluates a safe built-in) rather than running real system commands or touching data. The {{7\*7}}=49 plus an accurate description of the realistic RCE path is a strong, safe finding — you've proven the sink; you don't need to pop a shell on a live system to make the point.

Anywhere user input might reach a template as code:

If a feature lets users influence the *format* of output, not just the values, test it.

The root cause is always the same — user input became template *code* — so the fix is to keep it as *data*.

SSTI is the result of a small, understandable mistake with an outsized payoff: a developer builds a template string with user input to make personalization easy, and in doing so hands the user a programming language that runs on the server. The tell is almost comically simple — {{7\*7}} comes back as 49 — and the fix is equally simple to state: user input is a *value*, never part of the template. Keep that line and SSTI can't happen.

If you build or test apps that generate anything from templates — pages, emails, reports — do one thing this week: drop {{7\*7}} into every field that ends up in that output. If any of them answer 49, your template just became a shell, and you know exactly which line to change.

I’m Vignesh Kumar, a security researcher working across application security, DevSecOps, cloud security, and vulnerability research.

I share practical findings from security assessments and responsible disclosures to help improve the security of real-world systems.

*The techniques in this article are described for defending and testing systems you own or are authorized to assess.*
