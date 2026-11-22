# JavaScript Prototype Pollution Attack

- **Source URL:** https://medium.com/@dodir.sec/javascript-prototype-pollution-attack-a-simplified-guide-c3b4ba8a6441?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20260821165726/https://medium.com/@dodir.sec/javascript-prototype-pollution-attack-a-simplified-guide-c3b4ba8a6441
- **Fetched:** 2026-11-22
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/6227 (id 6227)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# JavaScript Prototype Pollution Attack: A Simplified Guide

JavaScript might seem challenging, but understanding its vulnerabilities, such as prototype pollution, is critical for penetration testers. Although prototype pollution might appear complex and uncommon, it can lead to significant security issues. This article aims to simplify the concept of prototype pollution, explaining it in clear terms. We will also provide practical guidance on how to detect, address, and exploit this vulnerability.

## What is an Object in JavaScript?

In JavaScript, an **object** is a collection of pairs that contain keys and their corresponding values. Think of it as a storage box holding items labeled with tags, making it easy to organize and access different pieces of information. Here’s a simple example:

```
const car = { color: "red" };
console.log(car.color); // Outputs: red
```
In this example, the `car` object has a property `color` with the value "red". Accessing this property is pretty straightforward.

## What is a Prototype?

A prototype is essentially a blueprint for creating objects in JavaScript. It allows one object to inherit properties and methods from another, forming a “prototype chain.” This chain enables objects to share behaviors and functionality, reducing redundancy and enhancing code efficiency. Here’s how it works:

```
function Person(name) {
  this.name = name;
}
Person.prototype.sayHello = function() {
  console.log("Hello, my name is " + this.name);
};
```
```
const alice = new Person("Alice");
alice.sayHello(); // Outputs: Hello, my name is Alice
```
In this example, the `Person` constructor function creates a new object with a `name` property. By adding the `sayHello` method to `Person.prototype`, all instances of `Person` can access this method, demonstrating how prototypes facilitate inheritance and code reuse in JavaScript.

## What is Prototype Pollution?

Prototype pollution is a JavaScript vulnerability that enables an attacker to add arbitrary properties to global object prototypes, which may then be inherited by user-defined objects.

Prototype pollution is a bug that is not yet as well documented and it only started being discussed by researchers around 2017 and first vulnerabilities started appearing in early 2018.

### Key Components of Prototype Pollution:

Successful exploitation of prototype pollution requires three key components:

- **A Prototype Pollution Source**: This is any input that enables an attacker to poison prototype objects with arbitrary properties.
- **A Sink**: A JavaScript function or DOM element that enables arbitrary code execution.
- **An Exploitable Gadget**: Any property that is passed into a sink without proper filtering or sanitization.

## Prototype Pollution — Client side

### Detection Methods for Client-Side Prototype Pollution:

Detecting client-side prototype pollution vulnerabilities can be achieved through various tools and techniques. Here are a couple of options:

- **Burp Suite DOM Invader:** Built-in Chromium tool for identifying prototype pollution vulnerabilities. [Burp Suite DOM Invader](https://portswigger.net/burp/documentation/desktop/tools/dom-invader)
- **PPScan Chrome Extension:** Browser extension that scans for prototype pollution. [PPScan](https://github.com/msrkp/PPScan)
- **Manual Detection:** Use specific payloads to test for vulnerabilities. [Client-Side Prototype Pollution Payloads](https://github.com/BlackFan/client-side-prototype-pollution)

### Attack example:

Let’s delve into a client-side example where improper handling of user input enables an attacker to exploit the application using prototype pollution, ultimately leading to an XSS attack.

Consider the following JavaScript code snippet, which dynamically loads a script based on a configuration URL:

```
let transport_url = config.transport_url || defaults.transport_url;
let script = document.createElement('script');
script.src = `${transport_url}/example.js`;
document.body.appendChild(script)
```
In this scenario, `config.transport_url` is expected to be a safe URL from which a script will be loaded. However, if an attacker can manipulate the `config` object via prototype pollution, they can change the `transport_url` to a malicious value.

### Exploitation via URL Injection:

An attacker can exploit this by accessing the vulnerable application with a specially crafted URL:

`https://vulnerable-website.com/?__proto__[transport_url]=data:,alert(1);//`
### Here’s how it works:

1. **Injection:** The URL includes `__proto__[transport_url]=data:,alert(1);//`, which manipulates the `__proto__` property of the global object.
2. **Pollution:** This sets `transport_url` to `data:,alert(1);//` in the prototype chain.
3. **Script Execution:** The vulnerable code then constructs the script URL as `data:,alert(1);//example.js`, leading to the execution of `alert(1)`.

The JavaScript code after the attack would look like this:

```
let transport_url = config.transport_url || defaults.transport_url; // Now `transport_url` is "data:,alert(1);//"
let script = document.createElement('script');
script.src = `${transport_url}/example.js`; // "data:,alert(1);//example.js"
document.body.appendChild(script); // Executes alert(1)
```
**This example was inspired by the following PortSwigger lab:**

## Get dodir’s stories in your inbox

Join Medium for free to get updates from this writer.

## Prototype Pollution — Server side

### Why is Server-Side Prototype Pollution More Difficult to Detect and Why We Should Be Careful?

- **No access to source code:** it’s hard to find vulnerabilities and potential gadget properties in server-side environments.
- **Testing in production can cause unintentional DoS:** exploiting vulnerabilities can be tricky without breaking the site.
- **Pollution of server-side prototypes persists throughout the lifetime of the Node process:** unlike in a browser where changes can be easily reversed.

### Non-Destructive Detection Methods for Server-Side Prototype Pollution:

**Polluted Property Reflection:**

Add properties to the object and observe if they reflect in the server’s response.

```
{
  "__proto__": {
    "foo": "bar"
  }
}
```
**Without polluted property reflection examples:**

**Status code override:** Injecting a new status code to see if the server response status changes, indicating prototype pollution.

```
{
  "__proto__": {
    "status": 555
  }
}
```
**JSON spaces override:** Changing the JSON formatting spaces to detect if the output formatting changes, which signifies successful pollution.

```
{
  "__proto__": {
    "json spaces": 5
  }
}
```
**Charset override:** Altering the content type charset to a non-standard value and checking for changes in the server response, indicating prototype pollution.

```
{
  "__proto__": {
    "content-type": "application/json; charset=utf-7",
    "+AGYAbwBv-": "foo"
  }
}
```
All of these injections create a noticeable change in server behavior without causing damage, providing a consistent method to detect successful exploitation.

### Attack Example:

Prototype pollution can be exploited to escalate privileges, such as by setting an `isAdmin` property to `true`. Here's how an attacker might achieve this:

Consider the following server-side JavaScript code that checks if a user is an admin:

```
function checkAdmin(user) {
    if (user.isAdmin) {
        console.log("User is an admin");
        // Perform admin actions
    } else {
        console.log("User is not an admin");
        // Perform regular user actions
    }
}
```
If the application server takes user input and merges it into the user object without proper validation, it becomes vulnerable to prototype pollution.

### Attack Payload:

An attacker can craft a payload to exploit this vulnerability by adding an `isAdmin` property to the `__proto__` object:

```
{
  "__proto__": {
    "isAdmin": true
  }
}
```
The payload modifies the prototype of the global object, adding the `isAdmin` property. When the server-side code checks the user’s admin status, the polluted prototype causes all user objects to inherit `isAdmin: true`. When the `checkAdmin` function runs, it will see `user.isAdmin` as `true`, granting admin privileges to any user.

**This example was inspired by the following PortSwigger lab:**

## Impact Possibilities of Prototype Pollution

Prototype pollution can have several severe impacts on an application. Here are some potential attack scenarios:

- **Denial of Service (DoS):** When the object prototype holds functions that can be inherited and called for various operations, for example, the `toString()` method, changing that method to a random function such as a simple `console.log()` can cause significant issues. This can result in unexpected behaviors and crashes when the method is called on another object, leading to a Denial of Service (DoS).
- **Privilege Escalation:** An attacker can pollute properties that could alter the state of the environment or change specific items from the codebase, such as cookies or tokens, and other attributes. For example, by setting the `isAdmin` property to `true`, the attacker can gain administrative privileges and access restricted areas or functionalities.
- **Cross-Site Scripting (XSS):** An attacker can use prototype pollution to inject malicious code into the application’s prototype chain. This malicious code can then be executed in the context of other users who access the application, leading to XSS attacks. This can allow attackers to steal sensitive information, hijack user sessions, or deface the website.
- **Remote Code Execution (RCE):** An attacker can leverage prototype pollution to manipulate the server’s execution flow, potentially leading to Remote Code Execution (RCE). By injecting properties that change the behavior of critical functions or introduce malicious code paths, attackers can execute arbitrary code on the server, gaining full control over the application and its environment.

## Mitigation Strategies for Prototype Pollution

- **Perform Validation on JSON Inputs:** Ensure that all JSON inputs are validated against the application’s schema. This helps prevent unexpected properties from being added to objects.
- **Use** **Map**
 **Instead of** **Object:** 
`Map` objects instead of plain `Object` for storing key-value pairs. `Map` does not inherit from `Object.prototype` and is therefore not susceptible to prototype pollution.
- **Freeze Properties with** **Object.freeze:**
`Object.freeze` to make an object immutable. Freezing `Object.prototype` can prevent attackers from modifying the prototype chain.
- **Avoid Using Recursive Merge Functions Unsafely:** Be cautious when using recursive merge functions. Ensure they do not merge input objects with `Object.prototype`. Use safe deep merge libraries or implement safe merge logic.
- **Use Objects Without Prototype Properties:** Create objects without a prototype to avoid affecting the prototype chain. This can be done using `Object.create(null)`.
- **Regularly Update Libraries:** Keep your dependencies and libraries up to date with the latest security patches. Regularly review and update packages to ensure any known vulnerabilities are addressed.

## Conclusion

Prototype pollution is an important vulnerability that penetration testers should be aware of due to its potential impacts like DoS, privilege escalation, XSS, and RCE. Fortunately, testing for prototype pollution is straightforward and can be seamlessly integrated into your testing methodology. By validating JSON inputs, using `Map` instead of `Object`, freezing prototype properties, avoiding unsafe merges, and using prototype-free objects, you can help ensure application security. Regularly updating libraries also helps mitigate risks. Including these checks in your routine assessments can enhance your security testing effectiveness.

**Disclaimer**: This article is for educational purposes only, aimed at enhancing understanding of web security vulnerabilities and their mitigation. The techniques discussed should not be used for unethical or illegal activities. Readers are urged to apply this knowledge responsibly and in compliance with applicable laws and ethical standards. Unauthorized access to computer systems is illegal and contrary to ethical hacking principles. Let’s collaborate to ensure a secure web ecosystem.
