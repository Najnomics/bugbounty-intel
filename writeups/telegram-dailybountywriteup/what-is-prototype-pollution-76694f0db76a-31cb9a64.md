# What is prototype pollution?

- **Source URL:** https://cyberw1ng.medium.com/what-is-prototype-pollution-76694f0db76a?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20240731002737/https://cyberw1ng.medium.com/what-is-prototype-pollution-76694f0db76a
- **Fetched:** 2026-11-27
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/6465 (id 6465)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# What is prototype pollution?

## Prototype pollution is a JavaScript vulnerability that enables an attacker to add arbitrary properties to global object prototypes, which may then be inherited by user-defined objects | Karthikeyan Nagaraj

# Source:

# How do prototype pollution vulnerabilities arise?

Prototype pollution vulnerabilities typically arise when a JavaScript function recursively merges an object containing user-controllable properties into an existing object, without first sanitizing the keys. This can allow an attacker to inject a property with a key like `__proto__`, along with arbitrary nested properties.

Due to the [special meaning of](https://portswigger.net/web-security/prototype-pollution/javascript-prototypes-and-inheritance#accessing-an-object-s-prototype-using-proto) [\_\_proto\_\_](https://portswigger.net/web-security/prototype-pollution/javascript-prototypes-and-inheritance#accessing-an-object-s-prototype-using-proto)[prototype](https://portswigger.net/web-security/prototype-pollution/javascript-prototypes-and-inheritance#what-is-a-prototype-in-javascript) instead of the target object itself. As a result, the attacker can pollute the prototype with properties containing harmful values, which may subsequently be used by the application in a dangerous way.

It’s possible to pollute any prototype object, but this most commonly occurs with the [built-in global](https://portswigger.net/web-security/prototype-pollution/javascript-prototypes-and-inheritance#the-prototype-chain) [Object.prototype](https://portswigger.net/web-security/prototype-pollution/javascript-prototypes-and-inheritance#the-prototype-chain)

Successful exploitation of prototype pollution requires the following key components:

- [A prototype pollution source](https://portswigger.net/web-security/prototype-pollution#prototype-pollution-sources) — This is any input that enables you to poison prototype objects with arbitrary properties.
- [A sink](https://portswigger.net/web-security/prototype-pollution#prototype-pollution-sinks) — In other words, a JavaScript function or DOM element that enables arbitrary code execution.
- [An exploitable gadget](https://portswigger.net/web-security/prototype-pollution#prototype-pollution-gadgets) — This is any property that is passed into a sink without proper filtering or sanitization.

# Prototype pollution sources

A prototype pollution source is any user-controllable input that enables you to add arbitrary properties to prototype objects. The most common sources are as follows:

- The [URL](https://portswigger.net/web-security/prototype-pollution#prototype-pollution-via-the-url) via either the query or fragment string (hash)
- [JSON-based input](https://portswigger.net/web-security/prototype-pollution#prototype-pollution-via-json-input)
- Web messages

# Prototype pollution via the URL

Consider the following URL, which contains an attacker-constructed query string:

[https://vulnerable-website.com/?\_\_proto\_\_\[evilProperty\]=payload](https://vulnerable-website.com/?__proto__%5BevilProperty%5D=payload)

When breaking the query string down into `key:value` pairs, a URL parser may interpret `__proto__` as an arbitrary string. But let's look at what happens if these keys and values are subsequently merged into an existing object as properties.

You might think that the `__proto__` property, along with its nested `evilProperty`, will just be added to the target object as follows:

```
{
    existingProperty1: 'foo',
    existingProperty2: 'bar',
    __proto__: {
        evilProperty: 'payload'
    }
}
```
However, this isn’t the case. At some point, the recursive merge operation may assign the value of `evilProperty` using a statement equivalent to the following:

`targetObject.__proto__.evilProperty = 'payload';`

During this assignment, the JavaScript engine treats `__proto__` as a getter for the prototype. As a result, `evilProperty` is assigned to the returned prototype object rather than the target object itself. Assuming that the target object uses the default `Object.prototype`, all objects in the JavaScript runtime will now inherit `evilProperty`, unless they already have a property of their own with a matching key.

In practice, injecting a property called `evilProperty` is unlikely to have any effect. However, an attacker can use the same technique to pollute the prototype with properties that are used by the application, or any imported libraries.

# Prototype pollution via JSON input

User-controllable objects are often derived from a JSON string using the `JSON.parse()` method. Interestingly, `JSON.parse()` also treats any key in the JSON object as an arbitrary string, including things like `__proto__`. This provides another potential vector for prototype pollution.

Let’s say an attacker injects the following malicious JSON, for example, via a web message:

```
{
    "__proto__": {
        "evilProperty": "payload"
    }
}
```
If this is converted into a JavaScript object via the `JSON.parse()` method, the resulting object will in fact have a property with the key `__proto__`:

```
const objectLiteral = {__proto__: {evilProperty: 'payload'}};
const objectFromJson = JSON.parse('{"__proto__": {"evilProperty": "payload"}}');
objectLiteral.hasOwnProperty('__proto__');     // false
objectFromJson.hasOwnProperty('__proto__');    // true
```
If the object created via `JSON.parse()` is subsequently merged into an existing object without proper key sanitization, this will also lead to prototype pollution during the assignment, as we saw in the previous [URL-based example](https://portswigger.net/web-security/prototype-pollution#prototype-pollution-via-the-url).

# Prototype pollution sinks

A prototype pollution sink is essentially just a JavaScript function or DOM element that you’re able to access via prototype pollution, which enables you to execute arbitrary JavaScript or system commands. We’ve covered some client-side sinks extensively in our topic on [DOM XSS](https://portswigger.net/web-security/cross-site-scripting/dom-based).

As prototype pollution lets you control properties that would otherwise be inaccessible, this potentially enables you to reach a number of additional sinks within the target application. Developers who are unfamiliar with prototype pollution may wrongly assume that these properties are not user controllable, which means there may only be minimal filtering or sanitization in place.

# Prototype pollution gadgets

A gadget provides a means of turning the prototype pollution vulnerability into an actual exploit. This is any property that is:

- Used by the application in an unsafe way, such as passing it to a sink without proper filtering or sanitization.
- Attacker-controllable via prototype pollution. In other words, the object must be able to inherit a malicious version of the property added to the prototype by an attacker.

A property cannot be a gadget if it is defined directly on the object itself. In this case, the object’s own version of the property takes precedence over any malicious version you’re able to add to the prototype. [Robust websites](https://portswigger.net/web-security/prototype-pollution/preventing#preventing-an-object-from-inheriting-properties) may also explicitly set the prototype of the object to `null`, which ensures that it doesn't inherit any properties at all.

A YouTube Channel for Cybersecurity Lab’s Poc and Write-ups

Telegram Channel for Free Ethical Hacking Dumps

Thank you for Reading!

Happy Ethical Hacking \~

`Author: Karthikeyan Nagaraj ~ Cyberw1ng`
