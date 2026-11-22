# Prototype Pollution

- **Source URL:** https://medium.com/@mayank_prajapati/prototype-pollution-the-hidden-danger-in-javascript-c8b17002e8da?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20260821165720/https://medium.com/@mayank_prajapati/prototype-pollution-the-hidden-danger-in-javascript-c8b17002e8da
- **Fetched:** 2026-11-22
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/6229 (id 6229)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Prototype Pollution: The Hidden Danger in JavaScript

Prototype Pollution is a type of vulnerability that arises when an attacker can manipulate or inject properties into the prototype of object. In JavaScript, objects inherit properties from their prototype. Object.Prototype is the parent object from which all other objects gets derived. If we add any property to Object.prototype, it would be available automatically to all the objects.

## How prototype pollution vulnerability occurs?🌪️

This vulnerability occurs when user supplied input is not properly handled/sanitized resulting in modifying the properties of an object.Property can be added/overridden using \_\_proto\_\_(the prototype) which pollute the prototype chain.

## Practical example using JavaScript📗

In the above screenshot we have defined an object called ‘user’. It is inheriting all the properties from its parent object Object.Prototype. toString() is property that got assigned to our declared object ‘user’. Lets override this property and pollute the user object.

We have overrided the toString() function and injected our own code into it. Lets try executing it now.

### Code snippet

```
let user = {'name': 'mayank', 'age': 25} 
user.name 
user.name.toString()
user.name.__proto__.toString = ()=>{alert(11111)}
user.name.toString() 
```
## Impact of prototype pollution🏹

- Infinite loops in the code can be introduced by the attacker that would result in heavy consumption of resources.
- Client side prototype pollution can become the cause of DOM XSS while on server side it may also cause RCE.
- It corrupts the behavior of the object that can lead to unexpected sensitive data exposure or bypassing security mechanism implemented.

## Mitigation🔨

- Ensure that the user input doesn’t contain \_\_proto\_\_, constructor, or prototype that affect prototype chain.
- By freezing the Object.prototype can also prevent this vulnerability using Object.freeze(Object.prototype), however it is less likely recommended due to compatibility issue.

You can read more about prototype pollution on portswigger site: [https://portswigger.net/web-security/prototype-pollution](https://portswigger.net/web-security/prototype-pollution)

## Get Mayank Kumar Prajapati’s stories in your inbox

Join Medium for free to get updates from this writer.

Hope you enjoyed reading:)😇
