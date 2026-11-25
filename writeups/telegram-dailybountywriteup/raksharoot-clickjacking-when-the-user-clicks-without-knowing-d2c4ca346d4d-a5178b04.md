# Clickjacking

- **Source URL:** https://medium.com/@raksharoot/clickjacking-when-the-user-clicks-without-knowing-d2c4ca346d4d
- **Fetched from:** https://medium.com/@raksharoot/clickjacking-when-the-user-clicks-without-knowing-d2c4ca346d4d?source=rss-4206d471b207------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14949 (id 14949)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** Raksharoot / Thu, 15 Oct 2026 16:35:15 GMT

Disclaimer: Educational content only. Only test systems you own or have written permission to test. Never use these techniques on real users without explicit authorization.

Clickjacking is one of those bugs that sounds simple until you actually try it.

***The idea is basic:*** put a transparent iframe over a button, get the user to click, and they end up clicking something on the hidden page. Classic UI redressing.

But the modern version of this bug is a lot weirder than the 2010-era tutorials make it sound. There are SVG filter tricks that distort iframes you can’t even read. Double-click timing attacks that land clicks on pages you never framed. Popup-based variants that don’t use iframes at all. And browser extension clickjacking that hijacks autofill dropdowns.

Let me walk through how this actually works today.

A clickjacking attack has three pieces:

***The classic version:*** set the iframe’s opacity to something like 0.1 , position it over a decoy button, and let the user click.

The user sees “*Click me.*” They click. The click lands on the hidden iframe’s submit button. Done.

The trick above only works if the form is already filled out. Otherwise the user clicks a submit button on an empty form and nothing happens.

But a lot of apps support prepopulation via query parameters.

*If ?email=attacker@evil.com* fills the email field, you don’t need the user to type anything. They just click, and the form submits with your value.

That turns a “meh” clickjacking bug into a full account takeover primitive. If the form is a password reset, an email change, or an MFA disable — you own the account.

Always test for parameter prepopulation on framable forms. It’s the difference between a PoC and a payout.

Sometimes the form won’t prepopulate. The user has to type something.

Drag-and-drop solves this.

The attacker page has a draggable element with the payload embedded:

The user drags the element into the framed form’s input field. The text gets written in. No typing required, just a drag and a click.

This works because drag-and-drop is a native browser behavior that crosses iframe boundaries in ways normal input doesn’t. It’s a smaller attack surface, but it’s real.

Here’s a pattern that keeps showing up.

You find a self XSS, an XSS that only fires when the user submits their own input. Normally it’s useless, because you can’t force a victim to type a payload into their own profile.

But if the page with the form is framable and supports parameter prepopulation, you can combine the two:

The form submits. The XSS fires. You now have XSS in the victim’s session.

That’s how a low-severity self-XSS becomes a high-severity account takeover.

Every few years, browsers add a new clickjacking defense. And every few years, someone finds a new way around it.

DoubleClickjacking is the latest example. It doesn’t rely on iframes at all, or at least, not in the traditional way.

***The idea:*** ask the victim to double-click a button. Then use the timing gap between *mousedown* and *click* to swap what’s under the cursor. The first click lands on your button. The second click lands on the target page’s button, because you swapped the pages in between.

This bypasses every frame-busting defense, because the target is never framed. It’s a full-page navigation that happens mid-double-click.

***The catch:*** it only works for actions that require a single click. OAuth permission prompts. One-click confirmations. Approval dialogs.

So it’s not universal, but for OAuth flows it’s devastating.

Some variants skip iframes entirely and use a popup window that tracks the cursor.

The attacker page tracks *mousemove* and moves a small popup window to stay under the cursor. While the popup is same-origin, *moveTo()* works. Once it’s aligned with a target button, the popup navigates back to the target origin, so the next click lands on the real button.

Because cross-origin *moveTo()* is blocked, the popup has to briefly navigate to an attacker origin for repositioning, then use *history.back()* or *location* tricks to return to the target.

It’s fiddly, but it works. And it means clickjacking doesn’t require iframes anymore

If a framable page renders a secret, a reset code, an API token, a session ID, you can distort the pixels until they look like a CAPTCHA. Then you add an input field on your own page that says “type the code you see.”

The user transcribes the victim’s secret into your input. You capture it. Game over.

The *pattern* attribute can even enforce the exact format of the secret, so the user can’t submit anything wrong:

\<input pattern=”⁶c79 ?7261 ?706f ?6e79$” required>

This is genuinely clever. It turns a rendered-secret page into a self-service extraction tool.

Filters can also surgically erase placeholder text, validation hints, or labels, while keeping the user’s keystrokes visible.

The technique uses **feComposite** to amplify brightness, **feTile** to crop to the input field, **feMorphology** to thicken the typed glyphs, and **feColorMatrix** to isolate them. ***The result*:** the victim types their real password into what looks like a normal input field, but they’re actually typing into the hidden iframe.

On top of that, the attacker can overlay their own HTML labels — “Enter your email,” “Enter your password”, so the victim thinks they’re filling out a legitimate form.

This is the part that’s genuinely wild.

By cropping a tiny 2–4 pixel region of the iframe with **feTile** , tiling it to full viewport, and thresholding the color, you can read UI state without JavaScript.

Then you can chain Boolean operations- AND, OR, XOR, NOT entirely inside the SVG filter graph. Which means you can build a state machine that tracks whether a dialog is open, whether a checkbox is checked, whether a success banner appeared.

Each state gates a different overlay bitmap. So you can walk a user through a multi-step workflow — password reset, approval, destructive confirmation, without ever touching the DOM or knowing what’s actually on the page.

This is one of those techniques that’s so far outside the normal mental model of “clickjacking” that most testers never look for it.

Here’s a niche one.

A sandboxed iframe without *allow-popups* normally can’t open dialogs. But a *401* response with a *WWW-Authenticate: Basic* header triggers a browser-native auth prompt, and that prompt isn’t considered a popup by the sandbox.

So you can do this:

The browser shows a login prompt inside a “sandboxed” widget. Users see a modal asking for credentials on a page that doesn’t look like it should be asking. Some will type their real credentials. Password managers may even offer to autofill them.

It’s phishing, but dressed up as a legitimate iframe widget.

This is a newer variant and it’s nasty.

Password managers inject autofill dropdowns near focused inputs. The attacker page focuses a controlled input and overlays or hides the extension’s dropdown. A coerced user click selects a stored credential, and it gets filled into the attacker’s field instead of a legitimate one.

No iframe required. Just DOM and CSS manipulation.

***A real-world example:*** Dashlane disclosed a passkey dialog clickjacking issue in 2025. If the relying party domain had XSS, an attacker could overlay HTML on the extension’s passkey dialog. A click on the attacker’s element would proceed with the legitimate passkey login. The passkey material itself wasn’t exposed, but the login went through, which is enough.

This is the kind of bug that only exists because browser extensions inject UI into pages. It’s a new attack surface, and it’s not well understood yet.

Okay, enough attack stuff. What actually stops this?

Frame-busting scripts like *if (top !== self) top.location = self.location* are the old standby. They’re better than nothing, but they fail more often than people think.

\<iframe src=”https://victim.com" sandbox=”allow-forms allow-scripts”>

That’s it. The frame-busting script is neutralized. The iframe renders, the user can interact with it, and the script can’t do anything about it.

So don’t rely on frame-busting scripts alone.

**X-Frame-Options —** the original header:

*Content-Security-Policy: frame-ancestors ‘self’;*

*Options:*

This is the header you want. *X-Frame-Options* is still useful for old browsers, but frame-ancestors is the future.

Control what your page can frame, not who can frame you. Related but different:

*Content-Security-Policy: frame-src ‘self’ https://trusted-website.com;*

the last line of defense. Even if a clickjacking attack succeeds, a valid CSRF token makes the resulting request fail. But this only works if every state-changing endpoint actually validates the token.

Not exhaustive, but this is the order I go in:

Clickjacking isn’t a single bug. It’s a **category of UI manipulation** that gets reinvented every time browsers add a new feature.

The classic iframe trick still works on a shocking number of sites. The SVG filter tricks are terrifying once you understand them. And the newer variants, double-click timing, popup tracking, extension UI overlay, are still flying under most testers radars.

When you’re testing, don’t just check *X-Frame-Options* and move on. Look for sensitive actions that can be triggered with one click. Look for pages that render secrets. Look for browser-native UI that isn’t protected by the same rules as the page itself.

That’s where the real clickjacking bugs live.

That’s Part 6. Read the whole series in order: [Web Pentesting: A Complete Guide](https://medium.com/@raksharoot/list/web-pentesting-a-complete-guide-ad31d529002a).
