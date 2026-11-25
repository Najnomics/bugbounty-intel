# Client-Side Template Injection

- **Source URL:** https://medium.com/@raksharoot/client-side-template-injection-when-the-browser-executes-your-input-597b47534586
- **Fetched from:** https://medium.com/@raksharoot/client-side-template-injection-when-the-browser-executes-your-input-597b47534586?source=rss-4206d471b207------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:**  (id 14951)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** Raksharoot / Sat, 17 Oct 2026 17:06:28 GMT

Disclaimer: Educational content only. Only test systems you own or have written permission to test. Never use these techniques on real users without explicit authorization.

Server-side template injection gets all the attention. SSTI is the flashy one, {{7\*7}} becomes 49, and suddenly you’re running code on the server.

But there’s a whole other class of this bug that lives in the browser.

Client-Side Template Injection (CSTI) is the same idea, just shifted one layer up. Instead of hitting a Python or Ruby backend, you’re hitting a frontend framework — AngularJS, Vue, Alpine.js, Mavo, and getting them to evaluate your input as a template expression.

The impact is usually XSS. Which, depending on the app, is account takeover.

And the wild part? CSTI often slips past XSS filters, because the framework does the parsing, not the browser.

Here’s where most testers go wrong: they see HTML injection and assume it’s CSTI. It’s not.

HTML injection just means your input lands in the page. CSTI means the framework re-parses your input as a template expression and evaluates it.

Those are very different things.

The quick test is the same as SSTI. *Submit something like:*

*{{7\*7}}*

If the page renders 49, the framework is evaluating your expression. If it renders *{{7\*7}}*, it’s just being reflected as text.

But before you even try that, fingerprint the framework. Look for these markers in the page source:

If the app is using a runtime only Vue build, template compilation might not even happen client-side. So a plain reflection into HTML isn’t enough, you need to hit an actual compilation sink.

That’s the thing most people miss. HTML injection ≠ CSTI. You have to confirm the framework is compiling your input as a template.

This one is genuinely clever.

Most apps don’t just escape your input and move on. They escape it, then pass it through an HTML sanitizer like DOMPurify. Two layers of defense.

***But here’s the thing:*** if those two layers run in the wrong order, they can actually enable the bug they’re trying to prevent.

A 2024 Wiki.js advisory showed exactly this. The app escaped the template delimiters first, then handed the result to DOMPurify. The attacker’s payload was:

The *\<xyzabcd>* tag was invalid, so it survived the escaping step. Then DOMPurify ran and, because the tag was invalid, it removed it. Which left the previously protected {{7\*7}} sitting bare in the DOM, ready for Vue to compile.

If the live page renders *49* , you’ve confirmed the bug. Then escalate:

This is a great trick for rich-text editors and Markdown previews. Try unknown tags, unclosed tags, misnested formatting, a newline before the expression. Compare three states:

If those three states differ in a way that exposes a live expression, you’ve found the boundary.

AngularJS was the framework that made CSTI famous.

The *ng-app* directive tells Angular to process its HTML content. Any double-curly-brace expression inside that scope gets evaluated. So if user input lands inside an *ng-app* region, you can run arbitrary JavaScript.

*Basic payloads:*

*Or via a directive:*

AngularJS had an expression sandbox until version 1.6. Before that, you needed a sandbox escape to get code execution. From 1.6 onward, the sandbox was removed, so

*{{constructor.constructor(‘alert(1)’)()}}* just works.

If the app has CSP enabled but Angular is running in *ng-csp* mode, you can still get execution using filters.

PortSwigger’s research shows that *orderBy* plus an event path can turn a constrained expression into code execution:

If the app reflects your input into an existing AngularJS directive rather than plain HTML text, prioritize directive-based payloads — ng-focus , ng-click , filter abuse, over raw mustache expressions.

Vue is trickier than Angular, because of build modes.

The **runtime-only** build doesn’t include the template compiler. So *{{7\*7}}* won’t do anything unless the app is explicitly passing strings through *Vue.compile()* or a full build.

The ***full build*** does include the compiler. That’s the vulnerable case.

There’s a public playground for this: *vue-client-side-template-injectionexample.azu.now.sh*. A working payload looks like:

Vue 3 exposes different helpers in the template scope. Some useful ones:

The exact helper names vary depending on the Vue version and build output. Once you confirm Vue 3 CSTI, enumerate nearby helpers, don’t assume *\_openBlock* is always present.

This one is a chain, not a standalone bug.

Vue 2’s template compiler used to read inherited values of properties like *staticClass* and *staticStyle* when generating render code. If another bug lets you set those properties on *Object.prototype*, later template compilation turns your polluted string into JavaScript execution.

Affected versions: *vue-template-compiler* from 2.0.0 up to (but not including) 3.0.0. Vue 2 has no upstream patch for this, you’d have to move to Vue 3.

To exploit this, you need three things:

And clean up between tests, polluted prototypes break unrelated components and give you misleading results.

Runtime-only Vue builds eliminate this specific sink. They don’t fix the prototype pollution source, though.

Mavo is niche, but it has its own expression parser that isn’t JavaScript. That means payloads that wouldn’t pass a filter looking for classic JS tokens can still fire.

Useful payloads:

The thing about Mavo is that its syntax allows expressions that look nothing like JavaScript. If a WAF is filtering *alert(1)* but not *\[(1,alert)(1)\]*, Mavo becomes a bypass.

If you see *mv-* or *data-mv-* attributes in the page source, it’s worth a probe.

Before throwing payloads at anything, confirm:

Then test with *{{7\*7}}* or *\[7\*7\]* . If it evaluates, escalate. If not, look for directive/event sinks, alternate delimiters, or dynamic template compilation.

CSTI isn’t just “SSTI but in the browser.” It’s a class of bug where the frontend framework becomes the interpreter, and where sanitizer ordering, build modes, and prototype pollution can all turn a harmlesslooking reflection into code execution.

The key insight: **HTML injection is not CSTI.** You have to confirm the framework is actually compiling your input as a template. Once you do, the payloads are just a matter of knowing the version and the sink.

And the sanitizer ordering bug is the one I’d watch for. It’s the kind of thing that turns a “secure” two-layer defense into the exploit itself.

Read the whole series in order: [Web Pentesting: A Complete Guide.](https://medium.com/@raksharoot/list/web-pentesting-a-complete-guide-ad31d529002a)
