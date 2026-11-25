# WebSockets

- **Source URL:** https://medium.com/@y_shivkumar/websockets-the-hidden-door-behind-real-time-web-apps-f13b1f60aaad
- **Fetched from:** https://medium.com/@y_shivkumar/websockets-the-hidden-door-behind-real-time-web-apps-f13b1f60aaad?source=rss-13de31b67c0b------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14892 (id 14892)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** ShivKumar / Mon, 31 Aug 2026 21:09:11 GMT

Imagine you’re chatting with someone on a website.

You send:

*“Hello!”*

The message appears instantly. No page refresh. No waiting.

Behind the scenes, a **WebSocket** may be keeping a persistent connection between your browser and the server.

That sounds convenient — but whenever a new communication channel appears, new security problems can appear too.

While working through the WebSocket labs on **PortSwigger Web Security Academy**, I came across three interesting attack scenarios that helped me understand where WebSocket security can go wrong.

Imagine Alice is logged into a vulnerable application.

She visits an attacker’s page.

The attacker’s JavaScript creates a WebSocket connection to the application.

If the server relies only on the victim’s browser cookies for authentication and doesn’t properly validate the **Origin**, the server may accept that connection.

The attacker can potentially interact with the WebSocket as Alice.

That’s the basic idea behind **Cross-Site WebSocket Hijacking (CSWSH)**.

Usually because the application:

During an authorized security test, I would:

The important lesson:

**A WebSocket handshake is part of your application’s security boundary.**

Now imagine a chat application.

A user sends:

Hello everyone!

The server broadcasts the message.

But what happens if the application inserts that message directly into an HTML page?

For example, conceptually:

chat.innerHTML = message;

Now the message isn’t necessarily treated as text anymore.

It may become HTML.

That’s where **WebSocket-based XSS** can appear.

The WebSocket itself isn’t necessarily the vulnerability.

The problem is the **unsafe handling of WebSocket data after it reaches the browser**.

Common causes include:

In an authorized lab or application, I would send a harmless test value and observe:

**WebSocket → JavaScript → DOM**

Then determine whether the value is inserted as text or interpreted as HTML.

The key lesson:

*WebSocket messages are still untrusted user input.*

Here’s another interesting situation.

Suppose a WebSocket client sends:

```
{
  "action": "delete",
  "id": "123"
}
```
The server receives it and performs the operation.

But does the server actually verify that the user is allowed to delete object 123?

If it doesn’t, an attacker may be able to modify WebSocket messages and access functionality they shouldn’t have.

This is essentially an **authorization problem over a real-time communication channel**.

Developers sometimes assume:

*“The request came through our WebSocket, so it must be legitimate.”*

But the client is controlled by the user.

Anything sent by the browser can potentially be modified.

I would inspect legitimate WebSocket messages and look for:

Then I would test whether changing those values causes unauthorized behavior.

The server should always enforce authorization independently.

These three labs are only the beginning.

When testing WebSocket applications, I would also consider:

Can an unauthenticated user connect?

Can an expired session continue using an existing connection?

Can one user manipulate another user’s objects simply by changing an identifier?

Does the server blindly accept connections from arbitrary origins?

Are WebSocket messages later used in:

The WebSocket transport doesn’t magically make the data safe.

Can an attacker send huge numbers of messages or extremely large messages?

Does the server have:

Does the WebSocket expose sensitive information such as:

Instead of thinking:

*“What WebSocket payload should I send?”*

I find it more useful to ask:

**1. Where is the connection created?**

**2. How is the user authenticated?**

**3. Does the server validate Origin?**

**4. What messages can the client send?**

**5. Which values can I control?**

**6. Does the server perform authorization?**

**7. Where does the received data go?**

**8. Is that data safely handled?**

**9. Are there limits on connections and messages?**

WebSockets are not inherently insecure.

They’re simply another communication channel.

And just like HTTP requests, WebSocket messages must be treated as **untrusted input**.

The biggest lesson I took from the PortSwigger labs was this:

***Don’t trust the connection. Don’t trust the client. Don’t trust the message.***

Validate authentication.

Validate authorization.

Validate the origin where appropriate.

Validate the data.

And always test what happens when the client stops behaving exactly as the developer expected.
